---
size: 9
radical: 冫
date-last-perfect:
tags: [lookup]

---


## Dataview
```dataview
TABLE 注音 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "冫"
SORT stroke_count ASC