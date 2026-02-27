---
size: 1
radical: 長
---
> [[Radicals]]

## Characters

1. [[長 (char)|長]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "長"
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