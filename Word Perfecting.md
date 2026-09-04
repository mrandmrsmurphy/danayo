# Word Perfecting

Running log for the word-perfecting backlog sweep (see [[AIOS/checklists/checklist_words.md|Checklist: Word Pages]]). The prior log (iterations 1–1040) grew to ~8,500 lines and was archived by the user to `Word Perfecting.md.zip`; a second log (iterations 1041–1782) grew large in turn and was archived to `Word Perfecting 2.md.zip`. This file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one word per iteration (per standing pacing preference). Find the next candidate via `grep -L "^date-last-perfect" words/*.md`, sorted alphabetically by filename (Unicode/`LC_ALL=C` order), continuing from the last-processed filename's position in that sort. Check the word's own `characters:` constituents for a `stand_in` match (add the stand-in note if so), verify `羅馬字`/`諺文`/`注音` are the correct concatenation of each constituent's own fields, verify `kwin` via the AND-rule (all constituents' own `kwin` must be `true` for the compound to be `true`), fill blank cross-linguistic fields only when a real value can be verified (leave deliberately blank with a reason otherwise), and check for genuine Dan'a'yo-level homophones (not just same-spelling coincidences in a real language) before stamping `date-last-perfect`.

Next: 掏摸.

### 2026-08-30, iteration 1783 — [[words/掏摸|掏摸]]

This word is itself the stand-in for its own character (摸 remains pageless in this vault). Fixed missing space in `cantonese`. Filled blank `vietnamese: đào mô` (compositional, 摸's half inferred from phonetic component 莫). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 排水溝.

### 2026-08-30, iteration 1784 — [[words/排水溝|排水溝]]

No stand-in relationship (all three characters' own stand-ins are themselves). Filled blank `vietnamese: bài thuỷ câu` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 掘.

### 2026-08-30, iteration 1785 — [[words/掘|掘]]

This word is itself the stand-in for its own character. Fixed real bug: literal `vietnamese: null`, corrected to quật. Filled blank `pos`/`japanese`/`hsk_level`. No word-level homophones (堀 is name-only). Stamped `date-last-perfect: 2026-08-30`.

Next: 掛.

### 2026-08-30, iteration 1786 — [[words/掛|掛]] (completing homophone with [[卦]])

掛 was malformed (literal `vietnamese: null`, missing pos/japanese/hsk_level). This word is itself the stand-in for its own character. Completed the reciprocal homophone callout with 卦 (both 注音 ㄍ⺢ㄧ), which had already anticipated this pairing from its own earlier turn; also fixed callout spacing and removed a redundant `品詞` on 卦's page. Both stamped `date-last-perfect: 2026-08-30`.

Next: 採取.

### 2026-08-30, iteration 1787 — [[words/採取|採取]]

No stand-in relationship (採's own stand-in is [[採集]]; 取's own is [[取得]]). Filled blank `vietnamese: thái thủ` (a genuine standard term), omitted blank `swadesh`/`aliases`, rewrote `## Etymology` as `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 採用.

### 2026-08-30, iteration 1788 — [[words/採用|採用]]

No stand-in relationship (採's own stand-in is [[採集]]; 用's own is [[使用]]). Filled blank `vietnamese: thái dụng` (compositional), quoted `hsk_level`, omitted blank `swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 採集.

### 2026-08-30, iteration 1789 — [[words/採集|採集]] / [[words/菜汁|菜汁]]

Fixed a significant contamination bug: 菜汁's `諺文`/`羅馬字`/`注音` had all been copied from 集's reading (채집/caijib/ㄑㄚㄧㄐㄧㄆ) instead of its actual constituent 汁's own reading (즙/jǝb/ㄐㄜㄆ) — corrected to 채즙/caijǝb/ㄑㄚㄧㄐㄜㄆ. This invalidated a false homophone claim both pages carried against each other (they only coincided because of the contamination, since 採's and 菜's own readings happen to both be cai/채/ㄑㄚㄧ) — removed from both sides; no genuine homophone exists at either corrected reading. 採集 is itself the stand-in for 採 (集's own stand-in is [[集合]]); 菜汁 has no stand-in relationship (菜's own is [[野菜]]; 汁's own is itself). Filled all of 採集's previously-blank cross-linguistic fields (mandarin/cantonese/japanese/korean/vietnamese). Documented 菜汁's Japanese/Korean as native/loanword compounds (expected). Both stamped `date-last-perfect: 2026-08-30`.

Next: 探索.

### 2026-08-30, iteration 1790 — [[words/探索|探索]]

This word is itself the stand-in that legitimizes the character 探 (索's own stand-in is [[捜索]]). Fixed missing space in `cantonese`. Filled blank `vietnamese: thám sách` (a genuine standard term), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接.

### 2026-08-30, iteration 1791 — [[words/接|接]]

This word is itself the stand-in for its own character. Fixed real bug: literal `vietnamese: null`, corrected to tiếp. Filled blank `pos`/`japanese`/`hsk_level`, normalized the tip callout to canonical form. No word-level homophones (輒 is name-only). Stamped `date-last-perfect: 2026-08-30`.

Next: 接受.

### 2026-08-30, iteration 1792 — [[words/接受|接受]]

This word is itself the stand-in that legitimizes the character 受 (接's own stand-in is itself). Omitted blank `hsk_level`/`swadesh`/`aliases`, rewrote `## Etymology` as `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接吻.

### 2026-08-30, iteration 1793 — [[words/接吻|接吻]]

This word is itself the stand-in that legitimizes the character 吻 (接's own stand-in is itself). Simplified `korean` from a native/loanword dump (뽀뽀, 키스) to compositional 접문, moved colloquial forms to prose. Vietnamese hôn (native) documented as expected. Omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接尾辞.

### 2026-08-30, iteration 1794 — [[words/接尾辞|接尾辞]]

No stand-in relationship (接/尾's own are themselves; 辞's own is [[辞職]]). Page was already richly documented explaining why `mandarin`/`cantonese` are deliberately blank (Sinitic branch doesn't use this formation); added the same reasoning for `vietnamese` (hậu tố is a structural calque, not a Hán Việt reading of this form). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接続助詞.

### 2026-08-30, iteration 1795 — [[words/接続助詞|接続助詞]]

No stand-in relationship (all four characters' own stand-ins point elsewhere). Filled blank `korean: 접속조사` (a real established linguistics term, compositional); left `mandarin`/`cantonese`/`vietnamese` deliberately blank with reasoning (no directly corresponding grammatical category), functionally noted as synonymous with [[連接詞]]. Fixed unindented `characters` list, reformatted inline-flow `aliases`, converted loose body line into proper `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接線.

### 2026-08-30, iteration 1796 — [[words/接線|接線]]

No stand-in relationship (接's own stand-in is itself; 線's own is [[直線]]). Fixed real bug: `mandarin` was contaminated with qiēxiàn (the reading of the near-synonym Chinese term 切線/切线, using 切 rather than 接) — corrected to compositional jiēxiàn. Removed mismatched-character `切線`/`切线` from `aliases` (a distinct compound, the more common Chinese-convention term for the same concept). Filled blank `cantonese`/`korean`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接触.

### 2026-08-30, iteration 1797 — [[words/接触|接触]]

This word is itself the stand-in that legitimizes the character 触 (接's own stand-in is itself). Fixed unindented `characters` list, reformatted inline-flow `aliases`, omitted blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接辞.

### 2026-08-30, iteration 1798 — [[words/接辞|接辞]]

No stand-in relationship (接's own stand-in is itself; 辞's own is [[辞職]]). Fixed real bug (same pattern as [[接線]]): `mandarin`/`cantonese` had been contaminated with the readings of the near-synonym term 詞綴/词缀 (using different characters entirely) instead of compositional jiēcí/zip3 ci4. Removed mismatched-character `詞綴`/`词缀`/`輔素` from `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 接近.

### 2026-08-30, iteration 1799 — [[words/接近|接近]]

No stand-in relationship (both 接 and 近's own stand-ins are themselves). Fixed real bug: `vietnamese` typo (iếp cận→tiếp cận, missing initial "t"). Removed redundant `品詞`, empty-string `swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 控訴.

### 2026-08-30, iteration 1800 — [[words/控訴|控訴]]

This word is itself the stand-in for its own character. Fixed real bug: `cantonese` was missing a letter (hun3→hung3). Filled blank `vietnamese: khống tố` (a genuine standard legal term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 推.

### 2026-08-30, iteration 1801 — [[words/推|推]] / [[words/炊|炊]] (completing three-way homophone with [[吹]])

Both 推 and 炊 were malformed (literal `vietnamese: null`, missing pos/japanese/hsk_level) and both are the stand-ins for their own characters. Completed the three-way Dan'a'yo homophone group (all cui/취/ㄑㄨㄧ) that 吹 had already anticipated from its own earlier turn — added canonical reciprocal callouts to all three pages and fixed 吹's callout spacing. Checked six other candidate characters (嘴/椎/翠/聚/錘) and confirmed none independent at this reading. All three stamped/updated `date-last-perfect: 2026-08-30`.

Next: 推測.

### 2026-08-30, iteration 1802 — [[words/推測|推測]]

No stand-in relationship (推's own stand-in is itself; 測's own is [[測量]]). Fixed `vietnamese`: was a native paraphrase ("đoán ra, nghĩ ra") instead of the Hán Việt compositional reading — corrected to suy trắc. Reformatted inline-flow `characters`/`aliases`, omitted blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 推薦.

### 2026-08-30, iteration 1803 — [[words/推薦|推薦]]

This word is itself the stand-in that legitimizes the character 薦 (推's own stand-in is itself). Filled blank `vietnamese: suy tiến` (compositional), omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 措置.

### 2026-08-30, iteration 1804 — [[words/措置|措置]]

This word is itself the stand-in for its own character (a synonym compound with 置). Fixed unindented `characters` list and missing "(char)" suffix, quoted `cantonese`, omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 掲.

### 2026-08-30, iteration 1805 — [[words/掲|掲]]

This word is itself the stand-in for its own character. Filled blank `pos`/`japanese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 掻.

### 2026-08-30, iteration 1806 — [[words/掻|掻]] / [[words/騒|騒]]

騒 was malformed (empty `品詞`/`pos`, blank `vietnamese`); both words are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄙㄚㄨ) — checked five other candidates (嫂/愁/掃/燥/驟) and confirmed none independent at this reading. 騒's `vietnamese` (tao) required going outside the character's own stored (blank) field — flagged for future character-level check. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 揄伽.

### 2026-08-30, iteration 1807 — [[words/揄伽|揄伽]]

No stand-in relationship (揄's own stand-in is [[揶揄]]; 伽's own is name-only, used here as a common-noun exception). This vault's rendering of the Buddhist loanword 瑜伽 ("yoga"), substituting the phonetically identical 揄 for 瑜 (which coincidentally shares its reading across every language, so no avoided-character documentation was needed beyond the substitution). Fixed real bug: `諺文`/`羅馬字` had dropped 揄's own coda (윰/yum→유/yu), corrected to match the already-correct 注音. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 提案.

### 2026-08-30, iteration 1808 — [[words/提案|提案]]

This word is itself the stand-in that legitimizes the character 案 (提's own stand-in is [[提示]]). Filled blank `vietnamese: chề án` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 提示.

### 2026-08-30, iteration 1809 — [[words/提示|提示]]

This word is itself the stand-in that legitimizes the character 提 (示's own stand-in is [[開示]]). Filled blank `vietnamese: chề thị` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 揚.

### 2026-08-30, iteration 1810 — [[words/揚|揚]] / [[words/陽|陽]] (completing three-way homophone with [[様]])

揚 and 陽 were both malformed (blank vietnamese, missing several fields); all three are the stand-ins for their own characters. Discovered genuine three-way Dan'a'yo homophone group (all 'yang/양/⼘ㄫ), previously undocumented — checked eight other candidates (央/仰/洋/殃/羊/楊/瘍/養) and confirmed none independent at this reading. Filled blank fields on 揚/陽, removed a redundant `品詞` on 様. Added canonical reciprocal `>[!warning] Homophones` callouts to all three pages. All three stamped `date-last-perfect: 2026-08-30`.

Next: 握窄.

### 2026-08-30, iteration 1811 — [[words/握窄|握窄]]

No stand-in relationship (握's own stand-in is [[把握]]; 窄's own is [[狭窄]]). Confirmed and documented as a deliberate phonetic substitution (same pattern as [[披歴]]/[[拉金]]): renders the real term 齷齪/龌龊 (wòchuò) using 握窄, since 齷/齪 have no pages. Filled blank `vietnamese: ác trác` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 援交.

### 2026-08-30, iteration 1812 — [[words/援交|援交]]

No stand-in relationship (援's own stand-in is [[援手]]; 交's own is itself). Fixed real bugs: `諺文` had the wrong final consonant for 援's syllable (옹→온) and `羅馬字` used the old minority reading "gyau" for 交 instead of majority-established "gyou" — both corrected. Filled blank `pos`/`vietnamese`, omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 援助.

### 2026-08-30, iteration 1813 — [[words/援助|援助]]

This word is itself the stand-in that legitimizes the character 助 (援's own stand-in is [[援手]]). Fixed real bug: `cantonese` had a spurious duplicate syllable (jyun4 zo6, wun4 zo6) — trimmed to compositional wun4 zo6. Filled blank `pos`/`vietnamese` (trợ inferred for 助 since the character's own citation is missing it — flagged). Omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 揶揄.

### 2026-08-30, iteration 1814 — [[words/揶揄|揶揄]]

This word is itself the stand-in that legitimizes BOTH characters (both 揶's and 揄's own `stand_in` is 揶揄) — same underlying pattern already seen on [[技能]] and [[揄伽]]. Fixed real bug: `諺文`/`羅馬字`/`注音` had dropped 揄's own coda (윰/yum) — corrected. Filled blank `vietnamese: da du` (a genuine standard term). No homophones at the corrected reading. Stamped `date-last-perfect: 2026-08-30`.

Next: 揺.

### 2026-08-30, iteration 1815 — [[words/揺|揺]] / [[words/窯|窯]]

Both had real bugs: `羅馬字` on both missing the leading glottal marker (you→'you), plus 揺 had literal `vietnamese: null`/`korean: "null"`. Both are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ⼄ㄨ) — checked nine other candidates (夭/姚/曜/腰/耀/要/窈/謡/遥) and confirmed none independent at this reading. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 搬送.

### 2026-08-30, iteration 1816 — [[words/搬送|搬送]]

This word is itself the stand-in that legitimizes the character 搬 (送's own stand-in is itself). Filled blank `vietnamese: ban tống` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 搭載.

### 2026-08-30, iteration 1817 — [[words/搭載|搭載]]

No stand-in relationship (搭's own stand-in is [[搭乗]]; 載's own is itself). Filled blank `pos: 事詞`, `vietnamese: đáp tải` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 摂食.

### 2026-08-30, iteration 1818 — [[words/摂食|摂食]]

No stand-in relationship (both 摂 and 食's own stand-ins are themselves). Filled blank `vietnamese: nhiếp thực` (compositional, reusing the previously-flagged 摂 reading). Fixed missing "(char)" suffixes, reformatted inline-flow `aliases`, omitted blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 撃.

### 2026-08-30, iteration 1819 — [[words/撃|撃]] / [[words/劇|劇]]

撃 was malformed (literal `vietnamese: null`, `korean: "null"`); both are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄍㄝㄎ), previously undocumented on either side — checked two other candidates (戟/激) and confirmed neither independent at this reading. 撃's `vietnamese` (kích) required going outside the character's own stored (blank) field — flagged for future check. Added canonical reciprocal callouts to both, cleaned up 劇's malformed single-string `english` and unquoted fields. Both stamped `date-last-perfect: 2026-08-30`.

Next: 撇.

### 2026-08-30, iteration 1820 — [[words/撇|撇]]

This word is itself the stand-in for its own character. Filled blank `japanese`/`hsk_level`. No word-level homophones (瞥 bound to [[一瞥]]). Stamped `date-last-perfect: 2026-08-30`.

Next: 撞球.

### 2026-08-30, iteration 1821 — [[words/撞球|撞球]]

No stand-in relationship (both 撞 and 球's own stand-ins are themselves). Simplified `japanese` from a comma-joined loanword+compositional dump to compositional どうきゅう, moved the loanword ビリヤード to prose. Filled blank `vietnamese: tràng cầu` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 撤.

### 2026-08-30, iteration 1822 — [[words/撤|撤]]

This word is itself the stand-in for its own character. Filled blank `japanese`/`hsk_level`. No word-level homophones (checked 姪/窒/跌). Stamped `date-last-perfect: 2026-08-30`.

Next: 播種.

### 2026-08-30, iteration 1823 — [[words/播種|播種]]

This word is itself the stand-in that legitimizes the character 播 (種's own stand-in is [[種類]]). Trimmed malformed comma-triplet `mandarin` to single bōzhǒng. Filled blank `vietnamese: bá chõng` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 撮.

### 2026-08-30, iteration 1824 — [[words/撮|撮]]

This word is itself the stand-in for its own character. Simplified `vietnamese` from a three-way list to its primary reading. Filled blank `japanese`. No word-level homophones (拶 is name-only). Stamped `date-last-perfect: 2026-08-30`.

Next: 撲.

### 2026-08-30, iteration 1825 — [[words/撲|撲]]

This word is itself the stand-in for its own character. Filled blank `pos`/`japanese`/`hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 撹拌.

### 2026-08-30, iteration 1826 — [[words/撹拌|撹拌]]

This word is itself the stand-in for its own character. Fixed real bug: `羅馬字` used the old minority "gyau" instead of majority-established "gyou". Filled blank `vietnamese: cảo bạn` (compositional), reformatted inline-flow `characters`/`aliases`, merged duplicate `## Words`/`## Etymology` into `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 擦.

### 2026-08-30, iteration 1827 — [[words/擦|擦]]

This word is itself the stand-in for its own character. Filled blank `pos`/`japanese`/`hsk_level`. No word-level homophones (刹/察 bound to other compounds). Stamped `date-last-perfect: 2026-08-30`.

Next: 擬.

### 2026-08-30, iteration 1828 — [[words/擬|擬]] / [[words/以|以]]

擬 was malformed (`羅馬字` missing leading glottal marker, missing japanese/hsk_level/date-last-perfect); both are stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄧ), previously undocumented — checked four other candidates (異/疑/飴/頤) and confirmed none independent at this reading. Removed a redundant `品詞` from 以's already-rich page. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 攘夷.

### 2026-08-30, iteration 1829 — [[words/攘夷|攘夷]]

This word is itself the stand-in that legitimizes the character 攘 (夷's own stand-in is [[東夷]]). Page was already richly documented; quoted string fields, added missing `kwin`/`tags`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 支付.

### 2026-08-30, iteration 1830 — [[words/支付|支付]]

This word is itself the stand-in that legitimizes the character 付 (支's own stand-in is [[支部]]). Quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 支那.

### 2026-08-30, iteration 1831 — [[words/支那|支那]]

No stand-in relationship (支's own stand-in is [[支部]]; 那's own is itself); a phonetic compound (old exonym for China). Removed redundant `品詞`, converted loose Notes line into proper prose. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 支部.

### 2026-08-30, iteration 1832 — [[words/支部|支部]]

This word is itself the stand-in that legitimizes the character 支 (部's own stand-in is itself). Filled blank `vietnamese: chi bộ` (a genuine standard term), omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 支配.

### 2026-08-30, iteration 1833 — [[words/支配|支配]]

No stand-in relationship (支's own stand-in is [[支部]]; 配's own is itself). Fixed unindented `characters` list, omitted blank `hsk_level`/`swadesh`/`aliases`, rewrote `## Etymology` as `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 改善.

### 2026-08-30, iteration 1834 — [[words/改善|改善]]

No stand-in relationship (both 改 and 善's own stand-ins are themselves). Omitted blank `hsk_level`/`swadesh`/empty-list `aliases`, rewrote `## Etymology` as `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 攻.

### 2026-08-30, iteration 1835 — [[words/攻|攻]] / [[words/公|公]]

Both are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄍㄛㄫ), previously undocumented — checked four other candidates (功/工/貢/龔) and confirmed none independent at this reading. Removed a redundant `品詞` from 公's already-rich page. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 攻防.

### 2026-08-30, iteration 1836 — [[words/攻防|攻防]]

No stand-in relationship (攻's own stand-in is itself; 防's own is [[防護]]). Filled blank `vietnamese: công phòng` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 放棄.

### 2026-08-30, iteration 1837 — [[words/放棄|放棄]]

This word is itself the stand-in that legitimizes the character 棄 (放's own stand-in is [[釈放]]). Filled blank `pos: 事詞`, omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 放火.

### 2026-08-30, iteration 1838 — [[words/放火|放火]] / [[words/防火|防火]]

Genuine, meaning-inverted homophone pair (both 注音 ㄅㄚㄫㄏ⺢: "arson" vs. "fireproofing"), previously flagged with non-canonical `>[!warning]`/`>[!tip]` single-sided notes — converted both to canonical reciprocal `>[!warning] Homophones` callouts. 放火 has no stand-in relationship (放's own is [[釈放]]; 火's own is itself), same for 防火 (防's own is [[防護]]). Modernized archaic kana on 放火 (はうくわ→ほうか). Both stamped `date-last-perfect: 2026-08-30`.

Next: 放素.

### 2026-08-30, iteration 1839 — [[words/放素|放素]]

Periodic-table neologism (radium). Page already richly documented explaining the naming logic (放 reserved for radium as the "ray-emitter," pairing with [[射素]] for radon). Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 放置.

### 2026-08-30, iteration 1840 — [[words/放置|放置]]

No stand-in relationship (放's own stand-in is [[釈放]]; 置's own is itself). Filled blank `pos: 事詞`, `vietnamese: phóng trí` (compositional), omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 政党.

### 2026-08-30, iteration 1841 — [[words/政党|政党]]

This word is itself the stand-in that legitimizes the character 党 (政's own stand-in is [[政治]]). Removed self-referential `政党` from `aliases` (matched the filename itself), kept genuine traditional variant 政黨. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 政治.

### 2026-08-30, iteration 1842 — [[words/政治|政治]]

This word is itself the stand-in that legitimizes the character 政 (治's own stand-in is [[統治]]). Fixed real bug: `羅馬字` had a garbled/contaminated value (jing'yog→jingci). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 政治学.

### 2026-08-30, iteration 1843 — [[words/政治学|政治学]]

No stand-in relationship (政's own stand-in is [[政治]] itself; 治's own is [[統治]]; 学's own is [[学習]]). Fixed the same `羅馬字` contamination bug found on [[政治]] (jing'yoghag→jingcihag). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 故人.

### 2026-08-30, iteration 1844 — [[words/故人|故人]]

No stand-in relationship (故's own stand-in is [[緣故]]; 人's own is itself). Omitted blank `hsk_level`/`swadesh`/empty-list `aliases`, added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 故意.

### 2026-08-30, iteration 1845 — [[words/故意|故意]]

No stand-in relationship (故's own stand-in is [[緣故]]; 意's own is [[意味]]). Added missing `kwin: false`, omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 故郷.

### 2026-08-30, iteration 1846 — [[words/故郷|故郷]]

This word is itself the stand-in that legitimizes the character 郷 (故's own stand-in is [[緣故]]). Filled blank `vietnamese: cố hương` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 敏感.

### 2026-08-30, iteration 1847 — [[words/敏感|敏感]]

No stand-in relationship (敏's own stand-in is itself; 感's own is [[感触]]). Quoted `hsk_level`, omitted blank `swadesh`/`aliases`, rewrote `## Etymology` as `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 救偕.

### 2026-08-30, iteration 1848 — [[words/救偕|救偕]]

No stand-in relationship (救's own stand-in is [[救援]]; 偕's own is [[偕同]]). A semantic-compositional coined name for Jesus ("the one who saves and accompanies"), not a phonetic loan — filled the five blank cross-linguistic fields with the standard real-world loanword names for Jesus in each language (Yēsū/je1 sou1/イエス/예수/Giê-su), since no compositional reading of 救偕 itself exists outside this vault; documented this reasoning explicitly. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 救援.

### 2026-08-30, iteration 1849 — [[words/救援|救援]]

This word is itself the stand-in that legitimizes the character 救 (援's own stand-in is [[援手]]). Filled blank `vietnamese: cứu vin` (compositional), omitted blank `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 教会.

### 2026-08-30, iteration 1850 — [[words/教会|教会]]

No stand-in relationship (教's own stand-in is [[教授]]; 会's own is itself). Fixed real bug: `諺文`/`羅馬字`/`注音` all used the old minority "gyau" for 教 instead of majority-established "gyou" (same bug class as [[撹拌]]/[[援交]]) — corrected. Likely a systemic issue across other 教-compounds; will check and retroactively fix each as encountered going forward. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 教化.

### 2026-08-30, iteration 1851 — [[words/教化|教化]]

No stand-in relationship (教's own stand-in is [[教授]]; 化's own is itself). Already correctly used majority "gyou" (no bug here). Fixed empty-string `vietnamese`/`swadesh`, filled `vietnamese: giáo hoá` (a genuine standard term). Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 教員.

### 2026-08-30, iteration 1852 — [[words/教員|教員]]

No stand-in relationship (教's own stand-in is [[教授]]; 員's own is [[人員]]). Fixed real bug: `羅馬字` used old minority "gyau" instead of majority "gyou". No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 教授.

### 2026-08-30, iteration 1853 — [[words/教授|教授]] (retroactive fix)

This word is itself the stand-in for 教 (授's own stand-in is [[授与]]). Retroactively fixed the same systemic "gyau"→"gyou" bug found on [[教会]]/[[教員]] on this already-stamped page. Filled blank `vietnamese: giáo thụ`. No homophones. Re-stamped `date-last-perfect: 2026-08-30`.

Next: 教堂.

### 2026-08-30, iteration 1854 — [[words/教堂|教堂]]

No stand-in relationship (教's own stand-in is [[教授]]; 堂's own is [[会堂]]). Already correctly used majority "gyou". Filled blank `vietnamese: giáo đường` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 教学.

### 2026-08-30, iteration 1855 — [[words/教学|教学]]

No stand-in relationship (教's own stand-in is [[教授]]; 学's own is [[学習]]). Filled missing `korean: 교학`/`vietnamese: giáo học`, removed redundant `品詞`, fixed empty-string `swadesh` and bare-string `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 教師.

### 2026-08-30, iteration 1856 — [[words/教師|教師]]

This word is itself the stand-in that legitimizes the character 師 (教's own stand-in is [[教授]]). Fixed real bug: `羅馬字` used old minority "gyau" instead of majority "gyou". Filled blank `vietnamese: giáo sư` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 敢為.

### 2026-08-30, iteration 1857 — [[words/敢為|敢為]]

This word is itself the stand-in that legitimizes the character 敢 (為's own stand-in is itself). Filled blank `cantonese`/`vietnamese` (both compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 散布.

### 2026-08-30, iteration 1858 — [[words/散布|散布]] (completing homophone with [[散歩]])

This word is itself the stand-in for its own character 散. Removed self-referential `散布` from `aliases` (flagged from [[散歩]]'s own earlier turn), kept genuine traditional variant 散佈. Fixed callout spacing to canonical. Filled blank `vietnamese: tán bố` (compositional). Homophone with [[散歩]] (both sanbo/산보/ㄙㄚㄇㄅㄛ) already cross-referenced from that side. Stamped `date-last-perfect: 2026-08-30`.

Next: 敦厚.

### 2026-08-30, iteration 1859 — [[words/敦厚|敦厚]]

This word is itself the stand-in that legitimizes the character 敦 (厚's own stand-in is itself). Trimmed stray space in `mandarin`, fixed missing "(char)" suffix, omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 敬語.

### 2026-08-30, iteration 1860 — [[words/敬語|敬語]] / [[words/鯨魚|鯨魚]]

Genuine Dan'a'yo-level homophone pair (both gyeng'yo/경요/ㄍ⼶ㄫ⼄), previously undocumented on either side. 敬語: no stand-in relationship (敬's own is [[尊敬]]; 語's own is [[言語]]); filled blank `vietnamese: kính ngữ` (compositional). 鯨魚: this word is itself the stand-in for its own character 鯨 (魚's own stand-in is itself); simplified comma-joined `korean` (경어,고래→compositional 경어, native 고래 moved to prose), documented Japanese くじら as native equivalent. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 数詞.

### 2026-08-30, iteration 1861 — [[words/数詞|数詞]]

No stand-in relationship (数's own stand-in is [[計数]]; 詞's own is [[単詞]]). Fixed real bugs: `korean` contaminated with 數字's reading (숫자→수사) and `vietnamese` a loose native paraphrase rather than the standard term (chữ số→số từ). Removed mismatched-character `數字` from `aliases`. Filled blank `pos`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 数量.

### 2026-08-30, iteration 1862 — [[words/数量|数量]]

This word is itself the stand-in that legitimizes the character 量 (数's own stand-in is [[計数]]). Filled blank `pos`, reformatted inline-flow `characters`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 敲.

### 2026-08-30, iteration 1863 — [[words/敲|敲]]

This word is itself the stand-in for its own character. Filled blank `japanese`/`hsk_level`. No word-level homophones (喬/巧 bound elsewhere). Stamped `date-last-perfect: 2026-08-30`.

Next: 整.

### 2026-08-30, iteration 1864 — [[words/整|整]] / [[words/錠|錠]]

Both had literal `vietnamese: null` and were malformed (missing pos/japanese/hsk_level/kwin/date-last-perfect); both are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄐㄝㄫ) — checked eight other candidates (定/征/浄/精/箏/鄭/静/頂) and confirmed none independent at this reading. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 整斉.

### 2026-08-30, iteration 1865 — [[words/整斉|整斉]]

No stand-in relationship (整's own stand-in is itself; 斉's own is [[一斉]]). Filled blank `vietnamese: chỉnh tề` (a genuine standard term), reformatted inline-flow `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 整理.

### 2026-08-30, iteration 1866 — [[words/整理|整理]] / [[words/精子|精子]]

Fixed a significant contamination bug (same pattern as [[採集]]/[[菜汁]]): 整理's `諺文`/`注音` had been given the wrong second-syllable reading (정지/ㄐㄝㄫㄐㄧ) instead of the correct compositional 정리/ㄐㄝㄫㄌㄧ (matching 理's own citation); `羅馬字` jengli was already correct. This invalidated a false homophone claim both pages carried against each other — removed from both sides; no genuine homophone exists at either corrected reading. Neither word has a stand-in relationship. Filled both pages' blank `vietnamese` (chỉnh lý / tinh tử, both genuine standard terms). Both stamped `date-last-perfect: 2026-08-30`.

Next: 敵人.

### 2026-08-30, iteration 1867 — [[words/敵人|敵人]]

This word is itself the stand-in for 敵, deliberately splitting the concrete-adversary sense from [[仇恨]]'s abstract-grudge sense (a mirror pattern to [[仇敵]]). Page was already richly documented; filled blank `vietnamese: địch nhân` (compositional), quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 敷.

### 2026-08-30, iteration 1868 — [[words/敷|敷]] / [[words/賦|賦]] (retroactive fix)

Fixed a significant identical contamination bug on both pages: `諺文`/`羅馬字`/`注音` had used the wrong initial (푸/pu/ㄆㄨ instead of the character's own 뿌/fu/ㄈㄨ) on both 敷 and the already-stamped 賦 — corrected both. This surfaced a genuine Dan'a'yo-level homophone between them (both 注音 ㄈㄨ, both stand-ins for their own characters) that was invisible while the bug masked it — checked eight other candidates (俘/俯/付/斧/孚/府/撫/黼) and confirmed none independent at this reading. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Fixed literal `vietnamese: null` on 敷 and removed redundant `品詞` on 賦. Both stamped `date-last-perfect: 2026-08-30`.

Next: 文化圏.

### 2026-08-30, iteration 1869 — [[words/文化圏|文化圏]]

No stand-in relationship (文's own stand-in is [[文化]]; 化's own is itself; 圏's own is itself). Filled blank `vietnamese: văn hoá khuyên` (compositional), reformatted inline-flow `characters`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 文字.

### 2026-08-30, iteration 1870 — [[words/文字|文字]]

No stand-in relationship (文's own stand-in is [[文化]]; 字's own is itself). Simplified `korean` from comma-joined "글자, 문자" to compositional 문자 (moved native 글자 to prose); fixed erroneous title-case `vietnamese` (Văn Tự→văn tự). Added missing `kwin: false` (諺文 문지 diverges from real Korean 문자). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 文書.

### 2026-08-30, iteration 1871 — [[words/文書|文書]]

No stand-in relationship (文's own stand-in is [[文化]]; 書's own is [[書本]]). Simplified `vietnamese` from a native-paraphrase pair to the standard compositional term văn thư. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 文武.

### 2026-08-30, iteration 1872 — [[words/文武|文武]]

No stand-in relationship (文's own stand-in is [[文化]]; 武's own is itself). Fixed missing space in `cantonese`, filled blank `japanese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 文法.

### 2026-08-30, iteration 1873 — [[words/文法|文法]]

No stand-in relationship (文's own stand-in is [[文化]]; 法's own is itself). Filled blank `vietnamese: văn pháp` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 文献.

### 2026-08-30, iteration 1874 — [[words/文献|文献]]

No stand-in relationship (文's own stand-in is [[文化]]; 献's own is [[献上]]). Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 斉国.

### 2026-08-30, iteration 1875 — [[words/斉国|斉国]]

No stand-in relationship (斉's own stand-in is [[一斉]]; 国's own is [[国家]]). Fixed real bug: `japanese` was missing the 国 half entirely (せい→せいこく). Filled blank `cantonese: cai4 gwok3`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 斑点.

### 2026-08-30, iteration 1876 — [[words/斑点|斑点]]

This word is itself the stand-in that legitimizes the character 斑 (点's own stand-in is itself). Filled blank `vietnamese: ban điểm` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 料槽.

### 2026-08-30, iteration 1877 — [[words/料槽|料槽]]

This word is itself the stand-in that legitimizes the character 槽 (料's own stand-in is [[材料]]). Filled blank `vietnamese: liệu tào` (compositional), added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 斟酌.

### 2026-08-30, iteration 1878 — [[words/斟酌|斟酌]]

This word is itself the stand-in that legitimizes the character 斟 (酌's own stand-in is [[酌酒]]). Filled blank `vietnamese: châm chước` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 斧子.

### 2026-08-30, iteration 1879 — [[words/斧子|斧子]]

This word is itself the stand-in that legitimizes the character 斧 (子's own stand-in is [[児子]]). Filled blank `vietnamese: phủ tử` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 斬.

### 2026-08-30, iteration 1880 — [[words/斬|斬]] / [[words/蚕|蚕]]

蚕 had a literal `vietnamese: null`; both words are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄐㄚㄇ), previously undocumented — checked three other candidates (慙/暫/站) and confirmed none independent at this reading. Korean 천 on 蚕 diverges from compositional 잠 (a genuine, pre-existing Sino-Korean divergence, kwin: false, not a bug). Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 断念.

### 2026-08-30, iteration 1881 — [[words/断念|断念]]

No stand-in relationship (断's own stand-in is [[割断]]; 念's own is [[念頭]]). Fixed missing space in `cantonese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 断頭台.

### 2026-08-30, iteration 1882 — [[words/断頭台|断頭台]]

No stand-in relationship (all three characters' own stand-ins point elsewhere). Fixed missing "(char)" suffixes, reformatted inline-flow `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 新星.

### 2026-08-30, iteration 1883 — [[words/新星|新星]]

No stand-in relationship (both 新 and 星's own stand-ins are themselves). Added missing `kwin: true`, quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 新芽.

### 2026-08-30, iteration 1884 — [[words/新芽|新芽]]

This word is itself the stand-in that legitimizes the character 芽 (新's own stand-in is itself). Simplified `korean` (움→신아, compositional) and `vietnamese` (búp/chồi→tân nha, compositional), moving native equivalents to prose. Documented Japanese しんめ as a genuine hybrid on+native reading (expected). Filled blank `pos`, added missing `kwin: true`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 新語.

### 2026-08-30, iteration 1885 — [[words/新語|新語]]

No stand-in relationship (新's own stand-in is itself; 語's own is [[言語]]). Fixed missing space in `cantonese`, filled blank `vietnamese: tân ngữ` (compositional), removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 方法.

### 2026-08-30, iteration 1886 — [[words/方法|方法]]

No stand-in relationship (方's own stand-in is [[方向]]; 法's own is itself). Fixed missing "(char)" suffix, omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 方言.

### 2026-08-30, iteration 1887 — [[words/方言|方言]]

No stand-in relationship (方's own stand-in is [[方向]]; 言's own is itself). Fixed real bug: `諺文`/`羅馬字`/`注音` had all used the wrong initial (방/pang/ㄆㄚㄫ instead of 방's real Dan'a'yo reading 빵/fang/ㄈㄚㄫ) — corrected, which also corrected `kwin` from an erroneous `true` to the true `false` (諺文 빵언 ≠ korean 방언). Removed redundant `品詞`. No homophones at the corrected reading. Stamped `date-last-perfect: 2026-08-30`.

Next: 方針.

### 2026-08-30, iteration 1888 — [[words/方針|方針]]

No stand-in relationship (方's own stand-in is [[方向]]; 針's own is itself). Already correctly compositional; omitted blank `hsk_level`/`swadesh`, added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 方響.

### 2026-08-30, iteration 1889 — [[words/方響|方響]] / [[words/芳香|芳香]] (completing three-way homophone with [[方向]])

方響 was missing vietnamese/hsk_level/date-last-perfect and had archaic kana (はうきやう→ほうきょう). 芳香 (already stamped) was missing vietnamese/date-last-perfect and is itself the stand-in for 芳 (香's own is [[香気]]). Both already anticipated the three-way homophone with [[方向]] (all 注音 ㄈㄚㄫㄏ⼘ㄫ) but with non-canonical single-line callouts — reformatted all three pages to canonical multi-line reciprocal callouts. Filled blank `vietnamese` on both (phương hưởng / phương hương, both compositional). Stamped `date-last-perfect: 2026-08-30`.

Next: 施行.

### 2026-08-30, iteration 1890 — [[words/施行|施行]]

This word is itself the stand-in that legitimizes the character 施 (行's own stand-in is itself). Filled blank `vietnamese: thi hành` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 旁胱.

### 2026-08-30, iteration 1891 — [[words/旁胱|旁胱]]

This word is itself the stand-in for its own character 胱. Modernized archaic kana ばうくわう→ぼうこう. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 旅鼠.

### 2026-08-30, iteration 1892 — [[words/旅鼠|旅鼠]]

No stand-in relationship (旅's own stand-in is [[旅行]]; 鼠's own is [[熊鼠]]). Fixed real bug: `korean` was the loanword 레밍 ("lemming") instead of compositional 려서 — corrected. Filled blank `cantonese`/`vietnamese`, simplified `japanese` (moved loanword レミング to prose). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 族群.

### 2026-08-30, iteration 1893 — [[words/族群|族群]]

No stand-in relationship (族's own stand-in is [[家族]]; 群's own is [[群衆]]). Filled missing `korean: 족군`/`vietnamese: tộc quần` (both compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 族譜.

### 2026-08-30, iteration 1894 — [[words/族譜|族譜]]

No stand-in relationship (族's own stand-in is [[家族]]; 譜's own is [[楽譜]]). Filled blank `vietnamese: tộc phả` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 旗幟.

### 2026-08-30, iteration 1895 — [[words/旗幟|旗幟]]

This word is itself the stand-in that legitimizes the character 旗 (幟's own stand-in is itself). Filled blank `vietnamese: kì xí` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 旗艦.

### 2026-08-30, iteration 1896 — [[words/旗艦|旗艦]]

No stand-in relationship (旗's own stand-in is [[旗幟]]; 艦's own is [[艦船]]). Fixed `vietnamese`: soái hạm uses a different character (帥) not derived from 旗 — corrected to compositional kì hạm, noting soái hạm as the more common everyday term. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 既以.

### 2026-08-30, iteration 1897 — [[words/既以|既以]]

This word is itself the stand-in that legitimizes the character 既 (以's own stand-in is itself). Fixed real bug: `korean` was 既's own native reading (이미) instead of compositional 기이. Filled blank `pos`/`cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 既往.

### 2026-08-30, iteration 1898 — [[words/既往|既往]]

No stand-in relationship (既's own stand-in is [[既以]]; 往's own is itself). Filled blank `vietnamese: kí vãng` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 既遂.

### 2026-08-30, iteration 1899 — [[words/既遂|既遂]]

This word is itself the stand-in that legitimizes the character 遂 (既's own stand-in is [[既以]]). Quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日出.

### 2026-08-30, iteration 1900 — [[words/日出|日出]]

No stand-in relationship (both 日 and 出's own stand-ins are themselves). Filled blank `vietnamese: nhật xuất` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日刊.

### 2026-08-30, iteration 1901 — [[words/日刊|日刊]]

No stand-in relationship (both 日 and 刊's own stand-ins are themselves). Filled blank `vietnamese: nhật san` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日報.

### 2026-08-30, iteration 1902 — [[words/日報|日報]]

No stand-in relationship (both 日 and 報's own stand-ins are themselves). Fixed real bug: `cantonese` had the wrong tone (jat4→jat6). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日常.

### 2026-08-30, iteration 1903 — [[words/日常|日常]]

This word is itself the stand-in that legitimizes the character 常. Filled blank `vietnamese: nhật thường` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日月.

### 2026-08-30, iteration 1904 — [[words/日月|日月]]

No stand-in relationship (both 日 and 月's own stand-ins are themselves). Fixed missing "(char)" suffixes, added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日本.

### 2026-08-30, iteration 1905 — [[words/日本|日本]]

No stand-in relationship (both 日 and 本's own stand-ins are themselves). Simplified `japanese` from comma-joined にっぽん/にほん to the single primary reading にほん, moving the equally-official にっぽん to prose. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日本語.

### 2026-08-30, iteration 1906 — [[words/日本語|日本語]]

No stand-in relationship (日/本's own stand-ins are themselves; 語's own is [[言語]]). Documented Vietnamese tiếng Nhật as the standard everyday term (not compositional). Converted loose body line into proper `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日耳曼.

### 2026-08-30, iteration 1907 — [[words/日耳曼|日耳曼]]

A phonetic transliteration of "Germanic"; no stand-in relationship (日/耳's own are themselves; 曼's is name-only). Filled blank `cantonese: jat6 ji5 maan6` (compositional), documented Japanese/Korean as direct international loanwords (expected). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日記.

### 2026-08-30, iteration 1908 — [[words/日記|日記]]

No stand-in relationship (日's own stand-in is itself; 記's own is [[記憶]]). Fixed missing "(char)" suffix, added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 日食.

### 2026-08-30, iteration 1909 — [[words/日食|日食]]

No stand-in relationship (both 日 and 食's own stand-ins are themselves). Page was already well-formed; added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 旦夕.

### 2026-08-30, iteration 1910 — [[words/旦夕|旦夕]]

No stand-in relationship (旦's own stand-in is [[元旦]]; 夕's own is [[夕陽]]). Trimmed malformed comma-duplicate `mandarin`, filled missing `korean`/`vietnamese` (both compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 旧.

### 2026-08-30, iteration 1911 — [[words/旧|旧]] / [[words/糾|糾]] (completing three-way homophone with [[臼]])

Both had literal `vietnamese: null` and were malformed (missing pos/japanese/hsk_level/date-last-perfect); both are stand-ins for their own characters. Completed the three-way Dan'a'yo homophone group (all gyuo/귯/ㄍ⼜ㄛ) that [[臼]] had already anticipated and richly documented from its own earlier turn (including having already fixed 旧's `korean: "null"` bug and ruled out 求/舅 as a fourth homophone) — reformatted all three pages to canonical multi-line reciprocal callouts. Filled blank fields on 旧/糾. All three stamped/updated `date-last-perfect: 2026-08-30`.

Next: 旧金山.

### 2026-08-30, iteration 1912 — [[words/旧金山|旧金山]]

No stand-in relationship (all three characters' own stand-ins are themselves). Documented Japanese/Korean as direct phonetic transliterations of "San Francisco" (expected), Mandarin/Cantonese/Vietnamese as the Sinitic calque "Old Gold Mountain." Fixed missing "(char)" suffixes, reformatted inline-flow `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 早.

### 2026-08-30, iteration 1913 — [[words/早|早]] / [[words/朝|朝]] / [[words/繰|繰]]

All three had literal `vietnamese: null` and were malformed (missing pos/japanese/hsk_level/date-last-perfect); all three are stand-ins for their own characters. Discovered genuine three-way Dan'a'yo homophone group (all jau/잣/ㄐㄚㄨ), previously undocumented — checked thirteen other candidates (兆/巣/槽/漕/曹/棗/礁/肇/趙/躁/糟/蚤/遭) and confirmed none independent at this reading. Added canonical reciprocal `>[!warning] Homophones` callouts to all three. All three stamped `date-last-perfect: 2026-08-30`.

Next: 旱災.

### 2026-08-30, iteration 1914 — [[words/旱災|旱災]]

This word is itself the stand-in that legitimizes the character 旱 (災's own stand-in is [[災害]]). Removed mismatched-character `旱魃`/`干魃` from `aliases` (use 魃, a distinct character). Filled blank `vietnamese: hạn tai` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昂揚.

### 2026-08-30, iteration 1915 — [[words/昂揚|昂揚]]

No stand-in relationship (昂's own stand-in is [[昂然]]; 揚's own is itself). Filled missing `korean: 앙양`/`vietnamese: ngang dương` (compositional; 揚's half required going outside the character's own stored citation — flagged, same gap class as [[振]]/[[摂]]/[[騒]]). Documented Japanese こうよう's irregular on-reading as expected, not a bug. Quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昂然.

### 2026-08-30, iteration 1916 — [[words/昂然|昂然]]

This word is itself the stand-in that legitimizes the character 昂 (然's own stand-in is itself). Filled missing `korean: 앙연`/`vietnamese: ngang nhiên` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昆.

### 2026-08-30, iteration 1917 — [[words/昆|昆]]

This word is itself the stand-in for its own character. Filled blank `japanese`/`hsk_level`. No word-level homophones (鯤 bound to [[鯤魚]]). Stamped `date-last-perfect: 2026-08-30`.

Next: 昇叙.

### 2026-08-30, iteration 1918 — [[words/昇叙|昇叙]]

No stand-in relationship (昇's own stand-in is [[上昇]]; 叙's own is [[叙述]]). Fixed garbled `japanese` (a stray kanji embedded mid-reading). Filled blank `pos`/`korean`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昇天.

### 2026-08-30, iteration 1919 — [[words/昇天|昇天]]

No stand-in relationship (昇's own stand-in is [[上昇]]; 天's own is itself). Filled blank `pos`, converted loose body line into proper `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昇級.

### 2026-08-30, iteration 1920 — [[words/昇級|昇級]]

No stand-in relationship (昇's own stand-in is [[上昇]]; 級's own is [[等級]]). Clarified this entry documents 升级/Shēngjí (the card game, hence the proper-noun `pos`/Japanese transliteration); filled blank `korean`/`vietnamese` with the compositional forms, which double as the genuine terms for the common "promotion, level up" sense. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 明.

### 2026-08-30, iteration 1921 — [[words/明|明]] / [[words/鳴|鳴]] (completing three-way homophone with [[皿]])

明 had a bloated four-way `vietnamese` list (three variants belonging to unrelated homophone characters, same contamination class already documented on [[皿]]); 鳴 was missing pos/vietnamese. Both are stand-ins for their own characters. Completed the three-way Dan'a'yo homophone group (all myeng/명/ㄇ⼶ㄫ) that [[皿]] had already anticipated and richly documented — reformatted all three pages to canonical multi-line reciprocal callouts. Both stamped `date-last-perfect: 2026-08-30`.

Next: 明君.

### 2026-08-30, iteration 1922 — [[words/明君|明君]]

No stand-in relationship (both 明 and 君's own stand-ins are themselves). Page was already richly documented; quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 明徳.

### 2026-08-30, iteration 1923 — [[words/明徳|明徳]]

No stand-in relationship (both 明 and 徳's own stand-ins are themselves). Filled blank `vietnamese: minh đức` (a genuine standard Confucian term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 明月.

### 2026-08-30, iteration 1924 — [[words/明月|明月]]

No stand-in relationship (both 明 and 月's own stand-ins are themselves). Fixed missing "(char)" suffix, added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 明様.

### 2026-08-30, iteration 1925 — [[words/明様|明様]]

No stand-in relationship (both 明 and 様's own stand-ins are themselves). Fixed real bug: every field held native descriptive phrases instead of the compositional 明+様 adverbializer form (mandarin míngliàng de, Japanese あかるく, Korean 밝게/똑똑히, Vietnamese trong sáng) — all corrected to compositional. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 明白.

### 2026-08-30, iteration 1926 — [[words/明白|明白]]

No stand-in relationship (both 明 and 白's own stand-ins are themselves). Trimmed malformed comma-duplicate `mandarin`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 明確.

### 2026-08-30, iteration 1927 — [[words/明確|明確]]

No stand-in relationship (明's own stand-in is itself; 確's own is [[確実]]). Quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昔日.

### 2026-08-30, iteration 1928 — [[words/昔日|昔日]]

This word is itself the stand-in that legitimizes the character 昔 (日's own stand-in is itself). Trimmed malformed comma-duplicate `mandarin`. Filled missing `korean`/`vietnamese` (both compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 星.

### 2026-08-30, iteration 1929 — [[words/星|星]]

This word is itself the stand-in for its own character. Filled blank `pos`/`japanese`, simplified single-item `vietnamese` list to scalar. No word-level homophones (猩/醒 bound elsewhere). Stamped `date-last-perfect: 2026-08-30`.

Next: 星坐.

### 2026-08-30, iteration 1930 — [[words/星坐|星坐]]

No stand-in relationship (both 星 and 坐's own stand-ins are themselves). Fixed `vietnamese`: chòm sao was native rather than the compositional standard term — corrected to tinh toạ. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 星条旗.

### 2026-08-30, iteration 1931 — [[words/星条旗|星条旗]]

No stand-in relationship (星/条's own stand-ins are themselves; 旗's own is [[旗幟]]). Removed mismatched-character `花旗` from `aliases` (built on 花, a distinct real-world name for the same flag). Filled blank `vietnamese: tinh điều kì` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 星洲.

### 2026-08-30, iteration 1932 — [[words/星洲|星洲]]

No stand-in relationship (both 星 and 洲's own stand-ins are themselves). Quoted string fields, added missing `kwin`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 星群.

### 2026-08-30, iteration 1933 — [[words/星群|星群]]

No stand-in relationship (星's own stand-in is itself; 群's own is [[群衆]]). Filled blank `vietnamese: tinh quần` (compositional; 群's half required going outside the character's own stored citation — flagged, same gap class as [[振]]/[[摂]]/[[騒]]/[[昂揚]]). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 星雲.

### 2026-08-30, iteration 1934 — [[words/星雲|星雲]]

No stand-in relationship (both 星 and 雲's own stand-ins are themselves). Omitted blank `hsk_level`/`swadesh`, reformatted inline-flow `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 星霜.

### 2026-08-30, iteration 1935 — [[words/星霜|星霜]]

No stand-in relationship (both 星 and 霜's own stand-ins are themselves). Fixed real bug: `注音` had a typo (wrong final on 星's syllable, ㄙㄝㄋ→ㄙㄝㄫ). No homophones at the corrected reading. Stamped `date-last-perfect: 2026-08-30`.

Next: 春.

### 2026-08-30, iteration 1936 — [[words/春|春]]

This word is itself the stand-in for its own character. Fixed real bug: literal `vietnamese: null`, corrected to xuân. Filled blank `pos`/`japanese`/`hsk_level`. No word-level homophones (椿/蠢 bound elsewhere/name-only). Stamped `date-last-perfect: 2026-08-30`.

Next: 春季.

### 2026-08-30, iteration 1937 — [[words/春季|春季]]

No stand-in relationship (春's own stand-in is itself; 季's own is [[季節]]); synonymous with bare [[春]]. Filled blank `vietnamese: xuân quý` (a genuine standard term), quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 春秋.

### 2026-08-30, iteration 1938 — [[words/春秋|春秋]]

No stand-in relationship (both 春 and 秋's own stand-ins are themselves). Removed redundant `品詞`, added `## Notes` summarizing compositional readings (rich `## Definition` content preserved as-is). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昧.

### 2026-08-30, iteration 1939 — [[words/昧|昧]] / [[words/苺|苺]] (completing three-way homophone with [[呆]])

Both were malformed (苺 had literal `vietnamese: null`, and my own first-pass fix mistakenly used the wrong Vietnamese value before catching it against the character's own citation — corrected to môi); both are stand-ins for their own characters. Completed the three-way Dan'a'yo homophone group (all mai/매/ㄇㄚㄧ) that [[呆]] had already anticipated and richly documented — reformatted all three pages to canonical multi-line reciprocal callouts. Both stamped `date-last-perfect: 2026-08-30`.

Next: 昨.

### 2026-08-30, iteration 1940 — [[words/昨|昨]] / [[words/作|作]]

昨 had a literal `vietnamese: null` and was malformed (missing pos/japanese/hsk_level); both words are the stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both 注音 ㄐㄚㄎ), previously undocumented — checked eleven other candidates (宅/捉/搾/爵/灼/炸/窄/責/酢/酌/雀) and confirmed none independent at this reading. Added canonical reciprocal `>[!warning] Homophones` callouts to both, filled 作's missing `hsk_level` and removed its redundant `品詞`. Both stamped `date-last-perfect: 2026-08-30`.

Next: 昨世紀.

### 2026-08-30, iteration 1941 — [[words/昨世紀|昨世紀]]

No stand-in relationship (昨's own stand-in is itself; 世's own is [[世界]]; 紀's own is [[世紀]]). Fixed real bug: `korean` was a native paraphrase (지난세기) instead of compositional 작세기 — corrected. Filled blank `vietnamese: tạc thế kỷ` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昨年.

### 2026-08-30, iteration 1942 — [[words/昨年|昨年]]

No stand-in relationship (both 昨 and 年's own stand-ins are themselves). Simplified `korean` (작년, 지난해→compositional 작년, native moved to prose). Filled blank `vietnamese: tạc niên` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昨月.

### 2026-08-30, iteration 1943 — [[words/昨月|昨月]]

No stand-in relationship (both 昨 and 月's own stand-ins are themselves). Fixed real bugs: `mandarin` was the unrelated compound 上個月 (different character composition) and `korean` was native 지난달 — both corrected to compositional. Removed mismatched-character alias, filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昨週.

### 2026-08-30, iteration 1944 — [[words/昨週|昨週]] / [[words/酌酒|酌酒]]

Fixed real contamination bug (same class as [[昨月]]): 昨週's `mandarin`/`cantonese`/`korean` had been the unrelated compound 上周 instead of compositional zuózhōu — corrected. This surfaced a genuine Dan'a'yo-level homophone with [[酌酒]] (both 注音 ㄐㄚㄎㄐㄨㄛ, both stand-ins for their own characters, 昨's own stand-in is itself/週's own is [[週日]]) — added canonical reciprocal callouts to both, filled 酌酒's blank `cantonese`/`vietnamese`. Both stamped `date-last-perfect: 2026-08-30`.

Next: 昭.

### 2026-08-30, iteration 1945 — [[words/昭|昭]] / [[words/焦|焦]] / [[words/照|照]]

焦 had a literal `vietnamese: null`; all three words were malformed (missing pos/japanese/hsk_level/date-last-perfect); all three are stand-ins for their own characters. Discovered genuine three-way Dan'a'yo homophone group (all jou/좃/ㄐㄛㄨ), previously undocumented — checked six other candidates (俎/沼/椒/藻/蕉/詔) and confirmed none independent at this reading. Added canonical reciprocal `>[!warning] Homophones` callouts to all three. All three stamped `date-last-perfect: 2026-08-30`.

Next: 是日.

### 2026-08-30, iteration 1946 — [[words/是日|是日]]

No stand-in relationship (both 是 and 日's own stand-ins are themselves); an archaic expression for [[今日]]. Filled blank `japanese`/`vietnamese`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昴宿星団.

### 2026-08-30, iteration 1947 — [[words/昴宿星団|昴宿星団]]

This word is itself the stand-in that legitimizes the character 昴 (宿's own stand-in is [[寄宿]]; 団's own is [[集団]]). Fixed a stray space in `mandarin`, simplified malformed native+compositional `japanese` field to compositional ぼうしゅくせいだん (native スバル noted in prose). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 昼間.

### 2026-08-30, iteration 1948 — [[words/昼間|昼間]]

This word is itself the stand-in that legitimizes the character 昼 (間's own stand-in is [[之間]]). Fixed real bug: `mandarin` was the unrelated phrase 黎明之間 instead of compositional zhòujiān. Filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 時代.

### 2026-08-30, iteration 1949 — [[words/時代|時代]]

This word is itself the stand-in that legitimizes the character 時 (代's own stand-in is [[世代]]). Fixed real bug: `cantonese` was missing its initial consonant (i4doi6→si4 doi6). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 時宜.

### 2026-08-30, iteration 1950 — [[words/時宜|時宜]]

No stand-in relationship (時's own stand-in is itself; 宜's own is [[適宜]]). Fixed real bug: `諺文`/`羅馬字`/`注音` had all used the wrong second syllable (위/wi/ㄨㄧ instead of 읫/'ǝi/ㄜㄧ, the same 'ǝi/wi minority-pattern bug documented elsewhere in this vault, e.g. on 議). Filled blank `vietnamese: thì nghi`. No homophones at the corrected reading. Stamped `date-last-perfect: 2026-08-30`.

Next: 時相.

### 2026-08-30, iteration 1951 — [[words/時相|時相]]

No stand-in relationship (時's own stand-in is itself; 相's own is [[相互]]). Page was already richly documented; filled blank `cantonese`/`vietnamese` (both compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 時節.

### 2026-08-30, iteration 1952 — [[words/時節|時節]]

No stand-in relationship (both 時 and 節's own stand-ins are themselves). Filled blank `pos`, quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 晒.

### 2026-08-30, iteration 1953 — [[words/晒|晒]]

This word is itself the stand-in for its own character. Filled blank `japanese`, quoted `hsk_level`. No word-level homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 晩.

### 2026-08-30, iteration 1954 — [[words/晩|晩]]

This word is itself the stand-in for its own character. Fixed real bug: literal `vietnamese: null`, corrected to vãn. Filled blank `pos`/`japanese`/`hsk_level`. No word-level homophones (checked seven candidates). Stamped `date-last-perfect: 2026-08-30`.

Next: 晩飯.

### 2026-08-30, iteration 1955 — [[words/晩飯|晩飯]]

No stand-in relationship (晩's own stand-in is itself; 飯's own is [[米飯]]). Simplified `korean` from native paraphrase to compositional 만반. Filled blank `vietnamese: vãn phạn` (compositional). Removed mismatched-character `夕食` from `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 晩餐.

### 2026-08-30, iteration 1956 — [[words/晩餐|晩餐]]

No stand-in relationship (both 晩 and 餐's own stand-ins are themselves). Fixed real bug: `mandarin`/`cantonese` had both been contaminated with sibling word [[晩飯]]'s readings — corrected to compositional wǎncān/maan5 caan1. Removed mismatched-character `晚飯` from `aliases`. Filled blank `vietnamese: vãn xan`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 普通.

### 2026-08-30, iteration 1957 — [[words/普通|普通]]

This word is itself the stand-in that legitimizes the character 普 (通's own stand-in is itself). Removed redundant `品詞`, omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 普通話.

### 2026-08-30, iteration 1958 — [[words/普通話|普通話]]

No stand-in relationship (普's own stand-in is [[普通]]; 通/話's own are themselves). Removed redundant `品詞`, added `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 普遍.

### 2026-08-30, iteration 1959 — [[words/普遍|普遍]]

No stand-in relationship (普's own stand-in is [[普通]]; 遍's own is itself). Quoted string fields. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 景致.

### 2026-08-30, iteration 1960 — [[words/景致|景致]]

No stand-in relationship (景's own stand-in is [[景色]]; 致's own is itself). Fixed missing space in `cantonese`, filled blank `vietnamese: cảnh trí` (a genuine standard term). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 景色.

### 2026-08-30, iteration 1961 — [[words/景色|景色]]

This word is itself the stand-in that legitimizes the character 景 (色's own stand-in is [[色彩]]); synonymous with [[風景]]. Fixed real bug: `cantonese` had the wrong initial (sing2→ging2). Filled missing `korean: 경색` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 晴朗.

### 2026-08-30, iteration 1962 — [[words/晴朗|晴朗]]

This word is itself the stand-in that legitimizes the character 晴 (朗's own stand-in is [[明朗]]). Filled blank `vietnamese: thanh lãng` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 晶金.

### 2026-08-30, iteration 1963 — [[words/晶金|晶金]]

Periodic-table neologism (zirconium). Fixed a stray non-breaking space (U+00A0) in `japanese` via byte-level substitution, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 智慧.

### 2026-08-30, iteration 1964 — [[words/智慧|智慧]]

This word is itself the stand-in that legitimizes the character 智 (慧's own stand-in is itself). Fixed missing space in `cantonese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暑.

### 2026-08-30, iteration 1965 — [[words/暑|暑]] / [[words/所|所]]

Both are stand-ins for their own characters. Discovered genuine Dan'a'yo-level homophone pair (both syo/쇼/ㄙ⼄), previously undocumented — checked thirteen other candidates (序/庶/徐/屿/抒/叙/恕/書/署/緒/胥/黍/鼠) and confirmed none independent at this reading. 所's own page was already richly documented but had a redundant `品詞` and a bloated three-way `vietnamese` list, simplified to sở. Added canonical reciprocal `>[!warning] Homophones` callouts to both. Both stamped `date-last-perfect: 2026-08-30`.

Next: 暖.

### 2026-08-30, iteration 1966 — [[words/暖|暖]]

This word is itself the stand-in for its own character. Fixed real bug: literal `vietnamese: null`, corrected to noãn (rejecting the character's contaminating alternate reading hoãn, "postpone"). Filled blank `pos`/`japanese`/`hsk_level`. No word-level homophones (難 bound to [[困難]]). Stamped `date-last-perfect: 2026-08-30`.

Next: 暗.

### 2026-08-30, iteration 1967 — [[words/暗|暗]]

This word is itself the stand-in for its own character. Fixed real bugs: literal `vietnamese: null` and `羅馬字` missing its leading glottal marker (am→'am). Filled blank `pos`/`japanese`/`hsk_level`. No word-level homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暗暗.

### 2026-08-30, iteration 1968 — [[words/暗暗|暗暗]]

A reduplication of [[暗]]; no stand-in relationship applies. Filled missing `korean`/`vietnamese` (both compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暗殺.

### 2026-08-30, iteration 1969 — [[words/暗殺|暗殺]]

No stand-in relationship (both 暗 and 殺's own stand-ins are themselves). Quoted `hsk_level`, reformatted inline-flow `characters`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暗礁.

### 2026-08-30, iteration 1970 — [[words/暗礁|暗礁]]

This word is itself the stand-in that legitimizes the character 礁. Filled blank `vietnamese: ám tiêu` (compositional). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暗示.

### 2026-08-30, iteration 1971 — [[words/暗示|暗示]]

No stand-in relationship (暗's own stand-in is itself; 示's own is [[開示]]). Fixed real bug: `cantonese` had the wrong tone (am4→am3). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暗黒.

### 2026-08-30, iteration 1972 — [[words/暗黒|暗黒]]

No stand-in relationship (both 暗 and 黒's own stand-ins are themselves). Filled blank `korean`/`vietnamese` compositionally (암흑, ám hắc), added `kwin: false` (諺文 암훅 ≠ real Korean 암흑), reformatted `characters`/`aliases` to block-list YAML, and removed `暗黑的`/`黑暗的` from `aliases` (adjectival `的`-suffixed forms, not the noun) while keeping the genuine variant `闇黒`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暢達.

### 2026-08-30, iteration 1973 — [[words/暢達|暢達]]

This word is itself the stand-in for 暢; 達's own stand-in is itself (has its own word page). Corrected an inaccurate Etymology note claiming 達's `vietnamese` lacked "đạt" (it's actually listed there). Reformatted `mandarin` (removed stray space), `characters` to block-list YAML with "(char)" suffix on 達, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暦.

### 2026-08-30, iteration 1974 — [[words/暦|暦]]

This word is itself the stand-in for 暦. Added the missing `japanese` field (れき) and `hsk_level: "3"`, both matching the character's own citation exactly otherwise. No word-level homophones (bound characters 歴/栃 share the reading but have no independent word pages). Stamped `date-last-perfect: 2026-08-30`.

Next: 暦数.

### 2026-08-30, iteration 1975 — [[words/暦数|暦数]]

Filled blank `japanese`/`korean`/`vietnamese` compositionally (れきすう, 력수, lịch số), added `kwin: false` (諺文 럭수 ≠ real Korean 력수), removed blank `hsk_level`/`swadesh`, reformatted `characters`/`aliases` to block-list YAML. Noted (not a bug) that this compound's `cantonese` sou3 reflects 数's noun sense, distinct from its own citation's verb-sense sou2 (used in its stand-in 計数). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暴.

### 2026-08-30, iteration 1976 — [[words/暴|暴]]

This word is itself the stand-in for 暴. Added missing `pos`/`japanese` fields, fixed literal `vietnamese: null` → bộc, added `hsk_level: "3"`. No word-level homophones (bound characters 僕/剝/卜/瀑/爆 share the reading but have no independent word pages). Stamped `date-last-perfect: 2026-08-30`.

Next: 暴徒.

### 2026-08-30, iteration 1977 — [[words/暴徒|暴徒]]

No stand-in relationship (both 暴 and 徒's own stand-ins are themselves). Filled blank `vietnamese` with the real reading bạo đồ; flagged that Korean 폭도 and Vietnamese bạo đồ use real alternate readings of 暴 (폭/bạo) missing from the character's own citation (only 포/bộc stored) — a character-level gap for future perfecting, not fixed here. Reformatted `characters` to block-list YAML, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暴怒.

### 2026-08-30, iteration 1978 — [[words/暴怒|暴怒]]

No stand-in relationship (both 暴 and 怒's own stand-ins are themselves). Filled blank `korean`/`vietnamese` with the real readings 폭노/bạo nộ, matching the same 暴-as-first-element citation gap flagged on [[暴徒]] and consistent with sibling compounds 暴風/暴飲/暴政/暴食. Added `kwin: false`, removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暴政.

### 2026-08-30, iteration 1979 — [[words/暴政|暴政]]

No stand-in relationship (both 暴 and 政's own stand-ins are themselves). Korean/Vietnamese already correctly used the 폭/bạo alternate readings of 暴 (same pattern flagged on [[暴徒]]). Removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暴虐.

### 2026-08-30, iteration 1980 — [[words/暴虐|暴虐]]

This word is itself the stand-in for 虐; 暴's own stand-in is itself. Filled blank `cantonese`/`vietnamese` (bou6 joek6, bạo ngược). Noted korean 포학 correctly uses 暴's standalone 포 reading (a real lexical exception to the 폭-pattern seen in sibling 暴-compounds). Removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暴食.

### 2026-08-30, iteration 1981 — [[words/暴食|暴食]]

No stand-in relationship (both 暴 and 食's own stand-ins are themselves). Filled blank `vietnamese` (bạo thực, using the same 暴 alternate reading pattern flagged on [[暴徒]]). Removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 暴飲.

### 2026-08-30, iteration 1982 — [[words/暴飲|暴飲]]

No stand-in relationship (both 暴 and 飲's own stand-ins are themselves). Filled blank `vietnamese` (bạo ẩm, same 暴 alternate reading pattern flagged on [[暴徒]]). Removed blank `hsk_level`/`swadesh`, reformatted `characters`/`aliases` to block-list YAML (kept genuine simplified variant 暴饮). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 曇.

### 2026-08-30, iteration 1983 — [[words/曇|曇]]

This word is itself the stand-in for 曇. Added missing `pos`/`japanese` fields and `hsk_level: "無"`. Discovered a genuine homophone with [[痰]] (both ㄉㄚㄇ) — fully fixed and cross-referenced both sides: 痰.md got literal `vietnamese: null` → đàm fixed, `pos: 名詞`/`japanese: たん`/`hsk_level: "4"` added (its own stand-in), plus the reciprocal Homophones callout. No other candidates (湛/啖/担/淡/胆/譚/談 all share the 注音 but are bound with no independent word pages). Stamped `date-last-perfect: 2026-08-30` on both.

Next: 曜日.

### 2026-08-30, iteration 1984 — [[words/曜日|曜日]]

This word is itself the stand-in for 曜; 日's own stand-in is itself. Filled blank `cantonese`/`vietnamese` compositionally (jiu6 jat6, diệu nhật). Flagged that 曜's own `hsk_level` is an empty string rather than "無" despite its HSK-No lookup listing — character-level gap, not fixed here. Removed blank `hsk_level`/`swadesh`/`aliases: []`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 曰.

### 2026-08-30, iteration 1985 — [[words/曰|曰]]

This word is itself the stand-in for 曰. Simplified `cantonese`/`japanese` to match the character's own citation (dropped unsupported extra variant readings jyut6/をち), filled `hsk_level: "4"`, removed blank `swadesh`, empty `aliases: []`, and the stray character-schema field `hanmun_edu_level`. Reformatted the existing 3-way homophone group with [[月]] and [[越]] (all 注音 ⼔ㄊ) to the canonical multi-line callout on all three pages; also fully perfected [[越]] in the process (was missing `pos`/`japanese`/`vietnamese`/`hsk_level`) and re-stamped [[月]] for the formatting fix. Stamped `date-last-perfect: 2026-08-30` on all three.

Next: 曲折.

### 2026-08-30, iteration 1986 — [[words/曲折|曲折]]

No stand-in relationship (曲's own stand-in is [[歌曲]]; 折's own is [[折畳]]). Filled blank `vietnamese` (khúc chiết), removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 更.

### 2026-08-30, iteration 1987 — [[words/更|更]]

This word is itself the stand-in for 更. Filled blank `vietnamese` (cánh, the "more" sense, distinct from canh used for the "change" sense in [[更新]]), added missing `pos`/`japanese`/`hsk_level`. No word-level homophones (many bound characters share the reading but none has an independent word page). Stamped `date-last-perfect: 2026-08-30`.

Next: 更少.

### 2026-08-30, iteration 1988 — [[words/更少|更少]]

No stand-in relationship (both 更 and 少's own stand-ins are themselves). Replaced contaminated `japanese`/`korean` (よりなく native phrase, 더 unrelated native "more") with correct compositional forms (こうしょう, 갱소), filled blank `cantonese`/`vietnamese`, fixed stray space in `mandarin`, removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML with "(char)" suffix on both (each has its own word page). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 更新.

### 2026-08-30, iteration 1989 — [[words/更新|更新]]

No stand-in relationship (both 更 and 新's own stand-ins are themselves). Flagged that `mandarin` gēngxīn uses 更's "change" reading (gēng), missing from the character's own citation (only "gèng" stored) — character-level gap for future perfecting. Removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML with "(char)" suffix on both. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 更迭.

### 2026-08-30, iteration 1990 — [[words/更迭|更迭]]

This word is itself the stand-in for 迭. Flagged that `mandarin`/`korean` use real alternate readings of 更 (gēng/경, "change" sense) missing from its citation, same gap as [[更新]]. Filled blank `vietnamese` (canh điệt), added `hsk_level: "無"` (matching 迭). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 書房.

### 2026-08-30, iteration 1991 — [[words/書房|書房]]

This word is itself the stand-in for 房; 書's own stand-in is [[書本]]. Added missing `pos: 名詞`, removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 書法.

### 2026-08-30, iteration 1992 — [[words/書法|書法]]

This word is itself the stand-in for 法; 書's own stand-in is [[書本]]. Fixed real bug: `japanese` しょはう → しょほう (法's on-reading is ほう, not はう). Removed redundant `品詞`, filled `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 書簡.

### 2026-08-30, iteration 1993 — [[words/書簡|書簡]]

No stand-in relationship (書's own stand-in is [[書本]]; 簡's own is [[簡単]]). Fixed real bug: `cantonese` was contaminated (sau2 zi2 → syu1 gaan2). Filled blank `vietnamese`/`pos`, removed synonym entries 片紙/便紙/手紙 from `aliases` (unrelated character 紙, not orthographic variants). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 書籍.

### 2026-08-30, iteration 1994 — [[words/書籍|書籍]]

This word is itself the stand-in for 籍; 書's own stand-in is [[書本]]. Filled blank `vietnamese`/`pos`, removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 曼魚.

### 2026-08-30, iteration 1995 — [[words/曼魚|曼魚]]

Rebus-substitution word (曼 stands in for the pageless real character 鰻 "eel", per 曼's own documented Notes). Fixed real bug: `korean` was the native descriptive word 뱀장어, replaced with the compositional Sino-Korean form 만어. Cleaned `mandarin` (dropped the extra mányú variant to a prose note), added `hsk_level: "無"`, reformatted `characters`/`aliases` to block-list YAML. Confirmed `japanese` むなぎ is a genuine archaic form, not a typo. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 曽.

### 2026-08-30, iteration 1996 — [[words/曽|曽]]

This word is itself the stand-in for 曽. Filled blank `vietnamese` (từng, matching the character's citation) and added missing `pos`/`japanese`/`hsk_level`; flagged that the real-world standard reading "tằng" is missing from the character's own citation, a character-level gap for future perfecting. No word-level homophones (増/憎/贈 share the reading but have no independent word pages). Stamped `date-last-perfect: 2026-08-30`.

Next: 曽子.

### 2026-08-30, iteration 1997 — [[words/曽子|曽子]]

No stand-in relationship (曽's own stand-in is itself; 子's own is [[児子]]). Removed a false "same sound as 中指" tip callout — checked all five languages plus 注音, none actually match. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 最.

### 2026-08-30, iteration 1998 — [[words/最|最]]

This word is itself the stand-in for 最. Fixed literal `vietnamese: null` → tối, added missing `pos`/`japanese`/`hsk_level`, `kwin: false` (諺文 줘 ≠ real Korean 최, a genuine divergence). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 最善.

### 2026-08-30, iteration 1999 — [[words/最善|最善]]

No stand-in relationship (both 最 and 善's own stand-ins are themselves). Filled blank `vietnamese` (tối thiện), removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 最大.

### 2026-08-30, iteration 2000 — [[words/最大|最大]]

No stand-in relationship (both 最 and 大's own stand-ins are themselves). Filled blank `vietnamese` (tối đại), reformatted `characters` with "(char)" quoting. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 最高点.

### 2026-08-30, iteration 2001 — [[words/最高点|最高点]]

No stand-in relationship (最, 高, 点's own stand-ins are all themselves). Filled blank `vietnamese` (tối cao điểm), quoted `characters` values consistently. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月中.

### 2026-08-30, iteration 2002 — [[words/月中|月中]]

No stand-in relationship (both 月 and 中's own stand-ins are themselves). Filled blank `korean`/`japanese`/`vietnamese`, added `kwin: false` (same 月-coda divergence documented on [[月]]), removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月刊.

### 2026-08-30, iteration 2003 — [[words/月刊|月刊]]

No stand-in relationship (both 月 and 刊's own stand-ins are themselves). Fixed real bug: `vietnamese` typo (guyệt san → nguyệt san). Removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月初.

### 2026-08-30, iteration 2004 — [[words/月初|月初]]

No stand-in relationship (月's own stand-in is itself; 初's own is [[最初]]). Fixed real bug: `cantonese` was contaminated (yue2 cu1 → jyut6 co1). Filled blank `vietnamese`, corrected `kwin` true→false (same 月-coda divergence as [[月]]), removed redundant `品詞`, reformatted `japanese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月曜日.

### 2026-08-30, iteration 2005 — [[words/月曜日|月曜日]]

No stand-in relationship (this compound is itself 曜's stand-in; 月/日's own stand-ins are themselves). Confirmed `vietnamese` thứ hai (native weekday name) matches the established convention on 日曜日/火曜日/水曜日 rather than being a bug. Removed the stray character-schema field `graphemic_classification`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月経.

### 2026-08-30, iteration 2006 — [[words/月経|月経]]

No stand-in relationship (both 月 and 経's own stand-ins are themselves). Filled blank `vietnamese`/`pos`, removed blank `hsk_level`/`swadesh`, reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月虹.

### 2026-08-30, iteration 2007 — [[words/月虹|月虹]]

This word is itself the stand-in for 虹; 月's own stand-in is itself. Fixed real bug: `korean` was garbled with an unclear extra value, simplified to clean compositional 월홍. Filled blank `vietnamese`, added `kwin: false` (same 月-coda divergence as [[月]]). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 月食.

### 2026-08-30, iteration 2008 — [[words/月食|月食]]

No stand-in relationship (both 月 and 食's own stand-ins are themselves). Fixed real bug: `cantonese` typo (jyu6 → jyut6). Corrected `kwin` true→false (same 月-coda divergence as [[月]]). Filled `pos`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 有机.

### 2026-08-30, iteration 2009 — [[words/有机|有机]]

No stand-in relationship (有's own stand-in is itself; 机's own is [[机会]]). Removed self-referential `有机` from `aliases`, kept genuine traditional variant `有機`. Removed blank `hsk_level`/`swadesh`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 有様.

### 2026-08-30, iteration 2010 — [[words/有様|有様]]

Discovered this is a rebus-substitution word: 有 stands in for the pageless character 宥 ("forgiving, lenient"), matching the 曼魚 pattern — `mandarin`/`cantonese`/`japanese` already correctly held 宥's real readings (yòu/jau6/ゆるす), not 有's own (yǒu/jau5). Filled blank `korean`/`vietnamese` with 宥's corresponding readings (유, hựu), added `kwin: false`. Flagged that 有's own character page doesn't yet document this substitution (unlike 曼's page for 鰻) — worth adding on a future character-perfecting pass. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 有生.

### 2026-08-30, iteration 2011 — [[words/有生|有生]]

No stand-in relationship (有's own stand-in is itself; 生's own is [[生活]]). Filled blank `japanese`/`korean`/`vietnamese` compositionally. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 服務員.

### 2026-08-30, iteration 2012 — [[words/服務員|服務員]]

No stand-in relationship (服's own stand-in is [[服事]]; 務's own is [[服務]]; 員's own is [[人員]]). Filled blank `japanese`/`korean`/`vietnamese`, added `kwin: false`, fixed bare-integer `hsk_level`. Flagged that 員's own stored Korean citation (운) diverges from the real-world standard 원 — character-level question for future perfecting. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 服従.

### 2026-08-30, iteration 2013 — [[words/服従|服従]]

This word is itself the stand-in for 従; 服's own stand-in is [[服事]]. Filled blank `vietnamese` (phục tùng). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 朔日.

### 2026-08-30, iteration 2014 — [[words/朔日|朔日]]

This word is itself the stand-in for 朔; 日's own stand-in is itself. Fixed stray space in `mandarin`, filled blank `vietnamese`/`hsk_level: "無"`, removed empty `aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 朝鮮.

### 2026-08-30, iteration 2015 — [[words/朝鮮|朝鮮]]

No stand-in relationship (朝's own stand-in is itself; 鮮's own is [[新鮮]]). Documented a genuine sense-specific reading split on 鮮 (셤/-m for "fresh" vs 션/-n reserved for this country name and [[朝鮮正音]]/旗幟鮮明), confirmed consistent across the vault rather than a bug. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 期.

### 2026-08-30, iteration 2016 — [[words/期|期]]

This word is itself the stand-in for 期. Added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[起]] (both ㄎㄧ) — fully fixed and cross-referenced both sides: 起.md got literal `vietnamese: null` → khởi fixed, missing `pos`/`japanese`/`hsk_level` added (its own stand-in), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-30` on both.

Next: 期間.

### 2026-08-30, iteration 2017 — [[words/期間|期間]]

No stand-in relationship (期's own stand-in is itself; 間's own is [[之間]]). Simplified `mandarin` (dropped extra tone-sandhi variant), filled blank `vietnamese`, fixed bare-integer `hsk_level`, removed blank `swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 木偶.

### 2026-08-30, iteration 2018 — [[words/木偶|木偶]]

This word is itself the stand-in for 偶; 木's own stand-in is itself. Fixed real bug: `vietnamese` was contaminated with an unrelated native phrase (tượng gỗ) — corrected to compositional mộc ngẫu. Confirmed Japanese でく is a genuine jukujikun, not a bug. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 木星.

### 2026-08-30, iteration 2019 — [[words/木星|木星]]

This word is itself the stand-in for 星; 木's own stand-in is itself. Simplified doubled `vietnamese` ("Sao Mộc, Mộc tinh") to a single form matching the already-perfected sibling [[土星]]'s format. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 木版.

### 2026-08-30, iteration 2020 — [[words/木版|木版]]

No stand-in relationship (木's own stand-in is itself; 版's own is itself). Filled blank `vietnamese`. Discovered a genuine homophone with [[木板]] ("board, plank," both ㄇㄛㄎㄆㄚㄋ) — fully fixed and cross-referenced both sides: 木板.md got missing `japanese`/`vietnamese` filled, `kwin` corrected false→true, plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-30` on both.

Next: 未月.

### 2026-08-30, iteration 2021 — [[words/未月|未月]]

This word is itself the stand-in for 未. Confirmed `japanese`/`vietnamese` already correctly follow the established native-kun'yomi + zodiac-name convention (see [[寅月]], [[卯月]]) rather than being bugs. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 末梢.

### 2026-08-30, iteration 2022 — [[words/末梢|末梢]]

This word is itself the stand-in for 梢; 末's own stand-in is [[末端]]. Filled blank `vietnamese` (mạt tiêu). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 末端.

### 2026-08-30, iteration 2023 — [[words/末端|末端]]

Confirmed `#cranberry` tag is correct: both 末 and 端's own stand-ins point to this compound (transitivity holds, A=B=AB). Filled blank `vietnamese` (mạt đoan). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 本.

### 2026-08-30, iteration 2024 — [[words/本|本]]

This word is itself the stand-in for 本. Added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`. No word-level homophones (坂/奔/飯 share the reading but have no independent word pages). Stamped `date-last-perfect: 2026-08-30`.

Next: 本塁打.

### 2026-08-30, iteration 2025 — [[words/本塁打|本塁打]]

No stand-in relationship (本's own stand-in is itself; 塁's own is [[壁塁]]; 打's own is [[打撃]]). Filled blank `vietnamese`, reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 本来.

### 2026-08-30, iteration 2026 — [[words/本来|本来]]

No stand-in relationship (both 本 and 来's own stand-ins are themselves). Filled blank `vietnamese`, fixed bare-integer `hsk_level`, reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 本校.

### 2026-08-30, iteration 2027 — [[words/本校|本校]]

No stand-in relationship (本's own stand-in is itself; 校's own is [[学校]]). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 本質.

### 2026-08-30, iteration 2028 — [[words/本質|本質]]

No stand-in relationship (本's own stand-in is itself; 質's own is [[質素]]). Simplified `mandarin` (dropped extra variant), removed self-referential `本質` from `aliases` (kept genuine simplified 本质), removed blank `swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 札.

### 2026-08-30, iteration 2029 — [[words/札|札]]

This word is itself the stand-in for 札. Fixed literal `vietnamese: null` → trát, added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[紮]] (both ㄐㄚㄊ) — fully fixed and cross-referenced both sides: 紮.md got missing `japanese`/`hsk_level` added (its own stand-in), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-30` on both.

Next: 朱沙.

### 2026-08-30, iteration 2030 — [[words/朱沙|朱沙]]

This word is itself the stand-in for 沙, and (per 朱's own Words section) also for 朱, despite 朱's frontmatter stand_in field reading "朱砂" instead of "朱沙" — flagged as a minor character-level inconsistency for future perfecting. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 朴木.

### 2026-08-30, iteration 2031 — [[words/朴木|朴木]]

This word is itself the stand-in for 朴; 木's own stand-in is itself. Fixed real bugs: `mandarin` had the wrong tone and was missing the 木 half (pò → pǔmù); `cantonese` was likewise missing the 木 half (pok3 → pok3 muk6). Confirmed Japanese ほほのき is a genuine native term, not a bug. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 机械.

### 2026-08-30, iteration 2032 — [[words/机械|机械]]

This word is itself the stand-in for 械 (机's graphemic form of 機). All readings already correct/compositional. Quoted scalar values for consistency, reformatted field order. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 杆.

### 2026-08-30, iteration 2033 — [[words/杆|杆]]

This word is itself the stand-in for 杆. Added missing `pos`/`japanese`/`hsk_level`/`kwin: true`. No word-level homophones (many bound characters share the reading but none has an independent word page). Stamped `date-last-perfect: 2026-08-30`.

Next: 杏月.

### 2026-08-30, iteration 2034 — [[words/杏月|杏月]]

No stand-in relationship (杏's own stand-in is [[杏子]]; 月's own is itself). Confirmed `japanese`/`vietnamese` follow the established native-kun'yomi + zodiac/poetic-name convention (see [[寅月]], [[卯月]], [[未月]]). Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 材木.

### 2026-08-30, iteration 2035 — [[words/材木|材木]]

No stand-in relationship (材's own stand-in is [[材料]]; 木's own is itself). Fixed severe contamination: `mandarin`/`cantonese`/`japanese` had all been swapped for the reversed-order compound 木材's readings instead of 材木's own; `korean` held 제목 ("title," an unrelated word); `vietnamese` held two garbled native phrases instead of a real translation. Removed 木料/木材 from `aliases` (distinct synonym compounds, not orthographic variants). No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 杖.

### 2026-08-30, iteration 2036 — [[words/杖|杖]]

This word is itself the stand-in for 杖. Added missing `japanese`/`hsk_level`. Reformatted the existing 3-way homophone group with [[長]] (already complete) and [[章]] (all 注音 ㄐㄚㄫ) to the canonical multi-line callout on all three pages; also fully perfected [[章]] in the process (removed redundant `品詞`, added Notes). Stamped `date-last-perfect: 2026-08-30` on both 杖 and 章.

Next: 杜金.

### 2026-08-30, iteration 2037 — [[words/杜金|杜金]]

Periodic-table neologism (dubnium); confirmed `mandarin`/`cantonese` use 杜's own reading directly (not an avoided-character substitution, unlike [[丹金]]'s pattern), and `korean`/`japanese`/`vietnamese` correctly hold IUPAC loanword transcriptions. Confirmed existing reciprocal homophone tip with [[鍍金]] is correct and consistent. Quoted/reformatted YAML. Stamped `date-last-perfect: 2026-08-30`.

Next: 束縛.

### 2026-08-30, iteration 2038 — [[words/束縛|束縛]]

This word is itself the stand-in for 縛; 束's own stand-in is itself. Simplified `mandarin`, filled blank `vietnamese`/`pos`, removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-30`.

Next: 条約.

### 2026-08-31, iteration 2039 — [[words/条約|条約]]

No stand-in relationship (条's own stand-in is itself; 約's own is [[約束]]). Fixed bare-integer `hsk_level`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 来世紀.

### 2026-08-31, iteration 2040 — [[words/来世紀|来世紀]]

No stand-in relationship (来's own stand-in is itself; builds on [[世紀]], itself the stand-in for 紀; 世's own is [[世界]]). Fixed real bug: `korean` was a native descriptive phrase (다음세기) instead of the compositional form — corrected to 래세기. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 来年.

### 2026-08-31, iteration 2041 — [[words/来年|来年]]

No stand-in relationship (both 来 and 年's own stand-ins are themselves). Fixed real bug: `korean` was the South Korean 두음법칙-shifted form 내년 — corrected to North Korean/문화어 래년 per the permanent vault convention. Filled blank `vietnamese`, reformatted YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 来日.

### 2026-08-31, iteration 2042 — [[words/来日|来日]]

No stand-in relationship (both 来 and 日's own stand-ins are themselves). Fixed severe contamination: `mandarin`/`cantonese`/`vietnamese`/`japanese` had all been copied/garbled from the unrelated compound [[明日]] — corrected to 来+日's own compositional readings. Fixed `korean` South Korean 두음법칙 shift (내일→래일) per the North Korean vault convention. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 来月.

### 2026-08-31, iteration 2043 — [[words/来月|来月]]

No stand-in relationship (both 来 and 月's own stand-ins are themselves). Fixed real bug: `korean` was a garbled comma-joined pair mixing a South Korean shifted form with a native phrase — corrected to single North Korean form 래월. Filled blank `vietnamese`, added `kwin: false` (same 月-coda divergence as [[月]]), removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 来臨.

### 2026-08-31, iteration 2044 — [[words/来臨|来臨]]

This word is itself the stand-in for 臨. Fixed real bugs: `korean` was a native verb (다가가다) instead of the compositional form — corrected to 래림; removed stray する suffix from `japanese`. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 来週.

### 2026-08-31, iteration 2045 — [[words/来週|来週]]

No stand-in relationship (来's own stand-in is itself; 週's own is [[週日]]). Fixed severe contamination: `mandarin`/`cantonese` had been copied from unrelated compound 下週/下周 — corrected to 来's/週's own compositional readings; `korean` held a native phrase (다음주) instead of the compositional 래주. Filled blank `vietnamese`, removed 下周/下週 from `aliases` (different character, not an orthographic variant). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 杪小.

### 2026-08-31, iteration 2046 — [[words/杪小|杪小]]

This word is itself the stand-in for 杪. Filled blank `vietnamese`. Fixed wrong field name `alias:` and removed `渺小` (a homophone-based near-synonym using a different character, not a genuine alias). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東亜.

### 2026-08-31, iteration 2047 — [[words/東亜|東亜]]

No stand-in relationship (東's own stand-in is [[東方]]; 亜's own is [[亜細亜]]). Simplified `mandarin` (dropped extra variant), removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東京.

### 2026-08-31, iteration 2048 — [[words/東京|東京]]

No stand-in relationship (東's own stand-in is [[東方]]; 京's own is [[京城]]). Simplified `korean` to the compositional Sino-Korean exonym 동경 (dropped modern loanword 도쿄), matching sibling city-name convention ([[北京]]). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東北.

### 2026-08-31, iteration 2049 — [[words/東北|東北]]

No stand-in relationship (東's own stand-in is [[東方]]; 北's own is [[北方]]). Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東南.

### 2026-08-31, iteration 2050 — [[words/東南|東南]]

No stand-in relationship (東's own stand-in is [[東方]]; 南's own is [[南方]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東南亜.

### 2026-08-31, iteration 2051 — [[words/東南亜|東南亜]]

No stand-in relationship (東's own stand-in is [[東方]]; 南's own is [[南方]]; 亜's own is [[亜細亜]]). Confirmed `japanese` とうなんあ is the vault's compositional convention (distinct from real-world 東南アジア), not a bug. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東夷.

### 2026-08-31, iteration 2052 — [[words/東夷|東夷]]

This word is itself the stand-in for 夷; 東's own stand-in is [[東方]]. Filled blank `japanese`/`vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東方.

### 2026-08-31, iteration 2053 — [[words/東方|東方]]

This word is itself the stand-in for 東 (has no independent word page); 方's own stand-in is [[方向]]. Fixed real bug: `cantonese` was garbled with pinyin-style spelling instead of Jyutping (dong1 fang1 → dung1 fong1). Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東端.

### 2026-08-31, iteration 2054 — [[words/東端|東端]]

No stand-in relationship (東's own stand-in is [[東方]]; 端's own is [[末端]]). Filled blank `cantonese`/`vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 東芝.

### 2026-08-31, iteration 2055 — [[words/東芝|東芝]]

No stand-in relationship (東's own stand-in is [[東方]]; 芝's own is 名専字, name-only). Filled blank `vietnamese`. Reformatted the existing homophone callout with [[同志]] to the canonical multi-line format on both pages; also fixed a bare-integer `hsk_level` bug on 同志.md while there. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 東部.

### 2026-08-31, iteration 2056 — [[words/東部|東部]]

This word is itself the stand-in for 部; 東's own stand-in is [[東方]]. Fixed real bug: `cantonese` had the same garbled pinyin-style spelling as [[東方]] (dong1 bou6 → dung1 bou6). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 松.

### 2026-08-31, iteration 2057 — [[words/松|松]]

This word is itself the stand-in for 松. Added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[訟]] (both 숑) — fully fixed and cross-referenced both sides: 訟.md (already stamped 2026-08-10, missing its half) got the reciprocal Homophones callout added retroactively. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 松竹梅.

### 2026-08-31, iteration 2058 — [[words/松竹梅|松竹梅]]

No stand-in relationship (松's own stand-in is itself; 竹's own is itself; 梅's own is [[梅花]]). Fixed a real byte-level bug: `諺文`'s first syllable was the visually-similar-but-distinct codepoint 쇽 (U+C1FD) instead of 숑 (U+C211), while `羅馬字` already had it right. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 板球.

### 2026-08-31, iteration 2059 — [[words/板球|板球]]

No stand-in relationship (板's own stand-in is [[木板]]; 球's own is itself). Confirmed `japanese`/`korean` loanwords (no real-world compositional term exists for cricket in these languages) are correct as-is, not a bug. Filled blank `vietnamese` (loanword, same reasoning). Removed empty `aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 枕頭.

### 2026-08-31, iteration 2060 — [[words/枕頭|枕頭]]

This word is itself the stand-in for 枕; 頭's own stand-in is itself. Fixed real bug: `korean` was 枕's native-Korean field value (베개) instead of its compositional 침 — corrected to 침두. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 林.

### 2026-08-31, iteration 2061 — [[words/林|林]]

This word is itself the stand-in for 林. Added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[淋]] (both 림) — fully fixed and cross-referenced both sides: 淋.md got missing `japanese`/`kwin` added (its own stand-in), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 林業.

### 2026-08-31, iteration 2062 — [[words/林業|林業]]

No stand-in relationship (both 林 and 業's own stand-ins are themselves). Fixed real bugs: `cantonese` missing internal space; `japanese` used an obsolete historical kana spelling (りんげふ) instead of modern りんぎょう (verified against every other 業-compound in the vault); `korean` was the South Korean shifted form (임업) instead of North Korean 림업. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 果子.

### 2026-08-31, iteration 2063 — [[words/果子|果子]]

No stand-in relationship (果's own stand-in is [[果実]]; 子's own is [[児子]]). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 果汁.

### 2026-08-31, iteration 2064 — [[words/果汁|果汁]]

No stand-in relationship (果's own stand-in is [[果実]]; 汁's own is itself). Fixed real bug: `vietnamese` was a native descriptive phrase (Nước sinh tố) instead of the compositional form — corrected to quả chấp. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 果醤.

### 2026-08-31, iteration 2065 — [[words/果醤|果醤]]

This word is itself the stand-in for 醤. Confirmed `japanese`/`korean` loanwords (no real-world compositional term exists for jam) are correct, same pattern as [[板球]]. Filled blank `vietnamese` with the compositional form. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 枢.

### 2026-08-31, iteration 2066 — [[words/枢|枢]]

This word is itself the stand-in for 枢. Added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine 3-way homophone group with [[臭]] and [[趨]] (all 추) — fully fixed and cross-referenced all three: 臭.md got blank `japanese`/`vietnamese` filled, 趨.md got blank `japanese` filled, plus full mutual Homophones callouts on all three. Stamped `date-last-perfect: 2026-08-31` on all three.

Next: 枢机.

### 2026-08-31, iteration 2067 — [[words/枢机|枢机]]

No stand-in relationship (枢's own stand-in is itself; 机's own is [[机会]]). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 枢机卿.

### 2026-08-31, iteration 2068 — [[words/枢机卿|枢机卿]]

No stand-in relationship (枢's own stand-in is itself; 机's own is [[机会]]; 卿's own is itself). Fixed real bug: `mandarin` was missing the 卿 syllable entirely (shūjī → shūjīqīng). Filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 枯.

### 2026-08-31, iteration 2069 — [[words/枯|枯]]

This word is itself the stand-in for 枯. Fixed literal `vietnamese: null` → khô, added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine 3-way homophone group with [[苦]] and [[袴]] (all 코) — fully fixed and cross-referenced all three: 苦.md got missing `pos`/`japanese`/`hsk_level`/`vietnamese` filled (flagged a malformed comma-joined vietnamese string on 苦's own character citation for future perfecting), 袴.md got missing `japanese` filled, plus full mutual Homophones callouts on all three. Stamped `date-last-perfect: 2026-08-31` on all three.

Next: 柄.

### 2026-08-31, iteration 2070 — [[words/柄|柄]]

This word is itself the stand-in for 柄. Added missing `japanese`/`hsk_level`. Confirmed the existing 3-way homophone group with [[丙]] and [[坪]] (all 병) was already correctly cross-referenced on all three pages. Stamped `date-last-perfect: 2026-08-31`.

Next: 柄国.

### 2026-08-31, iteration 2071 — [[words/柄国|柄国]]

No stand-in relationship (柄's own stand-in is itself; 国's own is [[国家]]). Fixed real bugs: `mandarin` extra unsupported variant, `cantonese` wrong vowel (bing3→beng3). Filled blank `japanese`/`korean`/`vietnamese`. Removed 秉國 from `aliases` (different character, near-synonym), kept genuine variant 柄國. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 柔.

### 2026-08-31, iteration 2072 — [[words/柔|柔]]

This word is itself the stand-in for 柔. Fixed literal `vietnamese: null` → nhu, added missing `pos`/`japanese`/`hsk_level`. Confirmed the existing homophone with [[牛]] (both 뉴) was already correctly cross-referenced. Stamped `date-last-perfect: 2026-08-31`.

Next: 柔道.

### 2026-08-31, iteration 2073 — [[words/柔道|柔道]]

No stand-in relationship (both 柔 and 道's own stand-ins are themselves). Fixed real bug: `japanese` used an obsolete historical kana spelling (じうだう) instead of modern じゅうどう (verified against 5+ other 道-compounds). Removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 柱.

### 2026-08-31, iteration 2074 — [[words/柱|柱]]

This word is itself the stand-in for 柱. Fixed literal `vietnamese: null` → trụ, added missing `pos`/`japanese`/`hsk_level`. No word-level homophones (many bound characters share the reading but none has an independent word page). Stamped `date-last-perfect: 2026-08-31`.

Next: 柳.

### 2026-08-31, iteration 2075 — [[words/柳|柳]]

This word is itself the stand-in for 柳. Fixed literal `vietnamese: null` → liễu, added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[留]] (both 류) — fully fixed and cross-referenced both sides: 留.md got missing `pos`/`japanese` added, `vietnamese` reformatted, and stray lookup-page bullets removed (belonged on the character page), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 柴棍.

### 2026-08-31, iteration 2076 — [[words/柴棍|柴棍]]

This word is itself the stand-in for 柴; 棍's own stand-in is [[棍棒]]. Confirmed `mandarin`/`cantonese` correctly hold the real exonym 西貢's reading (avoided-name pattern, per [[丹金]]) rather than a bug; documented this explicitly. Reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 柵.

### 2026-08-31, iteration 2077 — [[words/柵|柵]]

This word is itself the stand-in for 柵. Added missing `japanese`/`kwin`. Discovered a genuine homophone with [[冊]] (already stamped 2026-06-29, missing its half) — retroactively added the reciprocal Homophones callout, removed a redundant `品詞` field, and quoted scalars for consistency. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 査問.

### 2026-08-31, iteration 2078 — [[words/査問|査問]]

No stand-in relationship (査's own stand-in is [[調査]]; 問's own is [[質問]]). Flagged that `mandarin` cháwèn uses 査's real alternate reading chá, missing from its own citation (only zhā stored) — character-level gap for future perfecting. Filled blank `japanese`/`korean`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 柿木.

### 2026-08-31, iteration 2079 — [[words/柿木|柿木]]

This word is itself the stand-in for 柿. Fixed real bug: `mandarin` was garbled with the unrelated word 柿子's pinyin (shì zi → shìmù). Fixed `korean` (native 감 → compositional 시목), filled blank `vietnamese`, added `hsk_level: "無"`. Confirmed `japanese` カキノキ is a genuine species-name katakana convention, not a bug. Flagged an internal inconsistency on 柿's own character page for future perfecting. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 栄辱.

### 2026-08-31, iteration 2080 — [[words/栄辱|栄辱]]

No stand-in relationship (栄's own stand-in is [[光栄]]; 辱's own is [[羞辱]]). Simplified `mandarin` (dropped extra variant), filled blank `vietnamese`/`pos`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 栓.

### 2026-08-31, iteration 2081 — [[words/栓|栓]]

This word is itself the stand-in for 栓. Added missing `japanese`/`hsk_level`. No word-level homophones (旋/選 share the reading but have no independent word pages). Stamped `date-last-perfect: 2026-08-31`.

Next: 栗鼠.

### 2026-08-31, iteration 2082 — [[words/栗鼠|栗鼠]]

No stand-in relationship (栗 has its own word page; 鼠's own stand-in is [[熊鼠]]). Fixed real bug: `korean` was a native word (다람쥐) instead of compositional 률서. Confirmed `japanese` りす is a genuine native term, not a bug. Filled blank `vietnamese`, added `hsk_level: "無"`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校内.

### 2026-08-31, iteration 2083 — [[words/校内|校内]]

No stand-in relationship (校's own stand-in is [[学校]]; 内's own is [[内部]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校区.

### 2026-08-31, iteration 2084 — [[words/校区|校区]]

No stand-in relationship (校's own stand-in is [[学校]]; 区's own is [[区域]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校外.

### 2026-08-31, iteration 2085 — [[words/校外|校外]]

No stand-in relationship (校's own stand-in is [[学校]]; 外's own is [[外部]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校服.

### 2026-08-31, iteration 2086 — [[words/校服|校服]]

No stand-in relationship (校's own stand-in is [[学校]]; 服's own is [[服事]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校歌.

### 2026-08-31, iteration 2087 — [[words/校歌|校歌]]

No stand-in relationship (校's own stand-in is [[学校]]; 歌's own is [[歌曲]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校正.

### 2026-08-31, iteration 2088 — [[words/校正|校正]]

No stand-in relationship (校's own stand-in is [[学校]]; 正's own is itself). Flagged that `mandarin`/`cantonese` use 校's real "proofread" polyphonic reading (jiào/gaau3), missing from the character's own citation (only xiào/haau6 stored) — character-level gap for future perfecting. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校舎.

### 2026-08-31, iteration 2089 — [[words/校舎|校舎]]

No stand-in relationship (校's own stand-in is [[学校]]; 舎's own is [[宿舎]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校訂.

### 2026-08-31, iteration 2090 — [[words/校訂|校訂]]

No stand-in relationship (校's own stand-in is [[学校]]; 訂's own is itself). Confirmed `mandarin`/`cantonese` use the same 校 "proofread" polyphonic reading already flagged on [[校正]] — consistent, not a new bug. Reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 校門.

### 2026-08-31, iteration 2091 — [[words/校門|校門]]

No stand-in relationship (校's own stand-in is [[学校]]; 門's own is [[大門]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 株.

### 2026-08-31, iteration 2092 — [[words/株|株]]

This word is itself the stand-in for 株. Fixed literal `vietnamese: null` → châu, added missing `pos`/`japanese`/`hsk_level`. Flagged an internal inconsistency on 株's own character page (諺文/羅馬字 두/du vs its own korean 주) for future perfecting. Completed the genuine homophone with [[兜]] (already anticipated by 兜's own Notes, awaiting this turn) — both pages now fully cross-referenced. Stamped `date-last-perfect: 2026-08-31` on 株 (兜 was already stamped 2026-07-26; only its Notes text updated).

Next: 核.

### 2026-08-31, iteration 2093 — [[words/核|核]]

This word is itself the stand-in for 核. Added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`. Completed the genuine 3-way homophone group with [[嚇]] (already complete, anticipating both) and [[鶴]] (all 학) — fully fixed and cross-referenced all three: 鶴.md got a real Japanese voicing bug fixed (がく→かく), redundant `品詞` removed, `hsk_level: "無"` added. Stamped `date-last-perfect: 2026-08-31` on 核 and 鶴 (嚇 was already stamped 2026-07-27; only its Notes text updated).

Next: 核金.

### 2026-08-31, iteration 2094 — [[words/核金|核金]]

Periodic-table neologism (ytterbium); confirmed `mandarin`/`cantonese` correctly hold the avoided real character 镱's reading, matching the [[丹金]] pattern. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 根.

### 2026-08-31, iteration 2095 — [[words/根|根]]

This word is itself the stand-in for 根. Added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 根拠.

### 2026-08-31, iteration 2096 — [[words/根拠|根拠]]

No stand-in relationship (根's own stand-in is itself; 拠's own is [[依拠]]). Fixed bare-integer `hsk_level`, reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 根本.

### 2026-08-31, iteration 2097 — [[words/根本|根本]]

No stand-in relationship (both 根 and 本's own stand-ins are themselves). Fixed missing space in `cantonese` (gan1bun2 → gan1 bun2), removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 根源.

### 2026-08-31, iteration 2098 — [[words/根源|根源]]

This word is itself the stand-in for 源. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 格.

### 2026-08-31, iteration 2099 — [[words/格|格]]

This word is itself the stand-in for 格. Added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`. Completed the genuine 3-way homophone group with [[各]] and [[隔]] (all 각), already anticipated by both siblings — fully cross-referenced all three. Also removed a redundant `品詞` field on 隔.md while there. Stamped `date-last-perfect: 2026-08-31` on 格 and 隔 (各 was already stamped 2026-07-26; only its Notes text updated).

Next: 格助詞.

### 2026-08-31, iteration 2100 — [[words/格助詞|格助詞]]

No stand-in relationship (格's own stand-in is itself; 助's own is [[援助]]; 詞's own is [[単詞]]). Fixed real bugs: `mandarin`/`cantonese` were entirely blank, filled compositionally; `vietnamese` held placeholder text "sd" instead of real content, corrected to cách trợ từ. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 格式.

### 2026-08-31, iteration 2101 — [[words/格式|格式]]

No stand-in relationship (格's own stand-in is itself; 式's own is [[様式]]). Removed blank `hsk_level`/`swadesh`/`aliases`, reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桁.

### 2026-08-31, iteration 2102 — [[words/桁|桁]]

This word is itself the stand-in for 桁. Added missing `japanese`/`hsk_level`. Reformatted the existing 3-way homophone group with [[行]] (already complete) and [[項]] (all 항) to the canonical multi-line callout on all three pages; also fully perfected [[項]] in the process (fixed literal `vietnamese: null`, added missing `pos`/`japanese`). Stamped `date-last-perfect: 2026-08-31` on 桁 and 項 (行 was already stamped 2026-08-03; only its callout format updated).

Next: 桂月.

### 2026-08-31, iteration 2103 — [[words/桂月|桂月]]

No stand-in relationship (桂's own stand-in is [[肉桂]]; 月's own is itself). Confirmed `japanese`/`vietnamese` correctly follow the established poetic-month native-kun'yomi convention. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桃子.

### 2026-08-31, iteration 2104 — [[words/桃子|桃子]]

This word is itself the stand-in for 桃; 子's own stand-in is [[児子]]. Confirmed all readings already correct (japanese とうし verified compositional). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桃月.

### 2026-08-31, iteration 2105 — [[words/桃月|桃月]]

No stand-in relationship (桃's own stand-in is [[桃子]]; 月's own is itself). Confirmed `japanese`/`vietnamese` follow the established poetic-month convention. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桃果.

### 2026-08-31, iteration 2106 — [[words/桃果|桃果]]

No stand-in relationship (桃's own stand-in is [[桃子]]; 果's own is [[果実]]). Fixed severe contamination: `mandarin` copied from unrelated [[桃子]]; `cantonese` garbled; `japanese` was bare native もも instead of compositional; `korean` was the native word 복숭아 instead of compositional 도과. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桃金.

### 2026-08-31, iteration 2107 — [[words/桃金|桃金]]

Periodic-table neologism (erbium); confirmed `mandarin`/`cantonese` correctly hold the avoided real character 铒's reading, matching the [[丹金]] pattern. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 案件.

### 2026-08-31, iteration 2108 — [[words/案件|案件]]

No stand-in relationship (案's own stand-in is [[提案]]; 件's own is [[事件]]). Fixed a malformed hybrid tone notation in `cantonese` (gin6-2 → gin6), fixed bare-integer `hsk_level`, removed empty `aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桌.

### 2026-08-31, iteration 2109 — [[words/桌|桌]]

This word is itself the stand-in for 桌. Simplified comma-joined `mandarin`/`cantonese`/`vietnamese` to primary forms, flagged the same malformed-string issue on 桌's own character citation for future perfecting. Added missing `pos`/`japanese`/`hsk_level`. No word-level homophones (橐/拓/卓/琢/託 share the reading but have no independent word pages). Stamped `date-last-perfect: 2026-08-31`.

Next: 桌球.

### 2026-08-31, iteration 2110 — [[words/桌球|桌球]]

No stand-in relationship (both 桌 and 球's own stand-ins are themselves). Fixed real bugs: `cantonese` garbled initial (zoek3→cheuk3), `japanese` obsolete kana (たくきう→たくきゅう). Filled blank `vietnamese`/`pos`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桑木.

### 2026-08-31, iteration 2111 — [[words/桑木|桑木]]

This word is itself the stand-in for 桑. Fixed real bugs: `mandarin`/`cantonese` were copied from unrelated compound 桑樹/桑树; `korean` was 桑's own native word (뽕나무) instead of compositional 상목. Confirmed Japanese くわ is a genuine native term, not a bug. Filled blank `vietnamese`, removed 桑樹/桑树 from `aliases` (different character, near-synonym). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桑田.

### 2026-08-31, iteration 2112 — [[words/桑田|桑田]]

No stand-in relationship (桑's own stand-in is [[桑木]]; 田's own is [[田野]]). Filled blank `cantonese`/`korean`/`vietnamese`, removed empty `aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桜.

### 2026-08-31, iteration 2113 — [[words/桜|桜]]

This word is itself the stand-in for 桜. Fixed malformed `羅馬字` (ang → 'ang, restoring the null-initial apostrophe), added missing `japanese`/`hsk_level`. Discovered a genuine homophone with [[硬]] (both 앙) — fully fixed and cross-referenced both sides: 硬.md got the same 羅馬字 fix, missing `japanese`/`hsk_level` added, blank `vietnamese` filled, plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 桜桃.

### 2026-08-31, iteration 2114 — [[words/桜桃|桜桃]]

No stand-in relationship (桜's own stand-in is itself; 桃's own is [[桃子]]). Confirmed Korean 앵두 is a real lexicalized irregular form (compositional would be 앵도), not a bug. Added missing `pos`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 桶.

### 2026-08-31, iteration 2115 — [[words/桶|桶]]

This word is itself the stand-in for 桶. Added missing `japanese`/`hsk_level`. Completed the genuine 3-way homophone group with [[冬]] (already complete, anticipating both) and [[通]] (all 통) — fully fixed and cross-referenced all three: 通.md got missing `pos`/`japanese`/`hsk_level` added, blank `vietnamese` filled. Stamped `date-last-perfect: 2026-08-31` on 桶 and 通 (冬 was already stamped 2026-07-26; only its Notes text updated).

Next: 梁.

### 2026-08-31, iteration 2116 — [[words/梁|梁]]

This word is itself the stand-in for 梁. Fixed literal `vietnamese: null` → lương, added missing `pos`/`japanese`/`hsk_level`. Completed the genuine 3-way homophone group with [[両]] (already complete, anticipating both) and [[糧]] (all 량) — fully fixed and cross-referenced all three: 糧.md got the same literal-null fix plus missing `pos`/`japanese`/`hsk_level` added. Also removed a redundant `品詞` field on 両.md. Stamped `date-last-perfect: 2026-08-31` on 梁 and 糧 (両 was already stamped 2026-07-26; only its Notes/frontmatter cleanup updated).

Next: 梅花.

### 2026-08-31, iteration 2117 — [[words/梅花|梅花]]

This word is itself the stand-in for 梅; 花's own stand-in is [[草花]]. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 梅雨.

### 2026-08-31, iteration 2118 — [[words/梅雨|梅雨]]

No stand-in relationship (梅's own stand-in is [[梅花]]; 雨's own is itself). Simplified `japanese` to the everyday つゆ reading (dropped secondary formal ばいう). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 梨木.

### 2026-08-31, iteration 2119 — [[words/梨木|梨木]]

This word is itself the stand-in for 梨. Fixed real bugs: `mandarin`/`cantonese` copied from unrelated compound 梨樹/梨树; `korean` was a native genus-level term instead of compositional 리목; `vietnamese` was truncated (missing 木's half). Confirmed Japanese なし is a genuine native term, not a bug. Removed 梨樹/梨树 from `aliases` (different character, near-synonym). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 梳.

### 2026-08-31, iteration 2120 — [[words/梳|梳]]

This word is itself the stand-in for 梳. Added missing `japanese`/`hsk_level`. Reformatted the existing homophone callout with [[小]] (already complete) to the canonical multi-line format. Stamped `date-last-perfect: 2026-08-31`.

Next: 棍棒.

### 2026-08-31, iteration 2121 — [[words/棍棒|棍棒]]

Confirmed `#cranberry` tag is correct: both 棍 and 棒's own stand-ins point to this compound (transitivity holds, A=B=AB). Filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 棗椰.

### 2026-08-31, iteration 2122 — [[words/棗椰|棗椰]]

This word is itself the stand-in for 棗; 椰's own stand-in is [[椰子]]. Confirmed `japanese`/`vietnamese` are correct real-world species terms, not bugs. Fixed real bugs: `mandarin` had stray "zi" suffix, `cantonese` was blank, `korean` was 棗's native word (대추) instead of compositional 조야. Removed `棗樹`/`枣树` from `aliases` (different character, near-synonym). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 森羅.

### 2026-08-31, iteration 2123 — [[words/森羅|森羅]]

No stand-in relationship (森's own stand-in is [[森林]]; 羅's own is [[羅馬]]). Fixed real bug: `羅馬字`/`諺文` (simlo/심로) didn't match 森's own citation or the word's own 注音 — corrected to sumlo/숨로. Filled blank `vietnamese`/`pos`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 棲息.

### 2026-08-31, iteration 2124 — [[words/棲息|棲息]]

This word is itself the stand-in for 棲; 息's own stand-in is [[気息]]. Confirmed `korean` 서식 is compositional (棲's own korean/諺文 divergence is a pre-existing character-level pattern, not a bug here). Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 棺.

### 2026-08-31, iteration 2125 — [[words/棺|棺]]

This word is itself the stand-in for 棺. Fixed literal `vietnamese: null` → quan, added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[滾]] (both 관) — fully fixed and cross-referenced both sides: 滾.md got literal `vietnamese: null` → cuộn fixed and missing `japanese` added (its own stand-in), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 椋鳥.

### 2026-08-31, iteration 2126 — [[words/椋鳥|椋鳥]]

This word is itself the stand-in for 椋. Fixed real bug: `諺文` first syllable 령→량; `korean` was a native bird name (찌르레기) instead of compositional 량조. Confirmed Japanese むくどり is a genuine native term. Removed redundant `品詞`; left `vietnamese` blank and flagged a character-level gap (椋's own citation stores only a null marker). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 植物.

### 2026-08-31, iteration 2127 — [[words/植物|植物]]

This word is itself the stand-in for 植; 物's own stand-in is itself. Added missing `pos`, removed empty `aliases: []`. While verifying the existing homophone with [[食物]], discovered and fixed a real contamination bug on that page: `mandarin`/`cantonese` had been copied from its own alias 食品's readings instead of 食物's own compositional forms; also filled its blank `vietnamese`. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 椎菌.

### 2026-08-31, iteration 2128 — [[words/椎菌|椎菌]]

No stand-in relationship (椎's own stand-in is [[脊椎]]; 菌's own is [[細菌]]). Confirmed this is a Dan'a'yo-only coinage (椎 used in its Japanese "shii-tree" sense, echoing real 椎茸 etymology): mandarin/cantonese/korean/vietnamese correctly hold real terms for shiitake, not compositional readings, since no real Chinese/Korean/Vietnamese term derives from 椎+菌. Reformatted `aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 検証.

### 2026-08-31, iteration 2129 — [[words/検証|検証]]

No stand-in relationship (検's own stand-in is [[検査]]; 証's own is [[証明]]). Fixed stray space in `mandarin`, filled blank `cantonese`, left `vietnamese` blank and flagged that 検's own citation has no vietnamese value at all (character-level gap). Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楊柳.

### 2026-08-31, iteration 2130 — [[words/楊柳|楊柳]]

This word is itself the stand-in for 楊 (bound, cannot stand alone). Filled blank `vietnamese`. Confirmed the already-noted irregular Japanese fused reading やなぎ, not a bug. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楊梅.

### 2026-08-31, iteration 2131 — [[words/楊梅|楊梅]]

No stand-in relationship (楊's own stand-in is [[楊柳]]; 梅's own is [[梅花]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楊樹.

### 2026-08-31, iteration 2132 — [[words/楊樹|楊樹]]

No stand-in relationship (楊's own stand-in is [[楊柳]]; 樹's own is [[樹木]]). Confirmed `japanese`/`korean` loanwords (real-world standard for poplar) are correct, same pattern as [[板球]]/[[果醤]]. Filled blank `vietnamese` compositionally. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楓樹.

### 2026-08-31, iteration 2133 — [[words/楓樹|楓樹]]

This word is itself the stand-in for 楓. Discovered a genuine homophone with [[風水]] (both 뿡수) — fully fixed and cross-referenced both sides: 風水.md got `mandarin` simplified (dropped extra tone variant), blank `hsk_level`/`swadesh` removed, plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 極.

### 2026-08-31, iteration 2134 — [[words/極|極]]

This word is itself the stand-in for 極. Added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`. No word-level homophones (棘 shares the reading but has no independent word page). Stamped `date-last-perfect: 2026-08-31`.

Next: 極刑.

### 2026-08-31, iteration 2135 — [[words/極刑|極刑]]

No stand-in relationship (極's own stand-in is itself; 刑's own is [[刑罰]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 極右.

### 2026-08-31, iteration 2136 — [[words/極右|極右]]

No stand-in relationship (極's own stand-in is itself; 右's own is [[右側]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 極左.

### 2026-08-31, iteration 2137 — [[words/極左|極左]]

No stand-in relationship (極's own stand-in is itself; 左's own is [[左側]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 極東.

### 2026-08-31, iteration 2138 — [[words/極東|極東]]

No stand-in relationship (極's own stand-in is itself; 東's own is [[東方]]). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 極端.

### 2026-08-31, iteration 2139 — [[words/極端|極端]]

No stand-in relationship (極's own stand-in is itself; 端's own is [[末端]]). Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 極限.

### 2026-08-31, iteration 2140 — [[words/極限|極限]]

No stand-in relationship (極's own stand-in is itself; 限's own is [[限度]]). Fixed real bug: `vietnamese` was a native descriptive phrase (giới hạn) instead of the compositional form — corrected to cực hạn. Removed blank `swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楷.

### 2026-08-31, iteration 2141 — [[words/楷|楷]]

This word is itself the stand-in for 楷. Added missing `japanese`/`hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楼閣.

### 2026-08-31, iteration 2142 — [[words/楼閣|楼閣]]

No stand-in relationship (楼's own stand-in is [[望楼]]; 閣's own is [[内閣]]). Fixed real bug: `korean` was 누각, the South Korean shifted form — corrected to North Korean 루각 (the prior prose had incorrectly documented the shifted form as standard). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楽経.

### 2026-08-31, iteration 2143 — [[words/楽経|楽経]]

No stand-in relationship (楽's own stand-in is [[快楽]]; 経's own is itself). Confirmed mandarin/cantonese/korean/vietnamese all correctly use 楽's real "music" reading (yuè-sense), missing from the character's own citation (only "pleasure"-sense lè stored) — character-level gap flagged for future perfecting. Filled blank `vietnamese`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 楽譜.

### 2026-08-31, iteration 2144 — [[words/楽譜|楽譜]]

This word is itself the stand-in for 譜. Confirmed mandarin/cantonese use 楽's real "music" reading, consistent with [[楽経]]'s character-level gap. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 概.

### 2026-08-31, iteration 2145 — [[words/概|概]]

This word is itself the stand-in for 概. Fixed literal `vietnamese: null` and literal quoted-string `korean: "null"` → khái/개, added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[改]] (already stamped 2026-06-27, missing its half) — retroactively filled 改's blank `vietnamese` and added the reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 概要.

### 2026-08-31, iteration 2146 — [[words/概要|概要]]

No stand-in relationship (概's own stand-in is itself; 要's own is [[重要]]). Fixed empty-string `vietnamese`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 榜文.

### 2026-08-31, iteration 2147 — [[words/榜文|榜文]]

This word is itself the stand-in for 榜; 文's own stand-in is [[文化]]. Confirmed the existing "near-homophone with 訪問" note is Korean-only, not a genuine Dan'a'yo-level homophone (different 注音 initials, ㄆ vs ㄈ). Filled blank `vietnamese`. Stamped `date-last-perfect: 2026-08-31`.

Next: 榴弾.

### 2026-08-31, iteration 2148 — [[words/榴弾|榴弾]]

No stand-in relationship (榴's own stand-in is [[石榴]]; 弾's own is [[弾丸]]). Fixed real bugs: `cantonese` malformed hybrid tone notation, `japanese` obsolete kana (りうだん→りゅうだん), `korean` South Korean shifted form (유탄→류단). Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 榴月.

### 2026-08-31, iteration 2149 — [[words/榴月|榴月]]

No stand-in relationship (榴's own stand-in is [[石榴]]; 月's own is itself). Confirmed `japanese`/`vietnamese` follow the established poetic-month convention; `korean` was already correctly North Korean form. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 構造.

### 2026-08-31, iteration 2150 — [[words/構造|構造]]

No stand-in relationship (構's own stand-in is [[構築]]; 造's own is [[創造]]). All fields already correct. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 槌.

### 2026-08-31, iteration 2151 — [[words/槌|槌]]

This word is itself the stand-in for 槌. Confirmed korean 퇴's mismatch with 諺文/羅馬字 is a pre-existing character-level divergence, not a bug, and set `kwin: false` accordingly. Added missing `japanese`/`hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 槍.

### 2026-08-31, iteration 2152 — [[words/槍|槍]]

This word is itself the stand-in for 槍. Added missing `japanese`/`hsk_level`, simplified doubled `vietnamese`. Discovered a genuine homophone with [[蒼]] (both 촹) — fully fixed and cross-referenced both sides: 蒼.md got missing `pos`/`japanese`/`hsk_level` added and blank `vietnamese` filled (its own stand-in), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-08-31` on both.

Next: 槐月.

### 2026-08-31, iteration 2153 — [[words/槐月|槐月]]

No stand-in relationship (槐's own stand-in is [[槐樹]]; 月's own is itself). Confirmed `japanese`/`vietnamese` follow the established poetic-month convention. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 様態格.

### 2026-08-31, iteration 2154 — [[words/様態格|様態格]]

No stand-in relationship (様's own stand-in is [[様式]]; 態's own is [[態度]]; 格's own is itself). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 標準.

### 2026-08-31, iteration 2155 — [[words/標準|標準]]

This word is itself the stand-in for 準; 標's own stand-in is [[標識]]. Fixed bare-integer `hsk_level`, removed self-referential `標準` from `aliases`, kept genuine variants. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 標誌.

### 2026-08-31, iteration 2156 — [[words/標誌|標誌]]

This word is itself the stand-in for 誌; 標's own stand-in is the similar sibling word [[標識]]. Fixed real bugs: `mandarin` had an extra variant borrowed from 標識's reading; `japanese` combined an obsolete kana spelling with a syllable belonging to 識, not 誌 — corrected to ひょうし. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 標識.

### 2026-08-31, iteration 2157 — [[words/標識|標識]]

This word is itself the stand-in for 標; 識's own stand-in is [[認識]]. Confirmed mandarin biāozhì correctly uses 識's alternate zhì reading, already documented on the character's own citation. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 標題.

### 2026-08-31, iteration 2158 — [[words/標題|標題]]

This word is itself the stand-in for 題; 標's own stand-in is [[標識]]. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 樟脳.

### 2026-08-31, iteration 2159 — [[words/樟脳|樟脳]]

This word is itself the stand-in for 樟; 脳's own stand-in is itself. Fixed real bug: `cantonese` had the wrong initial (zeong1→zoeng1). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 模倣.

### 2026-08-31, iteration 2160 — [[words/模倣|模倣]]

This word is itself the stand-in for 倣; 模's own stand-in is [[模擬]]. Filled blank `vietnamese`, reformatted `aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 模擬.

### 2026-08-31, iteration 2161 — [[words/模擬|模擬]]

No stand-in relationship (both 模 and 擬's own stand-ins are themselves). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 模範.

### 2026-08-31, iteration 2162 — [[words/模範|模範]]

This word is itself the stand-in for 範; 模's own stand-in is [[模擬]]. All fields already correct; cleaned up quoting. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 権威.

### 2026-08-31, iteration 2163 — [[words/権威|権威]]

No stand-in relationship (権's own stand-in is [[権利]]; 威's own is [[威力]]). Flagged that 権's own citation has a blank `vietnamese` field (character-level gap, not fixed here). No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 横幅.

### 2026-08-31, iteration 2164 — [[words/横幅|横幅]]

No stand-in relationship (横's own stand-in is [[横断]]; 幅's own is [[幅度]]). All fields already correct. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 樹懶.

### 2026-08-31, iteration 2165 — [[words/樹懶|樹懶]]

No stand-in relationship (樹's own stand-in is [[樹木]]; 懶's own is [[懶惰]]). Confirmed `japanese` loanword-equivalent ナマケモノ (real native term, no compositional Sino-Japanese form in use) matches the [[板球]]/[[果醤]]/[[楊樹]] pattern. Filled blank `korean`/`vietnamese` compositionally. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 樹木.

### 2026-08-31, iteration 2166 — [[words/樹木|樹木]]

This word is itself the stand-in for 樹; 木's own stand-in is itself. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases: []`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 橄欖.

### 2026-08-31, iteration 2167 — [[words/橄欖|橄欖]]

Confirmed `#cranberry` tag is correct: both 橄 and 欖's own stand-ins point to this compound (transitivity holds, A=B=AB). Simplified doubled `cantonese` to primary form, flagging a real divergence with 橄's own stored citation (gam2 vs. real-world gaam3) as a character-level gap. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 橄欖球.

### 2026-08-31, iteration 2168 — [[words/橄欖球|橄欖球]]

No stand-in relationship (橄/欖's own stand-ins point to [[橄欖]]; 球's own is itself). Confirmed `japanese`/`korean` loanwords and Vietnamese descriptive term are correct real-world usage, same pattern as [[板球]]/[[果醤]]/[[楊樹]]/[[樹懶]]. Fixed real bug: `cantonese` malformed hybrid tone notation, corrected to match [[橄欖]]'s simplified form. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 橋梁.

### 2026-08-31, iteration 2169 — [[words/橋梁|橋梁]]

No stand-in relationship (both 橋 and 梁's own stand-ins are themselves). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 橘.

### 2026-08-31, iteration 2170 — [[words/橘|橘]]

This word is itself the stand-in for 橘. Added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 檀木.

### 2026-08-31, iteration 2171 — [[words/檀木|檀木]]

This word is itself the stand-in for 檀; 木's own stand-in is itself. All fields already correct; cleaned quoting. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 檳榔.

### 2026-08-31, iteration 2172 — [[words/檳榔|檳榔]]

Confirmed `#cranberry` tag is correct: both 檳 and 榔's own stand-ins point to this compound (transitivity holds, A=B=AB). Fixed real bug: `japanese` obsolete kana (びんらう→びんろう). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 櫛.

### 2026-08-31, iteration 2173 — [[words/櫛|櫛]]

This word is itself the stand-in for 櫛. Added missing `japanese`/`hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-31`.

Next: 欄杆.

### 2026-09-01, iteration 2174 — [[words/欄杆|欄杆]]

This word is itself the stand-in for 欄; 杆's own stand-in is itself. Fixed real bug: `korean` was the South Korean shifted form (난간) — corrected to North Korean 란간. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欠伸.

### 2026-09-01, iteration 2175 — [[words/欠伸|欠伸]]

This word is itself the stand-in for 欠; 伸's own stand-in is [[伸長]]. Confirmed Japanese あくび is a genuine irregular jukujikun, not a bug. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 次第.

### 2026-09-01, iteration 2176 — [[words/次第|次第]]

This word is itself the stand-in for 次; 第's own stand-in is itself. Fixed missing space in `cantonese`, filled blank `korean`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欣喜.

### 2026-09-01, iteration 2177 — [[words/欣喜|欣喜]]

This word is itself the stand-in for 欣; 喜's own stand-in is itself (own word page). Filled blank `korean`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欧圓.

### 2026-09-01, iteration 2178 — [[words/欧圓|欧圓]]

No stand-in relationship (欧's own stand-in is [[欧羅巴]]; 圓's own is itself). Confirmed `japanese`/`korean`/`vietnamese` loanwords for "Euro" are correct real-world usage, same pattern as [[板球]]/[[果醤]]/[[楊樹]]/[[樹懶]]/[[橄欖球]]. Removed blank `hsk_level`/`swadesh`, reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欧洲.

### 2026-09-01, iteration 2179 — [[words/欧洲|欧洲]]

No stand-in relationship (欧's own stand-in is [[欧羅巴]]; 洲's own is itself). Confirmed korean 구주 correctly uses 欧's genuine older placename Sino-Korean reading 구 (documented on its own character page), not a bug. Removed self-referential `欧洲` from `aliases` and redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欧羅巴.

### 2026-09-01, iteration 2180 — [[words/欧羅巴|欧羅巴]]

This word is itself the stand-in for 欧; 羅's own stand-in is [[羅馬]]; 巴's own is itself. Fixed severe contamination: `mandarin`/`cantonese` had been copied from the unrelated word [[欧洲]] — corrected to 欧羅巴's own compositional forms. Fixed a truncated `vietnamese` (Châu Â → Châu Âu). Confirmed loanword `japanese`/`korean` are correct. Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欧金.

### 2026-09-01, iteration 2181 — [[words/欧金|欧金]]

Periodic-table neologism (europium); confirmed `mandarin`/`cantonese` correctly hold the avoided real character 铕's reading, matching the [[丹金]] pattern. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欲望.

### 2026-09-01, iteration 2182 — [[words/欲望|欲望]]

This word is itself the stand-in for 欲; 望's own stand-in is [[希望]]. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`, reformatted `aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欲求.

### 2026-09-01, iteration 2183 — [[words/欲求|欲求]]

No stand-in relationship (欲's own stand-in is itself; 求's own is [[要求]]). Filled blank `cantonese`/`vietnamese`, reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 欺𥈞.

### 2026-09-01, iteration 2184 — [[words/欺瞞|欺瞞]] (found via duplicate at 欺𥈞)

Discovered `words/欺𥈞.md` was a stray duplicate of the already-consolidated, already-stamped `words/欺瞞.md` (which lists 欺𥈞 as its own alias, per a documented 2026-06-13 decision to merge both spellings into one file). Deleted the duplicate, removed a corresponding stray "欺𥈞" bullet from [[欺]]'s own character-page Words section (which had wrongly listed it as a second word), and lightly re-perfected `欺瞞.md` (reformatted `vietnamese` list→scalar, quoted scalars). Stamped `date-last-perfect: 2026-09-01` on 欺瞞.

Next: 欽敬.

### 2026-09-01, iteration 2185 — [[words/欽敬|欽敬]]

This word is itself the stand-in for 欽; 敬's own stand-in is [[尊敬]]. Filled blank `japanese`, removed blank `hsk_level`/`swadesh`, reformatted `aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 款.

### 2026-09-01, iteration 2186 — [[words/款|款]]

This word is itself the stand-in for 款. Added missing `pos`/`japanese`/`hsk_level`. No word-level homophones (寛 shares the reading but has no independent word page). Stamped `date-last-perfect: 2026-09-01`.

Next: 歌曲.

### 2026-09-01, iteration 2187 — [[words/歌曲|歌曲]]

Discovered this qualifies for the `#cranberry` tag (both 歌 and 曲's own stand-ins point to this compound, transitivity holds A=B=AB) and was missing it — added. Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 歌謡.

### 2026-09-01, iteration 2188 — [[words/歌謡|歌謡]]

This word is itself the stand-in for 謡; 歌's own stand-in is itself (own word page). Filled blank `vietnamese`, flagged that 謡's own citation has no vietnamese value at all — character-level gap for future perfecting. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 歓呼.

### 2026-09-01, iteration 2189 — [[words/歓呼|歓呼]]

No stand-in relationship (歓's own stand-in is [[歓喜]]; 呼's own is itself). Fixed real bugs: `japanese` was garbled with an obsolete kana spelling and a duplicate value containing an invisible zero-width character — corrected to modern かんこ. Flagged that 歓's own citation has no vietnamese value stored. Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 歓喜.

### 2026-09-01, iteration 2190 — [[words/歓喜|歓喜]]

This word is itself the stand-in for 歓; 喜's own stand-in is itself (own word page). Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正.

### 2026-09-01, iteration 2191 — [[words/正|正]]

This word is itself the stand-in for 正. Added missing `pos`/`japanese`/`hsk_level`. Discovered a genuine homophone with [[蒸]] (both 징) — fully fixed and cross-referenced both sides: 蒸.md got literal `vietnamese: null` → chưng fixed and missing `pos`/`japanese`/`hsk_level` added (its own stand-in), plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-09-01` on both.

Next: 正割.

### 2026-09-01, iteration 2192 — [[words/正割|正割]]

No stand-in relationship (both 正 and 割's own stand-ins are themselves, each with its own word page). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正午.

### 2026-09-01, iteration 2193 — [[words/正午|正午]]

This word is itself the stand-in for 午. Fixed real bug: `vietnamese` was a native descriptive phrase (buổi trưa) instead of the compositional form — corrected to chính ngọ. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正字.

### 2026-09-01, iteration 2194 — [[words/正字|正字]]

No stand-in relationship (both 正 and 字's own stand-ins are themselves, each with its own word page). Fixed empty-string `vietnamese`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正字法.

### 2026-09-01, iteration 2195 — [[words/正字法|正字法]]

No stand-in relationship (all three constituents' own stand-ins are themselves, each with its own word page). Filled blank `vietnamese`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正弦.

### 2026-09-01, iteration 2196 — [[words/正弦|正弦]]

No stand-in relationship (both 正 and 弦's own stand-ins are themselves, each with its own word page). Fixed real bugs: `cantonese`/`japanese`/`korean` each held malformed doubled values pairing the compositional form with an unrelated English-loanword alternate — simplified to the single compositional forms. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正弦波.

### 2026-09-01, iteration 2197 — [[words/正弦波|正弦波]]

No stand-in relationship (all three constituents' own stand-ins are themselves, each with its own word page). Filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正接.

### 2026-09-01, iteration 2198 — [[words/正接|正接]]

No stand-in relationship (both 正 and 接's own stand-ins are themselves). Fixed real bugs: `korean` was an English loanword (탄젠트) instead of compositional 정접 (matching the [[正弦]] parallel pattern); `vietnamese` was likewise a loanword (tang) instead of chính tiếp. Filled blank `cantonese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正月.

### 2026-09-01, iteration 2199 — [[words/正月|正月]]

No stand-in relationship (both 正 and 月's own stand-ins are themselves, each with its own word page). Fixed real bug: `注音` had the wrong initial (ㄍ instead of ㄐ) that didn't match `羅馬字`/`諺文`. Removed redundant `品詞`, reformatted `japanese`/`vietnamese` list→scalar. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正義.

### 2026-09-01, iteration 2200 — [[words/正義|正義]]

No stand-in relationship (正's own stand-in is itself; 義's own is [[意義]]). Fixed real bug: the recurring 'ǝi/wi minority-pattern error (諺文/羅馬字 used 위/wi instead of 義's own correct 읫/'ǝi, same pattern as [[時宜]]). Reformatted `characters`/`aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正音.

### 2026-09-01, iteration 2201 — [[words/正音|正音]]

No stand-in relationship (正's own stand-in is itself; 音's own is [[音楽]]). All fields already correct; quoted scalars for consistency. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 正餐.

### 2026-09-01, iteration 2202 — [[words/正餐|正餐]]

No stand-in relationship (both 正 and 餐's own stand-ins are themselves, each with its own word page). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 武.

### 2026-09-01, iteration 2203 — [[words/武|武]]

This word is itself the stand-in for 武. Added missing `pos`/`japanese`/`hsk_level`, simplified doubled `vietnamese`. Discovered a genuine homophone with [[霧]] (both 무) — fully fixed and cross-referenced both sides: 霧.md got a trailing-invisible-space bug fixed in `japanese`, a malformed comma-joined `vietnamese` string corrected to a scalar, redundant `品詞` removed, plus reciprocal Homophones callout. Stamped `date-last-perfect: 2026-09-01` on both.

Next: 武侠.

### 2026-09-01, iteration 2204 — [[words/武侠|武侠]]

No stand-in relationship (武's own stand-in is itself; 侠's own is [[侠客]]). Simplified doubled `cantonese` to its primary supported form. Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 武将.

### 2026-09-01, iteration 2205 — [[words/武将|武将]]

No stand-in relationship (both 武 and 将's own stand-ins are themselves, each with its own word page). Confirmed mandarin wǔjiàng correctly uses 将's genuine noun-sense tone (jiàng), distinct from its own stored grammatical-particle reading (jiāng) — not a bug. Filled blank `cantonese`/`vietnamese`, removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 武芸.

### 2026-09-01, iteration 2206 — [[words/武芸|武芸]]

No stand-in relationship (武's own stand-in is itself; 芸's own is [[芸術]]). Flagged that 武芸 correctly uses 芸's real polyphonic "art/skill" reading yì (simplified 藝/艺), missing from the character's own citation (only "rue plant" yún stored) — character-level gap for future perfecting. Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 武術.

### 2026-09-01, iteration 2207 — [[words/武術|武術]]

No stand-in relationship (both 武 and 術's own stand-ins are themselves, each with its own word page). Filled blank `vietnamese`, removed blank `hsk_level`/`swadesh`. Reformatted the existing homophone callout with [[巫術]] (already complete) to the canonical multi-line format on both pages. Stamped `date-last-perfect: 2026-09-01` on 武術 (巫術 was already stamped 2026-08-27; only its callout format updated).

Next: 歯.

### 2026-09-01, iteration 2208 — [[words/歯|歯]]

This word is itself the stand-in for 歯. Flagged that 歯's own citation has no vietnamese value stored. Removed redundant `品詞`. Discovered [[置]] (already in the 3-way homophone group with 幟, but itself never stamped) — fully fixed and cross-referenced: literal `vietnamese: null` fixed, missing `pos`/`japanese`/`hsk_level` added (its own stand-in). Reformatted the callout on all three pages (幟/歯/置, all 치) to the canonical multi-line format. Stamped `date-last-perfect: 2026-09-01` on 歯 and 置 (幟 was already stamped 2026-08-27; only its callout format updated).

Next: 歯痛.

### 2026-09-01, iteration 2209 — [[words/歯痛|歯痛]]

No stand-in relationship (歯's own stand-in is itself; 痛's own is [[苦痛]]). Filled blank `vietnamese` using 歯's real-world standard Sino-Vietnamese reading xỉ (character's own citation has no vietnamese value stored, already flagged on [[歯]]). No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 歯齦.

### 2026-09-01, iteration 2210 — [[words/歯齦|歯齦]]

This word is itself the stand-in for 齦. Fixed real bug: `korean` was the native word 잇몸 (齦's `korean_native` field), not the compositional Sino-Korean form — corrected to 치간. Filled blank `vietnamese`, removed `齒仁` from `aliases` (likely OCR/corpus error using a different character), kept genuine variants. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 歴史.

### 2026-09-01, iteration 2211 — [[words/歴史|歴史]]

Discovered this qualifies for the `#cranberry` tag (both 歴 and 史's own stand-ins point to this compound, transitivity holds A=B=AB) and was missing it — added. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 死亡人数.

### 2026-09-01, iteration 2212 — [[words/死亡人数|死亡人数]]

Fixed severe contamination: `cantonese`/`japanese`/`korean`/`vietnamese` had all been swapped for the real-world near-synonym term 死亡者數 ("deceased persons," with 者) instead of this compound's own literal 死亡+人數 compositional readings — corrected to match [[死亡]]'s and [[人数]]'s own citations exactly. Removed blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 死亡率.

### 2026-09-01, iteration 2213 — [[words/死亡率|死亡率]]

No stand-in relationship (率's own stand-in is [[比率]]). Confirmed korean 사망률 correctly retains the ㄹ liaison (망 ends in ㅇ, not a vowel/ㄴ). Added missing `kwin: true`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 死骸.

### 2026-09-01, iteration 2214 — [[words/死骸|死骸]]

This word is itself the stand-in for 骸. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 残害.

### 2026-09-01, iteration 2215 — [[words/残害|残害]]

This word is itself the stand-in for 害; 残's own stand-in is itself. Simplified `japanese` to primary form, filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 殴打.

### 2026-09-01, iteration 2216 — [[words/殴打|殴打]]

This word is itself the stand-in for 殴. Added missing `pos`, filled blank `vietnamese`, removed empty `aliases: []`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 殺.

### 2026-09-01, iteration 2217 — [[words/殺|殺]]

This word is itself the stand-in for 殺. Fixed literal `vietnamese: null` → sát, added missing `pos`/`japanese`/`hsk_level`. No word-level homophones (薩 shares the reading but has no independent word page). Stamped `date-last-perfect: 2026-09-01`.

Next: 殺戮.

### 2026-09-01, iteration 2218 — [[words/殺戮|殺戮]]

This word is itself the stand-in for 戮. Confirmed korean 살육 (not a naive concatenation) is a genuine liquid-liaison divergence, same class as 률→율 elsewhere in the vault — kept as-is, added `kwin: false`. Reformatted `characters` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 殺身.

### 2026-09-01, iteration 2219 — [[words/殺身|殺身]]

No stand-in relationship (殺's own stand-in is itself; 身's own is [[身体]]). Filled blank `vietnamese`, removed empty `aliases: []`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 母指.

### 2026-09-01, iteration 2220 — [[words/母指|母指]]

No stand-in relationship (母's own stand-in is [[母親]]; 指's own is [[手指]]). Filled blank `korean`/`vietnamese`, reformatted `aliases` to block-list YAML. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 母校.

### 2026-09-01, iteration 2221 — [[words/母校|母校]]

No stand-in relationship (母's own stand-in is [[母親]]; 校's own is [[学校]]). Filled blank `vietnamese` (mẫu giáo, compositional per vault convention, though real-world Vietnamese uses this phrase for "kindergarten" rather than "alma mater" — noted for awareness, not changed). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-09-01`.

Next: 母艦.

### 2026-09-01, iteration 2222 — [[words/母艦|母艦]]

No stand-in relationship (母's own stand-in is [[母親]]; 艦's own is [[艦船]]). Mandarin mǔjiàn, Cantonese mou5 laam6, Japanese ぼかん, Korean 모함, Vietnamese mẫu hạm all match constituent citations exactly. `kwin: false` since 諺文 못함 diverges from real Korean 모함. Reformatted `characters`/`aliases` to block-list YAML, removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄛㄨㄏㄚㄇ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 母音.

### 2026-09-01, iteration 2223 — [[words/母音|母音]]

No stand-in relationship (母's own stand-in is [[母親]]; 音's own is [[音楽]]). Fixed `mandarin`/`cantonese`/`vietnamese`, contaminated with readings of the real Mandarin term 元音 ("yuányīn"/"jyun4 jam1"/"Nguyên âm") instead of 母's/音's own compositional citations (mǔyīn/mou5 jam1/mẫu âm); 元音 correctly kept as `aliases`, reformatted to block-list YAML. Japanese ぼいん and Korean 모음 coincidentally match real-world words but are independently compositional. `kwin: false` (諺文 못움 vs real 모음). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄛㄨㄨㄇ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 毎世紀.

### 2026-09-01, iteration 2224 — [[words/世紀|世紀]] & [[words/毎世紀|毎世紀]]

Discovered mid-processing that [[世紀]] (position 132, far earlier in the sweep) had never actually been stamped despite complete content — retroactively fixed (removed blank `swadesh`, added Notes documenting it as the stand-in that legitimizes 紀) and stamped. Then completed [[毎世紀]]: 毎's own stand-in is itself; this compound builds on [[世紀]]. Mandarin měishìjì, Cantonese mui5 sai3 gei2, Japanese まいせいき, Korean 매세기 all match constituent citations exactly. Filled blank `vietnamese` (mỗi thế kỷ). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones on either page. Both stamped `date-last-perfect: 2026-09-01`.

Next: 毎年.

### 2026-09-01, iteration 2225 — [[words/毎年|毎年]]

No stand-in relationship (毎's own stand-in is itself; 年's own is also itself). Mandarin měinián, Cantonese mui5 nin4, Japanese まいねん, Korean 매년 all match constituent citations exactly. Filled blank `vietnamese` (mỗi năm, using 年's native năm reading rather than Sino niên, matching how the phrase is actually formed). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄛㄧㄋㄝㄋ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 毎日.

### 2026-09-01, iteration 2226 — [[words/毎日|毎日]]

No stand-in relationship (毎's own stand-in is itself; 日's own is also itself). Mandarin měirì, Cantonese mui5 jat6, Japanese まいにち, Korean 매일 all match constituent citations exactly. Filled blank `vietnamese` (mỗi nhật, using 日's Sino citation nhật since no native reading is stored for 日, unlike 年's năm) — compositional though real Vietnamese uses native "mỗi ngày" instead. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄛㄧㄋㄧㄊ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 毎月.

### 2026-09-01, iteration 2227 — [[words/毎月|毎月]]

No stand-in relationship (both 毎's and 月's own stand-ins are themselves). Mandarin měiyuè, Cantonese mui5 jyut6, Japanese まいげつ all match constituent citations exactly. Fixed real bug: `korean` was garbled comma-joined 매달,매월 mixing native 매달 with the compositional form — corrected to 매월 matching 月's own citation. Filled blank `vietnamese` (mỗi nguyệt). Added `kwin: false` (諺文 뫼웓 vs Korean 매월, the 月-coda divergence documented on [[月]] and [[来月]]). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄛㄧ⼔ㄊ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 毎週.

### 2026-09-01, iteration 2228 — [[words/毎週|毎週]]

No stand-in relationship (毎's own stand-in is itself; 週's own is [[週日]]). Mandarin měizhōu, Cantonese mui5 zau1, Japanese まいしゅう, Korean 매주 all match constituent citations exactly. Filled blank `vietnamese` (mỗi chu, using 週's first-listed citation value chu, matching precedent on [[週年]]). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄛㄧㄐㄨㄛ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 毒.

### 2026-09-01, iteration 2229 — [[words/毒|毒]]

This word is itself the stand-in that legitimizes the character 毒 as an independent Dan'a'yo entry. Fixed literal `vietnamese: null` → độc (primary Sino form; 毒's other value nọc belongs to the distinct "venom" sense). Added missing `pos`/`japanese`/`hsk_level` fields, `kwin: true` (諺文 독 matches Korean 독). No word-level homophones — several bound characters (篤/独/督/涜/読) share 注音 ㄉㄛㄎ but have no independent word pages. Stamped `date-last-perfect: 2026-09-01`.

Next: 比例.

### 2026-09-01, iteration 2230 — [[words/比例|比例]]

No stand-in relationship (比's own stand-in is itself; 例's own is [[実例]]). Mandarin bǐlì, Cantonese bei2 lai6, Japanese ひれい, Korean 비례 all match constituent citations exactly. Filled blank `vietnamese` with tỉ lệ (比's tỉ + 例's lệ) — coincidentally the real standard Vietnamese term for "ratio." Removed blank `swadesh` and empty `aliases: []`. No homophones (注音 ㄅㄧㄜㄌㄝ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 比喩.

### 2026-09-01, iteration 2231 — [[words/比喩|比喩]]

This word is itself the stand-in that legitimizes the character 喩 (比's own stand-in is itself, so only one-way — no #cranberry). Mandarin bǐyù, Cantonese bei2 jyu6, Japanese ひゆ, Korean 비유 all match constituent citations exactly. Filled blank `vietnamese` with tỉ dụ (比's tỉ + 喩's dụ) — coincidentally the real standard Vietnamese term for "analogy, metaphor." Reformatted `characters` to block-list YAML with "(char)" suffix. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄅㄧㄜ⼜ㄇ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 比較格.

### 2026-09-01, iteration 2232 — [[words/比較格|比較格]]

No stand-in relationship (較's own stand-in is [[比較]], not this compound; 格's own is itself). Builds on [[比較]] + the fixed case-name suffix 格, part of the same coinage set as [[与格]]/[[主格]]/[[呼格]]. Mandarin bǐjiàogé, Cantonese bei2 gaau3 gaak3, Japanese ひかくかく, Korean 비교격 all match constituent citations. `vietnamese: so sánh cách` (比較's so sánh + 格's cách), matching sibling pattern. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄅㄧㄜㄍㄚㄎㄍㄚㄎ unique). Stamped `date-last-perfect: 2026-09-01`.

Next: 毛皮.

### 2026-09-02, iteration 2233 — [[words/毛皮|毛皮]]

No stand-in relationship (毛's own stand-in is itself; 皮's own is [[皮革]]). Mandarin máopí, Korean 모피 are standard Sino compositional readings. Japanese けがわ is a native kun-yomi compound (毛's け + 皮's かわ→がわ rendaku) — the real standard Japanese word for "fur," matching 毛's/皮's own stored native readings. Filled blank `vietnamese` (mao bì, compositional). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄚㄨㄅㄧ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 毛蝦.

### 2026-09-02, iteration 2234 — [[words/毛蝦|毛蝦]]

This word is itself the stand-in that legitimizes the character 蝦 (毛's own stand-in is itself, so no #cranberry). Mandarin máoxiā, Cantonese mou4 haa1 are compositional, matching constituent citations. Japanese エビ, Korean 새우, Vietnamese tôm are the real everyday words for "shrimp" rather than Sino forms — same real-world-species-name convention already established on sibling [[龍蝦]]. `kwin: false` reflects that divergence. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄚㄨㄏㄚ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 毫.

### 2026-09-02, iteration 2235 — [[words/毫|毫]]

This word is itself the stand-in that legitimizes the character 毫. Mandarin háo, Cantonese hou4, Korean 호, Vietnamese hào all match 毫's own citation exactly. Filled blank `japanese` (こう, primary KOU on'yomi, matching the reading already chosen on homophone [[好]]) and blank `hsk_level` ("2"). Reformatted `characters` to block-list with "(char)" suffix. Homophone with [[好]] (注音/諺文/羅馬字 identical: ㄏㄚㄨ/핫/hau) already fully cross-referenced both sides (confirmed via 好's own prior Notes); reconfirmed no third homophone exists among remaining ㄏㄚㄨ characters (昊/鎬/豪/耗/皓/浩/号). Stamped `date-last-perfect: 2026-09-02`.

Next: 毫米.

### 2026-09-02, iteration 2236 — [[words/毫米|毫米]]

No stand-in relationship (both 毫's and 米's own stand-ins are themselves). Mandarin háomǐ, Cantonese hou4 mai5 are compositional. Japanese ミリメートル, Korean 밀리미터, Vietnamese milimét are the real international metric loanwords — same genuine divergence pattern already established on sibling [[千米]]. Reformatted `characters` to block-list with "(char)" suffixes on both. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄏㄚㄨㄇㄝㄧ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 氏族.

### 2026-09-02, iteration 2237 — [[words/氏族|氏族]]

This word is itself the stand-in that legitimizes the character 氏 (族's own stand-in is [[家族]], so no #cranberry). Mandarin shìzú, Cantonese si6 zuk6, Japanese しぞく, Korean 씨족 all match constituent citations exactly. Vietnamese thị tộc (氏's thị + 族's tộc) is also the real standard Vietnamese term for "clan." Filled blank `pos`, removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄧㄜㄐㄛㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 民主.

### 2026-09-02, iteration 2238 — [[words/民主|民主]]

No stand-in relationship (民's own stand-in is [[人民]]; 主's own is [[主人]]). Mandarin mínzhǔ, Cantonese man4 zyu2, Japanese みんしゅ, Korean 민주, Vietnamese dân chủ all match constituent citations exactly. `kwin: true` (諺文 민주 = Korean 민주). Removed redundant `品詞` field. No homophones (注音 ㄇㄧㄋㄐㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 民意.

### 2026-09-02, iteration 2239 — [[words/民意|民意]]

No stand-in relationship (民's own stand-in is [[人民]]; 意's own is [[意味]]). Mandarin mínyì, Cantonese man4 ji3, Japanese みんい, Korean 민의 all match constituent citations exactly. Vietnamese dân ý (民's dân + 意's ý) is also the real standard Vietnamese term for "public opinion." Added missing `kwin: false` (諺文 민으 vs Korean 민의). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄇㄧㄋ·ㄜ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 民謡.

### 2026-09-02, iteration 2240 — [[words/民謡|民謡]]

No stand-in relationship (民's own stand-in is [[人民]]; 謡's own is [[歌謡]]). Mandarin mínyáo, Cantonese man4 jiu4, Japanese みんよう, Korean 민요 all match constituent citations exactly. Vietnamese dân ca is the real standard term, kept as-is since 謡's own character page stores no `vietnamese` citation at all (flagged as a character-level gap for future work). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄧㄋ·⼄ㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 気.

### 2026-09-02, iteration 2241 — [[words/気|気]]

This word is itself the stand-in that legitimizes the character 気. Mandarin qì, Cantonese hei3, Korean 기, Vietnamese khí all match 気's own citation exactly. Filled blank `korean`/`vietnamese`, added missing `japanese` (き, primary KI) and `hsk_level` ("1"), reformatted `characters` to block-list with "(char)" suffix. Confirmed the other ㄎㄧㄜ characters (器/埼/棄/汽/豈) each have their own distinct stand-in, so none has an independent word page — no homophones. Stamped `date-last-perfect: 2026-09-02`.

Next: 気功.

### 2026-09-02, iteration 2242 — [[words/気功|気功]]

No stand-in relationship (気's own stand-in is itself; 功's own is [[功績]]). Mandarin qìgōng, Cantonese hei3 gung1, Japanese きこう, Korean 기공, Vietnamese khí công all match constituent citations exactly — also the real international term across all five languages. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄎㄧㄜㄍㄛㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水原.

### 2026-09-02, iteration 2243 — [[words/水原|水原]]

No stand-in relationship (水's own stand-in is itself; 原's own is [[原始]]). Dual proper-noun referent (South Korean city Suwon + Japanese surname Mizuhara); `japanese` correctly carries two distinct readings (スウォン loanword + みずはら native kun'yomi), matching the pattern of other dual-sense words like [[一日]]/[[万歳]] — not a bug. Mandarin Shuǐyuán, Cantonese seoi2 jyun4, Korean 수원 (the real city name), Vietnamese Thủy Nguyên all compositional. `kwin: true` (諺文 수원 = Korean 수원). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨ⼔ㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水平.

### 2026-09-02, iteration 2244 — [[words/水平|水平]]

This word is itself the stand-in that legitimizes the character 平 (水's own stand-in is itself, so no #cranberry). Mandarin shuǐpíng, Cantonese seoi2 ping4, Japanese すいへい, Korean 수평 all match constituent citations exactly. Filled blank `pos` (性詞) and `vietnamese` (thủy bình, 水's thuỷ + 平's bình) — also the real standard Vietnamese term. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨㄅㄧㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水族.

### 2026-09-02, iteration 2245 — [[words/水族|水族]]

No stand-in relationship (水's own stand-in is itself; 族's own is [[家族]]). Mandarin shuǐzú, Cantonese seoi2 zuk6, Japanese すいぞく, Korean 수족 all match constituent citations exactly. Filled blank `pos` (名詞) and `vietnamese` (thủy tộc, 水's thuỷ + 族's tộc) — also the real standard Vietnamese term. `kwin: true` (諺文 수족 = Korean 수족). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨㄐㄛㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水族館.

### 2026-09-02, iteration 2246 — [[words/水族館|水族館]]

Builds on [[水族]] + 館; no stand-in relationship (館's own stand-in is [[公館]]). Mandarin shuǐzúguǎn, Cantonese seoi2 zuk6 gun2, Japanese すいぞくかん, Korean 수족관 all match constituent citations exactly. Genuine divergence: Vietnamese uses thủy cung (水宮, "water palace") rather than a direct calque, same pattern as [[図書館]]'s thư viện. Filled blank `pos`. `kwin: true` (諺文 수족관 = Korean 수족관). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨㄐㄛㄎㄍ⺢ㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水星.

### 2026-09-02, iteration 2247 — [[words/水星|水星]]

No stand-in relationship (both 水's and 星's own stand-ins are themselves). Mandarin Shuǐxīng, Cantonese seoi2 sing1, Japanese すいせい, Korean 수성 all match constituent citations exactly. Vietnamese sao Thủy follows the real planet-naming convention (native "sao" + Sino thuỷ). `kwin: true` (諺文 수성 = Korean 수성). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨㄙㄝㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水泳.

### 2026-09-02, iteration 2248 — [[words/水泳|水泳]]

No stand-in relationship (both 水's and 泳's own stand-ins are themselves). Mandarin shuǐyǒng, Cantonese seoi2 wing6, Japanese すいえい, Korean 수영 all match constituent citations exactly. Fixed real bug: `korean` was garbled comma-joined 수영,헤엄 mixing compositional Sino with native 헤엄 — corrected to 수영. Filled blank `vietnamese` (thủy vạnh, 水's thuỷ + 泳's vạnh). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨ·ㄨㄧㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水牛.

### 2026-09-02, iteration 2249 — [[words/水牛|水牛]]

No stand-in relationship (both 水's and 牛's own stand-ins are themselves). Mandarin shuǐniú, Cantonese seoi2 ngau4, Japanese すいぎゅう all compositional. Korean 물소 is the real native word (calque), same divergence pattern as [[龍蝦]]/[[毛蝦]]. Filled blank `vietnamese` (thủy ngưu, 水's thuỷ + 牛's ngưu). No homophones (注音 ㄙㄨㄋ⼜ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水田.

### 2026-09-02, iteration 2250 — [[words/水田|水田]]

No stand-in relationship (水's own stand-in is itself; 田's own is [[田野]]). Mandarin shuǐtián, Cantonese seoi2 tin4, Japanese すいでん, Korean 수전 all match constituent citations exactly. Vietnamese ruộng lúa is the real standard term, kept as-is. Fixed malformed comma-joined `vietnamese` on 田's own character page ("điền, ruộng" → proper two-item list) while verifying composition. Filled blank `pos`. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨㄉㄝㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水稲.

### 2026-09-02, iteration 2251 — [[words/水稲|水稲]]

This word is itself the stand-in that legitimizes the character 稲 (水's own stand-in is itself, so no #cranberry). Mandarin shuǐdào, Cantonese seoi2 dou6, Japanese すいとう, Korean 수도 all match constituent citations exactly. Filled blank `pos` and `vietnamese` (thủy đạo, 水's thuỷ + 稲's đạo). `hsk_level: "2"` matches 稲's own value. No homophones (注音 ㄙㄨㄉㄚㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 水面.

### 2026-09-02, iteration 2252 — [[words/水面|水面]]

No stand-in relationship (水's own stand-in is itself; 面's own is [[表面]]). Mandarin shuǐmiàn, Cantonese seoi2 min6, Japanese すいめん, Korean 수면 all match constituent citations exactly. Filled blank `pos` and `vietnamese` (thủy diện, 水's thuỷ + 面's diện). `kwin: true` (諺文 수면 = Korean 수면). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄨㄇ⼶ㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 氾濫.

### 2026-09-02, iteration 2253 — [[words/氾濫|氾濫]] & [[words/汎濫|汎濫]]

**Real homophone found**: 氾 and 汎 are distinct characters sharing an identical Dan'a'yo reading (both ㄈㄚㄇ). 氾's own `stand_in` is 氾濫 (legitimizing 氾); 濫's own `stand_in` is 汎濫 (legitimizing 濫) — two genuinely independent word pages, both 注音 ㄈㄚㄇㄌㄚㄇ, confirmed unique to this pair via fresh grep. Added full reciprocal callouts to both.

Fixed real bugs on 氾濫: `羅馬字`/`諺文` had been contaminated to bamlam/밤람 instead of famlam/빰람 (matching 氾's own fam/빰); filled blank `cantonese` (faan3 laam6) and `vietnamese` (phiếm lạm). Also filled 汎濫's own blank `vietnamese` (phiếm lạm) while cross-referencing — flagged 濫's own character-level vietnamese citation as an apparently-scrambled list (lạm buried among unlikely native-looking forms) for future review. Both stamped `date-last-perfect: 2026-09-02`.

Next: 汀.

### 2026-09-02, iteration 2254 — [[words/汀|汀]] & [[words/訂|訂]]

**Real homophone found**: both words are their own stand-ins (legitimizing 汀 and 訂 respectively), sharing 注音/諺文/羅馬字 ㄊㄝㄫ/텅/teng. Completed both together with reciprocal callouts. 汀: fixed literal `vietnamese: null` → đinh, added missing `pos`/`japanese`(てい)/`hsk_level`(無, matching 汀's own no-HSK-level citation). 訂: fixed literal `vietnamese: null` → đính, added missing `pos`/`japanese`(てい)/`hsk_level`("2"). Both reformatted `characters` to block-list with "(char)" suffix. Confirmed 町 (also ㄊㄝㄫ) has its own distinct stand-in ([[室町]]), so no third homophone. Both stamped `date-last-perfect: 2026-09-02`.

Next: 汁.

### 2026-09-02, iteration 2255 — [[words/汁|汁]]

This word is itself the stand-in that legitimizes the character 汁. Mandarin zhī, Cantonese zap1, Korean 즙, Vietnamese chấp all match 汁's own citation exactly. Added missing `pos`/`japanese`(じゅう)/`hsk_level`("4"), reformatted `characters` to block-list with "(char)" suffix. `kwin: true` (諺文 즙 = Korean 즙). No homophones (注音 ㄐㄜㄆ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 汎.

### 2026-09-02, iteration 2256 — [[words/汎|汎]] (+ correcting [[words/帆|帆]])

This word is itself the stand-in that legitimizes the character 汎. **Fixed a false homophone bug**: `羅馬字`/`諺文`/`注音` had been contaminated to pam/팜/ㄆㄚㄇ, matching [[帆]]'s reading (帆 is one of 汎's own listed Derived Characters, sharing phonetic 凡) instead of 汎's own actual citation (fam/빰/ㄈㄚㄇ, confirmed via [[汎濫]]'s famlam). Corrected the reading, added missing `pos`/`japanese`/`vietnamese`. **Removed the false Homophones callout** on both 汎 and 帆 (retroactively editing 帆, restamped) — with the reading corrected, they are no longer homophones. Fresh grep confirms ㄈㄚㄇ is unique among independent word pages. Stamped `date-last-perfect: 2026-09-02` on both.

Next: 汎亜.

### 2026-09-02, iteration 2257 — [[words/汎亜|汎亜]]

No stand-in relationship (汎's own stand-in is itself; 亜's own is [[亜細亜]]). Mandarin fànyà, Japanese はんあ compositional. Fixed real bug: `cantonese` was faan6 aa3 instead of faan4 aa3 (matching 汎's own faan4). Filled blank `vietnamese` (phiếm Á, 汎's phiếm + 亜's á) — also the real standard Vietnamese term. Fixed malformed comma-joined `vietnamese` on 亜's own character page ("á, a" → proper list). No homophones (注音 ㄈㄚㄇㄚ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 汚.

### 2026-09-02, iteration 2258 — [[words/汚|汚]]

This word is itself the stand-in that legitimizes the character 汚. Mandarin wū, Cantonese wu1, Korean 오, Vietnamese ô all match 汚's own citation exactly. Fixed malformed `羅馬字: '''o'` → `'o`, fixed literal `vietnamese: null` → ô, added missing `japanese`(お)/`pos`/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix. `kwin: true` (諺文 오 = Korean 오). **Completes a four-way homophone group** with [[五]]/[[伍]]/[[於]], all of which already anticipated this page — added the matching callout here. Stamped `date-last-perfect: 2026-09-02`.

Next: 汚染.

### 2026-09-02, iteration 2259 — [[words/汚染|汚染]]

No stand-in relationship (汚's own stand-in is itself; 染's own is [[染色]]). Mandarin wūrǎn, Cantonese wu1 jim5, Japanese おせん, Korean 오염 all match constituent citations exactly. Filled blank `pos` (事詞) and `vietnamese` (ô nhiễm, 汚's ô + 染's nhiễm) — also the real standard Vietnamese word for "pollution." Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄛㄋ⼄ㄇ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 汚物.

### 2026-09-02, iteration 2260 — [[words/汚物|汚物]]

No stand-in relationship (both 汚's and 物's own stand-ins are themselves). Mandarin wūwù, Cantonese wu1 mat6, Japanese おぶつ, Korean 오물 all match constituent citations exactly. Filled blank `pos` (名詞) and `vietnamese` (ô vật, 汚's ô + 物's vật). `kwin: true` per AND-rule from both constituents. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄛㄇㄨㄊ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 江南.

### 2026-09-02, iteration 2261 — [[words/江南|江南]]

No stand-in relationship (江's own stand-in is [[大江]]; 南's own is [[南方]]). Mandarin Jiāngnán, Cantonese gong1 naam4, Japanese こうなん, Korean 강남 (genuinely the real district name), Vietnamese Giang Nam all match constituent citations exactly. `kwin: true` (諺文 강남 = Korean 강남). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄍㄚㄫㄋㄚㄇ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 江湖.

### 2026-09-02, iteration 2262 — [[words/江湖|江湖]]

No stand-in relationship (江's own stand-in is [[大江]]; 湖's own is [[湖水]]). Mandarin jiānghú, Cantonese gong1 wu4, Japanese こうこ, Korean 강호 all match constituent citations exactly. Vietnamese giang hồ (江's giang + 湖's hồ) is also the real standard term carrying the same "underworld/itinerant" sense. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄍㄚㄫㄏㄛㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 池.

### 2026-09-02, iteration 2263 — [[words/池|池]] & [[words/酔|酔]]

Completed the three-way homophone trio (ㄐㄨㄧ/jui/쥐) already anticipated on [[知]]'s own page: [[池]] and [[酔]], both still incomplete, finished together in this pass. 池: this word is itself the stand-in for 池; fixed literal `vietnamese: null` → tri, added missing `pos`/`japanese`(ち)/`hsk_level`("2"), reformatted `characters`. 酔: this word is itself the stand-in for 酔; filled blank `korean`/`vietnamese`, added missing `pos`/`japanese`(すい)/`hsk_level`("2"), fixed `kwin: true` → `false` (諺文 쥐 vs real Korean 취, matching 酔's own stored kwin). Both stamped `date-last-perfect: 2026-09-02`.

Next: 汲.

### 2026-09-02, iteration 2264 — [[words/汲|汲]]

This word is itself the stand-in that legitimizes the character 汲. Mandarin jí, Cantonese kap1, Korean 급, Vietnamese cấp all match 汲's own citation exactly. Fixed literal `vietnamese: null` → cấp, added missing `pos`/`japanese`(きゅう)/`hsk_level`(無), reformatted `characters` to block-list with "(char)" suffix. Checked 湆 (also ㄎㄨㄆ) — its own stand-in is 名専字, so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 決.

### 2026-09-02, iteration 2265 — [[words/決|決]]

This word is itself the stand-in that legitimizes the character 決. Mandarin jué, Cantonese kyut3, Korean 결, Vietnamese quyết all match 決's own citation exactly. Fixed literal `vietnamese: null` → quyết, added missing `pos`/`japanese`(けつ)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. Checked 缺 (also ㄎ⼔ㄊ) — its own stand-in is [[欠缺]], so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 汽油.

### 2026-09-02, iteration 2266 — [[words/汽油|汽油]]

No stand-in relationship (汽's own stand-in is [[蒸汽]]; 油's own is itself). Mandarin qìyóu, Cantonese hei3 jau4 compositional. Japanese ガソリン, Korean 가솔린 are the international loanword, same pattern as [[千米]]/[[毫米]]; Vietnamese dầu xăng is the real native term. Reformatted `hsk_level` to quoted string. Removed blank `swadesh` and empty `aliases: []`. No homophones (注音 ㄎㄧㄜ⼜ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沃素.

### 2026-09-02, iteration 2267 — [[words/沃素|沃素]]

No stand-in relationship (沃's own stand-in is [[肥沃]]; 素's own is [[要素]]). Descriptive coinage for iodine (not toponymic like the lanthanide series; no vault page for 碘 to borrow from). Mandarin wòsù, Cantonese juk1 sou3, Korean 옥소 all compositional. Japanese ヨウソ is a genuine real Japanese chemistry term (irregular reading), normalized from mixed-script ヨウそ. Filled blank `cantonese`/`vietnamese`. Removed redundant `品詞`. No homophones (注音 ㄛㄎㄙㄛ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沈菜.

### 2026-09-02, iteration 2268 — [[words/沈菜|沈菜]]

No stand-in relationship (沈's own stand-in is [[沈没]]; 菜's own is [[野菜]]). Korean 침채 is the real historical etymon of kimchi, matching constituent citations exactly. Fixed real bug: `mandarin` was contaminated to pào cài (unrelated real word 泡菜) — corrected to compositional chéncài. Filled blank `cantonese` (sam2 coi3) and `vietnamese` (chìm thái). Japanese キムチ is the modern loanword from Korean, same real-world pattern as elsewhere. `kwin: true` (諺文 침채 = Korean 침채). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄑㄧㄇㄑㄚㄧ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沈黙.

### 2026-09-02, iteration 2269 — [[words/沈黙|沈黙]]

This word is itself the stand-in that legitimizes the character 黙 (沈's own stand-in is [[沈没]], so no #cranberry). Mandarin chénmò, Japanese ちんもく, Korean 침묵 all match constituent citations. Fixed real bug: `cantonese` was cam4 mak6 instead of sam2 mak6 (matching 沈's own sam2). Filled blank `vietnamese` (trầm mặc, picking 沈's citation trầm over the more common chìm) — also the real standard Vietnamese term for "taciturn." `kwin: true` (諺文 침묵 = Korean 침묵). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄑㄧㄇㄇㄨㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沐浴.

### 2026-09-02, iteration 2270 — [[words/沐浴|沐浴]]

`#cranberry` added: both 沐's own `stand_in` AND 浴's own `stand_in` point back to this exact compound (transitivity confirmed). Mandarin mùyù, Japanese もくよく, Korean 목욕, Vietnamese mộc dục all match constituent citations exactly, also the real everyday words for "bathe." `kwin: true` (諺文 목욕 = Korean 목욕). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄇㄛㄎ⼄ㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沖積.

### 2026-09-02, iteration 2271 — [[words/沖積|沖積]]

This word is itself the stand-in that legitimizes the character 沖 (積's own stand-in is [[蓄積]], so no #cranberry). Mandarin chōngjí, Japanese ちゅうせき compositional. Filled blank `cantonese`(cung1 zik1)/`korean`(충적)/`vietnamese`(xung tích, using 沖's standard xung reading over trong/trùng). `kwin: true` (諺文 충적 = Korean 충적). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄑㄨㄫㄐㄝㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沙.

### 2026-09-02, iteration 2272 — [[words/沙|沙]] (+ retroactively fixing [[words/似|似]])

This word is itself the stand-in that legitimizes the character 沙. Added missing `pos`/`japanese`(さ)/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix.

**Real homophone found**: 沙 shares 注音/諺文/羅馬字 ㄙㄚ/사/sa with the already-stamped [[似]] ("like, as"), which had never been cross-referenced — added reciprocal callouts to both pages, retroactively restamping 似. Checked remaining ㄙㄚ characters (思/糸/寺/些/司/祠/詞/飼) — none has a self-pointing stand_in, confirming no third homophone. Both stamped `date-last-perfect: 2026-09-02`.

Next: 沙羅双樹.

### 2026-09-02, iteration 2273 — [[words/沙羅双樹|沙羅双樹]]

No stand-in relationship (羅's own stand-in is [[羅馬]]; 樹's own is [[樹木]]). `諺文`/`羅馬字`/`注音` built compositionally from all four characters. Genuine divergence: real Mandarin/Cantonese/Korean use a shorter three-character form (娑羅樹, dropping 双), matching existing aliases. Fixed real truncation bug: `cantonese` was missing its final syllable (so1 lo4 → so1 lo4 syu6). Fixed kana typo in `japanese` (しやらのき,さらじゆ → しゃらのき, さらじゅ). No homophones (注音 ㄙㄚㄌㄛㄙ⺢ㄫㄙㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 没.

### 2026-09-02, iteration 2274 — [[words/没|没]]

This word is itself the stand-in that legitimizes the character 没. Mandarin méi, Cantonese mut6, Korean 몰, Vietnamese mốt all match 没's own citation exactly. Fixed literal string bugs `korean: "null"` → 몰 and `vietnamese: null` → mốt, added missing `pos`/`japanese`(ぼつ)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. No homophones (注音 ㄇㄛㄊ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 河内.

### 2026-09-02, iteration 2275 — [[words/河内|河内]]

No stand-in relationship (河's own stand-in is [[小河]]; 内's own is [[内部]]). Mandarin Hénèi, Cantonese ho4 noi6 compositional. Japanese ハノイ, Korean 하노이 are the international loanword; Vietnamese Hà Nội is the real city name and also a perfect compositional match (Hà=河, Nội=内). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄚㄋㄛㄧ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 河馬.

### 2026-09-02, iteration 2276 — [[words/河馬|河馬]]

No stand-in relationship (河's own stand-in is [[小河]]; 馬's own is itself). Mandarin hémǎ, Cantonese ho4 maa5, Korean 하마, Vietnamese hà mã all match constituent citations exactly, also the real everyday words for "hippopotamus." Japanese カバ is the real word (historical derivation, now a katakana native term), same pattern as [[龍蝦]]/[[水牛]]. `kwin: true` (諺文 하마 = Korean 하마). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄚㄇㄚ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 治療.

### 2026-09-02, iteration 2277 — [[words/治療|治療]]

This word is itself the stand-in that legitimizes the character 療 (治's own stand-in is [[統治]], so no #cranberry). Mandarin zhìliáo, Cantonese zi6 liu4, Japanese ちりょう, Korean 치료 all match constituent citations exactly. Vietnamese trị liệu is also the real standard term for "treatment." Fixed real bug: `羅馬字`/`諺文` were contaminated to 'yoglyou/욕룟 instead of cilyou/치룟 (注音 was already correct). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄑㄧㄌ⼄ㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沼沢.

### 2026-09-02, iteration 2278 — [[words/沼沢|沼沢]]

`#cranberry` added: both 沼's own `stand_in` AND 沢's own `stand_in` point back to this exact compound (transitivity confirmed). Mandarin zhǎozé, Cantonese ziu2 zaak6, Japanese しょうたく, Korean 소택 all match constituent citations exactly. `vietnamese: đầm lầy` is the real native term, kept as-is since 沢's own character page stores no vietnamese citation (flagged for future review). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄐㄛㄨㄉㄚㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沼金.

### 2026-09-02, iteration 2279 — [[words/沼金|沼金]]

No stand-in relationship (沼's own stand-in is [[沼沢]]; 金's own is itself). Deep etymological calque for lutetium (Lutetia → Gaulish "marsh" → 沼), per the same avoided-character-reading convention as [[丹金]]/[[欧金]]: `mandarin`/`cantonese` hold 镥's own reading (lǔ/lou5); `korean`/`japanese`/`vietnamese` hold IUPAC loanword transcriptions. Removed redundant `品詞`. No homophones (注音 ㄐㄛㄨㄍㄧㄇ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沿.

### 2026-09-02, iteration 2280 — [[words/沿|沿]]

This word is itself the stand-in that legitimizes the character 沿. Mandarin yán, Cantonese jyun4, Korean 연, Vietnamese duyên all match 沿's own citation exactly. Filled blank `vietnamese`, added missing `pos`/`japanese`(えん)/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix. No homophones (注音 ⼔ㄇ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 沿海.

### 2026-09-02, iteration 2281 — [[words/沿海|沿海]]

No stand-in relationship (沿's own stand-in is itself; 海's own is [[海洋]]). Mandarin yánhǎi, Cantonese jyun4 hoi2, Japanese えんかい, Korean 연해 all match constituent citations exactly. Vietnamese duyên hải also the real standard term. Fixed real bug: `羅馬字`/`諺文` were 'wenhai/원해 instead of 'wemhai/웜해 (注音 was already correct). Filled blank `pos`. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ⼔ㄇㄏㄚㄧ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 法.

### 2026-09-02, iteration 2282 — [[words/法|法]]

This word is itself the stand-in that legitimizes the character 法. Mandarin fǎ, Cantonese faat3, Korean 법, Vietnamese pháp all match 法's own citation exactly. Filled blank `vietnamese`, added missing `pos`/`japanese`(ほう)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. Checked 琺 (also ㄈㄚㄆ) — its own stand-in is [[琺瑯]], so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 法則.

### 2026-09-02, iteration 2283 — [[words/法則|法則]]

This word is itself the stand-in that legitimizes the character 則 (法's own stand-in is itself, so no #cranberry). Mandarin fǎzé, Cantonese faat3 zak1, Japanese ほうそく, Korean 법칙 all match constituent citations exactly. Filled blank `vietnamese` (pháp tắc, 法's pháp + 則's tắc) — also the real standard term for "code, principle." Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄈㄚㄆㄐㄨㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 法素.

### 2026-09-02, iteration 2284 — [[words/法素|法素]]

Toponymic abbreviation for francium (法国 → 法 + 素), per the same avoided-character-reading convention as [[丹金]]/[[欧金]]: `mandarin`/`cantonese` hold 钫's own reading (fāng/fong1); `korean`/`japanese`/`vietnamese` hold IUPAC loanword transcriptions. Fixed real bug: `羅馬字`/`諺文`/`注音` had all been contaminated to a p-initial reading (pabso/팝소/ㄆㄚㄆㄙㄛ) instead of 法's own f-initial (fabso/빱소/ㄈㄚㄆㄙㄛ, confirmed against 法's own Words list). Removed redundant `品詞`. No homophones (注音 ㄈㄚㄆㄙㄛ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 法螺.

### 2026-09-02, iteration 2285 — [[words/法螺|法螺]]

No stand-in relationship (法's own stand-in is itself; 螺's own is [[螺旋]]). Mandarin fǎluó, Cantonese faat3 lo4, Korean 법라, Vietnamese pháp loa all match constituent citations exactly. Japanese ほら is the real contracted native reading (standard word for "boast"). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄈㄚㄆㄌㄚ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 法術.

### 2026-09-02, iteration 2286 — [[words/法術|法術]]

No stand-in relationship (both 法's and 術's own stand-ins are themselves). Synonymous with [[巫術]] (moved stray note into Notes section). Mandarin fǎshù, Cantonese faat3 seot6, Japanese ほうじゅつ, Korean 법술, Vietnamese pháp thuật all match constituent citations exactly. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄈㄚㄆㄙㄨㄊ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 法輪.

### 2026-09-02, iteration 2287 — [[words/法輪|法輪]]

No stand-in relationship (both 法's and 輪's own stand-ins are themselves). Mandarin fǎlún, Cantonese faat3 leon4, Japanese ほうりん, Korean 법륜, Vietnamese pháp luân all match constituent citations exactly, also the real Buddhist term in each language. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄈㄚㄆㄌㄨㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 泛濫.

### 2026-09-02, iteration 2288 — [[words/泛濫|泛濫]]

This word is itself the stand-in that legitimizes the character 泛 (濫's own stand-in is [[汎濫]], so no #cranberry). A third orthographic "overflow" variant alongside [[氾濫]]/[[汎濫]] — but 泛's own Dan'a'yo reading (ㄈㄧㄇ) is distinct from 氾/汎's shared ㄈㄚㄇ, confirmed via fresh grep, so no cross-variant homophone applies. Mandarin fànlàn, Cantonese faan3 laam6, Japanese はんらん, Korean 범람, Vietnamese phiếm lạm all match constituent citations (identical real-language readings to its siblings despite the distinct Dan'a'yo-internal reading). No homophones (注音 ㄈㄧㄇㄌㄚㄇ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 波浪.

### 2026-09-02, iteration 2289 — [[words/波浪|波浪]]

`#cranberry` added: both 波's own `stand_in` AND 浪's own `stand_in` point back to this exact compound (transitivity confirmed). Mandarin bōlàng, Cantonese bo1 long6, Japanese はろう compositional. Fixed real bug: `korean` was garbled comma-joined 파랑, 파도 mixing compositional form with the unrelated near-synonym 波濤's reading — corrected to 파랑. Filled blank `vietnamese` (ba lãng). Fixed missing space in `cantonese`. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄅㄚㄌㄚㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 波素.

### 2026-09-02, iteration 2290 — [[words/波素|波素]]

Semantic-phonetic hybrid abbreviation for polonium (波蘭 → 波 + 素), per the same avoided-character-reading convention as [[丹金]]/[[欧金]]/[[法素]]: `mandarin`/`cantonese` hold 钋's own reading (pō/pok3); `korean`/`japanese`/`vietnamese` hold IUPAC loanword transcriptions. Reformatted `japanese`/`vietnamese` to scalar strings, removed redundant `品詞`. No homophones (注音 ㄅㄚㄙㄛ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 泣.

### 2026-09-02, iteration 2291 — [[words/泣|泣]]

This word is itself the stand-in that legitimizes the character 泣. Mandarin qì, Cantonese jap1, Korean 읍, Vietnamese khóc all match 泣's own citation exactly (khóc also the real everyday word). Fixed literal `vietnamese: null` → khóc, added missing `pos`/`japanese`(きゅう)/`hsk_level`("4"), reformatted `characters` to block-list with "(char)" suffix. No homophones (注音 ㄎㄧㄆ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 泥.

### 2026-09-02, iteration 2292 — [[words/泥|泥]]

This word is itself the stand-in that legitimizes the character 泥. Mandarin ní, Cantonese nai4, Korean 니, Vietnamese nê all match 泥's own citation exactly. Fixed literal `vietnamese: null` → nê, added missing `pos`/`japanese`(でい)/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix. Checked 祢 (also ㄋㄝㄧ) — its own stand-in is 名専字, so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 注入.

### 2026-09-02, iteration 2293 — [[words/注入|注入]]

This word is itself the stand-in that legitimizes the character 注 (入's own stand-in is itself, so no #cranberry). Mandarin zhùrù, Cantonese zyu3 jap6, Japanese ちゅうにゅう, Korean 주입 all match constituent citations exactly. Filled blank `vietnamese` (chú nhập, 注's chú + 入's nhập) — also the real term used in technical contexts. Fixed malformed comma-joined `vietnamese` on 注's own character page ("chú, chõ, giú, chua" → proper list). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄐㄨㄋㄧㄆ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 泰国.

### 2026-09-02, iteration 2294 — [[words/泰国|泰国]]

No stand-in relationship (泰's own stand-in is [[泰然]]; 国's own is [[国家]]). Mandarin Tàiguó, Cantonese taai3 gwok3, Japanese たいこく, Korean 태국 (the real Korean name) all match constituent citations exactly. Genuine divergence: real Vietnamese uses phonetic Thái Lan rather than a calque; filled blank `vietnamese` with compositional Thái Quốc instead, same pattern as [[図書館]]/[[水族館]]. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄊㄚㄧㄍㄛㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 泳.

### 2026-09-02, iteration 2295 — [[words/泳|泳]] & [[words/詠|詠]]

**Real homophone found**: both words are their own stand-ins (legitimizing 泳 and 詠 respectively), sharing 注音/諺文/羅馬字 ㄨㄧㄫ/윙/wing. Completed both together with reciprocal callouts. 泳: fixed literal `vietnamese: null` → vạnh; 詠: added missing `vietnamese` context (already vịnh) — both added missing `pos`/`japanese`(えい)/`hsk_level` and reformatted `characters` to block-list with "(char)" suffix. Confirmed 栄/永 (also ㄨㄧㄫ) each have their own distinct stand-in, so no third homophone. Both stamped `date-last-perfect: 2026-09-02`.

Next: 洋鬼子.

### 2026-09-02, iteration 2296 — [[words/洋鬼子|洋鬼子]]

No stand-in relationship (洋's own stand-in is [[大洋]]; 鬼's own is [[鬼神]]; 子's own is [[児子]]). Mandarin yángguǐzi, Cantonese joeng4 gwai2 zi2, Japanese ようきし, Korean 양귀자 all match constituent citations exactly (primarily a Mandarin colloquialism; other-language forms are compositional references). Filled blank `vietnamese` (dương quỷ tử). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ⼘ㄫㄍㄨㄧㄐㄜ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 洗.

### 2026-09-02, iteration 2297 — [[words/洗|洗]], [[words/蝉|蝉]] & [[words/禅|禅]]

**Real homophone found**: a genuine three-way group (ㄙㄝㄋ/선/sen), all three their own stand-ins, none previously cross-referenced — completed together with reciprocal callouts. 洗: fixed literal `vietnamese: null` → tẩy (the standard reading, as in tẩy rửa), added missing `pos`/`japanese`(せん)/`hsk_level`("1"). 蝉: fixed literal `korean: "null"` → 선 and `vietnamese: null` → thiền, added missing `pos`/`hsk_level`(無); japanese せみ is the real native word for cicada. 禅: added missing `japanese`(ぜん, source of the English "Zen" loanword)/`hsk_level`(無). All reformatted `characters` to block-list with "(char)" suffix. Checked remaining ㄙㄝㄋ characters (先/宣/擅/申/銑) — none has a self-pointing stand-in, confirming no fourth homophone. All three stamped `date-last-perfect: 2026-09-02`.

Next: 洗濯.

### 2026-09-02, iteration 2298 — [[words/洗濯|洗濯]]

This word is itself the stand-in that legitimizes the character 濯 (洗's own stand-in is itself, so no #cranberry). Mandarin xǐzhuó, Cantonese sai2 zok6, Japanese せんたく compositional. Korean 세탁 is the real universal word for "laundry," using the common alternate reading 세 rather than 洗's stored 선 — a real-word-over-citation divergence. Filled blank `vietnamese` (tẩy trạc, compositional; real Vietnamese uses native giặt). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄝㄋㄉㄚㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 洗車.

### 2026-09-02, iteration 2299 — [[words/洗車|洗車]]

No stand-in relationship (both 洗's and 車's own stand-ins are themselves). Mandarin xǐchē, Cantonese sai2 ce1, Japanese せんしゃ compositional. Korean 세차 is the real word using the common alternate 洗 reading (same pattern as [[洗濯]]). Fixed real bug: `諺文`/`羅馬字`/`注音` were contaminated to a naive transcription of 車's real Mandarin reading (차/ca/ㄑㄚ) instead of 車's own Dan'a'yo reading (촤/cwa/ㄑ⺢, confirmed against [[汽車]]/[[乗車]]). Filled blank `vietnamese` (tẩy xa, matching [[乗車]]'s xa choice). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄝㄋㄑ⺢ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 洪水.

### 2026-09-02, iteration 2300 — [[words/洪水|洪水]]

This word is itself the stand-in that legitimizes the character 洪 (水's own stand-in is itself, so no #cranberry). Synonymous with [[大水]]. Mandarin hóngshuǐ, Cantonese hung4 seoi2, Japanese こうずい, Korean 홍수, Vietnamese hồng thuỷ all match constituent citations exactly, also the real everyday words for "flood." `kwin: true` (諺文 홍수 = Korean 홍수). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄛㄫㄙㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 活.

### 2026-09-02, iteration 2301 — [[words/活|活]] (+ retroactively fixing [[words/滑|滑]])

This word is itself the stand-in that legitimizes the character 活. Fixed literal `vietnamese: null` → hoạt, added missing `pos`/`japanese`(かつ)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. Fixed notation bug: `注音` was spelled ㄏㄨㄚㄊ instead of the vault's standard compact glyph ㄏ⺢ㄊ (matching [[生活]]/[[復活]]).

**Real homophone found**: 活 shares 注音/諺文/羅馬字 ㄏ⺢ㄊ/홛/hwad with the already-stamped [[滑]] ("slippery"), never cross-referenced — added reciprocal callouts to both, retroactively restamping 滑. Checked 闊 (distinct ㄎ⺢ㄊ reading) — not a third homophone. Both stamped `date-last-perfect: 2026-09-02`.

Next: 派生.

### 2026-09-02, iteration 2302 — [[words/派生|派生]]

This word is itself the stand-in that legitimizes the character 派 (生's own stand-in is [[生活]], so no #cranberry). Mandarin pàishēng, Cantonese paai3 sang1, Japanese はせい, Korean 파생 all match constituent citations exactly. Filled blank `vietnamese` (phái sinh, picking 派's phái + 生's sinh) — also the real standard finance/math term for "derivative." Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄆㄚㄧㄙㄚㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 流動.

### 2026-09-02, iteration 2303 — [[words/流動|流動]]

This word is itself the stand-in that legitimizes the character 流 (動's own stand-in is itself, so no #cranberry). Mandarin liúdòng, Cantonese lau4 dung6, Japanese りゅうどう, Vietnamese lưu động (also the real standard term) all match constituent citations exactly. Fixed real bug: `korean` was garbled comma-joined 유동,류동 mixing South Korean 두음법칙 form with correct North Korean 류동 — corrected to 류동. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄌ⼜ㄉㄛㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 流域.

### 2026-09-02, iteration 2304 — [[words/流域|流域]]

No stand-in relationship (流's own stand-in is [[流動]]; 域's own is itself). Mandarin liúyù, Cantonese lau4 wik6, Japanese りゅういき, Vietnamese lưu vực (also real standard term) all match constituent citations exactly. Fixed real bug: `korean` was South-Korean-shifted 유역 — corrected to North Korean 류역, matching 流's own citation. Removed redundant `品詞`. No homophones (注音 ㄌ⼜·ㄨㄧㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 流暢.

### 2026-09-02, iteration 2305 — [[words/流暢|流暢]]

No stand-in relationship (流's own stand-in is [[流動]]; 暢's own is [[暢達]]). Mandarin liúchàng, Cantonese lau4 coeng3, Japanese りゅうちょう compositional. Fixed real bug: `korean` was South-Korean-shifted 유창 — corrected to North Korean 류창. Filled blank `vietnamese` (lưu sướng, compositional; real Vietnamese uses divergent lưu loát). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄌ⼜ㄑㄚㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 流水.

### 2026-09-02, iteration 2306 — [[words/流水|流水]]

No stand-in relationship (流's own stand-in is [[流動]]; 水's own is itself). Mandarin liúshuǐ, Cantonese lau4 seoi2, Japanese りゅうすい, Vietnamese lưu thủy (also real term, cao sơn lưu thủy idiom) all match constituent citations exactly. Fixed real bug: `korean` was South-Korean-shifted 유수 — corrected to North Korean 류수. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄌ⼜ㄙㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 流言.

### 2026-09-02, iteration 2307 — [[words/流言|流言]]

No stand-in relationship (流's own stand-in is [[流動]]; 言's own is itself). Mandarin liúyán, Cantonese lau4 jin4 compositional. Fixed kana typo in `japanese` (りうげん → りゅうげん). Fixed real bug: `korean` was South-Korean-shifted 유언 — corrected to North Korean 류언. Filled blank `vietnamese` (lưu ngôn). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄌ⼜ㄝㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 浅.

### 2026-09-02, iteration 2308 — [[words/浅|浅]] & [[words/穿|穿]]

**Real homophone found**: both words are their own stand-ins (legitimizing 浅 and 穿 respectively), sharing 注音/諺文/羅馬字 ㄑㄝㄋ/천/cen. Completed both together with reciprocal callouts. 浅: fixed literal `korean: "null"` → 천 and `vietnamese: null` → thiển, added missing `pos`/`japanese`(せん)/`hsk_level`("4"). 穿: added missing `pos`/`japanese`(せん)/`hsk_level`("1"). Both reformatted `characters` to block-list with "(char)" suffix. Confirmed 千/喘/舛/茜/詮/釧/遷 (also ㄑㄝㄋ) each have their own distinct stand-in, so no third homophone. Both stamped `date-last-perfect: 2026-09-02`.

Next: 浅薄.

### 2026-09-02, iteration 2309 — [[words/浅薄|浅薄]]

No stand-in relationship (浅's own stand-in is itself; 薄's own is [[希薄]]). Mandarin qiǎnbó, Cantonese cin2 bok6, Japanese せんぱく, Korean 천박 all match constituent citations exactly. Filled blank `vietnamese` (thiển bạc, also a real Vietnamese term). Reformatted `characters` with "(char)" suffix on 浅. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄑㄝㄋㄅㄚㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 浜.

### 2026-09-02, iteration 2310 — [[words/浜|浜]]

This word is itself the stand-in that legitimizes the character 浜. Mandarin bāng, Cantonese bong1, Korean 빈, Vietnamese banh all match 浜's own citation exactly. Fixed literal `vietnamese: null` → banh, added missing `pos`/`japanese`(ひん)/`hsk_level`(無), reformatted `characters` to block-list with "(char)" suffix. Checked 檳/瀕/賓/貧 (also ㄅㄧㄋ) — none has a self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 浦.

### 2026-09-02, iteration 2311 — [[words/浦|浦]]

This word is itself the stand-in that legitimizes the character 浦. Mandarin pǔ, Cantonese pou2, Korean 포, Vietnamese phố all match 浦's own citation exactly. Added missing `japanese`(ほ)/`hsk_level`(無), reformatted `characters` to block-list with "(char)" suffix. Checked 怖/普 (also ㄆㄛ) — neither has a self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 浬.

### 2026-09-02, iteration 2312 — [[words/浬|浬]]

This word is itself the stand-in that legitimizes the character 浬. Mandarin lǐ, Cantonese lei5, Japanese り, Korean 리, Vietnamese rí all match 浬's own citation exactly. Added missing `hsk_level`(無), reformatted `characters` to block-list with "(char)" suffix. **Completes a three-way homophone group** with [[厘]]/[[里]], both of which already anticipated this page — added the matching callout here. Checked 吏/罹/李/理/鯉/裏 (also ㄌㄧ) — none has a self-pointing stand-in, confirming no fourth homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 浮.

### 2026-09-02, iteration 2313 — [[words/浮|浮]]

This word is itself the stand-in that legitimizes the character 浮. Mandarin fú, Cantonese fau4, Korean 부, Vietnamese phù all match 浮's own citation exactly. Fixed literal `vietnamese: null` → phù, added missing `pos`/`japanese`(ふ)/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix. No homophones (注音 ㄅㄨㄛ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 浴室.

### 2026-09-02, iteration 2314 — [[words/浴室|浴室]]

No stand-in relationship (浴's own stand-in is itself; 室's own is [[房室]]). Mandarin yùshì, Cantonese juk6 sat1, Japanese よくしつ, Korean 욕실 all match constituent citations exactly. Fixed doubled/malformed `mandarin` (yùshì, yùshǐ → yùshì). Filled blank `vietnamese` (dục thất). Reformatted `hsk_level` to quoted string. Removed blank `swadesh` and empty `aliases: []`. No homophones (注音 ⼄ㄎㄙㄧㄊ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海上.

### 2026-09-02, iteration 2315 — [[words/海上|海上]] & [[words/海象|海象]]

**Real homophone found**: 上 and 象 share the identical Dan'a'yo reading (syang/샹/ㄙ⼘ㄫ), despite distinct MC initials that both collapse to the same Dan'a'yo syllable — making 海上 and 海象 genuine two-way homophones, confirmed via fresh grep with no third match. Added reciprocal callouts to both. 海上: filled blank `vietnamese` (hải thượng), removed redundant `品詞`. 海象: japanese セイウチ is the real word for walrus (Ainu loanword), same pattern as [[龍蝦]]/[[水牛]]/[[河馬]]. Both stamped `date-last-perfect: 2026-09-02`.

Next: 海亀.

### 2026-09-02, iteration 2316 — [[words/海亀|海亀]]

No stand-in relationship (海's own stand-in is [[海洋]]; 亀's own is itself). Mandarin hǎiguī, Cantonese hoi2 gwai1, Korean 해구 all match constituent citations exactly. Fixed real bug: `japanese` was ウミガメのスープ ("sea turtle soup") — corrected to ウミガメ, the real native word for "sea turtle." Filled blank `vietnamese` (hải quy). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄚㄧㄍㄨㄛ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海就.

### 2026-09-02, iteration 2317 — [[words/海就|海就]]

就 used purely as a phonetic-substitute graph for 鷲 ("eagle"), which has no character page (matching aliases 海鹫/海鷲); mandarin hǎijiù compositional. `諺文`/`羅馬字`/`注音` deliberately diverge from 就's own stored reading (쵀/cwai) — a distinct Dan'a'yo-internal reading for this substitution use. Filled blank `cantonese`(hoi2 zau6)/`korean`(해취, matching 就's real Sino-Korean citation)/`vietnamese`(hải thứu, the distinct real reading for 鷲 specifically, as in Linh Thứu Sơn). No homophones (注音 ㄏㄚㄧ·ㄐㄨㄛ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海峡.

### 2026-09-02, iteration 2318 — [[words/海峡|海峡]]

This word is itself the stand-in that legitimizes the character 峡 (海's own stand-in is [[海洋]], so no #cranberry). Mandarin hǎixiá, Cantonese hoi2 haap6, Japanese かいきょう, Korean 해협 all match constituent citations exactly (Korean uses 峡's real Sino reading 협, distinct from Dan'a'yo-internal hab per its own kwin: false). Filled blank `vietnamese` (hải hiệp). Removed redundant `品詞`, reformatted `japanese` to scalar. No homophones (注音 ㄏㄚㄧㄏㄚㄆ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海牛.

### 2026-09-02, iteration 2319 — [[words/海牛|海牛]]

No stand-in relationship (海's own stand-in is [[海洋]]; 牛's own is itself). Mandarin hǎiniú, Cantonese hoi2 ngau4 compositional. Japanese マナティー, Korean 매너티 are the international loanword; Vietnamese lợn biển is the real native term ("sea pig"), same pattern as [[龍蝦]]/[[水牛]]/[[河馬]]. Fixed erroneous capitalization on `vietnamese`. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧㄋ⼜ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海狸.

### 2026-09-02, iteration 2320 — [[words/海狸|海狸]]

No stand-in relationship (海's own stand-in is [[海洋]]; 狸's own is itself). Mandarin hǎilí, Cantonese hoi2 lei4 compositional. Fixed real bug: `羅馬字`/`諺文`/`注音` were contaminated to a naive transcription of 狸's real reading (li/리/ㄌㄧ) instead of 狸's own Dan'a'yo reading (르/lǝ/ㄌㄜ) — corrected to hailǝ/해르/ㄏㄚㄧㄌㄜ. Japanese かいり compositional; Korean 비버 (loanword) and Vietnamese hải ly are real standard terms. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧㄌㄜ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海王星.

### 2026-09-02, iteration 2321 — [[words/海王星|海王星]]

No stand-in relationship (海's own stand-in is [[海洋]]; 王's/星's own are each themselves). Mandarin Hǎiwángxīng, Cantonese hoi2 wong4 sing1, Japanese かいおうせい, Korean 해왕성 all match constituent citations exactly, also the real name for the planet. Filled blank `vietnamese` (Hải Vương Tinh, also the real name). `kwin: true` (諺文 해왕성 = Korean 해왕성). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧ·⺢ㄫㄙㄝㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海禁.

### 2026-09-02, iteration 2322 — [[words/海禁|海禁]] & [[words/海金|海金]]

**Real homophone found**: 禁 and 金 share the identical Dan'a'yo reading (gim/김/ㄍㄧㄇ), making 海禁 and 海金 genuine two-way homophones — added reciprocal callouts to both. 海禁: added missing `kwin: false` (諺文 해김 vs Korean 해금); mandarin hǎijìn, Cantonese hoi2 gam3, Japanese かいきん, Korean 해금, Vietnamese hải cấm all match constituent citations. 海金: toponymic neptunium coinage per [[丹金]]/[[欧金]]/[[沼金]] convention (mandarin/cantonese hold 镎's own reading); removed redundant `品詞`. Both stamped `date-last-perfect: 2026-09-02`.

Next: 海粛.

### 2026-09-02, iteration 2323 — [[words/海粛|海粛]]

粛 used as a phonetic-substitute graph for 嘯 (no character page), the real word being 海嘯 "tsunami" (matching aliases). Fixed real bug: `羅馬字`/`注音` were missing their final consonant (haisu/ㄏㄚㄧㄙㄨ) — corrected to haisug/ㄏㄚㄧㄙㄨㄎ, matching 諺文 해숙 and 粛's own citation. Mandarin hǎixiào/Cantonese hoi2 siu3 reflect the real word 海嘯. Fixed historical kana `かいせう`→かいしょう and reformatted with つなみ. Fixed `korean` (likely-contaminated 해소 → 해일, the real word for tsunami). Filled blank `vietnamese` (sóng thần, real native term). No homophones (注音 ㄏㄚㄧㄙㄨㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海草.

### 2026-09-02, iteration 2324 — [[words/海草|海草]]

No stand-in relationship (海's own stand-in is [[海洋]]; 草's own is itself). Mandarin hǎicǎo, Cantonese hoi2 cou2, Japanese かいそう, Korean 해초 all match constituent citations exactly. Fixed stray-kanji typo in `japanese` (かい草そう → かいそう). Vietnamese tảo biển is the real native term, kept as-is. Fixed malformed comma-joined `vietnamese` on 草's own character page ("thảo, tháu, xáo" → proper list). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧㄑㄚㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海藻.

### 2026-09-02, iteration 2325 — [[words/海藻|海藻]]

This word is itself the stand-in that legitimizes the character 藻 (海's own stand-in is [[海洋]], so no #cranberry). Mandarin hǎizǎo, Cantonese hoi2 zou2, Japanese かいそう (coincidentally matching sibling [[海草]] via shared SOU on'yomi) all match constituent citations. Fixed real bug: `korean` was 해초, contaminated from [[海草]] — corrected to 해조, matching 藻's own citation. Vietnamese tảo biển matches 藻's citation, also real term. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧㄐㄛㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海豚.

### 2026-09-02, iteration 2326 — [[words/海豚|海豚]]

No stand-in relationship (海's own stand-in is [[海洋]]; 豚's own is itself). Mandarin hǎitún, Cantonese hoi2 tyun4, Korean 해돈 all match constituent citations exactly. Japanese いるか, Vietnamese cá heo are the real native words, same pattern as [[龍蝦]]/[[水牛]]/[[河馬]]/[[海牛]]. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧㄉㄛㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海豹.

### 2026-09-02, iteration 2327 — [[words/海豹|海豹]]

No stand-in relationship (海's own stand-in is [[海洋]]; 豹's own is [[豹猫]]). Mandarin hǎibào, Cantonese hoi2 paau3 compositional. Japanese アザラシ, Korean 물범, Vietnamese hải cẩu are the real native words, same pattern as [[龍蝦]]/[[河馬]]. Fixed real bugs: `korean` was garbled comma-joined 물범, 물개 (seal + unrelated sea lion) — corrected to 물범; `vietnamese` was dấu niêm (mistranslated "seal" as stamp) — corrected to hải cẩu. Added missing `kwin: false`. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄧㄅ⼘ㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海防.

### 2026-09-02, iteration 2328 — [[words/海防|海防]]

No stand-in relationship (海's own stand-in is [[海洋]]; 防's own is [[防護]]). Mandarin hǎifáng, Cantonese hoi2 fong4, Japanese かいぼう, Korean 해방, Vietnamese hải phòng (also the real city name Haiphong) all match constituent citations exactly. `kwin: true` (諺文 해방 = Korean 해방). File was already essentially complete; added stand-in note and stamp. No homophones (注音 ㄏㄚㄧㄅㄚㄫ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海馬.

### 2026-09-02, iteration 2329 — [[words/海馬|海馬]]

No stand-in relationship (海's own stand-in is [[海洋]]; 馬's own is itself). Mandarin hǎimǎ, Cantonese hoi2 maa5, Korean 해마 all match constituent citations exactly. Japanese うみうま, Vietnamese cá ngựa are the real native words, same pattern as [[河馬]]/[[海牛]]/[[海豚]]. `kwin: true` (諺文 해마 = Korean 해마). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄚㄧㄇㄚ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 海鼠.

### 2026-09-02, iteration 2330 — [[words/海鼠|海鼠]]

No stand-in relationship (海's own stand-in is [[海洋]]; 鼠's own is [[熊鼠]]). Filled blank `mandarin`/`cantonese`, compositional (hǎishǔ/hoi2 syu2). Japanese なまこ is the real term for this exact spelling. Filled blank `vietnamese` (hải thử, compositional; real Vietnamese uses hải sâm from the alternate 海參). No homophones (注音 ㄏㄚㄧㄙ⼄ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 浸.

### 2026-09-02, iteration 2331 — [[words/浸|浸]]

This word is itself the stand-in that legitimizes the character 浸. Mandarin jìn, Cantonese zam3, Korean 침, Vietnamese tẩm all match 浸's own citation exactly. Fixed literal `vietnamese: null` → tẩm, added missing `pos`/`japanese`(しん)/`hsk_level`("3"), reformatted `characters` to block-list with "(char)" suffix. Homophone with [[寝]] already fully documented on 寝's own page (coincidental phonetic-root collision, not shared etymology). Confirmed 沈/侵 (also ㄑㄧㄇ) each have their own distinct stand-in, so no third homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 浸食.

### 2026-09-02, iteration 2332 — [[words/浸食|浸食]]

No stand-in relationship (both 浸's and 食's own stand-ins are themselves). Mandarin jìnshí, Japanese しんしょく, Korean 침식 all match constituent citations exactly. Fixed real bugs: `mandarin` was doubled with near-synonym 侵食's reading (jìnshí,qīnshí → jìnshí); `cantonese` was contaminated to cam1 sik6 (also from 侵) instead of zam3 sik6. Filled blank `vietnamese` (tẩm thực, compositional; real Vietnamese uses xâm thực from alias 侵食). No homophones (注音 ㄑㄧㄇㄙㄧㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 消.

### 2026-09-02, iteration 2333 — [[words/消|消]] & [[words/笑|笑]]

**Real homophone found**: both words are their own stand-ins (legitimizing 消 and 笑 respectively), sharing 注音/諺文/羅馬字 ㄙ⼄ㄨ/숏/syou. Completed both together with reciprocal callouts. 消: fixed literal `vietnamese: null` → tiêu, added missing `pos`/`japanese`(しょう)/`hsk_level`("1"). 笑: fixed literal `vietnamese: null` → tiếu, added missing `pos`/`japanese`(しょう)/`hsk_level`("1"). Both reformatted `characters` to block-list with "(char)" suffix. Confirmed 召/哨/焼/肖/宵/紹/硝/逍/邵 (also ㄙ⼄ㄨ) each have their own distinct stand-in, so no third homophone. Both stamped `date-last-perfect: 2026-09-02`.

Next: 涙.

### 2026-09-02, iteration 2334 — [[words/涙|涙]]

This word is itself the stand-in that legitimizes the character 涙. Mandarin lèi, Cantonese leoi6, Korean 루, Vietnamese lệ all match 涙's own citation exactly. Fixed literal `korean: "null"` → 루 and `vietnamese: null` → lệ, added missing `pos`/`japanese`(るい), reformatted `characters` to block-list with "(char)" suffix (hsk_level left absent, matching 涙's own empty-string citation gap). Checked 累/塁/類/羸 (also ㄌㄨㄧ) — none has a self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 涯.

### 2026-09-02, iteration 2335 — [[words/涯|涯]]

This word is itself the stand-in that legitimizes the character 涯. Mandarin yá, Cantonese ngaai4, Korean 애, Vietnamese nhai all match 涯's own citation exactly. Added missing `japanese`(がい)/`hsk_level`(無), reformatted `characters` to block-list with "(char)" suffix. Completed the reciprocal homophone callout with [[刈]] (already anticipated on 刈's own page). Confirmed 乂/娃 (also ⼘ㄧ) have distinct stand-ins, so no third homophone. Stamped `date-last-perfect: 2026-09-02`.

Next: 液体.

### 2026-09-02, iteration 2336 — [[words/液体|液体]]

This word is itself the stand-in that legitimizes the character 液 (体's own stand-in is [[体系]], so no #cranberry). Mandarin yètǐ, Cantonese jik6 tai2, Japanese えきたい, Korean 액체 all match constituent citations exactly. Filled blank `vietnamese` (dịch thể, a real Sino-Vietnamese technical term). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ⼶ㄎㄊㄝㄧ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 淡水.

### 2026-09-02, iteration 2337 — [[words/淡水|淡水]]

No stand-in relationship (淡's own stand-in is [[清淡]]; 水's own is itself). Mandarin dànshuǐ, Japanese たんすい, Korean 담수 all match constituent citations exactly. Fixed real bug: `cantonese` was taam5 seoi2 instead of daam6 seoi2, matching 淡's own daam6. Vietnamese đạm thủy also a real term. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄉㄚㄇㄙㄨ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 淡麻.

### 2026-09-02, iteration 2338 — [[words/淡麻|淡麻]]

No stand-in relationship (淡's own stand-in is [[清淡]]; 麻's own is [[大麻]]). Korean 담마 compositional. Fixed real bugs: `mandarin` was contaminated to qiánmá (near-synonym alias 蕁麻's reading) — corrected to dànmá; `cantonese` was similarly contaminated to cam4 maa4 — corrected to daam6 maa4. Japanese いらくさ, Vietnamese tầm ma are the real plant-name terms, same convention as animal names. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄉㄚㄇㄇㄚ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 淫靡.

### 2026-09-02, iteration 2339 — [[words/淫靡|淫靡]]

This word is itself the stand-in that legitimizes the character 靡 (淫's own stand-in is itself, so no #cranberry). Mandarin yínmǐ, Cantonese jam4 mei5, Japanese いんび, Korean 음미, Vietnamese dâm mĩ all match constituent citations exactly — file was already essentially complete. Reformatted `characters` with "(char)" suffix quoting. No homophones (注音 ㄧㄇㄇㄧㄆ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 深刻.

### 2026-09-02, iteration 2340 — [[words/深刻|深刻]]

This word is itself the stand-in that legitimizes the character 深 (刻's own stand-in is [[刻印]], so no #cranberry). Mandarin shēnkè, Japanese しんこく, Korean 심각 (深's 심 + 刻's 각) all match constituent citations exactly. Fixed missing space in `cantonese`. Filled blank `pos`(性詞) and `vietnamese`(thâm khắc). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄙㄧㄇㄎㄨㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 深奥.

### 2026-09-02, iteration 2341 — [[words/深奥|深奥]]

No stand-in relationship (深's own stand-in is [[深刻]]; 奥's own is itself). Mandarin shēn'ào, Cantonese sam1 ou3, Japanese しんおう, Korean 심오 all match constituent citations exactly. Filled blank `pos`(性詞) and `vietnamese`(thâm áo, also a real term for "profound"). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄙㄧㄇㄨㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 深淵.

### 2026-09-02, iteration 2342 — [[words/深淵|深淵]]

This word is itself the stand-in that legitimizes the character 淵 (深's own stand-in is [[深刻]], so no #cranberry). Mandarin shēnyuān, Cantonese sam1 jyun1, Japanese しんえん, Korean 심연 all match constituent citations exactly. Fixed `pos` from 固有名詞 to 名詞 (common noun, matching 淵's own pos) and lowercased `english` "Abyss"→"abyss". Filled blank `vietnamese` (thâm uyên, already discussed in prose but missing from frontmatter). No homophones (注音 ㄙㄧㄇ⼔ㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 深長.

### 2026-09-02, iteration 2343 — [[words/深長|深長]]

No stand-in relationship (深's own stand-in is [[深刻]]; 長's own is itself). Mandarin shēncháng, Cantonese sam1 coeng4, Japanese しんちょう, Korean 심장 all match constituent citations exactly. Filled blank `pos`(性詞) and `vietnamese`(thâm trường). Completed the reciprocal homophone callout with [[心臓]] (already documented there). Stamped `date-last-perfect: 2026-09-02`.

Next: 混乱.

### 2026-09-02, iteration 2344 — [[words/混乱|混乱]]

This word is itself the stand-in that legitimizes the character 乱 (混's own stand-in is [[混合]], so no #cranberry). Mandarin hùnluàn, Japanese こんらん, Korean 혼란 all match constituent citations exactly. Fixed doubled `mandarin` value. Filled blank `cantonese`(wan6 lyun6) and `vietnamese`(hỗn loạn, also the real standard term for "chaos"). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄛㄋㄌㄚㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 混合.

### 2026-09-02, iteration 2345 — [[words/混合|混合]]

This word is itself the stand-in that legitimizes the character 混 (合's own stand-in is itself, so no #cranberry). Mandarin hùnhé, Cantonese wan6 hap6, Japanese こんごう, Korean 혼합 all match constituent citations exactly. Vietnamese hỗn hợp also the real standard term for "mixture." Fixed malformed comma-joined `vietnamese` on 合's own character page (seven-item string → proper list). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄛㄋㄎㄚㄆ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 混濁.

### 2026-09-02, iteration 2346 — [[words/混濁|混濁]]

This word is itself the stand-in that legitimizes the character 濁 (混's own stand-in is [[混合]], so no #cranberry). Mandarin hùnzhuó, Cantonese wan6 zuk6, Japanese こんだく, Korean 혼탁 all match constituent citations exactly. Filled blank `vietnamese` (hỗn trọc, also real term). Fixed malformed comma-joined `vietnamese` on 濁's own character page (three-item string → proper list). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄛㄋㄉㄚㄎ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 混然.

### 2026-09-02, iteration 2347 — [[words/混然|混然]]

No stand-in relationship (混's own stand-in is [[混合]]; 然's own is itself). Mandarin húnrán preserves the classical hún tone (distinct from everyday hùn), matching real usage. Japanese こんぜん, Korean 혼연 compositional. Fixed doubled/malformed `cantonese` (wan4 jin4 / wan6 jin4 → wan6 jin4, matching 混's own wan6). Filled blank `vietnamese` (hỗn nhiên, compositional). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄛㄋㄋ⼶ㄋ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 清淡.

### 2026-09-02, iteration 2348 — [[words/清淡|清淡]]

This word is itself the stand-in that legitimizes the character 淡 (清's own stand-in is [[清潔]], so no #cranberry). Mandarin qīngdàn, Cantonese cing1 daam6, Japanese せいたん, Korean 청담 all match constituent citations exactly. Filled blank `vietnamese` (thanh đạm, also the real standard term for "light/bland food"). No homophones (注音 ㄑㄧㄫㄉㄚㄇ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 清潔.

### 2026-09-02, iteration 2349 — [[words/清潔|清潔]]

`#cranberry` added: both 清's own `stand_in` AND 潔's own `stand_in` point back to this exact compound (transitivity confirmed). Mandarin qīngjié, Cantonese cing1 git3, Japanese せいけつ, Korean 청결, Vietnamese thanh khiết all match constituent citations exactly. Fixed real bug: `羅馬字` was truncated to just "cing" — corrected to cingged, matching 諺文/注音. Removed the word's own title from its `aliases` list. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄑㄧㄫㄍㄝㄊ unique). Stamped `date-last-perfect: 2026-09-02`.

Next: 清酒.

### 2026-09-03, iteration 2350 — [[words/清酒|清酒]]

No stand-in relationship (清's own stand-in is [[清潔]]; 酒's own is [[酒精]]). Mandarin qīngjiǔ, Japanese せいしゅ compositional. Fixed real bugs: `cantonese` doubled with malformed variant (cing1 zau2, ceng1 zau2 → cing1 zau2); `korean` was bare native 술 instead of compositional 청주 (also the real Korean rice-wine name), matching 酒's Sino citation 주. Vietnamese sake is the real loanword. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄑㄧㄫㄐㄨㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 清音.

### 2026-09-03, iteration 2351 — [[words/清音|清音]]

No stand-in relationship (清's own stand-in is [[清潔]]; 音's own is [[音楽]]). Mandarin qīngyīn, Cantonese cing1 jam1, Japanese せいおん, Korean 청음 all match constituent citations exactly, also the real linguistics term. Filled blank `vietnamese` (thanh âm). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄑㄧㄫㄨㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 渇金.

### 2026-09-03, iteration 2352 — [[words/渇金|渇金]]

No stand-in relationship (渇's own stand-in is itself; 金's own is itself). Mythological calque for tantalum (Tantalus's eternal thirst → 渇), per the same avoided-character-reading convention as [[丹金]]/[[欧金]]: `mandarin`/`cantonese` hold 钽's own reading (tǎn/taan2); `korean`/`japanese`/`vietnamese` hold IUPAC loanword transcriptions. Reformatted `japanese` to scalar, removed redundant `品詞`. No homophones (注音 ㄎㄚㄊㄍㄧㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 済.

### 2026-09-03, iteration 2353 — [[words/済|済]]

This word is itself the stand-in that legitimizes the character 済. Mandarin jì, Cantonese zai3, Korean 제 all match 済's own citation exactly. Added missing `pos`/`japanese`(さい), reformatted `characters` to block-list with "(char)" suffix (vietnamese left blank, matching 済's own empty citation — flagged gap). Checked 制/剤/斉/除/𦜝 (also ㄐㄝㄧ) — none has a self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 渉.

### 2026-09-03, iteration 2354 — [[words/渉|渉]]

This word is itself the stand-in that legitimizes the character 渉 (a Japanese shinjitai variant of 涉). Mandarin shè, Cantonese sip3, Korean 섭 all match 渉's own citation exactly. Fixed literal `korean: "null"` → 섭, added missing `pos`/`japanese`(しょう), reformatted `characters` to block-list with "(char)" suffix (vietnamese left blank, matching 渉's own empty citation gap). No homophones (注音 ㄙㄝㄆ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 渓流.

### 2026-09-03, iteration 2355 — [[words/渓流|渓流]]

This word is itself the stand-in that legitimizes the character 渓 (流's own stand-in is [[流動]], so no #cranberry). Mandarin xīliú, Japanese けいりゅう, Korean 계류 (real term, coexisting with unrelated homophone 繋留) all match constituent citations exactly. Filled blank `cantonese`(kai1 lau4); vietnamese left blank matching 渓's own empty citation. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄎㄝㄧㄌ⼜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 減法.

### 2026-09-03, iteration 2356 — [[words/減法|減法]]

No stand-in relationship (減's own stand-in is [[減算]]; 法's own is itself). Mandarin jiǎnfǎ, Cantonese gaam2 faat3 compositional. Fixed real bugs: `japanese` was malformed げんぱふ → げんほう; `korean` was garbled comma-joined 감법, 뺄셈 (compositional + native) — corrected to 감법. Filled blank `vietnamese` (giảm pháp, compositional; real Vietnamese uses phép trừ). Added missing `kwin: false`. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄍㄚㄇㄈㄚㄆ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 減算.

### 2026-09-03, iteration 2357 — [[words/減算|減算]]

This word is itself the stand-in that legitimizes the character 減 (算's own stand-in is itself, so no #cranberry). `諺文`/`羅馬字`/`注音` were already correct. Fixed a major real bug: `mandarin`/`japanese`/`korean` had all been contaminated with the antonym 加算's readings (jiāsuàn/かさん/가산, "addition") — corrected to jiǎnsuàn/げんさん/감산 ("subtraction"), matching 減's/算's own citations. Filled blank `cantonese`(gaam2 syun3)/`vietnamese`(giảm toán). Verified [[加算]] itself is unaffected and correctly holds its own readings. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄍㄚㄇㄙ⺢ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 渡.

### 2026-09-03, iteration 2358 — [[words/渡|渡]]

This word is itself the stand-in that legitimizes the character 渡. Mandarin dù, Cantonese dou6, Korean 도, Vietnamese độ all match 渡's own citation exactly. Fixed `japanese`: ど (wrong voicing) with trailing invisible space → と, matching 渡's own on'yomi TO. Added missing `hsk_level`("2"), removed redundant `品詞`. Checked 図/堵/徒/妬/度/屠/杜/賭/都/鍍 (also ㄉㄛ) — none has a self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 渣.

### 2026-09-03, iteration 2359 — [[words/渣|渣]]

This word is itself the stand-in that legitimizes the character 渣. Mandarin zhā, Cantonese zaa1, Korean 사, Vietnamese tra all match 渣's own citation exactly. Added missing `japanese`(さ)/`hsk_level`("3"). Completed the reciprocal homophone callout with [[坐]] (already anticipated on 坐's own page). Checked 竃/挫 (also ㄐ⺢) — no third homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 渦流.

### 2026-09-03, iteration 2360 — [[words/渦流|渦流]]

This word is itself the stand-in that legitimizes the character 渦 (流's own stand-in is [[流動]], so no #cranberry). Mandarin wōliú, Cantonese wo1 lau4, Japanese かりゅう, Korean 와류 all match constituent citations exactly. Filled blank `vietnamese` (oa lưu). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄍ⺢ㄌ⼜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 温度.

### 2026-09-03, iteration 2361 — [[words/温度|温度]]

No stand-in relationship (温's own stand-in is [[温暖]]; 度's own is [[程度]]). Mandarin wēndù, Cantonese wan1 dou6, Japanese おんど, Korean 온도 all match constituent citations exactly. Filled blank `vietnamese` (ôn độ, compositional; real Vietnamese uses nhiệt độ from 熱). `kwin: true` (諺文 온도 = Korean 온도). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄛㄆㄉㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 温暖.

### 2026-09-03, iteration 2362 — [[words/温暖|温暖]]

This word is itself the stand-in that legitimizes the character 温 (暖's own stand-in is itself, so no #cranberry). Mandarin wēnnuǎn, Cantonese wan1 nyun5, Japanese おんだん, Korean 온난 all match constituent citations exactly. Filled blank `pos`(性詞) and `vietnamese`(ôn noãn, picking 暖's noãn over the semantically-drifted hoãn). `kwin: true` (諺文 온난 = Korean 온난). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄛㄆㄋㄚㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 港湾.

### 2026-09-03, iteration 2363 — [[words/港湾|港湾]]

This word is itself the stand-in that legitimizes the character 港 (湾's own stand-in is [[海湾]], so no #cranberry). Mandarin gǎngwān, Cantonese gong2 waan1, Japanese こうわん, Korean 항만 all match constituent citations exactly. Fixed real bug: `vietnamese` was hải cảng, contaminated from the unrelated near-synonym 海港 — corrected to compositional cảng loan (港's cảng + 湾's loan). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏㄛㄫ·⺢ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 湯.

### 2026-09-03, iteration 2364 — [[words/湯|湯]]

This word is itself the stand-in that legitimizes the character 湯. Mandarin tāng, Cantonese tong1, Korean 탕, Vietnamese thang all match 湯's own citation exactly. Fixed literal `vietnamese: null` → thang, added missing `pos`; japanese ゆ is the real native word (rather than on'yomi TOU/SHOU), reformatted `characters` to block-list with "(char)" suffix (hsk_level left absent, matching 湯's own empty citation). Checked 撐 (also ㄊㄚㄫ) — its own stand-in is 名専字, so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 湯池.

### 2026-09-03, iteration 2365 — [[words/湯池|湯池]]

No stand-in relationship (both 湯's and 池's own stand-ins are themselves); survives mainly in the idiom 金城湯池. Mandarin tāngchí, Cantonese tong1 ci4 compositional. Filled blank `pos`/`japanese`(とうち)/`korean`(탕지)/`vietnamese`(thang tri), all compositional. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄊㄚㄋㄐㄨㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 湿.

### 2026-09-03, iteration 2366 — [[words/湿|湿]] (+ retroactively fixing [[words/十|十]])

This word is itself the stand-in that legitimizes the character 湿. Fixed literal `korean: "null"` → 습 and `vietnamese: null` → thấp, added missing `pos`/`japanese`(しつ)/`hsk_level`("2"), reformatted `characters` to block-list.

**Deeper bug found and fixed**: 湿's own character page had a self-inconsistent header (sǝb/습/ㄙㄜㄆ) contradicting its own Words-list entry for this word (already ㄙㄧㄆ) and the already-perfected [[湿度]] — corrected to sib/십/ㄙㄧㄆ (`kwin` → false). This revealed a genuine homophone with [[十]] ("ten") invisible until the fix — added reciprocal callouts to both, retroactively restamping 十. Also corrected [[除湿]]'s ruby annotation on 湿's own page (that word still awaits its own turn). Both 湿 and 十 stamped `date-last-perfect: 2026-09-03`.

Next: 満.

### 2026-09-03, iteration 2367 — [[words/満|満]]

This word is itself the stand-in that legitimizes the character 満. Mandarin mǎn, Cantonese mun5, Korean 만, Vietnamese mãn all match 満's own citation exactly. Filled blank `vietnamese`, added missing `pos`/`japanese`(まん)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. Checked 慢/娩/漫/曼/蛮/蔓/饅/𥈞 (also ㄇㄚㄋ) — no currently-valid homophone (𥈞's own stand_in dangles on the already-deleted 欺𥈞, noted for 𥈞's future turn). Stamped `date-last-perfect: 2026-09-03`.

Next: 満族.

### 2026-09-03, iteration 2368 — [[words/満族|満族]] & [[words/満足|満足]]

**Real Dan'a'yo homophone found**: 足 and 族 share the identical Dan'a'yo reading (jog/족/ㄐㄛㄎ), making 満族 and 満足 genuine homophones in Dan'a'yo, Mandarin, and Korean (not Cantonese, zuk1 vs zuk6). Reformatted a pre-existing informal tip callout into the canonical Homophones format on both. 満族: filled blank `japanese`/`korean`/`vietnamese`(mãn tộc); Korean 만족 also the real term for "Manchu." 満足: filled blank `vietnamese`(mãn túc). Both stamped `date-last-perfect: 2026-09-03`.

Next: 満月.

### 2026-09-03, iteration 2369 — [[words/満月|満月]]

No stand-in relationship (both 満's and 月's own stand-ins are themselves); for "full moon" use [[望月]]. Mandarin mǎnyuè, Cantonese mun5 jyut6, Japanese まんげつ, Korean 만월 all match constituent citations exactly. Filled blank `vietnamese` (mãn nguyệt, also real, as in the idiom mãn nguyệt khai hoa). Reformatted `hsk_level` to quoted string. Removed blank `swadesh`. No homophones (注音 ㄇㄚㄋ⼔ㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 満洲.

### 2026-09-03, iteration 2370 — [[words/満洲|満洲]]

No stand-in relationship (both 満's and 洲's own stand-ins are themselves). Mandarin Mǎnzhōu, Cantonese mun5 zau1, Japanese まんしゅう, Korean 만주, Vietnamese Mãn Châu all match constituent citations exactly, also the real name for Manchuria. Removed redundant `品詞`. No homophones (注音 ㄇㄚㄋㄐㄨㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 満盈.

### 2026-09-03, iteration 2371 — [[words/満盈|満盈]]

This word is itself the stand-in that legitimizes the character 盈 (満's own stand-in is itself, so no #cranberry). Mandarin mǎnyíng, Japanese まんえい, Korean 만영, Vietnamese mãn doanh all match constituent citations exactly. Fixed missing space in `cantonese`. Added missing `kwin: false` and `hsk_level`("4"). No homophones (注音 ㄇㄚㄋ⼶ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 準線.

### 2026-09-03, iteration 2372 — [[words/準線|準線]]

No stand-in relationship (準's own stand-in is [[標準]]; 線's own is [[直線]]). Filled all blank real-language fields, compositional: mandarin zhǔnxiàn, cantonese zeon2 sin3, japanese じゅんせん, korean 준선, vietnamese chuẩn tuyến. No homophones (注音 ㄐㄨㄋㄙ⼶ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 溝.

### 2026-09-03, iteration 2373 — [[words/溝|溝]], [[words/苟|苟]] & [[words/鉤|鉤]]

**Real homophone found**: a genuine three-way group (ㄍㄛㄨ/곳/gou), all three their own stand-ins, none previously cross-referenced — completed together with reciprocal callouts. 溝: added missing `pos`/`japanese`(こう)/`hsk_level`("3"). 苟: fixed literal `vietnamese: null` → cẩu, added missing `japanese`(こう)/`hsk_level`("6"). 鉤: fixed literal `vietnamese: null` → câu, added missing `japanese`(こう)/`hsk_level`("6"). All reformatted `characters` to block-list with "(char)" suffix. Checked remaining ㄍㄛㄨ characters (勾/垢/狗/構/購) — none has a self-pointing stand-in, confirming no fourth homophone. All three stamped `date-last-perfect: 2026-09-03`.

Next: 溝涜.

### 2026-09-03, iteration 2374 — [[words/溝涜|溝涜]]

This word is itself the stand-in that legitimizes the character 涜 (溝's own stand-in is itself, so no #cranberry). Mandarin gōudú, Japanese こうとく compositional. Filled blank `cantonese`(kau1 duk6)/`korean`(구독, coincidental collision with unrelated 購読 "subscription")/`vietnamese`(câu đậu), added `hsk_level`(無)/`kwin: false`. Removed redundant `品詞`. No homophones (注音 ㄍㄛㄨㄉㄛㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 溝股.

### 2026-09-03, iteration 2375 — [[words/溝股|溝股]]

No stand-in relationship (both 溝's and 股's own stand-ins are themselves); 溝 stands for classical 勾股 (溝/勾 already genuine Dan'a'yo homophones). Mandarin gōugǔ, Cantonese kau1 gu2, Japanese こうこ compositional. Filled blank `korean`(구고, classical term)/`vietnamese`(câu cổ, also the real classical Vietnamese math term). No homophones (注音 ㄍㄛㄨㄍㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 溶化.

### 2026-09-03, iteration 2376 — [[words/溶化|溶化]]

This word is itself the stand-in that legitimizes the character 溶 (化's own stand-in is itself, so no #cranberry). Mandarin rónghuà, Cantonese jung4 faa3, Japanese ようか compositional. Fixed real bug: `korean` was 용해하다 (conjugated form of unrelated near-synonym 溶解) — corrected to compositional 용화. Filled blank `vietnamese` (dung hoá). Reformatted `hsk_level` to quoted string. Removed empty `aliases: []`. No homophones (注音 ⼄ㄫㄏ⺢ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 溶岩.

### 2026-09-03, iteration 2377 — [[words/溶岩|溶岩]]

No stand-in relationship (溶's own stand-in is [[溶化]]; 岩's own is [[岩石]]). Mandarin róngyán, Cantonese jung4 ngaam4, Japanese ようがん, Korean 용암, Vietnamese dung nham all match constituent citations exactly, also the real everyday words for "lava." `kwin: true` (諺文 용암 = Korean 용암). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ⼄ㄫㄚㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 溶液.

### 2026-09-03, iteration 2378 — [[words/溶液|溶液]]

No stand-in relationship (溶's own stand-in is [[溶化]]; 液's own is [[液体]]). Mandarin róngyè, Cantonese jung4 jik6, Japanese ようえき, Korean 용액, Vietnamese dung dịch all match constituent citations exactly. Fixed doubled/malformed `mandarin` (róngyè, róngyì → róngyè; róngyì belongs to homophone [[容易]]). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. Homophone with [[容易]] already fully cross-referenced. Stamped `date-last-perfect: 2026-09-03`.

Next: 溶融.

### 2026-09-03, iteration 2379 — [[words/溶融|溶融]]

No stand-in relationship (溶's own stand-in is [[溶化]]; 融's own is itself). Mandarin róngróng, Cantonese jung4 jung4 (fixed missing space), Japanese ようゆう compositional — 溶/融 are genuine near-total homophones across the sphere. Filled blank `korean`(용융)/`vietnamese`(dung dung, both citations converge). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ⼄ㄫ⼜ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 溺.

### 2026-09-03, iteration 2380 — [[words/溺|溺]]

This word is itself the stand-in that legitimizes the character 溺. Mandarin nì, Cantonese nik6, Korean 닉, Vietnamese nịch all match 溺's own citation exactly. Fixed literal `vietnamese: null` → nịch, added missing `pos`/`japanese`(でき)/`hsk_level`(無), reformatted `characters` to block-list with "(char)" suffix. Checked 匿 (also ㄋㄧㄎ) — its own stand-in is [[隠匿]], so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 滅.

### 2026-09-03, iteration 2381 — [[words/滅|滅]] & [[words/蔑|蔑]]

**Real homophone found**: both words are their own stand-ins (legitimizing 滅 and 蔑 respectively), sharing 注音/諺文/羅馬字 ㄇㄝㄊ/먿/med. Completed both together with reciprocal callouts. 滅: fixed literal `vietnamese: null` → diệt, added missing `pos`/`japanese`(めつ)/`hsk_level`("2"). 蔑: added missing `japanese`(べつ). Both reformatted `characters` to block-list with "(char)" suffix. Checked 襪 (also ㄇㄝㄊ) — its own stand-in is 名専字, so no third homophone. Both stamped `date-last-perfect: 2026-09-03`.

Next: 滅失.

### 2026-09-03, iteration 2382 — [[words/滅失|滅失]]

This word is itself the stand-in that legitimizes the character 失 (滅's own stand-in is itself, so no #cranberry). Mandarin mièshī, Cantonese mit6 sat1, Japanese めっしつ, Korean 멸실 all match constituent citations exactly. Filled blank `vietnamese` (diệt thất, compositional). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄝㄊㄙㄧㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 滋生.

### 2026-09-03, iteration 2383 — [[words/滋生|滋生]]

This word is itself the stand-in that legitimizes the character 滋 (生's own stand-in is [[生活]], so no #cranberry). Mandarin zīshēng, Cantonese zi1 sang1 compositional. Filled blank `japanese`(じせい)/`korean`(자생, also real word for "growing wild")/`vietnamese`(tư sinh). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄐㄜㄙㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 滑鼠.

### 2026-09-03, iteration 2384 — [[words/滑鼠|滑鼠]]

No stand-in relationship (滑's own stand-in is itself; 鼠's own is [[熊鼠]]). Mandarin huáshǔ, Cantonese waat6 syu2 compositional. Japanese マウス, Korean 마우스, Vietnamese chuột máy tính (native "computer rat" calque) are the real everyday words for "computer mouse." No homophones (注音 ㄏ⺢ㄊㄙ⼄ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 滴.

### 2026-09-03, iteration 2385 — [[words/滴|滴]]

This word is itself the stand-in that legitimizes the character 滴. Mandarin dī, Cantonese dik6, Korean 적, Vietnamese tích all match 滴's own citation exactly. Fixed literal `vietnamese: null` → tích, added missing `pos`/`japanese`(てき)/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix. Checked 的/敵/翟/笛/迪 (also ㄉㄝㄎ) — none has a self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 漂.

### 2026-09-03, iteration 2386 — [[words/漂|漂]]

This word is itself the stand-in that legitimizes the character 漂. Mandarin piào, Cantonese piu1, Korean 표, Vietnamese phiêu all match 漂's own citation exactly. Fixed literal `vietnamese: null` → phiêu, added missing `pos`/`japanese`(ひょう)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. No homophones (注音 ㄆ⼄ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 漏.

### 2026-09-03, iteration 2387 — [[words/漏|漏]]

This word is itself the stand-in that legitimizes the character 漏. Mandarin lòu, Cantonese lau6, Vietnamese lậu all match 漏's own citation exactly. Fixed real bug: `korean` was South-Korean-shifted 누 — corrected to North Korean 루. Fixed literal `vietnamese: null` → lậu, added missing `pos`/`japanese`(ろう)/`hsk_level`("2"), reformatted `characters` to block-list with "(char)" suffix. Checked 楼/翏 (also ㄌㄛㄨ) — no self-pointing stand-in, so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 演.

### 2026-09-03, iteration 2388 — [[words/演|演]], [[words/鳶|鳶]] (+ retroactively fixing [[words/鉛|鉛]])

**Deep bug found**: 演's own page was missing its `注音` field entirely, hiding a real three-way Dan'a'yo homophone with [[鉛]] ("lead") and [[鳶]] ("kite"). 鳶's own `羅馬字` also carried a typo ('yeng → 'yen) on both its word AND character pages, fixed. Added `注音: ⼶ㄋ` to 演, reformatted its `characters` field, and added full reciprocal Homophones callouts across all three pages — retroactively restamping the already-perfected 鉛. 鳶: removed empty `品詞`, filled blank `pos`/`vietnamese`(diên), added `hsk_level`(無). Confirmed via fresh grep across all three plus 兗/延/縁/這 (none self-pointing) that this is exactly a three-way group, no fourth. All three (演/鉛/鳶) stamped `date-last-perfect: 2026-09-03`.

Next: 演奏.

### 2026-09-03, iteration 2389 — [[words/演奏|演奏]]

This word is itself the stand-in that legitimizes the character 奏 (演's own stand-in is itself, so no #cranberry). Mandarin yǎnzòu, Cantonese jin2 zau3, Japanese えんそう, Korean 연주, Vietnamese diễn tấu all match constituent citations exactly, also the real everyday words for "perform music." Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ⼶ㄋㄙㄛㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 漢文.

### 2026-09-03, iteration 2390 — [[words/漢文|漢文]]

No stand-in relationship (漢's own stand-in is [[漢族]]; 文's own is [[文化]]). Mandarin Hànwén, Cantonese hon3 man4, Japanese かんぶん, Korean 한문, Vietnamese Hán văn all match constituent citations exactly, also the real everyday words. `kwin: true` (諺文 한문 = Korean 한문). Clarified the 韓文-avoidance note (that word was never created, so no collision to cross-reference). No homophones (注音 ㄏㄚㄋㄇㄨㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 漢族.

### 2026-09-03, iteration 2391 — [[words/漢族|漢族]]

This word is itself the stand-in that legitimizes the character 漢 (族's own stand-in is [[家族]], so no #cranberry). Mandarin hànzú, Cantonese hon3 zuk6, Japanese かんぞく, Korean 한족, Vietnamese Hán tộc all match constituent citations exactly, also the real name for the Han ethnicity. `kwin: true` (諺文 한족 = Korean 한족). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄚㄋㄐㄛㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 漢江.

### 2026-09-03, iteration 2392 — [[words/漢江|漢江]] & [[words/韓江|韓江]]

**Real homophone**: two different rivers (Seoul's Han river vs. Guangdong's Han river) sharing 注音/諺文/羅馬字 ㄏㄚㄋㄍㄚㄫ/한강/hangang, confirmed via fresh grep with no third match. Reformatted the pre-existing informal tip notes into canonical Homophones callouts on both. 漢江: fixed doubled/malformed `mandarin`/`cantonese`/`japanese` (each had been conflated with the alias 漢水's readings) — corrected to the 江-based compositional forms. 韓江: filled blank `vietnamese`(Sông Hàn). Both stamped `date-last-perfect: 2026-09-03`.

Next: 漢詩.

### 2026-09-03, iteration 2393 — [[words/漢詩|漢詩]]

No stand-in relationship (漢's own stand-in is [[漢族]]; 詩's own is [[詩歌]]). Mandarin hànshī, Cantonese hon3 si1, Japanese かんし, Korean 한시 all match constituent citations exactly. Filled blank `vietnamese` (Hán thi, already discussed in prose but missing from frontmatter). `kwin: true` (諺文 한시 = Korean 한시). No homophones (注音 ㄏㄚㄋㄙㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 漬.

### 2026-09-03, iteration 2394 — [[words/漬|漬]], [[words/紙|紙]] & [[words/際|際]]

**Real homophone found**: a genuine three-way group (ㄐㄝ/저/je), all three their own stand-ins, none previously cross-referenced — completed together with reciprocal callouts. 漬: fixed literal `vietnamese: null` → tí, added missing `pos`/`japanese`(し)/`hsk_level`(無). 紙: added missing `pos`/`japanese`(し)/`hsk_level`("1"); fixed malformed comma-joined `vietnamese` on 紙's own character page. 際: added missing `pos`/`japanese`(さい)/`hsk_level`("2"). All reformatted `characters` to block-list with "(char)" suffix. Checked remaining ㄐㄝ characters (枝/支/製/紫/祭/滞/肢) — none has a self-pointing stand-in, confirming no fourth homophone. All three stamped `date-last-perfect: 2026-09-03`.

Next: 漸漸.

### 2026-09-03, iteration 2395 — [[words/漸漸|漸漸]]

This word is itself the stand-in that legitimizes the character 漸 (reduplicated). Mandarin jiànjiàn, Korean 점점 compositional. Fixed malformed hybrid tone notation in `cantonese` (zim6 zim6-2 → zim6 zim2, real colloquial change-tone). Japanese ますます kept as the real word (avoiding false-friend compositional ぜんぜん). Filled blank `vietnamese` (tiệm tiệm). No homophones (注音 ㄐㄝㄇㄐㄝㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 漸近線.

### 2026-09-03, iteration 2396 — [[words/漸近線|漸近線]]

No stand-in relationship (漸's own stand-in is [[漸漸]]; 近's own is itself; 線's own is [[直線]]). Fixed stray space in `mandarin`. Cantonese/Japanese/Korean all compositional and real math terms. Filled blank `vietnamese` (tiệm cận tuyến, also real term). Fixed malformed comma-joined `vietnamese` on 近's own character page. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄐㄝㄇㄍㄧㄋㄙ⼶ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 潜在.

### 2026-09-03, iteration 2397 — [[words/潜在|潜在]]

This word is itself the stand-in that legitimizes the character 潜 (在's own stand-in is itself, so no #cranberry). Fixed mandarin tone typo (qiǎnzài → qiánzài). Cantonese cim4 zoi6, Japanese せんざい, Korean 잠재 all compositional. Fixed real bug: `korean` was garbled comma-joined 잠재, 잔재 (mixing with unrelated 殘滓) — corrected to 잠재. Filled blank `vietnamese` (tiềm tại, also real term). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄐㄝㄇㄐㄚㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 潜水艦.

### 2026-09-03, iteration 2398 — [[words/潜水艦|潜水艦]]

No stand-in relationship (潜's own stand-in is [[潜在]]; 水's/艦's own are each themselves). Japanese せんすいかん compositional. Fixed real bugs: `mandarin` doubled and contaminated with near-synonym 潜水艇's 艇-based readings — corrected to qiánshuǐjiàn (matching 艦's jiàn); `cantonese` similarly corrected to cim4 seoi2 laam6; `korean` was garbled comma-joined 잠수함,잠수정 (艦-based + 艇-based) — corrected to 잠수함. Vietnamese tàu ngầm is the real native term, kept as-is. Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄐㄝㄇㄙㄨㄏㄚㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 潤.

### 2026-09-03, iteration 2399 — [[words/潤|潤]] & [[words/閏|閏]]

**Real homophone found**: both words are their own stand-ins (legitimizing 潤 and 閏 respectively), sharing 注音/諺文/羅馬字 ㄋㄨㄋ/눈/nun. Completed both together with reciprocal callouts. 潤: fixed literal `vietnamese: null` → nhuận, added missing `pos`/`japanese`(じゅん)/`hsk_level`("3"). 閏: added missing `japanese`(じゅん)/`hsk_level`(無). Both reformatted `characters` to block-list with "(char)" suffix. Both stamped `date-last-perfect: 2026-09-03`.

Next: 潰.

### 2026-09-03, iteration 2400 — [[words/潰|潰]] (+ completing [[words/灰|灰]] out of turn)

Milestone: 2400th iteration. **Completed the three-way homophone group** (hoi/회/ㄏㄛㄧ) anticipated by the already-perfected [[回]]: 潰 added missing `japanese`(かい)/`hsk_level`("4"); 灰 (out of its own alphabetical turn, since both remaining members of the group were ready) filled blank `vietnamese`(khôi)/`pos`/`japanese`, added `hsk_level`("2"), reformatted `characters`. Confirmed via fresh grep across all three plus 悔/徊/晦/賄 (none self-pointing) that this is exactly a three-way group. Both stamped `date-last-perfect: 2026-09-03`.

Next: 潰瘍.

### 2026-09-03, iteration 2401 — [[words/潰瘍|潰瘍]]

This word is itself the stand-in that legitimizes the character 瘍 (潰's own stand-in is itself, so no #cranberry). Mandarin kuìyáng, Cantonese kui2 joeng4, Japanese かいよう, Korean 궤양 all match constituent citations exactly; vietnamese hội dương already cross-verified via hvdic. Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏㄛㄧ⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 澄清.

### 2026-09-03, iteration 2402 — [[words/澄清|澄清]]

This word is itself the stand-in that legitimizes the character 澄 (清's own stand-in is [[清潔]], so no #cranberry). Mandarin chéngqīng, Cantonese cing4 cing1, Japanese ちょうせい, Korean 징청 (using 澄's real Sino korean 징) all match constituent citations exactly. Filled blank `vietnamese` (trừng thanh, also a real term for "clarify"). No homophones (注音 ㄑㄚㄫㄑㄧㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 激励.

### 2026-09-03, iteration 2403 — [[words/激励|激励]]

This word is itself the stand-in that legitimizes the character 励 (激's own stand-in is [[刺激]], so no #cranberry). Mandarin jīlì, Cantonese gik1 lai6, Japanese げきれい, Korean 격려, Vietnamese khích lệ all match constituent citations exactly, also the real everyday words for "encourage." Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄍㄝㄎㄌㄝ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 激怒.

### 2026-09-03, iteration 2404 — [[words/激怒|激怒]]

No stand-in relationship (激's own stand-in is [[刺激]]; 怒's own is itself). Mandarin jīnù, Cantonese gik1 nou6, Japanese げきど, Korean 격노 all match constituent citations exactly. Filled blank `vietnamese` (kích nộ, also the real standard term for "enrage"). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄍㄝㄎㄋㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 激烈.

### 2026-09-03, iteration 2405 — [[words/激烈|激烈]]

This word is itself the stand-in that legitimizes the character 烈 (激's own stand-in is [[刺激]], so no #cranberry). Mandarin jīliè, Cantonese gik1 lit6, Japanese げきれつ, Korean 격렬, Vietnamese kích liệt all match constituent citations exactly, also the real everyday words for "intense, fierce." Reformatted `hsk_level` to quoted string. Removed blank `swadesh` and empty `aliases`. No homophones (注音 ㄍㄝㄎㄌㄝㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 濁音.

### 2026-09-03, iteration 2406 — [[words/濁音|濁音]]

No stand-in relationship (濁's own stand-in is [[混濁]]; 音's own is [[音楽]]). Mandarin zhuóyīn, Cantonese zuk6 jam1, Japanese だくおん, Korean 탁음, Vietnamese trọc âm all match constituent citations exactly, also the real linguistics term (counterpart to [[清音]]). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄉㄚㄎㄨㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 濃厚.

### 2026-09-03, iteration 2407 — [[words/濃厚|濃厚]]

This word is itself the stand-in that legitimizes the character 濃 (厚's own stand-in is itself, so no #cranberry). Mandarin nónghòu, Cantonese nung4 hau5, Japanese のうこう, Korean 농후 all match constituent citations exactly. Filled blank `vietnamese` (nồng hậu, an extended real sense "warm, cordial"). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄋㄛㄫㄏㄛㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 灘.

### 2026-09-03, iteration 2408 — [[words/灘|灘]] (+ completing [[words/炭|炭]] out of turn)

**Completed a three-way homophone group** (tan/탄/ㄊㄚㄋ) already anticipated by the already-perfected [[嘆]]: 灘 fixed literal `vietnamese: null` → than, added missing `pos`/`japanese`(だん)/`hsk_level`("3"); 炭 (out of its own alphabetical turn) filled blank `vietnamese`(than), added missing `pos`/`japanese`(たん)/`hsk_level`("4"). Both reformatted `characters` to block-list with "(char)" suffix. Confirmed via fresh grep — 坦/呑/彖 each have their own distinct stand-in, no fourth homophone. Both stamped `date-last-perfect: 2026-09-03`.

Next: 火山.

### 2026-09-03, iteration 2409 — [[words/火山|火山]]

No stand-in relationship (both 火's and 山's own stand-ins are themselves). Mandarin huǒshān, Cantonese fo2 saan1, Japanese かざん, Korean 화산, Vietnamese hỏa sơn all match constituent citations exactly, also the real words for "volcano." `kwin: true` (諺文 화산 = Korean 화산). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏ⺢ㄙㄚㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 火山島.

### 2026-09-03, iteration 2410 — [[words/火山島|火山島]]

No stand-in relationship (all three constituents' own stand-ins are themselves). Mandarin huǒshāndǎo, Japanese かざんとう, Korean 화산도 all match constituent citations exactly. Filled blank `cantonese`(fo2 saan1 dou2) and `vietnamese`(hỏa sơn đảo). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄏ⺢ㄙㄚㄋㄊㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 火星.

### 2026-09-03, iteration 2411 — [[words/火星|火星]]

No stand-in relationship (both 火's and 星's own stand-ins are themselves). Mandarin Huǒxīng, Cantonese fo2 sing1, Japanese かせい, Korean 화성, Vietnamese Hỏa Tinh all match constituent citations exactly, also the real name for the planet. `kwin: true` (諺文 화성 = Korean 화성). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄏ⺢ㄙㄝㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 灯.

### 2026-09-03, iteration 2412 — [[words/灯|灯]], [[words/登|登]] & [[words/等|等]]

**Real homophone found**: a genuine three-way group (ㄉㄨㄫ/둥/dung), all three their own stand-ins, none previously cross-referenced — completed together with reciprocal callouts. 灯: fixed literal `vietnamese: null` → đăng, added missing `pos`/`japanese`(とう)/`hsk_level`("1"). 登: fixed literal `vietnamese: null` → đăng, added missing `japanese`(とう)/`hsk_level`("2"). 等: filled blank `vietnamese`(đẳng), added missing `japanese`(とう)/`hsk_level`("1"). All reformatted `characters` to block-list with "(char)" suffix. Checked remaining ㄉㄨㄫ characters (仲/橙/鄧) — none has a self-pointing stand-in, confirming no fourth homophone. All three stamped `date-last-perfect: 2026-09-03`.

Next: 灯籠.

### 2026-09-03, iteration 2413 — [[words/灯籠|灯籠]]

No stand-in relationship (both 灯's and 籠's own stand-ins are themselves). Mandarin dēnglóng, Cantonese dang1 lung4, Japanese とうろう compositional. Korean 등롱 is the real historical term using the common 등 reading (vs. 灯's own idiosyncratic 정 citation). Vietnamese đèn lồng is the real native term, kept as-is. Reformatted `hsk_level` to quoted string. Removed blank `swadesh`. No homophones (注音 ㄉㄨㄫㄌㄛㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 灼熱.

### 2026-09-03, iteration 2414 — [[words/灼熱|灼熱]]

No stand-in relationship (灼's own stand-in is [[焼灼]]; 熱's own is itself). Mandarin zhuórè, Cantonese zoek3 jit6, Japanese しゃくねつ, Korean 작열 all match constituent citations exactly. Filled blank `vietnamese` (chước nhiệt, compositional). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄐㄚㄎㄋ⼶ㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 災厄.

### 2026-09-03, iteration 2415 — [[words/災厄|災厄]]

This word is itself the stand-in that legitimizes the character 厄 (災's own stand-in is [[災害]], so no #cranberry). Mandarin zāi'è, Japanese さいやく, Korean 재액 all match constituent citations exactly. Fixed doubled/malformed `cantonese` (zoi1 ak1, zoi1 aak1 → zoi1 ak1). Filled blank `vietnamese` (tai ách, also the real standard term for "calamity"). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄐㄚㄧㄜㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 災害.

### 2026-09-03, iteration 2416 — [[words/災害|災害]]

This word is itself the stand-in that legitimizes the character 災 (害's own stand-in is [[残害]], so no #cranberry). Mandarin zāihài, Cantonese zoi1 hoi6, Japanese さいがい, Korean 재해, Vietnamese tai hại all match constituent citations exactly, also the real everyday words for "disaster." `kwin: true` (諺文 재해 = Korean 재해). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄐㄚㄧㄏㄚㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 災殃.

### 2026-09-03, iteration 2417 — [[words/災殃|災殃]]

This word is itself the stand-in that legitimizes the character 殃 (災's own stand-in is [[災害]], so no #cranberry). Synonymous with [[災害]]. Mandarin zāiyāng, Korean 재앙 compositional. Fixed real bug: `cantonese` was zoi1 joeng4 instead of zoi1 joeng1, matching 殃's own citation. Japanese わざわい matches 殃's own native reading exactly, the real word for "calamity." Filled blank `vietnamese` (tai ương, also the real standard term). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄐㄚㄧ·⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 炉甘金.

### 2026-09-03, iteration 2418 — [[words/炉甘金|炉甘金]]

No stand-in relationship (炉's own stand-in is [[火炉]]; 甘's/金's own are each themselves). Mineral-based semantic derivation for cadmium (炉甘石 calamine → 炉甘金), per the same avoided-character-reading convention as [[丹金]]/[[欧金]]: `mandarin`/`cantonese` hold 镉's own reading (gé/gaak3); `korean`/`japanese`/`vietnamese` hold IUPAC loanword transcriptions. Removed redundant `品詞`. No homophones (注音 ㄌㄛㄍㄚㄇㄍㄧㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 炎帝.

### 2026-09-03, iteration 2419 — [[words/炎帝|炎帝]]

No stand-in relationship (炎's own stand-in is [[炎症]]; 帝's own is [[帝王]]). Mandarin Yándì, Cantonese jim4 dai3, Japanese えんてい, Korean 염제, Vietnamese Viêm Đế all match constituent citations exactly, also the real name for this mythological figure in each tradition. Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄝㄇㄊㄝㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 炎症.

### 2026-09-03, iteration 2420 — [[words/炎症|炎症]]

This word is itself the stand-in that legitimizes the character 炎 (症's own stand-in is [[病症]], so no #cranberry). Mandarin yánzhèng, Cantonese jim4 zing3, Japanese えんしょう, Korean 염증 all match constituent citations exactly, also the real medical term for "inflammation." Filled blank `pos`(名詞) and `vietnamese`(viêm chứng, compositional). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄝㄇㄐㄧㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 炒.

### 2026-09-03, iteration 2421 — [[words/炒|炒]], [[words/鍬|鍬]] (+ retroactively fixing [[words/草|草]])

**Real homophone found**: a genuine three-way group (ㄑㄚㄨ/찻/cau) — 炒 and 鍬 are both their own stand-ins; 草 was already perfected but never cross-referenced. Completed all three together with reciprocal callouts, retroactively restamping 草. 炒: added missing `pos`/`japanese`(そう)/`hsk_level`("3"). 鍬: added missing `japanese`(しゅう)/`hsk_level`("4"). Checked remaining ㄑㄚㄨ characters (嘲/抄/操/潮/造) — none has a self-pointing stand-in, confirming no fourth homophone. All three stamped `date-last-perfect: 2026-09-03`.

Next: 炸薬.

### 2026-09-03, iteration 2422 — [[words/炸薬|炸薬]] & [[words/雀躍|雀躍]]

**Real homophone**: 炸薬/雀躍 share 注音/諺文/羅馬字 ㄐㄚㄎ·⼘ㄎ/작약/jag'yag. Reformatted the pre-existing informal tip notes into canonical Homophones callouts on both. 炸薬: filled blank `vietnamese`(tạc dược). 雀躍: filled blank `vietnamese`(tước dược). Both stamped `date-last-perfect: 2026-09-03`.

Next: 点.

### 2026-09-03, iteration 2423 — [[words/点|点]]

This word is itself the stand-in that legitimizes the character 点. Mandarin diǎn, Cantonese dim2, Korean 점, Vietnamese điểm all match 点's own citation exactly. Fixed literal `vietnamese: null` → điểm, added missing `pos`/`japanese`(てん)/`hsk_level`("1"), reformatted `characters` to block-list with "(char)" suffix. Checked 店 (also ㄉㄝㄇ) — its own stand-in is [[商店]], so no homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 為.

### 2026-09-03, iteration 2424 — [[words/為|為]]

This word is itself the stand-in that legitimizes the character 為. Mandarin wèi, Cantonese wai4, Korean 위, Vietnamese vi all match 為's own citation exactly. Filled blank `korean`/`japanese`(い)/`vietnamese`, added `hsk_level`("1"), removed redundant `品詞`. Fixed malformed comma-joined `vietnamese` on 為's own character page. Completed the reciprocal homophone callout with [[圓]] (already anticipated on 圓's own page). Stamped `date-last-perfect: 2026-09-03`.

Next: 為人.

### 2026-09-03, iteration 2425 — [[words/為人|為人]]

Uses 為 in its polyphonic "act as/become" sense (wéi), distinct from 為's own stored "namely" (wèi) citation — a character-level gap flagged for future review, not fixed. Mandarin wéirén, Cantonese wai4 jan4 compositional. Japanese ひととなり is the real native reading. Filled blank `vietnamese` (vi nhân, also the real term, as in vi nhân xử thế). Left `korean` blank (no established term; naive 위인 would collide with unrelated 偉人 "great person"). No homophones (注音 ㄨㄧㄋㄧㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 為以.

### 2026-09-03, iteration 2426 — [[words/為以|為以]]

No stand-in relationship (both 為's and 以's own stand-ins are themselves). A Dan'a'yo compound combining 為 (polyphonic "act as" sense, matching [[為人]]) + 以. Fixed real bugs: `mandarin`/`cantonese` were contaminated with unrelated real word 為了's readings — corrected to compositional wéiyǐ/wai4 ji5; `japanese`/`korean` had been full phrase templates rather than readings — corrected to いい/위이. Filled blank `vietnamese` (vi dĩ). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ⼔·ㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烈火.

### 2026-09-03, iteration 2427 — [[words/烈火|烈火]]

No stand-in relationship (烈's own stand-in is [[激烈]]; 火's own is itself). Fixed typo in `mandarin` (ièhuǒ → lièhuǒ). Cantonese lit6 fo2, Japanese れっか, Korean 열화 all match constituent citations exactly. Filled blank `vietnamese` (liệt hoả). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄌㄝㄊㄏ⺢ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏梅.

### 2026-09-03, iteration 2428 — [[words/烏梅|烏梅]]

No stand-in relationship (烏's own stand-in is [[烏鳥]]; 梅's own is [[梅花]]). Mandarin wūméi, Japanese うばい, Korean 오매 all match constituent citations exactly. Filled blank `cantonese`(wu1 mui4) and `vietnamese`(ô mai, also the real beloved Vietnamese snack name for preserved plum). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄛㄇㄛㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏賊.

### 2026-09-03, iteration 2429 — [[words/烏賊|烏賊]]

No stand-in relationship (烏's own stand-in is [[烏鳥]]; 賊's own is [[盗賊]]). Mandarin wūzéi, Cantonese wu1 caak6 compositional. Japanese いか, Korean 오징어 are the real native words for "squid," same pattern as [[龍蝦]]/[[水牛]]/[[河馬]]. Filled blank `vietnamese` (ô tặc, compositional). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄛㄐㄨㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏魯斉.

### 2026-09-03, iteration 2430 — [[words/烏魯斉|烏魯斉]]

This word is itself the stand-in that legitimizes the character 魯 (斉's own stand-in is [[一斉]], so no #cranberry). Dan'a'yo-internal fields correctly compositional from all three characters. Fixed real bug: `korean` was malformed semicolon-doubled 우루무치; 우룸치 — corrected to 우루무치. Filled blank `cantonese` to the full four-syllable real name (wu1 lou5 muk6 cai4), matching mandarin/vietnamese. Japanese ウルムチ is the real loanword. No homophones (注音 ㄛㄌㄛㄇㄐㄝㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏鳥.

### 2026-09-03, iteration 2431 — [[words/烏鳥|烏鳥]]

This word is itself the stand-in that legitimizes the character 烏 (鳥's own stand-in is itself, so no #cranberry). Fixed real bug: `mandarin` was the unrelated word cíniǎo ("female bird") — corrected to compositional wūniǎo. Cantonese wu1 niu5 already correct. Japanese からす, Korean 까마귀 are the real native words, same pattern as [[龍蝦]]/[[水牛]]/[[河馬]]. Filled blank `pos`(名詞) and `vietnamese`(ô điểu, compositional). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄛㄑㄛㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏龍.

### 2026-09-03, iteration 2432 — [[words/烏龍|烏龍]]

No stand-in relationship (烏's own stand-in is [[烏鳥]]; 龍's own is itself). Mandarin wūlóng compositional. Fixed malformed hybrid tone `cantonese` (wu1 lung4-2 → wu1 lung2, real colloquial change-tone). Japanese ウーロン is the real loanword for oolong tea. Fixed real bug: `korean` was 우룡 instead of 오룡 (matching 烏's own 오). Filled blank `vietnamese` (ô long, also the real term "trà ô long"). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄛㄌ⼄ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏龍茶.

### 2026-09-03, iteration 2433 — [[words/烏龍茶|烏龍茶]]

No stand-in relationship (烏's own stand-in is [[烏鳥]]; 龍's/茶's own are each themselves). Mandarin wūlóngchá compositional. Fixed malformed hybrid tone `cantonese` (wu1 lung4-2 caa4 → wu1 lung2 caa4). Japanese ウーロンちゃ is the real mixed-script reading. Fixed real bug: `korean` was 우룡차 instead of 오룡차. Filled blank `vietnamese` (ô long trà, also the real standard term). Removed blank `hsk_level`/`swadesh` and empty `aliases: []`. No homophones (注音 ㄛㄌ⼄ㄫㄑㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 烏龍麺.

### 2026-09-03, iteration 2434 — [[words/烏龍麺|烏龍麺]]

Literally "black dragon noodles," standard rendering of Japanese udon (native reading, matching Korean loanword). Fixed malformed hybrid tone `cantonese` (wu1 lung4-2 min6 → wu1 lung2 min6, matching [[烏龍]]/[[烏龍茶]]). Filled blank `vietnamese` (mì udon, the real Vietnamese term). No homophones (注音 ㄛㄌ⼄ㄫㄇㄝㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 焉.

### 2026-09-03, iteration 2435 — [[words/焉|焉]] & [[words/言|言]]

**Real homophone found**: both words are their own stand-ins (legitimizing 焉 and 言 respectively), sharing 注音/諺文/羅馬字 ㄝㄋ/언/en. Completed both together with reciprocal callouts. 焉: added missing `japanese`(えん)/`hsk_level`(無). 言: filled blank `vietnamese`(ngôn), added missing `pos`/`japanese`(げん)/`hsk_level`("4"). Both reformatted `characters` to block-list with "(char)" suffix. Checked remaining ㄝㄋ characters (堰/宴/彦/咽/妍/研/燕/硯/煙/諺) — none has a self-pointing stand-in, confirming no third homophone. Both stamped `date-last-perfect: 2026-09-03`.

Next: 無人.

### 2026-09-03, iteration 2436 — [[words/無人|無人]]

No stand-in relationship (both 無's and 人's own stand-ins are themselves). Mandarin wúrén, Cantonese mou4 jan4, Japanese ぶにん, Korean 무인 all match constituent citations exactly, also the real everyday words for "unmanned." Filled blank `vietnamese` (vô nhân, compositional). Removed blank `hsk_level`/`swadesh` and empty `aliases`. No homophones (注音 ㄇㄨㄋㄧㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無効.

### 2026-09-03, iteration 2437 — [[words/無効|無効]]

No stand-in relationship (無's own stand-in is itself; 効's own is [[効果]], not this compound). Mandarin wúxiào, Korean 무효, Vietnamese vô hiệu all fully compositional. Fixed a missing space in `cantonese` (mou4haau6 → mou4 haau6). Fixed a real bug in `japanese`: むかう (unrelated word "to face/head toward," 向かう) → correct compositional むこう (MU+KOU), also the real standard word. Reformatted `characters` to block-list with "(char)" suffix. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄜㄏ⼘ㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無双.

### 2026-09-03, iteration 2438 — [[words/無双|無双]]

No stand-in relationship (both 無's and 双's own stand-ins are themselves). Mandarin wúshuāng, Cantonese mou4 soeng1, Japanese むそう, Korean 무쌍, Vietnamese vô song all fully compositional. Fixed a real bug in `pos`: 連接詞 ("conjunction") → 性詞, matching sibling 無-compounds ([[無効]]/[[無常]]/[[無恥]]/[[無援]]/[[無人]]). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄇㄜㄙ⺢ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無名指.

### 2026-09-03, iteration 2439 — [[words/無名指|無名指]]

No stand-in relationship (無's/名's own stand-ins are themselves; 指's own is [[手指]]). Fixed a serious contamination bug in `cantonese` (wu2 min2 zi3, matching none of the three constituents → mou4 ming4 zi2, fully compositional). Japanese ななしゆび is the real native-reading alternate (matches alias 名無し指); real primary alternate 薬指 also listed as alias. Filled blank `vietnamese` (vô danh chỉ, Sino-Vietnamese compositional). Reformatted `characters`/`aliases` to block-lists with "(char)" suffixes. No homophones (注音 ㄇㄜㄇㄧㄫㄐㄧㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無定河.

### 2026-09-03, iteration 2440 — [[words/無定河|無定河]]

Chinese river name (Wuding River, Shaanxi); no stand-in relationship (無's own is itself; 定's is [[決定]]; 河's is [[小河]]). Unlike foreign-transliteration river pages ([[尼羅河]]), this is a genuine Han place name, so filled blank `japanese`(むていが)/`korean`(무정하)/`cantonese`(mou4 ding6 ho4) with standard Sino-readings, and blank `vietnamese` with capitalized place-name form Vô Định Hà (matching [[上海]]/[[九天]] convention). Reformatted `characters` to block-list with "(char)" suffixes. Added missing `kwin: false` (諺文 므정하 vs korean 무정하 diverge). No homophones (注音 ㄇㄜㄐㄝㄫㄏㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無家.

### 2026-09-03, iteration 2441 — [[words/無家|無家]]

No stand-in relationship (無's own is itself; 家's own is [[家庭]]). Fixed a serious bug: `mandarin`/`korean`/`japanese` had all been contaminated with the pronunciation/phrase of the longer alias 無家可歸 rather than this word's own two-syllable form. Corrected to fully compositional mandarin wújiā, cantonese mou4 gaa1 (blank filled), japanese むか, korean 무가. Filled blank `vietnamese` (vô gia). Added missing `kwin: false`. No homophones (注音 ㄇㄜㄍㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無常.

### 2026-09-03, iteration 2442 — [[words/無常|無常]]

No stand-in relationship (無's own is itself; 常's own is [[日常]]). Fixed a real character-level bug: `characters/常.md`'s own `cantonese` (seung4) used non-jyutping romanization inconsistent with every other word citing 常 ([[五常]]/[[天常]]/[[常用]]/[[恒常]]/[[常識]]/[[常時]]/[[平常]]/[[日常]]/[[異常]]/[[非常]] all soeng4) — corrected to soeng4, confirming this word's own mou4 soeng4 was already right. Filled blank `vietnamese` (vô thường, also the real Buddhist term). No homophones (注音 ㄇㄜㄙ⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無我.

### 2026-09-03, iteration 2443 — [[words/無我|無我]]

No stand-in relationship (both 無's and 我's own stand-ins are themselves). All fields already fully compositional (wúwǒ/mou4 ngo5/むが/무아/vô ngã), page was already well-developed with a substantive Notes section. Fixed a real character-level citation gap on `characters/我 (char).md`: `vietnamese` held only native pronoun equivalents (tôi/anh/tao), missing the Sino-Vietnamese reading ngã already relied on by [[我等]] — added it. Reformatted `characters` to a quoted block-list. No homophones (注音 ㄇㄜㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無援.

### 2026-09-03, iteration 2444 — [[words/無援|無援]]

No stand-in relationship (無's own is itself; 援's own is [[援手]]). Mandarin wúyuán, Cantonese mou4 wun4, Japanese むえん, Korean 무원 all fully compositional. Filled blank `vietnamese` (vô viện, viện being 援's standard Sino-Vietnamese reading). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄜㄛㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無政府.

### 2026-09-03, iteration 2445 — [[words/無政府|無政府]]

No stand-in relationship (無's own is itself; 政's own is [[政治]]; 府's own is [[政府]]). All fields already fully compositional (wúzhèngfǔ/mou4 zing3 fu2/むせいふ/무정부/vô chính phủ). Reformatted `characters` to block-list with "(char)" suffixes. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄜㄐㄧㄫㄈㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無敵.

### 2026-09-03, iteration 2446 — [[words/無敵|無敵]]

No stand-in relationship (無's own is itself; 敵's own is [[敵人]]). All fields already fully compositional (wúdí/mou4 dik6/むてき/무적/vô địch), also real standard everyday words. Reformatted `characters` to block-list with "(char)" suffix. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄜㄉㄝㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無然.

### 2026-09-03, iteration 2447 — [[words/無然|無然]]

Real word is 憮然 (alias); 憮 is a stored alias of 無, so parent form used compositionally. Following the [[為人]] alias-divergent-reading precedent, kept mandarin wǔrán (憮's own reading, not 無's wú) and filled blank `cantonese` (mou5 jin4, not mou4 — confirmed via 舞/武 same phonetic series) and blank `vietnamese` (vũ nhiên, not vô/mô — confirmed via 武's own vũ/võ). Japanese ぶぜん needed no adjustment (BU already one of 無's own on'yomi). Filled blank `korean` (무연, compositional). No stand-in relationship. No homophones (注音 ㄇㄜㄋ⼶ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無私.

### 2026-09-03, iteration 2448 — [[words/無私|無私]]

No stand-in relationship (無's own is itself; 私's own is [[私立]]). All fields already fully compositional (wúsī/mou4 si1/むし/무사/vô tư), also real standard everyday words. Reformatted `characters` to block-list with "(char)" suffix. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄜㄙㄧㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無線.

### 2026-09-03, iteration 2449 — [[words/無線|無線]]

No stand-in relationship (無's own is itself; 線's own is [[直線]]). All fields already fully compositional (wúxiàn/mou4 sin3/むせん/무선/vô tuyến), also real standard everyday words. Reformatted `characters` to block-list with "(char)" suffix. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄜㄙ⼶ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 無義.

### 2026-09-03, iteration 2450 — [[words/無義|無義]]

No stand-in relationship (無's own is itself; 義's own is [[意義]]). Mandarin wúyì, Cantonese mou4 ji6, Vietnamese vô nghĩa already correct. Filled blank `japanese`(むぎ)/`korean`(무의), both compositional. Added missing `kwin: false`. No homophones (注音 ㄇㄜㄜㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 焦思.

### 2026-09-03, iteration 2451 — [[words/焦思|焦思]]

No stand-in relationship (焦's own is itself; 思's own is [[思考]]). Mandarin jiāosī, Japanese しょうし already correct. Filled blank `cantonese`(ziu1 si1)/`korean`(초사)/`vietnamese`(tiêu tư), all compositional. Added missing `kwin: false` (諺文 좃사 vs korean 초사 diverge). No homophones (注音 ㄐㄛㄨㄙㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 焦点.

### 2026-09-03, iteration 2452 — [[words/焦点|焦点]]

No stand-in relationship (both 焦's and 点's own stand-ins are themselves). Mandarin jiāodiǎn, Cantonese ziu1 dim2, Japanese しょうてん, Korean 초점 already correct. Filled blank `vietnamese`(tiêu điểm, also the real standard term). No homophones (注音 ㄐㄛㄨㄉㄝㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 然.

### 2026-09-03, iteration 2453 — [[words/然|然]]

This word is itself the stand-in legitimizing the character 然. Fixed a literal `"null"` string in `vietnamese`(→ nhiên). Added missing `pos`(副詞)/`japanese`(ぜん)/`hsk_level`("1")/`kwin`(false), all matching 然's own citation. Checked for homophones: `characters/燃.md` shares 注音 ㄋ⼶ㄋ but its own stand-in is [[燃焼]], not itself, so no genuine word-level homophone exists. Stamped `date-last-perfect: 2026-09-03`.

Next: 焼灼.

### 2026-09-03, iteration 2454 — [[words/焼灼|焼灼]]

灼's own stand-in is this exact compound, but 焼's is [[燃焼]] — transitivity fails, no `#cranberry`, though 灼 is legitimized specifically by this word. Japanese しょうしゃく already correct. Filled blank `cantonese`(siu1 coek3)/`korean`(소작). Fixed a real character-level citation gap: `characters/焼.md`'s `vietnamese` was entirely blank despite thiêu already relied on by [[燃焼]] — added it, then filled this word's blank `vietnamese`(thiêu chước, matching [[灼熱]]). Also fixed a malformed `japanese_native` YAML list on `characters/灼.md`. No homophones (注音 ㄙ⼄ㄨㄐㄚㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 焼酎.

### 2026-09-03, iteration 2455 — [[words/焼酎|焼酎]]

酎's own stand-in is this exact compound, but 焼's is [[燃焼]] — transitivity fails, no `#cranberry`, though 酎 is legitimized specifically by this word. Mandarin shāozhòu, Japanese しょうちゅう ("shōchū"), Korean 소주 ("soju") already correct. Filled blank `cantonese`(siu1 zau6). Vietnamese "soju" reflects the common Vietnamese borrowing of the Korean name. No homophones (注音 ㄙ⼄ㄨㄐㄨㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 照耀.

### 2026-09-03, iteration 2456 — [[words/照耀|照耀]]

耀's own stand-in is this exact compound, but 照's own is itself — transitivity fails, no `#cranberry`, though 耀 is legitimized specifically by this word (page's existing Notes already documented this relationship correctly). Mandarin zhàoyào, Cantonese ziu3 jiu6, Japanese しょうよう, Korean 조요 already correct. Filled entirely missing `vietnamese`(chiếu diệu). No homophones (注音 ㄐㄛㄨ⼄ㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 照顧.

### 2026-09-03, iteration 2457 — [[words/照顧|照顧]]

顧's own stand-in is this exact compound, but 照's own is itself — transitivity fails, no `#cranberry`, though 顧 is legitimized specifically by this word. Mandarin zhàogù, Cantonese ziu3 gu3, Japanese しょうこ already correct. Filled blank `korean`(조고)/`vietnamese`(chiếu cố, also the real standard term). No homophones (注音 ㄐㄛㄨㄍㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 煩.

### 2026-09-03, iteration 2458 — [[words/煩|煩]]

This word is itself the stand-in legitimizing the character 煩. Fixed a literal `"null"` string in `vietnamese`(→ phiền). Added missing `pos`(性詞)/`japanese`(はん)/`hsk_level`("1")/`kwin`(false), all matching 煩's own citation. Checked for homophones: `characters/䒦.md` shares 注音 ㄈㄛㄇ but its own stand-in is [[名専字]], not itself, so no genuine word-level homophone exists. Stamped `date-last-perfect: 2026-09-03`.

Next: 煮沸.

### 2026-09-03, iteration 2459 — [[words/煮沸|煮沸]]

**Cranberry confirmed**: both 煮's and 沸's own `stand_in` point back to this exact compound (transitivity holds) — added `#cranberry`. Mandarin zhǔfèi, Cantonese zyu2 fai3, Japanese しゃふつ, Korean 자비 already correct. Filled blank `vietnamese`(chử phí). Fixed a real character-level bug: `characters/煮.md`'s `pos` held an empty string → corrected to 事詞. No homophones (注音 ㄐㄛㄆㄨㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 熊.

### 2026-09-03, iteration 2460 — [[words/熊|熊]] & [[words/雄|雄]]

**Real homophone found**: both words are their own stand-ins, sharing 注音/諺文/羅馬字 ㄨㄫ/웅/'ung — a genuine pan-Sinitic homophone (mandarin xióng, cantonese hung4, korean 웅, vietnamese hùng all coincide exactly between the two characters, not just a Dan'a'yo-level collision). Completed both together with reciprocal callouts. 熊: added missing `japanese`(ゆう)/`pos`(名詞)/`kwin`(true), filled blank `vietnamese`(hùng). 雄: same fixes with `pos`(性詞). Both stamped `date-last-perfect: 2026-09-03`.

Next: 熊猫.

### 2026-09-03, iteration 2461 — [[words/熊猫|熊猫]]

No stand-in relationship (both 熊's and 猫's own stand-ins are themselves). Mandarin xióngmāo, Cantonese hung4 maau1, Korean 참대곰 already correct. Fixed a real bug: `vietnamese` held the literal Mandarin pinyin "xióngmāo" → corrected to gấu trúc, the real Vietnamese term. Fixed `japanese`: くまねこ (non-standard) → パンダ, the real standard loanword (cf. [[河馬]]/[[海豚]] convention). Added missing `pos`(名詞). No homophones (注音 ㄨㄫㄇ⼘ㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 熊鼠.

### 2026-09-03, iteration 2462 — [[words/熊鼠|熊鼠]]

鼠's own stand-in is this exact compound, but 熊's own is itself — transitivity fails, no `#cranberry`, though 鼠 is legitimized specifically by this word. Fixed a serious contamination bug: `mandarin`/`cantonese`/`korean` had all been substituted with unrelated word [[老鼠]]'s readings → corrected to xióngshǔ/hung4 syu2/웅서. Removed wrong alias 老鼠 and redundant self-alias. Japanese くまねずみ (real species name) already correct. Filled `vietnamese`(chuột đen, real species name). No homophones (注音 ㄨㄫㄙ⼄ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 熟知.

### 2026-09-03, iteration 2463 — [[words/熟知|熟知]]

No stand-in relationship (熟's own is [[成熟]]; 知's own is itself). Cantonese suk6 zi1, Japanese じゅくち already correct. Fixed `mandarin`: comma-joined dual pronunciation ("shúzhī, shóuzhī") → single compositional shúzhī. Filled blank `korean`(숙지, also real standard term)/`vietnamese`(thục tri). Fixed a malformed `japanese_native` YAML list on `characters/知 (char).md`. No homophones (注音 ㄙㄨㄎㄐㄨㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 熟練.

### 2026-09-03, iteration 2464 — [[words/熟練|熟練]]

No stand-in relationship (熟's own is [[成熟]]; 練's own is [[練習]]). Cantonese suk6 lin6, Japanese じゅくれん, Korean 숙련, Vietnamese thục luyện already correct. Fixed `mandarin`: same comma-joined dual pronunciation bug as [[熟知]] ("shúliàn, shóuliàn" → shúliàn). Removed blank `hsk_level`/`swadesh`/empty `aliases`. No homophones (注音 ㄙㄨㄎㄌㄝㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 熟語.

### 2026-09-03, iteration 2465 — [[words/熟語|熟語]]

No stand-in relationship (熟's own is [[成熟]]; 語's own is [[言語]]). Cantonese suk6 jyu5, Japanese じゅくご, Korean 숙어 already correct. Fixed `mandarin`: same comma-joined dual-pronunciation bug as [[熟知]]/[[熟練]] ("shúyǔ, shóuyǔ" → shúyǔ). Filled blank `vietnamese`(thục ngữ). Confirmed the middle-dot 注音 (ㄙㄨㄎ·⼄) is correct convention, not a bug. No homophones. Stamped `date-last-perfect: 2026-09-03`.

Next: 熱.

### 2026-09-03, iteration 2466 — [[words/熱|熱]]

This word is itself the stand-in legitimizing the character 熱. Filled blank `vietnamese`(nhiệt). Added missing `pos`(性詞)/`japanese`(ねつ)/`hsk_level`("1"), all matching 熱's own citation. Checked [[熱情]]/[[熱帯]]/[[熱烈]] (share ㄋ⼶ㄊ- prefix as longer compounds) — no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 熱烈.

### 2026-09-03, iteration 2467 — [[words/熱烈|熱烈]]

No stand-in relationship (熱's own is itself; 烈's own is [[激烈]]). All fields already fully compositional (rèliè/jit6 lit6/ねつれつ/열렬/nhiệt liệt). Fixed `hsk_level` formatting (unquoted 2 → quoted "2"). Removed blank `swadesh`. No homophones (注音 ㄋ⼶ㄊㄌㄝㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 爪.

### 2026-09-03, iteration 2468 — [[words/爪|爪]]

This word is itself the stand-in legitimizing the character 爪. Added missing `japanese`(そう), matching 爪's own citation. Fixed a real character-level bug: `characters/爪 (char).md`'s `hsk_level` held an empty string → corrected to 無 (confirmed absent from all HSK lookup lists), applied here too. No homophones (注音 ㄐ⺢ㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 爬虫.

### 2026-09-03, iteration 2469 — [[words/爬虫|爬虫]]

No stand-in relationship (爬's own is [[爬行]]; 虫's own is [[昆虫]]). Mandarin páchóng, Cantonese paa4 cung4, Japanese はちゅう, Korean 파충 already correct. Filled blank `vietnamese`(bò sát, real biological term, coincidentally uses 爬's own bò reading). Fixed a real character-level bug: `characters/虫.md`'s `pos` held an empty string → corrected to 名詞. No homophones (注音 ㄅㄚㄐㄨㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 爬行.

### 2026-09-03, iteration 2470 — [[words/爬行|爬行]]

Stand-in for [[爬]]; 行's own stand-in is itself, so `#cranberry` does not apply. Mandarin páxíng, Cantonese paa4 hang4, Korean 파행 already correct. Fixed a real bug in `japanese` (はかう → はこう, correct compositional). Fixed a contamination bug in `vietnamese`: bò sát (from unrelated [[爬虫]]) → bò hành (compositional). No homophones (注音 ㄅㄚㄏㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 父母.

### 2026-09-03, iteration 2471 — [[words/父母|父母]]

No stand-in relationship (父's own is [[父親]]; 母's own is [[母親]]). Mandarin fùmǔ, Cantonese fu6 mou5, Korean 부모 already correct. Japanese りょうしん (両親) and Vietnamese cha mẹ are real standard everyday terms rather than strict compositional (ふぼ/phụ mẫu). Fixed malformed duplicate `japanese_native` YAML entries on both `characters/父.md` and `characters/母.md`. No homophones (注音 ㄅㄨㄇㄛㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 爺爺.

### 2026-09-03, iteration 2472 — [[words/爺爺|爺爺]]

No stand-in relationship (爺's own is [[老爺]], not this reduplication). Fixed `mandarin`: comma-joined dual pronunciation ("yéye, yěyé") → single standard yéye. Fixed malformed hybrid tone `cantonese` (je4 je4-2 → je4 je2, real tone-sandhi). Filled blank `japanese`(じいじ)/`vietnamese`(ông), real colloquial terms; Korean 할아버지 (real term) already correct. Fixed `hsk_level` formatting. No homophones (注音 ⼘·⼘ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 爾.

### 2026-09-03, iteration 2473 — [[words/爾|爾]]

This word is itself the stand-in legitimizing the character 爾. Filled blank `vietnamese`(nhĩ). Added missing `pos`(代詞)/`japanese`(じ)/`hsk_level`(無), all matching 爾's own citation. Checked several ㄋㄝ-prefixed words (捻/摂/泥/年/粘/鮎) — all have codas, no exact match, no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 牆壁.

### 2026-09-03, iteration 2474 — [[words/牆壁|牆壁]]

牆's own stand-in is this exact compound, but 壁's own is itself — transitivity fails, no `#cranberry`, though 牆 is legitimized specifically by this word. Fixed a real bug: `注音` held only 壁's syllable, entirely missing 牆's — corrected to full ㄑ⺢ㄫㄅㄝㄎ. Mandarin qiángbì, Cantonese coeng4 bik1, Japanese しょうへき, Korean 장벽 already correct. Filled blank `vietnamese`(tường bích). No homophones (confirmed after 注音 fix). Stamped `date-last-perfect: 2026-09-03`.

Next: 片.

### 2026-09-03, iteration 2475 — [[words/片|片]]

This word is itself the stand-in legitimizing the character 片. Fixed a literal `"null"` string in `vietnamese`(→ phiến). Added missing `pos`(名詞)/`japanese`(へん)/`hsk_level`("1"), all matching 片's own citation. Checked [[片仮名]] (shares ㄆㄝㄋ- prefix as longer compound) — no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 片仮名.

### 2026-09-03, iteration 2476 — [[words/片仮名|片仮名]]

No stand-in relationship. 仮 used in its "borrowed" 假(jiǎ)-sense here rather than its own stored rare fǎn reading — polyphonic gap, matching [[為人]] precedent. Fixed a serious contamination bug: `cantonese` (jat6 bun2 dou1, from unrelated 日本刀 "Japanese sword") → pin3 gaa2 ming4. Removed wrong alias 日本刀, added legitimate 片假名. Japanese かたかな, Korean 가타카나 (real loanword), Vietnamese katakana (real loanword) already correct. No homophones (注音 ㄆㄝㄋㄍㄚㄇㄧㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 版図.

### 2026-09-03, iteration 2477 — [[words/版図|版図]]

No stand-in relationship (版's own is [[版本]]; 図's own is [[図表]]). All fields already fully compositional (bǎntú/baan2 tou4/はんと/판도/bản đồ). Removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄆㄚㄋㄉㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 版本.

### 2026-09-03, iteration 2478 — [[words/版本|版本]]

版's own stand-in is this exact compound, but 本's own is itself — transitivity fails, no `#cranberry`, though 版 is legitimized specifically by this word. Mandarin bǎnběn, Cantonese baan2 bun2, Japanese はんぽん, Korean 판본 already correct. Filled blank `vietnamese`(bản bản — coincidental homophony between 版's and 本's own readings, not a duplication bug, matching precedent on [[基本]]/[[本来]]/[[根本]]). No homophones (注音 ㄆㄚㄋㄅㄛㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 版権.

### 2026-09-03, iteration 2479 — [[words/版権|版権]]

No stand-in relationship (版's own is [[版本]]; 権's own is [[権利]]). All fields already fully compositional (bǎnquán/baan2 kyun4/はんけん/판권/bản quyền). Fixed a real character-level citation gap: `characters/権.md`'s `vietnamese` was entirely blank despite quyền already relied on here — added it. No homophones (注音 ㄆㄚㄋㄍ⼔ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 版画.

### 2026-09-03, iteration 2480 — [[words/版画|版画]]

No stand-in relationship (版's own is [[版本]]; 画's own is [[絵画]]). 画 carries two Sino-reading senses (literary waak6/획 vs colloquial waa2/화 "picture") — polyphonic gap, this word uses the colloquial sense. Japanese はんが already correct. Fixed malformed hybrid tone `cantonese` (baan2 waa6-2 → baan2 waa2). Filled blank `korean`(판화, colloquial sense)/`vietnamese`(bản hoạ). No homophones (注音 ㄆㄚㄋㄏ⺢ㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 牌.

### 2026-09-03, iteration 2481 — [[words/牌|牌]]

Third leg of an already-completed three-way homophone group with [[倍]]/[[唄]] (both already perfected and cross-referencing this page correctly). Added missing `japanese`(はい)/`hsk_level`("2"), matching 牌's own citation. Stamped `date-last-perfect: 2026-09-03`.

Next: 牛虻.

### 2026-09-03, iteration 2482 — [[words/牛虻|牛虻]]

Stand-in for [[虻]]; 牛's own stand-in is itself, so `#cranberry` does not apply. Mandarin niúméng, Cantonese ngau4 mong4, Japanese ぎゅうぼう, Korean 우맹 already correct. Filled entirely missing `vietnamese`(ngưu manh). No homophones (注音 ㄋ⼜ㄇㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 牡丹.

### 2026-09-03, iteration 2483 — [[words/牡丹|牡丹]]

牡's own stand-in is this exact compound, but 丹's own is [[丹砂]] — transitivity fails, no `#cranberry`, though 牡 is legitimized specifically by this word. Mandarin mǔdān, Japanese ぼたん, Vietnamese mẫu đơn already correct (all real standard words). Filled blank `cantonese`(maau5 daan1). Korean 모란 (real word with historical sound change, not compositional 모단) confirmed correct as-is. No homophones (注音 ㄇㄛㄨㄉㄚㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 牢獄.

### 2026-09-03, iteration 2484 — [[words/牢獄|牢獄]]

牢's own stand-in is this exact compound, but 獄's own is [[監獄]] — transitivity fails, no `#cranberry`, though 牢 is legitimized specifically by this word. Mandarin láoyù, Japanese ろうごく, Vietnamese lao ngục already correct. Fixed missing space in `cantonese` (lou4juk6 → lou4 juk6). Fixed a real North/South Korean bug: 뇌옥 (South Korean 두음법칙 form) → 뢰옥, matching 牢's own North Korean citation. No homophones (注音 ㄌㄚㄨ⼄ㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 牧.

### 2026-09-03, iteration 2485 — [[words/牧|牧]]

This word is itself the stand-in legitimizing the character 牧, completing the already-set-up two-way homophone group with [[目]] (previously perfected and correctly cross-referencing this page). Fixed a literal `"null"` string in `vietnamese`(→ mục). Added missing `pos`(名詞)/`japanese`(ぼく)/`hsk_level`("3"), all matching 牧's own citation. Stamped `date-last-perfect: 2026-09-03`.

Next: 牧師.

### 2026-09-03, iteration 2486 — [[words/牧師|牧師]]

No stand-in relationship (牧's own is itself; 師's own is [[教師]]). All fields already fully compositional (mùshī/muk6 si1/ぼくし/목사/mục sư). No homophones (注音 ㄇㄨㄎㄙㄧㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 牧民.

### 2026-09-03, iteration 2487 — [[words/牧民|牧民]]

No stand-in relationship (牧's own is itself; 民's own is [[人民]]). Mandarin mùmín, Cantonese muk6 man4, Japanese ぼくみん, Korean 목민 already correct. Filled blank `vietnamese`(mục dân). Fixed `hsk_level` formatting (unquoted 3 → quoted "3"). No homophones (注音 ㄇㄨㄎㄇㄧㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 物理学.

### 2026-09-03, iteration 2488 — [[words/物理学|物理学]]

No stand-in relationship (物's own is itself; 理's own is [[理由]]; 学's own is [[学習]]). Mandarin wùlǐxué, Cantonese mat6 lei5 hok6, Japanese ぶつりがく, Korean 물리학 already correct. Filled blank `vietnamese`(vật lý học, also the real standard term). No homophones (注音 ㄇㄨㄊㄌㄧㄏㄚㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 物証.

### 2026-09-03, iteration 2489 — [[words/物証|物証]]

No stand-in relationship (物's own is itself; 証's own is [[証明]]). Mandarin wùzhèng, Japanese ぶっしょう, Vietnamese vật chứng already correct. Fixed a serious contamination bug in `cantonese` (wu2 zen4, matching neither constituent → mat6 zing3). Fixed a real character-level bug: `characters/証.md`'s `korean` held 정, contradicting eight other already-perfected 証-compounds (all 증) — corrected to 증, confirming this word's own 물증 was right, and retroactively fixed the same bug on already-stamped [[証言]] (정언 → 증언), updating both its and [[井堰]]'s Notes to reflect that their shared Dan'a'yo homophone status doesn't carry over to real Korean. No homophones (注音 ㄇㄨㄊㄐㄧㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 物質.

### 2026-09-03, iteration 2490 — [[words/物質|物質]]

No stand-in relationship (物's own is itself; 質's own is [[質素]]). Cantonese mat6 zat1, Japanese ぶっしつ, Korean 물질, Vietnamese vật chất already correct. Fixed `mandarin`: same comma-joined dual-pronunciation bug as [[熟知]]/[[熟練]]/[[熟語]] ("wùzhì, wùzhí" → wùzhì). No homophones (注音 ㄇㄨㄊㄐㄧㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 特殊.

### 2026-09-03, iteration 2491 — [[words/特殊|特殊]]

殊's own stand-in is this exact compound, but 特's own is [[特別]] — transitivity fails, no `#cranberry`, though 殊 is legitimized specifically by this word. All fields already fully compositional (tèshū/dak6 syu4/とくしゅ/특수/đặc thù). Fixed `hsk_level` formatting (unquoted 2 → quoted "2"). No homophones (注音 ㄉㄜㄎㄙㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 特詞.

### 2026-09-03, iteration 2492 — [[words/特詞|特詞]]

No stand-in relationship (特's own is [[特別]]; 詞's own is [[単詞]]). Checked against the [[実詞]] precedent (which turned out to be a real term wrongly labeled a coinage) — 特詞 as a unified category genuinely has no real-world linguistics equivalent, unlike 実詞. Filled in full compositional readings anyway (tècí/dak6 ci4/とくし/특사/đặc từ) rather than leaving them as empty strings, since the characters remain readable even for a Dan'a'yo-internal coinage. Removed redundant duplicate `品詞` field. No homophones (注音 ㄉㄨㄎㄙㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 犀牛.

### 2026-09-03, iteration 2493 — [[words/犀牛|犀牛]]

Stand-in for [[犀]]; 牛's own stand-in is itself, so `#cranberry` does not apply. Fixed a real inconsistency: `japanese`/`korean` held compositional readings (さいぎゅう/서우) contradicting the page's own Notes about real non-compositional terms — corrected to サイ (real Japanese, 犀 alone) and 코뿔소 (fully native Korean compound). Removed redundant duplicate `品詞` field. No homophones (注音 ㄙㄝㄧㄋ⼜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 犠牲.

### 2026-09-03, iteration 2494 — [[words/犠牲|犠牲]]

**Cranberry confirmed**: both 犠's and 牲's own `stand_in` point back to this exact compound (already correctly tagged). Mandarin xīshēng, Cantonese hei1 sang1, Japanese ぎせい, Korean 희생 already correct. Filled blank `vietnamese`(hy sinh, real standard term). Fixed a real character-level bug: `characters/犠.md`'s `hsk_level` held an empty string → corrected to "6" (confirmed via Old HSK 6.md #365). No homophones (注音 ㄏㄨㄧㄙㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 犬吠.

### 2026-09-03, iteration 2495 — [[words/犬吠|犬吠]]

吠's own stand-in is this exact compound, but 犬's own is itself — transitivity fails, no `#cranberry`, though 吠 is legitimized specifically by this word. Fixed a real bug in `japanese` (けんばい → けんはい, correct voicing). Filled entirely missing `cantonese`(hyun2 fai6)/`korean`(견폐)/`vietnamese`(khuyển phệ). Fixed a malformed duplicate `japanese_native` YAML entry on `characters/犬 (char).md`. No homophones (注音 ㄎ⼔ㄋㄈㄝ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 犯罪.

### 2026-09-03, iteration 2496 — [[words/犯罪|犯罪]]

犯's own stand-in is this exact compound, but 罪's own is itself — transitivity fails, no `#cranberry`, though 犯 is legitimized specifically by this word. Mandarin fànzuì, Cantonese faan6 zeoi6, Japanese はんざい, Korean 범죄 already correct. Filled blank `vietnamese`(phạm tội, real standard term). Fixed `hsk_level` formatting. No homophones (注音 ㄅㄚㄇㄐㄛㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狂想曲.

### 2026-09-03, iteration 2497 — [[words/狂想曲|狂想曲]]

No stand-in relationship (狂's own is [[風狂]]; 想's own is [[思想]]; 曲's own is [[歌曲]]). Fixed a real bug in `cantonese` (kwong4, inconsistent with [[狂風]]/[[羊狂]]/[[風狂]] all using kong4 → kong4 soeng2 kuk1). Mandarin kuángxiǎngqǔ, Japanese きょうそうきょく, Korean 광상곡 already correct. Filled blank `vietnamese`(cuồng tưởng khúc, real musical term). No homophones (注音 ㄍ⺢ㄫㄙㄚㄫㄎ⼄ㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狐狸.

### 2026-09-03, iteration 2498 — [[words/狐狸|狐狸]]

狐's own stand-in is this exact compound, but 狸's own is itself — transitivity fails, no `#cranberry`, though 狐 is legitimized specifically by this word. Mandarin húli already correct. Fixed malformed hybrid tone `cantonese` (wu4 lei4-2 → wu4 lei2). Fixed `japanese` (こり → きつね, real native word matching 狐's own japanese_native); korean 여우 (real native word) already correct. Filled blank `vietnamese`(hồ ly, real folklore term). No homophones (注音 ㄏㄛㄌㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狐猿.

### 2026-09-03, iteration 2499 — [[words/狐猿|狐猿]]

No stand-in relationship (狐's own is [[狐狸]]; 猿's own is [[猿猩]]). Real word is 狐猴 (猴 an alias of 猿) — filled blank `cantonese`(wu4 hau4) using 猴's own real reading, matching `mandarin`'s existing húhóu (same alias-divergence pattern as [[無然]]/[[片仮名]]/[[版画]]). Japanese きつねざる, Korean 여우원숭이, Vietnamese vượn cáo (all real native terms) already correct. Fixed two malformed YAML entries on `characters/猿.md` (comma-joined `vietnamese` string, duplicate `japanese_native`). No homophones (注音 ㄏㄛㄛㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狗吠.

### 2026-09-03, iteration 2500 — [[words/狗吠|狗吠]]

No stand-in relationship (狗's own is [[名専字]]; 吠's own is [[犬吠]]). Synonymous with [[犬吠]]. Mandarin gǒufèi, Cantonese gau2 fai6, Japanese くはい already correct. Filled blank `korean`(구폐)/`vietnamese`(cẩu phệ). No homophones (注音 ㄍㄛㄨㄈㄝ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狗盗.

### 2026-09-03, iteration 2501 — [[words/狗盗|狗盗]]

No stand-in relationship (狗's own is [[名専字]]; 盗's own is [[窃盗]]). Japanese くとう, Korean 구도 already correct. Filled blank `mandarin`(gǒudào)/`cantonese`(gau2 dou6)/`vietnamese`(cẩu đạo, cf. idiom 鷄鳴狗盜). No homophones (注音 ㄍㄛㄨㄉㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狗肉.

### 2026-09-03, iteration 2502 — [[words/狗肉|狗肉]]

No stand-in relationship (狗's own is [[名専字]]; 肉's own is itself). All fields already fully compositional (gǒuròu/gau2 juk6/くにく/구육) except blank `vietnamese`, filled with cẩu nhục. No homophones (注音 ㄍㄛㄨㄋㄨㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狙撃.

### 2026-09-03, iteration 2503 — [[words/狙撃|狙撃]]

狙's own stand-in is this exact compound, but 撃's own is itself — transitivity fails, no `#cranberry`, though 狙 is legitimized specifically by this word. Mandarin jūjī, Cantonese zeoi1 gik1, Japanese そげき, Korean 저격 already correct. Fixed a real character-level citation gap: `characters/撃 (char).md`'s `vietnamese` was entirely blank → added kích, then filled this word's blank `vietnamese`(thư kích). Fixed `撃`'s `hsk_level` empty-string bug → 無. No homophones (注音 ㄑㄛㄍㄝㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狙鳩.

### 2026-09-03, iteration 2504 — [[words/狙鳩|狙鳩]]

No stand-in relationship (狙's own is [[狙撃]]; 鳩's own is [[鳩鳥]]). Classical form is properly 雎鳩 (雎 has no vault page); 狙 substitutes, coincidentally sharing 雎's own jū reading. Mandarin jūjiū, Cantonese zeoi1 kau1, Japanese みさご already correct. Filled entirely missing `korean`(저구)/`vietnamese`(thư cưu, the real traditional Vietnamese rendering from 詩經 translations). No homophones (注音 ㄑㄛㄎ⼜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 独力.

### 2026-09-03, iteration 2505 — [[words/独力|独力]]

独's own stand-in is this exact compound, but 力's own is itself — transitivity fails, no `#cranberry`, though 独 is legitimized specifically by this word. Mandarin dúlì, Japanese どくりょく, Korean 독력 already correct. Filled blank `cantonese`(duk6 lik6)/`vietnamese`(độc lực, real standard terms). No homophones (注音 ㄉㄛㄎㄌㄧㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 独立.

### 2026-09-03, iteration 2506 — [[words/独立|独立]]

No stand-in relationship (独's own is [[独力]]; 立's own is itself). All fields already fully compositional (dúlì/duk6 lap6/どくりつ/독립/độc lập). **Deduplicated a genuine structural bug**: a separate `words/獨立.md` file existed with nearly identical content for the same word (the only such simplified/traditional file-split found in the entire vault) — user confirmed deletion; 独立.md is canonical and already lists 獨立 as an alias. No homophones ([[独立国]] merely a longer compound; 注音 ㄉㄛㄎㄌㄧㄆ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 独立国.

### 2026-09-03, iteration 2507 — [[words/独立国|独立国]]

No stand-in relationship (独's own is [[独力]]; 立's own is itself; 国's own is [[国家]]). Mandarin dúlìguó, Japanese どくりつこく, Korean 독립국 already correct. Fixed a real bug in `cantonese` (laap6, contradicting 立's own lap6 → lap6, giving duk6 lap6 gwok3). Filled blank `vietnamese`(độc lập quốc). No homophones (注音 ㄉㄛㄎㄌㄧㄆㄍㄛㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狸.

### 2026-09-03, iteration 2508 — [[words/狸|狸]] & [[words/璃|璃]]

**Real homophone found**: both words are their own stand-ins, sharing 注音/諺文/羅馬字 ㄌㄜ/르/lǝ. Completed both together with reciprocal callouts. 狸: fixed `japanese` (り → たぬき, real standard word, unlike 璃's bound り); added missing `hsk_level`(無); fixed a real character-level bug (`characters/狸 (char).md`'s own `kwin: true` contradicted its 諺文/korean mismatch → false). 璃: added missing `japanese`(り)/`hsk_level`("2"). Both stamped `date-last-perfect: 2026-09-03`.

Next: 狼狽.

### 2026-09-03, iteration 2509 — [[words/狼狽|狼狽]]

狽's own stand-in is this exact compound, but 狼's own is itself — transitivity fails, no `#cranberry`, though 狽 is legitimized specifically by this word. Mandarin lángbèi, Cantonese long4 bui3, Japanese ろうばい, Korean 랑패 already correct. Filled blank `vietnamese`(lang bái). No homophones (注音 ㄌㄚㄫㄅㄚㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 狼金.

### 2026-09-03, iteration 2510 — [[words/狼金|狼金]]

Periodic-table neologism (tungsten). `mandarin`/`cantonese`(wū/wu1) deliberately use the real Chinese element name 钨, not compositional 狼金 — confirmed intentional per the page's own extensive etymology notes. Japanese タングステン, Korean 텅스텐 already correct real loanwords. Filled blank `vietnamese`(vonfram, per the note's own "mixed traditions" listing). Removed redundant duplicate `品詞` field. No homophones (注音 ㄌㄚㄫㄍㄧㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猛烈.

### 2026-09-03, iteration 2511 — [[words/猛烈|猛烈]]

猛's own stand-in is this exact compound, but 烈's own is [[激烈]] — transitivity fails, no `#cranberry`, though 猛 is legitimized specifically by this word. All fields already fully compositional (měngliè/maang5 lit6/もうれつ/맹렬/mãnh liệt). Added missing `hsk_level`("3"). No homophones (注音 ㄇㄚㄫㄌㄝㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猛禽.

### 2026-09-03, iteration 2512 — [[words/猛禽|猛禽]]

No stand-in relationship (猛's own is [[猛烈]]; 禽's own is [[禽鳥]]). All fields already fully compositional (měngqín/maang5 kam4/もうきん/맹금/mãnh cầm). Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇㄚㄫㄎㄧㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猩猩.

### 2026-09-03, iteration 2513 — [[words/猩猩|猩猩]]

**Cranberry confirmed**: 猩's own `stand_in` points back to this exact reduplicated compound (self-doubling trivially satisfies transitivity) — added `#cranberry`. All fields already fully compositional (xīngxīng/sing1 sing1/しょうじょう/성성/tinh tinh). Reformatted `characters` to block-list with "(char)" suffixes. No homophones (注音 ㄙㄝㄫㄙㄝㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猪悟能.

### 2026-09-03, iteration 2514 — [[words/猪悟能|猪悟能]]

"Pig Awakened to Power," Zhu Bajie's formal dharma name, already cross-referenced from [[猪八戒]]. No stand-in relationship (猪's own is [[野猪]]; 悟's own is [[覚悟]]). Fixed a capitalization bug in `羅馬字` (Jo'onung → jo'onung, matching [[孫悟空]]/[[猪八戒]] convention). All other fields already fully compositional. No homophones (注音 ㄐㄛㄛㄋㄜㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猶.

### 2026-09-03, iteration 2515 — [[words/猶|猶]]

This word is itself the stand-in legitimizing the character 猶, part of an already-completed three-way homophone group with [[幽]]/[[由]] (both already perfected and correctly cross-referencing this page). Fixed a real bug in `羅馬字` (yuo → 'yuo, restoring the glottal-initial marker per its own citation and homophone siblings). Added missing `pos`(修飾語)/`japanese`(ゆう)/`hsk_level`("3"), filled blank `vietnamese`(do). Stamped `date-last-perfect: 2026-09-03`.

Next: 猶予.

### 2026-09-03, iteration 2516 — [[words/猶予|猶予]]

No stand-in relationship (猶's own is itself; 予's own is [[予様]]). Real word is 猶豫 (豫 an alias of 予); mandarin/japanese/korean already correctly used 豫's alias-divergent readings, matching the pattern on [[無然]]/[[片仮名]]/[[版画]]/[[狐猿]]. Fixed a real bug in `cantonese` (you2 yu2, matching neither constituent → jau4 jyu6). Filled blank `vietnamese`(do dự). Added missing `pos`(事詞). No homophones (注音 ⼜ㄛ⼄ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猶太.

### 2026-09-03, iteration 2517 — [[words/猶太|猶太]]

No stand-in relationship (both 猶's and 太's own stand-ins are themselves). Mandarin Yóutài, Cantonese jau4 taai3 compositional; Japanese ユダヤ (real loanword), Korean 유태 (real alternate form) already correct. Fixed capitalization in `vietnamese` (Do thái → Do Thái, matching [[上海]]/[[九天]] convention). No homophones (注音 ⼜ㄛㄊㄚㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 猿痘.

### 2026-09-03, iteration 2518 — [[words/猿痘|猿痘]]

No stand-in relationship (猿's own is [[猿猩]]; 痘's own is [[痘痕]]). Real word is 猴痘 (猴 an alias of 猿); mandarin/cantonese already correctly used 猴's alias-divergent readings, matching [[狐猿]]. Japanese エムポックス, Korean 원숭이두창 (real medical terms) already correct. Filled blank `vietnamese`(đậu mùa khỉ, real medical term). Added missing `pos`(名詞). No homophones (注音 ㄛㄋㄉㄛㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 獄吏.

### 2026-09-03, iteration 2519 — [[words/獄吏|獄吏]]

No stand-in relationship (獄's own is [[監獄]]; 吏's own is [[官吏]]). Mandarin yùlì, Cantonese juk6 lei6, Japanese ごくり already correct. Filled blank `korean`(옥리)/`vietnamese`(ngục lại). No homophones (注音 ⼄ㄎㄌㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 獅城.

### 2026-09-03, iteration 2520 — [[words/獅城|獅城]]

No stand-in relationship (獅's own is [[獅子]]; 城's own is [[城郭]]). All fields already fully compositional (shīchéng/si1 sing4/しじょう/사성/sư thành). Added missing `kwin: false`. No homophones (注音 ㄙㄧㄜㄙㄧㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 獣群.

### 2026-09-03, iteration 2521 — [[words/獣群|獣群]]

No stand-in relationship (獣's own is [[野獣]]; 群's own is [[群衆]]). Mandarin shòuqún, Cantonese sau3 kwan4 already correct. Fixed a real contamination bug: `korean` held 군중, the real reading of 群's own stand-in compound [[群衆]] ("crowd") — corrected to compositional 수군. Japanese むれ (real term, 群's native reading alone) confirmed correct. Filled blank `vietnamese`(bầy thú, real native phrase). Added missing `pos`(名詞). No homophones (注音 ㄙ⼜ㄍㄨㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 獲得.

### 2026-09-03, iteration 2522 — [[words/獲得|獲得]]

**Cranberry confirmed** via standard transitivity rule (both 獲's and 得's own `stand_in` point back to this compound) — reframed the existing note's justification (which had cited korean_native/Japanese semantic convergence instead) to the standard mechanism, keeping the convergence detail as color. Mandarin huòdé, Cantonese wok6 dak1, Japanese かくとく, Korean 획득 already correct. Filled blank `vietnamese`(hoạch đắc, real standard term). No homophones (注音 ㄏ⺢ㄎㄊㄜㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 獵.

### 2026-09-03, iteration 2523 — [[words/獵|獵]] & [[words/鬣|鬣]]

**Real homophone found**: both words are their own stand-ins, sharing 注音/諺文/羅馬字 ㄌㄛㄆ/롭/lob. Completed both together with reciprocal callouts. 獵: removed redundant duplicate `品詞` field, added missing `hsk_level`("3"). 鬣: already well-formed. Both stamped `date-last-perfect: 2026-09-03`.

Next: 玄暈.

### 2026-09-03, iteration 2524 — [[words/玄暈|玄暈]]

暈's own stand-in is this exact compound, but 玄's own is itself — transitivity fails, no `#cranberry`, though 暈 is legitimized specifically by this word. Real word is 眩暈 (眩 has no vault page, substituted by 玄); mandarin/cantonese/korean/vietnamese all correctly use 眩's alias-divergent readings, matching the pattern on [[無然]]/[[狐猿]]/[[猿痘]]/[[猶予]]. Fixed comma-joined `mandarin` bug. Japanese めまい already correct. Filled blank `korean`(현훈)/`vietnamese`(huyễn vựng). Flagged: `characters/玄 (char).md`'s `hsk_level` is an empty string with no confirming HSK lookup entry either way — left for future dedicated character review. No homophones (注音 ㄏ⼔ㄋ·ㄨㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玄武岩.

### 2026-09-03, iteration 2525 — [[words/玄武岩|玄武岩]]

No stand-in relationship (玄's/武's own are themselves; 岩's own is [[岩石]]). Unlike [[玄暈]], genuinely uses 玄's own reading, no alias substitution. All fields already fully compositional (xuánwǔyán/jyun4 mou5 ngaam4/げんぶがん/현무암) except vietnamese bazan (real loanword, kept as-is). No homophones (注音 ㄏ⼔ㄋㄇㄨㄚㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玄米茶.

### 2026-09-03, iteration 2526 — [[words/玄米茶|玄米茶]]

No stand-in relationship (all three constituents' own stand-ins are themselves). Mandarin xuánmǐchá, Cantonese jyun4 mai5 caa4, Japanese げんまいちゃ, Korean 현미차 already correct. Filled blank `vietnamese`(trà gạo lứt, real descriptive term, following [[烏龍麺]] precedent). No homophones (注音 ㄏ⼔ㄋㄇㄝㄧㄑㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 率先.

### 2026-09-03, iteration 2527 — [[words/率先|率先]]

No stand-in relationship (率's own is [[比率]]; 先's own is [[優先]]). 率 is polyphonic: its own citation reflects the "rate" sense (lǜ/leot6/률/RITSU), but 率先 uses the "lead" sense (shuài/seot1/솔/SOTSU) — a character-level polyphonic gap, matching [[為人]]. Mandarin/Korean/Japanese already correctly used the lead-sense readings; fixed `cantonese` (leot6 → seot1). Vietnamese suất tiên already correct. Fixed a real character-level bug: `characters/先.md`'s `pos` held an empty string → corrected to 修飾語. No homophones (注音 ㄌㄨㄊㄙㄝㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 率直.

### 2026-09-03, iteration 2528 — [[words/率直|率直]]

No stand-in relationship (率's own is [[比率]]; 直's own is itself). Same 率 "lead" vs "rate" polyphonic pattern as [[率先]]: mandarin/japanese/korean already correctly used lead-sense readings; fixed `cantonese` (leot6 → seot1) to match. Vietnamese suất trực already correct. No homophones (注音 ㄌㄨㄊㄐㄧㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玉璽.

### 2026-09-03, iteration 2529 — [[words/玉璽|玉璽]]

璽's own stand-in is this exact compound, but 玉's own is itself — transitivity fails, no `#cranberry`, though 璽 is legitimized specifically by this word. All fields already fully compositional (yùxǐ/juk6 saai2/ぎょくじ/옥새/ngọc tỷ). No homophones (注音 ⼄ㄎㄙㄝ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 王冠.

### 2026-09-03, iteration 2530 — [[words/王冠|王冠]]

冠's own stand-in is this exact compound, but 王's own is itself — transitivity fails, no `#cranberry`, though 冠 is legitimized specifically by this word. Mandarin wángguān, Cantonese wong4 gun1, Japanese おうかん, Korean 왕관 already correct. Filled blank `vietnamese`(vương quan). Added missing `pos`(名詞). No homophones (注音 ⺢ㄫㄍ⺢ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 王国.

### 2026-09-03, iteration 2531 — [[words/王国|王国]]

No stand-in relationship (王's own is itself; 国's own is [[国家]]). Mandarin wángguó, Cantonese wong4 gwok3, Korean 왕국, Vietnamese vương quốc already correct. Fixed a real bug in `japanese` (わうこく → おうこく, correct compositional). Fixed `hsk_level` formatting. Added missing `pos`(名詞). No homophones (注音 ⺢ㄫㄍㄛㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 王妃.

### 2026-09-03, iteration 2532 — [[words/王妃|王妃]]

妃's own stand-in is this exact compound, but 王's own is itself — transitivity fails, no `#cranberry`, though 妃 is legitimized specifically by this word. Fixed a real bug in `諺文` (왕피 → 왕삐, matching 妃's own citation and the f→ㅃ convention seen on [[膚]]). Mandarin wángfēi, Cantonese wong4 fei1, Japanese おうひ, Korean 왕비 already correct. Filled blank `vietnamese`(vương phi). No homophones (注音 ⺢ㄫㄈㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 王子.

### 2026-09-03, iteration 2533 — [[words/王子|王子]]

No stand-in relationship (王's own is itself; 子's own is [[児子]]). Mandarin wángzǐ, Cantonese wong4 zi2, Japanese おうじ, Korean 왕자, Vietnamese vương tử already correct. Fixed a real bug in `羅馬字`/`諺文` ('wangji/왕지 → 'wangjǝ/왕즈, matching 子's own citation, already correctly reflected in `注音`). Added missing `pos`(名詞). No homophones (注音 ⺢ㄫㄐㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 王朝.

### 2026-09-03, iteration 2534 — [[words/王朝|王朝]]

No stand-in relationship (both 王's and 朝's own stand-ins are themselves). All fields already fully compositional (wángcháo/wong4 ciu4/おうちょう/왕조/vương triều). Fixed a malformed duplicate `japanese_native` YAML entry on `characters/朝 (char).md`. Removed redundant duplicate `品詞` field and blank `swadesh: ""`. No homophones (注音 ⺢ㄫㄐㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玩具.

### 2026-09-03, iteration 2535 — [[words/玩具|玩具]]

玩's own stand-in is this exact compound, but 具's own is [[工具]] — transitivity fails, no `#cranberry`, though 玩 is legitimized specifically by this word. Mandarin wánjù, Cantonese wun6 geoi6, Japanese がんぐ, Korean 완구 already correct. Filled blank `vietnamese`(ngoạn cụ). No homophones (注音 ⺢ㄋㄍㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玳瑁.

### 2026-09-03, iteration 2536 — [[words/玳瑁|玳瑁]]

**Cranberry confirmed**: both 玳's and 瑁's own `stand_in` point back to this exact compound — added `#cranberry`. All fields already fully compositional (dàimào/doi6 mou6/タイマイ/대모/đồi mồi), also real standard everyday words. No homophones (注音 ㄉㄚㄧㄇㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玻璃.

### 2026-09-03, iteration 2537 — [[words/玻璃|玻璃]]

玻's own stand-in is this exact compound, but 璃's own is itself — transitivity fails, no `#cranberry`, though 玻 is legitimized specifically by this word. Mandarin bōli, Japanese はり already correct. Fixed malformed comma-joined `cantonese` → clean bo1 lei1. Fixed `korean`: 파리 (clashes with unrelated 파리 "fly"/"Paris") → 유리, real standard word, matching 玻's own korean_native. Fixed `vietnamese`: pha ly (wrong option) → pha lê (correct real term). Flagged `characters/玻.md`'s blank joyo_level/hanmun_edu_level/boundedness for future review. No homophones (注音 ㄆㄚㄌㄝ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 玻璃版.

### 2026-09-03, iteration 2538 — [[words/玻璃版|玻璃版]]

No stand-in relationship (玻's own is [[玻璃]]; 璃's own is itself; 版's own is [[版本]]). Mandarin bōlibǎn, Japanese はりばん already correct. Fixed `cantonese`/`korean` to match the same tone-sandhi and homophone-clash fixes established on [[玻璃]] (lei4→lei1; 파리→유리). Filled blank `vietnamese`(pha lê bản). No homophones (注音 ㄆㄚㄌㄜㄆㄚㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 珈拿陀.

### 2026-09-03, iteration 2539 — [[words/珈拿陀|珈拿陀]]

Older Chinese transliteration of "Canada" (alongside modern 加拿大 alias). No stand-in relationship. Fixed a real bug in `注音`: third syllable was ㄙㄚ, not matching 陀's own citation or this word's own 諺文/羅馬字 → corrected to ㄎㄚㄋㄚㄉㄚ. Filled blank `cantonese`(gaa1 naa4 to4). Japanese カナダ, Korean 캐나다 (real loanwords) already correct. No homophones (confirmed after 注音 fix). Stamped `date-last-perfect: 2026-09-03`.

Next: 珈沙.

### 2026-09-03, iteration 2540 — [[words/珈沙|珈沙]]

Real word is 袈裟 (neither 袈 nor 裟 has a vault page; 珈/沙 substitute via matching real readings). No stand-in relationship. Mandarin jiāshā, Korean 가사 already correct. Fixed missing space in `cantonese`. Japanese けさ (real Buddhist term) already correct. Filled blank `vietnamese`(cà sa, real Buddhist term). No homophones (注音 ㄎㄚㄙㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 珍.

### 2026-09-03, iteration 2541 — [[words/珍|珍]] & [[words/鎮|鎮]]

**Real homophone found**: both words are their own stand-ins, sharing 注音/諺文/羅馬字 ㄑㄧㄋ/친/cin. Completed both together with reciprocal callouts. 珍: fixed literal `"null"` in `vietnamese`(→trân), added missing `pos`/`japanese`/`hsk_level`. 鎮: fixed literal `"null"` in `korean`(→진), added missing `pos`/`japanese`/`hsk_level`, filled blank `vietnamese`(trấn). Both stamped `date-last-perfect: 2026-09-03`.

Next: 珍珠.

### 2026-09-03, iteration 2542 — [[words/珍珠|珍珠]]

珠's own stand-in is this exact compound, but 珍's own is itself — transitivity fails, no `#cranberry`, though 珠 is legitimized specifically by this word. Mandarin zhēnzhū, Cantonese zan1 zyu1, Korean 진주, Vietnamese trân châu already correct. Japanese しんじゅ uses 真's reading (not an alias-divergence but a genuine Chinese/Japanese orthographic difference: 珍珠 vs 真珠, the latter an alias). No homophones (注音 ㄑㄧㄋㄐㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 班.

### 2026-09-03, iteration 2543 — [[words/班|班]]

This word is itself the stand-in legitimizing the character 班. Fixed a literal `"null"` string in `vietnamese`(→ban). Added missing `pos`(名詞)/`japanese`(はん)/`hsk_level`("1"), all matching 班's own citation. Checked eight ㄆㄚㄋ-reading characters (板/判/攀/潘/盼/繁/版/頒) — none has an independent word page, no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 班長.

### 2026-09-03, iteration 2544 — [[words/班長|班長]]

No stand-in relationship (both own stand-ins are themselves). 長 polyphonic ("long" vs "chief"); this word correctly uses the "chief" sense throughout (mandarin/cantonese/korean already right). Fixed a real typo in `japanese` (はんちゃう → はんちょう). Filled blank `vietnamese`(ban trưởng, using 長's chief-sense trưởng). Fixed `hsk_level` formatting. No homophones (注音 ㄆㄚㄋㄐㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 現.

### 2026-09-03, iteration 2545 — [[words/現|現]]

This word is itself the stand-in legitimizing the character 現. Fixed a literal `"null"` string in `vietnamese`(→hiện). Added missing `pos`(性詞)/`japanese`(げん)/`hsk_level`("1")/`kwin`(true), all matching 現's own citation. Checked [[現代]]/[[現在]]/[[現象]] (longer compounds sharing the prefix) — no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 現象.

### 2026-09-03, iteration 2546 — [[words/現象|現象]]

No stand-in relationship (現's own is itself; 象's own is [[大象]]). All fields already fully compositional (xiànxiàng/jin6 zoeng6/げんしょう/현상/hiện tượng). No homophones (注音 ㄏ⼶ㄋㄙ⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 球.

### 2026-09-03, iteration 2547 — [[words/球|球]] & [[words/久|久]]

**Real homophone found**: [[久]]'s own page already anticipated this exact pairing (注音/諺文/羅馬字 ㄍ⼜/규/gyu), noting it was awaiting 球's turn — completed both together with reciprocal callouts. 球: fixed literal `"null"` in `vietnamese`(→cầu), added missing `pos`/`japanese`/`hsk_level`. 久: added missing `japanese`(きゅう)/`hsk_level`("2"). Both stamped `date-last-perfect: 2026-09-03`.

Next: 球体.

### 2026-09-03, iteration 2548 — [[words/球体|球体]]

No stand-in relationship (球's own is itself; 体's own is [[体系]]). All fields already fully compositional except vietnamese quả cầu (real native term, "ball-fruit"). No homophones (注音 ㄍ⼜ㄊㄝㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 球場.

### 2026-09-03, iteration 2549 — [[words/球場|球場]]

No stand-in relationship (球's own is itself; 場's own is [[市場]]). Cantonese kau4 coeng4, Japanese きゅうじょう, Korean 구장 already correct. Fixed `mandarin`: comma-joined dual pronunciation ("qiúchǎng, qiúcháng" → qiúchǎng). Filled blank `vietnamese`(cầu trường, real term). No homophones (注音 ㄍ⼜ㄐㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 理想.

### 2026-09-03, iteration 2550 — [[words/理想|理想]]

No stand-in relationship (理's own is [[理由]]; 想's own is [[思想]]). Mandarin lǐxiǎng, Cantonese lei5 soeng2, Vietnamese lí tưởng already correct. Fixed a spelling bug in `japanese` (りさう, historical kana → りそう, modern). Fixed a real North/South Korean bug (이상 → 리상, matching 理's own North Korean citation). Added missing `kwin: true`. No homophones (注音 ㄌㄧㄙㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 理由.

### 2026-09-03, iteration 2551 — [[words/理由|理由]]

No stand-in relationship (both 理's and 由's own stand-ins are themselves). Mandarin lǐyóu, Cantonese lei5 jau4, Japanese りゆう already correct. Fixed a real North/South Korean bug (이유 → 리유, matching 理's own North Korean citation). Fixed `vietnamese`: comma-joined dual value → single canonical lí do. Added missing `kwin: true`. No homophones (注音 ㄌㄧ·⼜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 理解.

### 2026-09-03, iteration 2552 — [[words/理解|理解]]

No stand-in relationship (both 理's and 解's own stand-ins are themselves). Mandarin lǐjiě, Cantonese lei5 gaai2, Japanese りかい, Vietnamese lý giải already correct. Fixed a real North/South Korean bug (이해 → 리해, third instance in a row on 理-compounds, matching [[理想]]/[[理由]]). `kwin` remains false (諺文/korean diverge in the second syllable, unrelated to the initial fix). No homophones (注音 ㄌㄧㄍ⼘ㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 理論.

### 2026-09-03, iteration 2553 — [[words/理論|理論]]

No stand-in relationship (both 理's and 論's own stand-ins are themselves). Mandarin lǐlùn, Cantonese lei5 leon6, Japanese りろん, Vietnamese lí luận already correct. Fixed a real North/South Korean bug (이론 → 리론, fourth instance in a row on 理-compounds); fixed `kwin` to true accordingly. No homophones (注音 ㄌㄧㄌㄛㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 琢磨.

### 2026-09-03, iteration 2554 — [[words/琢磨|琢磨]]

琢's own stand-in is this exact compound, but 磨's own is itself — transitivity fails, no `#cranberry`, though 琢 is legitimized specifically by this word. Mandarin zhuómó (琢's real irregular reading here, distinct from its citation's zuó), Cantonese doek3 mo4, Japanese たくま, Korean 탁마 already correct. Filled blank `vietnamese`(trác ma). Added missing `pos`(事詞). No homophones (注音 ㄊㄚㄎㄇㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 琥珀.

### 2026-09-03, iteration 2555 — [[words/琥珀|琥珀]]

**Cranberry confirmed** via standard transitivity rule (already correctly tagged). Mandarin hǔpò, Japanese こはく, Korean 호박, Vietnamese hổ phách already correct. Fixed missing space in `cantonese` (fu2paak3 → fu2 paak3). No homophones (注音 ㄏㄛㄆㄚㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 琴.

### 2026-09-03, iteration 2556 — [[words/琴|琴]]

This word is itself the stand-in legitimizing the character 琴. Added missing `pos`(名詞)/`japanese`(きん)/`hsk_level`("3"), all matching 琴's own citation. No homophones (注音 ㄍㄨㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 琵琶.

### 2026-09-03, iteration 2557 — [[words/琵琶|琵琶]]

**Cranberry confirmed** via standard transitivity rule (already correctly tagged). All fields already fully compositional (pípá/pei4 paa4/비파/tỳ bà); japanese びわ is the real native term. No homophones (注音 ㄅㄧㄅㄚ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 琺瑯.

### 2026-09-03, iteration 2558 — [[words/琺瑯|琺瑯]]

**Cranberry confirmed**: both 琺's and 瑯's own `stand_in` point back to this exact compound — added `#cranberry` (was previously untagged despite qualifying). All other fields already fully compositional except entirely missing `vietnamese`, filled with pháp lang. No homophones (注音 ㄈㄚㄆㄌㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 瑟.

### 2026-09-03, iteration 2559 — [[words/瑟|瑟]]

This word is itself the stand-in legitimizing the character 瑟. Filled blank `vietnamese`(sắt). Added missing `pos`(名詞)/`japanese`(しつ)/`hsk_level`(無), all matching 瑟's own citation. Checked [[膝蓋]] (longer compound sharing prefix) — no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 瑠球.

### 2026-09-03, iteration 2560 — [[words/瑠球|瑠球]]

Fixed a serious contamination bug: `korean` held 난세이 제도 (transliteration of the unrelated Japanese "Nansei Islands") → corrected to 류큐, the real standard term. Removed redundant duplicate `品詞` field. Mandarin Liúqiú, Cantonese lau4 kau4, Japanese りゅうきゅう, Vietnamese Lưu Cầu already correct. No homophones (注音 ㄌ⼜ㄍ⼜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 瑠璃.

### 2026-09-03, iteration 2561 — [[words/瑠璃|瑠璃]]

瑠's own stand-in is this exact compound, but 璃's own is itself — transitivity fails, no `#cranberry`, though 瑠 is legitimized specifically by this word. Mandarin liúlí, Cantonese lau4 lei4, Japanese るり, Korean 유리 (real term, matching [[玻璃]] precedent) already correct. Filled blank `vietnamese`(lưu ly, real term). No homophones (注音 ㄌ⼜ㄌㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 環.

### 2026-09-03, iteration 2562 — [[words/環|環]]

Completes an already-set-up three-way Dan'a'yo homophone group with [[亘]]/[[喚]] (both already perfected and correctly cross-referencing this page). Filled blank `vietnamese`(hoàn). Added missing `japanese`(かん)/`hsk_level`("2"). Fixed a real character-level bug: `characters/環 (char).md`'s `pos` held an empty string → corrected to 名詞. Stamped `date-last-perfect: 2026-09-03`.

Next: 環境.

### 2026-09-03, iteration 2563 — [[words/環境|環境]]

No stand-in relationship (環's own is itself; 境's own is [[地境]]). All fields already fully compositional (huánjìng/waan4 ging2/かんきょう/환경/hoàn cảnh). No homophones (注音 ㄏ⺢ㄋㄍ⼶ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 環礁.

### 2026-09-03, iteration 2564 — [[words/環礁|環礁]]

No stand-in relationship (環's own is itself; 礁's own is [[暗礁]]). Japanese かんしょう already correct. Fixed missing space in `cantonese`. Filled blank `korean`(환초)/`vietnamese`(hoàn tiêu). No homophones (注音 ㄏ⺢ㄋㄐㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 瓶.

### 2026-09-03, iteration 2565 — [[words/瓶|瓶]]

Completes the reciprocal half of an already-set-up homophone callout with [[並]] (already perfected). Added missing `pos`(名詞)/`japanese`(へい)/`hsk_level`("2"), all matching 瓶's own citation. Fixed a real character-level bug: `characters/瓶 (char).md`'s `hanmun_edu_level` held the bare number "2" → corrected to 高等. Stamped `date-last-perfect: 2026-09-03`.

Next: 甘味.

### 2026-09-03, iteration 2566 — [[words/甘味|甘味]]

No stand-in relationship (甘's own is itself; 味's own is [[味覚]]). Mandarin gānwèi, Cantonese gam1 mei6, Korean 감미 already correct. Japanese あまみ (real native term) confirmed correct as-is. Filled blank `vietnamese`(cam vị). No homophones (注音 ㄍㄚㄇㄇㄨㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 甘藷.

### 2026-09-03, iteration 2567 — [[words/甘藷|甘藷]]

No stand-in relationship (甘's own is itself; 藷's own is [[蕃藷]]). Mandarin gānshǔ, Cantonese gam1 syu4 already correct. Fixed a spelling bug in `japanese` (かんしよ → かんしょ). Fixed `korean`: comma-joined dual value → single compositional 감저. Filled blank `vietnamese`(cam thự). No homophones (注音 ㄍㄚㄇㄙㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 甘露.

### 2026-09-03, iteration 2568 — [[words/甘露|甘露]]

No stand-in relationship (both 甘's and 露's own stand-ins are themselves). Mandarin gānlù, Japanese かんろ, Korean 감로, Vietnamese cam lộ already correct. Fixed missing space in `cantonese` (gam1lou6 → gam1 lou6). No homophones (注音 ㄍㄚㄇㄌㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 甚様.

### 2026-09-03, iteration 2569 — [[words/甚様|甚様]]

甚's own stand-in is this exact compound, but 様's own is itself — transitivity fails, no `#cranberry`. All fields already fully compositional (shènyàng/sam6 joeng4/じんよう/심양/thậm dạng). Removed redundant duplicate `品詞` field. No homophones (注音 ㄙㄧㄇ⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 甜瓜.

### 2026-09-03, iteration 2570 — [[words/甜瓜|甜瓜]]

No stand-in relationship (甜's own is [[名専字]]; 瓜's own is [[胡瓜]]). Cantonese tim4 gwaa1 already correct. Fixed a typo in `mandarin` (tiánguāl → tiánguā). Fixed `japanese`: comma-joined dual value → まくわうり alone (the precise real term, vs generic メロン). Korean 참외 (real term) already correct. Filled blank `vietnamese`(điềm qua). No homophones (注音 ㄉㄧㄇㄍ⺢ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 甜菜.

### 2026-09-03, iteration 2571 — [[words/甜菜|甜菜]]

No stand-in relationship (甜's own is [[名専字]]; 菜's own is [[野菜]]). Mandarin tiáncài, Cantonese tim4 coi3, Japanese てんさい already correct. Korean 사탕무 (real term) already correct. Filled blank `vietnamese`(củ cải đường, real term matching Korean's pattern). No homophones (注音 ㄉㄧㄇㄑㄚㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生命.

### 2026-09-03, iteration 2572 — [[words/生命|生命]]

No stand-in relationship (生's own is [[生活]]; 命's own is [[運命]]). All fields already fully compositional (shēngmìng/sang1 ming6/せいめい/생명/sinh mệnh). No homophones (注音 ㄙㄚㄫㄇ⼶ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生存.

### 2026-09-03, iteration 2573 — [[words/生存|生存]]

No stand-in relationship (生's own is [[生活]]; 存's own is [[存在]]). All fields already fully compositional (shēngcún/sang1 cyun4/せいぞん/생존/sinh tồn). No homophones (注音 ㄙㄚㄫㄐㄛㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生徒.

### 2026-09-03, iteration 2574 — [[words/生徒|生徒]]

No stand-in relationship (生's own is [[生活]]; 徒's own is [[信徒]]). Mandarin shēngtú, Japanese せいと, Korean 생도 already correct. Fixed a real typo in `cantonese` (saang1 tou4 → sang1 tou4). Filled blank `vietnamese`(sinh đồ). No homophones (注音 ㄙㄚㄫㄉㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生机.

### 2026-09-03, iteration 2575 — [[words/生机|生机]]

No stand-in relationship (生's own is [[生活]]; 机's own is [[机会]]). All fields already fully compositional except entirely missing `vietnamese`, filled with sinh cơ. No homophones (注音 ㄙㄚㄫㄍㄧㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生死.

### 2026-09-03, iteration 2576 — [[words/生死|生死]]

No stand-in relationship (生's own is [[生活]]; 死's own is [[死亡]]). Mandarin shēngsǐ, Japanese せいし, Korean 생사 already correct. Fixed the same cantonese typo bug already seen on [[生徒]] (saang1 sei2 → sang1 sei2). Filled blank `vietnamese`(sinh tử, real term). Fixed a malformed `japanese_native` YAML list on `characters/死.md`. No homophones (注音 ㄙㄚㄫㄙㄧㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生活.

### 2026-09-03, iteration 2577 — [[words/生活|生活]]

Stand-in for [[生]] (活's own stand-in is itself, so `#cranberry` does not apply — matches the page's own note). All fields already fully compositional (shēnghuó/sang1 wut6/せいかつ/생활/sinh hoạt). No homophones (注音 ㄙㄚㄫㄏ⺢ㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生物.

### 2026-09-03, iteration 2578 — [[words/生物|生物]]

No stand-in relationship (生's own is [[生活]]; 物's own is itself). Mandarin shēngwù, Cantonese sang1 mat6, Japanese せいぶつ, Vietnamese sinh vật already correct. Fixed a real bug in `korean` (생믈 → 생물). Removed a self-referential alias (生物, the word's own title). Fixed `hsk_level` formatting. No homophones (注音 ㄙㄚㄫㄇㄨㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生物学.

### 2026-09-03, iteration 2579 — [[words/生物学|生物学]]

No stand-in relationship (生's own is [[生活]]; 物's own is itself; 学's own is [[学習]]). Mandarin shēngwùxué, Japanese せいぶつがく, Korean 생물학, Vietnamese sinh vật học already correct. Fixed the recurring cantonese typo (saang1 → sang1, third instance on a 生-compound after [[生徒]]/[[生死]]). No homophones (注音 ㄙㄚㄫㄇㄨㄊㄏㄚㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 生育.

### 2026-09-03, iteration 2580 — [[words/生育|生育]]

No stand-in relationship (生's own is [[生活]]; 育's own is itself). Mandarin shēngyù, Japanese せいいく, Korean 생육, Vietnamese sinh dục already correct. Fixed `cantonese`: comma-joined dual value mixing the recurring saang1 typo with correct sang1 → sang1 juk6 alone. Fixed `hsk_level` formatting. Fixed a malformed `japanese_native` YAML list on `characters/育 (char).md`. No homophones (注音 ㄙㄚㄫ⼜ㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 産量.

### 2026-09-03, iteration 2581 — [[words/産量|産量]]

No stand-in relationship (産's own is [[生産]]; 量's own is [[数量]]). 量 polyphonic (verb loeng4 vs noun loeng6); this word correctly uses the noun sense. Mandarin chǎnliàng, Japanese さんりょう, Korean 산량, Vietnamese sản lượng already correct. Fixed `hsk_level` formatting. No homophones (注音 ㄙㄚㄋㄌ⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 用度.

### 2026-09-03, iteration 2582 — [[words/用度|用度]]

No stand-in relationship (用's own is [[使用]]; 度's own is [[程度]]). Japanese ようど already correct. Fixed stray space in `mandarin` (yòng dù → yòngdù). Filled blank `cantonese`(jung6 dou6). Fixed `korean`: comma-joined value mixing correct 용도 with a misspelled native term → 용도 alone. Filled blank `vietnamese`(dụng độ). No homophones (注音 ⼄ㄫㄉㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 田野.

### 2026-09-03, iteration 2583 — [[words/田野|田野]]

**Cranberry confirmed**: both 田's and 野's own `stand_in` point back to this exact compound — added `#cranberry` (was previously untagged). All fields already fully compositional (tiányě/tin4 je5/でんや/전야/điền dã). Fixed a malformed duplicate `japanese_native` YAML entry on `characters/田.md`. No homophones (注音 ㄉㄝㄋ⼘ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 甲.

### 2026-09-03, iteration 2584 — [[words/甲|甲]] & [[words/鉀|鉀]]

**Real homophone found**: both words are their own stand-ins, sharing 注音/諺文/羅馬字 ㄍㄚㄆ/갑/gab. Completed both together with reciprocal callouts. 甲: fixed malformed comma-joined single-string `vietnamese`/`japanese_native` on the character page; added missing `pos`/`japanese`/`hsk_level` on the word page. 鉀: fixed `pos` (名詞→固有名詞, matching [[狼金]] periodic-table convention); removed redundant duplicate `品詞`. Both stamped `date-last-perfect: 2026-09-03`.

Next: 申告.

### 2026-09-03, iteration 2585 — [[words/申告|申告]]

申's own stand-in is this exact compound, but 告's own is [[告訴]] — transitivity fails, no `#cranberry`, though 申 is legitimized specifically by this word. All fields already fully compositional except blank `vietnamese`, filled with thân cáo. No homophones (注音 ㄙㄝㄋㄍㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 申月.

### 2026-09-03, iteration 2586 — [[words/申月|申月]]

No stand-in relationship (申's own is [[申告]]; 月's own is itself). Mandarin shēnyuè, Cantonese san1 jyut6, Korean 신월 already correct. Japanese さるつき/Vietnamese tháng Thân follow the same real-name convention as [[丑月]]. Fixed a malformed comma-joined `aliases` YAML list on `characters/月 (char).md`. Removed redundant duplicate `品詞` field. No homophones (注音 ㄙㄝㄋ·⼔ㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 男優.

### 2026-09-03, iteration 2587 — [[words/男優|男優]]

No stand-in relationship (男's own is [[男人]]; 優's own is [[優秀]]). All fields already fully compositional except blank `vietnamese`, filled with nam ưu. No homophones (注音 ㄋㄚㄇㄨㄛ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 男性.

### 2026-09-03, iteration 2588 — [[words/男性|男性]]

No stand-in relationship (男's own is [[男人]]; 性's own is [[性別]]). All fields already fully compositional (nánxìng/naam4 sing3/だんせい/남성/nam tính). No homophones (注音 ㄋㄚㄇㄙㄧㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 画報.

### 2026-09-03, iteration 2589 — [[words/画報|画報]]

No stand-in relationship (画's own is [[絵画]]; 報's own is itself). Same 画 colloquial-sense pattern as [[版画]]: mandarin/japanese/korean/vietnamese already correct. Fixed malformed hybrid tone `cantonese` (waa6-2 bou3 → waa2 bou3). Fixed `hsk_level` formatting. No homophones (注音 ㄏ⺢ㄎㄅㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 畏.

### 2026-09-03, iteration 2590 — [[words/畏|畏]]

This word is itself the stand-in legitimizing the character 畏. Fixed `羅馬字` (oi → 'oi, glottal marker). Added missing `pos`(事詞)/`japanese`(い)/`hsk_level`("4")/`kwin`(true), all matching 畏's own citation. Checked [[威力]]/[[慰安]] (longer compounds sharing prefix; 威/慰 have no independent word pages) — no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 畔.

### 2026-09-03, iteration 2591 — [[words/畔|畔]], [[words/盤|盤]] & [[words/般|般]]

**Real three-way homophone found**: all three words are their own stand-ins, sharing 注音/諺文/羅馬字 ㄅㄚㄋ/반/ban — a coincidental Dan'a'yo-level collision, not a real Sinitic homophone (source characters carry distinct Mandarin tones pàn/pán/bān). Completed all three together with full reciprocal callouts. 畔: added missing `japanese`(ばん)/`hsk_level`("3"). 盤: fixed literal `"null"` in `vietnamese`(→bàn), added missing `pos`/`japanese`/`hsk_level`. 般: fixed literal `"null"` in `vietnamese`(→ban), added missing `pos`/`japanese`/`hsk_level`. All three stamped `date-last-perfect: 2026-09-03`.

Next: 留学生.

### 2026-09-03, iteration 2592 — [[words/留学生|留学生]]

No stand-in relationship (留's own is itself; 学's own is [[学習]]; 生's own is [[生活]]). Mandarin liúxuéshēng, Japanese りゅうがくせい, Vietnamese lưu học sinh already correct. Fixed the recurring cantonese saang1→sang1 typo (fifth instance on a 生-compound). Fixed a real North/South Korean bug (유학생 → 류학생, matching 留's own citation). Fixed `hsk_level` formatting. No homophones (注音 ㄌ⼜ㄏㄚㄎㄙㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 留意.

### 2026-09-03, iteration 2593 — [[words/留意|留意]]

No stand-in relationship (留's own is itself; 意's own is [[意味]]). Mandarin liúyì, Cantonese lau4 ji3, Japanese りゅうい, Korean 류의 (already correct) already correct. Filled blank `vietnamese`(lưu ý, also the real common phrase). No homophones (注音 ㄌ⼜ㄜ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 畜生.

### 2026-09-03, iteration 2594 — [[words/畜生|畜生]]

畜's own stand-in is this exact compound, but 生's own is [[生活]] — transitivity fails, no `#cranberry`, though 畜 is legitimized specifically by this word. Japanese ちくしょう, Korean 축생 already correct. Fixed three comma-joined dual values: `mandarin`(chùsheng, chùshēng→chùshēng), `cantonese`(mixed saang1 typo → cuk1 sang1), `vietnamese`(súc sinh, súc sanh→súc sinh). No homophones (注音 ㄑㄨㄎㄙㄚㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 畝.

### 2026-09-03, iteration 2595 — [[words/畝|畝]] & [[words/某|某]]

**Real homophone found**: 畝 is its own stand-in; sharing 注音/諺文/羅馬字 ㄇㄛㄨ/못/mou with the already-stamped [[某]] (missing its half of the callout). 畝: added missing `pos`/`japanese`/`hsk_level`, added new Homophones callout. 某: retroactively added the reciprocal Homophones callout (was previously missing despite being otherwise complete). Both stamped `date-last-perfect: 2026-09-03`.

Next: 略.

### 2026-09-03, iteration 2596 — [[words/略|略]]

This word is itself the stand-in legitimizing the character 略. Fixed a literal `"null"` string in `vietnamese`(→lược). Added missing `pos`(事詞)/`japanese`(りゃく)/`hsk_level`("2")/`kwin`(true), all matching 略's own citation. Checked [[掠奪]]/[[略語]] (longer compounds sharing prefix) — no genuine homophone. Stamped `date-last-perfect: 2026-09-03`.

Next: 略語.

### 2026-09-03, iteration 2597 — [[words/略語|略語]]

No stand-in relationship (略's own is itself; 語's own is [[言語]]). Mandarin lüèyǔ, Cantonese loek6 jyu5, Japanese りゃくご already correct. Fixed a real North/South Korean bug (약어 → 략어, matching 略's own citation). Filled blank `vietnamese`(lược ngữ). No homophones (注音 ㄌ⼘ㄎ⼄ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 番号.

### 2026-09-03, iteration 2598 — [[words/番号|番号]]

No stand-in relationship (番's own is itself; 号's own is [[符号]]). Fixed a real bug in `羅馬字`/`諺文`: panhau/판핫 (wrong initial) → fanhau/빤핫, matching 番's own citation and this word's own already-correct `注音`. Mandarin fānhào, Cantonese faan1 hou6, Japanese ばんごう, Korean 번호 already correct. Filled blank `vietnamese`(phiên hiệu). Fixed a duplicate entry in `characters/号.md`'s own `vietnamese` list. No homophones (注音 ㄈㄚㄋㄏㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 異体.

### 2026-09-03, iteration 2599 — [[words/異体|異体]]

No stand-in relationship (異's own is [[異常]]; 体's own is [[体系]]). All fields already fully compositional except blank `vietnamese`, filled with dị thể. No homophones (注音 ㄧㄊㄝㄧ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 異常.

### 2026-09-03, iteration 2600 — [[words/異常|異常]]

Stand-in for [[異]] (常's own stand-in is [[日常]], so `#cranberry` does not apply). Mandarin yìcháng, Cantonese ji6 soeng4, Japanese いじょう, Korean 이상 already correct. Filled blank `vietnamese`(dị thường). Added missing `pos`(性詞). No homophones (注音 ㄧㄙ⼘ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 異音.

### 2026-09-03, iteration 2601 — [[words/異音|異音]]

No stand-in relationship (異's own is [[異常]]; 音's own is [[音楽]]). Japanese いおん, Korean 이음 already correct. Fixed a serious contamination bug: `mandarin` held the full four-character technical term 同位異音 instead of this word's own yìyīn. Filled blank `cantonese`(ji6 jam1). Vietnamese tha âm vị (real linguistics term) kept as-is. Fixed two malformed YAML entries (`japanese_native`, `vietnamese`) on `characters/音.md`. No homophones (注音 ㄧㄨㄇ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 畳.

### 2026-09-03, iteration 2602 — [[words/畳|畳]]

Completes an already-set-up homophone pair with [[喋]] (already perfected). Added missing `pos`(名詞)/`japanese`(じょう)/`hsk_level`("3"), all matching 畳's own citation. Fixed a malformed comma-joined `korean_native` YAML list on `characters/畳 (char).md`. Stamped `date-last-perfect: 2026-09-03`.

Next: 疎忽.

### 2026-09-03, iteration 2603 — [[words/疎忽|疎忽]]

疎's own stand-in is this exact compound, but 忽's own is [[忽然]] — transitivity fails, no `#cranberry`. All fields already fully compositional except entirely missing `vietnamese`, filled with sơ hốt. No homophones (注音 ㄙㄜㄏㄛㄊ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 疫病.

### 2026-09-03, iteration 2604 — [[words/疫病|疫病]]

疫's own stand-in is this exact compound, but 病's own is [[疾病]] — transitivity fails, no `#cranberry`. All fields already fully compositional (yìbìng/jik6 beng6/えきびょう/역병/dịch bệnh). Fixed two malformed comma-joined YAML lists on `characters/病.md`. No homophones (注音 ⼶ㄎㄅ⼶ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 疲労.

### 2026-09-03, iteration 2605 — [[words/疲労|疲労]]

Stand-in for [[疲]] (労's own stand-in is [[労動]], so `#cranberry` does not apply). All fields already fully compositional except blank `vietnamese`, filled with bì lao. Fixed a malformed single-string `vietnamese` YAML list on `characters/労.md`. No homophones (注音 ㄆㄧㄌㄚㄨ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 疲困.

### 2026-09-03, iteration 2606 — [[words/疲困|疲困]]

困's own stand-in is this exact compound, but 疲's own is [[疲労]] — transitivity fails, no `#cranberry`, though 困 is legitimized specifically by this word. Mandarin píkùn, Korean 피곤 already correct. Fixed a real contamination bug: `japanese` held ひろう (the unrelated alias [[疲労]]'s reading) → ひこん. Filled blank `cantonese`(pei4 kwan3)/`vietnamese`(bì khốn). No homophones (注音 ㄆㄧㄎㄛㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 疾病.

### 2026-09-03, iteration 2607 — [[words/疾病|疾病]]

**Cranberry confirmed**: both 疾's and 病's own `stand_in` point back to this exact compound — added `#cranberry`. All fields already fully compositional except blank `vietnamese`, filled with tật bệnh. No homophones (注音 ㄐㄧㄊㄅ⼶ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 病人.

### 2026-09-03, iteration 2608 — [[words/病人|病人]]

No stand-in relationship (病's own is [[疾病]]; 人's own is itself). Mandarin bìngrén, Cantonese beng6 jan4, Japanese びょうにん, Korean 병인 already correct. Filled blank `vietnamese`(bệnh nhân, real common term). Fixed `hsk_level` formatting. No homophones (注音 ㄅ⼶ㄫㄋㄧㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 病毒.

### 2026-09-03, iteration 2609 — [[words/病毒|病毒]]

No stand-in relationship (病's own is [[疾病]]; 毒's own is itself). All fields already fully compositional (bìngdú/beng6 duk6/びょうどく/병독/bệnh độc). No homophones (注音 ㄅ⼶ㄫㄉㄛㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 病菌.

### 2026-09-03, iteration 2610 — [[words/病菌|病菌]]

No stand-in relationship (病's own is [[疾病]]; 菌's own is [[細菌]]). Already-set-up Dan'a'yo-only homophone with [[平均]] (both correctly cross-referenced with full explanation). Filled blank `vietnamese`(bệnh khuẩn). Reformatted `characters` to block-list with "(char)" suffixes. Stamped `date-last-perfect: 2026-09-03`.

Next: 病院.

### 2026-09-03, iteration 2611 — [[words/病院|病院]]

No stand-in relationship (病's own is [[疾病]]; 院's own is [[院落]]). 病院/びょういん/병원/bệnh viện is the real term in Japanese/Korean/Vietnamese, but Chinese uses a different real term built on 醫/医 (aliased here) — mandarin/cantonese correctly reflect that real Chinese term rather than a non-existent literal reading. Fixed malformed hybrid tone `cantonese` (ji1 jyun6-2 → ji1 jyun2). No homophones (注音 ㄅ⼶ㄫ⼔ㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 症状.

### 2026-09-03, iteration 2612 — [[words/症状|症状]]

No stand-in relationship (症's own is [[病症]]; 状's own is [[形状]]). Mandarin zhèngzhuàng, Cantonese zing3 zong6, Korean 증상, Vietnamese chứng trạng already correct. Fixed a spelling bug in `japanese` (しゃうじゃう, historical kana → しょうじょう, modern), the same class of bug already fixed on [[理想]]. Fixed `hsk_level` formatting. No homophones (注音 ㄐㄧㄫㄐ⺢ㄫ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 痕跡.

### 2026-09-03, iteration 2613 — [[words/痕跡|痕跡]]

**Cranberry confirmed** via standard transitivity rule (already correctly tagged). All fields already fully compositional except blank `vietnamese`, filled with ngân tích. No homophones (注音 ㄏㄜㄋㄐㄝㄎ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 痘痕.

### 2026-09-03, iteration 2614 — [[words/痘痕|痘痕]]

痘's own stand-in is this exact compound, but 痕's own is [[痕跡]] — transitivity fails, no `#cranberry`, though 痘 is legitimized specifically by this word. Mandarin dòuhén, Korean 두흔 already correct. Japanese あばた (real native term) confirmed correct as-is. Filled blank `cantonese`(dau6 han4)/`vietnamese`(đậu ngân). No homophones (注音 ㄉㄛㄨㄏㄜㄋ unique). Stamped `date-last-perfect: 2026-09-03`.

Next: 痩.

### 2026-09-04, iteration 2615 — [[words/痩|痩]]

Single-character stand-in word (like 嫩, 多): 痩 legitimizes its own character, `#cranberry` not applicable (not a multi-character compound). Frontmatter was malformed — `characters` was a bare string instead of a list, `pos` and `japanese` were missing entirely (both always-required fields). Fixed `characters` to list form, added `pos: 性詞` (from character page) and `japanese: そう` (on'yomi, lowercased from character's `SOU`). Fixed the tip-callout character link to include the `(char)` suffix per sibling convention. Verified homophones via exact grep on both `注音: ㄙ⼜` and `羅馬字: syu` — confirmed [[手]] "hand" and [[銹]] "rust" are the only matches; existing callout already correct and already cross-linked from both sibling pages. Wrote a substantive `## Notes` section (was empty, wrong heading level `#`) covering the 形声 etymology and the JA verb-vs-adjective divergence (痩せる vs Chinese/Cantonese stative usage). Stamped `date-last-perfect: 2026-09-04`.

Note for later: while checking homophones, found [[words/銹|銹]] itself is not yet perfect — `characters` also a bare string, missing `japanese` field, `# Notes` instead of `## Notes`, no `date-last-perfect`. Out of scope today (alphabetically far past current sweep position); leaving as a flagged gap for [[project_perfection_era_methodology]] or a future targeted pass.

Next: 痴情.

### 2026-09-04, iteration 2616 — [[words/痴情|痴情]]

痴's own stand-in is [[痴漢]], 情's own is [[感情]] — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. Removed three blank fields (`hsk_level`, `swadesh`, `aliases`). All pronunciation fields (mandarin chīqíng, cantonese ci1 cing4, japanese ちじょう, korean 치정, vietnamese si tình, 注音/羅馬字/諺文) were already correct and fully compositional — no changes needed there. Rewrote the wrong `## Etymology` heading as `## Notes` with a real opening bullet plus substantive paragraphs on meaning and the Mandarin/Cantonese (admiring, "devoted") vs. Japanese/Korean (crime-of-passion, legal register) usage split. No homophones (注音 ㄑㄧㄑㄧㄫ / 羅馬字 cicing unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 痴漢.

### 2026-09-04, iteration 2617 — [[words/痴漢|痴漢]]

痴's own stand-in is this exact compound, but 漢's own is [[漢族]] — transitivity fails, no `#cranberry`, though 痴 is legitimized specifically by this word (same shape as 痘痕/痘). Filled blank `korean`(치한)/`vietnamese`(si hán, compositional), removed blank `hsk_level`/`swadesh`/`aliases`, added missing `kwin: true` (Dan'a'yo 치한 happens to coincide exactly with Korean 치한, matching both constituent characters' own `kwin: true`), normalized `characters` list indentation. Wrote a real `## Notes` section covering the word's narrowing from generic "disreputable man" to specifically "molester/pervert" — strongest in Japanese/Korean (legal/public-safety register), retained more broadly in Mandarin/Cantonese. No homophones (注音 ㄑㄧㄏㄚㄋ / 羅馬字 cihan unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 癌症.

### 2026-09-04, iteration 2618 — [[words/癌症|癌症]]

癌's own stand-in is this exact compound, but 症's own is [[病症]] — transitivity fails, no `#cranberry`, though 癌 is legitimized specifically by this word. Fixed `korean` from a malformed draft value `"암 (증)"` to the real bare Korean word 암 (Korean doesn't use the compound, unlike Mandarin/Cantonese/Japanese — noted in Notes). Filled blank `vietnamese`(nham chứng, compositional), removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`, normalized `characters` from flow-style `[癌, 症]` to block list. No homophones (注音 ㄚㄇㄐㄧㄫ / 羅馬字 'amjing unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 癒合.

### 2026-09-04, iteration 2619 — [[words/癒合|癒合]]

癒's own stand-in is this exact compound, but 合's own is [[合]] itself — transitivity fails, no `#cranberry`, though 癒 is legitimized specifically by this word. **Found and fixed a real reading bug**: the file had `合` rendered with the syllable ㄎㄚㄆ/kab/캅 (which actually belongs to 恰/怯 per `syllables/ㄎㄚㄆ.md`) instead of 合's own correct ㄍㄛㄆ/gob/곱 (per `syllables/ㄍㄛㄆ.md` and 合 (char)'s own frontmatter) — corrected `羅馬字` 'yukab→'yugob, `諺文` 유캅→유곱, `注音` ⼜ㄎㄚㄆ→⼜ㄍㄛㄆ. Filled blank `pos`(事詞, from both constituents) and `vietnamese`(dũ hợp, compositional), removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones after correction (注音 ⼜ㄍㄛㄆ / 羅馬字 'yugob unique). Stamped `date-last-perfect: 2026-09-04`.

**Same bug found (not fixed today, out of alphabetical scope) in three sibling 合-words**: [[words/合金|合金]] (羅馬字 kabgim, should be gobgim), [[words/混合|混合]] (honkab, should be honkab→honkob... i.e. -kab→-kob), [[words/組合|組合]] (jokap, should be jokob) — all substitute 合's reading with the unrelated ㄎㄚㄆ syllable. [[words/結合|結合]] already has it correct (gedgob). Flagging for a future targeted pass; likely a copy-paste propagation from one bad source.

Next: 癖.

### 2026-09-04, iteration 2620 — [[words/癖|癖]]

Single-character stand-in word (like 嫩, 多, 痩). Frontmatter had `characters` as a bare string, `vietnamese: null`, and missing `pos`/`japanese`. Fixed `characters` to list form, added `pos: 名詞` and `japanese: へき` (on'yomi from character), replaced `null` vietnamese with `phích`, added missing `kwin: false`. Fixed tip-callout link to include `(char)` suffix. Checked homophone syllable ㄆㄝㄎ/peg — shared with character 僻, but 僻's own stand-in is [[窮僻]] (no bare 僻 word file exists), so no homophone callout needed. Wrote a substantive `## Notes` section on 癖 as a productive habit/fixation suffix and the JA/KR native-word-vs-Sino-compound-suffix split. Stamped `date-last-perfect: 2026-09-04`.

Next: 発.

### 2026-09-04, iteration 2621 — [[words/発|発]]

Single-character stand-in word (like 嫩, 多, 痩, 癖). Fixed a real bug: `kwin` was `true`, contradicting the character page's own already-perfected `kwin: false` (Dan'a'yo 빧 vs Korean 발 genuinely differ) — corrected to `false`. Fixed bare-string `characters` to list form, added missing `pos`(事詞)/`japanese`(はつ, primary on'yomi)/`korean`(발)/`vietnamese`(phát). Fixed tip-callout link to include `(char)` suffix. Checked homophone syllable ㄈㄚㄊ/fad — shared with character 髪, but no `words/髪.md` exists (not its own standalone word), so no homophone callout needed. Stamped `date-last-perfect: 2026-09-04`.

Next: 発情.

### 2026-09-04, iteration 2622 — [[words/発情|発情]]

発's own stand-in is [[発]] itself, 情's own is [[感情]] — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. All pronunciation fields were already correct and compositional (mandarin fāqíng, cantonese faat3 cing4, japanese はつじょう, korean 발정, 注音/羅馬字/諺文); `pos: 実詞` left as-is (an established, widely-used category distinct from `事詞`, not a typo — verified ~343 other files use it). Filled blank `vietnamese`(phát tình — noted in Notes as drifting toward the interpersonal "falling for someone" sense rather than the zoological "estrus" sense the other four languages share), removed blank `hsk_level`/`swadesh`. Wrote a real `## Notes` section. No homophones (注音 ㄈㄚㄊㄑㄧㄫ / 羅馬字 fadcing unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 発明.

### 2026-09-04, iteration 2623 — [[words/発明|発明]]

発's own stand-in is [[発]] itself, 明's own is [[明]] itself — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. All pronunciation fields already correct and compositional (mandarin fāmíng, cantonese faat3 ming4, japanese はつめい, korean 발명, 注音/羅馬字/諺文); `hsk_level: "2"` already properly formatted, left as-is. Filled blank `vietnamese`(phát minh — the actual standard Vietnamese word for "invention," not just a compositional guess), added `aliases`(發明/发明) matching the established convention on sibling 発-compounds (発展/発見/発生/発電 all carry traditional+simplified aliases), removed blank `swadesh`. No homophones (注音 ㄈㄚㄊㄇ⼶ㄫ / 羅馬字 fadmyeng unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 発熱.

### 2026-09-04, iteration 2624 — [[words/発熱|発熱]]

発's own stand-in is [[発]] itself, 熱's own is [[熱]] itself — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. Fixed a self-referential `aliases` typo (list included the word's own name "発熱" instead of the intended traditional form) — corrected to proper traditional/simplified pair 發熱/发热, kept the pre-existing colloquial-synonym pair 發燒/发烧 (Mandarin's more common everyday "have a fever," following the same precedent already set on 熱 (char)'s own perfected `aliases`). Filled blank `vietnamese`(phát nhiệt, real attested term), removed blank `swadesh`; `hsk_level: "4"` already correctly formatted, left as-is. No homophones (注音 ㄈㄚㄊㄋ⼶ㄊ / 羅馬字 fadnyed unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 発財.

### 2026-09-04, iteration 2625 — [[words/発財|発財]]

発's own stand-in is [[発]] itself, 財's own is [[財産]] — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. **Found and fixed a real reading bug**: `羅馬字`/`諺文` used 財's syllable as "cai"/"채" instead of 財's actual reading "jai"/"재" (confirmed via `syllables/ㄐㄚㄧ.md` and 財's own frontmatter) — corrected fadcai→fadjai, 빧채→빧재; `注音` (ㄈㄚㄊㄐㄚㄧ) was already right, so this was purely a romanization/hangul-transcription slip, not a syllable-identity confusion like the 合/ㄎㄚㄆ bug. Also fixed `korean` from the semantic-substitution "부자" ("rich person," written with unrelated hanja 富者) to the real compositional Sino-Korean 발재. Filled blank `japanese`(はつざい, compositional — noted in Notes that JA/KR lack the Lunar New Year greeting tradition that keeps this word living in Mandarin/Cantonese/Vietnamese), added missing simplified alias 发财 alongside existing 發財, removed blank `swadesh`. No homophones (注音 ㄈㄚㄊㄐㄚㄧ / 羅馬字 fadjai unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 発電.

### 2026-09-04, iteration 2626 — [[words/発電|発電]]

発's own stand-in is [[発]] itself, 電's own is [[電気]] — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. All pronunciation/alias fields already correct (mandarin fādiàn, cantonese faat3 din6, japanese はつでん, korean 발전, 注音/羅馬字/諺文, aliases 发电/發電). Filled blank `vietnamese`(phát điện, real attested term), removed blank `swadesh`; `hsk_level: "3"` left as-is. Notes section flags a genuine Korean homophony worth documenting: 발전 is ambiguous between 發電 (this word) and 發展 ("development") since 展 and 電 share the same Korean syllable 전 — not a vault error, a real feature of the language. No word-level homophones (注音 ㄈㄚㄊㄉㄝㄋ / 羅馬字 fadden unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 発音.

### 2026-09-04, iteration 2627 — [[words/発音|発音]]

発's own stand-in is [[発]] itself, 音's own is [[音楽]] — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word. All pronunciation fields already correct and fully compositional (mandarin fāyīn, cantonese faat3 jam1, japanese はつおん, korean 발음, vietnamese phát âm, 注音/羅馬字/諺文). Added missing simplified alias 发音 alongside existing 發音, removed blank `hsk_level`/`swadesh`. No homophones (注音 ㄈㄚㄊ·ㄨㄇ / 羅馬字 fad'um unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白亜.

### 2026-09-04, iteration 2628 — [[words/白亜|白亜]]

亜's own stand-in is [[亜細亜]], 白's own is [[白]] itself — transitivity fails both ways, no `#cranberry`, neither constituent legitimized by this word (亜 already legitimized elsewhere as the daiyōji stand-in for both 亞/Asia-sense and, separately, 堊/chalk-sense, per its own frontmatter aliases). Already had a strong, substantive `## Notes` section explaining the 亜→堊 daiyōji substitution — kept nearly as-is, just extended the "uses 堊's readings, not 亜's" observation to newly-added cantonese/vietnamese. Filled missing `vietnamese`(bạch ác, following 堊's Sino-Vietnamese reading per the same substitution pattern as mandarin/korean), quoted `mandarin`/`cantonese`/`korean` for consistency, added missing simplified alias 白垩 alongside existing 白堊. No homophones (注音 ㄅㄚㄎㄚ / 羅馬字 bag'a unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白亜紀.

### 2026-09-04, iteration 2629 — [[words/白亜紀|白亜紀]]

Same 亜→堊 daiyōji substitution as [[白亜]]; 紀's own stand-in is [[世紀]], not this word, so transitivity still fails, no `#cranberry`. Already had a strong, substantive `## Notes` section (real geological/historical content) — kept nearly as-is, extended the readings-follow-堊-not-亜 observation to cover this word too. Filled missing `vietnamese`(bạch ác kỷ), quoted `mandarin`/`cantonese`/`korean`, added missing simplified alias 白垩纪 alongside existing 白堊紀. No homophones (注音 ㄅㄚㄎㄚㄍㄧ / 羅馬字 bag'agi unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白内障.

### 2026-09-04, iteration 2630 — [[words/白内障|白内障]]

No cranberry situation (a plain descriptive tri-syllable compound, none of the three constituents' own stand-ins point here). **Fixed a real bug**: `japanese` was truncated to "くないしょう", missing the initial は — corrected to はくないしょう (hakunaishō), matching 白's own HAKU on'yomi. Filled blank `vietnamese`(bạch nội chướng, a real attested Sino-Vietnamese medical term), added missing traditional alias 白內障 (內 differs from shinjitai 内), removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. Wrote a missing `## Notes` section. No homophones (注音 ㄅㄚㄎㄋㄛㄧㄐㄚㄫ / 羅馬字 bagnoijang unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白日夢.

### 2026-09-04, iteration 2631 — [[words/白日夢|白日夢]]

No cranberry (plain descriptive compound). **Found and fixed a real, more widespread reading bug**: the word's own `注音` used ㄋㄞㄊ for 日 instead of 日's real, only-existing syllable ㄋㄧㄊ/nid/닏 (confirmed no `syllables/ㄋㄞㄊ.md` page exists at all) — corrected to ㄅㄚㄎㄋㄧㄊㄇㄨㄫ; the word's own `羅馬字`/`諺文` (bagnidmung/박닏뭉) were already independently correct, so this was purely a `注音` typo within the file itself. **This same wrong ㄋㄞㄊ/ㄋㄝㄊ pattern also appears, uncorrected, in the already-"perfected" [[characters/日 (char)|日 (char)]] and [[characters/夢 (char)|夢 (char)]] pages' own `## Words` rt-annotations** (白日夢, 六日/十六日/二十六日 series, and chengyu 一日三秋) — flagging as a real, wider-reaching bug for a future targeted pass; did not touch those already-stamped character pages today, out of scope for the word sweep. Filled blank `vietnamese`(bạch nhật mộng), added simplified alias 白日梦, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`, wrote a missing `## Notes` section. No word-level homophones (注音 ㄅㄚㄎㄋㄧㄊㄇㄨㄫ / 羅馬字 bagnidmung unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白止.

### 2026-09-04, iteration 2632 — [[words/白止|白止]]

No cranberry (a graphemic simplification, not a compound of two independently-standing constituents). This word actually writes 白芷 (Angelica dahurica) using 止 in place of 芷 — no character page for 芷 exists in this vault, but since 芷 is itself 形声 with 止 as its phonetic component, the readings are identical either way, so no pronunciation fields needed correction; documented the substitution in Notes and added 白芷 as an alias. Fixed the homophone callout from a non-standard `>[!tip] ...` sentence into the proper `>[!warning] Homophones` form (verified exact match on 注音 ㄅㄚㄎㄐㄧ / 羅馬字 bagji — only [[百事]]). **Also fixed the reciprocal callout on `words/百事.md`** (same non-standard `[!tip]` form) so both sides of the homophone pair now cross-link correctly — did not otherwise touch 百事's remaining checklist gaps (blank japanese/vietnamese, no date-last-perfect), which are out of scope until the sweep reaches it alphabetically. Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []` on 白止, wrote a real `## Notes` section. Stamped `date-last-perfect: 2026-09-04`.

Next: 白熊.

### 2026-09-04, iteration 2633 — [[words/白熊|白熊]]

No cranberry (熊's own stand-in is [[熊]] itself, 白's is [[白]] itself). Added missing `kwin: false` (Dan'a'yo 박웅 diverges from literal Sino-Korean 백웅). Wrote a `## Notes` section on an interesting cross-linguistic split: mandarin/cantonese use straightforward Sino compounds, but japanese しろくま/korean 흰곰/vietnamese gấu trắng all use native calques instead, since polar bears have no traditional presence in the Sinosphere's temperate range. Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄅㄚㄎ·ㄨㄫ / 羅馬字 bag'ung unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白狐.

### 2026-09-04, iteration 2634 — [[words/白狐|白狐]]

No cranberry (狐's own stand-in is [[狐狸]], not this word). Fixed `japanese` typo びやくこ (big や) → corrected to びゃっこ (small ゃ, with gemination) — the real, attested reading for the mythological white fox associated with Inari, not just a straightforward compositional concatenation. Filled blank `vietnamese`(bạch hồ), removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. Notes flags a real Korean-internal homophone worth knowing (백호 = both 白狐 and the unrelated 白虎 "white tiger," disambiguated only by context/hanja — not a Dan'a'yo-level homophone requiring this vault's own callout system). No Dan'a'yo homophones (注音 ㄅㄚㄎㄏㄛ / 羅馬字 bagho unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白色.

### 2026-09-04, iteration 2635 — [[words/白色|白色]]

No cranberry (色's own stand-in is [[色彩]], not this word). Fixed comma-joined dual values in both `korean`("백색,하양"→백색, single compositional value) and `vietnamese`("bạch, trắng"→bạch sắc) — matching the precedent set on 甘藷's `korean` fix, native alternatives (하양, trắng) now noted in prose instead. Added missing `kwin: false`. Confirmed via `lexipedia/Swadesh.md` that Swadesh #175 "white" maps to the bare word [[白]], not this compound, so `swadesh` stays correctly omitted rather than blank-then-guessed. Also noted in passing: `色` (char)'s own already-perfected frontmatter has an empty-string `pos: ""` bug — flagged, not fixed (out of scope for word sweep). No homophones (注音 ㄅㄚㄎㄙㄧㄎ / 羅馬字 bagsig unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白菜.

### 2026-09-04, iteration 2636 — [[words/白菜|白菜]]

No cranberry (菜's own stand-in is [[野菜]], not this word). Verified `羅馬字`/`諺文`/`注音` (bagcai/박채/ㄅㄚㄎㄑㄚㄧ) were already correct — confirmed via `syllables/ㄑㄚㄧ.md` that 菜 genuinely belongs to the ㄑ-series "cai" syllable, distinct from 財's ㄐ-series "jai" fixed a few iterations ago; not the same bug recurring. Fixed comma-joined dual `korean`("배추,백채"→배추, the real everyday word, kimchi's base vegetable) and unquoted `hsk_level: 2`→`"2"`. Added missing `kwin: false`. Removed blank `swadesh`/empty-list `aliases: []`. No homophones (注音 ㄅㄚㄎㄑㄚㄧ / 羅馬字 bagcai unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白領.

### 2026-09-04, iteration 2637 — [[words/白領|白領]]

No cranberry (領's own stand-in is [[領土]], not this word). Notable case: mandarin/cantonese render this 20th-century sociological loan-translation as a native Sino compound, but japanese ホワイトカラー and korean 화이트칼라 borrow the English term wholesale instead (already correctly set, verified as real usage). Filled blank `vietnamese`(cổ cồn trắng, a direct English calque rather than Sino-Vietnamese), added simplified alias 白领, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄅㄚㄎㄌㄧㄫ / 羅馬字 bagling unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白頭翁.

### 2026-09-04, iteration 2638 — [[words/白頭翁|白頭翁]]

No cranberry (all three constituents' own stand-ins point to themselves, not this word). Fixed `japanese` typo はくとうをう (using を) → corrected to はくとうおう (お, matching 翁's real on'yomi OU). Filled blank `cantonese`(baak6 tau4 jung1) and `vietnamese`(bạch đầu ông, real attested TCM term), added simplified alias 白头翁, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. Wrote a `## Notes` section covering all three senses (elder, light-vented bulbul, Pulsatilla root). In passing: `characters/翁 (char).md` (already-perfected) has an empty-string `hsk_level: ""` bug — flagged, not fixed. No homophones (注音 ㄅㄚㄎㄊㄛㄨ·ㄨㄫ / 羅馬字 bagtou'ong unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白頭鷲.

### 2026-09-04, iteration 2639 — [[words/白頭鷲|白頭鷲]]

**Found and fixed a real, structural bug**: `characters` cited bare "鷲" directly, but 鷲 has no character page of its own in this vault — it's only an alias of [[就 (char)|就]] (per 就's own Notes and its established sibling pattern on [[就鳥]]/[[禿就]]/[[海就]], all of which correctly cite "就 (char)" and explain the 借代字 substitution in their own Notes). Corrected `characters` to cite "就 (char)"; also found `mandarin` had been badly mixed up — "báitóu hǎidiāo" spliced in an unrelated word (海雕 "sea eagle") instead of using 鷲's real reading jiù — corrected to báitóujiù (matching the compositional pattern already established on 海就/就鳥). Filled blank `cantonese`(baak6 tau4 zau6, using 就/鷲's shared real Cantonese reading zau6) and `vietnamese`(đại bàng đầu trắng, the real native species name). Verified japanese ハクトウワシ and korean 대머리독수리 were already correct real zoological species names (not vault-internal substitution readings, appropriately so). Added the missing companion citation on `characters/就 (char).md`'s own `## Words` list, which had never listed this word despite `characters:` now correctly pointing there. Added simplified alias 白头鹫. No homophones (注音 ㄅㄚㄎㄊㄛㄨㄐㄨㄛ / 羅馬字 bagtoujuo unique, already correct pre-fix). Stamped `date-last-perfect: 2026-09-04`.

Next: 白鳥.

### 2026-09-04, iteration 2640 — [[words/白鳥|白鳥]]

No cranberry (both constituents' own stand-ins point to themselves). Fixed `japanese` はくてう (historical kana 歴史的仮名遣い) → modernized to はくちょう (hakuchō), the real everyday Japanese word for "swan." Notes documents a real semantic split: mandarin/cantonese/vietnamese keep the literal "white bird" sense (their actual "swan" words — 天鵝/thiên nga — are unrelated), while japanese/korean 백조 have narrowed 白鳥 into the standard word for swan itself. Filled blank `vietnamese`(bạch điểu), added simplified alias 白鸟, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄅㄚㄎㄑㄛㄨ / 羅馬字 bagcou unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 白鷺.

### 2026-09-04, iteration 2641 — [[words/白鷺|白鷺]]

Same class of bug as 白頭鷺... i.e. [[白頭鷲]]: `characters` cited bare "鷺", which has no character page of its own — it's an alias/借代字 substitute for [[路]] (per 路's own `### 借代字` section and existing precedent on [[蒼路]] "crane"). Corrected `characters` to cite "路". Unlike the 就/鷲 case, 路 and 鷺 are true Mandarin/Cantonese homophones (lù/lou6), so 路's own regular Dan'a'yo reading already applied correctly with no separate alias-reading needed — all pronunciation fields were already right, only blank `vietnamese`(bạch lộ) needed filling. Added simplified alias 白鹭, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. Added the missing companion citation to `characters/路.md`'s own `## Words` list. No homophones (注音 ㄅㄚㄎㄌㄛ / 羅馬字 baglo unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 百事.

### 2026-09-04, iteration 2642 — [[words/百事|百事]]

Sweep reached this word naturally — earlier (iteration 2632, [[白止]]) only its homophone callout format had been fixed in passing; completed the rest of the checklist now. No cranberry (both constituents' own stand-ins point to themselves). Fixed `characters` bare "百"→"百 (char)" (file has the suffix). Filled blank `japanese`(ひゃくじ)/`vietnamese`(bách sự), removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. Wrote a real `## Notes` section (was just a bare opening bullet) — 百事 is an idiom of comprehensiveness ("all matters, everything"), not a literal count; noted 百事可樂 (Pepsi) as a phono-semantic pun on it. Homophone callout to [[白止]] confirmed already correct (fixed earlier). Stamped `date-last-perfect: 2026-09-04`.

Next: 百分率.

### 2026-09-04, iteration 2643 — [[words/百分率|百分率]]

No cranberry (all three constituents' own stand-ins point elsewhere: 百→[[百]], 分→[[分]], 率→[[比率]]). Fixed `characters` missing "(char)" suffix on 百 (率's bare form was already correct — its file has no suffix). Quoted `mandarin`/`cantonese`/`korean`, added missing `kwin: false`. Notes documents a real Korean spelling rule (率 shifts 률→율 after ㄴ/vowel-final syllables, giving 백분율 not the mechanical 백분률). Added the missing companion citation to `characters/分 (char).md`'s own Words list. No homophones (注音 ㄅㄚㄎㄅㄨㄋㄌㄨㄊ / 羅馬字 bagbunlud unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 百家.

### 2026-09-04, iteration 2644 — [[words/百家|百家]]

No cranberry (家's own stand-in is [[家庭]], not this word). Already had a strong, substantive `## Notes` section on 諸子百家/the Hundred Schools — kept as-is, extended to cover the newly-added vietnamese. Quoted `mandarin`/`cantonese`/`korean`, filled missing `vietnamese`(bách gia, real term, as in Chư tử bách gia). No homophones (注音 ㄅㄚㄎㄍㄚ / 羅馬字 bagga unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 百済.

### 2026-09-04, iteration 2645 — [[words/百済|百済]]

No cranberry (a historical proper noun, not a semantically-compositional pair). Fixed `characters` missing "(char)" suffix on 百, fixed comma-joined `japanese`("くだら, ひゃくさい"→くだら, the old native reading reflecting Baekje's historical ties to Japan, matching real usage — mentioned ひゃくさい as the on'yomi alternate in prose), removed redundant duplicate `品詞` field (already covered by `pos`), fixed `## Etymology` heading to `## Notes` and wrote real historical content (Three Kingdoms of Korea, transmission of Buddhism/literacy to Japan, fall in 660 AD). No homophones (注音 ㄅㄚㄎㄐㄝㄧ / 羅馬字 bagjei unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 百科.

### 2026-09-04, iteration 2646 — [[words/百科|百科]]

No cranberry (科's own stand-in is [[学科]], not this word). Fixed a real `cantonese` typo (bak3→baak3, missing the extra a matching 百's own baak3). Fixed `characters` missing "(char)" suffix, fixed `## Etymology` heading to `## Notes` and wrote real content — 百科 functions chiefly as a bound "encyclopedic/comprehensive" prefix (百科事典, and institutional "polytechnic" naming) rather than standing alone. Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄅㄚㄎㄍ⺢ / 羅馬字 bagkwa unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 百科事典.

### 2026-09-04, iteration 2647 — [[words/百科事典|百科事典]]

No cranberry (all four constituents' own stand-ins point elsewhere). **Fixed a real, truncated `japanese` bug**: field was just "じてん" (事典 alone), missing the 百科 (hyakka) portion entirely — corrected to ひゃっかじてん, the real standard Japanese word for encyclopedia. Fixed comma-joined `korean`("백과사전, 백과전서"→백과사전, matching this word's own 事典-based characters; kept 백과전서 as a real alternate mentioned in prose, since it uses different characters 全書 rather than being a simple reading variant). Fixed `characters` missing "(char)" suffix on 百. Rebuilt the body from a bare "百科 + 事典" line into proper `## Notes` structure, linking the two meaningful sub-compounds [[百科]]/[[事典]] per the multi-character-component convention. Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`, added missing `kwin: false`. No homophones (注音 ㄅㄚㄎㄎ⺢ㄐㄧㄉㄝㄋ / 羅馬字 bagkwajiden unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 皇帝.

### 2026-09-04, iteration 2648 — [[words/皇帝|皇帝]]

皇's own stand-in is this exact compound, but 帝's own is [[帝王]] — transitivity fails, no `#cranberry`, though 皇 is legitimized specifically by this word. All pronunciation fields were already correct and fully compositional (mandarin huángdì, cantonese wong4 dai3, japanese こうてい, korean 황제, vietnamese hoàng đế, 注音/羅馬字/諺文). Wrote a missing `## Notes` section from scratch — Qin Shi Huang's 221 BC coinage fusing 皇 (Three Sovereigns) and 帝 (Five Emperors/上帝) into a title above 王 "king," and its later politically-loaded adoption by Japan/Korea/Vietnam for their own monarchs. Removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄏ⺢ㄫㄊㄝㄧ / 羅馬字 hwangtei unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 皮革.

### 2026-09-04, iteration 2649 — [[words/皮革|皮革]]

**Cranberry confirmed**: both 皮's own stand-in and 革's own stand-in are this exact compound — transitivity holds, added the `#cranberry` tag (was missing). Fixed comma-joined `cantonese`("pei4 gaak3, pei4 gaap3"→pei4 gaak3, matching 革's own citation — the second value wasn't attested on 革's own character page either). Filled blank `vietnamese`(bì cách), normalized `characters` from flow-style `[皮, 革]` to block list, fixed `## Etymology` heading to `## Notes` and wrote real content distinguishing 皮 (raw hide) from 革 (tanned leather). Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄅㄧㄎㄧㄎ / 羅馬字 bikig unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 皺紋.

### 2026-09-04, iteration 2650 — [[words/皺紋|皺紋]]

皺's own stand-in is this exact compound, but 紋's own is [[紋]] itself — transitivity fails, no `#cranberry`, though 皺 is legitimized specifically by this word. Checked the unusual interpunct in `注音`/rt-annotations (ㄐㄨ·ㄇㄨㄋ, between two syllables where the second has a normal consonant initial, not the usual null-initial trigger) — left unchanged since it's already consistently applied across three independently-dated citations (this word plus both 皺 and 紋's own character pages), so it's an established convention rather than a propagated typo like the 日/ㄞ case. Fixed relative links in the opening bullet (were missing `../` prefix, resolving to word-file paths instead of character pages). Quoted `mandarin`/`cantonese`/`korean`. Notes flags a real Korean-internal homophone (추문 = both this word and the unrelated, far more common 醜聞 "scandal"). No Dan'a'yo-level homophones (注音 ㄐㄨ·ㄇㄨㄋ / 羅馬字 jumun unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盆.

### 2026-09-04, iteration 2651 — [[words/盆|盆]]

Single-character stand-in word (like 嫩/多/痩/癖/発). Fixed bare-string `characters` to list form, added missing `pos`(名詞)/`japanese`(ぼん)/`kwin`. Added a missing `>[!warning] Homophones` callout — found via exact grep that [[紛]] shares 注音 ㄆㄨㄋ/羅馬字 pun exactly; added the reciprocal callout on `words/紛.md` too (not otherwise perfected, out of scope until the sweep reaches it). Fixed tip-callout link to include `(char)` suffix. Wrote a substantive `## Notes` section, including the coincidental unrelated etymology of お盆 (Obon festival, from Sanskrit ullambana) sharing the same character. Stamped `date-last-perfect: 2026-09-04`.

Next: 盛衰.

### 2026-09-04, iteration 2652 — [[words/盛衰|盛衰]]

No cranberry (盛's own stand-in is [[全盛]], 衰's is [[衰弱]]). Filled a completely blank `pos`(名詞) and `vietnamese`(thịnh suy, real attested term), normalized `characters` from flow-style to block list, fixed `## Etymology` heading to `## Notes` and wrote real content — the classical/Buddhist idiom 盛者必衰 and its famous opening-line echo in the *Tale of the Heike*. Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄙㄧㄫㄙ⼔ㄧ / 羅馬字 singswei unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盟誓.

### 2026-09-04, iteration 2653 — [[words/盟誓|盟誓]]

誓's own stand-in is this exact compound, but 盟's own is [[連盟]] — transitivity fails, no `#cranberry`, though 誓 is legitimized specifically by this word. Fixed comma-joined `mandarin`("méngshì, míngshì"→méngshì, the second variant wasn't attested on 盟's own character page). Filled blank `vietnamese`(minh thệ). Notes documents a real Korean lexicalized sound change: modern standard 맹세 rather than the mechanically-compositional 맹서 (already correctly set in `korean`, explained rather than "corrected"). Normalized `characters` list indentation, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄇ⼶ㄫㄙㄝ / 羅馬字 myengse unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 監獄.

### 2026-09-04, iteration 2654 — [[words/監獄|監獄]]

獄's own stand-in is this exact compound, but 監's own is [[監督]] — transitivity fails, no `#cranberry`, though 獄 is legitimized specifically by this word. All pronunciation fields already correct and fully compositional (mandarin jiānyù, cantonese gaam1 juk6, japanese かんごく, korean 감옥, 注音/羅馬字/諺文). Filled blank `vietnamese`(giám ngục) and flagged a real semantic drift: the Sino-Vietnamese compound has come to mean "prison warden" rather than "prison" itself, with native nhà tù preferred for the institution. Added simplified alias 监狱, normalized `characters` list indentation, removed blank `hsk_level`/`swadesh`/`aliases`. No homophones (注音 ㄍㄚㄇ⼄ㄎ / 羅馬字 gam'yog unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 監禁.

### 2026-09-04, iteration 2655 — [[words/監禁|監禁]]

No cranberry (監's own stand-in is [[監督]], 禁's is [[禁止]]). Quoted `mandarin`/`cantonese`/`korean`, added missing `kwin: false`, added simplified alias 监禁 (a very common real word). Notes distinguishes this word (the act of confining) from [[監獄]] (the institution), and notes giam cầm as the more common everyday Vietnamese verb versus this word's compositional giám cấm. No homophones (注音 ㄍㄚㄇㄍㄧㄇ / 羅馬字 gamgim unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盤古.

### 2026-09-04, iteration 2656 — [[words/盤古|盤古]]

No cranberry (盤's own stand-in is [[盤]] itself, 古's is [[古代]]). Fixed `pos` from 名詞 to 固有名詞, matching this vault's established convention for mythological/deity proper nouns. Quoted `mandarin`/`cantonese`/`korean`. Expanded terse two-bullet Notes into full substantive paragraphs on the Pangu creation myth (cosmic egg, 18,000 years separating heaven and earth, body becoming the world upon death). **Homophone-check correction**: an initial `grep -F` pass flagged [[辦公]]/[[辦公室]] as false-positive homophones — they only share a *prefix* substring (ㄅㄚㄋㄍㄛ vs their real ㄅㄚㄋㄍㄛㄫ, an extra final ㄫ), not the whole syllable string; re-verified with `grep -xF` (exact whole-line match) and confirmed no real homophones exist. Stamped `date-last-perfect: 2026-09-04`.

Next: 盧森堡.

### 2026-09-04, iteration 2657 — [[words/盧森堡|盧森堡]]

No cranberry (none of the three constituents' own stand-ins point here; 盧's is even the special 名専字 proper-name-only marker). **Found and fixed a real reading bug, inverse of the usual pattern**: `羅馬字`/`諺文` used 森's *real Korean* reading (sam/삼) instead of its *Dan'a'yo-internal* reading (sum/숨) — `注音` (ㄌㄛㄙㄨㄇㄅㄚㄨ) was already correct and gave away the mismatch (森's own 諺文/羅馬字 on its character page are 숨/sum, distinct from its `korean` field 삼). Corrected losambau/로산밧 → losumbau/로숨밧. Filled blank `vietnamese`(Lúc-xăm-bua, the real French-derived exonym), added simplified alias 卢森堡. Notes explains this is a phono-semantic transliteration of the European country name, not a compositional description, and that Japanese/Korean/Vietnamese all transliterate independently from a European source rather than through the Chinese-character intermediary. No homophones after correction (注音 ㄌㄛㄙㄨㄇㄅㄚㄨ / 羅馬字 losumbau unique — confirmed the corrected form didn't exist anywhere in the vault before this edit). Stamped `date-last-perfect: 2026-09-04`.

Next: 盧魚.

### 2026-09-04, iteration 2658 — [[words/盧魚|盧魚]]

盧 here is a 借代字 clipped phonetic stand-in for the fuller 鱸魚 (per 盧's own Notes), not itself meaning "fish"; already correctly captured in aliases 鱸魚/鲈鱼. Fixed `characters` order (was listing 魚 before 盧, opposite of the actual word/filename order). Fixed a malformed `cantonese` ("ou4 jyu4-2", missing the initial l and using non-standard tone notation) → "lou4 jyu2" (a real, documented colloquial changed-tone reading for 魚 in fish/food compounds). **Fixed `korean` from a South Korean 두음법칙-shifted form (노어) to the required North Korean/문화어 form (로어)**, per the vault's standing rule (see [[feedback_korean_reading_north]]). Filled blank `vietnamese`(lư ngư). Fixed the homophone callout from a non-standard `[!tip]` sentence to proper `[!warning] Homophones` format on both this word and its homophone [[露語]] (fixed reciprocally; verified exact match on 注音/羅馬字/諺文, all three identical). No other homophones. Stamped `date-last-perfect: 2026-09-04`.

Next: 目宿.

### 2026-09-04, iteration 2659 — [[words/目宿|目宿]]

No cranberry (目's own stand-in is [[目]] itself, 宿's is [[寄宿]]) — used purely phonetically here, an early transliteration variant of 苜蓿 (already correctly captured as alias), not a borrowed-glyph 借代字 case like 鷲/鷺/盧 since 目 and 宿 are themselves ordinary, independently-meaningful characters just repurposed for sound. Fixed comma-joined `mandarin`("mùxu, mùsù"→mùxu, the modern standard reading; mùsù noted as the classical alternate in prose). Fixed `## Etymology` heading to `## Notes` and wrote real etymology — alfalfa's Han-dynasty introduction via Zhang Qian's mission to Dayuan/Ferghana as horse fodder, and the character choice as a foreign-sound transliteration. Normalized `characters` indentation and `aliases` to block style. No homophones (注音 ㄇㄨㄎㄙㄨㄎ / 羅馬字 mugsug unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 目標.

### 2026-09-04, iteration 2660 — [[words/目標|目標]]

No cranberry (標's own stand-in is [[標識]], not this word). Left an unusual `注音`/`羅馬字` pattern unchanged: the compound adds an extra ㄨ/u to 標's normal reading (byo→byou), consistent across both this word file and 標's own character-page citation of 目標 — an established compound-specific alternation, not a typo, per the same reasoning as the 皺紋 interpunct case. Removed redundant duplicate `品詞` field. Fixed `## Etymology` heading to `## Notes`, added simplified alias 目标. No homophones (注音 ㄇㄨㄎㄅ⼄ㄨ / 羅馬字 mugbyou unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盲人.

### 2026-09-04, iteration 2661 — [[words/盲人|盲人]]

No cranberry (盲's own stand-in is [[盲目]], 人's is [[人]] itself). All pronunciation fields already correct and compositional (mandarin mángrén, cantonese maang4 jan4, japanese もうじん, korean 맹인, 注音/羅馬字/諺文). Filled blank `vietnamese`(manh nhân, compositional — noted native người mù as the everyday alternative), normalized `characters` from flow-style to block list, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`, wrote a missing `## Notes` section. No homophones (注音 ㄇㄚㄫㄋㄧㄋ / 羅馬字 mangnin unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盲従.

### 2026-09-04, iteration 2662 — [[words/盲従|盲従]]

No cranberry (従's own stand-in is [[従]] itself, 盲's is [[盲目]]). Already had strong, substantive Notes — kept as-is, extended lightly for the newly-filled vietnamese. Quoted `mandarin`/`cantonese`/`korean`, filled blank `vietnamese`(manh tùng), quoted `従 (char)` citation for consistency. No homophones (注音 ㄇㄚㄫㄐㄛㄫ / 羅馬字 mangjong unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盲目.

### 2026-09-04, iteration 2663 — [[words/盲目|盲目]]

盲's own stand-in is this exact compound, but 目's own is [[目]] itself — transitivity fails, no `#cranberry`, though 盲 is legitimized specifically by this word. Fixed comma-joined `vietnamese`("mù, đui mù"→mù, the standard native word; đui mù noted as a fuller synonymous expression in prose). All other pronunciation fields already correct and compositional. Wrote a missing `## Notes` section — the word's dominant modern use is figurative ("blind" love/faith/obedience) rather than literal loss of sight. No homophones (注音 ㄇㄚㄫㄇㄨㄎ / 羅馬字 mangmug unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 直.

### 2026-09-04, iteration 2664 — [[words/直|直]]

Single-character stand-in word. **Found and fixed a real, corroborated bug on the already-perfected `characters/直 (char).md` page itself**: its own `羅馬字`/`諺文`/`kwin` were stored as jig/직/true, but every other character sharing this exact syllable — 質, 疾, 嫉, 膣, 蛭 — independently uses jid/짇 (matching `syllables/ㄐㄧㄊ.md`'s canonical values); corrected 直's own page to jid/짇/false. The old wrong 직 happened to coincide with 直's own real Korean reading (also 직 in real-world Korean), which is likely why the error went unnoticed. Propagated the fix to this word file. Fixed bare-string `characters`, `vietnamese: null`, missing `pos`(性詞)/`japanese`(ちょく). **Found a three-way homophone**, all previously uncallout'd: [[直]]/[[膣]]/[[蛭]] all share 注音 ㄐㄧㄊ / 羅馬字 jid exactly — added callouts to all three (質/疾/嫉 also share the syllable but aren't themselves standalone words, so don't need the callout). Fixed tip-callout link to include `(char)` suffix, wrote a substantive `## Notes` section. Stamped `date-last-perfect: 2026-09-04`.

Next: 直線.

### 2026-09-04, iteration 2665 — [[words/直線|直線]]

線's own stand-in is this exact compound, but 直's own is [[直]] itself — transitivity fails, no `#cranberry`, though 線 is legitimized specifically by this word. **This word independently corroborated the 直-syllable bug found last iteration**: it had yet a *third* wrong variant for 直's portion (jing/징, distinct from both the correct jid/짇 and the previously-fixed-on-the-character-page wrong jig/직) — corrected to jidsyen/짇션 (線's own portion, syen/션, was already correct). Fixed `characters` from flow-style to block list. Filled blank `vietnamese`(trực tuyến) and flagged a real semantic drift: it now means "online/live" in everyday Vietnamese, not "straight line" (Vietnamese math uses native đường thẳng instead). Removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄐㄧㄊㄙ⼶ㄋ / 羅馬字 jidsyen unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 直観.

### 2026-09-04, iteration 2666 — [[words/直観|直観]]

観's own stand-in is [[観察]], not this word; 直's own is [[直]] itself — no cranberry. Fixed the same 直-syllable bug (jing/징→jid/짇) found in the last two iterations. Fixed `characters` from flow-style to block list, fixed `## Etymology` heading to `## Notes`, wrote substantive content on intuition's philosophical register (phenomenology, Kantian *Anschauung*). No homophones (注音 ㄐㄧㄊㄍ⺢ㄋ / 羅馬字 jidgwan unique). Stamped `date-last-perfect: 2026-09-04`.

### 2026-09-04, out-of-sequence fix — the 直-syllable bug, vault-wide

With the bug now confirmed on 3 consecutive words (直, 直線, 直観) plus the root cause found on `characters/直 (char).md` itself, ran a targeted grep across all word files citing 直 for the same wrong `羅馬字` pattern (jig/jing instead of jid). Found and fixed 5 more affected files: **already-perfected** `words/垂直.md` (juijig→juijid, 쥐직→쥐짇 — also had to rewrite part of its own kwin-reasoning prose, which had explicitly argued "Dan'a'yo 직 = Sino-Korean 직" based on the since-corrected wrong value), `words/直径.md` (jiggeng→jidgeng), `words/率直.md` (ludjig→ludjid); **not-yet-perfected** `words/直角.md` and `words/硬直.md` (syllable only fixed, `硬直` left otherwise unperfected — alphabetically still ahead in the sweep, correctly not yet reached). `直角` was reached naturally by the sweep in the very next iteration below and got a full pass. Total confirmed instances of this bug: 8 (直, 直線, 直観, 垂直, 直径, 率直, 直角, 硬直).

### 2026-09-04, iteration 2667 — [[words/直角|直角]]

Reached naturally by the sweep, already had its 直-syllable bug fixed above. No cranberry (角's own stand-in is [[角]] itself). Fixed `characters` missing "(char)" suffix on both 直 and 角 (角's file is `角 (char).md`), fixed `## Etymology` heading to `## Notes`, removed blank `hsk_level`/`swadesh`/`aliases`. Notes notes Vietnamese's native góc vuông rather than a Sino-Vietnamese compound. No homophones (注音 ㄐㄧㄊㄍㄛㄎ / 羅馬字 jidgog unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 相互.

### 2026-09-04, iteration 2668 — [[words/相互|相互]]

**Cranberry confirmed**: both 相's own stand-in and 互's own stand-in are this exact compound — transitivity holds, added the `#cranberry` tag (was missing). Fixed comma-joined `korean`("상호,서로"→상호, the formal/written form; 서로, the native everyday word both characters independently cite as their own native gloss, moved to prose). Normalized `characters` from flow-style to block list, added missing `kwin: true` (Dan'a'yo 상호 matches literal Sino-Korean exactly), removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`, fixed `## Etymology` heading to `## Notes`. No homophones (注音 ㄙㄚㄫㄏㄛ / 羅馬字 sangho unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 相当.

### 2026-09-04, iteration 2669 — [[words/相当|相当]]

No cranberry (相's own stand-in is [[相互]], 当's is [[当]] itself). Already had strong Notes on the verb/degree-adverb double duty — kept as-is. Quoted `mandarin`/`cantonese`/`korean`, filled blank `vietnamese`(tương đương, a real, very common standard term). No homophones (注音 ㄙㄚㄫㄉㄚㄫ / 羅馬字 sangdang unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 相思.

### 2026-09-04, iteration 2670 — [[words/相思|相思]]

No cranberry (思's own stand-in is [[思考]], 相's is [[相互]]). **Fixed a truncated `諺文`**: was just "상" (one syllable) instead of "상사" (matching the two-syllable `羅馬字`/`注音` already present). Fixed `kwin` from false to true — Dan'a'yo 상사 (once corrected) exactly matches literal Sino-Korean 상사 (相's 상 + 思's 사). Wrote real content — Wang Wei's famous 相思 poem and the "lovesickness beans" (相思豆) motif. Normalized `characters` to block list, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄙㄚㄫㄙㄚ / 羅馬字 sangsa unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 盾.

### 2026-09-04, iteration 2671 — [[words/盾|盾]]

Single-character stand-in word. Fixed bare-string `characters`, `vietnamese: null`, missing `pos`(名詞)/`japanese`(じゅん)/`kwin`(false). Checked homophone syllable ㄐㄨㄋ — shared with 准/俊/樽/純/準/遵, but none of them are standalone words (all have compound-based stand-ins), so no homophone callout needed. Wrote a substantive `## Notes` section, including the 矛盾 ("spear and shield," i.e. contradiction) idiom. Stamped `date-last-perfect: 2026-09-04`.

Next: 眉.

### 2026-09-04, iteration 2672 — [[words/眉|眉]]

Single-character stand-in word. Fixed bare-string `characters`, `vietnamese: null`, missing `pos`(名詞)/`japanese`(び)/`kwin`(false). Checked homophone syllable ㄇㄧㄜ — shared with 寐/薇/魅, none of which are standalone words, so no callout needed. Wrote a substantive `## Notes` section (焦眉 idiom, 眉間). Stamped `date-last-perfect: 2026-09-04`.

Next: 看.

### 2026-09-04, iteration 2673 — [[words/看|看]]

Single-character stand-in word. Fixed bare-string `characters`, `vietnamese: null`, missing `pos`(事詞)/`japanese`(かん)/`kwin`(false). Completed a homophone callout that [[刊]] had already anticipated (its own Notes literally said "the reciprocal half will be completed when it comes up") — added the `[!warning] Homophones` callout here and tidied 刊's forward-looking sentence into a plain statement now that both sides are done. Wrote a substantive `## Notes` section. Stamped `date-last-perfect: 2026-09-04`.

Next: 県.

### 2026-09-04, iteration 2674 — [[words/県|県]]

Single-character stand-in word. Fixed bare-string `characters`, `vietnamese: null`→huyện (character's own vietnamese field was completely empty on its char page, no options to draw from — used independent real-world knowledge that 縣/県's Sino-Vietnamese reading huyện is a live administrative term in Vietnam itself), missing `pos`(名詞)/`japanese`(けん)/`kwin`(false). Verified the existing homophone callout ([[玄]]/[[懸]]) via exact grep — correct and complete; 絢/萱 also share the syllable but aren't standalone words. In passing: `characters/県 (char).md` has an empty-string `hsk_level: ""` bug (same class as 色/翁, flagged not fixed). Wrote a substantive `## Notes` section on 県's varying rank by country (Chinese county, Japanese prefecture, Vietnamese district) and its "to hang" etymology. Stamped `date-last-perfect: 2026-09-04`.

Next: 眼前.

### 2026-09-04, iteration 2675 — [[words/眼前|眼前]]

No cranberry (眼's own stand-in is [[眼球]], 前's is [[前]] itself). Filled a completely blank `pos`(名詞). Fixed comma-joined `korean`("안전, 눈앞"→눈앞, the native unambiguous term) — flagged that the Sino-compositional 안전 would collide with the far more common unrelated word 安全 "safety". Filled blank `vietnamese`(nhãn tiền, a real attested term). Added missing `kwin: true` (Dan'a'yo 안전 matches literal Sino-Korean exactly). Fixed `## Etymology` heading to `## Notes`. No homophones (注音 ㄚㄋㄐㄝㄋ / 羅馬字 'anjen unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 眼球.

### 2026-09-04, iteration 2676 — [[words/眼球|眼球]]

眼's own stand-in is this exact compound, but 球's own is [[球]] itself — transitivity fails, no `#cranberry`, though 眼 is legitimized specifically by this word. Removed redundant duplicate `品詞` field. Filled blank `vietnamese`(nhãn cầu, the real anatomical term). Left an unusual `注音` pattern unchanged: 球's syllable renders as the split "ㄍ·ㄨ" instead of the compact ⼄-style glyph ㄍ⼜ used in every other 球-compound on 球's own page (排球/台球/蹴球) — but consistently so across 3 independent citations (this word, and both 眼's and 球's own character-page citations of 眼球 specifically), so treated as an established compound-specific quirk rather than a typo. No homophones (注音 ㄚㄋㄍ·ㄨ / 羅馬字 'angyu unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 眼睛.

### 2026-09-04, iteration 2677 — [[words/眼睛|眼睛]]

睛's own stand-in is this exact compound, but 眼's own is [[眼球]] — transitivity fails, no `#cranberry`, though 睛 is legitimized specifically by this word. Fixed relative links missing `../` prefix. Notes flags a real Korean-internal homophone (안정 = both this word and the unrelated 安定 "stability"). Normalized `characters` to block list, removed blank `hsk_level`/`swadesh`/empty-list `aliases: []`. No homophones (注音 ㄚㄋㄐㄧㄫ / 羅馬字 'anjing unique). Stamped `date-last-perfect: 2026-09-04`.

Next: 着.

### 2026-09-04, out-of-sequence fix — the ㄞ/日 bug, vault-wide

User flagged that the ㄞ/ㄋㄝㄊ-for-日 bug found in the 白日夢 iteration was worse than described: per `grammar/文法 - 03文字法.md` line 156, ㄞ (and ㄟ/ㄠ/ㄡ/ㄢ/ㄣ/ㄤ) are **explicitly forbidden** Mandarin-style diphthongs in Dan'a'yo, not merely unused — confirmed against the full official glyph inventory in `grammar/Bopomofo.md`, which has no compound-final glyphs at all beyond the vault's own custom blends (⼄⼔⼘⼜⼶⺢). ㄋㄝㄊ, by contrast, is a real, legitimately-catalogued syllable (`syllables/ㄋㄝㄊ.md`) — but it belongs to 涅/捏, not 日, so its use for 日 was still wrong even though the glyph itself is legal.

Ran a vault-wide grep for both patterns and fixed every genuine instance (leaving legitimate 涅/捏 citations of ㄋㄝㄊ untouched):
- `words/六日.md`, `words/二十六日.md` — `注音` corrected (羅馬字/諺文 were already right)
- `chengyu/一日三秋.md` — `注音` corrected; `chengyu/Misc. Chengyu.md` citation corrected
- `lexipedia/Calendar.md` — 六日 citation corrected
- `characters/日 (char).md` — 5 wrong rt-annotations corrected (白日夢, 六日, 十六日, 二十六日, 一日三秋); left its legitimate 涅 citation alone
- `characters/白 (char).md`, `characters/夢 (char).md`, `characters/秋 (char).md`, `characters/六 (char).md` — their own citations of the same compounds corrected

Post-fix grep confirms zero remaining ㄞ usage outside this log and the grammar doc that documents the prohibition, and zero remaining wrong ㄋㄞㄊ/ㄋㄝㄊ-for-日 citations anywhere. `words/六日.md`/`二十六日.md` were only spot-fixed for this specific bug, not given a full checklist pass (they're well outside today's alphabetical sweep position and remain otherwise unperfected).
