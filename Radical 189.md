---
size: 1
---

## Data check
```dataview
TABLE 韓文 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "高"
SORT stroke_count ASC