---
tags: [lookup]
---
Working notes from the first `lint SKIP` pass (2026-07-05). Not a permanent lookup page — a scratch tracking file for in-progress cleanup. Delete once everything below is resolved.





## Genuine content mismatches (declared `size` disagrees with ground truth)

Separate from formatting bugs below — these need someone to find the actual missing/extra character, not just reformat.


## Formatting bugs (existing leaf files not in checklist_skip.md format)

### No `## Characters` heading at all (~53 files, excludes the 4 legitimate SKIP-4-0-# subtype overviews which correctly have none)
SKIP-1: 1-1-4, 1-12-5, 1-12-4, 1-11-16, 1-6-1, 1-1-8, 1-4-1, 1-12-9, 1-1-11, 1-12-10, 1-12-7, 1-13-6, 1-2-15, 1-11-15, 1-13-2, 1-1-7, 1-12-2, 1-12-6, 1-1-3, 1-2-14
SKIP-2: 2-14-5, 2-12-14, 2-14-4, 2-12-5, 2-1-7, 2-13-4, 2-10-3, 2-1-2, 2-13-5, 2-11-4, 2-1-1, 2-3-2, 2-2-3, 2-14-3, 2-8-2, 2-15-2, 2-14-2, 2-12-13, 2-8-3, 2-13-9
SKIP-3: 3-1-4, 3-2-22, 3-2-12, 3-4-11, 3-1-7, 3-10-16
SKIP-4: 4-8-4, 4-9-2, 4-10-2, 4-1-1, 4-12-4, 4-11-3, 4-10-3

### Of those, uses a bulleted list instead of the numbered ruby+gloss format (17 files)
1-1-4, 1-2-3, 1-1-8, 1-4-1, 1-1-7, 1-1-3, 2-1-2, 2-11-4, 2-1-1, 2-3-2, 2-2-3, 2-8-2, 2-8-3, 2-12-8, 3-4-11, 4-1-1, 4-1-4


## Deferred: Aliases section research (separate pass, per 武明帥 2026-07-05)

~41 individual glyphs across ~17 leaf files have bare, unexplained entries under `### Aliases` (no `--> target` per checklist format). Needs real per-character research (is each glyph a graphic variant of an existing vault character, and of which one), not mechanical fixing. Files affected: SKIP-1-10-11, SKIP-1-11-11, SKIP-1-11-14, SKIP-1-6-16, SKIP-1-6-17, SKIP-2-2-15, SKIP-2-2-16, SKIP-2-3-18, SKIP-2-10-2, SKIP-2-10-8, SKIP-2-10-10, SKIP-2-6-17, SKIP-2-6-19, SKIP-2-8-10, SKIP-1-3-21 (the `[[衢]]` entry), SKIP-3-3-18 (`廱`, newly found), plus SKIP-4-2-1 and SKIP-4-2-4 which have an `### Aliases` heading with nothing under it at all. (Note: `SKIP-3-10-11`'s 魑 has been resolved — it was a real character miscategorized as an alias, not a genuine alias-research case — removed from this list.)

## Not yet swept

SKIP-1/2/3 index files (`SKIP-#-#.md`) haven't been checked yet beyond `SKIP-1-9.md` (fixed: truncated preview, size 2→correct). Same categories of bug (truncated previews, missing leaf links, un-marked gaps) likely recur across the other ~30 index files — this pass only reached leaf files.
