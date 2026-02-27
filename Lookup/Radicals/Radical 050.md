---
radical: 巾
size: 24
---
> [[Radicals]]

## Characters

```dataview
LIST
FROM "characters"
WHERE radical = "巾"
```

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "巾"
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