#!/usr/bin/env python3
"""Regenerate AIOS/facts.yaml (the vault's front door for outside agents).

Run from anywhere: python3 AIOS/scripts/build_facts.py
Counts come from `git ls-files -z` (never find; NUL-split so non-ASCII names survive).
Note: new untracked files are not counted until `git add`ed.
"""
import datetime
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def ls(folder):
    out = subprocess.run(["git", "ls-files", "-z", folder], cwd=ROOT,
                         capture_output=True, check=True).stdout.decode("utf-8")
    return [p for p in out.split("\0") if p]


def md(folder, pred=lambda name: True):
    return [p for p in ls(folder) if p.endswith(".md") and pred(Path(p).name)]


characters = md("characters")
words = md("words")
syllables = md("syllables")
chengyu = md("chengyu")
lessons = md("lessons", lambda n: re.fullmatch(r"Lesson \d+\.md", n) is not None)
grammar_en = md("grammar", lambda n: n.endswith(".en.md") and n.startswith("文法 - "))
lexipedia = md("lexipedia")

lines = f"""# Machine-readable vault facts for outside agents. Regenerate: AIOS/scripts/build_facts.py
vault: danayo
language: Dan'a'yo (単亜語)
hub: README.md
counts:
  characters: {len(characters)}  # characters/*.md; `X (char).md` files are characters, not words
  words: {len(words)}  # words/*.md, includes affix pages and single-character words
  syllables: {len(syllables)}  # includes the Syllables.md index
  chengyu: {len(chengyu)}  # includes the grouping pages
  lexipedia_pages: {len(lexipedia)}
progress:
  lessons_written: {len(lessons)}
  lessons_planned: 20
  grammar_chapters_with_english_mirror: {len(grammar_en)}
key_pages:
  grammar_index: grammar/単亜語之文法書.md
  lesson_outline: lessons/lesson-outline.md
  lexipedia_index: lexipedia/Lexipedia.md
  swadesh: lexipedia/Swadesh.md
  vault_structure: AIOS/vault-structure.md
  memory_index: AIOS/memory-index.md
source_record: none
generated: {datetime.date.today().isoformat()}
"""
(ROOT / "AIOS" / "facts.yaml").write_text(lines, encoding="utf-8")
print(lines)
