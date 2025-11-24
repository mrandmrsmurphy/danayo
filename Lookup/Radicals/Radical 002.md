## Data check
```dataview
TABLE file.link AS "Character", radical AS "Radical", 韓文 AS "Sound"
FROM "characters"
WHERE radical = "丨"
SORT file.name ASC