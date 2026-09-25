---
size: 15
middle_chinese_final: ɣiɪp
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 緝B三** genuinely two-way splits, matching its own documented ip/up ambiguity

## CJKV Evolution
緝B三 [ɣiɪp] splits nearly evenly along its own documented ambiguous D value (`ip/up`): 8 of 15 characters land on **ㄧㄆ** (ip), and 7 land on **ㄨㄆ** (up).

The k/g class scatters across both groups — 急, 級, 給 land on ㄧㄆ while 及, 汲 land on ㄨㄆ — another instance of the same-initial-class scatter documented repeatedly in this sweep.

## Characters
### In Use
- ㄧㄆ: <ruby>[[吸 (char)|吸]]<rt>ㄏㄧㄆ</rt></ruby>, <ruby>[[急 (char)|急]]<rt>ㄍㄧㄆ</rt></ruby>, <ruby>[[泣 (char)|泣]]<rt>ㄎㄧㄆ</rt></ruby>, <ruby>[[蟄 (char)|蟄]]<rt>ㄑㄧㄆ</rt></ruby>, <ruby>[[渋]]<rt>ㄙㄧㄆ</rt></ruby>, <ruby>[[級]]<rt>ㄍㄧㄆ</rt></ruby>, <ruby>[[給]]<rt>ㄍㄧㄆ</rt></ruby>, <ruby>[[邑]]<rt>ㄧㄆ</rt></ruby>
- ㄨㄆ: <ruby>[[及 (char)|及]]<rt>ㄍㄨㄆ</rt></ruby>, <ruby>[[汲 (char)|汲]]<rt>ㄎㄨㄆ</rt></ruby>, <ruby>[[湆]]<rt>ㄎㄨㄆ</rt></ruby>, <ruby>[[皀]]<rt>ㄆㄨㄆ</rt></ruby>, <ruby>[[翕]]<rt>ㄏㄨㄆ</rt></ruby>, <ruby>[[雴]]<rt>ㄊㄨㄆ</rt></ruby>, <ruby>[[鵖]]<rt>ㄅㄨㄆ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiɪp
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiɪp"
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
