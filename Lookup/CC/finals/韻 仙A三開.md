---
size: 40
middle_chinese_final: iᴇn
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 仙A三開** splits into ⼶ㄋ vs ㄝㄋ, tracking no single initial class cleanly (see below)

## CJKV Evolution
仙A三開 [iᴇn] fractures 24-15 between **⼶ㄋ** and **ㄝㄋ**, matching the y-glide quality of the Vowels table's documented winner (`yen`).

The split is not clean by initial type — this final adds another confirmed instance of the recurring "same initial, arbitrary outcome" pattern seen throughout this sweep (之, 魚, etc). Sibilant/palatal initials (s/ʑ/ɕ/d͡ʑ) appear heavily on both sides: 仙, 線, 膳, 腺, 善, 繕, 扇 (7 members) land on ⼶ㄋ, while 禅, 蝉, 擅 (3 members) land on ㄝㄋ — the same general initial class, no findable distinguishing factor. The nasal ȵ (燃, 然 vs 肰) and null ŋ (這 vs 彦) show the identical scatter on a smaller scale.

**鮮**, sharing its initial (s) with the already-crowded 7-member sibilant cluster on ⼶ㄋ, dodges via a coda-shift and lands on **⼶ㄇ**.

## Characters
### In Use
- ⼶ㄋ: <ruby>[[面]]<rt>ㄇ⼶ㄋ</rt></ruby>, <ruby>[[甄]]<rt>ㄍ⼶ㄋ</rt></ruby>, <ruby>[[燃]]<rt>ㄋ⼶ㄋ</rt></ruby>, <ruby>[[綿]]<rt>ㄇ⼶ㄋ</rt></ruby>, <ruby>[[編]]<rt>ㄅ⼶ㄋ</rt></ruby>, <ruby>[[篇 (char)|篇]]<rt>ㄆ⼶ㄋ</rt></ruby>, <ruby>[[腺]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[膳]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[騙 (char)|騙]]<rt>ㄆ⼶ㄋ</rt></ruby>, <ruby>[[然 (char)|然]]<rt>ㄋ⼶ㄋ</rt></ruby>, <ruby>[[扁]]<rt>ㄆ⼶ㄋ</rt></ruby>, <ruby>[[蓮 (char)|蓮]]<rt>ㄌ⼶ㄋ</rt></ruby>, <ruby>[[線]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[兗]]<rt>⼶ㄋ</rt></ruby>, <ruby>[[繕]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[扇]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[便 (char)|便]]<rt>ㄅ⼶ㄋ</rt></ruby>, <ruby>[[善 (char)|善]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[延]]<rt>⼶ㄋ</rt></ruby>, <ruby>[[這]]<rt>⼶ㄋ</rt></ruby>, <ruby>[[連 (char)|連]]<rt>ㄌ⼶ㄋ</rt></ruby>, <ruby>[[仙]]<rt>ㄙ⼶ㄋ</rt></ruby>, <ruby>[[演]]<rt>⼶ㄋ</rt></ruby>, <ruby>[[偏 (char)|偏]]<rt>ㄆ⼶ㄋ</rt></ruby>
- ㄝㄋ: <ruby>[[遣 (char)|遣]]<rt>ㄎㄝㄋ</rt></ruby>, <ruby>[[賎]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[箭]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[煎]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[禅 (char)|禅]]<rt>ㄙㄝㄋ</rt></ruby>, <ruby>[[浅 (char)|浅]]<rt>ㄑㄝㄋ</rt></ruby>, <ruby>[[蝉 (char)|蝉]]<rt>ㄙㄝㄋ</rt></ruby>, <ruby>[[銭]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[剪 (char)|剪]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[遷]]<rt>ㄑㄝㄋ</rt></ruby>, <ruby>[[擅]]<rt>ㄙㄝㄋ</rt></ruby>, <ruby>[[彦]]<rt>ㄝㄋ</rt></ruby>, <ruby>[[践]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[肰]]<rt>ㄋㄝㄋ</rt></ruby>, <ruby>[[戦]]<rt>ㄐㄝㄋ</rt></ruby>
- ⼶ㄇ: <ruby>[[鮮]]<rt>ㄙ⼶ㄇ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iᴇn
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iᴇn"
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
