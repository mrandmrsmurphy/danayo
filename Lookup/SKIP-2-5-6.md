```dataview
TABLE file.link AS "Character", skip_number AS "SKIP"
FROM "characters"
WHERE skip_number = "2-5-6"
SORT file.name ASC
