---
date-last-perfect: 2026-11-12
size: 30
stroke_count: 3
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 03](lookup/Stroke/Stroke%2003.md)

These are all the <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> of 3 (three) strokes, whether that be a top line, bottom line, middle line, or otherwise.

1. [SKIP-4-3-1](lookup/SKIP/SKIP-4/SKIP-4-3-1.md): 下, 久, 于, 叉, 及, 口, 已, 弓, 兀, 夕, 子, 工, 己, 巳, 干
2. [SKIP-4-3-2](lookup/SKIP/SKIP-4/SKIP-4-3-2.md): 上, 也, 土, 士, 亡
3. [SKIP-4-3-3](lookup/SKIP/SKIP-4/SKIP-4-3-3.md): 千, 屮, 巾, 才
4. [SKIP-4-3-4](lookup/SKIP/SKIP-4/SKIP-4-3-4.md): 丈, 与, 之, 大, 女, 丸

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-3")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```
