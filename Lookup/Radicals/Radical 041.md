---
size: 13
radical: 寸
---
> [[Radicals]]

寸 (char) 寺 対 寿 封 専 尃 射 将 (char) 尉 (char) 尊 尋 (char) 導

寽 red
## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "寸"
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