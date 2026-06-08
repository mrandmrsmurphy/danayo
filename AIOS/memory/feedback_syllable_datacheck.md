---
name: feedback-syllable-datacheck
description: Broken syllable data check queries (matching on 諺文 instead of 注音) silently hide characters that belong on the page — always grep all characters by 注音 before trusting the listed entries
type: feedback
---

When fixing a syllable page, the data check block is often broken — querying `WHERE 諺文 = "X"` instead of `WHERE 注音 = "X"`. This means characters whose 諺文 differs from the syllable's 諺文 (e.g. because they share the same sound but have a different Hangul representation) are invisible in Obsidian's live query and were never added to the hand-curated list.

**Why:** Discovered on ㄅㄚㄫ — 旁 had `注音: ㄅㄚㄫ` but was missing from the page entirely because the old `WHERE 諺文 = "방"` query never surfaced it.

**How to apply:** When fixing any syllable page, always run a bash grep for all characters with that 注音 value and cross-reference against the listed entries — don't trust the page's existing list as complete. The fixed query (`WHERE 注音 = "ㄙㄜ"` etc.) is the authoritative check.
