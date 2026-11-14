---
size: 3
middle_chinese_final: ɣiuᴇi
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 祭B三合** evolved into ㄝ

## CJKV Evolution
祭B三合 [ɣiuᴇi] has only 3 characters (彗, 穢, 衛), and all three converge on **ㄝ**, matching the Vowels table's documented winner (`e`).

This is a 合 (rounded) final, yet none of its 3 characters carries a w-glide, so the 合 → w-glide tendency has no support here. The daughters do show the rounding: Cantonese *wai* for all three (*wai6*, *wai3*, *wai6*), Mandarin *huì*/*huì*/*wèi*, and Korean 혜/예/위. 彗 and 穢 share Mandarin *huì* but differ in Cantonese tone and in Korean, so none is a homophone of another.

## Characters
### In Use
- ㄝ: <ruby>[[彗]]<rt>ㄏㄝ</rt></ruby>, <ruby>[[穢]]<rt>ㄝ</rt></ruby>, <ruby>[[衛]]<rt>ㄝ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiuᴇi
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiuᴇi"
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
