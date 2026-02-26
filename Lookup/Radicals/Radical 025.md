---
date-last-perfect:
size: 4
---


## Dataview
```dataview
TABLE 韓文 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "卜"
SORT stroke_count ASC