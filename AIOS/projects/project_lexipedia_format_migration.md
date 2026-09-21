---
name: project-lexipedia-format-migration
description: "Active (2026-09-17) - migrating existing lexipedia domain pages to the checklist_lexipedia.md template; 3/19 in-scope pages done"
type: project
---

**Status: active, 4 of 19 in-scope pages done.** [[AIOS/checklists/checklist_lexipedia.md]] (moved 2026-09-18 from `lexipedia/format.md`, which had been living as vault content despite being a how-to-validate page — see that checklist's own note) specifies a template every "domain page" should follow: frontmatter (`type: lexipedia`, `domain`, `related_domains`, `status: new|stub|partial|complete`, `date-last-perfect`), then `# Domain` → Domain Overview → `## Core Vocabulary (A1–A2)` → `## Intermediate (B1–B2)` with `###` subcategories → `## Advanced / Specialized (C1+)` → `## Semantic Range Notes` → `## See Also`. **On audit (2026-09-17), zero of the 28 existing files in `lexipedia/` followed this template** — not just the two pages worked on this session (Numbers, Metals), but also spot-checked `Color.md` and `Elements.md`, both plain flat lists with `language: English` frontmatter only. The template had never actually been applied to the real corpus.

## Scope, established by reading `lexipedia/Lexipedia.md` (the index page) closely

`Lexipedia.md` itself distinguishes three categories, which sets the real scope of this migration:

1. **~50 "domain pages"** in the main bulleted list, explicitly told to follow `format.md` ("See format.md... before creating or expanding a domain page below"). Of these, **only ~21 currently have a file** (the rest — Existence, Government, Kinship, Knowledge, Law, Life, Light, Locatives, Love, Measurement, Mind, Movement, Nature, Physical, Physics, Plants, Possession, Religion, Shape, Sensation, Sex, Sin, Society, Speech, Substances, Time, Tools, Trade, Valuation, War — are red-linked, no content exists at all). **This project is about migrating the existing files, not authoring the ~29 missing ones — that's a separate, much larger content-creation task, explicitly out of scope here unless the user asks for it directly.**
2. **A separate "## Swadesh" section** listing `[[Swadesh]]` and `[[Sophomore List]]` — Rosenfelder's own distinct word-frequency lists, structurally different (Swadesh is a giant cross-linguistic comparison table; it already has its own completed, separately-tracked audit — see `project_swadesh_audit.md` in the assistant's memory). **Excluded from this migration.**
3. **A separate "## Others" section**, explicitly captioned "functional IAL self-description" rather than domain vocabulary: `Geography`, `Calendar`, `Periodic Table`. **Excluded from this migration** — this independently validates the judgment call already made on `Periodic Table.md` earlier this session (it's a reference table, not a tiered vocabulary page) and extends the same reasoning to Geography and Calendar.

`基督敎.md` and `歴史綱要.md` are not listed in `Lexipedia.md`'s index at all — different content type (religious/historical encyclopedic content, not domain vocabulary), **excluded from this migration**.

## In-scope file list (19 remaining, sorted by size — smallest first, cheapest to migrate)

- [x] **Numbers** (2026-09-17, done this session)
- [x] **Metals** (2026-09-17, done this session)
- [x] **Color** (2026-09-18) — 31 real vocabulary entries (the "181 words" estimate above was a prose-length heuristic, not an entry count). All 31 word pages backlinked. Found and fixed 3 broken word pages while touching them for the backlink: `赤.md` was stamped `date-last-perfect` but had an empty `# Notes` (wrong heading level) and a malformed scalar `characters:` field — rebuilt with real content; `紫色.md` had no Notes section at all despite its stamp — rebuilt, plus filled its blank `vietnamese` field; `蒼.md` and `黄金.md` (from the Metals pass) had the missing-`../`-prefix link bug, fixed. Also found and fixed the domain page's own version of that same missing-`../` bug on **both** `Numbers.md` (was using GitHub-breaking leading-slash `/words/`) and `Metals.md` (was using Obsidian-fragile bare `words/`) — see `checklist_lexipedia.md`'s new "Wrong relative path to word files" entry.
- [ ] Elements (26 words) — likely trivial, near-empty stub; may just need the 7-element "Main" list (air/earth/fire/metal/stone/water/wood/ether) organized into tiers plus a Domain Overview
- [ ] Conflict (46 words)
- [x] **Work** (2026-09-21) — original page was 25 flat entries (24 bullets + a 1-item "Addendum"), not 52 (another prose-length overestimate). Migrated to 34 vocabulary entries across 8 Core / 14 Intermediate (2 subcategories) / 12 Advanced (2 subcategories) entries, all from pre-existing perfected words (no new coinage needed) — a `words/` grep on each original English gloss's `english:` frontmatter list turned up a real match every time. Backlinked all 33 newly-cited words' `## Notes` with `- See [Work](../lexipedia/Work.md).` (`術.md` already existed but was genuinely broken — see below). Found and fixed 3 real bugs while touching pages for the backlink: (1) `製品.md`'s `characters:` field cited bare `品` instead of `"品 (char)"`, the missing-`(char)`-suffix bug documented in `checklist_words.md`; (2) `術.md` (linked for "skill, method, technique," the base morpheme under 技術/芸術) had a stamped `date-last-perfect` despite a completely empty `## Notes` section and missing `japanese`/`vietnamese`/`pos` fields — rebuilt properly with real content and re-stamped; (3) a genuine vault-integrity bug: `工場.md` wrongly listed `工廠` as an `aliases` entry, but `工廠` is independently the `stand_in` that legitimizes the character `廠` and carries its own distinct Dan'a'yo pronunciation (ㄍㄛㄫㄑㄚㄫ vs. 工場's ㄍㄛㄫㄐㄚㄫ) — an alias can never be used independently per vault convention, so this was a real contradiction, not a stylistic issue; fixed by removing the alias entry and documenting the correction on both word pages and in Work's own Semantic Range Notes. Semantic Range Notes covers three genuine near-synonym clusters: the build trio (建築/建設/構築, by object/formality/abstraction), the repair trio (修理/修繕/修補, by object/register) plus the maintain pair (維持/保持, general vs. retentive-of-status-quo) and the factory-word bug, and the supply/toil pairs (提供/供給, 労動/辛苦) — plus an honest note that Dan'a'yo has no dedicated "craft" word (the closest fit, 芸術, belongs to the Art domain and is cross-referenced rather than duplicated).
- [ ] Clothing (63 words)
- [ ] Efforts (64 words)
- [ ] Containers (66 words)
- [ ] Directions (75 words)
- [ ] Events (103 words)
- [~] **Water** (started 2026-09-21, Core tier only) — original page was 3 flat sections (16-item unlabeled "general" list, "## Bodies of Water" 20 items, "## Ships" ~23 items across three lines), not 111 (another prose-length overestimate). Only the unlabeled first section has been migrated to `## Core Vocabulary (A1–A2)` so far, per explicit user instruction to do "just the first section" this pass — `## Bodies of Water` and `## Ships` remain below in their original raw form, untouched, for a future session. `status: stub` (no `date-last-perfect` — page is genuinely incomplete). 14 of the 16 original glosses matched existing perfected words via the same `english:`-field grep method as Work; "spill" had no attested match and was flagged as a documented gap rather than force-mapped (same treatment as "craft" on Work) — a coinage decision to make on a future pass, not decided unilaterally here. "ice" and "wave" both resolve to compounds (氷水, 波浪) rather than bare nouns, because 氷 and 波 are both bound characters in this vault with no independent word page of their own — 氷水 for "ice" matches the resolution already reached independently on Swadesh item #165, so this isn't a new judgment call. Backlinked all 14 cited words with `- See [Water](../lexipedia/Water.md).`; no bugs found needing correction this pass (unlike Work).
- [ ] Art (115 words)
- [ ] Emotions (124 words)
- [ ] Food (128 words)
- [ ] Dimensions (144 words)
- [ ] Animals (223 words)
- [ ] Buildings (234 words)
- [ ] Grammar (261 words) — borderline case: functional/grammatical vocabulary rather than a concrete semantic domain, but it IS listed in Lexipedia.md's main domain index, so in scope; may need a judgment call on how literally to apply the A1-C1 tiering to grammatical categories.
- [ ] Body (446 words)
- [ ] Astronomy (515 words)

## Migration method, established by the Numbers/Metals work this session

1. Read the existing page in full; do **not** discard any existing content — every linked word gets preserved, just reorganized.
2. Verify every existing ruby-link entry: file exists, `注音` matches the linked word's own current stored value (lexipedia pages cache readings inline and silently drift when the underlying word is later corrected — found and fixed 2 stale readings on Metals this way, e.g. `合金`'s reading had been fixed on the word page in an earlier session but never propagated back here).
3. Sort existing entries into A1–A2 (absolute-core vocabulary) / B1–B2 (expanded, with `###` semantic subcategories) / C1+ (specialized/technical) by genuine difficulty and centrality — don't force an arbitrary split.
4. Write a real Domain Overview (2–4 sentences) and real Semantic Range Notes (the substantive part — document genuine cross-linguistic divergences found during the word-level work, not filler prose).
5. Build a See Also section with real, verified links only — checked at least one fabricated idiomatic-use example out during the Metals migration (点金術 doesn't exist as a word; caught before publishing, replaced with a verified real one).
6. Add `related_domains` only to domains that actually have files (or, per Numbers, one or two functionally-related "Others" pages like Periodic Table/Calendar, since those remain useful cross-references even though they don't follow this same template themselves).
7. Set `status: complete` and `date-last-perfect` once every criterion in [[AIOS/checklists/checklist_lexipedia.md]] is met; run a final script check for broken links and duplicate `注音` readings within the page before moving on.

## Note for whoever resumes this

This is real content-authoring work per page (Domain Overview + Semantic Range Notes are not mechanical), not a linking/verification sweep — budget accordingly. The smallest pages (Elements, Conflict, Work, Clothing) are good next targets to keep momentum without a huge single-session commitment.
