---
size: 2
middle_chinese_final: ɣiᴇp
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 葉B三** has two ʈ-initial characters, each landing on a different group

## CJKV Evolution
葉B三 [ɣiᴇp] has only two characters, 耴 and 輒 — both ʈ-initial, both Cantonese *zip3*, both Korean 첩 — yet they land on two different groups: 耴 on **ㄨㄆ**, 輒 on **ㄛㄆ** (the Vowels table's documented value for this final is `up/op`, row 156 of 文法 - 99韻図, covering both, and 輒's ㄛ is also the main outcome on the related [[韻 葉三|葉三]]). They are a same-initial, near-homophone split: they share Cantonese and Korean, but Mandarin differs (*yì* against *zhé*) and so does Vietnamese (*ngất* against *triếp*).

## Characters
### In Use
- ㄨㄆ: <ruby>[[耴]]<rt>ㄐㄨㄆ</rt></ruby>
- ㄛㄆ: <ruby>[[輒]]<rt>ㄐㄛㄆ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇp
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇp"
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
