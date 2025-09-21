```dataview
TABLE file.link AS Character, cantonese
FROM "characters"
WHERE cantonese = null OR cantonese = ""
SORT file.name ASC
```
