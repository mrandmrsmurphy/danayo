---
name: feedback-english-field-format
description: The english field in word/character frontmatter must be a YAML list, not a semicolon-separated string
type: feedback
---

Always format the `english` field in frontmatter (words, characters, chengyu) as a YAML list, never as a semicolon-separated string.

**Why:** The field is queried as data in Obsidian Bases. Semicolon-separated strings break queries and require manual cleanup.

**How to apply:** Use list format with comma separation or block-list style. Never use semicolons.

```yaml
# ✗ wrong
english: axe; hatchet

# ✓ correct
english: [axe, hatchet]

# ✓ also correct (linter may reformat to this — both are valid)
english:
  - axe
  - hatchet
```

Single-value fields can remain as a plain string. This applies to all word files, chengyu files, character files, and any other frontmatter `english` field across the vault.
