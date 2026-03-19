---
size: 411
---
This is one of the [[六書]].

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - graphemic_classification == "會意"
    order:
      - file.name
      - graphemic_classification
      - english
      - stroke_count
      - date-last-perfect
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.graphemic_classification: 84
      note.english: 147

```