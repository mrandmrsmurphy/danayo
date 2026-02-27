---
size: 16
radical: 隹
---
> [[Radicals]]

## Characters

隹 隼 (char) 雀 雁 (char) 雄 (char) 雅 集 雇 雉 (char) 雌 雑 (char) 雍 雖 (char) 雛 離 難

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "隹"
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