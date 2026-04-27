---
date-last-perfect:
size: 5
tags: [lookup]

---


## Dataview
```dataview
TABLE 注音 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "凵"
SORT stroke_count ASC