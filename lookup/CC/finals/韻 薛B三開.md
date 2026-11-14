---
size: 8
middle_chinese_final: ɣiᴇt
date-last-perfect: 2026-11-14
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 薛B三開** evolved into ㄝㄊ, with one exception (see below)

## CJKV Evolution
薛B三開 [ɣiᴇt] is nearly uniform: 7 of 8 characters land on **ㄝㄊ**, matching the Vowels table's documented winner (`et`, row 083 of 文法 - 99韻図).

**屮** is the lone exception, landing on **ㄧㄊ**. Its daughter readings (Mandarin *chè*, Cantonese *cit3*, Korean 철, Vietnamese *triệt*) are identical to those of 撤 and 澈, which stay on ㄝㄊ as ㄉㄝㄊ and ㄐㄝㄊ; the three also differ in their initial letter (ㄊ for 屮, whose MC initial is ʈʰ, against ㄉ for 撤 and ㄐ for 澈, whose MC initial is ɖ in both cases). So the vowel difference sits alongside an initial-letter difference that the character pages own.

## Characters
### In Use
- ㄝㄊ: <ruby>[[別 (char)|別]]<rt>ㄅㄝㄊ</rt></ruby>, <ruby>[[掲 (char)|掲]]<rt>ㄎㄝㄊ</rt></ruby>, <ruby>[[撤 (char)|撤]]<rt>ㄉㄝㄊ</rt></ruby>, <ruby>[[偈]]<rt>ㄍㄝㄊ</rt></ruby>, <ruby>[[傑]]<rt>ㄍㄝㄊ</rt></ruby>, <ruby>[[哲]]<rt>ㄐㄝㄊ</rt></ruby>, <ruby>[[澈]]<rt>ㄐㄝㄊ</rt></ruby>
- ㄧㄊ: <ruby>[[屮]]<rt>ㄊㄧㄊ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇt
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇt"
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - middle_chinese_initial
      - middle_chinese_final
      - 注音
      - tags
    sort:
      - property: 注音
        direction: ASC
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
      note.middle_chinese_final: 86

```
