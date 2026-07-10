---
name: checklist-cc
description: Completion rubric for CC initials (聲 X.md) and finals (韻 X.md) pages — how a Middle Chinese initial/final evolved into its Dan'a'yo outcome(s) across the character corpus
metadata:
  type: checklist
---

# Checklist: CC Initials/Finals Pages

A CC page — `lookup/CC/initials/聲 X.md` or `lookup/CC/finals/韻 X.md` — documents how every character sharing one Middle Chinese initial or final actually resolved in Dan'a'yo: one dominant outcome, or a genuine split, with every exception explained or explicitly flagged as unexplained. The goal is a page a reader can use both as a lookup table (every character at this initial/final, grouped by outcome) and as the linguistic record of *why* that outcome happened. Distinct from [[AIOS/skills/skill_cc_phonology.md]] (how to build/derive the page) — this file is the pass/fail rubric for judging one that already exists.

Initials and finals pages share one structure; the only real difference between them is the frontmatter field name and the grouping rule (see below).

---

## Frontmatter

```yaml
---
size: N
middle_chinese_initial: X       # 聲 pages only
middle_chinese_final: X         # 韻 pages only — never both fields on the same page
date-last-perfect: YYYY-MM-DD
tags: [lookup]
---
```

**`size`** must equal the number of `<ruby>` entries in `## Characters` — no more, no less. This is the single most common defect: verify with `grep -o '<ruby>' <file> | wc -l` against the ground-truth count, never trust a pre-existing stated value.

**`middle_chinese_initial`**/**`middle_chinese_final`** must match, byte-for-byte including diacritics, the value used in the character corpus's own frontmatter for this initial/final — not a simplified or re-typed approximation. Watch for two real failure modes found in practice: diacritic-order typos on individual character files (`wɣæk` instead of `ɣwæk`), and Unicode look-alike confusion between `ə` (U+0259, schwa) and `ǝ` (U+01DD, turned e) — both render similarly but only one matches the corpus.

**`date-last-perfect`** is set only once every criterion below holds — not because a page merely has *a* date already.

---

## Opening

Immediately after frontmatter, two lines:

```markdown
> [Classical Chinese](../Classical%20Chinese.md)
> **Initial/Final X** [evolved into Y | mostly evolved into Y, with N exceptions | genuinely splits N ways]
```

The one-liner must accurately characterize the page's actual outcome shape — a single dominant winner, a dominant winner with exceptions, or a genuine multi-way split (see "Genuine splits" below). Don't default to exception-framing language for a final whose Vowels-table D value is itself documented as ambiguous.

---

## `## CJKV Evolution`

A prose section, not a bare list, covering:

1. **The dominant outcome** and what fraction of characters land there, with the Vowels-table (finals) or initials-evolution-table (initials) documented winner cited by name.
2. **Every non-majority character explained individually**, not lumped as "miscellaneous." Each one falls into one of these categories — identify which, don't just describe the outcome without diagnosing the mechanism:
   - **Crowding-driven escape**: the character's expected slot (by initial-letter or plain outcome) already holds one or more same-initial members, and this character dodges via vowel-shift, coda-shift, glide-add/drop, or (rarer) initial-letter substitution.
   - **True-homophone divergence**: two or more characters share identical (or near-identical) Mandarin/Cantonese/Korean readings yet land in different groups, with no crowding forcing it — a genuine unconditioned split, not a research gap. Check readings across *all* available daughter languages before calling something unexplained (see [[AIOS/skills/skill_cc_phonology.md]]'s daughter-language-check section) — Mandarin alone is not sufficient.
   - **Phonotactic constraint**: ㄉㄊㄑㄐ barred from y-glide; ㄈ barred from *on*-glides specifically (off-glides, i.e. coda glides after the vowel nucleus, are unaffected — don't conflate the two); ㄋㄌㄅㄆㄇ barred from w-glide. Cite the constraint by name rather than re-deriving it.
   - **Genuine initial-conditioned rule**: a real phonological split (e.g. plain vs. aspirated, voiced vs. voiceless) that holds with zero exceptions across every member — distinguish this explicitly from an unconditioned same-initial-arbitrary-outcome split, which looks superficially similar but has counter-examples.
   - **Corpus data-quality flag**: a character's own Mandarin/Cantonese/Korean/Japanese/Vietnamese fields are internally inconsistent (don't match each other or the character's own stated MC initial), suggesting a copy-paste or transcription error in the source data. Flag it in prose; don't silently "fix" the character's frontmatter as part of a CC-page pass unless the mismatch is unambiguous (e.g. a field value that plainly belongs to a different, identifiably-named character).
3. **Genuine splits** — when the relevant reference table itself documents more than one valid outcome for this initial/final (e.g. a finals-table D value like `ǝ/o/ung` or `im/um/om`), and the corpus shows real population across more than one group with no single group holding a clear supermajority, say so explicitly rather than forcing exception-framing onto what is actually a documented multi-way outcome. This is a distinct, valid page shape — not a defect.

Citing prior pages by name (`[[韻 X|X]]`) when the same pattern recurs elsewhere in the corpus is expected practice, not optional flourish — it's how the corpus-wide pattern catalog in `skill_cc_phonology.md` gets built and cross-referenced.

---

## `## Characters` → `### In Use`

One bullet per outcome group, in descending order by group size (largest/dominant group first):

```markdown
- [outcome]: <ruby>[[Char (char)|Char]]<rt>注音</rt></ruby>, <ruby>[[Char2]]<rt>注音</rt></ruby>, ...
```

- **Initials pages**: the outcome label is the resulting Dan'a'yo *initial letter* (ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄐㄑㄙㄏ, or `ø` for null-initial).
- **Finals pages**: the outcome label is the resulting Dan'a'yo *final* — 注音 with any leading initial letter stripped off. Never include the initial letter in a final-page group label, even for a character whose final genuinely is exceptional (label is the final substring alone, e.g. `⼜ㄎ`, never `ㄙ⼜ㄎ`). Before accepting a final-page group as a genuine exception, check whether the odd spelling is actually just initial-driven glide fusion (null/glide-type MC initials fuse into a single vowel-letter, e.g. ⼜ = "yu") rather than a real final-level fact — fold those into the main group instead of treating them as a separate outcome.
- Every character uses a ruby-annotated link (`<ruby>...<rt>注音</rt></ruby>`), pipe-aliased (`[[X (char)|X]]`) when the character's filename carries the ` (char)` suffix.
- Total ruby count across all groups equals `size` exactly.
- Every character whose corpus frontmatter carries this exact initial/final value appears exactly once, in the group matching its own `注音`; no character appears twice, and no character not actually carrying this initial/final appears at all.

---

## `## Datacheck`

```base
version: 1
views:
  - type: table
    name: Initial X   # or Final X
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_initial == "X"   # or middle_chinese_final
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - middle_chinese_initial
      - middle_chinese_final
      - 注音
    sort:
      - property: 羅馬字
        direction: ASC
      - property: middle_chinese_initial
        direction: ASC
      - property: characters
        direction: DESC
      - property: grade_level
        direction: ASC
    columns:
      - file
      - file.path
      - file.links.length
    columnSize:
      note.mandarin: 59
      note.cantonese: 71
      note.korean: 43
      note.middle_chinese_initial: 97
```

The `file.inFolder("characters")` filter is mandatory, not optional — its absence is the single most common inherited stub defect (see below) and silently inflates the apparent character count by exactly one, since the lookup page's own frontmatter also carries the `middle_chinese_initial`/`middle_chinese_final` field being queried. The filter value must match frontmatter's stored initial/final string exactly.

---

## `date-last-perfect` criteria

Set only when:

1. Frontmatter's `size` matches the ground-truth character count (`grep -lE '^middle_chinese_initial: "?X"?$' characters/*.md | wc -l`, swapping in `middle_chinese_final` for finals pages) **and** matches the page's own ruby-tag count.
2. Every non-majority character is individually explained in `## CJKV Evolution` under one of the categories above — none left as a bare list entry with no accompanying prose diagnosis.
3. Group labels on finals pages never embed the initial letter; initial-driven glide fusion has been folded into the main group where applicable.
4. `## Datacheck` includes the `file.inFolder("characters")` filter and its filter value matches frontmatter exactly.
5. The one-liner under the breadcrumb accurately reflects the page's actual outcome shape (dominant/dominant-with-exceptions/genuine-split).

---

## Common mistakes

- **Missing `file.inFolder("characters")` filter** — inherited from old stub pages; inflates the apparent `size` by 1 (the lookup page's own frontmatter self-matches).
- **Stated `size` never verified against ground truth** — the most common single defect across both initials and finals; corrections found in practice ranged from ±1 up to +42.
- **Finals-page group label includes the initial letter** — always strip it; the label is the final substring only.
- **Null/glide-initial glide fusion mistaken for a final-level exception** — check the character's own `middle_chinese_initial` before treating an odd-looking final spelling as a genuine exception; fold initial-driven fusion into the main group instead.
- **ㄈ's on-glide ban misapplied to off-glides** — an off-glide coda (the ㄧ in ㄈㄨㄧ, where ㄨ is the vowel nucleus) is not a violation; only a medial on-glide between the initial and the vowel is barred.
- **Exceptions explained by Mandarin alone** — check Cantonese, Korean, and Vietnamese too before calling something unexplained.
- **A genuinely ambiguous final treated as one dominant outcome plus exceptions** — when the Vowels table itself lists more than one D value for a final and the corpus shows real multi-group population, describe it as a genuine split.
- **Ruby count not re-verified after editing** — always re-run `grep -o '<ruby>' <file> | wc -l` against the final `size` immediately before stamping.
