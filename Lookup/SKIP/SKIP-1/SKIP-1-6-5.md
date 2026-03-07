---
stroke_count: 11
date-last-perfect:
skip_number: 1-6-5
---
> SKIP : 1 : [6](lookup/SKIP/SKIP-1/SKIP-1-6.md)
> [Stroke 11](lookup/Stroke/Stroke%2011.md)

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-6-5")
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
WHERE skip_number = "1-6-5"
SORT file.name ASC
```
