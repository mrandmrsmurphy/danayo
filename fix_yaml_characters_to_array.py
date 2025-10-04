#!/usr/bin/env python3
"""
fix_yaml_characters_to_array.py

Convert a YAML front matter field (default: 'characters') that is incorrectly
stored as a single quoted string with commas (e.g., "人, 名, 台") into a proper
YAML sequence:
  characters:
    - 人
    - 名
    - 台

Preserves ALL other YAML formatting, key order, and comments via ruamel.yaml
round-trip mode.

USAGE
-----
python3 fix_yaml_characters_to_array.py \
  --root "/path/to/your/obsidian/vault" \
  --glob "words/*.md" \
  [--key "characters"] \
  [--delimiter ","] \
  [--dry-run] \
  [--no-backup]

Notes
-----
- Install dependency first in a virtualenv:
    python3 -m venv .venv && source .venv/bin/activate
    pip install ruamel.yaml
- Front matter recognized only if the first line is '---' and a closing '---'
  appears later on its own line.
"""

import argparse
import io
import sys
from pathlib import Path

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedMap, CommentedSeq
except Exception as e:
    print("ERROR: This script requires 'ruamel.yaml'. Install with:", file=sys.stderr)
    print("  python3 -m pip install ruamel.yaml", file=sys.stderr)
    sys.exit(2)


def find_front_matter_bounds(lines):
    """
    Return (start_idx, end_idx) for YAML front matter delimiters '---'..'---'.
    If not present, return (-1, -1).
    """
    if not lines:
        return -1, -1
    if lines[0].strip() != "---":
        return -1, -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    return -1, -1


def to_list_from_string(value: str, delimiter: str):
    # Split on delimiter, trim whitespace, drop empties
    parts = [p.strip() for p in value.split(delimiter)]
    parts = [p for p in parts if p != ""]
    return parts


def process_file(path: Path, key: str, delimiter: str, dry_run: bool, make_backup: bool) -> str:
    text = path.read_text(encoding="utf-8", errors="surrogatepass")
    lines = text.splitlines(keepends=True)

    start, end = find_front_matter_bounds(lines)
    if start == -1:
        return f"[SKIP] {path}: no YAML front matter"

    yaml_block = "".join(lines[start + 1:end])
    before = "".join(lines[:start + 1])   # includes opening '---'
    after_delim = lines[end]              # the closing '---' line (with its original newline)
    body = "".join(lines[end + 1:])

    yaml_rt = YAML(typ="rt")  # round-trip
    try:
        data = yaml_rt.load(yaml_block)
    except Exception as e:
        return f"[SKIP] {path}: could not parse YAML ({e})"

    if not isinstance(data, CommentedMap):
        return f"[SKIP] {path}: front matter not a mapping"

    if key not in data:
        return f"[OK  ] {path}: no '{key}' field"

    value = data[key]

    # Case A: top-level scalar string with commas -> split to list
    if isinstance(value, str):
        items = to_list_from_string(value, delimiter)
        if len(items) <= 1:
            return f"[OK  ] {path}: '{key}' is a string but not comma-separated (no change)"
        new_seq = CommentedSeq(items)
        data[key] = new_seq
        action = f"string→list ({len(items)} items)"

    # Case B: list with a single string containing commas -> expand
    elif isinstance(value, list) and len(value) == 1 and isinstance(value[0], str) and delimiter in value[0]:
        items = to_list_from_string(value[0], delimiter)
        if len(items) <= 1:
            return f"[OK  ] {path}: '{key}' single-item list without commas (no change)"
        new_seq = CommentedSeq(items)
        data[key] = new_seq
        action = f"1-item-list→list ({len(items)} items)"

    else:
        return f"[OK  ] {path}: '{key}' already a list or not applicable"

    # Dump back (round-trip preserves everything else)
    buf = io.StringIO()
    yaml_rt.dump(data, buf)
    new_yaml = buf.getvalue()
    new_text = f"{before}{new_yaml}{after_delim}{body}"

    if dry_run:
        return f"[DRY ] {path}: would convert '{key}' {action}"

    if make_backup:
        path.with_suffix(path.suffix + ".bak").write_text(text, encoding="utf-8", errors="surrogatepass")

    path.write_text(new_text, encoding="utf-8", errors="surrogatepass")
    return f"[EDIT] {path}: converted '{key}' {action}"


def main():
    ap = argparse.ArgumentParser(description="Convert YAML 'characters' field from comma-joined string to list (format-preserving).")
    ap.add_argument("--root", required=True, help="Root folder to scan (Obsidian vault root)")
    ap.add_argument("--glob", default="words/*.md", help="Glob pattern relative to root (default: words/*.md)")
    ap.add_argument("--key", default="characters", help="YAML key to normalize (default: characters)")
    ap.add_argument("--delimiter", default=",", help="Delimiter used inside the string (default: ,)")
    ap.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    ap.add_argument("--no-backup", action="store_true", help="Do not create .bak backups")

    args = ap.parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        sys.exit(1)

    files = sorted(root.glob(args.glob))
    if not files:
        print(f"NOTE: No files matched {args.glob} under {root}", file=sys.stderr)

    make_backup = not args.no_backup

    counts = {"edit": 0, "ok": 0, "skip": 0, "dry": 0}
    for f in files:
        if not f.is_file():
            continue
        msg = process_file(f, key=args.key, delimiter=args.delimiter, dry_run=args.dry_run, make_backup=make_backup)
        print(msg)
        if msg.startswith("[EDIT]"):
            counts["edit"] += 1
        elif msg.startswith("[OK"):
            counts["ok"] += 1
        elif msg.startswith("[DRY"):
            counts["dry"] += 1
        else:
            counts["skip"] += 1

    print("\nSummary:", counts)


if __name__ == "__main__":
    main()
