---
size: 280
---
## Characters
[[不 (char)]], [[久 (char)]], [[乎 (char)]], [[乗 (char)]], [[争]], [[京]], [[代]], [[以 (char)]], [[伝]], [[位]], [[低]], [[例]], [[便 (char)]], [[信]], [[個 (char)]], [[借 (char)]], [[兄 (char)]], [[光 (char)]], [[児 (char)]], [[公 (char)]], [[共 (char)]], [[兵]], [[典]], [[再]], [[冷 (char)]], [[処 (char)]], [[別 (char)]], [[利]], [[功]], [[加]], [[化 (char)]], [[医]], [[単]], [[印]], [[収]], [[取]], [[古]], [[句 (char)]], [[各 (char)]], [[合 (char)]], [[同]], [[唱]], [[図]], [[在 (char)]], [[坐 (char)]], [[基]], [[堂]], [[報 (char)]], [[士 (char)]], [[変 (char)]], [[好 (char)]], [[守]], [[完]], [[将 (char)]], [[就 (char)]], [[展]], [[己]], [[布]], [[希]], [[常]], [[干]], [[平]], [[広 (char)]], [[弓 (char)]], [[引 (char)]], [[../characters/形 (char)]], [[従 (char)]], [[得]], [[快 (char)]], [[愛 (char)]], [[成 (char)]], [[我 (char)]], [[戦]], [[戸]], [[接 (char)]], [[推 (char)]], [[支]], [[救]], [[敗]], [[散]], [[方]], [[旧 (char)]], [[時 (char)]], [[暑 (char)]], [[暗 (char)]], [[最 (char)]], [[望]], [[未 (char)]], [[来 (char)]], [[栄]], [[植]], [[止]], [[此 (char)]], [[歴]], [[殺 (char)]], [[比 (char)]], [[民]], [[永]], [[決 (char)]], [[油 (char)]], [[治]], [[清]], [[満 (char)]], [[漁]], [[無 (char)]], [[然 (char)]], [[爾 (char)]], [[片 (char)]], [[物 (char)]], [[特]], [[現 (char)]], [[理]], [[由 (char)]], [[番 (char)]], [[皮]], [[直 (char)]], [[看 (char)]], [[示]], [[祖]], [[神 (char)]], [[科]], [[種]], [[約]], [[紅 (char)]], [[続]], [[美 (char)]], [[義]], [[老 (char)]], [[能]], [[自]], [[興 (char)]], [[舎]], [[良]], [[芸]], [[莫 (char)]], [[菜]], [[葉 (char)]], [[血 (char)]], [[衣]], [[被 (char)]], [[要]], [[角 (char)]], [[試]], [[詩]], [[説]], [[課 (char)]], [[調]], [[講]], [[謝]], [[谷 (char)]], [[貨]], [[責]], [[赤 (char)]], [[身]], [[軍]], [[退 (char)]], [[連 (char)]], [[達 (char)]], [[野]], [[量]], [[鉄 (char)]], [[銀 (char)]], [[銭]], [[関 (char)]], [[静]], [[非 (char)]], [[面]], [[順]], [[類]], [[飛]], [[首]], [[鳥 (char)]], [[鳴 (char)]], [[鼻 (char)]], [[晩 (char)]]

## Base check
```base
filters:
  and:
    - file.folder == "characters"
    - grade_level == "2"
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
        - grade_level == 2
    order:
      - file.name
      - 注音
      - english
      - danayo_id
      - hanmun_edu_level
      - hsk_level
      - joyo_level
      - formula.spot
      - date-last-perfect
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
      note.hsk_level: 52
      note.joyo_level: 39

```