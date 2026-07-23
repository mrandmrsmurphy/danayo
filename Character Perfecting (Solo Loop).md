### 2026-07-22, iteration 38 — [[characters/明 (char)|明]]

Next never-perfected character by `danayo_id` (134) — already had a good graphemic bullet and partial structure, needed a gap-fill and cleanup pass. Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 會意` matching the already-good 会意 bullet, 日+月).

**Content removed**: none.

**Small fixes**: disambiguated the graphemic bullet's `[[日]]`/`[[月]]` links to `[[日 (char)|日]]`/`[[月 (char)|月]]` (both collide with word files); merged a non-canonical bullet that crammed SKIP/Stroke/syllable into one line into the proper two-bullet split, and built a real MC-rank bullet from scratch (the old one was just two bare floating CC-initial/final links with no ordinal rank or syllable link at all).

**Caught and corrected before finalizing — a guessed chengyu gloss, same near-miss class flagged repeatedly this sweep**: while adding 旗幟鮮明 (present on the old page with no gloss at all), first copy-pasted 光明正大's gloss onto it since a quick single-line `grep` on the `english:` key appeared to show nothing for either — re-read both files in full and found 旗幟鮮明's real stored gloss is "have a clear-cut stand," entirely different from 光明正大's. Corrected before shipping; the single-line grep pattern itself was the failure mode (it only shows the `english:` key line, not the list item(s) below it for multi-line fields) — worth remembering as a sharper version of the extraction-script lesson from [[characters/国|国]] two iterations ago.

**Words cross-check** (33 total ground-truth hits): 11 already listed (several bare, reformatted); 22 missing — added, all from stored fields.

**Chengyu cross-check** (4 total): 1 already present (gloss fixed per above); 3 missing — 光明正大, 公明正大, 毎字明意 — added.

**Derived Characters** (2 hits via `graphemic_classification: 明`): 盟 ("alliance; covenant") and 萌 ("bud; sprout") — both exact `注音` matches, added.

**Incidental fix**: `characters/盟.md`'s `english` field had a typo, "aliance" → "alliance."

### 2026-07-22, iteration 39 — [[characters/東|東]]

Next never-perfected character by `danayo_id` (135). Stamped `date-last-perfect: 2026-07-22`.

**Real etymology correction, backed by a cross-reference already sitting on another perfected page**: `graphemic_classification` was stored as `會意`, and Notes had no bullet at all to check it against. Rather than write the popular "sun rising behind a tree" folk story that's often taught but not the accepted scholarly origin, checked [[characters/西|西]]'s own already-perfected page from earlier this loop — its Notes bullet explicitly states "Compare 東 (OC \*toːŋ, 'bundle > east'), 束 and 鹵," i.e. this vault had *already* recorded, on a different page, that 東's real etymology is a pictograph of a tied bundle/sack (the same "borrowed pictograph" family as 西 itself), not a 会意 compound. Corrected the field to `象形` and wrote the bullet accordingly, citing the 西 cross-reference directly and noting the sun-behind-tree story explicitly as a later reinterpretation rather than silently omitting it (a reader who's only heard the folk version deserves the correction spelled out, not just a different answer with no explanation).

**Body defects found**: `## Notes` was entirely empty; two floating CC-initial/final links sat inside the Words list; several entries were bare `[[link]] "gloss"` markdown, one used a relative link with a dash-gloss, one gloss had a stray leading dash baked into the quoted text itself ("- Eastern barbarian").

**Words cross-check** (15 total ground-truth hits): 7 already listed (reformatted, stray dash removed from 東夷's gloss); 5 missing — the `stand_in` compound 東方 itself, 東部, 極東, 東亜, 東京 — added, all from stored fields.

**Chengyu cross-check** (3 total): 古今東西 and 東奔西走 both reused verbatim from [[characters/西|西]]'s own already-perfected entries (same two chengyu, same character pair); 東亜自通 (単亜語-origin) added fresh from stored fields.

**Derived Characters** (3 hits via `graphemic_classification: 東`): 重 ("heavy" — a real if MC-divergent phonetic pair, ɖ+ɨoŋ vs 東's own t+uŋ, both nasal-final rimes, matching Shuowen's 従壬東聲), 凍 ("freeze"), 棟 ("ridgepole") — all added.

### 2026-07-22, iteration 40 — [[characters/育 (char)|育]]

Next never-perfected character by `danayo_id` (136). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 肉`) — verified rather than assumed: cross-checked 肉's own stored Middle Chinese (`ȵ`+`ɨuk`) against 育's own (`j`+`ɨuk`) and found an exact rime match with a plausible palatal-initial correspondence, confirming the field genuinely reflects Shuowen's real 従𠫓肉聲 analysis (semantic 𠫓, "inverted child" depicting childbirth, + phonetic 肉) rather than assuming it without checking, given how often this sweep has found the opposite.

**Content removed**: none.

**Graphemic bullet written from scratch**: as above, citing the exact MC rime match as the verifying evidence.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links — no other bullets, no `## Words` heading at all.

**Words cross-check** (7 total ground-truth hits): none were previously listed — added the stand-in 育 itself plus 教育, 体育, 体育館, 養育, 生育, 肥育, all from stored fields. No chengyu hits.

**Derived Characters** (1 hit via `graphemic_classification: 育`): 充 ("fill" — Shuowen's 従儿育省聲, phonetic 育 abbreviated), added.

**Incidental fix**: the character's own `english` field had a typo, "nuture" → "nurture."

### 2026-07-22, iteration 41 — [[characters/於 (char)|於]]

Next never-perfected character by `danayo_id` (138; 137 already stamped on inspection). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 修飾語`, matching its real function as a locative preposition/case particle; `graphemic_classification: 象形`).

**Content removed**: a stray, meaningless fragment line, "方,仒" — not real content, sitting where the graphemic bullet should have been. Removed outright.

**Graphemic bullet written from scratch**: 於 is a variant/simplified form of 烏 ("crow"), later borrowed purely for its sound to write the grammatical particle "at, in" — a standard, uncontested account (unlike a couple of other 象形 characters this loop has had to hedge on).

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (1 total ground-truth hit, the stand-in itself): added, from stored fields. **Chengyu built from scratch** (1 hit): 義重於音 (単亜語-origin), ruby/gloss from stored fields. No `graphemic_classification: 於` hits — no Derived Characters section applies.

### 2026-07-22, iteration 42 — [[characters/姉 (char)|姉]]

Next never-perfected character by `danayo_id` (139). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter fixed — a real etymology correction, no pre-existing bullet to check it against**: blank `pos: ""` → `名詞`. `graphemic_classification: 巾` was checked against 巾's own stored Middle Chinese (`k`+`ɣiɪn`) versus 姉's own (`t͡s`+`ia`) — no plausible phonetic relationship at all (different initial class, different rime shape, no shared feature). The real Shuowen etymology for 姊/姉 is 従女，𠂔聲 (phonetic 𠂔, a rare/obsolete glyph, not 巾) — corrected the field to `𠂔` and described the component in prose without a link, since it has no character page in this vault (same treatment as 気/气 and 左/𠂇 precedent elsewhere in this sweep).

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; both existing Words entries were bare `[[link]] "gloss"` with no ruby.

**Words cross-check** (4 total ground-truth hits): 2 already listed (reformatted); 2 missing — the stand-in 姉 itself and 兄弟姉妹 (ruby/gloss reused from [[characters/弟 (char)|弟]]'s and [[characters/妹|妹]]'s own entries for the same word) — added. No chengyu hits, no `graphemic_classification: 姉` hits.

### 2026-07-22, user-flagged correction — periodic-table abbreviation notes wrongly demoted on three pages

**User correction, mid-loop**: iterations 1 ([[characters/多 (char)|多]]), 13 ([[characters/西|西]]), and 21 ([[characters/里 (char)|里]]) each originally had a Notes bullet reading "abbreviation for [element]," which this loop treated as incidental trivia and moved into the `## Words` entry for the coined element-name compound, in some cases (西) losing the "abbreviation for" framing entirely down to a bare gloss. **This was wrong**: within this vault's element-naming system, a single Dan'a'yo character is deliberately assigned to function as that element's own abbreviation/symbol — the same role a letter like "Gd" or "Sg" plays in a real periodic table, not just a component of one specific coined word. That fact belongs on the *character's own page*, in Notes, not folded away as a parenthetical on the word page.

**Fixed**: restored a dedicated trailing Notes bullet on all three pages, keeping the "functions as an element-abbreviation character" framing explicit and linking to the actual coined word (加多金 gadolinium/Gd, 西博金 seaborgium/Sg, 居里金 curium/Cm) rather than just leaving it inside that word's own Words-section gloss. The Words-section entries themselves are left in place unchanged — this was about restoring the character-level fact, not removing the word-level listing.

**Standing rule going forward**: when a character's stored Notes content mentions "abbreviation for [element]" or similar, treat it as a real, permanent fact about that character (keep as its own trailing Notes bullet), not as duplicate/incidental content to fold into the Words section — even if a Words entry for the same compound already exists.

### 2026-07-22, iteration 43 — [[characters/学|学]]

Next never-perfected character by `danayo_id` (140). Stamped `date-last-perfect: 2026-07-22`. **The largest page this loop has done — 56 Words entries** (surpassing [[characters/国|国]]'s 63... actually 国 remains the largest by count, this is the second-largest).

**Frontmatter**: blank `pos: ""` → `事詞` — precedent from `words/学習.md`'s own stored `pos: 事詞`. **Real etymology correction**: `graphemic_classification: 指事` (a pure indicator/dot-marking classification) doesn't fit 学/學 at all — its real, uncontested etymology is 会意 of 爻 ("crossed counting rods") + 冖 ("roof") + 子 ("child"), a child studying calculation under a roof, one of the more famous textbook 会意 examples. No pre-existing bullet to contradict (Notes was empty) — corrected from scratch and wrote the bullet accordingly.

**Content removed**: none.

**Body defects found**: `## Words` used a numbered list (1–35) for most entries with only a handful ruby'd, switching to unordered bullets partway through with no clear reason; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (56 total ground-truth hits, computed via a full diff script rather than manual counting given the scale — confirmed zero false-positive "extra" entries, all 43 originally-listed items were genuine): 13 missing — the `stand_in` compound 学習 itself, 学生, 大学, 中学校, 教学, 儒学, 数学, 化学, 化学肥料, 人類学, 天文学, 物理学, 生物学, 老人学 — added, all from stored fields. **Two more missing-`注音` word files found** (same class as [[characters/国|国]]'s 中国人/中国語 two iterations ago): `words/中学校.md` only had `羅馬字`/`諺文` — reconstructed via constituent-character concatenation (中 ㄐㄨㄫ + 学 ㄏㄚㄎ + 校 ㄏ⼘ㄨ) and cross-verified against both stored fields before using it.

**Derived Characters** (1 hit via `graphemic_classification: 学`): 覚 ("perceive" — Shuowen's 従見學省聲, phonetic 学 abbreviated), added.

**Incidental fix**: `words/経済学.md`'s `english` field read "economic" (adjective) where "economics" (the field of study) was clearly meant — corrected.

### 2026-07-22, iteration 44 — [[characters/雨 (char)|雨]]

Next never-perfected character by `danayo_id` (141). Stamped `date-last-perfect: 2026-07-22`. Page already had a nice non-canonical extra — a radical-disambiguation callout line ("For the radical, see Radical 173") beyond the standard template — kept as-is per the "preserve genuinely useful extra content" precedent.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 象形` matching an already-good, sourced bullet with an Egyptian hieroglyph comparison).

**Content removed**: none.

**Body defects found**: `## Words`, `## Chengyu`, and `## Notes` appeared in that (wrong) order; two floating CC-initial/final links had no MC bullet to embed in; four Words-style entries (雨傘, 雨中, 俄雨, 小雨) were sitting inside `## Notes` instead of `## Words`.

**Words cross-check** (8 total ground-truth hits): 6 already present across the misplaced sections (consolidated, reformatted); 2 missing — the stand-in 雨 itself and 林雨 — added. Also added 梅雨, which despite appearing to already be covered by the general pattern was genuinely absent.

**Chengyu cross-check** (2 total): 1 already present (五風十雨); 1 missing — 未雨紬謬 (《詩經》-origin) — added.

**Derived Characters** (1 hit via `graphemic_classification: 雨`): 黍 ("millet" — Shuowen's 従禾雨省聲, phonetic 雨 abbreviated, an unusual but genuine attested relationship), added.

### 2026-07-22, iteration 45 — [[characters/門|門]]

Next never-perfected character by `danayo_id` (142). Stamped `date-last-perfect: 2026-07-22`. **First real application of the new standing rule** ([[feedback_element_abbreviation_characters]], added this session after the user's correction on 多/西/里): this page's own Notes already had an "abbreviation for mendelevium" bullet for [[門捷金]] — kept it as its own trailing Notes bullet this time instead of repeating the earlier mistake of folding it into the Words entry alone.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 象形`).

**Content removed**: none.

**Graphemic bullet expanded**: from a bare heading with no bullet at all — wrote it from scratch (a double door/gate, linking 門's own radical, [[Radical 169|門]], since the character depicts itself).

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/Levels bullets existed.

**Words cross-check** (10 total ground-truth hits): 3 already listed (専門, 門捷金, 奥門); 7 missing — the `stand_in` compound 大門 itself, 門戸, 校門, 凱旋門, 部門, 肛門, 陰門 — added, all from stored fields.

**Derived Characters** (3 hits via `graphemic_classification: 門`): 聞 ("hear"), 問 ("question"), 悶 ("agony") — all standard, well-attested 門-phonetic derivatives, added.

### 2026-07-22, iteration 46 — [[characters/苦 (char)|苦]]

Next never-perfected character by `danayo_id` (143). Stamped `date-last-perfect: 2026-07-22`. **Second application of the new element-abbreviation standing rule**: this page's Notes had a garbled numbered-list fragment ("1. bitter / 2. abbreviation for 'magnesium'") sitting before the real graphemic bullet — kept the magnesium-abbreviation fact as its own proper trailing Notes bullet (linking [[苦土素]]) rather than discarding it, per the rule added earlier this session.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 古` matching an already-good, OC-cited bullet).

**Content removed**: the garbled "1. bitter / 2. abbreviation..." numbered-list fragment (superseded by the real graphemic bullet and the restored magnesium note below it); a literal duplicate — `苦土素`'s ruby+gloss line was typed out twice on the same bullet ("magnesium `<ruby>...` magnesium `<ruby>...`"), collapsed to one; six Words entries (苦役, 苦難, 苦肉, 苦悩, 刻苦, 苦味) existed as **two separate copies each** — a bare `* [[link]] gloss` asterisk-bullet list followed later by a proper ruby'd dash-bullet list repeating the same six compounds — deduplicated, keeping the properly-formatted copy of each.

**Words cross-check** (14 total ground-truth hits): 9 already present after deduplication; 5 missing — the stand-in 苦 itself, 苦土, 苦悶, 苦渋, 辛苦 — added, all from stored fields. No chengyu hits, no `graphemic_classification: 苦` hits.

**Incidental fix**: `words/辛苦.md`'s `english` field had a typo, "word hard" → "work hard."

### 2026-07-22, iteration 47 — [[characters/空 (char)|空]]

Next never-perfected character by `danayo_id` (144). Stamped `date-last-perfect: 2026-07-22`. Page already had a real, correctly-cited graphemic bullet — this iteration was mostly reordering and gap-filling.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 工`).

**Content removed**: none.

**Body defects found**: `## Chengyu` sat before `## Words`; bullets 2–4 were merged into non-canonical forms — a Levels bullet came before the MC bullet, and the MC bullet crammed SKIP/Stroke/syllable/CC-links together with middle-dot separators instead of the canonical two-bullet split. Rebuilt into the standard four-bullet order.

**Words cross-check** (14 total ground-truth hits): 4 already listed (reformatted); 10 missing — the stand-in 空 itself, 空手道, 天空, 空気, 空港, 空白, 空虚, 航空, 航空母艦, 孫悟空 — added, all from stored fields.

**Chengyu cross-check** (4 total): 3 already present and correctly formatted; 1 missing — 海闊天空 — added.

**Derived Characters** (2 hits via `graphemic_classification: 空`): 控 ("accuse; charge") and 腔 ("chest cavity") — both standard, well-attested 工-family phonetic derivatives via 空, added.

### 2026-07-22, iteration 48 — [[characters/知 (char)|知]]

Next never-perfected character by `danayo_id` (146; 145 already stamped on inspection). Stamped `date-last-perfect: 2026-07-22`. Already flagged as unperfected as far back as [[Word Perfecting.md]] iteration 7 ("bare '矢, 口' Notes fragment") — that stray fragment was still sitting there unresolved.

**Real etymology correction**: `graphemic_classification: 矢` asserted 形声 with phonetic 矢, but the classical Shuowen entry for 知 reads "从口从矢" — both components stated as meaning-contributing (会意), with no phonetic relationship claimed at all. The page's own leftover "矢, 口" fragment (a bare component list, not a real bullet) was itself evidence pointing the same direction — someone had already identified both components as relevant, just never finished writing the analysis. Corrected the field to `會意` and wrote the bullet: an arrow's swiftness/directness + mouth/speech — words spoken as unerringly as an arrow flies, "to know." Linked 矢 to its Radical page (`[[Radical 111|矢]]`, since 知's own `radical:` field is 矢).

**Content removed**: the stray "矢, 口" component-list fragment (superseded by the real bullet) and an empty bullet (`- ` with nothing after it).

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; several Words entries were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (8 total ground-truth hits): 7 already listed (reformatted); 1 missing — the stand-in 知 itself — added.

**Chengyu**: 温故知新 already present and correctly formatted, no changes needed.

**Derived Characters** (3 hits via `graphemic_classification: 知`): 智 ("wisdom," transparently 知+日), 蜘 ("spider," as in 蜘蛛), 痴 ("stupid; foolish") — all standard, well-attested 知-phonetic derivatives, added.

**Incidental fix**: `words/知性.md`'s `english` field had a typo, "knowledgable" → "knowledgeable."

### 2026-07-22, iteration 49 — [[characters/夜 (char)|夜]]

Next never-perfected character by `danayo_id` (147). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 亦` — verified before writing the bullet: 亦's own stored MC, `j`+`iᴇk`, shares 夜's own initial `j` with a divergent entering-tone final, exactly matching Shuowen's explicit "亦省聲" — an abbreviated phonetic, not a full-syllable match — so the field is correct, not another false phonetic like earlier iterations).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 036|夕]] ("evening") + phonetic [[亦 (char)|亦]] (abbreviated) — the time after evening, "night."

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links plus three Words-style entries — no `## Words` heading, no SKIP/Stroke/MC/Levels bullets.

**Words cross-check** (6 total ground-truth hits): 3 already listed (reformatted); 3 missing — the stand-in 夜 itself, 今夜, 今夜安 — added, all from stored fields.

**Chengyu built from scratch** (1 hit): 雲昼火夜 (Bible-origin), ruby/gloss from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 夜`): 液 ("fluid; sap" — semantic 氵ᐩphonetic 夜, a standard pairing), added.

### 2026-07-22, iteration 50 — [[characters/注|注]]

Next never-perfected character by `danayo_id` (148). Stamped `date-last-perfect: 2026-07-22`. **50th iteration milestone for this loop.**

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 主` — already independently confirmed in [[Loop Work.md]] iteration 19, where 主's own Derived Characters check found 注 as an exact MC match; re-verified here directly against 主's own stored fields, `t͡ɕ`+`ɨo`, identical to 注's own — a clean, confirmed phonetic pair).

**Content removed**: a stray "水,主" component-list fragment, superseded by the real bullet.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 085|水]] ("water") + phonetic [[主]] — to pour, to concentrate liquid into a place.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no `## Words` heading existed (the two present entries sat directly under Notes).

**Words cross-check** (5 total ground-truth hits): 2 already listed (注音, 転注); 3 missing — the `stand_in` compound 注入 itself, 注意 (whose own vowel-hiatus-marked reading, ju'ǝ, was already resolved and documented back in [[Word Perfecting.md]] iteration 9), 注音符号 — added, all from stored fields. No chengyu hits, no `graphemic_classification: 注` hits.

**Loop status**: 50 iterations completed, one full skip ([[characters/両 (char)|両]]), one left unstamped pending a missing word ([[characters/声|声]]).

### 2026-07-22, iteration 51 — [[characters/彼 (char)|彼]]

Next never-perfected character by `danayo_id` (149). Stamped `date-last-perfect: 2026-07-22`. Another full correlative-row family (此/其/彼/何/毎/某/皆 × 事/物/名/処/時/様/多/類/人), same recurring pattern as [[characters/多 (char)|多]], [[characters/何 (char)|何]], and [[characters/事 (char)|事]] earlier this loop.

**Frontmatter**: already correct (`pos: 修飾語`, `graphemic_classification: 皮` — already independently confirmed genuine back in the Components-driven thread of [[Loop Work.md]], where 皮's own Derived Characters check found 彼 among its real phonetic family).

**Content removed**: a stray "Components: [[彳]], [[皮]]" fragment, superseded by the real bullet.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 060|彳]] ("step, road") + phonetic [[皮]] — movement toward a distant point, "that, yonder."

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; no `## Words` heading existed at all.

**Words cross-check** (10 total ground-truth hits): none were previously listed — built the entire section from scratch: the stand-in 彼 itself, 彼処, 彼時, 彼様, 彼多, 彼物, 彼類, 彼事, 彼人, 彼名, all from stored fields. No chengyu hits, no `graphemic_classification: 彼` hits.

### 2026-07-22, iteration 52 — [[characters/画|画]]

Next never-perfected character by `danayo_id` (150). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 會意`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意 of [[Radical 129|聿]] ("brush, writing implement") + [[Radical 102|田]] ("field, boundary lines") — drawing boundary lines with a brush, "to draw, to plan." 聿 has no character page of its own but is a genuine Kangxi radical (129), linked there per the established rule for unlinkable-but-real radical components.

**Body defects found**: `## Notes` was completely empty; `## Chengyu` sat before `## Words` with only one entry and no gloss; two floating CC-initial/final links had no MC bullet to embed in; several Words entries were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (7 total ground-truth hits): 5 already listed (reformatted); 2 missing — 筆画, 計画 — added, all from stored fields.

**Chengyu cross-check** (2 total): 1 already present (画蛇添足, gloss added from its stored field); 1 missing — 画龍点睛 — added. No `graphemic_classification: 画` hits — no Derived Characters section applies.

### 2026-07-22, iteration 53 — [[characters/幸|幸]]

Next never-perfected character by `danayo_id` (151). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 會意`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意 of 屰 ("reversal, going against") + 夭 ("a bent or dying person") — to reverse/escape misfortune, "lucky, fortunate."

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (3 total ground-truth hits): 1 already listed (幸福); 2 missing — the `stand_in` compound 幸運 itself and 不幸 — added, all from stored fields.

**One Derived Characters candidate deliberately excluded, not decided on the spot**: `graphemic_classification: 幸` hits only `characters/睾.md` (gāo, "testicle"), but its own stored Middle Chinese (`k`+`ɑu`) shares no plausible relationship with 幸's own (`ɣ`+`ɣɛŋ`) — different initial class and rime entirely. Same "field looks wrong on a different character's own page" situation as [[characters/耳 (char)|耳]]'s excluded `摂` candidate earlier this loop — left `睾.md` untouched and excluded it from 幸's Derived Characters rather than guessing either way; worth a dedicated look when 睾 comes up by its own `danayo_id`.

### 2026-07-22, iteration 54 — [[characters/林 (char)|林]]

Next never-perfected character by `danayo_id` (152). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 會意` matching an already-good bullet).

**Content removed**: none.

**Tooling note — repeated `Edit` mismatches on this file**: several attempted `Edit` calls against multi-line blocks containing this page's CJK content failed with "string not found" even when the text visually matched the `Read` output exactly, including on isolated single lines; splitting into progressively smaller anchors only partially helped. Fell back to a full `Write` rewrite of the file (content already in hand from `Read`) rather than continuing to fight the mismatch. Worth remembering as a fallback tactic if `Edit` repeatedly rejects an apparently-correct CJK string match.

**Small fix**: the radical-linking bullet used a broken plain-markdown link, `[木](Radical%20075)` (missing the `lookup/Radicals/` path and `.md` extension, and not a wikilink) — fixed to `[[Radical 075|木]]`.

**Body defects found**: `### Derived Character` was H3 and positioned before Words; no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; one Words entry used a broken relative link (`[[words/林雨]]`, a folder-qualified wikilink that doesn't resolve) with a dash-gloss instead of ruby format; a stray whitespace-only line sat between two real bullets.

**Words cross-check** (5 total ground-truth hits): 3 already listed (reformatted, 林雨's broken link fixed); 2 missing — the stand-in 林 itself and 森林 — added.

**Derived Characters** (3 hits via `graphemic_classification: 林`): 淋 ("drain; drip"), 琳 ("jade; gem"), 禁 ("restrict; prohibit" — already listed but bare) — all standard, well-attested 林-phonetic derivatives, added/reformatted.

### 2026-07-22, iteration 55 — [[characters/青 (char)|青]]

Next never-perfected character by `danayo_id` (154; 153 was already stamped from an earlier session, so skipped). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 生` — this exact 形声 relationship was independently verified via Wiktionary back in `Loop Work.md` iteration 22, so not re-litigated here).

**Content removed**: none. The page already had a periodic-table abbreviation bullet — `abbreviation for "caesium": [[青素]]` — which was correctly **preserved as its own trailing Notes bullet**, per the standing rule in `[[AIOS/memory/feedback_element_abbreviation_characters|feedback_element_abbreviation_characters]]`.

**Body defects found**: `# Notes` was H1 instead of H2; two floating CC-initial/final links (`[[Lookup/CC/initials/聲 清]]`, `[[Lookup/CC/finals/韻 青開]]`) sat outside any bullet instead of being embedded in a proper MC-rank bullet; no SKIP/Stroke or Levels bullet existed; the graphemic (形声) bullet was entirely missing.

**Words cross-check** (8 total ground-truth hits via `characters:` field, including inline-array and bare-scalar forms): 3 were already listed (青色, 青年, 青蛙 — all reformatted into ruby form with real stored 注音); 5 were missing and added — the stand-in 青 itself, 青州 ("Qing Province"), 青素 ("caesium," already present as a Notes-level abbreviation fact but also given its own proper Words entry since the two are not redundant per the standing rule), 青銅 ("bronze"), and 蕪青 ("turnip").

**Derived Characters** (10 hits via `graphemic_classification: 青` — the largest family found this entire loop): 請, 晴, 情, 清, 猜, 睛, 精, 錆, 靖, 鯖. All are extremely well-attested, standard 青-phonetic derivatives in real Chinese/Japanese (青 qīng is one of the most productive phonetic series in the language), so no individual MC-mismatch exclusion check was needed the way isolated single-hit cases (摂, 睾) required earlier in the loop. Filename collision found on 請 only (`words/請.md` exists) — linked as `[[請 (char)|請]]`; the other nine had no colliding word file.

**Incidental fix**: `characters/鯖.md` had a typo in its own `english` field, "mackerell" → "mackerel," fixed in passing.

---

**Loop ended by user instruction ("end loop") after this iteration.** 55 iterations completed this session (characters/danayo_id 84 through 154, with 両/98 skipped as an unresolved cross-sense conflation and 声/127 left unstamped pending the missing word 発声). Next continuation point, if resumed: danayo_id 155 onward.
