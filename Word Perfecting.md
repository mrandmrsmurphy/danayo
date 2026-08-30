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
