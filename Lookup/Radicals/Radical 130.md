---
size: 69
radical: 肉
---
> [[Radicals]]


# Data search
```dataview
TABLE radical AS "Radical", 注音 AS "Sound", stroke_count AS "S"
FROM "characters"
WHERE radical = "肉"
SORT stroke_count ASC