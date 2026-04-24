---
size: 13
radical: 子
---
> [Radicals](Radicals.md)

## Characters
1. <ruby>[子](/characters/子.md)<rt>ㄐㄧ</rt></ruby> - child
2. <ruby>[孔](/characters/孔%20(char).md)<rt>ㄎㄛㄫ</rt></ruby> - cavity
3. <ruby>[孕](/characters/孕.md)<rt>ㄧㄫ</rt></ruby>
4. <ruby>[字](/characters/字%20(char).md)<rt>ㄐㄧ</rt></ruby> - glyph
5. <ruby>[存](/characters/存.md)<rt>ㄐㄛㄋ</rt></ruby>
6. <ruby>[孚](/characters/孚.md)<rt>ㄆㄨ</rt></ruby>
7. <ruby>[孝](/characters/孝%20(char).md)<rt>ㄏ⼘ㄨ</rt></ruby>
8. <ruby>[孟](/characters/孟.md)<rt>ㄇㄚㄫ</rt></ruby>
9. 季
10. <ruby>[孤](/characters/孤.md)<rt>ㄍㄛ</rt></ruby> - lone
11. 孩
12. 学
13. 孫

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "子"
    order:
      - file.name
      - danayo_id
      - english
      - 注音
      - skip_number
      - stroke_count
      - date-last-perfect
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.danayo_id: 64
      note.english: 132
      note.skip_number: 73
      note.stroke_count: 71

```