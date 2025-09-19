```dataview
TABLE file.link AS "Character", radical AS "Radical"
FROM "characters"
WHERE radical = "一"
SORT file.name ASC
