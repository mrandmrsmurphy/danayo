

## Base check
```base
filters:
  and:
    - file.folder == "characters"
    - grade_level == "1"
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - grade_level == 1
    order:
      - file.name
      - 注音
      - english
      - danayo_id
      - date-last-perfect
    sort:
      - property: danayo_id
        direction: ASC
    columnSize:
      note.danayo_id: 64
      note.english: 236
  - type: list
    name: View
    order:
      - file.name
      - date-last-perfect
      - english
      - 注音
  - type: cards
    name: View 2

```