---
stroke_count: 6
date-last-perfect:
size: 145
---
> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "6" OR stroke_count = 6
SORT skip_number ASC