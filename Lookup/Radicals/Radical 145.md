---
size: 83
radical: 糸
---
> [Radicals](Radicals.md)

## Data check
```dataview
TABLE stroke_count AS "S", english AS "EN", 注音 AS "Sound"
FROM "characters"
WHERE radical = "糸"
SORT stroke_count ASC