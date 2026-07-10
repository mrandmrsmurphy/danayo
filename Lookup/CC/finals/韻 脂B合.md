---
size: 7
middle_chinese_final: ɣiuɪ
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂B合** mostly evolved into ㄨㄧ (see below)

## CJKV Evolution
脂B合 [ɣiuɪ] lands 5 of 7 characters on **ㄨㄧ**, matching the Vowels table's documented winner (`ui`). 位, the one null-initial member, spells ⼔ㄧ instead — the same null-initial convention already confirmed across [[韻 脂A合|脂A合]] and [[韻 支B三合|支B三合]], not a new phenomenon.

**水** is the more interesting case: its daughter readings (shuǐ, seoi2, 수) are entirely ordinary for this final, but it shares its resulting bopomofo initial (ㄙ) with 帥, which already occupies ㄙㄨㄧ — an exact collision. 水 dodges by dropping the -ㄧ entirely, landing on plain **ㄨ**.

## Characters
### In Use
- ㄨㄧ: <ruby>[[追 (char)|追]]<rt>ㄊㄨㄧ</rt></ruby>, <ruby>[[軌 (char)|軌]]<rt>ㄎㄨㄧ</rt></ruby>, <ruby>[[墜]]<rt>ㄐㄨㄧ</rt></ruby>, <ruby>[[帥]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[椎]]<rt>ㄑㄨㄧ</rt></ruby>
- ⼔ㄧ: <ruby>[[位]]<rt>⼔ㄧ</rt></ruby>
- ㄨ: <ruby>[[水 (char)|水]]<rt>ㄙㄨ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiuɪ
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiuɪ"
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
