---
name: vault-structure
description: What the Dan'a'yo vault is, how it's organized, plugin setup, frontmatter schemas, ruby-text syntax, and the .base databases. Read when working with vault content or structure.
type: reference
---

## What this is

An **Obsidian vault** for *単亜語* (Dan'a'yo), a constructed zonal auxiliary language for the East Asian cultural sphere (Mandarin, Cantonese, Japanese, Korean, Vietnamese). There is no build system — all content is Markdown with YAML frontmatter, queried and displayed by Obsidian plugins.

## Setup

Open the folder as a vault in Obsidian. Required plugins to enable:
- Core: **Bases**, **Dataview**, **Graph View**, **Templates**
- Community (install via Obsidian): **Templater**, **meta-bind**, **obsidian-furigana**, **obsidian-git**, **metaedit**

Note: the shared Obsidian settings (`app.json`, `appearance.json`, `core-plugins.json`, `community-plugins.json`, `types.json`, `templates.json` and `snippets/`) are tracked in the repo. Per-user state (`workspace.json`, plugin folders, themes) is gitignored, so install the community plugins listed in `community-plugins.json` yourself.

## Data model

Content is organized into four atomic entry types, all linked:

- **`characters/`** — one file per character, and only characters — none of these files is a word (e.g. `一 (char).md`, whose word counterpart is `words/一.md`), with cross-linguistic pronunciation, stroke/radical/SKIP metadata, grade levels across HSK/Jōyō/Korean edu systems, and danayo_id
- **`words/`** — multi-character compound words; frontmatter lists `characters:` (constituent parts), pronunciation across all five languages, `pos:`, and `注音:` (Bopomofo)
- **`chengyu/`** — idiomatic set phrases with similar structure to words
- **`syllables/`** — individual phonetic units represented in Bopomofo

Supporting content:
- **`grammar/`** — chapters of the grammar book (`文法 - 01序文.md` through chapter 97); `単亜語之文法書.md` is the index
- **`lexipedia/`** — semantic field groupings (Animals, Body, Numbers, Swadesh list, etc.), indexed from `lexipedia/Lexipedia.md`. Beyond indexing existing words, this is where Dan'a'yo's own semantic ranges get worked out as the language differentiates itself from its CJKV sources — distinct from word-page Notes, which survey the *source-language* landscape. See `AIOS/memory/feedback_lexipedia_semantic_differentiation.md`. Domain pages follow a standard tiered template (Core A1–A2, Intermediate B1–B2, Advanced C1+, plus Semantic Range Notes and See Also, with `status: new | stub | partial | complete` and `date-last-perfect` frontmatter fields) — see `AIOS/checklists/checklist_lexipedia.md` for the full completion rubric before creating or expanding a domain page.
- **`lessons/`** — a graded course curriculum for learners, built out of the vault's other content (phonology → characters → grammar → discourse). `lessons/lesson-outline.md` is the master syllabus (20 lessons across 5 tiers); individual `Lesson NN.md` files hold the worked lesson content as it's written, cross-linked back to `grammar/`, `characters/`, and `lexipedia/` pages. Prompted by the gap analysis in `AIOS/memory/analysis_documentation_sufficiency_2026_09_13.md` (reference use well-covered; learner use was not).
- **`lookup/`** — indexes into `characters/` by Radicals, SKIP, stroke count, HSK level, Jōyō level, Korean education level

## File naming in `characters/`

A character file is named either `X.md` or `X (char).md`. The distinction is intentional and determines how the character is linked:

- **`X (char).md`** — the character can also function as a stand-alone Dan'a'yo word, so `words/X.md` exists (`X.md` is reserved for the word file). The file in `characters/` is still the character, never the word. The `(char)` suffix prevents the character file from colliding with the word file of the same name. Link as `[[X (char)]]` or `[X (char)](../characters/X%20(char).md)`.
- **`X.md`** — the character is bound-only; it does not appear as a stand-alone word. Link as `[[X]]` or `[X](../characters/X.md)`.
  - A bound character that is a **fully productive affix** also stays `X.md`: its affix word is `words/－X.md` (suffix) or `words/X－.md` (prefix), using the fullwidth hyphen U+FF0D, so there is no collision and no `(char)` suffix is needed. A **semi-productive** affix has no affix word, only a note on the character page. See [[AIOS/memory/feedback_affix_naming_and_productivity.md]].

When writing `characters:` frontmatter for words, use the form that matches the actual filename: `X (char)` or plain `X`.

## Link formats

Both Obsidian wiki-links and relative Markdown links are valid throughout the vault:

- Wiki-link: `[[Syllables]]`, `[[壇 (char)]]`, `[[詩篇]]`
- Markdown link: `[Syllables](syllables/Syllables.md)`, `[壇 (char)](../characters/壇%20(char).md)`, `[詩篇](../words/詩篇.md)`

Do not convert existing Markdown links into wiki-links as a cleanup pass. Markdown links are desirable because the vault is also browsed on GitHub, where wiki-links do not resolve. When adding new links, match the surrounding page's style or use Markdown links for GitHub compatibility.

## Frontmatter conventions

**Character** frontmatter fields (all present on every entry):
```
mandarin, cantonese, korean, korean_native, japanese, japanese_native, vietnamese
middle_chinese_initial, middle_chinese_final
stroke_count, radical, skip_number
grade_level, joyo_level, hsk_level, hanmun_edu_level
pos, english, 羅馬字, 諺文, 注音
danayo_id, mc_id, graphemic_classification, stand_in
date-last-perfect
tags: [character]
```

**Word** frontmatter fields:
```
characters, 羅馬字, 諺文, mandarin, cantonese, korean, japanese, vietnamese, pos, 品詞, english, 注音
```

## Creating new entries

Use the Templater templates in `templates/` — they prompt for all required fields interactively:
- `character-template.md` → new character entry
- `word-template.md` → new word entry
- `chengyu-template.md` → new idiom entry

The `nav/char_info.md`, `nav/word_info.md`, and `nav/chengyu_info.md` files are meta-bind dashboards that display metadata for the currently active note — they are not content pages.

For the full step-by-step process (not just template invocation), see [[AIOS/skill-index.md]].

## Ruby text

Throughout the vault, ruby text (furigana) uses HTML syntax rendered by the obsidian-furigana plugin:
```html
<ruby>単亜語<rt>ㄉㄚㄋ·ㄚ⼄</rt></ruby>
```

## Databases

The `.base` files are Obsidian Bases databases for querying entries:
- `characters/Char base.base`
- `words/Words Base.base`
- `chengyu/All Chengyu Base.base`
- `Last Perfect.base` — tracks `date-last-perfect` for spaced repetition review

**Front door for outside agents:** [`AIOS/facts.yaml`](facts.yaml) holds machine-readable counts and key-page paths (reportage protocol shared with the UL and middle-semitic vaults). Regenerate with `python3 AIOS/scripts/build_facts.py` after any work that changes the numbers; don't recompute or quote counts from prose.

## Current state (as of 2026-10-24)

Counts drift; recompute with `git ls-files <folder> | grep -c '\.md$'` (use `git ls-files`, not `find`, because the vault is iCloud-synced and a plain walk can hang).

| Folder | `.md` files | Notes |
|---|---|---|
| `characters/` | ~3,370 | Characters only, no words. ~1,030 are `X (char).md` (have a same-name word). |
| `words/` | ~6,530 | All vocabulary. Includes the affix words `－X.md` / `X－.md`. |
| `chengyu/` | 241 | 238 idiom pages + 3 grouping pages (`Misc.`, `Dan'a'yo`, `Biblical Chengyu`). |
| `syllables/` | 902 | 901 syllable pages + `Syllables.md`. |

**Perfection status:** every file in all four folders carries `date-last-perfect` (no unperfected backlog). Chengyu citations were verified against their named sources in a 2026-10 sweep; roughly half of the earlier citations had been wrong and were fixed.

**Grammar** (`grammar/`): 単亜語之文法書 chapters 01–05 have English mirrors (`.en.md`); 06 語用 (pragmatics) is a short skeleton (~3 KB vs ~18 KB for chapters 04/05) and has no English mirror. 91–99 are appendices (source-language booklets, parts of speech, forbidden characters, 韻図).

**Lessons** (`lessons/`): `lesson-outline.md` plans 20 lessons; only Lesson 01–03 are written. Reference use of the vault is well covered; learner-facing material is the open frontier. The planned reader will be part of the lessons: once they're complete, it becomes a roadmap for advanced learners through `translation/` (not started) (see `AIOS/memory/analysis_documentation_sufficiency_2026_09_13.md`: ~85% sufficient for scholars, ~40% for learners).

**Other content:** `lexipedia/` (64 files, incl. the `Swadesh.md` comparative table: Old Chinese, Mandarin, Cantonese, Japanese, Korean, Vietnamese, Dan'a'yo); `translation/` (Analects, Zhuangzi, Dao De Jing, Art of War, Shijing, etc.; many fragmentary); `bible/` (partial); `lookup/` (CC initials/finals, Radicals, SKIP, Stroke, HSK, Japanese, Korean, Grade pages, and `List of …` pages).

**Tooling** (`AIOS/scripts/`): 7 report-only linters (`lint_cc`, `lint_chengyu`, `lint_chengyu_groups`, `lint_radicals`, `lint_skip`, `lint_stroke`, `lint_syllables`) plus `build_grade.py`, which rebuilds `lookup/Grade N.md`. There is no linter for `characters/` or `words/` pages; those are judged against `AIOS/checklists/`.
