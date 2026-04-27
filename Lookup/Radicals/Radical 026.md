---
date-last-perfect:
size: 8
tags: [lookup]

---

## Dataview
```dataview
TABLE 注音 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "卩"
SORT stroke_count ASC