---
size: 22
middle_chinese_final: iᴇm
---

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iᴇm
    filters:
      and:
        - middle_chinese_final == "iᴇm"
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - middle_chinese_initial
      - middle_chinese_final
      - 韓文
      - 羅馬字
    sort:
      - property: 羅馬字
        direction: ASC
      - property: middle_chinese_initial
        direction: ASC
      - property: characters
        direction: DESC
      - property: grade_level
        direction: ASC
    columns:
      - file
      - file.path
      - file.links.length
    columnSize:
      note.mandarin: 59
      note.cantonese: 71
      note.korean: 43
      note.middle_chinese_initial: 97

```