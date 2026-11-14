---
size: 18
middle_chinese_final: iɪp
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 緝A三** splits three ways, with ㄧㄆ the largest group (see below)

## CJKV Evolution
緝A三 [iɪp] lands 10 of 18 characters on **ㄧㄆ** (ip), matching the Vowels table's documented value (`ip`, row 141 of 文法 - 99韻図), while 4 land on **ㄨㄆ** (up) and 4 on **ㄜㄆ**.

The sibilant/palatal class (d͡ʑ, ʑ, z, ɕ, t͡ɕ) scatters across all three groups (十, 拾 and 湿 on ㄧㄆ; 汁, 習, 襲 on ㄜㄆ; 霫 on ㄨㄆ), with the null-initial 揖 also on ㄜㄆ and the ts-initial 葺 and 潗 on ㄨㄆ. The daughters show some of it as true homophony: 習, 襲 and 霫 are identical in Mandarin (*xí*), Cantonese (*zaap6*) and Korean (습), yet 習 and 襲 take ㄙㄜㄆ and 霫 takes ㄙㄨㄆ; 十 and 拾 share Mandarin *shí*, Cantonese *sap6* and Vietnamese *thập*. The l-initial class splits too: 立 and 笠 (Mandarin *lì*, Korean 립) land on ㄧㄆ while 粒 (*lì*, 립, but Cantonese *nap1*) lands on ㄨㄆ.

## Characters
### In Use
- ㄧㄆ: <ruby>[[入 (char)|入]]<rt>ㄋㄧㄆ</rt></ruby>, <ruby>[[十 (char)|十]]<rt>ㄙㄧㄆ</rt></ruby>, <ruby>[[拾]]<rt>ㄙㄧㄆ</rt></ruby>, <ruby>[[立 (char)|立]]<rt>ㄌㄧㄆ</rt></ruby>, <ruby>[[執]]<rt>ㄐㄧㄆ</rt></ruby>, <ruby>[[廿]]<rt>ㄋㄧㄆ</rt></ruby>, <ruby>[[笠]]<rt>ㄌㄧㄆ</rt></ruby>, <ruby>[[集]]<rt>ㄐㄧㄆ</rt></ruby>, <ruby>[[鴔]]<rt>ㄅㄧㄆ</rt></ruby>, <ruby>[[湿 (char)|湿]]<rt>ㄙㄧㄆ</rt></ruby>
- ㄜㄆ: <ruby>[[汁 (char)|汁]]<rt>ㄐㄜㄆ</rt></ruby>, <ruby>[[揖]]<rt>ㄜㄆ</rt></ruby>, <ruby>[[習]]<rt>ㄙㄜㄆ</rt></ruby>, <ruby>[[襲]]<rt>ㄙㄜㄆ</rt></ruby>
- ㄨㄆ: <ruby>[[葺 (char)|葺]]<rt>ㄑㄨㄆ</rt></ruby>, <ruby>[[潗]]<rt>ㄐㄨㄆ</rt></ruby>, <ruby>[[粒]]<rt>ㄌㄨㄆ</rt></ruby>, <ruby>[[霫]]<rt>ㄙㄨㄆ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iɪp
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iɪp"
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
