---
size: 24
middle_chinese_final: iuᴇn
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 仙A三合** splits into ㄝㄋ vs ⼔ㄋ, with several smaller intra-class exceptions (see below)

## CJKV Evolution
仙A三合 [iuᴇn] splits fairly evenly: 9 characters land on **ㄝㄋ** and 8 on **⼔ㄋ**, together matching the Vowels table's documented dual winner (`yen/wen`).

The final's yod-initial (j) characters themselves split further: 鳶, 縁, and 鉛 land on **⼶ㄋ**, while 沿 — sharing that same j initial — lands on **⼔ㄇ** instead, alongside 船. This is yet another instance of the "same initial, arbitrary outcome" pattern confirmed repeatedly across this sweep.

The most striking pair on this page is **串** and **川**: they share the *identical* MC initial (t͡ɕʰ) and land on near-identical spellings, **⺢ㄇ** and **⺢ㄋ** respectively — differing by only a single coda phoneme. 串's daughter readings are mostly close to 川's (chuàn/cyun3 vs chuān/cyun1), but its Korean reading (곶, a native word for "cape/promontory," not a regular Sino-Korean form) is a genuine outlier — plausibly the reason these two otherwise-matching characters diverged.

## Characters
### In Use
- ㄝㄋ: <ruby>[[磚]]<rt>ㄐㄝㄋ</rt></ruby>, <ruby>[[舛]]<rt>ㄑㄝㄋ</rt></ruby>, <ruby>[[宣]]<rt>ㄙㄝㄋ</rt></ruby>, <ruby>[[恋 (char)|恋]]<rt>ㄌㄝㄋ</rt></ruby>, <ruby>[[釧]]<rt>ㄑㄝㄋ</rt></ruby>, <ruby>[[穿 (char)|穿]]<rt>ㄑㄝㄋ</rt></ruby>, <ruby>[[喘]]<rt>ㄑㄝㄋ</rt></ruby>, <ruby>[[軟]]<rt>ㄋㄝㄋ</rt></ruby>, <ruby>[[詮]]<rt>ㄑㄝㄋ</rt></ruby>
- ⼔ㄋ: <ruby>[[絹 (char)|絹]]<rt>ㄍ⼔ㄋ</rt></ruby>, <ruby>[[全 (char)|全]]<rt>ㄐ⼔ㄋ</rt></ruby>, <ruby>[[圓 (char)|圓]]<rt>⼔ㄋ</rt></ruby>, <ruby>[[泉]]<rt>ㄐ⼔ㄋ</rt></ruby>, <ruby>[[萱]]<rt>ㄏ⼔ㄋ</rt></ruby>, <ruby>[[専]]<rt>ㄐ⼔ㄋ</rt></ruby>, <ruby>[[選]]<rt>ㄙ⼔ㄋ</rt></ruby>, <ruby>[[旋]]<rt>ㄙ⼔ㄋ</rt></ruby>
- ⼶ㄋ: <ruby>[[鳶 (char)|鳶]]<rt>⼶ㄋ</rt></ruby>, <ruby>[[縁]]<rt>⼶ㄋ</rt></ruby>, <ruby>[[鉛 (char)|鉛]]<rt>⼶ㄋ</rt></ruby>
- ⼔ㄇ: <ruby>[[沿 (char)|沿]]<rt>⼔ㄇ</rt></ruby>, <ruby>[[船]]<rt>ㄙ⼔ㄇ</rt></ruby>
- ⺢ㄇ: <ruby>[[串 (char)|串]]<rt>ㄐ⺢ㄇ</rt></ruby>
- ⺢ㄋ: <ruby>[[川 (char)|川]]<rt>ㄑ⺢ㄋ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iuᴇn
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iuᴇn"
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
