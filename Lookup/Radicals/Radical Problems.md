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

## 4. Missing character links (66 characters across 38 pages)

A character's own frontmatter says it belongs to this radical, but it isn't linked anywhere on the page yet:

- [ ] Radical 010: 兗
- [ ] Radical 012: 典, 兮, 具, 兵, 六
- [ ] Radical 015: 凝, 凜, 冶
- [ ] Radical 029: 反, 叔, 取, 叢, 受
- [ ] Radical 030: 嗇, 吠
- [ ] Radical 032: 址
- [ ] Radical 038: 嬴, 嫂
- [ ] Radical 040: 宏
- [ ] Radical 060: 徊, 徘
- [ ] Radical 061: 憑, 怯, 恍
- [ ] Radical 064: 攘
- [ ] Radical 073: 最, 曳, 曼, 曹, 替
- [ ] Radical 075: 榜
- [ ] Radical 085: 澈, 汐
- [ ] Radical 094: 狡
- [ ] Radical 098: 甕
- [ ] Radical 106: 的, 皓, 皐
- [ ] Radical 109: 瞰
- [ ] Radical 115: 穢
- [ ] Radical 117: 竦, 章
- [ ] Radical 120: 紐, 紇
- [ ] Radical 134: 舅
- [ ] Radical 140: 菲
- [ ] Radical 144: 衢
- [ ] Radical 145: 裔
- [ ] Radical 148: 解
- [ ] Radical 157: 跋
- [ ] Radical 166: 量
- [ ] Radical 167: 鑫
- [ ] Radical 173: 霅
- [ ] Radical 180: 韻, 響
- [ ] Radical 183: 飛 *(same entry as the malformed-link fix in section 2 — one fix resolves both)*
- [ ] Radical 186: 馨, 香
- [ ] Radical 187: 驟
- [ ] Radical 194: 魄, 魑
- [ ] Radical 201: 黄
- [ ] Radical 207: 鼓
- [ ] Radical 208: 鼠 *(same entry as the malformed-link fix in section 2 — one fix resolves both)*
- [ ] Radical 210: 斉

## 5. `size` mismatches (frontmatter vs actual numbered-entry count)

- [ ] Radical 181: declared 30, actual 29 (likely resolves itself once section 4 items are settled — recount after fixing)
- [ ] Radical 186: declared 2, actual 0 (matches section 4: 馨, 香 both missing)
- [ ] Radical 201: declared 1, actual 0 (matches section 4: 黄 missing)
- [ ] Radical 207: declared 1, actual 0 (matches section 4: 鼓 missing)
- [ ] Radical 210: declared 1, actual 0 (matches section 4: 斉 missing)

## 6. Breadcrumb style (should be `[[Radicals]]` wikilink)

- [x] **Radical 175.md** has no breadcrumb line at all — frontmatter goes straight to `## Characters`. Needs both the breadcrumb and a one-line description added.
- [ ] Markdown-link breadcrumb (`[Radicals](Radicals.md)`) instead of `[[Radicals]]` on: Radical 002, 003, 005, 016, 017, 021, 025, 028, 064, 101, 122, 126, 131, 137, 138, 139, 146, 158, 183, 190, 194, 196, 198, 201, 203

## 7. `## Data check` heading inconsistency

Checklist requires the heading `## Data check` consistently. 147 pages already use it correctly.

**`## Data search`** (46 pages) →
- [ ] Radical 001, 013, 054, 056, 058, 065, 071, 080, 081, 082, 083, 084, 087, 088, 089, 090, 092, 095, 097, 101, 107, 110, 116, 122, 126, 127, 129, 131, 132, 133, 137, 138, 139, 146, 150, 158, 192, 194, 197, 198, 199, 200, 201, 202, 203, 204

**`## Dataview`** (11 pages) →
- [ ] Radical 016, 017, 021, 022, 025, 175, 176, 177, 178, 179, 180

**No Data section heading at all** (10 pages) →
- [ ] Radical 011, 028, 034, 035, 043, 045, 049, 134, 168, 171

---

## Suggested order

1. Section 1 (broken queries) — 2 files, highest impact per fix.
2. Section 2 (malformed/unlinked entries) — 2 files, overlaps with section 4.
3. Section 4 (missing links) — 38 files, then section 5 (`size`) mostly falls out of this.
4. Section 3 (`+0 Stroke`) — 115 files, mechanical, batch by folder/fork per the skill's general procedure.
5. Sections 6–7 (breadcrumb / heading style) — pure mechanical find-replace, safe to batch last across all 214.
6. Re-run the `Radicals.md` cross-check once leaves are fixed, then stamp `date-last-perfect` per page as each is verified.
