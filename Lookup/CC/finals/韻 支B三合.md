---
size: 11
middle_chinese_final: ɣiuᴇ
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 支B三合** evolved into ⼔ㄧ, with two homophony-driven exceptions (see below)

## CJKV Evolution
支B三合 [ɣiuᴇ] lands 9 of 11 characters on **⼔ㄧ**, matching the Vowels table's documented winner (`wei`) for this final.

**為** is the standout exception. Its daughter readings (wèi, wai4, 위) look essentially identical to 委/萎/危/偽/倭's — there is no phonological reason it should differ. But the regular ⼔ㄧ slot already holds all 9 of those other characters, the single most crowded same-final slot found on this project so far, and 為 alone dodges it entirely, landing on **⼔ㄋ** instead.

**錘** shares its MC initial (ɖ) exactly with 槌, which already occupies ㄐ⼔ㄧ. Rather than colliding, 錘 shifts to **ㄨㄧ**, both losing the ⼔ and switching from plain ㄐ to aspirated ㄑ in the same move.

## Characters
### In Use
- ⼔ㄧ: <ruby>[[偽 (char)|偽]]<rt>⼔ㄧ</rt></ruby>, <ruby>[[委 (char)|委]]<rt>⼔ㄧ</rt></ruby>, <ruby>[[毀 (char)|毀]]<rt>ㄏ⼔ㄧ</rt></ruby>, <ruby>[[槌 (char)|槌]]<rt>ㄐ⼔ㄧ</rt></ruby>, <ruby>[[跪 (char)|跪]]<rt>ㄎ⼔ㄧ</rt></ruby>, <ruby>[[倭]]<rt>⼔ㄧ</rt></ruby>, <ruby>[[危]]<rt>⼔ㄧ</rt></ruby>, <ruby>[[萎]]<rt>⼔ㄧ</rt></ruby>, <ruby>[[衰]]<rt>ㄙ⼔ㄧ</rt></ruby>
- ⼔ㄋ: <ruby>[[為 (char)|為]]<rt>⼔ㄋ</rt></ruby>
- ㄨㄧ: <ruby>[[錘]]<rt>ㄑㄨㄧ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiuᴇ
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiuᴇ"
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
