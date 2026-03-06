---
date-last-perfect: 2026-02-13
---
> [[SKIP]] : 4
> These are all the "misc." characters with a vertical line visibly prominent.  The second number represents the number of stroke in total.

- 1: There are no SKIP-4-1-3 characters
- [[SKIP-4-2-3|2]]: 十
- [[SKIP-4-3-3|3]]: 巾, 才, <ruby>千<rt>ㄑㄝㄋ</rt></ruby>, 屮, 廾
- [[SKIP-4-4-3|4]]: 井, 牛, 手, 升, 中, 屯, 毛, 木
- [[SKIP-4-5-3|5]]: [[禾]]	[[乎 (char)]] [[申]]	[[半]]	[[本]]	[[末]]	[[未 (char)]]	[[朮]]	
- [[SKIP-4-6-3|6]]: 朱, 虫, 米, 朿, 耒, 聿
- [[SKIP-4-7-3|7]]: [[我]]	[[求]]	[[串]]	[[車 (char)]]	[[身]]	[[束 (char)]] [[釆]]	[[甫]]	[[来 (char)]]	~~亊~~	
- [[SKIP-4-8-3|8]]: 事, 東, 乖, 秉	
- [[lookup/SKIP/SKIP-4/SKIP-4-9-3|9]]: 乗, 柬, 禹, 禺
- [[SKIP-4-10-3|10]]: 乘 (just a variant of 乗)
- [[lookup/SKIP/SKIP-4/SKIP-4-11-3|11]]: 粛
- [[SKIP-4-13-3|13]]: 肅 (just a variant of 粛)

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