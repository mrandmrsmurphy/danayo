---
size: 2
---
> [[Radicals]]


## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "鹵"
SORT file.name ASC
```