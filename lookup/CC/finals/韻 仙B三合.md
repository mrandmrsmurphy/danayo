---
size: 12
middle_chinese_final: ɣiuᴇn
date-last-perfect: 2026-10-04
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 仙B三合** mostly evolved into ⼔ㄋ, with two null-initial exceptions (see below)

## CJKV Evolution
仙B三合 [ɣiuᴇn] lands 10 of 12 characters on **⼔ㄋ**, matching the y-glide-bearing half of the Vowels table's documented dual winner (`wen/on`).

**媛** and **援** are both null-initial (ø) — the exact same initial class as 院, which stays in the main group. Rather than joining 院 on the already 10-member-crowded ⼔ㄋ, 媛 and 援 drop the glide entirely and land on **ㄛㄋ**.

## Characters
### In Use
- ⼔ㄋ: <ruby>[[圏 (char)|圏]]<rt>ㄍ⼔ㄋ</rt></ruby>, <ruby>[[巻 (char)|巻]]<rt>ㄍ⼔ㄋ</rt></ruby>, <ruby>[[栓 (char)|栓]]<rt>ㄙ⼔ㄋ</rt></ruby>, <ruby>[[伝]]<rt>ㄐ⼔ㄋ</rt></ruby>, <ruby>[[倦]]<rt>ㄍ⼔ㄋ</rt></ruby>, <ruby>[[拳]]<rt>ㄍ⼔ㄋ</rt></ruby>, <ruby>[[権]]<rt>ㄍ⼔ㄋ</rt></ruby>, <ruby>[[篆]]<rt>ㄐ⼔ㄋ</rt></ruby>, <ruby>[[院]]<rt>⼔ㄋ</rt></ruby>, <ruby>[[転]]<rt>ㄐ⼔ㄋ</rt></ruby>
- ㄛㄋ: <ruby>[[媛]]<rt>ㄛㄋ</rt></ruby>, <ruby>[[援]]<rt>ㄛㄋ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiuᴇn
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiuᴇn"
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
