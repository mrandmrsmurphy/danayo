---
name: feedback-character-inclusion-philosophy
description: Rules of thumb for deciding whether a marginal character gets its own entry, becomes an alias on a phonetic parent, or qualifies for 名 (naming) grade
type: feedback
---

See also [[Character Inclusion Philosophy]] (vault root) for the full statistical rubric — grade-level thresholds, the 借代字 inclusion checklist, and the long-tail inclusion-pressure table. This memory captures the narrower judgment calls that came up in practice, which the rubric doesn't fully spell out.

**Alias as stand-in:** when a character is too narrow to justify a full entry but still needs "no recourse" coverage for names, add it as an alias on its phonetic parent rather than creating a new character file — provided the two are phonetically identical across all CJKV languages.

**Why:** keeps the database from bloating with near-duplicates while still giving every name-character a path into the system. The alias is cleanest when the parent is *both* phonetic and semantic source (寄 [布 ← 佈] is cleaner than 蒔 ← 時, where 時 is only phonetic, not semantic, parent of 蒔).

**How to apply:** before aliasing, confirm identical Dan'a'yo-relevant readings across Mandarin/Cantonese/Japanese/Korean/Vietnamese — examples: 蒔 (Jinmeiyō-only, 艹+時) → alias on 時; 佈 (traditional 布, names-only outside China, 亻+布) → alias on 布. See also [[feedback_session_pacing]]'s sibling project notes on alias judgment calls (legitimate aliasing requires both matching sound *and* a transparent meaning link — bad cases get reverted, e.g. 歇≠欠).

---

**The "no recourse" argument for 名 grade:** a character that appears in personal names across the CJKV sphere, with no substitutable form in Dan'a'yo, qualifies for `grade_level: 名` and `stand_in: 名専字` even when it fails ordinary vocabulary-grade criteria.

**Why:** Dan'a'yo needs to be able to render real names; a character can be indispensable for that purpose while being useless for general vocabulary. Korean Name-lookup presence is a direct signal that a character lives in this space.

**How to apply:** when a character fails HSK/Jōyō/vocabulary thresholds but turns up in the Korean Name lookup (or equivalent name indexes for other languages), default to 名 + `名専字` rather than excluding it.

---

**Semantic divergence across CJKV doesn't block 名 inclusion, only productive-vocabulary grades.** Example: 舅 means "maternal uncle" in Chinese/Vietnamese but "father-in-law" in Japanese — that mismatch disqualifies it from a shared-meaning vocabulary grade, but not from 名.

**Why:** 名-grade characters only need to render correctly in names, where the semantic-drift problem doesn't arise the same way it would in shared vocabulary.

**How to apply:** don't let cross-linguistic meaning mismatches talk you out of a 名 entry — check separately whether the *naming* use case is solid.

---

**Lopsided language presence (strong in some branches, absent in others) argues for 名 over 先進**, even when the character's HSK level looks low. Example: 址 has strong Chinese/Vietnamese presence but no real Japanese/Korean vocabulary footprint.

**Why:** 先進 (advanced vocabulary) implies the character pulls its weight across the whole CJKV sphere; a character that's productive in only two of the five branches is better classified by its narrower (naming) role.

**How to apply:** when assessing grade, weigh cross-linguistic *breadth* of vocabulary use, not just the strength of presence in any single language's frequency lists.
