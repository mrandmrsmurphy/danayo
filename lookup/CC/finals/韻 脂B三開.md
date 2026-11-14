---
size: 26
middle_chinese_final: ɣiɪ
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂B三開** evolved into ㄧㄜ, with a labial-initial subgroup on bare ㄧ (see below)

## CJKV Evolution
脂B三開 [ɣiɪ] converges cleanly: 23 of 26 characters land on **ㄧㄜ**, matching the Vowels table's documented winner (`iǝ`, row 017 of 文法 - 99韻図).

The 3 exceptions — 美, 丕, 砒 — all drop the trailing ㄜ and land on bare **ㄧ**. 美's regular ㄇㄧㄜ slot already holds 4 characters (眉, 寐, 薇, 魅), the most crowded syllable on the page, and 美 is a near-homophone of 眉 (Korean 미, Cantonese *mei5* against *mei4*, Mandarin *měi* against *méi*). 丕 and 砒 are identical in every daughter (Mandarin *pī*, Cantonese *pei1*, Korean 비) and share the syllable ㄆㄧ, so they are not separated from each other; their regular ㄆㄧㄜ is held by characters of other finals (屁, 匕), which accounts for the shift.

Data-quality flag: **鄙**'s 注音 (ㄈㄧㄜ) uses the labiodental ㄈ, but its MC initial is the plain bilabial stop *p*, and every daughter reading (Mandarin *bǐ*, Cantonese *pei2*, Korean 비, Vietnamese *bỉ*) points to a bilabial, not a labiodental, onset. This looks like a 注音 typo in the corpus (expected ㄅㄧㄜ or ㄆㄧㄜ) rather than a genuine outcome.

## Characters
### In Use
- ㄧㄜ: <ruby>[[悲 (char)|悲]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[眉 (char)|眉]]<rt>ㄇㄧㄜ</rt></ruby>, <ruby>[[致 (char)|致]]<rt>ㄑㄧㄜ</rt></ruby>, <ruby>[[遅 (char)|遅]]<rt>ㄑㄧㄜ</rt></ruby>, <ruby>[[雉 (char)|雉]]<rt>ㄉㄧㄜ</rt></ruby>, <ruby>[[備]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[器]]<rt>ㄎㄧㄜ</rt></ruby>, <ruby>[[尼]]<rt>ㄋㄧㄜ</rt></ruby>, <ruby>[[師]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[矢 (char)|矢]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[寐]]<rt>ㄇㄧㄜ</rt></ruby>, <ruby>[[懿]]<rt>ㄧㄜ</rt></ruby>, <ruby>[[指]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[旨]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[死]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[秘]]<rt>ㄅㄧㄜ</rt></ruby>, <ruby>[[稚]]<rt>ㄉㄧㄜ</rt></ruby>, <ruby>[[獅]]<rt>ㄙㄧㄜ</rt></ruby>, <ruby>[[砥]]<rt>ㄐㄧㄜ</rt></ruby>, <ruby>[[緻]]<rt>ㄉㄧㄜ</rt></ruby>, <ruby>[[鄙]]<rt>ㄈㄧㄜ</rt></ruby>, <ruby>[[薇]]<rt>ㄇㄧㄜ</rt></ruby>, <ruby>[[魅]]<rt>ㄇㄧㄜ</rt></ruby>
- ㄧ: <ruby>[[美 (char)|美]]<rt>ㄇㄧ</rt></ruby>, <ruby>[[丕]]<rt>ㄆㄧ</rt></ruby>, <ruby>[[砒]]<rt>ㄆㄧ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiɪ
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiɪ"
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
