#!/usr/bin/env python3
"""
Fill empty 'japanese_native' fields in character files using the
davidluzgouveia/kanji-data dataset (readings_kun).

Downloads kanji.json on first run and caches it beside this script as
kanji-data.json.  Only fills fields that are currently empty; already-
populated fields are left untouched.  For files missing the field entirely,
it is inserted immediately after japanese_nanori:.

The kun reading is derived by taking readings_kun[0] from the dataset and
stripping everything from the first '.' or '-' onward (e.g. 'ひと-' → 'ひと',
'た.べる' → 'た').  Readings that reduce to an empty string after stripping
(e.g. leading '-り') are skipped in favour of the next entry in the list.

Usage:
  python3 fill_japanese_native.py           # process all empty fields
  python3 fill_japanese_native.py --dry-run # preview without writing
"""

import json
import os
import re
import sys
import urllib.request

CHARS_DIR   = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH  = os.path.join(CHARS_DIR, "kanji-data.json")
DATASET_URL = (
    "https://raw.githubusercontent.com/davidluzgouveia/kanji-data"
    "/master/kanji.json"
)

DRY_RUN = "--dry-run" in sys.argv


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

def load_dataset():
    if not os.path.exists(CACHE_PATH):
        print(f"Downloading kanji dataset → {CACHE_PATH} …")
        req = urllib.request.Request(
            DATASET_URL,
            headers={"User-Agent": "Mozilla/5.0 (compatible; research bot)"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        with open(CACHE_PATH, "wb") as fh:
            fh.write(data)
        print("Download complete.\n")
    else:
        print(f"Using cached dataset: {CACHE_PATH}\n")

    with open(CACHE_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


def extract_kun(entry):
    """
    Return the base kun reading from a kanji-data entry, or None.

    Iterates readings_kun in order, strips from the first '.' or '-',
    and returns the first non-empty result.
    """
    for reading in entry.get("readings_kun", []):
        m = re.search(r"[.\-]", reading)
        base = reading[: m.start()] if m else reading
        if base:
            return base
    return None


# ---------------------------------------------------------------------------
# Character name extraction
# ---------------------------------------------------------------------------

def char_from_filename(fname):
    """'鞋 (char).md' → '鞋',  '社.md' → '社'"""
    base = fname[:-3]  # strip .md
    return base[:-7] if base.endswith(" (char)") else base


# ---------------------------------------------------------------------------
# Frontmatter inspection
# ---------------------------------------------------------------------------

def _field_is_empty(fm_text, field):
    """
    True if `field:` is present in the frontmatter but carries no value
    (bare colon, null, "", or '').
    """
    m = re.search(
        r"^" + re.escape(field) + r":[ \t]*(null|\"\"|\'{2}|)[ \t]*$",
        fm_text,
        re.MULTILINE,
    )
    if not m:
        return False
    # Not empty if list items follow on the next lines
    rest = fm_text[m.end():]
    return not re.match(r"\n[ \t]+-", rest)


def needs_fill(fm_text):
    """
    True if japanese_native should be written:
      - field is present but empty, OR
      - field is absent entirely.
    False if the field already has a real value.
    """
    if "japanese_native" not in fm_text:
        return True  # absent — needs to be inserted
    return _field_is_empty(fm_text, "japanese_native")


# ---------------------------------------------------------------------------
# Frontmatter update
# ---------------------------------------------------------------------------

def apply_value(content, value):
    """
    Insert or replace japanese_native: <value> in the YAML frontmatter.

    - If the field already exists (empty), replaces it in place.
    - If the field is absent, inserts it on the line after japanese_nanori:.
    """
    fm_m = re.match(r"^(---\n)(.*?)(\n---)", content, re.DOTALL)
    if not fm_m:
        return content  # no frontmatter — skip

    fm_text = fm_m.group(2)

    if re.search(r"^japanese_native:", fm_text, re.MULTILINE):
        # Replace the existing empty line
        new_fm = re.sub(
            r"^japanese_native:[ \t]*(null|\"\"|\'{2}|)[ \t]*$",
            lambda _: f"japanese_native: {value}",
            fm_text,
            flags=re.MULTILINE,
        )
    else:
        # Insert after japanese_nanori: (always a scalar in these files)
        new_fm = re.sub(
            r"^(japanese_nanori:[^\n]*)$",
            lambda m: m.group(1) + f"\njapanese_native: {value}",
            fm_text,
            flags=re.MULTILINE,
        )

    return fm_m.group(1) + new_fm + fm_m.group(3) + content[fm_m.end():]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dataset = load_dataset()
    print(f"Loaded {len(dataset):,} kanji entries.")

    files = sorted(f for f in os.listdir(CHARS_DIR) if f.endswith(".md"))

    if DRY_RUN:
        print("DRY RUN — no files will be written.\n")

    updated = skipped_populated = not_in_dataset = no_kun = 0

    for fname in files:
        fpath = os.path.join(CHARS_DIR, fname)
        content = open(fpath, encoding="utf-8").read()

        fm_m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_m:
            continue

        fm_text = fm_m.group(1)

        if not needs_fill(fm_text):
            skipped_populated += 1
            continue

        char = char_from_filename(fname)
        entry = dataset.get(char)
        if entry is None:
            not_in_dataset += 1
            continue

        value = extract_kun(entry)
        if not value:
            no_kun += 1
            continue

        print(f"  {char}  →  {value}")

        if not DRY_RUN:
            new_content = apply_value(content, value)
            with open(fpath, "w", encoding="utf-8") as fh:
                fh.write(new_content)
        updated += 1

    action = "Would update" if DRY_RUN else "Updated"
    print(
        f"\nDone.\n"
        f"  {action}:             {updated:>5}\n"
        f"  Already populated:   {skipped_populated:>5}\n"
        f"  Not in dataset:      {not_in_dataset:>5}\n"
        f"  No kun reading:      {no_kun:>5}\n"
    )


if __name__ == "__main__":
    main()
