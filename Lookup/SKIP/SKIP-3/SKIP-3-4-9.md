---
stroke_count: 13
date-last-perfect:
skip_number: 3-4-9
---
> SKIP : 3 : [4](lookup/SKIP/SKIP-3/SKIP-3-4.md)
> [Stroke 13](lookup/Stroke/Stroke%2013.md)

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "3-4-9")
// or stricter: .where(p => p["your_property"] === "value"
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()
  .join(", ");

dv.paragraph(titles || "No matching pages");
```

## Datacheck
```dataview
TABLE 注音 AS "Sound", english AS "en"
FROM "characters"
WHERE skip_number = "3-4-9"
SORT file.name ASC
```
