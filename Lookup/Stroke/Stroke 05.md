> [[Stroke]]

See also 
- SKIP 1: [[SKIP-1-1-4]], [[SKIP-1-2-3]], [[SKIP-1-3-2]]
- SKIP 2: [[SKIP-2-1-4]], [[SKIP-2-2-3]], [[SKIP-2-3-2]], [[SKIP-2-4-1]]
- SKIP 3: [[SKIP-3-1-4]], [[SKIP-3-2-3]], [[SKIP-3-3-2]]
- SKIP 4; 
	- [[SKIP-4-5-1]]: [[母]], [[且]]
	- [[SKIP-4-5-2]]
	- [[SKIP-4-5-3]]
	- [[SKIP-4-5-4]]


```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "5" OR stroke_count = 5
SORT file.name ASC