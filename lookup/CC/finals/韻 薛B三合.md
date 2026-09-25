---
size: 1
middle_chinese_final: ɣiuᴇt
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 薛B三合** has a single character, 綴

## CJKV Evolution
薛B三合 [ɣiuᴇt] has only one character in the corpus, 綴, which lands on **⼔ㄊ** — carrying the w-glide expected for a 合 (rounded) final, matching the Vowels table's documented winner (`wet`).

## Characters
### In Use
- ⼔ㄊ: <ruby>[[綴 (char)|綴]]<rt>ㄐ⼔ㄊ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiuᴇt
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiuᴇt"
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
