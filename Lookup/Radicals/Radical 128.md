---
size: 14
radical: 耳
---
> [[Radicals]]

## Characters

耳 (char) 耴 耶 (char) 耽 (char) 聊 (char) 聒 聖 聘 (char) 聚 聞 (char) 聡 聴 (char) 職 聾

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "耳"
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