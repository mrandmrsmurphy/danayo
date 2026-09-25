---
size: 12
middle_chinese_final: iᴇt
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 薛A三開** evolved into ㄝㄊ, with one exception (see below)

## CJKV Evolution
薛A三開 [iᴇt] is nearly uniform: 11 of 12 characters land on **ㄝㄊ**, matching the Vowels table's documented winner (`et`). **熱**, the only palatal-nasal (ȵ) initial character on this final, lands on **⼶ㄊ** with no same-initial neighbor to collide with — an unconditioned singleton.

## Characters
### In Use
- ㄝㄊ: <ruby>[[撇 (char)|撇]]<rt>ㄆㄝㄊ</rt></ruby>, <ruby>[[烈]]<rt>ㄌㄝㄊ</rt></ruby>, <ruby>[[列]]<rt>ㄌㄝㄊ</rt></ruby>, <ruby>[[舌 (char)|舌]]<rt>ㄙㄝㄊ</rt></ruby>, <ruby>[[設]]<rt>ㄙㄝㄊ</rt></ruby>, <ruby>[[洩]]<rt>ㄙㄝㄊ</rt></ruby>, <ruby>[[禼]]<rt>ㄙㄝㄊ</rt></ruby>, <ruby>[[薛]]<rt>ㄙㄝㄊ</rt></ruby>, <ruby>[[折]]<rt>ㄐㄝㄊ</rt></ruby>, <ruby>[[滅 (char)|滅]]<rt>ㄇㄝㄊ</rt></ruby>, <ruby>[[裂]]<rt>ㄌㄝㄊ</rt></ruby>
- ⼶ㄊ: <ruby>[[熱 (char)|熱]]<rt>ㄋ⼶ㄊ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iᴇt
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iᴇt"
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
