---
size: 13
radical: 子
---
> [[Radicals]]

## Characters
1. 子
2. 孔 (char)
3. 孕
4. <ruby>[字](/characters/字%20(char).md)<rt>ㄐㄧ</rt></ruby> - glyph
5. 存
6. 孚
7. 孝 (char)
8. 孟
9. 季
10. 孤
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
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.danayo_id: 64
      note.english: 236

```