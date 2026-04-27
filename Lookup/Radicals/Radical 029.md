---
size: 15
date-last-perfect:
radical: 又
tags: [lookup]

---


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "又"
    order:
      - file.name
      - danayo_id
      - english
      - 注音
      - skip_number
      - stroke_count
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.danayo_id: 75
      note.skip_number: 72
```