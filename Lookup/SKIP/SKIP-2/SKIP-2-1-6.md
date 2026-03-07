---
stroke_count: 7
date-last-perfect:
skip_number: 2-1-6
---
> SKIP : 2 : [1](lookup/SKIP/SKIP-2/SKIP-2-1.md)
> [Stroke 07](lookup/Stroke/Stroke%2007.md)

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "2-1-6")
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
WHERE skip_number = "2-1-6"
SORT file.name ASC
```
