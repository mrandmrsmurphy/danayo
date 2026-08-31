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
