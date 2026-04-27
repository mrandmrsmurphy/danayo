---
stroke_count: 16
date-last-perfect:
size: 142
tags: [lookup]

---
> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "16" OR stroke_count = 16
SORT file.name ASC