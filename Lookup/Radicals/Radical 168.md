---
size: 1
radical: 長
date-last-perfect: 2026-02-27
tags: [lookup]

---
> [[Radicals]]

## Characters

1. <ruby>[[長 (char)|長]]<rt>ㄐㄚㄫ</rt></ruby> - long

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "長"
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