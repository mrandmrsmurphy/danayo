---
size: 3
radical: 青
---
> [[Radicals]]

## Characters

1. [[青 (char)]]
2. [[靖]]
3. [[静]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "青"
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