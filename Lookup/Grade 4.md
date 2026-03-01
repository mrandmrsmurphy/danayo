---
size: 327
---
## Characters
```dataview
LIST
FROM "characters"
WHERE grade_level = "4" OR grade_level = 4
```

## Base check
```base
filters:
  and:
    - file.folder == "characters"
    - grade_level == "4"
formulas:
  spot: if(hsk_level=="1",303,0)+if(hsk_level=="2",248,0)+if(hsk_level=="3",201,0)+if(hsk_level=="4",111,0)+if(joyo_level=="1",299,0)+if(joyo_level=="2",277,0)+if(joyo_level=="3",254,0)+if(joyo_level=="4",223,0)+if(joyo_level=="5",206,0)+if(joyo_level=="6",179,0)+if(joyo_level=="高等",158,0)+if(joyo_level=="日本人名用漢字",99,0)+if(hanmun_edu_level=="中",401,0)+if(hanmun_edu_level=="高等",222,0)+if(hanmun_edu_level=="名",27,0)
properties:
  formula.spot:
    displayName: score
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - grade_level == 4
    order:
      - file.name
      - 注音
      - english
      - danayo_id
      - hanmun_edu_level
      - hsk_level
      - joyo_level
      - formula.spot
    sort:
      - property: formula.spot
        direction: DESC
      - property: joyo_level
        direction: ASC
      - property: hanmun_edu_level
        direction: DESC
      - property: danayo_id
        direction: ASC
    columnSize:
      file.name: 40
      note.english: 98
      note.danayo_id: 64
      note.hanmun_edu_level: 57

```