#!/usr/bin/env python3

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert quoted integer YAML values to unquoted integers for a chosen property."
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Actually write changes to files. Default is dry-run.",
    )
    return parser.parse_args()


def find_front_matter_bounds(text: str) -> tuple[int, int] | None:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None

    pos = len(lines[0])
    for line in lines[1:]:
        if line.strip() == "---":
            return (0, pos + len(line))
        pos += len(line)

    return None


def fix_numeric_property_in_front_matter(front_matter: str, prop: str) -> tuple[str, list[str]]:
    lines = front_matter.splitlines(keepends=True)
    changes: list[str] = []

    pattern = re.compile(
        rf'^({re.escape(prop)}:\s*)"([0-9]+)"(\s*(?:#.*)?)(\r?\n?)$'
    )

    for i, line in enumerate(lines):
        m = pattern.match(line)
        if not m:
            continue

        new_line = f"{m.group(1)}{m.group(2)}{m.group(3)}{m.group(4)}"
        if new_line != line:
            lines[i] = new_line
            changes.append(f"{line.rstrip()}  ->  {new_line.rstrip()}")

    return "".join(lines), changes


def process_file(path: Path, prop: str, commit: bool) -> bool:
    original_text = path.read_text(encoding="utf-8")
    bounds = find_front_matter_bounds(original_text)
    if bounds is None:
        return False

    start, end = bounds
    front_matter = original_text[start:end]
    new_front_matter, changes = fix_numeric_property_in_front_matter(front_matter, prop)

    if not changes:
        return False

    new_text = original_text[:start] + new_front_matter + original_text[end:]

    print(f"\n=== {path.name} ===")
    for change in changes:
        print(change)

    diff = difflib.unified_diff(
        original_text.splitlines(),
        new_text.splitlines(),
        fromfile=f"{path.name} (before)",
        tofile=f"{path.name} (after)",
        lineterm="",
    )
    print("\n".join(diff))

    if commit:
        path.write_text(new_text, encoding="utf-8")
        print("[written]")
    else:
        print("[dry-run only, not written]")

    return True


def main() -> int:
    args = parse_args()

    prop = input("Property name: ").strip()
    if not prop:
        print("No property name provided.", file=sys.stderr)
        return 1

    md_files = sorted(Path(".").glob("*.md"))
    if not md_files:
        print("No *.md files found in the current directory.")
        return 0

    changed_count = 0
    for path in md_files:
        try:
            if process_file(path, prop, args.commit):
                changed_count += 1
        except Exception as exc:
            print(f"\n=== {path.name} ===")
            print(f"Error: {exc}", file=sys.stderr)

    print()
    if args.commit:
        print(f"Done. Updated {changed_count} file(s).")
    else:
        print(f"Done. Would update {changed_count} file(s). Run with --commit to apply changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
