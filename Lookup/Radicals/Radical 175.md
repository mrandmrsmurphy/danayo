---
radical: 非
size: 3
---


## Dataview
```dataview
TABLE 韓文 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "非"
SORT stroke_count ASC