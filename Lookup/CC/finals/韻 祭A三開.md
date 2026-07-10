---
size: 17
middle_chinese_final: iᴇi
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 祭A三開** evolved into ㄝ (see below)

## CJKV Evolution
祭A三開 [iᴇi] lands 14 of 17 characters on **ㄝ**, matching the Vowels table's documented winner (`e`). 裔 and 曳 (both yod-initial) spell **⼶**, the established null/glide-initial convention seen throughout this sweep, not a distinct final-level fact.

**制** is the one real exception: it shares its MC initial (t͡ɕ) with 製, which already occupies ㄐㄝ. Rather than colliding, 制 adds a trailing ㄧ and lands on **ㄝㄧ**.

## Characters
### In Use
- ㄝ: <ruby>[[芸]]<rt>ㄝ</rt></ruby>, <ruby>[[厉 (char)|厉]]<rt>ㄌㄝ</rt></ruby>, <ruby>[[袂 (char)|袂]]<rt>ㄇㄝ</rt></ruby>, <ruby>[[世]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[製]]<rt>ㄐㄝ</rt></ruby>, <ruby>[[誓]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[励]]<rt>ㄌㄝ</rt></ruby>, <ruby>[[幣 (char)|幣]]<rt>ㄆㄝ</rt></ruby>, <ruby>[[勢]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[際 (char)|際]]<rt>ㄐㄝ</rt></ruby>, <ruby>[[貰]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[逝]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[蔽]]<rt>ㄆㄝ</rt></ruby>, <ruby>[[例]]<rt>ㄌㄝ</rt></ruby>
- ⼶: <ruby>[[裔]]<rt>⼶</rt></ruby>, <ruby>[[曳]]<rt>⼶</rt></ruby>
- ㄝㄧ: <ruby>[[制]]<rt>ㄐㄝㄧ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iᴇi
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iᴇi"
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
