---
size: 16
middle_chinese_final: ɣiɪn
date-last-perfect: 2026-10-06
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 眞B開** evolved into ㄧㄋ, with two escapees (see below)

## CJKV Evolution
眞B開 [ɣiɪn] converges cleanly: 14 of 16 characters land on **ㄧㄋ**, matching the Vowels table's documented winner (`in`) and its own division-3A sibling [[韻 眞A開|眞A開]].

**閔** dodges a crowded ㄇㄧㄋ (5 members: 憫, 珉, 敏, 旻, 暋, all m-initial like 閔 itself) via the familiar coda-shift to **ㄧㄇ**. **饉** dodges a more modest 1-member ㄍㄧㄋ (僅, also g-initial) by dropping the vowel entirely, landing on **ㄨㄋ**.

## Characters
### In Use
- ㄧㄋ: <ruby>[[陣]]<rt>ㄑㄧㄋ</rt></ruby>, <ruby>[[憫 (char)|憫]]<rt>ㄇㄧㄋ</rt></ruby>, <ruby>[[珉]]<rt>ㄇㄧㄋ</rt></ruby>, <ruby>[[敏 (char)|敏]]<rt>ㄇㄧㄋ</rt></ruby>, <ruby>[[旻]]<rt>ㄇㄧㄋ</rt></ruby>, <ruby>[[巾]]<rt>ㄎㄧㄋ</rt></ruby>, <ruby>[[彬]]<rt>ㄆㄧㄋ</rt></ruby>, <ruby>[[陳]]<rt>ㄐㄧㄋ</rt></ruby>, <ruby>[[銀 (char)|銀]]<rt>ㄧㄋ</rt></ruby>, <ruby>[[僅]]<rt>ㄍㄧㄋ</rt></ruby>, <ruby>[[鎮 (char)|鎮]]<rt>ㄑㄧㄋ</rt></ruby>, <ruby>[[貧]]<rt>ㄅㄧㄋ</rt></ruby>, <ruby>[[珍 (char)|珍]]<rt>ㄑㄧㄋ</rt></ruby>, <ruby>[[暋]]<rt>ㄇㄧㄋ</rt></ruby>
- ㄨㄋ: <ruby>[[饉]]<rt>ㄍㄨㄋ</rt></ruby>
- ㄧㄇ: <ruby>[[閔]]<rt>ㄇㄧㄇ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiɪn
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiɪn"
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
