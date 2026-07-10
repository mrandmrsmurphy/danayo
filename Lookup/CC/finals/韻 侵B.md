---
size: 21
middle_chinese_final: ɣiɪm
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 侵B** genuinely splits three ways, matching its own ambiguous documented D value

## CJKV Evolution
侵B [ɣiɪm], like [[韻 登開|登開]], has an ambiguous Vowels-table D value (`im/um/om`), and the corpus confirms all three: 10 of 21 characters land on **ㄨㄇ** (um), 7 on **ㄧㄇ** (im), and 2 on **ㄛㄇ** (om) — plus 2 more on a fourth group, **ㄜㄇ**.

The velar k/g class scatters across three of the four groups (琴 on ㄨㄇ; 今, 金, 禁, 襟, 禽 on ㄧㄇ; 錦 on ㄛㄇ), echoing the large same-initial-class scatters documented on [[韻 蒸|蒸]] and [[韻 之|之]]. **歆** and **鑫** are true homophones (both x-initial, Mandarin *xīn*, Cantonese *jam1*, Korean 흠) that diverge anyway, landing on ㄨㄇ and ㄜㄇ respectively.

## Characters
### In Use
- ㄨㄇ: <ruby>[[品 (char)|品]]<rt>ㄆㄨㄇ</rt></ruby>, <ruby>[[朕 (char)|朕]]<rt>ㄐㄨㄇ</rt></ruby>, <ruby>[[琴 (char)|琴]]<rt>ㄍㄨㄇ</rt></ruby>, <ruby>[[飲]]<rt>ㄨㄇ</rt></ruby>, <ruby>[[森]]<rt>ㄙㄨㄇ</rt></ruby>, <ruby>[[欽]]<rt>ㄎㄨㄇ</rt></ruby>, <ruby>[[歆]]<rt>ㄏㄨㄇ</rt></ruby>, <ruby>[[砧]]<rt>ㄉㄨㄇ</rt></ruby>, <ruby>[[闖]]<rt>ㄊㄨㄇ</rt></ruby>, <ruby>[[音]]<rt>ㄨㄇ</rt></ruby>
- ㄧㄇ: <ruby>[[今 (char)|今]]<rt>ㄍㄧㄇ</rt></ruby>, <ruby>[[賃 (char)|賃]]<rt>ㄋㄧㄇ</rt></ruby>, <ruby>[[金]]<rt>ㄍㄧㄇ</rt></ruby>, <ruby>[[陰]]<rt>ㄧㄇ</rt></ruby>, <ruby>[[禁]]<rt>ㄍㄧㄇ</rt></ruby>, <ruby>[[禽]]<rt>ㄎㄧㄇ</rt></ruby>, <ruby>[[襟]]<rt>ㄍㄧㄇ</rt></ruby>
- ㄜㄇ: <ruby>[[吟]]<rt>ㄜㄇ</rt></ruby>, <ruby>[[鑫]]<rt>ㄏㄜㄇ</rt></ruby>
- ㄛㄇ: <ruby>[[滲]]<rt>ㄙㄛㄇ</rt></ruby>, <ruby>[[錦]]<rt>ㄎㄛㄇ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiɪm
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiɪm"
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
