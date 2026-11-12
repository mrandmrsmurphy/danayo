---
date-last-perfect: 2026-11-11
size: 7
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

The surrounding part has 1 stroke.

1. [SKIP-3-1-1](lookup/SKIP/SKIP-3/SKIP-3-1-1.md): 乃, 刀, 匕
2. [SKIP-3-1-2](lookup/SKIP/SKIP-3/SKIP-3-1-2.md): 刃
3. SKIP-3-1-3: none
4. [SKIP-3-1-4](lookup/SKIP/SKIP-3/SKIP-3-1-4.md): 司
5. SKIP-3-1-5: none
6. SKIP-3-1-6: none
7. [SKIP-3-1-7](lookup/SKIP/SKIP-3/SKIP-3-1-7.md): 直, 虱

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-1")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```