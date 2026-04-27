---
size: 2
radical: 屮
date-last-perfect: 2026-03-04
tags: [lookup]

---
> [[Radicals]]
> This is the **shoot** radical

## Characters
1. <ruby>[屮](characters/屮.md)<rt>ㄊㄧㄊ</rt></ruby> - new plant
2. <ruby>[屯](characters/屯%20(char).md)<rt>ㄉㄨㄋ</rt></ruby> - hamlet

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "屮"
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