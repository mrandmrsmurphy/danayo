

## Data check
```dataview
TABLE stroke_count AS "S", radical AS "Radical", 韓文 AS "Sound"
FROM "characters"
WHERE radical = "糸"
SORT stroke_count ASC