---
size: 8
middle_chinese_final: ɣiuɪ
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂B合** mostly evolved into ㄨㄧ (see below)

## CJKV Evolution
脂B合 [ɣiuɪ] lands 5 of 8 characters on **ㄨㄧ**, matching the Vowels table's documented winner (`ui`, row 018 of 文法 - 99韻図). 位, the one null-initial member, spells ⼔ㄧ, the same null-initial convention as on [[韻 脂A合|脂A合]] and [[韻 支B三合|支B三合]].

**水** shares its resulting bopomofo initial (ㄙ) with 帥, which already occupies ㄙㄨㄧ, a syllable that 睡, 随, 髄 and others on [[韻 支三合|支三合]] also hold. 水 is a near-homophone of 帥 (Cantonese *seoi2* against *seoi3*, Korean 수 for both, Mandarin *shuǐ* against *shuài*), and dodges by dropping the -ㄧ entirely, landing on plain **ㄨ**.

**櫃** (g-initial; *guì*, *gwai6*, 궤) lands on **⼔**, the one character on bare ⼔: its regular ㄍㄨㄧ is held by 季, 愧 and 癸 on [[韻 脂A合|脂A合]], and 櫃 shares Cantonese *gwai* with all three.

## Characters
### In Use
- ㄨㄧ: <ruby>[[追 (char)|追]]<rt>ㄊㄨㄧ</rt></ruby>, <ruby>[[軌 (char)|軌]]<rt>ㄎㄨㄧ</rt></ruby>, <ruby>[[墜]]<rt>ㄐㄨㄧ</rt></ruby>, <ruby>[[帥]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[椎]]<rt>ㄑㄨㄧ</rt></ruby>
- ⼔ㄧ: <ruby>[[位]]<rt>⼔ㄧ</rt></ruby>
- ㄨ: <ruby>[[水 (char)|水]]<rt>ㄙㄨ</rt></ruby>
- ⼔: <ruby>[[櫃 (char)|櫃]]<rt>ㄍ⼔</rt></ruby>

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
