---
date-last-perfect:
---
> [[SKIP]] : 1

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-4-14")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. [SKIP-1-4-1](lookup/SKIP/SKIP-1/SKIP-1-4-1.md): 札, 礼
2. [SKIP-1-4-2](lookup/SKIP/SKIP-1/SKIP-1-4-2.md): 刑, 列, 印, 朴, 朽, 此, 灯, 肋, 肌
3. [SKIP-1-4-3](lookup/SKIP/SKIP-1/SKIP-1-4-3.md): 卵, 対, 形, 彤, 杆, 杉, 材, 村, 杖, 杜, 杞, 灼, 牡, 玖, 祁, 肘, 肛, 肝, 邢, 那, 邦, 邪
4. [SKIP-1-4-4](lookup/SKIP/SKIP-1/SKIP-1-4-4.md): 所, 放, 於, 旺, 明, 朋, 服, 杪, 杯, 杴, 松, 板, 枉, 析, 枕, 林, 枚, 枝, 枢, 欣, 欧, 殴, 炉, 炊, 炒, 爬, 版, 牧, 物, 玩, 祇, 祈, 祉, 股, 肢, 肥, 肪, 肭, 肰, 門, 非, 䏜, 𦚖
5. [SKIP-1-4-5](lookup/SKIP/SKIP-1/SKIP-1-4-5.md): 俎, 施, 映, 昧, 昨, 昭, 枯, 柄, 柉, 柊, 柏, 柑, 柩, 柯, 柱, 柳, 柵, 柿, 栃, 殃, 殆, 炢, 炸, 牲, 玲, 玳, 玻, 珀, 珂, 珈, 珉, 珊, 珍, 相, 祐, 祖, 祢, 肺, 胆, 胎, 胖, 胞
6. [SKIP-1-4-6](lookup/SKIP/SKIP-1/SKIP-1-4-6.md): 旅, 時, 晒, 晦, 朕, 栓, 校, 株, 核, 根, 格, 桁, 桂, 桃, 桐, 桓, 桔, 桜, 桟, 桧, 梅, 殉, 殊, 残, 特, 珠, 班, 祥, 胰, 胱, 胴, 胸, 脂, 脆, 脈
7. [SKIP-1-4-7](lookup/SKIP/SKIP-1/SKIP-1-4-7.md): 彬, 族, 晨, 桶, 梓, 梗, 梛, 梢, 械, 梳, 梶, 現, 球, 理, 琢, 脚, 脛, 脱, 脳, 規, 視, 豚
8. [SKIP-1-4-8](lookup/SKIP/SKIP-1/SKIP-1-4-8.md): 勝, 斑, 晩, 晴, 暁, 期, 棋, 棍, 棒, 棕, 棚, 棟, 棲, 棺, 椅, 椋, 植, 椎, 椒, 検, 極, 殖, 焰, 焼, 牌, 琥, 琳, 琺, 瑛, 脹, 脾, 腔, 腕, 雄, 𦜝
9. [SKIP-1-4-9](lookup/SKIP/SKIP-1/SKIP-1-4-9.md): 暇, 暖, 暗, 椰, 椿, 楊, 楓, 楔, 楕, 楠, 楢, 楷, 楼, 榔, 槌, 煌, 煙, 煤, 煥, 煩, 牒, 瑁, 瑚, 禅, 禎, 福, 腫, 腰, 腸, 腹, 腺, 腿, 頌, 頑, 頒, 頓
10. [SKIP-1-4-10](lookup/SKIP/SKIP-1/SKIP-1-4-10.md)
11. [SKIP-1-4-11](lookup/SKIP/SKIP-1/SKIP-1-4-11.md)
12. [SKIP-1-4-12](lookup/SKIP/SKIP-1/SKIP-1-4-12.md)
13. [SKIP-1-4-13](lookup/SKIP/SKIP-1/SKIP-1-4-13.md)
14. [SKIP-1-4-14](lookup/SKIP/SKIP-1/SKIP-1-4-14.md)
15. [SKIP-1-4-15](lookup/SKIP/SKIP-1/SKIP-1-4-15.md): 爆, 臓
16. [SKIP-1-4-16](lookup/SKIP/SKIP-1/SKIP-1-4-16.md): 朧, 騰
17. [SKIP-1-4-17](lookup/SKIP/SKIP-1/SKIP-1-4-17.md): 欄, 爛
18. [SKIP-1-4-18](lookup/SKIP/SKIP-1/SKIP-1-4-18.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```