---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [[SKIP]] : 4

This is the home page for SKIP characters of type 4-x-4.  These are <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> with a box-like or no pattern.


1. [SKIP-4-1-4](lookup/SKIP/SKIP-4/SKIP-4-1-4.md) - 一
2. [SKIP-4-2-4](lookup/SKIP/SKIP-4/SKIP-4-2-4.md) - 九, 人, 入, 卜, 力, 乂
3. [SKIP-4-3-4](lookup/SKIP/SKIP-4/SKIP-4-3-4.md) - 丈, 与, 之, 大, 女, 丸
4. [SKIP-4-4-4](lookup/SKIP/SKIP-4/SKIP-4-4-4.md) - 夫, 少, 火, 片, 犬, 内, 夭, 戈
5. [SKIP-4-5-4](lookup/SKIP/SKIP-4/SKIP-4-5-4.md) - 史, 央, 失, 弗, 戊, 犮
6. [SKIP-4-6-4](lookup/SKIP/SKIP-4/SKIP-4-6-4.md) - 成, 吏, 夷, 戌, 戍, 曳, 舟
7. [SKIP-4-7-4](lookup/SKIP/SKIP-4/SKIP-4-7-4.md) - 夹, 寿, 良
8. [SKIP-4-8-4](lookup/SKIP/SKIP-4/SKIP-4-8-4.md) - 兎
9. [[SKIP-4-9-4]] - 咸, 威, 為
10. no
11. [SKIP-4-11-4](lookup/SKIP/SKIP-4/SKIP-4-11-4.md) - 戚, 爽
12. [[SKIP-4-12-4]] - 幾
13. no
14. no
15. [[SKIP-4-15-4]] - 畿

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-0-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```