---
stroke_count: 16
date-last-perfect:
skip_number: 1-7-9
---
> SKIP : 1 : [7](lookup/SKIP/SKIP-1/SKIP-1-7.md)
> [Stroke 16](lookup/Stroke/Stroke%2016.md)

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-7-9")
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
WHERE skip_number = "1-7-9"
SORT file.name ASC
```
