---
name: checklist-radicals
description: Completion rubric for Radical lookup pages — stroke-grouped inventory of every character under one Kangxi radical
metadata:
  type: checklist
---

# Checklist: Radical Pages

A radical page is a complete inventory of every 漢字 classified under one Kangxi radical. The goal is to function as a lookup table: given a radical, a reader can find any character. There are **two accepted page styles**, chosen by `size`:

- **`size >= 20`** — the **grouped** style: a `## Strokes` section split into `### +N Stroke(s)` subsections, so a reader can find a character by counting strokes added beyond the radical. Required at this size because a flat list of 20+ entries stops being scannable.
- **`size < 20`** — either the grouped style, or the **prosaic** style: a `## Characters` section (not split by stroke count) preceded by a real encyclopedic description — what the radical depicts, its etymology, notable compounds — modeled on `Radical 212.md` (龍). Below `size` 20, splitting by stroke count usually produces several `### +N Strokes` headers holding exactly one entry each, which clutters more than it helps.

Both styles are fully documented below. Neither is a shortcut: a bare numbered list with no description is incomplete under *either* style — see "Common mistakes."

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

Immediately after the frontmatter, a breadcrumb linking to `Radicals`, then a description. How much description depends on the style. Use `[[Radicals]]` or `[Radicals](Radicals.md)` — both are valid.

**Grouped-style pages** get one short line: what the radical represents, any alternate forms it takes inside characters, and its SKIP position if notable.

```markdown
> [[Radicals]]
> Radical 1 is 一, the number one.
```
```markdown
> [[Radicals]]
> The water radical, appearing as 氵on the left side of the character (SKIP-1-3-x).
```

**Prosaic-style pages** get a real encyclopedic passage — several sentences to a few paragraphs — covering what the character depicts, its etymology, and anything notable about how it functions in compounds (e.g. as a phonetic complement). See `Radical 212.md` for the model: it covers the dragon radical's origin as a stylized drawing, its cross-CJKV zodiac/mythology sense, and a worked example of it supplying sound rather than meaning in 聾. A one-line description on a `size < 20` page is not sufficient to count as prosaic style — see "Common mistakes."

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

Present **only if the radical character itself is a standalone entry in `characters/`** — i.e. some character file's `radical:` field matches this radical's own value, at the radical's own `stroke_count`. When it is, it's entry 1, anchoring the numbering.

When the radical symbol is *not* used as a standalone character in the corpus — common for component-only radicals such as 儿, 冫, 宀, 彳, 艸 — there is nothing to put at +0. Don't invent a placeholder entry. Skip straight to the lowest stroke count that has a real entry, and say so explicitly in the opening description line so a reader (and a future lint pass) can tell this is deliberate rather than an oversight:

```markdown
> [[Radicals]]
> Radical 10 is 儿, legs/a walking person, 2 strokes; appears as the bottom component of characters. No character is filed at +0, so groupings below start at +1.
```

### Negative-stroke groups (rare)

Occasionally a character classified under a radical has *fewer* strokes than the radical's own baseline — this happens when a simplified or component variant of the radical is the one actually used for classification, while a character with fewer strokes than that variant still exists. Confirmed case: 才 (3 strokes) is filed under 手 (hand, 4 strokes), so `Radical 064.md` has a `### -1 Stroke` group. Verify against the character's own `stroke_count` field before assuming a negative heading is a typo — it can be correct. Negative groups follow the same continuous-numbering rules as any other group and sort before `+0`/`+1`.

### Numbered entries — character format

Each character that Dan'a'yo uses gets a numbered entry with a ruby-annotated link and an English gloss:

```markdown
N. <ruby>[X](../../characters/X%20(char).md)<rt>注音</rt></ruby> - english gloss
```

- Use the `(char)` suffix in the link path when the character file has it.
- The `rt` content is the Dan'a'yo 注音 pronunciation.
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

## Prosaic style *(alternative to Strokes section, `size < 20` only)*

Instead of `## Strokes`, a `## Characters` section. No stroke-count subsections — just the encyclopedic opening (see "Opening" above) doing the explanatory work instead.

```markdown
## Characters
### Used
1. <ruby>[[丸]]<rt>ㄏ⺢ㄋ</rt></ruby> - round
2. <ruby>[[丹]]<rt>ㄉㄚㄋ</rt></ruby> - cinnabar

### Aliases
- 丼 --> 井

### Forbidden
- 丷 --> Korean 구결 for '하다'

### Other
- [叉](../../characters/叉%20(char).md) has a 'dot' in it, but isn't listed under this radical.
```

- **`### Used`** — required. Numbered entries, same ruby + gloss format as the grouped style (see "Numbered entries — character format" below), just not split by stroke count. Numbering still counts toward `size`.
- **`### Aliases`** *(optional, include if any exist)* — alternate/ancient/simplified written forms that redirect to a proper character, same `-->` convention as grouped-style aliases. (`Radical 212.md` uses the older heading name `### Variants` for this — equivalent, but `### Aliases` is the name to use going forward, for consistency with the grouped style's own vocabulary.)
- **`### Forbidden`** *(optional, include if any exist)* — glyphs that resemble 漢字 but aren't standard, or are forbidden in Dan'a'yo, **each with a short reason**, not just the label "forbidden" — e.g. "obscure C character, forbidden in Dan'a'yo" or "(obsolete) vista of a dragon in flight, forbidden," not a bare `- 龓 --> forbidden`. (`Radical 212.md` calls this `### Illegal` — same older-naming note as above.)
- **`### Other`** *(optional, include if any exist)* — see "Other section" below; works identically in both styles, just nested as a `###` subsection here instead of a standalone `##` section.

A prosaic-style page with only `### Used` and no prose in the opening is a bare list wearing the wrong heading — see "Common mistakes."

---

## Other section *(optional, both styles)*

Some characters visually contain a radical as a component, but the *language's actual etymology* — how Dan'a'yo derives the character — classifies them under a *different* radical (their `radical:` frontmatter field, and their real `## Strokes`/`### Used` entry, both stay on that other page; nothing about their official classification changes). When a character's own page discusses this visual component in its etymology and links out to `[[Radical NNN]]` for the component radical, that link should be **reciprocated** here, so a reader browsing the component radical isn't left wondering why an obviously-related character is missing.

Worked example: 叉 (char)'s real radical is 又 (radical 29, "hand"), and its own page is what belongs under `Radical 029.md`'s `### Used`. But 叉 also visually contains 丶 (a dot stroke), so its etymology section links to `[[Radical 003]]`. Radical 3's page reciprocates that link under its own `### Other`:

```markdown
### Other
- [叉](../../characters/叉%20(char).md) has a 'dot' in it, but isn't listed under this radical.
```

In grouped-style pages this is a standalone `## Other` section (after `## Strokes`, before `## Data check`); in prosaic-style pages it's a `### Other` subsection alongside `### Used`/`### Aliases`/`### Forbidden`.

```markdown
### Other
- [孔 (char)](../../characters/孔%20(char).md)
- 肇 has this radical as a component, but is not listed under this radical.
- While not filed under this radical, [舜](../../characters/舜.md) has it as a top component.
```

Use a brief note explaining *why* the character appears here (it looks like it belongs, but doesn't). Plain character names or linked character files are both acceptable. Entries here never count toward `size`, on either style.

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

Set when, for **grouped-style** pages:

1. All three frontmatter fields are filled in.
2. Every character returned by the data check query has a numbered entry in the correct `+N Strokes` group.
3. No character in the numbered list is absent from the data check results.
4. All known aliases and forbidden glyphs for this radical are listed.
5. `size` matches the actual count of numbered entries.

Set when, for **prosaic-style** pages:

1. All three frontmatter fields are filled in.
2. The opening is a real encyclopedic passage (see "Opening"), not a one-line description.
3. Every character returned by the data check query has a numbered entry under `### Used`.
4. No character in the numbered list is absent from the data check results.
5. All known variants and forbidden glyphs for this radical are listed under `### Aliases` / `### Forbidden`, each forbidden entry with a reason.
6. `size` matches the actual count of numbered entries under `### Used`.

---

## Common mistakes

- **Flat comma-separated list** — some older pages list all characters in one block without ruby annotation at all. These need to be converted to a proper format regardless of style.
- **Bare numbered list mistaken for prosaic style** — a `size < 20` page with just a breadcrumb, one-line description, and a flat numbered list is *not* a finished prosaic page — it's missing the encyclopedic opening and the `### Used`/`### Aliases`/`### Forbidden`/`### Other` structure. `Radical 212.md` and `Radical 003.md` are the bar; a list alone doesn't clear it. (Confirmed instances needing this upgrade: `Radical 134.md`, `Radical 194.md`.)
- **Flat/bare list on a `size >= 20` page** — at this size, prosaic style isn't an option at all; it must be converted to the full grouped `+N Strokes` format. (Confirmed instances: `Radical 044.md`, `Radical 053.md`, `Radical 060.md`, `Radical 104.md`, `Radical 116.md`, `Radical 196.md`.)
- **No `+0 Strokes` group when one is warranted (grouped style only)** — if the radical itself has a standalone entry in `characters/`, it must appear as entry 1; omitting it breaks the continuous numbering and the completeness check. But check `characters/` first: if the radical symbol isn't a standalone character in the corpus, a missing `+0` is *correct*, not a bug — see above. Don't flag every `+0`-less page uniformly; confirm against the corpus per page. Not applicable to prosaic-style pages, which have no `+N` groups at all.
- **Renumbering per group** — entries are numbered continuously across all groups, not restarted at 1 for each stroke count.
- **Counting aliases in `size`** — only numbered entries count; aliases, forbidden, and Others do not.
- **`date-last-perfect` with no character list** — a page that has only a data check query and no curated list is not done, regardless of frontmatter.
- **Heading variants** — use `## Data check` consistently, not `## Data search`, `## Dataview`, or `### Data double check`.
- **Breadcrumb as plain link** — `[[Radicals]]` and `[Radicals](Radicals.md)` are both valid; do not convert one to the other as a cleanup pass.
