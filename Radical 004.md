> [[Radicals]]

## Data check
```dataview
TABLE file.link AS "Character", radical AS "Radical", 韓文 AS "Sound"
FROM "characters"
WHERE radical = "丿" OR radical = "乀" OR radical = "乁"
SORT file.name ASC