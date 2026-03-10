## Base check
```base
filters:
  and:
    - graphemic_classification == "象形"
views:
  - type: table
    name: Table
    filters:
      and:
        - graphemic_classification == "象形"
    order:
      - file.name
      - 注音
      - english
      - danayo_id
      - hanmun_edu_level
      - date-last-perfect
      - grade_level
    sort:
      - property: formula.spot
        direction: DESC
      - property: joyo_level
        direction: ASC
      - property: hanmun_edu_level
        direction: DESC
      - property: danayo_id
        direction: ASC
    columnSize:
      file.name: 40
      note.english: 98
      note.danayo_id: 64
      note.hanmun_edu_level: 57

```