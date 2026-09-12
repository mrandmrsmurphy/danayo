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

### 2026-09-11, word 61/246 — [[words/超|超]]
Never-perfected word; page had multiple structural problems. Fixed `characters:` stored as a bare scalar string instead of a list; fixed `vietnamese: null` (a literal YAML null) → filled with compositional siêu; filled a missing `japanese` field entirely (ちょう); filled entirely-missing `kwin` (false) and `date-last-perfect`; wrote a `## Notes` section from scratch (heading existed with zero content below it). Added a missing self-referential legitimizing note (超(char)'s own `stand_in` points to itself). Confirmed the reciprocal homophone callouts with [[島]] and [[倒]] were already correctly present on both those pages (this closes out the three-way group first flagged back when 倒 and 島 were perfected). `characters:` confirmed correct via `ls`, citation already present.

Next: 超越.

### 2026-09-11, word 62/246 — [[words/超越|超越]]
Never-perfected word. Disambiguated bare 超/越 (both words/超.md and words/越.md exist — confirmed via `ls`; Etymology prose was already using the disambiguated forms). **Found and fixed a japanese reading error**: てうゑつ (matching neither constituent's own on'yomi, no attested modern reading) → ちょうえつ, the genuine standard reading. Quoted bare `hsk_level`, removed dangling blank `swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 越南.

### 2026-09-11, word 63/246 — [[words/越南|越南]]
Never-perfected word. Fixed comma-joined `japanese`/`korean` fields into proper YAML lists (kept all attested candidates — Sino-xenic compound, modern phonetic transliteration, and Korean orthographic/transliteration variants — rather than discarding any without verification). Filled entirely-missing `kwin` (false) and `date-last-perfect`. Converted a raw-markdown-link reference to [[越南人]] into a proper wikilink, folding the stray "See/See also" bullet list into a full `## Notes` section. `characters:` confirmed correct via `ls`, both character-page citations already present, no homophone collision.

Next: 越南語.

### 2026-09-11, word 64/246 — [[words/越南語|越南語]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch, noting that Japanese/Korean use the modern phonetic-transliteration-based names (paralleling the same split already documented on [[越南]]) rather than a literal compositional calque. `characters:` confirmed correct via `ls`, all three character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 越境.

### 2026-09-11, word 65/246 — [[words/越境|越境]]
Never-perfected word. **Found and fixed a real `kwin` bug**: stored `true`, but byte-level verification shows own 諺文 웓경 genuinely diverges from own korean 월경 in the first syllable — corrected to `false`. Filled a blank `pos:` (事詞) and a missing `vietnamese` field with honest compositional "việt cảnh" (disclosing native vượt biên as the everyday phrase for illegal border crossing). Fixed inline-flow `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, merged `## Etymology` into a full `## Notes` section. Both character-page citations already present, no homophone collision.

Next: 越盟.

### 2026-09-11, word 66/246 — [[words/越盟|越盟]]
Never-perfected word. Filled entirely-blank `mandarin`/`cantonese`/`japanese`/`korean` fields with compositional readings — `korean: 월맹` is also a genuine historical South Korean term for North Vietnam/the Viet Minh. Fixed a typo ("aliance" → "alliance"), fixed inline-flow `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled entirely-missing `kwin` (false) and `date-last-perfect`, merged `## Etymology` into a full `## Notes` section. Both character-page citations already present, no homophone collision.

Next: 足指.

### 2026-09-11, word 67/246 — [[words/足指|足指]]
Never-perfected word. Filled entirely-blank `cantonese`/`korean`/`vietnamese` fields with compositional readings, disclosing that each daughter language's real everyday word for "toe" is instead a native "foot-finger" compound (matching Japanese あしゆび's own pattern). Fixed inline-flow `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled entirely-missing `kwin` (false) and `date-last-perfect`, wrote a `## Notes` section from scratch. Both character-page citations already present, no homophone collision.

Next: 足球.

### 2026-09-11, word 68/246 — [[words/足球|足球]]
Never-perfected word. Filled entirely-blank `japanese`/`korean`/`vietnamese` fields with compositional readings — `vietnamese: túc cầu` is a real historically-attested term; `korean: 족구` coincidentally names a real, different Korean sport ("foot volleyball"), disclosed honestly, since Korean's actual soccer word 축구 derives from [[蹴球]] instead. Fixed inline-flow `characters:` list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled entirely-missing `kwin` (false, byte-level verified) and `date-last-perfect`, integrated a stray unformatted note into a full `## Notes` section. Both character-page citations already present, no homophone collision.

Next: 足裏.

### 2026-09-11, word 69/246 — [[words/足裏|足裏]]
Never-perfected word. Disambiguated bare 足 to "足 (char)" (words/足.md exists). **Found and fixed a real content bug**: `mandarin` had been stored as jiǎodǐ, the reading of the entirely different compound 腳底 (different characters), not 足裏's own — corrected to compositional zúlǐ. **Found and fixed a bad aliases entry**: 腳底/脚底/腳掌/脚掌 (real Mandarin synonyms using different characters, no dedicated pages) had been listed as `aliases` of 足裏 itself — removed, disclosed as real synonyms in prose instead. Filled a missing `cantonese`/`vietnamese` with compositional readings, fixed a comma-joined `japanese` field into a proper list (both readings genuinely attested). Once `korean` was corrected to its own compositional 족리 (rather than the native 발바닥), it turned out to match this word's own 諺文 exactly — `kwin`, previously false, is now true. Filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Flagged**: 裏.md's own "Common Compounds" table duplicates several citations already in its formal `## Words` list (including this word) — a documentation redundancy, not urgent, noted for later.

Next: 跆拳道.

### 2026-09-11, word 70/246 — [[words/跆拳道|跆拳道]]
Never-perfected word. Fixed a typo ("taekwando" → "taekwondo," found in both the `english` field and a matching citation on 道(char).md). Filled an entirely-blank `vietnamese` field with the direct loanword "taekwondo" (matching Japanese テコンドー's own loanword pattern). Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. **Found and fixed a missing citation** on 跆.md's own Words list. `characters:` confirmed correct via `ls`, `kwin: false` confirmed, no homophone collision.

Next: 跋扈.

### 2026-09-11, word 71/246 — [[words/跋扈|跋扈]]
Never-perfected word. Filled a missing `vietnamese` field with honest compositional "bạt hỗ" and a missing `date-last-perfect` entirely. **Found and fixed a missing `#cranberry` tag**: both 跋 and 扈's own `stand_in` fields point to this word (transitivity A=B=AB confirmed), a genuine cranberry case that had gone untagged — added the tag and a closing note explaining it. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 距離.

### 2026-09-11, word 72/246 — [[words/距離|距離]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. Added a missing legitimizing note for 距, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: false` confirmed, no homophone collision.

Next: 跨.

The prior log (4397 iterations, 2026-08-05 through 2026-09-11) is archived as `Word Perfecting 5.md.zip`, following the same rollover convention as archives 2–4.

**The 246-word backlog** (confirmed via `grep -L "^date-last-perfect:" words/*.md`, LC_ALL=C sorted) is tracked in the memory file `project_word_sweep_position.md`, with a checked-off copy maintained there as the authoritative remaining-work list. This log records one entry per completed word going forward, same format as before.

---

### 2026-09-11, word 73/246 — [[words/跨|跨]]
Never-perfected word. Filled a missing `date-last-perfect` entirely, wrote a `## Notes` section from scratch. Added a missing legitimizing note for 跨 (char), whose own `stand_in` points to this exact word (itself). **Found and fixed a genuine word-to-word homophone with [[誇]]** ("boast, brag, exaggerate," previously perfected 2026-08-10 with no callout) — added reciprocal `>[!warning] Homophones` callouts and cross-linking prose to both pages. Character-page citation already present in correct self-standing format, `kwin: false` confirmed via byte-level comparison (콰 U+CF70 vs 과 U+ACFC).

Next: 跪.

### 2026-09-11, word 74/246 — [[words/跪|跪]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `pos`/`kwin`/`date-last-perfect`, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Added a missing legitimizing note for 跪 (char), whose own `stand_in` points to this exact word (itself). **Found and fixed two bugs on 跪(char).md**: a malformed `japanese_native` field (an orphan list item dangling off a scalar value, merged into a proper two-item list ひざまず/ひざまずく) and an entirely missing `## Words` section (added the citation). `kwin: false` confirmed via byte-level comparison (퀘 U+D018 vs 궤 U+ADA4), no homophone collision.

Next: 跳舞.

### 2026-09-11, word 75/246 — [[words/跳舞|跳舞]]
Never-perfected word. Filled entirely-blank `japanese`/`korean`/`vietnamese`, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section. Vietnamese "khiêu vũ" is a directly attested loanword; Japanese とうぶ/korean 도무 are honest compositional readings (とうぶ independently attested via 跳舞病). **Found and fixed a missing citation** on 跳.md's own Words list. Noted 舞's `stand_in` legitimizes this word, while 跳's own `stand_in` is 跳躍 instead. `kwin: false` confirmed, no homophone collision.

Next: 跳蚤.

### 2026-09-11, word 76/246 — [[words/跳蚤|跳蚤]]
Never-perfected word. **Found and fixed a genuine real-equivalent-instead-of-own-reading bug across all three of japanese/korean/vietnamese**: stored values were the everyday native terms for "flea" (のみ/ノミ, 벼룩, con bọ chét) plus a garbled korean value ("조조, 벼룩" — a doubled/malformed compositional attempt mashed with the native word) instead of the word's own honest compositional readings. Fixed to とうそう/도조/khiêu tảo (跳's own TOU/도/khiêu + 蚤's own SOU/조/tảo). Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section from scratch. Citation already present on 蚤.md, `kwin: false` confirmed, no homophone collision. Noted 蚤's `stand_in` legitimizes this word, while 跳's own `stand_in` is 跳躍 instead.

Next: 跳躍.

### 2026-09-11, word 77/246 — [[words/跳躍|跳躍]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "khiêu dược," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section from scratch. **Found and fixed a missing `#cranberry` tag**: both 跳 and 躍's own `stand_in` fields point to this word (transitivity A=B=AB confirmed) — added the tag and a closing note. **Also fixed a bare, un-ruby-formatted citation** on 跳.md's own Words list. 躍.md's own citation was already correctly ruby-formatted. `kwin: false` confirmed, no homophone collision.

Next: 踊躍.

### 2026-09-11, word 78/246 — [[words/踊躍|踊躍]]
Never-perfected word. Filled an entirely-missing `vietnamese` field with honest compositional "dũng dược," filled missing `date-last-perfect`, extended the existing rich `## Notes` prose with the kwin/homophone/legitimizing-note sentences. `kwin: true` confirmed via byte-level comparison (exact match). Citations already correctly present on both 踊.md and 躍.md. Noted 踊's `stand_in` legitimizes this word, while 躍's own `stand_in` is 跳躍 instead (no cranberry transitivity here).

Next: 蹲.

### 2026-09-11, word 79/246 — [[words/蹲|蹲]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a malformed `english:` list indentation, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `kwin`/`date-last-perfect`. Added a missing legitimizing note for 蹲 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed via byte-level comparison (존 U+C874 vs 준 U+C900). Citation already correctly present on the character page. Noted 注音 ㄐㄛㄋ is shared with 尊/存 but neither has its own word page, so no genuine word-to-word homophone.

Next: 蹴鞠.

### 2026-09-11, word 80/246 — [[words/蹴鞠|蹴鞠]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "xúc cúc," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section explaining the cognate-game proper-noun exception (Chinese cuju/Japanese kemari/Korean chukguk are each a real attested name for that culture's own historical game, not translations of each other). **Found and fixed a missing citation** on 鞠.md's own Words list. `kwin: true` confirmed, no homophone collision.

Next: 身体.

### 2026-09-11, word 81/246 — [[words/身体|身体]]
Never-perfected word. Filled a blank `pos: 名詞`, removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section from scratch. Confirmed `身體` alias is a legitimate traditional-character spelling variant (体→體), not a bad-aliases-entry bug. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Noted 身's `stand_in` legitimizes this word, while 体's own `stand_in` is 体系 instead.

Next: 車庫.

### 2026-09-11, word 82/246 — [[words/車庫|車庫]]
Never-perfected word. Fixed `characters:` disambiguation (bare 車 → "車 (char)," since [[車]] has its own word page). **Found and fixed a real-equivalent-instead-of-own-reading bug**: vietnamese held the everyday phrase "nhà để ô tô, ga ra" instead of the honest compositional "xa kho." **Found and removed a bad-aliases-entry bug**: `库车` is the unrelated real place name Kùchē/Kuqa, not a spelling variant. Removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 軌道.

### 2026-09-11, word 83/246 — [[words/軌道|軌道]]
Never-perfected word. Fixed `characters:` disambiguation (bare 軌/道 → "軌 (char)"/"道 (char)," since both have their own word pages), fixed a mandarin typo (guǐdà → guǐdào), removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed missing citations** on both 軌(char).md's and 道(char).md's own Words lists. `kwin: false` confirmed, no homophone collision. Neither constituent is legitimized by this compound — both already stand alone as words with self-referential `stand_in`.

Next: 軍人.

### 2026-09-11, word 84/246 — [[words/軍人|軍人]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed missing/bare citations**: 軍.md's own Words list was missing 軍人 entirely (added); 人(char).md had it in bare numbered-list format (upgraded to ruby, broader section reorg still flagged/deferred). `kwin: false` confirmed, no homophone collision. 軍's own `stand_in` is 軍隊, not this word.

Next: 軍艦.

### 2026-09-11, word 85/246 — [[words/軍艦|軍艦]]
Never-perfected word. Fixed `characters:` unindented list, removed dangling blank `hsk_level:`/`swadesh:`, fixed a malformed inline `aliases:` into a proper list, filled missing `date-last-perfect`, folded a stray floating comment ("narrower than 艦船") into a proper `## Notes` section as cited prose. Confirmed `军舰` alias is a legitimate simplified-character spelling variant, not a bug. Citation already correctly present on 艦.md, `kwin: true` confirmed, no homophone collision.

Next: 軍隊.

### 2026-09-11, word 86/246 — [[words/軍隊|軍隊]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 軍, whose own `stand_in` points to this exact word.

Next: 軟禁.

### 2026-09-11, word 87/246 — [[words/軟禁|軟禁]]
Never-perfected word. Filled missing `kwin`/`date-last-perfect`, extended the existing brief Notes with the standard readings/kwin/homophone verification sentences. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Neither constituent's `stand_in` points to this word (軟→柔軟, 禁→禁止).

Next: 転載.

### 2026-09-11, word 88/246 — [[words/転載|転載]]
Never-perfected word. Fixed `characters:` disambiguation (bare 載 → "載 (char)," since [[載]] has its own word page), fixed a malformed inline `aliases:` into a proper list (轉載/转载, legitimate trad/simplified variants). **Found and fixed a genuinely blank `vietnamese` field on 転.md itself** — filled with "chuyển," a well-attested Sino-Vietnamese reading for 轉/転's traditional form — enabling a real compositional/attested word vietnamese: "chuyển tải" on this page. Also fixed a bare, un-ruby-formatted citation on 転.md's own Words list. Removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Citation on 載(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 軸.

### 2026-09-11, word 89/246 — [[words/軸|軸]]
Never-perfected word. Filled a `vietnamese: null` with the character's own attested "trục," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`kwin`/`date-last-perfect`. Added a missing legitimizing note for 軸 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed. Noted 注音 ㄉㄨㄎ is shared with 逐 but it has no dedicated word page, so no genuine homophone.

Next: 軽罪.

### 2026-09-11, word 90/246 — [[words/軽罪|軽罪]]
Never-perfected word. Fixed `characters:` unindented list, filled a blank `vietnamese` with honest compositional "khinh tội," fixed a malformed inline `aliases:` into a proper list (輕罪/轻罪, legitimate trad/simplified variants), removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 載.

### 2026-09-11, word 91/246 — [[words/載|載]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "tải," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes," filled missing `pos`/`date-last-perfect`, wrote its content from scratch. Added a missing legitimizing note for 載 (char), whose own `stand_in` points to this exact word (itself). **Found a genuine three-way homophone group with [[哉]] and [[在]]** (both already perfected, already cross-linked to each other, but neither mentioned 載) — added 載 as the missing third member to both existing callouts and wrote a full reciprocal callout on 載's own page. `kwin: true` confirmed.

Next: 輔弼.

### 2026-09-11, word 92/246 — [[words/輔弼|輔弼]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "phụ bật," folded a stray floating comment ("rare") into proper `## Etymology`/`## Notes` prose, removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 弼, whose own `stand_in` points to this exact word; noted 輔's own `stand_in` is 輔佐 instead.

Next: 輩.

### 2026-09-11, word 93/246 — [[words/輩|輩]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level, wrong position) into a properly-placed "## Notes," filled missing `pos`/`date-last-perfect`. **Found and fixed an entirely missing `## Words` section** on 輩(char).md — added the self-standing citation. Added a missing legitimizing note for 輩 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed. Noted 注音 ㄈㄛㄧ is shared with 徘/佩/培 but none has its own word page, so no genuine homophone.

Next: 輪.

### 2026-09-11, word 94/246 — [[words/輪|輪]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "luân" (as in luân hồi/輪回), fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`date-last-perfect`. Added a missing legitimizing note for 輪 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed. Citation already correctly present. Noted 注音 ㄌㄨㄋ is shared with 倫 but it has no dedicated word page, so no genuine homophone.

Next: 輪郭.

### 2026-09-11, word 95/246 — [[words/輪郭|輪郭]]
Never-perfected word. **Found and fixed a wrong-dialect bug**: korean held the South Korean 두음법칙-shifted form 윤곽 instead of this vault's standing North Korean/문화어 convention 륜곽 (matching 輪's own stored 륜 directly) — corrected the field and the Notes prose that had been describing the South Korean shift as if it were the vault's own value. Filled a missing `vietnamese` with honest compositional "luân quách," filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 輸血.

### 2026-09-11, word 96/246 — [[words/輸血|輸血]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, filled a blank `pos: 性詞`, filled a blank `vietnamese` with honest compositional "thâu huyết," fixed a malformed inline `aliases:` into a proper list (输血, legitimate simplified variant), removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 輿.

### 2026-09-11, word 97/246 — [[words/輿|輿]]
Never-perfected word. Filled missing `kwin`/`date-last-perfect`, extended the existing Notes with the standard readings/kwin/legitimizing-note sentences. Confirmed the existing three-way homophone callout with [[魚]] and [[与]] was already correctly reciprocal on all three pages (no fix needed). `kwin: false` confirmed via byte comparison. Citation already correctly present on the character page.

Next: 辛苦.

### 2026-09-11, word 98/246 — [[words/辛苦|辛苦]]
Never-perfected word. Fixed `characters:` disambiguation (bare 苦 → "苦 (char)," since [[苦]] has its own word page). **Found and fixed a real-equivalent-instead-of-own-reading bug**: korean held 고생 (苦生, an unrelated hanja compound), replaced with honest compositional 신고. Filled a blank `vietnamese` with the directly-attested Sino-Vietnamese "tân khổ." **Found and fixed missing citations** on both 辛.md and 苦(char).md's own Words lists (辛苦 was absent from each). Filled missing `date-last-perfect`, wrote a `## Notes` section. `kwin: false` confirmed, no homophone collision. Neither constituent's `stand_in` points to this word.

Next: 辞令.

### 2026-09-11, word 99/246 — [[words/辞令|辞令]]
Never-perfected word. Fixed `characters:` disambiguation (bare 令 → "令 (char)," since [[令]] has its own word page). **Found and fixed a genuinely missing "lệnh" candidate on 令(char).md's own `vietnamese` field** (only rarer variants lanh/liệng/loanh had been listed; "lệnh" is the standard reading used elsewhere, e.g. 命令's "mệnh lệnh"). Filled blank `cantonese`/`vietnamese`, fixed a malformed inline `aliases:` (辭令, legitimate traditional variant), folded a stray floating comment ("we broaden this...") into proper Etymology/Notes prose, filled missing `date-last-perfect`. **Found and fixed a missing citation** on 令(char).md's own Words list. Citation on 辞.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辞任.

### 2026-09-11, word 100/246 — [[words/辞任|辞任]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating alias line ("辭任") into a proper `aliases:` field, filled a blank `vietnamese` with the directly-attested "từ nhiệm," filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 辞.md's own Words list. Citation on 任.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辞去.

### 2026-09-11, word 101/246 — [[words/辞去|辞去]]
Never-perfected word. Fixed `characters:` unindented list, filled a blank `vietnamese` with honest compositional "từ khứ," fixed a malformed inline `aliases:` into a proper list (辭去, legitimate traditional variant), removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辞退.

### 2026-09-11, word 102/246 — [[words/辞退|辞退]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating alias line ("辭退") into a proper `aliases:` field, filled a blank `vietnamese` with the directly-attested "từ thoái," filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辣.

### 2026-09-11, word 103/246 — [[words/辣|辣]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`date-last-perfect`. **Found and fixed a genuine `kwin` miscalculation on 辣(char).md itself**: byte-level comparison shows Dan'a'yo 랃 (U+B783) and Sino-Korean 랄 (U+B784) are visually near-identical but genuinely different Hangul syllables — corrected `kwin: true` → `false` on both pages (same divergence-bug class as the earlier 읫/의 finding). Added a missing legitimizing note for 辣 (char), whose own `stand_in` points to this exact word (itself). Citation already correctly present.

Next: 辦公.

### 2026-09-11, word 104/246 — [[words/辦公|辦公]]
Never-perfected word. Filled blank `japanese`/`vietnamese` with honest compositional べんこう/biện công, removed dangling blank `swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 公(char).md's own Words list. Citation on 辦.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辦公室.

### 2026-09-11, word 105/246 — [[words/辦公室|辦公室]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, **found and fixed a real-equivalent-instead-of-own-reading bug on japanese** (オフィス, the English loanword, replaced with honest compositional べんこうしつ), filled a blank `vietnamese` with honest compositional "biện công thất." **Found and removed a bad-aliases-entry**: 事務室 is a genuinely different compound, not a spelling variant. Folded a stray floating comment (building-vs-room distinction, referencing 事務所) into proper Notes prose. Removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`. **Found and fixed a missing citation** on 公(char).md's own Words list. Citations on 辦.md and 室.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辦理.

### 2026-09-11, word 106/246 — [[words/辦理|辦理]]
Never-perfected word. Filled a blank `pos: 実詞`, filled blank `japanese`/`vietnamese` with honest compositional べんり/biện lý (each a disclosed coincidental homophone of an unrelated real word — Japanese 便利, Vietnamese's old "public prosecutor" sense), removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 理.md's own Words list. Citation on 辦.md already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 辦, whose own `stand_in` points to this exact word; noted 理's own `stand_in` is 理由 instead.

Next: 辰月.

### 2026-09-11, word 107/246 — [[words/辰月|辰月]]
Never-perfected word. **Found and fixed a duplicate `pos`/`品詞` key bug** (removed the redundant `品詞`). **Found and fixed an entirely missing `## Words` section** on 辰.md (whose own `stand_in` is the proper-noun-only marker 名専字). Filled missing `date-last-perfect`, extended the Notes with readings/kwin/homophone verification. Citation on 月(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 農村.

### 2026-09-11, word 108/246 — [[words/農村|農村]]
Never-perfected word. Fixed `characters:`/`aliases:` formatting, removed dangling blank `swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing "(stand-in for 村)" annotation** on 村.md's own citation — 村's `stand_in` points to this exact word. `kwin: true` confirmed, no homophone collision. Noted 農's own `stand_in` is 農業 instead.

Next: 農業.

### 2026-09-11, word 109/246 — [[words/農業|農業]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, folded a stray floating comment ("Synonymous with 農耕") into proper Notes prose. Filled missing `date-last-perfect`. **Found and fixed a missing citation** on 業(char).md's own Words list. Citation on 農.md already correctly present, `kwin: true` confirmed, no homophone collision. Added a missing legitimizing note for 農, whose own `stand_in` points to this exact word.

Next: 農耕.

### 2026-09-11, word 110/246 — [[words/農耕|農耕]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating comment ("Synonymous with 農業") into proper Notes prose, filled a blank `vietnamese` with honest compositional "nông canh," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`. **Found and fixed a missing citation** on 耕.md's own Words list. Citation on 農.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 辺境.

### 2026-09-11, word 111/246 — [[words/辺境|辺境]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Fixed a missing quote mark on 辺.md's own citation. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Neither constituent's `stand_in` points to this word.

Next: 辺界.

### 2026-09-11, word 112/246 — [[words/辺界|辺界]]
Never-perfected word. **Found and fixed a wrong-compound reading bug on `japanese`**: へんきょう actually belongs to the unrelated (though similar-meaning) compound [[辺境]], not this word — corrected to honest compositional へんかい. **Found and removed a bad-aliases-entry**: `辺境` is that same genuinely different compound (different second character), not a spelling variant; kept the legitimate traditional variant `邊界`. Fixed `characters:` unindented list, removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 辺, whose own `stand_in` points to this exact word.

Next: 近処.

### 2026-09-11, word 113/246 — [[words/近処|近処]]
Never-perfected word. **Found and fixed a real-equivalent-instead-of-own-reading bug on `japanese`**: きんじょ is actually the reading of the different word 近所 (所, not 処), corrected to honest compositional きんしょ. Filled a blank `vietnamese` with honest compositional "cận xử." Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating alias-candidates line into a proper `aliases:` field, keeping the legitimate trad/simplified variants (近處/近处) and **excluding 近所** (a genuinely different compound coincidentally similar in meaning). Filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 近来.

### 2026-09-11, word 114/246 — [[words/近来|近来]]
Never-perfected word. **Found and fixed a real-equivalent-instead-of-own-reading bug on `korean`**: a garbled multi-value string "근래, 요사이, 요즈음" mashed the honest compositional reading with two unrelated native words for "recently" — trimmed to just 근래. Filled a blank `vietnamese` with honest compositional "cận lai." Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating alias line ("近來") into a proper `aliases:` field, filled missing `kwin`/`date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 返還.

### 2026-09-11, word 115/246 — [[words/返還|返還]]
Never-perfected word. Filled missing `date-last-perfect`, extended the existing Notes with readings/kwin/homophone verification. **Found and fixed an entirely missing `## Words` section** on 還.md — added both its own stand-in citation ([[送還]]) and this word's citation. Citation on 返.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 迦克敦.

### 2026-09-11, word 116/246 — [[words/迦克敦|迦克敦]]
Never-perfected word (proper noun — Chalcedon). Filled a missing `vietnamese` with "Canxêđoan," that language's own real attested name for the place (via French "Chalcédoine"), following this vault's proper-noun/named-referent convention rather than a compositional transliteration (cf. 冥王星, 出谷記). Filled missing `date-last-perfect`, extended the Notes. Both character-page citations (克, 敦) already correctly present, `kwin: false` confirmed, no homophone collision. Confirmed 迦 genuinely still lacks a character file (already correctly flagged in the existing Notes).

Next: 迫害.

### 2026-09-11, word 117/246 — [[words/迫害|迫害]]
Never-perfected word. Filled a blank `vietnamese` with the directly-attested "bách hại," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: true` confirmed, no homophone collision.

Next: 迷.

### 2026-09-11, word 118/246 — [[words/迷|迷]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "me," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`kwin`/`date-last-perfect`. Added a missing legitimizing note for 迷 (char), whose own `stand_in` points to this exact word (itself). Confirmed the existing three-way homophone callout with [[米]] and [[謎]] was already correctly reciprocal on all three pages (no fix needed). `kwin: false` confirmed.

Next: 追.

### 2026-09-11, word 119/246 — [[words/追|追]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "truy," fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `pos`/`kwin`/`date-last-perfect`, wrote a `## Notes` section from scratch (no prior Notes at all). **Found and fixed a missing "(stand-in for 追)" annotation** on 追(char).md's own ruby-formatted citation. `kwin: false` confirmed, no homophone collision.

Next: 追求.

### 2026-09-11, word 120/246 — [[words/追求|追求]]
Never-perfected word. **Found and fixed a duplicate `pos`/`品詞` key bug** (removed the redundant `品詞`), cleared blank empty-string `vietnamese: ""`/`swadesh: ""` placeholders and filled vietnamese with the directly-attested "truy cầu," filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 追随.

### 2026-09-11, word 121/246 — [[words/追随|追随]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "truy tuỳ," removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 退.

### 2026-09-11, word 122/246 — [[words/退|退]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "thoái," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`kwin`/`date-last-perfect`. Added a missing legitimizing note for 退 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed. Noted 注音 ㄊㄧㄜ is shared with 腿 but it has no dedicated word page, so no genuine homophone.

Next: 送球.

### 2026-09-11, word 123/246 — [[words/送球|送球]]
Never-perfected word. **Found and fixed a wrong-compound reading bug on `mandarin`/`cantonese`**: shǒuqiú/sau2 kau4 actually belong to the unrelated (same-sport) compound 手球, corrected to honest compositional sòngqiú/sung3 kau4. **Found and removed a bad-aliases-entry**: `手球` is that same genuinely different compound, not a spelling variant. Filled a blank `pos: 名詞`/`vietnamese` (honest compositional "tống cầu"), removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 逃亡.

### 2026-09-11, word 124/246 — [[words/逃亡|逃亡]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 逃避.

### 2026-09-11, word 125/246 — [[words/逃避|逃避]]
Never-perfected word. Fixed `characters:` disambiguation (bare 避 → "避 (char)," since [[避]] has its own word page). Filled a blank `vietnamese` with honest compositional "đào tị," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 逃, whose own `stand_in` points to this exact word.

Next: 逆.

### 2026-09-11, word 126/246 — [[words/逆|逆]]
Never-perfected word. **Found and fixed a malformed `vietnamese` field on both this page and 逆(char).md itself**: all five readings had been mashed into a single comma-separated string inside one list item, split into a proper five-item list on both pages. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes." Filled missing `pos`/`kwin`/`date-last-perfect`. Added a missing legitimizing note for 逆 (char), whose own `stand_in` points to this exact word (itself). Confirmed the existing "[叛]" cross-reference correctly links to 反(char).md per the vault's documented 叛→反 merge decision. `kwin: false` confirmed.

Next: 逆数.

### 2026-09-11, word 127/246 — [[words/逆数|逆数]]
Never-perfected word. **Found and fixed a wrong-compound reading bug on `mandarin`/`cantonese`**: dàoshǔ/dou3 sou2 actually belong to the unrelated compound 倒數/倒数, corrected to honest compositional nìshù/jik6 sou2. **Found and removed a bad-aliases-entry**: `倒數`/`倒数` is that same genuinely different compound, not a spelling variant. Fixed `characters:` from an inline flow list to a proper block list, filled a blank `pos: 名詞`/`vietnamese` (honest compositional "nghịch số"), removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 逍遥.

### 2026-09-11, word 128/246 — [[words/逍遥|逍遥]]
Never-perfected word. Fixed `characters:`/`aliases:` from inline flow lists to proper block lists, removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 逍, whose own `stand_in` points to this exact word; noted 遥's own `stand_in` is 遥遠 instead.

Next: 透.

### 2026-09-11, word 129/246 — [[words/透|透]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "thấu," fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `pos`/`kwin`/`date-last-perfect`, wrote a `## Notes` section. Added a missing legitimizing note for 透 (char), whose own `stand_in` points to this exact word (itself). Confirmed the existing three-way homophone callout with [[頭]] and [[套]] was already correctly reciprocal on all three pages (no fix needed). `kwin: false` confirmed.

Next: 透視.

### 2026-09-11, word 130/246 — [[words/透視|透視]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 視(char).md's own Words list. Citation on 透(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 途中.

### 2026-09-11, word 131/246 — [[words/途中|途中]]
Never-perfected word. Filled a missing `vietnamese` with honest compositional "đồ trung," filled missing `date-last-perfect`, extended the existing Notes. **Found and fixed a missing citation** on 中(char).md's own Words list. Citation on 途.md already correctly present (with the existing "stand-in" note for 途), `kwin: false` confirmed, no homophone collision.

Next: 逗号.

### 2026-09-11, word 132/246 — [[words/逗号|逗号]]
Never-perfected word. Filled entirely-blank `japanese`/`korean`/`vietnamese` with honest compositional とうごう/두호/đậu hiệu (disclosed against each language's real everyday term for "comma": 読点/カンマ, 쉼표, dấu phẩy). Fixed `characters:`/`aliases:` formatting, removed dangling blank `hsk_level:`/`swadesh:`, filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 逗留.

### 2026-09-11, word 133/246 — [[words/逗留|逗留]]
Never-perfected word. Filled a missing `vietnamese` with the directly-attested "đậu lưu," filled missing `date-last-perfect`, extended the existing Notes. Both character-page citations already correctly present (with the existing "stand-in" note for 逗), `kwin: false` confirmed, no homophone collision.

Next: 通信.

### 2026-09-11, word 134/246 — [[words/通信|通信]]
Never-perfected word. Filled missing `date-last-perfect`, extended the existing rich Notes with the readings/kwin/homophone verification sentence. Confirmed the Notes' own claim that vietnamese "thông tin" is honest compositional (通's thông + 信's tin), not a real-equivalent bug, despite the semantic drift toward "information" the prose itself describes. Both character-page citations already correctly present, `kwin: true` confirmed, no homophone collision.

Next: 通知.

### 2026-09-11, word 135/246 — [[words/通知|通知]]
Never-perfected word. Removed dangling blank `swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 通行.

### 2026-09-11, word 136/246 — [[words/通行|通行]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 通行証.

### 2026-09-11, word 137/246 — [[words/通行証|通行証]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "thông hành chứng," removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 証.md's own Words list. Citations on 通(char).md and 行(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 通貨.

### 2026-09-11, word 138/246 — [[words/通貨|通貨]]
Never-perfected word. **Found and fixed a typo on `cantonese`** (tong1 fo3 → tung1 fo3, matching 通's own stored tung1). **Found and fixed an invisible zero-width space (U+200B) inside `japanese`** (つ​うか, visually identical to つうか but with a hidden character — diagnosed via `repr()`). Filled a blank `vietnamese` with honest compositional "thông hoá," folded a stray floating comment (typo'd "synonmous with 貨幣") into proper Notes prose, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: true` confirmed, no homophone collision.

Next: 通過.

### 2026-09-11, word 139/246 — [[words/通過|通過]]
Never-perfected word. **Found and fixed a swapped mandarin/cantonese field bug**: pinyin-with-tone-marks had been stored under `cantonese` and Jyutping-with-tone-numbers under `mandarin`, corrected the swap. Filled a blank `vietnamese` with the directly-attested, extremely common "thông qua." Removed dangling blank `swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`. **Found and fixed a missing "(stand-in for 過)" annotation** on 過(char).md's own citation. Citations already correctly present on both character pages, `kwin: true` confirmed, no homophone collision.

Next: 逝去.

### 2026-09-11, word 140/246 — [[words/逝去|逝去]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, filled a blank `vietnamese` with honest compositional "thệ khứ," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, extended the existing Notes. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 逞.

### 2026-09-11, word 141/246 — [[words/逞|逞]]
Never-perfected word. **Found and fixed a korean reading bug on both this page and 逞(char).md itself**: 령 used a structurally incompatible ㄹ-initial (逞's own MC initial 徹/ʈʰ never surfaces as ㄹ in Sino-Korean) — corrected to 정 by direct analogy with 偵 (identical MC initial+final). Fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `kwin`/`date-last-perfect`. **Found and fixed a missing "(stand-in for 逞)" annotation** on 逞(char).md's own citation. Confirmed the existing homophone callout with [[請]] was already correctly reciprocal (no fix needed).

Next: 速.

### 2026-09-11, word 142/246 — [[words/速|速]]
Never-perfected word. **Found and fixed a real-equivalent-instead-of-own-reading bug on 速(char).md's own `vietnamese` field**: the native word "nhanh" had been mixed in with the genuine Sino-Vietnamese readings tốc/rốc — removed, using the honest tốc for this word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `pos`/`date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing "(stand-in for 速)" annotation** on 速(char).md's own citation. **Found a genuine homophone with [[俗]]**, already carrying a correct reciprocal callout dated today — added the matching callout to this page. `kwin: true` confirmed.

Next: 速様.

### 2026-09-11, word 143/246 — [[words/速様|速様]]
Never-perfected word. **Found and fixed a wrong-compound-reading bug across all five reading fields**: mandarin/cantonese/korean/vietnamese held each language's own real everyday word for "quickly" (a garbled comma-mashed korean value; a kanji+okurigana japanese value 速く instead of a kana reading) rather than the honest compositional 速+様 combination — corrected to sùyàng/cuk1 joeng4/そくよう/속양 (matching the word's own stored 諺文/羅馬字)/tốc dạng, and wrote a Notes section explaining this is a Dan'a'yo-internal derivational compound (like the 此様/其様/彼様/何様 correlative series), not independently attested in any source language. **Found and removed five bad-aliases-entries** (迅速地, 快速地, 急速地, 趕快地, 赶快地 — all genuinely different compounds using 地 as their adverbializer). Filled blank `pos: 副詞`, filled missing `kwin`/`date-last-perfect`. Both character-page citations already correctly present, no homophone collision.

Next: 造金.

### 2026-09-11, word 144/246 — [[words/造金|造金]]
Never-perfected word (chemistry neologism — technetium). Confirmed mandarin/cantonese/japanese/korean/vietnamese correctly follow the established proper-noun/named-referent convention for periodic-table neologisms (real element names/loanwords in each language, matching [[青素]]/[[重素]] precedent), not a bug. **Found and fixed a duplicate `pos`/`品詞` key bug** and an invisible non-breaking space (U+00A0) hidden inside the `japanese` list item (same bug class as the earlier 八卦.md finding). Filled missing `date-last-perfect`. **Found and fixed a missing citation** on 金(char).md's own Words list. Citation on 造.md already correctly present, `kwin: false` confirmed (matches 青素/重素 convention), no homophone collision.

Next: 連世紀.

### 2026-09-11, word 145/246 — [[words/連世紀|連世紀]]
Never-perfected word. Filled a missing `vietnamese` with honest compositional "liên thế kỷ" (連's own liên + 世紀's own attested "thế kỷ"), filled missing `date-last-perfect`, wrote a `## Notes` section. All three character-page citations (連, 世, 紀) already correctly present, `kwin: false` confirmed, no homophone collision. Confirmed this is a character+existing-word compound (連 + the standalone word 世紀), not three bare characters.

Next: 連帯.

### 2026-09-11, word 146/246 — [[words/連帯|連帯]]
Never-perfected word. Filled missing `date-last-perfect`, extended the existing rich Notes with the kwin/homophone verification sentence. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連年.

### 2026-09-11, word 147/246 — [[words/連年|連年]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "liên niên," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連接.

### 2026-09-11, word 148/246 — [[words/連接|連接]]
Never-perfected word. Fixed `characters:` disambiguation (bare 接 → "接 (char)," since [[接]] has its own word page). Filled blank `korean`/`vietnamese` (honest compositional 연접, directly-attested "liên tiếp"). **Found and fixed a missing citation** on 接(char).md's own Words list. Removed dangling blank `hsk_level:`/`swadesh:`, filled missing `kwin`/`date-last-perfect`. Citation on 連(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連接詞.

### 2026-09-11, word 149/246 — [[words/連接詞|連接詞]]
Never-perfected word. **Found and fixed a wrong-compound reading bug on `japanese`/`korean`**: せつぞくし/접속사 actually belong to the unrelated compound 接続詞/接續詞, corrected to honest compositional れんせつし/연접사. Fixed `vietnamese` from the unrelated phrase "sự liên kết" to honest compositional "liên tiếp từ" (noting the real grammatical term is actually "liên từ," from the different, shorter compound 連詞). **Found and removed three bad-aliases-entries**: 接續詞/接続詞 (genuinely different compound) and 連詞/连词 (a differently-composed synonym) — kept only the legitimate simplified variant 连接词. Filled missing `date-last-perfect`. **Found and fixed a missing citation** on 詞.md's own Words list. Citations on 連(char).md and 接(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連日.

### 2026-09-11, word 150/246 — [[words/連日|連日]]
Never-perfected word. **Found and fixed a duplicate `pos`/`品詞` key bug** (removed the redundant `品詞`). Filled a missing `vietnamese` with honest compositional "liên nhật," filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連月.

### 2026-09-11, word 151/246 — [[words/連月|連月]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "liên nguyệt," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連盟.

### 2026-09-11, word 152/246 — [[words/連盟|連盟]]
Never-perfected word. **Found and fixed a cantonese typo** (lyun4 mang4 → lin4 mang4, matching 連's own stored lin4). Filled a blank `vietnamese` with the directly-attested, extremely common "liên minh." Fixed `characters:` disambiguation (bare 連 → "連 (char)," since [[連]] has its own word page — caught and corrected a self-introduced slip on the first pass). Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 盟, whose own `stand_in` points to this exact word.

Next: 連続.

### 2026-09-11, word 153/246 — [[words/連続|連続]]
Never-perfected word. Filled missing `date-last-perfect`, extended the existing Notes with the kwin/homophone verification sentence. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連週.

### 2026-09-11, word 154/246 — [[words/連週|連週]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "liên chu," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 連邦.

### 2026-09-11, word 155/246 — [[words/連邦|連邦]]
Never-perfected word. Filled a blank `cantonese` with honest compositional "lin4 bong1," folded a stray floating alias line ("聯邦") into a proper `aliases:` field (a legitimate spelling variant using 連's own alias character 聯, per the vault's explicit merge policy documented on 連(char).md), filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 邦, whose own `stand_in` points to this exact word.

Next: 週中.

### 2026-09-11, word 156/246 — [[words/週中|週中]]
Never-perfected word. **Found and fixed a duplicate `pos`/`品詞` key bug** (removed the redundant `品詞`). Filled entirely-missing `mandarin`/`cantonese`/`japanese`/`vietnamese` with honest compositional readings, filled missing `date-last-perfect`. **Found and fixed a missing citation** on 中(char).md's own Words list — also noticed but did not fix a pre-existing, unrelated duplicate 途中 citation on that same disorganized Words section (flagged for a future cleanup pass). Citation on 週.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 週刊.

### 2026-09-11, word 157/246 — [[words/週刊|週刊]]
Never-perfected word. Fixed `characters:` disambiguation (bare 刊 → "刊 (char)," since [[刊]] has its own word page). Filled a blank `vietnamese` with honest compositional "chu khan," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 週期.

### 2026-09-11, word 158/246 — [[words/週期|週期]]
Never-perfected word. **Found and fixed a self-referential aliases-entry bug**: `週期` had been listed as its own alias (incoherent — removed), keeping `周期` (a genuinely common alternate written form using the homophonous 周 in place of 週; both characters share byte-identical reading fields). **Found and fixed `characters:` field**: was listing 周 instead of the word's own actual constituent 週 (matching the filename/title). **Found and fixed a missing citation** on 週.md's own Words list. Filled missing `date-last-perfect`, wrote a `## Notes` section explaining the 周/週 relationship. Citation on 期(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 進化.

### 2026-09-11, word 159/246 — [[words/進化|進化]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: true` confirmed, no homophone collision.

Next: 進撃.

### 2026-09-11, word 160/246 — [[words/進撃|進撃]]
Never-perfected word. **Found and fixed a real-equivalent-instead-of-own-reading bug on `vietnamese`**: "tấn công" (the everyday Vietnamese verb for "attack," unrelated to 撃's own reading) replaced with honest compositional "tấn kích." Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating alias line ("进击") into a proper `aliases:` field, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 進行.

### 2026-09-11, word 161/246 — [[words/進行|進行]]
Never-perfected word. Filled a blank `vietnamese` with the directly-attested "tiến hành," fixed `characters:`/`aliases:` formatting, folded a stray floating "Stand-in for [[進]]" comment into proper Notes prose, filled missing `date-last-perfect`. Both character-page citations already correctly present (with the existing "(stand-in for 進)" annotation confirmed accurate), `kwin: false` confirmed, no homophone collision.

Next: 逸.

### 2026-09-11, word 162/246 — [[words/逸|逸]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "dật," fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `pos`/`date-last-perfect`, wrote `## Notes` from scratch. **Found and fixed a genuine `kwin` miscalculation on 逸(char).md itself**: byte-level comparison shows Dan'a'yo 읻 (U+C77B) and Sino-Korean 일 (U+C77C) are visually near-identical but genuinely different Hangul syllables — corrected `kwin: true` → `false` on both pages (same divergence-bug class as 읫/의 and 랃/랄). Also **fixed a corrupted `羅馬字` value** (`'''id'` → `'id`). Added a missing legitimizing note for 逸 (char), whose own `stand_in` points to this exact word (itself). Confirmed the existing three-way homophone callout with [[一]] and [[壱]] was already correctly reciprocal on all three pages.

Next: 逸事.

### 2026-09-11, word 163/246 — [[words/逸事|逸事]]
Never-perfected word. Filled a blank `pos: 名詞`, filled blank `korean`/`vietnamese` with honest compositional 일사/dật sự, filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 逸話.

### 2026-09-11, word 164/246 — [[words/逸話|逸話]]
Never-perfected word. Filled a blank `pos: 名詞`, filled a blank `vietnamese` with honest compositional "dật thoại," filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遂道.

### 2026-09-11, word 165/246 — [[words/遂道|遂道]]
Never-perfected word. Confirmed the 遂 (rather than 隧) spelling is this vault's own deliberate, documented merge choice (遂's own `aliases` explicitly registers 隧), not a typo — `隧道` is correctly kept as an alias. **Found and fixed a vietnamese reading bug**: "tụy" isn't among 遂's own stored readings, corrected to honest compositional "toại đạo." Filled a blank `pos: 名詞`, fixed `characters:`/`aliases:` formatting, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遅到.

### 2026-09-11, word 166/246 — [[words/遅到|遅到]]
Never-perfected word. Fixed `characters:` disambiguation (bare 遅 → "遅 (char)," since [[遅]] has its own word page). Filled blank `japanese`/`korean`/`vietnamese` with honest compositional readings (real everyday usage instead favors the different compound 遅刻/遲刻). **Found and removed two bad-aliases-entries**: 遅刻/遲刻 are that same genuinely different compound, not spelling variants — kept only the legitimate trad/simplified variants 遲到/迟到. Filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, no homophone collision.

Next: 遊学.

### 2026-09-11, word 167/246 — [[words/遊学|遊学]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, folded a stray floating alias-candidates line ("遊學, 游学, 游學") into a proper `aliases:` field — all three confirmed legitimate spelling variants (遊's own alias character 游, 学's own alias character 學). Filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遊牧.

### 2026-09-11, word 168/246 — [[words/遊牧|遊牧]]
Never-perfected word. Filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 運数.

### 2026-09-11, word 169/246 — [[words/運数|運数]]
Never-perfected word. **Found and fixed a real-equivalent-instead-of-own-reading bug on `japanese`**: うんせい actually belongs to the different word 運勢, corrected to honest compositional うんすう. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: true` confirmed, no homophone collision.

Next: 運行.

### 2026-09-11, word 170/246 — [[words/運行|運行]]
Never-perfected word. Filled a blank `vietnamese` with the directly-attested "vận hành," fixed `characters:` formatting, folded a stray floating alias line ("运行") into a proper `aliases:` field, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 運送.

### 2026-09-11, word 171/246 — [[words/運送|運送]]
Never-perfected word. Filled a blank `vietnamese` with the directly-attested "vận tống," fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 送(char).md's own Words list. Citation on 運.md already correctly present, `kwin: true` confirmed, no homophone collision. Added a missing legitimizing note for 運, whose own `stand_in` points to this exact word.

**Correction**: 運転 was accidentally skipped in list order (jumped straight to 運送) — it remains in the backlog and is due next, ahead of 遍.

### 2026-09-11, word 172/246 — [[words/運転|運転]]
Never-perfected word. Fixed `characters:` disambiguation (bare 転 → "転 (char)," since [[転]] has its own word page). Filled a blank `vietnamese` with the directly-attested "vận chuyển," folded a stray floating alias line ("運轉") into a proper `aliases:` field, filled missing `date-last-perfect`. **Found and fixed a bare, un-ruby-formatted citation** on 転.md's own Words list. Citation on 運.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遍.

### 2026-09-11, word 173/246 — [[words/遍|遍]]
Never-perfected word. Filled a blank `vietnamese` with the character's own attested "biến," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`kwin`/`date-last-perfect`. Added a missing legitimizing note for 遍 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed. Noted 注音 ㄅㄝㄋ is shared with 辺/蝙 but neither has its own word page, so no genuine homophone.

Next: 過.

### 2026-09-11, word 174/246 — [[words/過|過]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "goá," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`kwin`/`date-last-perfect`. Citation and "(stand-in for 過)" annotation already correctly present on the character page (fixed on an earlier turn this session, during 通過). Confirmed the existing homophone callout with [[鍋]] was already correctly reciprocal (no fix needed). `kwin: true` confirmed.

Next: 過去.

### 2026-09-11, word 175/246 — [[words/過去|過去]]
Never-perfected word. **Found and fixed a missing tone number on `cantonese`** ("gwo heoi3" → "gwo3 heoi3"). **Found and fixed a real-equivalent-instead-of-own-reading bug on `korean`**: a garbled multi-value string "과거, 지난날" mashed the compositional reading with an unrelated native word, trimmed to just 과거. Removed dangling blank `swadesh:`/`aliases:`, filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 過激.

### 2026-09-11, word 176/246 — [[words/過激|過激]]
Never-perfected word. Fixed `characters:`/`aliases:` formatting, removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 過量.

### 2026-09-11, word 177/246 — [[words/過量|過量]]
Never-perfected word. **Found and fixed a korean reading bug**: 과령 used the wrong second syllable — 量's own korean is 량, not 령 — corrected to 과량, matching the word's own stored 諺文/羅馬字 exactly (which also flipped `kwin` from false to genuinely true). Filled entirely-blank `cantonese`/`japanese`/`vietnamese` with honest compositional readings, folded a stray floating gloss line into `english`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, no homophone collision.

Next: 道徳経.

### 2026-09-11, word 178/246 — [[words/道徳経|道徳経]]
Never-perfected word (proper noun — Tao Te Ching). Confirmed mandarin/cantonese/japanese/korean/vietnamese correctly follow the proper-noun/named-referent convention (each language's own real title), and confirmed all four aliases (道德經/道德经/道徳経/道徳經) are legitimate trad/simplified/orthographic variants. Filled missing `date-last-perfect`. All three character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. **Flagged, not fixed**: the linked [[道徳経 (book)]] page doesn't exist yet, same dangling-link class as 紘's own [[八紘一宇]] reference.

Next: 道教.

### 2026-09-11, word 179/246 — [[words/道教|道教]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 道理.

### 2026-09-11, word 180/246 — [[words/道理|道理]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 達.

### 2026-09-11, word 181/246 — [[words/達|達]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "thớt," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`date-last-perfect`, fixed a typo in `english` ("acheive" → "achieve"). **Found and fixed a missing "(stand-in for 達)" annotation** on 達(char).md's own citation. `kwin: false` confirmed, no homophone collision.

Next: 違反.

### 2026-09-11, word 182/246 — [[words/違反|違反]]
Never-perfected word. Filled a blank `vietnamese` with the directly-attested "vi phản," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 違, whose own `stand_in` points to this exact word.

Next: 違法.

### 2026-09-11, word 183/246 — [[words/違法|違法]]
Never-perfected word. Fixed `characters:` from an inline flow list to a proper block list, filled a blank `vietnamese` with honest compositional "vi pháp" (noting modern Vietnamese instead uses "vi phạm"), removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 違犯.

### 2026-09-11, word 184/246 — [[words/違犯|違犯]]
Never-perfected word. **Found and fixed a korean reading bug**: 위반 actually belongs to the sibling word 違反 (uses 反, not 犯) — corrected to honest compositional 위범, matching 犯's own stored korean 범. Confirmed japanese いはん is honestly compositional (犯's own HAN on-reading), a genuine coincidental homophone with 違反, not a bug. Fixed `characters:` from an inline flow list to a proper block list, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遠.

### 2026-09-11, word 185/246 — [[words/遠|遠]]
Never-perfected word. Filled a missing `vietnamese` with the character's own attested "viễn," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`date-last-perfect`. Added a missing legitimizing note for 遠 (char), whose own `stand_in` points to this exact word (itself). **Found a genuine homophone with [[垣]]**, which already carried a one-sided callout referencing 遠 — added the missing reciprocal callout here, completing the pair. `kwin: false` confirmed.

Next: 遠方.

### 2026-09-11, word 186/246 — [[words/遠方|遠方]]
Never-perfected word. Filled a blank `pos: 名詞`/`vietnamese` (honest compositional/attested "viễn phương"), fixed `characters:`/`aliases:` formatting, removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遣.

### 2026-09-11, word 187/246 — [[words/遣|遣]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `kwin`/`date-last-perfect`. Added a missing legitimizing note for 遣 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed. Noted 注音 ㄎㄝㄋ is shared with 牽 but it has no dedicated word page, so no genuine homophone.

Next: 遥遠.

### 2026-09-11, word 188/246 — [[words/遥遠|遥遠]]
Never-perfected word. Filled missing `date-last-perfect`, extended the existing Notes (already correctly noting the compositional Vietnamese and the 遥 legitimizing relationship) with readings/kwin/homophone verification. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 適宜.

### 2026-09-11, word 189/246 — [[words/適宜|適宜]]
Never-perfected word. Filled entirely-missing `korean`/`vietnamese` with compositional/directly-attested 적의/thích nghi, filled missing `kwin`/`date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing `#cranberry` tag**: both 適 and 宜's own `stand_in` fields point to this word (transitivity A=B=AB confirmed) — added the tag. Both character-page citations already correctly present (with their "(stand-in for X)" annotations), `kwin: false` confirmed, no homophone collision.

Next: 遭遇.

### 2026-09-11, word 190/246 — [[words/遭遇|遭遇]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 遭, whose own `stand_in` points to this exact word.

Next: 遮蔽.

### 2026-09-11, word 191/246 — [[words/遮蔽|遮蔽]]
Never-perfected word. Filled blank `cantonese`/`vietnamese` with honest compositional "ze1 bai3"/"già tế," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 遮, whose own `stand_in` points to this exact word.

Next: 遵守.

### 2026-09-11, word 192/246 — [[words/遵守|遵守]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 遵, whose own `stand_in` points to this exact word; noted 守's own `stand_in` is 守衛 instead.

Next: 遺.

### 2026-09-11, word 193/246 — [[words/遺|遺]]
Never-perfected word. Filled a blank `vietnamese` with the character's own attested "di," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`date-last-perfect`. **Found and fixed an entirely missing self-standing citation** on 遺(char).md's own Words list (the compound citations were present, but not the bare stand-in entry). Added a missing legitimizing note for 遺 (char), whose own `stand_in` points to this exact word (itself). **Found a genuine homophone with [[唯]]**, which already carried a one-sided callout referencing 遺 — added the missing reciprocal callout here. `kwin: false` confirmed.

**Correction**: 選択 was accidentally skipped in list order (jumped straight to 遺) — it remains in the backlog and is due next, ahead of 遺伝子.

### 2026-09-11, word 194/246 — [[words/選択|選択]]
Never-perfected word. Filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a bare, un-ruby-formatted citation missing its "(stand-in for 択)" annotation** on 択.md's own Words list. Citation on 選.md already correctly present, `kwin: false` confirmed, no homophone collision. Confirmed the existing `#cranberry` tag is accurate (both 選 and 択 stand_in to this compound).

Next: 遺伝子.

### 2026-09-11, word 195/246 — [[words/遺伝子|遺伝子]]
Never-perfected word. **Found and fixed an archaic-kana typo on `japanese`**: ゐでんし used the obsolete kana ゐ (wi), corrected to いでんし matching modern standard orthography. Confirmed vietnamese "gen" is the genuine real-world Vietnamese loanword, not a bug. Removed dangling blank `hsk_level:`/`swadesh:`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a bare citation** on 子.md's own Words list (broader section remains flagged). Citations on 遺(char).md and 伝.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遺憾.

### 2026-09-11, word 196/246 — [[words/遺憾|遺憾]]
Never-perfected word. Removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`. Existing Notes already correctly documented the legitimizing relationship and vietnamese attestation via hvdic. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 遺産.

### 2026-09-11, word 197/246 — [[words/遺産|遺産]]
Never-perfected word. Filled missing `date-last-perfect`. Existing Notes already thorough and correct. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 避.

### 2026-09-11, word 198/246 — [[words/避|避]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "tị," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`kwin`/`date-last-perfect`. Added a missing legitimizing note for 避 (char), whose own `stand_in` points to this exact word (itself). **Found a genuine homophone with [[卑]]**, which already carried a one-sided callout referencing 避 — added the missing reciprocal callout here. `kwin: false` confirmed.

Next: 那.

### 2026-09-11, word 199/246 — [[words/那|那]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, filled missing `pos`/`date-last-perfect`, extended the existing Notes. Citation and legitimizing note already correctly reflected by the character's self-referential `stand_in`; added the closing legitimizing sentence explicitly. `kwin: true` confirmed. Noted 注音 ㄋㄚ is shared with 梛/拿 but neither has its own word page, so no genuine homophone.

Next: 邦畿.

### 2026-09-11, word 200/246 — [[words/邦畿|邦畿]]
Never-perfected word. Filled blank `cantonese`/`vietnamese` with honest compositional readings, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 畿.md's own Words list. Citation on 邦.md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 邾国.

### 2026-09-11, word 201/246 — [[words/邾国|邾国]]
Never-perfected word (proper noun — ancient State of Zou). Filled a missing `vietnamese` with honest compositional "chu quốc," filled missing `kwin`/`date-last-perfect`. **Found and fixed a missing "(stand-in for 邾)" annotation** on 邾.md's own citation. Citation on 国.md already correctly present, `kwin: false` confirmed, no homophone collision. Added a legitimizing note for 邾, whose own `stand_in` points to this exact word.

Next: 部.

### 2026-09-11, word 202/246 — [[words/部|部]]
Never-perfected word. Filled `vietnamese: null` with the character's own attested "bộ," fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `pos`/`date-last-perfect`. Added a missing legitimizing note for 部 (char), whose own `stand_in` points to this exact word (itself). `kwin: false` confirmed, no homophone collision.

Next: 部分.

### 2026-09-11, word 203/246 — [[words/部分|部分]]
Never-perfected word. Removed dangling blank `swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed a missing citation** on 分(char).md's own Words list — also noticed (but did not fix) that page's broader Words section is disorganized, with a bare 分配 citation and misplaced Ancient-CC-initials/finals links inserted mid-list. Citation on 部(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 部族.

### 2026-09-11, word 204/246 — [[words/部族|部族]]
Never-perfected word. Fixed `characters:` unindented list, filled a blank `vietnamese` with the directly-attested "bộ tộc," removed dangling blank `hsk_level:`/`swadesh:`/`aliases:`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 部署.

### 2026-09-11, word 205/246 — [[words/部署|部署]]
Never-perfected word. Filled a blank `vietnamese` with honest compositional "bộ thự," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision. Added a missing legitimizing note for 署, whose own `stand_in` points to this exact word.

Next: 部長.

### 2026-09-11, word 206/246 — [[words/部長|部長]]
Never-perfected word. Filled a blank `vietnamese` with the directly-attested "bộ trưởng," fixed a malformed inline `aliases:` into a proper list, filled missing `date-last-perfect`, wrote a `## Notes` section. **Found and fixed two missing citations** on 長(char).md's own Words list: the bare self-standing [[長]] entry (resolving a long-standing carried-forward item from the old sweep) and [[部長]] itself, both entirely absent. Citation on 部(char).md already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 部門.

### 2026-09-11, word 207/246 — [[words/部門|部門]]
Never-perfected word. Fixed `characters:`/`aliases:` formatting, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 部隊.

### 2026-09-11, word 208/246 — [[words/部隊|部隊]]
Never-perfected word. Fixed `characters:`/`aliases:` formatting, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 部首.

### 2026-09-11, word 209/246 — [[words/部首|部首]]
Never-perfected word. Fixed `characters:` formatting, filled a blank `vietnamese` with the directly-attested "bộ thủ," removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, filled missing `date-last-perfect`, wrote a `## Notes` section. Both character-page citations already correctly present, `kwin: false` confirmed, no homophone collision.

Next: 郭.

### 2026-09-11, word 210/246 — [[words/郭|郭]]
Never-perfected word. Fixed `characters:` from a bare unlisted scalar to a proper YAML list, fixed a stray "# Notes" (wrong heading level) into "## Notes" and wrote its content from scratch. Filled missing `kwin`/`date-last-perfect`. Added a missing legitimizing note for 郭 (char), whose own `stand_in` points to this exact word (itself). `kwin: true` confirmed. Noted 注音 ㄍ⺢ㄎ is shared with 霍 but it has no dedicated word page, so no genuine homophone.

Next: 郭清.
