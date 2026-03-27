---
stroke_count: 12
date-last-perfect:
size: 344
---
> [Stroke](Stroke.md)

1. SKIP-1
	1. SKIP-1-11-1: No
	2. [[SKIP-1-10-2]]: 凱, 割, 創, 勤, 馭
	3. [[SKIP-1-9-3]]: 
	4. [[SKIP-1-8-4]]: 
	5. [[SKIP-1-7-5]]: 
	6. [[SKIP-1-6-6]]:
	7. [[SKIP-1-5-7]]:
	8. [[SKIP-1-4-8]]:
	9. [[SKIP-1-3-9]]:
	10. [[SKIP-1-2-10]]:
	11. [[SKIP-1-1-11]]:
2. SKIP-2
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "12" OR stroke_count = 12
SORT skip_number ASC