---
size: 3
middle_chinese_final: ɣiuᴇi
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 祭B三合** evolved into ㄝ

## CJKV Evolution
祭B三合 [ɣiuᴇi] has only 3 characters (彗, 穢, 衛), and all three converge on **ㄝ**, matching the Vowels table's documented winner (`e`).

Worth flagging: this is a 合 (rounded) final, yet none of its 3 characters carry a w-glide — the mirror image of the counter-example already found on [[韻 佳開|佳開]] (an 開 final that unexpectedly *did* carry one). Between the two, the "合→w-glide" rule documented in [[skill_cc_phonology]] now has confirmed exceptions in both directions; it remains a strong tendency (the large majority of 開/合 pairs still follow it cleanly) but is clearly not exceptionless.

## Characters
### In Use
- ㄝ: <ruby>[[彗]]<rt>ㄏㄝ</rt></ruby>, <ruby>[[穢]]<rt>ㄝ</rt></ruby>, <ruby>[[衛]]<rt>ㄝ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiuᴇi
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiuᴇi"
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
