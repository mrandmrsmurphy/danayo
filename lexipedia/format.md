---
name: lexipedia-format
description: Standard template and style guide for all semantic domain pages in the Lexipedia. Ensures consistency across domains and provides structure for vocabulary organization by frequency and semantic subcategory.
type: reference
---

# Lexipedia Format Guide

## Overview

Each semantic domain in `/lexipedia/` follows a consistent structure to ensure:
- **Pedagogical clarity** — vocabulary organized by learner level (A1–C1+)
- **Semantic precision** — how Dan'a'yo's boundaries differ from source languages
- **Navigation** — cross-linking to related domains, grammar chapters, and word files
- **Scholarly rigor** — etymology notes and cross-linguistic comparisons

---

## File Naming & Frontmatter

**Filename**: `[Domain Name].md`
- Use English domain name (e.g., `Kinship.md`, `Emotions.md`, `Time.md`)
- If domain name contains multiple words, use Title Case without hyphens

**Frontmatter** (YAML):
```yaml
---
language: English
type: lexipedia
domain: [Domain Name]
related_domains: [[Domain1]], [[Domain2]], [[Domain3]]
status: [new | stub | partial | complete]
---
```

- `domain`: Exact domain name
- `related_domains`: Wiki-links to 2–5 related domains (e.g., Animals ↔ Kinship; Time ↔ Calendar)
- `status`: One of:
  - `new` — Framework exists, minimal content
  - `stub` — Outline only, <500 words
  - `partial` — Some tiers filled, gaps remain
  - `complete` — All three tiers substantially filled (1500+ words)

---

## Section Structure

### 1. Domain Overview (Brief introduction)

**Purpose**: Explain what this domain covers and why it matters for Dan'a'yo learners.

**Length**: 2–4 sentences.

**Example**:
> Kinship terminology encodes family relationships across generations and lineages. Because Dan'a'yo inherits Chinese genealogical structure (with distinct terms for maternal vs. paternal kin, elder vs. younger siblings), understanding kinship vocabulary is essential for reading classical texts and for respectful social interaction.

---

### 2. Core Vocabulary (A1–A2)

**Who this is for**: Absolute beginners; learners of Lessons 01–06

**What belongs here**: High-frequency, universal concepts; overlaps with Swadesh List or basic conversation starters.

**Organization**: Alphabetical or semantic subcategory (whichever is clearer).

**Format**:
```markdown
- <ruby>[Character/Word](path/to/word.md)<rt>ㄅㄛ⼄</rt></ruby>: Definition (English). 
  - **Literal meaning**: Where useful, explain character composition or etymology.
  - **Cross-linguistic notes**: How Mandarin, Cantonese, Japanese, Korean differ.
  - **Usage note**: Connotation, register, common phrases.
```

**Example**:
```markdown
- <ruby>[母](words/母.md)<rt>ㄇㄚ</rt></ruby>: Mother.
  - **Literal**: Picture of woman + breast (ancient form).
  - **Cross-ling**: Mandarin 母 (mǔ), Japanese 母 (haha), Korean 모 (mo). 
  - **Usage**: Neutral/formal; diminutive form is 母母.

- <ruby>[父](words/父.md)<rt>ㄅㄚ</rt></ruby>: Father.
  - **Literal**: Hand + rod (ancient form; possibly ritual authority).
  - **Cross-ling**: Mandarin 父 (fù), Japanese 父 (chichi), Korean 아비 (abi, archaic) / 아버지 (abuji, modern).
  - **Usage**: Formal; very rarely diminutivized.
```

**Markdown vs. Wiki-links**: Use `[text](path)` markdown links for GitHub browsing; this ensures cross-linking works on both Obsidian and GitHub.

---

### 3. Intermediate (B1–B2)

**Who this is for**: Intermediate learners (Lessons 07–14); can handle compound words, subcategories, and specialized distinctions.

**What belongs here**: Expansions, refinements, and semantic subcategories not covered in A1–A2.

**Organization**: By semantic **subtopic** (e.g., in Kinship: "Consanguine Relatives," "Affinal Relatives," "Fictive Kin"). This makes vocabulary clusters memorable.

**Format**:
```markdown
### [Subcategory]

- <ruby>[Word](word.md)<rt>ruby</rt></ruby>: Definition.
  - **Etymology / notes**: Explain how this differs from or builds on A1–A2 vocabulary.
```

**Example**:
```markdown
### Extended Patrilineal Relations

- <ruby>[伯父](words/伯父.md)<rt>ㄅㄚㄍㄚ</rt></ruby>: Paternal uncle (father's elder brother).
  - **Note**: Distinct from 叔父 (paternal uncle, father's younger brother). 
  - **In Dan'a'yo**: Follows Classical Chinese convention; Modern Mandarin merges both as 伯伯.

- <ruby>[叔父](words/叔父.md)<rt>ㄕㄚㄍㄚ</rt></ruby>: Paternal uncle (father's younger brother).
  - **Etymology**: 叔 originally meant "uncle" in Old Chinese; 父 clarifies the paternal line.
```

---

### 4. Advanced / Specialized (C1+)

**Who this is for**: Advanced learners, scholars, fiction writers building worldbuilding; learners tackling classical texts or idiomatic expressions.

**What belongs here**: Rare terms, technical vocabulary, archaic distinctions, or terms specific to specialized domains (law, literature, science fiction, religion).

**Organization**: By historical period, register, or specialized context.

**Format**: Same as B1–B2, but include:
- Historical usage (archaic, obsolete)
- Register (ceremonial, literary, poetic)
- Frequency note (rare, literary only, SFF-original)

**Example**:
```markdown
### Archaic & Ceremonial Terms

- <ruby>[嫡嗣](words/嫡嗣.md)<rt>ㄉㄧㄙㄧ</rt></ruby>: Legitimate heir; son of the primary wife.
  - **Historical**: Common in classical genealogies; rare in modern contexts.
  - **Register**: Literary, ceremonial, legal/genealogical texts.
  - **Etymology**: 嫡 = legitimate; 嗣 = heir. Specific to patrilineal inheritance systems.

### Science Fiction & Speculative Terms

- <ruby>[義姉妹](words/義姉妹.md)<rt>ぎしまい</rt></ruby>: Sworn sisters; bonded-by-oath siblings (not biological).
  - **Status**: Common in Classical Chinese narrative (武侠); Dan'a'yo preserves this term.
  - **Modern use**: Fantasy/wuxia fiction, historical narratives.
```

---

### 5. Semantic Range Notes

**Purpose**: Explicitly address how Dan'a'yo's semantic boundaries differ from source languages or English.

**Length**: 1–3 paragraphs.

**What to cover**:
- Does Dan'a'yo **merge** concepts that other languages split? (e.g., "see" vs. "look" in English, but one word in many Asian languages)
- Does Dan'a'yo **split** concepts that other languages merge? (e.g., multiple copulas: 是, 有, 在)
- Are there cultural/philosophical assumptions built into the vocabulary? (e.g., kinship systems reflect patrilineal descent)
- What's unique to Dan'a'yo (if anything)?

**Example**:
```markdown
## Semantic Range Notes

Dan'a'yo's kinship system closely follows Classical Chinese, which distinguishes **generational depth**, **seniority within generation**, **biological vs. affinal relation**, and **patrilineal vs. matrilineal descent**. This differs markedly from English, which uses minimal affixation (uncle, aunt, cousin) and treats most extended relations as optional descriptors.

Notably, Dan'a'yo does **not** distinguish gender of the addressed person in second-person pronouns—both 君 (you singular) and 君等 (you plural) are gender-neutral, unlike Japanese's register-laden 彼 vs. 彼女. The language instead marks politeness via the suffix 公, applied to noun phrases rather than pronouns.

Matrilineal and step-relations are productive through affixation (e.g., 外伯父 "maternal uncle," literally "outside uncle"), but in classical texts these are less frequently instantiated than patrilineal terms, reflecting the historical dominance of patrilineal society in the Sinosphere.
```

---

### 6. See Also

**Purpose**: Cross-reference related domains, grammar chapters, and idiomatic uses.

**Format**:
```markdown
## See Also

**Related domains**:
- [[Emotions]] — expressions of familial affection
- [[Time]] — generational markers (ancestor, descendant)
- [[Society]] — social roles derived from kinship (elder, younger)

**Grammar chapters**:
- [Nominalization (–事, –物)](../grammar/文法\ -\ 05形態.en.md) — how kinship terms nominalizes ("being a father is difficult")
- [Postpositions](../grammar/文法\ -\ 05形態.en.md) — marking kinship relations with 之 (possessive) or 于 (dative)

**Idiomatic uses**:
- 老父 — respectful way to refer to one's own father (literally "old father")
- 親友 — family and close friends; intimate circle
- 骨肉相殘 — kin turning against each other (literally "bone and flesh harming each other")

**Example lesson**:
- [Lesson 05: Nouns, Pronouns & Copulas](../lessons/lesson-outline.md#lesson-05-nouns-pronouns--simple-copulas)
```

---

## General Formatting Rules

### Links
- **Internal word files**: Use markdown links `[text](path/to/word.md)` for cross-platform compatibility
- **Internal wiki-links** (Obsidian-only): Use `[[text]]` for Obsidian navigation, but **avoid** mixing styles in the same file
- **Ruby text**: Use HTML `<ruby>字<rt>ㄓ</rt></ruby>` for Bopomofo pronunciation

### Markdown Style
- **Headings**: Use `#` (H1) for domain title, `##` (H2) for tier sections, `###` (H3) for subcategories
- **Bold**: Use for word **type** (Etymology, Cross-ling, Usage, etc.)
- **Emphasis** (*italics*): Use sparingly; prefer bold for clarity
- **Code blocks**: Not needed for vocabulary lists; use plain text with ruby annotations

### Character & Bopomofo
- Always include Bopomofo ruby text for Dan'a'yo words
- Example: `<ruby>[魚](words/魚.md)<rt>⼄</rt></ruby>`
- Omit ruby for non-Dan'a'yo language examples (e.g., Mandarin, Japanese) unless pronunciation is non-obvious

### Word Boundaries

When a domain overlaps with another (e.g., Colors used in Clothing, or Kinship in Society):
- **Do not duplicate** — link to the primary domain instead
- **Example**: In Clothing, instead of listing "blue fabric," write "[[Color|blue]] fabric," linking to the Color domain
- This keeps each domain lean and encourages cross-domain thinking

---

## Domain Status Definitions

### New
- Framework/outline only
- < 200 words of actual vocabulary
- Frontmatter `status: new`
- **Next step**: Fill A1–A2 tier with core 15–20 terms

### Stub
- Some content, but incomplete
- 200–500 words
- Mostly A1–A2; B1–B2 tier missing or sparse
- **Next step**: Expand B1–B2 with subcategories and intermediate vocabulary

### Partial
- Two tiers substantially filled
- 500–1500 words
- A1–A2 and B1–B2 present; C1+ minimal or missing
- **Next step**: Add advanced/rare vocabulary and semantic range notes

### Complete
- All three tiers filled
- 1500+ words
- "Semantic Range Notes" and "See Also" sections present
- Ready for publication/pedagogy
- **Maintenance**: Review for outdated links; add new words as they're created

---

## Template File

Use this as a starting point for new domains:

````markdown
---
language: English
type: lexipedia
domain: [Domain Name]
related_domains: [[Domain1]], [[Domain2]]
status: new
---

# [Domain Name]

[1–2 sentence overview of domain and why it matters.]

## Core Vocabulary (A1–A2)

[Ordered by frequency or semantic subcategory]

- <ruby>[Word](words/Word.md)<rt>ruby</rt></ruby>: Definition.
  - **Literal meaning**: [if applicable]
  - **Cross-ling**: [Mandarin, Cantonese, Japanese, Korean equivalents]
  - **Usage**: [register, connotation, common phrases]

## Intermediate (B1–B2)

### [Subcategory 1]

[Vocabulary organized by semantic subtopic]

### [Subcategory 2]

[Vocabulary organized by semantic subtopic]

## Advanced / Specialized (C1+)

[Rare, technical, archaic, or specialized vocabulary]

## Semantic Range Notes

[How Dan'a'yo's semantic boundaries differ from source languages or English.]

## See Also

**Related domains**:
- [[Domain1]]
- [[Domain2]]

**Grammar chapters**:
- [Chapter Name](../grammar/path)

**Idiomatic uses**:
- Term — meaning

**Example lesson**:
- [Lesson N](../lessons/lesson-outline.md#lesson-n)
````

---

## Rationale

This format serves multiple audiences:

1. **Learners** (A1–B2): Can focus on Core and Intermediate tiers, skipping Advanced
2. **Teachers**: Can use "See Also" section to cross-reference grammar lessons and idiomatic contexts
3. **Scholars & writers**: Can drill down into Advanced tier and Semantic Range notes for nuance
4. **Maintainers**: Consistent structure makes it easy to audit coverage and add new domains
5. **GitHub users**: Markdown links + HTML ruby work seamlessly across Obsidian and web browsers

---

## Example: Completed Domain (Partial → Complete)

See **[[Swadesh]]** and **[[Calendar]]** for working examples of near-complete domains.

As a reference, **[[Body]]** is currently Partial; **[[Animals]]** is Stub; **[[Food]]** is New.

