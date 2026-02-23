---
size: 4
---
> [[Radicals]]


## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "黑" OR radical = "黒"
SORT file.name ASC