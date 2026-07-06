---
tags: [lookup]
---
Working notes from the first `lint SKIP` pass (2026-07-05). Not a permanent lookup page — a scratch tracking file for in-progress cleanup. Delete once everything below is resolved.

## Second pass (2026-07-05) — after 武明帥's manual cleanup

Re-ran ground truth (428 codes now, +2 from 衢/甕) and a full leaf-file re-scan: zero remaining issues in any previously-tracked category (missing leaves, size mismatches, `## Characters` heading, Datacheck heading level, bulleted-vs-numbered, broken links). Found and fixed 3 stragglers the manual pass missed: `SKIP-4-4-1.md` (still no `## Characters` heading), `SKIP-1-4-1.md` (two links missing `.md` extension), `SKIP-1-1-4.md` (old absolute-path breadcrumb).

Broadened the Datacheck-heading check (it was matching by literal text "Datacheck", missing text variants) and found 20 more files using "Data double check" / "Data doublecheck" / "Data check" / "Data Search" at various levels — normalized all to `## Datacheck`.

### Index (stem) files — swept for the first time

Built a validated glyph-extractor (handles `### Used`/`In Use`/`Use` and excludes `### Aliases`/`Redirects`/`Forbidden`/`Banned` sections and `-->` redirect bullets) and confirmed it matches every leaf's declared `size` before trusting it. Two genuine new leaf-level bugs surfaced during validation:
- `SKIP-1-3-16.md`: size said 3, actually has 4 real entries (懶/瀧/瀬/獺) — fixed to 4.
- `SKIP-2-10-3.md`: had 2 unlabeled bonus bullets (塰/髢) beyond its declared 3 — per 武明帥, these are candidates not yet in the database, size stays 3 (武明帥 also reformatted this file directly, moving them under `### Aliases` and renaming `### Used`→`### Use`, another heading variant now handled).

Then used the extractor to rewrite **145 stale/truncated preview lines** across all SKIP-1/2/3 index files — the `SKIP-1-9-4` truncation found earlier this session was not an isolated bug, it was systemic (dozens of index pages had "…"-truncated previews, some leaf lists running 30-90 characters). Also re-verified `SKIP-2-11.md`'s `ø`-marked positions (8/10/11/13) — confirmed these are the same legitimate size:0 convention used vault-wide, not a real gap.

### SKIP-4's distinct index structure — swept

Checked all 15 stroke-count indexes (`SKIP-4-#.md`) and all 4 subtype overviews (`SKIP-4-0-#.md`). Found and fixed:
- 3 truncated stroke-count indexes (`SKIP-4-4.md`, `SKIP-4-5.md` [two truncated entries], `SKIP-4-7.md`).
- `SKIP-4-0-1.md` (the table-layout overview): missing 𡈼 from the `SKIP-4-4-1` cell (added after 丑 was added to that leaf earlier this session).
- `SKIP-4-0-3.md`: stale/truncated entry for `SKIP-4-5-3` (was missing 未/冉, had a stray comma typo) — rewrote in full.

No structural gaps (every stroke-count index links every leaf that exists; every subtype overview covers every stroke-count that has a leaf of that subtype).

**Checklist correction**: `checklist_skip.md` claimed SKIP-4-0-2/3/4 "contain no character links of their own" — that was simply wrong; all three show per-leaf character previews in real practice, same as the stroke-count indexes. Fixed the checklist text and also fixed its own worked example, which had been modeling the truncation pattern with "...".

## SKIP-4 leaf files: also spot-checked

All 43 leaf files were already covered by the general leaf sweep (ground truth, size, `## Characters` heading, Datacheck heading, redirect formatting) earlier in this pass — nothing SKIP-4-specific remained outside the index layer covered above.

## Deferred: Aliases section research — almost entirely resolved

武明帥 independently resolved nearly the entire original ~35-glyph list while working in parallel with this pass — every file re-checked now has proper `X --> Y` (or `a.k.a.`) explanations: SKIP-1-11-11, SKIP-1-11-14, SKIP-1-6-16, SKIP-1-6-17, SKIP-2-2-15, SKIP-2-3-18, SKIP-2-10-2, SKIP-2-10-8, SKIP-2-10-10, SKIP-2-6-17, SKIP-2-6-19, SKIP-2-8-10, SKIP-3-3-18, SKIP-4-2-1, SKIP-4-2-4 are all done.

**One file still open**: `SKIP-1-10-11.md` — 9 bare, unexplained entries remain (驂, 驃, 騾, 髏, 鷁, 鶸, 鶺, 鷆, 鷏), each needing real research into what (if anything) they're a graphic variant of.

Two of the resolved files used an unusual redirect target worth flagging, not fixing: `SKIP-2-10-8.md` has "瞿 --> 衢" and `SKIP-2-10-10.md` has "矍 --> 衢" — i.e., pointing the whole 瞿/矍 phonetic family at 衢 rather than a true graphic variant, presumably since neither will ever get its own page (confirmed earlier: the entire 37-character 瞿/矍 family has zero vault representation). Not the usual sense of "alias," but a deliberate choice given the constraint.

## Status: lint SKIP is essentially clean end-to-end

Every mechanical category tracked across both passes — missing leaves, size mismatches, heading structure/level/text variants, bulleted-vs-numbered lists, broken links, truncated previews (leaf-level and both index-file structures) — is resolved for all four SKIP folders, and `date-last-perfect` has been stamped 2026-07-05 on every file that meets its criteria (523 files stamped this pass). The only file excluded from stamping, and the only thing left open in the whole `lint SKIP` effort, is `SKIP-1-10-11.md`'s 9 unresolved bare aliases above.
