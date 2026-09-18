---
name: checklist-lexipedia
description: Completion rubric for lexipedia domain pages — tiered vocabulary structure, frontmatter, and the Dan'a'yo-specific semantic-divergence requirement
metadata:
  type: checklist
---

# Checklist: Lexipedia Domain Pages

A lexipedia domain page (`lexipedia/*.md`, e.g. `Metals.md`, `Numbers.md`, `Kinship.md`) groups Dan'a'yo's existing vocabulary by semantic field — Animals, Kinship, Emotions, and the like — organized by learner level (A1 through C1+). It is not just an index of already-perfected words: it is the site where Dan'a'yo's own semantic boundaries get worked out, independent of any single source language. See [[AIOS/memory/feedback_lexipedia_semantic_differentiation.md]] for the philosophy, and [[AIOS/checklists/checklist_words.md]] for the reciprocal requirement — as of 2026-09-18, a word being newly perfected must link into a page like this one.

This checklist is distinct from the domain-list pages this vault treats as a different category: Swadesh, Sophomore List (Rosenfelder frequency lists, flat structure, no tiers), and Geography/Calendar/Periodic Table (functional IAL self-description, not semantic-field vocabulary — see `lexipedia/Lexipedia.md`'s own "Others" grouping). Nothing below applies to those.

---

## Frontmatter

Four fields, all required:

```yaml
---
language: English
type: lexipedia
domain: Metals                 # exact domain name, matches the filename
related_domains:
  - "[[Periodic Table]]"       # real YAML list — quoted wikilink strings, one per line
  - "[[Color]]"
status: complete                # new | stub | partial | complete
date-last-perfect: YYYY-MM-DD   # set only once every criterion below is met; leave absent otherwise
---
```

**`related_domains` must be a real YAML list**, not `related_domains: [[Domain1]], [[Domain2]]` on one line — that form is invalid YAML (the double-bracket nesting closes as a complete flow-sequence after the first token, leaving trailing comma-separated garbage that Obsidian reports as "Invalid properties"). Always use quoted wikilink strings, one per list item, as shown above. This exact bug was found live in both `format.md`'s own template and two migrated pages (Numbers, Metals) on 2026-09-17 — verify with a YAML parse, not just a glance, after editing this field.

**`status`** and **`date-last-perfect`** are not redundant — `status` tracks how far the page's *coverage* has grown (see Domain Status Definitions below), while `date-last-perfect` is the audit stamp confirming everything currently on the page is *correct*, matching the convention every other content type in this vault uses. A page can be `status: complete` with a stale `date-last-perfect` (or none at all) if it hasn't been audited since a linked word changed.

---

## Body structure

### 1. Domain Overview

2–4 sentences, immediately after the `# Domain` heading: what this domain covers and why it matters for Dan'a'yo learners. Not a bare one-line gloss.

### 2. Core Vocabulary (A1–A2)

High-frequency, universal concepts — overlaps with the Swadesh list or basic conversation. Each entry:

```markdown
- <ruby>[Word](words/Word.md)<rt>注音</rt></ruby>: definition.
```

Add `**Literal meaning**`, `**Cross-linguistic notes**`, or `**Usage note**` sub-bullets only where they add real content — don't pad every entry with all three if there's nothing non-obvious to say.

### 3. Intermediate (B1–B2)

Organized into `###` subcategories by semantic subtopic (e.g. "Precious & Structural Metals," "Alloys & Related Metals") — this is what makes a vocabulary cluster memorable, not a flat continuation of the A1–A2 list.

### 4. Advanced / Specialized (C1+)

Rare, technical, archaic, or register-specific vocabulary. Same entry format as B1–B2, with historical/register/frequency notes where relevant (e.g. "literary only," "SFF-original").

### 5. Semantic Range Notes

1–3 paragraphs, required. This is the section that does the actual work described in [[AIOS/memory/feedback_lexipedia_semantic_differentiation.md]]: does Dan'a'yo merge concepts other languages split, or split concepts other languages merge? Where a word's Dan'a'yo-specific sense diverges from the shared CJKV/international meaning, state it here explicitly — and also in that word's own `## Notes` section per `checklist_words.md`, not only here. Most words need no divergence stated at all; don't force one that isn't real.

### 6. See Also

```markdown
## See Also

**Related domains**:
- [[OtherDomain]] — why it's related

**Grammar chapters** *(if relevant)*:
- [Chapter](../grammar/path)

**Idiomatic uses** *(if any)*:
- [[word]] — figurative meaning
```

Every entry under **Idiomatic uses** must be a real, existing vault word — verify the file exists before listing it. A plausible-sounding invented example (e.g. a compound that looks like it should exist but doesn't) was caught and removed from `Metals.md` during its 2026-09-17 perfection pass; don't repeat that mistake.

---

## General formatting rules

- **Links**: markdown `[text](path/to/word.md)` for word files, so links work on both Obsidian and GitHub; `[[wikilink]]` only for `related_domains` and cross-domain references. Don't mix styles for the same kind of link within one file.
- **Ruby text**: `<ruby>[Word](path)<rt>注音</rt></ruby>` for every Dan'a'yo word. Omit ruby for non-Dan'a'yo comparison forms (Mandarin, Japanese, etc.) unless the pronunciation is non-obvious.
- **Don't duplicate across domains**: when a concept belongs primarily to another domain (e.g. a color mentioned inside Clothing), link to that domain instead of re-describing it — `[[Color|blue]] fabric`, not a redefinition.
- **Don't cache readings inline that can drift**: a word's 注音 shown here must match its own word-file frontmatter. Lexipedia pages have twice been found silently out of sync with a word file corrected after the fact (Metals' "lead"/"alloy" entries; a full duplicate table found on `lookup/List of 新語.md`) — when auditing, re-verify every ruby reading against its source word file, don't assume a page that "looks right" still is.

---

## Domain Status Definitions

| `status`  | Coverage                                              | Next step                                      |
|-----------|--------------------------------------------------------|-------------------------------------------------|
| `new`     | Framework/outline only, <200 words of vocabulary        | Fill Core (A1–A2) with 15–20 terms               |
| `stub`    | 200–500 words, mostly Core, Intermediate sparse/missing | Expand Intermediate with real subcategories      |
| `partial` | 500–1500 words, Core + Intermediate present, Advanced thin | Add Advanced vocabulary + Semantic Range Notes |
| `complete`| 1500+ words, all three tiers filled, Semantic Range Notes and See Also present | Maintenance: re-audit when linked words change |

---

## `date-last-perfect` criteria

Set it once, and only once, all of the following hold:

1. Frontmatter complete and valid (`language`, `type`, `domain`, `related_domains` as a real YAML list, `status`).
2. `status: complete` — all three vocabulary tiers substantively filled, not just Core.
3. Every listed word is a real, existing vault file — no invented compounds (verify each link resolves).
4. Every entry's chosen word actually carries the sense being claimed — a plausible-looking existing link isn't automatically correct; check the word's own Notes to confirm it means what this page says it means (a real bug: `同等` would have been wrongly linked as general "equal" on `Numbers.md` before its own Notes ruled that sense out).
5. Every ruby-text 注音 reading matches its word file's current frontmatter — no stale cached readings.
6. `## Semantic Range Notes` present with real content — genuine divergence stated where it exists, and no divergence invented where it doesn't.
7. `## See Also` present, `related_domains` entries reciprocated where the other domain page exists, and every idiomatic-use example verified to be a real vault word.

---

## Common mistakes

### Wrong relative path to word files

From `lexipedia/DomainName.md`, a word file link must be `../words/Word.md` — not `words/Word.md` (missing `../`, resolves to a nonexistent `lexipedia/words/` and only "works" in Obsidian if it falls back to filename search) and not `/words/Word.md` (leading-slash absolute, resolves fine in Obsidian but breaks on GitHub, defeating the dual-compatibility purpose of using markdown links at all — see General Formatting Rules above). Found in both directions across `Numbers.md` (leading-slash) and `Metals.md` (missing `../`) on 2026-09-18; fixed on both, plus caught pre-emptively while drafting `Color.md`. Check every lexipedia page's word links with `grep -n "](/words/\|](words/"` before trusting them.

### Broken `related_domains` YAML

`related_domains: [[Domain1]], [[Domain2]]` on one line is invalid YAML and breaks Obsidian's property parser ("Invalid properties"). Always write it as a real list of quoted wikilink strings — see Frontmatter above.

### Stale cached readings

A word's 注音 shown on a lexipedia page can silently drift out of sync when the word file itself is later corrected. Re-verify against the source word file when auditing, not just on creation.

### Treating `status: complete` as sufficient for `date-last-perfect`

`status` measures coverage; `date-last-perfect` measures verified correctness. A page can honestly be `status: complete` and still fail several of the criteria above (stale readings, an unverified idiomatic example, a semantically wrong link) — check all seven criteria, not just tier coverage.

### Inventing a Dan'a'yo-specific sense with no real basis

Semantic Range Notes should report genuine divergence, not manufacture some to look thorough. See [[AIOS/memory/feedback_lexipedia_semantic_differentiation.md]] — most words correctly keep the shared CJKV sense.

### Fabricating a plausible-sounding idiomatic example

Don't list an idiomatic use, alloy note, or cross-reference that sounds right without confirming the word file actually exists. Caught once already on `Metals.md` (a fabricated "点金術" entry, removed before publishing).
