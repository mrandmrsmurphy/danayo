---
size: 20
radical: 門
tags: [lookup]

---
> [[Radicals]]

## Characters

䦨 門 閉 閃 開 閏 (char) 閑 間 閔 関 (char) 閙 閣 閥 閨 閲 闊 (char) 閻 (char) 闖 闕 闘

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "門"
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
      note.注音: 65

```