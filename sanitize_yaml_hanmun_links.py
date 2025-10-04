#!/usr/bin/env python3
"""
sanitize_yaml_hanmun_links.py

Clean the YAML field '韓文' across Markdown files:
  - If it's a scalar string, extract inner text (strip [[...]] if present).
  - Remove control characters (U+0000–U+001F, U+007F).
  - Remove zero-width characters: U+200B, U+200C, U+200D, U+FEFF.
  - Trim whitespace.
  - Unicode-normalize to NFC (so '받' is composed).
  - Re-wrap as a proper wikilink: [[VALUE]].
Preserves ALL other YAML content (order, comments, quoting) using ruamel.yaml round-trip mode.

USAGE
-----
python3 sanitize_yaml_hanmun_links.py \
  --root "/path/to/your/obsidian/vault" \
  --glob "characters/*.md" \
  [--key "韓文"] \
  [--dry-run] \
  [--no-backup]
"""

import argparse
import io
import re
import sys
import unicodedata
from pathlib import Path

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedMap
except Exception as e:
    print("ERROR: This script requires 'ruamel.yaml'. Install with:", file=sys.stderr)
    print("  python3 -m pip install ruamel.yaml", file=sys.stderr)
    sys.exit(2)

WIKILINK_CAPTURE = re.compile(r'^\s*\[\[(.*)\]\]\s*$')

CONTROL_CHARS = ''.join(chr(c) for c in list(range(0x00, 0x20)) + [0x7F])
ZERO_WIDTH = ''.join([
    '\u200b', # ZERO WIDTH SPACE
    '\u200c', # ZERO WIDTH NON-JOINER
    '\u200d', # ZERO WIDTH JOINER
    '\ufeff', # ZERO WIDTH NO-BREAK SPACE
])
STRIP_CHARS = CONTROL_CHARS + ZERO_WIDTH
STRIP_TABLE = str.maketrans('', '', STRIP_CHARS)


def find_front_matter_bounds(lines):
    if not lines:
        return -1, -1
    if lines[0].strip() != "---":
        return -1, -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    return -1, -1


def sanitize_value(raw: str) -> str:
    # Extract inner text if value is a wikilink
    m = WIKILINK_CAPTURE.match(raw)
    if m:
        raw_inner = m.group(1)
    else:
        raw_inner = raw

    # Remove control + zero-width chars and trim
    cleaned = raw_inner.translate(STRIP_TABLE).strip()

    # Unicode normalize to NFC (compose Hangul, etc.)
    cleaned = unicodedata.normalize('NFC', cleaned)

    # Re-wrap as wikilink
    return f"[[{cleaned}]]" if cleaned else ""


def process_file(path: Path, key: str, dry_run: bool, make_backup: bool) -> str:
    text = path.read_text(encoding="utf-8", errors="surrogatepass")
    lines = text.splitlines(keepends=True)

    start, end = find_front_matter_bounds(lines)
    if start == -1:
        return f"[SKIP] {path}: no YAML front matter"

    yaml_block = "".join(lines[start + 1:end])
    before = "".join(lines[:start + 1])   # opening '---'
    after_delim = lines[end]              # closing '---' (with original newline)
    body = "".join(lines[end + 1:])

    yaml_rt = YAML(typ="rt")
    try:
        data = yaml_rt.load(yaml_block)
    except Exception as e:
        return f"[SKIP] {path}: could not parse YAML ({e})"

    if not isinstance(data, CommentedMap):
        return f"[SKIP] {path}: front matter not a mapping"

    if key not in data:
        return f"[OK  ] {path}: no '{key}' field"

    val = data[key]
    if not isinstance(val, str):
        return f"[OK  ] {path}: '{key}' is not a scalar string (no change)"

    new_val = sanitize_value(val)
    if not new_val:
        return f"[OK  ] {path}: '{key}' becomes empty after sanitize (skipping)"

    if new_val == val:
        return f"[OK  ] {path}: '{key}' already clean"

    data[key] = new_val

    # Dump back
    buf = io.StringIO()
    yaml_rt.dump(data, buf)
    new_yaml = buf.getvalue()
    new_text = f"{before}{new_yaml}{after_delim}{body}"

    if dry_run:
        return f"[DRY ] {path}: would set {key}: {new_val!r}"

    if make_backup:
        path.with_suffix(path.suffix + ".bak").write_text(text, encoding="utf-8", errors="surrogatepass")

    path.write_text(new_text, encoding="utf-8", errors="surrogatepass")
    return f"[EDIT] {path}: set {key}: {new_val!r}"


def main():
    ap = argparse.ArgumentParser(description="Sanitize YAML '韓文' to clean wikilink form [[...]] (format-preserving).")
    ap.add_argument("--root", required=True, help="Root folder to scan (Obsidian vault root)")
    ap.add_argument("--glob", default="characters/*.md", help="Glob pattern relative to root (default: characters/*.md)")
    ap.add_argument("--key", default="韓文", help="YAML key to sanitize (default: 韓文)")
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
