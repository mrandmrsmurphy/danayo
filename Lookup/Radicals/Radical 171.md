---
size: 1
radical: 隶
date-last-perfect: 2026-03-03
---
> [[Radicals]]

## Characters

1. <ruby>[[隷]]<rt>ㄌㄝㄧ</rt></ruby> - slave

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "隶"
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