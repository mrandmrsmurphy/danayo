
```dataview
TABLE file.link AS "Character", 韓文 AS "Sound", skip_number AS "SKIP"
FROM "characters"
WHERE skip_number = "1-4-4"
SORT file.name ASC