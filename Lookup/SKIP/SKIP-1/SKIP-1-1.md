---
date-last-perfect: 2026-02-01
---
> [[SKIP]] 

These are pages about <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> defined by a left-right split. The left half uses only one stroke.  The third number is the stroke count of the right half.

- [[SKIP-1-1-1]]
- [[SKIP-1-1-2]]
- [[SKIP-1-1-3]]
- [[SKIP-1-1-4]]
- SKIP/1/1/5 - none
- SKIP/1/1/6 - none
- [[SKIP-1-1-7]]
- [[SKIP-1-1-8]]
- SKIP/1/1/9 - none
- SKIP/1/1/10 - none
- [[SKIP-1-1-11]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-1")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
    columnSize:
      note.danayo_id: 64
      note.english: 236
```
