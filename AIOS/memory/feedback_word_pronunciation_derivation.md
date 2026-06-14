---
name: feedback-word-pronunciation-derivation
description: When perfecting a word's 羅馬字/諺文/注音, verify each component's actual pronunciation (including word-initial sound shifts) rather than concatenating character-page defaults
metadata:
  type: feedback
---

When perfecting a word page, double-check that `羅馬字`/`諺文`/`注音` are correctly *derived* from the component characters' real pronunciations — not just naively pasted from each character's bound-form reading in `characters/`.

**Why:** Found while perfecting `words/蜂巣.md` — its `諺文`/`羅馬字` correctly used 蜂's word-initial form (퐁/pong), matching the standalone word page `words/蜂.md`, but `注音` was left as the bound-character form (ㄈㄛㄫ/fong) from `characters/蜂 (char).md`, creating an internal inconsistency. The vault has systematic word-initial sound shifts (e.g. ㄈ→ㄆ devoicing) that the bound character form doesn't reflect — `words/蜂蜜.md` has the same unfixed bug (퐁밀/pongmid but 注音 still ㄈㄛㄫㄇㄧㄊ).

**How to apply:**
- For each component, check whether a standalone *word* page exists for that character (e.g. `words/蜂.md`) — if so, its `羅馬字`/`諺文`/`注音` reflect the word-initial form and should be used for the first component of a compound, not the `characters/` bound form.
- Verify `羅馬字`, `諺文`, and `注音` all agree with each other after concatenation — a mismatch between them (e.g. 諺文 reflects a sound shift but 注音 doesn't) is a red flag.
- `words/蜂蜜.md` still has this bug (注音 should start ㄆㄛㄫ not ㄈㄛㄫ) — fix when next touched.
