---
size: 43
middle_chinese_final: iɪ
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂A三開** evolved into ㄧㄜ, with 4 exceptions (see below)

## CJKV Evolution
脂A三開 [iɪ] converges cleanly: 39 of 43 characters land on **ㄧㄜ**, matching the Vowels table's documented winner (`iǝ`, row 015 of 文法 - 99韻図). The "A" in 脂A marks the chongniu-IV finals, which sit in the fourth row of the rime tables ([Wikipedia: Chongniu](https://en.wikipedia.org/wiki/Chongniu), read 2026-11-14), in contrast to its "B" counterpart [[韻 脂B三開|脂B三開]].

The 4 exceptions:
- **鼻**, **琵** (both b-initial) and **瓷** (d͡z-initial) drop the trailing ㄜ, landing on bare **ㄧ** — the regular slot ㄅㄧㄜ for 鼻/琵 is already the second-most-crowded syllable on the page (shared by 比, 庇, 毘), and 瓷's regular slot ㄑㄧㄜ is already held by 次. The daughters support this: 琵 is identical to 毘 in Mandarin (*pí*), Cantonese (*pei4*) and Korean (비), 鼻 is a near-homophone of 比 (Cantonese *bei6* against *bei2*, Korean 비), and 瓷 shares Cantonese *ci* with 次 (*ci4* against *ci3*).
- **屎** drops the ㄧ instead, landing on bare **ㄜ**. No other x-initial character occupies this final, so there is no collision to explain it; its readings (Mandarin *shǐ*, Cantonese *si2*, Korean 히, Vietnamese *hi*) show nothing that points to it.

## Characters
### In Use
- ㄧㄜ: <ruby>[[耆]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[二 (char)|二]]<rt>ㄋㄧㄜ</rt></ruby>, <ruby>[[四 (char)|四]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[地 (char)|地]]<rt>ㄉㄧㄜ</rt></ruby>, <ruby>[[屁 (char)|屁]]<rt>ㄆㄧㄜ</rt></ruby>, <ruby>[[履 (char)|履]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[梨 (char)|梨]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[比 (char)|比]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[至 (char)|至]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[視 (char)|視]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[貳 (char)|貳]]<rt>ㄋㄧㄜ</rt></ruby>, <ruby>[[伊]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[俐]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[利]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[匕]]<rt>ㄆㄧㄜ</rt></ruby>, <ruby>[[夷]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[姿]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[庇]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[恣]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[姨]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[摯]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[棄]]<rt>ㄎㄧㄜ</rt></ruby>, <ruby>[[毘]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[次]]<rt>ㄑㄧㄜ</rt></ruby>, <ruby>[[痢]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[祁]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[私]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[羨]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[肆]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[肌]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[脂]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[胰]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[自]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[茨]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[諡]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[諮]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[資]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[飢]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[鰭]]<rt>ㄍㄧㄜ</rt></ruby>
- ㄧ: <ruby>[[鼻 (char)|鼻]]<rt>ㄅㄧ</rt></ruby>, <ruby>[[琵]]<rt>ㄅㄧ</rt></ruby>, <ruby>[[瓷]]<rt>ㄑㄧ</rt></ruby>
- ㄜ: <ruby>[[屎 (char)|屎]]<rt>ㄏㄜ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iɪ
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iɪ"
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
