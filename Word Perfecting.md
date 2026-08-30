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
