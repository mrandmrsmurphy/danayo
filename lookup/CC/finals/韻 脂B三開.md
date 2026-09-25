---
size: 26
middle_chinese_final: ɣiɪ
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂B三開** evolved into ㄧㄜ, with a labial-initial subgroup on bare ㄧ (see below)

## CJKV Evolution
脂B三開 [ɣiɪ] converges cleanly: 23 of 26 characters land on **ㄧㄜ**, matching the Vowels table's documented winner (`iə`) — a "B"-grade chongniu final converging about as tightly as its "A"-grade counterpart [[韻 脂A三開|脂A三開]] did, which softens the earlier hypothesis that A always converges more cleanly than B; rhyme-class history (脂 vs 支) may matter more than chongniu grade alone.

The 3 exceptions — 美, 丕, 砒 — all drop the trailing ㄜ and land on bare **ㄧ**, echoing the labial-drops-ㄜ pattern already seen on 脂A三開 (鼻/琵) and the 皮/疲/被 finding on [[聲 並|聲並]]. 美 has a clean homophony explanation: its regular ㄇㄧㄜ slot already holds 4 characters (眉, 寐, 薇, 魅), the most crowded syllable on the page. 丕 and 砒 share an identical MC initial (pʰ) and would collide directly with *each other* at ㄆㄧㄜ if both took the regular form — though moving both to bare ㄧ doesn't actually separate them from one another, so this pair may simply be an unconditioned "simplicity principle" pick rather than true avoidance.

Worth flagging separately: **鄙**'s 注音 (ㄈㄧㄜ) uses the labiodental ㄈ, but its MC initial is the plain bilabial stop *p*, and every daughter reading (Mandarin bǐ, Cantonese pei2, Korean 비) points to a bilabial, not a labiodental, onset. This looks like a likely 注音 typo in the corpus (expected something like ㄅㄧㄜ or ㄆㄧㄜ) rather than a genuine outcome — similar to the 屎/靡/豕 anomalies flagged earlier in this sweep.

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
