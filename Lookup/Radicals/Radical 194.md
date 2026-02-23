---
size: 5
---

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "鬼"
SORT file.name ASC
```