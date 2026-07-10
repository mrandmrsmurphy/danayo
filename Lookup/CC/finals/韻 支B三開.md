---
size: 27
middle_chinese_final: ɣiᴇ
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 支B三開** splits by initial type into ㄨㄧ vs ㄜㄧ, with several smaller exceptions (see below)

## CJKV Evolution
支B三開 [ɣiᴇ] shows the dual outcome the Vowels table already documents (`wi/i`): 10 real-initial characters land on **ㄨㄧ**, while all 7 null-initial characters (倚, 儀, 宜, 椅, 義, 議, 誼) land on **ㄜㄧ** instead — a clean initial-type split, not just a spelling artifact of glide fusion.

A further 6 characters (被, 妓, 疲, 皮, 碑, 魑) drop the w-glide entirely and land on plain **ㄧ**. Four of these — 被, 疲, 皮, 碑 — are the same labial (b/p) family already documented scattering away from a w-glide outcome on [[聲 並|聲並]] (the 皮/疲/被 finding); 妓 dodges an already-crowded ㄍㄨㄧ (shared by 寄, 奇, 技, 騎); and 魑 has no daughter-language support either way (Mandarin chī, Cantonese ci1, Korean 치 show no /u/ quality, but neither does 知's identical-looking daughter set, and 知 still gets the w-glide) — a genuine unconditioned per-character pick.

Two further labials — 彼 and 馳 — drop both the w-glide and the -i entirely, landing on bare **ㄜ**.

Two singleton oddities round out the page: **晒** (⼘ㄧ) has no comparable same-initial neighbor to check against. **靡** (ㄧㄆ) is suspicious — Mandarin mí, Cantonese mei5, and Korean 미 all point to a plain open -i syllable with no coda at all, so the trailing ㄆ looks like a likely stray-character typo in the corpus rather than a genuine outcome; flagging for a possible data fix rather than treating it as a real exception.

## Characters
### In Use
- ㄨㄧ: <ruby>[[寄 (char)|寄]]<rt>ㄍㄨㄧ</rt></ruby>, <ruby>[[披 (char)|披]]<rt>ㄆㄨㄧ</rt></ruby>, <ruby>[[池 (char)|池]]<rt>ㄐㄨㄧ</rt></ruby>, <ruby>[[知 (char)|知]]<rt>ㄐㄨㄧ</rt></ruby>, <ruby>[[奇]]<rt>ㄍㄨㄧ</rt></ruby>, <ruby>[[戯]]<rt>ㄏㄨㄧ</rt></ruby>, <ruby>[[技]]<rt>ㄍㄨㄧ</rt></ruby>, <ruby>[[智]]<rt>ㄐㄨㄧ</rt></ruby>, <ruby>[[犠]]<rt>ㄏㄨㄧ</rt></ruby>, <ruby>[[騎]]<rt>ㄍㄨㄧ</rt></ruby>
- ㄜㄧ: <ruby>[[倚 (char)|倚]]<rt>ㄜㄧ</rt></ruby>, <ruby>[[儀]]<rt>ㄜㄧ</rt></ruby>, <ruby>[[宜]]<rt>ㄜㄧ</rt></ruby>, <ruby>[[椅]]<rt>ㄜㄧ</rt></ruby>, <ruby>[[義]]<rt>ㄜㄧ</rt></ruby>, <ruby>[[議]]<rt>ㄜㄧ</rt></ruby>, <ruby>[[誼]]<rt>ㄜㄧ</rt></ruby>
- ㄧ: <ruby>[[被 (char)|被]]<rt>ㄆㄧ</rt></ruby>, <ruby>[[妓]]<rt>ㄍㄧ</rt></ruby>, <ruby>[[疲]]<rt>ㄆㄧ</rt></ruby>, <ruby>[[皮]]<rt>ㄅㄧ</rt></ruby>, <ruby>[[碑]]<rt>ㄅㄧ</rt></ruby>, <ruby>[[魑]]<rt>ㄑㄧ</rt></ruby>
- ㄜ: <ruby>[[彼 (char)|彼]]<rt>ㄅㄜ</rt></ruby>, <ruby>[[馳]]<rt>ㄑㄜ</rt></ruby>
- ⼘ㄧ: <ruby>[[晒 (char)|晒]]<rt>ㄙ⼘ㄧ</rt></ruby>
- ㄧㄆ: <ruby>[[靡]]<rt>ㄇㄧㄆ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇ
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇ"
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - middle_chinese_initial
      - middle_chinese_final
      - 注音
    sort:
      - property: 羅馬字
        direction: ASC
      - property: middle_chinese_initial
        direction: ASC
      - property: characters
        direction: DESC
      - property: grade_level
        direction: ASC
    columns:
      - file
      - file.path
      - file.links.length
    columnSize:
      note.mandarin: 59
      note.cantonese: 71
      note.korean: 43
      note.middle_chinese_initial: 97

```
