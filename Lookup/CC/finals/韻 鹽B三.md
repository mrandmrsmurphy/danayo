---
size: 13
middle_chinese_final: ɣiᴇm
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 鹽B三** evolved into ㄝㄇ, with a crowding escape and a labial y-glide pair (see below)

## CJKV Evolution
鹽B三 [ɣiᴇm] converges mostly: 10 of 13 characters land on **ㄝㄇ**, matching the Vowels table's documented winner (`em`).

**砭** and **窆** are true homophones (both p-initial, Mandarin *biān*/*biǎn*, Korean 폄) and land together on **⼶ㄇ** — labials combine freely with the y-glide here, consistent with the phonotactic rule banning only the *w*-glide after labials.

**芡** shares its initial-class (g/k) with a crowded 4-member slot in the main group (鉗, 倹, 検, 瞼) and dodges via vowel-shift, landing alone on **⼘ㄇ**.

## Characters
### In Use
- ㄝㄇ: <ruby>[[粘 (char)|粘]]<rt>ㄋㄝㄇ</rt></ruby>, <ruby>[[諂 (char)|諂]]<rt>ㄑㄝㄇ</rt></ruby>, <ruby>[[鉗 (char)|鉗]]<rt>ㄍㄝㄇ</rt></ruby>, <ruby>[[険 (char)|険]]<rt>ㄏㄝㄇ</rt></ruby>, <ruby>[[験 (char)|験]]<rt>ㄝㄇ</rt></ruby>, <ruby>[[俺]]<rt>ㄝㄇ</rt></ruby>, <ruby>[[倹]]<rt>ㄍㄝㄇ</rt></ruby>, <ruby>[[検]]<rt>ㄍㄝㄇ</rt></ruby>, <ruby>[[炎]]<rt>ㄝㄇ</rt></ruby>, <ruby>[[瞼]]<rt>ㄍㄝㄇ</rt></ruby>
- ⼶ㄇ: <ruby>[[砭]]<rt>ㄆ⼶ㄇ</rt></ruby>, <ruby>[[窆]]<rt>ㄅ⼶ㄇ</rt></ruby>
- ⼘ㄇ: <ruby>[[芡]]<rt>ㄍ⼘ㄇ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇm
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇm"
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
