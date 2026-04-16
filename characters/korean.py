#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
from urllib.parse import quote

from playwright.sync_api import sync_playwright

FILENAME_RE = re.compile(r"^(?P<char>.+?)(?: \(char\))?\.md$")
DEFAULT_REVIEW_FILE = "korean_native_review.jsonl"


@dataclass
class ReviewEntry:
    file: str
    query_used: str
    korean: str | None
    old_korean_native: str | None
    new_korean_native: str
    aliases: list[str]
    source: str = "naver_hanja"


def is_target_markdown(path: Path) -> bool:
    return path.is_file() and bool(FILENAME_RE.match(path.name))


def extract_filename_char(path: Path) -> str | None:
    m = FILENAME_RE.match(path.name)
    if not m:
        return None
    return m.group("char")


def korean_native_is_filled(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def yaml_quote(s: str) -> str:
    escaped = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_scalar(value: str) -> Any:
    v = value.strip()
    if v == '""':
        return ""
    if v == "''":
        return ""
    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
        return v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        try:
            return int(v)
        except ValueError:
            return v
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    return v


def load_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")

    end_marker = "\n---\n"
    end_idx = text.find(end_marker, 4)
    if end_idx == -1:
        raise ValueError("Could not find end of YAML frontmatter")

    yaml_text = text[4:end_idx]
    body = text[end_idx + len(end_marker):]

    lines = yaml_text.splitlines()
    data: dict[str, Any] = {}
    i = 0

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        if line.startswith(" ") or line.startswith("\t"):
            raise ValueError(f"Unexpected indentation in YAML frontmatter: {line!r}")

        if ":" not in line:
            raise ValueError(f"Malformed YAML line: {line!r}")

        key, rest = line.split(":", 1)
        key = key.strip()
        rest = rest.rstrip()

        if rest.strip() == "":
            items: list[Any] = []
            i += 1
            while i < len(lines):
                sub = lines[i]
                if not sub.strip():
                    i += 1
                    continue
                if not (sub.startswith("  - ") or sub.startswith("\t- ")):
                    break
                item = sub[sub.index("-") + 1 :].strip()
                items.append(parse_scalar(item))
                i += 1
            data[key] = items
            continue

        data[key] = parse_scalar(rest.strip())
        i += 1

    return data, body


def dump_frontmatter(data: dict[str, Any], body: str) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                if isinstance(item, str):
                    lines.append(f"  - {item}")
                else:
                    lines.append(f"  - {item}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, int):
            lines.append(f"{key}: {value}")
        elif isinstance(value, str):
            if value == "":
                lines.append(f'{key}: ""')
            elif re.fullmatch(r"[A-Za-z0-9_./+-]+", value):
                lines.append(f"{key}: {value}")
            else:
                lines.append(f"{key}: {yaml_quote(value)}")
        elif value is None:
            lines.append(f'{key}: ""')
        else:
            lines.append(f"{key}: {yaml_quote(str(value))}")
    lines.append("---")
    return "\n".join(lines) + "\n" + body


def normalize_aliases(value: Any) -> list[str]:
    if isinstance(value, list):
        out = []
        for x in value:
            if isinstance(x, str) and x.strip():
                out.append(x.strip())
        return out
    return []


def build_query_candidates(path: Path, data: dict[str, Any]) -> list[str]:
    queries: list[str] = []

    ch = extract_filename_char(path)
    if ch:
        queries.append(ch)

    aliases = normalize_aliases(data.get("aliases"))
    for alias in aliases:
        if alias not in queries:
            queries.append(alias)

    return queries


def find_markdown_files(root: Path) -> list[Path]:
    files = [p for p in root.rglob("*.md") if is_target_markdown(p)]
    files.sort()
    return files


def read_markdown_data(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    return load_frontmatter(text)


def write_markdown_data(path: Path, data: dict[str, Any], body: str) -> None:
    path.write_text(dump_frontmatter(data, body), encoding="utf-8")


def load_review_entries(review_path: Path) -> list[ReviewEntry]:
    entries: list[ReviewEntry] = []
    if not review_path.exists():
        return entries

    with review_path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw:
                continue
            try:
                obj = json.loads(raw)
                entries.append(ReviewEntry(**obj))
            except Exception as e:
                raise ValueError(f"Invalid review file line {line_no}: {e}") from e
    return entries


def append_review_entry(review_path: Path, entry: ReviewEntry) -> None:
    with review_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")


def already_in_review(existing: list[ReviewEntry], file_path: Path) -> bool:
    target = str(file_path)
    return any(entry.file == target for entry in existing)


def fetch_hanja_entry_from_naver(page, query_char: str) -> dict[str, str] | None:
    url = f"https://hanja.dict.naver.com/#/search?query={quote(query_char)}&range=all"
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(3500)

    text = page.locator("body").inner_text()

    patterns = [
        re.compile(rf"음·한자\s+\d+\s+{re.escape(query_char)}\s+([가-힣]+)\s+([가-힣]+)", re.MULTILINE),
        re.compile(rf"{re.escape(query_char)}\s+([가-힣]+)\s+([가-힣]+)")
    ]

    for pattern in patterns:
        m = pattern.search(text)
        if m:
            return {
                "query": query_char,
                "korean_native": m.group(1).strip(),
                "korean": m.group(2).strip(),
            }

    return None


def collect_phase(
    root: Path,
    review_path: Path,
    delay_seconds: float,
    headless: bool,
) -> int:
    existing_entries = load_review_entries(review_path)
    files = find_markdown_files(root)
    added = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()

        try:
            for idx, path in enumerate(files, start=1):
                try:
                    if already_in_review(existing_entries, path):
                        print(f"[{idx}/{len(files)}] SKIP {path}: already in review file")
                        continue

                    data, _body = read_markdown_data(path)

                    if korean_native_is_filled(data.get("korean_native")):
                        print(f"[{idx}/{len(files)}] SKIP {path}: korean_native already filled")
                        continue

                    queries = build_query_candidates(path, data)
                    if not queries:
                        print(f"[{idx}/{len(files)}] SKIP {path}: no query candidates")
                        continue

                    yaml_korean = data.get("korean")
                    yaml_korean = yaml_korean.strip() if isinstance(yaml_korean, str) else None
                    aliases = normalize_aliases(data.get("aliases"))
                    old_native = data.get("korean_native")
                    old_native = old_native if isinstance(old_native, str) else None

                    matched: ReviewEntry | None = None

                    for query in queries:
                        try:
                            result = fetch_hanja_entry_from_naver(page, query)
                        except Exception as e:
                            print(f"[{idx}/{len(files)}] ERROR {path}: query {query}: {e}")
                            result = None

                        if not result:
                            print(f"[{idx}/{len(files)}] MISS {path}: query {query}")
                            time.sleep(delay_seconds)
                            continue

                        scraped_korean = result["korean"]
                        scraped_native = result["korean_native"]

                        if yaml_korean and scraped_korean != yaml_korean:
                            print(
                                f"[{idx}/{len(files)}] REJECT {path}: query {query} "
                                f"gave korean={scraped_korean}, expected={yaml_korean}"
                            )
                            time.sleep(delay_seconds)
                            continue

                        matched = ReviewEntry(
                            file=str(path),
                            query_used=query,
                            korean=yaml_korean,
                            old_korean_native=old_native,
                            new_korean_native=scraped_native,
                            aliases=aliases,
                        )
                        append_review_entry(review_path, matched)
                        existing_entries.append(matched)
                        added += 1
                        print(
                            f"[{idx}/{len(files)}] ADD {path}: "
                            f"query={query} korean={scraped_korean} native={scraped_native}"
                        )
                        break

                    if matched is None:
                        print(f"[{idx}/{len(files)}] NO MATCH {path}")

                    time.sleep(delay_seconds)

                except Exception as e:
                    print(f"[{idx}/{len(files)}] ERROR {path}: {e}")
                    time.sleep(delay_seconds)

        finally:
            browser.close()

    return added


def prompt_choice(prompt: str, valid: set[str], default: str | None = None) -> str:
    while True:
        raw = input(prompt).strip().lower()
        if raw == "" and default is not None:
            return default
        if raw in valid:
            return raw
        print(f"Please enter one of: {', '.join(sorted(valid))}")


def apply_phase(review_path: Path, delay_seconds: float) -> int:
    entries = load_review_entries(review_path)
    if not entries:
        print(f"No entries found in {review_path}")
        return 0

    changed = 0
    accept_all = False

    for idx, entry in enumerate(entries, start=1):
        path = Path(entry.file)

        if not path.exists():
            print(f"[{idx}/{len(entries)}] SKIP {path}: file missing")
            continue

        try:
            data, body = read_markdown_data(path)
        except Exception as e:
            print(f"[{idx}/{len(entries)}] ERROR {path}: {e}")
            continue

        if korean_native_is_filled(data.get("korean_native")):
            print(f"[{idx}/{len(entries)}] SKIP {path}: korean_native already filled")
            continue

        print()
        print("=" * 70)
        print(f"[{idx}/{len(entries)}] File:              {path}")
        print(f"Query used:        {entry.query_used}")
        print(f"korean:            {entry.korean or ''}")
        print(f"old korean_native: {entry.old_korean_native or ''}")
        print(f"new korean_native: {entry.new_korean_native}")
        print("=" * 70)

        if accept_all:
            choice = "y"
        else:
            choice = prompt_choice("Apply? [y/N/q/a]: ", {"y", "n", "q", "a"}, default="n")

        if choice == "q":
            print("Stopped by user.")
            return changed
        if choice == "a":
            accept_all = True
            choice = "y"

        if choice != "y":
            print(f"[{idx}/{len(entries)}] SKIP {path}: not applied")
            time.sleep(delay_seconds)
            continue

        data["korean_native"] = entry.new_korean_native

        try:
            write_markdown_data(path, data, body)
            changed += 1
            print(f"[{idx}/{len(entries)}] UPDATED {path}")
        except Exception as e:
            print(f"[{idx}/{len(entries)}] ERROR writing {path}: {e}")

        time.sleep(delay_seconds)

    return changed


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Two-phase Naver hanja collector/apply tool for Obsidian character markdown files."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_collect = subparsers.add_parser("collect", help="Collect candidate korean_native values into a review file.")
    p_collect.add_argument("--root", type=Path, default=Path("."), help="Root directory to scan. Default: current directory.")
    p_collect.add_argument("--review-file", type=Path, default=Path(DEFAULT_REVIEW_FILE), help="Review file path.")
    p_collect.add_argument("--delay", type=float, default=4.0, help="Delay in seconds between requests. Default: 4.0")
    p_collect.add_argument("--show-browser", action="store_true", help="Show browser window while collecting.")

    p_apply = subparsers.add_parser("apply", help="Prompt and apply review file values into markdown files.")
    p_apply.add_argument("--review-file", type=Path, default=Path(DEFAULT_REVIEW_FILE), help="Review file path.")
    p_apply.add_argument("--delay", type=float, default=0.5, help="Delay in seconds between writes. Default: 0.5")

    return parser


def main() -> int:
    parser = build_argparser()
    args = parser.parse_args()

    if args.command == "collect":
        added = collect_phase(
            root=args.root,
            review_path=args.review_file,
            delay_seconds=args.delay,
            headless=not args.show_browser,
        )
        print(f"\nDone. Added {added} review entr{'y' if added == 1 else 'ies'}.")
        return 0

    if args.command == "apply":
        changed = apply_phase(
            review_path=args.review_file,
            delay_seconds=args.delay,
        )
        print(f"\nDone. Applied {changed} change{'s' if changed != 1 else ''}.")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())

