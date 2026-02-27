---
size: 170
radical: 水
---
> [[Radicals]]

## Characters
```dataview
LIST
FROM "characters"
WHERE radical = "水"
```

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "水"
SORT file.name ASC
```