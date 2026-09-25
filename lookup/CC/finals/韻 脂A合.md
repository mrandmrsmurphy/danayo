---
size: 21
middle_chinese_final: iuɪ
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 脂A合** evolved into ㄨㄧ, with two homophony-driven exceptions (see below)

## CJKV Evolution
脂A合 [iuɪ] is the rounded counterpart of [[韻 脂A三開|脂A三開]], and shows the same clean chongniu-A convergence: 16 of 21 characters land on **ㄨㄧ**, matching the Vowels table's documented winner (`ui`).

**誰** is the more interesting exception. Its regular outcome would be ㄙㄨㄧ, but that slot already holds 5 characters (穂, 雖, 粋, 綏, 遂) — the most crowded syllable on this page. Rather than picking a new vowel, 誰 instead borrows the null-initial spelling convention normally reserved for yod/glide-initial characters, landing on **⼶ㄧ** alongside 唯, 遺, and 維 — a distinct kind of escape from the ones seen so far (reusing an existing group's spelling rather than inventing a new one).

**悸** dodges a smaller but still real collision: its regular ㄍㄨㄧ already holds 3 characters (季, 愧, 癸), so it drops the w-glide and lands on plain **ㄍㄧ**.

## Characters
### In Use
- ㄨㄧ: <ruby>[[推 (char)|推]]<rt>ㄑㄨㄧ</rt></ruby>, <ruby>[[涙 (char)|涙]]<rt>ㄌㄨㄧ</rt></ruby>, <ruby>[[穂 (char)|穂]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[酔 (char)|酔]]<rt>ㄐㄨㄧ</rt></ruby>, <ruby>[[雖 (char)|雖]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[塁]]<rt>ㄌㄨㄧ</rt></ruby>, <ruby>[[季]]<rt>ㄍㄨㄧ</rt></ruby>, <ruby>[[愧]]<rt>ㄍㄨㄧ</rt></ruby>, <ruby>[[癸]]<rt>ㄍㄨㄧ</rt></ruby>, <ruby>[[粋]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[綏]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[翠]]<rt>ㄑㄨㄧ</rt></ruby>, <ruby>[[蕤]]<rt>ㄋㄨㄧ</rt></ruby>, <ruby>[[遂]]<rt>ㄙㄨㄧ</rt></ruby>, <ruby>[[類]]<rt>ㄌㄨㄧ</rt></ruby>, <ruby>[[錐]]<rt>ㄐㄨㄧ</rt></ruby>
- ⼶ㄧ: <ruby>[[唯 (char)|唯]]<rt>⼶ㄧ</rt></ruby>, <ruby>[[誰 (char)|誰]]<rt>ㄙ⼶ㄧ</rt></ruby>, <ruby>[[遺 (char)|遺]]<rt>⼶ㄧ</rt></ruby>, <ruby>[[維]]<rt>⼶ㄧ</rt></ruby>
- ㄧ: <ruby>[[悸]]<rt>ㄍㄧ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iuɪ
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iuɪ"
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
