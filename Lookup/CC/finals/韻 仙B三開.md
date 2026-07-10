---
size: 11
middle_chinese_final: ɣiᴇn
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 仙B三開** mostly evolved into ⼶ㄋ, with three exceptions (see below)

## CJKV Evolution
仙B三開 [ɣiᴇn] lands 8 of 11 characters on **⼶ㄋ**, matching the y-glide-bearing half of the Vowels table's documented dual winner (`yen/en`). The remaining 3 — 諺, 展, 纏 — land on **ㄝㄋ** instead, with no same-initial neighbor in the main group to explain the shift; 展 and 纏 (retroflex ʈ/ɖ) share their own initial class only with each other.

## Characters
### In Use
- ⼶ㄋ: <ruby>[[冕]]<rt>ㄇ⼶ㄋ</rt></ruby>, <ruby>[[乾 (char)|乾]]<rt>ㄍ⼶ㄋ</rt></ruby>, <ruby>[[卞]]<rt>ㄅ⼶ㄋ</rt></ruby>, <ruby>[[免]]<rt>ㄇ⼶ㄋ</rt></ruby>, <ruby>[[変 (char)|変]]<rt>ㄅ⼶ㄋ</rt></ruby>, <ruby>[[件]]<rt>ㄍ⼶ㄋ</rt></ruby>, <ruby>[[鍵 (char)|鍵]]<rt>ㄍ⼶ㄋ</rt></ruby>, <ruby>[[勉 (char)|勉]]<rt>ㄇ⼶ㄋ</rt></ruby>
- ㄝㄋ: <ruby>[[諺]]<rt>ㄝㄋ</rt></ruby>, <ruby>[[展]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[纏]]<rt>ㄐㄝㄋ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇn
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇn"
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
