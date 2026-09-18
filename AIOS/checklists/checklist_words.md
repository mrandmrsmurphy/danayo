---
name: checklist-words
description: Completion rubric for word pages — frontmatter fields, constituent character links, and Bases queryability
metadata:
  type: checklist
---

# Checklist: Word Pages

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
date-last-perfect: YYYY-MM-DD  # set only once every criterion below is met; leave absent/blank otherwise
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

### `date-last-perfect`

Set it once, and only once, a word page satisfies every criterion in this checklist: all required frontmatter present and correctly formatted (blank-optional fields omitted, not left empty), the meta-bind-embed first, a homophone callout if applicable (correct `[!warning]` form and placement), a real encyclopedic `## Notes` section (not just the character-linking bullet), and — added 2026-09-18, see [[AIOS/memory/feedback_lexipedia_semantic_differentiation.md]] — **lexipedia placement** (the word appears on at least one `lexipedia/` domain page, and its Notes states the word's own Dan'a'yo-specific sense; see "Lexipedia placement" under Body structure below). Leave it absent while any of that is still outstanding — don't stamp a word just because its frontmatter looks tidy.

**Scope note on the lexipedia-placement criterion**: this requirement is **prospective only** (decided 2026-09-18). It applies to words being perfected or re-touched for any reason from this date forward. It does **not** retroactively invalidate the ~6,000 words already stamped under the pre-2026-09-18 rubric — don't launch a dedicated re-audit sweep of the existing corpus on the strength of this criterion alone. Backfill lexipedia placement opportunistically when an already-stamped word is touched again for some other reason, or when a lexipedia page is being built out and naturally pulls in existing words.

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

### Homophone callout *(when needed)*

When a word shares its exact Dan'a'yo pronunciation (same 注音 / 羅馬字) with another word, add a `>[!warning] Homophones` callout **immediately after** the meta-bind-embed block, **before** `## Notes`:

```markdown
>[!warning] Homophones
> [[OtherWord]] "gloss"
```

- Both words must carry the callout, cross-linking each other.
- List each homophone with its short English gloss; separate multiple homophones with em-dashes on one line, or one per line.
- Do **not** note the homophone only in the Notes prose, and do **not** put it before the meta-bind-embed — the callout goes after the embed, and is the canonical place.

### Notes section

After the homophone callout (or after the meta-bind-embed if there is none), add a `## Notes` section. This is a **substantive, encyclopedic** section, not a one-line gloss — see [[AIOS/memory/feedback_notes_style.md]]. Structure:

1. **Opening bullet**, linking each constituent character back to its character page:

```markdown
## Notes
- [今 (char)](../characters/今%20(char).md) "present" + [週](../characters/週.md) "week"
```

**Link format rules for the opening bullet:**
- Always use `../characters/` relative paths, not word-file paths.
- URL-encode the space before `(char)` as `%20`: `今%20(char).md`.
- Include the English gloss of each character in quotes after its link.
- Use `+` to separate components.
- When a component is a meaningful compound word in its own right (e.g. 世紀), also link to its word page in the same directory: `[世紀](世紀.md)`.
- If this word is the `stand_in` that legitimizes one of its own constituent characters, append that fact to this bullet — see [[AIOS/memory/feedback_standin_note.md]].

2. **One or more substantive paragraphs** after the opening bullet, covering (as applicable): etymology/origin, historical or cultural context, and — especially — cross-linguistic variation where the concept differs meaningfully across Chinese/Japanese/Korean/Vietnamese (semantic drift, narrowing, homophone collisions, native coinages). Numbered lists for canonical sets (Nine Ministers, Six Hollow Organs, etc.). Cross-link related vault words. Aim for at least 2–3 real paragraphs of content, not a restatement of the gloss.

After the notes, if there are multiple definitions, they should be listed in a numbered list.

### Lexipedia placement *(required for words perfected 2026-09-18 or later — see scope note above)*

A word being newly perfected (or re-touched for any other reason) must **link into at least one `lexipedia/` domain page** — i.e. appear as an entry on a page like `lexipedia/Metals.md` or `lexipedia/Numbers.md`, placing it within a semantic field rather than leaving it a free-floating translation. If no domain page exists yet for the word's field, add the word to the nearest existing page it plausibly belongs to, or note in the word's own `## Notes` that it awaits a domain page rather than skipping the requirement silently.

The point of this isn't bookkeeping — it's semantic. See [[AIOS/memory/feedback_lexipedia_semantic_differentiation.md]]. Placing a word within a semantic field is the occasion to ask whether Dan'a'yo's own sense of the word should **narrow, shift, or broaden** relative to the meaning shared across Mandarin/Cantonese/Japanese/Korean/Vietnamese — the CJKV/"international" baseline. Most words won't need this; a plain shared meaning is fine and normal. But when the lexipedia domain reveals a genuine reason to diverge (a collision with a neighboring word in the same field, a gap the domain needs filled, an opportunity to make Dan'a'yo function on its own terms rather than as a transliteration), state that Dan'a'yo-specific sense explicitly as part of the word's `## Notes` prose — don't just note it on the lexipedia page and leave the word page itself silent. Don't invent a divergence that isn't real just to satisfy this bullet; an honest "same as the shared CJKV sense" is correct far more often than not.

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

### Stamping `date-last-perfect` without lexipedia placement

For a word being perfected or re-touched from 2026-09-18 forward, don't stamp `date-last-perfect` just because the frontmatter, embed, and Notes section all look complete — check it actually appears on a `lexipedia/` domain page first. This does **not** apply to already-stamped words from before that date; see the scope note under `date-last-perfect` above. Don't treat an old stamp's lack of lexipedia placement as a defect to fix on sight — only backfill it if you're touching that word for some other real reason.

### Inventing a Dan'a'yo-specific sense that isn't real

The lexipedia-placement criterion is not a mandate to manufacture a narrowed/shifted/broadened meaning for every word. Most words correctly keep the shared CJKV/international sense with no divergence at all — see [[AIOS/memory/feedback_lexipedia_semantic_differentiation.md]] for the standing caution against forcing premature disambiguation. Only state a Dan'a'yo-specific sense when the lexipedia domain surfaces a real reason for one.
