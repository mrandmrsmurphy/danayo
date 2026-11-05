---
name: project-alias-protocol-issues
description: Trouble hit while rolling out the ## Aliases section on character pages; for the user's morning review
metadata:
  type: project
---

# Alias protocol issues (for morning review)

## 2026-11-05 — 零 (char): alias 〇 has no SKIP, radical or stroke home

零 lists the alias 〇 (U+3007, the ideographic zero). 〇 is a CJK symbol, not a Han character: Wiktionary has no Han-character entry for it (no radical, no stroke count), EDRDG has no SKIP code, and it has no rank in the Classical Chinese lists. So the three required redirects (Stroke page, SKIP leaf, Radical page) and the SKIP/stroke figures have nowhere to go. 零 was **not stamped**; its Notes, Words and Derived Characters are otherwise checked and unchanged.

Options: (a) treat 〇 as 1 stroke with SKIP 4-1-4 and a "no radical" note, and put the redirect on Stroke 01 and SKIP-4-1-4 only; (b) allow a non-Han alias to skip the three redirects and say so in its subsection; (c) drop 〇 from `aliases:` and mention it only in Notes. The linter's C4 check would need to match whichever you choose.
