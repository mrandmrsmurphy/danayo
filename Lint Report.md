---
tags:
  - lookup
date-last-perfect: 2026-10-29
---
# Lint Report

Generated 2026-10-29 by `AIOS/scripts/make_lint_report.py` from the linters' own output. Every flagged page is a clickable link. Re-run any section with the command shown.

> Related: [[lookup/Characters|Characters]] · [[lookup/Words|Words]] · [[AIOS/skills/skill_lint|Lint skill]] · [[AIOS/checklists/checklist_words|Words checklist]] · [[AIOS/checklists/checklist_characters|Characters checklist]]

## Linter status

| Linter | Command | State today |
|---|---|---|
| Syllables | `python3 AIOS/scripts/lint_syllables.py` | Pass; stamped 2026-10-29 |
| SKIP | `python3 AIOS/scripts/lint_skip.py` | Pass; stamped 2026-10-29 |
| Radicals | `python3 AIOS/scripts/lint_radicals.py` | Pass; stamped 2026-10-29 |
| CC | `python3 AIOS/scripts/lint_cc.py` | Pass; stamped 2026-10-29 |
| Stroke | `python3 AIOS/scripts/lint_stroke.py` | Clean (does not stamp) |
| Chengyu | `python3 AIOS/scripts/lint_chengyu.py`, `lint_chengyu_groups.py` | Clean; grouping pages stamped 2026-10-29 |
| Characters | `python3 AIOS/scripts/lint_characters.py` | Default run clean; stamped 2026-10-29. `--deep`: C1 268, C2 64 |
| **Words** | `python3 AIOS/scripts/lint_words.py` | **Fails**: C2 61, C3 25 |

## Contents

- [[#Words (lint_words.py)]]
- [[#Characters, --deep run]]
- [[#Judgment items still open]]

## Words (lint_words.py)


### [C2] a markdown link does not resolve (51)

- [[words/互連網|互連網]]: /characters/連.md
- [[words/互連網|互連網]]: /characters/網.md
- [[words/互連網|互連網]]: ../characters/連.md
- [[words/互連網|互連網]]: ../characters/網.md
- [[words/人気|人気]]: ../characters/気.md
- [[words/付加|付加]]: ../words/加.md
- [[words/代表之|代表之]]: /characters/之.md
- [[words/分校|分校]]: /characters/分.md
- [[words/分校|分校]]: ../characters/分.md
- [[words/到達|到達]]: /characters/達.md
- [[words/到達|到達]]: ../characters/達.md
- [[words/前舌|前舌]]: ../characters/前.md
- [[words/前舌|前舌]]: ../characters/舌.md
- [[words/協力|協力]]: /characters/力.md
- [[words/協力|協力]]: ../characters/力.md
- [[words/南部|南部]]: /characters/部.md
- [[words/南部|南部]]: ../characters/部.md
- [[words/古層|古層]]: ../characters/層.md
- [[words/叩頭|叩頭]]: /characters/頭.md
- [[words/叩頭|叩頭]]: ../characters/頭.md
- [[words/夫婦|夫婦]]: ../characters/婦.md
- [[words/巨人|巨人]]: ../characters/人.md
- [[words/巨大|巨大]]: ../characters/大.md
- [[words/広東|広東]]: ../characters/広.md
- [[words/広東|広東]]: ../words/東.md
- [[words/打撃|打撃]]: ../characters/撃.md
- [[words/撞球|撞球]]: ../characters/撞.md
- [[words/火山島|火山島]]: ../characters/山.md
- [[words/火山島|火山島]]: ../characters/島.md
- [[words/火星|火星]]: ../characters/星.md
- [[words/灰塵|灰塵]]: ../characters/灰.md
- [[words/無名指|無名指]]: ../characters/指 (char).md
- [[words/無政府|無政府]]: ../characters/政 (char).md
- [[words/無政府|無政府]]: ../characters/府 (char).md
- [[words/疑問|疑問]]: ../words/疑.md
- [[words/硬口蓋|硬口蓋]]: ../words/蓋.md
- [[words/空隙|空隙]]: ../characters/空.md
- [[words/空隙|空隙]]: ../characters/隙.md
- [[words/終止|終止]]: ../words/終.md
- [[words/胸部|胸部]]: ../characters/部.md
- [[words/自分|自分]]: ../characters/分.md
- [[words/苦渋|苦渋]]: ../characters/苦.md
- [[words/草屋|草屋]]: ../characters/草.md
- [[words/草屋|草屋]]: ../characters/屋.md
- [[words/軟口蓋|軟口蓋]]: ../words/軟.md
- [[words/軟口蓋|軟口蓋]]: ../words/蓋.md
- [[words/送気|送気]]: ../characters/気.md
- [[words/過程|過程]]: ../characters/過.md
- [[words/部族|部族]]: ../characters/部.md
- [[words/階段|階段]]: ../characters/段.md
- [[words/露国|露国]]: ../characters/露.md

### [C2] a [[wikilink]] does not resolve (10)

- [[words/客人|客人]]: [[来客]]
- [[words/性交|性交]]: [[個性]]
- [[words/愛爾蘭|愛爾蘭]]: [[共和國]]
- [[words/愛爾蘭|愛爾蘭]]: [[共和國]]
- [[words/白路|白路]]: [[鷺]]
- [[words/瞻妄|瞻妄]]: [[譫]]
- [[words/脂肪|脂肪]]: [[方 (char)]]
- [[words/見|見]]: [[卩]]
- [[words/計画|計画]]: [[安排]]
- [[words/高句麗|高句麗]]: [[渤海]]

### [C3] the lexipedia domain page does not link this word (22)

- [[words/中華民国|中華民国]] -> Geography
- [[words/兗州|兗州]] -> Geography
- [[words/北海|北海]] -> Geography
- [[words/四海|四海]] -> Geography
- [[words/地図学|地図学]] -> Geography
- [[words/基金|基金]] -> Geography
- [[words/密度|密度]] -> Geography
- [[words/拡散|拡散]] -> Geography
- [[words/毅然|毅然]] -> Mind
- [[words/王畿|王畿]] -> Geography
- [[words/理由|理由]] -> Knowledge
- [[words/環状|環状]] -> Geography
- [[words/甄選|甄選]] -> Mind
- [[words/真摯|真摯]] -> Mind
- [[words/粒子|粒子]] -> Physics
- [[words/自閉|自閉]] -> Mind
- [[words/航路|航路]] -> Geography
- [[words/荊州|荊州]] -> Geography
- [[words/西海|西海]] -> Geography
- [[words/観察|観察]] -> Mind
- [[words/言及|言及]] -> Mind
- [[words/鎬京|鎬京]] -> China

### [C3] `lexipedia:` property and the "See" bullets name different domains (3)

- [[words/中華民国|中華民国]]: property ['Geography'] vs bullets []
- [[words/四海|四海]]: property ['China', 'Geography'] vs bullets ['China']
- [[words/恭喜発財|恭喜発財]]: property [] vs bullets ['Calendar']

## Characters, --deep run

The default run checks only pages changed since their own stamp and is clean. `python3 AIOS/scripts/lint_characters.py --deep` checks every page and finds this hidden drift in already-stamped pages.

### [C1] link in a Notes bullet is missing the `../` prefix (177)

- [[characters/丙 (char)|丙 (char)]]
- [[characters/両 (char)|両 (char)]]
- [[characters/乃 (char)|乃 (char)]]
- [[characters/久 (char)|久 (char)]]
- [[characters/乎 (char)|乎 (char)]]
- [[characters/也 (char)|也 (char)]]
- [[characters/亀 (char)|亀 (char)]]
- [[characters/争|争]]
- [[characters/今 (char)|今 (char)]]
- [[characters/以 (char)|以 (char)]]
- [[characters/但 (char)|但 (char)]]
- [[characters/低|低]]
- [[characters/佛 (char)|佛 (char)]]
- [[characters/佳 (char)|佳 (char)]]
- [[characters/侘|侘]]
- [[characters/便 (char)|便 (char)]]
- [[characters/俗 (char)|俗 (char)]]
- [[characters/信|信]]
- [[characters/修|修]]
- [[characters/倍 (char)|倍 (char)]]
- [[characters/借 (char)|借 (char)]]
- [[characters/停|停]]
- [[characters/備|備]]
- [[characters/億|億]]
- [[characters/兵|兵]]
- [[characters/典|典]]
- [[characters/冊 (char)|冊 (char)]]
- [[characters/再|再]]
- [[characters/処 (char)|処 (char)]]
- [[characters/凶 (char)|凶 (char)]]
- [[characters/列|列]]
- [[characters/初|初]]
- [[characters/功|功]]
- [[characters/勇|勇]]
- [[characters/勉 (char)|勉 (char)]]
- [[characters/勝|勝]]
- [[characters/匹 (char)|匹 (char)]]
- [[characters/印|印]]
- [[characters/危|危]]
- [[characters/取|取]]
- [[characters/古|古]]
- [[characters/句 (char)|句 (char)]]
- [[characters/只 (char)|只 (char)]]
- [[characters/各 (char)|各 (char)]]
- [[characters/吹 (char)|吹 (char)]]
- [[characters/品 (char)|品 (char)]]
- [[characters/唱|唱]]
- [[characters/問|問]]
- [[characters/在 (char)|在 (char)]]
- [[characters/均 (char)|均 (char)]]
- [[characters/坐 (char)|坐 (char)]]
- [[characters/城|城]]
- [[characters/基|基]]
- [[characters/堂|堂]]
- [[characters/報 (char)|報 (char)]]
- [[characters/士 (char)|士 (char)]]
- [[characters/失|失]]
- [[characters/守|守]]
- [[characters/完|完]]
- [[characters/官|官]]
- [[characters/宙 (char)|宙 (char)]]
- [[characters/定|定]]
- [[characters/客|客]]
- [[characters/室|室]]
- [[characters/害|害]]
- [[characters/容 (char)|容 (char)]]
- [[characters/宿|宿]]
- [[characters/密 (char)|密 (char)]]
- [[characters/富|富]]
- [[characters/察|察]]
- [[characters/寸 (char)|寸 (char)]]
- [[characters/将 (char)|将 (char)]]
- [[characters/就 (char)|就 (char)]]
- [[characters/岩|岩]]
- [[characters/島 (char)|島 (char)]]
- [[characters/布|布]]
- [[characters/希|希]]
- [[characters/席|席]]
- [[characters/干|干]]
- [[characters/平|平]]
- [[characters/店|店]]
- [[characters/建|建]]
- [[characters/弓 (char)|弓 (char)]]
- [[characters/弱 (char)|弱 (char)]]
- [[characters/強 (char)|強 (char)]]
- [[characters/彙 (char)|彙 (char)]]
- [[characters/往 (char)|往 (char)]]
- [[characters/得|得]]
- [[characters/忘|忘]]
- [[characters/念|念]]
- [[characters/情|情]]
- [[characters/想|想]]
- [[characters/意|意]]
- [[characters/愛 (char)|愛 (char)]]
- [[characters/成 (char)|成 (char)]]
- [[characters/技|技]]
- [[characters/投 (char)|投 (char)]]
- [[characters/支|支]]
- [[characters/政|政]]
- [[characters/救|救]]
- [[characters/散|散]]
- [[characters/方|方]]
- [[characters/族|族]]
- [[characters/旧 (char)|旧 (char)]]
- [[characters/昨 (char)|昨 (char)]]
- [[characters/晴|晴]]
- [[characters/暑 (char)|暑 (char)]]
- [[characters/暗 (char)|暗 (char)]]
- [[characters/最 (char)|最 (char)]]
- [[characters/望|望]]
- [[characters/朝 (char)|朝 (char)]]
- [[characters/期 (char)|期 (char)]]
- [[characters/未 (char)|未 (char)]]
- [[characters/松 (char)|松 (char)]]
- [[characters/果|果]]
- [[characters/案|案]]
- [[characters/植|植]]
- [[characters/極 (char)|極 (char)]]
- [[characters/樹|樹]]
- [[characters/橋 (char)|橋 (char)]]
- [[characters/止|止]]
- [[characters/此 (char)|此 (char)]]
- [[characters/歩|歩]]
- [[characters/比 (char)|比 (char)]]
- [[characters/決 (char)|決 (char)]]
- [[characters/油 (char)|油 (char)]]
- [[characters/浅 (char)|浅 (char)]]
- [[characters/深|深]]
- [[characters/漢|漢]]
- [[characters/点 (char)|点 (char)]]
- [[characters/無 (char)|無 (char)]]
- [[characters/然 (char)|然 (char)]]
- [[characters/熱 (char)|熱 (char)]]
- [[characters/爾 (char)|爾 (char)]]
- [[characters/片 (char)|片 (char)]]
- [[characters/現 (char)|現 (char)]]
- [[characters/留 (char)|留 (char)]]
- [[characters/登 (char)|登 (char)]]
- [[characters/省 (char)|省 (char)]]
- [[characters/看 (char)|看 (char)]]
- [[characters/真 (char)|真 (char)]]
- [[characters/研|研]]
- [[characters/破 (char)|破 (char)]]
- [[characters/笑 (char)|笑 (char)]]
- [[characters/答 (char)|答 (char)]]
- [[characters/算 (char)|算 (char)]]
- [[characters/節 (char)|節 (char)]]
- [[characters/紙 (char)|紙 (char)]]
- [[characters/耗|耗]]
- [[characters/興 (char)|興 (char)]]
- [[characters/草 (char)|草 (char)]]
- [[characters/莫 (char)|莫 (char)]]
- [[characters/被 (char)|被 (char)]]
- [[characters/話 (char)|話 (char)]]
- [[characters/語|語]]
- [[characters/課 (char)|課 (char)]]
- [[characters/豆 (char)|豆 (char)]]
- [[characters/買|買]]
- [[characters/起 (char)|起 (char)]]
- [[characters/路|路]]
- [[characters/農|農]]
- [[characters/送 (char)|送 (char)]]
- [[characters/速 (char)|速 (char)]]
- [[characters/達 (char)|達 (char)]]
- [[characters/遡|遡]]
- [[characters/都|都]]
- [[characters/酒|酒]]
- [[characters/銀 (char)|銀 (char)]]
- [[characters/開|開]]
- [[characters/間|間]]
- [[characters/頗 (char)|頗 (char)]]
- [[characters/風 (char)|風 (char)]]
- [[characters/飛 (char)|飛 (char)]]
- [[characters/馬 (char)|馬 (char)]]
- [[characters/高 (char)|高 (char)]]
- [[characters/鳴 (char)|鳴 (char)]]
- [[characters/鼻 (char)|鼻 (char)]]

### [C1] Stroke link is not its zero-padded Stroke page (e.g. Stroke%2004) (68)

- [[characters/㐬|㐬]]
- [[characters/㑒|㑒]]
- [[characters/䏜|䏜]]
- [[characters/䒦|䒦]]
- [[characters/丕|丕]]
- [[characters/乃 (char)|乃 (char)]]
- [[characters/今 (char)|今 (char)]]
- [[characters/仗|仗]]
- [[characters/令 (char)|令 (char)]]
- [[characters/佛 (char)|佛 (char)]]
- [[characters/佞|佞]]
- [[characters/佤|佤]]
- [[characters/俁|俁]]
- [[characters/兮 (char)|兮 (char)]]
- [[characters/劦|劦]]
- [[characters/匕|匕]]
- [[characters/匡|匡]]
- [[characters/厓|厓]]
- [[characters/叙|叙]]
- [[characters/叚|叚]]
- [[characters/叵|叵]]
- [[characters/垂|垂]]
- [[characters/奔|奔]]
- [[characters/奴|奴]]
- [[characters/姿|姿]]
- [[characters/宋|宋]]
- [[characters/巡|巡]]
- [[characters/彤|彤]]
- [[characters/役|役]]
- [[characters/担|担]]
- [[characters/攻 (char)|攻 (char)]]
- [[characters/旻|旻]]
- [[characters/杴|杴]]
- [[characters/柉|柉]]
- [[characters/歪|歪]]
- [[characters/毘|毘]]
- [[characters/汗 (char)|汗 (char)]]
- [[characters/汽|汽]]
- [[characters/沈|沈]]
- [[characters/洙|洙]]
- [[characters/洵|洵]]
- [[characters/洸|洸]]
- [[characters/灸|灸]]
- [[characters/炉|炉]]
- [[characters/炭 (char)|炭 (char)]]
- [[characters/炸|炸]]
- [[characters/熊 (char)|熊 (char)]]
- [[characters/狗|狗]]
- [[characters/珍 (char)|珍 (char)]]
- [[characters/皀|皀]]
- [[characters/砒|砒]]
- [[characters/胞|胞]]
- [[characters/芡|芡]]
- [[characters/芦|芦]]
- [[characters/芼|芼]]
- [[characters/荇|荇]]
- [[characters/衂|衂]]
- [[characters/豕|豕]]
- [[characters/軋|軋]]
- [[characters/迄|迄]]
- [[characters/迪|迪]]
- [[characters/邑|邑]]
- [[characters/邢|邢]]
- [[characters/邾|邾]]
- [[characters/采|采]]
- [[characters/陀|陀]]
- [[characters/𡈼|𡈼]]
- [[characters/𡿺|𡿺]]

### [C1] ancient-sound bullet lacks the CC initial/final links (10)

- [[characters/䎎|䎎]]
- [[characters/䒦|䒦]]
- [[characters/傘|傘]]
- [[characters/哱|哱]]
- [[characters/拐|拐]]
- [[characters/搭|搭]]
- [[characters/灋|灋]]
- [[characters/袋 (char)|袋 (char)]]
- [[characters/賠|賠]]
- [[characters/𡈼|𡈼]]

### [C1] ancient-sound bullet does not link its syllable (10)

- [[characters/䎎|䎎]]
- [[characters/䒦|䒦]]
- [[characters/傘|傘]]
- [[characters/哱|哱]]
- [[characters/拐|拐]]
- [[characters/搭|搭]]
- [[characters/灋|灋]]
- [[characters/袋 (char)|袋 (char)]]
- [[characters/賠|賠]]
- [[characters/𡈼|𡈼]]

### [C1] no Classical Chinese / ancient-sound bullet (2)

- [[characters/佤|佤]]
- [[characters/字 (char)|字 (char)]]

### [C1] no SKIP/Stroke bullet (1)

- [[characters/字 (char)|字 (char)]]

### [C2] word is listed in ## Words without a <ruby> reading (29)

- [[characters/噸 (char)|噸 (char)]] -> 噸
- [[characters/坪 (char)|坪 (char)]] -> 坪
- [[characters/壅 (char)|壅 (char)]] -> 壅
- [[characters/嫡 (char)|嫡 (char)]] -> 嫡
- [[characters/嫩 (char)|嫩 (char)]] -> 嫩
- [[characters/屁 (char)|屁 (char)]] -> 屁
- [[characters/幟 (char)|幟 (char)]] -> 幟
- [[characters/慧 (char)|慧 (char)]] -> 慧
- [[characters/憫 (char)|憫 (char)]] -> 憫
- [[characters/撮 (char)|撮 (char)]] -> 撮
- [[characters/擬 (char)|擬 (char)]] -> 擬
- [[characters/晒 (char)|晒 (char)]] -> 晒
- [[characters/槍 (char)|槍 (char)]] -> 槍
- [[characters/毫 (char)|毫 (char)]] -> 毫米
- [[characters/潰 (char)|潰 (char)]] -> 潰
- [[characters/牌 (char)|牌 (char)]] -> 牌
- [[characters/矣 (char)|矣 (char)]] -> 矣
- [[characters/碼 (char)|碼 (char)]] -> 碼
- [[characters/繰 (char)|繰 (char)]] -> 繰
- [[characters/肴 (char)|肴 (char)]] -> 肴
- [[characters/蘿|蘿]] -> 女蘿
- [[characters/跨 (char)|跨 (char)]] -> 跨
- [[characters/蹲 (char)|蹲 (char)]] -> 蹲
- [[characters/輿 (char)|輿 (char)]] -> 輿
- [[characters/鋸 (char)|鋸 (char)]] -> 鋸
- [[characters/錮 (char)|錮 (char)]] -> 錮
- [[characters/鍬 (char)|鍬 (char)]] -> 鍬
- [[characters/鍾 (char)|鍾 (char)]] -> 鍾
- [[characters/魂 (char)|魂 (char)]] -> 魂

### [C2] ruby reading in ## Words differs from the word's 注音 (24)

- [[characters/俗 (char)|俗 (char)]] -> 習俗 (ㄙㄧㄆㄙㄛㄎ vs ㄙㄜㄆㄙㄛㄎ)
- [[characters/命|命]] -> 命令 (ㄇ⼶ㄫㄌㄚㄫ vs ㄇ⼶ㄫㄌㄝㄫ)
- [[characters/天 (char)|天 (char)]] -> 天子 (ㄊㄝㄋㄐㄧ vs ㄊㄝㄋㄐㄜ)
- [[characters/天 (char)|天 (char)]] -> 天道 (ㄊㄝㄋㄙㄚㄨ vs ㄊㄝㄋㄉㄚㄨ)
- [[characters/就 (char)|就 (char)]] -> 就 (ㄐㄨㄛ vs ㄑ⺢ㄧ)
- [[characters/尺 (char)|尺 (char)]] -> 尺蠖 (ㄑㄝㄎㄏ⺢ㄎ vs ㄑㄝㄎ·⺢ㄎ)
- [[characters/思|思]] -> 思議 (ㄙㄚ·ㄨㄧ vs ㄙㄚㄜㄧ)
- [[characters/患 (char)|患 (char)]] -> 罹患 (ㄌㄧㄏ⼘ㄋ vs ㄌㄧㄏ⺢ㄇ)
- [[characters/悼 (char)|悼 (char)]] -> 哀悼 (ㄚㄋㄙㄚㄨ vs ㄚㄧㄉㄚㄨ)
- [[characters/愚 (char)|愚 (char)]] -> 下愚 (ㄏㄚㄨ vs ㄏㄚ·ㄨ)
- [[characters/愛 (char)|愛 (char)]] -> 恩愛 (ㄚㄋ·ㄚㄧ vs ㄜㄋ·ㄚㄧ)
- [[characters/授|授]] -> 教授 (ㄍ⼘ㄨㄙ⼜ vs ㄍ⼄ㄨㄙ⼜)
- [[characters/揄|揄]] -> 揶揄 (⼘·⼜ vs ⼘⼜ㄇ)
- [[characters/整 (char)|整 (char)]] -> 整理 (ㄐㄝㄫㄐㄧ vs ㄐㄝㄫㄌㄧ)
- [[characters/方|方]] -> 方言 (ㄆㄚㄫ·ㄝㄋ vs ㄈㄚㄫㄝㄋ)
- [[characters/月 (char)|月 (char)]] -> 正月 (ㄍㄧㄫ·⼔ㄊ vs ㄐㄧㄫ⼔ㄊ)
- [[characters/正 (char)|正 (char)]] -> 正月 (ㄍㄧㄫ·⼔ㄊ vs ㄐㄧㄫ⼔ㄊ)
- [[characters/法 (char)|法 (char)]] -> 法則 (ㄈㄚㄆㄐㄜㄎ vs ㄈㄚㄆㄐㄨㄎ)
- [[characters/癒|癒]] -> 癒合 (⼜ㄎㄚㄆ vs ⼜ㄍㄛㄆ)
- [[characters/芬|芬]] -> 芬蘭 (ㄆㄨㄋㄌㄚㄋ vs ㄈㄨㄋㄌㄚㄋ)
- [[characters/蘭|蘭]] -> 芬蘭 (ㄆㄨㄋㄌㄚㄋ vs ㄈㄨㄋㄌㄚㄋ)
- [[characters/言 (char)|言 (char)]] -> 方言 (ㄆㄚㄫ·ㄝㄋ vs ㄈㄚㄫㄝㄋ)
- [[characters/霜 (char)|霜 (char)]] -> 星霜 (ㄙㄝㄋㄙ⺢ㄫ vs ㄙㄝㄫㄙ⺢ㄫ)
- [[characters/駁|駁]] -> 反駁 (ㄆㄛㄋㄅㄚㄎ vs ㄈㄛㄋㄅㄚㄎ)

### [C2] word using this character is missing from ## Words (11)

- [[characters/墊 (char)|墊 (char)]] -> 墊
- [[characters/字 (char)|字 (char)]] -> 別字
- [[characters/字 (char)|字 (char)]] -> 単字
- [[characters/字 (char)|字 (char)]] -> 字庫
- [[characters/字 (char)|字 (char)]] -> 字形
- [[characters/字 (char)|字 (char)]] -> 旧字体
- [[characters/字 (char)|字 (char)]] -> 用字
- [[characters/暴 (char)|暴 (char)]] -> 暴
- [[characters/難|難]] -> 難金
- [[characters/麻|麻]] -> 大麻
- [[characters/麻|麻]] -> 麻雀鳥

## Judgment items still open

- **Words listed under a lexipedia domain whose page doesn't link them (C3 above):** add the word to the domain page, or drop the placement. Across the whole corpus there are 63.
- **Three words naming a lexipedia domain page that doesn't exist:** [[words/信条|信条]], [[words/傾向|傾向]], [[words/六府|六府]].
- **Sound exceptions (B5, resolved):** the 191 stale words were reset to their characters' readings and 5 more had their 注音 fixed (夫婦, 大夫, 理由, 自家, 弥勒). Thirteen words keep a documented divergence and are exempt via `SOUND_EXCEPTIONS` in `lint_words.py`: 反乱, 就鳥, 海就, 白頭就, 禿就, 得点, 特点, 杜選, 瞻妄, 統率, 率性, 釩金, 蓬藁 (plus 棕枝 and 棕枝主日).
- **Alias glyphs listed as characters:** [[words/神霊|神霊]] lists 神靈 and 神灵 in `characters:`; [[words/土着|土着]] is the other alias-glyph word.
- **`mc_id` drift (characters C3, resolved):** all 24 fixed. Twelve were off by one, eight point at an alias and now say "ranked there under", four were stale ranks reset to the CC list (吝, 啖, 稼, 酋).
