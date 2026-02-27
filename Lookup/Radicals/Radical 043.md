---
size: 2
radical: 尢
---
> [[Radicals]]

## Characters
1. [[尤]]
2. [[尭]]
3. [[就 (char)]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "尢"
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