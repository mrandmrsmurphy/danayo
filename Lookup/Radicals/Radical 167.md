---
size: 62
radical: 金
---
> [[Radicals]]

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "金"
SORT file.name ASC
```