---
name: feedback_variant_word_check
description: before creating a word, check whether it already exists under a shinjitai/traditional variant spelling of one of its characters
metadata:
  type: feedback
---

Before writing a new word file, check `words/` for the same compound spelled with a variant (shinjitai/traditional/simplified) form of either constituent character — not just whether the character itself exists. E.g. 每週 vs 毎週 (每 is an alias of 毎): I built and wrote a full 每週.md, only to find `words/毎週.md` already existed with nearly identical content, requiring a delete-and-merge cleanup.

**Why:** [[feedback_variant_character_check]] already covers checking a character's own `aliases:` list before concluding a *character* is missing — but that check doesn't automatically catch the word level, since a word can be searched/linked under either spelling. Same root cause, different layer.

**How to apply:** Before creating word X-Y, glob/grep `words/` for the compound spelled with any alias of X or Y (check each constituent character's `aliases:` field first). If a variant-spelled word file already exists, don't create a duplicate — instead add the searched-for spelling to that file's `aliases:` field and resolve the broken link to point at the canonical (alias-free) spelling.
