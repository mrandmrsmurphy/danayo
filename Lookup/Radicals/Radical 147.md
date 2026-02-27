---
size: 8
radical: 見
---
> [[Radicals]]

## Characters

1. [[見 (char)]]
2. [[規]]
3. [[覓]]
4. [[視 (char)]]
5. [[覚]]
6. [[覧]]
7. [[親]]
8. [[観]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "見"
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