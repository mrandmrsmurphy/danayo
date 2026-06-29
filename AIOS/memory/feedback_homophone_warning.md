---
name: feedback-homophone-warning
description: Words with Dan'a'yo homophones must have a [!warning] callout
metadata:
  type: feedback
---

When a word has Dan'a'yo homophones, include a `>[!warning] Homophones` callout block immediately after the meta-bind-embed block and before `## Notes`.

**Why:** The original body text on these words had the homophone note as plain prose, which was lost when the Notes were rewritten. The user expects a visible callout, not a buried mention in paragraph text.

**How to apply:** Format as:
```
>[!warning] Homophones
> [[WordA]] gloss — [[WordB]] gloss
```
List each homophone with its short English gloss, separated by em-dashes.
