---
size: 10
stroke_count: 11
skip_number: 2-7-4
---
> SKIP : 2 : [7](lookup/SKIP/SKIP-2/SKIP-2-7.md)
> [Stroke 11](lookup/Stroke/Stroke%2011.md)
## Characters
1. 黒 (char)
2. 軣
3. 梨 (char)
4. 梁 (char)
5. 望
6. 曹
7. 悪 (char)
8. 患 (char)
9. 悠
10. 悉

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-4"
SORT file.name ASC