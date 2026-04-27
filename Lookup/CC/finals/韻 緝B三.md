---
size: 15
middle_chinese_final: ɣiɪp
tags: [lookup]

---


## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iɪp
    filters:
      and:
        - middle_chinese_final == "ɣiɪp"
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - 羅馬字
      - middle_chinese_initial
      - middle_chinese_final
    sort:
      - property: middle_chinese_initial
        direction: ASC
      - property: 羅馬字
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
      note.korean: 51
      note.middle_chinese_initial: 97

```