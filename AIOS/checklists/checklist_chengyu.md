---
name: checklist-chengyu
description: Completion rubric for chengyu pages — encyclopedic depth, origin/textual history, and cross-CJKV pronunciation
metadata:
  type: checklist
---

# Checklist: Chengyu Pages

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
羅馬字: "'idpamfungsyun"  # Dan'a'yo romanisation
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

**`origin`** drives category membership. Use the name of a classical source text (e.g. `"史記: 春申君列傳"`), a period or tradition (e.g. `"Ming period"`, `"Japanese 茶道"`), `"単亜語"` for Dan'a'yo-coined idioms, or `"Bible"` for Biblical idioms. This field determines which grouping file the chengyu belongs to.

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

For Dan'a'yo-coined idioms (`origin: 単亜語`), explain the design intention of the idiom.

Classical quotations follow this format:
```markdown
**《世說新語·言語》** (compiled 5th c.):
> "王夷甫神識清澄，**瞭然**自得。"
> (Wang Yifu's mind was lucid, clearly at ease.)
```

### 4. `## Standard Form` *(omit if no meaningful variants)*

Note any orthographic variants — simplified/traditional alternates, regional preferences, historical alternates. State which form is standard for Dan'a'yo and which forms are listed as aliases.

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

## Back-linking character pages

After creating a chengyu file, add a ruby-annotated entry to the `## Chengyu` section of **every constituent character's page**. Create the section if it does not exist.

```markdown
## Chengyu
- <ruby>[[弱不禁風]]<rt>ㄋ⼘ㄎㄅㄛㄊㄍㄧㄇㄈㄨㄫ</rt></ruby> "so frail as to be unable to withstand the wind"
```

- The `<rt>` content is the full Dan'a'yo 注音 of the chengyu.
- The quoted gloss is the `english` frontmatter value.
- Place `## Chengyu` **after** `## Words` (if that section exists) and before any lookup links.

---

## `date-last-perfect` criteria

Set when:
1. All frontmatter fields are filled in, including `origin` and `aliases`.
2. The `meta-bind-embed` block is the first thing in the body.
3. The category link correctly reflects the `origin` value.
4. All eight canonical sections are present (or deliberately omitted with good reason).
5. The Source and Origin section cites a specific text or explains the modern provenance clearly. **Every named citation has been verified against the source itself (see "Source check" below)** (added 2026-10-04): each quoted line was found in the named work, and the work, chapter and section label match the passage actually quoted (e.g. a 戰國策 passage filed under the wrong 策). Check against a primary text (wikisource, ctext, or the Bible text for Biblical pages), not against another secondary page or a memory of it. If the citation cannot be found, correct it or remove it; never stamp on an unverified quotation. Dan'a'yo coinages (`origin: 単亜語`) have no external source to verify, but any classical text they cite as a model still falls under this rule.
6. All five CJKV pronunciations are present in the frontmatter and in the Pronunciations section.
7. At least two example sentences are included.
8. All constituent character pages have been back-linked in their `## Chengyu` section.

---

## Source check (required to perfect a chengyu)

Added 2026-10-04. A chengyu is not perfect until its `Source and Origin` section has been **checked against a primary text**, and the check is part of perfecting the page, not a separate audit. Concretely, before stamping `date-last-perfect`:

1. **Find the passage.** Locate every quoted line in the named work (wikisource, ctext, CBETA, or the Bible text for Biblical pages) and confirm the wording, the work, and the chapter or section label. Do not rely on another secondary page or on memory.
2. **Check that the source really contains the idiom.** Many chengyu pages named a famous work that does not contain the four characters (the idiom was coined later from a story, or from a different text). If the four-character form is not in the cited text, say what the text does contain and name the earliest text in which you can verify the four characters.
3. **Record what you could not verify.** If a source cannot be reached or checked, say so on the page and do not state it as fact. Do not invent a context, a commentator or a quotation to fill the gap.
4. **Set `origin` to what you verified**, a single value, quoted if it contains a colon.
5. **Coinages** (`origin: 単亜語`) have no external source, but any outside claim they make (a historical date, a theory) is checked the same way.

**Scope.** This applies to every chengyu that is newly perfected or re-touched from 2026-10-04 on. It does not oblige a re-audit of already-stamped pages, which were perfected under the earlier rubric; fix a page's citations when you next work on it. A 10-page random sample of the September pages found roughly half with a citation problem, so the check is worth doing whenever a page is touched.

The mechanical lint (`AIOS/scripts/lint_chengyu.py`) cannot check citations; it needs a source lookup, so this step is always done by hand.

---

## Grouping pages (`Misc. Chengyu.md`, `Dan'a'yo Chengyu.md`, `Biblical Chengyu.md`)

Added 2026-10-04. Each grouping page is a full-length index of every chengyu whose `origin` maps to it (see the table under "Fixed opening"). They are unordered bulleted lists: order carries no meaning, and new entries may go anywhere.

Each entry is exactly one bullet in this form, with the same shape on all three pages:

```markdown
- <ruby>[一刀両断](chengyu/一刀両断.md)<rt>ㄧㄊㄊㄚㄨㄌ⼘ㄫㄉ⺢ㄋ</rt></ruby> - cut in two with one stroke
```

A grouping page is complete (`date-last-perfect` may be set) when all of these hold on the stamping date:

1. **Membership is exact.** The entries are precisely the leaf pages whose `origin` maps to this page: no missing leaf, no extra, no duplicate. Derive the set by script (`python3 AIOS/scripts/lint_chengyu_groups.py`), never by eye. A chengyu with `origin: 単亜語` is never listed on `Misc.`, whatever it was once filed under.
2. **Every entry is ruby-annotated, in one link style.** A relative markdown link `chengyu/NAME.md`, never a bare `[[wikilink]]` or an absolute `/chengyu/` path. The `<rt>` text equals the leaf's `注音` byte for byte, so a change to a leaf's 注音 makes this page stale.
3. **Every entry has a short English gloss** after ` - `. Keep an existing hand-written gloss; otherwise use the leaf's `english`.
4. **No stray marks** (the old ✅ creation-tracking suffix is meaningless and must be removed) and no doubled separators.
5. **The `## Base check` block** filters on the correct `origin` for this page's classification (`== "単亜語"`, `== "Bible"`, or neither of those for `Misc.`).
6. **`size` property.** The frontmatter has `size: N`, where N is the number of entries in the list (the same convention as syllable pages). Update it whenever an entry is added or removed; the script checks it against the actual count.
7. **An over-arching chengyu is just another entry.** Do not give one a special header line (the old "Over all is [[創反救成]]" intro on the Biblical page became an ordinary entry).

The stamp goes stale whenever a leaf is added, removed, re-origined or has its 注音 changed. Re-run the script after any such change and fix the page before keeping the stamp.

---

## Common mistakes

- **Unverified or misattributed citations** — a quotation or chapter label taken on trust. Eleven pre-perfection pages were found with invented or misattributed classical quotes, and 舎本逐末 had a correct quote filed under the wrong chapter (趙策四 for 齊策四). Verify every named source at perfecting time; a stamp is a claim that this was done.
- **`meta-bind-embed` not first** — any content before the embed block will appear above the dashboard. Nothing goes before it.
- **`origin` left blank** — this field drives the Base check filters in the grouping files; a blank origin is an invisible chengyu.
- **Mixing `##` and `###` heading levels** — pick one level for main sections and use it consistently throughout the file. `##` is preferred.
- **Pronunciations in frontmatter only, not in body** — the frontmatter values feed the database; the body Pronunciations section is what a reader actually reads. Both are needed.
- **Omitting the category link** — the `meta-bind-embed` is not the category link. The category link is a separate line immediately after the embed block.
- **`aliases` missing variant scripts** — simplified Chinese, traditional Chinese, and Japanese shinjitai forms are all distinct and all worth listing so that searches in any script resolve to this page.
