#!/usr/bin/env python3
"""
wrap_yaml_hanmun_to_wikilink.py

Turn a scalar YAML front matter field (default: '韓文') into an Obsidian wikilink:
  韓文: 배        -> 韓文: [[배]]
  韓文: "배"      -> 韓文: [[배]]
  韓文: '배'      -> 韓文: [[배]]

Skips if value is already a wikilink ([[...]]), empty/null, or not a scalar.
Preserves ALL other YAML formatting (order, comments, quoting) using ruamel.yaml round-trip mode.

USAGE
-----
python3 wrap_yaml_hanmun_to_wikilink.py \
  --root "/path/to/your/obsidian/vault" \
  --glob "characters/*.md" \
  [--key "韓文"] \
  [--dry-run] \
  [--no-backup]

Notes
-----
- Use a virtualenv and install ruamel.yaml:
    python3 -m venv .venv && source .venv/bin/activate
    pip install ruamel.yaml
"""

import argparse
import io
import re
import sys
from pathlib import Path

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedMap
except Exception as e:
    print("ERROR: This script requires 'ruamel.yaml'. Install with:", file=sys.stderr)
    print("  python3 -m pip install ruamel.yaml", file=sys.stderr)
    sys.exit(2)

WIKILINK_RE = re.compile(r'^\s*\[\[.+\]\]\s*$')


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


def process_file(path: Path, key: str, dry_run: bool, make_backup: bool) -> str:
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

    # Only convert scalar strings; leave lists/mappings untouched
    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "" or WIKILINK_RE.match(stripped):
            return f"[OK  ] {path}: '{key}' already wikilink or empty"
        new_value = f"[[{stripped}]]"
        data[key] = new_value
        # Dump back (round-trip preserves everything else)
        buf = io.StringIO()
        yaml_rt.dump(data, buf)
        new_yaml = buf.getvalue()
        new_text = f"{before}{new_yaml}{after_delim}{body}"

        if dry_run:
            return f"[DRY ] {path}: would wrap '{key}' -> {new_value}"

        if make_backup:
            path.with_suffix(path.suffix + ".bak").write_text(text, encoding="utf-8", errors="surrogatepass")

        path.write_text(new_text, encoding="utf-8", errors="surrogatepass")
        return f"[EDIT] {path}: wrapped '{key}' -> {new_value}"

    else:
        return f"[OK  ] {path}: '{key}' not a scalar string (no change)"


def main():
    ap = argparse.ArgumentParser(description="Wrap YAML '韓文' value with wikilinks [[...]] (format-preserving).")
    ap.add_argument("--root", required=True, help="Root folder to scan (Obsidian vault root)")
    ap.add_argument("--glob", default="characters/*.md", help="Glob pattern relative to root (default: characters/*.md)")
    ap.add_argument("--key", default="韓文", help="YAML key to wrap (default: 韓文)")
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
        msg = process_file(f, key=args.key, dry_run=args.dry_run, make_backup=make_backup)
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
