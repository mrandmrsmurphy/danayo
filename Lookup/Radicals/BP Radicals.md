---
language: English
tags:
  - lookup
  - best-practice
---

# Best Practices: Radical Pages

A radical page is a complete, stroke-grouped inventory of every 漢字 classified under one Kangxi radical. The goal is to function as a lookup table: given a radical, a reader can find any character by counting the strokes added beyond the radical itself.

---

## Frontmatter

Three fields, all required:

```yaml
---
date-last-perfect: YYYY-MM-DD   # leave blank until the page is complete
size: 20                         # count of numbered character entries only
radical: 一                      # the radical character itself (matches the radical field in character frontmatter)
---
```

**`size`** counts only the numbered entries in the stroke-group lists. Aliases, forbidden entries, and Others do not count toward `size`.

**`radical`** must match exactly the string used in character frontmatter `radical:` fields, since the data check queries on it.

---

## Opening

Immediately after the frontmatter, two lines:

```markdown
> [[Radicals]]
> Brief description of the radical — what it depicts or means.
```

The breadcrumb uses the wiki-link form `[[Radicals]]`. The description is one short phrase: what the radical represents, any alternate forms it takes inside characters, and its SKIP position if notable.

Examples:
```markdown
> [[Radicals]]
> Radical 1 is 一, the number one.
```
```markdown
> [[Radicals]]
> The water radical, appearing as 氵on the left side of the character (SKIP-1-3-x).
```

---

## Strokes section

The main body is a single `## Strokes` section containing `### +N Stroke(s)` subsections, one per stroke count. "Strokes" here means strokes added *beyond* the radical itself.

```markdown
## Strokes

### +0 Strokes
1. <ruby>[一](../../characters/一%20(char).md)<rt>·ㄧㄊ</rt></ruby> - one

### +1 Stroke
2. <ruby>[丁](../../characters/丁%20(char).md)<rt>ㄉㄝㄫ</rt></ruby> - fourth
3. <ruby>[七](../../characters/七%20(char).md)<rt>ㄑㄧㄊ</rt></ruby> - seven
- 丂 --> ancient variant of 于 and of 考
- 丄 --> ancient variant of 上

### +2 Strokes
4. <ruby>[万](../../characters/万.md)<rt>ㄇㄛㄋ</rt></ruby> - ten-thousand
...
```

### The `+0 Strokes` subsection

Always present. Contains exactly one entry: the radical character itself, listed as entry 1. This anchors the numbering.

### Numbered entries — character format

Each character that Danayo uses gets a numbered entry with a ruby-annotated link and an English gloss:

```markdown
N. <ruby>[X](../../characters/X%20(char).md)<rt>注音</rt></ruby> - english gloss
```

- Use the `(char)` suffix in the link path when the character file has it.
- The `rt` content is the Danayo 注音 pronunciation.
- The English gloss should be brief — one to four words.
- Numbering is continuous across all `+N` subsections; do not restart at 1 for each group.

### Non-numbered entries within stroke groups

Three types of entries appear as unnumbered bullets inside stroke groups, mixed in with the numbered ones:

**Aliases** — alternate written forms that redirect to a proper character. Use `-->`:
```markdown
- 丌 --> ancient variant of 其
- 书 --> ancient variant of 書
```

**Forbidden** — glyphs that resemble 漢字 but are not: Korean 口訣 marks, phonetic symbols, Chữ Nôm inventions, etc.:
```markdown
- 丷 --> Korean 구결 for '하다'
- forbidden 㐃
```

**违法字** — characters that appear in some databases (e.g. HSK) but are not recognized internationally as standard 漢字. Mark with `¡ !` and bold label:
```markdown
* ¡丟/丢! - **違法字** - HSK/1 but not internationally known.
```

Omit stroke-count groups entirely if they contain only non-numbered entries; or include them with a closing note explaining the absence of proper characters.

A closing note is appropriate when a large swath of high-stroke entries is empty:
```markdown
*All other forms are missing from dictionary or are chữ Nôm inventions.*
```

---

## Other section *(optional)*

If there are characters that visually contain the radical as a component but are officially classified under a *different* radical, list them here. These represent incoming links that a reader might expect to find on this page.

```markdown
### Other
- [孔 (char)](../../characters/孔%20(char).md)
- 肇 has this radical as a component, but is not listed under this radical.
- While not filed under this radical, [舜](../../characters/舜.md) has it as a top component.
```

Use a brief note explaining *why* the character appears here (it looks like it belongs, but doesn't). Plain character names or linked character files are both acceptable.

---

## Data check

The final section. A `dataview` query that returns every character whose `radical` field matches this radical, sorted by stroke count. This lets you verify that the numbered list is complete and that no characters are missing or misfiled.

```markdown
## Data check
​```dataview
TABLE 注音 AS "Sound", english AS "EN"
FROM "characters"
WHERE radical = "一"
SORT stroke_count ASC
​```
```

The heading is always `## Data check`. Sort by `stroke_count ASC` to match the stroke-group order of the body.

When a radical has multiple written forms (e.g. 丿 / 乀 / 乁), query all of them:
```markdown
WHERE radical = "丿" OR radical = "乀" OR radical = "乁"
```

---

## `date-last-perfect` criteria

Set when:

1. All three frontmatter fields are filled in.
2. Every character returned by the data check query has a numbered entry in the correct `+N Strokes` group.
3. No character in the numbered list is absent from the data check results.
4. All known aliases and forbidden glyphs for this radical are listed.
5. `size` matches the actual count of numbered entries.

---

## Common mistakes

- **Flat comma-separated list** — some older pages list all characters in one block without stroke grouping or ruby annotation. These need to be converted to the full grouped format.
- **No `+0 Strokes` group** — the radical itself must appear as entry 1; omitting it breaks the continuous numbering and the completeness check.
- **Renumbering per group** — entries are numbered continuously across all groups, not restarted at 1 for each stroke count.
- **Counting aliases in `size`** — only numbered entries count; aliases, forbidden, and Others do not.
- **`date-last-perfect` with no character list** — a page that has only a data check query and no curated list is not done, regardless of frontmatter.
- **Heading variants** — use `## Data check` consistently, not `## Data search`, `## Dataview`, or `### Data double check`.
- **Breadcrumb as plain link** — prefer `[[Radicals]]` wiki-link over `[Radicals](Radicals.md)` markdown link for consistency with the rest of the vault.
