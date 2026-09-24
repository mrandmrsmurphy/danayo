---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> These are all the "misc." characters with a vertical line visibly prominent.  The second number represents the number of stroke in total.

- 1: There are no SKIP-4-1-3 characters
- [SKIP-4-2-3](lookup/SKIP/SKIP-4/SKIP-4-2-3.md): 十
- [SKIP-4-3-3](lookup/SKIP/SKIP-4/SKIP-4-3-3.md): 千, 屮, 巾, 才
- [SKIP-4-4-3](lookup/SKIP/SKIP-4/SKIP-4-4-3.md): 中, 井, 升, 屯, 手, 木, 毛, 牛
- [SKIP-4-5-3](lookup/SKIP/SKIP-4/SKIP-4-5-3.md): 乎, 未, 本, 禾, 冉, 半, 末, 朮, 申
- [SKIP-4-6-3](lookup/SKIP/SKIP-4/SKIP-4-6-3.md): 米, 朱, 虫
- [SKIP-4-7-3](lookup/SKIP/SKIP-4/SKIP-4-7-3.md): 車, 身, 甫, 求, 来, 束, 我, 串
- [SKIP-4-8-3](lookup/SKIP/SKIP-4/SKIP-4-8-3.md): 乖, 事, 東, 秉
- [SKIP-4-9-3](lookup/SKIP/SKIP-4/SKIP-4-9-3.md): 乗, 柬, 禹, 禺
- [SKIP-4-10-3](lookup/SKIP/SKIP-4/SKIP-4-10-3.md): ø
- [SKIP-4-11-3](lookup/SKIP/SKIP-4/SKIP-4-11-3.md): 粛
- [SKIP-4-13-3](lookup/SKIP/SKIP-4/SKIP-4-13-3.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-0-3")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```