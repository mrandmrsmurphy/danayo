---
name: skill-lint
description: Argument-driven bulk-consistency sweep over one content type at a time (e.g. "lint SKIP"). Cross-references lookup pages against the character/word corpus to find gaps, truncated previews, stale entries, and stamps date-last-perfect once verified.
type: skill
---

# Skill: Lint

The vault is too large and heterogeneous for one linter to cover everything at once. `lint` always takes an argument naming *what* to sweep — `lint SKIP`, and later `lint Radicals`, `lint Stroke`, `lint Syllables`, etc. Each argument gets its own procedure section below, grounded in that content type's `AIOS/checklists/checklist_*.md` rubric. Don't run `lint` bare.

## General shape of a lint pass

1. **Ground truth first.** Every lookup tree (SKIP, Radicals, Stroke, ...) is a derived index over the real data in `characters/` (and sometimes `words/`). Before touching any lookup page, grep the corpus for the field that tree is indexing (`skip_number`, `radical`, `stroke_count`, ...) and build the authoritative map of what *should* exist. Never trust the lookup tree's current content as ground truth — it's exactly what's being checked.
2. **Fix bottom-up.** Leaf files (the actual per-code lookup targets) before index/stem files (the pages that summarize and link leaves), before any top-level overview. Index previews are derived from leaf contents (character list, `size`), so fixing leaves first means the index rebuild has correct data to summarize instead of propagating stale numbers. This was confirmed necessary in practice: `SKIP-1-9-11`'s `size` had to be corrected before `SKIP-1-9.md`'s preview line could be trusted.
3. **Batch by folder, not by file.** At hundreds of files, work stroke-group by stroke-group (e.g. everything under `SKIP-1/` for left-half-count 9) rather than one file at a time — one ground-truth query serves an entire folder.
4. **Dispatch to forks for the mechanical sweep.** The per-file diff-and-fix work is high-volume, low-judgment, and its raw tool output isn't worth keeping in the main conversation. Fork per batch (e.g. one fork per `SKIP-N-M` folder-group), report back a short list of what was fixed/created/flagged, and keep the coordinating conversation to the summary level. Judgment calls (e.g. "is this character actually forbidden, or just miscategorized") get surfaced back, not resolved silently by the fork.
5. **Stamp `date-last-perfect` last**, only after a file's own checklist criteria are actually satisfied — not as a bulk find-replace independent of verification. A page whose gaps couldn't be resolved (e.g. a leaf file is missing and creating it requires data not on hand) keeps its old date or stays unstamped, and gets flagged in the summary instead.

## `lint SKIP`

Rubric: [[AIOS/checklists/checklist_skip.md]] — read it in full before running this; the summary below assumes it.

### 0. Scope

`lookup/SKIP/` is ~536 files: `SKIP.md` (one top-level overview), four first-number folders `SKIP-1/` (189 files) through `SKIP-4/` (62 files), each containing index files (`SKIP-#-#.md`) and leaf files (`SKIP-#-#-#.md`). SKIP-4 additionally has stroke-count indexes (`SKIP-4-#.md`) and four subtype-overview files (`SKIP-4-0-#.md`) — see the checklist for how its breadcrumbs and structure differ from SKIP-1/2/3.

### 1. Build ground truth

```bash
grep -h "^skip_number:" characters/*.md
```
normalized into a map of `skip_number → [character files]`. This tells you definitively which leaf codes should exist and which characters belong on each — independent of what the lookup tree currently says.

### 2. Leaf files first

For every `skip_number` that appears in the ground-truth map:
- **Missing leaf file** → create it: frontmatter (`stroke_count`, `size`, `skip_number`, `date-last-perfect`), breadcrumb, `## Characters` (numbered, ruby + gloss, per checklist format), `## Datacheck` block. SKIP-4 leaves need the double breadcrumb (stroke-count index + subtype overview).
- **Existing leaf file** → verify:
  - `size` equals the actual character-entry count (aliases/redirects don't count)
  - every character in the ground-truth map for this code appears in the `## Characters` list, and vice versa (catches both omissions and stale/wrong entries — a character listed here that no longer has this `skip_number` in its own file)
  - `### Aliases` / `### Forbidden` sections present where applicable, per the checklist's definitions of each
  - `Datacheck` query's `skip_number` string matches frontmatter exactly
  - Fix what's wrong, then stamp `date-last-perfect` to today.

### 3. Index (stem) files second

For every `SKIP-#-#.md` (and SKIP-4's `SKIP-4-#.md` / `SKIP-4-0-#.md`):
- List **every leaf file that exists** on disk under it, in numeric order — not just the ones an old preview happened to mention.
- Each preview line shows **every** character in that leaf, no truncation. (`SKIP-1-9-4` had 12 characters; the index preview showed 8 and an ellipsis — that's the exact bug class to hunt for. Cross-check preview character count against the leaf's own `size` field to catch this mechanically.)
- Positions with no leaf file get an explicit `none`/`no` line — don't just omit them silently, and don't extend the list past the highest position that actually has data or an intentional gap-marker.
- `## Base check` block present.
- Stamp `date-last-perfect` once the above hold.

### 4. Top-level `SKIP.md`

One file, checked last since it just links the 1/2/3/4 category pages and the four `SKIP-4-0-#` placeholders. Confirm every linked stroke-count page (`SKIP-1-1` through `SKIP-1-15`, etc.) actually exists and is a real link, not dead text — `SKIP.md` currently has exactly this bug at its "14." entry under First Number 1: literal text `14` instead of a link, because `SKIP-1-14.md` doesn't exist yet. Either create the missing index (if the ground-truth map has characters at that position) or confirm it's legitimately empty and represent that explicitly rather than leaving broken filler text.

### 5. Report

Per folder-group: counts of leaves created / leaves fixed / indexes fixed / dates stamped, plus a short list of anything that needed a judgment call rather than a mechanical fix (miscategorized character, ambiguous alias, etc.) for the user to weigh in on.
