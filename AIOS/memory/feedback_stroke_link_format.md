---
name: feedback-stroke-link-format
description: Stroke lookup page links always use two-digit zero-padded numbers (Stroke 02, not Stroke 2)
type: feedback
---

Stroke lookup page filenames and display text always use two-digit zero-padded numbers.

**Why:** Consistent alphabetical sort in the filesystem and in Obsidian's link resolver. "Stroke 2" would not resolve to the correct page.

**How to apply:** In Notes bullet 2 of every character page, write `[Stroke 02](lookup/Stroke/Stroke%2002.md)` — never `Stroke 2`. Applies to all single-digit stroke counts (01 through 09). The same zero-padding convention applies to Radical lookup files, but to 3 digits (`Radical 085.md`, not `Radical 85`).
