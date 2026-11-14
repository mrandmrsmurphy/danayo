---
size: 8
middle_chinese_final: iuᴇt
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 薛A三合** evolved into ⼔ㄊ, with a null-initial subgroup and one singleton (see below)

## CJKV Evolution
薛A三合 [iuᴇt] lands 5 of 8 characters on **⼔ㄊ**, and the Vowels table's documented value for this final (`wet`, row 082 of 文法 - 99韻図) is that outcome. The 2 null/yod-initial characters (悦, 閲) spell **⼶ㄊ** instead, the real-vs-null-initial spelling distinction also seen on [[韻 支B三開|支B三開]]; 悦 and 閲 are identical in every daughter that has a reading (Mandarin *yuè*, Cantonese *jyut6*, Korean 열). 雪 and 説 share Cantonese *syut3* and Korean 설 and take the same syllable ㄙ⼔ㄊ.

**劣**, the only l-initial character on this final, lands on **ㄝㄊ** with no w-glide: l-initial characters avoid the w-glide, as on [[韻 戈一合|戈一合]], so this is a phonotactic constraint rather than an unconditioned singleton. Its Cantonese *lyut3*, Mandarin *liè*, Korean 렬 and Vietnamese *liệt* are otherwise ordinary for the final.

## Characters
### In Use
- ⼔ㄊ: <ruby>[[絶 (char)|絶]]<rt>ㄐ⼔ㄊ</rt></ruby>, <ruby>[[雪 (char)|雪]]<rt>ㄙ⼔ㄊ</rt></ruby>, <ruby>[[拙]]<rt>ㄐ⼔ㄊ</rt></ruby>, <ruby>[[説]]<rt>ㄙ⼔ㄊ</rt></ruby>, <ruby>[[缺]]<rt>ㄎ⼔ㄊ</rt></ruby>
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
