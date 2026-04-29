#!/usr/bin/env python3
"""
wiktionary_scraper.py — scrapes graphemic classification data from Wiktionary
and writes the graphemic Notes bullet into Dan'a'yo character pages.

Usage:
    python scripts/wiktionary_scraper.py 儒          # dry run — print proposed bullet
    python scripts/wiktionary_scraper.py 儒 --write  # update the character file
    python scripts/wiktionary_scraper.py --batch     # dry run all chars missing bullet 1
    python scripts/wiktionary_scraper.py --batch --write  # update all

Run from the vault root.

Dependencies: pip install requests beautifulsoup4
"""

import argparse
import re
import sys
import time
import urllib.parse
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup, Tag
except ImportError:
    sys.exit("Install dependencies: pip install requests beautifulsoup4")

# ── Paths ────────────────────────────────────────────────────────────────────

VAULT = Path(__file__).parent.parent
CHARS_DIR = VAULT / "characters"
RADICALS_DIR = VAULT / "lookup" / "Radicals"

# ── Radical lookup ────────────────────────────────────────────────────────────

def build_radical_map() -> tuple[dict, dict]:
    """
    Return (canonical, variants) where:
      canonical: radical_char -> zero-padded number string, e.g. "人" -> "009"
      variants:  variant_char -> same number string, e.g.  "亻" -> "009"
    """
    canonical: dict[str, str] = {}
    variants: dict[str, str] = {}

    for f in sorted(RADICALS_DIR.glob("Radical *.md")):
        m = re.match(r"Radical (\d+)\.md", f.name)
        if not m:
            continue
        num = m.group(1).zfill(3)
        text = f.read_text(encoding="utf-8")

        # frontmatter radical field
        fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if fm:
            rm = re.search(r"^radical:\s*(.+)$", fm.group(1), re.MULTILINE)
            if rm:
                ch = rm.group(1).strip().strip('"').strip("'")
                canonical[ch] = num

        # body: "Appears as 亻when…" — grab only the leading CJK character(s)
        for vm in re.finditer(r"Appears as\s*([⺀-鿿]+)", text):
            ch = vm.group(1)
            variants[ch] = num

    return canonical, variants


def radical_link(sem_char: str, canonical: dict, variants: dict) -> str:
    """
    Return the Obsidian wiki-link for the semantic radical component.
    Format: [[Radical NNN|亻]] when we know the number, else [[亻]].
    """
    num = canonical.get(sem_char) or variants.get(sem_char)
    if num:
        return f"[[Radical {num}|{sem_char}]]"
    return f"[[{sem_char}]]"


# ── Character file lookup ────────────────────────────────────────────────────

def find_char_file(char: str) -> Path | None:
    for name in (f"{char} (char).md", f"{char}.md"):
        p = CHARS_DIR / name
        if p.exists():
            return p
    return None


def read_frontmatter(text: str) -> dict:
    """Return a flat dict of frontmatter key→value (strings only)."""
    result: dict[str, str] = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return result
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if kv:
            result[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return result


# ── Wiktionary scraping ──────────────────────────────────────────────────────

HEADERS = {"User-Agent": "DanayoWikiBot/1.0 (Dan'a'yo vault; educational use)"}


def fetch_soup(char: str) -> BeautifulSoup:
    url = f"https://en.wiktionary.org/wiki/{urllib.parse.quote(char)}"
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def _text_of(tag: Tag) -> str:
    return tag.get_text(separator=" ", strip=True)


def _find_para(soup: BeautifulSoup, href_fragment: str) -> Tag | None:
    for a in soup.find_all("a", href=re.compile(re.escape(href_fragment))):
        p = a.find_parent("p")
        if p:
            return p
    return None


def parse_graphemic(soup: BeautifulSoup) -> dict | None:
    """
    Detect graphemic type and return structured data.
    Returns None if nothing is found.
    """
    # ── 形声 (phono-semantic) ────────────────────────────────────────────────
    p = _find_para(soup, "phono-semantic_compound")
    if p:
        return _parse_phono_semantic(p)

    # ── 会意 (compound ideograph) ────────────────────────────────────────────
    p = _find_para(soup, "ideogrammic_compound")
    if p:
        return {"type": "会意", "raw": _text_of(p)}

    # ── 象形 (pictogram) ─────────────────────────────────────────────────────
    p = _find_para(soup, "pictogram")
    if p and ("象形" in _text_of(p) or "Pictogram" in _text_of(p)):
        return {"type": "象形", "raw": _text_of(p)}

    # ── 指事 (ideographic indicator) ─────────────────────────────────────────
    p = _find_para(soup, "ideographic_indicator")
    if p:
        return {"type": "指事", "raw": _text_of(p)}

    return None


def _parse_phono_semantic(p: Tag) -> dict:
    # OC reconstructions: lang="och-Latn-fonipa" spans
    ipa = p.find_all("span", {"lang": "och-Latn-fonipa"})
    oc_whole    = ipa[0].get_text() if len(ipa) > 0 else ""
    oc_phonetic = ipa[1].get_text() if len(ipa) > 1 else ""

    # Hani mentions: i tags with lang="zh" and class containing "Hani"
    hani = [t for t in p.find_all("i", lang="zh") if "Hani" in (t.get("class") or [])]
    semantic_char = hani[0].get_text() if len(hani) > 0 else ""
    phonetic_char = hani[1].get_text() if len(hani) > 1 else ""

    # Semantic gloss: first .mention-gloss span
    gloss_spans = p.find_all("span", class_="mention-gloss")
    semantic_gloss = gloss_spans[0].get_text() if gloss_spans else ""

    # Optional explanatory note after the phonetic block
    raw = _text_of(p)
    note = ""
    m = re.search(r'\)\s*[–—-]+\s*(.+?)\.?\s*$', raw)
    if m:
        note = m.group(1).strip()

    return {
        "type": "形声",
        "oc_whole": oc_whole,
        "semantic_char": semantic_char,
        "semantic_gloss": semantic_gloss,
        "phonetic_char": phonetic_char,
        "oc_phonetic": oc_phonetic,
        "note": note,
    }


# ── Bullet formatting ────────────────────────────────────────────────────────

def escape_asterisk(s: str) -> str:
    """Escape leading * so Markdown doesn't italicise OC reconstructions."""
    return s.replace("*", r"\*")


def format_bullet(data: dict, canonical: dict, variants: dict) -> str:
    t = data["type"]

    if t == "形声":
        oc_w  = escape_asterisk(data["oc_whole"])
        oc_ph = escape_asterisk(data["oc_phonetic"])
        sem   = data["semantic_char"]
        gloss = data["semantic_gloss"]
        phon  = data["phonetic_char"]
        note  = data.get("note", "")

        sem_link  = radical_link(sem, canonical, variants)
        phon_link = f"[[{phon}]]"

        bullet = (
            f"- 形声 (OC {oc_w}): "
            f"semantic {sem_link} (\"{gloss}\") "
            f"+ phonetic {phon_link} (OC {oc_ph})"
        )
        if note:
            bullet += f" — {note}"
        bullet += "."
        return bullet

    elif t == "会意":
        raw = data["raw"]
        # Strip the leading "Ideogrammic compound (会意 / 会意, ...) " prefix
        cleaned = re.sub(
            r'^Ideogrammic compound\s*\([^)]+\)\s*[–—:]*\s*', '', raw
        ).strip()
        return f"- 会意: {cleaned}"

    elif t == "象形":
        raw = data["raw"]
        cleaned = re.sub(
            r'^Pictogram\s*\([^)]+\)\s*[–—:]*\s*', '', raw
        ).strip()
        return (
            f"- [List of 象形](lookup/List%20of%20象形.md): "
            f"{cleaned}"
        )

    elif t == "指事":
        raw = data["raw"]
        cleaned = re.sub(
            r'^Ideographic indicator\s*\([^)]+\)\s*[–—:]*\s*', '', raw
        ).strip()
        return (
            f"- [List of 指事](lookup/List%20of%20指事.md): "
            f"{cleaned}"
        )

    return f"- {data.get('raw', '')}"


# ── File update ──────────────────────────────────────────────────────────────

GRAPHEMIC_PREFIXES = ("- 形声", "- 会意", "- 象形", "- 指事",
                      "- [List of 象形", "- [List of 指事")


def has_graphemic_bullet(text: str) -> bool:
    """Return True if the Notes section already has a graphemic bullet."""
    in_notes = False
    for line in text.splitlines():
        if re.match(r"^## Notes", line):
            in_notes = True
            continue
        if in_notes and re.match(r"^##", line):
            break
        if in_notes and any(line.startswith(p) for p in GRAPHEMIC_PREFIXES):
            return True
    return False


def insert_or_replace_bullet(text: str, new_bullet: str) -> str:
    """
    Replace an existing graphemic bullet in ## Notes,
    or insert one as the first bullet if none exists.
    """
    lines = text.splitlines(keepends=True)
    in_notes = False
    notes_start = None

    for i, line in enumerate(lines):
        if re.match(r"^## Notes", line):
            in_notes = True
            notes_start = i
            continue
        if in_notes:
            if re.match(r"^##", line):
                # End of Notes section — insert before this heading
                lines.insert(i, new_bullet + "\n")
                return "".join(lines)
            if any(line.strip().startswith(p) for p in GRAPHEMIC_PREFIXES):
                # Replace existing graphemic bullet
                lines[i] = new_bullet + "\n"
                return "".join(lines)
            if line.strip().startswith("- ") and notes_start is not None:
                # First non-graphemic bullet — insert before it
                lines.insert(i, new_bullet + "\n")
                return "".join(lines)
            if line.strip() == "" and i > notes_start + 1:
                # Blank line after Notes header — insert here
                lines[i] = new_bullet + "\n"
                return "".join(lines)

    # Notes section never found — append it
    if not text.endswith("\n"):
        text += "\n"
    text += f"\n## Notes\n{new_bullet}\n"
    return text


# ── Core logic ───────────────────────────────────────────────────────────────

def process_char(char: str, write: bool, canonical: dict, variants: dict,
                 verbose: bool = True) -> bool:
    """
    Scrape and (optionally) update one character.
    Returns True on success, False on failure.
    """
    path = find_char_file(char)
    if path is None:
        print(f"[{char}] No character file found.", file=sys.stderr)
        return False

    text = path.read_text(encoding="utf-8")
    fm   = read_frontmatter(text)

    # Fetch Wiktionary
    try:
        soup = fetch_soup(char)
    except Exception as e:
        print(f"[{char}] Wiktionary fetch failed: {e}", file=sys.stderr)
        return False

    data = parse_graphemic(soup)
    if data is None:
        print(f"[{char}] No graphemic description found on Wiktionary.")
        return False

    bullet = format_bullet(data, canonical, variants)

    existing_gc = fm.get("graphemic_classification", "")
    already_done = has_graphemic_bullet(text)

    if verbose:
        print(f"\n{'─'*60}")
        print(f"  Character : {char}  ({path.name})")
        print(f"  Wiktionary: {data['type']}")
        if data["type"] == "形声":
            print(f"  Phonetic  : {data['phonetic_char']}  OC {data['oc_whole']}")
            print(f"  Semantic  : {data['semantic_char']} ({data['semantic_gloss']})")
            if fm.get("graphemic_classification") not in ("象形","指事","会意","會意"):
                current = existing_gc or "(blank)"
                match = "✓" if existing_gc == data["phonetic_char"] else "≠"
                print(f"  gc field  : {current}  {match}  Wiktionary phonetic: {data['phonetic_char']}")
        print(f"\n  Proposed bullet:")
        print(f"  {bullet}")
        if already_done:
            print(f"  (replaces existing graphemic bullet)")

    if write:
        new_text = insert_or_replace_bullet(text, bullet)
        path.write_text(new_text, encoding="utf-8")
        print(f"  → Written to {path.name}")

    return True


# ── Batch mode ───────────────────────────────────────────────────────────────

def batch(write: bool, canonical: dict, variants: dict):
    """Process all character files that are missing a graphemic bullet."""
    files = sorted(CHARS_DIR.glob("*.md"))
    total = skipped = updated = failed = 0

    for f in files:
        if f.name in ("BP Characters.md",):
            continue

        text = f.read_text(encoding="utf-8")

        # Only process files that have a ## Notes section but lack bullet 1
        if "## Notes" not in text:
            skipped += 1
            continue
        if has_graphemic_bullet(text):
            skipped += 1
            continue

        fm = read_frontmatter(text)
        # Derive character from filename
        char = f.stem.replace(" (char)", "")

        total += 1
        ok = process_char(char, write, canonical, variants, verbose=True)
        if ok:
            updated += 1
        else:
            failed += 1

        time.sleep(0.5)  # be polite to Wiktionary

    print(f"\nDone. {total} processed, {updated} {'written' if write else 'proposed'}, "
          f"{failed} failed, {skipped} skipped.")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="Scrape Wiktionary graphemic data for Dan'a'yo character pages."
    )
    ap.add_argument("chars", nargs="*",
                    help="Character(s) to process (e.g. 儒 詩)")
    ap.add_argument("--write", action="store_true",
                    help="Write the graphemic bullet to the character file "
                         "(default: dry run)")
    ap.add_argument("--batch", action="store_true",
                    help="Process all characters missing a graphemic bullet")
    args = ap.parse_args()

    if not args.chars and not args.batch:
        ap.print_help()
        sys.exit(1)

    print("Building radical map…")
    canonical, variants = build_radical_map()
    print(f"  {len(canonical)} canonical radicals, {len(variants)} variants loaded.")

    if args.batch:
        batch(args.write, canonical, variants)
    else:
        for char in args.chars:
            process_char(char, args.write, canonical, variants)

    if not args.write:
        print("\n(Dry run — pass --write to update files.)")


if __name__ == "__main__":
    main()
