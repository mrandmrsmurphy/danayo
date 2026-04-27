---
size: 7
radical: 小
tags: [lookup]

---
> [[Radicals]]

## Characters
小 (char) 少 (char) 尖 尗 尚 (char) 当 (char) 爾 (char)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "小"
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