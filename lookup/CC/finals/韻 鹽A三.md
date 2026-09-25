---
size: 22
middle_chinese_final: iᴇm
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 鹽A三** actually converges more on a plain group than its own documented y-glide winner (see below)

## CJKV Evolution
鹽A三 [iᴇm] splits 11–8 between **ㄝㄇ** (plain, the plurality in this corpus) and **⼶ㄇ** (y-glide, matching the Vowels table's documented winner `yem`) — the documented winner is actually the minority outcome here.

**冉**, **染**, and **髯** all share the same phonetic root (冉) and the same ȵ initial — 冉 and 染 are even true homophones (both Mandarin *rǎn*, Cantonese *jim5*, Korean 염) — yet all three land on three different groups: 冉 on ⼶ㄇ, 染 on **⼄ㄇ**, and 髯 on **ㄛㄇ**. A three-way phonetic-family scatter, deliberately avoiding convergence, matching the pattern documented on [[韻 豪|豪]]'s 喿/竃/藻.

**㑒** shares its initial (t͡sʰ) with 鹸 on the main ㄝㄇ group and dodges via vowel-shift, landing alone on **ㄨㄇ**.

## Characters
### In Use
- ㄝㄇ: <ruby>[[占 (char)|占]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[鎌 (char)|鎌]]<rt>ㄌㄝㄇ</rt></ruby>, <ruby>[[鹸 (char)|鹸]]<rt>ㄑㄝㄇ</rt></ruby>, <ruby>[[尖]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[漸]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[潜]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[瞻]]<rt>ㄐㄝㄇ</rt></ruby>, <ruby>[[簾]]<rt>ㄌㄝㄇ</rt></ruby>, <ruby>[[繊]]<rt>ㄙㄝㄇ</rt></ruby>, <ruby>[[閃]]<rt>ㄙㄝㄇ</rt></ruby>, <ruby>[[陝]]<rt>ㄙㄝㄇ</rt></ruby>
- ⼶ㄇ: <ruby>[[㪘 (char)|㪘]]<rt>ㄌ⼶ㄇ</rt></ruby>, <ruby>[[塩 (char)|塩]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[廉 (char)|廉]]<rt>ㄌ⼶ㄇ</rt></ruby>, <ruby>[[艶]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[閻]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[冉]]<rt>ㄋ⼶ㄇ</rt></ruby>, <ruby>[[奄]]<rt>⼶ㄇ</rt></ruby>, <ruby>[[焰]]<rt>⼶ㄇ</rt></ruby>
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
