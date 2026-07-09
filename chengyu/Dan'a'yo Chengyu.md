---
tags:
  - chengyu
---

- <ruby>[合漢再決](chengyu/合漢再決.md)<rt>ㄍㄛㄆㄏㄚㄋㄐㄚㄧㄎ⼔ㄊ</rt></ruby> - The Renew Sinosphere Chooses Unity
- <ruby>[一字一音](chengyu/一字一音.md)<rt>ㄧㄊㄐㄧ·ㄧㄊ·ㄨㄇ</rt></ruby> - one character, one sound
- <ruby>[覧昭和決](chengyu/覧昭和決.md)<rt>ㄌㄚㄇㄐㄛㄨㄏ⺢ㄎ⼔ㄊ</rt></ruby> - Shōwa decides the look
- <ruby>[朝鮮正音](chengyu/朝鮮正音.md)<rt>ㄐㄚㄨㄙ⼶ㄋㄐㄧㄫ·ㄨㄇ</rt></ruby> - Joseon standardizes the sound
- <ruby>[保頭断尾](chengyu/保頭断尾.md)<rt>ㄅㄚㄨㄊㄛㄨㄉ⺢ㄋㄇㄨㄧ</rt></ruby> - guard the core, prune the periphery
- <ruby>[文言継承](chengyu/文言継承.md)<rt>ㄇㄨㄋ·ㄝㄋㄍㄝㄧㄙㄨㄫ</rt></ruby> - continuity with the classical written standard
- <ruby>[現代適応](chengyu/現代適応.md)<rt>ㄏ⼶ㄋㄉㄚㄧㄙㄝㄎㄧㄫ</rt></ruby> - adaptation to modern speech
- <ruby>[日用必備](chengyu/日用必備.md)<rt>ㄋㄧㄊ⼄ㄫㄅㄧㄊㄅㄧㄜ</rt></ruby> - daily use, always needed

## Base check
```base
filters:
  and:
    - file.folder == "chengyu"
    - origin == "単亜語"
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "chengyu"
        - origin == "単亜語"
    order:
      - file.name
      - date-last-perfect
      - 注音
      - english
    sort:
      - property: date-last-perfect
        direction: ASC
      - property: size
        direction: ASC
    columnSize:
      note.date-last-perfect: 131
      note.注音: 81

```