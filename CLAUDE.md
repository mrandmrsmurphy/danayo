# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An **Obsidian vault** for *単亜語* (Dan'a'yo), a constructed zonal auxiliary language for the East Asian cultural sphere (Mandarin, Cantonese, Japanese, Korean, Vietnamese). There is no build system — all content is Markdown with YAML frontmatter, queried and displayed by Obsidian plugins.

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
- [[characters/BP Characters.md]]
- [[words/BP Words.md]]

## Skills

Step-by-step guides for the complicated tasks that I've been coaching Claude on how to do live in `AIOS/skills/`, indexed at [[AIOS/skill-index.md]]:
- [[AIOS/skills/skill_word_creation.md|Word creation]] - for making a new word in `words/`
- [[AIOS/skills/skill_character_creation.md|Character creation]] - for making a new character in `characters/`
- [[AIOS/skills/skill_mediawiki_migration.md|MediaWiki migration]] - for comparing conlang.org wiki pages against vault content

## Persistence

**All durable memory lives inside this vault, in `AIOS/` ("AI Operating System") — never in the external `~/.claude/projects/.../memory/` location.**

That external location isn't backed up the way this git-tracked vault is, and isn't portable across machines — anything written there can be lost between sessions or left behind on a new one. `AIOS/` is the canonical home for everything meant to survive: standing knowledge of the user, feedback on collaboration style, ongoing-project status, and workflow skills.

Structure:
- **`AIOS/memory-index.md`** — index of standing memories: who the user is, feedback/corrections on how to work here, pointers to external systems. **Read this at the start of every session.**
- **`AIOS/memory/`** — individual files: `user_*.md` (who Robert is, how he thinks), `feedback_*.md` (corrections and confirmations — lead with the rule, then `**Why:**` and `**How to apply:**`), `reference_*.md` (pointers to external systems)
- **`AIOS/skill-index.md`** — index of step-by-step workflow guides; read the relevant skill in full before starting that kind of work
- **`AIOS/skills/`** — individual `skill_*.md` guides
- **`AIOS/projects.md`** — living status document for ongoing work; read at the start of every session to see what's active and where to resume
- **`AIOS/projects/`** — deeper history for individual projects, as `project_*.md` files linked from `projects.md`

When you discover something valuable for future sessions — architectural decisions, gotchas, corrections, project status changes — write it into the appropriate `AIOS/` file and index it. Don't wait to be asked, and don't wait for the session to end.

## License

Code/tooling: MIT. Content: CC BY-SA.
