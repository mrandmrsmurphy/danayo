---
stroke_count: 22
date-last-perfect:
size: 11
tags: [lookup]

---

> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "22" OR stroke_count = 22
SORT skip_number ASC