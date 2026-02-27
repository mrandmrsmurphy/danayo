---
size: 4
radical: 幺
---
> [[Radicals]]

## Characters

1. [[幻]]
2. [[幼]]
3. [[幽 (char)]]
4. [[幾 (char)]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "幺"
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