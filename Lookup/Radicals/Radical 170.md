---
radical: 阜
size: 35
---
> [[Radicals]]

## Characters

阜 防 阮 阿 (char) 阻 陀 附 (char) 陋 降 限 陛 院 陝 陣 陥 (char) 除 陪 (char) 陰 (char) 陳 陵 陶 陸 険 (char) 陽 (char) 隅 (char) 隊 (char) 隆 (char) 階 隙 (char) 隔 随 際 (char) 障 隠 隣 (char)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "阜"
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