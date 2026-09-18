---
name: project-lexipedia-format-migration
description: "Active (2026-09-17) - migrating existing lexipedia domain pages to the format.md template; 2/19 in-scope pages done"
type: project
---

**Status: active, 2 of 19 in-scope pages done.** `lexipedia/format.md` specifies a template every "domain page" should follow: frontmatter (`type: lexipedia`, `domain`, `related_domains`, `status: new|stub|partial|complete`), then `# Domain` → Domain Overview → `## Core Vocabulary (A1–A2)` → `## Intermediate (B1–B2)` with `###` subcategories → `## Advanced / Specialized (C1+)` → `## Semantic Range Notes` → `## See Also`. **On audit (2026-09-17), zero of the 28 existing files in `lexipedia/` followed this template** — not just the two pages worked on this session (Numbers, Metals), but also spot-checked `Color.md` and `Elements.md`, both plain flat lists with `language: English` frontmatter only. `format.md` had never actually been applied to the real corpus.

## Scope, established by reading `lexipedia/Lexipedia.md` (the index page) closely

`Lexipedia.md` itself distinguishes three categories, which sets the real scope of this migration:

1. **~50 "domain pages"** in the main bulleted list, explicitly told to follow `format.md` ("See format.md... before creating or expanding a domain page below"). Of these, **only ~21 currently have a file** (the rest — Existence, Government, Kinship, Knowledge, Law, Life, Light, Locatives, Love, Measurement, Mind, Movement, Nature, Physical, Physics, Plants, Possession, Religion, Shape, Sensation, Sex, Sin, Society, Speech, Substances, Time, Tools, Trade, Valuation, War — are red-linked, no content exists at all). **This project is about migrating the existing files, not authoring the ~29 missing ones — that's a separate, much larger content-creation task, explicitly out of scope here unless the user asks for it directly.**
2. **A separate "## Swadesh" section** listing `[[Swadesh]]` and `[[Sophomore List]]` — Rosenfelder's own distinct word-frequency lists, structurally different (Swadesh is a giant cross-linguistic comparison table; it already has its own completed, separately-tracked audit — see `project_swadesh_audit.md` in the assistant's memory). **Excluded from this migration.**
3. **A separate "## Others" section**, explicitly captioned "functional IAL self-description" rather than domain vocabulary: `Geography`, `Calendar`, `Periodic Table`. **Excluded from this migration** — this independently validates the judgment call already made on `Periodic Table.md` earlier this session (it's a reference table, not a tiered vocabulary page) and extends the same reasoning to Geography and Calendar.

`基督敎.md` and `歴史綱要.md` are not listed in `Lexipedia.md`'s index at all — different content type (religious/historical encyclopedic content, not domain vocabulary), **excluded from this migration**.

## In-scope file list (19 remaining, sorted by size — smallest first, cheapest to migrate)

- [x] **Numbers** (2026-09-17, done this session)
- [x] **Metals** (2026-09-17, done this session)
- [ ] Elements (26 words) — likely trivial, near-empty stub; may just need the 7-element "Main" list (air/earth/fire/metal/stone/water/wood/ether) organized into tiers plus a Domain Overview
- [ ] Conflict (46 words)
- [ ] Work (52 words)
- [ ] Clothing (63 words)
- [ ] Efforts (64 words)
- [ ] Containers (66 words)
- [ ] Directions (75 words)
- [ ] Events (103 words)
- [ ] Water (111 words)
- [ ] Art (115 words)
- [ ] Emotions (124 words)
- [ ] Food (128 words)
- [ ] Dimensions (144 words)
- [ ] Color (181 words)
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
7. Set `status: complete` once genuinely done; run a final script check for broken links and duplicate `注音` readings within the page before moving on.

## Note for whoever resumes this

This is real content-authoring work per page (Domain Overview + Semantic Range Notes are not mechanical), not a linking/verification sweep — budget accordingly. The smallest pages (Elements, Conflict, Work, Clothing) are good next targets to keep momentum without a huge single-session commitment.
