---
language: English
---

# Best Practices: SKIP Pages

SKIP (System of Kanji Indexing by Patterns) assigns every 漢字 a three-number code. These pages exist to look up characters by shape when you don't know the reading. There are two distinct file types — **index files** and **leaf files** — and SKIP-4 has a substantially different internal structure from SKIP-1, -2, and -3.

---

## SKIP code semantics

| Type | First # | Second # | Third # |
|------|---------|----------|---------|
| 1 | left-right split | strokes in **left** half | strokes in **right** half |
| 2 | top-bottom split | strokes in **top** half | strokes in **bottom** half |
| 3 | enclosure | strokes in **surrounding** part | strokes in **enclosed** part |
| 4 | undivided | *(ignored — use 0)* | **total** strokes | subtype (see below) |

SKIP-4 subtypes: **1** = prominent top horizontal line (雨), **2** = prominent bottom horizontal line (白), **3** = prominent vertical line (虫), **4** = none of the above (丼).

---

## File types

Every folder contains two kinds of files.

### Index files — `SKIP-#-#.md`

One per stroke group. Their job is navigation: list which leaf files exist and preview the characters they contain.

**Frontmatter** (minimal):
```yaml
---
date-last-perfect: YYYY-MM-DD
---
```
`size` and `skip_number` are not needed on index files.

**Body structure:**
1. Breadcrumb: `> [SKIP](lookup/SKIP/SKIP.md) : 1` (linking back up to the top-level SKIP.md)
2. One-sentence description of what the middle number represents in this context.
3. Numbered list of leaf files, with characters previewed inline:
   ```markdown
   - [SKIP-1-1-1](lookup/SKIP/SKIP-1/SKIP-1-1-1.md): 八
   - SKIP-1-1-2: 小, 川
   - SKIP/1/1/5 - none
   ```
   List every position; write `none` or `no` for positions with no file.
4. `## Base check` block (Obsidian Bases query filtering to this folder and linking to this file).

### Leaf files — `SKIP-#-#-#.md`

One per unique SKIP code. These are the actual lookup targets.

**Frontmatter:**
```yaml
---
date-last-perfect: YYYY-MM-DD
stroke_count: 20          # total stroke count of characters on this page
size: 3                   # number of character entries (excluding aliases/redirects)
skip_number: 1-10-10      # the full SKIP code as a string
---
```

**Body structure:**
1. Breadcrumb linking back to parent index (see details per type below).
2. Optional orientation note — e.g. `> These are all of [Stroke 20](lookup/Stroke/Stroke 20.md)`.
3. `## Characters` section with the numbered character list.
4. `### Aliases` section (if any).
5. `### Forbidden` section (if any).
6. `## Datacheck` block.

---

## SKIP-1, -2, -3 leaf files

### Breadcrumb

Single parent link:
```
> SKIP : 1 : [1](lookup/SKIP/SKIP-1/SKIP-1-1.md)
```

### Character list

Characters are listed in a numbered list. The canonical entry uses a ruby-annotated link and an English gloss:

```markdown
1. <ruby>[壇](characters/壇%20(char).md)<rt>ㄉㄚㄋ</rt></ruby> - altar
2. <ruby>[競](/characters/競.md)<rt>ㄍ⼶ㄫ</rt></ruby> - compete
```


There is **no** Common / Advanced / Naming subdivision here — that is a syllable-page convention, not a SKIP convention. All characters on a SKIP page are simply in a flat numbered list.

### Aliases section

Characters that redirect here because they are graphic variants or have been reassigned:
```markdown
### Aliases
- 刂 --> Radical 018, from 刀
- 儿 --> 児
```

### Forbidden section

Characters that visually resemble 漢字 but are not — Korean 口訣 marks, phonetic symbols, etc.:
```markdown
### Forbidden
- 丷 --> A Korean 口訣 for '하다'.
```

### Redirect-only entries

If a leaf file exists only to document that a character is a variant of another, the body can be a single redirect line instead of a character list, and `size` should be `0`:
```markdown
埀 --> 垂
```

### Datacheck block

```markdown
## Datacheck
​```dataview
TABLE 注音 AS "Sound", english AS "en"
FROM "characters"
WHERE skip_number = "1-10-10"
SORT file.name ASC
​```
```

The query uses the `skip_number` property (string), which must match the frontmatter exactly. Every character returned by the query should appear in the Characters list, and vice versa.

---

## SKIP-4 — important differences

SKIP-4 is structurally distinct from the others because undivided characters cannot be split into parts. The **second number is the total stroke count** and the **third number is the subtype** (1–4). This creates a two-dimensional grid (strokes × subtype), which is navigated through an extra layer of index files.

### Three file types in SKIP-4

1. **Stroke-count index** — `SKIP-4-#.md` — lists which leaf files exist for that stroke count, linking also to the corresponding subtype overview.
2. **Subtype overview** — `SKIP-4-0-#.md` — surveys all characters of one subtype across all stroke counts. These are the four "type 0" files: SKIP-4-0-1 (top line), SKIP-4-0-2 (bottom line), SKIP-4-0-3 (vertical), SKIP-4-0-4 (other).
3. **Leaf files** — `SKIP-4-#-#.md` — the actual lookup pages, same purpose as in SKIP-1/2/3.

### SKIP-4 leaf breadcrumb — two parent links

Because each leaf belongs to both a stroke-count index and a subtype overview, the breadcrumb links to both:
```
> SKIP : 4 : [10](lookup/SKIP/SKIP-4/SKIP-4-10.md) | [SKIP-4-0-2](lookup/SKIP/SKIP-4/SKIP-4-0-2.md)
```

This double link is what makes the Base check queries work correctly in both index types.

### SKIP-4 stroke-count index (`SKIP-4-#.md`)

Same structure as other index files, but also cross-reference the subtype overview:
```markdown
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 05](lookup/Stroke/Stroke 05.md)

- [SKIP-4-5-1](lookup/SKIP/SKIP-4/SKIP-4-5-1.md): 正, 凹, 瓦 ...
- [SKIP-4-5-2](lookup/SKIP/SKIP-4/SKIP-4-5-2.md): 白, 由, 丘 ...
- [SKIP-4-5-3](lookup/SKIP/SKIP-4/SKIP-4-5-3.md): 禾, 申, 本 ...
- [SKIP-4-5-4](lookup/SKIP/SKIP-4/SKIP-4-5-4.md): 央, 史, 失 ...
```

### SKIP-4 subtype overview (`SKIP-4-0-#.md`)

Lists every character of that subtype, grouped by stroke count, with links to the leaf files. SKIP-4-0-1 uses a table layout to show all top-line characters at a glance. These pages contain **no character links of their own** — they link only to the leaf files. No `skip_number` or `size` in frontmatter.

### SKIP-4 character list (simpler format)

SKIP-4 leaf files use a simpler list than SKIP-1/2/3. Ruby annotation is encouraged where helpful but many entries are plain wiki-links, especially for well-known characters:

```markdown
1. [[正]]
2. [[凹]]
3. <ruby>[疋](/characters/疋.md)<rt>ㄙ⼄</rt></ruby> - bolt of cloth
```

Aliases and redirect notes follow the same convention as in SKIP-1/2/3.

---

## `date-last-perfect` criteria

### Leaf files
Set when:
1. All frontmatter fields are filled in (`stroke_count`, `size`, `skip_number`, `date-last-perfect`).
2. Every character with that SKIP code in the database appears in the Characters list.
3. Every entry in the Characters list has been confirmed to exist in the database (Datacheck returns no surprises).
4. Aliases and Forbidden sections are complete.
5. `size` matches the actual count of character entries.

### Index files
Set when:
1. Every leaf file that exists is linked.
2. Every position without a leaf file is explicitly marked `none` or `no`.
3. The Base check block is in place.

---

## Common mistakes

- **Putting `skip_number` on index files** — only leaf files need it; the datacheck query matches on it.
- **Wrong `stroke_count`** — for SKIP-1/2/3 this is the *total* stroke count of the characters on the page; for SKIP-4 leaf files the same applies.
- **Missing the second breadcrumb in SKIP-4** — every SKIP-4 leaf must link to both its stroke-count index and its subtype overview for Base check to work in both indexes.
- **Using `dataviewjs` instead of `dataview`** — auto-generated pages sometimes drop in a `dataviewjs` placeholder; replace it with the `dataview` query shown above.
- **`size` counting aliases** — aliases and redirects do not count toward `size`; only true character entries do.
- **Leaving positions blank in the index list** — write `none` or `no` explicitly so it's clear the gap is intentional, not an oversight.
