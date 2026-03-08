---
size: 2
date-last-perfect:
stroke_count: 4
skip_number: 4-4-2
---
> SKIP : 4 : [4](lookup/SKIP/SKIP-4/SKIP-4-4.md) | [SKIP-4-0-2](lookup/SKIP/SKIP-4/SKIP-4-0-2.md)
> [Stroke 04](lookup/Stroke/Stroke%2004.md)

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "4-4-2")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "4-4-2"
SORT file.name ASC