---
language: English
tags:
  - syllable
  - best-practice
---

# Best Practices: Syllable Pages

A syllable page documents one phonological unit of 単亜語, linking it to all characters that carry that sound and establishing which character is the *stand-alone* (the primary Dan'a'yo word for that syllable).

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
english:                         # meaning(s) of the stand-alone character(s)
  - altar
  - only
tags:
  - syllable
---
```

**`size`** is the count of all character entries (Common + Advanced + Naming combined). Update it whenever entries are added or removed.

**`english`** lists the meanings of the stand-in character(s) — i.e., the word(s) Dan'a'yo actually uses alone for this syllable. If there is no stand-in, use `ø`.

**`諺文`** uses the unusual convention of final-ㅅ for final-u, ㅃ for f, and 어 for `e`. 

---

## Intro block

Immediately after the frontmatter, write a short intro block. The canonical form is a blockquote with all three scripts, then the primary meaning, citing the stand-alone character in parentheses:

```markdown
> [[Syllables]]
> **ㄚ/아/'a** means "I/me" (我) or "ah" (阿)
```

- List multiple meanings with "or" when there are multiple stand-alone characters.
- If there is no stand-alone at all, write: `> **ㄆㄨㄆ** has no intrinsic meaning.`
- If the syllable only appears in a secondary role, explain briefly.

### Audio (optional)

If an audio file exists in `/images/`, add it on the line after the meaning line:

```markdown
> ![a](/images/ㄚ.m4a)
```

Audio files are hard to source; omit this line rather than leave a broken link.

---

## Characters section

Replace the auto-generated `dataviewjs` block entirely with a hand-curated numbered list. Organize entries into three subsections:

```markdown
## Characters
### Common
### Advanced
### Naming
```

### Stand-alone
All characters have a `stand_in` value in their frontmatter.  If it is essentially the same value as the character filename minus ` (char)`, they are stand-alone words.  Their entry format is to link the character file, quote the meaning, then link to the word file with `-->`:

```markdown
1. [[壇 (char)]] "altar" --> [[壇]]
2. [[但 (char)]] "only, but" --> [[但]]
```

Use the `[[X (char)]]` wiki-link form because these character file use the `(char)` naming convention. The word link after `-->` is the plain `[[X]]` wiki-link.

### Bound
Characters that exist in Dan'a'yo but only inside compound words are not stand-alone. Use a `but requires` clause with a ruby-annotated compound link:

```markdown
3. [[誕]] "be born", but requires <ruby>[[誕生]]<rt>ㄉㄚㄋㄙㄚㄫ</rt></ruby>
4. [[蛋]] "egg white", but requires [[蛋白]]
```

Include the ruby annotation whenever the compound's pronunciation's is available.

### Levels
Characters that have a Dan'a'yo `grade_level` of 1-6 are the `common` characters. Characters that have a Dan'a'yo `grade_level` of `先進` are `advanced` characters.  Lastly, there is the `名` or `naming` level.

### Naming
Some Naming Characters only appear in proper names or are otherwise unavailable as Dan'a'yo vocabulary:

```markdown
5. [[簞]] "bamboo basket", but it's a 名専字
6. [[擺]] "pendulum", but it's a 名専字
```

Use **名専字** for characters that are restricted to names. Characters that technically require a compound should note the compound.

---

## Data check block

End every page with a `dataview` block that queries characters by 諺文:

```markdown
## Data check
​```dataview
TABLE english AS "EN", stand_in AS "SI", grade_level AS "Grade"
FROM "characters"
WHERE 注音 = "ㄙㄚ"
SORT grade_level ASC
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
