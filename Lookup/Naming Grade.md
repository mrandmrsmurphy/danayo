
## Data check
```dataview
TABLE danayo_id AS "ID", grade_level AS "gr", 韓文 AS "Sound"
FROM "characters"
WHERE grade_level = "名"
SORT file.name ASC