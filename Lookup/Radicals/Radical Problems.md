---
tags: [todo]
---

# Radical Problems

To-do list from the first `lint Radicals` test run (see [[AIOS/skills/skill_lint.md]], `lint Radicals` section; rubric at [[AIOS/checklists/checklist_radicals.md]]). Ground truth built from `characters/*.md` frontmatter, cross-referenced against all 215 files in `lookup/Radicals/`.

Work bottom-up per the skill: fix leaf pages first, stamp `date-last-perfect` only once a page's own checklist criteria are satisfied, then re-check `Radicals.md` last.

## Clean (no action needed)

- [x] 0 character pages missing the `radical:` property.
- [x] `Radicals.md` itself: all 214 radicals present, every shown count matches its leaf's `size` field. No action needed here — it just mirrors whatever the leaf currently says (garbage in, garbage out), so leaf fixes below will auto-correct it once re-verified at the end.

---

## 1. Broken Data-check queries (frontmatter `radical:` doesn't match canonical form) — fix first, highest severity

These two pages' `## Data`/`## Dataview` query returns **zero rows** right now because the frontmatter `radical:` value isn't the string actually used in character frontmatter.

- [x] **Radical 179.md** — frontmatter says `radical: 韮`, should be `radical: 韭` (韮 "leek" is a *character* classified under this radical, not the radical symbol itself; canonical form per `characters/*.md` and `Radicals.md` is 韭).
- [x] **Radical 211.md** — frontmatter says `radical: 歯`, should be `radical: 齒` (歯 is the simplified/Japanese form; canonical form per character frontmatter and `Radicals.md` is 齒). Page note already admits "The (simplified) radical itself is ironically not found here" — just needs the frontmatter corrected to match.

## 2. Malformed/unlinked entries

- [x] **Radical 183.md**, entry 1 — broken wikilink syntax: `[[../../characters/飛 (char)]]` (a raw relative path stuffed inside `[[ ]]`). Fix to a proper link, e.g. `[[飛 (char)|飛]]`.
- [x] **Radical 208.md**, entry 1 — 鼠 has no link at all, just plain text (`<ruby>鼠<rt>...`). Needs a proper character link.

## 3. Missing `+0 Stroke` group (115 of 214 pages)

Checklist requires every leaf page to open its `## Strokes` section with a `+0 Stroke(s)` group containing exactly the radical itself as entry 1. These pages skip straight to `+1` or later:

- [ ] Radical 002, 003, 004, 005, 006, 008, 010, 011, 013, 014, 015, 016, 017, 020, 021, 022, 023, 025, 026, 027, 028, 031, 034, 035, 043, 044, 045, 049, 052, 053, 054, 055, 056, 058, 059, 060, 065, 066, 071, 076, 079, 080, 081, 082, 083, 084, 087, 088, 089, 090, 092, 097, 101, 104, 105, 107, 110, 114, 116, 122, 126, 127, 129, 131, 132, 133, 134, 137, 138, 139, 140, 141, 146, 150, 153, 158, 162, 165, 168, 171, 173, 175, 176, 177, 178, 179, 180, 182, 183, 185, 186, 189, 190, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214

## 4. Missing character links (66 characters across 38 pages) — DONE

A character's own frontmatter says it belongs to this radical, but it isn't linked anywhere on the page yet. All 66 added with ruby (native 注音) + short English gloss, inserted into the correct `+N Strokes` group (creating new stroke-count headers where none existed), with all subsequent entries renumbered continuously and `size` updated to match. Re-ran the ground-truth cross-check afterward: 0 missing links remain.

- [x] Radical 010: 兗
- [x] Radical 012: 典, 兮, 具, 兵, 六
- [x] Radical 015: 凝, 凜, 冶
- [x] Radical 029: 反, 叔, 取, 叢, 受
- [x] Radical 030: 嗇, 吠
- [x] Radical 032: 址
- [x] Radical 038: 嬴, 嫂
- [x] Radical 040: 宏
- [x] Radical 060: 徊, 徘
- [x] Radical 061: 憑, 怯, 恍
- [x] Radical 064: 攘
- [x] Radical 073: 最, 曳, 曼, 曹, 替
- [x] Radical 075: 榜
- [x] Radical 085: 澈, 汐
- [x] Radical 094: 狡
- [x] Radical 098: 甕
- [x] Radical 106: 的, 皓, 皐
- [x] Radical 109: 瞰
- [x] Radical 115: 穢
- [x] Radical 117: 竦, 章
- [x] Radical 120: 紐, 紇
- [x] Radical 134: 舅 *(page uses a flat, header-less `## Characters` list — added as entry 3 without imposing `+N Strokes` structure; that's section 3's job)*
- [x] Radical 140: 菲
- [x] Radical 144: 衢
- [x] Radical 145: 裔
- [x] Radical 148: 解
- [x] Radical 157: 跋
- [x] Radical 166: 量
- [x] Radical 167: 鑫
- [x] Radical 173: 霅 *(also normalized this page's `### +N` headers to the standard `+N Strokes` form as a byproduct of renumbering)*
- [x] Radical 180: 韻, 響 *(page has no stroke-group structure at all; 音 itself was already entry 1 — appended as 2, 3)*
- [x] Radical 183: 飛 *(same entry as the malformed-link fix in section 2 — one fix resolved both)*
- [x] Radical 186: 馨, 香 — **correction**: both were already present as un-numbered bullets (`- <ruby>...`), which is why the lint's numbered-entry parser couldn't see them. Converted to numbered `1.`/`2.` entries; also fixed a typo ("fragrent" → "fragrant"). No characters were actually missing here.
- [x] Radical 187: 驟
- [x] Radical 194: 魄, 魑
- [x] Radical 201: 黄 — **correction**: same as 186, already present as an un-numbered bullet with a stray "That's it!" line. Converted to a numbered entry, removed the stray line.
- [x] Radical 207: 鼓 — **correction**: same pattern, un-numbered bullet converted to numbered entry.
- [x] Radical 208: 鼠 *(same entry as the malformed-link fix in section 2 — one fix resolved both)*
- [x] Radical 210: 斉 — **correction**: same pattern, un-numbered bullet under `### Used` converted to numbered entry.

## 5. `size` mismatches (frontmatter vs actual numbered-entry count)

- [x] Radical 181: declared 30, actual 29 — **still open**, unrelated to section 4 (no character was missing here; some other discrepancy in this page's own count needs investigating separately)
- [x] Radical 186: resolved by the section-4 fix above (declared 2, now 2 actual)
- [x] Radical 201: resolved by the section-4 fix above (declared 1, now 1 actual)
- [x] Radical 207: resolved by the section-4 fix above (declared 1, now 1 actual)
- [x] Radical 210: resolved by the section-4 fix above (declared 1, now 1 actual)

## 6. Breadcrumb style (should be `[[Radicals]]` wikilink) — DONE

- [x] **Radical 175.md** — **correction**: it did have a breadcrumb, just typo'd as `< [[Radicals]]` (wrong angle bracket). Fixed to `>` and added the missing one-line description (its two other checklist gaps — no `+N Strokes` structure, no character-count description — are section 3's problem, not touched here).
- [x] Markdown-link breadcrumb (`[Radicals](Radicals.md)` and, on Radical 021/203, `[Radicals](lookup/Radicals/Radicals.md)`) converted to `[[Radicals]]` on all 25 pages originally listed, plus 021 and 203 which used a third link-path variant not caught by the first pass.
- Verified: all 214 leaf pages now open with `> [[Radicals]]`.

## 7. `## Data check` heading inconsistency — DONE, with one open question

Checklist requires the heading `## Data check` consistently.

- [x] **`## Data search`** and **`## Dataview`** headings renamed to `## Data check` across all affected pages (bulk sed, verified no stragglers remain).
- [x] **Radical 011.md** — was a special case: `# Data search` (wrong heading *level*, single `#`, as well as wrong label). Fixed to `## Data check`.
- [ ] **Open question — 9 pages use `## Base check` instead, with an Obsidian Base `base` query block rather than a `dataview` block**: Radical 028, 034, 035, 043, 045, 049, 134, 168, 171. This isn't a mislabeled Data-check section — it's a different, complete, and consistently-used query mechanism (Obsidian's native Base feature vs. the Dataview plugin). The checklist ([[AIOS/checklists/checklist_radicals.md]]) only documents the `## Data check` + dataview form. Didn't force these into dataview format since that's a bigger content change than "relabel," not a mechanical rename — left as-is pending a decision on whether `## Base check` should be recognized as an equally valid alternative in the checklist, or converted.
- Verified: all 214 pages now have either `## Data check` or `## Base check` — none are missing a query section entirely.

---

## Suggested order

1. Section 1 (broken queries) — 2 files, highest impact per fix.
2. Section 2 (malformed/unlinked entries) — 2 files, overlaps with section 4.
3. Section 4 (missing links) — 38 files, then section 5 (`size`) mostly falls out of this.
4. Section 3 (`+0 Stroke`) — 115 files, mechanical, batch by folder/fork per the skill's general procedure.
5. Sections 6–7 (breadcrumb / heading style) — pure mechanical find-replace, safe to batch last across all 214.
6. Re-run the `Radicals.md` cross-check once leaves are fixed, then stamp `date-last-perfect` per page as each is verified.
