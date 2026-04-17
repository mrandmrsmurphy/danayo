---
size: 5
radical: 鬼
---
## Characters
鬼, 魁, 魂 (char), 魅, 魏, 魔

## Data search
```dataview
TABLE english AS "English", radical AS "Radical", 注音 AS "Sound"
FROM "characters"
WHERE radical = "鬼"
SORT file.name ASC
```