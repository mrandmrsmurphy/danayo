---
size: 9
radical: 羊
---
> [[Radicals]]

## Characters

1. [[羊]]
2. [[羌]]
3. [[美 (char)]]
4. [[羚]]
5. [[羞]]
6. [[群]]
7. [[羨]]
8. [[義]]
9. [[羸]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "羊"
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