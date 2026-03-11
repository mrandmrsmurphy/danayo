---
stroke_count: 11
date-last-perfect:
size: 328
---
> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "11" OR stroke_count = 11
SORT skip_number ASC