---
stroke_count: 28
date-last-perfect: 2026-02-23
size: 1
---
> [[Stroke]]

- <ruby>[[鸚]]<rt>ㄚㄫ</rt></ruby> - parrot

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "28" OR stroke_count = 28
SORT file.name ASC