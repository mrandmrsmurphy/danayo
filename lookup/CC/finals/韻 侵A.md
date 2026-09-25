---
size: 25
middle_chinese_final: iɪm
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 侵A** evolved into ㄧㄇ, with a near-homophone pair diverging into two separate escapes (see below)

## CJKV Evolution
侵A [iɪm] converges heavily: 21 of 25 characters land on **ㄧㄇ**, matching the Vowels table's documented winner (`im`).

**凜** and **懍** are near-homophones (both l-initial, Mandarin *lǐn*, Cantonese *lam5*, Korean 름) dodging the crowded 4-member l-slot on the main group (林, 淋, 琳, 臨) — but by two different routes: 凜 lands on **ㄨㄇ**, 懍 on **ㄜㄇ**, converging with neither the main group nor each other. **稟** (p), the only labial in this final, lands alongside 凜 on ㄨㄇ, unconditioned.

Data-quality flag: 冘 is tagged with initial m, but its Mandarin (*yín*), Cantonese (*jam4*), and Korean (유) readings all point to a y-initial (以) word, not an m-initial one — likely mistagged.

## Characters
### In Use
- ㄧㄇ: <ruby>[[妊 (char)|妊]]<rt>ㄋㄧㄇ</rt></ruby>, <ruby>[[寝 (char)|寝]]<rt>ㄑㄧㄇ</rt></ruby>, <ruby>[[尋 (char)|尋]]<rt>ㄙㄧㄇ</rt></ruby>, <ruby>[[心 (char)|心]]<rt>ㄙㄧㄇ</rt></ruby>, <ruby>[[林 (char)|林]]<rt>ㄌㄧㄇ</rt></ruby>, <ruby>[[浸 (char)|浸]]<rt>ㄑㄧㄇ</rt></ruby>, <ruby>[[淋 (char)|淋]]<rt>ㄌㄧㄇ</rt></ruby>, <ruby>[[淫]]<rt>ㄧㄇ</rt></ruby>, <ruby>[[針]]<rt>ㄐㄧㄇ</rt></ruby>, <ruby>[[鱏 (char)|鱏]]<rt>ㄏㄧㄇ</rt></ruby>, <ruby>[[任]]<rt>ㄋㄧㄇ</rt></ruby>, <ruby>[[侵]]<rt>ㄑㄧㄇ</rt></ruby>, <ruby>[[壬]]<rt>ㄋㄧㄇ</rt></ruby>, <ruby>[[審]]<rt>ㄙㄧㄇ</rt></ruby>, <ruby>[[斟]]<rt>ㄐㄧㄇ</rt></ruby>, <ruby>[[枕]]<rt>ㄐㄧㄇ</rt></ruby>, <ruby>[[沈]]<rt>ㄑㄧㄇ</rt></ruby>, <ruby>[[深]]<rt>ㄙㄧㄇ</rt></ruby>, <ruby>[[琳]]<rt>ㄌㄧㄇ</rt></ruby>, <ruby>[[甚]]<rt>ㄙㄧㄇ</rt></ruby>, <ruby>[[臨]]<rt>ㄌㄧㄇ</rt></ruby>
- ㄨㄇ: <ruby>[[凜 (char)|凜]]<rt>ㄌㄨㄇ</rt></ruby>, <ruby>[[冘]]<rt>ㄇㄨㄇ</rt></ruby>, <ruby>[[稟]]<rt>ㄅㄨㄇ</rt></ruby>
- ㄜㄇ: <ruby>[[懍]]<rt>ㄌㄜㄇ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iɪm
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iɪm"
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
