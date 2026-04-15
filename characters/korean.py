#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

import yaml


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


def load_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("Malformed YAML frontmatter")

    yaml_text = parts[1]
    body = parts[2]
    data = yaml.safe_load(yaml_text) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML frontmatter is not a mapping")
    return data, body


def dump_frontmatter(data: dict[str, Any], body: str) -> str:
    yaml_text = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )
    return f"---\n{yaml_text}---\n{body}"


def extract_filename_char(path: Path) -> str | None:
    m = FILENAME_RE.match(path.name)
    if not m:
        return None
    return m.group("char")


def is_target_markdown(path: Path) -> bool:
    return path.is_file() and bool(FILENAME_RE.match(path.name))


def korean_native_is_filled(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def normalize_aliases(value: Any) -> list[str]:
    if isinstance(value, list):
        return [x.strip() for x in value if isinstance(x, str) and x.strip()]
    return []


def build_query_candidates(path: Path, data: dict[str, Any]) -> list[str]:
    queries: list[str] = []

    primary = extract_filename_char(path)
    if primary:
        queries.append(primary)

    aliases = normalize_aliases(data.get("aliases"))
    for alias in aliases:
        if alias not in queries:
            queries.append(alias)

    return queries


def prompt_choice(prompt: str, valid: set[str], default: str | None = None) -> str:
    while True:
        raw = input(prompt).strip().lower()
        if raw == "" and default is not None:
            return default
        if raw in valid:
            return raw
        print(f"Please enter one of: {', '.join(sorted(valid))}")


def prompt_yes_no_skip_quit(
    header_lines: Iterable[str],
    allow_all: bool = False,
    default: str = "n",
) -> str:
    print()
    print("=" * 70)
    for line in header_lines:
        print(line)
    print("=" * 70)

    valid = {"y", "n", "q"}
    suffix = "[y/N/q]"
    if allow_all:
        valid.add("a")
        suffix = "[y/N/q/a]"

    return prompt_choice(f"Choose {suffix}: ", valid=valid, default=default)


def find_markdown_files(root: Path) -> list[Path]:
    files = [p for p in root.rglob("*.md") if is_target_markdown(p)]
    files.sort()
    return files


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
                raise ValueError(
                    f"Could not parse review file {review_path} line {line_no}: {e}"
                ) from e
    return entries


def append_review_entry(review_path: Path, entry: ReviewEntry) -> None:
    with review_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")


def already_in_review(review_entries: list[ReviewEntry], file_path: Path) -> bool:
    target = str(file_path)
    return any(entry.file == target for entry in review_entries)


def read_markdown_data(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    return load_frontmatter(text)


def write_markdown_data(path: Path, data: dict[str, Any], body: str) -> None:
    text = dump_frontmatter(data, body)
    path.write_text(text, encoding="utf-8")


def should_skip_for_collect(path: Path, data: dict[str, Any]) -> tuple[bool, str]:
    if korean_native_is_filled(data.get("korean_native")):
        return True, "korean_native already filled"
    if not build_query_candidates(path, data):
        return True, "no query candidates"
    return False, ""


def should_skip_for_apply(path: Path, data: dict[str, Any], entry: ReviewEntry) -> tuple[bool, str]:
    if korean_native_is_filled(data.get("korean_native")):
        return True, "korean_native already filled now"
    if not entry.new_korean_native.strip():
        return True, "review entry has empty new_korean_native"
    return False, ""


# ----------------------------------------------------------------------
# Scraping hook
# ----------------------------------------------------------------------
def fetch_korean_native_from_naver(query_char: str, expected_korean: str | None) -> str | None:
    """
    Replace this stub with your real Naver logic.

    Contract:
    - Input: a single hanja query character and optionally the expected 음 (e.g. '삽')
    - Output: the 훈/native Korean string only (e.g. '껄끄러울'), or None if not found

    Suggested implementation options:
    1. Direct JSON endpoint discovered in browser DevTools
    2. Browser automation with Playwright
    3. Manual lookup fallback during development

    For now, this function prompts the user manually so the rest of the
    two-phase agent is fully usable immediately.
    """
    print()
    print(f"Query character: {query_char}")
    if expected_korean:
        print(f"Expected korean 음: {expected_korean}")
    value = input("Enter scraped korean_native value manually, or leave blank if not found: ").strip()
    return value or None


def collect_phase(root: Path, review_path: Path, delay_seconds: float) -> int:
    existing_entries = load_review_entries(review_path)
    files = find_markdown_files(root)

    added = 0
    accept_all = False

    for path in files:
        if already_in_review(existing_entries, path):
            print(f"SKIP {path}: already present in review file")
            continue

        try:
            data, _body = read_markdown_data(path)
        except Exception as e:
            print(f"ERROR {path}: {e}")
            continue

        skip, reason = should_skip_for_collect(path, data)
        if skip:
            print(f"SKIP {path}: {reason}")
            continue

        queries = build_query_candidates(path, data)
        korean = data.get("korean")
        aliases = normalize_aliases(data.get("aliases"))
        old_native = data.get("korean_native")

        found_entry: ReviewEntry | None = None

        for query in queries:
            new_native = fetch_korean_native_from_naver(query, korean)
            if not new_native:
                print(f"NOT FOUND for {path} using query {query}")
                time.sleep(delay_seconds)
                continue

            lines = [
                f"File:              {path}",
                f"Query used:        {query}",
                f"korean:            {korean or ''}",
                f"old korean_native: {old_native or ''}",
                f"new korean_native: {new_native}",
                f"aliases:           {aliases}",
                "Add this to review file?",
            ]

            if accept_all:
                choice = "y"
            else:
                choice = prompt_yes_no_skip_quit(lines, allow_all=True, default="n")

            if choice == "q":
                print("Stopped by user.")
                return added
            if choice == "a":
                accept_all = True
                choice = "y"

            if choice == "y":
                found_entry = ReviewEntry(
                    file=str(path),
                    query_used=query,
                    korean=korean if isinstance(korean, str) else None,
                    old_korean_native=old_native if isinstance(old_native, str) else None,
                    new_korean_native=new_native,
                    aliases=aliases,
                )
                append_review_entry(review_path, found_entry)
                existing_entries.append(found_entry)
                added += 1
                print(f"ADDED review entry for {path}")
                break

            print(f"SKIPPED candidate for {path} using query {query}")
            # if user said no, continue to next query candidate
            time.sleep(delay_seconds)

        if found_entry is None:
            print(f"NO REVIEW ENTRY for {path}")

        time.sleep(delay_seconds)

    return added


def apply_phase(review_path: Path, delay_seconds: float) -> int:
    entries = load_review_entries(review_path)
    if not entries:
        print(f"No entries found in {review_path}")
        return 0

    changed = 0
    accept_all = False

    for entry in entries:
        path = Path(entry.file)

        if not path.exists():
            print(f"SKIP {path}: file no longer exists")
            continue

        try:
            data, body = read_markdown_data(path)
        except Exception as e:
            print(f"ERROR {path}: {e}")
            continue

        skip, reason = should_skip_for_apply(path, data, entry)
        if skip:
            print(f"SKIP {path}: {reason}")
            continue

        lines = [
            f"File:              {path}",
            f"Query used:        {entry.query_used}",
            f"korean:            {entry.korean or ''}",
            f"old korean_native: {entry.old_korean_native or ''}",
            f"new korean_native: {entry.new_korean_native}",
            "Write this value into the markdown file?",
        ]

        if accept_all:
            choice = "y"
        else:
            choice = prompt_yes_no_skip_quit(lines, allow_all=True, default="n")

        if choice == "q":
            print("Stopped by user.")
            return changed
        if choice == "a":
            accept_all = True
            choice = "y"

        if choice != "y":
            print(f"SKIP {path}: not applied")
            time.sleep(delay_seconds)
            continue

        data["korean_native"] = entry.new_korean_native
        try:
            write_markdown_data(path, data, body)
            changed += 1
            print(f"UPDATED {path}")
        except Exception as e:
            print(f"ERROR writing {path}: {e}")

        time.sleep(delay_seconds)

    return changed


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Two-phase agent for collecting and applying korean_native values in Obsidian markdown files."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    p_collect = subparsers.add_parser(
        "collect",
        help="Scan markdown files and build the review file.",
    )
    p_collect.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Root directory to scan. Default: current directory.",
    )
    p_collect.add_argument(
        "--review-file",
        type=Path,
        default=Path(DEFAULT_REVIEW_FILE),
        help=f"Review file path. Default: {DEFAULT_REVIEW_FILE}",
    )
    p_collect.add_argument(
        "--delay",
        type=float,
        default=1.5,
        help="Delay in seconds between lookups. Default: 1.5",
    )

    p_apply = subparsers.add_parser(
        "apply",
        help="Read the review file and apply approved values into markdown files.",
    )
    p_apply.add_argument(
        "--review-file",
        type=Path,
        default=Path(DEFAULT_REVIEW_FILE),
        help=f"Review file path. Default: {DEFAULT_REVIEW_FILE}",
    )
    p_apply.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay in seconds between writes. Default: 0.5",
    )

    return parser


def main() -> int:
    parser = build_argparser()
    args = parser.parse_args()

    if args.command == "collect":
        added = collect_phase(
            root=args.root,
            review_path=args.review_file,
            delay_seconds=args.delay,
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

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main())

