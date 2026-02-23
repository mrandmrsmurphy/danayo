---
size: 102
---
> [[Radicals]]

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "心"
SORT file.name ASC
```