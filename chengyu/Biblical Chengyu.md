---
date-last-perfect: 2026-09-12
tags:
  - chengyu
---

Over all is [[創反救成]] - Creation/Fall/Redemption/Consummation

- [[指記二碑]] - the two tables of the law
- <ruby>[上下無偶](/chengyu/上下無偶.md)<rt>ㄙ⼘ㄫㄏㄚㄇㄨ·ㄛㄊ</rt></ruby> - above and below no idols
- [[愛主耳錐]] - love master?  ear awl
- [[瑠璃清天]] - lapis lazuli, like heaven for clearness
- [[血誓盟約]] - the blood of the covenant
- [[心性意力]] - heart soul mind and strength
- [[愛隣如自]] - love your neighbor as yourself
- [[数数衡分]] - mene, mene, tekel, upharsim
- [[帰塵帰土]] - ashes to ashes, dust to dust
- [[汗食帰泥]] - by the sweat of your brow
- [[腹行食塵]] - crawl belly eat dust
- [[破頭傷足]] - smash head hurt foot
- [[家分不立]] - a house divided against itself cannot stand
- [[豹斑改乎]] - Can a leopard change his spots?
- [[財愛悪根]] - The love of money is the root of evil
- [[剣生剣死]] - Live by the sword, die by the sword
- [[骨肉相連]] - Bone of my bone and flesh of my flesh
- [[金銀銅鉄]] - gold, silver, copper, iron
- [[石山盈界]] - stone mountain fills the earth
- [[事事皆旧]] - there is nothing new under the sun
- [[乳蜜流地]] - a land flowing with milk and honey
- [[六作一止]] - six days of labor, one of rest
- [[殺姦窃偽]] - murder, adultery, theft, lying
- [[荊棘荻蓬]] - thorns and thistles
- [[多召少選]] - many are called, few are chosen
- [[生机勃勃]] - resurrection life
- [[飲食歓楽]] - eat, drink, and be merry
- [[加哀痛産]] - add sorrow to painful labor
- [[道活墨殺]] - Letter kills, Spirit life
- [[勿妄称名]] - Don't take the Name in vain
- [[不打不成器]] - spare the rod, spoil the child
- [[世仇宿敵]] - generational feud with a long-standing enemy
- [[世間罪盛]] - the world is sinful
- [[主宰万物]] - Dominion over all things
- [[勿貪隣物]] - don't covet neighbor's things
- [[十人不滅]] - for ten people I will not destroy, quorum, minyan
- [[塩地光世]] - salt of the earth and light of the world
- [[孝親天賜]] - Honor your parents, that heaven may gift (you)
- [[尊敬父母]] - Honor parents
- [[引出奴家]] - I lead you out of slavery
- [[愛偕者神]] - Love YHWH your God
- [[招災引禍]] - invite disaster cause trouble
- [[欲夫治汝]] - Wanting your husband, he will rule you
- [[珠投猪前]] - throwing pearls before swine
- [[禍延子孫]] - prolonged disaster: for one's descendants
- [[羊衣餓狼]] - wolf in sheep's clothing
- [[詛地哀食]] - Cursed ground, sorrowful eating
- [[轄魚鳥牲]] - Rule fish, birds, life
- [[造人像形]] - Create man (in our) image (and) likeness
- [[邪心常悪]] - evil hearts, evil intents
- [[銀盤呈首]] - Head on a silver platter
- [[除我莫神]] - There are no other gods but me
- [[雲昼火夜]] - cloud by day, fire by night

## Base check
```base
filters:
  and:
    - file.folder == "chengyu"
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "chengyu"
        - origin == "Bible"
    order:
      - file.name
      - date-last-perfect
      - 注音
      - 羅馬字
      - 諺文
      - vietnamese
    sort:
      - property: date-last-perfect
        direction: ASC
      - property: size
        direction: ASC
    columnSize:
      note.date-last-perfect: 131
      note.注音: 81

```