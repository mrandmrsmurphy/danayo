---
size: 22
radical: 尸
---
> [[Radicals]]

## Characters
### +1
1. [[尺 (char)]]
2. 尻 (char) 尼 尽 尾 (char) 尿 (char) 局 (char) 屁 (char) 居 屈 (char) 届 (char) 屋 (char) 屍 屎 (char) 屏 屑 (char) 展 属 屠 屢 (char) 層 (char) 履 (char)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "尸"
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