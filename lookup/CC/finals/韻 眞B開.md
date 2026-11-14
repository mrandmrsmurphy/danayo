---
size: 16
middle_chinese_final: ɣiɪn
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 眞B開** evolved into ㄧㄋ, with two escapees (see below)

## CJKV Evolution
眞B開 [ɣiɪn] converges cleanly: 14 of 16 characters land on **ㄧㄋ**, matching the Vowels table's documented winner (`in`) and the pattern of its division-3A sibling [[韻 眞A開|眞A開]].

**閔** dodges a crowded ㄇㄧㄋ (5 members: 憫, 珉, 敏, 旻, 暋, all m-initial like 閔 itself) via a coda-shift to **ㄧㄇ**; 閔 is identical to 憫 in Mandarin (*mǐn*), Cantonese (*man5*), Korean (민) and Vietnamese (*mẫn*), and none of its readings has an m coda. **饉** is a true homophone of 僅 in Mandarin (*jǐn*), Cantonese (*gan2*) and Korean (근), and its regular syllable ㄍㄧㄋ is held by 僅 and also by 近, 勤, 斤 and others on [[韻 欣|欣]]; it takes the otherwise unused vowel, landing on **ㄍㄨㄋ**, a syllable that 君, 軍, 群 and 郡 on [[韻 文|文]] also occupy.

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
