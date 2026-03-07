---
stroke_count: 10
date-last-perfect:
skip_number: 1-4-6
size: 35
---
> SKIP : 1 : [4](lookup/SKIP/SKIP-1/SKIP-1-4.md)
> [Stroke 10](lookup/Stroke/Stroke%2010.md)

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-4-6")
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
WHERE skip_number = "1-4-6"
SORT file.name ASC
```
