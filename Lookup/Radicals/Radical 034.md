---
size: 2
radical: 夂
---
> [[Radicals]]

1. <ruby>[[変 (char)|変]]<rt>ㄅ˙ㄝㄋ</rt></ruby> - change, alter
2. <ruby>[[夌]]<rt>ㄌ˙ㄨㄥ</rt></ruby> - dawdle

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "夂"
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