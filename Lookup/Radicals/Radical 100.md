---
size: 3
radical: 生
tags: [lookup]

---
> [[Radicals]]

## Characters

1. [[生]]
2. [[産]]
3. [[甥 (char)]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "生"
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