---
size: 5
---
> [[Radicals]]

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "鹿"
SORT file.name ASC
```