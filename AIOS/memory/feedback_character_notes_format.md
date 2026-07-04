---
name: feedback-character-notes-format
description: Corrections to the Notes bullet format in character files — syllable link placement, filename convention, and blank mc_id
type: feedback
---

**Syllable link goes only on bullet 3** (MC rank/initial/final line), never on bullet 2 (SKIP/Stroke). Bullet 2 ends after the Stroke link — no em-dash, no syllable.

**Why:** Pronunciation belongs on the phonology line. The [[AIOS/checklists/checklist_characters.md|checklist_characters.md]] bullet-2 example is wrong (it shows a syllable link there); user confirmed bullet 3 is the correct location.

**How to apply:** Bullet 2 format: `[SKIP-X-Y-Z](...) ([Stroke NN](...))` — stop there. Bullet 3 format: `Nth most used... Ancient [initial] + [final] → [syllable](...)`.

---

**`X (char).md` filename only when a `words/X.md` also exists.** Characters with `stand_in: 名専字` have no word file and use plain `X.md`.

**Why:** Obsidian needs unique filenames when both a character page and a word page share the same character name.

**How to apply:** Before naming, check whether a word file for that character exists. 名専字 characters never get the `(char)` suffix.

---

**Characters absent from all CC corpus files (covering ranks 1–4000) leave `mc_id:` blank and `date-last-perfect:` blank.**

**Why:** Guessing a CC rank is worse than leaving it empty; the field documents classical frequency, not modern usage.
