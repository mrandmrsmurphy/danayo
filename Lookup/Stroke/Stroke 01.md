---
date-last-perfect: 2026-02-22
stroke_count: 1
size: 2
tags: [lookup]

---
> [Stroke](lookup/Stroke/Stroke.md)

## Characters
### In Use
1. <ruby>[[一 (char)|一]]<rt>ㄧㄊ</rt></ruby> - one
2. <ruby>[[乙 (char)|乙]]<rt>ㄛㄊ</rt></ruby> - second

### Aliases
- 丨
- 丶
- 丿
- 乀
- 乁
- 乚
- 乛
- 亅

### Data check
```dataview
TABLE stroke_count AS "Stroke", skip_number AS "SKIP", english AS "en", 注音 as "注音"
FROM "characters"
WHERE stroke_count = "1" OR stroke_count = 1
SORT file.name ASC