---
size: 8
middle_chinese_final: iuᴇt
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 薛A三合** evolved into ⼔ㄊ, with a null-initial subgroup and one singleton (see below)

## CJKV Evolution
薛A三合 [iuᴇt] lands 5 of 8 characters on **⼔ㄊ**, matching the w-glide-bearing half of the Vowels table's documented winner (`wet`). The 2 null/yod-initial characters (悦, 閲) spell **⼶ㄊ** instead — the same real-vs-null-initial spelling distinction already confirmed on [[韻 支B三開|支B三開]] and elsewhere. **劣**, the only l-initial character on this final, lands on **ㄝㄊ** with no same-initial neighbor to collide with — an unconditioned singleton.

## Characters
### In Use
- ⼔ㄊ: <ruby>[[絶 (char)|絶]]<rt>ㄐ⼔ㄊ</rt></ruby>, <ruby>[[雪]]<rt>ㄙ⼔ㄊ</rt></ruby>, <ruby>[[拙]]<rt>ㄐ⼔ㄊ</rt></ruby>, <ruby>[[説]]<rt>ㄙ⼔ㄊ</rt></ruby>, <ruby>[[缺]]<rt>ㄎ⼔ㄊ</rt></ruby>
- ⼶ㄊ: <ruby>[[悦]]<rt>⼶ㄊ</rt></ruby>, <ruby>[[閲]]<rt>⼶ㄊ</rt></ruby>
- ㄝㄊ: <ruby>[[劣]]<rt>ㄌㄝㄊ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iuᴇt
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iuᴇt"
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
