---
size: 8
middle_chinese_final: ɣiᴇt
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 薛B三開** evolved into ㄝㄊ, with one exception (see below)

## CJKV Evolution
薛B三開 [ɣiᴇt] is nearly uniform: 7 of 8 characters land on **ㄝㄊ**, matching the Vowels table's documented winner (`et`).

**屮** is the lone exception, landing on **ㄧㄊ** — and it's a particularly clean illustration of the "no findable rule" phenomenon: its daughter readings (chè, cit3, 철) are *identical* to 撤's, which stays on the regular ㄉㄝㄊ. Two characters, matching MC-derived pronunciation in all three checked daughter languages, still diverge — echoing the 瑟/虱 pair on [[韻 櫛|櫛]].

## Characters
### In Use
- ㄝㄊ: <ruby>[[別 (char)|別]]<rt>ㄅㄝㄊ</rt></ruby>, <ruby>[[掲 (char)|掲]]<rt>ㄎㄝㄊ</rt></ruby>, <ruby>[[撤 (char)|撤]]<rt>ㄉㄝㄊ</rt></ruby>, <ruby>[[偈]]<rt>ㄍㄝㄊ</rt></ruby>, <ruby>[[傑]]<rt>ㄍㄝㄊ</rt></ruby>, <ruby>[[哲]]<rt>ㄐㄝㄊ</rt></ruby>, <ruby>[[澈]]<rt>ㄐㄝㄊ</rt></ruby>
- ㄧㄊ: <ruby>[[屮]]<rt>ㄊㄧㄊ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇt
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇt"
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - middle_chinese_initial
      - middle_chinese_final
      - 注音
      - tags
    sort:
      - property: 注音
        direction: ASC
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
      note.middle_chinese_final: 86

```
