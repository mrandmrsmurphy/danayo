---
size: 41
middle_chinese_final: iɪ
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂A三開** evolved into ㄧㄜ, with 3 exceptions (see below)

## CJKV Evolution
脂A三開 [iɪ] converges far more cleanly than a typical division-3 final: 38 of 41 characters land on **ㄧㄜ**, matching the Vowels table's documented winner (`iə`). This tracks real historical linguistics — the "A" in 脂A marks a *chongniu* division-3 final that patterns like division-4 (clean convergence), in contrast to its "B" counterpart [[韻 支B三開|支B三開]]/[[韻 支B三合|支B三合]], which fractured heavily earlier in this sweep. Chongniu A/B status turns out to be directly visible in how uniform a final's outcome page ends up looking.

The 3 exceptions:
- **鼻** and **琵** (both b-initial) drop the trailing ㄜ, landing on bare **ㄧ** — likely homophony overflow, since their regular slot ㄅㄧㄜ is already the second-most-crowded syllable on the page (shared by 比, 庇, 毘).
- **屎** drops the ㄧ instead, landing on bare **ㄜ**. Unlike the other two, this isn't obviously homophony-driven (no other x-initial character occupies this final at all). Worth flagging: 屎's own daughter readings in the corpus (Mandarin xī, Cantonese hei1, Korean 히) don't match the character's real standard Mandarin reading (shǐ, "feces") — this may be a data mix-up with a different character rather than a genuine outcome, similar to the 豕/靡 anomalies found earlier in this sweep.

## Characters
### In Use
- ㄧㄜ: <ruby>[[二 (char)|二]]<rt>ㄋㄧㄜ</rt></ruby>, <ruby>[[四 (char)|四]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[地 (char)|地]]<rt>ㄉㄧㄜ</rt></ruby>, <ruby>[[屁 (char)|屁]]<rt>ㄆㄧㄜ</rt></ruby>, <ruby>[[履 (char)|履]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[梨 (char)|梨]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[比 (char)|比]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[至 (char)|至]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[視 (char)|視]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[貳 (char)|貳]]<rt>ㄋㄧㄜ</rt></ruby>, <ruby>[[伊]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[俐]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[利]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[匕]]<rt>ㄆㄧㄜ</rt></ruby>, <ruby>[[夷]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[姿]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[庇]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[恣]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[姨]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[摯]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[棄]]<rt>ㄎㄧㄜ</rt></ruby>, <ruby>[[毘]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[次]]<rt>ㄑㄧㄜ</rt></ruby>, <ruby>[[痢]]<rt>ㄌㄧㄜ</rt></ruby>, <ruby>[[祁]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[私]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[羨]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[肆]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[肌]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[脂]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[胰]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[自]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[茨]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[諡]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[諮]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[資]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[飢]]<rt>ㄍㄧㄜ</rt></ruby>, <ruby>[[鰭]]<rt>ㄍㄧㄜ</rt></ruby>
- ㄧ: <ruby>[[鼻 (char)|鼻]]<rt>ㄅㄧ</rt></ruby>, <ruby>[[琵]]<rt>ㄅㄧ</rt></ruby>
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
