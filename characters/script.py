#!/usr/bin/env python3

from __future__ import annotations

import re
import argparse
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("This script requires PyYAML. In your venv: python -m pip install pyyaml")
    raise


CHAR_FILE_RE = re.compile(r"^(?P<char>.) \(char\)\.md$")
FRONTMATTER_RE = re.compile(r"^(---\n)(.*?)(\n---\n?)", re.DOTALL)


def normalize(text: str) -> str:
    return text.strip().casefold()


def coerce_aliases(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [x for x in value if isinstance(x, str)]
    return []


def process_file(path: Path, apply: bool) -> bool:
    m = CHAR_FILE_RE.match(path.name)
    if not m:
        return False

    char = m.group("char")

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Could not read {path}: {e}")
        return False

    match = FRONTMATTER_RE.match(text)
    if not match:
        return False

    start, raw_yaml, end = match.groups()

    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        print(f"YAML parse error in {path}: {e}")
        return False

    if not isinstance(data, dict) or "aliases" not in data:
        return False

    aliases = coerce_aliases(data.get("aliases"))
    if not aliases:
        return False

    norm_char = normalize(char)

    removed = [a for a in aliases if normalize(a) == norm_char]
    if not removed:
        return False

    new_aliases = [a for a in aliases if normalize(a) != norm_char]

    print(f"\n{path}")
    print(f"  character: {char}")
    print(f"  removing: {removed}")
    print(f"  remaining: {new_aliases if new_aliases else '[] (aliases will be deleted)'}")

    if not apply:
        return True

    # apply change
    if not new_aliases:
        del data["aliases"]
    else:
        data["aliases"] = new_aliases

    new_yaml = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip()

    new_text = f"{start}{new_yaml}{end}{text[match.end():]}"
    path.write_text(new_text, encoding="utf-8")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove self-alias from X (char).md files")
    parser.add_argument("--apply", action="store_true", help="Modify files")
    parser.add_argument("--confirm", action="store_true", help="Ask before applying")
    args = parser.parse_args()

    root = Path(".")
    matches = []

    for path in root.glob("*.md"):
        if process_file(path, apply=False):
            matches.append(path)

    if not matches:
        print("No matching aliases found.")
        return

    print(f"\nFound {len(matches)} file(s) with self-alias.")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to modify files.")
        return

    if args.confirm:
        resp = input("Proceed with changes? [y/N] ").strip().lower()
        if resp != "y":
            print("Aborted.")
            return

    changed = 0
    for path in root.glob("*.md"):
        if process_file(path, apply=True):
            changed += 1

    print(f"\nDone. Updated {changed} file(s).")


if __name__ == "__main__":
    main()

