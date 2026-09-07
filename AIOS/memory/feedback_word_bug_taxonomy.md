---
name: feedback-word-bug-taxonomy
description: recurring bug classes found across the alphabetical word-perfecting sweep, and how to check for each
metadata:
  type: feedback
---

The alphabetical [[AIOS/projects.md|word-perfecting sweep]] surfaces the same handful of bug shapes repeatedly. Two are genuinely distinct checks, not one:

**1. Internal-reading bugs** — a compound's own `羅馬字`/`諺文`/`注音` should be the exact concatenation of each constituent's own stored values (see [[feedback_word_pronunciation_derivation]]). When one of the three fields disagrees with the constituent characters while the other two match, that's the bug, not evidence of a sound-shift rule — the field that stayed correct across many prior fixes has usually been `注音`, but not always (e.g. `肋骨` had a wrong `羅馬字` with `諺文`/`注音` already correct). Common shape: voicing or place-of-articulation confusion (p/f, k/g, t/d) on a single syllable, sometimes cascading across every compound built on the same mis-transcribed character until the character-level source is fixed.

**2. Cross-linguistic-field bugs** — a different check entirely, applied to the *real*-language fields (`cantonese`/`japanese`/`korean`/`vietnamese`), which are NOT always simple concatenation (real compounds can have fused/irregular readings, e.g. Japanese rendaku or gemination). Found this sweep:
- A native gloss substituted for the compositional Sino reading (e.g. `与 (char)`'s own `vietnamese` field held và/với, the native words for "and"/"with", instead of the real Sino-Vietnamese reading dữ/dự).
- An unrelated word's real reading copied in by mistake (e.g. 肉桂's korean held 계피, the reading for the unrelated compound 桂皮, not 肉桂's own compositional 육계).
- Garbled or wrong-language text (e.g. 質問's cantonese held "zhíwèn", Mandarin-pinyin-shaped text, not real Cantonese).
- A spurious extra reading fabricated via a nonexistent variant (e.g. 質素's mandarin had a comma-joined second form "zhísù" — 質 has no zhí reading at all).

**How to apply:** when perfecting a word, run both checks independently. For cross-linguistic fields, don't assume "matches convention" is enough — verify the syllables actually correspond to each constituent's own stored reading in that language, and be alert that a **constituent character's own page** can carry the wrong real-language reading (found on `characters/買.md` and `characters/与 (char).md` this sweep) — worth fixing in passing when caught, not just the word under perfection.

**Structural bugs to check for on every pass**: missing `kwin` field entirely; empty-string fields (`hsk_level: ""`); the literal string `"null"` (quoted or unquoted) where a real value belongs; comma-joined values that should be YAML lists; a `characters:` entry citing a bare redlink (e.g. `赤`) instead of the real filename (`赤 (char)`); stray cantonese spacing — the established convention this sweep is **no space** between jyutping syllables in a compound field (`zat1man6`, not `zat1 man6`); a `pos` that contradicts the word's plainly verbal/adjectival English gloss and a constituent's own `pos` (fix to match the constituent, e.g. 賭博/起伏/起床 all had `性詞` corrected to `事詞` for verbal glosses).

Constituent character pages inherited from old batches sometimes have structurally malformed `## Words`/`## Chengyu` sections — orphaned CC-lookup wikilinks dangling mid-list (belongs in Notes prose), or ordinary compound words mislabeled under a `## Chengyu` heading instead of `## Words`. Same "old batch, worse format" pattern already documented for the Stroke/Chengyu/Syllables lints — fix in passing when a word-perfecting pass touches that character page anyway.
