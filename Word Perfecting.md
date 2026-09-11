# Word Perfecting Log

**2026-09-11: Methodology pivot.** The sweep previously ran a strict alphabetical (`LC_ALL=C`) resweep over *every* file in `words/`, re-verifying and re-stamping each one regardless of whether it already had a `date-last-perfect`. That's slow and wasteful: as of this pivot, 6011 words exist total, but only **246 have never been touched at all** (no `date-last-perfect` field whatsoever) — the rest already carry a stamp from an earlier pass. The user corrected this: going forward, the sweep processes **only the 246 never-perfected words**, one per cron firing, until that list is empty. The full alphabetical resweep can resume afterward if desired.

### 2026-09-11, word 1/246 — [[words/僧伽|僧伽]]
Never-perfected word, genuinely untouched. Fixed inline-flow `characters:`, filled blank `pos:` (名詞), unspaced cantonese, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, merged thin `## Etymology` into a full `## Notes` section. **Found and fixed a real internal self-contradiction**: this word's own `注音` (ㄙㄜㄫㄍ⼘, "seng"-pattern) didn't match its own `諺文`/`羅馬字` (숭갸/sunggya, "sung"-pattern) — corrected `注音` to ㄙㄨㄫㄍ⼘, joining the "sung" variant already used consistently by sibling words [[僧侶]]/[[尼僧]]/[[密陀僧]] (per 僧(char)'s own long-standing flagged note about this cross-word inconsistency, now updated to record the fix). Updated the citation ruby on 僧.md to match. **Found and fixed an entirely-missing `## Words` section** on 伽.md (had no Words list at all) — added citations for both 僧伽 and 揄伽. `kwin: false` confirmed (own 諺文 숭갸 vs own korean 승가 diverge), no homophone collision, both constituent citations now present.

Next: 僧家.

### 2026-09-11, word 2/246 — [[words/僧家|僧家]]
Never-perfected word. Filled two entirely-blank fields (`cantonese: ""` and `vietnamese: ""`) with compositional readings (zang1 gaa1, tăng gia — the latter a coincidental homograph with the common phrase "to increase," disclosed rather than avoided). Removed duplicate `品詞` key, merged thin `## Etymology` into a full `## Notes` section, filled a missing `date-last-perfect` entirely. Added a missing legitimizing note for 僧, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: true` confirmed exact match, no homophone collision.

Next: 儀式.

### 2026-09-11, word 3/246 — [[words/儀式|儀式]]
Never-perfected word. Filled entirely-missing `kwin` (false, verified byte-level: own 諺文 읫식 U+C76B ≠ own korean 의식 U+C758, same 읫/의 divergence pattern as 倚/義) and entirely-missing `date-last-perfect`; wrote a `## Notes` section from scratch (page had none). Added a missing legitimizing note for 儀, whose own `stand_in` points to this word. Both character-page citations already present, no homophone collision.

Next: 儀礼.

### 2026-09-11, word 4/246 — [[words/儀礼|儀礼]]
Never-perfected word. Removed duplicate `品詞` key, flattened single-item `japanese`/`vietnamese` lists, filled entirely-missing `kwin` (false) and `date-last-perfect`, fixed broken relative links, integrated a stray unformatted note ("Also the name of a famous book") into proper prose about the Confucian classic 儀禮. `characters:` confirmed correct via `ls` (礼 (char) disambiguation necessary), both character-page citations already present, no homophone collision.

Next: 儒学.

### 2026-09-11, word 5/246 — [[words/儒学|儒学]]
Never-perfected word. Fixed inline-flow `characters:`/`aliases:` lists. **Found and fixed a bad aliases entry**: 儒教 and 孔教 were listed as if spelling variants of 儒学, but both are separately-attested Confucianism-related terms with their own dedicated vault pages — removed, kept only genuine traditional form 儒學. **Found and fixed a mismatched link**: an "Emphasizes" list item displayed "智" (wisdom) but linked to the unrelated word [[知]] ("to know") — corrected to link to [[智慧]] (智's own legitimizing word, confirmed via 智(char)'s own `stand_in` field). Converted raw-markdown links to wikilinks throughout that list. Filled a missing `date-last-perfect` entirely. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 儒教.

### 2026-09-11, word 6/246 — [[words/儒教|儒教]]
Never-perfected word. Fixed inline-flow `characters:`/`aliases:` lists, removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch (page had none). **Found and fixed a bad aliases entry**: 儒家 was listed as a spelling variant of 儒教, but it's a separately-attested term ("the Confucian school") with its own dedicated vault page — removed, kept only genuine old-form variant 儒敎. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 元年.

### 2026-09-11, word 7/246 — [[words/元年|元年]]
Never-perfected word. Filled a missing `vietnamese` field with honest compositional "nguyên niên" (noting the native năm đầu is more common), filled entirely-missing `kwin` (false, byte-level verified 넌≠년) and `date-last-perfect`. `characters:` confirmed correct via `ls` (年 (char) disambiguation necessary), both character-page citations already present, no homophone collision. Confirmed 元's own `stand_in` is [[元素]] (not this word), so no legitimizing note needed here.

Next: 元日.

### 2026-09-11, word 8/246 — [[words/元日|元日]]
Never-perfected word. Removed duplicate `品詞` key, flattened a single-item `japanese` list. Filled entirely-missing `korean`/`vietnamese` fields with honest compositional readings (원일, nguyên nhật — noting 元旦/nguyên đán is the more common everyday term), entirely-missing `kwin` (false) and `date-last-perfect`. Fixed broken relative links. `characters:` confirmed correct via `ls` (日 (char) disambiguation necessary), both character-page citations already present, no homophone collision.

Next: 兄弟.

### 2026-09-11, word 9/246 — [[words/兄弟|兄弟]]
Never-perfected word. Fixed an unspaced cantonese field, removed dangling blank `swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged a stray unformatted note ("one of the 天常") into proper prose linking [[天常]] (confirmed the page exists). **Found and fixed missing ruby/注音 formatting** on two citations (兄弟, 兄弟姉妹) on 兄(char).md's own Words list — they were plain wikilinks with no ruby tag at all, one also missing a space in its gloss. `characters:` confirmed correct via `ls`, `kwin: false` confirmed, no homophone collision. Confirmed both 兄 and 弟's own `stand_in` point to themselves (not this word), so no legitimizing note needed here.

Next: 先後.

### 2026-09-11, word 10/246 — [[words/先後|先後]]
Never-perfected word. Fixed a full-width-comma-joined `japanese` string into a proper YAML list, filled a missing `vietnamese` field with honest compositional "tiên hậu," filled a missing `date-last-perfect` entirely, integrated a stray unformatted note ("not the same as 前後") into proper prose (confirmed [[前後]] exists). `characters:` confirmed correct via `ls` (後 (char) disambiguation necessary), both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 先進.

### 2026-09-11, word 11/246 — [[words/先進|先進]]
Never-perfected word. Fixed inline-flow `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. `characters:` confirmed correct via `ls`, both character-page citations already present, `kwin: true` confirmed exact match, no homophone collision.

Next: 光子.

### 2026-09-11, word 12/246 — [[words/光子|光子]]
Never-perfected word. Filled a blank `japanese` field (こうし, compositional 光's KOU + 子's SHI, a real attested Japanese word); removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`; filled a missing `date-last-perfect` entirely; wrote a `## Notes` section from scratch. **Found and fixed a missing citation** on 子.md's own Words list (光子 was documented on 光(char).md but never cited back — noted that 子.md's Words section is itself large/disorganized, mixed ruby and bare-link citations, consistent with the already-known cleanup backlog on similar character pages). `characters:` confirmed correct via `ls`, `kwin: false` confirmed, no homophone collision.

Next: 光明.

### 2026-09-11, word 13/246 — [[words/光明|光明]]
Never-perfected word; unusually a massive essay-length page (~150 lines of Notes) rather than the vault's typical concise style, but factually sound. Removed duplicate `品詞` key, added the missing standard `>[!tip]` header block, renamed the non-standard `## Definition and Etymology` heading to `## Notes` (kept all its `###` subheadings and content as-is — a substantive rewrite was out of scope for this pass), filled a missing `date-last-perfect` entirely, added `kwin`/homophone verification sentence. `characters:` confirmed correct via `ls` (明 (char) disambiguation necessary), both character-page citations already present, `kwin: true` confirmed exact match, no homophone collision.

Next: 光栄.

### 2026-09-11, word 14/246 — [[words/光栄|光栄]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch (page had none). Added a missing legitimizing note for 栄, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 児児.

### 2026-09-11, word 15/246 — [[words/児児|児児]]
Never-perfected word. **Found and fixed a real-equivalent-word-instead-of-own-reading bug affecting all five reading fields simultaneously**: mandarin/cantonese/japanese/korean/vietnamese had each been filled with that language's own everyday equivalent for "baby" (bǎobèi 寶貝, ベイビー the English loanword, 애기, em bé) rather than 児児's own compositional doubled reading of 児 — corrected all five to honest compositional doublings (érér, ji4 ji4, じじ, 아아, nhi nhi), disclosing that none are independently attested and that じじ coincidentally collides with the unrelated real word 爺 ("old man"). Filled a blank `pos:` (名詞) and a missing `date-last-perfect` entirely; integrated a stray unformatted/typo'd note ("synonymouys") into proper prose; merged `## Etymology` into `## Notes`. No homophone collision. **Flagged**: this same real-equivalent-word pattern may affect other reduplicated words already marked "perfected" under the old sweep (spot-checked [[妹妹]], whose japanese いもうと/korean 여동생 look like the identical bug) — outside current 246-word scope, noted for a future dedicated pass.

Next: 児童.

### 2026-09-11, word 16/246 — [[words/児童|児童]]
Never-perfected word. Fixed inline-flow `characters:`/`aliases:` lists, filled a blank `pos:` (名詞), fixed unspaced cantonese, trimmed a comma-joined `korean` field (native synonym 어린이 moved to prose, kept Sino-Korean 아동 alone), quoted bare `hsk_level`, filled entirely-missing `kwin` (false) and `date-last-perfect`, wrote a `## Notes` section from scratch. Added a missing legitimizing note for 童, whose own `stand_in` points to this word. Both character-page citations already present, no homophone collision.

Next: 入口.

### 2026-09-11, word 17/246 — [[words/入口|入口]]
Never-perfected word. Disambiguated bare 入/口 to "入 (char)"/"口 (char)" (both words/入.md and words/口.md exist — confirmed via `ls`; Etymology prose was already using the disambiguated forms, frontmatter wasn't). Quoted bare `hsk_level`, removed dangling blank `swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. **Found and fixed a missing citation** on 口(char).md's own Words list. Disclosed (rather than silently changed) that Vietnamese `nhập khẩu` — the same compositional compound as this word — has semantically drifted to mean "import" in modern usage, not "entrance." `kwin: false` confirmed, no homophone collision.

Next: 八十.

### 2026-09-11, word 18/246 — [[words/八十|八十]]
Never-perfected word. Disambiguated bare 十 to "十 (char)" (words/十.md exists — confirmed via `ls`). Removed duplicate `品詞` key, filled an entirely-blank `vietnamese` field (bát thập, directly attested), filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Found and fixed missing ruby/注音 formatting** on the 八十 citations on both 八(char).md and 十(char).md's own Words lists (both were bare wikilinks with no ruby tag) — noted both pages have several other similarly bare/unformatted citations, part of the same larger disorganized-Words-section pattern already flagged on 人(char)/子.md, out of scope to fully fix here. `kwin: false` confirmed, no homophone collision.

Next: 八千.

### 2026-09-11, word 19/246 — [[words/八千|八千]]
Never-perfected word, but otherwise already well-formed. Filled a missing `date-last-perfect` entirely; added `kwin`/homophone verification sentence. `characters:` confirmed correct via `ls`, both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 八卦.

### 2026-09-11, word 20/246 — [[words/八卦|八卦]]
Never-perfected word. Removed duplicate `品詞` key, a duplicated `meta-bind-embed` block (rendered the word-info panel twice), filled a missing `date-last-perfect` entirely, wrapped the bare trigram list in a proper `## Notes` section with intro text and closing readings synthesis. **Found and fixed invisible non-breaking spaces (U+00A0)** throughout the trigram list (between each element name and its hanzi/pinyin) that were silently defeating a first Edit attempt — resolved via direct `python3` content rewrite once diagnosed. **Found and fixed missing citations** on both 八(char).md (was a bare wikilink, no ruby) and 卦(char).md (missing entirely) for this word. `characters:` confirmed correct via `ls` (卦 (char) disambiguation necessary), `kwin: false` confirmed, no homophone collision.

Next: 八百.

### 2026-09-11, word 21/246 — [[words/八百|八百]]
Never-perfected word. Disambiguated bare 百 to "百 (char)" (words/百.md exists — confirmed via `ls`). Filled an entirely-blank `cantonese` field, replaced the native-Vietnamese `vietnamese: tám trăm` with the Sino-Vietnamese compositional "bát bách" (noting native tám trăm as the everyday alternative in prose rather than silently dropping it), removed duplicate `品詞`/dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Found and fixed missing ruby formatting** on 八(char).md's own bare-wikilink citation for this word. `kwin: false` confirmed, no homophone collision, 百(char).md's own citation already correctly present.

Next: 八紘.

### 2026-09-11, word 22/246 — [[words/八紘|八紘]]
Never-perfected word. Fixed a garbled `english` gloss (literal "eight \bcords" escape typo → "eight cords"). Filled entirely-missing `cantonese`/`vietnamese` fields with compositional readings (baat3 wang4, bát hoành), removed duplicate `品詞`, filled a missing `date-last-perfect` entirely, wrote a proper `## Notes` section (preserving the existing classical *Liezi* citation below it). Added a missing legitimizing note for 紘, whose own `stand_in` points to this word. **Found and fixed a missing citation** on 八(char).md's own Words list. Noted (but did not create) that 紘(char).md's own citation for [[八紘一宇]] points to a page that doesn't exist yet — disclosed honestly in prose rather than left as a silent dangling link. `kwin: false` confirmed, no homophone collision.

Next: 公司.

### 2026-09-11, word 23/246 — [[words/公司|公司]]
Never-perfected word. Disambiguated bare 公 to "公 (char)" (words/公.md exists — confirmed via `ls`; prose already used the disambiguated form). Filled a blank `korean` field with the compositional 공사 (which happens to match this word's own 諺文 exactly, so `kwin` — entirely missing — was filled in as `true`); filled a missing `date-last-perfect` entirely; merged `## Etymology` into a full `## Notes` section. Added a missing legitimizing note for 司, whose own `stand_in` points to this word. **Found and fixed a bare-wikilink citation** (missing ruby, plus a missing-space gloss) on 公(char).md's own Words list. No homophone collision.

Next: 公噸.

### 2026-09-11, word 24/246 — [[words/公噸|公噸]]
Never-perfected word. Disambiguated bare 公/噸 to disambiguated forms (both conflicting word files exist). **Found and fixed a real-equivalent-word bug in `korean`**: 메트릭톤 (a different loanword-based phrase) → compositional 공톤, which conveniently matches this word's own 諺文 exactly, flipping `kwin` from false to true. Fixed a comma-joined `japanese` field, dropping a likely-erroneous second candidate (グラムトン, "gram-ton," not a real unit) and keeping the genuinely attested メトリックトン. Filled blank `cantonese` and honest compositional `vietnamese: công đốn` (noting native tấn as the real everyday word). Filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Found/fixed a bare-wikilink citation on 公(char).md. No homophone collision.

Next: 公尺.

### 2026-09-11, word 25/246 — [[words/公尺|公尺]]
Never-perfected word. **Found and fixed a real-equivalent-word bug in `korean`**: a comma-joined pair of loanword variants (미터, 메터) → compositional 공척, which conveniently matches this word's own 諺文 exactly, filling entirely-missing `kwin` as true. Expanded a compatibility-ligature `japanese` value (㍍, a single symbol standing for メートル) into actual text. Filled honest compositional `vietnamese: công xích` (noting real everyday mét). Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely. **Found and fixed** a raw-markdown-link citation on 尺(char).md and a missing citation entirely on 公(char).md. No homophone collision.

Next: 公民.

### 2026-09-11, word 26/246 — [[words/公民|公民]]
Never-perfected word. Disambiguated bare 公 to "公 (char)" (words/公.md exists). Fixed unindented `characters:` list, quoted bare `hsk_level`, removed dangling blank `swadesh:`/`aliases:`, merged `## Etymology` into a full `## Notes` section. Found/fixed a bare-wikilink citation (missing ruby, missing comma-space) on 公(char).md. `kwin: true` confirmed exact match, no homophone collision.

Next: 公開.

### 2026-09-11, word 27/246 — [[words/公開|公開]]
Never-perfected word. Disambiguated bare 公. Fixed unspaced cantonese, quoted bare `hsk_level`, removed dangling blank `swadesh:`/`aliases:`, merged `## Etymology` into a full `## Notes` section. **Found and fixed a genuine japanese reading error**: こうくわい (an incorrect archaic-looking rendering not matching 開's own modern on'yomi KAI) → こうかい, the real standard reading. Found/fixed a bare-wikilink citation on 公(char).md. `kwin: false` confirmed, no homophone collision.

Next: 六十.

### 2026-09-11, word 28/246 — [[words/六十|六十]]
Never-perfected word. Disambiguated bare 十 to "十 (char)" (words/十.md exists — confirmed via `ls`). Flattened single-item `japanese`/`vietnamese` lists; replaced native `vietnamese: sáu mươi` with the Sino-Vietnamese compositional "lục thập" (disclosing native sáu mươi as the everyday alternative). Removed duplicate `品詞` key, filled entirely-missing `kwin` (false) and `date-last-perfect`, fixed a broken relative link. **Found and fixed a malformed citation** on 十(char).md's own Words list (was `[[words/六十]] - 60`, a full-path wikilink with a dash-number gloss instead of the standard ruby format). No homophone collision.

Next: 六府.

### 2026-09-11, word 29/246 — [[words/六府|六府]]
Never-perfected word, but otherwise already well-formed. Filled a missing `date-last-perfect` entirely; added `kwin`/homophone verification sentence. `characters:` confirmed correct via `ls`, both character-page citations already present, confirmed 腑 is a genuine alias of 府 (not a bug) and 府's own `stand_in` is [[政府]] (not this word, so no legitimizing note needed), `kwin: false` confirmed, no homophone collision.

Next: 六日.

### 2026-09-11, word 30/246 — [[words/六日|六日]]
Never-perfected word; page previously ended right after a bare `## Notes` heading with no content at all. Flattened single-item `japanese`/`vietnamese` lists; **found and fixed an incomplete/wrong `vietnamese` field** ("sáu," bare "six" with no day-word at all) → honest compositional "lục nhật" (disclosing native mùng sáu as the everyday phrase). Removed duplicate `品詞` key, filled a missing `date-last-perfect` entirely, wrote a full `## Notes` section from scratch clarifying this means "the sixth day of the month" (matching sibling [[十六日]]/[[二十六日]]). Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 六芸.

### 2026-09-11, word 31/246 — [[words/六芸|六芸]]
Never-perfected word; **resolved the long-standing MAJOR FINDING** about two apparently-parallel Six-Arts documentation systems. Investigation showed this was never a real conflict: 六芸.md's own list (礼/音楽/射術/御術/書法/数学) names the six *general arts* — three of which (礼, 音楽, 射術, 御術) already explicitly self-identify in their own prose as "one of the Six Arts (六芸)" — while the count-prefixed cluster (五礼/六楽/五射/五馭/六書/九数) documents each art's own *specific numbered sub-curriculum* one level down, and those five pages already consistently cross-reference each other and 六芸 by name. The two sets are complementary levels of one hierarchy, not competitors. Rewrote 六芸's Notes to explicitly link both levels together for each of the six arts, resolving the apparent disconnect. Also disclosed, rather than silently reconciled, a genuine separate finding along the way: [[六書]]'s own page documents the well-known but historically distinct Han-dynasty "six categories of character formation" theory, not literally "six calligraphic styles" — the vault reuses the same well-attested name for the Six Arts' writing component, a real coincidence of naming rather than an error to fix. Closed up a spaced `mandarin` field, removed duplicate `品詞`, filled a missing `date-last-perfect` entirely, renamed the non-standard `## Definition` heading to `## Notes`. `characters:` confirmed correct via `ls`, both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 共同.

### 2026-09-11, word 32/246 — [[words/共同|共同]]
Never-perfected word. Disambiguated bare 共 to "共 (char)" (words/共.md exists — confirmed via `ls`). Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. Disclosed (rather than silently changed) that Vietnamese `cộng đồng` — the same compositional compound as this word — has narrowed to specifically mean "community" (noun) in modern usage, not the adjectival "common, joint" sense this word documents. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 共和.

### 2026-09-11, word 33/246 — [[words/共和|共和]]
Never-perfected word. **Found and fixed two genuine reading errors**: `cantonese` (gong4 ho2, matching neither constituent's own reading) → compositional gung6 wo4; `korean` (고화, missing a coda entirely) → compositional 공화. Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Found and fixed a missing citation** for bare 共和 on 共(char).md's own Words list (only 共和国 had been cited, not 共和 itself). `kwin: false` confirmed, no homophone collision.

Next: 共産.

### 2026-09-11, word 34/246 — [[words/共産|共産]]
Never-perfected word. Disambiguated bare 共 to "共 (char)" (words/共.md exists). Fixed inline-flow `characters:`/`aliases:` lists, removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. `characters:` (bare 産) confirmed correct via `ls`, both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 兵法.

### 2026-09-11, word 35/246 — [[words/兵法|兵法]]
Never-perfected word. Fixed an unspaced cantonese field, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, merged `## Etymology` and a stray dangling-link note into a full `## Notes` section (honestly disclosing that [[孫子兵法]] has no dedicated page yet, rather than leaving a broken link). `characters:` confirmed correct via `ls` (法 (char) disambiguation necessary), both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 再度.

### 2026-09-11, word 36/246 — [[words/再度|再度]]
Never-perfected word. Trimmed a comma-joined `korean` field (native synonyms 다시/또 moved to prose, kept compositional 재도 alone — which conveniently matches this word's own 諺文 exactly, so `kwin`, entirely missing, was filled in as true). Replaced the native `vietnamese: lại` with the compositional `tái độ` (disclosing native lại as the everyday word). Filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. Added a missing legitimizing note for 再, whose own `stand_in` points to this word. Both character-page citations already present, no homophone collision. **Flagged**: 度(char).md's own `vietnamese` field lists dác/dạc/giạc/đo/đác but is missing the expected độ candidate (the reading actually used compositionally here) — worth checking on 度's own future turn.

Next: 写真.

### 2026-09-11, word 37/246 — [[words/写真|写真]]
Never-perfected word. Filled a blank `pos:` (名詞), fixed inline-flow `characters:`/`aliases:` lists, removed dangling blank `hsk_level:`/`swadesh:`, replaced native `vietnamese: tấm hình` with honest compositional "tả chân" (disclosing it's attested for "realistic depiction" generally, not specifically "photograph," and that tấm hình/ảnh is the everyday word). Filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. **Found and fixed a missing citation** on 真(char).md's own Words list. `characters:` (真 (char) disambiguation) confirmed correct via `ls`, `kwin: false` confirmed, no homophone collision.

Next: 冥王星.

### 2026-09-11, word 38/246 — [[words/冥王星|冥王星]]
Never-perfected word. Filled an entirely-blank `cantonese` field with the compositional ming4 wong4 sing1, removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Found and fixed missing citations** on both 冥(char).md and 星(char).md's own Words lists (only 王(char).md already had it). `characters:` confirmed correct via `ls` (all three disambiguations necessary), `kwin: false` confirmed, no homophone collision.

Next: 冷麺.

### 2026-09-11, word 39/246 — [[words/冷麺|冷麺]]
Never-perfected word. Disambiguated bare 冷/麺 (both words/冷.md and words/麺.md exist — confirmed via `ls`; Etymology prose was already using the disambiguated forms, frontmatter wasn't). Fixed a wrongly-capitalized `vietnamese` field (Lãnh miến → lowercase lãnh miến, a common noun not a proper name), disclosing native mì lạnh as the everyday phrase. Removed dangling blank `hsk_level:`/`swadesh:`, fixed inline-flow `aliases:` list, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 凄惨.

### 2026-09-11, word 40/246 — [[words/凄惨|凄惨]]
Never-perfected word. **Found and fixed a real-equivalent-word bug in `korean`**: 비참한 (a different word built from unrelated characters 悲慘 plus an adjectival suffix) → compositional 처참 (凄's own 처 + 惨's own 참). Disambiguated bare 惨 to "惨 (char)" (words/惨.md exists). Removed dangling blank `hsk_level:`/`swadesh:`, fixed inline-flow `aliases:` list, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 凱旋門.

### 2026-09-11, word 41/246 — [[words/凱旋門|凱旋門]]
Never-perfected word, but otherwise already well-formed (verified 凱's own unusual cantonese hoi2 is genuinely correct, not a corruption). Fixed unindented `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. All three character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 凹凸.

### 2026-09-11, word 42/246 — [[words/凹凸|凹凸]]
Never-perfected word. Fixed a typo ("bumby" → "bumpy," confirmed against both character-page citations' own correct spelling). Fixed a comma-joined `mandarin` field with a typo'd variant (āotū, āotú → just āotū, matching 凸's own stored reading exactly). Filled a blank `pos:` (性詞), fixed inline-flow `characters:`/`aliases:` lists, removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 出版.

### 2026-09-11, word 43/246 — [[words/出版|出版]]
Never-perfected word. **Found and fixed a real `kwin` bug**: stored `true`, but byte-level verification shows own 諺文 춛판 (coda ㅊ) genuinely diverges from own korean 출판 (coda ㄹ) — corrected to `false`. Fixed unindented `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. `characters:` confirmed correct via `ls`, both character-page citations already present, no homophone collision.

Next: 出生率.

### 2026-09-11, word 44/246 — [[words/出生率|出生率]]
Never-perfected word. Filled entirely-missing `kwin` (false, byte-level verified: own 諺文 춛상룯 diverges from own korean 출생률 in all three syllables) and entirely-missing `date-last-perfect`. `characters:` confirmed correct via `ls`, all three character-page citations already present, no homophone collision.

Next: 出血.

### 2026-09-11, word 45/246 — [[words/出血|出血]]
Never-perfected word. Disambiguated bare 血 to "血 (char)" (words/血.md exists — confirmed via `ls`). Fixed unindented `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 出谷記.

### 2026-09-11, word 46/246 — [[words/出谷記|出谷記]]
Never-perfected word (Book of Exodus, historical Chinese Catholic name). Reordered `characters:` list to match the word's own character order (was 出/記/谷, corrected to 出/谷/記) and disambiguated bare 谷. Removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch explaining the Catholic/Protestant naming distinction, and gave proper heading/context/translation to a bare, unlabeled "## 20" section that was actually a condensed classical-style summary of the Ten Commandments. **Deliberately did not "correct" the mandarin/cantonese/japanese/korean/vietnamese fields** despite each one naming the real-world Exodus by its OWN language's common title rather than a compositional Dan'a'yo transliteration — this matches established vault practice for proper nouns/titles (e.g. [[冥王星]]), not the real-equivalent-word bug pattern seen on common vocabulary. **Found and fixed a missing citation** on 谷(char).md's own Words list. No homophone collision.

Next: 出身.

### 2026-09-11, word 47/246 — [[words/出身|出身]]
Never-perfected word. **Found and fixed a real `kwin` bug**: stored `true`, but byte-level verification shows own 諺文 춛신 genuinely diverges from own korean 출신 in the first syllable's coda — corrected to `false`. Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. `characters:` confirmed correct via `ls`, both character-page citations already present, no homophone collision.

Next: 刀剣.

### 2026-09-11, word 48/246 — [[words/刀剣|刀剣]]
Never-perfected word. Filled an entirely-blank `cantonese` field with the compositional dou1 gim3. Removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, replaced casual stand-in prose with the standard legitimizing-note phrasing (刀's own `stand_in` confirmed pointing to this word), merged `## Etymology` into a full `## Notes` section. **Found and fixed a bare-wikilink citation** on 刀.md's own Words list (missing ruby and the "(stand-in for 刀)" annotation). `characters:` confirmed correct, `kwin: false` confirmed, no homophone collision.

Next: 分子.

### 2026-09-11, word 49/246 — [[words/分子|分子]]
Never-perfected word. Disambiguated bare 分 to "分 (char)" (words/分.md exists — confirmed via `ls`). Fixed a semicolon-joined `vietnamese` field into a proper YAML list (phân tử/phần tử, two distinct tonal words for the two distinct senses — molecule vs. numerator). Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Found and fixed missing/malformed citations**: 分子 was missing entirely from 分(char).md's own Words list, and was a bare dash-gloss (no ruby) on 子.md's. `kwin: false` confirmed, no homophone collision.

Next: 判別式.

### 2026-09-11, word 50/246 — [[words/判別式|判別式]]
Never-perfected word. Fixed inline-flow `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section — confirmed `vietnamese: biệt thức` is a genuine shortened standard math term, not an error. **Found and fixed a missing citation** on 式.md's own Words list (only 判.md and 別(char).md already had it). `characters:` confirmed correct via `ls`, `kwin: false` confirmed, no homophone collision.

Next: 判断.

### 2026-09-11, word 51/246 — [[words/判断|判断]]
Never-perfected word. Fixed inline-flow `characters:`/`aliases:` lists, quoted bare `hsk_level`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Added a missing legitimizing note for 判, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 利潤.

### 2026-09-11, word 52/246 — [[words/利潤|利潤]]
Never-perfected word. Disambiguated bare 潤 to "潤 (char)" (words/潤.md exists — confirmed via `ls`; Etymology prose was already using the disambiguated form). Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Added a missing legitimizing note for 利, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 利率.

### 2026-09-11, word 53/246 — [[words/利率|利率]]
Never-perfected word. Filled entirely-missing `kwin` (false, byte-level verified) and entirely-missing `date-last-perfect`. `characters:` confirmed correct via `ls`, both character-page citations already present, no homophone collision.

Next: 制約.

### 2026-09-11, word 54/246 — [[words/制約|制約]]
Never-perfected word. Filled a missing `date-last-perfect` entirely; added `kwin`/homophone verification sentence. **Found and fixed stale prose**: the Notes claimed [[制限]] and [[約束]] were "not yet created," but both now exist as real vault pages — converted to proper wikilinks. `characters:` confirmed correct via `ls`, both character-page citations already present, `kwin: true` confirmed exact match, no homophone collision.

Next: 刹那.

### 2026-09-11, word 55/246 — [[words/刹那|刹那]]
Never-perfected word. Disambiguated bare 那 to "那 (char)" (words/那.md exists). **Found and fixed a real `kwin` bug**: stored `true`, but byte-level verification shows own 諺文 찯나 genuinely diverges from own korean 찰나 in the first syllable's coda — corrected to `false`. Fixed a comma-joined `mandarin` field into a proper YAML list (both readings genuinely attested, kept both). Filled an entirely-blank `cantonese` field, quoted bare `hsk_level`, wrote a `## Notes` section from scratch. Added a missing legitimizing note for 刹, whose own `stand_in` points to this word. Both character-page citations already present, no homophone collision.

Next: 刺激.

### 2026-09-11, word 56/246 — [[words/刺激|刺激]]
Never-perfected word. Disambiguated bare 刺 to "刺 (char)" (words/刺.md exists). Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section — confirmed Vietnamese `kích thích`'s reversed syllable order relative to the Chinese original is a genuine, common Sino-Vietnamese pattern, not an error. Added a missing legitimizing note for 激, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 前兆.

### 2026-09-11, word 57/246 — [[words/前兆|前兆]]
Never-perfected word. Fixed an unspaced cantonese field, replaced the native `vietnamese: điềm` with the directly-attested Sino-Vietnamese compositional "tiền triệu" (disclosing native điềm as the everyday alternative). Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. Added a missing legitimizing note for 兆, whose own `stand_in` points to this word. **Found and fixed a raw-markdown-link-instead-of-wikilink self-citation** on 兆.md's own Words list. `kwin: false` confirmed, no homophone collision.

Next: 前提.

### 2026-09-11, word 58/246 — [[words/前提|前提]]
Never-perfected word. Removed duplicate `品詞` key, flattened single-item `japanese`/`vietnamese` lists, fixed broken relative links, filled a missing `date-last-perfect` entirely. `characters:` confirmed correct via `ls`, both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 文学者.

### 2026-09-11, word 59/246 — [[words/文学者|文学者]]
Never-perfected word. **Found and fixed a real content bug affecting three fields at once**: `mandarin`, `cantonese`, and `korean` had all been filled with the reading of the alias 文学家 (using 家, not this word's own 者) rather than 文学者's own characters — corrected to wénxuézhě, man4 hok6 ze2, and 문학자 (trimmed from a comma-joined crammed field). Filled an entirely-blank `vietnamese` field with honest compositional "văn học giả." Disambiguated bare 者 to "者 (char)," filled entirely-missing `kwin`/`date-last-perfect`, wrote a `## Notes` section from scratch. All three character-page citations already present, no homophone collision.

Next: 文明.

### 2026-09-11, word 60/246 — [[words/文明|文明]]
Never-perfected word, but otherwise already well-formed. Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. `characters:` confirmed correct via `ls`, both character-page citations already present, `kwin: true` confirmed exact match, no homophone collision.

Next: 超.

The prior log (4397 iterations, 2026-08-05 through 2026-09-11) is archived as `Word Perfecting 5.md.zip`, following the same rollover convention as archives 2–4.

**The 246-word backlog** (confirmed via `grep -L "^date-last-perfect:" words/*.md`, LC_ALL=C sorted) is tracked in the memory file `project_word_sweep_position.md`, with a checked-off copy maintained there as the authoritative remaining-work list. This log records one entry per completed word going forward, same format as before.

---
