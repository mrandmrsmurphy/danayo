---
size: 61
---
> [[Radicals]]

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "女"
SORT file.name ASC
```