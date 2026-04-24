---
tags:
  - chengyu
---

- <ruby>[合漢再決](chengyu/合漢再決.md)<rt>ㄍㄛㄆㄏㄚㄋㄐㄚ˙ㄎ⼔ㄊ</rt></ruby></ruby> - The Renew Sinosphere Chooses Unity
- <ruby>[一字一音](chengyu/一字一音.md)<rt>ㄧㄊㄐㄧ·ㄧㄊ·ㄨㄇ</rt></ruby> - one character, one sound
- <ruby>[覧昭和決](chengyu/覧昭和決.md)<rt>ㄌㄚㄇㄐㄛˇㄏㆼㄎ⼔ㄊ</rt></ruby> - Shōwa decides the look
- <ruby>[朝鮮正音](chengyu/朝鮮正音.md)<rt>ㄐㄚˇㄙ⼶ㄋㄐㄧㄫ·ㄨㄇ</rt></ruby> - Joseon standardizes the sound
- [[形助顯理]]

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