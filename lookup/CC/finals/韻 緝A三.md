---
size: 18
middle_chinese_final: iɪp
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 緝A三** genuinely three-way splits, extending its own documented two-way D ambiguity (see below)

## CJKV Evolution
緝A三 [iɪp]'s Vowels-table D value is already listed as ambiguous (`ip/up`), and the corpus shows a third group besides: 8 of 18 characters land on **ㄧㄆ** (ip), 4 on **ㄨㄆ** (up), and 6 on a third group, **ㄜㄆ**.

The sibilant/palatal class (d͡ʑ, ʑ, z, ɕ, t͡ɕ) scatters across all three groups (十 on ㄧㄆ; 拾, 習, 襲, 湿 on ㄜㄆ; 霫 on ㄨㄆ), echoing the recurring scatter pattern documented on [[韻 之|之]], [[韻 蒸|蒸]], and [[韻 侵B|侵B]]. The l-initial class splits too: 立/笠 land on ㄧㄆ while 粒 lands on ㄨㄆ.

## Characters
### In Use
- ㄧㄆ: <ruby>[[入 (char)|入]]<rt>ㄋㄧㄆ</rt></ruby>, <ruby>[[十 (char)|十]]<rt>ㄙㄧㄆ</rt></ruby>, <ruby>[[立 (char)|立]]<rt>ㄌㄧㄆ</rt></ruby>, <ruby>[[執]]<rt>ㄐㄧㄆ</rt></ruby>, <ruby>[[廿]]<rt>ㄋㄧㄆ</rt></ruby>, <ruby>[[笠]]<rt>ㄌㄧㄆ</rt></ruby>, <ruby>[[集]]<rt>ㄐㄧㄆ</rt></ruby>, <ruby>[[鴔]]<rt>ㄅㄧㄆ</rt></ruby>
- ㄜㄆ: <ruby>[[汁 (char)|汁]]<rt>ㄐㄜㄆ</rt></ruby>, <ruby>[[湿 (char)|湿]]<rt>ㄙㄜㄆ</rt></ruby>, <ruby>[[拾]]<rt>ㄙㄜㄆ</rt></ruby>, <ruby>[[揖]]<rt>ㄜㄆ</rt></ruby>, <ruby>[[習]]<rt>ㄙㄜㄆ</rt></ruby>, <ruby>[[襲]]<rt>ㄙㄜㄆ</rt></ruby>
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
