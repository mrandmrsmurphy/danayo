---
size: 6
radical: 夕
tags: [lookup]

---
> [[Radicals]]

## Characters
1. [[夕]]
2. [[外]]
3. [[夗]]
4. [[多 (char)]]
5. [[夜 (char)]]
6. [[夢 (char)]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "夕"
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