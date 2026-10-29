---
tags:
  - lookup
date-last-perfect: 2026-10-29
---
# Lint Report

Generated 2026-10-29 from the linters' own output. Every flagged page is a clickable link. Re-run any section with the command shown. Nothing listed here has been fixed.

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
| Characters | `python3 AIOS/scripts/lint_characters.py` | Default run clean; stamped 2026-10-29. `--deep` shows the drift listed below. |
| **Words** | `python3 AIOS/scripts/lint_words.py` | **Fails**: A2 1, A3 2, B1 4, B2 6, B5 310, C1 3, C2 58, C3 22 (snapshot; the sections below list the earlier run) |

## Contents

- [[#Words (lint_words.py)]]
- [[#Characters, --deep run]]
- [[#Judgment items still open]]

## Words (lint_words.py)

Done already this session: the `word` tag (7), " (char)" suffixes on `characters:` entries (198 added, 37 removed), `kwin` (167 + 9), lexipedia "See" bullets (116) and homophone callouts (57). What is left:

### [B2] pos is blank (3)

- [[words/人|人]]
- [[words/名|名]]
- [[words/大食|大食]]

### [B2] pos '形容詞' is not a legal part of speech (3)

- [[words/凸|凸]]
- [[words/拙劣|拙劣]]
- [[words/絢乱|絢乱]]

### [B5] 羅馬字 differs from the characters joined (203)

- [[words/七万|七万]] (citmon vs cidmon)
- [[words/七情|七情]] (citcing vs cidcing)
- [[words/三角法|三角法]] (samgogpab vs samgogfab)
- [[words/不亦V乎|不亦V乎]] (bod'ǝg...ho vs bod'ǝgho)
- [[words/中日韓越|中日韓越]] (jungnithan'wed vs jungnidhan'wed)
- [[words/中華民国|中華民国]] (junghwamingok vs junghwamingog)
- [[words/九九|九九]] (kyukyu vs kyu)
- [[words/事務所|事務所]] (jimusyo vs jimusǝ)
- [[words/二十二日|二十二日]] (niǝsibniǝnid vs niǝsibnid)
- [[words/亜細亜|亜細亜]] ('asei'a vs 'asei)
- [[words/交互|交互]] (gyauho vs gyouho)
- [[words/交付|交付]] (gyaupu vs gyoufu)
- [[words/交叉|交叉]] (gyaucai vs gyoucai)
- [[words/交友|交友]] (gyau'yuo vs gyou'yuo)
- [[words/交尾|交尾]] (gyaumui vs gyoumui)
- [[words/交差|交差]] (gyauca vs gyouca)
- [[words/交情|交情]] (gyaucing vs gyoucing)
- [[words/交接|交接]] (gyaujob vs gyoujob)
- [[words/交換|交換]] (gyauhwam vs gyouhwam)
- [[words/交易|交易]] (gyau'yeg vs gyou'yeg)
- [[words/交流|交流]] (gyaulyu vs gyoulyu)
- [[words/交溝|交溝]] (gyaugou vs gyougou)
- [[words/交点|交点]] (gyaudem vs gyoudem)
- [[words/交通|交通]] (gyautong vs gyoutong)
- [[words/交遊|交遊]] (gyau'yuo vs gyou'yuo)
- [[words/交際|交際]] (gyauje vs gyouje)
- [[words/交響|交響]] (gyauhyang vs gyouhyang)
- [[words/人人|人人]] (ninnin vs nin)
- [[words/仁徳|仁徳]] (nindug vs nintug)
- [[words/仲介|仲介]] (dungye vs dunggye)
- [[words/休息室|休息室]] (hyusiksid vs hyusigsid)
- [[words/伯伯|伯伯]] (bagbag vs bag)
- [[words/低廉|低廉]] (deilye vs deilyem)
- [[words/作坊|作坊]] (jagbang vs jagfang)
- [[words/便宜|便宜]] (byen'wi vs byen'ǝi)
- [[words/俘虜|俘虜]] (pulo vs fulo)
- [[words/倉鼠|倉鼠]] (cangsyo vs cwangsyo)
- [[words/個人|個人]] (ganin vs gǝnin)
- [[words/儀礼|儀礼]] ('wilei vs 'ǝilei)
- [[words/儒教|儒教]] (nugyau vs nugyou)
- [[words/光明|光明]] (gwangmyeng vs kwangmyeng)
- [[words/兌換|兌換]] (dwaihwan vs dwaihwam)
- [[words/兗州|兗州]] ('yengjuo vs 'yenjuo)
- [[words/入籍|入籍]] (nibjek vs nibjeg)
- [[words/兵法|兵法]] (byengpab vs byengfab)
- [[words/凹凸|凹凸]] ('auded vs 'audod)
- [[words/出谷記|出谷記]] (cudgigog vs cudgoggi)
- [[words/分校|分校]] (bunhya vs bunhyau)
- [[words/副用|副用]] (pug'yong vs fug'yong)
- [[words/創傷|創傷]] (cangsyang vs cwangsyang)
- [[words/加沙|加沙]] (kasa vs gasa)
- [[words/加法|加法]] (gapab vs gafab)
- [[words/勃興|勃興]] (bodhing vs bodhǝng)
- [[words/反乱|反乱]] (banlan vs fonlan)
- [[words/反切|反切]] (ponced vs fonced)
- [[words/反哺|反哺]] (ponbo vs fonbo)
- [[words/反応|反応]] (pon'ing vs fon'ing)
- [[words/反映|反映]] (pon'yeng vs fon'yeng)
- [[words/反駁|反駁]] (ponbag vs fonbag)
- [[words/可憐|可憐]] (kalen vs kǝlen)
- [[words/各位|各位]] (gak'wei vs gag'wei)
- [[words/同窓|同窓]] (dongjwang vs dongcwang)
- [[words/哲学|哲学]] (jethag vs jedhag)
- [[words/唐突|唐突]] (dwangdod vs dwangtod)
- [[words/唱和|唱和]] (canghwa vs cwanghwa)
- [[words/嗣子|嗣子]] (sijǝ vs sǝjǝ)
- [[words/回教|回教]] (hoigyau vs hoigyou)
- [[words/回教徒|回教徒]] (hoigyaudo vs hoigyoudo)
- [[words/地方|地方]] (diǝpang vs diǝfang)
- [[words/地球儀|地球儀]] (diǝgyu'wi vs diǝgyu'ǝi)
- [[words/基督教|基督教]] (gidoggyau vs gidoggyou)
- [[words/堕天使|堕天使]] (datensi vs dwatensi)
- [[words/堕胎|堕胎]] (datai vs dwatai)
- [[words/塑膠|塑膠]] (sogyau vs sogyou)
- [[words/外交|外交]] ('waigyau vs 'waigyou)
- [[words/外祖母|外祖母]] ('waijomou vs 'waijǝmou)
- [[words/外祖父|外祖父]] ('waijobu vs 'waijǝbu)
- [[words/多少|多少]] (dasou vs dǝsou)
- [[words/多彩|多彩]] (dacai vs dǝcai)
- [[words/大夫|大夫]] (daibu vs daifǝ)
- [[words/大腿|大腿]] (daitoi vs daitiǝ)
- [[words/大部分|大部分]] (daiboubin vs daiboubun)
- [[words/太太|太太]] (taitai vs tai)
- [[words/夫婦|夫婦]] (bubyu vs fǝbyu)
- [[words/奔放|奔放]] (bonbang vs bonfang)
- [[words/奔騰|奔騰]] (bondung vs bondǝng)
- [[words/奥門|奥門]] ('omon vs 'ugmon)
- [[words/奨励|奨励]] (janle vs jangle)
- [[words/妨害|妨害]] (panghai vs fanghai)
- [[words/姑丈|姑丈]] (gojang vs gocang)
- [[words/嫉妬|嫉妬]] (jitdo vs jiddo)
- [[words/学問|学問]] (hakmun vs hagmun)
- [[words/小冊子|小冊子]] (socakjǝ vs socagjǝ)
- [[words/就鳥|就鳥]] (juocou vs cwaicou)
- [[words/巨大|巨大]] (gyotai vs gyodai)
- [[words/弥勒|弥勒]] (melug vs melǝg)
- [[words/得点|得点]] (dugdem vs tǝgdem)
- [[words/徳国|徳国]] (duggog vs tuggog)
- [[words/性交|性交]] (singgyau vs singgyou)
- [[words/恭喜発財|恭喜発財]] (gyonghifadcai vs gyonghifadjai)
- [[words/感覚|感覚]] (gamgak vs gamgag)
- [[words/憲法|憲法]] (henpab vs henfab)
- [[words/懶惰|懶惰]] (langwa vs landwa)
- [[words/懸垂|懸垂]] (hwensui vs hwenjui)
- [[words/手巾|手巾]] (syugin vs syukin)
- [[words/才能|才能]] (jainung vs jainǝng)
- [[words/振幅|振幅]] (jinpug vs jinfug)
- [[words/控訴|控訴]] (kongsu vs kongso)
- [[words/推測|推測]] (cuicig vs cuicǝg)
- [[words/握窄|握窄]] ('agcag vs 'agjag)
- [[words/放棄|放棄]] (bangkiǝ vs fangkiǝ)
- [[words/放火|放火]] (banghwa vs fanghwa)
- [[words/放物線|放物線]] (bangmudsyen vs fangmudsyen)
- [[words/放置|放置]] (bangci vs fangci)
- [[words/政府|政府]] (jingpu vs jingfu)
- [[words/教室|教室]] (gyausid vs gyousid)
- [[words/教材|教材]] (gyaucai vs gyoucai)
- [[words/明徳|明徳]] (myengdug vs myengtug)
- [[words/明治|明治]] (myengchi vs myengci)
- [[words/木偶|木偶]] (mok'ou vs mog'ou)
- [[words/木曜日|木曜日]] (mok'younid vs mog'younid)
- [[words/本日|本日]] (honnid vs bonnid)
- [[words/杜選|杜選]] (dojyen vs doswen)
- [[words/束縛|束縛]] (syogbag vs syogfag)
- [[words/果汁|果汁]] (gwajib vs gwajǝb)
- [[words/査問|査問]] (juomun vs jamun)
- [[words/校歌|校歌]] (hyauga vs hyaugǝ)
- [[words/根拠|根拠]] (gangyo vs gǝngyo)
- [[words/根本|根本]] (ganbon vs gǝnbon)
- [[words/極右|極右]] (gig'u vs gig'yu)
- [[words/極左|極左]] (gigjwa vs gigja)
- [[words/模倣|模倣]] (mopang vs mofang)
- [[words/正字法|正字法]] (jingjipap vs jingjifab)
- [[words/殺戮|殺戮]] (sadluk vs sadlug)
- [[words/比喩|比喩]] (biǝ'yu vs biǝ'yum)
- [[words/汚染|汚染]] ('onyem vs 'onyom)
- [[words/流域|流域]] (lyuwik vs lyu'wig)
- [[words/海就|海就]] (haijuo vs haicwai)
- [[words/海豚|海豚]] (haidon vs haitun)
- [[words/港湾|港湾]] (hong'wan vs hong'wam)
- [[words/満月|満月]] (man'wet vs man'wed)
- [[words/滋生|滋生]] (jisang vs jǝsang)
- [[words/演奏|演奏]] ('yenjou vs 'yensou)
- [[words/灼熱|灼熱]] (jagned vs jagnyed)
- [[words/災殃|災殃]] (jai'ang vs jai'yang)
- [[words/無名指|無名指]] (mumyengjiǝ vs mǝmingjiǝ)
- [[words/無政府|無政府]] (mǝjingpu vs mǝjingfu)
- [[words/煮沸|煮沸]] (jopud vs jofud)
- [[words/特殊|特殊]] (dugsu vs dǝgsu)
- [[words/特点|特点]] (dugdem vs dǝgdem)
- [[words/特詞|特詞]] (dugsa vs dǝgsa)
- [[words/猪悟能|猪悟能]] (jo'onung vs jo'onǝng)
- [[words/率性|率性]] (sudsing vs ludsing)
- [[words/王妃|王妃]] ('wangpi vs 'wangfi)
- [[words/玻璃|玻璃]] (pale vs palǝ)
- [[words/玻璃版|玻璃版]] (palepan vs palǝpan)
- [[words/理由|理由]] (li'yu vs li'yuo)
- [[words/瑠璃|瑠璃]] (lyule vs lyulǝ)
- [[words/甜瓜|甜瓜]] (demgwa vs dimgwa)
- [[words/甜菜|甜菜]] (demcai vs dimcai)
- [[words/用疽|用疽]] ('yongjo vs 'yongjǝ)
- [[words/疾病|疾病]] (jitbyeng vs jidbyeng)
- [[words/痘痕|痘痕]] (douhan vs douhǝn)
- [[words/白粉|白粉]] (bagbun vs bagfun)
- [[words/白頭就|白頭就]] (bagtoujuo vs bagtoucwai)
- [[words/皮膚|皮膚]] (bipu vs bifǝ)
- [[words/瞻余|瞻余]] (jemjo vs jem'yo)
- [[words/瞻妄|瞻妄]] (semmang vs jemmang)
- [[words/破戒|破戒]] (pegye vs pǝgye)
- [[words/社交|社交]] (syagyau vs syagyou)
- [[words/禿就|禿就]] (togjuo vs togcwai)
- [[words/空隙|空隙]] (konggeg vs kongkeg)
- [[words/系詞|系詞]] (heysa vs heisa)
- [[words/統率|統率]] (tongsud vs tonglud)
- [[words/肩章|肩章]] (gengjang vs genjang)
- [[words/自家|自家]] (jiǝgab vs jiǝga)
- [[words/苹果|苹果]] (byenggwa vs fenggwa)
- [[words/落下傘|落下傘]] (lakhasan vs laghasan)
- [[words/蓬藁|蓬藁]] (bonghau vs bonggau)
- [[words/超越|超越]] (cau'wed vs tau'wed)
- [[words/足裏|足裏]] (jokli vs jogli)
- [[words/輸血|輸血]] (suhwed vs sumhwed)
- [[words/辛苦|辛苦]] (hangko vs sinko)
- [[words/辞退|辞退]] (citoi vs citiǝ)
- [[words/辦理|辦理]] (bangli vs banli)
- [[words/道教|道教]] (daugyau vs daugyou)
- [[words/違反|違反]] ('wipon vs wifon)
- [[words/違法|違法]] ('wipab vs wifab)
- [[words/郵便局|郵便局]] ('uobyengyok vs 'uobyengyog)
- [[words/郵帖|郵帖]] ('uoteb vs 'uotob)
- [[words/鄭重|鄭重]] (cengcong vs jengcong)
- [[words/醜悪|醜悪]] (cu'ag vs cuo'ag)
- [[words/釈放|釈放]] (segbang vs segfang)
- [[words/釉薬|釉薬]] ('yuo'yak vs 'yuo'yag)
- [[words/釩金|釩金]] (vangim vs fangim)
- [[words/開放|開放]] (kaibang vs kaifang)
- [[words/陵墓|陵墓]] (lingmo vs lǝngmo)
- [[words/階段|階段]] (gyedwan vs gyeidwan)
- [[words/雰囲|雰囲]] (pun'wi vs funwi)
- [[words/電子版|電子版]] (denjǝban vs denjǝpan)
- [[words/頭髪|頭髪]] (toubad vs toufad)
- [[words/餃子|餃子]] (gyaujǝ vs gyoujǝ)
- [[words/黼黻|黼黻]] (bupud vs fufud)

### [B5] 諺文 differs from the characters joined (101)

- [[words/三菱|三菱]] (삼링 vs 삼릉)
- [[words/三角法|三角法]] (삼곡팝 vs 삼곡빱)
- [[words/不亦V乎|不亦V乎]] (볻윽...호 vs 볻윽호)
- [[words/中央|中央]] (중앙 vs 중양)
- [[words/九九|九九]] (큐큐 vs 큐)
- [[words/二十二日|二十二日]] (늬십늬닏 vs 늬십닏)
- [[words/五常|五常]] (오양 vs 오샹)
- [[words/亜細亜|亜細亜]] (아세아 vs 아세)
- [[words/交情|交情]] (걋칭 vs 굣칭)
- [[words/交際|交際]] (걋저 vs 굣저)
- [[words/人人|人人]] (닌닌 vs 닌)
- [[words/伯伯|伯伯]] (박박 vs 박)
- [[words/俘虜|俘虜]] (푸로 vs 뿌로)
- [[words/偽善|偽善]] (워션 vs 웨션)
- [[words/儀礼|儀礼]] (위레 vs 읫레)
- [[words/儒教|儒教]] (누걋 vs 누굣)
- [[words/光明|光明]] (광명 vs 쾅명)
- [[words/兌換|兌換]] (돼환 vs 돼홤)
- [[words/兵法|兵法]] (병팝 vs 병빱)
- [[words/凹凸|凹凸]] (앗덛 vs 앗돋)
- [[words/出谷記|出谷記]] (춛기곡 vs 춛곡기)
- [[words/副用|副用]] (푹용 vs 뿍용)
- [[words/反乱|反乱]] (반란 vs 뽄란)
- [[words/反切|反切]] (폰첟 vs 뽄첟)
- [[words/反哺|反哺]] (폰보 vs 뽄보)
- [[words/反応|反応]] (폰잉 vs 뽄잉)
- [[words/反映|反映]] (폰영 vs 뽄영)
- [[words/反駁|反駁]] (폰박 vs 뽄박)
- [[words/呻吟|呻吟]] (신움 vs 신음)
- [[words/嗣子|嗣子]] (시지 vs 스즈)
- [[words/圓滑|圓滑]] (원활 vs 원홛)
- [[words/城郭|城郭]] (싱광 vs 싱곽)
- [[words/基督教|基督教]] (기독걋 vs 기독굣)
- [[words/塑膠|塑膠]] (소걋 vs 소굣)
- [[words/外交|外交]] (왜걋 vs 왜굣)
- [[words/外祖母|外祖母]] (왜조못 vs 왜즈못)
- [[words/外祖父|外祖父]] (왜조부 vs 왜즈부)
- [[words/多彩|多彩]] (다채 vs 드채)
- [[words/大夫|大夫]] (대부 vs 대쁘)
- [[words/太太|太太]] (태태 vs 태)
- [[words/夫婦|夫婦]] (부뷰 vs 쁘뷰)
- [[words/奥門|奥門]] (오몬 vs 욱몬)
- [[words/妨害|妨害]] (팡해 vs 빵해)
- [[words/姑丈|姑丈]] (고장 vs 고창)
- [[words/就鳥|就鳥]] (줏촛 vs 쵀촛)
- [[words/得点|得点]] (둑덤 vs 특덤)
- [[words/徳国|徳国]] (둑곡 vs 툭곡)
- [[words/性交|性交]] (싱걋 vs 싱굣)
- [[words/恭喜発財|恭喜発財]] (굥히빧채 vs 굥히빧재)
- [[words/憲法|憲法]] (헌팝 vs 헌빱)
- [[words/手巾|手巾]] (슈긴 vs 슈킨)
- [[words/握窄|握窄]] (악착 vs 악작)
- [[words/放棄|放棄]] (방킈 vs 빵킈)
- [[words/放火|放火]] (방화 vs 빵화)
- [[words/放物線|放物線]] (방묻션 vs 빵묻션)
- [[words/放置|放置]] (방치 vs 빵치)
- [[words/明徳|明徳]] (명둑 vs 명툭)
- [[words/星条旗|星条旗]] (성조기 vs 성조키)
- [[words/有机|有机]] (우긔 vs 유긔)
- [[words/本日|本日]] (혼닏 vs 본닏)
- [[words/杜選|杜選]] (도젼 vs 도숸)
- [[words/束縛|束縛]] (쇽박 vs 쇽빡)
- [[words/極右|極右]] (긱우 vs 긱유)
- [[words/極左|極左]] (긱좌 vs 긱자)
- [[words/正字法|正字法]] (징지팝 vs 징지빱)
- [[words/水泳|水泳]] (수욍 vs 수윙)
- [[words/汚染|汚染]] (온염 vs 오뇸)
- [[words/海就|海就]] (해줏 vs 해쵀)
- [[words/演奏|演奏]] (연좃 vs 연솟)
- [[words/災殃|災殃]] (재앙 vs 재양)
- [[words/煮沸|煮沸]] (조푿 vs 조뿓)
- [[words/特点|特点]] (둑덤 vs 득덤)
- [[words/特詞|特詞]] (둑사 vs 득사)
- [[words/率性|率性]] (수싱 vs 룯싱)
- [[words/玻璃|玻璃]] (파러 vs 파르)
- [[words/玻璃版|玻璃版]] (파러판 vs 파르판)
- [[words/理由|理由]] (리유 vs 리윳)
- [[words/用疽|用疽]] (용조 vs 용즈)
- [[words/申告|申告]] (성갓 vs 선갓)
- [[words/白粉|白粉]] (박분 vs 박뿐)
- [[words/白頭就|白頭就]] (박톳줏 vs 박톳쵀)
- [[words/白頭翁|白頭翁]] (박톳웅 vs 박톳옹)
- [[words/皮膚|皮膚]] (비푸 vs 비쁘)
- [[words/瞻妄|瞻妄]] (섬망 vs 점망)
- [[words/社交|社交]] (샤걋 vs 샤굣)
- [[words/禿就|禿就]] (톡줏 vs 톡쵀)
- [[words/統率|統率]] (통숟 vs 통룯)
- [[words/自家|自家]] (즤갑 vs 즤가)
- [[words/苹果|苹果]] (병과 vs 뻥과)
- [[words/蓬藁|蓬藁]] (봉핫 vs 봉갓)
- [[words/輸血|輸血]] (수훧 vs 숨훧)
- [[words/辞退|辞退]] (치퇴 vs 치틔)
- [[words/辦理|辦理]] (방리 vs 반리)
- [[words/道教|道教]] (닷걋 vs 닷굣)
- [[words/違反|違反]] (위폰 vs 위뽄)
- [[words/違法|違法]] (위팝 vs 위빱)
- [[words/郵帖|郵帖]] (웃텁 vs 웃톱)
- [[words/釈放|釈放]] (석방 vs 석빵)
- [[words/釩金|釩金]] (반김 vs 빤김)
- [[words/雰囲|雰囲]] (푼위 vs 뿐위)
- [[words/頭髪|頭髪]] (톳받 vs 톳빧)

### [B5] 注音 differs from the characters joined (24)

- [[words/九九|九九]] (ㄎ⼜·ㄎ⼜ vs ㄎ⼜)
- [[words/二十二日|二十二日]] (ㄋㄧㄜㄙㄧㄆㄋㄧㄜㄋㄧㄊ vs ㄋㄧㄜㄙㄧㄆㄋㄧㄊ)
- [[words/亜細亜|亜細亜]] (ㄚㄙㄝㄧ·ㄚ vs ㄚㄙㄝㄧ)
- [[words/人人|人人]] (ㄋㄧㄋㄋㄧㄋ vs ㄋㄧㄋ)
- [[words/伯伯|伯伯]] (ㄅㄚㄎㄅㄚㄎ vs ㄅㄚㄎ)
- [[words/反乱|反乱]] (ㄅㄚㄋㄌㄚㄋ vs ㄈㄛㄋㄌㄚㄋ)
- [[words/大夫|大夫]] (ㄉㄚㄧㄅㄨ vs ㄉㄚㄧㄈㄜ)
- [[words/太太|太太]] (ㄊㄚㄧㄊㄚㄧ vs ㄊㄚㄧ)
- [[words/夫婦|夫婦]] (ㄅㄨㄅ⼜ vs ㄈㄜㄅ⼜)
- [[words/就鳥|就鳥]] (ㄐㄨㄛㄑㄛㄨ vs ㄑ⺢ㄧㄑㄛㄨ)
- [[words/弥勒|弥勒]] (ㄇㄝㄌㄨㄎ vs ㄇㄝㄌㄜㄎ)
- [[words/得点|得点]] (ㄉㄨㄎㄉㄝㄇ vs ㄊㄜㄎㄉㄝㄇ)
- [[words/杜選|杜選]] (ㄉㄛㄐ⼶ㄋ vs ㄉㄛㄙ⼔ㄋ)
- [[words/海就|海就]] (ㄏㄚㄧ·ㄐㄨㄛ vs ㄏㄚㄧㄑ⺢ㄧ)
- [[words/特点|特点]] (ㄉㄨㄎㄉㄝㄇ vs ㄉㄜㄎㄉㄝㄇ)
- [[words/率性|率性]] (ㄙㄨㄙㄧㄫ vs ㄌㄨㄊㄙㄧㄫ)
- [[words/理由|理由]] (ㄌㄧ·⼜ vs ㄌㄧ⼜ㄛ)
- [[words/白頭就|白頭就]] (ㄅㄚㄎㄊㄛㄨㄐㄨㄛ vs ㄅㄚㄎㄊㄛㄨㄑ⺢ㄧ)
- [[words/瞻妄|瞻妄]] (ㄙㄝㄇㄇㄚㄫ vs ㄐㄝㄇㄇㄚㄫ)
- [[words/禿就|禿就]] (ㄊㄛㄎㄐㄨㄛ vs ㄊㄛㄎㄑ⺢ㄧ)
- [[words/統率|統率]] (ㄊㄛㄫㄙㄨㄊ vs ㄊㄛㄫㄌㄨㄊ)
- [[words/自家|自家]] (ㄐㄧㄜㄍㄚㄆ vs ㄐㄧㄜㄍㄚ)
- [[words/蓬藁|蓬藁]] (ㄅㄛㄫㄏㄚㄨ vs ㄅㄛㄫㄍㄚㄨ)
- [[words/釩金|釩金]] (ㄪㄚㄋㄍㄧㄇ vs ㄈㄚㄋㄍㄧㄇ)

### [C1] no `## Notes` section (3)

- [[words/爺爺|爺爺]]
- [[words/特殊|特殊]]
- [[words/甲|甲]]

### [C2] a markdown link does not resolve (45)

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
- [[words/広東|広東]]: ../characters/広.md
- [[words/広東|広東]]: ../words/東.md
- [[words/打撃|打撃]]: ../characters/撃.md
- [[words/撞球|撞球]]: ../characters/撞.md
- [[words/火山島|火山島]]: ../characters/山.md
- [[words/火山島|火山島]]: ../characters/島.md
- [[words/火星|火星]]: ../characters/星.md
- [[words/灰塵|灰塵]]: ../characters/灰.md
- [[words/疑問|疑問]]: ../words/疑.md
- [[words/硬口蓋|硬口蓋]]: ../words/蓋.md
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

### [C2] a [[wikilink]] does not resolve (13)

- [[words/安慰|安慰]]: [[紹介]]
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

### [C3] the lexipedia domain page does not link this word (21)

- [[words/兗州|兗州]] -> [[lexipedia/Geography|Geography]]
- [[words/北海|北海]] -> [[lexipedia/Geography|Geography]]
- [[words/四海|四海]] -> [[lexipedia/Geography|Geography]]
- [[words/地図学|地図学]] -> [[lexipedia/Geography|Geography]]
- [[words/基金|基金]] -> [[lexipedia/Geography|Geography]]
- [[words/密度|密度]] -> [[lexipedia/Geography|Geography]]
- [[words/拡散|拡散]] -> [[lexipedia/Geography|Geography]]
- [[words/毅然|毅然]] -> [[lexipedia/Mind|Mind]]
- [[words/王畿|王畿]] -> [[lexipedia/Geography|Geography]]
- [[words/理由|理由]] -> [[lexipedia/Knowledge|Knowledge]]
- [[words/環状|環状]] -> [[lexipedia/Geography|Geography]]
- [[words/甄選|甄選]] -> [[lexipedia/Mind|Mind]]
- [[words/真摯|真摯]] -> [[lexipedia/Mind|Mind]]
- [[words/粒子|粒子]] -> [[lexipedia/Physics|Physics]]
- [[words/自閉|自閉]] -> [[lexipedia/Mind|Mind]]
- [[words/航路|航路]] -> [[lexipedia/Geography|Geography]]
- [[words/荊州|荊州]] -> [[lexipedia/Geography|Geography]]
- [[words/西海|西海]] -> [[lexipedia/Geography|Geography]]
- [[words/観察|観察]] -> [[lexipedia/Mind|Mind]]
- [[words/言及|言及]] -> [[lexipedia/Mind|Mind]]
- [[words/鎬京|鎬京]] -> [[lexipedia/China|China]]

### [C3] `lexipedia:` property and the "See" bullets name different domains (1)

- [[words/四海|四海]]: property ['China', 'Geography'] vs bullets ['China']

## Characters, --deep run

The default run checks only pages changed since their own stamp and is clean. `python3 AIOS/scripts/lint_characters.py --deep` checks all 3,373 and finds this hidden drift in already-stamped pages.

### [C1] link in a Notes bullet is missing the `../` prefix (178)

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
- [[characters/攘|攘]]
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

### [C1] Stroke link is not its zero-padded Stroke page (e.g. Stroke%2004) (69)

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
- [[characters/显|显]]
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

### [C1] SKIP bullet does not link the SKIP leaf of its skip_number (1)

- [[characters/显|显]]

### [C2] word is listed in ## Words without a <ruby> reading (29)

- [[characters/噸 (char)|噸 (char)]] -> [[words/噸|噸]]
- [[characters/坪 (char)|坪 (char)]] -> [[words/坪|坪]]
- [[characters/壅 (char)|壅 (char)]] -> [[words/壅|壅]]
- [[characters/嫡 (char)|嫡 (char)]] -> [[words/嫡|嫡]]
- [[characters/嫩 (char)|嫩 (char)]] -> [[words/嫩|嫩]]
- [[characters/屁 (char)|屁 (char)]] -> [[words/屁|屁]]
- [[characters/幟 (char)|幟 (char)]] -> [[words/幟|幟]]
- [[characters/慧 (char)|慧 (char)]] -> [[words/慧|慧]]
- [[characters/憫 (char)|憫 (char)]] -> [[words/憫|憫]]
- [[characters/撮 (char)|撮 (char)]] -> [[words/撮|撮]]
- [[characters/擬 (char)|擬 (char)]] -> [[words/擬|擬]]
- [[characters/晒 (char)|晒 (char)]] -> [[words/晒|晒]]
- [[characters/槍 (char)|槍 (char)]] -> [[words/槍|槍]]
- [[characters/毫 (char)|毫 (char)]] -> [[words/毫米|毫米]]
- [[characters/潰 (char)|潰 (char)]] -> [[words/潰|潰]]
- [[characters/牌 (char)|牌 (char)]] -> [[words/牌|牌]]
- [[characters/矣 (char)|矣 (char)]] -> [[words/矣|矣]]
- [[characters/碼 (char)|碼 (char)]] -> [[words/碼|碼]]
- [[characters/繰 (char)|繰 (char)]] -> [[words/繰|繰]]
- [[characters/肴 (char)|肴 (char)]] -> [[words/肴|肴]]
- [[characters/蘿|蘿]] -> [[words/女蘿|女蘿]]
- [[characters/跨 (char)|跨 (char)]] -> [[words/跨|跨]]
- [[characters/蹲 (char)|蹲 (char)]] -> [[words/蹲|蹲]]
- [[characters/輿 (char)|輿 (char)]] -> [[words/輿|輿]]
- [[characters/鋸 (char)|鋸 (char)]] -> [[words/鋸|鋸]]
- [[characters/錮 (char)|錮 (char)]] -> [[words/錮|錮]]
- [[characters/鍬 (char)|鍬 (char)]] -> [[words/鍬|鍬]]
- [[characters/鍾 (char)|鍾 (char)]] -> [[words/鍾|鍾]]
- [[characters/魂 (char)|魂 (char)]] -> [[words/魂|魂]]

### [C2] ruby reading in ## Words differs from the word's 注音 (24)

- [[characters/俗 (char)|俗 (char)]] -> [[words/習俗|習俗]] (ㄙㄧㄆㄙㄛㄎ vs ㄙㄜㄆㄙㄛㄎ)
- [[characters/命|命]] -> [[words/命令|命令]] (ㄇ⼶ㄫㄌㄚㄫ vs ㄇ⼶ㄫㄌㄝㄫ)
- [[characters/天 (char)|天 (char)]] -> [[words/天子|天子]] (ㄊㄝㄋㄐㄧ vs ㄊㄝㄋㄐㄜ)
- [[characters/天 (char)|天 (char)]] -> [[words/天道|天道]] (ㄊㄝㄋㄙㄚㄨ vs ㄊㄝㄋㄉㄚㄨ)
- [[characters/就 (char)|就 (char)]] -> [[words/就|就]] (ㄐㄨㄛ vs ㄑ⺢ㄧ)
- [[characters/尺 (char)|尺 (char)]] -> [[words/尺蠖|尺蠖]] (ㄑㄝㄎㄏ⺢ㄎ vs ㄑㄝㄎ·⺢ㄎ)
- [[characters/思|思]] -> [[words/思議|思議]] (ㄙㄚ·ㄨㄧ vs ㄙㄚㄜㄧ)
- [[characters/患 (char)|患 (char)]] -> [[words/罹患|罹患]] (ㄌㄧㄏ⼘ㄋ vs ㄌㄧㄏ⺢ㄇ)
- [[characters/悼 (char)|悼 (char)]] -> [[words/哀悼|哀悼]] (ㄚㄋㄙㄚㄨ vs ㄚㄧㄉㄚㄨ)
- [[characters/愚 (char)|愚 (char)]] -> [[words/下愚|下愚]] (ㄏㄚㄨ vs ㄏㄚ·ㄨ)
- [[characters/愛 (char)|愛 (char)]] -> [[words/恩愛|恩愛]] (ㄚㄋ·ㄚㄧ vs ㄜㄋ·ㄚㄧ)
- [[characters/授|授]] -> [[words/教授|教授]] (ㄍ⼘ㄨㄙ⼜ vs ㄍ⼄ㄨㄙ⼜)
- [[characters/揄|揄]] -> [[words/揶揄|揶揄]] (⼘·⼜ vs ⼘⼜ㄇ)
- [[characters/整 (char)|整 (char)]] -> [[words/整理|整理]] (ㄐㄝㄫㄐㄧ vs ㄐㄝㄫㄌㄧ)
- [[characters/方|方]] -> [[words/方言|方言]] (ㄆㄚㄫ·ㄝㄋ vs ㄈㄚㄫㄝㄋ)
- [[characters/月 (char)|月 (char)]] -> [[words/正月|正月]] (ㄍㄧㄫ·⼔ㄊ vs ㄐㄧㄫ⼔ㄊ)
- [[characters/正 (char)|正 (char)]] -> [[words/正月|正月]] (ㄍㄧㄫ·⼔ㄊ vs ㄐㄧㄫ⼔ㄊ)
- [[characters/法 (char)|法 (char)]] -> [[words/法則|法則]] (ㄈㄚㄆㄐㄜㄎ vs ㄈㄚㄆㄐㄨㄎ)
- [[characters/癒|癒]] -> [[words/癒合|癒合]] (⼜ㄎㄚㄆ vs ⼜ㄍㄛㄆ)
- [[characters/芬|芬]] -> [[words/芬蘭|芬蘭]] (ㄆㄨㄋㄌㄚㄋ vs ㄈㄨㄋㄌㄚㄋ)
- [[characters/蘭|蘭]] -> [[words/芬蘭|芬蘭]] (ㄆㄨㄋㄌㄚㄋ vs ㄈㄨㄋㄌㄚㄋ)
- [[characters/言 (char)|言 (char)]] -> [[words/方言|方言]] (ㄆㄚㄫ·ㄝㄋ vs ㄈㄚㄫㄝㄋ)
- [[characters/霜 (char)|霜 (char)]] -> [[words/星霜|星霜]] (ㄙㄝㄋㄙ⺢ㄫ vs ㄙㄝㄫㄙ⺢ㄫ)
- [[characters/駁|駁]] -> [[words/反駁|反駁]] (ㄆㄛㄋㄅㄚㄎ vs ㄈㄛㄋㄅㄚㄎ)

### [C2] word using this character is missing from ## Words (11)

- [[characters/墊 (char)|墊 (char)]] -> [[words/墊|墊]]
- [[characters/字 (char)|字 (char)]] -> [[words/別字|別字]]
- [[characters/字 (char)|字 (char)]] -> [[words/単字|単字]]
- [[characters/字 (char)|字 (char)]] -> [[words/字庫|字庫]]
- [[characters/字 (char)|字 (char)]] -> [[words/字形|字形]]
- [[characters/字 (char)|字 (char)]] -> [[words/旧字体|旧字体]]
- [[characters/字 (char)|字 (char)]] -> [[words/用字|用字]]
- [[characters/暴 (char)|暴 (char)]] -> [[words/暴|暴]]
- [[characters/難|難]] -> [[words/難金|難金]]
- [[characters/麻|麻]] -> [[words/大麻|大麻]]
- [[characters/麻|麻]] -> [[words/麻雀鳥|麻雀鳥]]

### [C2] ## Words links a word that has no file (3)

- [[characters/魶 (char)|魶 (char)]] -> words/魶
- [[characters/鱏 (char)|鱏 (char)]] -> words/鱏

### [C3] mc_id differs from the lookup/CC list (24)

- [[characters/俯|俯]] — mc_id 2049 but lookup/CC lists it at 2050
- [[characters/刪|刪]] — mc_id 3588 but lookup/CC lists it at 3589
- [[characters/台 (char)|台 (char)]] — mc_id 840 but lookup/CC lists it at 1973
- [[characters/吝|吝]] — mc_id 2687 but lookup/CC lists it at 2869
- [[characters/啖|啖]] — mc_id 2103 but lookup/CC lists it at 3808
- [[characters/喬|喬]] — mc_id 1974 but lookup/CC lists it at 1975
- [[characters/塵|塵]] — mc_id 1906 but lookup/CC lists it at 1907
- [[characters/岡|岡]] — mc_id 3783 but lookup/CC lists it at 3784
- [[characters/希|希]] — mc_id 3110 but lookup/CC lists it at 1750
- [[characters/従 (char)|従 (char)]] — mc_id 85 but lookup/CC lists it at 2390
- [[characters/攘|攘]] — mc_id 644 but lookup/CC lists it at 1944
- [[characters/檀|檀]] — mc_id 2364 but lookup/CC lists it at 2365
- [[characters/洩|洩]] — mc_id 1300 but lookup/CC lists it at 2745
- [[characters/猿|猿]] — mc_id 3524 but lookup/CC lists it at 3525
- [[characters/稼|稼]] — mc_id 4658 but lookup/CC lists it at 1658
- [[characters/範|範]] — mc_id 940 but lookup/CC lists it at 2424
- [[characters/糟|糟]] — mc_id 2730 but lookup/CC lists it at 2731
- [[characters/糸|糸]] — mc_id 1392 but lookup/CC lists it at 1812
- [[characters/絞|絞]] — mc_id 2636 but lookup/CC lists it at 2637
- [[characters/網 (char)|網 (char)]] — mc_id 2014 but lookup/CC lists it at 2015
- [[characters/舛|舛]] — mc_id 3936 but lookup/CC lists it at 3937
- [[characters/花|花]] — mc_id 2952 but lookup/CC lists it at 2953
- [[characters/賛|賛]] — mc_id 1316 but lookup/CC lists it at 3534
- [[characters/酋|酋]] — mc_id 6579 but lookup/CC lists it at 2791

## Judgment items still open

- **Words listed under a lexipedia domain whose page doesn't link them (C3 above):** add the word to the domain page, or drop the placement. Across the whole corpus there are 63.
- **Three words naming a lexipedia domain page that doesn't exist:** [[words/信条|信条]], [[words/傾向|傾向]], [[words/六府|六府]].
- **Stale readings (B5):** a word's 羅馬字, 諺文 or 注音 differs from its characters. The character is the authority, so the word is stale, except documented stand-ins such as [[words/棕枝|棕枝]] (which reads 枝 as 櫚). Fixing a 注音 also means updating the cached rubies on character, lexipedia and lookup pages.
- **Alias glyphs listed as characters:** [[words/神霊|神霊]] lists 神靈 and 神灵 in `characters:`.
- **Filename vs characters (A3):** two alias-glyph words, [[words/土着|土着]] and [[words/神霊|神霊]].
