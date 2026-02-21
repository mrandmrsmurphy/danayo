#!/usr/bin/env python3
"""
Duplicate stand-in markdown files into a subfolder, trimming YAML keys and
rewriting nav paths in the duplicate only.

Requirements:
  pip install pyyaml
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any, Dict, Tuple, Optional

import yaml


KEEP_KEYS = {
    "mandarin",
    "cantonese",
    "korean",
    "vietnamese",
    "english",
    "羅馬字",
    "韓文",
    "注音",
}

DEFAULT_OUTDIR = "char_info_duplicates"


FRONT_MATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---\s*\n?",
    re.DOTALL,
)


def split_front_matter(text: str) -> Tuple[Optional[str], str, str]:
    """
    Returns (yaml_text_or_None, body_text, full_front_matter_block_or_empty).

    - If YAML front matter exists at the very start of the file, extracts it.
    - Otherwise returns (None, original_text, "").
    """
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None, text, ""
    yaml_text = m.group(1)
    fm_block = m.group(0)  # includes --- delimiters
    body = text[len(fm_block):]
    return yaml_text, body, fm_block


def parse_yaml(yaml_text: str, src: Path) -> Dict[str, Any]:
    try:
        data = yaml.safe_load(yaml_text) if yaml_text.strip() else {}
    except yaml.YAMLError as e:
        raise RuntimeError(f"YAML parse error in {src}: {e}") from e

    if data is None:
        return {}
    if not isinstance(data, dict):
        raise RuntimeError(f"Front matter in {src} is not a mapping/dict.")
    return data


def truthy_stand_in(value: Any) -> bool:
    """
    Accepts:
      TRUE / true / "TRUE" / "true" / True
    """
    if isinstance(value, bool):
        return value is True
    if isinstance(value, str):
        return value.strip().lower() == "true"
    return False


def dump_yaml(data: Dict[str, Any]) -> str:
    # allow_unicode keeps the CJK keys readable
    # sort_keys=False preserves insertion order (Python 3.7+)
    return yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=120,
    ).rstrip() + "\n"


def process_file(src: Path, outdir: Path) -> bool:
    """
    Returns True if a duplicate was created.
    """
    text = src.read_text(encoding="utf-8")
    yaml_text, body, _ = split_front_matter(text)

    if yaml_text is None:
        return False  # no front matter => no stand_in property

    fm = parse_yaml(yaml_text, src)

    if not truthy_stand_in(fm.get("stand_in")):
        return False

    # Build new front matter with only allowed keys (if they exist),
    # preserving their values (including lists, dicts, etc.).
    new_fm: Dict[str, Any] = {}
    for k in KEEP_KEYS:
        if k in fm:
            new_fm[k] = fm[k]

    # Add characters: X (filename stem)
    new_fm["characters"] = src.stem

    # Rewrite nav path in body only
    new_body = body.replace("nav/word_info", "nav/char_info")

    # Write duplicate
    outdir.mkdir(parents=True, exist_ok=True)
    dst = outdir / src.name
    new_text = "---\n" + dump_yaml(new_fm) + "---\n" + new_body
    dst.write_text(new_text, encoding="utf-8")

    return True


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(description="Duplicate stand-in md files into a subfolder with trimmed YAML.")
    p.add_argument(
        "-o",
        "--outdir",
        default=DEFAULT_OUTDIR,
        help=f"Output subfolder name (default: {DEFAULT_OUTDIR})",
    )
    args = p.parse_args()

    cwd = Path(".").resolve()
    outdir = cwd / args.outdir

    created = 0
    scanned = 0

    for src in sorted(cwd.glob("*.md")):
        scanned += 1
        if process_file(src, outdir):
            created += 1

    print(f"Scanned {scanned} *.md files.")
    print(f"Created {created} duplicates in: {outdir}")


if __name__ == "__main__":
    main()
