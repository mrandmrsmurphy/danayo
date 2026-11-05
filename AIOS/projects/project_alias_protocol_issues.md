---
name: project-alias-protocol-issues
description: Trouble hit while rolling out the ## Aliases section on character pages; for the user's morning review
metadata:
  type: project
---

# Alias protocol issues (for morning review)

## 2026-11-05 — 零 (char): alias 〇 has no SKIP, radical or stroke home — RESOLVED 2026-11-05

Resolution (user): treat 〇 as 1 stroke, SKIP 4-1-4 (guessed), "has no radical"; redirects on Stroke 01 and SKIP-4-1-4 only. The linter skips the radical redirect when the subsection says "has no radical"; the checklist says so. 零 is stamped.

零 lists the alias 〇 (U+3007, the ideographic zero). 〇 is a CJK symbol, not a Han character: Wiktionary has no Han-character entry for it (no radical, no stroke count), EDRDG has no SKIP code, and it has no rank in the Classical Chinese lists. So the three required redirects (Stroke page, SKIP leaf, Radical page) and the SKIP/stroke figures have nowhere to go. 零 was **not stamped**; its Notes, Words and Derived Characters are otherwise checked and unchanged.

Options: (a) treat 〇 as 1 stroke with SKIP 4-1-4 and a "no radical" note, and put the redirect on Stroke 01 and SKIP-4-1-4 only; (b) allow a non-Han alias to skip the three redirects and say so in its subsection; (c) drop 〇 from `aliases:` and mention it only in Notes. The linter's C4 check would need to match whichever you choose.

## 2026-11-05 — 冪: vault stroke count and SKIP disagree with EDRDG (and with its own phonetic 幕) — RESOLVED 2026-11-05

Resolution (user): follow EDRDG. 冪 is now 15 strokes, SKIP 2-2-13; moved off Stroke 16 and SKIP-2-2-14 onto Stroke 15 and SKIP-2-2-13, Radical 014 group renamed +13. Alias 幂 added (Radical 050, SKIP 2-9-3 guessed, 12 strokes). 冪 is stamped.

冪 (character page) has `stroke_count: 16` and `skip_number: 2-2-14`. EDRDG gives **15 strokes and SKIP 2-2-13**; Wiktionary gives 16 (it counts the traditional 14-stroke 幕). The vault's own 幕 (char) has `stroke_count: 13`, so 冖 (2) + 幕 (13) = 15 is the vault-consistent figure. The Character Creation skill says SKIP comes from EDRDG. Fixing it would move 冪 from Stroke 16 to Stroke 15 and from SKIP-2-2-14 to SKIP-2-2-13 (leaf sizes, SKIP-2-2 index, lint counts), so I did not change it. 冪 was **not stamped**.

The alias 幂 (simplified; Wiktionary: 12 strokes, radical 巾, ⿱冖旲巾 / ⿱𠖇巾; EDRDG has no entry) could not have its `## Aliases` subsection finished until this is decided: its SKIP would be 2-2-… depending on the reading of its parts, and its strokes/radical differ from 冪's (Radical 050 巾, not 014 冖).

Question for the morning: follow EDRDG (15 strokes, 2-2-13) for 冪, or keep Wiktionary's 16? The same split may recur for other characters whose phonetic has a Japanese-form stroke count lower than the traditional one.

## OPEN 2026-11-05 — 惹: vault stroke count and SKIP disagree with EDRDG (same pattern as 冪)

惹 has `stroke_count: 13` and `skip_number: 2-9-4`. EDRDG gives **SKIP 2-3-9** and two stroke counts, **12 and 13** (12 first). The vault counts 艹 as 3 strokes elsewhere (蕾 is 16 = 艹 3 + 雷 13), and 若 (char) is the phonetic. If 艹 is 3, 惹 is 12 strokes with 艹 over 右心 = 2-3-9, which is EDRDG's primary reading; the vault's 13 / 2-9-4 counts 艹 as 4. Following your 冪 ruling (EDRDG wins) the fix would be: stroke 12, SKIP 2-3-9, moving 惹 off Stroke 13 and SKIP-2-9-4 onto Stroke 12 and SKIP-2-3-9. I did **not** change it or stamp 惹.

Worth deciding once: do other 艹-over-X characters carry the same 艹 = 4 count (so a sweep for "SKIP differs from EDRDG" would find more)? The characters lint does not compare SKIP to EDRDG, so these only surface by hand.

Extra evidence for 惹: the vault's own 若 (char) is 8 strokes, SKIP 2-3-5 (艹 counted as 3), so 若 (8) + 心 (4) = 12, which matches EDRDG's 12 / 2-3-9 and contradicts the vault's 13 / 2-9-4 for 惹.

## OPEN 2026-11-05 — 抛: stroke count 7 vs 8, and the alias 拋 depends on it

抛 has `stroke_count: 8` and `skip_number: 1-3-5`. EDRDG lists **two stroke counts, 7 and 8**, with SKIP 1-3-5 (which implies 8: 扌 3 + 5). Wiktionary gives 抛 **7 strokes** (扌 + 𠠵, where 𠠵 is 九 + 力 at 2 + 2 = 4, so 3 + 4 = 7) and its traditional form 拋 **8 strokes** (扌 + 尢 over 力, ⿰扌⿺尢力). The vault's Notes describe 抛 as 九 + 力, which is 7. So the vault's 8 / 1-3-5 may be the count for 拋's shape rather than 抛's.

The alias 拋 (traditional; EDRDG has no entry for it) cannot be written up until this is decided: if 抛 is 7 strokes, SKIP would be 1-3-4 and 拋 takes the 8-stroke / 1-3-5 slot; if 抛 stays 8, both would share Stroke 08 / SKIP-1-3-5. 抛 was **not stamped** and nothing was changed.

Question: is 抛 7 strokes (Wiktionary, EDRDG's first count, and what 九 + 力 adds up to) with SKIP 1-3-4, or does the vault keep 8 / 1-3-5? I'd lean 7 / 1-3-4 if you want it to match the glyph, but EDRDG's own SKIP says 1-3-5.

## OPEN 2026-11-05 — 拿: vault SKIP disagrees with EDRDG, and `mc_id` is above an alias's rank

拿 has `skip_number: 2-6-4` (合 6 over 手 4). EDRDG gives **2-2-8** for 拿 (stroke count 10 agrees): it splits the top as 𠆢 (2) over 一口手 (8). Note that 2-6-4 is EDRDG's code for the alias **挐**, not for 拿, so the page may have taken its SKIP from the wrong glyph. Following your EDRDG-wins ruling the fix would move 拿 from SKIP-2-6-4 to SKIP-2-2-8 (leaf exists? not checked) and update the Notes link.

Also, 拿 has three aliases and their data differ: 拏 (EDRDG: Radical 064, 9 strokes, SKIP 2-5-4; "to connect"), 挐 (EDRDG: 10 strokes, SKIP 2-6-4; CC rank **3988**), 㧱 (no EDRDG entry; Wiktionary: Radical 064, 10 strokes, ⿰合手, so a computed SKIP 1-6-4). Under the new rule `mc_id` must be the lowest rank among the character and its aliases: 挐 is 3988 and 拿 itself is not on the CC lists, so `mc_id` 5165 should probably become 3988. 拏 and 挐 are real variants people type; 㧱 is the rare kind you said you don't need.

拿 was **not stamped** and nothing was changed. Questions: (1) move 拿 to SKIP-2-2-8? (2) change `mc_id` to 3988? (3) drop 㧱 from the aliases?

## OPEN 2026-11-05 — 欝: the aliases need SKIP leaves and index slots that do not exist

欝 (character) checks out (EDRDG: SKIP 2-12-14, strokes 26/25, radical 木). Its aliases are 鬱 (EDRDG: Radical 192 鬯, SKIP **2-14-15**, 29 strokes, CC rank 1620 = the page's `mc_id`) and 鬰 (no EDRDG entry; Radical 192, 27 strokes; SKIP by analogy to 鬱 would be **2-12-15**). Neither leaf `SKIP-2-14-15` nor `SKIP-2-12-15` exists, and the parent indexes `SKIP-2-14.md` (slots 1-5) and `SKIP-2-12.md` (slots up to 14) have no slot 15. The earlier fix for a missing leaf (a size-0 redirect-only leaf plus an `ø` index entry, as done for 亂 at 1-12-1) assumed the slot already existed as "no"; here the index itself would have to grow to 15 slots.

欝 was **not stamped**. Decide: (a) extend the two indexes to slot 15 and create the two redirect-only leaves, or (b) put alias redirects for these tall SKIP codes somewhere else. Also a judgment call: 鬰 is the rare kind of alias you said you don't need; dropping it would leave only 鬱, which people do type.

## JUDGMENT CALL 2026-11-05 — 誕 / 诞: Chinese vs Japanese stroke counting

誕's page uses the Japanese count (15 strokes, SKIP 1-7-8, 延 = 8). The simplified alias 诞 was written up with the **Chinese** count (8 strokes, SKIP 1-2-6, 延 = 6) because Wiktionary gives that for 诞. Using the Japanese count instead would make 诞 10 strokes, SKIP 1-2-8. This can recur for any simplified form containing 延 or other characters whose stroke count differs between the two systems. Decide whether alias stroke counts follow the alias's own (Chinese) count or the vault's Japanese counting; the row is on `project_alias_skip_guesses.md`.

## OPEN 2026-11-05 — 逗 (and a wider 辶 pattern): vault counts 辶 as 4 strokes on some pages, 3 on others

逗 has `stroke_count: 11` and `skip_number: 3-4-7`. EDRDG gives **10 strokes (alternates 9 and 11) and SKIP 3-3-7**. The vault is inconsistent about 辶 / 辵: 連 is 10 / 3-3-7 and 追 is 9 / 3-3-6 (辶 = 3, matching EDRDG), while 速 (char) is 11 / 3-4-7 and 逗 is 11 / 3-4-7 (辶 = 4). A rough count shows 44 pages with `skip_number: 3-4-…` against 146 with `3-3-…`, so a good share of the 3-4 pages may be this same slip, though not all (some 3-4 codes are genuine). Following your EDRDG-wins ruling, 逗 would move to 10 strokes and SKIP 3-3-7 (Stroke 11 → Stroke 10, SKIP-3-4-7 → SKIP-3-3-7). I did **not** change it or stamp it.

Suggest: a one-time check of all `3-4-N` pages against EDRDG before the loop reaches them, since each will trip the same question.

## OPEN 2026-11-05 — 雴: SKIP type looks wrong (left-right 1-8-5 vs top-bottom glyph)

雴 has `skip_number: 1-8-5`, which is a left-right split. Wiktionary's decomposition is **⿱雨立** (雨 on top of 立, a top-bottom glyph), which would be **SKIP 2-8-5** (top 雨 = 8, bottom 立 = 5). EDRDG has no entry for 雴, so there is no authority to check against; 13 strokes is right either way. If the glyph is top-bottom, 雴 should move from SKIP-1-8-5 to SKIP-2-8-5. Everything else on the page checked out (Wiktionary: chì/lì, cap1, Radical 173; not ranked in the CC corpus).

雴 was **not stamped** (the stamp and a blank-line fix were reverted) and nothing was changed. Question: is 雴 left-right or top-bottom? I'd lean top-bottom, 2-8-5.

## OPEN 2026-11-05 — 馨: alias 馫 needs SKIP 2-9-18, the same missing-slot problem as 欝

馨 itself checks out against EDRDG (Radical 186 香, SKIP 2-11-9, 20 strokes; CC rank 3974 = `mc_id`). Its alias 馫 (Wiktionary: Radical 186 香, 27 strokes, 香 over 𩡐, so SKIP **2-9-18**; EDRDG has no entry) has no leaf `SKIP-2-9-18`, and the index `SKIP-2-9.md` stops at slot 12. Same decision as 欝: extend the SKIP index to the needed slot and create a redirect-only leaf, or handle very tall SKIP codes another way. 馫 is also a very rare character (three 香), the kind you said you don't need as an alias, so dropping it from `aliases:` would remove the problem. 馨 was **not stamped**; nothing changed.

## OPEN 2026-11-05 — 齢: the page carries the traditional 齡's stroke count and SKIP

齢 has `stroke_count: 20` and `skip_number: 1-15-5`. EDRDG gives the shinjitai 齢 (the page's own headword, U+9F62) **17 strokes and SKIP 1-12-5** (歯 12 + 令 5), and gives the alias 齡 (U+9F61) 20 strokes and SKIP 1-15-5 (齒 15 + 令 5). So the page's numbers belong to 齡, not 齢. The radical is also 齒 on the page (Radical 211, which is the same radical page for 歯/齒). Following your EDRDG-wins ruling, 齢 would move to 17 strokes and SKIP 1-12-5 (Stroke 20 → Stroke 17, SKIP-1-15-5 → SKIP-1-12-5), and 齡 would keep 20 / 1-15-5 as the alias's numbers. Neither 齢 nor 齡 is on the CC lists, so `mc_id` 4728 is a long-tail rank and is not affected.

齢 was **not stamped**; nothing was changed. This is probably a pattern for any shinjitai page whose numbers were taken from the traditional form (we saw it with 冪, 惹 and 逗 in a different guise).
