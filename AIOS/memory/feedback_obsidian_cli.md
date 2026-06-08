---
name: feedback-obsidian-cli
description: Use the Obsidian CLI for character and word property lookups instead of grep — cleaner, path-independent, wikilink-style name resolution
type: feedback
---

Use the `obsidian` CLI (at `/usr/local/bin/obsidian`) for property lookups, not `grep`. Always pass `vault=danayo`.

- **All properties for a file**: `obsidian properties file="謄" vault=danayo` — returns full frontmatter, resolves by wikilink name (no path needed, handles `(char)` suffix automatically)
- **Single property**: `obsidian property:read name=注音 file="謄録" vault=danayo` — returns just the value, clean for word 注音 lookups
- **Finding characters by 注音**: still use `grep` — `obsidian search` treats `:` as an operator and fails on property queries like `注音: ㄉㄝㄊ`

**Why:** CLI is cleaner, path-independent, and resolves wikilink names automatically. grep/Read are slower and path-dependent.

**How to apply:**
- **Word 注音 lookups**: always `obsidian property:read name=注音 file="WORD" vault=danayo`, never grep
- **Character frontmatter**: always `obsidian properties file="CHAR" vault=danayo`, never grep
- **Body content** (Words/Notes sections): still use `Read` — CLI only returns frontmatter
- **Finding characters by 注音**: still use `grep` — obsidian search can't filter on the 注音 property
- **Finding vault files**: still use `find` — CLI has no file-discovery command
