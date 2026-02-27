---
size: 22
radical: 大
---
> [[Radicals]]

大 (char) 天 (char) 太 (char) 夫 (char) 夭 央 失 夷 夹 奄 奇 奉 奏 契 奔 套 (char) 奚 (char) 奢 奥 (char) 奨 奪 奮

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "大"
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