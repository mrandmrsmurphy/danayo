---
stroke_count: 1
date-last-perfect: 2026-02-06
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 01](lookup/Stroke/Stroke%2001.md)
These are all the <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> of 一 stroke, whether that be a top line, bottom line, middle line, or otherwise.

- [SKIP-4-1-1](lookup/SKIP/SKIP-4/SKIP-4-1-1.md) : 乙
- SKIP-4-1-2 does not exist
- SKIP-4-1-3 does not exist
- [SKIP-4-1-4](lookup/SKIP/SKIP-4/SKIP-4-1-4.md) : 一.  


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-1")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```