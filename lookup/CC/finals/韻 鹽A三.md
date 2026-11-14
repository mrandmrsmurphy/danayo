---
size: 24
middle_chinese_final: iᴇm
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 鹽A三** splits 13–8 between ㄝㄇ and ⼶ㄇ, with three singletons (see below)

## CJKV Evolution
鹽A三 [iᴇm] splits 13–8 between **ㄝㄇ** (plain, matching the Vowels table's documented value `em`, row 153 of 文法 - 99韻図) and **⼶ㄇ** (y-glide), the plurality group and the minority respectively, plus three singletons.

The split is not decided by the daughters: 掩 and 奄 are identical in Mandarin (*yǎn*), Cantonese (*jim2*) and Korean (엄) yet take ㄝㄇ and ⼶ㄇ, and 鎌 and 廉 share Mandarin *lián*, Cantonese *lim4* and Vietnamese *liêm* yet split the same way.

**冉**, **染** and **髯** share the same phonetic root (冉) and the same ȵ initial, and land on three different groups: 冉 on ⼶ㄇ, 染 on **⼄ㄇ**, and 髯 on **ㄛㄇ**. 冉 and 染 are identical in all four daughters (Mandarin *rǎn*, Cantonese *jim5*, Korean 염, Vietnamese *nhiễm*) and 髯 is a near-homophone (*rán*, *jim4*, 염).

**㑒** (t͡sʰ-initial) shares its initial letter with 鹸 on the main ㄝㄇ group, with which it shares Korean 첨, and lands alone on **ㄨㄇ**.

## Characters
### In Use
- ㄝㄇ: <ruby>[[占 (char)|占]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[鎌 (char)|鎌]]<rt>ㄌㄝㄇ</rt></ruby>, <ruby>[[鹸 (char)|鹸]]<rt>ㄑㄝㄇ</rt></ruby>, <ruby>[[尖]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[漸]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[潜]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[瞻]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[簾]]<rt>ㄌㄝㄇ</rt></ruby>, <ruby>[[繊]]<rt>ㄙㄝㄇ</rt></ruby>, <ruby>[[閃]]<rt>ㄙㄝㄇ</rt></ruby>, <ruby>[[陝]]<rt>ㄙㄝㄇ</rt></ruby>, <ruby>[[掩]]<rt>ㄝㄇ</rt></ruby>, <ruby>[[暹]]<rt>ㄙㄝㄇ</rt></ruby>
- ⼶ㄇ: <ruby>[[㪘 (char)|㪘]]<rt>ㄌ⼶ㄇ</rt></ruby>, <ruby>[[塩 (char)|塩]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[廉 (char)|廉]]<rt>ㄌ⼶ㄇ</rt></ruby>, <ruby>[[艶 (char)|艶]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[閻 (char)|閻]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[冉]]<rt>ㄋ⼶ㄇ</rt></ruby>, <ruby>[[奄]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[焰]]<rt>⼶ㄇ</rt></ruby>
- ㄨㄇ: <ruby>[[㑒]]<rt>ㄑㄨㄇ</rt></ruby>
- ⼄ㄇ: <ruby>[[染]]<rt>ㄋ⼄ㄇ</rt></ruby>
- ㄛㄇ: <ruby>[[髯]]<rt>ㄋㄛㄇ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iᴇm
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iᴇm"
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
