---
language: English
---

# Best Practices: Syllable Pages

A syllable page documents one phonological unit of 単亜語, linking it to all characters that carry that sound and establishing which character is the *stand-in* (the primary Danayo word for that syllable).

---

## Frontmatter

All six fields are required. `date-last-perfect` stays blank until the page is fully done.

```yaml
---
date-last-perfect: YYYY-MM-DD   # leave blank until the page is complete
size: 7                          # total number of character entries in the Characters section
羅馬字: dan                       # Danayo romanisation
諺文: 단                          # Hangul representation
注音: ㄉㄚㄋ                       # Bopomofo (matches the filename)
english:                         # meaning(s) of the stand-in character(s)
  - altar
  - only
tags:
  - syllable
---
```

**`size`** is the count of all character entries (Common + Advanced + Naming combined). Update it whenever entries are added or removed.

**`english`** lists the meanings of the stand-in character(s) — i.e., the word(s) Danayo actually uses for this syllable. If there is no stand-in, use `ø`.

**`aliases`** may be added for the romanisation and Hangul so they are searchable by those strings.

---

## Intro block

Immediately after the frontmatter, write a short intro block. The canonical form is a blockquote with all three scripts, then the primary meaning, citing the stand-in character in parentheses:

```markdown
> [[Syllables]]
> **·ㄚ/아/'a** means "I/me" (我) or "ah" (阿)
```

- List multiple meanings with "or" when there are multiple stand-in characters.
- If there is no stand-in at all, write: `> **ㄆㄨㄆ** has no intrinsic meaning.`
- If the syllable only appears in a secondary role, explain briefly.

### Audio (optional)

If an audio file exists in `/images/`, add it on the line after the meaning line:

```markdown
> ![a](/images/ㄚ.m4a)
```

Audio files are hard to source; omit this line rather than leave a broken link.

---

## Characters section

Replace the auto-generated `dataviewjs` block entirely with a hand-curated numbered (or bulleted) list. Organize entries into three subsections:

```markdown
## Characters
### Common
### Advanced
### Naming
```

### Common

Characters that can be used as standalone Danayo words at the primary level. These have a `stand_in` value in their frontmatter.

Entry format — link the character file, quote the meaning, then link to the word file with `-->`:

```markdown
1. [[壇 (char)]] "altar" --> [[壇]]
2. [[但 (char)]] "only, but" --> [[但]]
```

Use the `[[X (char)]]` wiki-link form when the character file uses the `(char)` naming convention. The word link after `-->` is the plain `[[X]]` wiki-link (or `[[X|displayText]]` if needed).

### Advanced

Characters that exist in Danayo but only inside compound words — they cannot stand alone. Use a `but requires` clause with a ruby-annotated compound link:

```markdown
3. [[誕]] "be born", but requires <ruby>[[誕生]]<rt>ㄉㄚㄋㄙㄚㄫ</rt></ruby>
4. [[蛋]] "egg white", but requires [[蛋白]]
```

Include the ruby annotation whenever the compound's pronunciation is non-obvious. Omit it for very short or obvious compounds.

### Naming

Characters that only appear in proper names or are otherwise unavailable as Danayo vocabulary. Two sub-cases:

```markdown
5. [[簞]] "bamboo basket", but it's a 名専字
6. [[岡]] "hill", but requires <ruby>[[山岡]]<rt>ㄙㄚㄋㄍㄚㄫ</rt></ruby>
```

Use **名専字** for characters that are restricted to names. Characters that technically require a compound but also belong to this category can note both.

---

## Data check block

End every page with a `dataview` block that queries characters by 諺文:

```markdown
## Data check
​```dataview
TABLE file.link AS "Character", 注音 AS "Sound", grade_level AS "Grade"
FROM "characters"
WHERE 注音 = "ㄙㄚ"
SORT file.name ASC
​```
```

This serves as a live sanity check: every character that appears in the table should have a corresponding entry in the Characters section, and vice versa.

---

## What "done" means

Set `date-last-perfect` when all of the following are true:

1. All frontmatter fields are filled in.
2. The intro line is complete (meaning stated, stand-in cited).
3. Every character returned by the data-check query has a curated entry (no `dataviewjs` placeholder remains).
4. Each entry is correctly categorised as Common, Advanced, or Naming.
5. Every compound in a `but requires` clause has been verified to exist as a word.
6. `size` matches the actual count of entries.

---

## Common mistakes to avoid

- **Leaving the `dataviewjs` block** — auto-generated pages use it as a placeholder. A completed page replaces it with the hand-curated list.
- **Wrong `size`** — recount entries whenever the section changes.
- **Blank `english` on a page with a stand-in** — if a character has `stand_in`, its meaning belongs in `english`.
- **Missing `(char)` suffix in links** — character files are named `X (char).md`; use `[[X (char)]]`, not `[[X]]`, unless the file genuinely lacks the suffix.
- **Broken compound links** — verify that linked word files actually exist before marking a page perfect.
