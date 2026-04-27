---
language: English
tags:
  - chengyu
  - best-practice
---

# Best Practices: Chengyu Pages

A chengyu page is an encyclopedic article on a single four-character idiom: its literal and figurative meaning, its origin and textual history, its pronunciations across the CJKV sphere, its cultural valence, and its use in context. The target standard is thorough — each page should be able to stand alone as a reference.

---

## Frontmatter

All fields below are required.

```yaml
---
characters:
  - 一 (char)      # each constituent character, using (char) suffix where applicable
  - 帆 (char)
  - 風 (char)
  - 順
諺文: 읻팜뿡슌        # Hangul transcription of the full chengyu
羅馬字: "'idpamfungsyun"  # Danayo romanisation
english: smooth sailing, bon voyage   # core meaning; brief
mandarin: yīfānfēngshùn   # Pinyin, no tones required but include if known
cantonese: jat1 faan4 fung1 seon6     # Jyutping
japanese: じゅんぷうまんぱん            # hiragana (on-yomi preferred)
korean: 순풍만범                        # Hangul Sino-Korean
vietnamese: nhất phàm phong thuận    # Sino-Vietnamese (Hán-Việt)
注音: ㄧㄊㄆㄚㄇㄈㄨㄫㄙ⼜ㄋ              # Bopomofo pronunciation of the full chengyu
origin: Ming period      # source text, period, tradition, "単亜語", or "Bible"
aliases:                 # simplified, traditional, or Japanese variant forms
  - 一帆风顺
date-last-perfect: YYYY-MM-DD
tags:
  - chengyu
---
```

**`origin`** drives category membership. Use the name of a classical source text (e.g. `"史記: 春申君列傳"`), a period or tradition (e.g. `"Ming period"`, `"Japanese 茶道"`), `"単亜語"` for Danayo-coined idioms, or `"Bible"` for Biblical idioms. This field determines which grouping file the chengyu belongs to.

**`characters`** lists each constituent character in order. Use the `X (char)` form when the character file carries that suffix; otherwise use the plain name.

**`aliases`** should include all commonly encountered orthographic variants — simplified/traditional alternates, Japanese shinjitai forms, historical alternates. These are what Obsidian will search on.

---

## Body structure

The body has a fixed opening, then a sequence of named sections.

### Fixed opening

The first two lines of every chengyu body are always:

```markdown
​```meta-bind-embed
[[nav/chengyu_info]]
​```
[Misc. Chengyu](chengyu/Misc. Chengyu.md)
```

The `meta-bind-embed` block must come **before any other content** — place it immediately after the frontmatter closing `---`. The category link on the following line points to one of the three grouping files:

| `origin` value | Grouping file |
|---|---|
| `単亜語` | `[Dan'a'yo Chengyu](chengyu/Dan'a'yo Chengyu.md)` |
| `Bible` | `[Biblical Chengyu](chengyu/Biblical Chengyu.md)` |
| anything else | `[Misc. Chengyu](chengyu/Misc. Chengyu.md)` |

A callout may follow the category link when the chengyu is cross-referenced elsewhere in the vault:
```markdown
>[!Tip] For a usage of this idiom, see [[文法 - 03文字法]]
```

---

## Encyclopedic sections

Use `##` for all main sections. The canonical order is:

### 1. `## Literal Meaning`

State the character-by-character gloss, then the literal English rendering.

```markdown
## Literal Meaning
- 一 — one
- 帆 — sail
- 風 — wind
- 順 — favorable

Literally: "One sail with a favorable wind."
```

Link each character to its character file when the connection is informative:
```markdown
- [一](characters/一%20(char).md) — one
```

Plain text glosses are also acceptable when the character's meaning is unambiguous.

### 2. `## Extended Meaning`

The figurative or idiomatic sense in modern usage. Explain what the idiom *means* when used, not just what it *says*. Note whether it is positive, negative, or neutral; whether it is used literally or only figuratively; and what domains it typically appears in.

### 3. `## Source and Origin`

The most important section for classical idioms. Include:

- The source text, with full classical citation if traceable (e.g. **《史記·春申君列傳》**)
- A quotation in the source language, with English translation
- The historical or literary context that produced the phrase
- Whether the fixed four-character form appears in the original or crystallized later

For idioms of modern or non-Chinese origin (e.g. calques, Japanese coinages), explain that origin clearly and trace the phrase's adoption into the broader CJKV sphere.

For Danayo-coined idioms (`origin: 単亜語`), explain the design intention of the idiom.

Classical quotations follow this format:
```markdown
**《世說新語·言語》** (compiled 5th c.):
> "王夷甫神識清澄，**瞭然**自得。"
> (Wang Yifu's mind was lucid, clearly at ease.)
```

### 4. `## Standard Form` *(omit if no meaningful variants)*

Note any orthographic variants — simplified/traditional alternates, regional preferences, historical alternates. State which form is standard for Danayo and which forms are listed as aliases.

```markdown
## Standard Form
**一目瞭然**
- 一目了然 — simplified form (瞭 → 了); dominant in Mainland China
- Both forms current; Taiwan and Japan prefer 瞭
```

Omit this section entirely if the characters are stable across all regions and scripts.

### 5. `## Pronunciations`

List all five CJKV pronunciations, in this order, with consistent labeling:

```markdown
## Pronunciations
- **Mandarin (Pinyin):** yī fān fēng shùn
- **Cantonese (Jyutping):** jat1 faan4 fung1 seon6
- **Japanese (on-yomi, hiragana):** いっぱんふうじゅん
- **Korean (Sino-Korean):** 일범풍순 (il-beom-pung-sun)
- **Vietnamese (Hán–Việt):** nhất phàm phong thuận
```

Note variant Japanese readings (on-yomi vs. kun-yomi or native compound) where they exist.

### 6. `## Cultural Notes`

Regional differences in usage, register, and connotation. Address each CJKV language separately when the idiom means or feels different across them. Include:

- Contextual domains (formal speech, business, ceremony, casual conversation)
- Whether it is a set-phrase blessing, a literary reference, or neutral vocabulary
- Differences in frequency or register between regions

### 7. `## Example Sentences`

Two to four examples, mixing classical citation and modern usage. Include at least one example in a CJKV language and one in English. Bilingual examples are ideal:

```markdown
## Example Sentences
1. 學問非一朝一夕之功。
2. Trust cannot be built in _yī zhāo yī xī_.
3. His career has been one of steady success — almost _yī fān fēng shùn_.
```

### 8. `## Sentiment`

One to three lines. State the emotional valence (positive / negative / neutral / mixed) and the register or tone. Be specific:

```markdown
## Sentiment
Strongly positive; auspicious and ceremonial in tone.
Often formulaic — used at New Year, departures, and business openings.
```

---

## Optional sections

These appear in some files and should be added when relevant:

- **`## Usage Note`** — when a common misunderstanding, a grammatical restriction, or a contrast with a similar idiom warrants a dedicated note.
- **`## Variants`** — when variant forms have distinct histories or connotations worth discussing beyond the `## Standard Form` summary.
- **`## Origins`** with dated sub-headers — for idioms with complex, multi-stage histories (e.g. 一期一会), structure the origin section as numbered sub-sections tracing each stage.

---

## `date-last-perfect` criteria

Set when:
1. All frontmatter fields are filled in, including `origin` and `aliases`.
2. The `meta-bind-embed` block is the first thing in the body.
3. The category link correctly reflects the `origin` value.
4. All eight canonical sections are present (or deliberately omitted with good reason).
5. The Source and Origin section cites a specific text or explains the modern provenance clearly.
6. All five CJKV pronunciations are present in the frontmatter and in the Pronunciations section.
7. At least two example sentences are included.

---

## Common mistakes

- **`meta-bind-embed` not first** — any content before the embed block will appear above the dashboard. Nothing goes before it.
- **`origin` left blank** — this field drives the Base check filters in the grouping files; a blank origin is an invisible chengyu.
- **Mixing `##` and `###` heading levels** — pick one level for main sections and use it consistently throughout the file. `##` is preferred.
- **Pronunciations in frontmatter only, not in body** — the frontmatter values feed the database; the body Pronunciations section is what a reader actually reads. Both are needed.
- **Omitting the category link** — the `meta-bind-embed` is not the category link. The category link is a separate line immediately after the embed block.
- **`aliases` missing variant scripts** — simplified Chinese, traditional Chinese, and Japanese shinjitai forms are all distinct and all worth listing so that searches in any script resolve to this page.
