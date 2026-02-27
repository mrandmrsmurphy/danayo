---
size: 6
radical: 工
---
> [[Radicals]]

## Characters

1. 工
2. 左
3. 巧
4. 巨
5. 巫
6. 差

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "工"
    order:
      - file.name
      - danayo_id
      - english
      - 注音
      - skip_number
      - stroke_count
    columnSize:
      note.danayo_id: 64
      note.english: 236
```