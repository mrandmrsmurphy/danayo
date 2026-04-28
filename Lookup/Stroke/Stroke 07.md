---
stroke_count: 7
date-last-perfect:
size: 187
tags:
  - lookup
---

> [[Stroke]]

* [[局]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "7" OR stroke_count = 7
SORT file.name ASC