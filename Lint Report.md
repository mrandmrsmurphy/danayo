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
| Characters | `python3 AIOS/scripts/lint_characters.py` | Default run clean; stamped 2026-10-29. `--deep`: C1 265, C2 52 |
| **Words** | `python3 AIOS/scripts/lint_words.py` | Default run clean; stamped 2026-10-29. `--deep`: C1 56, C2 46, C3 54 |

## Contents

- [[#Words (lint_words.py)]]
- [[#Words, --deep run]]
- [[#Characters, --deep run]]
- [[#Judgment items still open]]

## Words (lint_words.py)


The default run is clean.

## Words, --deep run

The default run checks the body only of pages changed since their own stamp. `python3 AIOS/scripts/lint_words.py --deep` checks every word and finds this drift in already-stamped pages.

### [C1] no `## Notes` section (56)

- [[words/天地|天地]]
- [[words/太始|太始]]
- [[words/深淵|深淵]]
- [[words/焦思|焦思]]
- [[words/焦点|焦点]]
- [[words/熊猫|熊猫]]
- [[words/熟練|熟練]]
- [[words/熱烈|熱烈]]
- [[words/爬虫|爬虫]]
- [[words/牆壁|牆壁]]
- [[words/片仮名|片仮名]]
- [[words/版図|版図]]
- [[words/版本|版本]]
- [[words/版権|版権]]
- [[words/牡丹|牡丹]]
- [[words/牢獄|牢獄]]
- [[words/牧民|牧民]]
- [[words/物証|物証]]
- [[words/物質|物質]]
- [[words/犬吠|犬吠]]
- [[words/犯罪|犯罪]]
- [[words/狂想曲|狂想曲]]
- [[words/狐狸|狐狸]]
- [[words/狗吠|狗吠]]
- [[words/狗盗|狗盗]]
- [[words/狗肉|狗肉]]
- [[words/猛禽|猛禽]]
- [[words/猩猩|猩猩]]
- [[words/猿痘|猿痘]]
- [[words/獄吏|獄吏]]
- [[words/玩具|玩具]]
- [[words/班長|班長]]
- [[words/現象|現象]]
- [[words/球体|球体]]
- [[words/球場|球場]]
- [[words/理想|理想]]
- [[words/理論|理論]]
- [[words/琢磨|琢磨]]
- [[words/環境|環境]]
- [[words/甘味|甘味]]
- [[words/甘藷|甘藷]]
- [[words/甘露|甘露]]
- [[words/産量|産量]]
- [[words/用度|用度]]
- [[words/男性|男性]]
- [[words/畝|畝]]
- [[words/異体|異体]]
- [[words/異常|異常]]
- [[words/異音|異音]]
- [[words/畳|畳]]
- [[words/疲労|疲労]]
- [[words/痕跡|痕跡]]
- [[words/盤|盤]]
- [[words/般|般]]
- [[words/遺憾|遺憾]]
- [[words/黒暗|黒暗]]

### [C2] a [[wikilink]] does not resolve (46)

- [[words/一|一]]: [[nav/Numerals]]
- [[words/七|七]]: [[nav/Numerals]]
- [[words/並立|並立]]: [[並行]]
- [[words/主題|主題]]: [[主語]]
- [[words/九|九]]: [[nav/Numerals]]
- [[words/借|借]]: [[藉]]
- [[words/偕者|偕者]]: [[助偕]]
- [[words/偕者|偕者]]: [[誰偕]]
- [[words/光|光]]: [[卩]]
- [[words/兮|兮]]: [[丂]]
- [[words/凶|凶]]: [[凵]]
- [[words/出|出]]: [[凵]]
- [[words/十|十]]: [[nav/Numerals]]
- [[words/反|反]]: [[厂]]
- [[words/古形|古形]]: [[正体]]
- [[words/合|合]]: [[亼]]
- [[words/喚|喚]]: [[奐]]
- [[words/天鼠|天鼠]]: [[飛鼠]]
- [[words/好|好]]: [[子 (char)]]
- [[words/嬴洲|嬴洲]]: [[瀛]]
- [[words/宗徒|宗徒]]: [[行傳]]
- [[words/寝|寝]]: [[牀]]
- [[words/尭舌|尭舌]]: [[饒]]
- [[words/徐様|徐様]]: [[緩慢様]]
- [[words/心理学|心理学]]: [[心理学家]]
- [[words/性質|性質]]: [[個性]]
- [[words/景色|景色]]: [[風景]]
- [[words/楊梅|楊梅]]: [[山桃]]
- [[words/汽車|汽車]]: [[列車]]
- [[words/洗車|洗車]]: [[lexipedia/scratch.md]]
- [[words/混沌|混沌]]: [[混淪]]
- [[words/混沌|混沌]]: [[開天闢地]]
- [[words/火車|火車]]: [[列車]]
- [[words/特点|特点]]: [[特徵]]
- [[words/白頭就|白頭就]]: [[鷲]]
- [[words/盧魚|盧魚]]: [[鱸魚]]
- [[words/神道教|神道教]]: [[仏教]]
- [[words/禁書|禁書]]: [[書經]]
- [[words/第|第]]: [[nav/Numerals]]
- [[words/股|股]]: [[殳]]
- [[words/肥脊|肥脊]]: [[瘠]]
- [[words/肺臓|肺臓]]: [[肺腑]]
- [[words/道|道]]: [[首 (char)]]
- [[words/重畳|重畳]]: [[迂言]]
- [[words/零|零]]: [[nav/Numerals]]
- [[words/龍|龍]]: [[wikilink]]

### [C3] the lexipedia domain page does not link this word (41)

- [[words/䔥国|䔥国]] -> China
- [[words/中原|中原]] -> Geography
- [[words/中央情報局|中央情報局]] -> Geography
- [[words/九州|九州]] -> Geography
- [[words/九龍|九龍]] -> Geography
- [[words/予州|予州]] -> Geography
- [[words/亜細亜|亜細亜]] -> Geography
- [[words/内乱|内乱]] -> Geography
- [[words/分布|分布]] -> Geography
- [[words/協議|協議]] -> Geography
- [[words/商路|商路]] -> Geography
- [[words/地域|地域]] -> Geography
- [[words/地理|地理]] -> Geography
- [[words/地龍|地龍]] -> Animals
- [[words/報応|報応]] -> Law
- [[words/多様|多様]] -> Geography
- [[words/多辺|多辺]] -> Geography
- [[words/大韓民国|大韓民国]] -> Geography
- [[words/媒体|媒体]] -> Geography
- [[words/宇宙観|宇宙観]] -> Geography
- [[words/対外|対外]] -> Geography
- [[words/希州|希州]] -> Geography
- [[words/徐州|徐州]] -> Geography
- [[words/徳|徳]] -> Periodic Table
- [[words/持続|持続]] -> Geography
- [[words/揚州|揚州]] -> Geography
- [[words/東伝|東伝]] -> Geography
- [[words/梁州|梁州]] -> Geography
- [[words/殖民|殖民]] -> Geography
- [[words/漢城|漢城]] -> Geography
- [[words/熱帯|熱帯]] -> Geography
- [[words/珈啡因|珈啡因]] -> Food
- [[words/界水|界水]] -> Geography
- [[words/界線|界線]] -> Geography
- [[words/蘇連|蘇連]] -> Geography
- [[words/要地|要地]] -> Geography
- [[words/語言|語言]] -> Geography
- [[words/資源|資源]] -> Geography
- [[words/邾国|邾国]] -> China
- [[words/雍州|雍州]] -> Geography
- [[words/青州|青州]] -> Geography

### [C3] `lexipedia:` property and the "See" bullets name different domains (13)

- [[words/䔥国|䔥国]]: property ['China'] vs bullets []
- [[words/中原|中原]]: property ['Geography'] vs bullets []
- [[words/中央情報局|中央情報局]]: property ['Geography'] vs bullets []
- [[words/九州|九州]]: property ['China', 'Geography'] vs bullets ['China']
- [[words/九龍|九龍]]: property ['Geography'] vs bullets []
- [[words/予州|予州]]: property ['Geography'] vs bullets []
- [[words/亜細亜|亜細亜]]: property ['Geography', 'Society'] vs bullets ['Society']
- [[words/信条|信条]]: property ['Mind', '信條'] vs bullets ['Mind']
- [[words/傾向|傾向]]: property ['Mind', '倾向'] vs bullets ['Mind']
- [[words/六府|六府]]: property ['Body', '六腑'] vs bullets ['Body']
- [[words/安排|安排]]: property ['Efforts', 'Work'] vs bullets ['Efforts']
- [[words/徳|徳]]: property ['Periodic Table', 'Society'] vs bullets ['Society']
- [[words/邾国|邾国]]: property ['China'] vs bullets []

## Characters, --deep run

The default run checks only pages changed since their own stamp and is clean. `python3 AIOS/scripts/lint_characters.py --deep` checks every page and finds this hidden drift in already-stamped pages.

### [C1] link in a Notes bullet is missing the `../` prefix (176)

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

### [C1] no Classical Chinese / ancient-sound bullet (1)

- [[characters/佤|佤]]

### [C2] word is listed in ## Words without a <ruby> reading (27)

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

### [C2] word using this character is missing from ## Words (1)

- [[characters/蘿|蘿]] -> 女蘿

## Judgment items still open

- **Default words run:** clean and stamped. The words `--deep` run (above) shows the drift in already-stamped pages: C1 56 (no Notes section), C2 87 (unresolved links) and C3 54 (domain placement). The C2 markdown links and the C3 placements on this page's default scope were fixed in bulk; the deep ones are the same kinds of fix.
- **Three words naming a lexipedia domain page that doesn't exist:** [[words/信条|信条]], [[words/傾向|傾向]], [[words/六府|六府]].
- **Sound exceptions (B5, resolved):** 13 words keep a documented divergence from their characters and are exempt via `SOUND_EXCEPTIONS` in `lint_words.py`: 反乱, 就鳥, 海就, 白頭就, 禿就, 得点, 特点, 杜選, 瞻妄, 統率, 率性, 釩金, 蓬藁 (plus 棕枝 and 棕枝主日).
- **`mc_id` drift (characters C3, resolved):** all 24 fixed.
