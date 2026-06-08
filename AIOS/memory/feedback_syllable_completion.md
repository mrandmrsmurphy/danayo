---
name: feedback-syllable-completion
description: When creating a stand-in word that unblocks a syllable page, proactively complete the syllable page too — add ruby annotation and set date-last-perfect
type: feedback
---

When a new word is created that serves as a stand-in for a bounded character, immediately also update the relevant syllable page: add the ruby annotation to the character's entry, and set `date-last-perfect` to today if all other entries on the page already resolve.

**Why:** User confirmed this is the expected behaviour — the word creation and syllable completion are one logical unit of work, not two separate tasks.

**How to apply:** After writing a stand-in word file, check whether that word is the last missing compound on its syllable page (cross-reference every entry, not just the one you just fixed — other entries may have been silently resolved by earlier sessions without the ruby annotation being added). If the page is now fully resolved, update the ruby annotation and mark the page perfect (`date-last-perfect: <today>`) in the same pass.
