---
size: 42
tags: [lookup]

---
> [[Radicals]]

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "竹"
SORT file.name ASC
```