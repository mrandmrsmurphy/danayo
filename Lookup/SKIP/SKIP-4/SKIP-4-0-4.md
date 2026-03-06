---
date-last-perfect: 2026-02-01
---
> [[SKIP]] : 4

This is the home page for SKIP characters of type 4-x-4.  These are <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> with a box-like or no pattern.


1. [SKIP-4-1-4](lookup/SKIP/SKIP-4/SKIP-4-1-4.md) - 一
2. [SKIP-4-2-4](lookup/SKIP/SKIP-4/SKIP-4-2-4.md) - 九, 人, 入, 卜, 力, 乂, 勹, 厶
3. [SKIP-4-3-4](lookup/SKIP/SKIP-4/SKIP-4-3-4.md) - 丸, 女, 丈, 大, 之, 与 , 宀	幺	广	弋	
4. [SKIP-4-4-4](lookup/SKIP/SKIP-4/SKIP-4-4-4.md) - 火, 犬, 少, 内, 夫, 片, 匁	卅	夬	夭	戈	爿	
5. [SKIP-4-5-4](lookup/SKIP/SKIP-4/SKIP-4-5-4.md) - 央 史	失	弗	戊	丼	冉	戉	
6. [SKIP-4-6-4](lookup/SKIP/SKIP-4/SKIP-4-6-4.md) - 夷	曳 舟	成	吏	戍	戌	
7. [SKIP-4-7-4](lookup/SKIP/SKIP-4/SKIP-4-7-4.md) - 寿	良	夾	曵
8. [SKIP-4-8-4](SKIP-4-8-4) - 兎	
9. [[SKIP-4-9-4 - 威	為	咸	臾	
10. no
11. [[lookup/SKIP/SKIP-4/SKIP-4-11-4]] - 戚	爽
12. [[SKIP-4-12-4]] -  幾
13. no
14. no
15. [[SKIP-4-15-4]] - 畿, 臧

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