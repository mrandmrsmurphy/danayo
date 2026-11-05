---
name: project-alias-protocol-issues
description: Trouble hit while rolling out the ## Aliases section on character pages; for the user's morning review
metadata:
  type: project
---

# Alias protocol issues (for morning review)

## 2026-11-05 — 零 (char): alias 〇 has no SKIP, radical or stroke home — RESOLVED 2026-11-05

Resolution (user): treat 〇 as 1 stroke, SKIP 4-1-4 (guessed), "has no radical"; redirects on Stroke 01 and SKIP-4-1-4 only. The linter skips the radical redirect when the subsection says "has no radical"; the checklist says so. 零 is stamped.

零 lists the alias 〇 (U+3007, the ideographic zero). 〇 is a CJK symbol, not a Han character: Wiktionary has no Han-character entry for it (no radical, no stroke count), EDRDG has no SKIP code, and it has no rank in the Classical Chinese lists. So the three required redirects (Stroke page, SKIP leaf, Radical page) and the SKIP/stroke figures have nowhere to go. 零 was **not stamped**; its Notes, Words and Derived Characters are otherwise checked and unchanged.

Options: (a) treat 〇 as 1 stroke with SKIP 4-1-4 and a "no radical" note, and put the redirect on Stroke 01 and SKIP-4-1-4 only; (b) allow a non-Han alias to skip the three redirects and say so in its subsection; (c) drop 〇 from `aliases:` and mention it only in Notes. The linter's C4 check would need to match whichever you choose.

## 2026-11-05 — 冪: vault stroke count and SKIP disagree with EDRDG (and with its own phonetic 幕) — RESOLVED 2026-11-05

Resolution (user): follow EDRDG. 冪 is now 15 strokes, SKIP 2-2-13; moved off Stroke 16 and SKIP-2-2-14 onto Stroke 15 and SKIP-2-2-13, Radical 014 group renamed +13. Alias 幂 added (Radical 050, SKIP 2-9-3 guessed, 12 strokes). 冪 is stamped.

冪 (character page) has `stroke_count: 16` and `skip_number: 2-2-14`. EDRDG gives **15 strokes and SKIP 2-2-13**; Wiktionary gives 16 (it counts the traditional 14-stroke 幕). The vault's own 幕 (char) has `stroke_count: 13`, so 冖 (2) + 幕 (13) = 15 is the vault-consistent figure. The Character Creation skill says SKIP comes from EDRDG. Fixing it would move 冪 from Stroke 16 to Stroke 15 and from SKIP-2-2-14 to SKIP-2-2-13 (leaf sizes, SKIP-2-2 index, lint counts), so I did not change it. 冪 was **not stamped**.

The alias 幂 (simplified; Wiktionary: 12 strokes, radical 巾, ⿱冖旲巾 / ⿱𠖇巾; EDRDG has no entry) could not have its `## Aliases` subsection finished until this is decided: its SKIP would be 2-2-… depending on the reading of its parts, and its strokes/radical differ from 冪's (Radical 050 巾, not 014 冖).

Question for the morning: follow EDRDG (15 strokes, 2-2-13) for 冪, or keep Wiktionary's 16? The same split may recur for other characters whose phonetic has a Japanese-form stroke count lower than the traditional one.
