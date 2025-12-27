> [[Radicals]]

## Data check
```dataview
TABLE file.link AS "Character", radical AS "Radical", 韓文 AS "Sound"
FROM "characters"
WHERE radical = "乙"
SORT file.name ASC