---
size: 269
stroke_count: 13
date-last-perfect:
---

> [[Stroke]]

```dataview
LIST
FROM "characters"
WHERE stroke_count = 13
SORT skip_number ASC
```


```dataview
TABLE 注音 AS "注音", radical AS "rad", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "13" OR stroke_count = 13
SORT skip_number ASC