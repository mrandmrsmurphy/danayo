---
size: 7
middle_chinese_final: iuᴇi
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 祭A三合** evolved into ㄝ (see below)

## CJKV Evolution
祭A三合 [iuᴇi] lands 5 of 7 characters on **ㄝ**, matching the Vowels table's documented winner (`e`). The remaining 2 (叡, 鋭) are both yod-initial and spell **⼶**, the established null/glide-initial convention — not a genuine exception. This final is fully explained without any unconditioned outliers.

## Characters
### In Use
- ㄝ: <ruby>[[歳]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[税]]<rt>ㄙㄝ</rt></ruby>, <ruby>[[脆]]<rt>ㄑㄝ</rt></ruby>, <ruby>[[芮]]<rt>ㄋㄝ</rt></ruby>, <ruby>[[魏]]<rt>ㄝ</rt></ruby>
- ⼶: <ruby>[[叡]]<rt>⼶</rt></ruby>, <ruby>[[鋭]]<rt>⼶</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iuᴇi
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iuᴇi"
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
