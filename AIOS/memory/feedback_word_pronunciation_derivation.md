---
name: feedback-word-pronunciation-derivation
description: 羅馬字/諺文/注音 for a word are a direct concatenation of component characters' values — don't invent sound-shift rules from an inconsistent word page
metadata:
  type: feedback
---

When perfecting a word's `羅馬字`/`諺文`/`注音`, the correct value is a **direct concatenation of each component character's values from `characters/`** — per `words/BP Words.md`. There is no word-initial devoicing or other sound-shift rule in this conlang.

**Why:** While perfecting `words/蜂巣.md` and `words/蜂蜜.md`, I found `諺文`/`羅馬字` used 퐁/pong (ㄆ) while `注音` used ㄈㄛㄫ (matching `characters/蜂 (char).md`'s fong/뽕/ㄈㄛㄫ). I incorrectly "fixed" `注音` to match 퐁/pong, inventing a sound-shift rule based on `words/蜂.md` (which itself has pong/퐁/ㄆㄛㄫ — inconsistent with the character page). The user corrected me: 蜂 = fong/뽕/ㄈㄛㄫ, so 蜂巣 = fongjau/뽕잣/ㄈㄛㄫㄐㄚㄨ. I reverted and fixed `諺文`/`羅馬字` to fongjau/뽕잣 and fongmid/뽕믿 instead.

**How to apply:**
- Always derive a compound's `羅馬字`/`諺文`/`注音` from `characters/` (the bound/character form), not from another word page — word pages can themselves be unperfected/wrong.
- If a single-character word page (e.g. `words/蜂.md`) disagrees with the corresponding `characters/X (char).md` page, that's a red flag on the *word* page, not evidence of a sound-shift rule. `words/蜂.md` (pong/퐁/ㄆㄛㄫ) still disagrees with `characters/蜂 (char).md` (fong/뽕/ㄈㄛㄫ) — flagged for whenever that word is perfected, but don't change it without checking with the user first.
