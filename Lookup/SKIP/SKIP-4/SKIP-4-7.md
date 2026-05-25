---
date-last-perfect: 2026-05-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 07](lookup/Stroke/Stroke%2007.md)

- [SKIP-4-7-1](lookup/SKIP/SKIP-4/SKIP-4-7-1.md): 里, 酉, 豕, 更, 巫, 亜
- [SKIP-4-7-2](lookup/SKIP/SKIP-4/SKIP-4-7-2.md): 坐
- [SKIP-4-7-3](lookup/SKIP/SKIP-4/SKIP-4-7-3.md): 車, 身, 甫, 求, 来, 束...
- [SKIP-4-7-4](lookup/SKIP/SKIP-4/SKIP-4-7-4.md): 夹, 寿, 良

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-7")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
