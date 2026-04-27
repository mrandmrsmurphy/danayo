# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An **Obsidian vault** for *単亜語* (Danayo), a constructed zonal auxiliary language for the East Asian cultural sphere (Mandarin, Cantonese, Japanese, Korean, Vietnamese). There is no build system — all content is Markdown with YAML frontmatter, queried and displayed by Obsidian plugins.

## Setup

Open the folder as a vault in Obsidian. Required plugins to enable:
- Core: **Bases**, **Dataview**, **Graph View**, **Templates**
- Community (install via Obsidian): **Templater**, **meta-bind**, **obsidian-furigana**, **obsidian-git**, **metaedit**

Note: `.obsidian/` is gitignored, so plugin configs are not tracked in the repo.

## Data model

Content is organized into four atomic entry types, all linked:

- **`characters/`** — one file per character (e.g. `一 (char).md`), with cross-linguistic pronunciation, stroke/radical/SKIP metadata, grade levels across HSK/Jōyō/Korean edu systems, and danayo_id
- **`words/`** — multi-character compound words; frontmatter lists `characters:` (constituent parts), pronunciation across all five languages, `pos:`, and `注音:` (Bopomofo)
- **`chengyu/`** — idiomatic set phrases with similar structure to words
- **`syllables/`** — individual phonetic units represented in Bopomofo

Supporting content:
- **`grammar/`** — chapters of the grammar book (`文法 - 01序文.md` through chapter 97); `単亜語之文法書.md` is the index
- **`lexipedia/`** — semantic field groupings (Animals, Body, Numbers, Swadesh list, etc.)
- **`lookup/`** — indexes into `characters/` by Radicals, SKIP, stroke count, HSK level, Jōyō level, Korean education level

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

## Ruby text

Throughout the vault, ruby text (furigana) uses HTML syntax rendered by the obsidian-furigana plugin:
```html
<ruby>単亜語<rt>ㄉㄚㄋ·ㄚ·⼄</rt></ruby>
```

## Databases

The `.base` files are Obsidian Bases databases for querying entries:
- `characters/Char base.base`
- `words/Words Base.base`
- `chengyu/All Chengyu Base.base`
- `Last Perfect.base` — tracks `date-last-perfect` for spaced repetition review

## Best Practices

A growing number of file types have a `best practices` page, which documents the "correct" way to make a page of that kind:
- [[chengyu/BP Chengyu.md]]
- [[lookup/SKIP/BP SKIP.md]]
- [[lookup/Radicals/BP Radicals.md]]
- [[lookup/Stroke/BP Stroke.md]]
- [[syllables/BP syllables.md]]

## License

Code/tooling: MIT. Content: CC BY-SA.
