---
date-last-perfect: 2026-02-13
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> These are all the "misc." characters with a vertical line visibly prominent.  The second number represents the number of stroke in total.

- 1: There are no SKIP-4-1-3 characters
- [SKIP-4-2-3](lookup/SKIP/SKIP-4/SKIP-4-2-3.md): 十
- [SKIP-4-3-3](lookup/SKIP/SKIP-4/SKIP-4-3-3.md): 巾, 才, <ruby>千<rt>ㄑㄝㄋ</rt></ruby>, 屮, 廾
- [SKIP-4-4-3](lookup/SKIP/SKIP-4/SKIP-4-4-3.md): 井, 牛, 手, 升, 中, 屯, 毛, 木
- [SKIP-4-5-3](lookup/SKIP/SKIP-4/SKIP-4-5-3.md): 禾, 乎, 申, 半, 本, 末, ,朮
- [SKIP-4-6-3](lookup/SKIP/SKIP-4/SKIP-4-6-3.md): 朱, 虫, 米, 朿, 耒, 聿
- [SKIP-4-7-3](lookup/SKIP/SKIP-4/SKIP-4-7-3.md): 我, 求, 串, 車, 身, 束, 釆, 甫, 来
- [SKIP-4-8-3](lookup/SKIP/SKIP-4/SKIP-4-8-3.md): 事, 東, 乖, 秉	
- [SKIP-4-9-3](lookup/SKIP/SKIP-4/SKIP-4-9-3.md): 乗, 柬, 禹, 禺
- [SKIP-4-10-3](lookup/SKIP/SKIP-4/SKIP-4-10-3.md): ø
- [SKIP-4-11-3](lookup/SKIP/SKIP-4/SKIP-4-11-3.md)]: 粛
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