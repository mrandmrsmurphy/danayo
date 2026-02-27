---
size: 21
radical: 車
---
> [[Radicals]]

## Characters

```dataview
LIST
FROM "characters"
WHERE radical = "車"
```

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "車"
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