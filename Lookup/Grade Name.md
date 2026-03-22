---
size: 795
---


## Base check
```base
filters:
  and:
    - file.folder == "characters"
    - grade_level == "名"
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
        - grade_level == "名"
    order:
      - file.name
      - 注音
      - english
      - date-last-perfect
      - danayo_id
    sort:
      - property: danayo_id
        direction: ASC
      - property: 注音
        direction: ASC
      - property: date-last-perfect
        direction: ASC
      - property: stand_in
        direction: ASC
      - property: formula.spot
        direction: DESC
      - property: joyo_level
        direction: ASC
      - property: hanmun_edu_level
        direction: DESC
    columnSize:
      file.name: 40
      note.english: 215
      note.graphemic_classification: 87

```