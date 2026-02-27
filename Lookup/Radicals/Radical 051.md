---
size: 5
radical: 干
---
> [[Radicals]]

## Characters

1. [[干]]
2. [[平]]
3. [[年 (char)]]
4. [[幸]]
5. [[幹]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "干"
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