---
size: 306
---

## List
1. <ruby>[九](/characters/九%20(char).md)<rt>ㄎ˙ㄨ</rt></ruby> - elbow (nine)
2. <ruby>[勿](/characters/勿%20(char).md)<rt>ㄇㄨㄊ</rt></ruby> - blood on a knife (do not)
3. <ruby>[長](/characters/長%20(char).md)<rt>ㄐㄚㄥ</rt></ruby> - old man with long hair (long)
4. <ruby>[羊](/characters/羊.md)<rt>˙ㄚㄥ</rt></ruby> - sheep
5. <ruby>[己](/characters/己.md)<rt>ㄍㄧ</rt></ruby> - silk rope (self)
6. <ruby>[魚](/characters/魚%20(char).md)<rt>˙ㄛ</rt></ruby> - fish
7. <ruby>[月](/characters/月%20(char).md)<rt>ˇㄝㄊ</rt></ruby> - moon

丁 (char), 七 (char), 万, 不 (char), 丐, 且 (char), 世, 丙 (char), 串 (char), 丸, 丹, 主, 丼, 乃 (char), 久 (char), 乍, 乖, 乙 (char), 也 (char), 亀 (char), 了 (char), 争, 于 (char), 互, 五 (char), 井, 亜, 亢, 交 (char), 亥, 亨, 享, 京, 人 (char), 以 (char), 余, 侯 (char), 俎, 倉, 傘, 兀, 元, 兆, 免, 兎 (char), 兜 (char), 入 (char), 其 (char), 冉, 冊 (char), 再, 冘, 凡, 凶 (char), 凸 (char), 出 (char), 函, 刀, 力 (char), 勺 (char), 包, 匕, 升 (char), 午, 半, 卍, 南, 単, 卞, 卯, 卵, 又 (char), 口 (char), 只 (char), 史, 呂, 咼, 回 (char), 囧, 土 (char), 圭, 垂, 士 (char), 壬, 夕, 夗, 大 (char), 天 (char), 夫 (char), 夭, 夷, 奚 (char), 奥 (char), 女 (char), 子, 害, 寅, 対, 尗, 屮, 屯 (char), 山 (char), 岩, 川 (char), 州 (char), 巠, 巣, 工, 巨, 巫, 已 (char), 巳, 巴 (char), 巻 (char), 巾, 市, 帚, 帝, 帯 (char), 干, 平, 庚, 弓 (char), 弔 (char), 弟 (char), 微, 心 (char), 必 (char), 戈, 戊, 戸, 手 (char), 才, 敖, 文, 斗 (char), 斤, 方, 於 (char), 日 (char), 昆 (char), 易, 曰 (char), 曽 (char), 朋, 木 (char), 未 (char), 朮, 朱, 朶, 束 (char), 来 (char), 果, 栗 (char), 業 (char), 止, 歯 (char), 歹, 殿, 母, 毒 (char), 毛 (char), 氏, 氐, 民, 水 (char), 氷, 永, 氾, 求, 泉, 淵, 火 (char), 為 (char), 烏, 焉 (char), 無 (char), 燕, 爪 (char), 父, 爾 (char), 片 (char), 牙, 牛 (char), 犬 (char), 犮, 玄 (char), 率, 玉 (char), 王 (char), 琴 (char), 瓜, 瓦 (char), 甘 (char), 生, 用, 甫, 田, 由 (char), 甲 (char), 申, 畐, 畜, 番 (char), 疋, 癸, 白 (char), 皀, 皇, 皿 (char), 目 (char), 盾 (char), 眉 (char), 矛, 矢 (char), 示, 禺, 禼, 禾 (char), 立 (char), 竹 (char), 箕, 米 (char), 粟, 糸, 素, 索, 缶, 美 (char), 羸, 羽, 考, 者 (char), 而 (char), 耳 (char), 耴, 肉 (char), 胃 (char), 胤, 能, 臣, 自, 至 (char), 臼 (char), 舌 (char), 舜, 舟, 良, 莫 (char), 華, 萬, 蛇 (char), 蜀, 衆, 衣, 衰, 西, 角 (char), 託, 谷 (char), 豆 (char), 豊, 豕, 象, 貝, 走 (char), 車 (char), 辰, 酉, 酋, 門, 闘, 阜, 隔, 隹, 雨 (char), 非 (char), 面, 革, 韮, 頁 (char), 飛, 食 (char), 首, 馬 (char), 高 (char), 鬼, 鳥 (char), 鸛, 鹵, 鹿 (char), 黒 (char), 鼎 (char), 鼡, 龍 (char), 㐬, 㒼, 𡈼


## Base check
```base
filters:
  and:
    - graphemic_classification == "象形"
views:
  - type: table
    name: Table
    filters:
      and:
        - graphemic_classification == "象形"
    order:
      - file.name
      - 注音
      - english
      - danayo_id
      - hanmun_edu_level
      - date-last-perfect
      - grade_level
    sort:
      - property: date-last-perfect
        direction: ASC
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