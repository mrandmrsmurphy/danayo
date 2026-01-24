
## Data check
```dataview
TABLE file.link AS "Character", grade_level AS "gr", 韓文 AS "Sound"
FROM "characters"
WHERE grade_level = "先進"
SORT file.name ASC