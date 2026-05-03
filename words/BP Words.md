---
language: English
tags:
  - word
  - best-practice
---

# Best Practices: Word Pages

A word page is the canonical record for one multi-character Dan'a'yo compound: its pronunciation across the CJKV sphere, its Dan'a'yo phonology, its constituent characters, and its meaning. Every page must be queryable via Obsidian Bases and must link cleanly back to its component character pages.

---

## Frontmatter

Fields in the first group are **always required**. Fields in the second group are **only included when non-empty** — omit them entirely if they would be blank.

```yaml
---
characters:            # constituent characters, in order — always required
  - 今 (char)          # use "X (char)" form when the character file has that suffix
  - 週                 # use plain name when the character file has no suffix
羅馬字: gimjuo          # Dan'a'yo romanisation — concatenation of component romanisations
諺文: 김줏              # Hangul transcription of the Dan'a'yo pronunciation
english: this week     # English gloss; brief
pos: 名詞               # part of speech: 名詞, 動詞, 性詞, 数詞, 副詞, 助詞, etc.
mandarin: "jīnzhōu      # Pinyin (tone marks preferred)"
cantonese: "gam1 zau1   # Jyutping with tone numbers"
japanese: こんしゅう      # hiragana reading
korean: "금주            # Hangul (Sino-Korean or native as appropriate)"
注音: ㄍㄧㄇㄐㄨㄛ         # Bopomofo — concatenation of component 注音 values
tags:
  - word
---
```

**Only include these fields when they have a value:**

```yaml
vietnamese: tuần này   # Sino-Vietnamese or modern Vietnamese
hsk_level: "2"         # HSK level as a quoted string, if the word appears in HSK
swadesh: number          # only present if this is a Swadesh-list word
aliases:               # simplified, traditional, or alternate orthographic forms
  - 今周
```

---

## `characters` field

List every constituent character in order. Use the `X (char)` form when the character file is named `X (char).md`; use the plain name when it is simply `X.md`. When a component is itself a multi-character compound (e.g. 世紀 in 今世紀), list its individual characters separately — do not nest compounds.

```yaml
characters:      # ✓ correct — every character listed individually
  - 今 (char)
  - 世
  - 紀
```

---

## Body structure

The body has two fixed elements.

### meta-bind-embed block

The first line of the body is always:

```
​```meta-bind-embed
[[nav/word_info]]
​```
```

### Notes section

After the meta-bind-embed block, add a `## Notes` section that links each constituent character back to its character page:

```markdown
## Notes
- [今 (char)](../characters/今%20(char).md) "present" + [週](../characters/週.md) "week"
```

**Link format rules:**
- Always use `../characters/` relative paths, not word-file paths.
- URL-encode the space before `(char)` as `%20`: `今%20(char).md`.
- Include the English gloss of each character in quotes after its link.
- Use `+` to separate components.
- When a component is a meaningful compound word in its own right (e.g. 世紀), also link to its word page in the same directory: `[世紀](世紀.md)`.

---

## Common mistakes

### Blank properties left in the frontmatter

Do not include `vietnamese:`, `hsk_level:`, `swadesh:`, or `aliases:` with an empty value. Remove the key entirely when there is nothing to put there. Blank properties clutter the Bases database and create false nulls in queries.

```yaml
# ✗ wrong
vietnamese:
hsk_level:
swadesh:
aliases:

# ✓ correct — omit the key entirely
```

### Missing Notes section

Every word page must have a `## Notes` section linking to each component character. A page without it cannot be verified for correctness and breaks navigation from the word back to the character.

### Linking to a word file instead of a character file

When a component is a single character, the Notes link must point to `../characters/X.md`, not to `X.md`. The `/words/` directory may contain a word with the same spelling as a character (e.g. `日.md`, `年.md`), and a bare `[日](日.md)` link will resolve to the word file, not the character.

```markdown
<!-- ✗ wrong — resolves to words/日.md if that file exists -->
- [日](日.md) "day"

<!-- ✓ correct — always targets the character file -->
- [日](../characters/日%20(char).md) "day"
```

### Wrong or missing `(char)` suffix in the characters list

Check whether the character file is named `X (char).md` or `X.md` before writing the characters list. Using plain `X` when the file is `X (char).md` creates a broken or ambiguous Obsidian link.

### Using a mandarin-style romanisation instead of Dan'a'yo

`羅馬字` is the **Dan'a'yo** romanisation, not Pinyin. It is the direct concatenation of the 羅馬字 values from each component character file. Do not enter Pinyin, Yale, or any other romanisation system here.
