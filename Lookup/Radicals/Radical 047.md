---
size: 6
radical: 巛
tags: [lookup]

---
> [[Radicals]]

## Characters

川 (char) 州 (char) 巠 巡 巣 𡿺

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "巛"
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