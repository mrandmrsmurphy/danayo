---
name: feedback-translation-kanbun-origin
description: Why old translation/ pages (道徳経, 論語) have reversed word order and stray ㄹ characters — trust current vault data, not the legacy text order
metadata:
  type: feedback
---

Many pages in `translation/` (e.g. `道徳経 (book).md`, `論語 (book) - 01学而.md`) were originally transcribed from a vertical calligraphy piece where 武明帥 invented a kind of kanbun (漢文訓読-style reading order) for Dan'a'yo. Converting that back to normal horizontal Dan'a'yo word order lost a lot of the original ordering, which is why so many old translation lines have:
- **Word order reversed** from the real vault word (e.g. 友朋 instead of [[朋友]], 常恒 instead of [[恒常]], 犯侵 instead of [[侵犯]], 本根 instead of [[根本]], 生出 instead of [[出生]])
- **Stray ㄹ characters** sprinkled in — leftover kanbun-style reading-order/return marks that never got cleaned up in the transcription

**Why:** these pages predate the current word-pronunciation-derivation convention ([[feedback_word_pronunciation_derivation]]) and were typed by hand from a calligraphy source using a different reading-order system entirely.

**How to apply:** when cleaning up an old `translation/` page — don't try to preserve or make sense of the legacy word order or the ㄹ marks. Strip stray ㄹ's outright. When a multi-character sequence in the old text isn't a real vault word, check the reversed order before concluding it's broken — it's very often the real word written backwards. Always rebuild ruby/bopomofo from current `characters/`/`words/` data, never from the old hangul (which is also frequently just wrong/outdated, separate from the ordering issue).
