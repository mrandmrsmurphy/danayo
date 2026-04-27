---
stroke_count: 4
date-last-perfect:
size: 88
tags: [lookup]

---
> [[Stroke]]

### Data check
```dataview
TABLE stroke_count AS "Stroke", skip_number AS "SKIP", english AS "en", 注音 as "注音"
FROM "characters"
WHERE stroke_count = "4" OR stroke_count = 4
SORT file.name ASC