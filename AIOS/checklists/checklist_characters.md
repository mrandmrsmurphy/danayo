---
name: checklist-characters
description: Completion rubric for character pages — frontmatter fields, body structure, and the date-last-perfect criteria
metadata:
  type: checklist
---

# Checklist: Character Pages

A character page is the canonical record for one 漢字 in Dan'a'yo: its orthography, pronunciations across all five CJKV languages, graphemic origin, phonological history, and its role in Dan'a'yo words and chengyu. Every page must be self-contained as a reference while also feeding the database via its frontmatter.

---

## Frontmatter

All fields are required unless marked *(optional)*.

```yaml
---
mandarin: shī              # Pinyin with tone marks
cantonese: si1             # Jyutping with tone number
korean: 시                  # Sino-Korean Hangul
korean_native: 시           # Native Korean descriptive gloss
japanese:                  # on-yomi in rōmaji, as a list
  - SHI
japanese_native:           # kun-yomi in hiragana, as a list 
  - うた
vietnamese:                # Sino-Vietnamese reading(s), as a list
  - thi
middle_chinese_initial: ɕ  # IPA symbol for the Middle Chinese initial
middle_chinese_final: ɨ    # IPA symbol for the Middle Chinese final
stroke_count: 13            # integer — total stroke count
radical: 言                 # Kangxi radical name (character only, no number)
skip_number: 1-7-6         # SKIP code as a string, three hyphen-separated integers
grade_level: "2"            # Dan'a'yo grade: "1"–"6", "先進", or "名"
pos: 名詞                   # part of speech: 名詞, 動詞, 性詞, 数詞, etc.
english:                   # English gloss(es), as a list
  - poem
羅馬字: si                  # Dan'a'yo romanisation
諺文: 시                    # Hangul of the Dan'a'yo pronunciation
joyo_level: "3"             # Japanese level — see Level links table below
hsk_level: "2"              # HSK level — see Level links table below
hanmun_edu_level: 中        # K level: 中 (MS), 高等 (HS), 名 (name), or 無 (absent)
danayo_id: 2230             # Dan'a'yo character unique ID (integer)
mc_id: 351                  # Middle Chinese frequency rank 
graphemic_classification: 寺  # phonetic component name (形声) or type name (象形/指事/会意)
stand_in: 詩歌              # character itself, a required compound, or 名専字
aliases:                   # simplified, historical, regional variants
  - 诗
注音: ㄙㄧ                   # Bopomofo pronunciation
date-last-perfect: YYYY-MM-DD  # leave blank until all criteria are met
kwin: true                 # boolean — if "same" as Korean
tags:                      # tag always present
  - character
---
```

### `graphemic_classification`

This single field encodes both the graphemic type and, for 形声 characters, the phonetic component:

| Value | Meaning |
|---|---|
| `象形` | pure pictograph — depicts an object |
| `指事` | ideographic indicator — marks a position or abstraction |
| `会意` (or `會意`) | compound ideograph — components combine to make meaning |
| any character (e.g. `寺`, `工`) | 形声 — value names the **phonetic component** |

Do **not** set this field to `形声`. For 形声 characters, store the phonetic component character.

### `stand_in`

Controls the character's role in Dan'a'yo vocabulary:

- Character's own name (`stand_in: 詩`) — it is a standalone Dan'a'yo word
- A compound (`stand_in: 詩歌`) — it only appears inside that compound, which is the actual word
- `名専字` — restricted to proper names, no standalone Dan'a'yo use

### `mc_id`

The frequency rank in Classical Chinese; 351 means the 351st most-used character in the CC corpus. Used verbatim in the MC rank bullet (see below).

**Policy (2026-07-11): never blank an existing large `mc_id` just because you can't verify it in `lookup/CC/CC 0000–3000.md`.** Those four files only mirror the top ~4000 ranks; a large existing value (e.g. `9813`, `5262`) reflects the character's real long-tail rank from the fuller source ranking this vault was built from, not a fabrication — treat it as trusted ground truth and use it verbatim in the MC bullet, even though you personally can't cross-check it locally. Do not "correct" it to blank.

**`mc_id: 0` is a real, meaningful value** — it means *confirmed not present in the MC usage ranking at all*, not "unknown" and not a placeholder needing a blank. Leave it as `0` and phrase the MC bullet accordingly (e.g. "Not present in the Classical Chinese usage ranking"), rather than treating it as an error to fix.

Blank (no value at all) still means "not yet checked" and is the only state that should ever be filled in or left blank during perfection work — never invent a number, but also never erase one that's already there.

---

## Body structure

```
[disambiguation callout — as needed]
[meta-bind-embed block — required, must be first or directly after callout]
## Notes
## Words
## Chengyu       ← as needed
## Derived Characters  ← as needed
```

### Disambiguation callout *(optional)*

When the character shares its name with a word file, add a callout **before** the meta-bind-embed:

```markdown
>[!tip] This is a page about the character 詩.
>For the word, see [詩](words/詩.md)
```

Use `[!tip]` for standard disambiguation. Use `[!warning]` when there is a restriction or easy confusion (e.g. a homographic radical alias, a character forbidden in Dan'a'yo).

### `meta-bind-embed` block

Place immediately after the callout (or at the top of the body if no callout). Nothing else precedes it.

~~~markdown
```meta-bind-embed
[[nav/char_info]]
```
~~~

---

## `## Notes` section

The Notes section contains exactly four bullets in this fixed order:

```markdown
## Notes
- [graphemic classification]
- [SKIP and Stroke]
- [Middle Chinese rank and phonology]
- [Level links]
```

### Bullet 1 — Graphemic classification

**形声:**
```markdown
- 形声 (OC *hljɯ): semantic [[Radical 149|言]] ("speech") + phonetic [[寺]] (OC *ljɯs) — poetry is a form of language.
```
Include: the Old Chinese reconstruction of the whole character in parentheses; the semantic radical linked to its Radical lookup page with an English gloss in quotes; the phonetic component linked to its character page with its OC reconstruction; a dash-note on the semantic motivation when non-obvious.

**会意:**
```markdown
- 会意 of [[Radical 009|亻]] ("person upright") and [[𠤎]] ("person inverted") — the concept of reversal or transformation.
```
Include: each constituent component linked with English gloss; a dash-note on the resulting compound meaning. If a historical source (e.g. Shuowen) offers a different analysis, note it briefly. **Any component that is itself a Kangxi radical — semantic or not, 形声 or 会意 — links to its Radical lookup page** (`[[Radical NNN|char]]`), the same as the semantic component in a 形声 bullet; only non-radical components (like 𠤎, or a 形声 phonetic component) get a bare `[[char]]` link.

**指事:**
```markdown
- [List of 指事](lookup/List%20of%20指事.md): a short stroke placed *above* a horizontal line marks the concept of "above"; original form 丄.
```
Open with a link to [[lookup/List of 指事]]. Describe what the indicator marks or what the diagram depicts. Note the original or seal-script form when it clarifies the intent.

**象形:**
```markdown
- [List of 象形](lookup/List%20of%20象形.md): depicts a curved plow blade; the original bronze-script form shows the curve more clearly.
```
Open with a link to [[lookup/List of 象形]]. Describe what the character depicts, referencing seal-script or oracle-bone forms. For uncertain origins lead with "uncertain" and give the prevailing scholarly interpretation.

**This radical-linking rule applies to every bullet type, not just 会意** — if the character's own `radical` frontmatter value (or any depicted/named component) is itself a Kangxi radical, link it as `[[Radical NNN|char]]` wherever it's mentioned in the graphemic bullet, including 指事 and 象形 descriptions. Don't just describe the depicted shape in prose without linking the radical it corresponds to.

---

### Bullet 2 — SKIP and Stroke

```markdown
- [SKIP-1-7-6](lookup/SKIP/SKIP-1/SKIP-1-7-6.md) ([Stroke 13](lookup/Stroke/Stroke%2013.md))
```

Two links in sequence: the SKIP leaf page and the Stroke count page. No syllable link here — the syllable belongs on bullet 3.

---

### Bullet 3 — Middle Chinese rank and phonology

```markdown
- 351st most used character in Classical Chinese. Ancient [[Lookup/CC/initials/聲 書|ɕ]] + [[Lookup/CC/finals/韻 之|ɨ]] → [ㄙㄧ](syllables/ㄙㄧ.md)
```

Format: ordinal rank from `mc_id` + "most used character in Classical Chinese." Then `Ancient` followed by the CC initial link and CC final link — use the IPA symbol as the display text via the pipe alias. Close with `→` and the Dan'a'yo syllable link.

The `[[Lookup/CC/initials/…]]` and `[[Lookup/CC/finals/…]]` links live **here**, embedded in this bullet. They must not float at the bottom of the file.

---

### Bullet 4 — Level links

```markdown
- [Grade 2](lookup/Grade%202.md), [Old HSK 2](lookup/HSK/Old%20HSK%202.md), [Jōyō - Kyōiku](lookup/Japanese/Jōyō%20-%20Kyōiku.md), [Korean MS](lookup/Korean/Korean%20MS.md)
```

List all four levels in order: Dan'a'yo grade, HSK, Jōyō, Korean. Include all four — use the "absent" file when a level is missing.

**Level file mapping:**

| Field | Value | Link |
|---|---|---|
| `grade_level` | `"1"`–`"6"` | `[[Grade N]]` |
| `grade_level` | `"名"` | `[[Grade Name]]` |
| `hsk_level` | `"1"` | `[[lookup/HSK/HSK Beginner]]` |
| `hsk_level` | `"2"`–`"6"` | `[[lookup/HSK/Old HSK N]]` |
| `hsk_level` | `"無"` | `[[lookup/HSK/HSK No]]` |
| `joyo_level` | `"1"`–`"6"` | `[[lookup/Japanese/Jōyō - Kyōiku]]` |
| `joyo_level` | `高等` | `[[lookup/Japanese/Jōyō - Kōtō]]` |
| `joyo_level` | `表外字` | `[[lookup/Japanese/Hyōgai]]` |
| `joyo_level` | `日本人名用漢字` | `[[lookup/Japanese/Jinmeiyō]]` |
| `hanmun_edu_level` | `中` | `[[lookup/Korean/Korean MS]]` |
| `hanmun_edu_level` | `高等` | `[[lookup/Korean/Korean HS]]` |
| `hanmun_edu_level` | `名` | `[[Lookup/Korean/Korean Name X]]` |
| `hanmun_edu_level` | `無` | `[[lookup/Korean/Korean Missing]]` |

Real corpus values are always the full strings above (`高等`, `表外字`, `日本人名用漢字`) — never a bare `高` or a raw number beyond 6. A handful of files (introduced in error during a 2026-07-10 session) used `人名用字` instead — that string is not the vault's real convention; correct it to `日本人名用漢字` when found.

---

## `## Words` section

List every Dan'a'yo word that uses this character. Format: ruby-annotated link followed by an English gloss in quotes.

```markdown
## Words
- <ruby>[[詩篇]]<rt>ㄙㄧㄆ⼶ㄋ</rt></ruby> "poem, psalm"
- <ruby>[唐詩](../words/唐詩.md)<rt>ㄉ⺢ㄫㄙㄧ</rt></ruby> "Tang poetry"
```

Both wiki-links and relative Markdown links are valid inside the `<ruby>` element.

- The `<rt>` content is the full Dan'a'yo Bopomofo pronunciation of the word.
- The English gloss in quotes follows the ruby element.
- Order: most common or most central words first.
- **Exception — thematic subheadings for very long lists**: on the small number of high-frequency characters whose Words list runs to dozens of entries spanning distinct senses or a naturally grouped set (e.g. [[characters/月 (char)|月]]'s "Moon" vs. "Month" senses, [[characters/日 (char)|日]]'s "Sun" vs. "Day" senses), `###` subheadings inside `## Words` are allowed and preferred over one long undifferentiated list — they help human readers navigate. Not the default: don't add subheadings to an ordinarily-sized Words list just to look organized, and don't treat a missing subheading as a defect on its own. Ruby+gloss formatting rules are unchanged within each subgroup.

---

## `## Chengyu` section *(optional)*

Include when the character appears in one or more chengyu. Plain links with a short English gloss. 

```markdown
## Chengyu
- [[空前絶後]] "unprecedented and unrepeated"
- [一心同体](../chengyu/一心同体.md) "one heart, one body"
```

Wiki-links and relative Markdown links are equally valid.

---

## `## Derived Characters` section *(optional)*

Include when this character serves as a phonetic or semantic component in other characters that already exist in the database — i.e. this character is a graphemic "branch point" with its own descendants. Each descendant gets a ruby-annotated link showing *that descendant's own* Dan'a'yo syllable (not a word-level reading) plus a short English gloss, same `<ruby>` markup as `## Words`. It's normal — expected, even — for every bullet to carry the same ruby: descendants sharing the parent's phonetic component very often converge on the same MC initial+final and thus the same Dan'a'yo syllable, and the whole point of the section is to make that convergence visible at a glance.

```markdown
## Derived Characters
- <ruby>[[啖]]<rt>ㄉㄚㄇ</rt></ruby> "eat"
- <ruby>[[痰 (char)|痰]]<rt>ㄉㄚㄇ</rt></ruby> "phlegm"
- <ruby>[[談]]<rt>ㄉㄚㄇ</rt></ruby> "discuss"
```

This is distinct from the graphemic bullet's own phonetic-component link (bullet 1, which points *up* to a character's own phonetic parent) — Derived Characters points *down* to children. When perfecting a character page, check whether other characters in the database name this one as their `graphemic_classification` (phonetic component) or list it as a semantic/component link in their own graphemic bullet; if any do and aren't listed here, that's a gap, the same as a missing `## Words` entry.

---

## `date-last-perfect` criteria

Set when:

1. All required frontmatter fields are filled in, including `graphemic_classification`, `stand_in`, `mc_id`, and `danayo_id`.
2. `graphemic_classification` stores the phonetic component name (not `形声`) for 形声 characters.
3. The callout (if any) is present and correct; the `meta-bind-embed` block is the first content element after it (or first overall).
4. All four Notes bullets are present in the correct order.
5. Graphemic bullet correctly identifies the type and links the relevant components or list-of page.
6. SKIP/Stroke bullet links two targets (SKIP leaf, Stroke page) — no syllable link.
7. MC bullet states the ordinal rank, embeds both CC links with IPA display text, and links the syllable.
8. Levels bullet includes all four level links and they match the frontmatter values per the mapping table.
9. Every Dan'a'yo word that uses this character appears in `## Words` with a gloss.
10. Every chengyu that uses this character appears in `## Chengyu`.
11. Every other character in the database that names this one as its phonetic/semantic component appears in `## Derived Characters`, ruby-annotated with its own syllable, if any such descendants exist.

---

## Common mistakes

- **`graphemic_classification: 形声`** — this field stores the *phonetic component name* for 形声 characters (e.g. `寺`), not the string `形声`.
- **Floating CC links** — `[[Lookup/CC/initials/…]]` and `[[Lookup/CC/finals/…]]` do not belong at the bottom of the file; they are embedded inside the MC rank bullet.
- **`meta-bind-embed` not first** — the callout (if present) comes before the embed; the embed comes before everything else. No section headings, no prose, no links precede it.
- **`stand_in` blank** — every character must have a declared `stand_in` value, even if only `名専字`.
- **`pos` blank (`""`)** — required, not optional, and easy to miss because a blank string doesn't look broken the way a missing bullet does. Roughly a quarter of the corpus has this gap pre-existing, so don't assume a page is fine on this front just because it's otherwise well-formed — check it explicitly every time, the same as `mc_id` or `danayo_id`. See [[grammar/文法 - 97品詞]] for the real taxonomy (名詞/事詞/性詞/連接詞/etc.) — pick based on the character's actual grammatical behavior, not just "noun-ish vs verb-ish."
- **Heading level inconsistency** — use `##` (H2) for Notes, Words, Chengyu, and Derived Characters. Using `#` (H1) or `###` (H3) for these top-level sections is a mistake.
- **Words entries without glosses** — every word link should be followed by an English gloss in quotes.
- **Notes bullets out of order or missing** — the four-bullet sequence (graphemic → SKIP/Stroke → MC → levels) is fixed. All four must be present.
- **Missing `## Derived Characters`** — easy to overlook because it's optional and easy to forget to check *for*. A character with a real graphemic family (its phonetic component is reused by several other vault characters, e.g. [[炎]] → 啖/痰/談) should surface that family here; don't assume the section doesn't apply just because the page never had one before.
- **Callout/link paths missing the `../` prefix** — a recurring defect on older pages: `[X](words/X.md)` or `[[Lookup/...]]`-style links written as if the page lived at the vault root, when it actually needs `../words/X.md` etc. from inside `characters/`. Also watch for the inverse mistake — a relative-path prefix accidentally baked into wiki-link syntax itself, e.g. `[[../lookup/CC/finals/韻 X]]` (Obsidian wiki-links resolve by name, not path, so the `../` breaks it) — the fix there is just to drop the prefix, not the link.
- **`mc_id` off-by-one** — don't trust a stored rank at face value even when a plausible-looking number is present; cross-check it against the actual line in `lookup/CC/CC 0000–3000.md`. Found twice in one night (艮: stored 2146 which is actually 鉞's rank,真 rank 2147; 煌: stored 2062 which is actually 蚡's rank, real rank 2063) — both were the entry immediately before the correct one, suggesting a systematic one-line-off transcription error somewhere upstream, not a one-off typo.
