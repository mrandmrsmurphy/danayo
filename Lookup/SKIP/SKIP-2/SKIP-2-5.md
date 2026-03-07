---
aliases:
---
> [[SKIP]] : 2

1. [SKIP-2-5-1](lookup/SKIP/SKIP-2/SKIP-2-5-1.md): 丞	
2. [SKIP-2-5-2](lookup/SKIP/SKIP-2/SKIP-2-5-2.md): 兵	甼	労	禿	秀	児	呉 皃	見	貝	皀	努	男	
3. [SKIP-2-5-3](lookup/SKIP/SKIP-2/SKIP-2-5-3.md): 岳	学	季 委	具	妻	弩	帛	帑	孥	妾	垈	咎 岱	奉	長	
4. [SKIP-2-5-4](lookup/SKIP/SKIP-2/SKIP-2-5-4.md): 胄	架	怨	春	胃	某 発	竒	胥	怒	栄	冑	背	畏	癸	泉 染	拏	怱	怎	界	罘	皇	香	奏	毘 思	
5. [SKIP-2-5-5](lookup/SKIP/SKIP-2/SKIP-2-5-5.md): 烝	秦	帯	泰	党	畠	留	冓 哥	皋	祟	罟	罠	芻	
6. [SKIP-2-5-6](lookup/SKIP/SKIP-2/SKIP-2-5-6.md): 紮	袰	畧 皐	焉	蛍	袈	畢	累	蛋	常	舂	堂 袋	異	
7. [SKIP-2-5-7](lookup/SKIP/SKIP-2/SKIP-2-5-7.md): 塁	貸	貿	貰	畳	黹	掌 棠	黍	貴	發	覚	賀	詈	買	営	登 費
8. [SKIP-2-5-8](lookup/SKIP/SKIP-2/SKIP-2-5-8.md): 罩	罫	罧	業	署	蜀	當	甞 置	罪	罨	惷	
9. [SKIP-2-5-9](lookup/SKIP/SKIP-2/SKIP-2-5-9.md): 罰	盡	嘗	裳
10. [SKIP-2-5-10](lookup/SKIP/SKIP-2/SKIP-2-5-10.md): 磊	罷	罸	駑	駕	罵	賞
11. [SKIP-2-5-11](lookup/SKIP/SKIP-2/SKIP-2-5-11.md): 鴦 鴬	黛	冀	罹	鴛	疂
12. [SKIP-2-5-12](lookup/SKIP/SKIP-2/SKIP-2-5-12.md): 竃
13. [SKIP-2-5-13](lookup/SKIP/SKIP-2/SKIP-2-5-13.md):  羃	叢	壘 羂	
14. [SKIP-2-5-14](lookup/SKIP/SKIP-2/SKIP-2-5-14.md): 羆	羅	
15. [SKIP-2-5-15](lookup/SKIP/SKIP-2/SKIP-2-5-15.md): 黨	
16. [SKIP-2-5-16](lookup/SKIP/SKIP-2/SKIP-2-5-16.md) : 贔	罍
17. [SKIP-2-5-17](lookup/SKIP/SKIP-2/SKIP-2-5-17.md) : 羇	疉	疊	
18. no
19. [SKIP-2-5-19](lookup/SKIP/SKIP-2/SKIP-2-5-19.md): 羈


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-5")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```