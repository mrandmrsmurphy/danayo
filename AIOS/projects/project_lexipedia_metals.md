---
name: project-lexipedia-metals
description: "Closed 2026-09-17 - Metals lexipedia page audited, 2 stale readings fixed, 1 word perfected, 7 items added"
type: project
---

**Status: closed.** `lexipedia/Metals.md` (Rosenfelder-style topic list, 3 grouped clusters: precious/common metals, alloys/related metals, metalworking vocabulary) audited and completed. Given a `date-last-perfect` field, matching the treatment established on [[AIOS/projects/project_lexipedia_numbers.md|Numbers]] and [[AIOS/projects/project_periodic_table_perfection.md|Periodic Table]].

## Stale-reading fixes (2, same pattern as Periodic Table's duplicate-table drift)

Two entries had readings that no longer matched their underlying word file, because those word files had been corrected in earlier, unrelated sessions without this page being updated:
- **lead**: page showed ⼶ㄇ; `words/鉛.md`'s real, already-correct reading is ⼶ㄋ.
- **alloy**: page showed ㄎㄚㄆㄍㄧㄇ (the old, buggy "kab" reading); `words/合金.md` documents its own prior correction to ㄍㄛㄆㄍㄧㄇ ("gob," after a documented copy-forward bug affecting [[合金]]/[[混合]]/[[組合]] alike was fixed). The lexipedia page was never updated to reflect it.

**Lesson reinforced**: any lexipedia/topic-list page that caches a ruby reading inline is a second copy of that data, silently divergeable from the word file whenever the word gets fixed later. Worth spot-checking on any future lexipedia audit, not just assuming an existing link is current just because the target file exists.

## `## to smith` was an unlinked placeholder — investigated and perfected

`[[鍛冶]]` existed but was under-perfected (missing `korean`/`vietnamese`, one-line Notes). Perfecting it surfaced a genuine semantic question: this vault already had **[[鍛錬]]** linked for "to forge," and the two words share their leading character (鍛) and look near-synonymous. Verified via search this is **not** a redundancy:
- **[[鍛冶]]** (かじ) = the craft/trade of metalworking, and by extension the blacksmith who practices it — stays literal, no figurative drift.
- **[[鍛錬]]** (たんれん) = the specific act of forging by repeated striking, **but has drifted heavily in modern Japanese/Mandarin usage toward the figurative sense of rigorous training/self-discipline** ("tempering" body or character) — the literal metalworking sense is now the minority usage.

Both Notes sections were expanded to cross-reference and explain this distinction, so a future pass doesn't "simplify" one into the other. Korean 단야 confirmed as a real, attested (if secondary to native 대장장이) Sino-Korean term for 鍛冶; Vietnamese đoán dã is compositional only (no independent attestation found), noted honestly rather than presented as living usage.

## 7 items added, all pre-existing perfected words simply not yet linked here

No new word coinage was needed this pass — a `words/` sweep for the domain's obvious remaining gaps (platinum, aluminum, nickel, tungsten, rust, smelt) turned up real, already-complete matches every time:
- **platinum** → [[白金]], **nickel** → [[魔銅]], **tungsten** → [[狼金]] — all three are this vault's own coined periodic-table element names (same dual-duty pattern already established by the pre-existing gold/[[黄金]] and iron/[[鉄]] links — the periodic-table coinage *is* the everyday word here, not a separate colloquial term).
- **aluminum** → [[軽銀]] ("light silver"), deliberately **not** the periodic-table entry [[礬素]] — 軽銀 is documented on its own page as this vault's chosen colloquial/everyday term (the "tin foil" analogy: aluminum foil is called "tin foil" in English despite no tin), parallel to how "aluminum foil" itself isn't named after the periodic element suffix. This is the one case in this domain where the everyday word and the periodic-table word are genuinely two different, both-legitimate compounds — worth remembering if another metal element turns up the same split.
- **to smelt** → [[冶錬]], **rust** → [[銹]] — straightforward existing matches, no complications.

## Method note (same as Numbers)

Confirmed again: before assuming a Rosenfelder-style topic-list gap needs new coinage, a `words/` search by English gloss is cheap and frequently turns up an already-perfected match. New coinage should be the last resort, not the default, for lexipedia-page gap-filling.
