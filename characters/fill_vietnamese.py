#!/usr/bin/env python3
"""
Fill empty 'vietnamese' fields in character files by scraping nomfoundation.org.
Throttled to one request per 10 seconds.

Usage:
  python3 fill_vietnamese.py               # process all empty fields
  python3 fill_vietnamese.py --dry-run     # preview without writing
  python3 fill_vietnamese.py --limit 5     # process at most 5 files
"""

import html
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CHARS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = (
    "https://www.nomfoundation.org/nom-tools/Nom-Lookup-Tool/"
    "Nom-Lookup-Tool"
)
DELAY = 10  # seconds between requests

DRY_RUN = "--dry-run" in sys.argv
LIMIT = None
for i, arg in enumerate(sys.argv):
    if arg == "--limit" and i + 1 < len(sys.argv):
        LIMIT = int(sys.argv[i + 1])


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def char_from_filename(fname):
    """Extract the character from 'X (char).md' or 'X.md'."""
    base = fname[:-3]  # strip .md
    if base.endswith(" (char)"):
        return base[:-7]
    return base


def is_empty_vietnamese(fm_text):
    """
    Return True if the vietnamese field is present but has no value.
    Handles: bare 'vietnamese:', 'vietnamese: null', 'vietnamese: ""', "vietnamese: ''"
    Returns False for any non-empty scalar or list value.
    """
    m = re.search(
        r"^vietnamese:[ \t]*(null|\"\"|\'{2}|)[ \t]*$",
        fm_text,
        re.MULTILINE,
    )
    if not m:
        return False
    # Make sure there are no list items on subsequent lines
    rest = fm_text[m.end():]
    if re.match(r"\n[ \t]+-", rest):
        return False
    return True


def fetch_html(char):
    """Fetch the nomfoundation lookup page for the given character."""
    encoded = urllib.parse.quote(char)
    url = (
        f"{BASE_URL}?input_type=rqn_or_hn"
        f"&inputText={encoded}&uiLang=en&GO=GO"
    )
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; research bot)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_readings(page_html):
    """
    Extract unique Quoc Ngu readings from the nomfoundation results table.

    The page has a <table class=reference> whose header row columns are:
      Quốc Ngữ | Hán-Nôm | Context | Ref. | English

    Each data row has the reading in the first <td>, inside <font size=+1>.
    """
    table_m = re.search(
        r"<table[^>]+class=reference[^>]*>(.*?)</table>",
        page_html,
        re.DOTALL | re.IGNORECASE,
    )
    if not table_m:
        return []

    readings = []
    for row_m in re.finditer(
        r"<tr[^>]*>(.*?)</tr>", table_m.group(1), re.DOTALL | re.IGNORECASE
    ):
        row = row_m.group(1)
        # Skip header rows (yellow background or <th> elements)
        if re.search(r"bgcolor=#[Ff]{4}99", row):
            continue
        if re.search(r"<th[\s>]", row, re.IGNORECASE):
            continue
        # First <td> is the Quoc Ngu column
        td_m = re.search(r"<td[^>]*>(.*?)</td>", row, re.DOTALL | re.IGNORECASE)
        if not td_m:
            continue
        # Reading is wrapped in <font size=+1>
        font_m = re.search(
            r"<font[^>]*size=\+1[^>]*>(.*?)</font>",
            td_m.group(1),
            re.DOTALL | re.IGNORECASE,
        )
        if not font_m:
            continue
        reading = html.unescape(font_m.group(1).strip())
        if reading and reading not in readings:
            readings.append(reading)

    return readings


def set_vietnamese(content, readings):
    """
    Replace the empty 'vietnamese:' line in the YAML frontmatter with a
    populated list.  Single reading stays as a one-item list for consistency.
    """
    list_items = "\n".join(f"  - {r}" for r in readings)
    replacement = f"vietnamese:\n{list_items}"

    # Use a lambda so the replacement is never interpreted as a regex string
    return re.sub(
        r"^vietnamese:[ \t]*(null|\"\"|\'{2}|)[ \t]*$",
        lambda _: replacement,
        content,
        flags=re.MULTILINE,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    all_files = sorted(f for f in os.listdir(CHARS_DIR) if f.endswith(".md"))

    # Collect files with empty vietnamese field
    to_process = []
    for fname in all_files:
        fpath = os.path.join(CHARS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as fh:
            content = fh.read()
        fm_m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_m:
            continue
        if is_empty_vietnamese(fm_m.group(1)):
            to_process.append((fname, fpath, content))

    if LIMIT is not None:
        to_process = to_process[:LIMIT]

    total = len(to_process)
    print(f"Found {total} character files with empty vietnamese field.")
    if DRY_RUN:
        print("DRY RUN — no files will be written.\n")

    updated = 0
    no_result = 0
    errors = 0
    last_request_time = 0.0

    for i, (fname, fpath, content) in enumerate(to_process, 1):
        char = char_from_filename(fname)
        print(f"[{i}/{total}] {char}  ", end="", flush=True)

        # Throttle: wait until DELAY seconds have passed since last request
        elapsed = time.monotonic() - last_request_time
        if elapsed < DELAY:
            wait = DELAY - elapsed
            print(f"(waiting {wait:.1f}s) ", end="", flush=True)
            time.sleep(wait)

        try:
            page_html = fetch_html(char)
            last_request_time = time.monotonic()
        except (urllib.error.URLError, OSError) as exc:
            print(f"ERROR: {exc}")
            errors += 1
            last_request_time = time.monotonic()
            continue

        readings = parse_readings(page_html)

        if not readings:
            print("— no readings found")
            no_result += 1
            continue

        print("→ " + ", ".join(readings))

        if not DRY_RUN:
            new_content = set_vietnamese(content, readings)
            with open(fpath, "w", encoding="utf-8") as fh:
                fh.write(new_content)
        updated += 1

    action = "Would update" if DRY_RUN else "Updated"
    print(
        f"\nDone.  {action}: {updated} | No result: {no_result} | Errors: {errors}"
    )


if __name__ == "__main__":
    main()
