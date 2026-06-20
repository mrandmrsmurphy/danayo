---
name: feedback-variant-character-check
description: before declaring a character "missing" and blocking a word, check whether an existing character file already covers it via aliases (shinjitai/traditional variant glyphs)
metadata:
  type: feedback
---

Before concluding a candidate word is blocked because one of its constituent characters "doesn't exist in the vault," check whether an existing character file already covers it as a variant glyph, listed in that file's `aliases:` field — not just an exact filename match.

**Why:** During the Geography.md sweep, 北冰洋/南冰洋 (Arctic/Southern Ocean) were skipped as blocked on a "missing" character 冰. In fact `characters/氷.md` already exists and lists `冰` as an alias (氷 is simply the Japanese shinjitai glyph for the same character as traditional 冰). The user caught this directly: "Isn't it just 氷 in Dan'a'yo?" The words were real and well-attested all along (Mandarin 北冰洋/南冰洋, Japanese 北氷洋/南氷洋, Korean 북빙양/남빙양, Vietnamese Bắc Băng Dương/Nam Băng Dương) — created as `北氷洋`/`南氷洋` using the vault's actual shinjitai filename.

**How to apply:** When a word-creation candidate seems blocked by a "missing" character, grep `characters/*.md` for that character appearing in any `aliases:` list before concluding it needs full character creation. This is especially likely for 氷/冰, 国/國, and other shinjitai/traditional pairs where the vault's base script (Japanese shinjitai, per `CLAUDE.md`) uses the simplified glyph as the primary file and files the traditional form as an alias.
