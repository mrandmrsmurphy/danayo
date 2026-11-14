---
size: 2
middle_chinese_final: ɣiᴇi
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 祭B三開** evolved into ㄝ

## CJKV Evolution
祭B三開 [ɣiᴇi] has only 2 characters, 憩 and 滞, and both converge on **ㄝ**, matching the Vowels table's documented winner (`e`, row 037 of 文法 - 99韻図) — no exceptions. Their daughter readings are Mandarin *qì*/*zhì*, Cantonese *hei3*/*zai6*, Korean 게/체 and Vietnamese *khế*/*chệ*; they differ in initial and in every reading, so neither is a homophone of the other.

## Characters
### In Use
- ㄝ: <ruby>[[憩]]<rt>ㄎㄝ</rt></ruby>, <ruby>[[滞]]<rt>ㄐㄝ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇi
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇi"
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
