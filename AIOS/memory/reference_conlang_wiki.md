---
name: reference-conlang-wiki
description: danayo.conlang.org is the legacy MediaWiki site being migrated into this vault — source of pre-Obsidian character data
type: reference
---

`danayo.conlang.org` is a MediaWiki site that predates this Obsidian vault. It holds older character data (sometimes more complete in places — prose notes, compounds, components, aliases — sometimes corrupted or stale in others, e.g. wrong-language native glosses).

**Purpose of the migration:** pull every still-valuable piece of data into the vault, then the user deletes the wiki pages himself once a character is confirmed complete. See [[skill_mediawiki_migration]] for the full workflow and what does/doesn't get imported.

**Access:** the site has a self-signed cert — WebFetch fails; use `curl -sk` via Bash. Two template formats exist on the wiki (`Infobox_字` newer, `Dan'a'yo_Character` older).
