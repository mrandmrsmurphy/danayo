#!/usr/bin/env python3
"""
Fix a YAML front matter property in all *.md files in the current directory.

Behavior:
1) Prompts the user for a property name (unless supplied as a positional argument).
2) Opens each *.md file in the current directory.
3) Checks YAML front matter for the property.
4) If it exists and is already a quoted scalar, leaves it alone.
5) If it exists and is an unquoted inline scalar, converts it to a quoted scalar.
6) If it exists and is a single-item YAML list, converts it to a quoted scalar.
7) Default behavior is dry-run: show changes on screen only.
   Use --commit to actually write changes.

Examples of fixes:
    grade_level: 名
becomes
    grade_level: "名"

    grade_level:
      - 先進
becomes
    grade_level: "先進"
"""

from __future__ import annotations

import argparse
import difflib
import glob
import re
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fix a YAML front matter property in Markdown files."
    )
    parser.add_argument(
        "property_name",
        nargs="?",
        help="YAML property name to inspect/fix. If omitted, you will be prompted.",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Actually write changes to files. Default is dry-run.",
    )
    return parser.parse_args()


def find_front_matter_bounds(text: str) -> tuple[int, int] | None:
    """
    Return (start_index, end_index) of the YAML front matter block, including
    the opening and closing --- lines, or None if no valid front matter exists.
    """
    if not text.startswith("---"):
        return None

    lines = text.splitlines(keepends=True)
    if not lines:
        return None

    if lines[0].strip() != "---":
        return None

    offset = len(lines[0])
    for line in lines[1:]:
        if line.strip() == "---":
            return (0, offset + len(line))
        offset += len(line)

    return None


def quote_yaml_scalar(value: str) -> str:
    """
    Return a safe double-quoted YAML scalar.
    """
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def strip_inline_comment(value: str) -> tuple[str, str]:
    """
    Split an inline YAML scalar into (main_value, inline_comment).

    This is intentionally simple:
    - If there is ' #' somewhere, everything from that hash onward is treated
      as an inline comment.
    - If the value starts quoted, we leave it as-is and do not try to split.
    """
    stripped = value.lstrip()
    if stripped.startswith('"') or stripped.startswith("'"):
        return value.rstrip(), ""

    match = re.search(r"\s+#", value)
    if match:
        idx = match.start()
        return value[:idx].rstrip(), value[idx:]
    return value.rstrip(), ""


def is_already_quoted_scalar(value: str) -> bool:
    v = value.strip()
    return (
        (len(v) >= 2 and v.startswith('"') and v.endswith('"'))
        or (len(v) >= 2 and v.startswith("'") and v.endswith("'"))
    )


def fix_property_in_front_matter(front_matter_text: str, prop: str) -> tuple[str, list[str]]:
    """
    Return (new_front_matter_text, change_descriptions).

    Only modifies the first matching top-level occurrence of the property.
    """
    lines = front_matter_text.splitlines(keepends=True)
    changes: list[str] = []

    prop_pattern = re.compile(rf"^({re.escape(prop)}):([ \t]*)(.*?)(\r?\n?)$")

    i = 0
    while i < len(lines):
        line = lines[i]
        m = prop_pattern.match(line)
        if not m:
            i += 1
            continue

        key = m.group(1)
        spacing_after_colon = m.group(2)
        value_part = m.group(3)
        line_ending = m.group(4)

        original_block_start = i

        # Case 1: Inline value on same line
        if value_part.strip():
            value_main, comment = strip_inline_comment(value_part)

            # Already quoted scalar: do nothing
            if is_already_quoted_scalar(value_main):
                return front_matter_text, changes

            # Ignore obvious complex YAML values
            complex_starts = ("[", "{", "|", ">", "!", "&", "*")
            if value_main.strip().startswith(complex_starts):
                return front_matter_text, changes

            fixed_value = quote_yaml_scalar(value_main.strip())
            new_line = f"{key}:{spacing_after_colon}{fixed_value}{comment}{line_ending}"
            if new_line != line:
                lines[i] = new_line
                changes.append(
                    f'Inline scalar fixed: {key}: {value_main.strip()} -> {key}: {fixed_value}'
                )
            return "".join(lines), changes

        # Case 2: Property with nested block, possibly a single-item list
        # Example:
        # grade_level:
        #   - 先進
        j = i + 1
        child_lines: list[str] = []

        while j < len(lines):
            next_line = lines[j]

            # blank lines belong to child block
            if next_line.strip() == "":
                child_lines.append(next_line)
                j += 1
                continue

            # top-level key starts when line begins at column 0 and looks like a key
            if re.match(r"^[^\s][^:]*:", next_line):
                break

            child_lines.append(next_line)
            j += 1

        nonblank_children = [ln for ln in child_lines if ln.strip()]

        # Only fix a single-item list block
        if len(nonblank_children) == 1:
            child = nonblank_children[0]
            lm = re.match(r"^[ \t]+-[ \t]+(.+?)(\r?\n?)$", child)
            if lm:
                item_value_raw = lm.group(1).rstrip()
                item_value, comment = strip_inline_comment(item_value_raw)

                if not is_already_quoted_scalar(item_value):
                    fixed_value = quote_yaml_scalar(item_value.strip())
                else:
                    # If the list item is already quoted, normalize to a scalar using that content
                    fixed_value = quote_yaml_scalar(item_value.strip().strip("'\""))

                # Preserve the newline style from the original property line if possible
                new_line = f"{key}:{spacing_after_colon}{fixed_value}{comment}{line_ending or 
lm.group(2)}"

                original_block = "".join(lines[original_block_start:j])
                lines[original_block_start:j] = [new_line]
                changes.append(
                    f'Single-item list fixed: {key}: [ {item_value.strip()} ] -> {key}: {fixed_value}'
                )
                return "".join(lines), changes

        # No supported fix for this property occurrence
        return front_matter_text, changes

    return front_matter_text, changes


def process_file(path: Path, prop: str, commit: bool) -> bool:
    original_text = path.read_text(encoding="utf-8")
    bounds = find_front_matter_bounds(original_text)
    if bounds is None:
        return False

    start, end = bounds
    front_matter = original_text[start:end]
    new_front_matter, changes = fix_property_in_front_matter(front_matter, prop)

    if not changes or new_front_matter == front_matter:
        return False

    new_text = original_text[:start] + new_front_matter + original_text[end:]

    print(f"\n=== {path.name} ===")
    for c in changes:
        print(c)

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

    prop = args.property_name
    if not prop:
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
            changed = process_file(path, prop, args.commit)
            if changed:
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

