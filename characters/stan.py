#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Optional, Tuple


# Front matter must be at the start of the file.
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.DOTALL)


def split_front_matter(text: str) -> Optional[Tuple[str, str]]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None
    return m.group(1), m.group(2)


def build_stand_in_true_line_re() -> re.Pattern:
    """
    Match a YAML line like:
      stand_in: TRUE
      stand_in: "TRUE"
      stand_in: true
      stand_in: "true"
      stand_in: True
    preserving indentation and trailing comments.
    """
    return re.compile(
        r"""
        ^([ \t]*stand_in[ \t]*:[ \t]*)
        (?:
            TRUE|True|true
          | "TRUE"|"True"|"true"
          | 'TRUE'|'True'|'true'
        )
        ([ \t]*(?:\#.*)?)$
        """,
        re.MULTILINE | re.VERBOSE,
    )


def plan_changes(path: Path) -> Optional[Tuple[str, str, Path]]:
    """
    If file should be changed, returns:
      (old_stand_in_line, new_stand_in_line, new_path)
    Otherwise returns None.

    This function does not perform any writes.
    """
    stem = path.stem  # X
    text = path.read_text(encoding="utf-8")
    parts = split_front_matter(text)
    if parts is None:
        return None

    fm, body = parts
    line_re = build_stand_in_true_line_re()

    m = line_re.search(fm)
    if not m:
        return None

    # Compute the exact old line from the match span (line text only)
    # Find the line boundaries around the match
    start, end = m.span()
    # Extract matched line in front matter (including indentation + comments)
    old_line = fm[start:end]

    prefix = m.group(1)
    suffix = m.group(2) or ""
    new_line = f"{prefix}{stem}{suffix}"

    new_name = f"{stem} (char){path.suffix}"
    new_path = path.with_name(new_name)

    return old_line, new_line, new_path


def apply_changes(path: Path) -> bool:
    """
    Apply stand_in line change and rename file.
    Returns True if changes were made.
    """
    stem = path.stem
    text = path.read_text(encoding="utf-8")
    parts = split_front_matter(text)
    if parts is None:
        return False

    fm, body = parts
    line_re = build_stand_in_true_line_re()

    def repl(m: re.Match) -> str:
        prefix = m.group(1)
        suffix = m.group(2) or ""
        return f"{prefix}{stem}{suffix}"

    new_fm, n = line_re.subn(repl, fm, count=1)
    if n == 0:
        return False

    new_text = f"---\n{new_fm}\n---\n{body}"

    # Write content change first (same file), then rename.
    path.write_text(new_text, encoding="utf-8")

    new_path = path.with_name(f"{stem} (char){path.suffix}")
    if new_path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {new_path}")

    path.rename(new_path)
    return True


def main() -> None:
    ap = argparse.ArgumentParser(
        description="In /characters: if YAML has stand_in: TRUE, change it to stand_in: X and rename to 'X (char).md'."
    )
    ap.add_argument(
        "--commit",
        action="store_true",
        help="Actually modify files. Without this flag, runs in preview mode.",
    )
    ap.add_argument(
        "--pattern",
        default="*.md",
        help="Glob pattern of files to scan (default: *.md).",
    )
    args = ap.parse_args()

    cwd = Path(".").resolve()
    files = sorted(cwd.glob(args.pattern))

    if not files:
        print(f"No files matched {args.pattern} in {cwd}")
        return

    preview_count = 0
    commit_count = 0

    for p in files:
        if not p.is_file():
            continue

        planned = plan_changes(p)
        if planned is None:
            continue

        old_line, new_line, new_path = planned
        preview_count += 1

        print(f"\nFILE: {p.name}")
        print("  YAML:")
        print(f"    - {old_line}")
        print(f"    + {new_line}")
        print(f"  RENAME:")
        print(f"    {p.name}  ->  {new_path.name}")

        if args.commit:
            try:
                apply_changes(p)
                commit_count += 1
            except Exception as e:
                print(f"  ERROR: {e}", file=sys.stderr)

    if args.commit:
        print(f"\nCommitted {commit_count} change(s). Previewed {preview_count} eligible file(s).")
    else:
        print(f"\nPreviewed {preview_count} change(s). Re-run with --commit to apply.")


if __name__ == "__main__":
    main()

