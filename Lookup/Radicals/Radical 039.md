---
size: 13
radical: 子
---
> [[Radicals]]

子 孔 (char) 孕 字 (char) 存 孚 孝 (char) 孟 季 孤 孩 学 孫

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