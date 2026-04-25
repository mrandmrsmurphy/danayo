---
size: 14
---
> [[Radicals]]

## Data check
```dataview
TABLE file.link AS "Character", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "儿"
SORT file.name ASC