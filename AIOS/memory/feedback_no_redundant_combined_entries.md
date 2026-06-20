---
name: feedback-no-redundant-combined-entries
description: before creating an N-character word, check whether it decomposes into two already-real (or independently real) shorter words — if so, link two words, don't create one combined entry
metadata:
  type: feedback
---

Before creating a multi-character word, check whether it's just the transparent composition of two shorter words that are each independently real (attested in a dictionary on their own, not just as part of the longer string). If so, link the two existing/creatable words side by side (`[[A]][[B]]`) rather than creating a third combined entry for the whole string — even if the whole string is also individually attestable in a dictionary.

**Why:** Caught twice in the same project. First with 対外戦争 ("foreign war"): created it as its own word, then the user said "delete it, it is just two words" ([[対外]]+[[戦争]], both already real). Then, instead of learning the lesson proactively, I repeated it with 行政区域 ("administrative region"): created it as its own 4-character word, and the user immediately asked "Isn't 行政区域 just two separate words?" — 行政 ("administration") is itself a basic, independently real word across all 5 languages, and [[区域]] already existed in the vault; the 4-character form was just their plain combination, not an independently lexicalized unit needing its own entry.

**How to apply:**
- For any 3+ character candidate, split it into plausible sub-words and check each sub-word's own dictionary attestation *before* checking the whole string's attestation.
- If every sub-word is independently real/creatable on its own, default to linking them separately (`[[A]][[B]]`), not creating the combined form — regardless of whether the combined form also happens to have its own dictionary entry.
- The bar for creating the combined form as its own entry is that it carries meaning, idiom, or fixed usage beyond plain composition (e.g. [[太平]][[洋]] was *not* combined, but a fully idiomatic/non-transparent compound would be) — see [[feedback_idiom_component_attestation]] for the inverse case (when a *short* candidate fails standalone attestation but is still real as part of something longer).
- When in doubt, create the missing shorter sub-word first, then decide.
