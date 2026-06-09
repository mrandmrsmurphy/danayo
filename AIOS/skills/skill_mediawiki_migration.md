---
name: skill-mediawiki-migration
description: Checklist for migrating a character from danayo.conlang.org MediaWiki to the Obsidian vault, and verifying the vault version is complete
type: skill
---

# Skill: MediaWiki Migration (conlang.org → Obsidian vault)

Goal: get everything valuable off danayo.conlang.org so those pages can be deleted. See [[reference_conlang_wiki]].

## Workflow

1. User names a character.
2. Run `find .../characters -name "CHAR*"` and `curl` the wiki page in parallel.
3. Present a comparison table of discrepancies.
4. User says what to import (often "all", "both", "yes", or names specific fields).
5. Apply approved edits. Say "Done. Next?"

## Checklist per character

1. **Open vault file** — `find characters -name "X*"` (run from the vault root; may be `X.md` or `X (char).md`); read it fully.
2. **Fetch wiki page** — `curl -sk "http://danayo.conlang.org/w/index.php?title=URL_ENCODED_CHAR&action=view" | sed 's/<[^>]*>//g' | grep -v '^[[:space:]]*$' | grep -A200 "Jump to navigation" | head -100`
3. **Compare** — produce a side-by-side table of discrepancies and flag wiki-only data (prose notes, compounds, aliases, components).
4. **Ask** — present findings and ask what to import.
5. **Apply** — make the approved edits.
6. **Move on** — user deletes wiki pages themselves; just present the next character when asked.

## URL pattern

- `http://danayo.conlang.org/w/index.php?title=CHAR&action=view`
- URL-encode non-ASCII: e.g. 矢 → `%E7%9F%A2`
- WebFetch fails (self-signed cert) — always use curl via Bash.
- Two wiki template formats exist: newer `Infobox_字` and older `Dan'a'yo_Character`. Both work with the same curl+sed approach, but the older one has messier output.

## Nearly universal fixes (apply unless vault already correct)

- **`# Notes` → `## Notes`** — almost every character needs this; do it automatically when present.
- **`pos: ""`** — fill from wiki using POS mapping below.
- **Components** — wiki's Components field is almost always worth importing as `- Components: [[X]], [[Y]]` bullet in Notes.
- **Empty `joyo_level`/`hanmun_edu_level`/`hsk_level`** — fill from wiki when vault field is blank.
- **Missing aliases** — import aliases in wiki but not vault.

## POS mapping (wiki → vault)

| Wiki | Vault |
|---|---|
| noun | 名詞 |
| verb | 事詞 |
| adjective | 性詞 |
| 自動詞 | 事詞 |
| 他動詞 | 事詞 |
| classifier | 量詞 |
| adverb | 副詞 |
| postposition | 後置詞 |
| SFP / exclamatory | 感詞 |
| conjunction | 連接詞 |

## What the user almost always imports

- `pos` — nearly always imported (see mapping above)
- `components` — nearly always imported; add as `- Components: [[X]], [[Y]]` bullet in Notes
- `joyo_level` when vault field is blank
- `aliases` when wiki has ones the vault is missing
- Prose/usage notes when they contain grammatical or cultural info not in vault
- Example compounds → `## Words` section (check vault for existing files to add ruby annotations)

## What the user does NOT import

- Phonological discrepancies (`羅馬字`, `諺文`, `注音`) — vault's current phonology is authoritative; linter manages these
- Extra cantonese readings beyond the primary one
- `japanese_native` / `korean_native` differences — usually left as-is unless user asks
- Wiki data that's clearly corrupt or erroneous
- `stand_in` when wiki says 姓名 and vault has 名専字 — vault convention is newer

## Structural fixes to make while editing

- Always fix `# Notes` → `## Notes` if present (wrong heading level per BP)
- CC links (`[[Lookup/CC/initials/…]]`, `[[Lookup/CC/finals/…]]`) floating loose in Notes are a pre-existing issue — flag but don't fix unless asked

## Words section

When adding compounds from the wiki:
- Check if word file exists: `find .../words -name "WORD*"`
- If found: get 注音 and english (`grep "^注音:\|^english:" -A2 file`), add `<ruby>[[WORD]]<rt>注音</rt></ruby> "gloss"`
- If not found: add plain `[[WORD]] "gloss"`

## Other notes

- Do NOT delete wiki pages — user does that themselves after confirming vault is complete.
- Some wiki fields are corrupt (e.g. Korean native showing Vietnamese text) — flag and ignore.
- `mc_id: 0` in vault means character not in CC corpus; leave blank per BP.
- The wiki's `Requires: X` = `stand_in: X` in vault; `This character is special` = standalone word.
- When user says "both" / "all" / "yes" after the table, apply everything listed as **Import**.
- The user names characters one at a time; just say "Done. Next?" after each.
