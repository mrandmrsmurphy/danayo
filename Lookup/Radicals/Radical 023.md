---
size: 5
---

## Dataview
```dataview
TABLE 韓文 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "匸"
SORT stroke_count ASC