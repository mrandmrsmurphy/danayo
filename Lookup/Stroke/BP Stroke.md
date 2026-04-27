---
language: English
tags:
  - lookup
  - best-practice
---

# Best Practices: Stroke Pages

A stroke page is a complete, SKIP-grouped inventory of every 漢字 in Danayo with a given total stroke count. The goal is to function as a lookup table: given a stroke count, a reader can find any character by its SKIP shape code.

---

## Frontmatter

Three fields, all required:

```yaml
---
stroke_count: 3              # integer — the stroke count this page covers
date-last-perfect: YYYY-MM-DD   # leave blank until the page is complete
size: 39                     # count of character entries in ### In Use only
---
```

**`stroke_count`** must be an integer (not a string) and must match the filename (e.g. `Stroke 03.md` → `stroke_count: 3`).

**`size`** counts only characters listed under `### In Use`. Aliases, forbidden entries, and redirect notes do not count.

**`date-last-perfect`** is left blank until all criteria below are met.

---

## Opening

Immediately after the frontmatter, one line:

```markdown
> [[Stroke]]
```

The breadcrumb uses the wiki-link form `[[Stroke]]`.

---

## Characters section

The main body is a `## Characters` section with two subsections.

### `### In Use`

An unordered list, one line per SKIP code, of every character at this stroke count that Danayo uses. SKIP codes are listed in ascending order — first by the first digit (1 before 2 before 3 before 4), then by the second digit, then the third.

The format for each line:

```markdown
- SKIP-code: <ruby>[[Char (char)|Char]]<rt>注音</rt></ruby>, <ruby>[[Char2]]<rt>注音</rt></ruby>
```

- The SKIP code is written as three hyphen-separated numbers (e.g. `1-1-2`), not linked.
- Each character uses a ruby-annotated wiki-link. Use the `(char)` pipe alias form when the character file has that suffix: `[[小 (char)|小]]`. For files without the suffix: `[[刃]]`.
- The `rt` content is the Danayo 注音 pronunciation.
- Multiple characters sharing the same SKIP code appear on one line, separated by commas.

Full example for a 2-stroke page:

```markdown
## Characters
### In Use
- 1-1-1: <ruby>[[八 (char)|八]]<rt>ㄅㄚㄊ</rt></ruby>
- 2-1-1: <ruby>[[二 (char)|二]]<rt>ㄋㄧㄜ</rt></ruby>
- 3-1-1: <ruby>[[乃 (char)|乃]]<rt>ㄋㄚㄧ</rt></ruby>, <ruby>[[匕]]<rt>ㄆㄧㄜ</rt></ruby>, <ruby>[[刀]]<rt>ㄊㄚㄨ</rt></ruby>
- 4-2-1: <ruby>[[丁 (char)|丁]]<rt>ㄉㄝㄫ</rt></ruby>, <ruby>[[又 (char)|又]]<rt>ㄨㄛ</rt></ruby>
- 4-2-2: <ruby>[[七 (char)|七]]<rt>ㄑㄧㄊ</rt></ruby>
- 4-2-3: <ruby>[[十]]<rt>ㄙㄧㄆ</rt></ruby>
- 4-2-4: <ruby>[[乂]]<rt>⼘ㄧ</rt></ruby>, <ruby>[[九 (char)|九]]<rt>ㄎ⼜</rt></ruby>, <ruby>[[人 (char)|人]]<rt>ㄋㄧㄋ</rt></ruby>, <ruby>[[入 (char)|入]]<rt>ㄋㄧㄆ</rt></ruby>, <ruby>[[力 (char)|力]]<rt>ㄌㄧㄎ</rt></ruby>
```

### `### Aliases`

An unordered list of glyphs at this stroke count that are not full Danayo characters: ancient variants, component-only forms, stroke symbols, etc. These are plain text — no links, no ruby. Use `-->` to indicate what a glyph redirects to:

```markdown
### Aliases
- 丨
- 廾 --> variant of 共
```

### `### Forbidden` *(optional)*

If any glyphs at this stroke count resemble 漢字 but are not — Korean 口訣 marks, phonetic symbols, Chữ Nôm inventions — list them here:

```markdown
### Forbidden
- 乜 - Cantonese/dialects only
```

Omit this subsection entirely if there are no forbidden entries.

---

## Data check

The final section. A `dataview` query returning every character with this stroke count, used to verify the `### In Use` list is complete:

```markdown
## Data check
​```dataview
TABLE file.link AS "Character", 注音 AS "Sound", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "3" OR stroke_count = 3
SORT skip_number ASC
​```
```

The heading is always `## Data check`. The `OR stroke_count = N` clause (unquoted integer) handles both quoted and unquoted YAML values across the database. Sort by `skip_number ASC` to match the order of the `### In Use` list.

---

## `date-last-perfect` criteria

Set when:

1. All three frontmatter fields are filled in.
2. Every character returned by the data check query appears in `### In Use` under its correct SKIP code.
3. No character in `### In Use` is absent from the data check results.
4. Every `### In Use` entry has a ruby-annotated link.
5. All known aliases and forbidden glyphs at this stroke count are listed.
6. `size` matches the actual count of characters in `### In Use`.

---

## Common mistakes

- **Plain wiki-links without ruby** — every `### In Use` entry must have `<ruby>...<rt>注音</rt></ruby>`; bare `[[Char]]` links or comma-separated plain text are incomplete.
- **Adding glosses** — stroke pages do not include English glosses; ruby pronunciation only.
- **SKIP codes out of order** — sort ascending: first digit first, then second, then third.
- **One line per character instead of one line per SKIP code** — characters sharing a SKIP code belong on a single comma-separated line.
- **Counting aliases in `size`** — only `### In Use` entries count toward `size`.
- **`stroke_count` as a string** — use an integer (`3`, not `"3"`).
- **Missing `OR stroke_count = N`** — the data check query needs both the quoted and unquoted form to catch all records regardless of how the frontmatter was entered.
- **`## Data search` heading** — always use `## Data check`, not `## Data search` or `### Data check`.
