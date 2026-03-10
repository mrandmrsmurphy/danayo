from pathlib import Path

while True:
    name = input("Enter 注音 name (blank to quit): ").strip()
    if name == "":
        print("Done.")
        break

    filename = Path(f"{name}.md")

    content = f"""---
date-last-perfect:
size:
羅馬字:
韓文:
注音: {name}
---
> [Syllables](syllables/Syllables.md)
> **{name}**  means 

## Characters
```dataviewjs
const pages = dv.pages()
  .where(p => p.注音 === "{name}")

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
```

## Data check
```dataview
TABLE english AS "EN", stand_in AS "SI", grade_level AS "GL"
FROM "characters"
WHERE 注音 = "{name}"
SORT grade_level ASC
```
"""

    filename.write_text(content, encoding="utf-8")
    print(f"Created {filename}")
