---
date-last-perfect: 2026-05-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

Surrounding component has 8 strokes. Dominant component: 門.

1. ø
2. [SKIP-3-8-2](lookup/SKIP/SKIP-3/SKIP-3-8-2.md): 勉, 閃
3. [SKIP-3-8-3](lookup/SKIP/SKIP-3/SKIP-3-8-3.md): 問, 彪, 閉
4. [SKIP-3-8-4](lookup/SKIP/SKIP-3/SKIP-3-8-4.md): 悶, 開, 閏, 閑, 間...
5. ø
6. [SKIP-3-8-6](lookup/SKIP/SKIP-3/SKIP-3-8-6.md): 聞, 関, 閣, 閥, 閨
7. [SKIP-3-8-7](lookup/SKIP/SKIP-3/SKIP-3-8-7.md): 閲, 魅
8. [SKIP-3-8-8](lookup/SKIP/SKIP-3/SKIP-3-8-8.md): 䦨
9. [SKIP-3-8-9](lookup/SKIP/SKIP-3/SKIP-3-8-9.md): 闊
10. [SKIP-3-8-10](lookup/SKIP/SKIP-3/SKIP-3-8-10.md): 闕, 闖, 闘

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-8")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
