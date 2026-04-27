---
size: 7
radical: 士
tags: [lookup]

---
> [[Radicals]]

## Characters
### Used
1. [[士 (char)]]
2. [[壬]]
3. [[壮]]
4. [[声]]
5. [[壱 (char)]]
6. [[売]]
7. [[壷]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "士"
    order:
      - file.name
      - danayo_id
      - english
      - 注音
      - skip_number
      - stroke_count
    columnSize:
      note.danayo_id: 64
      note.english: 236
```