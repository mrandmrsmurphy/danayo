---
language: English
tags:
  - character
  - best-practice
---

# Best Practices: Character Pages

A character page is the canonical record for one 漢字 in Danayo: its orthography, pronunciations across all five CJKV languages, graphemic origin, phonological history, and its role in Danayo words and chengyu. Every page must be self-contained as a reference while also feeding the database via its frontmatter.

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
grade_level: "2"            # Danayo grade: "1"–"6", "先進", or "名"
pos: 名詞                   # part of speech: 名詞, 動詞, 性詞, 数詞, etc.
english:                   # English gloss(es), as a list
  - poem
羅馬字: si                  # Danayo romanisation
諺文: 시                    # Hangul of the Danayo pronunciation
joyo_level: "3"             # Japanese level — see Level links table below
hsk_level: "2"              # HSK level — see Level links table below
hanmun_edu_level: 中        # K level: 中 (MS), 高 (HS), 名 (name), or 無 (absent)
danayo_id: 2230             # Danayo character ID (integer)
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

Use `[!tip]` for standard disambiguation. Use `[!warning]` when there is a restriction or easy confusion (e.g. a homographic radical alias, a character forbidden in Danayo).

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
- 会意 of [[亻]] ("person upright") and [[𠤎]] ("person inverted") — the concept of reversal or transformation.
```
Include: each constituent component linked with English gloss; a dash-note on the resulting compound meaning. If a historical source (e.g. Shuowen) offers a different analysis, note it briefly.

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

---

### Bullet 2 — SKIP and Stroke

```markdown
- [SKIP-1-7-6](lookup/SKIP/SKIP-1/SKIP-1-7-6.md) ([Stroke 13](lookup/Stroke/Stroke%2013.md)) — [ㄙㄧ](syllables/ㄙㄧ.md)
```

Three links in sequence: the SKIP leaf page, the Stroke count page, and the Danayo syllable page. Separate the syllable link with an em-dash `—`.

---

### Bullet 3 — Middle Chinese rank and phonology

```markdown
- 351st most used character in Classical Chinese. Ancient [[Lookup/CC/initials/聲 書|ɕ]] + [[Lookup/CC/finals/韻 之|ɨ]] → [ㄙㄧ](syllables/ㄙㄧ.md)
```

Format: ordinal rank from `mc_id` + "most used character in Classical Chinese." Then `Ancient` followed by the CC initial link and CC final link — use the IPA symbol as the display text via the pipe alias. Close with `→` and the Danayo syllable link.

The `[[Lookup/CC/initials/…]]` and `[[Lookup/CC/finals/…]]` links live **here**, embedded in this bullet. They must not float at the bottom of the file.

---

### Bullet 4 — Level links

```markdown
- [Grade 2](lookup/Grade%202.md), [Old HSK 2](lookup/HSK/Old%20HSK%202.md), [Jōyō - Kyōiku](lookup/Japanese/Jōyō%20-%20Kyōiku.md), [Korean MS](lookup/Korean/Korean%20MS.md)
```

List all four levels in order: Danayo grade, HSK, Jōyō, Korean. Include all four — use the "absent" file when a level is missing.

**Level file mapping:**

| Field | Value | Link |
|---|---|---|
| `grade_level` | `"1"`–`"6"` | `[[Grade N]]` |
| `grade_level` | `"名"` | `[[Grade Name]]` |
| `hsk_level` | `"1"` | `[[lookup/HSK/HSK Beginner]]` |
| `hsk_level` | `"2"`–`"6"` | `[[lookup/HSK/Old HSK N]]` |
| `hsk_level` | `"無"` | `[[lookup/HSK/HSK No]]` |
| `joyo_level` | `"1"`–`"6"` | `[[lookup/Japanese/Jōyō - Kyōiku]]` |
| `joyo_level` | value > 6 | `[[lookup/Japanese/Jōyō - Kōtō]]` |
| `joyo_level` | `表外字` | `[[lookup/Japanese/Hyōgai]]` |
| `joyo_level` | `人名用字` | `[[lookup/Japanese/Jinmeiyō]]` |
| `hanmun_edu_level` | `中` | `[[lookup/Korean/Korean MS]]` |
| `hanmun_edu_level` | `高` | `[[lookup/Korean/Korean HS]]` |
| `hanmun_edu_level` | `名` | `[[Lookup/Korean/Korean Name X]]` |
| `hanmun_edu_level` | `無` | `[[lookup/Korean/Korean Missing]]` |

---

## `## Words` section

List every Danayo word that uses this character. Format: ruby-annotated wiki-link followed by an English gloss in quotes.

```markdown
## Words
- <ruby>[[詩篇]]<rt>ㄙㄧㄆ⼶ㄋ</rt></ruby> "poem, psalm"
- <ruby>[[詩歌]]<rt>ㄙㄧㄍㄚ</rt></ruby> "poetry"
- <ruby>[[唐詩]]<rt>ㄉ⺢ㄫㄙㄧ</rt></ruby> "Tang poetry"
```

- The `<rt>` content is the full Dan'a'yo Bopomofo pronunciation of the word.
- The English gloss in quotes follows the ruby element.
- Order: most common or most central words first.

---

## `## Chengyu` section *(optional)*

Include when the character appears in one or more chengyu. Plain wiki-links with a short English gloss. 

```markdown
## Chengyu
- [[空前絶後]] "unprecedented and unrepeated"
- [[一心同体]] "one heart, one body"
```

---

## `## Derived Characters` section *(optional)*

Include when this character serves as a phonetic or semantic component in other characters in the database. Plain character links, one per line.

```markdown
## Derived Characters
- [[髯]]
- [[冄]]
```

---

## `date-last-perfect` criteria

Set when:

1. All required frontmatter fields are filled in, including `graphemic_classification`, `stand_in`, `mc_id`, and `danayo_id`.
2. `graphemic_classification` stores the phonetic component name (not `形声`) for 形声 characters.
3. The callout (if any) is present and correct; the `meta-bind-embed` block is the first content element after it (or first overall).
4. All four Notes bullets are present in the correct order.
5. Graphemic bullet correctly identifies the type and links the relevant components or list-of page.
6. SKIP/Stroke bullet links all three targets (SKIP leaf, Stroke page, syllable page).
7. MC bullet states the ordinal rank, embeds both CC links with IPA display text, and links the syllable.
8. Levels bullet includes all four level links and they match the frontmatter values per the mapping table.
9. Every Danayo word that uses this character appears in `## Words` with a gloss.
10. Every chengyu that uses this character appears in `## Chengyu`.

---

## Common mistakes

- **`graphemic_classification: 形声`** — this field stores the *phonetic component name* for 形声 characters (e.g. `寺`), not the string `形声`.
- **Floating CC links** — `[[Lookup/CC/initials/…]]` and `[[Lookup/CC/finals/…]]` do not belong at the bottom of the file; they are embedded inside the MC rank bullet.
- **`meta-bind-embed` not first** — the callout (if present) comes before the embed; the embed comes before everything else. No section headings, no prose, no links precede it.
- **`stand_in` blank** — every character must have a declared `stand_in` value, even if only `名専字`.
- **Heading level inconsistency** — use `##` (H2) for Notes, Words, Chengyu, and Derived Characters. Using `#` (H1) or `###` (H3) for these top-level sections is a mistake.
- **Words entries without glosses** — every word link should be followed by an English gloss in quotes.
- **Notes bullets out of order or missing** — the four-bullet sequence (graphemic → SKIP/Stroke → MC → levels) is fixed. All four must be present.
