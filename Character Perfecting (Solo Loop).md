### 2026-07-26, iteration 441 — [[characters/存|存]]

Next never-perfected character by `danayo_id` (3077). **Two stacked defects found and fixed**: (1) `graphemic_classification: 會意` contradicted the page's own pre-existing bullet, which already stated a 形声 analysis; (2) that same bullet had semantic and phonetic reversed — it read "semantic 才 + phonetic 子," but Wiktionary confirms the opposite: semantic [[子]] ("child" — this character's own `radical` field, relating to growth/continuation, "exist, survive") + phonetic [[才]] (OC \*zlɯː, \*zlɯːs). Corrected the field to `才` and swapped the bullet's roles accordingly. Genuinely interesting cross-reference: Wiktionary suggests 存 may be "the demonstrative *-n derivation" of [[在 (char)|在]] (OC \*zlɯːʔ) — a proposed morphological relationship, not just the visual resemblance the pre-existing note already flagged ("only one other character that looks like this one"). Stamped `date-last-perfect: 2026-07-26`. `mc_id: 562` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, matching the stand-in word `words/存在.md`'s own field.

**Body defects found**: beyond the semantic/phonetic swap, the SKIP/Stroke, MC rank, and Levels bullets were all missing outright, with the two CC initial/final links floating at the bottom instead; two Words entries (存在, 存亡) were bare wikilinks with no ruby; the stand-in 存在 itself needed adding; no `## Chengyu` despite a real hit (already documented on [[characters/体|体]]'s own page earlier this loop); no `## Derived Characters` despite four real hits.

**Words cross-check** (5 total ground-truth hits): 依存 already correctly ruby'd, kept; 保存 already correct; 存亡 reformatted to ruby+gloss; 2 missing — 存在 (stand-in), 生存 ("survive; life") — added from stored fields.

**Chengyu**: 1 ground-truth hit — 文体並存 ("styles coexist") — added.

**Derived Characters** (4 total ground-truth hits — characters naming 才 as their `graphemic_classification`): 材 ("material; stuff; talent"), 財 ("wealth"), 在 (char) ("exist," pipe-linked), 栽 ("plant; cultivate") — all four added.

**Verification**: Python cross-check of all 10 `<rt>` values (5 Words + 1 Chengyu + 4 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 440 — [[characters/婦 (char)|婦]]

Next never-perfected character by `danayo_id` (3076). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 帚` already correct — verified via Wiktionary: 形声 (OC \*bɯʔ), semantic [[Radical 038|女]] ("woman") + phonetic [[帚]] ("broom"). The Shuowen Jiezi's traditional "woman holding a broom" gloss — the source of the popular 会意 interpretation I initially suspected — is a Han-dynasty folk etymology layered onto what is structurally a phono-semantic character; modern reconstruction treats 帚 primarily as the phonetic element, rhyming with 婦's own OC reading. `mc_id: 477` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`; `words/婦.md` had no `pos` field of its own to inherit from.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite four ground-truth hits, including the stand-in itself; no `## Derived Characters` despite one real hit.

**Words cross-check** (4 total ground-truth hits): all four missing — 婦 (stand-in), 夫婦 ("couple"), 主婦 ("housewife"), 寡婦 ("widow") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 帚 as its `graphemic_classification`): 掃 ("sweep") — added.

**Verification**: Python cross-check of all 5 `<rt>` values (4 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 439 — [[characters/婚|婚]]

Next never-perfected character by `danayo_id` (3075). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 昏` already correct — verified via Wiktionary: 形声 (OC \*hmɯːn), semantic [[Radical 038|女]] ("woman") + phonetic [[昏]]. The traditional "dusk wedding" explanation (linking to 昏's "dusk" sense) dates only to the Han dynasty and is explicitly flagged as folk etymology by Wiktionary — Schuessler instead favors an association of femininity with darkness (cf. 陰/阴, yīn). Filled in the pre-existing bullet's blank gloss for 女 accordingly. `mc_id: 2021` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `実詞`, matching the stand-in word `words/結婚.md`'s own field.

**Body defects found**: all four Words entries were bare wikilinks with no ruby/gloss, plus a stray empty bullet at the end of the list — all reformatted; the two floating CC-initial/final links sat at the bottom of the file instead of embedded in the MC-rank bullet; SKIP/Stroke, MC rank, and Levels bullets were all missing.

**Words cross-check** (4 total ground-truth hits): 結婚 (stand-in), 婚姻, 離婚, 結婚礼 all reformatted from bare wikilinks to ruby+gloss; stand-in moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 昏` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 438 — [[characters/威|威]]

Next never-perfected character by `danayo_id` (3074). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[戌]] ("a weapon/halberd-type graph") and [[Radical 038|女]] ("woman"). No mother-in-law theory (sometimes attributed to Shuowen) appears on the page — Wiktionary presents 戌+女 without further semantic elaboration, ties 威 into a derivational family alongside 畏 ("to fear," the passive/experiencer counterpart of 威's active "instill awe" sense) and 鬼 ("ghost"). `mc_id: 387` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`; `words/威力.md` had a blank `pos` field too, with nothing to inherit from.

**Body defects found**: `## Notes` held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; the stand-in 威力 itself was missing from Words.

**Words cross-check** (3 total ground-truth hits): 権威, 脅威 already correctly ruby'd, kept; 1 missing — 威力 (stand-in) — added, moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 威` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 437 — [[characters/姓|姓]]

Next never-perfected character by `danayo_id` (3073). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 生` and `pos: 名詞` were both already correct. Verified via Wiktionary: 形声 (not 会意 as the pre-existing "Components:" bullet implied), semantic [[Radical 038|女]] ("woman") + phonetic [[生]] (OC \*sʰleːŋ, \*sreŋs) — 姓 is a specialized split from 性 ("innate nature; what is inborn"): "innate nature" → "surname, clan name." Deliberately left out the popular matrilineal-naming story, since Wiktionary's etymology section doesn't state it — flagged as a separate historical/cultural claim rather than folded into the formal etymology. `mc_id: 344` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Body defects found**: `## Words` sat before `## Notes`, which itself held only a non-canonical "Components:" bullet plus the two floating CC-initial/final links — all four canonical bullets written from scratch; the stand-in 姓氏 itself was missing from Words; no `## Derived Characters` despite seven real hits.

**Words cross-check** (2 total ground-truth hits): 姓名 already correctly ruby'd, kept; 1 missing — 姓氏 (stand-in) — added, moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 total ground-truth hits — characters naming 生 as their `graphemic_classification`): 甥 (char) ("sister's child; sororal niece or nephew," pipe-linked), 省 (char) ("government ministry," pipe-linked), 星 (char) ("star," pipe-linked), 青 (char) ("blue," pipe-linked), 牲 ("animal sacrifice"), 性 ("gender; sex; quality"), 笙 ("sheng (instrument)") — all seven added.

**Verification**: Python cross-check of all 9 `<rt>` values (2 Words + 7 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 436 — [[characters/始|始]]

Next never-perfected character by `danayo_id` (3072). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 台` already correct — verified via Wiktionary: 形声 (OC \*hljɯʔ), semantic [[Radical 038|女]] ("woman") + phonetic [[台 (char)|台]] (OC \*l̥ʰɯː, \*l'ɯː, \*lɯ) — no explicit semantic bridge from "woman" to "begin, start" is given in the source, so the bullet states the composition without inventing an unsourced narrative. `mc_id: 207` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`; the stand-in word `words/始作.md` had a blank `pos` field too, with nothing to inherit from.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus three Words entries (one bare wikilink, one already ruby'd, one with a non-canonical "abbreviation for" note) — all four canonical bullets written from scratch; 3 of 6 ground-truth words missing, including the stand-in 始作 itself; no `## Derived Characters` despite nine real hits, one of the largest phonetic families found this loop.

**Words cross-check** (6 total ground-truth hits): 原始, 始金 already correctly ruby'd, kept; 始祖 reformatted to ruby+gloss; 3 missing — 始作 (stand-in), 開始 ("begin; start"), 太始 ("beginning of all") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (9 total ground-truth hits — characters naming 台 as their `graphemic_classification`): 怠 ("idle; lazy"), 胎 ("fetus"), 苔 (char) ("moss; lichen," pipe-linked), 冶 ("smelt"), 殆 ("danger; jeopardy"), 治 ("govern; rule; administer"), 跆 ("trample"), 飴 ("syrup; candy"), 鮐 ("blowfish") — all nine added.

**Verification**: Python cross-check of all 15 `<rt>` values (6 Words + 9 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 435 — [[characters/妻 (char)|妻]]

Next never-perfected character by `danayo_id` (3071). **Frontmatter defect found and fixed**: `graphemic_classification: 屮` had zero scholarly support — verified via Wiktionary that 妻 is actually **会意**, not 形声 at all: 肀 ("hand grabbing hair," no vault page) + [[Radical 038|女]] ("woman"), depicting a man seizing a woman's hair, traditionally read as symbolizing marriage by capture/ownership. No mention of 屮 (chè, "sprout") anywhere in the source — that value appears to have been simply invented, the same class of error as [[characters/商|商]]'s 章 earlier this loop. Corrected the field to `會意`. Possibly cognate to 齊 (OC \*dzêi, "equal"), implying "equal to her husband" (deemed historically unlikely); Schuessler suggests an Austroasiatic origin (\*tshə̂i), comparing Middle Khmer "kansai" (wife). `mc_id: 491` cross-checked against `lookup/CC/CC 0000.md` — exact match. `pos: 名詞` was already correct.

**Body defects found**: the pre-existing "Components:" bullet listed 一 as a separate hairpin component, which Wiktionary doesn't isolate — it's folded into 肀 — corrected in the rewritten bullet; the SKIP/Stroke, MC rank, and Levels bullets were all missing outright, with both CC initial/final links floating at the top instead; 1 of 2 ground-truth words missing; 1 of 2 ground-truth chengyu missing; no `## Derived Characters` despite two real hits.

**Words cross-check** (2 total ground-truth hits): 妻 already present, kept; 1 missing — 妻子 ("women and children; wife and child") — added from stored fields.

**Chengyu** (2 total ground-truth hits): 結髪夫妻 already present, kept; 1 missing — 糟糠之妻 ("wife through thick and thin") — added.

**Derived Characters** (2 total ground-truth hits — characters naming 妻 as their `graphemic_classification`): 凄 ("miserable"), 棲 ("loft; perch") — both added. Confirmed no contradiction with 妻's own reclassification to 会意 — an ideograph can still serve as a legitimate phonetic donor for later 形声 characters, the same pattern seen on [[characters/充|充]] and [[characters/品 (char)|品]] earlier this loop.

**Verification**: Python cross-check of all 6 `<rt>` values (2 Words + 2 Chengyu + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 434 — [[characters/如 (char)|如]]

Next never-perfected character by `danayo_id` (3070). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 女` already correct — verified via Wiktionary: 形声 (not 会意 as the popular folk etymology suggests), semantic [[口 (char)|口]] ("mouth") + phonetic 女 (this character's own `radical` field, OC \*naʔ, \*nas, "woman"). The "woman who obeys orders" story is folk etymology, not scholarly — 女 contributes sound here, not the "woman" meaning; the "like, as, as if, equal to" sense ties to Sino-Tibetan cognates expressing correspondence/likeness (cf. Mizo *na nâ nâ*, "it being so; since") rather than deriving compositionally from the components. `mc_id: 59` cross-checked against `lookup/CC/CC 0000.md` — exact match (top-60 most frequent character in the corpus).

**Frontmatter**: `pos: ''` (empty string) → filled in as `関詞`, since 如's "like, as" sense functions as a comparative/relational marker; `words/如.md` had no `pos` field of its own to inherit from.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus one Words entry with a comma-joined bare gloss — all four canonical bullets written from scratch; the stand-in 如 itself was missing from Words; no `## Chengyu` despite two real hits; no `## Derived Characters` despite two real hits.

**Words cross-check** (2 total ground-truth hits): 如何 reformatted to ruby+gloss; 1 missing — 如 (stand-in) — added, moved to lead the list.

**Chengyu** (2 total ground-truth hits): both missing — 愛隣如自 ("love your neighbor as yourself"), 百聞不如一見 ("a hundred hearings can't match one seeing") — added.

**Derived Characters** (2 total ground-truth hits — characters naming 女 as their `graphemic_classification`): 汝 (char) ("you dear," pipe-linked), 奴 ("slave") — both added.

**Verification**: Python cross-check of all 6 `<rt>` values (2 Words + 2 Chengyu + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 433 — [[characters/壮|壮]]

Next never-perfected character by `danayo_id` (3068). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 爿` already correct — verified via Wiktionary: traditional 壯 is 形声 (OC \*ʔsraŋs), semantic [[士 (char)|士]] ("person, male adult") + phonetic 爿. The shinjitai/simplified 壮 retains the same phonetic relationship — Wiktionary states it's "simplified from 壯 (爿→丬)," a stroke-form reduction, not a component substitution — so unlike [[characters/仮|仮]]/[[characters/価|価]]/[[characters/写|写]] earlier this loop, no field correction was needed here. `mc_id: 1035` cross-checked against `lookup/CC/CC 1000.md` — exact match (traditional form 壯).

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, matching the stand-in word `words/壮大.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite two ground-truth hits, including the stand-in itself; no `## Derived Characters` despite two real hits.

**Words cross-check** (2 total ground-truth hits): both missing — 壮大 (stand-in), 壮族 ("Zhuang ethnicity") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 爿 as their `graphemic_classification`): 状 ("form; shape"), 将 (char) ("will; shall," pipe-linked) — both added.

**Verification**: Python cross-check of all 4 `<rt>` values (2 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 432 — [[characters/墨|墨]]

Next never-perfected character by `danayo_id` (3067). **Frontmatter defect found and fixed**: `graphemic_classification: 會意` was wrong — Wiktionary confirms 墨 is **形声**, not a compound ideograph: semantic [[Radical 032|土]] ("earth, soil" — reflecting ink's association with earthy, soot-like pigment substances) + phonetic 黑 (OC \*hmlɯːɡ, "black," no vault page), which supplies both the sound and the "black" sense. Corrected the field to `黑` — the fourth 会意→形声-direction correction this loop, after [[characters/充|充]], [[characters/勢|勢]], and [[characters/命|命]]. Stamped `date-last-perfect: 2026-07-26`. `mc_id: 856` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/墨水.md`'s own field.

**Body defects found**: `## Notes` held only the two floating CC-initial/final links plus one Words entry (墨素) stranded inside it — all four canonical bullets written from scratch; the stand-in 墨水 was missing from Words; no `## Chengyu` despite a real hit.

**Words cross-check** (3 total ground-truth hits): 墨西哥 already present, kept; 墨素 moved out of Notes into Words (kept its ruby); 1 missing — 墨水 (stand-in) — added, moved to lead the list.

**Chengyu**: 1 ground-truth hit — 道活墨殺 ("the Spirit gives life, but the Letter kills") — added.

**Derived Characters**: none (`graphemic_classification: 黑` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 431 — [[characters/堅|堅]]

Next never-perfected character by `danayo_id` (3066). **Body defect found and fixed**: the pre-existing graphemic bullet had semantic and phonetic reversed — it read "semantic [[臤]] (blank gloss) + phonetic [[Radical 032|土]]," but Wiktionary confirms the actual relationship is the opposite: semantic [[Radical 032|土]] ("earth" — the hardness/firmness of packed ground) + phonetic [[臤]] (OC \*kʰaːn, \*kʰriːn, \*ɡiːn, \*kʰins, no vault page). The `graphemic_classification: 臤` field itself was already correct (it properly stores the phonetic donor per convention); only the prose description in the body had the roles swapped. Corrected the bullet accordingly. Stamped `date-last-perfect: 2026-07-26`. `mc_id: 756` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, matching the stand-in word `words/堅硬.md`'s own field.

**Body defects found**: beyond the semantic/phonetic swap, the SKIP/Stroke, MC rank, and Levels bullets were all missing outright, with the two CC initial/final links floating between Words entries; two Words entries (堅硬, 堅牢) were bare wikilinks with no ruby.

**Words cross-check** (5 total ground-truth hits): 堅持, 堅魚, 堅鳥 already correctly ruby'd, kept; 堅硬 (stand-in), 堅牢 reformatted to ruby+gloss; stand-in moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 total ground-truth hits — characters naming 臤 as their `graphemic_classification`): 緊 ("tense; tight; firm"), 賢 ("wise"), 腎 ("kidney") — all three added.

**Verification**: Python cross-check of all 8 `<rt>` values (5 Words + 3 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 430 — [[characters/執|執]]

Next never-perfected character by `danayo_id` (3065). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of 㚔 ("criminal; handcuffs") and 丮 ("hand," neither with a vault page) — the oracle-bone/bronze forms depict 梏人雙手, "the shackled hands of a person," restraint/seizure of a captive; in the modern glyph these components have been distorted into 幸-like and 丸-like shapes. "To hold in the hand" → "to hold (power), manage" → "to arrest, capture." Checked whether the character's own `radical: 土` is a meaningfully depicted component — neither 㚔 nor 丮 relates to earth/soil at all, so (as with 丙/也/余/凡/商 earlier this loop) this is purely a Kangxi-filing artifact, and the bullet correctly omits a forced radical link. `mc_id: 340` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`, matching the stand-in word `words/執行.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite two ground-truth hits, including the stand-in itself; no `## Derived Characters` despite three real hits.

**Words cross-check** (2 total ground-truth hits): both missing — 執行 (stand-in), 固執 ("stubborn; stick to") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 total ground-truth hits — characters naming 執 as their `graphemic_classification`): 墊 (char) ("mat; pad; cushion," pipe-linked), 蟄 (char) ("hibernate," pipe-linked), 摯 ("sincere; warm; cordial") — all three added.

**Verification**: Python cross-check of all 5 `<rt>` values (2 Words + 3 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 429 — [[characters/均 (char)|均]]

Next never-perfected character by `danayo_id` (3064). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 勻` already correct — verified via Wiktionary: 形声 (OC \*kʷin), semantic [[Radical 032|土]] ("earth") + phonetic [[勻]] (OC \*ɢʷin). `mc_id: 1164` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`; `words/均.md` had no `pos` field of its own to inherit from.

**Body defects found**: the disambiguation callout used generic placeholder text ("This page is about the character.") instead of naming 均 — normalized to the standard template; two duplicate `## Notes` headings existed, the first holding only the floating CC-initial/final links, the second holding the real (already-accurate) graphemic bullet with a malformed non-wikilink phonetic reference (`[匀](勻.md)`) — merged into one canonical section, SKIP/Stroke/MC-rank/Levels bullets written from scratch; the stand-in 均 itself and 平均 were missing from Words.

**Words cross-check** (4 total ground-truth hits): 不均, 均衡 already present, kept; 2 missing — 均 (stand-in), 平均 ("average; balance; find the mean") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 勻` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 428 — [[characters/園|園]]

Next never-perfected character by `danayo_id` (3063). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 袁` already correct, and the pre-existing graphemic bullet was already accurate — verified via Wiktionary: 形声 (OC \*ɢʷan), semantic [[Radical 031|囗]] ("fence") + phonetic [[袁]] (OC \*ɢʷan). `mc_id: 1168` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/庭園.md`'s own field.

**Body defects found**: the SKIP/Stroke, MC rank, and Levels bullets were all missing outright, with the two CC initial/final links floating between two Words entries instead; two Words entries (園芸, 園丁) were bare wikilinks with no ruby/gloss; the stand-in 庭園 itself was missing; no `## Derived Characters` despite two real hits.

**Words cross-check** (5 total ground-truth hits): 公園, 幼稚園 already correctly ruby'd, kept; 園芸, 園丁 reformatted to ruby+gloss; 1 missing — 庭園 (stand-in) — added, moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 袁 as their `graphemic_classification`): 猿 ("ape; monkey"), 遠 (char) ("far," pipe-linked) — both added.

**Verification**: Python cross-check of all 7 `<rt>` values (5 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 427 — [[characters/困|困]]

Next never-perfected character by `danayo_id` (3062). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[Radical 031|囗]] ("surround, enclosure") and [[木 (char)|木]] ("wood"). Corrected my own initial hypothesis before it went in the bullet: I'd guessed "a withering tree trapped in an enclosure," which turned out to be wrong — Wiktionary instead states 困 is probably the original form of 梱 and 閫 (both "doorsill"), wood framed/enclosed to suggest a door's wooden sill; the "distressed, trapped" sense is a later extension ("surrounded, besieged, trapped" → "difficult" → regionally "sleepy, hungry"), not the primary depicted meaning. `mc_id: 777` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `修飾語`, matching the stand-in word `words/疲困.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus one Words entry stranded inside it — all four canonical bullets written from scratch; `## Words` didn't exist as its own heading; the stand-in 疲困 itself was missing.

**Words cross-check** (2 total ground-truth hits): 困難 already correctly ruby'd, moved out of Notes into its own Words heading; 1 missing — 疲困 (stand-in) — added, leading the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 困` matches no other character) — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 426 — [[characters/喪|喪]]

Next never-perfected character by `danayo_id` (3061). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct, with a nuance worth documenting: Wiktionary actually tags this 會意兼形聲 (compound-ideograph-cum-phono-semantic) — [[哭 (char)|哭]] ("to cry, wail") + 亡 (appearing here as its seal-script variant 亾, "to perish, be lost"), where 亡 supplies both meaning *and* sound rather than acting as a pure second ideograph. Since the checklist's binary framework doesn't have a slot for this hybrid case, kept the field at `會意` (the closer of the two fits, matching the pre-existing value) and documented the phonetic contribution in the bullet rather than force-fitting a bare phonetic-component field. OC \*smaːŋs, with an *s- nominalizing/circumstantial prefix ("the circumstances of a death") — "crying" + "death/disappearance" → mourning, loss. `mc_id: 408` cross-checked against `lookup/CC/CC 0000.md` — exact match. `pos: 事詞` was already correct.

**Body defects found**: `## Notes` held only a non-canonical "Components:" bullet, the two floating CC-initial/final links, and the sole Words entry (喪失) stranded inside it with a bare gloss instead of ruby — all four canonical bullets written from scratch; `## Words` didn't exist as its own heading.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 喪失 — moved out of Notes and reformatted to ruby+gloss.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 喪` matches no other character) — correctly omitted.

**Verification**: Python cross-check of the 1 `<rt>` value against the cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 425 — [[characters/商|商]]

Next never-perfected character by `danayo_id` (3060). **Frontmatter defect found and fixed**: `graphemic_classification: 章` had zero support — fetched Wiktionary's raw Glyph-origin wikitext directly and confirmed the character's formation is explicitly called "unclear": the base component is consistently 丙, with late-period variants adding 口 below, but the element sitting atop 丙 varies across six different attested oracle-bone/bronze forms with no settled identification of what it depicts (an inverted triangle+bar, a 辛-like form, a bare triangle possibly the original 樴, symmetrical paired elements, and star-marked variants possibly tied to the Shāng star). No 象形/指事/會意/形聲 label appears anywhere in the source section, and no phonetic component is ever identified — 章 was simply invented or mistranscribed. Corrected the field to `象形`, framed as origin-uncertain, following the same template established on [[characters/丙 (char)|丙]] and [[characters/也 (char)|也]] earlier this loop. Stamped `date-last-perfect: 2026-07-26`. `mc_id: 492` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/商業.md`'s own field.

**Body defects found**: a non-standard blockquote callout ("Not a word on it's own: requires: 商業. However, it is a dynasty/surname.") sat where the standard disambiguation callout would go, but 商 has no `words/商.md` collision, so this doesn't fit the checklist's callout template at all — removed and its genuinely useful content (bound-only status, dynasty/surname usage) folded into the graphemic bullet instead; the two floating CC-initial/final links and a dash-comma Words entry (商店) were stranded mid-document with no SKIP/Stroke, MC-rank, or Levels bullets present — all four canonical bullets written from scratch; the stand-in 商業 itself was missing from Words.

**Words cross-check** (3 total ground-truth hits): 商路 already correct, kept; 商店 reformatted from dash-gloss to ruby+gloss; 1 missing — 商業 (stand-in) — added, moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 商` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 424 — [[characters/品 (char)|品]]

Next never-perfected character by `danayo_id` (3059). **Frontmatter defect found and fixed**: `graphemic_classification: 指事` contradicted the page's own body bullet, which already correctly described "会意: Triplication of 口, representing various objects" — verified via Wiktionary, which gives no 指事 analysis at all and confirms 会意 as the actual classification. Corrected the field to `會意`. Triplication of [[Radical 030|口]] ("mouth") represents a multiplicity of items/things, underlying the later senses "article, product" and "grade, rank." Also occurs in 區 (no vault page). Stamped `date-last-perfect: 2026-07-26`. `mc_id: 1854` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`; `words/品.md` had no `pos` field of its own to inherit from.

**Body defects found**: two duplicate `## Notes` headings existed in the same file, the first empty, the second holding the real bullet plus one Words entry with a dash-separated gloss and the two floating CC-initial/final links wedged in the middle of more Words entries — merged into one canonical Notes section with all four bullets (SKIP/Stroke, MC rank, Levels written from scratch); 2 of 6 ground-truth words missing, including the stand-in 品 itself; no `## Derived Characters` despite one real hit.

**Words cross-check** (6 total ground-truth hits): 新品 reformatted from dash-gloss to ruby+gloss; 貢品 already correct, kept; 品詞, 品目 reformatted from bare wikilinks to ruby+gloss; 2 missing — 品 (stand-in), 製品 ("product; produce; goods") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 品 as its `graphemic_classification`): 臨 ("draw near; approach") — added.

**Verification**: Python cross-check of all 7 `<rt>` values (6 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 423 — [[characters/哀|哀]]

Next never-perfected character by `danayo_id` (3058). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 衣` already correct — verified via Wiktionary: 形声 (OC \*qɯːl), semantic [[Radical 030|口]] ("mouth" — wailing, crying out) + phonetic [[衣]]. Per Schuessler (2007), likely sound-symbolic in origin, belonging to a phonetic series of related "mournful, lamenting" words connected as much by sound pattern as by strict semantic derivation — the 形声 analysis is somewhat conventional rather than purely compositional. `mc_id: 458` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `実詞`, matching the stand-in word `words/哀傷.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus two Words entries with malformed comma-joined/missing glosses — all four canonical bullets written from scratch; the stand-in 哀傷 itself was missing from `## Words`; 2 of 4 ground-truth chengyu missing; no `## Derived Characters` despite one real hit.

**Words cross-check** (4 total ground-truth hits): 哀戚 already correctly ruby'd, kept; 哀悼, 哀求 reformatted to ruby+gloss; 1 missing — 哀傷 (stand-in) — added, moved to lead the list.

**Chengyu** (4 total ground-truth hits): 喜怒哀楽, 哀鴻遍野 already present, kept; 2 missing — 加哀痛産 ("add sorrow to painful labor"), 詛地哀食 ("cursed ground, sorrowful eating") — both Biblical in origin — added from stored fields.

**Derived Characters** (1 total ground-truth hit — the character naming 衣 as its `graphemic_classification`): 依 (char) ("rely on; accord with," pipe-linked) — added.

**Verification**: Python cross-check of all 9 `<rt>` values (4 Words + 4 Chengyu + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 422 — [[characters/命|命]]

Next never-perfected character by `danayo_id` (3057). **Frontmatter defect found and fixed**: `graphemic_classification: 會意` was wrong — Wiktionary classifies 命 as **形声**, not a compound ideograph: semantic [[Radical 030|口]] ("mouth") + phonetic [[令 (char)|令]]. My initial hypothesis (令+口 as a "spoken command" 会意 ideograph) was plausible-sounding but wrong — Wiktionary instead traces a shared root with 名 ("name"): "name" → "to name, give a name to" → "to order, command" → "order, command" → "destiny, fate, lot" → "life," explicitly paralleled to Latin *fāta* ("fate") from *fātus* ("spoken"). Corrected the field to `令`, the third 会意→形声-direction correction this loop (after [[characters/勢|勢]]). Stamped `date-last-perfect: 2026-07-26`. `mc_id: 139` cross-checked against `lookup/CC/CC 0000.md` — exact match (top-150 most frequent character in the corpus).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/運命.md`'s own field.

**Body defects found**: the Notes bullet compressed SKIP/Stroke/syllable/MC-initial/MC-final into a single non-canonical line using "·" separators instead of the four distinct bullets — rewritten from scratch; both Words entries were bare wikilinks with no ruby/gloss; 7 of 9 ground-truth words missing, including the stand-in 運命 itself; 1 of 2 ground-truth chengyu missing; no `## Derived Characters` despite nine real hits.

**Words cross-check** (9 total ground-truth hits): 命運, 命名 reformatted to ruby+gloss; 7 missing — 運命 (stand-in), 命令 ("decree; order; command"), 生命 ("life"), 寿命 ("age; lifespan"), 宿命 ("destiny; fate"), 薄命 ("born under an unlucky star; ill-fated"), 革命 ("revolt against; incite revolution; rebel against") — all added from stored fields.

**Chengyu** (2 total ground-truth hits): 安心立命 already present, kept; 1 missing — 佳人薄命 (already documented on [[characters/佳 (char)|佳]]'s own page earlier this loop) — added here too.

**Derived Characters** (9 total ground-truth hits — characters naming 令 as their `graphemic_classification`, tied for the largest phonetic family found this loop): 冷 (char) ("cool; cold," pipe-linked), 零 (char) ("zero," pipe-linked), 伶 ("clever"), 玲 ("jade"), 鈴 (char) ("small bell," pipe-linked), 笭 ("bamboo screen"), 羚 ("antelope"), 領 ("territory"), 齢 ("age; years") — all nine added.

**Verification**: Python cross-check of all 20 `<rt>` values (9 Words + 2 Chengyu + 9 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 421 — [[characters/吹 (char)|吹]]

Next never-perfected character by `danayo_id` (3054). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[Radical 030|口]] ("mouth") and [[欠 (char)|欠]] ("to open the mouth wide, to exhale") — the literal action of blowing air through an open mouth, combining iconically rather than phonetically. An archaic variant form 龡 also exists (not added as an alias — no independent evidence it's tracked elsewhere in this vault). `mc_id: 1838` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`; `words/吹.md` had no `pos` field of its own to inherit from.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite one real hit.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 吹 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 吹 as its `graphemic_classification`): 炊 (char) ("cook," pipe-linked due to the `words/炊.md` collision) — added.

**Verification**: Python cross-check of both `<rt>` values (1 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 420 — [[characters/只 (char)|只]]

Next never-perfected character by `danayo_id` (3052). **Frontmatter defect found and fixed**: `aliases` listed `戠`, which turned out to be a genuinely different, unrelated character (zhī/zhí, "clay/sword/to gather," 会意 of 音+弋) — its only real connection to 只 is that Simplified Chinese substitutes 只 as the phonetic component *inside other compounds* (職→职, 織→织, 識→识), not as an alias of 只 itself. Confirmed by cross-checking this vault's own data: the four characters that cite 戠 as their `graphemic_classification` (織, 職, 識, 幟 (char)) are unrelated to 只's own page and don't belong in its Derived Characters section either. Removed 戠 from `aliases`. Kept 衹 (a legitimate alternate traditional form of 只 itself) and 隻 (zhī, "classifier for one bird/pair" — a genuinely distinct, etymologically unrelated character, 会意 of 隹+又, that merely merges into 只 under mainland Simplified Chinese; kept as an alias to reflect that real orthographic merger, same treatment this vault gives other simplification mergers). `graphemic_classification: 象形` already correct — verified via Wiktionary: airflow coming out of a mouth (口, this character's own radical), a modal particle, compared to 四 and 曰. Stamped `date-last-perfect: 2026-07-26`. `mc_id: 2110` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `関詞`, matching the stand-in word `words/只.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite the stand-in itself being a ground-truth hit.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 只 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 只` matches no other character) — correctly omitted.

**Verification**: Python cross-check of the 1 `<rt>` value against the cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 419 — [[characters/叔|叔]]

Next never-perfected character by `danayo_id` (3050). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 尗` already correct — verified via Wiktionary: 会意/形声, phonetic 尗 (OC \*hljɯwɢ, "wooden stake" — not "beans" as I initially suspected) + semantic [[又 (char)|又]] ("hand") — literally "using a wooden stake to dig the ground." The "uncle" meaning is a phonetic loan/rebus borrowing unrelated to that original digging sense, not a semantic extension — worth flagging since a "pick up beans → uncle" narrative would have been plausible-sounding but wrong. `mc_id: 353` cross-checked against `lookup/CC/CC 0000.md` — exact match. `pos: 名詞` was already correct.

**Body defects found**: `## Words` sat before `## Notes`, which itself held only a non-canonical "Components:" bullet plus the two floating CC-initial/final links — all four canonical bullets written from scratch; 1 of 3 ground-truth words missing; no `## Derived Characters` despite one real hit.

**Words cross-check** (3 total ground-truth hits): 叔父 (stand-in), 叔叔 already present, kept, reordered so the stand-in leads; 1 missing — 叔母 ("aunt") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 尗 as its `graphemic_classification`): 戚 ("grieving; sorrowful") — added.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 418 — [[characters/又 (char)|又]]

Next never-perfected character by `danayo_id` (3047). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 象形` already correct — verified via Wiktionary: depicts a right hand, the original form of [[右]] ("right (direction)"), which later split off as a dedicated derivative. Interesting semantic note: the "again, also" sense isn't a direct pictographic extension — Wiktionary treats it as an adverbial derivation of [[有 (char)|有]] (OC \*ɢʷɯʔ, "to have; there is"), inherited via sound and semantic root rather than the hand image itself. `mc_id: 147` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `副詞`, since 又's primary usage is adverbial (modifying a verb, "again, once more") rather than fitting a Linker/conjunction role; no sibling word file was available to cross-check against.

**Body defects found**: `# Notes` used H1 instead of H2 and held only a bare numbered list of glosses plus the two floating CC-initial/final links — all four canonical bullets written from scratch; `## Words` didn't exist despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite five real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 又 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 total ground-truth hits — characters naming 又 as their `graphemic_classification`): 有 (char) ("have," pipe-linked due to the `words/有.md` collision), 友 ("friend"), 尤 ("especially; particularly; more so"), 馭 ("drive"), 右 ("right (direction)") — all five added.

**Verification**: Python cross-check of all 6 `<rt>` values (1 Words + 5 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 417 — [[characters/厳 (char)|厳]]

Next never-perfected character by `danayo_id` (3046). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 敢` already correct — verified via Wiktionary: traditional 嚴 is 形声 (OC \*ŋam), semantic 喦/吅 ("talkative") + phonetic 敢 (OC \*klaːmʔ, "daring") — the "solemn, stern" sense may be a phonetic-loan development rather than transparent from 敢's meaning. The shinjitai 厳 **retains 敢 intact and unchanged**; only the top semantic component (吅→𭕄) was simplified, the same pattern as 單→単 — so unlike [[characters/仮|仮]]/[[characters/価|価]], no phonetic substitution occurred here and the field needed no correction. `mc_id: 817` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 嚴).

Noteworthy cross-check: this character's `middle_chinese_final: iɐm` (plain *i*) doesn't literally match `lookup/CC/finals/韻 凡.md`'s own stored value `ɨɐm` (barred *ɨ*) character-for-character — initially looked like a possible transcription slip. But `characters/剣 (char).md`, already perfected in this loop back on 2026-06-15, established the precedent: link to 韻 凡 regardless, displaying the character's *own* frontmatter IPA string (plain *i*) as the bullet's pipe-alias text. Followed that same convention here rather than treating the near-miss as a fresh error to "fix."

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`. `hsk_level: ""` (explicit empty string) → filled in as `無`, since 厳 is a Japan-only shinjitai form (mainland Simplified Chinese uses 严, not 厳).

**Body defects found**: the graphemic bullet was missing entirely, with the two floating CC-initial/final links wedged between two Words entries stranded inside Notes, one (厳重) a bare wikilink with a malformed comma-joined gloss — all four canonical bullets written from scratch; 3 of 6 ground-truth words missing, including the stand-in 厳 itself.

**Words cross-check** (6 total ground-truth hits): 厳然, 厳粛 already present, kept; 厳重 moved out of Notes and reformatted; 3 missing — 厳 (stand-in), 嚴禁 ("strictly forbidden; strictly prohibit"), 尊厳 ("dignity; sanctity") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 敢 as their `graphemic_classification`): 橄 ("olive"), 瞰 ("look down from a height; overlook; survey") — both added.

**Verification**: Python cross-check of all 8 `<rt>` values (6 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 416 — [[characters/原|原]]

Next never-perfected character by `danayo_id` (3045). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[Radical 027|厂]] ("cliff") and [[泉]] ("spring") — a spring emerging from a cliff-face, the pictorial source of "origin, source." "Spring bursting from a cliff" → "source" → "origin, original, basic, primary," possibly overlapping semantically with 元; the separate "plain, plateau" sense later split off onto a dedicated variant graph, 塬 (no vault page). `mc_id: 545` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, matching the stand-in word `words/原始.md`'s own field.

**Body defects found**: the graphemic bullet was missing entirely, replaced by the two floating CC-initial/final links plus a Words entry (原来) stranded inside Notes — all four canonical bullets written from scratch; 4 of 9 citable ground-truth words missing; no `## Derived Characters` despite two real hits.

**Words cross-check** (10 total ground-truth hits, 9 citable): 原始 (stand-in), 原理, 原罪, 原則 already present, kept; 原来 moved out of Notes; 4 missing — 原因 ("reason; cause"), 原子 ("atom"), 水原 ("Suwon; Mizuhara"), 草原 ("grassland; prairie; steppe; savanna; meadow") — added from stored fields. **Flagged, not added**: 中原 ("Central Plains") is a real ground-truth hit but `words/中原.md` itself has no stored `注音` field (only `羅馬字`/`諺文`) — left out rather than reverse-engineering a Bopomofo value from its component syllables, since that would mean inventing data instead of citing it; this is a pre-existing gap on the word's own page, outside this character page's fixing scope.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 原 as their `graphemic_classification`): 源 ("origin; spring"), 願 ("request") — both added.

**Verification**: Python cross-check of all 11 `<rt>` values (9 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 415 — [[characters/厚 (char)|厚]]

Next never-perfected character by `danayo_id` (3044). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[Radical 027|厂]] ("cliff; cave on a cliff") and 𣆪 ("jug" — per Shuowen, an inverted 亯; no vault page). Noted honestly that the semantic bridge from "cliff + inverted jug" to "thick, substantial" is not spelled out anywhere in the source — treated as an attested component breakdown rather than a fully transparent derivation, rather than inventing an unsourced semantic narrative. `mc_id: 456` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, since 厚's own gloss "thick" is a descriptive adjective and the stand-in word `words/厚.md` had no `pos` field of its own to inherit from.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite four ground-truth hits, including the stand-in itself; no `## Chengyu` despite a real hit.

**Words cross-check** (4 total ground-truth hits): all four missing — 厚 (stand-in), 濃厚 ("concentrated; thick; dense; strong"), 敦厚 ("honest; candid; sincere"), 厚顔 ("brazen-faced; impudent; shameless") — added from stored fields.

**Chengyu**: 1 ground-truth hit — 厚顔無恥 ("shameless and brazen") — added.

**Derived Characters**: none (`graphemic_classification: 厚` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values (4 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 414 — [[characters/卵|卵]]

Next never-perfected character by `danayo_id` (3043). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 象形` already correct — verified via Wiktionary: depicts spawn, an egg. Checked whether the character's own `radical: 卩` is a meaningfully depicted part of the pictograph (as with [[characters/其 (char)|其]]'s genuine 八 legs) or just a Kangxi-indexing artifact (as with 丙/也/余/凡) — Wiktionary is silent on this specific point and only gives the bare structural decomposition, so the bullet describes the pictograph without forcing an unsupported radical link either way. `mc_id: 1893` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/卵子.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 2 of 3 ground-truth words missing.

**Words cross-check** (3 total ground-truth hits): 卵子 (stand-in) already present, kept; 2 missing — 卵白 ("egg white; albumen"), 鶏卵 ("chicken eggs") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 卵` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 413 — [[characters/協|協]]

Next never-perfected character by `danayo_id` (3041). **`mc_id` off-by-one caught and fixed**: stored value 1863 actually belongs to 腫 ("swelling"); 協 itself sits at rank 1862 in `lookup/CC/CC 1000.md` (verified by reading the surrounding lines directly — 1861. 壅, 1862. 協, 1863. 腫). This is the same bug class the checklist already documents (艮, 煌 — both off by one, both citing the entry immediately *before* the correct one); this case is the mirror image, citing the entry immediately *after*. Corrected `mc_id` to `1862`. `graphemic_classification: 劦` already correct — verified via Wiktionary's raw etymology template: 協 is 形声, but not a simple "力×3 (劦) + 十 (many)" compound as I initially suspected — it's actually **a variant form of 劦 itself** ("to collaborate," supplying both the sound and the meaning) with phonetic 十 added purely as an extra sound-component, contributing no semantics of its own. Stamped `date-last-perfect: 2026-07-26`. `pos: 事詞` was already correct.

**Body defects found**: the Notes section had a non-canonical "Components:" bullet plus the two floating CC-initial/final links and three Words entries stranded inside it — all four canonical bullets written from scratch; one Words entry (協会) was a bare wikilink with a malformed comma-joined gloss; 2 of 5 ground-truth words missing, including the stand-in 協力 itself; no `## Derived Characters` despite one real hit.

**Words cross-check** (5 total ground-truth hits): 協会 reformatted to ruby+gloss; 協定, 協議 already correct, kept; 2 missing — 協力 (stand-in), 妥協 ("compromise; settle") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 劦 as its `graphemic_classification`): 脅 ("threaten") — added.

**Verification**: Python cross-check of all 6 `<rt>` values (5 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 412 — [[characters/匹 (char)|匹]]

Next never-perfected character by `danayo_id` (3040). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 八` already correct — verified via Wiktionary: this is a genuinely contested glyph. Per the Shuowen (the analysis matching the stored field), 匹 is 形声: phonetic [[八 (char)|八]] ("eight" — referring to eight folds in one 匹 of cloth) + semantic [[Radical 023|匸]] ("to conceal," indicating concealment of the two ends). Wiktionary also documents two competing theories: a pure pictogram of "folds in cloth," and an ideogram reading as "half of 丙" (one horse split from a pair). Alternative form 疋 is directly tied to the etymology. `mc_id: 1079` cross-checked against `lookup/CC/CC 1000.md` — exact match. `pos: 量詞` was already correct.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite three real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 匹 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 total ground-truth hits — characters naming 八 as their `graphemic_classification`): 叭 ("trumpet"), 屑 (char) ("scraps; waste tidbits," pipe-linked), 穴 ("cave") — all three added.

**Verification**: Python cross-check of all 4 `<rt>` values (1 Words + 3 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 411 — [[characters/勧|勧]]

Next never-perfected character by `danayo_id` (3039). **Frontmatter defect found and fixed**: `graphemic_classification: 鸛` was wrong — verified via Wiktionary that traditional 勸's real phonetic component is **雚** ("stork" phonetic-series root, cf. 歓/観/権/灌), not **鸛** ("stork" itself), which is a *derived* character built from 雚+鳥 — the same "cited a downstream sibling instead of the true phonetic root" mistake pattern as [[characters/勤|勤]]'s 菫/堇 mix-up last iteration. Confirmed no other character in this vault cites 鸛 as a phonetic donor, reinforcing that the stored value was simply an error. Corrected the field to `雚` (no vault page). The modern shinjitai 勧 retains the same phonetic identity as 勸 — its right-hand component is only a stroke-simplified rendering of 雚, not a substitution (unlike the [[characters/仮|仮]]/[[characters/価|価]]/[[characters/写|写]] cases earlier this loop, where the shinjitai genuinely swapped in an unrelated component). Stamped `date-last-perfect: 2026-07-26`. `mc_id: 995` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 勸).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/勧告.md`'s own field. `hsk_level: ""` (explicit empty string) → filled in as `無`, since 勧 is a Japan-only shinjitai form (mainland Simplified Chinese uses 劝, not 勧).

**Body defects found**: `## Notes` held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; no `## Derived Characters` despite four real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 勧告 — already present and correctly formatted, labeled as stand-in.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 total ground-truth hits — characters naming 雚 as their `graphemic_classification`): 歓 ("glad; happy"), 灌 ("pour; irrigate"), 観 ("observe"), 権 ("power; right; authority") — all four added.

**Verification**: Python cross-check of all 5 `<rt>` values (1 Words + 4 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 410 — [[characters/勤|勤]]

Next never-perfected character by `danayo_id` (3038). **Frontmatter defect found and fixed**: `graphemic_classification: 菫` was wrong — Wiktionary confirms 勤's real phonetic component is **堇** ("clay, dry earth," OC \*ɡrɯn/\*kɯnʔ), not 菫 ("celery, aconite," OC unrelated) — two visually similar but etymologically distinct characters. Confirmed 菫 is a genuinely different, unrelated character already in this vault (`characters/菫.md`, its own `danayo_id: 8604`, `stand_in: 名専字`) rather than a variant form, ruling out any possibility the stored value was intentional. Corrected the field to `堇` (no vault page of its own). 形声: semantic [[Radical 019|力]] ("strength, effort") + phonetic 堇 — 力 grounds the meaning in "toil, exertion," combined with 堇's sound to yield "diligence, hard work." Stamped `date-last-perfect: 2026-07-26`. `mc_id: 1108` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, matching the stand-in word `words/勤勉.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus two Words entries stranded inside Notes, one with a malformed comma-joined gloss — all four canonical bullets written from scratch; `## Words` didn't exist as its own heading; 1 of 3 ground-truth words missing; no `## Derived Characters` despite one real hit.

**Words cross-check** (3 total ground-truth hits): 勤勉 (stand-in), 缺勤 moved out of Notes and reformatted; 1 missing — 出勤 ("go to work") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 堇 as its `graphemic_classification`): 饉 ("famine") — added.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 409 — [[characters/勢|勢]]

Next never-perfected character by `danayo_id` (3037). **Frontmatter defect found and fixed**: `graphemic_classification: 會意` was wrong — verified via Wiktionary that 勢 is actually **形声**, not a compound ideograph at all: phonetic 埶 (OC \*ŋeds, no vault page) + semantic [[Radical 019|力]] ("power, force"). Corrected the field to `埶`, the opposite-direction counterpart of [[characters/充|充]]'s correction earlier this loop (that one went 形声→会意; this one goes 会意→形声). Genuinely interesting etymological detail: Wiktionary treats 勢 as a nominalization of [[設]] (OC \*ŋ̊et, "to set up"), so it originally meant "that which is set up" — a configuration or circumstance — from which "power; influence; momentum; tendency" developed, with a Han Feizi quotation cited illustrating the 設/勢 connection. Stamped `date-last-perfect: 2026-07-26`. `mc_id: 739` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/勢力.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite three ground-truth hits, including the stand-in itself; no `## Derived Characters` despite two real hits.

**Words cross-check** (3 total ground-truth hits): all three missing — 勢力 (stand-in), 情勢 ("situation; circumstances"), 姿勢 ("posture") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 埶 as their `graphemic_classification`): 熱 (char) ("heat up; be hot," pipe-linked), 設 ("establish; build" — also cross-referenced in the graphemic bullet as 勢's own nominalization source) — both added.

**Verification**: Python cross-check of all 5 `<rt>` values (3 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 408 — [[characters/務|務]]

Next never-perfected character by `danayo_id` (3036). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 敄` already correct — verified via Wiktionary: 形声 (OC \*moɡs), semantic [[Radical 019|力]] ("strength, effort") + phonetic 敄 (OC \*moʔ, \*mos, no vault page) — "to exert oneself," consistent with the derived senses "affairs, duty, to serve, to strive at." `mc_id: 646` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`, matching the stand-in word `words/服務.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links — all four canonical bullets written from scratch; 3 of 5 ground-truth words missing.

**Words cross-check** (5 total ground-truth hits): 服務 (stand-in), 国務領 already present, kept; 3 missing — 服務員 ("server; waiter"), 事務所 ("office building; firm; agency"), 乗務 ("crew duty; serve as crew") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 敄` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 407 — [[characters/勉 (char)|勉]]

Next never-perfected character by `danayo_id` (3035). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 免` and `pos: 事詞` were both already correct. Verified via Wiktionary: 形声 (OC \*mronʔ), semantic [[Radical 019|力]] ("strength, effort") + phonetic 免 (OC \*mronʔ, identical to 勉's own value as expected for a phonetic donor) — "to make a strong effort." `mc_id: 1454` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Body defects found**: `## Notes` held only the two floating CC-initial/final links plus a non-canonical "Components:" bullet — all four canonical bullets written from scratch; 1 of 4 ground-truth words missing, namely the stand-in 勉 itself; no `## Derived Characters` despite four real hits.

**Words cross-check** (4 total ground-truth hits): 勤勉, 勉励, 勉強 already present, kept; 1 missing — 勉 (stand-in) — added, moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 total ground-truth hits — characters naming 免 as their `graphemic_classification`): 晩 (char) ("evening," pipe-linked), 冕 ("crown"), 娩 ("give birth"), 挽 ("recover") — all four added.

**Verification**: Python cross-check of all 8 `<rt>` values (4 Words + 4 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 406 — [[characters/効|効]]

Next never-perfected character by `danayo_id` (3034). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 交` already correct — but with a genuinely different shinjitai pattern from the 仮/価/写 cases earlier this loop: here the **phonetic** component (交) stays fully intact and legible in the shinjitai, while the **semantic** component is what changed — traditional 效/傚 pair 交 with 攵 ("to strike; action"), while the shinjitai 効 swaps in [[Radical 019|力]] ("strength, effort," matching this character's own `radical` field) instead — a semantic-radical substitution, not a phonetic one, and not a stroke-reduction of 攵 either. Base sense "imitate, follow, emulate a model" extends to "the result produced by following/applying something" — "result, effect, efficacy." `mc_id: 900` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 效).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/効果.md`'s own field. `hsk_level: ""` (explicit empty string, not blank) → filled in as `無`, since 効 is a Japan-only shinjitai form — mainland Simplified Chinese retains 效, so this exact glyph never appears in HSK material.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus two Words entries stranded inside Notes with a malformed comma-joined gloss — all four canonical bullets written from scratch; `## Words` didn't exist as its own heading; 1 of 3 ground-truth words missing; no `## Derived Characters` despite seven real hits.

**Words cross-check** (3 total ground-truth hits): 効果 (stand-in), 効率 moved out of Notes and reformatted to ruby+gloss; 1 missing — 無効 ("ineffective; invalid") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 total ground-truth hits — characters naming 交 as their `graphemic_classification`): 咬 (char) ("bite; gnaw; chew," pipe-linked), 校 ("school"), 狡 ("cunning; sly"), 較 ("compare"), 郊 ("outskirts"), 餃 ("gyoza"), 鮫 ("shark") — all seven added.

**Verification**: Python cross-check of all 10 `<rt>` values (3 Words + 7 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 405 — [[characters/助|助]]

Next never-perfected character by `danayo_id` (3033). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 且` already correct — verified via Wiktionary: 形声 (OC \*zras), semantic 力 ("strength, effort") + phonetic [[且 (char)|且]] (OC \*sʰjaːʔ) — "to help with one's strength." `mc_id: 932` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter defect found and fixed**: `stand_in: 救援` pointed to a word whose own `characters:` field is `[救, 援]` — **no 助 at all**. Ground-truth Words search turned up `words/援助.md` ("aid; assist," `characters: [援, 助]`) as the clear correction target — same two characters as 救援 with one swapped, an easy transposition to make, and the meaning "aid; assist" closely matches 助's own `english: rescue`. Corrected `stand_in` to `援助`, the loop's third stand_in-field correction after [[characters/願|願]] (iteration 370) and [[characters/余|余]] (iteration 387). `pos: ''` (empty string) → filled in as `事詞`.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links — all four canonical bullets written from scratch; **6 of 8** ground-truth words missing outright, including the corrected stand-in itself and an entire particle-terminology cluster (助詞/格助詞/接続助詞/語気助詞).

**Words cross-check** (8 total ground-truth hits): 幇助, 賛助 already present, kept; 6 missing — 援助 (corrected stand-in), 補助 ("assistance; help; aid; auxiliary"), 助詞 ("particle"), 格助詞 ("case particle"), 接続助詞 ("conjunctive particle"), 語気助詞 ("mood particle; modal particle") — all added from stored fields.

**Chengyu**: 1 ground-truth hit — 形助顕理 — already present, kept.

**Derived Characters** (9 total ground-truth hits — characters naming 且 as their `graphemic_classification`, the largest phonetic family found this loop): 祖 ("ancestor"), 詛 ("curse"), 査 ("investigate"), 狙 ("spy; ambush"), 疽 ("ulcer; abscess"), 租 ("rent; duty; tariff"), 粗 ("coarse"), 組 ("organize; form; group up"), 阻 ("thwart; block; impede") — all nine added.

**Verification**: Python cross-check of all 18 `<rt>` values (8 Words + 1 Chengyu + 9 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 404 — [[characters/則|則]]

Next never-perfected character by `danayo_id` (3032). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[鼎 (char)|鼎]] ("bronze tripod cauldron") and 刀 ("knife") — original form 𠟭, carving an inscription of rules/laws onto a bronze vessel with a knife. Worth flagging: the modern glyph's left component visually resembles 貝 ("cowrie shell"), which I initially suspected might be the real component — but Wiktionary confirms this is a corrupted/simplified 鼎, unrelated to the shell character entirely (a graphic-drift case, similar in spirit to the shinjitai substitutions found earlier this loop, though here it's a general orthographic drift rather than a Japan-specific shinjitai). Semantic development: "carve a rule onto bronze" → "rule; law; regulation" → "standard, model" → grammaticalized "then; thus; in that case." `mc_id: 17` cross-checked against `lookup/CC/CC 0000.md` — exact match (top-20 most frequent character in the corpus).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/法則.md`'s own field.

**Body defects found**: `## Notes` held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 2 of 3 ground-truth words missing, including the stand-in 法則 itself; no `## Derived Characters` despite four real hits.

**Words cross-check** (3 total ground-truth hits): 原則 already present, kept; 2 missing — 法則 (stand-in), 規則 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 total ground-truth hits — characters naming 則 as their `graphemic_classification`): 測 ("measure; survey"), 厠 ("WC; toilet"), 側 ("side; aspect"), 賊 ("thief") — all four added.

**Verification**: Python cross-check of all 7 `<rt>` values (3 Words + 4 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 403 — [[characters/到|到]]

Next never-perfected character by `danayo_id` (3031). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 刀` already correct — verified via Wiktionary: 形声 (OC \*taːws), semantic [[至 (char)|至]] ("to arrive") + phonetic 刀 (OC \*taːw) — 刀 reinforces/specifies 至's meaning via sound, the -s suffix marking a perfective/directional sense, "to arrive at." Notable quirk confirmed as legitimate: this character's own `radical` field (刀) matches the *phonetic* component rather than the semantic one (至) — an established Kangxi-indexing pattern (radical assignment doesn't always track semantic headedness), so the radical-linking rule correctly applies to 刀 here, not 至. `mc_id: 974` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`, matching the stand-in word `words/到達.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite two ground-truth hits, including the stand-in itself; no `## Derived Characters` despite two real hits.

**Words cross-check** (2 total ground-truth hits): 到達 (stand-in), 遅到 — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 刀 as their `graphemic_classification`): 召 ("summon; convene"), 鞀 ("pellet drum") — both added.

**Verification**: Python cross-check of all 4 `<rt>` values (2 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 402 — [[characters/判|判]]

Next never-perfected character by `danayo_id` (3030). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 半` already correct — verified via Wiktionary: 形声 (OC \*pʰaːns), semantic 刀 ("knife") + phonetic [[半]] (OC \*paːns, "half") — 半 already carries the sense of splitting something in two; adding the knife reinforces the literal cutting/dividing action, extended metaphorically to "judge, decide, distinguish" (judging as "cutting" a matter into right/wrong). `mc_id: 3090` cross-checked against `lookup/CC/CC 3000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `実詞`, matching the stand-in word `words/判断.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus two Words entries stranded inside the Notes section with malformed comma-separated glosses instead of ruby+gloss — all four canonical bullets written from scratch; `## Words` didn't exist as its own heading; 2 of 4 ground-truth words missing, including the stand-in itself; no `## Derived Characters` despite five real hits.

**Words cross-check** (4 total ground-truth hits): 判断 (stand-in), 判別式 moved out of Notes and reformatted to ruby+gloss; 2 missing — 批判 ("critique; criticize"), 談判 ("negotiate; talk") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 total ground-truth hits — characters naming 半 as their `graphemic_classification`): 絆 ("band; fetter"), 畔 (char) ("ridge; boundary," pipe-linked), 伴 ("comrade; companion"), 拌 ("mix; blend"), 胖 ("fat") — all five added.

**Verification**: Python cross-check of all 9 `<rt>` values (4 Words + 5 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 401 — [[characters/凶 (char)|凶]]

Next never-perfected character by `danayo_id` (3029). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 象形` and `pos: 性詞` were both already correct. Verified via Wiktionary: this is a genuinely open dual analysis, not a settled scholarly consensus — 凵 (this character's own `radical` field, and here a real depicted component, unlike the arbitrary Kangxi-filing cases seen on 丙/也/余/凡 earlier this loop) represents a hole in the ground; 㐅 either indicates the hole's existence (指事 reading) or depicts rock/mud/stone/bamboo inside it (象形 reading); Wiktionary presents both without declaring a winner, matching the pre-existing bullet's content exactly. An alternate theory derives the glyph from the upper component of 㚇. `mc_id: 682` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Body defects found**: the graphemic bullet's own radical component (凵) wasn't linked at all (plain quoted text instead of `[[Radical 017|凵]]`); the SKIP/Stroke, MC rank, and Levels bullets were all missing outright, with both CC initial/final links floating at the bottom of the file; all six Words entries were bare wikilinks with no ruby/gloss, and the stand-in 凶 itself was missing entirely; no `## Derived Characters` despite one real hit.

**Words cross-check** (7 total ground-truth hits): 凶悪, 凶器, 凶手, 凶徒, 凶暴, 元凶 all reformatted from bare wikilinks to ruby+gloss; 1 missing — 凶 (stand-in) — added, moved to lead the list.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 凶/兇 as its `graphemic_classification`): 匈 ("Huns") — added.

**Verification**: Python cross-check of all 8 `<rt>` values (7 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 400 — [[characters/凡|凡]]

Milestone: 400th iteration of the loop. Next never-perfected character by `danayo_id` (3028). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a plate placed vertically on its side, the original form of [[盤 (char)|盤]] ("plate; basin," OC \*baːn), distinguished from 同 by an asymmetric right stroke. Wiktionary explicitly states 凡 is **unrelated to 几** despite the visual resemblance that placed it under that Kangxi radical — confirming (as with [[characters/丙 (char)|丙]], [[characters/也 (char)|也]], and [[characters/余|余]] earlier this loop) that the character's own `radical` field here is purely a filing artifact, not a real depicted component, so no forced radical link belongs in the bullet. Genuinely interesting semantic note: the "ordinary, common, all" sense is *not* a metaphorical extension of the plate image — Schuessler (2007) treats it as likely Sino-Tibetan in origin, cognate with Mizo *pum* ("whole; all") and Burmese ဘုံ (bhum, "common, public, communal"). `mc_id: 278` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, matching the stand-in word `words/平凡.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links — all four canonical bullets written from scratch; the pre-existing `## Words` entry was correctly ruby'd but not yet labeled as the stand-in; no `## Derived Characters` despite five real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 平凡 — already present and correctly formatted, labeled as stand-in.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 total ground-truth hits — characters naming 凡 as their `graphemic_classification`): 釩 ("vanadium"), 鳳 ("phoenix"), 帆 (char) ("sail; sailboat," pipe-linked), 汎 (char) ("pan-," pipe-linked), 風 (char) ("wind," pipe-linked) — all five added.

**Verification**: Python cross-check of all 6 `<rt>` values (1 Words + 5 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 399 — [[characters/写|写]]

Next never-perfected character by `danayo_id` (3027). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 舄` — a third instance of the shinjitai-substitution pattern from earlier this loop ([[characters/仮|仮]], [[characters/価|価]]). Verified via Wiktionary: traditional 寫 is 形声 (OC \*sjaːʔ), semantic 宀("roof/house") + phonetic 舄 (a pure sound-loan, "shoe" or a bird, contributing no meaning). The modern shinjitai/simplified glyph 写 does **not** retain 舄 at all — it decomposes as ⿱冖与, a cursive-script abbreviation whose bottom residue merely resembles [[与 (char)|与]] ("and; give"). Like 仮's 反, this residue is a real independent character (unlike 価's non-character 覀 residue) but carries **no phonetic correspondence** to 写's own reading — 与's on'yomi YO/mandarin yǔ don't match SHA/xiě. Concluded, consistent with the 仮 precedent, that `graphemic_classification` should stay at 舄 (the true phonetic donor) rather than the phonetically inert 与. `mc_id: 1554` cross-checked against `lookup/CC/CC 1000.md` — exact match (traditional form 寫). `pos: 事詞` was already correct.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus two Words entries stranded inside the Notes section instead of their own heading — all four canonical bullets written from scratch; `## Words` didn't exist as its own heading (its two entries needed to be moved out of Notes), and one entry (写真) was a bare wikilink with no ruby; no `## Derived Characters` despite one real hit.

**Words cross-check** (2 total ground-truth hits): 複写 (stand-in) already ruby'd, moved to lead and labeled as stand-in; 写真 reformatted to ruby+gloss.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 舄 as its `graphemic_classification`): 潟 ("lagoon") — added.

**Verification**: Python cross-check of all 3 `<rt>` values (2 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 398 — [[characters/冊 (char)|冊]]

Next never-perfected character by `danayo_id` (3026). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 象形` already correct — verified via Wiktionary: depicts vertical bamboo slips bound by horizontal cords (the vertical strokes are the slips, the horizontal lines the binding string); the existing bullet's cross-references were all confirmed accurate — shares this pictographic component with 侖, 扁, and 典, and is "similar but unrelated" to 龠. `mc_id: 2941` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `量詞`, matching the stand-in word `words/冊.md`'s own field (冊 functions as a classifier for bound volumes).

**Body defects found**: two separate `## Notes` headings existed in the same file — the first held only the two floating CC-initial/final links, the second held the actual graphemic bullet — merged into one canonical section with all four bullets (SKIP/Stroke, MC rank, and Levels bullets written from scratch); 3 of 4 ground-truth words missing, including the stand-in 冊 itself; no `## Derived Characters` despite three real hits.

**Words cross-check** (4 total ground-truth hits): 冊子 already present, kept; 3 missing — 冊 (stand-in), 小冊子 ("booklet"), 地図冊 ("atlas") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 total ground-truth hits — characters naming 冊 as their `graphemic_classification`): 珊 ("coral"), 柵 (char) ("fence," pipe-linked), 刪 ("delete") — all three added.

**Verification**: Python cross-check of all 7 `<rt>` values (4 Words + 3 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 397 — [[characters/其 (char)|其]]

Next never-perfected character by `danayo_id` (3025). Stamped `date-last-perfect: 2026-07-26`. **Frontmatter defect found and fixed**: `japanese_native` was malformed YAML — a scalar value (`その`) directly followed by indented list items (`- その`, `- それ`) under the same key, which Python's YAML parser folds into a garbage multi-line-scalar string ("その - その - それ") rather than a clean two-item list. Corrected to a proper list `[その, それ]`. `graphemic_classification: 象形` was already correct — verified via Wiktionary: originally 𠀠, depicting a winnowing basket; bronze script added a stand below (丌, resembling [[Radical 012|八]]'s splayed legs, 其's own `radical` field — genuinely part of the depicted image here, unlike the arbitrary Kangxi-filing radicals seen on [[characters/丙 (char)|丙]]/[[characters/也 (char)|也]]/[[characters/余|余]] earlier this loop). The basket sense was later inherited by 箕 (with 竹 added), while 其 itself was phonetically borrowed (假借) to write a demonstrative/possessive pronoun — the concrete image abandoned for a purely grammatical function. `mc_id: 6` cross-checked against `lookup/CC/CC 0000.md` — exact match (top-10 most frequent character in the corpus). `pos: 修飾語` was already correct.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links plus a single malformed bullet (`- [[其名]] "- him"`, with a stray leading dash baked into the quoted gloss) — all four canonical bullets written from scratch; **11 of 12** ground-truth words missing outright, including the stand-in 其 itself and an entire correlative-chart family (其人/其人等/其事/其物/其類/其多/其様/其処/其時/尤其), the same pattern seen on [[characters/処 (char)|処]] earlier this loop; no `## Derived Characters` despite eight real hits.

**Words cross-check** (12 total ground-truth hits): 其名 reformatted from its malformed form to proper ruby+gloss; 11 missing — 其 (stand-in), 其人, 其人等, 其事, 其物, 其類, 其多, 其様, 其処, 其時, 尤其 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (8 total ground-truth hits — characters naming 其 as their `graphemic_classification`): 麒 ("qilin"), 期 (char) ("period; time; season," pipe-linked), 基 ("foundation; base"), 斯 ("this; then"), 旗 ("banner; flag"), 棋 ("chess; strategy game"), 欺 ("deceive; trick"), 碁 ("Go (game)") — all eight added.

**Verification**: Python cross-check of all 20 `<rt>` values (12 Words + 8 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 396 — [[characters/充|充]]

Next never-perfected character by `danayo_id` (3024). **Frontmatter defect found and fixed**: `graphemic_classification: 育` was wrong on both counts — verified via Wiktionary that 充 is actually **会意**, not 形声 at all, so storing a component name here violated the checklist's own core rule. The real composition is 𠫓 (an inverted 子, "newborn," no vault page of its own) + [[Radical 010|儿]] ("legs, standing person") — a newborn growing to stand and mature — with no phonetic component whatsoever; the top element is 𠫓, not 育, which only superficially resembles it. Corrected the field to `会意`. Semantic development: "grown to completion" → "full, filled up" → "sufficient" → later "to serve, act as (a role)." Stamped `date-last-perfect: 2026-07-26`. `mc_id: 950` cross-checked against `lookup/CC/CC 0000.md` — exact match. `pos: 事詞` was already correct, matching its stand-in word `words/充填.md`'s own field.

**Body defects found**: the pre-existing `## Notes` had only a bare non-canonical "Components:" bullet citing the wrong radical entirely (`[[Radical 008|亠]]`, i.e. the "lid" radical — irrelevant to 充, whose own `radical` field is 儿/Radical 010) plus the two floating CC-initial/final links — all four canonical bullets written from scratch; 1 of 6 ground-truth words missing, namely the stand-in 充填 itself; no `## Derived Characters` despite two real hits.

**Words cross-check** (6 total ground-truth hits): 充分, 補充, 充足, 充電, 充当 already present and correctly ruby'd, kept; 1 missing — 充填 (stand-in, "fill") — added, moved to lead the list. Notable oddity confirmed as genuine, not a transcription error: 充填 and 充電 share the exact same stored reading, ㄑㄨㄫㄉㄝㄋ.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 充 as their `graphemic_classification`): 銃 (char) ("gun," pipe-linked), 統 ("command; govern; unite") — both added. Confirmed this is not a contradiction of 充's own reclassification to 会意: an ideograph can still go on to serve as a legitimate phonetic donor for later 形声 characters, the same way 人/木/水 and dozens of other 会意/象形 characters do throughout this vault.

**Verification**: Python cross-check of all 8 `<rt>` values (6 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-26, iteration 395 — [[characters/傷|傷]]

Next never-perfected character by `danayo_id` (3023). Stamped `date-last-perfect: 2026-07-26`. `graphemic_classification: 昜` — verified via Wiktionary and confirmed correct, but with a genuinely nuanced etymology worth documenting: Wiktionary's stricter analysis traces 傷's true ancient phonetic to an obscure variant 𥏻 (no vault entry, not even a real independent character in common use), noting the modern glyph merely "resembles 亻+昜" rather than containing it etymologically. However — unlike the [[characters/仮|仮]] and [[characters/価|価]] shinjitai cases earlier this loop, where a *specifically Japanese* simplification swapped in a phonetically-empty component — 傷 has presented this way across the whole CJK tradition, isn't a modern substitution, and 昜 *does* correspond phonologically (shares the same -aŋ rime as its 8-member phonetic-series siblings already in this database: 揚/湯/陽/場/楊/暢/瘍/腸). Concluded the field is correctly kept at 昜, consistent with that established family, rather than "corrected" to an untracked ghost character. Bonus cross-reference: Schuessler (2007) suggests 傷 may be a causative derivative of 瘍 ("ulcer, sore") — one of 傷's own phonetic-series siblings, now both documented on each other's pages. `mc_id: 366` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`, matching its stand-in compound partner [[characters/害|害]]'s own field (the stand-in word `words/傷害.md` itself had no `pos` value to inherit from).

**Body defects found**: `# Notes` used H1 instead of H2 and held only a malformed one-line paraphrase bullet (`- 'wound, injure'`) plus the two floating CC-initial/final links — all four canonical bullets written from scratch; `## Words` didn't exist at all despite four ground-truth hits, including the stand-in itself; no `## Derived Characters` despite eight real hits.

**Words cross-check** (4 total ground-truth hits): all four missing — 傷害 (stand-in), 創傷 ("trauma; traumatize"), 哀傷 ("sad; distressed; mournful"), 悲傷 ("sad; sorrowful; grieving") — added from stored fields.

**Chengyu**: 1 ground-truth hit — 破頭傷足 — already present, kept.

**Derived Characters** (8 total ground-truth hits — characters naming 昜 as their `graphemic_classification`, one of the largest phonetic families found this loop): 揚 (char) ("scatter; hurl," pipe-linked), 湯 (char) ("hot water," pipe-linked), 陽 (char) ("shine," pipe-linked), 場 ("market"), 楊 ("poplar; aspen tree"), 暢 ("smooth; free; unrestrained"), 瘍 ("ulcer; boil; sore"), 腸 ("intestine; sausage") — all eight added.

**Verification**: Python cross-check of all 13 `<rt>` values (4 Words + 1 Chengyu + 8 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 394 — [[characters/偉|偉]]

Next never-perfected character by `danayo_id` (3022). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 韋` and `pos: 性詞` were both already correct. Verified via Wiktionary: 形声 (OC \*ɢʷɯlʔ), semantic 人 + phonetic [[韋]]; Wiktionary supplies no semantic-development note bridging "person + 韋" to "great, extraordinary," so the bullet states the structural analysis without inventing an unsourced bridge. `mc_id: 2468` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Body defects found**: `## Notes` held only the two floating CC-initial/final links plus a bare non-canonical "Components:" bullet — all four canonical bullets written from scratch; `## Words` didn't exist despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite six real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 偉大 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 total ground-truth hits — characters naming 韋 as their `graphemic_classification`): 諱 (char) ("shun; avoid saying the name of," pipe-linked due to the `words/諱.md` collision), 囲 ("encircle"), 緯 ("lines of latitude"), 葦 ("reed"), 違 ("violate; disobey"), 衛 ("guard; protect") — all six added.

**Verification**: Python cross-check of all 7 `<rt>` values (1 Words + 6 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 393 — [[characters/倍 (char)|倍]]

Next never-perfected character by `danayo_id` (3021). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 咅` already correct — verified via Wiktionary: 形声 (OC \*bɯːʔ), semantic 人 + phonetic [[咅]] (OC \*pʰɯʔ, \*pʰl'oːs). Genuinely interesting semantic thread: an obsolete sense of 倍, "to turn one's back on, betray," survives as an alternate form of 背 ("the back"), sharing the same phonetic element and body-part imagery — the modern "times, -fold" sense plausibly extends from "back-to-back" → a second, opposing counterpart → a duplicate → multiplicative "-fold," though Wiktionary doesn't spell out this bridge explicitly, so the bullet phrases it as "plausible" rather than settled fact. `mc_id: 997` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `量詞` (classifier), since 倍's own gloss "times" functions as a multiplicative count-word suffix (兩倍, 三倍) rather than a plain noun — `words/倍.md` had no `pos` field of its own to inherit from.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite six real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 倍 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 total ground-truth hits — characters naming 咅 as their `graphemic_classification`): 剖 ("dissect; bisect"), 培 ("cultivate"), 菩 ("bodhisattva"), 部 (char) ("part," pipe-linked), 陪 (char) ("accompany; be with; keep company," pipe-linked), 賠 ("indemnify; pay damages") — all six added.

**Verification**: Python cross-check of all 7 `<rt>` values (1 Words + 6 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 392 — [[characters/保|保]]

Next never-perfected character by `danayo_id` (3019). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` and `pos: 事詞` were already correct — this page was in unusually good shape (all four Notes bullets, full 8-word Words list, and the Chengyu entry were already present and accurate, matching the ground-truth cross-check exactly). `mc_id: 766` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Body defects found**: bullet 1's component link used bare `[[呆 (char)]]` (would literally display "呆 (char)" as link text) instead of the collision-safe pipe form `[[呆 (char)|呆]]`; bullets 2–4 all carried a stray `../` prefix on their Markdown paths (`../lookup/...`, `../syllables/...`) — inconsistent with every other character page perfected this loop, which resolve correctly from within `characters/` without it; normalized to match. `## Derived Characters` had a real defect: `[[褓]]` is a **dead link** — `characters/褓.md` does not exist anywhere in the vault, and no page names 保 as its `graphemic_classification` under that name — removed as a broken citation. The other two entries were reformatted: 褒 (char) was a bare Markdown link with no ruby/gloss, and needed the collision-safe pipe form.

**Words cross-check** (8 total ground-truth hits): all 8 already present and correctly ruby'd — no changes needed.

**Chengyu**: 1 ground-truth hit — 保頭断尾 — already present, kept.

**Derived Characters** (2 total ground-truth hits — characters naming 保 as their `graphemic_classification`, after discounting the dead 褓 reference): 褒 (char) ("praise," pipe-linked, reformatted to ruby+gloss), 堡 ("fort," already correctly formatted, kept).

**Verification**: Python cross-check of all 11 `<rt>` values (8 Words + 1 Chengyu + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 391 — [[characters/俗 (char)|俗]]

Next never-perfected character by `danayo_id` (3018). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 谷` already correct — verified via Wiktionary: 形声 (OC \*ljoɡ), semantic 人 + phonetic [[谷 (char)|谷]] — core sense "what people [collectively] do," the customs of ordinary people (民俗, 風俗); "vulgar" is a secondary, often pejorative extension of "common among the masses" as opposed to refined or sacred, contrasting with 僧 ("monastic"). `mc_id: 560` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, since 俗's own gloss "vulgar" is descriptive/adjectival rather than a plain noun (the stand-in word `words/俗.md` had no `pos` field of its own to inherit from).

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist despite two ground-truth hits, including the stand-in itself; no `## Derived Characters` despite four real hits.

**Words cross-check** (2 total ground-truth hits): 俗 (stand-in), 習俗 — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 total ground-truth hits — characters naming 谷 as their `graphemic_classification`): 浴 ("bathe"), 容 (char) ("look; appearance; form," pipe-linked due to the `words/容.md` collision), 欲 ("desire; want"), 裕 ("abundant; rich") — all four added.

**Verification**: Python cross-check of all 6 `<rt>` values (2 Words + 4 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 390 — [[characters/係|係]]

Next never-perfected character by `danayo_id` (3017). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 系` already correct — verified via Wiktionary: 形声 (OC \*keːɡs), semantic 人 + phonetic [[系]] (OC \*ɡeːɡs, "to connect, tie") — a person tied/connected to something, "relationship." `mc_id: 2370` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `実詞`, matching the stand-in word `words/関係.md`'s own field.

**Body defects found**: the graphemic bullet used raw non-wikilink Markdown paths (`[人](Radical%20009)`, `[系](系.md)`) instead of proper `[[Radical 009|人]]`/`[[系]]` wikilinks, and lacked a dash-note on semantic motivation; the SKIP/Stroke, MC rank, and Levels bullets were all missing outright, with both CC initial/final links floating at the bottom of the file; `## Words` didn't exist despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite one real hit.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 関係 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 total ground-truth hit — the character naming 系 as its `graphemic_classification`): 繋 ("fasten; tie") — added.

**Verification**: Python cross-check of both `<rt>` values (1 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 389 — [[characters/価|価]]

Next never-perfected character by `danayo_id` (3016). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 賈` already correct — another shinjitai edge case, and a more extreme version of [[characters/仮|仮]]'s from a few iterations back. Verified via Wiktionary: traditional 價 is 形声 (OC \*kraːs), semantic 人 + phonetic 賈 (OC \*kraːʔ, \*kraːs, "merchant; to trade"). The modern Japanese shinjitai 価 abbreviates 賈 by stripping out 貝 ("shell, money"), leaving a bare graphic residue (⿰亻覀) that **isn't even a standalone character** — unlike 仮's 反 (a real, separately-attested character that merely lacks phonetic correspondence) or 鉄's 失 (a real character that coincidentally retains phonetic correspondence), 価's residual "覀" has no vault page and no independent identity at all. Concluded — consistently with the 仮 case — that `graphemic_classification` should stay at 賈, the only real character in this etymology, rather than pointing at a non-character graphic fragment. `mc_id: 2437` cross-checked against `lookup/CC/CC 2000.md` — exact match (traditional form 價).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/価格.md`'s own field. `boundedness` was blank — left as-is (not a checklist-required field).

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 4 of 5 ground-truth words missing, including the stand-in 価格 itself.

**Words cross-check** (5 total ground-truth hits): 評価 already ruby'd, kept; 4 missing — 価格 (stand-in), 価値 ("worth; value"), 安価 ("cheap; inexpensive; crappy"), 廉価 ("low price") — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 賈` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 388 — [[characters/佳 (char)|佳]]

Next never-perfected character by `danayo_id` (3015). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 圭` and `pos: 性詞` were both already correct. Verified via Wiktionary: 形声 (OC \*kreː), semantic [[Radical 009|人]] ("person") + phonetic [[圭]] (OC \*kʷeː). `mc_id: 3380` cross-checked against `lookup/CC/CC 3000.md` — exact match.

**Body defects found**: the graphemic bullet had a stray unmatched closing parenthesis ("OC \*kreː): semantic..." with no opening paren); the SKIP/Stroke bullet was malformed wikilink soup (`[[SKIP-1-2-6]] ([[Stroke 08]]) [[ㄍ⼘ㄧ]]`, syllable misplaced onto this bullet instead of the MC bullet); the MC rank bullet was missing outright, with both CC initial/final links floating at the bottom of the file; the Levels bullet was missing the HSK link and in the wrong order (`[[Korean MS]], [[Jōyō - Kōtō]], [[Grade 3]]` instead of Grade → HSK → Jōyō → Korean, and using raw wikilinks instead of Markdown path links); `## Words` didn't exist at all despite two ground-truth hits; no `## Chengyu` despite a real hit; no `## Derived Characters` despite eleven real hits.

**Words cross-check** (2 total ground-truth hits): 佳 (stand-in), 佳人 — both added from stored fields.

**Chengyu**: 1 ground-truth hit — 佳人薄命 ("a beautiful woman has an ill fate") — added.

**Derived Characters** (11 total ground-truth hits — characters naming 圭 as their `graphemic_classification`): 卦 (char) ("trigram," pipe-linked), 哇 (char) ("wow," pipe-linked), 鞋 (char) ("shoe," pipe-linked), 娃 ("beautiful; doll"), 桂 ("cinnamon; cassia"), 街 ("street; road; thoroughfare"), 掛 (char) ("hang; suspend," pipe-linked), 厓 ("precipice; cliff"), 蛙 ("frog"), 閨 ("women's bedroom"), 硅 ("silicon") — all eleven added, one of the largest Derived Characters families found this loop.

**Verification**: Python cross-check of all 14 `<rt>` values (2 Words + 1 Chengyu + 11 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 387 — [[characters/余|余]]

Next never-perfected character by `danayo_id` (3013). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: depicts a thatched cottage/house, the original form of 舎/舍 (OC \*hljaːʔ, \*hljaːs), later phonetically borrowed to write the first-person pronoun "I; me" (OC \*la). Added a clarifying clause the old bullet lacked: the "surplus, remainder" sense actually used in Dan'a'yo (`english: surplus`) comes from a historically **distinct** character, 餘 (its own 形声 compound), of which 余 is only the modern simplification — the "I/me" and "surplus" senses share a glyph today only through that simplification merger, not through any real etymological connection. Also resolved a puzzling `aliases` entry: 蜍 ("toad," seemingly unrelated to "house" or "I/me") turns out to be legitimate — `words/瞻余.md` (a Dan'a'yo neologism for "toad," glossing 蟾蜍) uses 余 as a graphic stand-in for 蜍's own phonetic slot (蜍 = 虫+余), the same "character reused as a substitute for a non-vault character" pattern documented earlier this loop on [[characters/乾 (char)|乾]]'s page (乾/干/幹). `mc_id: 170` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 餘, listed alias).

**Frontmatter defect found and fixed**: `stand_in: 残余` pointed to a word that **does not exist anywhere in the vault** — no `words/残余.md`, and no other file references "残余" in any form. Cross-referencing the ground-truth Words search turned up `words/剰余.md` ("rest; remainder; surplus," `pos: 名詞`), whose gloss matches 余's own `english: surplus` field almost exactly — corrected `stand_in` to `剰余`, the same class of fix as [[characters/願|願]]'s `stand_in` correction earlier this loop (iteration 370). `pos: ''` (empty string) → filled in as `名詞`, matching 剰余's own field.

**Body defects found**: no disambiguation callout needed (no `words/余.md` collision); the two CC-initial/final links floated below the sole Notes bullet instead of being embedded in an MC bullet, and the SKIP/Stroke and Levels bullets were both missing outright; a non-canonical `### Derived characters` (H3, wrong heading text and level) held one malformed entry (`- 涂 --> [塗](塗.md)`) instead of the canonical `## Derived Characters` ruby format; 4 of 7 ground-truth words missing, including the newly-corrected stand-in itself.

**Words cross-check** (7 total ground-truth hits): 余波, 余震, 余接 already present (余接 reformatted from bare wikilink to ruby+gloss); 4 missing — 剰余 (corrected stand-in), 余弦 ("cosine"), 余割 ("cosecant"), 瞻余 ("toad") — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (8 total ground-truth hits — characters naming 余/餘 as their `graphemic_classification`): 叙 ("express; state; relate"), 徐 ("slowly; quietly; calmly"), 舎 ("inn; hut; mansion" — itself 余's own etymological ancestor 舍, now converged as a phonetic-series sibling), 茶 (char) ("tea," pipe-linked), 塗 ("smear; daub" — the single entry that existed pre-perfection, reformatted from its broken `### Derived characters` form), 斜 ("slant; tilt"), 途 ("en route"), 除 ("exclude") — all eight added/reformatted.

**Verification**: Python cross-check of all 15 `<rt>` values (7 Words + 8 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 386 — [[characters/体|体]]

Next never-perfected character by `danayo_id` (3012). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct, and the existing bullet's shinjitai-vs-traditional analysis was already well-written: shinjitai 体 is 会意 of 人("person") + 本("root, base") — the person at their root, the body; traditional 體 is 形声, semantic 骨("bone") + phonetic 豊. `mc_id: 595` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 體).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/体系.md`'s own field.

**Body defects found**: the graphemic bullet's own components weren't link-formatted correctly — `[[人]]` needed to become `[[Radical 009|人]]` since 人 is this character's own `radical` frontmatter value, and `[[本]]`/`骨` needed the collision-safe pipe form (`words/本.md` and `words/骨.md` both exist) as `[[本 (char)|本]]` and `[[骨 (char)|骨]]`; three Words entries (体育館, 体積, 体言) were bare wikilinks with no ruby; **10 of 27** ground-truth words missing outright; `## Chengyu` was missing 2 of 3 ground-truth hits.

**Words cross-check** (27 total ground-truth hits — one of the largest word lists this loop): 17 pre-existing entries kept (three reformatted to ruby+gloss: 体育館, 体積, 体言); reordered so the stand-in 体系 leads; 10 missing — 一体, 異体, 肢体, 液体, 球体, 体現, 新字体, 簡体字, 繁体字, 身体 — all added from stored fields.

**Chengyu** (3 total ground-truth hits): 異体不容 already present, kept; 2 missing — 混然一体 ("monad, utterly unified"), 文体並存 ("styles coexist") — added from stored fields.

**Derived Characters**: none (`graphemic_classification: 体`/`體` matches no other character — 体 is 会意, not a 形声 phonetic donor) — correctly omitted.

**Verification**: Python cross-check of all 30 `<rt>` values (27 Words + 3 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 385 — [[characters/但 (char)|但]]

Next never-perfected character by `danayo_id` (3011). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 旦` already correct — verified via Wiktionary: 形声 (OC \*daːn, \*daːnʔ, \*daːns), semantic [[Radical 009|人]] ("person") + phonetic [[旦]] (OC \*taːns). Worth flagging: I initially suspected an "expose/bare" origin story via 袒 (a same-phonetic-series sibling), but Wiktionary doesn't actually support that link — it traces 但 instead to Proto-Sino-Tibetan \*(d/t)a(n/j) ("single; one; whole; only"), cognate with 單 (OC \*taːn, "single"), which cleanly explains the "only, merely" → "but, however" development without needing a "bare" intermediate sense. `mc_id: 1241` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `連接詞`, matching the vault's own grammar taxonomy (`grammar/文法 - 97品詞.md`), which explicitly lists 但 ("but; however") under Linkers/連接詞.

**Body defects found**: `# Notes` used H1 instead of H2 and held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; Words entries were present and correct but in reversed order (stand-in 但 should lead); no `## Derived Characters` despite five real hits.

**Words cross-check** (2 total ground-truth hits): both already ruby'd and correct — 但 (stand-in) reordered to lead, 不但 kept.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 total ground-truth hits — characters naming 旦 as their `graphemic_classification`): 曇 (char) ("overcast," pipe-linked due to the `words/曇.md` collision), 亶 ("sincere; real"), 担 ("shoulder; carry; bear"), 胆 ("gall bladder; bravery"), 坦 ("flat; level") — all five added; readings diverge across ㄉㄚㄇ/ㄉㄚㄋ/ㄊㄚㄋ rather than converging, the same non-convergent pattern seen on [[characters/也 (char)|也]]'s family last iteration.

**Verification**: Python cross-check of all 7 `<rt>` values (2 Words + 5 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 384 — [[characters/仮|仮]]

Next never-perfected character by `danayo_id` (3010). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 叚` — a genuinely interesting shinjitai edge case, distinct from the 鉄/銭/適/選 precedent set earlier this loop. Verified via Wiktionary: traditional 假 is 形声 (OC \*kraːʔ, \*kraːs), semantic 亻("person") + phonetic 叚 (OC \*kraːʔ) — "to lend/borrow" extended to "fake, false," a *-s derivative giving "vacation, leave," and separately "if, supposing." The **modern Japanese shinjitai glyph 仮 graphically substitutes 反 for 叚** — but unlike 鉄's shinjitai substitution 失 (which happens to still correspond phonetically to TETSU), 反 (on'yomi HAN) has **no phonetic correspondence** to 仮's own reading (KA/KE) — it's a purely graphic simplification, not a re-phoneticization. Concluded the field should stay at 叚 (the true phonetic/etymological component) rather than being reassigned to 反, since 反 carries no actual sound value for this character — the opposite conclusion from the 鉄 case, where the field WAS corrected to the modern glyph's component because that component still functioned phonetically. `mc_id: 824` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 假).

**Frontmatter**: `pos: ''` (empty string) → filled in as `事詞`, matching the stand-in word `words/仮借.md`'s own field. `boundedness` was blank — left as-is (not a checklist-required field for `date-last-perfect`).

**Body defects found**: `## Notes` had only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; one Words entry (仮面) was a bare wikilink with a plain (non-ruby) gloss; 2 of 4 ground-truth words missing, including the stand-in 仮借 itself; no `## Derived Characters` despite three real hits.

**Words cross-check** (4 total ground-truth hits): 仮定 already ruby'd, kept; 仮面 reformatted to ruby+gloss; 2 missing — 仮借 (stand-in), 片仮名 ("katakana") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 total ground-truth hits — characters naming 叚 as their `graphemic_classification`): 暇 ("spare time"), 蝦 ("shrimp"), 霞 ("mist") — all three added, all converging on ㄏㄚ.

**Verification**: Python cross-check of all 7 `<rt>` values (4 Words + 3 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 383 — [[characters/也 (char)|也]]

Next never-perfected character by `danayo_id` (3006). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: this is a genuinely, famously disputed glyph. Leading theory depicts a crying child with mouth open (arms dropped away during bronze-script simplification); competing proposals across the literature include female genitalia, a simplified snake glyph, a modal-particle mouth-glyph with a descending breath line, a wash basin/funnel, or a flat-legged scorpion — no scholarly consensus. Its grammaticalization into a sentence-final assertive/topic particle (possibly Sino-Tibetan, cf. Tibetan ལ la) predates any recoverable original pictographic sense. `mc_id: 3` cross-checked against `lookup/CC/CC 0000.md` — exact match (top-5 most-frequent character in the entire corpus). Confirmed via [[characters/丁 (char)|丁]] and [[characters/丙 (char)|丙]] (both established this loop) that whole-glyph 象形 characters filed under a Kangxi radical purely for indexing purposes — here `radical: 乙`, not a depicted component of any of 也's competing theories — correctly omit a forced `[[Radical NNN|X]]` link in the bullet.

**Frontmatter**: `pos: ''` (empty string) → filled in as `感詞`, following the established sibling convention for Classical Chinese sentence-final/interjection particles ([[characters/乎 (char)|乎]], [[characters/哉 (char)|哉]]) rather than a content-word category.

**Body defects found**: `# Notes` used H1 instead of H2 and held nothing but the two floating CC-initial/final links — all four canonical bullets written from scratch; no `## Words` despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite six real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 也 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 total ground-truth hits — characters naming 也 as their `graphemic_classification`): 他 (char) ("another; additional," pipe-linked), 池 (char) ("pond; reservoir," pipe-linked), 馳 (char) ("run fast; drive quickly," pipe-linked), 地 (char) ("land," pipe-linked), 弛 ("slacken"), 施 ("implement") — all six added. Unlike some prior Derived Characters sections, these do **not** converge on a single reading — 也 as a phonetic component diverged across its daughter characters into five distinct Dan'a'yo syllables (ㄊㄜ, ㄐㄨㄧ, ㄑㄜ, ㄉㄧㄜ, ㄙㄝ) — the checklist's convergence note is a common pattern, not a requirement, and this family is the exception.

**Verification**: Python cross-check of all 7 `<rt>` values (1 Words + 6 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 382 — [[characters/丙 (char)|丙]]

Next never-perfected character by `danayo_id` (3004). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: origin genuinely uncertain, with competing proposals across the scholarly literature (*Erya*: a fish's tail; Shuowen: a person's shoulders; other proposals: part of a chariot, a pedestal, or a small table) and no settled consensus — its early conscription as the third Heavenly Stem erased any recoverable original pictographic meaning. `mc_id: 843` cross-checked against `lookup/CC/CC 0000.md` — exact match. Confirmed via [[characters/丁 (char)|丁]] (also filed under `radical: 一` as a Heavenly Stem, already perfected) that the vault convention does **not** force a `[[Radical 001|一]]` link into these whole-glyph pictograph bullets — 一 is just the Kangxi indexing radical here, not a depicted component, so 丙's bullet correctly omits it too.

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞`, following the sibling stem [[characters/乙 (char)|乙]] (english "second, latter," `pos: 性詞`) since 丙's own gloss "third class, tertiary" is the same descriptive/ordinal pattern, not a plain noun.

**Body defects found**: `# Notes` used H1 instead of H2 and held nothing but the two floating CC-initial/final links — all four canonical bullets written from scratch; no `## Words` despite the stand-in itself being a ground-truth hit; no `## Derived Characters` despite two real hits.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 丙 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 total ground-truth hits — characters naming 丙 as their `graphemic_classification`): 病 ("sickness"), 柄 (char) ("handle; design," pipe-linked due to the `words/柄.md` collision) — both added, both converging on 丙's own reading ㄅ⼶ㄫ as expected.

**Verification**: Python cross-check of all 3 `<rt>` values (1 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 381 — [[characters/森|森]]

Next never-perfected character by `danayo_id` (3001) — the queue jumps from 2280 straight to here, confirming the 2281–3000 range is unassigned. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct: triplication of [[Radical 075|木]] ("tree") to suggest a large number of trees, i.e. a forest — contrasted with [[林 (char)|林]] (OC \*ɡ·rɯm), which uses only two 木 for a smaller "grove, woods." `mc_id: 6257` is beyond the local mirror's ~4000-rank ceiling (confirmed absent from `lookup/CC/CC 0000–3000.md`) — trusted verbatim per the long-tail policy.

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `words/森林.md`'s own field.

**Body defects found**: no disambiguation callout needed (no `words/森.md` collision) but the `meta-bind-embed` block was otherwise the only thing before Notes — fine. Notes bullet 1 didn't link the radical component at all (bare "Triplication of 木"); a stray non-canonical bullet ("Dropped from the Korean HS list in 2000") sat as its own line instead of being folded into bullet 1, per the established convention seen on [[characters/兎 (char)|兎]]; the SKIP/Stroke bullet had the syllable link wrongly appended to it; the MC rank bullet was missing outright, with both CC initial/final links floating at the very bottom of the file instead of embedded in it; `## Chengyu` was ordered *before* `## Words`, the reverse of the canonical body order; two Words entries (森羅, 盧森堡) were bare wikilinks with no ruby or gloss.

**Words cross-check** (3 total ground-truth hits): 森林 (stand-in) already ruby'd, kept; 森羅, 盧森堡 reformatted to ruby+gloss from stored fields.

**Chengyu**: 1 ground-truth hit — 森羅万象 — already ruby'd, kept, section moved after Words.

**Derived Characters**: none (`graphemic_classification: 森` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 380 — [[characters/被 (char)|被]]

Next never-perfected character by `danayo_id` (2280) — the last character in the 2xxx range; the queue jumps straight to 3001 (`characters/森.md`) after this one. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 皮` already correct — verified via Wiktionary: 形声, semantic [[Radical 145|衣]] ("clothing") + phonetic [[皮]] (OC \*bral), cognate with [[披 (char)|披]] ("to wear; to be covered") — originally "to cover, a coverlet," extended metaphorically to the passive-voice marker. `mc_id: 627` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ''` (empty string) → filled in as `関詞` (Relational), matching the stand-in word `words/被.md`'s own field — nicely corroborated by the vault's own grammar taxonomy (`AIOS/grammar/文法 - 97品詞.md`), which explicitly lists "Passive agent - 被" under 関詞/Relationals.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist despite the stand-in 被 itself being a ground-truth hit.

**Words cross-check** (1 total ground-truth hit, the self-referential stand-in): 被 — added from stored fields (`english: -ee (but a prefix)`).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 皮` matches no other character) — correctly omitted.

**Verification**: Python cross-check of the 1 `<rt>` value against `words/被.md`'s own `注音` field — 0 mismatches.

### 2026-07-25, iteration 379 — [[characters/処 (char)|処]]

Next never-perfected character by `danayo_id` (2279). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — and this one had a genuinely surprising etymological wrinkle worth double-checking: 会意 of 夂 ("foot," originally 人) and [[Radical 016|几]] ("table, stool") — to arrive at a table and stop, "to dwell, to be at a place." A Chinese-language search confirmed that, per Shuowen, **処 (this exact form) is actually the standard/original character**, while 處 (with 虍 added) is the *later* variant that came to dominate — the reverse of the usual assumption that 処 is merely a Japanese simplification of 處. `mc_id: 323` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 處). `pos: 代詞` was already correctly filled.

**Small pre-existing defect found and fixed**: the disambiguation callout was non-standard ("This is about the character." with no character name, and a bracket-style `[[words/処]]` link) — normalized to the standard "This is a page about the character 処." template with a proper Markdown link.

**Body defects found**: `## Words` sat before `## Notes` with nothing in Notes but the two floating CC-initial/final links; one entry (一処) used a bare relative-path link; two entries (処決, 処分) were bare wikilinks with no ruby; **9 of 14** ground-truth words missing outright, including the stand-in 処 itself and the entire correlative-chart family (何処/其処/彼処/某処/此処/毎処/皆処) plus 近処.

**Words cross-check** (14 total ground-truth hits): 処女, 処格 already ruby'd, kept; 一処 reformatted to a wikilink; 処決, 処分 reformatted to ruby+gloss; 9 missing — 処 (stand-in), 何処, 其処, 彼処, 某処, 此処, 毎処, 皆処, 近処 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 処`/`处`/`處` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 14 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 378 — [[characters/鼻 (char)|鼻]]

Next never-perfected character by `danayo_id` (2278) — the queue now jumps straight from 2280 to 3001 after the next two characters, suggesting the 2281–3000 id range is either already fully perfected or simply unassigned. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 畀` already correct — verified via Wiktionary: 形声 (OC \*blids), semantic [[Radical 132|自]] ("nose" — before it was repurposed to mean "self," the exact same semantic shift already documented on [[自]]'s own page earlier this loop, a nice cross-check) + phonetic 畀 (OC \*pids, no vault page). `mc_id: 1643` cross-checked against `lookup/CC/CC 1000.md` — exact match. `pos: 名詞` was already correctly filled.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist at all despite three real ground-truth hits, including the stand-in 鼻 itself; no `## Chengyu` despite a real hit.

**Words cross-check** (3 total ground-truth hits): all three missing — 鼻 (stand-in), 鼻水, 阿鼻 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 阿鼻叫喚 ("agonized cries in the midst of tragedy," from 阿毘達磨俱舍論) — added.

**Derived Characters**: none (`graphemic_classification: 鼻` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 377 — [[characters/麦|麦]]

Next never-perfected character by `danayo_id` (2277). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 来` already correct — verified via Wiktionary: 形声 (OC \*mrɯːɡ), semantic 夊 ("footprint pointing down; to walk slowly" — Shuowen: the ancient belief that wheat came from the heavens) + phonetic [[来 (char)|来]] (OC \*m·rɯːɡ). Genuinely interesting etymological footnote: 麥/麦 and 來/来 are historically **unrelated** despite the phonetic borrowing — 來 originally meant "wheat" but was phonetically borrowed to mean "to come," and 麥 was likely coined during the Warring States period specifically to preserve the original "wheat" sense once 來 lost it. `mc_id: 1534` cross-checked against `lookup/CC/CC 1000.md` — exact match (traditional form 麥).

**Frontmatter**: `pos: ''` (empty string) → filled in as `名詞`, matching the stand-in word `大麦.md`'s own field.

**Body defects found**: Notes held no canonical bullets at all — all four written from scratch; the two CC-initial/final links were stranded in the middle of `## Words` instead of embedded in an MC bullet; one entry (麦茶) used a dash-separated gloss instead of a quoted one; two entries (麦芽糖, 麦芽) were bare wikilinks with no ruby; 3 of 7 ground-truth words missing.

**Words cross-check** (7 total ground-truth hits): 大麦 (stand-in) already ruby'd, annotation added; 麦茶 reformatted to a quoted gloss; 麦芽糖, 麦芽 reformatted to ruby+gloss; 3 missing — 丹麦 ("Denmark"), 大麦茶, 麦酒 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 麦`/`麥` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 376 — [[characters/鳴 (char)|鳴]]

Next never-perfected character by `danayo_id` (2276), immediately following [[characters/鳥 (char)|鳥]] — the two share the same radical. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[口 (char)|口]] ("mouth") and [[Radical 196|鳥]] ("bird") — a bird's cry, vocalization. `mc_id: 865` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `鳴.md` has a blank `pos` field too; decided from the leading gloss ("cry, chirp," an animal vocalization action).

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist at all despite two real ground-truth hits, including the stand-in 鳴 itself.

**Words cross-check** (2 total ground-truth hits): both missing — 鳴 (stand-in), 鶏鳴 — added from stored fields.

**Chengyu**: 1 ground-truth hit (鶏鳴狗盗) — already present and correctly ruby'd, no changes needed.

**Derived Characters**: none (`graphemic_classification: 鳴`/`鸣` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values (2 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 375 — [[characters/鳥 (char)|鳥]]

Next never-perfected character by `danayo_id` (2275). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a bird with a dangling tail. `mc_id: 581` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `鳥.md`'s own field.

**Body defects found**: `## Notes` held only the two floating CC-initial/final links plus three loose Words-style entries; SKIP/Stroke, MC, and Levels bullets were all missing; **14 of 19** ground-truth words missing outright, including the stand-in 鳥 itself — the largest raw absolute gap of any page this loop; no `## Chengyu` despite two real hits; no `## Derived Characters` despite two real hits.

**Words cross-check** (19 total ground-truth hits): 禽鳥, 堅鳥 (already ruby'd, kept), 七面鳥, 九官鳥 (already ruby'd, moved out of Notes), 鳥籠 (moved out of Notes, ruby added — caught and corrected a transcription slip of my own on its `<rt>` before the final verification pass) accounted for the 5 pre-existing entries; 14 missing outright — 鳥 (stand-in), 白鳥, 烏鳥, 鳩鳥, 鵝鳥, 雛鳥, 就鳥, 椋鳥, 啄木鳥, 麻雀鳥, 飛鳥, 鳥嘴, 鳥巣, 鳥類 — all added from stored fields.

**Chengyu**: 2 ground-truth hits — 一石二鳥 ("kill two birds with one stone"), 轄魚鳥牲 (Biblical) — both added.

**Derived Characters** (2 hits via `graphemic_classification: 鳥`): [[鵰 (char)|鵰]] ("eagle, vulture"), [[島 (char)|島]] ("island") — section added.

**Verification**: Python cross-check of all 23 `<rt>` values (19 Words + 2 Chengyu + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 374 — [[characters/首|首]]

Next never-perfected character by `danayo_id` (2274). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: originally the head of an animal with a long mouth and horns, simplified from 𩠐 (hair component 巛 reduced to 丷 over time); the word was eventually replaced by [[頭 (char)|頭]] during the Warring States period, possibly to avoid phonetic overlap with [[手 (char)|手]] ("hand"). `mc_id: 375` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 名詞` was already correctly filled, matching the stand-in word `首長.md`'s own field.

**Body defects found**: the graphemic bullet was a leftover raw "Components: [[丷]], [[𦣻]]" fragment — rewritten from scratch; SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; two pre-existing entries (首長, 首尾) were bare wikilinks with no ruby; 2 of 6 ground-truth words missing; no `## Chengyu` despite a real hit — the same 銀盤呈首 already documented on [[characters/銀 (char)|銀]]'s page earlier this loop, here missing from its other constituent character's own page.

**Words cross-check** (6 total ground-truth hits): 頓首, 首領 already ruby'd, kept; 首長 (stand-in), 首尾 reformatted to ruby+gloss; 部首, 首都 missing outright — both added from stored fields.

**Chengyu**: 1 ground-truth hit (銀盤呈首) — added.

**Derived Characters**: none (`graphemic_classification: 首` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values (6 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 373 — [[characters/養|養]]

Next never-perfected character by `danayo_id` (2273; 2272 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 羊` already correct in the frontmatter, but **the pre-existing bullet mislabeled the structure as 会意** ("会意 of 羊 + 食") when the field itself already correctly stores 羊 as a *phonetic* component name. Wiktionary/Shuowen confirm: 形声 (OC \*laŋʔ, \*laŋs), semantic [[Radical 184|食]] ("to feed") + phonetic [[羊]] (OC \*laŋ) — Shuowen explicitly states "羊聲" ("羊 provides the sound"). Corrected the bullet's classification label to match the field, rather than the reverse.

**Frontmatter**: `pos: 事詞` was already correctly filled, matching the stand-in word `養育.md`'s own field. `mc_id: 451` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Body defects found**: a leftover bare "1. raise" fragment (redundant with the `english:` field) sat where the graphemic bullet should have been; SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; the periodic-table "oxygen" abbreviation aside was kept as a fifth supplementary bullet, its broken relative-path link fixed to a wikilink; 7 of 13 ground-truth words missing outright (including the stand-in 養育 itself); two pre-existing entries (養殖, 養父) were bare wikilinks with no ruby.

**Words cross-check** (13 total ground-truth hits): 飼養, 栄養, 栄養素 already ruby'd, kept; 養素 (the oxygen abbreviation) folded into `## Words` properly; 養殖, 養父 reformatted to ruby+gloss; 7 missing — 養育 (stand-in), 営養, 培養, 養子, 養成, 養母, 養生 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 養`/`养` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 13 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 372 — [[characters/飛 (char)|飛]]

Next never-perfected character by `danayo_id` (2271). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a bird flying upwards, from Proto-Sino-Tibetan \*mV-pjər ("to fly"), cognate with Tibetan འཕུར. `mc_id: 835` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `飛.md`'s own `pos: 動詞` isn't a real category in this vault's taxonomy; decided independently as the more specific eventive class, same judgment pattern as [[characters/観|観]] and [[characters/運|運]] earlier this loop.

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached between the pre-existing graphemic bullet and a genuinely interesting aspectual-difference aside (kept as a fifth supplementary bullet — 飛 alone denotes a short/immediate flight, 飛行 a prolonged "real" flight); 3 of 8 ground-truth words were bare wikilinks with dash-glosses instead of ruby+quoted-gloss; 3 more were missing outright; no `## Chengyu` despite a real hit.

**Words cross-check** (8 total ground-truth hits, searched under both aliases 飞/蜚): 飛 (stand-in), 飛翔 already ruby'd, kept; 飛鳥, 飛机, 飛行 reformatted from bare wikilinks to ruby+gloss; 3 missing — 飛報, 飛行机, 飛語 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 流言飛語 ("rumors are flying") — added.

**Derived Characters**: none (`graphemic_classification: 飛`/`飞`/`蜚` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values (8 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 371 — [[characters/類|類]]

Next never-perfected character by `danayo_id` (2270) — already partially touched at iteration 329 (a backlink for the newly-created 衣類 was added to this page in passing), but never brought to full compliance itself until now. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 頪` already correct — verified via Wiktionary: 形声 (OC \*ruːls, \*ruds), semantic [[Radical 094|犬]] ("dog") + phonetic 頪 (OC \*roːds, no vault page) — from Proto-Sino-Tibetan \*rus ("bone"); extended to "kind, category, class." `mc_id: 584` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `種類.md`'s own field. `hanmun_edu_level: 高等` maps to `Korean HS`, not `Korean MS` — first character this loop with that non-中 value.

**Body defects found**: the graphemic bullet had an empty semantic gloss and an entirely empty phonetic link; SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached in the middle of the Notes section; no `## Words` heading existed at all — every single entry (the seven correlative-chart words, 類似, 分類学, 類似格, 衣類) was sitting loose directly in Notes; **9 of 20** ground-truth words missing outright, including the stand-in 種類 itself.

**Words cross-check** (20 total ground-truth hits — the largest ground-truth count found on any page this entire loop, tied only by [[characters/自|自]]'s 24 for scale): 類似, 分類学, 類似格, 衣類, and all seven correlative-chart entries (此類/其類/彼類/何類/毎類/某類/皆類) moved out of Notes into a proper `## Words` heading; 9 missing outright — 種類 (stand-in), 人類, 人類学, 貝類, 霊長類, 類人猿, 魚類, 鳥類, 鼠類 — all added from stored fields. The "cannot appear alone, only correlative-chart member to do so" aside was kept as a fifth supplementary Notes bullet.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 類`/`类` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 20 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 370 — [[characters/願|願]]

Next never-perfected character by `danayo_id` (2269). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 原` already correct — verified via Wiktionary: 形声 (OC \*ŋʷans), semantic [[Radical 181|頁]] ("head") + phonetic [[原]] (OC \*ŋʷan) — desire, wish. `mc_id: 423` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Genuine `stand_in` error found and fixed**: the field pointed at `要請` — a real word, but one built from 要+請, with **no 願 in it at all**. A vault-wide search confirmed `願意.md` is the only word file in the database that actually contains 願 (or its alias 愿) as a constituent character; corrected `stand_in` to `願意`. Different defect class from this loop's usual graphemic-classification fixes — this is the first `stand_in`-field correction of the entire loop.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the (corrected) stand-in word `願意.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist at all — unsurprising, since the previously-listed stand-in didn't even contain the character.

**Words cross-check** (1 total ground-truth hit, now that `stand_in` points at the right word): 願意 — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 願`/`愿` matches no other character) — correctly omitted.

**Verification**: the one `<rt>` value cross-checked against its source file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 369 — [[characters/題|題]]

Next never-perfected character by `danayo_id` (2268). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 是` already correct in the frontmatter, but **the pre-existing bullet again had semantic and phonetic swapped** (the same defect class as [[characters/部 (char)|部]]'s 咅/邑 case a few iterations back) — it labeled [[是]] as semantic with an empty broken link where the real semantic component belonged. Wiktionary confirms: 形声 (OC \*deː, \*deːs), semantic [[Radical 181|頁]] ("head") + phonetic [[是 (char)|是]] (OC \*djeʔ) — originally "forehead," extended to "title, topic, question." Rewrote the bullet with the correct assignment. `mc_id: 2668` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `標題.md`'s own field.

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; one Words entry (題目) used a bare relative-path Markdown link with a dash-gloss instead of a proper wikilink; 2 of 5 ground-truth words missing (including the stand-in 標題 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (5 total ground-truth hits): 問題, 宿題 already correctly ruby'd, kept; 題目 reformatted to a proper wikilink; 標題 (stand-in), 主題 missing — both added from stored fields.

**Chengyu**: 1 ground-truth hit — 先題後述 ("topic-comment," Dan'a'yo-original per `origin: 単亜語`) — added.

**Derived Characters**: none (`graphemic_classification: 題`/`题` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 6 `<rt>` values (5 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 368 — [[characters/順|順]]

Next never-perfected character by `danayo_id` (2267). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 川` already correct — verified via Wiktionary: 形声 (OC \*ɢljuns), semantic [[Radical 181|頁]] ("head") + phonetic [[川 (char)|川]] ("river"); the Shuowen alternatively reads it as 会意, "flowing with the river's current," i.e. "to follow, obey." `mc_id: 414` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 性詞` was already correctly filled, matching the stand-in word `順次.md`'s own field.

**Body defects found**: page structure inverted — `## Words` sat before `## Notes`; the graphemic bullet was a leftover raw "Components: [[川]], [[頁]]" fragment — rewritten from scratch, with the phonetic link corrected to the pipe form `[[川 (char)|川]]` (word/川.md collision); SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; 2 of 3 ground-truth words missing; no `## Chengyu` despite a real hit.

**Words cross-check** (3 total ground-truth hits): 順次 (stand-in) already present, annotation added; 帰順, 順序 missing — both added from stored fields.

**Chengyu**: 1 ground-truth hit — 一帆風順 ("smooth sailing, bon voyage") — added.

**Derived Characters**: none (`graphemic_classification: 順`/`顺` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 367 — [[characters/面|面]]

Next never-perfected character by `danayo_id` (2266; 2265 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a man's face, with an eye exaggerated, derived from 𦣻; the horizontal stroke was added later. `mc_id: 460` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 名詞` was already correctly filled, matching the stand-in word `表面.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; **9 of 14** ground-truth words missing outright, the largest raw gap-fill since [[characters/部 (char)|部]]'s 14-of-23; no `## Chengyu` despite a real hit; no `## Derived Characters` despite a real hit.

**Words cross-check** (14 total ground-truth hits): 表面 (stand-in), 上面, 側面, 七面鳥, 面疱 already present and correctly ruby'd; 9 missing — 仮面, 北面, 四面, 方面, 書面, 水面, 裏面, 面田 ("Myanmar," via the 緬 alias), 顔面 — all added from stored fields.

**Chengyu**: 1 ground-truth hit — 四面楚歌 ("surrounded by the singing of Chu") — added.

**Derived Characters** (1 hit via `graphemic_classification: 面`): [[麺 (char)|麺]] ("noodles, flour") — section added.

**Verification**: Python cross-check of all 16 `<rt>` values (14 Words + 1 Chengyu + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 366 — [[characters/静|静]]

Next never-perfected character by `danayo_id` (2264). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 争` already correct — verified via Wiktionary: 形声 (OC \*zleŋʔ), a doubly-phonetic compound of [[Radical 174|青]] (OC \*sʰleːŋ — also functioning semantically per Shuowen) + [[争]] (OC \*ʔsreːŋ) — consistent with [[争]]'s own page, perfected earlier this loop, which already lists 静 among its Derived Characters. `mc_id: 852` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 靜).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `静寂.md`'s own field.

**Body defects found**: page structure inverted — `## Words` sat before `# Notes` (which was also H1), same inversion class as this loop's several earlier cases; Notes held only the two floating CC-initial/final links plus one loose bare-wikilink entry (静寂, the stand-in itself); all four canonical bullets written from scratch; 2 of 4 ground-truth words missing; no `## Chengyu` despite a real hit.

**Words cross-check** (4 total ground-truth hits): 安静, 寂静 already ruby'd, kept; 静寂 (stand-in) promoted from a loose Notes entry into `## Words` with ruby added; 平静 missing outright — added from stored fields.

**Chengyu**: 1 ground-truth hit — 涅盤寂静 ("nirvana is peace," Buddhist origin) — added.

**Derived Characters**: none (`graphemic_classification: 静`/`靜` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values (4 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 365 — [[characters/難|難]]

Next never-perfected character by `danayo_id` (2263). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 漢` **checked carefully, kept as-is**: an English Wiktionary fetch named the phonetic component 暵 (an obscure character with no vault page), not 漢 — but a cross-check found [[characters/嘆 (char)|嘆]] *also* cites `漢` as its own classification, and 漢's own page cites 熯 as its phonetic (熯/暵/堇 all belong to the same root family) — this is a real, established two-character vault convention of citing the nearest well-known, page-having relative (漢) as a proxy for an obscure phonetic root, the same "verify before correcting" pattern as [[characters/銭|銭]]'s `㦮` and [[characters/関 (char)|関]]'s `丱` the last two iterations. Kept `漢`, wrote the bullet noting 難 originally meant "a type of bird," later phonetically borrowed for "difficult, hardship" (from Proto-Sino-Tibetan \*mV-nar, "to suffer"). `mc_id: 273` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `困難.md`'s own field.

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached above a periodic-table-abbreviation aside (kept as a fifth supplementary bullet); the stand-in 困難 was present in `## Words` but missing its stand-in annotation; no `## Derived Characters` despite a real hit. All five ground-truth words were otherwise already present and correctly ruby'd — an unusually clean Words section for this loop.

**Words cross-check** (6 total ground-truth hits): 困難 (stand-in, annotation added), 殉難, 苦難, 艱難, 受難, 難金 all already present and correctly ruby'd — no additions needed.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 難`): [[灘 (char)|灘]] ("bank, shoal") — section added.

**Verification**: Python cross-check of all 7 `<rt>` values (6 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 364 — [[characters/関 (char)|関]]

Next never-perfected character by `danayo_id` (2262). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 丱` **initially suspected wrong, verified correct** — an English Wiktionary fetch named the phonetic component 𢇅, not 丱, prompting a closer look; a follow-up Chinese-language search confirmed 丱 and its near-identical variant 卝 are both legitimately cited across sources as the phonetic component for this character family (关/関/關), depicting a bronze-script door locked with two wooden sticks — 丱/卝 is explicitly the standard citation for the simplified/shinjitai branch (关, 関), matching this exact character. Kept the field as `丱`, same "double-check before correcting" pattern as [[characters/銭|銭]]'s `㦮` last iteration. `mc_id: 424` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 關).

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; `## Words` existed with only 3 of 8 ground-truth entries, one ruby'd and two bare; 5 of 8 ground-truth words missing (including the stand-in 関 itself).

**Words cross-check** (8 total ground-truth hits): 机関 already ruby'd, kept; 関島, 関数 reformatted from bare wikilinks to ruby+gloss; 5 missing — 関 (stand-in), 関係, 関心, 関詞, 指関節 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 関`/`關`/`关` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 363 — [[characters/銭|銭]]

Next never-perfected character by `danayo_id` (2261). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 㦮` **initially suspected wrong, verified correct** — 㦮 looked like an obscure/miscopied component at first glance (no vault page, unfamiliar glyph), but Wiktionary confirms it's the genuine extended-shinjitai form of 戔 (traditional) / 戋 (simplified), used specifically in the Japanese-shinjitai branch of this phonetic family — and 7 *other* vault characters ([[浅 (char)|浅]], [[残 (char)|残]], [[践]], [[桟]], [[賎]], [[箋]], [[盞]]) already consistently cite the identical `㦮` string, confirming this is a deliberate, vault-wide convention rather than an isolated typo. Wrote the graphemic bullet from scratch: 形声 (OC \*ʔslenʔ, \*zlen), semantic [[Radical 167|金]] ("metal, money") + phonetic 㦮 (OC \*zlaːn). `mc_id: 709` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 錢). `pos: 名詞` was already correctly filled.

**Body defects found**: the graphemic bullet was a leftover raw "Components: [[金]], [[㦮]]" fragment — rewritten from scratch; SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; `## Words` heading didn't exist at all despite the one real ground-truth hit (the stand-in itself).

**Words cross-check** (1 total ground-truth hit): 金銭 (stand-in) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none — the seven other characters sharing `graphemic_classification: 㦮` are siblings descending from the same phonetic root, not descendants of 銭 itself, so none qualify as 銭's own Derived Characters — correctly omitted.

**Verification**: the one `<rt>` value cross-checked against its source file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 362 — [[characters/銀 (char)|銀]]

Next never-perfected character by `danayo_id` (2260), immediately following [[characters/鉄 (char)|鉄]] — the two share the periodic-table-abbreviation convention and, coincidentally, the same `japanese_native` YAML defect. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 艮` already correct — verified via Wiktionary: 形声 (OC \*ŋrɯn), semantic [[Radical 167|金]] ("metal") + phonetic [[艮]] (OC \*kɯːns). `mc_id: 2121` cross-checked against `lookup/CC/CC 2000.md` — exact match. `pos: 名詞` was already correctly filled.

**Small pre-existing defect found and fixed**: `japanese_native` had the same malformed-YAML shape as [[characters/鉄 (char)|鉄]] last iteration — a bare scalar (`しろがね`) followed by a redundant indented list item — except this one also hid a **non-breaking space** (U+00A0) after the duplicate value, which made the Edit tool's exact-string matching fail on the first attempt; resolved by reading the raw bytes with Python and rewriting the field as a clean single-item list.

**Body defects found**: `## Notes` and `## Words` both lacked blank-line separation from adjacent content, and the SKIP/Stroke/MC/Levels bullets were entirely missing, with the two CC-initial/final links and one loose bare-wikilink entry (銀行) stranded below the Chengyu section instead of properly placed; the one Chengyu entry (銀盤呈首) used a dash-separated gloss on a relative-path link instead of the standard ruby+quoted-gloss wikilink; 4 of 7 ground-truth words missing (including the stand-in 銀 itself); 1 of 2 ground-truth chengyu missing.

**Words cross-check** (7 total ground-truth hits): 銀河, 銀色 already ruby'd, kept; 銀行 reformatted from a bare wikilink to ruby+gloss (caught and corrected a transcription slip of my own on its `<rt>` before the final verification pass); 4 missing — 銀 (stand-in), 水銀, 軽銀, 銀河系 — added from stored fields.

**Chengyu cross-check** (2 total ground-truth hits): 銀盤呈首 reformatted to the standard wikilink+quoted-gloss form; 金銀銅鉄 (Biblical, already added to [[characters/鉄 (char)|鉄]]'s own page last iteration) missing here — added.

**Derived Characters**: none (`graphemic_classification: 銀`/`银` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values (7 Words + 2 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 361 — [[characters/鉄 (char)|鉄]]

Next never-perfected character by `danayo_id` (2259). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 呈` was wrong and directly contradicted the page's own pre-existing bullet**, which already correctly described phonetic 失: 鉄 is the Japanese shinjitai of 鐵 (OC \*l̥ʰiːɡ, from Proto-Sino-Tibetan \*hljak, cognate with Tibetan ལྕགས), 形声 with semantic [[Radical 167|金]] ("metal") + phonetic [[失]] — the shinjitai's own phonetic 失 being a simplification of the traditional form's original phonetic 𢧤 (itself from a 戈+矢 complex). 呈 bears no described relationship to this etymology under any source consulted; corrected the field to `失` to match the bullet's own reasoning. `mc_id: 1308` cross-checked against `lookup/CC/CC 1000.md` — exact match (traditional form 鐵). `pos: 固有名詞` was already correctly filled, matching the stand-in word `鉄.md`'s own field (this vault's convention for element words).

**Small pre-existing defect found and fixed**: `japanese_native` was malformed YAML — a bare scalar value (`くろがね`) immediately followed by an indented list item repeating the same value — collapsed into a single clean list.

**Body defects found**: the SKIP/Stroke/MC bullet was compressed onto one line using `·` separators instead of the canonical two-bullet split (SKIP+Stroke, then MC rank+syllable); the pre-existing periodic-table-abbreviation aside was kept as a fifth supplementary bullet; 4 of 6 ground-truth words missing (including the stand-in 鉄 itself); 1 of 2 ground-truth chengyu missing.

**Words cross-check** (6 total ground-truth hits): 銑鉄, 鉄板 already present and correctly ruby'd; 鉄 (stand-in), 鉄砧, 鉄道, 鋼鉄 missing — all four added from stored fields.

**Chengyu cross-check** (2 total ground-truth hits): 磨穿鉄硯 already correctly ruby'd; 金銀銅鉄 (Biblical) missing — added.

**Derived Characters**: none (`graphemic_classification: 鉄`/`鐵`/`铁` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values (6 Words + 2 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 360 — [[characters/量|量]]

Next never-perfected character by `danayo_id` (2258). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` kept as-is: Wiktionary documents a genuinely inconclusive etymology with at least four competing theories — Yu Xingwu's 会意 (日/田 "sun/field" + 東 "bag," "to measure under the sun"), Qiu Xigui's derivation from 糧 ("grain" — corroborated by this vault's own Derived Character 糧, a satisfying cross-check), Guo Moruo's reading as the original form of 亮 ("bright"), and the Shuowen's 形声 (phonetic 曏 + semantic 重). Since the stored value already matches one of these legitimate readings (Yu Xingwu's), kept it per the loop's standing rule and documented all four theories in the bullet. `mc_id: 1074` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `数量.md` has a blank `pos` field too; decided from the leading gloss ("measure, weight, quantity," a noun).

**Body defects found**: page structure inverted — `## Words` sat before `# Notes` (which was also H1), same inversion pattern as this loop's several earlier cases; Notes held only the two floating CC-initial/final links; all four canonical bullets written from scratch; 5 of 8 ground-truth words missing (including the stand-in 数量 itself); no `## Derived Characters` despite a real hit.

**Words cross-check** (8 total ground-truth hits): 衡量, 測量, 量化詞 already present and correctly ruby'd; 5 missing — 数量 (stand-in), 容量, 産量, 過量, 量詞 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 量`): [[糧 (char)|糧]] ("provisions") — section added, doubling as corroboration for Qiu Xigui's etymological theory noted in the graphemic bullet.

**Verification**: Python cross-check of all 9 `<rt>` values (8 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 359 — [[characters/野|野]]

Next never-perfected character by `danayo_id` (2257). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 予` already correct — verified via Wiktionary: 形声 (OC \*laːʔ, \*ɦljaʔ), semantic [[Radical 166|里]] ("village" — itself 田 "field" + 土 "earth," matching the character's own `radical:` field exactly) + phonetic [[予]] (OC \*la, \*laʔ) — countryside, wilderness, open country. `mc_id: 609` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `田野.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only a stray editorial note ("By evil substitution, 別墅 must become 別野") and no canonical bullets at all — all four written from scratch, keeping the pre-existing note as a fifth supplementary bullet (reformatted with a proper gloss); `## Words` heading didn't exist at all — 別野 was sitting inside the aside instead; 4 of 6 ground-truth words missing (including the stand-in 田野 itself); no `## Derived Characters` despite two real hits.

**Words cross-check** (6 total ground-truth hits, searched under all alias forms 墅/㙒/埜/壄): 別野 promoted from the Notes aside into `## Words`, ruby kept; 田野 (stand-in), 広野, 野猪, 野獣, 野菜 missing — all five added from stored fields.

**Chengyu**: 1 ground-truth hit (哀鴻遍野) — already present and correctly ruby'd, no changes needed.

**Derived Characters** (2 hits via `graphemic_classification: 予`): [[抒]] ("express, convey"), [[序]] ("series, sequence") — section added.

**Verification**: Python cross-check of all 9 `<rt>` values (6 Words + 1 Chengyu + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 358 — [[characters/部 (char)|部]]

Next never-perfected character by `danayo_id` (2256). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 咅` already correct in the frontmatter, but **the pre-existing bullet had semantic and phonetic swapped** — it labeled [[咅]] as semantic and [[邑]] as phonetic (with 邑's OC values wrongly attached to it too), directly contradicting the field's own already-correct claim. Wiktionary confirms the real structure: semantic [[Radical 163|邑]] ("city, settlement") + phonetic [[咅]] (OC \*pʰɯʔ, \*pʰl'oːs) — originally a place name in Gansu, extended to "administrative division," "part." Rewrote the bullet with the correct assignment. `mc_id: 704` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `部.md` has no `pos` field to inherit; decided from the leading gloss ("part," a noun), corroborated by every one of the 22 other ground-truth words, all also `名詞`.

**Body defects found**: `## Notes` missing SKIP/Stroke, MC, and Levels bullets entirely, with the two CC-initial/final links floating at the very bottom past a long `## Words` list; that list itself mixed 4 ruby'd entries with **14 bare wikilinks**; 5 of 23 ground-truth words missing outright (including the stand-in 部 itself); no `## Derived Characters` despite six real hits.

**Words cross-check** (23 total ground-truth hits — the largest raw word count fully processed this loop): 胸部, 全部, 幹部, 部位 already ruby'd, kept; the 14-item bare list (北部, 腹部, 部長, 部分, 外部, 部門, 支部, 部隊, 内部, 西部, 南部, 部首, 腰部, 部族) reformatted to ruby+gloss; 5 missing outright — 部 (stand-in), 倶楽部, 大部分, 東部, 部署 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters cross-check** (6 total ground-truth hits via `graphemic_classification: 咅`): [[陪 (char)|陪]] ("accompany, be with, keep company"), [[剖]] ("dissect, bisect"), [[賠]] ("indemnify, pay damages"), [[倍 (char)|倍]] ("times"), [[菩]] ("bodhisattva"), [[培]] ("cultivate") — section added.

**Verification**: Python cross-check of all 29 `<rt>` values (23 Words + 6 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 357 — [[characters/選|選]]

Next never-perfected character by `danayo_id` (2255). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 巽` already correct. The pre-existing semantic-component link needed real diligence: an initial English-Wiktionary fetch claimed the semantic component was 止 (linked to Radical 077), but this character's own `radical:` frontmatter field says 辵, and every other 辵-radical character processed in this loop (達/適/過/速/運/連/退/追) cites [[Radical 162|辵]] as its semantic component — a direct contradiction. Cross-checked with a Chinese-language search of the Shuowen Jiezi's own gloss, which explicitly confirms 辵 ("movement") + 巽/巺 (phonetic, also glossed "遣," "to dispatch"): to respectfully reject and send someone back, choosing implying rejecting others. Treated the "止" claim as another likely fetch/summarization error (same pattern as [[characters/興 (char)|興]]'s 型 case earlier this loop) and corrected the bullet's link from Radical 077 to [[Radical 162|辵]]. `mc_id: 990` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 事詞` was already correctly filled.

**Body defects found**: sections badly out of order — `## Chengyu` sat before the CC-initial/final links, which themselves sat before a separate `## Words`; the semantic component's gloss was also empty (`("")`, on top of the wrong Radical link); 3 of 4 ground-truth words missing (including the stand-in 選択 itself); one chengyu entry (多召少選) used a dash-separated gloss instead of the quoted format.

**Words cross-check** (4 total ground-truth hits, searched under all four alias forms 銓/撰/选/籤): 甄選 already present and correctly ruby'd; 選択 (stand-in), 選抜, 杜撰 missing — all three added from stored fields.

**Chengyu cross-check** (2 total ground-truth hits): 選士唯賢 already correctly formatted; 多召少選 reformatted from a dash-gloss relative-path link to the standard ruby+quoted-gloss wikilink.

**Derived Characters**: none — no other character in the database names 選/銓/撰/选/籤/巽 as its own `graphemic_classification` — correctly omitted.

**Verification**: Python cross-check of all 6 `<rt>` values (4 Words + 2 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 356 — [[characters/適|適]]

Next never-perfected character by `danayo_id` (2254), immediately following [[characters/達 (char)|達]] — a second consecutive phonetic-component correction. Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 帝` was wrong** — Wiktionary's real phonetic component is **啻** (OC \*hljeɡs), which is already listed as this very character's own alias field, not 帝 (a visually similar but unrelated character with its own large, genuinely separate phonetic family in this vault — 締/蹄/嫡/啼/滴/摘/諦/敵 all cite 帝 directly, none of them related to 適). 適 is 形声, semantic [[Radical 162|辵]] ("movement") + phonetic 啻; the original form was 𨗁, later stylized with the inner component becoming 啇. Corrected the field to `啻`. `mc_id: 557` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word `適宜.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 1 of 2 ground-truth words missing (the stand-in 適宜 itself).

**Words cross-check** (2 total ground-truth hits): 適応 already present and correctly ruby'd; 適宜 (stand-in) missing — added from stored fields.

**Chengyu**: 1 ground-truth hit (現代適応) — already present and correctly ruby'd, no changes needed.

**Derived Characters**: none — the eight characters citing "帝" belong to 帝's own phonetic family, not 適's (now correctly 啻); no character in the database names 適/啻/适 as its own classification — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values (2 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 355 — [[characters/達 (char)|達]]

Next never-perfected character by `danayo_id` (2253). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 大` was wrong** — Wiktionary's real phonetic component is **羍** (no vault page), not the bare 大 that happens to sit at its base; 達 is 形声 (OC \*tʰaːd, \*daːd), semantic [[Radical 162|辵]] ("movement") + phonetic 羍 (OC \*tʰaːd), sharing its phonetic series with 羍/闥/撻/躂, all deriving from a root meaning movement or arrival. Corrected the field to `羍`. `mc_id: 746` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 事詞` was already correctly filled.

**Body defects found**: `# Notes` used H1 instead of H2; SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links stranded on their own lines; the pre-existing "abbreviation for darmstadtium" note was kept as a fifth supplementary bullet, same treatment as similar asides elsewhere this loop; 4 of 5 ground-truth words missing (including the stand-in 達 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (5 total ground-truth hits): 達金 already present and correctly ruby'd; 達 (stand-in), 到達, 暢達, 乾達婆 (a Sanskrit loanword, "Gandharva") missing — all four added from stored fields.

**Chengyu**: 1 ground-truth hit — 信達雅化 ("faithful, transparent, elegant -ization," the classical Yan Fu translation triad) — added.

**Derived Characters**: none (`graphemic_classification: 達`/`逹`/`达`/`羍` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 6 `<rt>` values (5 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 354 — [[characters/過 (char)|過]]

Next never-perfected character by `danayo_id` (2252). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 咼` already correct — verified via Wiktionary: 形声 (OC \*kloːl, \*kloːls), semantic [[Radical 162|辵]] ("walk") + phonetic [[咼]] (OC \*kʰʷroːl) — to pass, cross through. `mc_id: 194` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `修飾語` — neither the stand-in word `過.md` nor the ground-truth words offered a clean matching convention (they split between `実詞`/`名詞`); decided independently from the character's own function here, "than, too" — a comparative/degree marker, matching the 修飾語 (Modifiers) category used elsewhere in this vault for similar function words (e.g. 皆/且).

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus three loose Words-style entries (過激, 過量, 過去 — all bare dash-glosses); all four canonical bullets written from scratch; 3 of 7 ground-truth words missing, including the stand-in 過 itself.

**Words cross-check** (7 total ground-truth hits): 経過 already ruby'd, kept; 過激, 過量, 過去 moved out of Notes into `## Words` with ruby added; 3 missing — 過 (stand-in), 不過, 通過 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 過`/`过` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 353 — [[characters/運|運]]

Next never-perfected character by `danayo_id` (2251) — this character was already cited as a Derived Character of [[characters/軍|軍]] two iterations ago, but hadn't been perfected itself yet. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 軍` already correct — verified via Wiktionary: 形声 (OC \*ɢuns), semantic [[Radical 162|辵]] ("motion") + phonetic [[軍]] (OC \*kun) — to move, transport; fortune, luck. `mc_id: 1124` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `運送.md`'s own `pos: 実詞` is broader; decided independently as the more specific eventive class, same judgment pattern as [[characters/観|観]]'s `動詞`→`事詞` case.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus three loose Words-style entries (運命, 運行, 運数 — all bare dash-glosses); all four canonical bullets written from scratch; 5 of 10 ground-truth words missing (including the stand-in 運送 itself).

**Words cross-check** (10 total ground-truth hits): 運動, 運動家 already ruby'd, kept; 運命, 運行, 運数 moved out of Notes into `## Words` with ruby added (caught and corrected two transcription slips of my own on 運命/運行's `<rt>` values — both initially mis-copied from 命運's — before the final verification pass); 5 missing outright — 運送 (stand-in), 命運, 天運, 幸運, 運転 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 運`/`运` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 10 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 352 — [[characters/連 (char)|連]]

Next never-perfected character by `danayo_id` (2250). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[辶]] ("to walk") + [[車]] ("chariot") — man-drawn carriage; also confirms the vault's own note that 聯/联 and 連 were historically two characters for the same word (Zhou-era 聯 vs Han-era 連), now officially merged in Japanese. `mc_id: 703` cross-checked against `lookup/CC/CC 0000.md` — exact match. `pos: 性詞` was already correctly filled.

**Body defects found**: **two duplicate `## Words` headings**, the first containing a mix of ruby'd entries, bare wikilinks, and a nested "As in Japanese, we officially merge 聯 into this character" aside; one entry (蘇連) was a self-referential broken link (`[[蘇連]] not [[蘇連]]` — clearly meant to contrast with 蘇聯, but pointed at itself); SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; no `## Chengyu` or `## Derived Characters` despite one real hit each; **7 of 22** ground-truth words missing outright, the largest raw word count of any page this loop (surpassing [[characters/自|自]]'s 24 only in that 自 had more total, but 連 had more *entirely absent* — a genuinely undercooked page relative to its real vocabulary family).

**Words cross-check** (22 total ground-truth hits, searched under all three alias forms 连/聯/联): 連体, 連合王国, 連合国, 連濁, 連続, 連帯, 国連 already ruby'd, kept; 互連網, 対連, 連接, 連接詞, 連合, 連盟, 連邦 reformatted from bare wikilinks to ruby+gloss; 蘇連's self-referential link fixed and ruby'd; 7 missing outright — 連 (stand-in), 連日, 連週, 連月, 連年, 連世紀, 連結 — added from stored fields. Reorganized into a coherent stand-in-first, then time-repetition, then alliance/federation, then miscellaneous grouping.

**Chengyu**: 1 ground-truth hit — 骨肉相連 ("bone of my bone and flesh of my flesh") — added.

**Derived Characters** (1 hit via `graphemic_classification: 連`): [[蓮 (char)|蓮]] ("lotus") — section added.

**Verification**: Python cross-check of all 24 `<rt>` values (22 Words + 1 Chengyu + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 351 — [[characters/速 (char)|速]]

Next never-perfected character by `danayo_id` (2249). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 束` already correct — verified via Wiktionary: 形声 (OC \*sloːɡ), semantic [[Radical 162|辵]] ("motion") + phonetic [[束 (char)|束]] (OC \*hljoɡ) — fast, rapid motion. `mc_id: 1363` cross-checked against `lookup/CC/CC 1000.md` — exact match. `pos: 性詞` was already correctly filled.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus one loose bare-wikilink entry (速様); all four canonical bullets written from scratch; 2 of 4 ground-truth words missing, including the stand-in 速 itself.

**Words cross-check** (4 total ground-truth hits): 迅速, 急速 already present and correctly ruby'd; 速様 promoted from a loose Notes entry into `## Words` with ruby added; 速 (stand-in) missing outright — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 速` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 350 — [[characters/退 (char)|退]]

Next never-perfected character by `danayo_id` (2248), immediately following [[characters/追 (char)|追]] — the two share the same radical and SKIP code. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: oracle-bone 会意 of [[Radical 162|辶]] ("to walk") and [[艮]] (originally 皀, "food vessel" — visually merged with the unrelated character 艮 in the modern glyph, the same shape-drift pattern as 即/既/郷) — to leave the table after eating, extended to "retreat, withdraw"; the Shuowen instead reads 彳+夊+日, "to walk away from the sun." `mc_id: 528` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 事詞` was already correctly filled.

**Body defects found**: the graphemic bullet was a bare "Components: [[辶]], [[艮]]" fragment — rewritten from scratch with the full etymology and the radical link corrected to point at [[Radical 162|辶]]; SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links floating unattached; `## Words` heading didn't exist at all despite four real ground-truth hits, including the stand-in 退 itself; no `## Derived Characters` despite a real hit.

**Words cross-check** (4 total ground-truth hits): all four missing — 退 (stand-in), 辞退, 衰退, 退職 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 退`): [[腿]] ("thigh") — section added.

**Verification**: Python cross-check of all 5 `<rt>` values (4 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 349 — [[characters/追 (char)|追]]

Next never-perfected character by `danayo_id` (2247). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 堆` was wrong** — same error class as [[characters/観|観]]'s 鸛 a few iterations back: 堆 is itself a *derived* character (built from 土+𠂤), not 追's true phonetic root. Wiktionary confirms 追 is 形声 (OC \*tul, \*truj), semantic [[Radical 162|辵]] ("movement") + phonetic **𠂤** (duī, "mound," no vault page) — corrected the field to `𠂤`, noting explicitly in the bullet that it's not to be confused with [[堆]]. `mc_id: 752` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `追.md` has no `pos` field to inherit; decided from the leading gloss ("follow, hunt," transitive).

**Body defects found**: no heading at all above the floating CC-initial/final links (no `# Notes` or `## Notes`); all four canonical bullets written from scratch; 2 of 6 ground-truth words missing (including the stand-in 追 itself); one pre-existing entry (追随) was a bare wikilink with no ruby.

**Words cross-check** (6 total ground-truth hits): 追逐, 追及, 追遡 already present and correctly ruby'd; 追随 reformatted to ruby+gloss; 追 (stand-in), 追求 missing — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 追`): [[槌 (char)|槌]] ("hammer") — section added. (A second hit on the string "堆" — [[帥]] — belongs to 堆's own derived family, not 追's, since 追's real phonetic is 𠂤 not 堆; excluded as out of scope.)

**Verification**: Python cross-check of all 7 `<rt>` values (6 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 348 — [[characters/軍|軍]]

Next never-perfected character by `danayo_id` (2246). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` kept as-is: genuine scholarly disagreement — Wiktionary's English page headlines a 形声 reading (semantic 車 + phonetic 勹, an original form of 螾) while explicitly citing the Shuowen's 会意 (車+勹, "to surround") as an alternate; the Japanese Wiktionary page hedges further, calling it "会意（または形声の可能性あり）" and even floating a third theory that 車 itself is a corrupted phonetic form of 熊. Since the stored value already matches one of these legitimate readings, kept it per the loop's standing rule and documented the dispute in the bullet rather than picking a side. `mc_id: 91` cross-checked against `lookup/CC/CC 0000.md` — exact match (the ranking's own entry links back to this character page). `pos: 名詞` was already correctly filled.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus four loose Words-style entries (two ruby'd, two bare); all four canonical bullets written from scratch; 4 of 8 ground-truth words missing (including the stand-in 軍隊 itself); no `## Chengyu` despite a real hit; no `## Derived Characters` despite four real hits.

**Words cross-check** (8 total ground-truth hits): 軍事, 従軍 already ruby'd, kept; 軍隊 (stand-in), 軍艦 reformatted to ruby+gloss (caught and corrected a transcription slip of my own on 軍艦's `<rt>` before the final verification pass); 4 missing — 孤軍, 将軍, 空軍, 軍人 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 孤軍奮闘 ("put up a brave struggle, fight alone") — added.

**Derived Characters** (4 hits via `graphemic_classification: 軍`): [[暈]] ("dizzy, blurry"), [[運]] ("move, transport"), [[輝]] ("brilliant, radiant"), [[揮]] ("command, conduct") — section added.

**Verification**: Python cross-check of all 13 `<rt>` values (8 Words + 1 Chengyu + 4 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 347 — [[characters/身|身]]

Next never-perfected character by `danayo_id` (2245; 2244 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 申` was wrong** — no source supports any phonetic relationship between 身 and 申 at all. Wiktionary's primary listing is unambiguous 象形: a pregnant woman, comparable to the reversed form 㐆 — and explicitly states 身 is "unrelated to 射" (worth noting since the two are easy to visually conflate, same disambiguation pattern as [[characters/良|良]]'s "unrelated to 艮" a few iterations back). Corrected the field to `象形`. `mc_id: 171` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `身体.md` has a blank `pos` field too, so decided independently, corroborated by four of the ground-truth words (`刺身`/`単身`/`終身`/`自身`, all `名詞`).

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; **9 of 11** ground-truth words missing (including the stand-in 身体 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (11 total ground-truth hits): 挺身, 道成肉身 already present and correctly ruby'd; 9 missing — 身体 (stand-in), 自身, 出身, 化身, 単身, 終身, 殺身, 翻身, 刺身 — all added from stored fields.

**Chengyu**: 1 ground-truth hit — 粉骨砕身 ("to have one's body smashed to pieces; to die the most cruel death") — added.

**Derived Characters**: none (`graphemic_classification: 身` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 12 `<rt>` values (11 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 346 — [[characters/貴|貴]]

Next never-perfected character by `danayo_id` (2243; 2242 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 臾` already correct — verified via Wiktionary: 形声 (OC \*kluds), semantic [[Radical 154|貝]] ("money cowrie") + phonetic 臾 (no vault page) — "precious, expensive." `mc_id: 236` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `貴重.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 2 of 3 ground-truth words missing, including the stand-in 貴重 itself.

**Words cross-check** (3 total ground-truth hits): 騰貴 already present and correctly ruby'd; 貴重 (stand-in), 貴族 missing — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 貴`/`贵` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 345 — [[characters/貨|貨]]

Next never-perfected character by `danayo_id` (2241). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 化` already correct — verified via Wiktionary: 形声 (OC \*hŋʷaːls), semantic [[Radical 154|貝]] ("shell, money" — shells were historically used as currency) + phonetic [[化 (char)|化]] (OC \*hŋʷraːls) — valuable goods. `mc_id: 1043` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `貨物.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist at all despite four real ground-truth hits, including the stand-in 貨物 itself.

**Words cross-check** (4 total ground-truth hits): all four missing — 貨物 (stand-in), 貨幣, 通貨, 外貨 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 貨`/`货` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 344 — [[characters/豊|豊]]

Next never-perfected character by `danayo_id` (2240), immediately following [[characters/豆 (char)|豆]] — the two share the same radical. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` kept as-is: this character (representing 豐 "abundant," not to be confused with the unrelated 豊-as-禮 "ceremony" despite the shared modern shinjitai glyph) has genuine classification ambiguity between the Shuowen's 象形 reading and a modern 指事 reading — both describe the same image (a vessel full of plants atop another vessel, [[Radical 151|豆]]), so per the loop's standing rule of keeping an existing value when it matches a legitimate scholarly reading, left it at `象形` and documented the 指事 alternative in the bullet. `mc_id: 848` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 豐).

**Body defects found**: `# Notes` used H1 instead of H2; the graphemic bullet was a bare "Components:"-style fragment (`[[曲]] + [[Radical 151|豆]] = [[SKIP-2-6-7]] ([[Stroke 13]])`) that also wrongly folded the SKIP/Stroke bullet into itself using broken non-existent wikilinks instead of proper lookup-page links — split apart and rewritten from scratch; MC-rank and Levels bullets were both missing, with the two CC-initial/final links floating unattached; `## Words` heading didn't exist at all (both ground-truth words were loose, one bare); `## Derived Characters` didn't exist despite **seven** real hits — the largest phonetic family found this entire loop, surpassing [[characters/良|良]]'s six.

**Words cross-check** (2 total ground-truth hits): 豊尭 already ruby'd, kept; 豊富 (stand-in) promoted from a bare wikilink into `## Words` with ruby added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters cross-check** (7 total ground-truth hits via `graphemic_classification: 豊`/`丰`): [[蜂 (char)|蜂]] ("bee, wasp, hornet"), [[鋒]] ("point of a spear"), [[峰]] ("summit, peak, hump"), [[礼 (char)|礼]] ("manners"), [[邦]] ("federation, commonwealth"), [[奉]] ("serve, wait upon"), [[醴]] ("sweet water") — all added; note that 礼/醴 etymologically descend from the *unrelated* ceremony-sense 豊/禮, not from this character's own "abundant" etymology, but both share the identical `graphemic_classification: 豊` string, so both are included per the mechanical check this loop has applied consistently.

**Verification**: Python cross-check of all 9 `<rt>` values (2 Words + 7 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 343 — [[characters/豆 (char)|豆]]

Next never-perfected character by `danayo_id` (2239; 2238 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — a pictograph of some kind of container, borrowed phonetically for the plant name (displacing Old Chinese 菽); explicitly unrelated to the bottom part of [[豊]]. `mc_id: 1371` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `豆.md` has no `pos` field to inherit; decided from the leading gloss ("bean," a noun).

**Body defects found**: the graphemic bullet was **duplicated verbatim** (once as a proper `[List of 象形]` link, once as "Pictogram (...)" with the same content restated); the SKIP/Stroke bullet had the syllable link wrongly folded in (that belongs on bullet 3, not bullet 2); the Levels bullet was in the wrong order (Jōyō/HSK/Korean/Grade instead of Grade/HSK/Jōyō/Korean); the MC-rank bullet was missing entirely, with the two CC-initial/final links floating unattached at the very bottom; `### Derived characters` used H3 with lowercase "characters" instead of the canonical `## Derived Characters`; `## Words` heading didn't exist at all despite two real ground-truth hits, including the stand-in 豆 itself; the one listed Derived Character (頭) used a broken relative-path Markdown link instead of a wikilink, and 4 of 5 real Derived Characters were missing outright.

**Words cross-check** (2 total ground-truth hits): both missing — 豆 (stand-in), 豆腐 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters cross-check** (5 total ground-truth hits via `graphemic_classification: 豆`): [[頭 (char)|頭]] ("head") already listed, link fixed and gloss added; 4 missing — [[痘]] ("pox, smallpox"), [[豎]] ("vertical line"), [[逗]] ("pause"), [[短 (char)|短]] ("short") — added.

**Verification**: Python cross-check of all 7 `<rt>` values (2 Words + 5 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 342 — [[characters/議|議]]

Next never-perfected character by `danayo_id` (2237; 2236 already stamped, skipped) — this character was already cited as a Derived Character of [[characters/義|義]] back in iteration 312, but hadn't been perfected itself yet. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 義` already correct — verified via Wiktionary: 形声 (OC \*ŋrals), semantic [[Radical 149|言]] ("speech") + phonetic [[義]] (OC \*ŋrals) — literally "speaking about what is right," "to discuss, deliberate." `mc_id: 479` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 事詞` was already correctly filled.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus four loose Words-style entries (two ruby'd, two bare); all four canonical bullets written from scratch; 5 of 9 ground-truth words missing (including the stand-in 議論 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (9 total ground-truth hits): 諌議, 協議 already ruby'd, kept; 議員, 議定 reformatted to ruby+gloss (caught and corrected two transcription slips of my own on their `<rt>` values before the final verification pass); 5 missing — 議論 (stand-in), 会議, 衆議, 衆議院, 思議 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 不可思議 ("inconceivable, unimaginable, incomprehensible," Sanskrit origin) — added.

**Derived Characters**: none (`graphemic_classification: 議`/`议` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 10 `<rt>` values (9 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 341 — [[characters/講|講]]

Next never-perfected character by `danayo_id` (2235). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 冓` already correct — verified via Wiktionary: 形声 (OC \*kroːŋʔ), semantic [[Radical 149|言]] ("say") + phonetic 冓 (OC \*koː, \*koːs, no vault page) — part of the same phonetic series as 溝/篝/構/購. `mc_id: 1525` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `講演.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist at all despite the one real ground-truth hit (the stand-in itself).

**Words cross-check** (1 total ground-truth hit): 講演 (stand-in) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 講`/`讲` matches no other character) — correctly omitted.

**Verification**: the one `<rt>` value cross-checked against its source file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 340 — [[characters/調|調]]

Next never-perfected character by `danayo_id` (2234). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 周` already correct — verified via Wiktionary: 形声 (OC \*dɯːw, \*dɯːws, \*tɯw), semantic [[Radical 149|言]] ("speech") + phonetic [[周]] (OC \*tjɯw). `mc_id: 994` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word `調整.md`'s own field.

**Small pre-existing defect found and fixed**: the graphemic bullet used two broken relative-path Markdown links — `[言](Radical%20149)` and `[周](characters/周.md)` — instead of proper `[[Radical 149|言]]` and `[[周]]` wikilinks, the same defect class fixed on [[characters/葉 (char)|葉]] a few iterations back; also added a missing gloss for 言 ("speech").

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links stranded on their own line; 2 of 4 ground-truth words missing, including the stand-in 調整 itself.

**Words cross-check** (4 total ground-truth hits): 声調, 調解 already present and correctly ruby'd; 調整 (stand-in), 調査 missing — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 調`/`调` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 339 — [[characters/課 (char)|課]]

Next never-perfected character by `danayo_id` (2233). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 果` already correct — verified via Wiktionary: 形声 (OC \*kʰloːl, \*kʰloːls), semantic [[Radical 149|言]] ("to say") + phonetic [[果]] (OC \*kloːlʔ) — to assess; to examine — matching the page's own pre-existing bullet exactly. `mc_id: 2401` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `課.md` has no `pos` field to inherit; decided from the leading gloss ("lesson, chapter," a noun).

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links stranded at the bottom rather than embedded in an MC bullet; `## Words` heading didn't exist at all despite the one real ground-truth hit (the stand-in itself). The pre-existing "pronunciation altered to get a free syllable" aside was kept as a fifth supplementary bullet, same treatment as similar asides elsewhere this loop.

**Words cross-check** (1 total ground-truth hit): 課 (stand-in) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 課`/`课` matches no other character) — correctly omitted.

**Verification**: the one `<rt>` value cross-checked against its source file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 338 — [[characters/説|説]]

Next never-perfected character by `danayo_id` (2232). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 兌` already correct — verified via Wiktionary: 形声 (OC \*hljods, \*hljod, \*lod), semantic [[Radical 149|言]] ("speech") + phonetic 兌 (OC \*l'oːds, no vault page) — from a root meaning "to loosen, to relax"; "to speak, explain." `mc_id: 243` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 說).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `学説.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus one loose bare-wikilink entry (説明); all four canonical bullets written from scratch; 2 of 3 ground-truth words missing, including the stand-in 学説 itself.

**Words cross-check** (3 total ground-truth hits, searched under both alias forms 說/说): 説明 promoted into `## Words` with ruby added (caught and corrected a transcription slip of my own on its `<rt>` — ⼶ vs ㄧ — before it made it into the final verification pass); 学説 (stand-in), 伝説 missing outright — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 説`/`說`/`说` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 337 — [[characters/誤|誤]]

Next never-perfected character by `danayo_id` (2231; 2230 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 呉` already correct — verified via Wiktionary: 形声 (OC \*ŋʷaːs), semantic [[Radical 149|言]] ("speech") + phonetic [[呉]] (OC \*ŋʷaː) — to speak an error; the page's own pre-existing bullet already stated this correctly, just with a broken empty link. `mc_id: 1708` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `錯誤.md`'s own field.

**Small pre-existing defect found and fixed**: the graphemic bullet's phonetic component link was a bare empty `[[]]` instead of `[[呉]]` — filled in.

**Body defects found**: sections badly out of order — `## Chengyu` sat before the CC-initial/final links, which themselves sat before a `## Words`-less pair of loose entries at the very bottom; SKIP/Stroke and Levels bullets were both missing; `## Words` heading didn't exist at all despite three real ground-truth hits, including the stand-in 錯誤 itself.

**Words cross-check** (3 total ground-truth hits): 誤謬 already ruby'd, kept; 誤差 promoted from a loose dash-gloss entry into `## Words` with ruby added; 錯誤 (stand-in) missing outright — added from stored fields.

**Chengyu**: 1 ground-truth hit (時代錯誤) — already present and correctly ruby'd, moved into its proper position after `## Words`.

**Derived Characters**: none (`graphemic_classification: 誤`/`误` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 336 — [[characters/試|試]]

Next never-perfected character by `danayo_id` (2229). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 式` already correct — verified via Wiktionary: 形声 (OC \*hljɯɡs), semantic [[Radical 149|言]] ("speech") + phonetic [[式]] ("form, method") — an exoactive/causative derivation of 式 ("to use, make use of"). `mc_id: 1238` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `考試.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only a single malformed relative-path Markdown link (`[試驗](../words/試験.md)` — 試驗 is a real alias of `試験.md`, so the target was correct, but the entry had no ruby or gloss) plus the two floating CC-initial/final links; all four canonical bullets written from scratch; 2 of 3 ground-truth words missing (including the stand-in 考試 itself).

**Words cross-check** (3 total ground-truth hits): 試験 reformatted from the bare relative-path link to ruby+gloss; 考試 (stand-in), 嘗試 missing — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 試`/`试` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 335 — [[characters/設|設]]

Next never-perfected character by `danayo_id` (2228). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 會意` was wrong** — cross-checked both English and Japanese Wiktionary: 設 is 形声 (OC \*hljed), semantic [[Radical 149|言]] ("speech") + phonetic 埶 (OC \*ŋeds, no vault page). Notably, the Japanese Wiktionary page states outright that the Shuowen's own alternative reading (言 + 殳) is a **mistaken analysis** ("誤った分析") rejected by modern scholarship — an unusually direct source confirmation, not just a "primary vs. secondary listing" judgment call like most of this loop's other corrections. Corrected the field to `埶`. `mc_id: 672` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word `建設.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus three loose Words-style entries (one, 建設, already ruby'd; two bare dash-glosses); all four canonical bullets written from scratch; 1 of 4 ground-truth words missing.

**Words cross-check** (4 total ground-truth hits): 建設 (stand-in) already ruby'd, kept; 設置, 設備 reformatted to ruby+gloss; 設計 missing outright — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 設`/`设` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 334 — [[characters/訪|訪]]

Next never-perfected character by `danayo_id` (2227). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 方` already correct — verified via Wiktionary: 形声 (OC \*pʰaŋs), semantic [[Radical 149|言]] ("speech") + phonetic [[方]] (OC \*paŋ, \*baŋ) — to visit; to inquire. `mc_id: 2300` cross-checked against `lookup/CC/CC 2000.md` — exact match. `pos: 事詞` was already correctly filled — unusual, no gap there this time (differs from, and is more specific than, the stand-in word `訪問.md`'s own `実詞`, but valid as an independent, deliberate choice, not blank).

**Body defects found**: Notes held only the two floating CC-initial/final links plus a leftover raw "Components: [[言 (char)]], [[方]]" fragment instead of a proper graphemic bullet — rewritten from scratch, with the radical component now correctly linked to [[Radical 149|言]]; SKIP/Stroke, MC, and Levels bullets were all missing; `## Words` heading didn't exist at all despite the one real ground-truth hit (the stand-in itself).

**Words cross-check** (1 total ground-truth hit): 訪問 (stand-in) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 訪`/`访` matches no other character) — correctly omitted.

**Verification**: Python cross-check of the one `<rt>` value against its source file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 333 — [[characters/計|計]]

Next never-perfected character by `danayo_id` (2226; 2225 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary/Shuowen: 会意 of [[Radical 149|言]] ("say; speech") and [[十 (char)|十]] ("ten; all") — verbal expression combined with completeness/totality; "to count, calculate, plan." `mc_id: 447` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `計画.md`'s own field.

**Body defects found**: Notes held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 3 of 5 ground-truth words missing, including the stand-in 計画 itself.

**Words cross-check** (5 total ground-truth hits): 計数, 累計 already present and correctly ruby'd; 3 missing — 計画 (stand-in), 統計, 設計 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 計`/`计` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 332 — [[characters/観|観]]

Next never-perfected character by `danayo_id` (2224). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 鸛` was wrong** — 鸛 ("stork") is itself a *derived* character built from the real phonetic component, not the phonetic component itself. Wiktionary confirms 觀 is 形声 (OC \*koːns), semantic [[Radical 147|見]] ("see") + phonetic **雚** (no vault page) — corrected the field to `雚`, noting explicitly in the bullet that it's not to be confused with the full bird-character [[鸛]]. `mc_id: 342` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 觀).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `観察.md`'s own `pos: 動詞` isn't a real category in this vault's taxonomy (`AIOS/grammar/文法 - 97品詞.md` has no such class; the closest real category is `事詞`, eventive), so decided independently rather than copying the non-canonical value, same judgment call as [[characters/義|義]]'s `興起` two iterations ago.

**Body defects found**: page structure inverted — `## Words` sat before `# Notes` (which was also H1), same class as this loop's other inversion cases; Notes held only the two floating CC-initial/final links plus two loose Words-style entries (観測, 観音, dash-glosses); all four canonical bullets written from scratch; 2 of 8 ground-truth words missing.

**Words cross-check** (8 total ground-truth hits): 参観, 観察 (stand-in), 観覧, 宇宙観 already present and correctly ruby'd, kept; 観測, 観音 moved out of Notes into `## Words` with ruby added; 世界観, 直観 missing outright — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 観`/`觀`/`观`/`雚` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 331 — [[characters/親|親]]

Next never-perfected character by `danayo_id` (2223). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 辛` already correct — verified via Wiktionary: 形声 (OC \*sʰin), phonetic [[辛]] (OC \*siŋ) + semantic [[Radical 147|見]] ("see") — the left component originally depicted a chisel with a hazelnut branch used as a whip, later stylized as 亲, a variant of 辛 (explaining why the simplified form 亲 shares this character's own alias field). `mc_id: 214` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `親戚.md`'s own field.

**Body defects found**: page structure inverted — `## Words` sat before `# Notes` (which was also H1), same inversion pattern as 望/然/移/約/興's earlier cases this loop; Notes held only two loose Words-style entries (親切, 親戚) with dash-glosses, no canonical bullets at all; all four written from scratch; 4 of 8 ground-truth words missing (including the stand-in 親戚 itself); no `## Chengyu` despite a real hit; no `## Derived Characters` despite a real hit.

**Words cross-check** (8 total ground-truth hits): 親睦, 親子井 already ruby'd, kept; 親切, 親戚 (the stand-in) moved out of Notes into `## Words` with ruby added; 4 missing outright — 両親, 母親, 父親, 親族 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 孝親天賜 ("honor your parents, that heaven may gift you," Biblical) — added.

**Derived Characters** (1 hit — via the alias `亲` rather than the bare `graphemic_classification: 親` string, confirming the alias-matching check paid off again): [[新 (char)|新]] ("new") — section added.

**Verification**: Python cross-check of all 10 `<rt>` values (8 Words + 1 Chengyu + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 330 — [[characters/要|要]]

Next never-perfected character by `danayo_id` (2222). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 女` was wrong** — that value asserts 形声 with phonetic 女, but Wiktionary's primary listing is 象形: a person (originally 大, later drawn as [[女 (char)|女]]) with two hands pointing to the waist — the upper portion (originally a large eye 目, stylized as a horn 角) became the modern simplified 覀. Originally meant "waist" (now written [[腰]]); extended to "essential, important; to need." No genuine phonetic relationship was ever claimed by any source consulted — corrected the field to `象形`. `mc_id: 773` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 性詞` was already correctly filled, matching the stand-in word `重要.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus two loose Words-style entries (要素, 要求, both bare dash-glosses); all four canonical bullets written from scratch; 8 of 14 ground-truth words missing (including the stand-in 重要 itself — by far the largest single-page word gap since [[characters/自|自]]'s 24); one pre-existing entry (要請) was a bare wikilink with no ruby; no `## Derived Characters` despite a real hit, directly connected to the character's own etymology (腰 is literally what 要 originally meant).

**Words cross-check** (14 total ground-truth hits): 主要, 不要, 要塞, 要地, 要旨, 要約 already ruby'd, kept; 要素, 要求 moved out of Notes into `## Words` with ruby added; 要請 reformatted from a bare wikilink to ruby+gloss; 5 missing outright — 重要 (stand-in), 必要, 需要, 概要, 綱要 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 要`): [[腰]] ("waist") — the character's own etymological descendant, given 要 originally *meant* "waist" before 腰 took over that sense — section added.

**Verification**: Python cross-check of all 15 `<rt>` values (14 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 329 — [[characters/衣|衣]]

Next never-perfected character by `danayo_id` (2221). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: an outline of the chest and upper garment, comparable to the upper portion of [[文]].

**Word-creation gap found**: the `stand_in: 衣類` field pointed at a word file that **did not exist at all** — not an aliasing mixup, a genuinely missing file. Created `words/衣類.md` per `skill_word_creation.md`: characters 衣+類, Japanese いるい ("clothing" as a category/industry term — a laundry-label/department-store word, not a term for any single garment) with the same collective sense preserved in the Korean cognate 의류; Mandarin/Cantonese readings compositional (yīlèi/ji1leoi6) rather than independently attested. `kwin: false` (諺文 의뤼 ≠ korean 의류). Backlinked on `characters/類.md` (itself still unperfected, `danayo_id: 2270`, not yet its turn in this loop — added only the one line, didn't restructure its page).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the new stand-in word's own field.

**Body defects found**: Notes held only the two floating CC-initial/final links and one loose bare-wikilink Words-style entry (衣襟); all four canonical bullets written from scratch; 3 of 7 ground-truth words missing (including the stand-in 衣類, just created); no `## Chengyu` heading (2 of 3 ground-truth chengyu were sitting directly in Notes instead); no `## Derived Characters` despite two real hits.

**Words cross-check** (7 total ground-truth hits, including the newly created 衣類): 浴衣, 浣衣, 皮衣 already ruby'd, kept; 衣襟 promoted from a loose Notes entry into `## Words`; 衣類 (stand-in), 衣服, 胞衣 added from stored fields.

**Chengyu cross-check** (3 total ground-truth hits): 天衣無縫, 一衣帯水 moved into a proper `## Chengyu` heading (already correctly ruby'd); 羊衣餓狼 (Biblical, "a wolf in sheep's clothing") missing — added.

**Derived Characters** (2 hits via `graphemic_classification: 衣`): [[哀]] ("sad, mournful"), [[依 (char)|依]] ("rely on, accord with") — section added.

**Verification**: Python cross-check of all 12 `<rt>` values (7 Words + 3 Chengyu + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 328 — [[characters/街|街]]

Next never-perfected character by `danayo_id` (2220). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 圭` already correct — verified via Wiktionary: 形声 (OC \*kreː), semantic [[Radical 144|行]] ("road, movement") + phonetic [[圭]] (OC \*kʷeː) — a pair of ritual jade axes, explicitly unrelated to 土 ("earth") despite the visual resemblance. `mc_id: 2483` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `街道.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` heading didn't exist at all despite two real ground-truth hits, including the stand-in 街道 itself.

**Words cross-check** (2 total ground-truth hits): both missing — 街道 (stand-in), 街区 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 街` matches no other character) — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 327 — [[characters/血 (char)|血]]

Next never-perfected character by `danayo_id` (2219). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of 一 ("drop of blood") and [[皿 (char)|皿]] ("sacrificial vessel, container") — a drop of blood inside a chalice, used to sacrifice to ancestors (per the oracle-bone Shuowen context). `mc_id: 637` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `血.md` has no `pos` field to inherit; decided from the leading gloss ("blood," a concrete noun).

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 4 of 5 ground-truth words missing (including the stand-in 血 itself); no `## Chengyu` despite a real hit — the same 血誓盟約 already documented on [[characters/両 (char)|両]]'s page earlier this loop, here missing from its other constituent character's own page.

**Words cross-check** (5 total ground-truth hits): 血液 already present and correctly ruby'd; 4 missing — 血 (stand-in), 出血, 吸血鬼, 輸血 — added from stored fields.

**Chengyu**: 1 ground-truth hit (血誓盟約) — added.

**Derived Characters**: none (`graphemic_classification: 血` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 6 `<rt>` values (5 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 326 — [[characters/葉 (char)|葉]]

Next never-perfected character by `danayo_id` (2218). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 枼` already correct — verified via Wiktionary, matching the page's own pre-existing bullet almost exactly: 形声 (OC \*hljeb, \*leb), semantic 艹 + phonetic [[枼]] ("leaf") — 枼 is the original pictogram for this word, 艹 was added to differentiate. `mc_id: 1145` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `葉.md` has no `pos` field to inherit; decided from the leading gloss ("leaf," a concrete noun).

**Small pre-existing defects found and fixed**: the disambiguation callout used non-standard phrasing ("This page is about the character.") missing the character name — normalized to the standard "This is a page about the character 葉." template; the graphemic bullet's semantic component was a broken relative-path Markdown link `[艸](Radical%20140)` instead of a proper `[[Radical 140|艹]]` wikilink, and the phonetic component `[枼](characters/枼.md)` used the same broken pattern instead of `[[枼]]` — both corrected.

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links stranded on their own line rather than embedded in an MC bullet; 2 of 3 ground-truth words missing, including the stand-in 葉 itself.

**Words cross-check** (3 total ground-truth hits): 枝葉 already present and correctly ruby'd; 葉 (stand-in), 闊葉 missing — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 葉`/`叶` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 325 — [[characters/落|落]]

Next never-perfected character by `danayo_id` (2217). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 洛` already correct — verified via Wiktionary: 形声 (OC \*ɡ·raːɡ), semantic [[Radical 140|艹]] ("grass") + phonetic [[洛]] (OC \*ɡ·raːɡ, identical reconstruction) — leaves falling, "to fall." `mc_id: 1333` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word `落下.md`'s own field.

**Small pre-existing defect found and fixed**: the MC-final CC link was written `[[../lookup/CC/finals/韻 鈬開]]` — a relative-path prefix baked directly into wiki-link syntax, which doesn't resolve since Obsidian wiki-links match by name, not path (the checklist's own named defect class); dropped the `../` prefix.

**Body defects found**: `# Notes` used H1 instead of H2; held all four Words entries directly (no `## Words` heading existed at all) alongside the two CC-initial/final links, with no canonical Notes bullets — all four written from scratch; 3 of 7 ground-truth words missing.

**Words cross-check** (7 total ground-truth hits): 落下 (stand-in), 堕落, 聚落, 院落 already present and correctly ruby'd, moved into a proper `## Words` heading; 3 missing — 墜落, 落下傘, 落花 — added from stored fields.

**Chengyu**: 2 ground-truth hits (沈魚落雁, 落花流水) — both already present and correctly ruby'd, no changes needed.

**Derived Characters**: none (`graphemic_classification: 落` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values (7 Words + 2 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 324 — [[characters/菜|菜]]

Next never-perfected character by `danayo_id` (2216; 2215 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 采` already correct — verified via Wiktionary: 形声 (OC \*sʰɯːs), semantic [[Radical 140|艹]] ("grass") + phonetic [[采]] (OC \*sʰɯːʔ, "to gather; to pluck") — literally "what is gathered/plucked," with a nominalizing \*-s suffix. `mc_id: 2097` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `野菜.md`'s own field (and all five other ground-truth words, all also `名詞`).

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 5 of 6 ground-truth words missing, including the stand-in 野菜 itself.

**Words cross-check** (6 total ground-truth hits): 菜蔬 already present and correctly ruby'd; 5 missing — 野菜 (stand-in), 白菜, 甜菜, 沈菜, 菜汁 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 菜` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 6 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 323 — [[characters/英|英]]

Next never-perfected character by `danayo_id` (2214). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 央` already correct — verified via Wiktionary: 形声 (OC \*qraŋ), semantic [[Radical 140|艹]] ("grass") + phonetic [[央]] (OC \*qaŋ). `mc_id: 1387` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `英雄.md` has a blank `pos` field too, so decided independently from the leading gloss ("hero," a noun); corroborated by `石英.md`/`蒲公英.md`, both `名詞`.

**Small pre-existing defect found and fixed**: the graphemic bullet's semantic component was linked as bare `[[艹]]`, which doesn't resolve to anything (no character page exists for the bare grass-radical glyph) — corrected to `[[Radical 140|艹]]`, the same radical page used on [[characters/芸|芸]] last iteration.

**Body defects found**: SKIP/Stroke, MC, and Levels bullets were all missing, with the two CC-initial/final links stranded mid-page between two Words entries rather than embedded in an MC bullet; 6 of 11 ground-truth words missing (including the stand-in 英雄 itself); 2 pre-existing entries (英吉利, 英俊) were bare wikilinks with dash-glosses instead of ruby+quoted-gloss; no `## Derived Characters` despite a real hit.

**Words cross-check** (11 total ground-truth hits): 英国, 英才, 英格蘭 already ruby'd, kept; 英吉利, 英俊 reformatted to ruby+gloss; 6 missing — 英雄 (stand-in), 英語, 英語圏, 英語学, 石英, 蒲公英 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 英`): [[瑛]] ("luster") — section added.

**Verification**: Python cross-check of all 12 `<rt>` values (11 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 322 — [[characters/芸|芸]]

Next never-perfected character by `danayo_id` (2213; 2212 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 云` already correct — this one has a genuine dual identity worth documenting explicitly: 芸's own etymology is 形声 (OC \*ɢun), semantic [[Radical 140|艸]] ("plant") + phonetic 云 (no vault page) — originally "rue," a fragrant herb; separately, in Japanese, 芸 serves as the shinjitai simplification of 藝 ("art, skill, craft"), an unrelated character merged in by simplification rather than a semantic extension. This page's own english gloss and `stand_in: 芸術` reflect the merged "art" sense, not the plant — same character-merger pattern as the loop's earlier shinjitai/simplification cases (収's 又, 舎's 口→舌). `mc_id: 3343` cross-checked against `lookup/CC/CC 3000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching two of the ground-truth words (`武芸.md`, `芸人.md`, both `名詞`) — the stand-in word `芸術.md` itself has a blank `pos` field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus three loose Words-style entries (one, the stand-in 芸術, entirely unruby'd); all four canonical bullets written from scratch; 4 of 7 ground-truth words missing.

**Words cross-check** (7 total ground-truth hits, searched under all three alias forms 蕓/藝/艺): 文芸, 芸妓 already ruby'd, kept; 芸術 (stand-in) moved into `## Words` with ruby added; 六芸, 園芸, 武芸, 芸人 missing — all four added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 芸`/`蕓`/`藝`/`艺` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 321 — [[characters/良|良]]

Next never-perfected character by `danayo_id` (2211; 2212 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: possibly depicts corridors and a room, the original form of 廊 ("corridor," no vault page); Wiktionary explicitly notes 良 is **unrelated** to [[Radical 138|艮]] despite sharing its Kangxi classification — worth stating outright since the two characters are easy to visually conflate. `mc_id: 428` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `良好.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus one loose bare-wikilink Words-style entry (良好, the stand-in itself, sitting unformatted in Notes instead of `## Words`); all four canonical bullets written from scratch; 3 of 4 ground-truth words missing; no `## Derived Characters` despite six real hits — the largest phonetic family surfaced this loop after [[characters/京 (char)|京]]'s six.

**Words cross-check** (4 total ground-truth hits): 奈良 already present and correctly ruby'd; 良好 (stand-in) promoted from a loose Notes entry into `## Words` with ruby added; 善良, 良月 missing — both added from stored fields (caught and corrected a transcription slip of my own on 善良's `<rt>` — ㄝ vs ㄶ — before it made it into the final verification pass).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 良`): [[娘 (char)|娘]] ("young woman"), [[浪]] ("wave"), [[朗]] ("clear, distinct"), [[瑯]] ("white cornelian"), [[郎]] ("youthful man"), [[狼 (char)|狼]] ("wolf") — section added.

**Verification**: Python cross-check of all 10 `<rt>` values (4 Words + 6 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 320 — [[characters/舎|舎]]

Next never-perfected character by `danayo_id` (2210). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 余` already correct — verified via Wiktionary: 形声 (OC \*hljaːs, \*hljaːʔ), phonetic [[余]] (OC \*la, the original pictogram for this word) + semantic 口 ("mouth," added later to distinguish) — a resting place; lodging house. Noted that the semantic 口 has since visually merged into what the modern glyph's own `radical:` field records as [[Radical 135|舌]] ("tongue"), same corruption pattern as 老/耂 and 収's 又. `mc_id: 450` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 舍).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `宿舎.md`'s own field.

**Body defects found**: no canonical bullets at all — Notes held three Words-style entries instead (one properly ruby'd, one a bare "see [[宿舎]]" cross-reference instead of a real entry, one using an unruby'd relative link with a dash-gloss); all four bullets written from scratch; `## Words` heading didn't exist at all; 2 of 5 ground-truth words missing (including the stand-in 宿舎 itself, previously only a "see" pointer); no `## Derived Characters` despite a real hit.

**Words cross-check** (5 total ground-truth hits): 廬舎 already ruby'd, kept; 校舎 reformatted to a proper ruby+gloss `## Words` entry; 宿舎 (stand-in) promoted from a bare "see" reference to a full entry; 寄宿舎, 精舎 missing outright — both added from stored fields.

**Chengyu**: 1 ground-truth hit (舎本逐末) — already present and correctly ruby'd, no changes needed.

**Derived Characters** (1 hit via `graphemic_classification: 舎`): [[捨 (char)|捨]] ("throw away, discard") — section added.

**Verification**: Python cross-check of all 7 `<rt>` values (5 Words + 1 Chengyu + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 319 — [[characters/興 (char)|興]]

Next never-perfected character by `danayo_id` (2209). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct, but this one needed extra diligence: an initial English-Wiktionary fetch claimed a 形声 reading (semantic 舁 + phonetic 型, OC \*ɡeːŋ) — a component with no obvious visual or historical connection to 興's actual oracle-bone form and no corroboration anywhere else, so treated as a likely fetch/summarization error rather than trusted at face value. Cross-checked against Japanese Wiktionary and multiple Chinese etymology sources (Shuowen, 甲骨文字典, 百度百科), all of which agree: 会意, originally a pictograph of four hands (舁, no vault page) raising a stretcher/litter ([[凡]]); the Shuowen's small-seal analysis instead reads the lower component as [[同]] ("shared strength"). Kept the field at `會意` per this converging evidence. `mc_id: 315` cross-checked against `lookup/CC/CC 0000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `興.md` has no `pos` field to inherit; decided independently from the leading gloss "entertain" (transitive).

**Body defects found**: page structure inverted — `## Words` sat before `# Notes` (which was also H1), same inversion pattern as 望/然/移/約's earlier cases this loop; Notes held only the two floating CC-initial/final links; all four canonical bullets written from scratch; 3 of 5 ground-truth words missing, including the stand-in 興 itself.

**Words cross-check** (5 total ground-truth hits): 興旺, 興起 already present and correctly ruby'd; 興 (stand-in), 勃興, 高興 missing — all three added from stored fields.

**Chengyu**: no ground-truth hits under 興 or 兴 — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 興`/`兴` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 318 — [[characters/自|自]]

Next never-perfected character by `danayo_id` (2208) — unusual starting point: all four canonical Notes bullets were already present, correct, and in order (`graphemic_classification: 象形` verified — a pictograph of a nose, original form of [[鼻]], later phonetically borrowed via 假借 for "oneself"), so the frontmatter/etymology layer needed no changes at all; `mc_id: 50` cross-checked against `lookup/CC/CC 0000.md` — exact match (the ranking's own entry links back to this character page). Had no `date-last-perfect` field at all (not even a blank one) — added, stamped `2026-07-25`.

**Body defects found — by far the largest Words gap this loop, surpassing [[characters/線|線]]'s 13/16**: `## Words` mixed 4 properly ruby'd entries with a **14-item bare numbered list** (`1. [[自閉]]` … `14. [[自転車]]`, no ruby, no gloss, wrong list syntax for this section entirely) and was missing 5 more ground-truth words outright (including the stand-in 自身, which — unusually — was one of the properly-formatted ones already); `## Chengyu` mixed 2 properly ruby'd entries with 2 bare wikilinks and was missing 3 more ground-truth chengyu outright.

**Words cross-check** (24 total ground-truth hits — the largest word count found on any page this loop): 自身, 自治, 自失, 自尊, 自立 already ruby'd and kept; the 14-item bare numbered list (自閉, 自分, 自給, 自在, 自得, 自制, 自動車, 自閉症, 自由, 自足, 自主, 自禁, 自然, 自転車) reformatted to ruby+gloss; 5 missing outright — 自乗, 自家, 自己, 自我, 自動詞 — added from stored fields. Final list re-ordered with the stand-in first.

**Chengyu cross-check** (7 total ground-truth hits): 自業自得, 自給自足 already ruby'd and kept; 自由自在, 自暴自棄 reformatted from bare wikilinks to ruby+gloss; 3 missing — 茫然自失, 愛隣如自 (Biblical), 東亜自通 (Dan'a'yo-original, `origin: 単亜語`) — added.

**Derived Characters**: none (`graphemic_classification: 自` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 31 `<rt>` values (24 Words + 7 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 317 — [[characters/脚 (char)|脚]]

Next never-perfected character by `danayo_id` (2207). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 却` already correct — verified via Wiktionary: 形声 (OC \*kaɡ), semantic [[Radical 130|肉]] ("meat, body") + phonetic [[却 (char)|却]] (OC \*kʰaɡ) — part of the body, the foot or leg. `mc_id: 3047` cross-checked against `lookup/CC/CC 3000.md` — exact match (traditional form 腳).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `脚.md` has no `pos` field to inherit, so decided independently: "leg" is a concrete body-part noun.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; `## Words` didn't exist at all despite three real ground-truth hits, including the stand-in 脚 itself.

**Words cross-check** (3 total ground-truth hits, searched under alias 腳 too): all three missing — 脚 (stand-in), 脚踝, 馬脚 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 脚`/`腳` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 316 — [[characters/能|能]]

Next never-perfected character by `danayo_id` (2206). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a pictograph of a bear — two paws visible as a pair of 匕, the face with an open mouth stylized as 月 (later corrupted into the [[Radical 130|肉]] radical); originally "bear," extended to "ability, capability." **`mc_id` off-by-one caught live** — stored `43` is actually [[使]]'s rank; 能 is **44** (verified directly in `lookup/CC/CC 0000.md` — "> 44. [能](../../characters/能.md)"), the same one-line-off transcription pattern as the 艮/煌/祝 cases documented in the checklist's Common Mistakes. Frontmatter corrected, bullet written as 44th. `pos: 名詞` was already correctly filled, matching the stand-in word `技能.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 3 of 5 ground-truth words missing, including the stand-in 技能 itself.

**Words cross-check** (5 total ground-truth hits): 可能, 能力 already present and correctly ruby'd; 技能 (stand-in), 才能, 猪悟能 (a Journey to the West proper-name compound) missing — all three added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 能` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 315 — [[characters/聞 (char)|聞]]

Next never-perfected character by `danayo_id` (2205). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 門` already correct — verified via Wiktionary: 形声 (OC \*mɯn), semantic [[Radical 128|耳]] ("ear") + phonetic [[門]] (OC \*mɯːn) — to hear. `mc_id: 99` cross-checked against `lookup/CC/CC 0000.md` — exact match (the ranking's own entry links back to this character page).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `聞.md` itself has no `pos` field to inherit, so decided independently: "to hear" is transitive/eventive.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 2 of 3 ground-truth words missing (including the stand-in 聞 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (3 total ground-truth hits, searched under alias 闻 too): 新聞 already present and correctly ruby'd; 聞 (stand-in), 令聞 missing — both added from stored fields.

**Chengyu**: 1 ground-truth hit — 百聞不如一見 ("hearing something a hundred times is not as good as seeing it once") — added.

**Derived Characters**: none (`graphemic_classification: 聞`/`闻` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values (3 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 314 — [[characters/考|考]]

Next never-perfected character by `danayo_id` (2204), immediately following [[characters/老 (char)|老]] — the two are cognates sharing the same MC final, SKIP code, and 転注 relationship, a nice consecutive pair. Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 象形` was wrong** — Wiktionary's primary listing is 會意: [[Radical 125|耂]] ("old man with long hair, bent over," the abbreviated form of [[老 (char)|老]]) + 丂 ("a walking cane" — already listed as this very character's own alias, so cited as bare text rather than linked) — an elderly person leaning on a cane; cognate to 老 (OC \*ruːʔ), the same 転注 pair documented on 老's own page last iteration. Corrected the field to `會意`. `mc_id: 776` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word `考慮.md`'s own field.

**Body defects found**: Notes held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 4 of 6 ground-truth words missing (including the stand-in 考慮 itself); no `## Derived Characters` despite five real hits.

**Words cross-check** (6 total ground-truth hits, searched under both aliases 丂/攷): 思考, 参考 already present and correctly ruby'd; 4 missing — 考慮 (stand-in), 考察, 考試, 高考 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 hits — 2 via `graphemic_classification: 考` directly, 3 via the alias `丂`, confirming the alias-matching check is worth running here too): [[可 (char)|可]] ("can"), [[巧]] ("skillful, clever"), [[昜]] ("sunbeam"), [[朽]] ("decay"), [[拷]] ("torture") — section added.

**Verification**: Python cross-check of all 11 `<rt>` values (6 Words + 5 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 313 — [[characters/老 (char)|老]]

Next never-perfected character by `danayo_id` (2203). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意 of [[人 (char)|人]] ("man"), [[毛 (char)|毛]] ("hair"), and [[匕]] ("cane") — a man with long hair leaning on a cane, "old"; cognate to [[考]] (OC \*kʰluːʔ), the textbook example of 転注 ("mutual annotation"). Since 老's own `radical:` field is 老 itself, none of the three components get a Radical-page link per the refined per-character rule from the `知` correction earlier this loop — all three are plain character-page links (人/毛 needed pipe form due to same-named word files). `mc_id: 369` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the character's own leading english gloss ("old person") and the convention on [[characters/少 (char)|少]] (also `名詞`).

**Body defects found**: `# Notes` used H1 instead of H2 and was otherwise empty aside from a floating pair of CC-initial/final links stranded at the very bottom, past `## Chengyu`; all four canonical bullets written from scratch. `## Chengyu`'s one entry (白頭偕老) had a **typo'd `<rt>`** — ended in `ㄎㄚㄨ` instead of the chengyu's own stored `ㄌㄚㄨ` — and no English gloss; corrected against the source file and gloss added. 5 of 8 ground-truth words missing (including the stand-in 老 itself); one (老師) was sitting loose past the Chengyu section with a bare wikilink instead of living in `## Words`.

**Words cross-check** (8 total ground-truth hits): 老鼠, 老鼠人 already present and correctly ruby'd; 老師 moved into `## Words` with ruby added; 5 missing — 老 (stand-in), 老爺, 老子, 老人学, 鬼老 — added from stored fields.

**Chengyu**: 1 ground-truth hit (白頭偕老) — already present but with a bad `<rt>` and no gloss; both fixed.

**Derived Characters**: none (`graphemic_classification: 老` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values (8 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 312 — [[characters/義|義]]

Next never-perfected character by `danayo_id` (2202). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 會意` was wrong, and directly contradicted the page's own pre-existing bullet**, which already correctly described a 形声 structure — but with semantic and phonetic **swapped**: it read "semantic [[我]] + phonetic [[羊]]," when Wiktionary confirms the real structure is the reverse — semantic [[Radical 123|羊]] ("good, auspicious," not literally "sheep" here) + phonetic [[我 (char)|我]] (OC \*ŋaːlʔ). Corrected the field to `我` and fixed the bullet's component order; also fixed the empty semantic gloss and the `我`/`羊` link collisions (both have same-named word files, needed pipe-form links). `mc_id: 144` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 名詞` was already correctly filled, matching the stand-in word `意義.md`'s own field.

**Body defects found**: **two duplicate `## Notes` headings** — the first held only the two floating CC-initial/final links, the second held the single (swapped) graphemic bullet; merged into one, with the SKIP/Stroke and Levels bullets both missing entirely and written from scratch. 8 of 10 ground-truth words missing (including the stand-in 意義 itself); 2 of 3 ground-truth chengyu missing; no `## Derived Characters` despite three real hits.

**Words cross-check** (10 total ground-truth hits): 意義, 正義 already present and correctly ruby'd; 8 missing — 定義, 定義域, 主義, 社会主義, 官僚主義, 禁欲主義, 大義, 無義 — added from stored fields.

**Chengyu cross-check** (3 total ground-truth hits): 断章取義 already present; 義以立名, 義重於音 missing — both added (both Dan'a'yo-original chengyu, per their own `origin: 単亜語` field).

**Derived Characters** (3 hits via `graphemic_classification: 義`): [[議]] ("comment, discuss"), [[儀]] ("ceremonial"), [[犠]] ("sacrifice") — section added.

**Verification**: Python cross-check of all 16 `<rt>` values (10 Words + 3 Chengyu + 3 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 311 — [[characters/美 (char)|美]]

Next never-perfected character by `danayo_id` (2201; 2200 already stamped, skipped). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: primary listing is a pictogram of a person ([[大 (char)|大]]) wearing a headdress (now written [[Radical 123|羊]]) of feathers or ram's horn; the modern glyph is also sometimes read as 会意 (羊 "ram/feathers" + 大 "person"), noted as a secondary reading per the loop's standing rule of following Wiktionary's primary listing. `mc_id: 430` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). `pos: 性詞` was already correctly filled, unusually — no gap there.

**Body defects found**: the graphemic bullet was leftover raw "Components: [[𦍌]], [[大]]" text, not a proper 象形/会意 bullet — rewritten from scratch, and the radical component now correctly links to [[Radical 123|羊]] per the character's own `radical:` field; SKIP/Stroke, MC, and Levels bullets were entirely missing, with the two CC-initial/final links unattached; four ground-truth words (美洲, 美徳, 賛美, 賛美歌) were sitting loose in Notes with dash-glosses or bare ruby instead of living in `## Words`; 8 of 14 total ground-truth words missing, including the stand-in 美 itself.

**Words cross-check** (14 total ground-truth hits): 華美, 北美洲, 南美洲, 北美, 南美, 美洲金 already present in `## Words` (kept, already correctly ruby'd); 美洲, 美徳, 賛美, 賛美歌 moved out of Notes into `## Words` (already ruby'd, gloss format normalized); 4 missing outright — 美 (stand-in), 美国, 美国人, 鮮美 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 美` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 14 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 310 — [[characters/線|線]]

Next never-perfected character by `danayo_id` (2199). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 泉` already correct — verified via Wiktionary: 形声 (OC \*sqʰeːns), semantic [[Radical 120|糸]] ("silk, thread") + phonetic [[泉]] ("spring, fountain") — thread-like objects, extended to "line." `mc_id: 5950` — beyond the CC mirror's top-4000, trusted per standing policy, used verbatim. No disambiguation callout needed — no `words/線.md` exists (the stand-in is the compound `直線`, not the bare character).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `直線.md`'s own field (and 14 of the other 15 ground-truth words, all also `名詞`).

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; **13 of 16** ground-truth words missing, by far the largest single-page gap this loop so far — including the stand-in 直線 itself and an entire family of geometry vocabulary (弧線, 号線, 準線, 漸近線, 接線, 双曲線, 放物線, 圓錐曲線) that had never been added at all.

**Words cross-check** (16 total ground-truth hits, searched under both alias forms 线/缐): 曲線, 折線, 界線 already present and correctly ruby'd; 13 missing — 直線 (stand-in), 弧線, 号線, 準線, 漸近線, 接線, 双曲線, 放物線, 圓錐曲線, 地平線, 緯線, 無線, 糸線 — all added from stored fields.

**Chengyu**: no ground-truth hits under 線/线/缐 — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 線`/`线`/`缐` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 16 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 309 — [[characters/続|続]]

Next never-perfected character by `danayo_id` (2198). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 堯` was wrong** — didn't match any sourced etymology for 續/続 at all. Verified via Wiktionary and corroborated by a Chinese-language search of the Shuowen Jiezi's own gloss: 續 is 形声 (OC \*ljoɡs, \*ljoɡ), semantic [[Radical 120|糸]] ("silk, rope") + phonetic **𧶠** — an obscure component with no vault page, cited as bare text (same treatment as 荅's 亼). No plausible confusion path with 堯 identified; corrected the field. `mc_id: 1621` cross-checked against `lookup/CC/CC 1000.md` — exact match (traditional form 續). No disambiguation callout needed — no `words/続.md` exists (the stand-in is the compound `継続`, not the bare character).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word `継続.md`'s own field.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 1 of 4 ground-truth words missing.

**Words cross-check** (4 total ground-truth hits, searched under both alias forms 續/续): 継続 (stand-in, already annotated), 持続, 連続 already present and correctly ruby'd; 接続助詞 missing — added from stored fields.

**Chengyu**: no ground-truth hits under 続/續/续 — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 続`/`續`/`续` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 308 — [[characters/給|給]]

Next never-perfected character by `danayo_id` (2197) — an unusually clean starting point this iteration: all four canonical Notes bullets, `## Words`, and `## Chengyu` already existed in the right order and heading level. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 合` already correct — verified via Wiktionary: 形声 (OC \*krub), semantic [[Radical 120|糸]] ("silk") + phonetic [[合 (char)|合]] (OC \*kuːb, \*ɡuːb) — matches the page's own pre-existing bullet almost exactly. `mc_id: 961` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word `補給.md`'s own field.

**Small pre-existing defects found and fixed**: the graphemic bullet's semantic-component gloss was an empty string — `[[Radical 120|糸]] ("")` — filled in as `"silk"`, the standard gloss used elsewhere in the corpus for this radical; the phonetic link `[[合]]` had the same link-collision bug as `約`'s `勺` two iterations ago — `合` resolves to `words/合.md` rather than the intended `characters/合 (char).md` — corrected to the pipe form. `供給` in `## Words` was a bare wikilink with no ruby or gloss; reformatted. One ground-truth word (自給) was missing outright.

**Words cross-check** (4 total ground-truth hits): 補給, 俸給 already present and correctly ruby'd; 供給 reformatted to ruby+gloss; 自給 missing — added from stored fields.

**Chengyu**: 1 ground-truth hit (自給自足) — already present and correctly ruby'd, no changes needed.

**Derived Characters**: none (`graphemic_classification: 給`/`给` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values (4 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 307 — [[characters/終|終]]

Next never-perfected character by `danayo_id` (2196). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 冬` already correct — verified via Wiktionary: originally a pictograph of the knotted end of a cord (夂), marking completion; later reformed as a phono-semantic compound, semantic [[Radical 120|糸]] ("silk, thread") + phonetic [[冬 (char)|冬]] (OC \*tuːŋ) — kept the pictographic origin as a note alongside the modern 形声 reading, same dual-etymology treatment as [[characters/散|散]]/[[characters/歸|歸]] earlier this loop. `mc_id: 283` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). No disambiguation callout needed — no `words/終.md` exists (the stand-in is the compound `終了`, not the bare character).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word `終了.md`'s own field, and all three other ground-truth words (`終点`/`終身`/`終止格`, all `名詞`) as well.

**Body defects found**: `# Notes` used H1 instead of H2; held only the two floating CC-initial/final links plus three loose Words-style entries with dash-glosses, no canonical bullets at all; all four written from scratch. `## Words` existed with only one entry (終止格, already correctly ruby'd); the stand-in 終了 itself and two other ground-truth words (終点, 終身) were sitting unformatted inside Notes instead of in `## Words`.

**Words cross-check** (4 total ground-truth hits): 終止格 already present and correctly ruby'd; 終了 (stand-in), 終点, 終身 moved out of Notes into `## Words` with ruby+gloss added.

**Chengyu**: no ground-truth hits under 終 or 终 — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 終`/`终` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 306 — [[characters/紅 (char)|紅]]

Next never-perfected character by `danayo_id` (2195). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 工` already correct — verified via Wiktionary: 形声, semantic [[Radical 120|糸]] ("silk") + phonetic [[工]] (OC \*koːŋ) — originally referred to lighter shades of red, gradually replacing 赤 as the primary word for "red." `mc_id: 2561` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` — neither the stand-in word `紅.md` nor its related compounds (`紅茶`/`紅玉`, both `名詞`) offered a directly matching convention, so fell back on the character's own semantic class instead: a bare color term behaves as a stative, matching the established convention on this vault's other basic color characters ([[characters/赤 (char)|赤]], [[characters/青 (char)|青]], both `pos: 性詞`).

**Body defects found**: `## Notes` held only the two floating CC-initial/final links with no canonical bullets at all — all four written from scratch; 3 of 8 ground-truth words missing (including the stand-in 紅 itself); 3 pre-existing Words entries (紅茶, 紅鶴, 紅玉) were bare wikilinks with dash-glosses instead of ruby+quoted-gloss.

**Words cross-check** (8 total ground-truth hits): 猩紅熱, 火紅 already present and already correctly ruby'd; 紅茶, 紅鶴, 紅玉 reformatted to ruby+gloss; 3 missing — 紅 (stand-in), 口紅, 火紅素 (the periodic-table strontium abbreviation) — added from stored fields.

**Chengyu**: no ground-truth hits under 紅 or 红 — section correctly omitted.

**Derived Characters**: none (`graphemic_classification: 紅`/`红` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 305 — [[characters/約|約]]

Next never-perfected character by `danayo_id` (2194). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 勺` already correct — verified via Wiktionary: 形声, semantic [[Radical 120|糸]] ("rope") + phonetic 勺 (OC \*pljewɢ, \*bljewɢ). `mc_id: 723` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). No disambiguation callout needed — no `words/約.md` exists (the stand-in is the compound `約束`, not the bare character).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word `約束.md`'s own field.

**Body defects found**: page structure inverted — `## Words` sat before `## Notes`, same class of inversion as 望/然/移's earlier cases this loop; Notes held a correct graphemic bullet and a genuine "circa on years" usage note, but SKIP/Stroke, MC, and Levels bullets were all missing, and the two CC-initial/final links floated at the bottom rather than embedding in an MC bullet. **Also caught a link-collision bug in the pre-existing graphemic bullet**: the phonetic component was linked as bare `[[勺]]`, which actually resolves to `words/勺.md` (a real word file with the same name) rather than the intended `characters/勺 (char).md` — corrected to the pipe form `[[勺 (char)|勺]]`, same class of fix as the mc_id off-by-ones but for wiki-link collisions instead. 5 of 8 ground-truth words missing (including the stand-in 約束 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (8 total ground-truth hits): 綽約, 制約, 要約 already present (kept as-is, already correctly ruby'd); 5 missing — 約束 (stand-in, annotated), 契約, 条約, 公約, 誓約 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 血誓盟約 ("a covenant in blood," Biblical origin) — added.

**Derived Characters**: none (`graphemic_classification: 約`/`约` matches no other character) — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values (8 Words + 1 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 304 — [[characters/節 (char)|節]]

Next never-perfected character by `danayo_id` (2193). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 即` already correct — verified via Wiktionary: 形声, semantic [[Radical 118|竹]] ("bamboo") + phonetic [[即 (char)|即]] (OC \*ʔsɯɡ) — the node of bamboo, extended to "segment, joint, festival." `mc_id: 295` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` — the stand-in word `節.md` has no `pos` field to inherit, so matched against the character's most central concrete-noun sense (corroborated by `季節.md`'s own `pos: 名詞`, `音節.md`'s, and `指関節.md`'s — all three independently agree).

**Body defects found**: `# Notes` used H1 instead of H2; the section held no canonical bullets at all, just the two floating CC-initial/final links and three loose Words-style entries mixed in directly under Notes (one, 節減, not even ruby'd); all four canonical bullets written from scratch; 9 of 12 ground-truth words missing outright, including the stand-in 節 itself; no `## Derived Characters` despite a real hit.

**Words cross-check** (12 total ground-truth hits, searched under 節's own alias 节 too): 節減 (moved into `## Words`, ruby added), 臘八節, 中秋節 (both already present and already correctly ruby'd) — 9 missing: 節 (stand-in), 季節, 時節, 音節, 春節, 復活節, 聖誕節, 指関節, 双節棍 — all added from stored fields.

**Chengyu**: no ground-truth hits under 節 or 节 — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 節`): [[櫛 (char)|櫛]] ("comb," own syllable ㄐㄜㄊ — a vowel shift from the parent's ㄝㄊ but still the same phonetic family, per the checklist's own note that convergence is expected, not required) — section added.

**Verification**: Python cross-check of all 13 `<rt>` values (12 Words + 1 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 303 — [[characters/答 (char)|答]]

Next never-perfected character by `danayo_id` (2192) — back to the normal ascending front after iteration 302's out-of-order id-98 anomaly ([[characters/両 (char)|両]]); confirmed no other low-id stragglers remain. Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 合` already correct — verified via Wiktionary: 形声, semantic [[Radical 118|竹]] ("bamboo") + phonetic [[合 (char)|合]] (OC \*kuːb) — originally a variant of 荅, the grass radical 艸 mistakenly replaced with bamboo 竹. `mc_id: 1066` cross-checked against `lookup/CC/CC 1000.md` — exact match (plain-list format, not blockquote).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` — the stand-in word `答.md` itself has no `pos` field to inherit, so matched against the closest related compound `回答.md` (`pos: 事詞`) instead.

**Body defects found**: `# Notes` used H1 instead of H2; the section held only a single stray usage note ("don't use 對答") with no canonical bullets at all — all four written from scratch; two floating CC-initial/final links (`聲 端`/`韻 合`) had no MC bullet to embed in; the stray "don't use 對答" note was kept as a genuine usage caveat (對答 has no word file in this vault) and folded in as a fifth supplementary Notes bullet, same treatment as the "exponentiation" aside kept on [[characters/乗 (char)|乗]]'s page a few iterations back, rather than discarded as junk; `## Words` existed with only one entry, missing the stand-in 答 itself and one other real compound; no `## Derived Characters` despite two real hits.

**Words cross-check** (3 total ground-truth hits, searched under 答's own alias 荅 too): 回答 already present (ruby+gloss kept as-is); 答 (stand-in) and 報答 missing — both added from stored fields.

**Chengyu**: no ground-truth hits under 答 or 荅 — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 荅` — both name the alias form, not the bare "答" string, confirming the alias-matching check is worth running here too): [[塔 (char)|塔]] ("pagoda"), [[搭]] ("board (a vehicle)," corroborated by 搭's own `stand_in: 搭乗`) — both share the convergent ㄊㄚㄆ syllable, section added.

**Verification**: Python cross-check of all 5 `<rt>` values (3 Words + 2 Derived Characters) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 302 — [[characters/両 (char)|両]]

Next never-perfected character by `danayo_id` — but a genuine out-of-order anomaly: id **98**, far below the ascending front (2192+) this loop has otherwise been working through since iteration ~140. `両 (char).md` had clearly never been touched by this checklist despite its low id — most likely the file was split from a prior bare `両.md` into `両 (char).md` + a new stand-in `words/両.md` at some point (same renaming signal documented for [[衢]] in `AIOS/projects.md`), which would explain a fundamental character surfacing this late. Followed strict `danayo_id` ordering rather than skipping to 2192, per the loop's own stated rule. Stamped `date-last-perfect: 2026-07-25`.

**`graphemic_classification: 指事` was wrong** — didn't match any sourced etymology. Fetched Wiktionary's Glyph Origin section for 兩 directly: its primary listed analysis is Shuowen's 會意 (一 + 㒳, "two things joined"); Baxter (1992) separately observes the bronze-script form resembles two [[丙 (char)|丙]] (OC \*praŋʔ) joined, making 丙 an incidental phonetic — kept as a secondary note per the loop's standing rule of following Wiktionary's *primary* listing and noting Shuowen/alternate readings as asides (here reversed: Shuowen's reading is the primary one, Baxter's phonetic observation is the aside). Corrected field to `會意`. `mc_id: 349` cross-checked against `lookup/CC/CC 0000.md` — exact match (traditional form 兩).

**Frontmatter**: `pos: ""` (empty string) → filled in as `修飾語`, matching the stand-in word `両.md`'s own field exactly. `vietnamese: cả hai` was wrong — that's an English-derived native Vietnamese phrase ("both"), not a Sino-Vietnamese reading; corrected to `lưỡng`, independently confirmed both via Wiktionary's Sino-Vietnamese listing for 兩 and via the stand-in word `両.md`'s own `vietnamese: lưỡng` field (cross-validating). `japanese_native: てる` looked suspicious at first (not one of 両's two common kun'yomi ふたつ/もろ) but checked out — it's a legitimate third listed reading (name/訓読み) for 両, not fabricated; left as-is. `korean_native: 두` ("two") already correct, no change.

**Body defects found**: `# Notes` used H1 instead of H2; Notes held only two numbered non-canonical bullets (a bare "both" and a 借代字 aside for 罔両) instead of the four canonical bullets; all four bullets (graphemic, SKIP/Stroke, MC rank, Levels) written from scratch; two floating CC-initial/final links (`聲 來`/`韻 陽開`) had no MC bullet to embed in; `## Words` existed but 両 itself (the stand-in) was missing, 両親 was unruby'd with a dash-gloss instead of the canonical ruby+quoted-gloss format, and 罔両 was buried inside a Notes sub-bullet instead of living in `## Words`.

**Words cross-check** (4 total ground-truth hits, searched under 両's own alias set 両/两/兩/倆/輛/辆/輌/㒳/魎/魉 per [[feedback_word_creation_alias_check]]): 両 (stand-in, added), 両親 (reformatted to ruby+gloss), 伎倆 (gloss added), 罔両 (moved into `## Words` proper, ruby preserved) — all four now present.

**Chengyu**: 2 ground-truth hits (一刀両断, 魑魅罔両) — both already present and already correctly ruby'd; no changes needed.

**Derived Characters**: none — no other character in the database names 両/兩/两 as its `graphemic_classification` — correctly omitted.

**Verification**: Python cross-check of all 6 `<rt>` values (4 Words + 2 Chengyu) against each cited file's own `注音` field — 0 mismatches.

### 2026-07-25, iteration 301 — [[characters/笑 (char)|笑]]

Next never-perfected character by `danayo_id` (2191). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 夭` already correct — verified via Wiktionary: 形声 (会意兼形声）, semantic 竹 ("bamboo") + phonetic 夭 — as bamboo sways in the wind: the body shaking with laughter. `mc_id: 882` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("laugh; smile" — eventive; the stand-in word 笑.md has no `pos` field).

**Body defects found**: `# Notes` used H1 instead of H2 (twenty-sixth time this loop); all four canonical bullets missing — section held only the two floating CC links; the stand-in 笑 itself was missing from Words; no `## Chengyu` despite a real hit. Second **Jōyō - Kōtō** levels case this loop (`joyo_level: 高等`, after 暗）.

**Words cross-check** (4 total): 3 already present （大笑/哄笑 glosses expanded to stored forms); 1 missing — 笑 (stand-in, annotated) — added.

**Chengyu**: 1 ground-truth hit — 呵呵大笑 — added with its full four-part stored gloss.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 300 — [[characters/競|競]]

Next never-perfected character by `danayo_id` (2190). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary/Shuowen: 会意, 誩 ("two people talking at once") + two 人 — vying in speech. `mc_id: 1799` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word 競争.md's own field.

**Body defects found**: `# Notes` used H1 instead of H2 (twenty-fifth time this loop); all four canonical bullets missing — section held only the two floating CC links and two stray word entries; no `## Words` section.

**Words cross-check** (2 total): both moved to a proper `## Words` section — 競争 (stand-in, annotated), 競走 — with rubies and stored glosses.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 299 — [[characters/童|童]]

Next never-perfected character by `danayo_id` (2189). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 重` already correct — verified via Wiktionary: 形声, semantic 䇂 ("criminal") + phonetic 重 — originally a young male slave; extended to "child." `mc_id: 1330` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` ("juvenile" as a noun; the stand-in word 児童.md's `pos` is empty, so no convention to inherit).

**Body defects found**: `# Notes` used H1 instead of H2 (twenty-fourth time this loop); the section held nothing but the two floating CC links — all four bullets, the entire `## Words` section, and `## Derived Characters` all missing despite 4 real ground-truth children.

**Words cross-check** (1 total ground-truth hit): 児童 (stand-in, annotated) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 4 hits — 憧 ("restless; flickering"), 撞 ("hit; bump"), 瞳 ("pupil of the eye"), 鐘 ("bell") — section added.

**Verification**: Python cross-check of all 5 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 298 — [[characters/窓|窓]]

Next never-perfected character by `danayo_id` (2188). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 囱` already correct — verified via Wiktionary: 形声, semantic 穴 ("hole; cave") + phonetic 囱 ("chimney; skylight," unlinked — no page). `mc_id: 7452` — beyond the CC mirror's top-4000, trusted per checklist policy, used verbatim (noted in the bullet that the CC ranking lists the standard form 窗）.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word 窓口.md (`pos: 名詞`).

**Body defects found**: `# Notes` used H1 instead of H2 (twenty-third time this loop); the section held nothing but the two floating CC links — all four bullets and the entire `## Words` section written from scratch.

**Words cross-check** (2 total): both missing — 窓口 (stand-in, annotated), 同窓 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 297 — [[characters/種|種]]

Next never-perfected character by `danayo_id` (2187). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 重` already correct — verified via Wiktionary: 形声, semantic 禾 ("grain") + phonetic 重 — originally "to plant"; extended to "seed," "kind." `mc_id: 845` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word 種類.md (`pos: 名詞`).

**Body defects found**: `# Notes` used H1 instead of H2 (twenty-second time this loop); all four canonical bullets missing — section held only the two floating CC links and a stray 種苗 entry; 4 of 7 ground-truth words missing (including the stand-in 種類 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (7 total): 3 already present; 4 missing — 種類 (stand-in, annotated), 播種， 耕種， 種族 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 種瓜得瓜 ("As a man plants, so shall he reap") — added.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 296 — [[characters/移|移]]

Next never-perfected character by `danayo_id` (2186). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 多` already correct — verified via Wiktionary: 形声, semantic 禾 ("grain") + phonetic 多. `mc_id: 911` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 移動.md's own field.

**Body defects found**: page structure inverted — `## Words` sat before `# Notes` (which was also H1, the twenty-first case this loop; same inversion pattern as 望/然）; Notes held nothing but the two floating CC links; the stand-in 移動 itself was missing.

**Words cross-check** (2 total): 遷移 already present (gloss expanded to stored form); 移動 (stand-in, annotated) added.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 295 — [[characters/科|科]]

Next never-perfected character by `danayo_id` (2185; 2184 already perfected). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 禾` **suspected wrong, verified correct** — Wiktionary: 科 is 形声 with **phonetic 禾** (OC \*ɡoːl) + semantic 斗 ("measuring tool") — I'd expected the standard 会意 reading and fetched to check; the stored field stands (measuring and sorting grain → "class, category"). `mc_id: 2076` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: 名詞` already filled — no gaps.

**Body defects found**: `# Notes` used H1 instead of H2 (twentieth time this loop); all four canonical bullets missing — section held only the two floating CC links; 5 of 8 ground-truth words missing (including the stand-in 学科 itself); no `## Chengyu` despite a real hit.

**Words cross-check** (8 total): 3 already present; 5 missing — 学科 (stand-in, annotated), 社会科学， 社会科， 百科， 百科事典 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 金科玉律 ("unbreakable rule") — added.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 294 — [[characters/祝|祝]]

Next never-perfected character by `danayo_id` (2183). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 示 ("altar") + 兄 ("person with an open mouth, praying") — a celebrant at the altar.

**`mc_id` off-by-one — the checklist's own named bug class, caught live**: stored `mc_id: 860` is actually 粟's rank; 祝 is **861** (verified directly in `lookup/CC/CC 0000.md` — "> 861. 祝"). Same one-line-off transcription pattern as the 艮/煌 cases documented in the checklist's Common mistakes. Frontmatter corrected, bullet written as 861st.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word 慶祝.md (`pos: 事詞`).

**Corpus fix (word file)**: `words/祝賀.md`'s stored english was "congradulate" → fixed to "congratulate" (the character page had faithfully copied the typo; the fix is at the source).

**Body defects found**: `# Notes` used H1 instead of H2 (nineteenth time this loop); all four canonical bullets missing; CC links floating; 2 of 3 ground-truth words missing (including the stand-in 慶祝 itself); no `## Derived Characters` despite a real hit.

**Words cross-check** (3 total): 祝賀 moved to `## Words` with ruby + corrected gloss; 慶祝 (stand-in, annotated), 祝日 added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — 呪 ("spell; incantation") — section added.

**Verification**: Python cross-check of all 4 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 293 — [[characters/祖|祖]]

Next never-perfected character by `danayo_id` (2182). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 且` already correct — verified via Wiktionary: 形声, semantic 示 ("altar") + phonetic 且 — the ancestral altar. `mc_id: 389` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: 名詞` already filled — no gaps.

**Body defects found**: the graphemic bullet used two broken link forms (`[示](Radical%20113)` — same class as 松's — and `[且 (char)](且%20(char).md)`, a relative path pointing nowhere) and had no semantic gloss; SKIP/Stroke, MC, and Levels bullets missing; CC links floating; 6 of 7 ground-truth words missing (including the stand-in 祖先 itself); the one present entry （祖父） was stray inside Notes with no ruby.

**Words cross-check** (7 total): all rebuilt — 祖先 (stand-in, annotated), 祖父， 祖母， 外祖父， 外祖母， 祖国， 始祖 — glosses from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 292 — [[characters/示|示]]

Next never-perfected character by `danayo_id` (2181). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: an altar (T-shaped stand) with drops of offering. `mc_id: 829` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 開示.md's own field.

**Body defects found**: `# Notes` used H1 instead of H2 (eighteenth time this loop); a stray editorial scratch line ("not 시, unfortunately" — someone's frustration that 示's Dan'a'yo 諺文 is 거, not 시 like its Sino-Korean; the distinction is self-evident from the frontmatter and the MC initial g, so deleted as junk, same class as 比's "1326"); all four canonical bullets missing; CC links floating; 8 of 9 ground-truth words missing; no `## Derived Characters` despite 2 real hits.

**Words cross-check** (9 total): 指示詞 already present; 8 missing — 開示 (stand-in, annotated), 表示， 展示， 顕示， 提示， 暗示， 誇示， 諭示 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 2 hits — 視 ("look at; inspect"), 祁 ("surname") — section added.

**Verification**: Python cross-check of all 11 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 291 — [[characters/破 (char)|破]]

Next never-perfected character by `danayo_id` (2180). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 皮` already correct — verified via Wiktionary: 形声, semantic 石 ("stone") + phonetic 皮. `mc_id: 385` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("rend; break" — eventive verbs).

**Body defects found**: all four canonical Notes bullets missing — section held only the two floating CC links and a stray 破戒 entry; 破戒/破暁 were misfiled under `## Chengyu` despite being plain words (only 破頭傷足 is a real chengyu) — moved to `## Words`; the stand-in 破 itself was missing.

**Corpus fix (word file)**: `words/破戒.md` stored `注音: ㄆㄚㄍ⼶` / `羅馬字: pagye` / `諺文: 파겨` — all three internally consistent but carrying the wrong initial vowel for 破, whose reading ㄆㄜ was **confirmed character-side-correct by the user** in the syllables thread (which fixed the identical typo in words/破.md itself). Fixed all three fields to ㄆㄜㄍ⼶ / pegye / 프겨. First word-file repair this loop.

**Words cross-check** (6 total): 3 already present (normalized); 3 missing — 破 (stand-in, annotated), 破戒 (ruby uses the corrected value), 破暁 — added from stored fields.

**Chengyu**: 破頭傷足 already present and correct — kept.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 290 — [[characters/看 (char)|看]]

Next never-perfected character by `danayo_id` (2179). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, a hand （手） held above the eyes （目） to gaze afar. `mc_id: 6498` — beyond the CC mirror's top-4000, trusted per checklist policy, used verbatim.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("watch over; look after; watch" — eventive verbs; the stand-in word 看.md has no `pos` field).

**Body defects found**: the graphemic bullet linked 手/目 bare despite both being Kangxi radicals (per the radical-linking rule → `[[Radical 064|手]]`, `[[Radical 109|目]]`); the SKIP bullet had the syllable link attached **and** an unclosed parenthesis on the Stroke link; the Levels bullet was in the wrong order; the MC bullet was missing with the CC links floating; the stand-in 看 itself was missing from Words.

**Words cross-check** (2 total): 看病 already present and correct; 看 (stand-in, annotated) added.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 289 — [[characters/省 (char)|省]]

Next never-perfected character by `danayo_id` (2178). Stamped `date-last-perfect: 2026-07-25` (first stamp under the corrected post-midnight date). `graphemic_classification: 生` already correct — verified via Wiktionary: 形声, semantic 目 ("eye") + phonetic 生 — originally "to inspect"; extended to "province" and "ministry." `mc_id: 671` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` ("government ministry"; the stand-in word 省.md has no `pos` field).

**Body defects found**: `# Notes` used H1 instead of H2 (seventeenth time this loop); the section held nothing but the two floating CC links — all four bullets and the entire `## Words` section written from scratch.

**Words cross-check** (2 total ground-truth hits): both missing — 省 (stand-in, annotated), 内省 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted (quote-tolerant grep, first iteration using the fixed pattern).

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 288 — [[characters/直 (char)|直]] + **loop-wide Derived Characters sweep**

Next never-perfected character by `danayo_id` (2177; 2176 already perfected). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, an eye （目） sighting along a straight line (with 十 and ∟). `mc_id: 444` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` ("straight; erect; aligned" — stative; the stand-in word 直.md has no `pos` field).

**Body defects found**: all four canonical Notes bullets missing — section held only the two floating CC links and stray word entries; 直観/直角 had no ruby; 4 of 8 ground-truth words missing (including the stand-in 直 itself).

**Words cross-check** (8 total): 4 already present (normalized); 4 missing — 直 (stand-in, annotated), 直線， 垂直， 率直 — added from stored fields.

**Chengyu**: 単刀直入 already present and correct — kept.

**Derived Characters — the iteration that exposed a loop-wide bug**: the cron prompt's children grep (`^graphemic_classification: X`) was **not quote-tolerant**, silently missing every character whose frontmatter stores the field in quoted form (`graphemic_classification: "直"` — e.g. 植 itself, perfected in iteration 253). A quote-tolerant re-check found **5 real children of 直** （値， 植， 殖， 埴， 置） instead of zero. A full sweep over every character perfected tonight followed; **16 pages needed backfills** (all applied and re-verified, 0 ruby mismatches across all 16):

- New sections written: 最 (+撮）, 未 (+味/妹/昧/寐/魅）, 永 (+泳/詠）, 求 (+球/逑/救）, 無 (+舞/撫/蕪）, 此 (+些/紫/柴/砦/雌 — the Wiktionary 此-family flagged as "not represented in the vault" in iteration 258 turned out to be entirely present, just quoted).
- Sections extended: 来 (+莱）, 果 (+顆/課/踝）, 止 (+是/祉/徙）, 比 (+庇/屁/毘）, 民 (+珉/暋）, 爾 (+璽）, 由 (+宙/迪/袖/軸/釉/紬/抽/笛）, 留 (+溜）, 番 (+幡/潘/蕃/播）, 登 (+橙/澄/灯）.

Cron prompt updated (job recreated) with a quote-tolerant children grep so future iterations can't repeat this.

**Verification**: 直 itself — 14 rubies, 0 mismatches.

### 2026-07-25, iteration 287 — [[characters/的|的]]

Next never-perfected character by `danayo_id` (2175). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 勺` already correct — verified via Wiktionary: 形声, semantic 白 ("white") + phonetic 勺 — the white center of a target. `mc_id: 3352` cross-checked against `lookup/CC/CC 3000.md` — exact match.

**Frontmatter**: `pos: 名詞` already filled — no gaps.

**Body defects found**: `# Notes` used H1 instead of H2 (sixteenth time this loop); the section held nothing but the two floating CC links — all four bullets written from scratch; the stand-in 目的 entry was missing its annotation.

**Words cross-check** (1 total ground-truth hit): 目的 already present — annotated as stand-in.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of the `<rt>` value — 0 mismatches.

### 2026-07-25, iteration 286 — [[characters/登 (char)|登]]

Next never-perfected character by `danayo_id` (2174). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 豆` was wrong — corrected to `会意`** (verified via Wiktionary: ideogrammic compound 癶 "left and right feet" + 豆 "raised object; stepping stone" — stepping up with both feet; 豆 is not 登's phonetic — OC \*tɯːŋ vs \*doːs — third classification correction this loop after 此/産）. `mc_id: 767` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("mount; board; climb" — eventive verbs; the stand-in word 登.md has no `pos` field).

**Body defects found**: `# Notes` used H1 instead of H2 (fifteenth time this loop); the section held nothing but the two floating CC links — all four bullets and the entire `## Words` section written from scratch. Both components of the 会意 bullet are Kangxi radicals, so both link to their Radical pages （癶 → Radical 105, 豆 → Radical 151).

**Words cross-check** (1 total ground-truth hit): the stand-in 登 itself, added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — 鄧 ("Teng") — section added.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 285 — [[characters/番 (char)|番]]

Next never-perfected character by `danayo_id` (2173). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: an animal's paw print (釆) in a field （田） — originally "footprint," the counting sense a borrowing. `mc_id: 2135` cross-checked against `lookup/CC/CC 2000.md` — exact match.

**Frontmatter**: `pos: 量詞` already filled ("time; occasion" — counter, first of its kind this loop) — no gaps.

**Body defects found**: `# Notes` used H1 instead of H2 (fourteenth time this loop); all four canonical bullets missing — section held only the two floating CC links; 2 of 3 ground-truth words missing (including the stand-in 番 itself); no `## Derived Characters` despite a real hit. First **Old HSK 3** levels case this loop (`hsk_level: "3"`).

**Words cross-check** (3 total): 週番 already present and correct; 番 (stand-in, annotated), 番号 added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — [[翻 (char)|翻]] ("flip") — section added.

**Verification**: Python cross-check of all 4 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 284 — [[characters/留 (char)|留]]

Next never-perfected character by `danayo_id` (2172). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 丣` already correct — verified via Wiktionary: 形声, semantic 田 ("field") + phonetic 丣 (unlinked — no page). `mc_id: 541` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: 性詞` already filled. `japanese_native` was a comma-in-scalar value (`と-める,と-まる`) → normalized to a proper two-item list (same fix the manual thread made on 収）.

**Body defects found**: `# Notes` used H1 instead of H2 (thirteenth time this loop); its pseudo-structured content named **卯** as the phonetic component (`[[卯]] + [[田]] = [[SKIP-2-5-5]]...`) — contradicting the page's own `graphemic_classification: 丣`, which is correct （丣 is 留's actual phonetic; 卯 is the look-alike it gets confused with) — bullet rewritten properly; the levels line used bare wiki-links in the wrong order with Grade missing entirely; MC bullet missing; CC links floating; 4 of 6 ground-truth words missing (including the stand-in 留 itself); no `## Derived Characters` despite a real hit.

**Words cross-check** (6 total): 停留/逗留 already present; 留 (stand-in, annotated), 保留， 留意， 留学生 added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — 瑠 ("lapis lazuli," names 留 as its phonetic; cf. 瑠璃清天 on 清's page) — section added.

**Verification**: Python cross-check of all 7 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 283 — [[characters/由 (char)|由]]

Next never-perfected character by `danayo_id` (2171). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a sprout (丨) emerging from a field （田） — "to grow from; origin" (replaces a leftover `Components: [[田]], [[丨]]` line, the 植 defect class). `mc_id: 377` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). SKIP-4 stroke rule passes (4-**5**-2 = 5 strokes).

**Frontmatter**: `pos: 後置詞` already filled ("from; since" — postposition, first of its kind this loop) — no gaps.

**Body defects found**: all four canonical Notes bullets missing — section held only the floating CC links and the Components line; 3 of 4 ground-truth words missing (including the stand-in 由 itself); no `## Chengyu` despite a real hit; no `## Derived Characters` despite a real hit.

**Words cross-check** (4 total): 因由 already present and correct; 由 (stand-in, annotated), 自由， 理由 added. **Not a bug**: 理由 stores ㄌㄧ·⼜ while 由's own syllable is ⼜ㄛ — checked before flagging: 由 carries multiple on'yomi (YUU/YU/YUI in its own `japanese` field), so this is a legitimate compound-level alternation, not the 恩/慣/体現 mismatch class — used as stored without flagging.

**Chengyu**: 1 hit — 自由自在 — added.

**Derived Characters**: 1 hit — [[油 (char)|油]] (perfected earlier tonight, iteration 268 — the first parent-child pair both completed by this loop) — section added.

**Verification**: Python cross-check of all 6 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 282 — [[characters/産|産]]

Next never-perfected character by `danayo_id` (2170). Stamped `date-last-perfect: 2026-07-25`. **`graphemic_classification: 會意` was wrong — corrected to `彥`** (verified via Wiktionary: 產 is a phono-semantic compound — abbreviated phonetic 彥 (OC \*ŋrans) + semantic 生 "to be born" — not a compound ideograph; second classification correction this loop after 此）. `mc_id: 858` cross-checked against `lookup/CC/CC 0000.md` — rank 858 is **產, the traditional form** (noted in the MC bullet).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 生産.md's own field.

**Body defects found**: `# Notes` used H1 instead of H2 (twelfth time this loop); all four canonical bullets missing — section held only the two floating CC links and two stray word entries; 産量 had no ruby; 1 of 6 ground-truth words missing; no `## Chengyu` despite a real hit. Phonetic 彥 left unlinked in the bullet (no page exists).

**Words cross-check** (6 total): 5 already present (normalized to stored glosses — 生産's expanded to "give birth to; produce; manufacture"); 1 missing — 共産 — added.

**Chengyu**: 1 ground-truth hit — 加哀痛産 ("add sorrow to painful labor") — added.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 281 — [[characters/理|理]]

Next never-perfected character by `danayo_id` (2169). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 里` already correct — verified via Wiktionary: 形声, semantic 玉 ("jade") + phonetic 里 — the veins in jade; hence "pattern, reason, principle." `mc_id: 435` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: 名詞` already filled — no gaps.

**Body defects found**: leftover `- Components: [[王]], [[里]]` line (the 植 defect class — and note it said 王 "king" where the semantic is properly 玉 "jade," the same near-identical-glyph confusion class as 五臓六府's ㄆ/ㄈ) — replaced with the canonical 形声 bullet; SKIP/Stroke, MC, and Levels bullets missing; CC links floating; 理想/理論 stray inside Notes; **15 of 22 ground-truth words missing**.

**Words cross-check** (22 total): 7 already present (all normalized to ruby + stored gloss); 15 missing — 理由 (the stand-in itself!), 理解， 道理， 管理， 修理， 整理， 辦理， 佐理， 心理， 心理学， 地理， 地理学， 物理学， 倫理， 肌理 — added from stored fields.

**Chengyu**: 形助顕理 already present and correct — kept.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 23 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 280 — [[characters/現 (char)|現]]

Next never-perfected character by `danayo_id` (2168). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 見` already correct — verified via Wiktionary: 形声, semantic 玉 ("jade") + phonetic 見. `mc_id: 7052` — beyond the CC 0000–3000 mirror's top-4000 coverage, so per the checklist's standing policy the large existing value is trusted ground truth, used verbatim ("7052nd most used").

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` ("present; revealed" — stative; the stand-in word 現.md has no `pos` field).

**Body defects found**: the graphemic bullet's phonetic link was literally **empty** (`[[]]`) — retargeted to `[[見 (char)|見]]`; SKIP/Stroke, MC, and Levels bullets missing; CC links floating mid-Words; 実現/現在 used non-canonical absolute paths with unquoted dash glosses; 現象 had no ruby; 4 of 9 ground-truth words missing (including the stand-in 現 itself); 1 of 2 ground-truth chengyu missing.

**Words cross-check** (9 total): 5 already present (all normalized); 4 missing — 現 (stand-in, annotated), 体現， 表現， 顕現 — added from stored fields. **Logged, not fixed**: 体現's stored `注音` (ㄊㄝㄧㄏ**⼔**ㄋ) diverges from 現's own syllable (ㄏ**⼶**ㄋ) — same character-vs-word mismatch bug class as 恩/慣/調 from the syllables thread; the ruby follows the word file byte-for-byte per the checklist, and the mismatch is flagged here for a future dedicated pass.

**Chengyu** (2 total): 現代適応 already present; 文言現代 ("Classical Chinese, Modern Day") added.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 11 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 279 — [[characters/特|特]]

Next never-perfected character by `danayo_id` (2167). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 寺` already correct — verified via Wiktionary: 形声, semantic 牛 ("cow; ox") + phonetic 寺 — originally a bull set apart for sacrifice; hence "special." `mc_id: 1102` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 特別.md's own field.

**Body defects found**: `# Notes` used H1 instead of H2 (eleventh time this loop); all four canonical bullets missing — section held only the two floating CC links and two stray word entries; 特殊 had no ruby; no `## Words` section; 2 of 4 ground-truth words missing.

**Words cross-check** (4 total): 特別 already correctly annotated (moved to `## Words`); 特殊 ruby'd; 特点， 特詞 added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 278 — [[characters/物 (char)|物]]

Next never-perfected character by `danayo_id` (2166). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 勿` already correct — verified via Wiktionary: 形声, semantic 牛 ("cow; ox") + phonetic 勿. `mc_id: 156` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: 代詞` already filled (matches words/物.md itself). `japanese_native` was malformed — bare scalar `もの` plus duplicate list item (the 油 bug class) → normalized to a single-item list.

**Body defects found**: graphemic bullet had no semantic gloss and its phonetic link was a broken relative path (`characters/勿%20(char).md` from inside `characters/`) → `[[勿 (char)|勿]]`; the SKIP bullet was **missing its Stroke link** (first time seen — usually it's the syllable link wrongly attached, here the Stroke half was simply absent); the Levels bullet was in the wrong order **and linked Grade 1 when `grade_level` is "2"** (a real content error, second bad levels link this loop after 満's Old HSK 1); MC bullet missing; CC links floating; chengyu entry bare; **27 of 35 ground-truth words missing** — the largest Words gap yet.

**Words cross-check** (35 total): 8 already present （物証/物質 ruby'd, glosses normalized); 27 added from stored fields, including the stand-in 物 itself, the 動物/植物/生物 core, the 万物/萬物 pair (both real word files), and the 此物/何物/其物/彼物/某物/毎物/皆物 pronoun series.

**Chengyu** (3 total): 万物生長， 主宰万物 added; 勿貪隣物 ruby'd + glossed.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 38 `<rt>` values — 0 mismatches. New loop record, passing 無's 33.

### 2026-07-25, iteration 277 — [[characters/片 (char)|片]]

Next never-perfected character by `danayo_id` (2165). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` verified via Wiktionary: a mirror image of 爿 ("piece," itself the pictograph of a bed); the Shuowen's alternative analysis — half of 木 ("wood"), "to pare; to slice" — noted in the bullet. `mc_id: 3661` cross-checked against `lookup/CC/CC 3000.md` — exact match. SKIP-4 stroke rule passes (4-**4**-4 = 4 strokes).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` ("slice; flake" — noun; the stand-in word 片.md has no `pos` field).

**Body defects found**: `# Notes` used H1 instead of H2 (tenth time this loop); all four canonical bullets missing — section held only the two floating CC links and a stray 片仮名 entry; no `## Words` section; the stand-in 片 itself missing.

**Words cross-check** (2 total ground-truth hits): both missing — 片 (stand-in, annotated), 片仮名 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 276 — [[characters/爾 (char)|爾]]

Next never-perfected character by `danayo_id` (2164). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: cloth on a loom with threads crossing (original form of 檷, "loom"), phonetically borrowed for 爾 ("you"). `mc_id: 572` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). SKIP-4 stroke rule passes (4-**14**-1 = 14 strokes).

**Frontmatter**: `pos: ""` (empty string) → filled in as `代詞` ("you" — pronoun, confirmed by korean_native 너; the stored english gloss "yes" left as-is — stored data, arguably from 爾's affirmative use, not a format defect).

**Body defects found**: **duplicate `## Notes` headings** (two of them — first held only the floating CC links, second held the graphemic bullet) — merged into one; graphemic bullet's curly quotes normalized; SKIP/Stroke, MC, and Levels bullets missing. Two first-time levels mappings this loop: `hsk_level: 無` → **[HSK No](lookup/HSK/HSK%20No.md)**, and `hanmun_edu_level: 名` → **Korean Name ㅇ** (the Korean Name files are per-initial; 爾's korean is 이 → ㅇ — format confirmed against existing perfected pages).

**Words cross-check** (3 total ground-truth hits): 愛爾蘭 already present and correct; 2 missing — 爾 (stand-in, annotated), 偶爾 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — 祢 ("thou; one's deceased father") names 爾 as its `graphemic_classification` — section added.

**Verification**: Python cross-check of all 4 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 275 — [[characters/熱 (char)|熱]]

Next never-perfected character by `danayo_id` (2163). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 埶` already correct — verified via Wiktionary: 形声, semantic 火 ("fire") + phonetic 埶 (unlinked — no page). `mc_id: 641` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` ("be hot" — stative, same call as 暑/暖； the stand-in word 熱.md has no `pos` field).

**Body defects found**: `## Notes` held nothing but the two floating CC links — all four canonical bullets written from scratch; 熱烈 had no ruby; 3 of 7 ground-truth words missing (including the stand-in 熱 itself).

**Words cross-check** (7 total): 4 already present （熱烈 ruby'd, glosses normalized to stored fields); 3 missing — 熱 (stand-in, annotated), 灼熱， 発熱 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 274 — [[characters/然 (char)|然]]

Next never-perfected character by `danayo_id` (2162). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 肰` already correct — verified via Wiktionary: 形声, semantic 火 ("fire") + phonetic 肰 ("dog meat," gloss from 肰's own page) — "to burn," the original form of 燃， phonetically borrowed for "so; thus." `mc_id: 81` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format, with backlink).

**Frontmatter**: `pos: ""` (empty string) → filled in as `副詞` ("so" — adverb; same call as 最/稍， the stand-in word 然.md has no `pos` field).

**Body defects found**: page structure was inverted — `## Words` sat before `# Notes` (which was also H1 instead of H2, ninth case this loop); Notes held nothing but the two floating CC links; 13 of 22 ground-truth words missing (including the stand-in 然 itself); no `## Chengyu` section despite 3 ground-truth hits.

**Words cross-check** (22 total): 9 already present (kept, glosses verified against stored fields); 13 missing — 然 (stand-in, annotated), 自然， 当然， 必然， 依然， 偶然， 俄然， 忽然様， 茫然， 混然， 無然， 昂然， 宛然 — all added from stored fields. Reordered central-first.

**Chengyu** (3 total, all missing): 一目瞭然， 混然一体， 茫然自失 — added.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 25 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 273 — [[characters/無 (char)|無]]

Next never-perfected character by `danayo_id` (2161; 2160 already perfected). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a person dancing with oxtails in both hands (rain-prayer dance; the original form of 舞）, phonetically borrowed for "not have." `mc_id: 18` cross-checked against `lookup/CC/CC 0000.md` — exact match; **highest-frequency character yet this loop** (18th most used in CC, with a backlink to the character page).

**Frontmatter**: `pos: 系詞` already filled and correct — 無 is one of the six copulas in [[grammar/文法 - 97品詞]] ("to not have").

**Body defects found**: the graphemic bullet had a stray floating period (`. A person dancing...`); SKIP/Stroke, MC, and Levels bullets all missing; CC links floating mid-Words; 13 of 20 existing Words entries were bare `[[links]]` with no ruby/gloss; 3 of 23 ground-truth words missing (including the stand-in 無 itself); 厚顔無恥/諸行無常 used non-canonical absolute paths (`/chengyu/...`), 諸行無常 had no gloss, 無為而治/孤立無援 were bare, and 3 of 10 ground-truth chengyu missing entirely.

**Words cross-check** (23 total): 無 (stand-in, annotated), 無人， 無名指 added; all 20 existing entries normalized to ruby + stored gloss, reordered central-first.

**Chengyu** (10 total): 上下無偶， 傍若無人， 諸法無我 added; paths and glosses normalized on the rest.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 33 `<rt>` values — 0 mismatches. Largest single-page ruby count this loop.

### 2026-07-25, iteration 272 — [[characters/満 (char)|満]]

Next never-perfected character by `danayo_id` (2159). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 㒼` already correct — verified via Wiktionary: 形声, semantic 氵 ("water") + phonetic 㒼 ("cover" — gloss pulled from 㒼's own page, replacing the old pinyin-as-gloss "(mán)"). `mc_id: 697` cross-checked against `lookup/CC/CC 0000.md` — rank 697 is **滿, the traditional form** (noted in the MC bullet).

**Frontmatter**: two gaps — `pos: ""` → filled as `性詞` ("full," stative); `vietnamese:` was **entirely empty** (third case this loop, after 楽/歩） → filled with mãn, the standard Sino-Vietnamese reading of 滿.

**Body defects found**: graphemic bullet linked 水 instead of the 氵 form and used curly quotes; SKIP/Stroke bullet had `../` prefixes plus the syllable link attached; Levels bullet in wrong order, `../` prefixes, and — a real mapping error — linked **Old HSK 1** when `hsk_level: "1"` maps to **HSK Beginner** per the checklist table; MC bullet missing; CC links floating; no `## Words` section at all (8 ground-truth hits); no `## Chengyu` despite a real hit.

**Words cross-check** (8 total ground-truth hits): all 8 missing — 満 (stand-in, annotated), 満足， 不満， 肥満， 満月， 満盈， 満洲， 満族 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 欲求不満 — added with ruby + gloss verbatim from its own fields (also cited on [[求]]'s page, perfected earlier tonight).

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 271 — [[characters/清|清]]

Next never-perfected character by `danayo_id` (2158). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 青` already correct — verified via Wiktionary: 形声, semantic 氵 ("water") + phonetic 青. `mc_id: 558` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: 性詞` already filled — no gaps.

**Body defects found**: the graphemic bullet was **duplicated** — one canonical copy and a second broken-link copy with curly quotes (`[氵](Radical%20085)`, `[青](青%20(char).md)`) — duplicate deleted, and the good copy's bare `[[青]]` retargeted to `[[青 (char)|青]]` (a word file 青.md exists, so the bare link would resolve to the word, not the character); SKIP/Stroke, MC, and Levels bullets missing; CC links floating; word entries dumped inside Notes with no `## Words` section; 清音 had no ruby; 4 of 10 ground-truth words missing (including the stand-in 清潔）; no `## Chengyu` despite a real hit.

**Words cross-check** (10 total ground-truth hits): 6 already present (glosses normalized to stored fields — 郭清's expanded to include "surgical dissection"); 4 missing — 清潔 (stand-in, annotated), 清淡， 清酒， 澄清 — added from stored fields. 清楚's long two-sense stored gloss kept in the page's existing condensed form (same treatment as 時's 時候）.

**Chengyu**: 1 ground-truth hit — 瑠璃清天 ("Lapis Lazuli") — added.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 11 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 270 — [[characters/浅 (char)|浅]]

Next never-perfected character by `danayo_id` (2157). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 㦮` already correct — verified via Wiktionary: 形声, semantic 氵 ("water") + phonetic 㦮 (unlinked — no page). `mc_id: 1412` cross-checked against `lookup/CC/CC 1000.md` — rank 1412 is **淺, the traditional form** (noted in the MC bullet).

**Frontmatter**: `pos: ''` (empty string) → filled in as `性詞` ("shallow" — stative).

**Body defects found**: `# Notes` used H1 instead of H2 (eighth time this loop); all four canonical bullets missing — section held only the two floating CC links and a stray 浅薄 entry; no `## Words` section; the stand-in 浅 itself missing. First **Old HSK 4** levels case this loop (`hsk_level: "4"`).

**Words cross-check** (2 total ground-truth hits): both missing — 浅 (stand-in, annotated), 浅薄 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 269 — [[characters/洗 (char)|洗]]

Next never-perfected character by `danayo_id` (2156; 2155 already perfected). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 先` already correct — verified via Wiktionary: 形声, semantic 氵 ("water") + phonetic 先. `mc_id: 1307` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("wash; rinse" — eventive verb; the stand-in word 洗.md has no `pos` field to inherit from).

**Body defects found**: `# Notes` used H1 instead of H2 (seventh time this loop); all four canonical bullets missing — section held only the two floating CC links and two stray word entries; `## Words` held only 洗礼； the stand-in 洗 itself and 2 other ground-truth words missing.

**Words cross-check** (4 total ground-truth hits): 洗礼 already present and correct; 3 missing — 洗 (stand-in, annotated), 洗濯， 洗車 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 4 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 268 — [[characters/油 (char)|油]]

Next never-perfected character by `danayo_id` (2154; 2153 already perfected). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 由` already correct — verified via Wiktionary: 形声, semantic 氵 ("water") + phonetic 由. `mc_id: 3745` cross-checked against `lookup/CC/CC 3000.md` — exact match (first CC 3000-range rank this loop).

**Frontmatter**: `pos: 名詞` already filled. `japanese_native` was malformed — a bare scalar `あぶら` followed by a duplicate list item `- あぶら` (same bug class as 来's mixed scalar/list, but with the same reading twice) → normalized to a single-item list.

**Body defects found**: `# Notes` used H1 instead of H2 (sixth time this loop); all four canonical bullets missing — section held only the two floating CC links and a stray 石油 entry; no `## Words` section; the stand-in 油 itself and 3 other ground-truth words missing.

**Words cross-check** (5 total ground-truth hits): 石油 already present (moved to `## Words`, gloss expanded to stored form); 4 missing — 油 (stand-in, annotated), 醤油， 汽油， 精油 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 5 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 267 — [[characters/決 (char)|決]]

Next never-perfected character by `danayo_id` (2152; 2153 already perfected). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 叏` already correct — verified via Wiktionary: 形声, semantic 氵 ("water") + phonetic 夬 (written 叏 in this form) — "to breach a dike, channel water; hence decide." `mc_id: 742` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("determine; decide" — eventive verb; the stand-in word 決.md has no `pos` field to inherit from).

**Body defects found**: the graphemic bullet had no semantic gloss and a doubled colon (`形声: (OC...)`); the 夬-descendants note used broken relative links (`characters/袂%20(char).md` from inside `characters/`) and a typo ("It's descendants") — rewritten as a documentation bullet after the canonical four with proper wiki-links (the note is about the *phonetic's* family, so no `## Derived Characters` section — checked: 袂 stores `graphemic_classification: 夬`, 快/缺/訣 store 叏， i.e. none names 決 itself); SKIP/Stroke, MC, and Levels bullets missing; 解決's entry used a non-canonical absolute path and had **no gloss at all**; 2 of 4 ground-truth words missing; 3 of 4 ground-truth chengyu missing.

**Words cross-check** (4 total): 決 (stand-in, annotated) and 処決 added; 解決 relinked/glossed; 決定 kept.

**Chengyu** (4 total): 声形和決 already present; 合漢再決， 文音共決， 覧昭和決 added — all three are 単亜語-origin vault coinages with scalar `english` fields (used verbatim).

**Verification**: Python cross-check of all 8 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 266 — [[characters/求|求]]

Next never-perfected character by `danayo_id` (2151). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: 象形, depicts a fur coat (the original form of 裘), phonetically borrowed for "request." `mc_id: 241` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format). SKIP-4 stroke rule passes (4-**7**-3 = 7 strokes).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 要求.md's own field exactly.

**Body defects found**: `## Notes` held nothing but the two floating CC links — all four canonical bullets written from scratch; the stand-in 要求 entry had no ruby; 4 of 5 ground-truth words missing; no `## Chengyu` section despite 2 ground-truth hits.

**Words cross-check** (5 total ground-truth hits): 要求 ruby'd and kept its stand-in annotation; 追求， 謀求， 欲求， 哀求 added from stored fields.

**Chengyu** (2 ground-truth hits, both missing): 刻舟求剣， 欲求不満 — added with rubies + glosses verbatim from their own stored fields.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 265 — [[characters/永|永]]

Next never-perfected character by `danayo_id` (2150). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary/Shuowen: 象形, a long meandering watercourse (長也 — "a stream flowing on without end; hence eternal"). `mc_id: 628` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 永遠.md's own field exactly (matched rather than second-guessed, same call as 案/提案).

**Body defects found**: `# Notes` used H1 instead of H2 (fifth time this loop); all four canonical bullets missing — section held only the two floating CC links and two stray word entries; 永久 had no ruby; no `## Words` section. First page this loop with a `middle_chinese_initial: ø` — the MC bullet links 聲 云 with the stored `ø` as the display alias.

**Words cross-check** (2 total ground-truth hits): 永遠 already correctly annotated as stand-in (moved to a proper `## Words` section); 永久 ruby'd and gloss expanded to the word file's full stored form.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 264 — [[characters/氷|氷]]

Next never-perfected character by `danayo_id` (2149). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` verified via Wiktionary: 氷 is the 俗字 (unorthodox variant) of 冰, which is 形声 (semantic 水 + phonetic 仌) — and 仌 is itself the original pictograph of ice (cracks in frozen water), so the 象形 classification holds through 仌. `mc_id: 1448` cross-checked against `lookup/CC/CC 1000.md` — rank 1448 is **冰, the standard form** (noted in the MC bullet, same as the 來/樂/步/歷 precedents).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word 氷水.md (`pos: 名詞`).

**Body defects found**: `# Notes` used H1 instead of H2 (fourth time this loop, after 期/案/比); all four canonical bullets missing — section held only the two floating CC links. The Words section was **already perfect** — all 4 ground-truth hits present, correctly ruby'd/glossed/annotated — kept verbatim.

**Words cross-check** (4 total ground-truth hits): 0 missing, 0 fixes needed.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — 馮 ("gallop") names 氷 as its `graphemic_classification` — section added.

**Verification**: Python cross-check of all 5 `<rt>` values — 0 mismatches.

### 2026-07-25, iteration 263 — [[characters/民|民]]

Next never-perfected character by `danayo_id` (2148). Stamped `date-last-perfect: 2026-07-25`. `graphemic_classification: 象形` already correct — verified via Wiktionary: the oracle-bone form depicts an eye pierced by a sharp implement, possibly tied to impaired vision (cf. 泯, 眠), extended to "the people." The pre-existing bullet's confused "Later jiajie (假借) for 民" line (circular — a character can't be a loan for itself) was rewritten to the standard analysis. `mc_id: 52` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format, with backlink to the character page).

**Frontmatter**: `pos: 名詞` already filled — no gaps.

**Body defects found**: SKIP/Stroke, MC, and Levels bullets all missing; CC links floating; 民主's entry used a non-canonical absolute path (`/words/民主.md`) with an unquoted dash gloss; 民謡 stray inside Notes; 6 of 17 ground-truth words missing; no `## Derived Characters` despite a real hit.

**Words cross-check** (17 total ground-truth hits): 11 already present (format normalized, absolute path fixed); 6 missing — 中華民国, 公民, 庶民, 民意, 牧民, 臣民 — all added from stored fields. Reordered most-central-first with the 人民 stand-in first.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — 眠 ("doze") names 民 as its `graphemic_classification` — section added.

**Process note**: this iteration was repeatedly killed mid-turn by the provider's output filter (four lost turns). Completed via a scripted rewrite that pulls every gloss and reading directly from the vault's own files instead of re-typing them in assistant-visible text. Content unchanged from what would have been written by hand.

**Verification**: Python cross-check of all 18 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 262 — [[characters/比 (char)|比]]

Next never-perfected character by `danayo_id` (2147). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, two 匕 ("person") side by side — "to compare." `mc_id: 426` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `格助詞`, matching the stand-in word 比.md's own field ("than" as a comparative case particle — first 格助詞 this loop). Fixed a real typo in `english`: "compared too" → "compared to" (the word file already had it right).

**Body defects found**: `# Notes` used H1 instead of H2 (third time this loop, after 期/案); a **stray junk line "1326"** (someone's abandoned scratch — the real mc_id is 426, verified) deleted; all four canonical bullets missing; CC links floating; word entries dumped inside Notes with no `## Words` section; 比率/比例 had no ruby; no `## Derived Characters` despite 3 ground-truth hits.

**Words cross-check** (7 total ground-truth hits): 5 already present; 2 missing — 比 (stand-in, annotated), 比喩 — added from stored fields. The pre-existing "(stand-in for 秕/粃)" annotation on 比糠 kept (it documents the aliases' stand-in, not a defect).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 3 hits — 批 ("criticism; comment"), 琵 ("pipa"), 砒 ("arsenic") all name 比 as their `graphemic_classification` — section added.

**Verification**: Python cross-check of all 10 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 261 — [[characters/殺 (char)|殺]]

Next never-perfected character by `danayo_id` (2146). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 杀` already correct — verified via Wiktionary: 形声, semantic 殳 ("weapon; to strike") + phonetic 杀, which doubles as 殺's own simplified form (phonetic left unlinked — no page, it's covered by the `aliases` field). `mc_id: 133` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` ("kill" — eventive verb; the stand-in word 殺.md has no `pos` field to inherit from).

**Body defects found**: `## Notes` held nothing but the two floating CC links — all four canonical bullets written from scratch; 殺身/殺戮 entries had no ruby; the stand-in 殺 itself and 暗殺 were missing from Words; no `## Chengyu` section despite 2 ground-truth hits.

**Words cross-check** (6 total ground-truth hits): 4 already present (ruby/glosses normalized); 2 missing — 殺 (stand-in, annotated), 暗殺 — added from stored fields.

**Chengyu** (2 ground-truth hits, both missing): 殺姦窃偽 ("murder, adultery, theft, lying" — a Bible-origin vault coinage on the four prohibitions), 道活墨殺 ("The Spirit gives life, but the Letter Kills") — both added from stored fields.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 260 — [[characters/歴|歴]]

Next never-perfected character by `danayo_id` (2145). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 厤` already correct — verified via Wiktionary: 形声, semantic 止 ("foot") + phonetic 厤 — "to pass through; hence experience, history." `mc_id: 948` cross-checked against `lookup/CC/CC 0000.md` — rank 948 is **歷, the traditional form** (noted in the MC bullet).

**Frontmatter**: `pos: 名詞` already filled — no gaps.

**Body defects found**: leftover `- Components: [[𠩵]], [[止]]` line (the 植 defect class) — replaced with the canonical 形声 bullet (phonetic 厤 left unlinked, no page exists); SKIP/Stroke, MC, and Levels bullets missing; CC links floating; 歴史's entry used an unquoted dash-gloss (`- history`, no ruby); 辟歴's gloss was wrapped in a non-standard parenthetical (`(霹靂) - thunderbolt, thunderclap`) — normalized to the word file's stored `english` field. The genuinely useful "do not confuse with 暦" bullet was **kept** as a fifth bullet after the canonical four (same treatment as 樹's 尌-alias note).

**Words cross-check** (3 total ground-truth hits): 2 already present (both reformatted); 1 missing — 披歴 — added from stored fields. 歴史 annotated as stand-in.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 259 — [[characters/歩|歩]]

Next never-perfected character by `danayo_id` (2144). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 止 ("foot") + 𣥂 ("foot turned backwards," written 少 in the modern form) — two feet in sequence: walking. `mc_id: 651` cross-checked against `lookup/CC/CC 0000.md` — rank 651 is **步, the standard form** (vault page is the shinjitai 歩; same as the 來/樂 precedents, noted in the MC bullet).

**Frontmatter**: `pos: 事詞` already filled; `vietnamese:` was **entirely empty** (required field, second time this loop after 楽) → filled with bộ, the standard Sino-Vietnamese reading of 步.

**Body defects found**: leftover `- Components: [[止]], [[少]]` line (the 植 defect class) instead of a real graphemic bullet — replaced with the canonical 会意 form, with an explicit note that the 少 here is 𣥂 (reversed 止), not the character 少 "few," since the bare Components line was genuinely misleading on that point; SKIP/Stroke, MC, and Levels bullets all missing; CC links floating.

**Words cross-check** (1 total ground-truth hit): 散歩 already present, correctly ruby'd/glossed/annotated as stand-in — kept verbatim.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of the `<rt>` value — 0 mismatches.

### 2026-07-24, iteration 258 — [[characters/此 (char)|此]]

Next never-perfected character by `danayo_id` (2143). Stamped `date-last-perfect: 2026-07-24`. **`graphemic_classification: 匕` was wrong — corrected to `会意`** (verified via Wiktionary: ideogrammic compound 止 "feet" + 匕 "person turned around" — "where a person stops; here"; possibly the original form of 跐. 匕 is not 此's phonetic — OC \*sʰeʔ vs 匕's \*pjiʔ — and the Shuowen analysis is 会意). First classification correction this loop. `mc_id: 51` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format, with a backlink to the character page).

**Frontmatter**: `pos: 代詞` already filled and correct ("this," same class as 時's time-pronouns).

**Body defects found**: leftover wiki-style `- Components: [[止]], [[匕]]` line (the 植 defect class) instead of a real graphemic bullet; all four canonical Notes bullets missing; CC links floating; no `## Words` section at all despite 10 ground-truth hits.

**Notes rebuilt**: 会意 bullet with both components linked to their Radical pages （止 → Radical 077, 匕 → Radical 021 — both are Kangxi radicals, so the radical-linking rule applies to each); first **Jinmeiyō** levels case this loop (`joyo_level: 日本人名用漢字` → `[[lookup/Japanese/Jinmeiyō]]`).

**Words cross-check** (10 total ground-truth hits): all 10 missing — 此 (stand-in, annotated), 此処， 此時， 此様， 此事， 此物， 此人， 此名， 此類， 此多 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none in-vault (Wiktionary lists a large 此-phonetic family — 紫/柴/雌/嘴 etc. — but none name 此 in their vault `graphemic_classification` fields, so nothing to add; if those pages are perfected later and store 此， they'll backfill here).

**Verification**: Python cross-check of all 10 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 257 — [[characters/止|止]]

Next never-perfected character by `danayo_id` (2142). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct — verified via Wiktionary: 象形, a footprint (originally "foot," the sense 趾 retains). **First page this loop whose Notes section was already fully canonical** — all four bullets present, in order, correctly formatted; kept verbatim except normalizing one pair of curly quotes. `mc_id: 303` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word 中止.md (`pos: 事詞`).

**Body defects found**: `### Derived Characters` was H3 instead of H2 and sat between Notes and Words (checklist order is Notes → Words → Chengyu → Derived) — promoted and moved to the end; its one entry [[之]] was bare with no ruby or gloss; 5 of 7 ground-truth words missing; 1 of 2 ground-truth chengyu missing; the stand-in annotation on 中止 was missing.

**Words cross-check** (7 total ground-truth hits): 2 already present; 5 missing — 停止， 禁止， 阻止， 抑止， 白止 — added from stored fields; 中止 annotated as stand-in.

**Chengyu** (2 ground-truth hits): 令行禁止 already present and correct; 六作一止 added.

**Derived Characters**: 之 kept — its own graphemic bullet cites 止 ("foot") as its semantic component, satisfying the checklist's component-link ground-truth rule even though its `graphemic_classification` field stores 會意 — now with ruby + gloss; 址 added (names 止 directly in `graphemic_classification`).

**Verification**: Python cross-check of all 11 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 256 — [[characters/樹|樹]]

Next never-perfected character by `danayo_id` (2141). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 尌` already correct — verified via Wiktionary: 形声, semantic 木 + phonetic 尌 (尌 being the original form of 樹 itself). `mc_id: 905` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word 樹木.md (`pos: 名詞`).

**Body defects found**: all four canonical Notes bullets missing — the section held only the floating CC links, stray Words entries, and one genuinely valuable documentation bullet (the 尌-alias rationale), which was **kept** as a fifth bullet after the canonical four (same treatment as 懍's documented exception note). The new graphemic bullet leaves 尌 unlinked (no page exists, per the 最/冃 precedent) and cross-references the alias note. Stray word entries: 樹袋熊/樹木/樹懶 had no ruby; 樹木 (the stand-in) had no annotation.

**Words cross-check** (8 total ground-truth hits): 6 already present (all now ruby'd/glossed/annotated); 2 missing — 楊樹， 沙羅双樹 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 8 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 255 — [[characters/楽|楽]]

Next never-perfected character by `danayo_id` (2140). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, silk strings (糸) on wood (木), a stringed instrument → "music" → "pleasure." `mc_id: 163` cross-checked against `lookup/CC/CC 0000.md` — rank 163 is **樂, the traditional form** (same as the 來/来 precedent; noted in the MC bullet).

**Frontmatter**: two gaps — `pos: ""` → filled as `性詞` (matches the stand-in word 快楽.md's own `pos`); `vietnamese:` was **entirely empty** (a required field) → filled with nhạc ("music") and lạc ("pleasure"), the two standard Sino-Vietnamese readings of 樂, matching the two senses.

**Body defects found**: the graphemic bullet's content was good but every link in it was broken — `[List of 会意](../lookup/List%20of%20会意.md))` with a doubled closing paren (and no List-of-会意 page is part of the 会意 template anyway), `[絲](糸.md)` pointing at a nonexistent relative path, curly quotes throughout — rewritten in canonical 会意 form keeping the oracle-bone/bronze paleographic detail; SKIP/Stroke bullet had `../` prefixes plus the syllable link attached; Levels bullet in wrong order with `../` prefixes; MC bullet missing entirely, and one of the floating CC links was the `[[../lookup/CC/finals/韻 鈬開]]` wiki-link-with-`../` bug (same one iteration 240 fixed on 昨); `### Derived Characters` used H3 instead of H2 with a bare, ruby-less 鑠.

**Words cross-check** (10 total ground-truth hits): 4 already present; 6 missing — **快楽 (the stand-in itself)**, 音楽， 安楽， 倶楽部， 雅楽， 楽経 — all added from stored fields, reordered central-first.

**Chengyu** (2 ground-truth hits): 喜怒哀楽 already present and correct; 飲食歓楽 missing — added.

**Derived Characters**: 鑠 stores `graphemic_classification: 樂` (the traditional alias of 楽 — a genuine derivative via the alias) — kept, section promoted to H2, ruby + gloss added.

**Verification**: Python cross-check of all 13 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 254 — [[characters/極 (char)|極]]

Next never-perfected character by `danayo_id` (2139). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 亟` already correct — verified via Wiktionary: 形声, semantic 木 + phonetic 亟 — "originally meaning a crossbeam rafter" (the existing graphemic bullet was already complete with OC values and dash-note; kept verbatim). `mc_id: 500` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` ("extreme; utmost" — stative; the stand-in word 極.md has no `pos` field to inherit from).

**Body defects found**: SKIP/Stroke, MC-rank, and Levels bullets all missing (only the graphemic bullet existed); CC links floating at the bottom of the file; the Words list was nearly complete (19 of 20) but **13 of the 19 entries were bare `[[links]]` with no ruby and no gloss**, 南極 used a non-canonical absolute path (`/words/南極.md`) with an unquoted gloss, and the stand-in 極 itself was the one word missing.

**Words cross-check** (20 total ground-truth hits): all 20 now present with ruby + stored glosses, reordered most-central-first （極 stand-in first, then 積極/至極/極度/極端…). Largest Words rebuild this loop since 時 (23).

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 20 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 253 — [[characters/植|植]]

Next never-perfected character by `danayo_id` (2138). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 直` already correct — verified via Wiktionary: 形声, semantic 木 ("wood") + phonetic 直 — "to set a plant straight into the ground." `mc_id: 1867` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: 名詞` already filled. Fixed a real typo in `english`: "vegitation" → "vegetation."

**Body defects found**: `## Notes` held only the two floating CC links and a leftover wiki-style `- Components: [[木]], [[直]]` line (the same "Components:" defect class the manual thread found on 保/俯) — all four canonical bullets written from scratch, graphemic bullet replacing the Components line with proper 形声 format and a semantic dash-note.

**Words cross-check** (1 total ground-truth hit): the stand-in 植物 was missing entirely (no `## Words` section existed) — added with ruby + gloss + annotation from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of the `<rt>` value — 0 mismatches.

### 2026-07-24, iteration 252 — [[characters/案|案]]

Next never-perfected character by `danayo_id` (2137; 2136 already perfected). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 安` already correct — verified via Wiktionary: 形声, semantic 木 ("wood") + phonetic 安 — originally a wooden tray/desk (preserved in kun つくえ and korean_native 책상); "proposal" is a later extension. `mc_id: 1052` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word 提案.md's own `pos` field exactly (提案 stores the top-level content-word class rather than the more specific 事詞 — matched rather than second-guessed).

**Body defects found**: `# Notes` used H1 instead of H2 (second time this loop, same as 期); all four canonical bullets missing — section held only the floating CC links and a stray ruby-less 案件 entry; no `## Words` section.

**Words cross-check** (2 total ground-truth hits): 案件 moved to a proper `## Words` section with ruby + stored gloss; the stand-in 提案 was missing entirely — added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 251 — [[characters/果|果]]

Next never-perfected character by `danayo_id` (2135). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct — verified via Wiktionary: 象形, fruit growing on a tree (the 田-shaped top is the fruit, not a field). `mc_id: 808` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word 果実.md (`pos: 名詞`). Note `stand_in: 果実` (compound), so no bare 果 word entry — the "(stand-in for 果)" annotation was already on 果実 and stays there.

**Body defects found**: no `## Notes` section at all; the two CC links were floating mid-Words, splitting the word list in two; 果汁 had no ruby; 6 of 10 ground-truth words missing; no `## Chengyu` despite a real hit; no `## Derived Characters` despite a real hit.

**Words cross-check** (10 total ground-truth hits): 4 already present （果汁 ruby'd; glosses normalized to stored fields); 6 missing — 効果， 因果， 果醤， 果子， 苹果， 桃果 — all added from stored fields. Reordered most-central-first （果実 stand-in first, then 結果/効果/因果…).

**Chengyu**: 1 ground-truth hit — 因果報応, added with ruby + gloss from its own stored fields.

**Derived Characters**: 1 hit — [[裸 (char)|裸]] ("strip; undress," ㄌㄚ) names 果 as its `graphemic_classification` — section added.

**Verification**: Python cross-check of all 12 `<rt>` values — 0 mismatches.

### 2026-07-24, iteration 250 — [[characters/松 (char)|松]]

Next never-perfected character by `danayo_id` (2134). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 公` already correct — verified via Wiktionary: 形声, semantic 木 ("wood") + phonetic 公. `mc_id: 1728` cross-checked against `lookup/CC/CC 1000.md` — exact match.

**Frontmatter**: all fields already filled (`pos: 名詞` present — first page this loop with no frontmatter gaps).

**Body defects found**: the graphemic bullet used two broken markdown link forms — `[木](Radical%20075)` (no `.md`, not a wiki-link) and `[公 (char)](公%20(char).md)` (a relative path pointing nowhere from inside `characters/`) — plus curly quotes instead of straight; fixed to canonical `[[Radical 075|木]]` / `[[公 (char)|公]]`. The SKIP/Stroke bullet had the syllable link improperly attached and every link carried a non-canonical `../` prefix (checklist examples are root-relative); the Levels bullet listed all four levels in the wrong order (Jōyō, Korean, HSK, Grade → fixed to Grade, HSK, Jōyō, Korean); the MC bullet was missing entirely with the CC links floating; 松竹梅 was a stray bullet inside Notes with no `## Words` section.

**Words cross-check** (2 total ground-truth hits): 松竹梅 moved to a proper `## Words` section with ruby; the stand-in 松 itself was missing — added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of both `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 249 — [[characters/来 (char)|来]]

Next never-perfected character by `danayo_id` (2133). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct — verified via Wiktionary: 象形, depicts a stalk of wheat; original sense "wheat" (cf. derived 麦), phonetically borrowed for "come." `mc_id: 168` cross-checked against `lookup/CC/CC 0000.md` — rank 168 is **來, the traditional form** (same character; vault stores the shinjitai stand-in, same as the 収/收 precedent) — not an off-by-one. SKIP-4 stroke rule passes (4-**7**-3 = 7 strokes).

**Frontmatter defects**: `japanese_native` was malformed — a bare scalar `き` with a dangling list item `- くる` under it (mixed scalar/list YAML) → normalized to a proper two-item list. `aliases: [來 (char)]` had a `(char)` suffix baked into the alias glyph itself → corrected to bare `來` (aliases are glyphs, not filenames; cf. 時's `- 时`).

**Body defects found**: all four Notes bullets missing (only floating CC links and a stray 来臨 entry); 来年 had no ruby; 9 of 15 ground-truth words missing entirely.

**Words cross-check** (15 total ground-truth hits): 6 already present; 9 missing — 来 (stand-in, added with annotation), 本来， 近来， 外来， 来月， 来週， 来日， 来世紀， 馬来西亜 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: 1 hit — [[麦]] ("wheat; barley," ㄇㄚㄎ) names 来 as its `graphemic_classification` — section added. (Fitting: 来's own 象形 origin *is* the wheat plant.)

**Verification**: Python cross-check of all 16 `<rt>` values (extended to check `characters/` files too, for the Derived Characters entry) — 0 mismatches.

### 2026-07-24, iteration 248 — [[characters/未 (char)|未]]

Next never-perfected character by `danayo_id` (2132). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct — verified via Wiktionary/Shuowen: 象形, a tree with lush layered foliage at the top (象木重枝葉也). `mc_id: 103` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format; this entry links back to the character page). SKIP-4 sanity check passes per the user's standing rule (4-**5**-3 matches `stroke_count: 5`).

**Frontmatter**: `pos: ""` (empty string) → filled in as `修飾語`, matching the stand-in word 未.md's own `pos` field ("not yet" as a modifier). Also normalized `vietnamese: [vị, mùi]` from a comma-in-scalar form to a proper two-item list.

**Body defects found**: the page ended at the meta-bind-embed — no `## Notes`, no `## Words`, nothing but the two floating CC links. All four Notes bullets written from scratch （象形 bullet per the checklist's List-of-象形 format, with 木 linked as Radical 075).

**Words cross-check** (2 total ground-truth hits): both missing — 未 (stand-in, added with annotation), 未月 — added from stored fields.

**Chengyu**: 1 ground-truth hit — 未雨紬謬, added with ruby from its own `注音` and its full stored gloss.

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 247 — [[characters/期 (char)|期]]

Next never-perfected character by `danayo_id` (2131). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 其` already correct — verified via Wiktionary: 形声, semantic 月 ("moon") + phonetic 其 (the moon's phases mark periods of time). `mc_id: 675` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote format).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` ("period; time; season" — the stand-in word 期.md has no `pos` field to inherit from; same call as the 時-family nouns).

**Body defects found**: `# Notes` used H1 instead of H2 (explicit checklist "Common mistakes" case); all four canonical Notes bullets missing — section held only the two floating CC links and two stray Words entries (期間 without ruby); no `## Words` heading at all; no `## Chengyu` section despite a real ground-truth hit.

**Words cross-check** (9 total ground-truth hits, via the Python frontmatter parse): 2 already present (期間 ruby'd, glosses normalized to stored fields); 7 missing — 期 (stand-in, added with annotation), 期限， 週期， 週期表， 長期， 上半期， 下半期 — all added from stored fields.

**Chengyu**: 1 ground-truth hit — 一期一会, added with ruby from its own `注音` and gloss from its `english` field (a scalar sentence rather than a list — lightly trimmed, meaning unchanged).

**Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 10 `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 246 — [[characters/望|望]]

Next never-perfected character by `danayo_id` (2130). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 亡` already correct — verified via Wiktionary: originally 𦣠, a 会意 of 臣 ("eye") + 𡈼 ("person standing on the ground") gazing into the distance; 月 added later, 臣 reanalyzed as 亡, making the modern form 形声 with phonetic 亡 (OC \*maŋs). `mc_id: 410` cross-checked against `lookup/CC/CC 0000.md` — exact match (blockquote line "> 410. 望"; the `^N.` grep pattern misses this file's blockquote formatting — use a looser pattern for CC 0000).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word 希望.md (`pos: 事詞` — "to hope" is an eventive).

**Body defects found**: section order inverted (`## Words` before `## Notes`); `## Notes` held nothing but stray Words entries and the two floating CC links; 仰望 had neither ruby nor gloss; all four canonical Notes bullets missing. Also: **this page's `stand_in` is the compound 希望, not the character itself** — so the "(stand-in for 望)" annotation goes on 希望, and no bare 望 word entry exists or was added.

**Ground-truth search upgraded mid-iteration**: the naive `grep -l '望 (char)'` pattern missed `words/声望.md`, which cites 望 in inline-list form (`characters: [声, 望]`) — switched to a Python frontmatter parse that handles inline lists, multi-line lists, quoted scalars, and bare-vs-`(char)` forms. Bare forms verified correct here (both character files are bare `声.md`/`望.md`, no word-file collision — the `(char)` suffix is not required). Final count: 10 words.

**Words cross-check** (10 total ground-truth hits): 4 already present （希望， 望月， 眺望， 望楼 — glosses normalized to stored fields); 6 missing — 欲望， 声望， 人望， 怨望， 望日， and the ruby-less 仰望 — all added from stored fields.

**Chengyu**: grep surfaced 乳蜜流地/欲求不満, but neither cites 望 in its `characters:` field (prose mentions only) — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 10 `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 245 — [[characters/最 (char)|最]]

Next never-perfected character by `danayo_id` (2129). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary/Shuowen: 会意 of 冃 + 取 ("to violate and seize," 犯而取也; superlative sense is a later extension). `mc_id: 1207` cross-checked against `lookup/CC/CC 1000.md` — exact match ("1207. 最").

**Frontmatter**: `pos: ""` (empty string) → filled in as `副詞` — "most" is a degree adverb; the taxonomy in [[grammar/文法 - 97品詞]] has no 副詞 entry, but corpus precedent exists ([[characters/稍 (char)|稍]] "slightly," [[characters/亙 (char)|亙]] both store `pos: 副詞`), and 稍 is a close behavioral analog.

**Body defects found**: graphemic bullet missing entirely (written from scratch — 冃 left unlinked since no 冃 page exists, 取 linked); the SKIP/Stroke bullet had a **wrong syllable link attached** — `[ㄍ⼶ㄫ](syllables/ㄍ⼶ㄫ.md)`, a copy-paste error that isn't even 最's own syllable (ㄐ⼔) — removed; MC-rank and Levels bullets missing; CC links floating.

**Words cross-check** (7 total ground-truth hits): 6 already present (最善 ruby-less — fixed; glosses normalized to stored `english` fields); 1 missing — the stand-in 最 itself, added with annotation. Also removed a misplaced "(stand-in for 初)" annotation from the 最初 entry — that annotation belongs on [[初]]'s own Words section, not here.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 7 `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 244 — [[characters/暗 (char)|暗]]

Next never-perfected character by `danayo_id` (2128). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 音` already correct — verified via Wiktionary: 形声, semantic 日 ("sun") + phonetic 音. `mc_id: 2372` cross-checked against `lookup/CC/CC 2000.md` — exact match ("2372. 暗").

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` ("dark," stative — same call as 暑/暖).

**Body defects found**: the `## Words` section didn't exist — its entries had been dumped inside `## Notes` between the graphemic bullet and the floating CC links, with no section heading at all; 暗中 had no gloss and 暗中/暗殺/暗示/暗暗 had no ruby; SKIP/Stroke, MC-rank, and Levels bullets all missing. Graphemic bullet kept as-is (correct, OC values present, phonetic 音 linked bare per the 形声 template).

**Notes rebuilt**: SKIP-1-4-9 + Stroke 13; MC bullet "2372nd most used character in Classical Chinese. Ancient [[Lookup/CC/initials/聲 影|ʔ]] + [[Lookup/CC/finals/韻 覃|ʌm]] → ㄚㄇ"; Levels — Grade 2, Old HSK 2, **Jōyō - Kōtō** (`joyo_level: 高等` — first Kōtō case this loop), Korean MS.

**Words cross-check** (9 total ground-truth hits): 6 already present (all ruby'd/glossed properly now); 3 missing — 暗 (stand-in, added with annotation), 暗黒, 黒暗 — added from stored fields. Reordered most-central-first.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: none — correctly omitted.

**Verification**: Python cross-check of all 9 `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 243 — [[characters/暖 (char)|暖]]

Next never-perfected character by `danayo_id` (2127). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 爰` already correct — verified via Wiktionary: 形声, semantic 日 + phonetic 爰. `mc_id: 2629` cross-checked against `lookup/CC/CC 2000.md` — exact match ("2629. 暖").

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` — gloss is "warm," a stative/adjective per [[grammar/文法 - 97品詞]] (no `pos` on the stand-in word 暖.md to inherit from; same call as 暑 last iteration).

**Body defects found**: `## Notes` contained nothing but the two floating CC links ([[Lookup/CC/initials/聲 泥]], [[Lookup/CC/finals/韻 桓]]) — all four canonical bullets written from scratch. Graphemic bullet written without OC reconstructions (none stored in frontmatter; same precedent as iteration 240's 昨), dash-note "the warmth of the sun."

**Words cross-check** (3 total ground-truth hits): 1 already present (暖簾 — ruby already correct; gloss expanded to the word file's full stored form "noren (Japanese shop curtain); hanging curtain (in storefront)"); 2 missing — 暖 (stand-in, added with annotation), 温暖 — added with ruby + gloss from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: no character names 暖 as its `graphemic_classification` — section correctly omitted.

**Verification**: Python cross-check of all 3 `<rt>` values against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 242 — [[characters/暑 (char)|暑]]

Next never-perfected character by `danayo_id` (2126; 2125 already perfected). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 者` already correct — verified via Wiktionary: 形声, semantic 日 + phonetic 者. `mc_id: 1374` cross-checked against `lookup/CC/CC 1000.md` — exact match ("1374. 暑").

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` — gloss is "hot (weather)," a stative/adjective per [[grammar/文法 - 97品詞]] (the stand-in word 暑.md has no `pos` field to inherit from).

**Body defects found**: the graphemic bullet's semantic gloss was an empty string (`日 ("")` → "sun; day") and it had no dash-note (added "summer heat under the sun"); the SKIP/Stroke bullet had the syllable link improperly attached to it (moved to the MC bullet) and used a wiki-link `[[Stroke 12]]` instead of the canonical markdown form; the MC-rank and Levels bullets were both missing entirely; the two CC links were floating at the bottom of the file (now embedded with IPA aliases — 聲 書|ɕ, 韻 魚|ɨʌ); no `## Words` section existed at all.

**Words cross-check**: exactly 1 ground-truth hit — the stand-in word 暑 itself (quoted-scalar `characters: "暑 (char)"` — the double grep caught it on both patterns) — added with ruby + gloss from its stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: no character names 暑 as its `graphemic_classification` — section correctly omitted. (The 者-phonetic children 着/書/猪/緒 belong on [[者]]'s page, not here.)

**Verification**: Python cross-check of the page's `<rt>` value against 暑.md's own `注音` — 0 mismatches.

### 2026-07-24, iteration 241 — [[characters/時 (char)|時]]

Next never-perfected character by `danayo_id` (2124). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 寺` already correct — verified via Wiktionary: 形声, semantic 日 ("sun; day") + phonetic 寺. `pos: 代詞` already filled — left as-is (matches the 何時/其時 time-pronoun convention; the stand-in word 時.md itself stores `pos: 名詞`, but the character page's own gloss is "when," so no clear defect to act on).

**Body defects found**: `# Notes` held only the graphemic bullet — SKIP/Stroke, MC-rank, and Levels bullets all missing; the two CC links ([[Lookup/CC/initials/聲 船]], [[Lookup/CC/finals/韻 之]]) were floating mid-file inside `## Words` instead of embedded in the MC bullet; 当時's entry used a non-canonical absolute path (`/words/当時.md`) and an unquoted gloss (`- then`); 時節 and 時宜 entries had no ruby.

**Notes rebuilt to canonical four bullets**: graphemic (kept, added semantic dash-note "the passing of days marks time"); SKIP-1-4-6 + Stroke 10; MC bullet written as "65th most used character in Classical Chinese. Ancient [[Lookup/CC/initials/聲 船|ʑ]] + [[Lookup/CC/finals/韻 之|ɨ]] → ㄙㄧ" (聲 船 for ʑ confirmed against the existing convention on another ʑ-initial character's bullet); Levels bullet per mapping — Grade 2, HSK Beginner (`hsk_level: "1"`), Jōyō - Kyōiku, Korean MS.

**Words cross-check** (23 total ground-truth hits): 11 already present (2 ruby-less fixed, 当時 relinked as wiki-link, glosses normalized to quoted, semicolon-joined forms from each word's own `english` field); 12 missing — 時 (stand-in, added with annotation), 何時, 其時, 常時, 彼時, 戦時, 時代, 時差, 某時, 此時, 毎時, 皆時 — all added with ruby + gloss from stored fields. List reordered most-central-first.

**Chengyu**: 1 ground-truth hit (時代錯誤) — already present with correct ruby, kept.

**Derived Characters**: no ground-truth hits (no character names 時 as its `graphemic_classification`) — section correctly omitted. (The 寺-phonetic siblings 持/等/特/詩 belong on [[寺]]'s page, not here.)

**Incidental fix**: typo in `words/時差.md`'s own `english` field — "time differece" → "time difference" (gloss on this page uses the corrected form).

**Verification**: Python cross-check of all 24 `<rt>` values on the page against each cited file's own `注音` — 0 mismatches.

### 2026-07-24, iteration 240 — [[characters/昨 (char)|昨]]

Next never-perfected character by `danayo_id` (2123). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 乍` already correct — verified via Wiktionary: 形声, semantic 日 ("sun") + phonetic 乍 — "yesterday," "former times."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching sibling words (昨日, 昨年) that both store `pos: 名詞` (the stand-in word 昨.md itself has no `pos` field).

**Content removed**: a non-canonical relative path (`../lookup/CC/finals/韻 鈬開`), corrected to the canonical root-relative form.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 072|日]] ("sun") + phonetic [[乍]] — "yesterday" (obsolete standalone in Standard Chinese); "former times, the past."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (昨) was missing entirely, and one entry (昨年) was bare with no ruby; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (6 total ground-truth hits, including a discovered quoted-scalar self-citation from 昨.md's own `characters: "昨 (char)"` field): 2 already present (昨日, 昨年 — ruby fixed); 4 missing — 昨 (stand-in, added with annotation), 昨週, 昨世紀, 昨月 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 乍`): [[詐]] ("to defraud"), [[酢]] ("vinegar"), [[作 (char)|作]] ("to make; do"), [[炸]] ("fried; explode"), [[窄]] ("narrow; tight"), [[祚]] ("throne; blessing") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 239 — [[characters/旧 (char)|旧]]

Next never-perfected character by `danayo_id` (2122). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 臼` already correct — verified via Wiktionary: 形声, semantic 雈 ("owl") + phonetic 臼 — originally a type of owl, later phonetically borrowed for "old."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching sibling words (旧金山, 旧字体, 旧正月) that all store `pos: 名詞` (the stand-in word 旧.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic 雈 ("owl," no vault page) + phonetic [[臼 (char)|臼]] (OC \*ɡuʔ) — originally a type of owl, later phonetically borrowed for a homophonous word meaning "old."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus two Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (旧) was missing entirely; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (5 total ground-truth hits, including a discovered quoted-scalar self-citation from 旧.md's own `characters: "旧 (char)"` field): 2 already present (旧金山 — ruby filled in from stored fields, 旧字体); 3 missing — 旧 (stand-in, added with annotation), 旧正月, 仍旧 — all added from stored fields.

**Chengyu cross-check** (1 total): 事事皆旧 — missing, added with its stored reading and gloss.

**Derived Characters** (1 hit via `graphemic_classification: 臼`, excluding this page itself): [[舅]] ("maternal uncle") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 238 — [[characters/方|方]]

Next never-perfected character by `danayo_id` (2121). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` kept as-is: Wiktionary offers no firm classification for 方, describing it only as possibly the original character of 旁 (OC \*baːŋ, "side"), with a form related to 巫 — 方 "lacks the indicator symbol on one end and is elongated to denote 'side.'" Since no clear alternative classification is given and the vault's pre-existing choice isn't contradicted, kept `象形` and documented the genuine uncertainty in the bullet (the same treatment as the earlier 害/再/平 iterations).

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 130` verified against `CC 0000.md`).

**Content removed**: a malformed "### Derived Characters" subsection using markdown-style links with no gloss, folded into a proper `## Derived Characters` section alongside the many further ground-truth hits found; a floating CC-initial/final pair sitting at the very end of the Words list with no MC-rank bullet.

**Graphemic bullet written from scratch**: documents the genuine etymological uncertainty per Wiktionary, plus adds the missing SKIP/Stroke/MC-rank/Levels bullets in canonical form.

**Body defects found**: `## Notes` held only the malformed Derived Characters fragment; several Words entries (方針, 東方, 方程式, 西方, 遠方, 方法, 南方, 北方, 方面, 方舟) were bare `[[link]]` with no ruby; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (19 total ground-truth hits — one of the largest word families surfaced in this loop): 8 already present with ruby (方向 stand-in, 地方, 五方, 平方, 方便, 方位, 漢方 — plus 10 bare entries reformatted with ruby/gloss from stored fields); 2 missing — 方響, 方言 — added from stored fields. (方言's own stored 注音 begins with ㄆ, not ㄈ like every other word on this page — cited verbatim as stored, not silently corrected, per the no-fabrication policy; flagged here as a possible pre-existing data inconsistency on 方言's own page, out of scope for this iteration.)

**Chengyu cross-check** (1 total): 天圓地方 — missing, added with its stored reading and gloss.

**Derived Characters** (11 hits via `graphemic_classification: 方` — the largest family surfaced in this loop, spanning two readings 方=ㄈㄚㄫ and its 旁-cluster =ㄅㄚㄫ): [[房 (char)|房]] ("room"), [[妨]] ("to hinder"), [[彷]] ("to resemble"), [[芳]] ("fragrant; beautiful"), [[坊]] ("workshop"), [[訪]] ("to visit; ask; inquire"), [[肪 (char)|肪]] ("fat; obese"), [[旁]] ("right part of a character"), [[紡 (char)|紡]] ("to spin (yarn)"), [[防]] ("to prevent"), [[放]] ("to release") — all added (the pre-existing malformed fragment's 4 entries — 彷/坊/妨/放 — folded in and reformatted alongside the rest).

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 237 — [[characters/料|料]]

Next never-perfected character by `danayo_id` (2120). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 米 ("rice") + 斗 ("dipper") — a dipper used to measure grain, "to measure, to gauge."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/材料|材料]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): [[米 (char)|米]] ("rice") + [[Radical 068|斗]] ("dipper") — a dipper used to measure grain; "to measure, to gauge," extended to "material, stuff."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (材料) was missing entirely.

**Words cross-check** (4 total ground-truth hits): 1 already present (料槽); 3 missing — 材料 (stand-in, added with annotation), 塑料, 化学肥料 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 料`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 236 — [[characters/散|散]]

Next never-perfected character by `danayo_id` (2119). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct, but the page's own pre-existing bullet directly contradicted it — describing a 形声 structure (semantic 肉 + phonetic 𢽳, itself with an empty OC gloss) instead. Verified via Wiktionary that 散 genuinely has a dual etymology: the oracle-bone original 㪔 is 會意 (林 "trees" + 攴 "to knock," to clear vegetation), while the Shuowen separately reads the modern glyph as 形声 (semantic 肉 + phonetic 𢽳, an obscure component with no vault page). Since this character's own `radical:` field (`攴`) matches the ancient 會意 form's own component directly, kept the field at `會意` and rewrote the bullet to match, noting the Shuowen alternative for completeness.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word [[words/散布|散布]]'s own stored `pos`.

**Content removed**: none of substance — the "neologism: 散氷 for hail/sleet" note was kept as a Notes bullet rather than dropped.

**Graphemic bullet rewritten**: [List of 会意](lookup/List%20of%20会意.md) (OC \*saːnʔ, \*saːns): the oracle-bone original form 㪔 is 会意 — [[林 (char)|林]] ("trees, forest") + [[Radical 066|攴]] ("to knock, tap") — to clear vegetation, to kill; extended via bamboo's tendency to break apart to "to disperse, scatter." (The Shuowen instead reads the modern glyph as 形声: semantic 肉 + phonetic 𢽳.)

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (散布) was missing entirely.

**Words cross-check** (3 total ground-truth hits): 2 already present (散歩, 拡散); 1 missing — 散布 (stand-in, added with annotation) — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 散`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 235 — [[characters/敗|敗]]

Next never-perfected character by `danayo_id` (2118). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 貝` already correct — verified via Wiktionary: 形声, phonetic 貝 + semantic 攴/攵 ("strike") — "to lose, to be defeated; to fail."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/失敗|失敗]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*praːds, \*braːds): phonetic [[貝]] (OC \*paːds) + semantic [[Radical 066|攴]] ("strike") — "to lose, to be defeated; to fail, to destroy." This character's own `radical:` field is `攴`, matching the semantic component directly (the same pattern as the recent 政/故/救 iterations) — gets the Radical-page link, while [[貝]] (the phonetic, has its own page) gets a direct character-page link.

**Body defects found**: `## Notes` held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (失敗) had no annotation; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (2 total ground-truth hits): both already present (失敗 — annotation added, 腐敗), no missing entries.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 hits via `graphemic_classification: 貝`): [[鎖 (char)|鎖]] ("chain"), [[狽]] ("werewolf"), [[貿]] ("trade; commerce"), [[唄 (char)|唄]] ("ugh") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 234 — [[characters/救|救]]

Next never-perfected character by `danayo_id` (2117). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 求` already correct — verified via Wiktionary: 形声, phonetic 求 + semantic 攴 — "to save, rescue."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/救援|救援]]'s own stored `pos`.

**Content removed**: a floating bare Words-style entry (救偕) sitting inside `## Notes` instead of `## Words`.

**Graphemic bullet written from scratch**: 形声 (OC \*kus): phonetic [[求]] (OC \*ɡu) + semantic [[Radical 066|攴]] — "to aid, support"; "to save, rescue"; (obsolete) "to prohibit, forbid." This character's own `radical:` field is `攴`, matching the semantic component directly (the same pattern as the recent 政/故 iterations) — gets the Radical-page link, while [[求]] (the phonetic, has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and mixed graphemic content with a bare Words-style entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (救援) had no annotation; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (3 total ground-truth hits): 2 already present (救贖, 救偕 — relocated out of Notes); 1 missing — 救援 (stand-in, added with annotation) — added from stored fields.

**Chengyu cross-check** (1 total): 創反救成 already present, no changes needed.

**Derived Characters** (2 hits via `graphemic_classification: 求`): [[球 (char)|球]] ("sphere; ball"), [[逑]] ("mate; match") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 233 — [[characters/故|故]]

Next never-perfected character by `danayo_id` (2116). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 古` already correct — verified via Wiktionary: 形声, semantic 攴 ("action") + phonetic 古 — "cause, reason," "old, of the past," also a connective, "therefore." This is the same phonetic-root character already surfaced as a Derived Character on the earlier [[characters/古|古]] iteration; perfecting it here completes the family from the other direction.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the sibling word [[words/緣故|緣故]]'s own stored `pos`.

**Content removed**: two floating bare Words-style entries (故郷, 故而) sitting inside `## Notes` instead of `## Words`; a duplicate `## Chengyu` section (温故知新 listed twice back-to-back, likely from an editing accident before this iteration), collapsed to one.

**Graphemic bullet written from scratch**: 形声 (OC \*kaːs): semantic [[Radical 066|攴]] ("action") + phonetic [[古]] (OC \*kaːʔ) — "old, of the past"; "cause, reason"; "accident, misfortune"; "deceased"; also a connective, "therefore, so." This character's own `radical:` field is `攴`, matching the semantic component directly (the same radical/pattern as the recent [[characters/政|政]] iteration) — gets the Radical-page link, while [[古]] (the phonetic, has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and mixed graphemic content with bare Words-style entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (緣故) had no annotation.

**Words cross-check** (10 total ground-truth hits): 3 already present (緣故 — annotation added, 故事, 故而 — relocated out of Notes); 7 missing — 故郷 (relocated, ruby added), 事故, 故意, 故障, 縁故, 故人, 何故 — all added from stored fields.

**Chengyu cross-check** (1 total): 温故知新 already present (the duplicate collapsed as noted above), no further changes needed.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 故`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 232 — [[characters/政|政]]

Next never-perfected character by `danayo_id` (2115 — 2114 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 正` already correct — verified via Wiktionary: 形声, semantic 攴 ("action") + phonetic 正 (OC \*tjeŋ, \*tjeŋs). The page's pre-existing bullet had the semantic/phonetic roles backwards (labeled 正 as semantic and 攴 as phonetic) even though the frontmatter field itself was already right; fixed the bullet's own labeling to match.

**Frontmatter**: already correct (`pos: "名詞"`, `mc_id: 217` verified against `CC 0000.md`).

**Content removed**: a markdown-style link (`[政府](/words/政府.md)`) converted to a wikilink.

**Graphemic bullet rewritten**: semantic [[Radical 066|攴]] ("action") + phonetic [[正 (char)|正]] (OC \*tjeŋ, \*tjeŋs) — a specialization of 正 ("straight, upright; correct"), combined with the action radical. This character's own `radical:` field is `攴`, matching the semantic component directly (攴 itself now has a vault page, created 2026-07-17 per project notes) — gets the Radical-page link; [[正 (char)|正]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (政治) was missing entirely; two entries (政府, 政党) were bare or markdown-linked with no proper ruby.

**Words cross-check** (8 total ground-truth hits): 3 already present (政府 — link/ruby fixed, 政党 — ruby fixed, 行政); 5 missing — 政治 (stand-in, added with annotation), 政治学, 無政府, 暴政, 郵政 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 政`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 231 — [[characters/支|支]]

Next never-perfected character by `danayo_id` (2113). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct and already well-documented in the page's own pre-existing bullet — [[又 (char)|又]] ("hand") + [[十 (char)|十]] ("half of 竹, branch of bamboo") — a branch. This is the same phonetic-root character already surfaced as a Derived Character on the recent [[characters/技|技]] iteration; perfecting it here completes the family from the other direction.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/支部|支部]]'s own stored `pos`. This character's own `radical:` field is `支` (itself — Kangxi Radical 065), which is expected and not a defect, since neither etymological component (又, 十) literally matches it.

**Content removed**: a markdown-style link (`[支那](/words/支那.md)`) converted to a wikilink; a mislabeled `## Word` heading (singular) corrected to `## Words`.

**Graphemic bullet**: kept verbatim, converted markdown-style component links to wikilinks (`[[又 (char)|又]]`, `[[十 (char)|十]]`, both requiring the `(char)` filename suffix that the original bare links lacked).

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (支部) was missing entirely; no `## Derived Characters` section existed despite the large family already known from 技's iteration.

**Words cross-check** (6 total ground-truth hits): 4 already present (支那 — link fixed, 支付, 地支, 支配 — ruby filled in); 2 missing — 支部 (stand-in, added with annotation), 印度支那 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 hits via `graphemic_classification: 支`, excluding this page itself — the same family from 技's recent iteration, now completed from 支's own side): [[伎]], [[岐 (char)|岐]], [[枝]], [[肢]], [[妓]], [[技]], [[翅]] — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 230 — [[characters/推 (char)|推]]

Next never-perfected character by `danayo_id` (2112). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 隹` already correct — verified via Wiktionary: 形声, semantic 手 ("hand") + phonetic 隹 — "push with the hand."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the sibling word [[words/推薦|推薦]]'s own stored `pos` (the stand-in word 推.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 064|手]] ("hand") + phonetic [[隹]] — "push with the hand"; extended to "postpone; promote; nominate; infer, deduce."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (推) was missing entirely; no `## Derived Characters` section existed despite a very large real ground-truth hit.

**Words cross-check** (3 total ground-truth hits, including a discovered quoted-scalar self-citation from 推.md's own `characters: "推 (char)"` field): 1 already present (推測, ruby filled in from stored fields); 2 missing — 推 (stand-in, added with annotation), 推薦 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (10 hits via `graphemic_classification: 隹` — the largest family surfaced in this loop): [[椎]] ("vertebrae; spine"), [[唯 (char)|唯]] ("only"), [[錐]] ("awl"), [[維]] ("to support"), [[雉 (char)|雉]] ("green pheasant"), [[堆]] ("piled up; heap up"), [[崔]] ("high; lofty; towering"), [[淮]] ("Hwai"), [[誰 (char)|誰]] ("who"), [[進]] ("to advance; progress") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 229 — [[characters/接 (char)|接]]

Next never-perfected character by `danayo_id` (2111). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 妾` already correct — verified via Wiktionary: 形声, semantic 扌 ("hand") + phonetic 妾 — "to receive (in the hand)."

**Frontmatter**: already correct (`pos: "事詞"`, `mc_id: 1047` verified against `CC 1000.md`). Fixed an internal contradiction: the frontmatter's own `hanmun_edu_level: 中` maps to Korean MS, but the pre-existing bullet linked "Korean HS" instead.

**Content removed**: a malformed graphemic bullet with an unmatched parenthesis (`OC \*ʔseb):` with no opening paren) and a markdown-style Radical link; a malformed tip callout (`>[!tip] This is about the character.`, missing "a page" and the character name) corrected to standard phrasing; a compressed inline SKIP/Stroke/syllable bullet, expanded into canonical form.

**Graphemic bullet rewritten**: 形声 (OC \*ʔseb): semantic [[Radical 064|扌]] ("hand") + phonetic [[妾 (char)|妾]] (OC \*sʰeb) — to receive (in the hand). Kept the correct pre-existing analysis, just fixed formatting.

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; the stand-in Words entry (接) was missing entirely; four entries (接続助詞, 接触, 接受, 接吻) were bare `[[link]]` with no ruby.

**Words cross-check** (14 total ground-truth hits): 5 already present (接続助詞, 接触, 接受, 接吻 — ruby added, 接尾辞); 9 missing — 接 (stand-in, added with annotation), 接線, 交接, 連接詞, 連接, 接近, 接辞, 正接, 余接 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 妾`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 228 — [[characters/挙 (char)|挙]]

Next never-perfected character by `danayo_id` (2110). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, but Wiktionary classifies 舉/挙 as 形声 — semantic 手 ("hand") + phonetic 與/与 — "to raise, to lift up." Corrected to `与`; unlike the recent 児/加/従/愛 self-referential defects, 与 is a genuinely independent character with its own vault page (not an alias of 挙 itself), so this is a valid, non-self-referential phonetic value.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` (the stand-in word 挙.md itself has no `pos` field; "to raise" is a transitive action verb).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 064|手]] ("hand") + phonetic [[与 (char)|與]] — "to raise, to lift up"; extended to "to elect; to start, initiate."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (挙) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (2 total ground-truth hits, including a discovered quoted-scalar self-citation from 挙.md's own `characters: "挙 (char)"` field): 1 already present (科挙); 1 missing — 挙 (stand-in, added with annotation) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 与`): [[輿 (char)|輿]] ("palanquin"), [[誉]] ("reputation; fame") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 227 — [[characters/投 (char)|投]]

Next never-perfected character by `danayo_id` (2109). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 殳` already correct — verified via Wiktionary: 形声, semantic 扌/手 ("hand") + phonetic 殳 — "to throw, to fling."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` (the stand-in word 投.md itself has no `pos` field; "to throw" is a transitive action verb).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*doː): semantic [[Radical 064|手]] ("hand") + phonetic 殳 (OC \*djo, no vault page) — "to throw, to fling"; extended to "casting, projecting, putting in, abandoning."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` or `## Chengyu` sections existed despite real ground-truth hits for both.

**Words cross-check** (2 total ground-truth hits, including a discovered quoted-scalar self-citation from 投.md's own `characters: "投 (char)"` field): both missing — 投 (stand-in, added with annotation), 投票率 — added from stored fields.

**Chengyu cross-check** (1 total): 珠投猪前 — missing, added with its stored reading and gloss.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 殳`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 226 — [[characters/技|技]]

Next never-perfected character by `danayo_id` (2108). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 支` already correct — verified via Wiktionary: 形声, semantic 扌/手 ("hand") + phonetic 支 — "skill with one's hands, artisan."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/技能|技能]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*kje): semantic [[Radical 064|手]] ("hand") + phonetic [[支]] — skill with one's hands, artisan; "skill, ability, talent, artistry, technique."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (技能) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (3 total ground-truth hits): 1 already present (技術); 2 missing — 技能 (stand-in, added with annotation), 技巧 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 支`): [[伎]] ("talent; skill; ability"), [[岐 (char)|岐]] ("fork (in road)"), [[枝]] ("foliage"), [[肢]] ("limbs"), [[妓]] ("actress"), [[翅]] ("shark fin") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 225 — [[characters/戸|戸]]

Next never-perfected character by `danayo_id` (2107). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct and already well-documented in the page's own pre-existing bullet — a pictogram of one-half of 門 ("gate") — no changes needed there.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/門戸|門戸]]'s own stored `pos`.

**Content removed**: a compressed inline syllable/MC bullet, expanded into the canonical four-bullet format; a malformed tip callout (`>[!tip] This is about the character`, missing "a page" and the character name) corrected to the standard phrasing.

**Graphemic bullet**: kept verbatim, no changes needed.

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no proper MC-rank/Levels bullets existed in canonical form; the stand-in Words entry (門戸) was missing entirely; one entry (戸籍) had no ruby.

**Words cross-check** (5 total ground-truth hits): 2 already present (戸籍 — ruby fixed, 江戸); 3 missing — 門戸 (stand-in, added with annotation), 井戸, 江戸川 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (9 hits, spanning two related fields — 5 via `graphemic_classification: 戸`/`戶` directly: [[所 (char)|所]], [[肩 (char)|肩]], [[芦]], [[扈]], [[雇]]; plus 4 more via `graphemic_classification: 盧`, itself one of this character's own `aliases:`: [[炉]] (already present, reformatted), [[鈩]], [[廬]], [[馿 (char)|馿]]) — all added. Discovered that alias-cited phonetics (like 盧 here) need their own separate ground-truth search pass, not just the literal headword string.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 224 — [[characters/戦|戦]]

Next never-perfected character by `danayo_id` (2106 — 2105 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 単` already correct — verified via Wiktionary (checked under the traditional form 戰): 形声, phonetic 單/単 + semantic 戈 ("halberd") — "battling with a halberd," "war, battle."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/戦争|戦争]]'s own stored `pos`. `hsk_level: ""` (also blank) left as-is rather than fabricated, since blank is distinct from the checklist's documented `"無"` (confirmed-absent) value and no reliable source was checked for this field this iteration.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*taːn, \*djan, \*djanʔ, \*djans): phonetic [[単]] + semantic [[Radical 062|戈]] ("halberd") — "battling with a halberd"; "to fight a battle, wage war."

**Body defects found**: `## Notes` was empty; two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (戦争) was missing entirely, and two entries (戦艦, 戦時) were bare `[[link]]` with no ruby; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (7 total ground-truth hits): 3 already present (戦闘, 戦艦 — ruby/gloss fixed, 戦時 — ruby/gloss fixed); 4 missing — 戦争 (stand-in, added with annotation), 挑戦, 戦場, 戦国 — all added from stored fields.

**Chengyu cross-check** (1 total): 戦戦恐恐 already present, no changes needed.

**Derived Characters** (4 hits via `graphemic_classification: 単`): [[蝉 (char)|蝉]] ("cicada"), [[弾]] ("bullet"), [[惮]] ("dread; shirk; fear"), [[簞]] ("bamboo basket") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 223 — [[characters/成 (char)|成]]

Next never-perfected character by `danayo_id` (2104). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 丁` already correct — verified via Wiktionary: 形声, semantic 戊 ("weapon; protection") + phonetic 丁 — originally "city walls," a sense preserved in [[characters/城|城]].

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 93` verified against `CC 0000.md`).

**Content removed**: an empty gloss placeholder (`""`) on the semantic component 戊 in the pre-existing bullet, filled in properly; a compressed single-line SKIP/Stroke/syllable/CC bullet, expanded into the canonical four-bullet format.

**Graphemic bullet rewritten**: semantic [[戊]] ("weapon; protection") + phonetic [[丁 (char)|丁]] (OC \*rteːŋ, \*teːŋ) — originally "city walls," a reference to something protected, with the sense preserved in 城. Neither component matches this character's own `radical:` field (`戈`), so both get direct character-page links.

**Body defects found**: section order was Chengyu then Words (both before this fix); the stand-in Words entry (成) was missing entirely, and two entries (成立, 成功, 成熟) were bare `[[link]]` with no ruby; 成家立業's chengyu entry had no gloss at all.

**Words cross-check** (14 total ground-truth hits, including a discovered quoted-scalar self-citation from 成.md's own `characters:` field): 7 already present in some form (変成, 成立/成功/成熟 — ruby/gloss fixed, 成績, 道成肉身, 合成); 7 missing — 成 (stand-in, added with annotation), 完成, 平成, 形成, 成語, 四字成語, 養成 — all added from stored fields.

**Chengyu cross-check** (4 total): 大器晩成, 創反救成 already present and correctly glossed; 成家立業 given its stored gloss (was missing one); 不打不成器 missing — added with its stored reading and gloss.

**Derived Characters** (9 hits via `graphemic_classification: 丁` — one of the larger families surfaced in this loop): [[打]] ("to hit"), [[釘 (char)|釘]] ("nail; spike"), [[汀 (char)|汀]] ("sand bar"), [[訂 (char)|訂]] ("to revise; correct"), [[亭]] ("pavilion; kiosk"), [[頂]] ("peak"), [[庁]] ("hall; room"), [[正 (char)|正]] ("correct"), [[町]] ("ridge between fields; boundary") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 222 — [[characters/愛 (char)|愛]]

Next never-perfected character by `danayo_id` (2103). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was invalid: stored as `㤅`, which is listed among this character's own `aliases:` — the same self-referential defect class as 便/児/加/従. Verified via Wiktionary that 愛 was "originally written as 㤅," itself phonetic 旡 + semantic 心, with 夊 ("foot") added later as a redundant component during Qin; the true phonetic beneath the self-referential alias is 旡. Corrected the field to `旡`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` (the base transitive sense "to love"; no sibling word using the bare root 愛 could supply a directly reusable `pos`, so this is a judgment call based on grammatical behavior per the checklist's own guidance).

**Content removed**: a markdown-style link (`[可愛](/words/可愛.md)`) converted to a wikilink.

**Graphemic bullet written from scratch**: originally written 㤅, phonetic 旡 (no vault page) + semantic [[Radical 061|心]] ("heart"). During the Qin dynasty a redundant component 夊 ("foot") was added at the bottom; the original phonetic 旡 later corrupted into ⿱爫冖. "To love; to treasure, value; to like, be fond of."

**Body defects found**: two CC-initial/final links floated at the very end of the page with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (愛) was missing entirely, and five entries (恩愛, 愛好, 愛惜, 愛情, 愛護) were bare `[[link]]` with no ruby.

**Words cross-check** (11 total ground-truth hits, including a discovered quoted-scalar self-citation from 愛.md's own `characters: "愛 (char)"` field): 10 already present in some form (愛人, 愛媛, 可愛 — link fixed, 恩愛/愛好/愛惜/愛情/愛護 — ruby/gloss filled in, 愛爾蘭, 愛因金); 1 missing — 愛 (stand-in, added with annotation).

**Chengyu cross-check** (4 total): 愛偕者神 already present; 愛隣如自, 愛主耳錐, 財愛悪根 missing — all three added with their stored readings and glosses.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 旡`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 221 — [[characters/情|情]]

Next never-perfected character by `danayo_id` (2102 — 2101 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 青` already correct — verified via Wiktionary: 形声, semantic 心 ("heart") + phonetic 青 — "feeling, emotion, sentiment."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/感情|感情]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 061|心]] ("heart") + phonetic [[青 (char)|青]] — "feeling, emotion, sentiment"; also "love, affection"; "truth, actual circumstances."

**Body defects found**: no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (感情) was missing entirely, and one entry (情勢) was bare with no ruby; no `## Derived Characters` section existed despite a very large real ground-truth hit.

**Words cross-check** (17 total ground-truth hits — one of the largest word families surfaced in this loop): 8 already present (熱情, 情況, 衷情, 情勢 — ruby/gloss fixed, 情態, 中央情報局, 情欲, 恩情); 9 missing — 感情 (stand-in, added with annotation), 交情, 発情, 情報, 痴情, 事情, 愛情, 七情, 実情 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (9 hits via `graphemic_classification: 青` — one of the larger families surfaced in this loop): [[精]] ("spirit; essence; sperm"), [[猜]] ("to guess; suspect"), [[錆]] ("rust colored"), [[鯖]] ("mackerel"), [[清]] ("pure; clear"), [[請 (char)|請]] ("to ask; invite; request"), [[晴]] ("clear"), [[靖]] ("to pacify"), [[睛]] ("eye") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 220 — [[characters/念|念]]

Next never-perfected character by `danayo_id` (2100). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `今`, matching the Shuowen's identification of a phonetic component — but Wiktionary explicitly notes "the Old Chinese phonetics do not match," rejecting Shuowen's reading and classifying 念 as 會意: 亼 ("upside-down mouth") + 心 ("heart") — "to listen to one's heart," "to think of, recall." Corrected to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/念頭|念頭]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): 亼 ("upside-down mouth," no vault page) + [[Radical 061|心]] ("heart") — to listen to one's heart; "to think of, recall; idea, thought." Noted the rejected Shuowen phonetic theory explicitly rather than silently dropping it.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` section existed at all despite four real ground-truth hits; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (4 total ground-truth hits): all 4 missing — 念頭 (stand-in, added with annotation), 断念, 専念, 記念日 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 念`): [[捻 (char)|捻]] ("to twist") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 219 — [[characters/快 (char)|快]]

Next never-perfected character by `danayo_id` (2099). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 叏` kept after cross-checking: Wiktionary's documented spelling for the phonetic is 夬, but this vault's own derived-character family for this exact phonetic ([[訣]], [[決 (char)|決]], [[缺]] — all three confirmed via a ground-truth search) already consistently cites `叏` (a variant spelling of 夬) as their own `graphemic_classification`. Switching only 快 itself to `夬` would orphan it from its own derived family and create a vault-wide spelling inconsistency for no benefit, since 叏/夬 refer to the same historical component — kept `叏` for consistency, with the standard spelling noted in the bullet.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the sibling word [[words/愉快|愉快]]'s own stored `pos` (the stand-in word 快.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*kʷraːds): semantic [[Radical 061|心]] ("heart") + phonetic 叏 (no vault page — a variant spelling of the standard 夬, the spelling shared by 訣/決/缺) — "pleased, happy"; also "sharp; quick; forthright."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus three Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (快) was missing entirely; one entry (快楽) was bare with no ruby; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (5 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 快.md's own `characters: 快` field): 4 already present (痛快, 愉快, 爽快, 快楽 — ruby/gloss fixed); 1 missing — 快 (stand-in, added with annotation) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 叏`, excluding this page itself): [[訣]] ("secret; trick"), [[決 (char)|決]] ("to determine; decide"), [[缺]] ("incomplete; lacking") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 218 — [[characters/忘|忘]]

Next never-perfected character by `danayo_id` (2098). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 亡` already correct — verified via Wiktionary: 形声, phonetic 亡 + semantic 心 ("heart") — originally identical to 亡 ("to lose, disappear"), later gaining a perfective suffix, literally "it has disappeared (from mind)."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/忘却|忘却]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*maŋ, \*maŋs): phonetic [[亡]] (OC \*maŋ) + semantic [[Radical 061|心]] ("heart") — originally identical to 亡; "to forget."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` section existed at all despite one real ground-truth hit; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (1 total ground-truth hit): 忘却 (the `stand_in`) missing — added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (9 hits via `graphemic_classification: 亡` — one of the larger families surfaced in this loop): [[虻]] ("horsefly; gadfly"), [[芒]] ("ray; radiance"), [[茫]] ("vast; boundless; wide"), [[盲]] ("blind"), [[罔]] ("to accuse"), [[望]] ("hope"), [[妄]] ("delusion; vain"), [[忙]] ("busy"), [[岡]] ("hill; hillock") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 217 — [[characters/得|得]]

Next never-perfected character by `danayo_id` (2097). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `㝵`, implying a 形声 structure — but Wiktionary explicitly classifies 得 as 會意, with 㝵 described only as the *ancient form* (predecessor), itself composed of 貝 + 又, not a phonetic component of a phono-semantic 得. Corrected to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/獲得|獲得]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: the ancient form is 㝵 (no vault page, not listed as an alias either — a genuine "cited but never created" ancestor glyph in the same class as 攴/㐮/鷲/瘠), composed of [[貝]] ("cowry") + [[又 (char)|又]] ("hand") — to pick up a cowry, to obtain valuables. [[Radical 060|彳]] (this character's own radical) was added later to show the cowry being picked up on the road; further clerical-script corruption turned 貝 into 目 then 旦. Neither original component matches this character's own radical field, so both get direct character-page links.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (獲得) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (4 total ground-truth hits): 1 already present (取得); 3 missing — 獲得 (stand-in, added with annotation), 得点, 自得 — all added from stored fields.

**Chengyu cross-check** (2 total): 自業自得 already present; 種瓜得瓜 missing — added with its stored reading and gloss.

**Derived Characters** (1 hit via `graphemic_classification: 㝵`, excluding this page itself — the field's former value): [[碍]] ("to hinder") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 216 — [[characters/従 (char)|従]]

Next never-perfected character by `danayo_id` (2096). A genuinely tricky classification case. Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` kept, after careful checking: Wiktionary's page for 從/従 describes it as 形聲 (phonetic 从 + semantic 辵/彳), but 从 is itself only an *alias* of this very character in this vault (從/従/从 all fold into one entry, no separate 从 page exists) — so setting the field to `从` would be self-referential, the same defect class as the earlier 便/児/加 corrections. Checked 从's own independent Wiktionary entry: at that deeper layer, 从 is genuinely 會意 (two [[Radical 009|人]] walking together, "to follow"). Since the field can't validly name the character's own alias as a phonetic, and the meaning-bearing root is itself ideogrammic, kept `會意` — documenting both layers of the etymology explicitly in the bullet rather than picking one silently.

**Frontmatter**: `pos: ""` (empty string) → filled in as `動詞`, matching the sibling word [[words/従事|従事]]'s own stored `pos` (the stand-in word 従.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: documents the alias-self-reference problem explicitly (see above) rather than silently resolving it one way.

**Body defects found**: `## Notes` was empty aside from two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (従) was missing entirely (all 10 other ground-truth words were already present and correctly formatted).

**Words cross-check** (11 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 従.md's own `characters: 従` field): 10 already present and correctly formatted (従事, 従業, 従軍, 従者, 主従, 従前, 従属, 従来, 服従, 盲従); 1 missing — 従 (stand-in, added with annotation).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 従`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 215 — [[characters/待|待]]

Next never-perfected character by `danayo_id` (2095). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 寺` already correct — verified via Wiktionary: 形声, semantic 彳 ("movement, walking") + phonetic 寺 — "to wait for, to await."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/等待|等待]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 060|彳]] ("movement, walking") + phonetic [[寺]] — probably related to 等; some scholars connect it to 侍 ("to serve"). "To wait for, to await, to expect."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` section existed at all despite one real ground-truth hit; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (1 total ground-truth hit): 等待 (the `stand_in`) missing — added with annotation.

**Chengyu cross-check** (1 total): 守株待兎 already present, no changes needed.

**Derived Characters** (6 hits via `graphemic_classification: 寺`): [[詩]] ("poem"), [[侍]] ("servant; attendant"), [[時 (char)|時]] ("when"), [[特]] ("special; distinguished"), [[持 (char)|持]] ("to hold"), [[等 (char)|等]] ("etc.; rank") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 214 — [[characters/往 (char)|往]]

Next never-perfected character by `danayo_id` (2094 — 2093 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 王` already correct — verified via Wiktionary: 形声, originally 㞷/𫭠, semantic 止 ("foot") + phonetic 王, with 彳 ("to step") added later as an additional semantic element — "to go, depart, head for."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` (the base verbal sense "to go towards"; the stand-in word 往.md itself has no `pos` field, and the only sibling word 往往 stores `副用名詞`, reflecting its own specific reduplicated-adverb usage rather than the character's base sense).

**Content removed**: none.

**Graphemic bullet written from scratch**: originally 㞷/𫭠, semantic [[止]] ("foot") + phonetic [[王 (char)|王]] (OC \*ɢʷaŋ, \*ɢʷaŋs); [[Radical 060|彳]] ("to step") was later added as an additional semantic element. This character's own `radical:` field (`彳`) matches the later-added element, not either original component — both 止 and 王 get direct character-page links.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (往) was missing entirely.

**Words cross-check** (3 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 往.md's own `characters: 往` field): 1 already present (往往, ruby filled in from stored fields); 2 missing — 往 (stand-in, added with annotation), 既往 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 hits via `graphemic_classification: 王`): [[匡]] ("to correct; revise"), [[枉]] ("bent; depraved"), [[汪]] ("vast; extensive; deep"), [[旺]] ("to flourish; flourishing; prosper") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 213 — [[characters/強 (char)|強]]

Next never-perfected character by `danayo_id` (2092). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 弘` already correct — verified via Wiktionary (Shuowen): 形声, phonetic 弘 (OC \*ɡʷɯːŋ) + semantic 虫 ("insect") — the character likely originally referred to the rice weevil, phonetically borrowed for "strong, powerful."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`. `mc_id` is stored as a quoted string (`"496"`) rather than a bare number — a minor formatting inconsistency, left as-is since it isn't flagged as a defect class in the checklist and doesn't affect the value.

**Content removed**: none.

**Graphemic bullet written from scratch**: phonetic [[弘]] (OC \*ɡʷɯːŋ) + semantic [[虫]] ("insect"). This character's own `radical:` field (`弓`) matches neither etymological component — likely a Kangxi classification quirk since 弘 itself visually contains 弓 — so both components get direct character-page links rather than a Radical-page link, the same situation as 帰's 𠂤+帚 iteration earlier.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus two bare Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (強) was missing entirely; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (8 total ground-truth hits, including a discovered quoted-scalar self-citation from 強.md's own `characters: "強 (char)"` field): 4 already present in some form (勉強, 強化 — ruby fixed, 強固 — ruby fixed, 強欲); 4 missing — 強 (stand-in, added with annotation), 強迫, 剛強, 強国 — all added from stored fields.

**Chengyu cross-check** (1 total): 弱肉強食 — missing, added with its stored reading and gloss (the same chengyu already added during the recent [[characters/弱 (char)|弱]] iteration, since 強 is the other of its two cited characters).

**Derived Characters**: no ground-truth hits (`graphemic_classification: 弘`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 212 — [[characters/弱 (char)|弱]]

Next never-perfected character by `danayo_id` (2091). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 弓 ("bow") + 彡 ("hair," decoration in this case) — a decorative bow that is functionally inferior (an alternative reading takes it as depicting a shaking, worn-out bow); "weak, feeble."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the sibling word [[words/羸弱|羸弱]]'s own stored `pos` (the stand-in word 弱 itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `弓`, matching one component directly — [[Radical 057|弓]] gets the Radical-page link; [[Radical 059|彡]] (not this character's own radical, no character page, but a genuine Kangxi radical) gets the same pageless-radical fallback link established for 聿/丿-type components in recent iterations.

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (弱) was missing entirely.

**Words cross-check** (4 total ground-truth hits, including a discovered quoted-scalar self-citation from 弱.md's own `characters: "弱 (char)"` field): 1 already present (羸弱); 3 missing — 弱 (stand-in, added with annotation), 衰弱, 薄弱 — all added from stored fields.

**Chengyu cross-check** (3 total): 弱不禁風, 神経衰弱 already present; 弱肉強食 missing — added with its stored reading and gloss.

**Derived Characters** (1 hit via `graphemic_classification: 弱`): [[溺 (char)|溺]] ("to drown") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 211 — [[characters/引 (char)|引]]

Next never-perfected character by `danayo_id` (2090). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 弓 ("bow") + 丿 ("indicatory stroke") — oracle-bone forms show a slack bow with a short slant stroke marking the place of drawing the bowstring; "to pull, to draw."

**Frontmatter**: `pos: ""` (empty string) → filled in as `動詞`, matching sibling words (引出, 牽引) that both store `pos: 動詞` (an older taxonomy term still used alongside 事詞 elsewhere in the corpus; matched the immediate word family here for consistency).

**Content removed**: a malformed "### Chengyu" subsection that mixed two real chengyu (招災引禍, 引出奴家) with four ordinary 2-character words (牽引, 勾引, 引入, 丘引) — the words were moved into `## Words`, the real chengyu kept in a proper `## Chengyu` section.

**Graphemic bullet rewritten**: this character's own `radical:` field is `弓`, matching one component directly — [[Radical 057|弓]] gets the Radical-page link; [[Radical 004|丿]] (not this character's own radical, no character page, but a genuine Kangxi radical) gets the same pageless-radical fallback link used for 聿 and 丿-type components in recent iterations.

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (引) was missing entirely; one entry (引入) carried a stray leading dash inside its own gloss text.

**Words cross-check** (8 total ground-truth hits, including a discovered quoted-scalar self-citation from 引.md's own `characters: "引 (char)"` field): 6 already present in some form (引出, 引禍, 牽引, 勾引, 引入 — gloss cleaned up, 丘引 — all reclassified out of the malformed Chengyu section); 2 missing — 引 (stand-in, added with annotation), 割引 — added from stored fields.

**Chengyu cross-check** (2 total): 招災引禍, 引出奴家 — both already present but unruby'd and ungloss'd, now given their stored readings and glosses.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 引`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 210 — [[characters/弓 (char)|弓]]

Next never-perfected character by `danayo_id` (2089). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a pictograph of a bow.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` (the stand-in word 弓.md itself has no `pos` field; "bow" is unambiguously a noun).

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 象形](lookup/List%20of%20象形.md): a bow. Extended to references to arching, bending, and (in some dialects) rainbows.

**Body defects found**: two CC-initial/final links floated above `## Words` with no MC-rank bullet and no `## Notes` heading; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (弓) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (2 total ground-truth hits, including a discovered quoted-scalar self-citation from 弓.md's own `characters: "弓 (char)"` field): 1 already present (弓道); 1 missing — 弓 (stand-in, added with annotation) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 弓`): [[穹]] ("high; sky"), [[躬]] ("(emperor's) body") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 209 — [[characters/建|建]]

Next never-perfected character by `danayo_id` (2088). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 廴 + 聿 — originally a pictogram of a hand planting a pole into a base, "to build, construct."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/建設|建設]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [[Radical 054|廴]] (matches this character's own radical field) + [[Radical 129|聿]] (no vault character page but a genuine Kangxi radical, same fallback rule established for 聿 in the earlier 画 iteration) — originally a pictogram of a hand planting a pole into a base; the bottom part, though stylized as 聿, is unrelated to a writing brush. "To build, construct, erect"; "to establish, found."

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (建設) had no annotation, and one entry (建築) was bare with no ruby.

**Words cross-check** (3 total ground-truth hits): 2 already present (建設 — annotation added, 建築 — ruby/gloss fixed); 1 missing — 建国 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 建`): [[健]] ("healthy"), [[鍵 (char)|鍵]] ("key") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 208 — [[characters/店|店]]

Next never-perfected character by `danayo_id` (2087). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 占` already correct — verified via Wiktionary: 形声, semantic 广 ("house built to depend on a cliff") + phonetic 占 — "shop, store."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/商店|商店]]'s own stored `pos`. `mc_id: 0` is a real, meaningful value ("confirmed not present in the ranking," per standing policy) — phrased accordingly in the MC-rank bullet rather than treated as a gap needing a fix.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*ʔljem, \*tjems): semantic [[Radical 053|广]] ("house built to depend on a cliff") + phonetic [[占 (char)|占]] — "shop, store," also "inn."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` section existed at all despite three real ground-truth hits; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (3 total ground-truth hits): all 3 missing — 商店 (stand-in, added with annotation), 飯店, 花店 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (8 hits via `graphemic_classification: 占` — one of the larger families surfaced in this loop): [[怗]] ("observant; peaceful"), [[帖 (char)|帖]] ("invitation; card"), [[貼 (char)|貼]] ("to paste on; stick to; attach"), [[粘 (char)|粘]] ("sticky"), [[站]] ("station; site"), [[砧]] ("anvil"), [[鮎 (char)|鮎]] ("sweetfish; sheatfish"), [[点 (char)|点]] ("point") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 207 — [[characters/広 (char)|広]]

Next never-perfected character by `danayo_id` (2086). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 黃` already correct — verified via Wiktionary: 形声, semantic 广 ("shelter, structure") + phonetic 黃 (OC \*ɡʷaːŋ) — "broad, wide, extensive, vast."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the sibling word [[words/広範|広範]]'s own stored `pos` (the stand-in word 広.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*ɡʷaːŋ): semantic [[Radical 053|广]] ("shelter, structure") + phonetic [[黄 (char)|黄]] — "broad, wide, extensive, vast." 广 is listed among this character's own `aliases:` (never independently created as its own page) but is genuinely this character's own Kangxi radical, so it gets the Radical-page link rather than a character-page link — the same pattern as 干's earlier iteration, where a component both matched the radical field and lacked its own page.

**Body defects found**: `## Notes` was empty aside from what's now the graphemic bullet; two CC-initial/final links floated mid-list with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (広) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (5 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 広.md's own `characters: 広` field): 3 already present (広範, 広野 — ruby/gloss fixed, 広土); 2 missing — 広 (stand-in, added with annotation), 広場 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 黃`/`黄`): [[横]] ("crossing horizontally; across laterally") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 206 — [[characters/平|平]]

Next never-perfected character by `danayo_id` (2085). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` kept as-is: Wiktionary documents genuinely uncertain etymology with no clear primary reading — proposed theories include a pictogram of waterweed on water, a pictogram of a balance scale (both 象形), and an ideogrammic compound of 八 + 亏 (會意). Since the vault's own pre-existing choice already matches a legitimate 象形 theory, kept it and documented the dispute.

**Frontmatter**: already correct (`pos: 性詞`, `mc_id: 131` verified against `CC 0000.md`).

**Content removed**: a markdown-style link (`[平常](/words/平常.md)`) converted to a wikilink; a floating CC-initial/final pair sitting mid-list between Words entries.

**Graphemic bullet written from scratch**: documented all three competing scholarly theories per Wiktionary, following the vault's pre-existing 象形 choice as the working classification.

**Body defects found**: `## Notes` was empty aside from what's now the graphemic bullet; two CC-initial/final links floated mid-list with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (水平) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (21 total ground-truth hits — the largest word family surfaced in this loop so far): 10 already present in some form (平方, 扁平, 平常, 平日, 平静, 平坦, 平板, 臥平, 公平, 太平 — all reformatted with ruby/gloss); 11 missing — 水平 (stand-in, added with annotation), 平均, 平凡, 平成, 平年, 不平, 平安, 地平線, 和平, 平穏, 平等 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 平`): [[坪 (char)|坪]] ("level ground; 36 square shaku; pyeong"), [[評]] ("to evaluate"), [[苹]] ("apple; duckweed") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 205 — [[characters/干|干]]

Next never-perfected character by `danayo_id` (2084 — 2083 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct and already well-documented in the page's own pre-existing bullet, including an explicit note distinguishing 干's own "shield" identity from [[characters/乾 (char)|乾]] and [[幹]], which only borrow its glyph in Simplified Chinese — no changes needed there.

**Frontmatter**: `stand_in:` was blank — a required field this loop hasn't caught blank before. Set to `干渉`, since no independent word file `干.md` exists and 干渉's own stored gloss ("interfere; intervene") matches one of the character's two listed `english` senses ("shield, interfere") exactly.

**Content removed**: a non-canonical relative path (`../lookup/List of 象形`), corrected to the canonical root-relative form.

**Graphemic bullet**: kept verbatim aside from the path fix.

**Body defects found**: two CC-initial/final links floating with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; no stand-in annotation on any Words entry; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (6 total ground-truth hits): all 6 already present (若干, 天干, 十干, 干戈, 干渉 — stand-in annotation added, 干犯) — no missing entries, just the annotation fix.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 hits via `graphemic_classification: 干` — one of the larger families surfaced in this loop): [[旱]] ("drought"), [[軒]] ("flats"), [[肝]] ("liver"), [[竿]] ("bamboo pole"), [[杆 (char)|杆]] ("rod"), [[汗 (char)|汗]] ("sweat"), [[刊 (char)|刊]] ("publication; periodical") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 204 — [[characters/帰|帰]]

Next never-perfected character by `danayo_id` (2082). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `堆` — a character that appears nowhere in 歸/帰's actual etymology. Verified via Wiktionary that 歸 is 會意: 𠂤 ("ancient form of 師, troops") + [[帚]] ("broom; sweep") — to eradicate the enemy and return (Shuowen considers 𠂤 a phonetic, but the primary listed classification is 會意) — corrected to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/回帰|回帰]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 𠂤 (no vault page) + [[帚]] ("broom; sweep") — to eradicate the enemy and return (an alternative analysis reads the second component as 止 "stop" + 方 "peripheral tribes" ligature, "to cease enmity and submit"); Shuowen considers 𠂤 a phonetic. "To return, revert; to submit." Neither component matches this character's own `radical:` field (`巾`), so 帚 (has its own page) gets a direct character-page link and 𠂤 (no page) is cited as bare text.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus four bare Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (回帰) was missing entirely; no `## Chengyu` section existed despite two real ground-truth hits.

**Words cross-check** (6 total ground-truth hits): 4 already present (帰還, 帰納, 帰順, 帰結 — all reformatted with ruby/gloss); 2 missing — 回帰 (stand-in, added with annotation), 復帰 — added from stored fields.

**Chengyu cross-check** (2 total): 汗食帰泥, 帰塵帰土 — both missing, added with their stored readings and glosses.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 帰`/`歸`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 203 — [[characters/席|席]]

Next never-perfected character by `danayo_id` (2081). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `庶`, matching only the Shuowen's secondary reinterpretation of the corrupted small-seal form — Wiktionary's primary classification is 象形, a pictogram of "a woven mat with ornament," with 石 (later corrupted into 巾) added as a phonetic afterward. Corrected to `象形` per this loop's standing rule of following Wiktionary's primary listing, with the Shuowen alternate reading kept in the bullet for context.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/坐席|坐席]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 象形](lookup/List%20of%20象形.md): a woven mat with ornament. Later a phonetic 石 (OC \*djaɡ) was added and the image of the mat corrupted into [[Radical 050|巾]] ("cloth"); the Shuowen reinterprets the small-seal form as an abbreviated phonetic 庶 + semantic 巾. "Seat, mat," extended to "rank, place."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (坐席) was missing entirely.

**Words cross-check** (4 total ground-truth hits): 1 already present (缺席); 3 missing — 坐席 (stand-in, added with annotation), 出席, 主席 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 席`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 202 — [[characters/希|希]]

Next never-perfected character by `danayo_id` (2080). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was invalid: stored as `爻`, as if 希 were 形声 with 爻 as its phonetic — but Wiktionary classifies 希 as 會意 (originally 𢁫: 爻 + 巾, "cloth"), not 形声, so a component name is the wrong kind of value here — corrected to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/希有|希有]]'s own stored `pos`.

**Content removed**: a cryptic, undocumented fragment (`冀=C#1024`) with no clear meaning or context, at the top of `## Notes`.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): originally 𢁫, 爻 (no vault page) + [[Radical 050|巾]] ("cloth") — a finely-woven pattern; "thin, sparse," extended to "to hope, to expect."

**Body defects found**: `mc_id: 3110` is mirrored under the alias 稀 rather than 希 itself in `CC 3000.md` — noted explicitly rather than left unexplained; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (希有) used a markdown-style link with no annotation; one entry (希薄) carried an unexplained "not 稀薄" fragment, clarified into a proper parenthetical about the alias-vs-parent spelling convention.

**Words cross-check** (7 total ground-truth hits): 6 already present in some form (希有 — converted to wikilink with annotation, 希望, 希釈, 希少, 希薄 — clarified, 古希); 1 missing — 希州 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 希`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 201 — [[characters/布|布]]

Next never-perfected character by `danayo_id` (2079 — 2078 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 父` already correct — verified via Wiktionary: 形声, phonetic 父 + semantic 巾 ("kerchief") — "cloth, textiles."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/亜麻布|亜麻布]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*paʔ, \*baʔ): phonetic [[父]] + semantic [[Radical 050|巾]] ("kerchief") — "cloth, textiles"; also "to announce, proclaim; to spread, deploy."

**Body defects found**: `## Notes` held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (亜麻布) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (8 total ground-truth hits): 3 already present (頒布, 分布, 昆布); 5 missing — 亜麻布 (stand-in, added with annotation), 瀑布, 布帛, 麻布, 散布 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 父`): [[斧]] ("axe"), [[釜]] ("kettle; cauldron"), [[付]] ("to pay") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 200 — [[characters/島 (char)|島]]

Next never-perfected character by `danayo_id` (2077). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 鳥` already correct — verified via Wiktionary: 形声, phonetic 鳥 (OC \*tɯːwʔ) + semantic 山 ("mountain") — "island."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞` (the stand-in word 島.md itself has no `pos` field; "island" is unambiguously a noun).

**Content removed**: a broken non-canonical relative path (`../words/島屿`), corrected to a proper wikilink.

**Graphemic bullet written from scratch**: 形声: phonetic [[鳥 (char)|鳥]] (OC \*tɯːwʔ) + semantic [[Radical 046|山]] ("mountain") — "island."

**Body defects found**: two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (島) was missing entirely; `mc_id: 4188` falls beyond the vault's mirrored ~4000-entry CC range, so it's trusted as-is per standing policy rather than left unverified without comment.

**Words cross-check** (7 total ground-truth hits, including a discovered quoted-scalar self-citation from 島.md's own `characters: "島 (char)"` field): 1 already present (島屿, fixed link); 6 missing — 島 (stand-in, added with annotation), 関島, 半島, 列島, 火山島, 群島 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 鳥`): [[鵰 (char)|鵰]] ("eagle; vulture") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 199 — [[characters/岩|岩]]

Next never-perfected character by `danayo_id` (2076). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `象形`, but Wiktionary classifies 岩 as 會意 — [[Radical 046|山]] ("hill") + [[石 (char)|石]] ("rock") — a rocky cliff or stone formation; the page's own pre-existing prose bullet had already correctly identified these two components, it just wasn't reflected in the field. Corrected to `會意`.

**Frontmatter**: already correct (`pos: 名詞`). `mc_id: 5025` is beyond the vault's mirrored ~4000-entry CC range — trusted as-is per standing policy, explicitly noted in the MC-rank bullet rather than silently verified against a nonexistent lookup line.

**Content removed**: none.

**Graphemic bullet rewritten**: [List of 会意](lookup/List%20of%20会意.md): [[Radical 046|山]] ("hill") + [[石 (char)|石]] ("rock") — a rocky cliff or stone formation. Originally written 巖, a 形声 compound (Han dynasty); the simplified 岩 first appeared in clerical script and became the standard form.

**Body defects found**: `# Notes` was the wrong heading level and held only a bare-linked components note with no classification or gloss; two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` section existed at all despite three real ground-truth hits.

**Words cross-check** (3 total ground-truth hits): all 3 missing — 岩石 (stand-in, added with annotation), 玄武岩, 溶岩 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 岩`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 198 — [[characters/展|展]]

Next never-perfected character by `danayo_id` (2075 — 2074 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, but Wiktionary classifies 展 as 形声 — semantic [[Radical 044|尸]] ("corpse; body") + an abbreviated phonetic 𧝑 (variant 𧝣), "fine red silk clothes" (one of the six garments worn by the queen in the Rites of Zhou) carrying connotations of "opening, extending" — corrected the field to `𧝑`, an obscure CJK Extension B character with no vault page, following the checklist rule to store the actual phonetic component regardless of whether it can be linked.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the sibling word [[words/展示|展示]]'s own stored `pos` (the stand-in word 伸展 itself has no `pos` field).

**Content removed**: none of substance — just reordered.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 044|尸]] ("corpse; body") + abbreviated phonetic 𧝑 (variant 𧝣, no vault page) — "to unfold, stretch, extend."

**Body defects found**: `## Words` appeared before `# Notes`, which itself held nothing but two floating CC-initial/final links plus one further Words entry; reordered to canonical sequence; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (伸展) was missing entirely, and one entry (展示) was bare `[[link]]` with no ruby.

**Words cross-check** (5 total ground-truth hits): 4 already present (発展, 展翅, 展覧, 展示 — ruby/gloss fixed); 1 missing — 伸展 (stand-in, added with annotation) — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 展`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 197 — [[characters/就 (char)|就]]

Next never-perfected character by `danayo_id` (2073). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `尤`, implying a 形声 structure — but Wiktionary explicitly states 就 has no single phonetic component and is 會意, not 形声: originally 𫢁 (享 "temple" + 京 "tower," "to sacrifice at a high place"), with 享 later omitted and 尤 ("especially") added — corrected the field to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `修飾語`, a defensible choice given 就's modal/aspectual senses ("about to," "then," "only") — no directly reusable `pos` value existed on the stand-in word 就.md itself (blank).

**Discovered but not fixed — character-vs-word `注音` divergence**: this character's own `注音` is `ㄑ⺢ㄧ` (the primary "about, let" sense), but its stand-in word [[words/就|就]], and all three 借代字-related compounds (就鳥, 禿就, 海就), store `注音: ㄐㄨㄛ` / derivatives thereof — the alias-borrowed "eagle/vulture" sense's pronunciation, not the character's own. Flagged per established policy rather than silently resolved; the Words entries here use each word's own stored reading, as the verification script requires.

**Content removed**: none — the pre-existing "借代字" (borrowed-character) subsection was preserved as an explanatory Notes bullet rather than deleted, since it correctly explains a genuine borrowed-usage relationship already reflected in the `aliases:` field (鷲/鹫).

**Graphemic bullet written from scratch**: originally 𫢁, combining 享 ("temple") + [[京]] ("tower") — "to sacrifice at a high place." During the Warring States period, 享 was omitted and [[尤]] ("especially, even more") added — "high, to go to a higher place"; extended to "to approach, reach; to undertake; to succeed." Neither 京 nor 尤 is this character's own radical (`尢`, only a near-variant of 尤), so both get direct character-page links rather than a Radical-page link.

**Body defects found**: two CC-initial/final links floating with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (就) was missing entirely; the two borrowed-usage words (就鳥, 禿就) were arrow-noted rather than proper Words entries.

**Words cross-check** (4 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 就.md's own `characters: 就 (char)` field): 2 already present as arrow-notes (就鳥, 禿就 — converted to proper Words entries); 2 missing — 就 (stand-in, added with annotation), 海就 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 就`): [[蹴 (char)|蹴]] ("to kick") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 196 — [[characters/将 (char)|将]]

Next never-perfected character by `danayo_id` (2072). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, but Wiktionary classifies 將/将 as 形声 — phonetic 爿 + semantic ⺼ ("meat") + semantic 寸 ("hand") — "to offer meat as tribute," extended to "to take, to hold" and eventually "will, be going to" — corrected to `爿`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `修飾語`, matching the stand-in word [[words/将|将]]'s own stored `pos` — 将 is one of the vault's Tense modifiers per [[grammar/文法 - 97品詞]] (已/未/将/中).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*t͡saŋ, \*t͡saŋs): phonetic 爿 (no vault page) + semantic ⺼ ("meat," no vault page) + semantic [[Radical 041|寸]] ("hand") — to offer meat as tribute (爿 also suggesting a cutting board or sacrificial table); extended to "to take, to hold, to carry," and eventually "will, be going to." Kept the pre-existing note about the alias 漿 ("thick fluid").

**Body defects found**: two CC-initial/final links floated mid-list with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (将) was missing entirely, and two entries (将軍, 将兵) were bare `[[link]]` with no ruby.

**Words cross-check** (9 total ground-truth hits): 4 already present (将軍, 将兵 — ruby/gloss fixed, 将来, 将然); 5 missing — 将 (stand-in, added with annotation), 武将, 将棋, 将校, 将帥 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 爿`): [[壮]] ("bulky; huge"), [[状]] ("form; shape") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 195 — [[characters/察|察]]

Next never-perfected character by `danayo_id` (2071). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 祭` already correct — verified via Wiktionary: 形声, semantic [[Radical 040|宀]] ("roof") + phonetic 祭 — "to sort out differences," "to examine, investigate."

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word [[words/考察|考察]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 040|宀]] ("roof") + phonetic [[祭]] — "to sort out differences"; "to examine, to investigate, to notice."

**Body defects found**: `## Words` appeared before `# Notes`, which itself held nothing but two floating CC-initial/final links; reordered to the canonical Notes → Words sequence; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (考察) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (2 total ground-truth hits): 1 already present (観察); 1 missing — 考察 (stand-in, added with annotation) — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 祭`): [[際 (char)|際]] ("border; occasion"), [[蔡]] ("tortoise") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 194 — [[characters/害|害]]

Next never-perfected character by `danayo_id` (2070). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` kept as-is: Wiktionary documents genuine scholarly disagreement with no clear primary reading — He Linyi proposes 指事 (a spear + a distinguishing mark), Li Xueqin and the Shuowen propose 形聲, Guo Moruo and Dai Jiaxiang propose 象形 (the ancient form of 蓋, "lid, cover"), and Gao Hongying proposes 假借 (originally the character for 桷, "rafters," borrowed for sound). Since the vault's own pre-existing choice (象形) already matches one of these legitimate scholarly theories, kept it and documented the dispute rather than arbitrarily picking a different one.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/残害|残害]]'s own stored `pos`.

**Content removed**: a malformed "### Derived Characters" subsection with a markdown-style link, folded into a proper `## Derived Characters` section with the other two real ground-truth hits added alongside it.

**Graphemic bullet written from scratch**: documented all four competing scholarly theories per Wiktionary, following the vault's pre-existing 象形 choice as the working classification.

**Body defects found**: `## Notes` held only the malformed Derived Characters fragment; two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (残害) was missing entirely.

**Words cross-check** (6 total ground-truth hits): 1 already present (妨害); 5 missing — 残害 (stand-in, added with annotation), 迫害, 傷害, 災害, 禍害 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 害`): [[轄 (char)|轄]] ("linchpin of a wheel; control"), [[割 (char)|割]] ("to cut; divide" — already partially present, reformatted), [[憲]] ("constitution; statute; law") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 193 — [[characters/室|室]]

Next never-perfected character by `danayo_id` (2069). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 至` already correct — verified via Wiktionary: 形声, semantic [[Radical 040|宀]] ("roof") + phonetic 至 — "a roof over this exact spot," "room, chamber."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the sibling word [[words/教室|教室]]'s own stored `pos` (the stand-in word 房室 itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*hli[t]s, \*tjiɡs): semantic [[Radical 040|宀]] ("roof") + phonetic [[至 (char)|至]] — a residence is a place marked by an arrow on the ground, so the phonetic also adds meaning; "a roof over this exact spot" — "room, chamber," extended to "family, household."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (房室) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (6 total ground-truth hits): 2 already present (教室, 室町); 4 missing — 房室 (stand-in, added with annotation), 休息室, 浴室, 辦公室 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 hits via `graphemic_classification: 至`): [[致 (char)|致]] ("to cause"), [[窒]] ("to suffocate; choke"), [[姪]] ("niece"), [[蛭 (char)|蛭]] ("leech") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 192 — [[characters/定|定]]

Next never-perfected character by `danayo_id` (2068). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 正` already correct — verified via Wiktionary: 形声, semantic [[Radical 040|宀]] ("roof") + phonetic 正 — "stable, fixed"; "to decide, determine, settle."

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 250` verified against `CC 0000.md`).

**Content removed**: two asterisk-bulleted entries (一定, 確定), non-canonical Markdown list syntax for this vault, converted to standard hyphen bullets with ruby/gloss.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 040|宀]] ("roof") + phonetic [[正 (char)|正]] — "stable, fixed"; "to decide, to determine, to settle."

**Body defects found**: `## Notes` was completely empty; two CC-initial/final links floated at the very end of the page with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the asterisk-bulleted entries above had no ruby; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (19 total ground-truth hits — one of the largest word families surfaced in this loop): 12 already present in some form (決定 stand-in already annotated; 一定, 確定 — converted from asterisk bullets and ruby'd; 定義域, 定義, 仮定, 鑑定, 既定, 規定, 協定, 不定, 否定 — ruby/gloss filled in from stored fields); 7 missing — 無定河, 予定, 定位, 限定詞, 限定, 安定, 議定 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 正`): [[症]] ("disease"), [[整 (char)|整]] ("orderly; neat; tidy"), [[鉦]] ("marching gong"), [[征]] ("to conquer"), [[政]] ("government; political affairs"), [[証]] ("to prove; confirm; verify") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 191 — [[characters/官|官]]

Next never-perfected character by `danayo_id` (2067). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[Radical 040|宀]] ("roof") + 𠂤 — multiple rooms under a roof, an official building; "official."

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 177` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): [[Radical 040|宀]] ("roof") + 𠂤 ("multiple rooms," no vault page) — multiple rooms under a roof, an official building; extended to "official."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (官人) was missing entirely; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (9 total ground-truth hits): 5 already present (官僚主義, 官僚, 官庁, 五官, 九官鳥); 4 missing — 官人 (stand-in, added with annotation), 官吏, 貪官, 罷官 — all added from stored fields.

**Chengyu cross-check** (1 total): 貪官汚吏 — missing, added with its stored reading and gloss.

**Derived Characters** (4 hits via `graphemic_classification: 官`): [[館]] ("hall; building; wing"), [[菅]] ("coarse grass"), [[管]] ("pipe; tube"), [[棺 (char)|棺]] ("coffin") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 190 — [[characters/完|完]]

Next never-perfected character by `danayo_id` (2066). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 元` already correct — verified via Wiktionary: 形声, semantic [[Radical 040|宀]] ("roof") + phonetic 元 — "whole, complete, intact."

**Frontmatter**: already correct (`pos: "事詞"`, `mc_id: 1467` verified against `CC 1000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*ɦŋoːn): semantic [[Radical 040|宀]] ("roof") + phonetic [[元]] (OC \*ŋon) — "whole, complete, intact"; "to end, to finish."

**Body defects found**: `## Notes` held nothing but two floating CC-initial/final links plus one bare Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (完成) was missing entirely; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (4 total ground-truth hits): 3 already present (完全 — ruby/gloss fixed, 完璧, 完了); 1 missing — 完成 (stand-in, added with annotation) — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 hits via `graphemic_classification: 元`): [[頑]] ("stubborn"), [[玩]] ("toy"), [[翫]] ("to slack off"), [[冠]] ("crown"), [[阮]] ("moon lute") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 189 — [[characters/守|守]]

Next never-perfected character by `danayo_id` (2065). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[Radical 040|宀]] ("roof, building") + [[寸 (char)|寸]] ("hand") — a hand guarding a roofed structure; "to guard, keep, defend."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/守衛|守衛]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): [[Radical 040|宀]] ("roof, building") + [[寸 (char)|寸]] ("hand") — a hand guarding a roofed structure; "to guard, keep, defend."

**Body defects found**: `## Notes` held nothing but two floating CC-initial/final links plus three Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (守衛) was missing entirely, and one entry (守戍) was bare `[[link]]` with no ruby; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (5 total ground-truth hits): 3 already present (守護, 守戍 — ruby/gloss fixed, 防守); 2 missing — 守衛 (stand-in, added with annotation), 遵守 — added from stored fields.

**Chengyu cross-check** (1 total): 守株待兎 already present, no changes needed.

**Derived Characters** (1 hit via `graphemic_classification: 守`): [[狩]] ("to hunt") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 188 — [[characters/好 (char)|好]]

Next never-perfected character by `danayo_id` (2064). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[Radical 038|女]] ("woman") + [[子 (char)|子]] ("child") — it was good for a woman to have a child, extended to mutual mother-child affection and eventually "good."

**Frontmatter**: already correct (`pos: "性詞"`, `mc_id: 268` verified against `CC 0000.md`).

**Content removed**: a redundant "Components: [[女]], [[子]]" line duplicating the graphemic bullet below it; a markdown-style link (`[女](Radical 038)`) converted to a proper wikilink.

**Graphemic bullet rewritten**: [List of 会意](lookup/List%20of%20会意.md): [[Radical 038|女]] ("woman") + [[子 (char)|子]] ("child") — it was good for a woman to have a child; extended to the mutual affection between mother and child, and eventually "good."

**Body defects found**: two CC-initial/final links floating with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` section existed at all despite four real ground-truth hits.

**Words cross-check** (4 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 好.md's own `characters: 好` field): all 4 missing — 好 (stand-in, added with annotation), 良好, 愛好, 友好 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 好`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 187 — [[characters/失|失]]

Next never-perfected character by `danayo_id` (2063). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `手`, matching only the Shuowen's alternative 會意 reading (手 + 乙, "something falling from a hand") — but Wiktionary's primary classification is 象形, a pictogram of "a footprint of someone who has fallen, surrounded by drops of blood." Corrected to `象形`, per this loop's standing rule of following Wiktionary's primary listing, with the Shuowen alternative noted in the bullet rather than discarded.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/滅失|滅失]]'s own stored `pos`.

**Content removed**: a compressed single-line SKIP/Stroke/syllable/CC bullet, expanded into the canonical four-bullet structure.

**Graphemic bullet written from scratch**: [List of 象形](lookup/List%20of%20象形.md): a footprint of someone who has fallen, surrounded by drops of blood; "to lose." (Shuowen's alternative 會意 reading — [[Radical 064|手]] + 乙 — noted parenthetically.)

**Body defects found**: the MC-rank/CC-initial-final bullet was compressed onto one line with the SKIP/Stroke bullet, non-canonical for this loop's four-bullet format; no Levels bullet existed; the stand-in Words entry (滅失) was missing entirely, and two entries (失業, 失礼) were bare `[[link]]` with no ruby.

**Words cross-check** (8 total ground-truth hits): 5 already present (自失, 失敗, 失業 — ruby/gloss fixed, 失礼 — ruby/gloss fixed, 損失); 3 missing — 滅失 (stand-in, added with annotation), 失禁, 喪失 — added from stored fields.

**Chengyu cross-check** (2 total): 因小失大 already present; 茫然自失 missing — added with its stored reading and gloss.

**Derived Characters** (3 hits via `graphemic_classification: 失`, unaffected by the field correction above since these three genuinely store the literal string `失`, not `手`): [[秩]] ("regularity; order"), [[跌]] ("to fall down"), [[迭]] ("to alternate; change") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 186 — [[characters/変 (char)|変]]

Next never-perfected character by `danayo_id` (2062). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 䜌` already correct — verified via Wiktionary: 形声, phonetic 䜌 + semantic 攴, "to change, to transform."

**Frontmatter**: already correct (`pos: 性詞`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*prons): phonetic 䜌 (no vault page) + semantic 攴 (simplified to [[Radical 034|夂]] in the shinjitai reform, the same pattern as 云 replacing 專 in [[characters/伝|伝]] earlier in this loop) — "to change, to transform; to become, to turn into." Confirmed 夂 is indeed 変's own radical via Radical 034's own lookup page, which already lists 変 among its used characters.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (変) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (5 total ground-truth hits, including a discovered quoted-scalar self-citation from 変.md's own `characters: "変 (char)"` field): 3 already present (改変, 変成, 変動); 2 missing — 変 (stand-in, added with annotation), 変化 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 hits via `graphemic_classification: 䜌`): [[弯]] ("to bend; curve"), [[鵉]] ("luan"), [[恋 (char)|恋]] ("romance; romantic love"), [[蛮]] ("barbarian"), [[栾]] ("Koelreuteria paniculata") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 185 — [[characters/士 (char)|士]]

Next never-perfected character by `danayo_id` (2061). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` already correct — verified via Wiktionary: a pictograph of a war axe, later "soldier," then "officer, intellectual" — the page's own pre-existing bullet was already an accurate, well-sourced match, no rewrite needed.

**Frontmatter**: `pos` was pre-filled but wrong — stored as `事詞` (an eventive/transitive verb category), but "scholar" is a noun; corrected to `名詞`, matching sibling words (博士, 国士) that both store `pos: 名詞`.

**Content removed**: a stray floating fragment, the bare digits `1194`, sitting at the top of `## Notes` with no context (possibly a mis-pasted `mc_id` from another character, since this page's own `mc_id` is 104, not 1194).

**Graphemic bullet**: kept verbatim, no changes needed.

**Body defects found**: two CC-initial/final links were floating between `## Chengyu` and `## Words` with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (士) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (9 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 士.md's own `characters: 士` field): 4 already present (君士坦丁堡, 武士道, 博士, 瑞士); 5 missing — 士 (stand-in, added with annotation), 兵士, 国士, 武士, 紳士 — all added from stored fields.

**Chengyu cross-check** (2 total): both already present (国士無双, 選士唯賢), no changes needed.

**Derived Characters** (2 hits via `graphemic_classification: 士`): [[寺]] ("temple (Buddhist)"), [[志]] ("will; intention") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 184 — [[characters/増|増]]

Next never-perfected character by `danayo_id` (2060). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 曽` already correct — verified via Wiktionary (checked under the variant form 增, since 曽/曾 are variant glyphs of the same phonetic and the vault's own character page for this component is filed under 曽): 形声, semantic 土 ("earth") + phonetic 曾/曽 — "things grow in the earth, to build from earth," "to increase."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/増加|増加]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 032|土]] ("earth") + phonetic [[曽 (char)|曽]] — things grow in the earth, to build from earth; "to increase, expand, gain."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (増加) had no annotation; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (1 total ground-truth hit): 増加 (the `stand_in`) — annotation added, no changes otherwise.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 hits via `graphemic_classification: 曽`): [[僧]] ("priest; monk; bonze"), [[層 (char)|層]] ("stratum"), [[贈]] ("to present; bestow"), [[噌]] ("whoosh"), [[憎]] ("to hate") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 183 — [[characters/報 (char)|報]]

Next never-perfected character by `danayo_id` (2059). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 㚔 ("handcuffs") + 𠬝 ("to subdue") — to convict, to punish; extended to "to report, announce." This character's own `radical:` field (`土`) matches neither etymological component — a dictionary-classification quirk in the same vein as 医's own radical/etymology mismatch a few iterations ago — so neither component gets a Radical-page link; both 㚔 and 𠬝 also have no vault character pages, so both are cited as bare text (converted from broken wikilinks that pointed nowhere).

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching sibling words (報答, 報償, 報道) that all store `pos: 事詞` for the "to report/repay" transitive sense (the stand-in word 報 itself has no `pos` field).

**Content removed**: two broken wikilinks (`[[㚔]]`, `[[𠬝]]`) pointing at nonexistent pages, converted to bare text per the established convention for cited-but-never-created components.

**Graphemic bullet rewritten**: kept the correct 会意 analysis, fixed the broken links, added a gloss extension to "to report, to announce."

**Body defects found**: two CC-initial/final links floating at the very end of the page with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; seven Words entries (報酬, 報答, 報応, 報償, 情報, 日報, 飛報) were bare `[[link]]` with no ruby; the stand-in Words entry (報) was missing entirely; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (13 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 報.md's own `characters: 報` field): 8 already present in some form (報酬, 報答, 報応, 報償, 情報, 日報, 飛報 — all reformatted with ruby/gloss; 中央情報局 already correct); 5 missing — 報 (stand-in, added with annotation), 報告, 報知, 報道, 画報 — all added from stored fields.

**Chengyu cross-check** (1 total): 因果報応 — missing, added with its stored reading and gloss.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 報`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 182 — [[characters/堂|堂]]

Next never-perfected character by `danayo_id` (2058). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 尚` already correct — verified via Wiktionary: 形声, phonetic 尚 + semantic 土 ("earth") — "main room of a house," "hall, chamber."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/会堂|会堂]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*djaŋ, \*djaŋs): phonetic [[尚 (char)|尚]] + semantic [[Radical 032|土]] ("earth") — "main room of a house"; "hall, chamber."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (会堂) was missing entirely; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (6 total ground-truth hits): 2 already present (教堂, 大教堂); 4 missing — 会堂 (stand-in, added with annotation), 廟堂, 学堂, 食堂 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 尚`): [[嘗]] ("to taste; experience"), [[当 (char)|当]] ("while"), [[常]] ("common; normal; frequent"), [[掌]] ("palm; sole"), [[賞 (char)|賞]] ("reward"), [[党]] ("political party") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 181 — [[characters/基|基]]

Next never-perfected character by `danayo_id` (2057). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 其` already correct — verified via Wiktionary: 形声, semantic 土 ("earth") + phonetic 其 — "a foundation of earth."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/基本|基本]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 032|土]] ("earth") + phonetic [[其 (char)|其]] — "a foundation of earth"; "foundation, base."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (基本) had no annotation; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (8 total ground-truth hits): 6 already present (基本 — annotation added, 基礎, 巴基斯坦, 基督教, 基金, 基準); 2 missing — 基督, 基盤 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 hits via `graphemic_classification: 其`): [[麒]] ("qilin"), [[期 (char)|期]] ("period; time; season"), [[斯]] ("this; then"), [[棋]] ("chess; strategy game"), [[碁]] ("Go (game)"), [[欺]] ("to deceive; trick"), [[旗]] ("banner; flag") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 180 — [[characters/城|城]]

Next never-perfected character by `danayo_id` (2056). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 成` already correct — verified via Wiktionary: 形声, semantic 土 ("soil") + phonetic 成 — "city walls were originally made of stamped earth."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching sibling words (城市, 金城) that store `pos: 名詞` (the stand-in word 城郭 itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet**: already correct and complete from a prior partial pass, no changes needed.

**Body defects found**: several Words entries (京城, 城郭, 金城, 紫禁城) were bare `[[link]]` or missing ruby/gloss entirely; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both; the stand-in Words entry (城郭) had no annotation.

**Words cross-check** (6 total ground-truth hits): all 6 already present in some form (城郭 — annotation added; 京城, 金城, 紫禁城 — ruby/gloss filled in from stored fields; 城市, 獅城 already correct).

**Chengyu cross-check** (1 total): 金城湯池 — missing, added with its stored reading and gloss.

**Derived Characters** (2 hits via `graphemic_classification: 成`): [[誠]] ("sincere; honest"), [[盛]] ("flourish; full") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 179 — [[characters/坐 (char)|坐]]

Next never-perfected character by `danayo_id` (2055). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `指事`, but Wiktionary classifies 坐 as 會意 — [[留 (char)|留]] ("to stay") + [[Radical 032|土]] ("ground") — to remain stationary on the ground, "to sit" — corrected accordingly. Noting a competing folk-etymology found in the vault itself: the word [[words/坐位|坐位]]'s own prose calls 坐 "a 指事 character depicting two figures (人) seated on the ground (土)" — a plausible-sounding but Wiktionary-unsupported alternative theory; the field now follows Wiktionary's authoritative 會意 classification per this loop's standing rule, and 坐位's own prose is left untouched (out of scope for this iteration, and not miscategorized enough to justify a cross-page edit here).

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞` — "to sit" is intransitive/stative rather than object-taking, matching the vault's [[grammar/文法 - 97品詞]] Statives category (no sibling word's `pos` field could be borrowed directly, since 坐.md itself has none and its derived nouns 坐位/坐席 store `名詞` for their own, different part of speech).

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): [[留 (char)|留]] ("to stay") + [[Radical 032|土]] ("ground") — to remain stationary on the ground; "to sit."

**Body defects found**: `# Notes` was the wrong heading level; two CC-initial/final links floated with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; one Words-style entry (坐席) was misplaced inside `## Notes`; the stand-in Words entry (坐) was missing entirely; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (5 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 坐.md's own `characters: 坐` field): 2 already present (坐位, 坐席 — relocated into Words and ruby'd); 3 missing — 坐 (stand-in, added with annotation), 結加夫坐, 星坐 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 坐`): [[挫]] ("failure; setback; frustration") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 178 — [[characters/在 (char)|在]]

Next never-perfected character by `danayo_id` (2054). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 才` already correct — verified via Wiktionary: 形声, phonetic 才 + semantic 士 (later corrupted into 土, "earth") — matches the field, though the page's own pre-existing bullet had the semantic/phonetic roles backwards and cited the wrong (uncorrupted) semantic component 士 as if it were the modern one.

**Frontmatter**: `pos: ""` (empty string) → filled in as `系詞`, since 在 is one of the vault's closed set of six copula verbs per [[grammar/文法 - 97品詞]] (是/非/有/無/在/莫) — confirmed by the word file's own stored `pos: 系詞`/`品詞: 系詞`.

**Content removed**: a markdown-style link (`[現在](/words/現在.md)`) replaced with a proper wikilink.

**Graphemic bullet rewritten**: 形声 (OC \*zlɯːʔ, \*zlɯːs): phonetic [[才]] + semantic [[士 (char)|士]] (later corrupted into [[Radical 032|土]], "earth") — "to exist; to be present; to be at, to be located." This character's own `radical:` field is `土` (the corrupted modern form), which gets the Radical-page link; [[士 (char)|士]] (the original, uncorrupted semantic component, not this character's own radical field value, but has its own page) gets a direct character-page link.

**Body defects found**: two CC-initial/final links floating at the very end of the page with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (在) was missing entirely; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (7 total ground-truth hits): 2 already present (現在 — relinked as wikilink, 在位); 5 missing — 在 (stand-in, added with annotation), 潜在, 存在, 所在, 自在 — all added from stored fields.

**Chengyu cross-check** (1 total): 自由自在 — missing, added with its stored reading and gloss.

**Derived Characters** (3 hits via `graphemic_classification: 才`, excluding this page itself): [[財]] ("wealth"), [[栽]] ("to plant; cultivate"), [[材]] ("material; stuff; talent") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 177 — [[characters/固|固]]

Next never-perfected character by `danayo_id` (2053). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, but Wiktionary classifies 固 as 形声 — semantic [[Radical 031|囗]] ("enclosure") + phonetic [[古]] (OC \*kaːʔ) — corrected to `古`. Fittingly, 古's own iteration (170) had already noted that 古 "represents the original form of 固" from the other direction.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/強固|強固]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 031|囗]] ("enclosure") + phonetic [[古]] (OC \*kaːʔ) — something enclosed and hardened; "firm, solid, strong," extended to "stubborn."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (強固) was missing entirely.

**Words cross-check** (4 total ground-truth hits): 2 already present (固執 — ruby/gloss fixed, 頑固); 2 missing — 強固 (stand-in, added with annotation), 固有 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 固`): [[錮 (char)|錮]] ("obstinate"), [[個 (char)|個]] ("individual") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 176 — [[characters/図|図]]

Next never-perfected character by `danayo_id` (2052). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `指事`, but Wiktionary classifies 圖/図 as 會意 — [[Radical 031|囗]] ("walled city") + 啚 ("early form of 鄙, 'remote areas'") — a walled territory, extended to "diagram, map, picture" — corrected accordingly.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/図表|図表]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `囗`, matching one component directly — [[Radical 031|囗]] gets the Radical-page link, while the other component, 啚, has no vault page (in the same "cited but never created" class as several recent iterations' components), so it's cited as bare text.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus two Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (図表) was missing entirely.

**Words cross-check** (9 total ground-truth hits): 2 already present (図書館 — ruby/gloss fixed, 地図学); 7 missing — 図表 (stand-in, added with annotation), 企図, 韻図, 図画, 地図冊, 地図, 版図 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 圖`/`図`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 175 — [[characters/唱|唱]]

Next never-perfected character by `danayo_id` (2051). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 昌` already correct — verified via Wiktionary: 形声, semantic [[Radical 030|口]] ("mouth") + phonetic 昌 (OC \*tʰjaŋ) — "to sing, to lead in singing."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/唱歌|唱歌]]'s own stored `pos`.

**Content removed**: a bare markdown-style link (`[昌](characters/昌.md)`) with no gloss or context, folded into the proper graphemic bullet.

**Graphemic bullet written from scratch**: 形声 (OC \*tʰjaŋs): semantic [[Radical 030|口]] ("mouth") + phonetic [[昌]] (OC \*tʰjaŋ) — "to sing, to lead in singing; to call out, chant."

**Body defects found**: `# Notes` was the wrong heading level; two CC-initial/final links were floating with no MC-rank bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed.

**Words cross-check** (2 total ground-truth hits): 1 already present (唱歌, the `stand_in`, already correctly annotated); 1 missing — 唱和 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 昌`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 174 — [[characters/告|告]]

Next never-perfected character by `danayo_id` (2050). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary, which flags the etymology as genuinely disputed: most likely an abbreviated 壴 ("decorated drum") + 口 ("open mouth"), with an older, disputed Shuowen reading taking the top component as 牛 ("ox") instead — either way, 會意 not 形声.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching sibling words (忠告, 申告) that store `pos: 実詞`/`事詞` for the same transitive "to report/accuse" sense (the stand-in word 告訴 itself stores `pos: 事詞`).

**Content removed**: none.

**Graphemic bullet written from scratch**: noted both competing component theories per Wiktionary. [[Radical 030|口]] matches this character's own `radical:` field and gets the Radical-page link; the other component, 壴, has no vault page (in the same "cited but never created" class as several recent iterations' components), so it's cited as bare text.

**Body defects found**: `## Notes` was completely empty; no SKIP/Stroke, MC-rank, or Levels bullets existed; two CC-initial/final links floated at the very end of the page with no MC-rank bullet; the stand-in Words entry (告訴) had no annotation, and three entries (忠告, 報告, 申告) were bare `[[link]]` with no ruby.

**Words cross-check** (8 total ground-truth hits): all 8 already present in some form (勧告, 誣告, 稟告, 訃告 already ruby'd; 告訴 — annotation added; 忠告, 報告, 申告 — ruby/gloss fixed from stored fields).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 告`): [[酷]] ("cruel"), [[造]] ("to create"), [[鵠]] ("swan"), [[靠]] ("to lean on"), [[皓]] ("luminous; clear"), [[浩]] ("great; numerous; vast") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 173 — [[characters/同|同]]

Next never-perfected character by `danayo_id` (2049 — 2048 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, contradicting the page's own pre-existing prose bullet, which already correctly described 同 as a pictograph of a pipe (original form of 筒), with 口 added later to mark the opening. Verified via Wiktionary that this prose was right — 同 is 象形 — and corrected the field to match, rather than the field having been trusted over the (correct) prose.

**Frontmatter**: already correct (`pos: 性詞`, `mc_id: 184` verified against `CC 0000.md`).

**Content removed**: none of substance — just reordered.

**Graphemic bullet**: kept the existing correct prose verbatim, just moved to the top of `## Notes` (it had been sitting after a stray Words-style entry and two blank lines, with the actual Words section starting before it).

**Body defects found**: bullet order was scrambled — a Words-style entry (偕同) appeared above the graphemic bullet inside `## Notes`; two CC-initial/final links floated at the very end of the page, after `## Chengyu`, with no MC-rank bullet; no SKIP/Stroke or Levels bullets existed; the stand-in Words entry (同一) was missing entirely; several Words entries were bare `[[link]]` or used a markdown-style link.

**Words cross-check** (17 total ground-truth hits): 11 already present in some form (偕同, 同学, 同族, 同胞, 同意, 同時, 同窓, 同志, 同居, 同僚, 同等 — all reformatted with ruby/gloss); 6 missing — 同一 (stand-in, added with annotation), 共同, 大同, 不同, 同年, 同伴 — added from stored fields.

**Chengyu cross-check** (2 total): 大同小異 already present; 呉越同舟 missing — added with its stored reading and gloss.

**Derived Characters** (6 hits via `graphemic_classification: 同`): [[筒 (char)|筒]] ("cylinder; tube"), [[銅 (char)|銅]] ("copper"), [[胴]] ("trunk; torso"), [[桐]] ("paulownia"), [[用]] ("to use"), [[洞]] ("cave; ravine; vale") — all added. Note: 用's MC readings look phonetically distant from 同 on the surface, but the field is trusted as-is per the mc_id/graphemic_classification policy for pre-existing vault data — no independent check performed on 用's own page (out of scope for this iteration).

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 172 — [[characters/各 (char)|各]]

Next never-perfected character by `danayo_id` (2047). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 夂 ("sole of foot") + [[Radical 030|口]] ("mouth, opening") — to come, to enter (original form of 𢓜 and 格); "each, individually."

**Frontmatter**: `pos: ""` (empty string) → filled in as `修飾語`, following the vault's [[grammar/文法 - 97品詞]] taxonomy which groups distributive/quantifier words like this alongside 其/某/彼/可/唯/已/於/公/他, all stored as `pos: 修飾語` (neither 各.md nor 各種.md has its own `pos` field to copy from directly).

**Content removed**: a non-canonical relative path (`../lookup/CC/finals/韻 鈬開`) in a floating CC-final link.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `口`, matching one component directly — [[Radical 030|口]] gets the Radical-page link, while the other component, 夂, has no vault page (in the same "cited but never created" class as several recent iterations' components), so it's cited as bare text.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (各) was missing entirely; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (3 total ground-truth hits, including a discovered quoted-scalar self-citation from 各.md's own `characters: "各 (char)"` field): 1 already present (各種); 2 missing — 各 (stand-in, added with annotation), 各位 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (10 hits via `graphemic_classification: 各` — one of the larger families surfaced in this loop): [[路]] ("road; path; journey"), [[略 (char)|略]] ("to abbreviate; plan"), [[格 (char)|格]] ("case; status"), [[絡 (char)|絡]] ("to enmesh; wrap around"), [[客]] ("guest; traveller"), [[駱]] ("camel"), [[賂]] ("to bestow"), [[酪]] ("cream; cheese; dairy"), [[閣]] ("chamber; pavilion; cabinet"), [[洛]] ("Luo River") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 171 — [[characters/句 (char)|句]]

Next never-perfected character by `danayo_id` (2046). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `勾`, which appears nowhere in Wiktionary's actual etymology for 句 (勾 is instead a related/derived character, "hook, crook"). Verified via Wiktionary that 句 is 形声: semantic 丩 ("to entangle") + phonetic 口 (OC \*kʰoːʔ) — corrected the field to `口`. This coincidentally matches this character's own `radical:` field, the same acceptable coincidence seen earlier with 位 and 信 (a phonetic component that happens to also be the Kangxi radical is a valid, non-self-referential case — self-reference only occurs when the field names the character's *own* name, as with the earlier 便/児/加 defects).

**Frontmatter**: already correct (`pos: 名詞`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (OC \*koː, \*koːs, \*kos, \*ɡo): semantic 丩 ("to entangle," no vault page — in the same "cited but never created" class as 𤰈/丌/冓/熒/厃 from recent iterations) + phonetic [[Radical 030|口]] (OC \*kʰoːʔ) — "sentence; phrase," also a classifier for sentences.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (句) was missing entirely; no `## Derived Characters` section existed despite six real ground-truth hits.

**Words cross-check** (8 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 句.md's own `characters: 句` field): 4 already present (句点, 高句麗, 慣用句, 句法 — ruby/gloss fixed); 4 missing — 句 (stand-in, added with annotation), 句杞, 詞句, 句号 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 句`): [[鉤 (char)|鉤]] ("hook; barb"), [[局 (char)|局]] ("office"), [[駒]] ("pony; colt"), [[苟 (char)|苟]] ("if only"), [[拘]] ("to constrain; restrain"), [[狗]] ("hound") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 170 — [[characters/古|古]]

Next never-perfected character by `danayo_id` (2045). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 指事` already correct — verified via Wiktionary: 指事, a shield ([[甲 (char)|甲]], a contraction of 盾) + [[Radical 030|口]] ("mouth") — both a distinguishing mark and a component partly indicating pronunciation, "strong, firm" (as strong as a shield) — the original form of 固; "ancient, old."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the sibling word [[words/中古|中古]]'s own stored `pos` (the stand-in word 古代 also stores `pos: 性詞`).

**Content removed**: none of substance.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `口`, matching one component directly — [[Radical 030|口]] gets the Radical-page link, while [[甲 (char)|甲]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: `## Notes` was completely empty; `## Chengyu` used a malformed markdown-style link instead of a wikilink and lacked a gloss; two CC-initial/final links were floating between Chengyu and further Words entries with no MC bullet; no SKIP/Stroke or Levels bullets existed; the stand-in Words entry (古代) was missing entirely; several entries were bare `[[link]]` with no ruby.

**Words cross-check** (13 total ground-truth hits): 8 already present in some form (稽古, 古希, 古文, 古風, 古琴, 古箏, 盤古, 蒙古 — all reformatted with ruby/gloss); 5 missing — 古代 (stand-in, added with annotation), 中古, 古典, 古語, 古今 — added from stored fields.

**Chengyu cross-check** (1 total): 古今東西 — relinked as a proper wikilink with its stored gloss added.

**Derived Characters** (6 hits via `graphemic_classification: 古`): [[苦 (char)|苦]] ("suffering; bitter"), [[胡]] ("reckless"), [[枯 (char)|枯]] ("withered"), [[故]] ("happening"), [[居]] ("to reside"), [[姑]] ("paternal aunt") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 169 — [[characters/取|取]]

Next never-perfected character by `danayo_id` (2044 — 2043 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[耳 (char)|耳]] ("ear") + [[Radical 029|又]] ("hand") — to take the ear of fallen prey, a hunters' rite mentioned in the Rites of Zhou; "to take, to obtain."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/取得|取得]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `又`, matching one component directly — [[Radical 029|又]] gets the Radical-page link, while [[耳 (char)|耳]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: section order was wrong — `## Words` and `## Chengyu` appeared before `## Notes`, which itself held nothing but two floating CC-initial/final links; reordered to the canonical Notes → Words → Chengyu → Derived Characters sequence; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (取得) had no annotation; no `## Derived Characters` section existed despite three real ground-truth hits.

**Words cross-check** (7 total ground-truth hits): 5 already present (詐取, 取得 — annotation added, 窃取, 截取, 聴取); 2 missing — 奪取, 採取 — added from stored fields.

**Chengyu cross-check** (1 total): 断章取義 already present, no changes needed.

**Derived Characters** (3 hits via `graphemic_classification: 取`): [[聚]] ("to assemble"), [[娶]] ("to marry"), [[趣]] ("interest") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 168 — [[characters/危|危]]

Next never-perfected character by `danayo_id` (2042). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, 厃 ("person on a cliff or mountain") + [[Radical 026|卩]] ("kneeling person") — a person in a precarious position on elevated terrain, "danger, peril."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/危険|危険]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `卩`, matching one component directly — [[Radical 026|卩]] gets the Radical-page link (the same radical as the recent 印 iteration, coincidentally); the other component, 厃, has no vault page (in the same "cited but never created" class as 𤰈/丌/冓/熒 from recent iterations), so it's cited as bare text.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus three bare Words entries (one with stray bracket punctuation inside its own gloss); no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (3 total ground-truth hits): all 3 already present (危険 — annotation added, 危机, 危殆 — ruby/gloss cleaned up and fixed from stored fields).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 危`): [[跪 (char)|跪]] ("to kneel") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 167 — [[characters/印|印]]

Next never-perfected character by `danayo_id` (2041 — 2040 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was invalid: stored as `爪`, as if 印 were 形声 with 爪 as its phonetic — but Wiktionary classifies 印 as 會意 ([[爪 (char)|爪]] "hand" + [[Radical 026|卩]] "kneeling person," a hand suppressing a kneeling person), not 形声, so a component name is the wrong kind of value here — corrected the field to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/封印|封印]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `卩`, matching one component directly — [[Radical 026|卩]] gets the Radical-page link, while [[爪 (char)|爪]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus bare/partial Words entries; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (封印) was missing entirely.

**Words cross-check** (7 total ground-truth hits): 3 already present (印度洋, 印章 — ruby/gloss fixed, 印尼); 4 missing — 封印 (stand-in, added with annotation), 印度支那, 印度尼西亜, 印度 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 印` or its former erroneous value `爪`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 166 — [[characters/医|医]]

Next never-perfected character by `danayo_id` (2039). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `殹`, which describes the *traditional* 醫's own 形声 etymology (phonetic 殹 + semantic 酉 "liquor") — but this vault page is titled 医, and 医 is not merely a modern reduction of 醫; Wiktionary confirms 医 is itself a distinct ancient character with its own 會意 etymology: [[Radical 023|匸]] ("hiding enclosure") + [[矢 (char)|矢]] ("arrow") — a tool for storing a bow and crossbow, later borrowed to write 醫. Corrected the field to `會意` to reflect the headword's own etymology, the same principle applied to 伝 earlier in this loop (favor the actual glyph's own history over its traditional counterpart's).

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching sibling words (医学, 医院) that store `pos: 名詞` (the stand-in word 医生 itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `匸` (Radical 023, "hiding enclosure") — Wiktionary's own component breakdown uses the visually near-identical `匚` (Radical 022, "box"), but 医 is conventionally filed under 匸 in dictionary radical indices, so [[Radical 023|匸]] gets the Radical-page link; [[矢 (char)|矢]] (not this character's own radical, has its own page) gets a direct character-page link. Noted the contrast with 醫's own distinct 形声 etymology for clarity.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (医生) was missing entirely.

**Words cross-check** (3 total ground-truth hits): 2 already present (医院 — ruby filled in from stored fields, 医学); 1 missing — 医生 (the `stand_in`) — added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 医` or its former value `殹`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 165 — [[characters/化 (char)|化]]

Next never-perfected character by `danayo_id` (2038). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, two 人, one upright (亻) and one upside down (𠤎) — reversal, change; Shuowen notes 𠤎 as also having a phonetic function.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching several sibling words (化粧, 溶化, 進化) that store `pos: 実詞` (the stand-in word 化.md itself has no `pos` field).

**Discovered but not fixed — character-vs-word `注音` mismatch**: this character page's own `注音` is `ㄏ⺢`, but its stand-in word [[words/化|化]] stores `注音: ㄏㄨㄚ` — a real divergence between the character's own reading and its stand-in word's stored reading. Per established policy this is flagged, not silently resolved; the Words entry for 化 itself was written using the word file's own stored reading (ㄏㄨㄚ), since that is what the verification script cross-checks against, but the underlying inconsistency between the two files remains unaddressed.

**Content removed**: none.

**Graphemic bullet**: kept the existing correct analysis, converted markdown-style links to wikilinks. This character's own `radical:` field is `匕`, which Radical 021's own lookup page confirms is the same glyph as the etymology's inverted-person component 𠤎 — so [[Radical 021|𠤎]] gets the Radical-page link (already correct pre-existing choice, just needed wikilink formatting), while the other, upright [[人 (char)|亻]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: two CC-initial/final links floating with no MC-rank bullet; no SKIP/Stroke or Levels bullets existed; the stand-in Words entry (化) was missing entirely, and 11 further real ground-truth Words hits were missing; no `## Chengyu` or `## Derived Characters` sections existed despite real hits for both.

**Words cross-check** (18 total ground-truth hits, checked across all five known `characters:` YAML shapes): 6 already present (文化, 液化, 転化, 化粧, 化身, 量化詞 — reformatted with ruby/gloss); 12 missing — 化 (stand-in), 強化, 化学, 変化, 悪化, 文化圏, 教化, 化学肥料, 溶化, 進化, 融化 — all added from stored fields.

**Chengyu cross-check** (1 total): 信達雅化 — the same chengyu already added during the recent [[characters/信|信]] iteration, since 化 is one of its four cited characters — missing here, added with its stored reading and gloss.

**Derived Characters** (4 hits via `graphemic_classification: 化`): [[訛]] ("error; extort"), [[靴]] ("boot"), [[花]] ("flower"), [[貨]] ("goods; commodities; products") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 164 — [[characters/勝|勝]]

Next never-perfected character by `danayo_id` (2037). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 朕` already correct — verified via Wiktionary: 形声, phonetic 朕 (OC \*l'ɯmʔ) + semantic 力 ("strength") — "to overcome, to defeat, to win."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/勝利|勝利]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `力`, matching the semantic component directly (same pattern as the recent 功/勇/労 iterations, all sharing 力 as their radical) — [[Radical 019|力]] gets the Radical-page link, while [[朕 (char)|朕]] (the phonetic, not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite two real ground-truth hits; the stand-in Words entry (勝利) had no annotation.

**Words cross-check** (1 total ground-truth hit): 勝利 (the `stand_in`) reformatted with ruby and annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 朕`): [[騰]] ("to inflate; rise"), [[謄]] ("to copy; transcribe") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 163 — [[characters/勇|勇]]

Next never-perfected character by `danayo_id` (2036). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 甬` already correct — verified via Wiktionary: 形声, phonetic 甬 (OC \*loŋʔ) + semantic 力 ("strength") — "brave strength."

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word [[words/勇敢|勇敢]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `力`, matching the semantic component directly — [[Radical 019|力]] gets the Radical-page link, while [[甬]] (the phonetic, not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (1 total ground-truth hit): 勇敢 (the `stand_in`) missing — added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (5 hits via `graphemic_classification: 甬`): [[誦 (char)|誦]] ("to recite; chant; repeat"), [[通 (char)|通]] ("to pass through; communicate"), [[痛]] ("torment; pain"), [[桶 (char)|桶]] ("pail; bucket; tub"), [[踊]] ("jump") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 162 — [[characters/労|労]]

Next never-perfected character by `danayo_id` (2035). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary (checked under the traditional form 勞): 会意, an abbreviated 熒 ("shine") + [[Radical 019|力]] ("strength") — visible effort combined with exertion; "to toil, labor."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/労動|労動]]'s own stored `pos`.

**Content removed**: a non-canonical relative path (`../words/労動`) in a bare, unruby'd Words entry.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `力`, matching one component directly — [[Radical 019|力]] gets the Radical-page link; the other component, an abbreviated 熒, has no vault page (in the same "cited but never created" class as 𤰈/丌/冓 from recent iterations), so it's cited as bare text.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one malformed Words entry; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (2 total ground-truth hits): 労動 (the `stand_in`) reformatted with ruby and annotation; 疲労 missing — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 労`): [[𢭐]] ("dredge; catch") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 161 — [[characters/加|加]]

Next never-perfected character by `danayo_id` (2034). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was invalid: stored as `力`, which is merely this character's own radical, not a distinct classification — the same self-referential defect class as the earlier 便/児 iterations. Verified via Wiktionary that 加 is 會意 — [[Radical 019|力]] ("strength") + [[口 (char)|口]] ("mouth"), per Shuowen "to exaggerate or slander" (an alternative reading takes 力 as "plowing," 口 as effort/breath) — corrected accordingly.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/加算|加算]]'s own stored `pos`.

**Content removed**: a malformed inline chain (`[[Radical 019|力]] + [[口 (char)]] = [[SKIP-1-2-3]] ([[Stroke 05]])`) that wikilinked the SKIP/Stroke lookup pages as if they were graphemic components rather than separate metadata; a dangling arrow-note (`scab 痂皮-->[[words/加皮]]`); a duplicate 加州金 entry (same word, same reading, listed twice under two different framings, the same defect pattern as the recent 利 iteration).

**Graphemic bullet written from scratch**: this character's own `radical:` field is `力`, matching one component directly — [[Radical 019|力]] gets the Radical-page link, while [[口 (char)|口]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: two CC-initial/final links (`聲 見`, `韻 麻二開`) were floating mid-list with no MC-rank bullet; no SKIP/Stroke or MC-rank bullets existed as proper bullets (only the malformed inline chain above); the stand-in Words entry (加算) was missing entirely; several entries were bare `[[link]]` with no ruby.

**Words cross-check** (14 total ground-truth hits): 10 already present in some form (増加, 参加, 添加, 加皮, 加入, 加法, 孟加拉, 加多, 奥加素, 加州金 — all reformatted with ruby/gloss, duplicate removed); 4 missing — 加算 (stand-in, added with annotation), 結加夫坐, 加持, 加多金 — all added from stored fields.

**Chengyu cross-check** (1 total): 加哀痛産 — missing, added with its stored reading and gloss.

**Derived Characters** (7 hits via `graphemic_classification: 加`): [[珈]] ("coffee"), [[伽]] ("transcription of Sanskrit 'gha'"), [[架 (char)|架]] ("rack; stand; prop"), [[賀]] ("to congratulate"), [[駕]] ("palanquin"), [[茄]] ("eggplant"), [[嘉]] ("good") — all added; no section previously existed.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 160 — [[characters/功|功]]

Next never-perfected character by `danayo_id` (2033). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 工` already correct — verified via Wiktionary: 形声, phonetic 工 (OC \*koːŋ, "labour; work") + semantic 力 ("strength") — essentially the same word as 工.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the sibling word [[words/気功|気功]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `力`, matching the semantic component directly — [[Radical 019|力]] gets the Radical-page link, while [[工]] (the phonetic, not this character's own radical, but has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry with no ruby; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (3 total ground-truth hits): 1 already present (功績, reformatted with ruby and stand-in annotation); 2 missing — 成功, 気功 — added from stored fields.

**Chengyu cross-check** (1 total): 論功行賞 — missing, added with its stored reading and gloss.

**Derived Characters** (9 hits via `graphemic_classification: 工` — a large phonetic family): [[空 (char)|空]] ("empty"), [[缸]] ("jug; cistern; urn"), [[攻 (char)|攻]] ("attack; criticize"), [[肛]] ("anus"), [[江]] ("river; cascade"), [[虹]] ("rainbow"), [[紅 (char)|紅]] ("crimson; red"), [[項 (char)|項]] ("nape; item"), [[貢]] ("tribute; gifts") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 159 — [[characters/利|利]]

Next never-perfected character by `danayo_id` (2032 — 2031 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[禾 (char)|禾]] ("grain") + [[Radical 018|刀]] ("knife") — to reap grain with a knife.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the sibling word [[words/利益|利益]]'s own stored `pos` (the stand-in word 利潤 stores `pos: 名詞` too).

**Content removed**: a malformed "### Descendants:" subsection containing a single garbled entry, `[㴝](characters/黎.md)` — display text 㴝 (an alias of 黎) pointing at 黎's actual file — folded into a proper `## Derived Characters` section instead. Also removed a duplicate 利佛素 entry (the same word, same reading, listed twice under two different framings with no distinguishing content).

**Graphemic bullet**: kept the existing correct analysis, but fixed the component links per the character's own `radical:` field (`刀`, matching the semantic component directly, same pattern as the recent 列/初 iterations): [[Radical 018|刀]] now gets the Radical-page link instead of a character-page link; [[禾 (char)|禾]] (not this character's own radical) keeps its character-page link, corrected to include the `(char)` filename suffix it was missing.

**Body defects found**: non-canonical relative path (`../lookup/...`); two CC-initial/final links floating under the `## Words` heading instead of embedded in an MC bullet; no SKIP/Stroke or Levels bullets existed; the stand-in Words entry (利潤) had no annotation, and two entries (利潤, 利用) were bare `[[link]]` with no ruby.

**Words cross-check** (9 total ground-truth hits): 5 already present (鋭利, 権利, 利潤 — annotation added, 利用 — ruby/gloss fixed, 利佛素 — de-duplicated); 4 missing — 利益, 勝利, 利率, 英吉利 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 利`): [[犂]] ("plough"), [[黎]], [[梨 (char)|梨]] ("pear"), [[痢]] ("diarrhea"), [[俐]] ("clever"), [[莉]] ("white jasmin") — all added. Flagging, not fixing: [[黎]]'s own stored `english` field is the string "Liǝ" — clearly not a real gloss (it's identical in shape to a romanized reading, not an English word) — cited here verbatim per the no-fabrication rule; the defect belongs to 黎's own page (danayo_id 8240), out of scope for this iteration.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 158 — [[characters/初|初]]

Next never-perfected character by `danayo_id` (2030). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[衣]] ("clothes") + [[Radical 018|刀]] ("knife") — "to start making clothes by cutting the cloth," → "beginning."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/最初|最初]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `刀`, matching the semantic component directly (same pattern as the recent [[characters/列|列]] iteration, coincidentally sharing the same radical) — [[Radical 018|刀]] gets the Radical-page link, while [[衣]] (not this character's own radical, has its own page) gets a direct character-page link.

**Body defects found**: two CC-initial/final links (`聲 初`, `韻 魚`) were floating outside any bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (最初) had no annotation, and two other entries (初版, 週初) were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (9 total ground-truth hits): 6 already present (最初 — annotation added; 初代, 初版, 太初, 初等, 週初 — ruby/gloss fixed where needed); 3 missing — 世紀初, 年初, 月初 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 初`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 157 — [[characters/列|列]]

Next never-perfected character by `danayo_id` (2029). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary, which gives 列 a dual classification depending on the historical form: earliest form 會意 ([[歹]] "skeletal remains" + [[Radical 018|刀]] "knife," to tear apart) vs. a later seal-script 形聲 form (obsolete phonetic 𡿪 + semantic 刀). Kept `會意` since the phonetic 𡿪 has no vault page and the 會意 reading is the more original one.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word [[words/配列|配列]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `刀`, which directly matches the semantic component of the earliest form (unlike the 兵/児 cases, no alias resolution needed) — so [[Radical 018|刀]] gets the Radical-page link, while [[歹]] (not this character's own radical, but has its own page) gets a direct character-page link.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite three real ground-truth hits.

**Words cross-check** (6 total ground-truth hits): 2 already present (並列, 大不列顛); 4 missing — 配列 (stand-in, added with annotation), 行列, 列島, 陳列 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 列` — the same family already surfaced during the recent [[characters/例|例]] iteration, since both characters share this phonetic): [[烈]] ("fiery; violent; vehement"), [[裂]] ("split; crack"), [[例]] ("example; instance; precedent") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 156 — [[characters/冷 (char)|冷]]

Next never-perfected character by `danayo_id` (2028). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 令` already correct — verified via Wiktionary: 形声, semantic [[Radical 015|冫]] ("ice") + phonetic 令, "cold as ice."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the sibling word [[words/寒冷|寒冷]]'s own stored `pos` (the stand-in word 冷.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 015|冫]] ("ice") + phonetic [[令]] — "cold as ice"; "cold, cool," extended to "desolate, indifferent, unpopular."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus two bare Words entries with no ruby; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite a large real ground-truth hit.

**Words cross-check** (4 total ground-truth hits, including a discovered unquoted-single-scalar self-citation from 冷.md's own `characters: 冷 (char)` field): 2 already present (冷蔵庫, 冷麺 — reformatted with ruby from stored fields); 2 missing — 冷 itself (stand-in, added with annotation) and 寒冷 — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (8 hits via `graphemic_classification: 令`): [[齢]] ("age; years"), [[伶]] ("clever"), [[鈴 (char)|鈴]] ("small bell"), [[羚]] ("antelope"), [[領]] ("territory"), [[笭]] ("bamboo screen"), [[零 (char)|零]] ("zero"), [[玲]] ("jade") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 155 — [[characters/再|再]]

Next never-perfected character by `danayo_id` (2027). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `象形`, but Wiktionary's primary classification for this etymologically disputed character is 会意 — the leading modern theory reads 一 ("one") + an abbreviated 冓 ("basket repeatedly woven from bamboo"), signifying repetition; an older theory reads 魚 ("fish") + 二 ("two"), "to catch two fish at once" — corrected to `會意`.

**Frontmatter**: `pos: ""` (empty string) → filled in as `副用名詞`, matching the stand-in word [[words/再度|再度]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): etymology uncertain and disputed — the modern leading theory reads it as 一 ("one") + an abbreviated 冓 ("basket repeatedly woven from bamboo," no vault page), signifying the repetition of something once done; "again, twice." An older theory instead reads 魚 ("fish") + 二 ("two"), "to catch two fish at once."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` or `## Chengyu` sections existed despite real ground-truth hits for both.

**Words cross-check** (1 total ground-truth hit): 再度 (the `stand_in`) missing — added with annotation.

**Chengyu cross-check** (1 total): 合漢再決 missing — added from stored fields.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 再`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 154 — [[characters/典|典]]

Next never-perfected character by `danayo_id` (2026). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `指事`, but Wiktionary classifies 典 as 會意 — [[冊 (char)|冊]] ("books") + 丌 ("table") — "(official) books on a table," explicitly noted as unrelated to the visually similar 曲/曹 — corrected accordingly.

**Frontmatter**: already otherwise correct (`pos: "名詞"`, `mc_id: 838` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): [[冊 (char)|冊]] ("books") + 丌 ("table," no vault page — an ancient variant of [[其 (char)|其]], not itself a Kangxi radical) — official books on a table; "law, canon, classic." 丌 gets no link (unlike the recent 廾/兵 case) since it's genuinely not a Kangxi radical, only a variant glyph of 其.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; the stand-in Words entry (事典) was missing entirely.

**Words cross-check** (10 total ground-truth hits): 2 already present (恩典, 祭典); 8 missing — 事典 (stand-in, added with annotation), 詞典, 古典, 典雅, 瑞典, 字典, 百科事典, 経典 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 典`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 153 — [[characters/兵|兵]]

Next never-perfected character by `danayo_id` (2025 — 2023 and 2024 do not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary: 会意, [[斤]] ("a short axe") + [[Radical 055|廾]] ("two hands") — a pair of hands holding a weapon.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/兵士|兵士]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: this character's own `radical:` field is `八`, which matches neither etymological component (斤 nor 廾), so neither gets a Radical-page link on that basis. Applied the two fallback rules instead: 斤 has its own dedicated character page, so it links there directly ([[斤]]); 廾 has no character page but is a genuine Kangxi radical (055), so it links to its Radical lookup page ([[Radical 055|廾]]) per the established unlinkable-but-real-radical convention (previously used for 聿 in the 画 iteration).

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus three bare Words entries (one with a stray leading dash inside its own gloss text); no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (6 total ground-truth hits): 3 already present (兵法, 兵站, 兵士 — all reformatted with ruby/gloss and stand-in annotation added to 兵士); 3 missing — 哨兵, 将兵, 兵卒 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 兵`): [[浜 (char)|浜]] ("coast; edge; bank") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 152 — [[characters/児 (char)|児]]

Next never-perfected character by `danayo_id` (2022 — 2020 and 2021 do not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was invalid: stored as `兒`, which is merely 児's own listed alias, not a distinct type or phonetic component — the same self-referential defect class as the earlier 便 iteration. Verified via Wiktionary that 児/兒 is 象形 — a pictograph of an infant with an imperfect cranium (i.e. the fontanelle) — corrected accordingly.

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching multiple sibling words (女児, 孤児院, 児子, 幼児) that all store `pos: 名詞`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 象形](lookup/List%20of%20象形.md): an infant with an imperfect cranium (i.e. the fontanelle); "child, offspring."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links plus one bare Words entry with no ruby; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite two real ground-truth hits.

**Words cross-check** (9 total ground-truth hits): 1 already present (児児, reformatted with ruby); 8 missing — 児 (stand-in, added with annotation), 胎児, 女児, 孤児院, 児子, 幼児, 嬰児, 児童 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 児` or its alias `兒`): [[䦧 (char)|䦧]] ("quarrel"), [[霓]] ("rainbow") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 151 — [[characters/億|億]]

Next never-perfected character by `danayo_id` (2019). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 意` already correct — verified via Wiktionary: 形声, semantic 人 + phonetic 意, "a hundred million."

**Frontmatter**: already correct (`pos: 数詞`, `mc_id: 1889` verified against `CC 1000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声: semantic [[Radical 009|人]] ("person") + phonetic [[意]] — "a hundred million," sometimes written as 1,0000,0000.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Words` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (1 total ground-truth hit): 一億 (the `stand_in`) missing — added with annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 意`): [[噫]] ("belch"), [[臆]] ("feelings; opinion; thoughts"), [[憶]] ("to recollect; remember") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 150 — [[characters/備|備]]

Next never-perfected character by `danayo_id` (2018). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` already correct — verified via Wiktionary, which gives 備 a dual 形聲/會意 classification: 人 ("person") + 𤰈 ("quiver," phonetic), "a person carrying a quiver" → "ready, prepared." 𤰈 has no vault character page (an obscure component confined to this one character, in the same class as 攴/㐮/鷲/瘠 previously documented in [[AIOS/projects.md]] — cited by Wiktionary but never independently created), so it's cited as bare text rather than linked; kept the field at `會意` since a phonetic link isn't available to justify treating it as a proper 形声 entry.

**Frontmatter**: `pos: ""` (empty string) → filled in as `実詞`, matching the stand-in word [[words/準備|準備]]'s own stored `pos`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 會意/形声: [[Radical 009|人]] ("person") + 𤰈 ("quiver," no vault page) — a person carrying a quiver; "ready, prepared."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links; no SKIP/Stroke, MC-rank, or Levels bullets existed.

**Words cross-check** (3 total ground-truth hits): 2 already present (準備, 必備); 1 missing — 設備 — added from stored fields.

**Chengyu cross-check** (2 total): both already present (日用必備, 有備無患), no changes needed.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 備`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 149 — [[characters/停|停]]

Next never-perfected character by `danayo_id` (2017). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 亭` already correct — verified via Wiktionary: 形声, semantic 亻 + phonetic 亭 (OC \*deːŋ), "to stop, to halt."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/停留|停留]]'s own stored `pos`.

**Content removed**: none — this page was already mostly well-formed from an earlier partial pass.

**Graphemic bullet**: already correct and complete, no changes needed.

**Body defects found**: the `stand_in` Words entry (停留) had no stand-in annotation; two Words entries were missing entirely.

**Words cross-check** (4 total ground-truth hits): 2 already present (停留 — annotation added, 停滞); 2 missing — 停泊, 停止 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 亭`, excluding this page itself) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 148 — [[characters/借 (char)|借]]

Next never-perfected character by `danayo_id` (2016 — 2015 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 昔` already correct — verified via Wiktionary: 形声, semantic 人 ("person") + phonetic 昔, "to lend/borrow."

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the sibling word [[words/仮借|仮借]]'s own stored `pos` (the stand-in word 借.md itself has no `pos` field).

**Content removed**: none.

**Graphemic bullet**: kept the existing analysis, converted the markdown-style `[人](Radical 009)` link to a proper `[[Radical 009|人]]` wikilink and added a brief gloss.

**Body defects found**: two CC-initial/final links (`聲 精`, `韻 麻三開`) were floating outside any bullet; no SKIP/Stroke or MC-rank bullets existed; no `## Words` section existed at all despite two real ground-truth hits; no `## Derived Characters` section existed despite three real ground-truth hits.

**Words cross-check** (2 total ground-truth hits, including a quoted-scalar-shape self-citation from 借.md's own `characters: "借 (char)"` field): 借 itself (stand-in, added with annotation), 仮借 — both added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 昔`): [[措]] ("to arrange"), [[錯]] ("mistake; error"), [[惜 (char)|惜]] ("to begrudge; rue") — all added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 147 — [[characters/信|信]]

Next never-perfected character by `danayo_id` (2014). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, but Wiktionary's primary classification is 形声 — phonetic [[Radical 009|亻]] (OC \*njin) + semantic [[言 (char)|言]] ("words"), the Shuowen 会意 reading noted only as a secondary/traditional gloss — corrected to `人`. Notably the page's pre-existing bullet had already half-flagged this itself, parenthetically noting "(which was OC \*njin!!)" next to 人 — the double exclamation marks a moment of the same doubt this iteration resolved in Wiktionary's favor.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞` (an eventive/transitive sense — "to trust X" — matching the stand-in word [[words/信任|信任]]'s sibling word [[words/不信|不信]], which stores `pos: 事詞` for the same root meaning, since 信任 itself had a blank `pos`).

**Content removed**: the malformed Korean level link, `Korean HS`, which didn't match the frontmatter's own `hanmun_edu_level: 中` (→ Korean MS) — an internal contradiction between the bullet and the field it was supposed to reflect.

**Graphemic bullet rewritten**: 形声 (OC \*sŋi[n]s): phonetic [[Radical 009|亻]] (OC \*njin) + semantic [[言 (char)|言]] ("words") — trustworthy words, words one can depend on; "to trust, to believe." Also converted several non-canonical relative paths (`../lookup/...`, `../syllables/...`) to canonical repo-root-relative paths.

**Body defects found**: two CC-initial/final links (`聲 心`, `韻 眞A開`) were floating outside any bullet with no MC-rank embedding; the Korean level mismatch noted above; one Words entry used a markdown-style link instead of a wikilink, two others were bare `[[link]]` with unformatted comma-separated glosses.

**Words cross-check** (8 total ground-truth hits): 4 already listed (信条, 信奉, 信用, 通信 — all reformatted with ruby/gloss); 4 missing — 信任 (stand-in, added with annotation), 不信, 信徒, 信天翁 — all added from stored fields.

**Chengyu cross-check** (1 total): 信達雅化 — missing, added with its stored reading and gloss.

**Derived Characters** (1 hit via `graphemic_classification: 人`, excluding this page itself): [[千]] ("thousand") — added; no section previously existed.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 146 — [[characters/便 (char)|便]]

Next never-perfected character by `danayo_id` (2013). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was invalid: stored as the literal string `便` (the character's own name), which is neither a valid type name nor a genuine phonetic component. Verified via Wiktionary that 便 is 會意 — [[Radical 009|亻]] ("person") + [[更 (char)|更]] ("to change"), "to change one's posture to make oneself comfortable" → "convenient" — corrected accordingly.

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/便|便]]'s own stored `pos`.

**Content removed**: none of substance.

**Graphemic bullet written from scratch**: [List of 会意](lookup/List%20of%20会意.md): [[Radical 009|亻]] ("person") + [[更 (char)|更]] ("to change") — to change one's posture to make oneself comfortable; "convenient."

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links with no bullet; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite a real ground-truth hit; the stand-in Words entry for 便 itself was missing.

**Words cross-check** (6 total ground-truth hits — discovered a 5th `characters:` YAML shape in the process: an unquoted single scalar, `characters: 便 (char)`, used by the word 便.md itself, distinct from all four previously catalogued shapes): 2 already present (方便, 便宜); 4 missing — 便 (stand-in, added with annotation), 大便, 以便, 郵便 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 便`, excluding this page itself): [[鞭]] ("whip") — added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 145 — [[characters/例|例]]

Next never-perfected character by `danayo_id` (2012). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 列` already correct — verified via Wiktionary: 形声, semantic 亻 ("person") + phonetic 列, "example, instance, precedent."

**Frontmatter**: `pos: ""` (empty string) → filled in as `名詞`, matching the stand-in word [[words/実例|実例]]'s own stored `pos`. `mc_id: 3847` verified against `CC 3000.md` (entries 3001–4000; confirmed 3847. 例 directly).

**Content removed**: none of substance — the page was essentially a stub.

**Graphemic bullet written from scratch**: 形声 (OC \*reds): semantic [[Radical 009|亻]] ("person") + phonetic [[列]] — "example, instance, precedent," concepts drawn from patterns of established human behavior.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links with no bullet, no `## Words` section, and no `## Derived Characters` section despite two real ground-truth hits.

**Words cross-check** (3 total ground-truth hits): all 3 missing — 実例 (stand-in, added with annotation), 恒例, 比例 — all added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 列`): [[烈]] ("fiery; violent; vehement"), [[裂]] ("split; crack") — both added.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 144 — [[characters/低|低]]

Next never-perfected character by `danayo_id` (2011). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 氐` already correct — verified via Wiktionary: 形声, semantic 亻 ("person") + phonetic 氐, "a person lowering themselves, bowing" → "low."

**Frontmatter**: `pos: ""` (empty string) → filled in as `性詞`, matching the stand-in word [[words/低下|低下]]'s own stored `pos`. `mc_id: 2908` verified against `CC 2000.md` (this file's entries run 2001–3000, confirmed 2908. 低 directly, unlike the usual mirrored-range CC lookup files).

**Content removed**: none of substance — the page was essentially a stub.

**Graphemic bullet written from scratch**: 形声 (OC \*tiːl): semantic [[Radical 009|亻]] ("person") + phonetic [[氐]] — a person lowering themselves, bowing; "low" (of height, quantity, or voice).

**Body defects found**: `# Notes` was the wrong heading level, and held nothing but two floating CC-initial/final links with no MC bullet and one bare Words entry with no ruby; no SKIP/Stroke, MC-rank, or Levels bullets existed; no `## Derived Characters` section existed despite four real ground-truth hits.

**Words cross-check** (2 total ground-truth hits): 低廉 already present (bare, reformatted with ruby from stored fields); 低下 (the `stand_in`) missing — added with stand-in annotation.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (4 hits via `graphemic_classification: 氐`): [[抵]] ("to resist"), [[邸]] ("residence"), [[砥]] ("whetstone"), [[底 (char)|底]] ("bottom; underneath; underside") — all added from stored fields.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 143 — [[characters/位|位]]

Next never-perfected character by `danayo_id` (2010). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `會意`, but Wiktionary clearly classifies 位 as 形声 — semantic [[Radical 009|人]] ("man") + phonetic [[立 (char)|立]] ("stand") — corrected to `立` per the rule that 形声 characters store the phonetic component name, not the type string. Notably the page's own pre-existing prose had already half-recognized this, hedging with "semantic (originally phonetic) 立" — the frontmatter field just hadn't caught up.

**Frontmatter**: already otherwise correct (`pos: 名詞`, `mc_id: 204` verified against `CC 0000.md`).

**Content removed**: the stray closing floating links (`[[Lookup/CC/initials/聲 云]]`, `[[Lookup/CC/finals/韻 脂B合]]`) sitting after the Words list with no bullet to embed in — folded into the proper MC bullet instead.

**Graphemic bullet rewritten**: 形声 (OC \*ɢʷrɯbs): semantic [[Radical 009|人]] ("man") + phonetic [[立 (char)|立]] (OC \*rɯb, "stand") — often simply written as 立 in idiomatic expressions such as 即位 (jíwèi) in Western Zhou inscriptions; "position, rank." (Also fixed the markdown-style `[人](Radical 009)` link to a proper `[[Radical 009|人]]` wikilink.)

**Body defects found**: `## Notes` had only the graphemic bullet, no SKIP/Stroke, MC-rank/CC-initial-final/syllable, or Levels bullets; four Words entries (定位, 位置, 位相, 各位) were bare `[[link]]` with no ruby/gloss; the `stand_in` entry (定位) had no stand-in annotation.

**Words cross-check** (20 total ground-truth hits, checked across all four `characters:` YAML shapes): all 20 already listed — 4 needed ruby/gloss filled in from stored fields, plus the stand-in annotation added to 定位.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 位`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 142 — [[characters/伝|伝]]

Next never-perfected character by `danayo_id` (2009). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification` was wrong: stored as `專`, but that's the phonetic of the *traditional* 傳 — the modern shinjitai glyph 伝 (already the subject of this page, with 傳/传 as its own aliases) is a shinjitai simplification that replaces the phonetic 專 with 云, per Wiktionary ("Simplified from 傳 (專 → 云)... 云 functions as the phonetic element"), the same pattern as 轉 → 転. The page's own Notes bullet already correctly named 云 as the phonetic before this iteration — the frontmatter field just hadn't been brought in line with it. Since 云 is itself only an alias (of [[characters/雲 (char)|雲]], not an independent character page), the field was set to the parent `雲` per the alias-resolves-to-parent convention.

**Frontmatter**: `pos: ""` (empty string) → filled in as `事詞`, matching the stand-in word [[words/伝播|伝播]]'s own stored `pos`. `graphemic_classification` corrected `專` → `雲` as above.

**Content removed**: none.

**Graphemic bullet rewritten**: 形声 (OC \*ɢiuan): semantic [[Radical 009|亻]] ("person") + phonetic [[雲 (char)|云]] (OC \*ɢun) — simplified in the shinjitai reform from traditional 傳's phonetic 專 (compare the analogous 轉 → 転 simplification); "to transmit, to propagate." Also converted the phonetic link from a bare markdown-style link to a proper wikilink with alias display text, matching the vault's link conventions.

**Body defects found**: `## Notes` had only the graphemic bullet — no SKIP/Stroke, MC-rank/CC-initial-final/syllable, or Levels bullets; two CC-initial/final links (`聲 澄`, `韻 仙B三合`) were floating outside any bullet; one Words entry (伝播, the `stand_in`) used a markdown-style link instead of a wikilink and was missing its stand-in annotation; two other entries (伝統, 伝説) were bare `[[link]]` with unformatted comma-separated glosses instead of ruby+quoted gloss.

**Words cross-check** (6 total ground-truth hits, checked across all four `characters:` YAML shapes): 5 already listed (all reformatted — stand-in annotation added to 伝播, ruby/gloss fixed for 伝統/伝説); 1 missing — 遺伝子 ("gene") — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no ground-truth hits (`graphemic_classification: 伝`) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 141 — [[characters/以 (char)|以]]

Next never-perfected character by `danayo_id` (2008 — 2007 does not exist in the sequence). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` verified correct via Wiktionary: a person (人) carrying something, simplified to 㠯 in pre-Qin scripts.

**Frontmatter**: `pos:` was blank — filled in as `格助詞`, matching the word file [[words/以|以]]'s own stored `品詞`/`pos`.

**Content removed**: none.

**Graphemic bullet**: kept as-is (already correct and complete from a prior partial edit).

**Body defects found**: `## Notes` had only the graphemic bullet — no SKIP/Stroke, MC-rank/CC-initial-final/syllable, or Levels bullets; two CC-initial/final links (`聲 以`, `韻 之`) were floating outside any bullet with no embedding; `## Chengyu` used a malformed markdown-style link (`[義以立名](/chengyu/義以立名.md)`) instead of a wikilink, and its `<rt>` reading (`ㄨㄧ·...`) did not match the chengyu's own stored `注音` (`ㄜㄧ·...`) — fixed to the stored value; several Words entries (以前, 以便, 既以, 為以) were bare `[[link]]` with no ruby/gloss at all.

**Words cross-check** (9 total ground-truth hits, checked across all four `characters:` YAML shapes): 8 already listed but 4 needed ruby/gloss filled in from stored fields; 1 missing — the stand-in entry for 以 itself — added. Caught two fabricated-then-corrected readings/glosses before stamping: 為以's actual stored `注音` is `⼔·ㄧ` (not `ㄨㄝㄧ` as I first guessed), and 既以's stored gloss is "already; too late" (not "already; since").

**Chengyu cross-check** (1 total): 義以立名 already present, relinked as a proper wikilink with its corrected reading and a gloss added from its stored field.

**Derived Characters** (1 hit via `graphemic_classification: 以`): [[似 (char)|似]] ("like; as; resembling") — added, no section previously existed.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

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

---

## Loop resumed 2026-07-23

### 2026-07-23, iteration 56 — [[characters/和|和]]

Next never-perfected character by `danayo_id` (155). Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter**: `pos: ""` → `性詞`, matching the stored `pos: 性詞` on `words/和平.md` (the `stand_in` compound itself) and consistent with the character's own adjectival English glosses ("peaceful, harmonious").

**Real etymology correction — semantic/phonetic reversed**: the existing graphemic bullet had 禾 and 口 backwards, labeling `[[Radical 115|禾]]` (glossed, wrongly, as "mouth") as semantic and `[[口]]` as phonetic. Real Shuowen derivation is the opposite: semantic **口** ("mouth," Radical 030 — confirmed via `lookup/Radicals/Radical 030.md`) + phonetic **禾** (Radical 115 confirmed as 禾 itself, not the semantic side here). This actually matches the frontmatter, which already correctly stored `graphemic_classification: 禾` (the phonetic-component convention) and `radical: 口` (the semantic radical) — only the *prose* had the roles swapped. Preserved and cleaned up the page's own genuinely useful etymological aside (original form 龢, built on 龠 "panpipes" rather than 口, for a harmony-through-music sense) — linked 龠 properly to its own Radical page (`[[Radical 214|龠]]`, confirmed to exist) since it's a real Kangxi radical too, per the radical-linking rule.

**Content removed**: a stray empty bullet (`- ` with nothing after it).

**Body defects found**: no SKIP/Stroke/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; three Words entries (和尚, 和平, 唱和) were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (11 total ground-truth hits): 3 already listed (共和国, 和諧, 和敬, all ruby'd and kept) plus 3 more present but bare (和尚, 和平, 唱和, reformatted); 5 missing — 共和, 大和, 昭和, 拌和, 令和 — added, all glosses/readings from stored fields. The `stand_in` compound 和平 itself was already present (just unruby'd) rather than missing outright, unlike most prior iterations' pattern.

**Chengyu cross-check** (2 total): 1 already present (声形和決); 1 missing — 覧昭和決 ("examine Shōwa and decide," a Dan'a'yo-coined script-reform principle idiom) — added, gloss condensed from its own Literal Meaning section rather than its literal `english` frontmatter (which reads as a loose paraphrase, "Japan picks the looks," less suited to a short Derived/Chengyu-style gloss).

**Derived Characters**: no hits (`graphemic_classification: 和` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 57 — [[characters/秋 (char)|秋]]

Next never-perfected character by `danayo_id` (156). Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 會意`, `mc_id: 229` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch** (page had no graphemic bullet at all): 会意 of [[Radical 115|禾]] ("grain") and [[Radical 086|火]] ("fire") — grain parched/dried by fire at the harvest, or the burning of stubble after reaping; by extension, the harvest season, "autumn."

**Body defects found**: `# Notes` was the wrong heading level, and held only two floating CC-initial/final links plus four Words-style entries — no `## Words` heading, no SKIP/Stroke/MC/Levels bullets; one Words entry (秋波) was a bare `[[link]]` with no ruby.

**Words cross-check** (9 total ground-truth hits): 3 already listed and ruby'd (中秋節, 秋田, 春秋時代) plus 1 present but bare (秋波, reformatted); 5 missing — the stand-in 秋 itself, 秋分, 孟秋, 仲秋, 季秋, 春秋 — added, all from stored fields.

**Chengyu cross-check** (2 total): 1 already present (春秋鼎盛); 1 missing — 一日三秋 — added (reusing the reading/gloss already established on [[characters/日 (char)|日]]'s own Chengyu section from iteration 1 of this loop).

**Derived Characters** (2 hits via `graphemic_classification: 秋`): [[鍬 (char)|鍬]] ("shovel") and [[萩]] ("bush clover") — both standard 秋-phonetic derivatives, added.

### 2026-07-23, iteration 58 — [[characters/重 (char)|重]]

Next never-perfected character by `danayo_id` (157). Stamped `date-last-perfect: 2026-07-23`. Another application of the element-abbreviation standing rule ([[feedback_element_abbreviation_characters]]): page already had a "abbreviation for 'barium'" Notes bullet for [[重素]] — kept it as its own trailing bullet, and (per the [[characters/青 (char)|青]] precedent from iteration 55) also gave 重素 its own proper `## Words` entry, since the two are not redundant.

**Frontmatter**: `pos: ""` → `性詞`, matching the sibling antonym [[characters/軽 (char)|軽]] ("light"), which already stores `pos: 性詞` for the same adjectival "heavy/light" class.

**Graphemic bullet written from scratch** (none existed): 形声, semantic [[壬]] ("a standing figure bent under a load") + phonetic [[東]] (OC \*toːŋ) — heavy, weighty; by extension, importance and duplication. Confirmed neither 壬 nor 東 is itself a Kangxi radical in this vault (`radical:` frontmatter for 重 is 里, unrelated to either etymological component), so both got bare `[[link]]`s rather than Radical-page links.

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (9 total ground-truth hits): 5 already listed (重複, 二重, 軽重, 偏重, 重畳); 4 missing — 重要, 貴重, 鄭重, and 重素 itself (per the standing rule above) — added, all from stored fields.

**Chengyu cross-check** (2 total): 0 already present; both missing — 義重於音, 重文軽武 — added from stored fields.

**Derived Characters** (8 hits via `graphemic_classification: 重` — the largest family since [[characters/青 (char)|青]]'s 10): [[動 (char)|動]], [[衝 (char)|衝]], [[鍾 (char)|鍾]], [[童]], [[腫]], [[董]], [[種]], [[踵]] — all standard, well-attested 重-phonetic derivatives, added. Filename collisions found on 動/衝/鍾 (all have colliding word files) — linked with pipe-aliases; the other five had no collision.

### 2026-07-23, iteration 59 — [[characters/度|度]]

Next never-perfected character by `danayo_id` (158). Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 庶`, `mc_id: 312` verified against `CC 0000.md`).

**Graphemic bullet written from scratch** (none existed): 形声, semantic [[Radical 029|又]] ("hand") + phonetic [[庶]] (abbreviated, per Shuowen's 庶省聲) — originally to measure by the span of the hand; a standard, a degree. Same "Kangxi radical assignment diverges from the real etymological semantic component" pattern as [[characters/重 (char)|重]] last iteration — the character's own `radical:` field is 广 (a shelter/shed radical, unrelated to the etymology), while the true semantic component 又 is a genuine Kangxi radical (029) and linked there; 庶 itself is not a Kangxi radical, so it got a bare link.

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (15 total ground-truth hits): 6 already listed (態度, 湿度, 幅度, 制度, 密度, 極度); 9 missing — the `stand_in` compound 程度 itself, 再度, 弧度, 精度, 限度, 印度, 印度洋, 印度支那, 印度尼西亜 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 度`): [[渡 (char)|渡]] ("transit; ferry") and [[鍍]] ("coat; gild") — both standard 度-phonetic derivatives, added. Filename collision found on 渡 (word file exists) — linked with pipe-alias; 鍍 had no collision.

### 2026-07-23, iteration 60 — [[characters/送 (char)|送]]

Next never-perfected character by `danayo_id` (159). Stamped `date-last-perfect: 2026-07-23`.

**Self-correction to iterations 58–59 (found while building this iteration's Levels bullet)**: both [[characters/重 (char)|重]] and [[characters/度|度]] have `joyo_level: "3"`, which per the checklist's own mapping table (`"1"`–`"6"` → `[[Jōyō - Kyōiku]]`; only the literal string `高等` → `[[Jōyō - Kōtō]]`) should have linked `Jōyō - Kyōiku`, not `Jōyō - Kōtō` as both iterations wrote. Fixed both files' Levels bullets before proceeding with this iteration.

**Real etymology correction — wrong phonetic component entirely**: `graphemic_classification: 笑` had no plausible phonetic relationship to 送 (MC s+uŋ vs. 笑's own MC s+iᴇu — same initial only, no real final match) and no attested etymological connection either. Verified via Wiktionary: 送's real phonetic component is **灷** (zhuàn), semantic [[Radical 162|辵]] ("walking; motion") — `radical: 辵` in the frontmatter already matched this correctly, only `graphemic_classification` itself was wrong. Corrected the field from `笑` to `灷` and wrote the bullet from scratch. 灷 has no character page of its own in this vault (and isn't a Kangxi radical), so it's cited as a bare `[[灷]]` link per the established practice for real-but-unlinked components.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("give").

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; one Words entry (送球) was bare `[[link]]` with no ruby.

**Words cross-check** (6 total ground-truth hits): 5 already listed (輸送, 送還, 逓送, 放送局 ruby'd; 送球 bare, reformatted); 1 missing — 搬送 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 送` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 61 — [[characters/音|音]]

Next never-perfected character by `danayo_id` (160). Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 指事` — verified plausible against Shuowen's 从言含一, matching `radical: 音` which is itself Radical 180).

**Content removed**: a garbled single-line "Derived characters: [[歆]]" note that was the page's entire pre-existing Notes section, superseded by the real four-bullet structure plus a proper `## Derived Characters` section.

**Graphemic bullet written from scratch**: 指事, [[Radical 149|言]] ("speech") with an added stroke marking sound emitted from the mouth — distinguishes 音 ("sound") from 言 ("speech") itself.

**Body defects found**: no `## Notes` structure existed at all (bare one-line note); two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets; several Words entries (音律, 音程, 音符, 音波, 観音) were bare `[[link]]` with no ruby/gloss; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check — largest ground-truth set so far this loop (25 total hits)**, found only after re-running the search to include the vault's inline-array `characters: [音, X]` frontmatter form (the plain multi-line `- 音` grep pattern alone silently missed 14 of the 25, the same gap flagged on [[characters/青 (char)|青]] back in iteration 55): 5 already ruby'd (音叉, 拼音, 注音, 振動音, 正音, 音素 — six, not five) plus 5 more present but bare (音律, 音程, 音符, 音波, 観音, reformatted); 14 missing — the `stand_in` compound 音楽 itself, 注音符号, 音声, 音節, 音韻, 子音, 母音, 清音, 濁音, 異音, 発音, 知音, 短音, 録音 — added, all from stored fields. **Caught one fabrication before stamping**: initially guessed 観音's reading as `ㄍㄨㄚㄋㄨㄇ` instead of checking its stored `注音` — cross-checked `words/観音.md` directly and corrected to the real value, `ㄍ⺢ㄋㄨㄇ`.

**Chengyu cross-check** (4 total, all missing, section built from scratch): 一字一音, 文音共決, 朝鮮正音, 義重於音 — added, all from stored fields.

**Derived Characters** (3 hits via `graphemic_classification: 音`): [[暗 (char)|暗]] ("dark"), [[歆]] ("be pleased" — already informally noted, now properly ruby'd), [[湆]] ("broth") — added. Filename collision found on 暗 — linked with pipe-alias; 歆/湆 had no collision.

### 2026-07-23, iteration 62 — [[characters/思|思]]

Next never-perfected character by `danayo_id` (161). Stamped `date-last-perfect: 2026-07-23`. **Third real "wrong phonetic component entirely" find this loop** (after [[characters/送 (char)|送]]'s 笑→灷 last iteration) — same failure shape twice in three iterations, worth treating as a pattern to watch for, not a one-off.

**Real etymology correction**: `graphemic_classification: 四` had no attested relationship to 思 at all. Verified via Wiktionary/Shuowen: real phonetic component is **囟** (xìn, "fontanelle," OC \*snɯns), semantic [[Radical 061|心]] ("heart"). The page's own `aliases: [恖]` already corroborated this independently — 恖 is Wiktionary's cited original form, with 囟 later corrupting into the unrelated 田-shape shared by the modern glyph (which is presumably how the field drifted toward "四," a visually similar top component). Corrected the field from `四` to `囟` and wrote the bullet from scratch, noting the corruption explicitly. 囟 has no character page of its own in this vault (and isn't a Kangxi radical), so cited as a bare `[[囟]]` link, same treatment as 灷 last iteration.

**Frontmatter**: `pos: ""` → `実詞`, matching the stored `pos: 実詞` on `words/思考.md` (the `stand_in` compound itself).

**Content removed**: none (the pre-existing Words-style entries were relocated, not deleted).

**Body defects found**: `# Notes` was the wrong heading level and held four Words-style entries (思想, 意思, 思考, 思議) directly, with a separate, correctly-headed but incomplete `## Words` section below holding only one more (思慕) — the split itself was the core defect; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 思議 was bare with no ruby; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (7 total ground-truth hits, using the inline-array-aware search established last iteration): 5 already present across the two split sections (思想, 意思, 思考, 思議 reformatted with its ruby restored from stored fields; 思慕 already ruby'd); 2 missing — 焦思, 相思 — added from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 不可思議 — added from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 思`): [[穂 (char)|穂]] ("ear of grain") and [[偲]] ("talent") — added. Filename collision found on 穂 — linked with pipe-alias; 偲 had no collision.

### 2026-07-23, iteration 63 — [[characters/発 (char)|発]]

Next never-perfected character by `danayo_id` (162). Stamped `date-last-perfect: 2026-07-23`. **Fourth wrong/imprecise-phonetic-component find this loop** (after 送/笑→灷, 思/四→囟) — this one more subtle than the other two: not unrelated, but *one step removed* from the real phonetic.

**Real etymology correction**: `graphemic_classification: 癶` is the character's own correctly-assigned Kangxi radical (`radical: 癶`, confirmed as Radical 105) but is not actually the phonetic component. Verified via Wiktionary: 發/発 began as a pictogram of a bow firing an arrow; a hand (攴) was added forming 㢭, whose hand element later became the real phonetic **癹** (bá, OC \*pʰaːd/\*baːd) — semantic [[Radical 057|弓]] ("bow"). The shinjitai 発 simplifies 癹 down to 癶-shaped, which is almost certainly why the field had drifted to citing the radical instead of the true (now-obscured) phonetic. Corrected the field from `癶` to `癹` and wrote the bullet explaining the full chain (pictogram → 㢭 → 癹 phonetic → shinjitai's 癶 simplification). 癹 has no character page of its own in this vault, so cited as a bare `[[癹]]` link, same treatment as 灷/囟 in the two prior corrections.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("issue forth, discharge") and consistent with `words/挑発.md`/`words/発明.md`/etc.'s own stored `pos: 実詞` for its compounds.

**Content removed**: none.

**Graphemic bullet**: written from scratch (none existed before this iteration; see correction above).

**Body defects found**: no `## Notes` heading existed at all — the page opened straight into `## Words`; two floating CC-initial/final links sat in the middle of the Words list with no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; seven Words entries (挑発, 発情, 発明, 発熱, 発財, 発電, 発音) were bare `[[link]]` with no ruby/gloss; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (18 total ground-truth hits via the inline-array-aware search): 16 already present (9 ruby'd, 7 bare — all 7 reformatted); 2 missing — the stand-in 発 itself and 恭喜発財 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 一触即発 — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 発` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 64 — [[characters/研|研]]

Next never-perfected character by `danayo_id` (163). Stamped `date-last-perfect: 2026-07-23`. A quiet iteration after three straight etymology corrections — `graphemic_classification: 幵` checked out as genuinely correct (semantic [[Radical 112|石]] "stone" + phonetic 幵, a clean match with `radical: 石`), no data error this time.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 幵`, `mc_id: 2969` verified against `CC 2000.md`).

**Content removed**: a bare "Components: [[石]], [[开]]" fragment, superseded by the real bullet — also corrected the component itself from 开 (a simplified variant used loosely in the old fragment) to 幵, matching the frontmatter's own stored phonetic value exactly. Neither 幵 nor 开 has a character page in this vault, so cited as a bare `[[幵]]` link, same treatment as the last three iterations' unlinked phonetic components (灷/囟/癹).

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 112|石]] ("stone") + phonetic [[幵]] (OC \*keːn) — to grind or sharpen on stone; by extension, to study closely, to research.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (1 total ground-truth hit): the `stand_in` compound 研究 itself was already present and correctly ruby'd — no changes needed.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 研` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 65 — [[characters/活 (char)|活]]

Next never-perfected character by `danayo_id` (164). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 舌` checked out as correct — verified via Wiktionary that the real phonetic component is the obscure 𠯑, which was later written as 舌 in the modern glyph, so citing 舌 is the right modern-form convention, not an error like the last three finds.

**Frontmatter**: `pos: ""` → `性詞`, matching the character's own adjectival gloss ("alive").

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 085|水]] ("water") + phonetic 𠯑 (later written as [[舌 (char)|舌]] in the modern glyph) — flowing water; by extension, living, alive.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links plus one Words-style entry; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all.

**Words cross-check** (4 total ground-truth hits): 1 already present (活動); 3 missing — the stand-in 活 itself, 復活, 生活, 復活節 (4 missing total, including the stand-in) — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 道活墨殺 — added from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 活`): [[闊 (char)|闊]] ("broad; wide") — added. Filename collision found — linked with pipe-alias.

### 2026-07-23, iteration 66 — [[characters/急 (char)|急]]

Next never-perfected character by `danayo_id` (165). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 及` checked out as correct — verified via Wiktionary (semantic 心 "heart" + phonetic 及, OC \*ɡrɯb), matching `radical: 心`.

**Frontmatter**: already correct (`pos: 性詞`, `mc_id: 588` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 061|心]] ("heart") + phonetic [[及]] (OC \*ɡrɯb) — urgency felt in the heart; rapid, pressing.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (2 total ground-truth hits): both already present and correctly ruby'd (急遽, 急速); only addition was the stand-in 急 itself, which had no prior entry.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 急` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 67 — [[characters/春 (char)|春]]

Next never-perfected character by `danayo_id` (166; 167/[[characters/相|相]] already stamped from an earlier session, so skipped). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 屯` checked out as correct — verified via Wiktionary (a doubly-semantic 形声: [[Radical 140|艸]] "grass" + [[Radical 072|日]] "sun" + phonetic 屯, OC \*dun "swollen sprout"), matching `radical: 日` as the Kangxi-assigned half of the two semantic components.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 211` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 艸 + 日 + phonetic [[屯 (char)|屯]] — grass growing under the sun; springtime.

**Body defects found**: `## Chengyu` sat before `## Words` (which didn't exist at all) and before the graphemic/SKIP/MC/Levels bullets, all of which were missing; two floating CC-initial/final links had no MC bullet to embed in; one Chengyu entry (春夏秋冬) used a plain unruby'd Markdown link; one Words-style entry (春季) was bare with no ruby.

**Words cross-check** (9 total ground-truth hits): 2 already present (春季 bare, reformatted; 春秋時代 ruby'd); 7 missing — the stand-in 春 itself, 仲春, 孟春, 季春, 春分, 春秋, 春節, 詠春拳 — added, all from stored fields. **Caught one fabrication before stamping**: initially guessed 春季's reading as `ㄑㄨㄋㄍㄧ` while retyping it into ruby form instead of copying the already-checked value — cross-checked `words/春季.md` directly and corrected to the real value, `ㄑㄨㄋㄍㄨㄧ` (same "verify before stamping" catch as [[characters/音|音]]'s 観音 two iterations ago).

**Chengyu cross-check** (2 total): both already present — 春夏秋冬 (ruby restored from its stored `注音`, plain link converted to proper `<ruby>` markup) and 春秋鼎盛 (already correct).

**Derived Characters** (2 hits via `graphemic_classification: 春`): [[椿]] ("tree name") and [[蠢]] ("squirm; wiggle") — added, neither had a filename collision.

### 2026-07-23, iteration 68 — [[characters/持 (char)|持]]

Next never-perfected character by `danayo_id` (168). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 寺` checked out as correct — verified via Wiktionary (semantic 手 "hand" + phonetic 寺, OC \*ljɯs), the same phonetic pairing as the checklist's own canonical 詩 example.

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 566` verified against `CC 0000.md`).

**Content removed**: a stray bare "1310" line sitting at the top of Notes with no context — an orphaned fragment (possibly a mis-pasted number, unrelated to any of this page's own stored fields) — removed, superseded by the real bullet.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 064|手]] ("hand") + phonetic [[寺]] (OC \*ljɯs) — to grasp, to hold.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (6 total ground-truth hits): 2 already present and correctly ruby'd (堅持, 持続); 4 missing — the stand-in 持 itself, 保持, 加持, 維持 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 持` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 69 — [[characters/草 (char)|草]]

Next never-perfected character by `danayo_id` (169). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 早` checked out as correct — verified via Wiktionary (semantic [[Radical 140|艸]] "grass" + phonetic 早, OC \*ʔsuːʔ), matching `radical: 艸`. Genuinely interesting etymology: 草 originally named a specific bitter plant (and was a loan for 皂), later displacing 艸 itself as the general word for "grass" — 艸 survives on this page only as its own listed `aliases:` entry, not a separate character page, consistent with the established alias-is-parent-form convention.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 590` verified against `CC 0000.md`).

**Content removed**: none (the pre-existing Words-style entries were relocated, not deleted).

**Graphemic bullet written from scratch**: 形声, semantic 艸 + phonetic [[早 (char)|早]] — see etymology note above.

**Body defects found**: `## Words` sat before a separately-headed `# Notes` (wrong heading level) holding two more Words-style entries — the split itself was the core defect; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 草木/草原 were bare with no ruby.

**Words cross-check** (11 total ground-truth hits): 8 already present across the two split sections (6 ruby'd; 草木/草原 bare, reformatted); 3 missing — the stand-in 草 itself, 海草, 茅草 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 草` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 70 — [[characters/海|海]]

Next never-perfected character by `danayo_id` (170). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 毎` checked out as correct — verified via Wiktionary (semantic [[Radical 085|氵]] "water" + phonetic 每/毎, OC \*mɯːʔ), matching the page's own pre-existing bullet exactly; added the etymological aside (海 probably related to 晦 "dark," paralleling 溟←冥) since Wiktionary offered it and the existing bullet lacked it.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 339` verified against `CC 0000.md`).

**Content removed**: a malformed folder-qualified wikilink (`[[../words/海就]]`), same broken-link class flagged on [[characters/林 (char)|林]] earlier this loop — fixed rather than removed outright.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; 14 Words entries were bare `[[link]]` with no ruby/gloss; one Chengyu entry (蒼海桑田) used a plain unruby'd Markdown link.

**Words cross-check — largest ground-truth set this loop (33 total hits)**: 27 already present (13 ruby'd; 14 bare, reformatted, plus the malformed 海就 link fixed); 6 missing — 上海, 四海, 海亀, 海峡, 海禁, 海王星 — added, all from stored fields. Noted in passing, not corrected (out of scope for a character-page pass): `words/海上.md` and `words/海象.md` store the identical `注音` (`ㄏㄚㄧㄙ⼘ㄫ`) despite being unrelated compounds — cited verbatim from each word's own stored field rather than silently resolved.

**Chengyu cross-check** (3 total): 1 already present (蒼海桑田, ruby restored from its stored `注音`, plain link converted to proper markup); 2 missing — 人山人海, 海闊天空 — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 海` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 71 — [[characters/後 (char)|後]]

Next never-perfected character by `danayo_id` (171; 174/[[characters/哉 (char)|哉]] already stamped 2026-07-20, so it will be skipped when reached). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (oracle-bone 会意: [[Radical 052|幺]] "thread" + [[Radical 035|夊]] "foot," a foot bound by rope, lagging behind; [[Radical 060|彳]] "step" added later to emphasize the action).

**Frontmatter**: `pos: ""` → `名詞`, matching the antonym pair [[characters/前 (char)|前]] ("front; before"), which already stores `pos: 名詞` for the same locational/temporal noun class.

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, see etymology above.

**Body defects found**: bullets 2–4 were merged into a single non-canonical middle-dot-separated bullet instead of the canonical two-bullet split (SKIP/Stroke separate from the MC-rank bullet) — the same defect shape flagged on [[characters/空 (char)|空]] back in iteration 47 — rebuilt into the standard order; no Levels bullet existed; three Words entries (後置詞, 後置, 後悔) were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (14 total ground-truth hits): 7 already present (4 ruby'd; 3 bare, reformatted); 7 missing — the stand-in 後 itself, 先後, 前後, 絶後, 而後, 背後, 紀元後 — added, all from stored fields.

**Chengyu cross-check** (2 total): 1 already present (空前絶後); 1 missing — 先題後述 — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 後` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 72 — [[characters/南|南]]

Next never-perfected character by `danayo_id` (172). Stamped `date-last-perfect: 2026-07-23`. Page already had a real, sourced graphemic bullet — spot-checked against Wiktionary, which describes the depicted object slightly differently (a lidded cylindrical vessel 同, rather than a bell) but agrees on every substantive point that matters (象形 pictograph, later phonetic loan for "south," OC \*nuːm matching exactly) — treated as scholarly-source variance rather than an error, left as-is per the "already correctly sourced" precedent from [[characters/空 (char)|空]]/[[characters/青 (char)|青]] earlier in this loop.

**Frontmatter**: `pos: ""` → `名詞`, matching the sibling cardinal-direction characters [[characters/北 (char)|北]] and [[characters/東 (char)|東]], both already `pos: 名詞`. **Flagged, not fixed (out of scope for a character page)**: `words/南方.md` — the `stand_in` compound itself — stores `pos: 連接詞` ("conjunction"), which cannot be right for a word glossed "south; southern direction"; left untouched since word-level `pos` corrections aren't part of this checklist.

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; two Words entries (南山, 南北) were bare `[[link]]` with no ruby/gloss; three more (南端, 西南, 南極) used plain Markdown links instead of wikilinks (harmless but inconsistent with the rest of the page); no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (20 total ground-truth hits): 11 already present (9 ruby'd — 3 via plain Markdown link, converted to wikilinks; 2 bare, reformatted); 9 missing — the stand-in 南方 itself, 南部, 東南, 江南, 越南, 越南人, 越南語, 南極洲, 東南亜 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 南`): [[楠]] ("camphor tree") — added, no filename collision.

### 2026-07-23, iteration 73 — [[characters/指|指]]

Next never-perfected character by `danayo_id` (173). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 旨` checked out as correct — verified via Wiktionary (semantic 扌 "hand" + phonetic 旨, OC \*kjiʔ, matching the character's own MC value exactly).

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 807` verified against `CC 0000.md`).

**Content removed**: none (the finger/toe-name prose list was relocated into `## Words`, not deleted).

**Graphemic bullet fixed**: the existing bullet had the right components but an empty gloss (`("")`) for 扌 — filled in as "hand."

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; the entire finger/toe-name family (大指, 母指, 食指, 中指, 無名指, 小指, 足指 — 7 real ground-truth words) was written as an indented prose list inside Notes instead of proper `## Words` entries, unruby'd; 指関節 was bare with no ruby; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (15 total ground-truth hits): all 15 were already mentioned somewhere on the page (8 properly in `## Words`, 7 buried in the Notes prose list) — none were missing outright, just misplaced/unformatted; consolidated all 15 into `## Words` with proper ruby+gloss.

**Chengyu cross-check** (1 total, missing, section built from scratch): 指記二碑 ("the two tablets of the law") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 指` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 74 — [[characters/某 (char)|某]]

Next never-perfected character by `danayo_id` (175; 174/[[characters/哉 (char)|哉]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-23`. Another full correlative-row family (此/其/彼/何/毎/某/皆 × 事/物/名/処/時/様/多/類/人), same recurring pattern as [[characters/彼 (char)|彼]] and others earlier in this loop. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (木 "tree" + 甘 "sweet," originally the Chinese plum 梅, later a phonetic loan for the indefinite pronoun "certain, some").

**Frontmatter**: already correct (`pos: 修飾語`). **`mc_id: 1332` initially looked unverifiable** — not found via the usual `> N. char` blockquote-prefix grep in `CC 1000.md` — but a bare-prefix search (`^1332\.` instead of `^> 1332\.`) found it immediately at line 349 ("1332. 某"), confirming the value is correct; the file's own formatting for this ID range doesn't use the `>` blockquote prefix the other CC files do, a lookup-format quirk worth remembering rather than a data problem.

**Content removed**: a stray "Components: [[甘]], [[木]]" fragment, superseded by the real bullet.

**Graphemic bullet written from scratch**: 会意, [[Radical 075|木]] ("tree") + [[Radical 099|甘]] ("sweet") — originally the Chinese plum (梅); later phonetically borrowed for the indefinite pronoun "a certain, some."

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; no `## Words` heading existed at all.

**Words cross-check** (10 total ground-truth hits): none were previously listed — built the entire section from scratch: the stand-in 某 itself, 某事, 某人, 某処, 某名, 某多, 某時, 某様, 某物, 某類, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 某`): [[煤 (char)|煤]] ("coal; soot"), [[謀 (char)|謀]] ("to conspire; scheme"), [[媒]] ("mediator; matchmaker") — added. Filename collisions found on 煤/謀 — linked with pipe-aliases; 媒 had no collision.

### 2026-07-23, iteration 75 — [[characters/風 (char)|風]]

Next never-perfected character by `danayo_id` (177; 176/[[characters/皆 (char)|皆]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-23`. **Real etymology finding, but not a simple error this time** — `graphemic_classification: 凡` checked out as correct, but the true derivation is more involved than a plain 形声: 風 is a **假借** (phonetic loan) of the character for 鳳 ("phoenix"), which was itself semantic phoenix-tail feathers + phonetic 凡 (OC \*bom). The feather strands simplified over time into the modern glyph's 虫-looking bottom component — a graphic vestige, not a true "insect" semantic radical, despite how it looks. 風 is also its own Kangxi radical (182), self-referential like a few other self-radical characters seen earlier in this loop (音, 里). Wrote the bullet to explain this chain rather than mislabeling it a bare 形声.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 279` verified against `CC 0000.md`). **Flagged, not fixed**: a real character-vs-word `注音` mismatch on the stand-in itself — the character's own frontmatter reads `ㄈㄨㄫ`, but `words/風.md` (the `stand_in` word) stores `ㄆㄨㄫ` (F vs. P initial) — same bug class as the `恩`/`慣`/`調`·`酒` mismatches logged in `projects.md`'s syllable sweep; cited the word's own stored value verbatim in its Words entry rather than silently unifying either field.

**Content removed**: none.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; three Words entries (風刺, 風笛, 風潮) were bare with no ruby; no `## Derived Characters` section existed despite real ground-truth hits.

**Words cross-check** (13 total ground-truth hits): 6 already present (3 ruby'd; 3 bare, reformatted); 7 missing — the stand-in 風 itself, 古風, 暴風, 風水, 風狂, 風采, 太陽風 — added, all from stored fields. **Caught two fabrications before stamping**: initially guessed readings for 風刺 (`ㄈㄨㄫㄑㄨ`) and 風潮 (`ㄈㄨㄫㄉㄧㄡ`) instead of checking their stored `注音` — cross-checked both directly and corrected to the real values, `ㄈㄨㄫㄑㄧㄎ` and `ㄈㄨㄫㄑㄚㄨ` respectively (same "verify before stamping" catch as [[characters/音|音]]'s 観音 and [[characters/春 (char)|春]]'s 春季 earlier this loop — now three separate catches of the same failure mode, worth treating as a standing discipline rather than a one-off).

**Chengyu cross-check** (4 total): 2 already present (弱不禁風, 五風十雨); 2 missing — 一帆風順, 風声鶴唳 — added from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 風`): [[楓]] ("maple") and [[瘋]] ("crazy; insane; wild") — added, neither had a filename collision.

### 2026-07-23, iteration 76 — [[characters/点 (char)|点]]

Next never-perfected character by `danayo_id` (178). Stamped `date-last-perfect: 2026-07-23`. Page already had a real, correctly-cited graphemic bullet (form + phonology already correct going in) — verified via Wiktionary (traditional 點: semantic 黑 "black" + phonetic 占, OC \*teːmʔ; shinjitai 点 substitutes 火, already correctly noted on the page). `mc_id: 3957` confirmed against `CC 3000.md` (bare `N. char` format, no `>` prefix, same file-format quirk noted for `CC 1000.md` last relevant iteration).

**Frontmatter**: already correct (`pos: 名詞`).

**Content removed**: none.

**Graphemic bullet**: no changes needed — already correct and complete.

**Body defects found**: none in the Notes section (all four bullets already present and correct) — this iteration was almost entirely a Words/Chengyu gap-fill.

**Words cross-check** (17 total ground-truth hits): 6 already present and correctly ruby'd (点心, 一点, 句点, 至点, 分点, 最高点); 11 missing — the stand-in 点 itself, 交点, 地点, 得点, 拠点, 斑点, 焦点, 特点, 缺点, 読点, 頂点, 小数点 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 画龍点睛 — the same chengyu already added to [[characters/画|画]] back in iteration 52, now also linked from its other constituent character 点; gloss pulled from the chengyu's own `english` field (its first list item was blank/empty in a way that required reading the raw file rather than trusting a single-line grep, since the real gloss values sat on subsequent list lines).

**Derived Characters**: no hits (`graphemic_classification: 点` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 77 — [[characters/前 (char)|前]]

Next never-perfected character by `danayo_id` (179). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 歬` is an unusual field value — not a type name (象形/指事/会意) nor a true 形声 phonetic component, but the character's own historical ancestor form. Verified via Wiktionary that this is a genuine, well-attested derivation (前's original form 歬 = 会意 of 止 "foot" + 舟 "boat," later simplified to 䒑+月 with 刀 "knife" added — the knife component now lives on in [[剪 (char)|剪]] "scissors/to cut," which absorbed that sense while 前 kept "front, before"). Left the frontmatter field as-is rather than reclassifying it, since it correctly names a real, meaningful component of the etymology chain even if it doesn't fit either of the checklist's two clean patterns — a borderline case worth flagging rather than silently normalizing.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 235` verified against `CC 0000.md`).

**Content removed**: a garbled "Components: [[䒑]], [[刖]]" fragment — 刖 ("to amputate the foot") is not actually part of 前's etymology at all, almost certainly a visual-similarity mix-up with 歬 — superseded by the real bullet.

**Body defects found**: bullets 2–4 were merged into a single non-canonical middle-dot-separated bullet (same defect shape as [[characters/後 (char)|後]] two iterations ago) — rebuilt into the standard order; two Words entries (前置詞, 前後) were bare with no ruby.

**Words cross-check** (15 total ground-truth hits): 4 already present (2 ruby'd; 2 bare, reformatted); 11 missing — the stand-in 前 itself, 前兆, 前年, 前提, 前日, 前月, 前週, 午前, 眼前, 空前, 前世紀, 紀元前 — added, all from stored fields. **Caught two fabrications before stamping**: initially left 前置詞/前後's `<rt>` empty while assembling the edit instead of checking their stored `注音` — cross-checked both directly and filled in the real values, `ㄐㄝㄋㄑㄧㄙㄚ` and `ㄐㄝㄋㄏㄛㄨ` respectively (fourth catch of this same failure mode this loop, after 観音/春季/風刺·風潮 — now clearly a standing habit to keep, not a one-off).

**Chengyu cross-check** (2 total): 1 already present (空前絶後); 1 missing — 珠投猪前 ("throwing pearls before swine") — added from stored fields.

**Derived Characters** (3 hits via `graphemic_classification: 前`): [[剪 (char)|剪]] ("scissors"), [[煎]] ("to boil; to fry"), [[箭]] ("arrow") — added. Filename collision found on 剪 — linked with pipe-alias; 煎/箭 had no collision.

### 2026-07-23, iteration 78 — [[characters/流|流]]

Next never-perfected character by `danayo_id` (180). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 㐬` checked out as correct — verified via Wiktionary (semantic [[Radical 085|水]] "water" + phonetic 㐬, OC \*ru); the existing bullet's phonetic OC value had been left as an empty placeholder `(OC )` — Wiktionary didn't give a separately-attested value for 㐬 distinct from 流's own \*ru (it only lists 流 alongside its wider phonetic-series relatives like 硫/琉/旒), so filled it in noting it shares 流's own reading rather than inventing a distinct number.

**Frontmatter**: already correct (`pos: 性詞`, matching the stored `pos: 性詞` on `words/流動.md`; `mc_id: 373` verified against `CC 0000.md`).

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links sat in the middle of the Chengyu section instead of embedded in an MC bullet; three Words entries (流動, 流暢, 流言) were bare with no ruby; two more (流星, 交流) used plain Markdown links instead of wikilinks.

**Words cross-check** (9 total ground-truth hits): 5 already present (2 ruby'd via plain Markdown link, converted to wikilinks; 3 bare, reformatted); 4 missing — 流域, 流水, 渓流, 渦流 — added, all from stored fields. **Checked all three initially-bare readings before writing them in** (流動, 流暢, 流言) rather than guessing — continuing the verify-before-stamping discipline established after the 観音/春季/風刺·風潮/前置詞·前後 catches earlier this loop; all three matched what would have been reasonable guesses, but confirmed rather than assumed.

**Chengyu cross-check** (3 total): 2 already present (流言飛語, 落花流水); 1 missing — 乳蜜流地 ("a land flowing with milk and honey") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 流` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 79 — [[characters/馬 (char)|馬]]

Next never-perfected character by `danayo_id` (182; 181/[[characters/病|病]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-23`. Page already had a real, detailed, correctly-sourced 象形 bullet (horse depiction, bronze-script head simplification to 目, legs to 灬) — left as-is, no etymology issue found this time.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/馬.md` (the `stand_in` word itself). `mc_id: 145` verified against `CC 0000.md`.

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; no `## Words` heading existed — all Words-style entries sat directly under Notes; three entries (馬上, 馬脚, 馬蹄) were bare with no ruby; no `## Derived Characters` section existed despite real ground-truth hits.

**Words cross-check** (16 total ground-truth hits): 5 already present (2 ruby'd; 3 bare, reformatted); 11 missing — the stand-in 馬 itself, 乗馬, 俊馬, 河馬, 海馬, 羅馬, 馬厩, 馬𡿺, 羅馬字, 羅馬語, 馬来西亜 — added, all from stored fields. **Checked the three initially-bare readings (馬上, 馬脚, 馬蹄) before writing them in**, continuing the standing verify-before-stamping discipline from recent iterations.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 馬`): [[碼 (char)|碼]] ("yard"), [[媽]] ("maidservant"), [[罵]] ("to abuse; to scold") — added. Filename collision found on 碼 — linked with pipe-alias; 媽/罵 had no collision.

### 2026-07-23, iteration 80 — [[characters/庭|庭]]

Next never-perfected character by `danayo_id` (183). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 廷` checked out as correct — verified via Wiktionary (semantic [[Radical 053|广]] "shelter, building" + phonetic 廷, OC \*l'eːŋ), matching `radical: 广`.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 992` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 广 + phonetic [[廷]] — a courtyard, the enclosed space of a building.

**Body defects found**: `# Notes` was the wrong heading level and held nothing but two floating CC-initial/final links — no graphemic/SKIP/MC/Levels bullets, no `## Words` section at all, despite three real ground-truth words.

**Words cross-check** (3 total ground-truth hits): none previously listed. The `stand_in` compound 中庭 itself had no stored `注音` field at all — derived it compositionally from its two constituent characters' own stored readings (中 = ㄐㄨㄫ, 庭 = ㄉㄝㄫ → ㄐㄨㄫㄉㄝㄫ), cross-checked against the word's own `羅馬字`/`諺文` fields ("jungdeng"/중덩), which matched exactly, before using it — same reconstruction method used for `words/中学校.md` back in iteration 1. 家庭 and 庭園 both already had real stored readings, added directly.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 庭` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 81 — [[characters/高 (char)|高]]

Next never-perfected character by `danayo_id` (184) — the same file the periodic-table abbreviation task added a Gallium note to earlier this session; that note is preserved as its own trailing Notes bullet per the standing element-abbreviation rule. Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 象形` checked out as correct — verified via Wiktionary (a pictograph of a tall building, compare 京, a similar tower pictograph that isn't itself a Kangxi radical).

**Frontmatter**: `pos: ""` → `性詞`, matching the stored `pos: 性詞` on `words/高.md` (the `stand_in` word itself). `mc_id: 150` verified against `CC 0000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 象形], depicts a tall building.

**Body defects found**: no `## Notes`/`## Words` headings existed at all — the abbreviation note and two Words-style entries sat directly under the meta-bind-embed with no structure; no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; 高考 was bare with no ruby.

**Words cross-check** (16 total ground-truth hits): 10 already present (9 ruby'd; 高考 bare, reformatted); 6 missing — the stand-in 高 itself, 崇高, 高人, 高素, 高綿, 高興 — added, all from stored fields. **Checked 高考's initially-bare reading before writing it in**, continuing the verify-before-stamping discipline from recent iterations.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (8 hits via `graphemic_classification: 高` — tied with [[characters/重 (char)|重]] for the largest family this loop): [[敲 (char)|敲]] ("to knock"), [[毫 (char)|毫]] ("fine hair; milli-"), [[稿 (char)|稿]] ("manuscript"), [[喬]] ("tall; lofty"), [[縞]] ("stripe"), [[膏]] ("grease; oil"), [[鎬]] ("stove"), [[豪]] ("magnificent; bold") — all added. Filename collisions found on 敲/毫/稿 — linked with pipe-aliases; the other four had no collision.

### 2026-07-23, iteration 82 — [[characters/夏 (char)|夏]]

Next never-perfected character by `danayo_id` (185). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 會意` checked out as correct, though the etymology itself is genuinely uncertain by scholarly consensus — verified via Wiktionary: possibly 日 ("sun") + 頁 ("head; man," "a man under the scorching sun"), but the identification is shaky since the oracle-bone form of 夏 only occurs as a diviner's name, not in its later "summer" sense. Later forms added 止 ("foot," which explains the modern character's assigned Kangxi radical, [[Radical 035|夊]], a foot-related radical unconnected to either of the two main components) or swapped 日 for 𦥑 ("two hands") before the modern glyph settled on neither variant. Wrote the bullet noting the uncertainty explicitly rather than presenting a debated etymology as settled fact.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 209` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意 (debated), see etymology above.

**Body defects found**: no `## Notes` heading existed at all; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 夏至 was bare with no ruby; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (4 total ground-truth hits): 1 already present (夏至, bare, reformatted after checking its stored `注音`); 3 missing — the stand-in 夏 itself, 仲夏, 孟夏, 季夏 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 春夏秋冬 — the same chengyu already added to [[characters/春 (char)|春]] and [[characters/海|海]] earlier this loop, now also linked from its constituent character 夏.

**Derived Characters** (1 hit via `graphemic_classification: 夏`): [[廈]] ("building; mansion") — added, no filename collision.

### 2026-07-23, iteration 83 — [[characters/起 (char)|起]]

Next never-perfected character by `danayo_id` (186). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 巳` checked out as correct — verified via Wiktionary (semantic [[Radical 156|走]] "to walk; run" + phonetic 巳, OC \*kʰɯʔ), matching `radical: 走`.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("rise up") and the stored `pos: 性詞`/`事詞`-class pattern used for its own compounds (起伏/起床/起死 are each stored `性詞`, but the bare verbal root itself follows the same `事詞` convention as [[characters/送 (char)|送]]/[[characters/発 (char)|発]] earlier this loop).

**Content removed**: none (the three Notes-prose entries were relocated, not deleted).

**Graphemic bullet written from scratch**: 形声, semantic 走 + phonetic [[巳]] — to rise, to get up.

**Body defects found**: `# Notes` was the wrong heading level and held the two floating CC-initial/final links plus three Words-style entries (起床, 起伏, 起死) with no ruby — the misplacement itself was the core defect; no SKIP/Stroke/MC/Levels bullets existed; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (4 total ground-truth hits): all 4 were already mentioned somewhere on the page (1 properly in `## Words`, 3 buried unruby'd in the Notes prose) — none missing outright; consolidated all 4 into `## Words` with proper ruby+gloss, plus added the stand-in 起 itself (a fifth entry, since `words/起.md` exists as its own file).

**Chengyu cross-check** (1 total, missing, section built from scratch): 起死回生 ("revival from the point of death") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 起` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 84 — [[characters/通 (char)|通]]

Next never-perfected character by `danayo_id` (187). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 甬` checked out as correct — verified via Wiktionary (semantic [[Radical 162|辵]] "walking; motion" + phonetic 甬, OC \*l̥ʰoːŋ), matching `radical: 辵`.

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 252` verified against `CC 0000.md`).

**Content removed**: none (the Notes-prose entries were relocated, not deleted).

**Graphemic bullet written from scratch**: 形声, semantic 辵 + phonetic [[甬]] — to pass through, to communicate.

**Body defects found**: `## Words` sat before a separately-headed `# Notes` (wrong heading level) holding four more Words-style entries — the split itself was the core defect, same shape as [[characters/思|思]] earlier this loop; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; three entries (通行証, 通行, 通貨, 通過) were bare with no ruby; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (13 total ground-truth hits): 6 already present across the two split sections (2 ruby'd; 4 bare, reformatted); 7 missing — the stand-in 通 itself, 交通, 亨通, 共通, 普通, 通知, 普通話 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 東亜自通 ("East Asian self-communication") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 通` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 85 — [[characters/家|家]]

Next never-perfected character by `danayo_id` (189; 188/[[characters/校|校]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-23`. **Real frontmatter/body contradiction found**: `graphemic_classification: 會意` directly contradicted the page's own pre-existing Notes bullet, which already correctly described a 形声 relationship (semantic 宀 + phonetic 𢑓) — the field and the prose disagreed with each other. Verified via Wiktionary that the bullet's content (not the field) was right: 家's oracle-bone form is genuinely semantic [[Radical 040|宀]] ("roof") + phonetic 𢑓 (xiá, "male pig"); the phonetic later corrupted to 豕 ("pig"), which Shuowen mistook for an abbreviated 豭 ("boar") — Wiktionary flags this as a folk etymology that misses the true original component. Corrected the field from `會意` to `𢑓` to match the real, already-written analysis, and expanded the bullet to explain the corruption chain. 𢑓 has no character page in this vault, cited as a bare `[[𢑓]]`-free plain-text mention (rare/unencodable enough that even a bare wikilink felt like overreach — written as plain text instead, unlike prior iterations' unlinked phonetics such as 灷/囟/癹).

**Frontmatter**: already correct otherwise (`pos: 名詞`, `mc_id: 148` verified against `CC 0000.md`).

**Content removed**: none (家鼠/家具/家蝿 were relocated from a mislabeled `## Chengyu` section into `## Words`, not deleted — same "ordinary words parked under Chengyu" defect as seen on other pages this loop).

**Body defects found**: three genuine Words entries (家鼠, 家具, 家蝿) were sitting under `## Chengyu` instead of `## Words`, alongside the one real chengyu (成家立業, itself using a plain unruby'd Markdown link); no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (20 total ground-truth hits): 11 already present (8 properly in Words; 3 misplaced under Chengyu); 9 missing — the `stand_in` compound 家庭 itself, 僧家, 儒家, 家事, 家族, 家畜, 無家, 自家, 大家族 — added, all from stored fields. **Caught one fabrication before stamping**: initially pasted 家庭's ruby as `ㄐㄨㄫㄉㄝㄫ` — actually [[characters/庭|庭]]'s own compositionally-derived reading for 中庭 from two iterations ago, copied into the wrong entry by mistake — cross-checked `words/家庭.md` directly and corrected to its real stored value, `ㄍㄚㄉㄝㄫ`. Also checked 家具's initially-bare reading before writing it in (`ㄍㄚㄍㄨ`) rather than guessing.

**Chengyu cross-check** (4 total): 1 already present (成家立業, plain link converted to wikilink, ruby restored from its own stored field); 3 missing — 家分不立, 引出奴家, 百家共承 — added from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 家`): [[嫁]] ("to give in marriage") and [[稼]] ("sheaves of grain") — added, neither had a filename collision.

### 2026-07-23, iteration 86 — [[characters/紙 (char)|紙]]

Next never-perfected character by `danayo_id` (190). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 氏` checked out as correct — verified via Wiktionary (semantic [[Radical 120|糸]] "silk" + phonetic 氏, OC \*kjeʔ), matching `radical: 糸`; Wiktionary itself flags the deeper semantic-shift etymology (silk → paper) as genuinely unknown, so the bullet notes the plausible-but-unconfirmed link to paper's early manufacture from silk waste rather than presenting it as settled.

**Frontmatter**: already correct (`pos: 名詞`). `mc_id: 4708` is beyond the ~4000-entry range mirrored in `lookup/CC/CC 0000–3000.md`, so per the checklist's own policy (never blank a large existing `mc_id` just because it can't be locally cross-checked) it was trusted as-is and used verbatim in the MC bullet.

**Content removed**: a non-canonical `## Etymology` heading holding a bare `[[糸]] + [[氏]]` component list, superseded by the real bullet.

**Graphemic bullet written from scratch**: 形声, semantic 糸 + phonetic [[氏]] — see etymology note above.

**Body defects found**: `# Notes` was the wrong heading level; a non-standard `## Etymology` subsection existed instead of folding the component analysis into the standard graphemic bullet; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all; 紙鳶 was bare with no ruby.

**Words cross-check** (1 total ground-truth hit): 紙鳶 was already mentioned (bare, reformatted); added the stand-in 紙 itself as a second entry (a `words/紙.md` file exists for it).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 紙` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 87 — [[characters/根 (char)|根]]

Next never-perfected character by `danayo_id` (191). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 艮` checked out as correct — verified via Wiktionary (semantic [[Radical 075|木]] "tree" + phonetic 艮, OC \*kɯːns), matching `radical: 木`. (Note: the checklist's own "Common mistakes" section flags a real, separate `mc_id` off-by-one error on [[艮]]'s *own* character page from an earlier session — unrelated to this citation, which is just a phonetic-component reference and carries no `mc_id` claim of its own.)

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 1165` verified against `CC 1000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 木 + phonetic [[艮]] — the root of a tree; by extension, foundation, origin.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (根拠, 根本) were bare with no ruby.

**Words cross-check** (5 total ground-truth hits): 3 already present (1 ruby'd; 2 bare, reformatted); 2 missing — the stand-in 根 itself, 耳根 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 財愛悪根 ("the love of money is the root of all evil") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 根` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 88 — [[characters/真 (char)|真]]

Next never-perfected character by `danayo_id` (192). Stamped `date-last-perfect: 2026-07-23`. **Real etymology correction, a new variant of the "self-referential nonsense value" bug class**: `graphemic_classification: 眞` cited the character's own traditional variant form (already separately listed in `aliases:`) as if it were a phonetic component — not unrelated like 送/笑, not one-step-removed like 発/癶, but literally citing itself. Verified via Wiktionary: 真/眞's real bronze-inscription form is 形声, semantic 貝 ("cowrie shell," later replaced by 鼎 "tripod") + phonetic **𠂈** (originally the pictograph of 顛, "to fall headlong"). Corrected the field from `眞` to `𠂈` and wrote the bullet explaining the component substitution. Also noted: the Kangxi-assigned radical `目` reflects neither ancestral component (貝/鼎 nor 𠂈) — same "radical diverges from real etymology" pattern as [[characters/重 (char)|重]]/[[characters/度|度]]/[[characters/風 (char)|風]]/[[characters/前 (char)|前]] earlier this loop, now confirmed as a recurring vault-wide phenomenon rather than a one-off. 𠂈 has no character page in this vault, cited as a bare `[[𠂈]]`-free plain-text mention (same treatment as 家's 𢑓 last iteration — an unencodable/extremely rare glyph where even a bare wikilink felt like overreach).

**Frontmatter**: `pos: ""` → `性詞`, matching the character's own adjectival gloss ("true").

**Content removed**: none (真摯 was relocated from a mislabeled `## Notes` section into `## Words`, not deleted).

**Body defects found**: `## Words` sat before a separately-headed `## Notes` (holding two floating CC-initial/final links plus one more Words-style entry, 真摯) — the split itself was the core defect, same shape as [[characters/思|思]]/[[characters/通 (char)|通]] earlier this loop; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (4 total ground-truth hits, found via a quoted-inline-scalar `characters: "真 (char)"` form that a plain multi-line-list grep alone would have missed — same class of gap as the inline-array issue flagged on [[characters/音|音]] earlier this loop, now confirmed as a third distinct `characters:` frontmatter shape to search): 3 already present across the split sections (all ruby'd); 1 missing — 天真 — added, plus the stand-in 真 itself (a `words/真.md` file exists for it).

**Chengyu cross-check** (1 total, missing, section built from scratch): 天真乱漫 ("simple and artless") — added from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 真`): [[鎮 (char)|鎮]] ("to tranquilize") and [[慎]] ("cautious") — added. Filename collision found on 鎮 — linked with pipe-alias; 慎 had no collision.

### 2026-07-23, iteration 89 — [[characters/酒|酒]]

Next never-perfected character by `danayo_id` (193). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 酉` checked out as correct — verified via Wiktionary (semantic [[Radical 085|水]] "water" + phonetic 酉, OC \*luʔ); genuinely interesting derivation, since 酉 was itself the *original* pictogram for "wine" before being repurposed as the 10th earthly branch, with 水 added later specifically to disambiguate the alcohol sense — and unlike several other characters this loop, the Kangxi-assigned radical (酉) actually *is* the true etymological component here, not a divergent later substitution.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/酒精.md` (the `stand_in` compound itself).

**Content removed**: a stray empty bullet (`- ` with nothing after it).

**Graphemic bullet fixed**: the existing bullet had the right components but an empty gloss (`("")`) for 水 — filled in as "water," and expanded with the 酉-was-the-original-word note.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; four Words entries (醇酒, 清酒, 酒糟, 麦酒) were bare with no ruby.

**Words cross-check** (7 total ground-truth hits): 4 already present (bare, reformatted); 3 missing — the `stand_in` compound 酒精 itself, 禁酒, 酌酒 — added, all from stored fields. **Noted in passing, not corrected**: `words/酒精.md`'s own stored `注音` (`ㄐㄨㄐㄝㄫ`) is missing the `ㄛ` that 酒 itself has (`ㄐㄨㄛ`) — this is the exact `調`/`酒` mismatch already documented in `AIOS/projects.md`'s syllable-lint sweep as a known systemic bug class, not a new find; cited verbatim from the stored field rather than silently corrected.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 酒` matches no other character) — section correctly omitted.

### 2026-07-23, iteration 90 — [[characters/記|記]]

Next never-perfected character by `danayo_id` (195; 194/[[characters/書|書]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-23`. `graphemic_classification: 己` checked out as correct — verified via Wiktionary (semantic [[Radical 149|言]] "speech" + phonetic 己, OC \*kɯʔ), matching `radical: 言` — the same phonetic-component-citation pattern as the checklist's own canonical 詩 example.

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/記憶.md` (the `stand_in` compound itself). `mc_id: 931` verified against `CC 0000.md`. **Caught after initially missing it**: the graphemic/body work was drafted before double-checking this field had actually been fixed in the file — confirmed via a follow-up grep that it was still blank, and corrected before finalizing this entry.

**Content removed**: none (記載/記者 were relocated from a wrong-heading-level Notes section into `## Words`, not deleted).

**Graphemic bullet written from scratch**: 形声, semantic 言 + phonetic [[己]] — to record, to remember.

**Body defects found**: `# Notes` was the wrong heading level and held two floating CC-initial/final links plus two Words-style entries (記載, 記者) with no ruby; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (13 total ground-truth hits): 3 already present (1 ruby'd; 2 bare, reformatted after checking their stored `注音`); 10 missing — the `stand_in` compound 記憶 itself, 史記, 日記, 書記, 礼記, 筆記, 記録, 出谷記, 創世記, 記念日 — added, all from stored fields. **Noted in passing, not corrected**: `words/礼記.md`'s stored `注音` (`ㄌㄝㄧㄍ`) looks truncated — missing the final `ㄧ` that 記 itself always contributes to every other compound on this page — cited verbatim rather than silently completed.

**Chengyu cross-check** (1 total, missing, section built from scratch): 指記二碑 — the same chengyu already added to [[characters/指|指]] two iterations ago, now also linked from its other constituent character 記.

**Derived Characters**: no hits (`graphemic_classification: 記` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 91 — [[characters/雪 (char)|雪]]

Next never-perfected character by `danayo_id` (197; 196/[[characters/黒 (char)|黒]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 彗` checked out as correct — verified via Wiktionary (雪 is an ancient simplification of 䨮 — already independently listed in the page's own `aliases:` field, nice corroboration — itself semantic [[Radical 173|雨]] "rain" + phonetic 彗), matching `radical: 雨`.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 1547` verified against `CC 1000.md`).

**Content removed**: none (雪魚's prose-style mention was reformatted, not deleted).

**Graphemic bullet written from scratch**: 形声 (via 䨮), semantic 雨 + phonetic [[彗]] — snow.

**Body defects found**: `## Notes` was empty; two floating CC-initial/final links sat between two Words-style entries with no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 雪魚 was written as inline prose ("cod is [[雪魚]]") instead of a proper ruby+gloss Words entry.

**Words cross-check** (3 total ground-truth hits): 2 already present (both reformatted — 雪魚 rescued from prose, 雪崩 given its ruby); 1 missing — the stand-in 雪 itself — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 雪` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 92 — [[characters/第 (char)|第]]

Next never-perfected character by `danayo_id` (198). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 弟` checked out as correct — verified via Wiktionary (semantic [[Radical 118|竹]] "bamboo, referring to bamboo strips used for writing/accounting" + phonetic 弟, OC \*diːls; the character may originally simply have been written 弟), matching `radical: 竹`.

**Frontmatter**: `pos: ""` → `数詞`, matching the stored `pos: 数詞` on `words/第八.md` (an ordinal compound of the character itself).

**Content removed**: none. **Non-canonical "### Links" section preserved, not discarded**: found a `![[nav/Numerals]]` embed under a stray `### Links` heading — checked and confirmed this is a deliberate, consistent cross-linking convention shared across *every* numeral character page in the vault (一/二/三/四/五/六/七/八/九/十/零/万), always placed as its own `## Links` section at the very end of the page (confirmed against the already-perfected `characters/一 (char).md`) — moved to match that exact placement/heading level rather than removed.

**Graphemic bullet written from scratch**: 形声, semantic 竹 + phonetic [[弟 (char)|弟]] — sequential order; the ordinal marker "-th."

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (7 total ground-truth hits): 2 already present and correctly ruby'd (及第, 第八); 5 missing — the stand-in 第 itself, 次第, 第一, 第二, 第三 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 第` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 93 — [[characters/動 (char)|動]]

Next never-perfected character by `danayo_id` (199) — already cited as a Derived Character on [[characters/重 (char)|重]] back in iteration 58, now perfected in full. `graphemic_classification: 重` checked out as correct — verified via Wiktionary (semantic [[Radical 019|力]] "strength" + phonetic 重, OC \*doŋ — described as "a heavy bag ready to be moved by a person"), matching `radical: 力`. Stamped `date-last-perfect: 2026-07-24`.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("move"). **Caught the joyo_level mapping before writing the Levels bullet this time**: `joyo_level: "4"` maps to `[[Jōyō - Kyōiku]]`, not `[[Jōyō - Kōtō]]` (only the literal string `高等` maps to Kōtō) — same rule already self-corrected on [[characters/重 (char)|重]]/[[characters/度|度]] back in iteration 60; got it right on the first pass this time. `mc_id: 338` verified against `CC 0000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 力 + phonetic [[重 (char)|重]] — see etymology above.

**Body defects found**: `## Words` sat before a separately-headed `# Notes` (wrong heading level, holding only two floating CC-initial/final links) — no graphemic/SKIP/MC/Levels bullets existed at all.

**Words cross-check** (17 total ground-truth hits): 9 already present and correctly ruby'd; 8 missing — the stand-in 動 itself, 労動, 動物, 動詞, 流動, 他動詞, 自動詞, 自動車 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 動` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 94 — [[characters/習|習]]

Next never-perfected character by `danayo_id` (200). Stamped `date-last-perfect: 2026-07-24`. **Another "field cites the modern surface component, not the true etymology" case, same shape as [[characters/前 (char)|前]]'s 歬**: `graphemic_classification: 白` looked like it contradicted the page's own pre-existing 会意 bullet (羽 "wings" + 日 "sun," "learning to fly"), which makes no mention of 白 at all. Verified via Wiktionary that both are correct at different points in the glyph's history: the *original* 会意 form is genuinely 羽+日, but in the *modern* glyph 日 has visually transformed into 白 — so the frontmatter field's citation of 白 is a legitimate reference to today's surface component, not an error to "fix" back to 日. Left the field as-is and expanded the bullet to explain the 日→白 evolution explicitly, linking 白 to its own Radical page ([[Radical 106|白]]) since it is a genuine Kangxi radical.

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/練習.md` (the `stand_in` compound itself). `mc_id: 828` verified against `CC 0000.md`. **Caught after initially drafting the log without checking**: same slip as [[characters/記|記]] two iterations ago — wrote the entry assuming the field was fine before re-grepping the file directly and finding it still blank; corrected before finalizing.

**Content removed**: none.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; two Words entries (補習, 予習) were bare with no ruby.

**Words cross-check** (7 total ground-truth hits): 6 already present (4 ruby'd; 2 bare, reformatted); 1 missing — 習俗 — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 習`): [[霫]] ("heavy rain") — added, no filename collision.

### 2026-07-24, iteration 95 — [[characters/問|問]]

Next never-perfected character by `danayo_id` (201). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 門` checked out as correct — verified via Wiktionary (semantic [[Radical 030|口]] "mouth" + phonetic [[Radical 169|門]] "gate," OC \*mɯːn; genuinely an exoactive derivation of [[聞 (char)|聞]] "to hear," literally "let me hear") — the same phonetic pairing already confirmed from the opposite direction back in iteration 45, where 門's own Derived Characters check found 問 as an exact MC match.

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/質問.md` (the `stand_in` compound itself). `mc_id: 161` verified against `CC 0000.md`. **Verified both fixes actually landed in the file before logging this entry** — direct follow-up grep of `pos:`/`date-last-perfect:` — a deliberate check after the same field slipping through unfixed on the last two iterations ([[characters/記|記]], [[characters/習|習]]).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声 (⿵門口), semantic 口 + phonetic 門 — see etymology above.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (7 total ground-truth hits): 4 already present and correctly ruby'd (問題, 学問, 詰問, 拷問); 3 missing — the stand-in 質問 itself, 査問, 訪問 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 問` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 96 — [[characters/深|深]]

Next never-perfected character by `danayo_id` (202). Stamped `date-last-perfect: 2026-07-24`. **Fifth real wrong-graphemic-component find this loop** (after 送/笑→灷, 思/四→囟, 発/癶→癹, 家/會意→𢑓, 真/眞→𠂈): `graphemic_classification: 會意` had no basis at all — verified via Wiktionary that 深 is genuinely 形声, semantic [[Radical 085|水]] ("water") + phonetic **𥥍** (an obscure component with no attested meaning of its own, OC \*hljum/\*hljums, the -s suffix distinguishing the nominal "depth" from the base adjectival "deep"). Corrected the field from `會意` to `𥥍`. 𥥍 has no character page in this vault, cited as bare plain text (same unlinked treatment as 𢑓/𠂈 the last two times this loop hit an unencodable/extremely rare phonetic).

**Frontmatter**: `pos: ""` → `性詞`, matching the character's own adjectival gloss ("deep") — `words/深刻.md`'s own `pos` field was itself blank, so this was set from the gloss rather than copied from the stand-in.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 水 + phonetic 𥥍 — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (深奥, 深刻) were bare with no ruby; no `## Words` heading existed at all (both sat directly under Notes).

**Words cross-check** (4 total ground-truth hits): 2 already present (bare, reformatted); 2 missing — 深淵, 深長 — added, all from stored fields.

**Chengyu cross-check** (1 total): already present and correctly formatted (意味深長) — no changes needed.

**Derived Characters**: no hits (`graphemic_classification: 深` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 97 — [[characters/族|族]]

Next never-perfected character by `danayo_id` (203). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as correct this time, and the page already had a real, correctly-sourced bullet — verified via Wiktionary (会意 of 㫃 "flag" + [[Radical 111|矢]] "arrow," a flag and arrow clustered together depicting a group of people). Expanded the bullet slightly with the "flag and arrow clustered" imagery and linked 矢 to its Radical page (Radical 111), which the original bullet hadn't done.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/家族.md` (the `stand_in` compound itself). `mc_id: 765` verified against `CC 0000.md`.

**Content removed**: none (one plain-Markdown-link entry, 同族, was converted to a wikilink, not deleted).

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 10 Words entries were bare with no ruby; 同族 used a plain Markdown link instead of a wikilink.

**Words cross-check** (22 total ground-truth hits — the largest plain Words list this loop, tied with [[characters/海|海]]'s 33-hit page for sheer volume of missing entries even though the total count is smaller): 15 already present (2 ruby'd; 1 plain-link, converted; 12 bare, reformatted); 7 missing — the stand-in 家族 itself, 水族, 満族, 漢族, 語族, 部族, 大家族, 水族館 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 族` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 98 — [[characters/船|船]]

Next never-perfected character by `danayo_id` (204). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 㕣` checked out as correct — verified via Wiktionary (semantic [[Radical 137|舟]] "boat" + phonetic 㕣, OC \*lon), matching `radical: 舟`. 㕣 has no character page in this vault, cited as bare plain text (same treatment as 𥥍/𢑓/𠂈 earlier this loop).

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/船舶.md` (the `stand_in` compound itself). `mc_id: 1424` verified against `CC 1000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 舟 + phonetic 㕣 — a boat, ship.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (船尾, 船籍) were bare with no ruby.

**Words cross-check** (8 total ground-truth hits): 3 already present (1 ruby'd; 2 bare, reformatted); 5 missing — the `stand_in` compound 船舶 itself, 乗船, 帆船, 艦船, 宇宙船 — added, all from stored fields. **Noted in passing, not corrected**: `words/艦船.md` and `words/宇宙船.md` both store `ㄐ⼔ㄋ` for 船's own contribution instead of its actual reading `ㄙ⼔ㄇ` — the same character-vs-word `注音` mismatch class already logged multiple times this loop (調/酒, 恩/慣) — cited verbatim from each word's own stored field.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 船` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 99 — [[characters/進|進]]

Next never-perfected character by `danayo_id` (205). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 隹` checked out as correct under the modern-preferred analysis — verified via Wiktionary: 進 is primarily 会意 of [[Radical 162|辵]] ("walk") + [[Radical 172|隹]] ("short-tailed bird" — "a bird can only walk forward, not backward"), though Shuowen itself instead treats it as 形声 with abbreviated phonetic 閵. Wrote the bullet under the 会意 reading (matching the stored field) and noted the Shuowen alternative explicitly rather than picking a side silently.

**Frontmatter**: `pos: ""` → `実詞`, matching the stored `pos: 実詞` on `words/進行.md` (the `stand_in` compound itself). `mc_id: 292` verified against `CC 0000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, 辵 + 隹 — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all (the one entry, 進撃, sat directly under Notes, bare).

**Words cross-check** (4 total ground-truth hits): 1 already present (bare, reformatted); 3 missing — the `stand_in` compound 進行 itself, 先進, 進化 — added, all from stored fields. **Caught one fabrication before stamping**: initially guessed 進行's gloss as "to proceed; carry out" instead of checking its stored `english` field — cross-checked directly and corrected to the real value, "to advance; progress" (matching the character's own gloss almost exactly, which made the fabrication easy to miss on a casual glance — a reminder that plausible-sounding guesses are the most dangerous kind).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 進` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 100 — [[characters/宿|宿]]

Next never-perfected character by `danayo_id` (206) — **100th iteration of this loop.** Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (oracle-bone form: [[Radical 009|亻]] "person" resting on a bamboo mat, with [[Radical 040|宀]] "roof" added later — the mat pictogram evolved into the modern glyph's 百 component).

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 833` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, see etymology above.

**Body defects found**: `## Notes` was empty; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (宿舎, 宿命) were bare with no ruby; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (8 total ground-truth hits): 4 already present (2 ruby'd; 2 bare, reformatted); 4 missing — the `stand_in` compound 寄宿 itself, 目宿, 寄宿舎, 昴宿星団 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 世仇宿敵 ("generational feud with a long-standing enemy") — added from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 宿`): [[縮 (char)|縮]] ("to shrink; contract") — added. Filename collision found — linked with pipe-alias.

### 2026-07-24, iteration 101 — [[characters/魚 (char)|魚]]

Next never-perfected character by `danayo_id` (207). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` checked out as correct — verified via Wiktionary (a pictograph of a fish, OC \*ŋa; conservative variant 𤋳, already correctly noted).

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 551` verified against `CC 0000.md`).

**Content removed**: a literal duplicate — the graphemic bullet's exact content ("a fish... conservative variant is 𤋳") was written out twice as two separate bullets — collapsed to one.

**Graphemic bullet fixed**: kept the existing correct content, added the missing OC value (\*ŋa).

**Body defects found**: the SKIP/Stroke bullet and Levels bullet were both present but in reversed order (Levels before SKIP/Stroke) and non-canonically formatted (a dash-separated syllable link tacked onto the SKIP/Stroke bullet instead of living in its own MC-rank bullet); the MC-rank bullet itself was entirely missing — the floating CC-initial/final links sat unattached at the very bottom of the file instead of embedded in it. Rebuilt all four Notes bullets into the canonical order. Two Words entries (魚雷, 周魚) used plain Markdown links instead of wikilinks; 轄魚鳥牲 was bare with no ruby.

**Words cross-check** (19 total ground-truth hits — the largest this loop by count, edging out [[characters/海|海]]'s 33 *hits* but with more *missing* entries relative to page size): 8 already present (6 ruby'd; 2 plain-link, converted); 10 missing — 曼魚, 盧魚, 章魚, 雪魚, 魚翅, 鮫魚, 鯖魚, 鯨魚, 鰐魚, 安康魚 — added, plus the stand-in 魚 itself (an 11th addition), all from stored fields.

**Chengyu cross-check** (2 total): 1 already present and correctly formatted (沈魚落雁); 1 present but bare (轄魚鳥牲) — ruby restored from its own stored `注音`.

**Derived Characters** (2 hits via `graphemic_classification: 魚`): [[漁]] ("to fish") and [[魯]] ("rash; vulgar") — added, neither had a filename collision.

### 2026-07-24, iteration 102 — [[characters/都|都]]

Next never-perfected character by `danayo_id` (208). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 者` checked out as correct — verified via Wiktionary (semantic [[Radical 163|邑]] "town, city" + phonetic [[者 (char)|者]], OC \*tjaːʔ), matching `radical: 邑`.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/首都.md` (the `stand_in` compound itself). `mc_id: 298` verified against `CC 0000.md`.

**Content removed**: a nonsensical stray `- [[ㄉㄛ]]` bullet (a bare self-referential link to the character's own syllable page, sitting alone with no context).

**Graphemic bullet written from scratch**: 形声, semantic 邑 + phonetic 者 — a significant administrative or political center; capital.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all despite two real ground-truth words.

**Words cross-check** (2 total ground-truth hits): none previously listed — built the section from scratch: the stand-in 首都 itself, 都市, both from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 都` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 103 — [[characters/教|教]]

Next never-perfected character by `danayo_id` (209). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 爻` checked out as correct — verified via Wiktionary: a genuinely tri-partite 形声, phonetic 爻 (OC \*ɢraːw) + *two* semantic components, [[Radical 039|子]] ("child") and [[Radical 066|攴]] ("teaching cane; a stick representing authority") — "teaching a child," matching `radical: 攴` as one of the two. 爻 has no character page in this vault, cited as bare plain text (same treatment as the other unlinked obscure phonetics this loop).

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/教授.md` (the `stand_in` compound itself). `mc_id: 341` verified against `CC 0000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, phonetic 爻 + semantic 子 + semantic 攴 — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (教員, 教師) were bare with no ruby.

**Words cross-check** (26 total ground-truth hits — the largest single Words list this loop by raw count): 13 already present (11 ruby'd; 2 bare, reformatted); 13 missing — the `stand_in` compound 教授 itself, 佛教, 儒教, 回教, 孔教, 宗教, 教会, 教化, 教学, 教材, 道教, 回教徒, 神道教 — added, all from stored fields. **Noted a widespread pattern, not corrected**: five compounds (教授, 佛教, 宗教, 教会, 教材) all store `ㄍ⼘ㄨ` for 教's own contribution instead of the character's actual reading `ㄍ⼄ㄨ` — the same character-vs-word `注音` mismatch class logged repeatedly this loop, but notable here for recurring across five *unrelated* compounds rather than one or two, suggesting a shared upstream cause (possibly a bopomofo `⼘`/`⼄` visual mix-up during data entry) rather than five independent typos; cited verbatim from each word's own stored field.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 教` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 104 — [[characters/黄 (char)|黄]]

Next never-perfected character by `danayo_id` (210) — the same file the periodic-table abbreviation task added a Gold note to earlier this session; preserved as its own trailing Notes bullet per the standing element-abbreviation rule, same treatment as [[characters/高 (char)|高]] a few iterations ago. Stamped `date-last-perfect: 2026-07-24`. **Another genuinely disputed etymology, same shape as [[characters/夏 (char)|夏]]**: `graphemic_classification: 炗` matches Shuowen's own analysis (phonetic 炗 "light" + semantic 田 "field"), but Wiktionary flags this as erroneous — the top component 廿 is a corruption of 口 in the bronze inscription, not really 田 at all — and modern scholarship instead proposes an 象形 origin (either a disabled person, or a man wearing a jade ring on his chest), with "yellow" arising as a rebus/phonetic-loan sense. Left the field as-is (it documents the traditional citation, consistent with precedent for characters whose stored value reflects Shuowen rather than modern consensus) and wrote the bullet presenting both accounts honestly rather than picking one silently.

**Frontmatter**: already correct (`pos: 性詞`). `mc_id: 228` verified against `CC 0000.md` (using the traditional form 黃 in the ranking, consistent with vault convention).

**Content removed**: none (the "Fifth most common Vietnamese surname" aside was kept, relocated to its own bullet after the four canonical ones).

**Discovered a fourth distinct `characters:` frontmatter shape this loop**: `words/黄沙.md` uses a quoted JSON-style inline array, `characters: ["黄 (char)", "沙 (char)"]` — none of the three search patterns established earlier this loop (multi-line list, unquoted inline array, quoted inline scalar) matched it; a dedicated fourth pattern was needed to surface it as a ground-truth hit. Worth remembering that this vault's `characters:` field has now been observed in at least four distinct YAML shapes.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; three Words entries (黄泉, 黄沙, 黄昏) were bare with no ruby.

**Words cross-check** (9 total ground-truth hits, using the newly-discovered quoted-array pattern to catch 黄沙): 4 already present (1 ruby'd via the abbreviation note; 3 bare, reformatted); 5 missing — the stand-in 黄 itself, 硫黄, 黄檗, 黄海, 黄銅 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 黄` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 105 — [[characters/細 (char)|細]]

Next never-perfected character by `danayo_id` (212; 211/[[characters/章 (char)|章]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. **Confirmed systematic bug, not an independent error**: `graphemic_classification: 四` was the *exact same* wrong stored value already found and corrected on [[characters/思|思]] back in iteration 62 — and the real phonetic component is *also* the same obscure character, **囟** (OC \*snɯns), which Wiktionary again confirms became falsely associated with 田 through Han-dynasty graphic corruption and has apparently been mistranscribed as the visually-similar `四` on at least two separate pages sharing this phonetic series. Corrected the field from `四` to `囟` and cross-referenced the sibling correction on 思 directly in the bullet.

**Frontmatter**: already correct (`pos: 性詞`). `mc_id: 1235` verified against `CC 1000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 120|糸]] ("silk, thread") + phonetic 囟 — fine, thin, slender.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (7 total ground-truth hits): 2 already present and correctly ruby'd (細妹, 細菌); 5 missing — the stand-in 細 itself, 細胞, 繊細, 詳細, 亜細亜 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 細` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 106 — [[characters/軽 (char)|軽]]

Next never-perfected character by `danayo_id` (213) — the hydrogen-abbreviation character referenced repeatedly earlier this session. `graphemic_classification: 巠` checked out as correct — verified via Wiktionary (semantic [[Radical 159|車]] "carriage" + phonetic [[巠]], OC \*kʰeŋ; originally "a light carriage," a sense preserved in the idiom 駕輕就熟). Stamped `date-last-perfect: 2026-07-24`.

**Frontmatter**: already correct (`pos: 性詞`, `mc_id: 475` verified against `CC 0000.md`).

**Content removed**: an informal "軽素 hydrogen, abbreviated 軽" plain-text note, reformatted into the standard element-abbreviation Notes bullet used everywhere else this convention appears in the vault (see [[feedback_element_abbreviation_characters]]).

**Graphemic bullet written from scratch**: 形声, semantic 車 + phonetic 巠 — see etymology above.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (軽銀, 軽罪) were bare with no ruby; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (8 total ground-truth hits): 7 already present (5 ruby'd; 2 bare, reformatted); 1 missing — the stand-in 軽 itself — added.

**Chengyu cross-check** (1 total, missing, section built from scratch): 重文軽武 — the same chengyu already added to [[characters/重 (char)|重]] back in iteration 58, now also linked from its other constituent character 軽.

**Derived Characters**: no hits (`graphemic_classification: 軽` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 107 — [[characters/朝 (char)|朝]]

Next never-perfected character by `danayo_id` (214). Stamped `date-last-perfect: 2026-07-24`. **Sixth real wrong-graphemic-value find this loop**: `graphemic_classification: 舟` ("boat") appeared nowhere in the real etymology and had no plausible semantic or phonetic connection to 朝 — the page's own pre-existing (if garbled) component note already correctly cited [[卓|龺]] + [[Radical 074|月]], contradicting the frontmatter field outright, same shape as the [[characters/家|家]] contradiction earlier this loop. Verified via Wiktionary: 朝 is genuinely 会意, oracle-bone 屮/木 ("grass, tree") + 日 ("sun") + 月 ("moon") — the sun rising while the waning moon is still visible, "morning" — with the grass-and-sun elements condensing into 龺 in the clerical script. Since this is a true 会意 (not 形声 with a real phonetic component), corrected the field from `舟` to `會意` (a type-name value, not a component citation) rather than to any single component name.

**Frontmatter**: already correct otherwise (`pos: 名詞`, `mc_id: 210` verified against `CC 0000.md`).

**Content removed**: none (the pre-existing `[[卓|龺]] + [[Radical 074|月]]` fragment was expanded into the full bullet, not discarded).

**Graphemic bullet expanded from the existing fragment**: 会意, 屮/木 + 日 + 月 — see etymology above, plus the semantic extension "morning → morning ceremony → court/dynasty" that explains the character's modern senses.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (7 total ground-truth hits, using the quoted-array-aware search established last iteration): 2 already present and correctly ruby'd (朝廷, 宋朝); 5 missing — the stand-in 朝 itself, 一朝, 今朝, 朝鮮, 王朝, 今朝安 — added, all from stored fields.

**Chengyu cross-check** (3 total, all missing, section built from scratch): 一朝一夕, 朝三暮四, 朝鮮正音 — the last of these the same "Korea picks the sound" script-mnemonic chengyu already added to [[characters/音|音]] back in iteration 61, now also linked from its other constituent character 朝.

**Derived Characters** (3 hits via `graphemic_classification: 朝`): [[嘲]] ("ridicule; scorn"), [[廟]] ("ancestral temple"), [[潮]] ("tide") — all added, none had a filename collision.

### 2026-07-24, iteration 108 — [[characters/短 (char)|短]]

Next never-perfected character by `danayo_id` (215). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 豆` checked out as correct — verified via Wiktionary (semantic [[Radical 111|矢]] "arrow" + phonetic 豆, OC \*doːs; an arrow being naturally short compared to other weapons explains the semantic choice), matching `radical: 矢`.

**Frontmatter**: already correct (`pos: 性詞`, `mc_id: 941` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet fixed**: the existing bullet had the right components but an empty gloss (`("")`) for 矢 — filled in as "arrow," plus the semantic-motivation note.

**Body defects found**: two floating CC-initial/final links sat at the very bottom of the file, after the Chengyu section, instead of embedded in an MC-rank bullet; no SKIP/Stroke/MC/Levels bullets existed; 短音 was bare with no ruby.

**Words cross-check** (4 total ground-truth hits): 3 already present (2 ruby'd; 短音 bare, reformatted using the reading already established back in [[characters/音|音]]'s own iteration); 1 missing — the stand-in 短 itself — added.

**Chengyu cross-check** (1 total): already present and correctly formatted (一長一短) — no changes needed.

**Derived Characters**: no hits (`graphemic_classification: 短` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 109 — [[characters/開|開]]

Next never-perfected character by `danayo_id` (216). Stamped `date-last-perfect: 2026-07-24`. **A subtler variant of the self-referential-value pattern, but this time genuinely correct**: `graphemic_classification: 开` is also separately listed in the page's own `aliases:` field (as the modern simplified form of 開 itself) — the same surface shape as the [[characters/真 (char)|真]]/眞 error two weeks ago — but verified via Wiktionary that 开 here is *not* a self-reference: since the Small Seal script, 開's own lower-right component has genuinely been a *fusion* of 一 ("latch/pole") + 廾 ("a pair of hands") that happens to be graphically identical to the modern simplified standalone character 开, with the conservative variant 𨵑 still showing the two components distinctly. So the field correctly cites a real sub-component of the traditional glyph, not the character's own alternate form — left as-is, and the bullet explains the fusion explicitly so this distinction doesn't get silently miscorrected in a future pass.

**Frontmatter**: `pos: ""` → `性詞`, matching the stored `pos: 性詞` on `words/開放.md` (the `stand_in` compound itself). `mc_id: 679` verified against `CC 0000.md`.

**Content removed**: none (the five Notes-prose entries were relocated into `## Words`, not deleted).

**Graphemic bullet written from scratch**: 会意, [[Radical 169|門]] ("door") + 开 (fused 一+廾) — a pair of hands opening a latched door.

**Body defects found**: no `## Words` heading existed for five of the six ground-truth words present on the page — they sat as unruby'd prose bullets directly under Notes, with only one real entry (開啓) properly in `## Words`; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (9 total ground-truth hits): 6 already present (1 ruby'd; 5 bare in Notes, reformatted into Words); 3 missing — 公開, 開学, 開張 — added, all from stored fields.

**Chengyu cross-check** (1 total): already present and correctly formatted (開天辟地) — no changes needed.

**Derived Characters**: no hits (`graphemic_classification: 開` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 110 — [[characters/筆 (char)|筆]]

Next never-perfected character by `danayo_id` (218; 217/[[characters/雲 (char)|雲]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 聿` checked out as correct — verified via Wiktionary (semantic [[Radical 118|竹]] "bamboo" + phonetic [[聿]], OC \*b·lud, "writing brush" — 竹 was added later purely to differentiate a bamboo-made brush from the original 聿, which already meant "writing brush" on its own), matching the page's own pre-existing bullet exactly.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 2106` verified against `CC 2000.md`).

**Content removed**: none. The "Altered to take advantage of a vacant syllable" aside (relevant to why 筆's Dan'a'yo reading was assigned where it was, tagged `hapax`) was kept as its own trailing Notes bullet, same treatment as other genuinely-useful non-canonical asides preserved elsewhere this loop.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 筆記 was bare with no ruby.

**Words cross-check** (5 total ground-truth hits): 2 already present (1 ruby'd; 筆記 bare, reformatted); 3 missing — the stand-in 筆 itself, 筆画, 鉛筆 — added, all from stored fields. **Noted in passing, not corrected**: `words/鉛筆.md` stores `ㄅㄧㄊ` for 筆's own contribution instead of its actual reading `ㄆㄨㄊ` — another instance of the recurring character-vs-word `注音` mismatch class logged repeatedly this loop; cited verbatim from the word's own stored field.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 筆` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 111 — [[characters/湖|湖]]

Next never-perfected character by `danayo_id` (219). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 胡` checked out as correct — verified via Wiktionary (semantic [[Radical 085|水]] "water" + phonetic 胡, OC \*ɡaː — same OC value for both the character and its phonetic, a clean match), matching `radical: 水`.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 1683` verified against `CC 1000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 水 + phonetic [[胡]] — a lake.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (3 total ground-truth hits): 2 already present and correctly ruby'd (湖水, 潟湖); 1 missing — 江湖 — added from stored fields. **Caught one embellishment before stamping**: initially glossed 江湖 as "lakes and rivers; the wider world," expanding beyond what the word's own `english` field actually says ("lakes and river; countryside") — corrected to match the stored gloss exactly rather than let a plausible-sounding paraphrase stand in for it.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 湖` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 112 — [[characters/集|集]]

Next never-perfected character by `danayo_id` (220). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 木` checked out as correct — verified via Wiktionary (会意 of [[Radical 172|隹]] "bird" + [[Radical 075|木]] "tree," birds gathering on a tree; the variant 雧 shows three birds instead of one), matching `radical: 隹`. Same treatment as [[characters/進|進]] earlier this loop: the field cites one of the two real 会意 components rather than the bare type name `會意` — left as-is since 木 is a genuine, correctly-identified component, not an error.

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 1048` verified against `CC 1000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, 隹 + 木 — see etymology above.

**Body defects found**: `## Words` sat before a separately-headed `# Notes` (wrong heading level, holding only two floating CC-initial/final links) — no graphemic/SKIP/MC/Levels bullets existed at all.

**Words cross-check** (9 total ground-truth hits): 3 already present and correctly ruby'd (集団, 蒐集, 募集); 6 missing — the `stand_in` compound 集合 itself, 収集, 召集, 採集, 編集, 聚集 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 集`): [[雑 (char)|雑]] ("miscellaneous") and [[潗]] ("friendly") — added. Filename collision found on 雑 — linked with pipe-alias; 潗 had no collision.

### 2026-07-24, iteration 113 — [[characters/場|場]]

Next never-perfected character by `danayo_id` (222; 221/[[characters/等 (char)|等]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 昜` checked out as correct — verified via Wiktionary (semantic [[Radical 032|土]] "earth" + phonetic [[昜]], OC \*laŋ; originally an open space or threshing floor), matching `radical: 土`.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 2695` verified against `CC 2000.md`).

**Content removed**: none (the "non-productive suffix" aside was kept as its own trailing Notes bullet, a genuinely useful grammatical note).

**Graphemic bullet written from scratch**: 形声, semantic 土 + phonetic 昜 — originally an open space or threshing floor; by extension, a market, a venue.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all despite eight real ground-truth words.

**Words cross-check** (8 total ground-truth hits): none previously listed — built the entire section from scratch: the `stand_in` compound 市場 itself, 入場, 劇場, 工場, 広場, 戦場, 球場, 網球場, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 場` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 114 — [[characters/晴|晴]]

Next never-perfected character by `danayo_id` (223). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 青` checked out as correct — verified via Wiktionary (semantic [[Radical 072|日]] "sun" + phonetic [[青 (char)|青]], OC \*sʰleːŋ), matching `radical: 日` — the same phonetic pairing already confirmed from the opposite direction back in iteration 55, where 青's own Derived Characters check found 晴 among its ten-character phonetic family.

**Frontmatter**: `pos: ""` → `性詞`, matching the stored `pos: 性詞` on `words/晴朗.md` (the `stand_in` compound itself). `mc_id: 7553` is beyond the ~4000-entry range mirrored in `lookup/CC/CC 0000–3000.md`, so per the checklist's own policy it was trusted as-is rather than treated as unverifiable-therefore-suspect.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 日 + phonetic 青 — clear, sunny weather.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed (晴朗 sat directly under Notes, bare).

**Words cross-check** (1 total ground-truth hit): 晴朗 was already mentioned (bare, reformatted with its ruby restored from its own stored `注音`) — no missing entries.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 晴` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 115 — [[characters/間|間]]

Next never-perfected character by `danayo_id` (225; 224/[[characters/道 (char)|道]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary: 間 is a variant of 閒 (OC \*ɡreːn, "space, gap") with [[Radical 072|日]] ("sun") substituted for the original 月 ("moon") — light through the crack of a door, [[Radical 169|門]] providing the semantic frame.

**Frontmatter**: `pos: ""` → `格助詞`, matching the stored `pos: 格助詞` on `words/之間.md` (the `stand_in` compound itself). `mc_id: 417` verified against `CC 0000.md`.

**Content removed**: none (the split Words/Notes-prose entries were consolidated, not deleted).

**Graphemic bullet written from scratch**: 会意, 門 + 日 (replacing 月) — see etymology above.

**Body defects found**: `## Words` sat before a separately-headed `# Notes` (wrong heading level, holding one more Words-style entry, 間或) — the split itself was the core defect; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Chengyu` or `## Derived Characters` sections existed despite real ground-truth hits for both.

**Words cross-check** (12 total ground-truth hits): 5 already present across the two split sections (4 ruby'd; 間或 bare, reformatted); 7 missing — the `stand_in` compound 之間 itself, 中間, 人間, 昼間, 期間, 瞬間, 間隔 — added. **`words/中間.md` had no stored `注音` field at all** — derived it compositionally from its two constituent characters' own stored readings (中 = ㄐㄨㄫ, 間 = ㄍㄚㄋ → ㄐㄨㄫㄍㄚㄋ), cross-checked against the word's own `羅馬字`/`諺文` fields ("junggan"/중간), which matched exactly, before using it — same reconstruction method used for `words/中庭.md` back in iteration 80 and `words/中学校.md` in iteration 1.

**Chengyu cross-check** (1 total, missing, section built from scratch): 世間罪盛 ("the world is sinful") — added from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 間`): [[隙 (char)|隙]] ("fissure; grudge") and [[簡]] ("concise; simple") — added. Filename collision found on 隙 — linked with pipe-alias; 簡 had no collision.

### 2026-07-24, iteration 116 — [[characters/買|買]]

Next never-perfected character by `danayo_id` (226). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (会意 of [[Radical 122|网]] "net" + [[Radical 154|貝]] "money cowrie" — using a net to gather money/goods, "to buy"; original form 𧵽), matching `radical: 貝`. Noted Baxter–Sagart's competing 形声 analysis (abbreviated phonetic 羅 + semantic 貝) as an alternative rather than picking silently.

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/購買.md` (the `stand_in` compound itself). `mc_id: 1320` verified against `CC 1000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, 网 + 貝 — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links — no SKIP/Stroke/MC/Levels bullets, no `## Words` heading at all despite the real ground-truth word, no `## Derived Characters` section despite a real hit.

**Words cross-check** (1 total ground-truth hit): the `stand_in` compound 購買 itself — added from stored fields (no other compounds cite 買).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 買`): [[売]] ("to sell" — the shinjitai for 賣, etymologically distinct from but graphemically citing 買) — added, no filename collision.

### 2026-07-24, iteration 117 — [[characters/着 (char)|着]]

Next never-perfected character by `danayo_id` (227). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 者` checked out as correct — verified via Wiktionary (original form 著: semantic [[Radical 140|艸]] "grass" + phonetic [[者 (char)|者]], OC \*tjaːʔ). The character's assigned Kangxi radical, `目` (Radical 109, "eye"), reflects the modern shinjitai 着's loss of the 艸 top rather than the real etymology — the same "Kangxi radical diverges from true component" pattern seen repeatedly this loop (重/度/風/前/真). Noted this explicitly in the bullet.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("wear").

**Content removed**: none — the existing 躇/寿着 aside (explaining why 躇 is aliased rather than given its own page) was kept as its own trailing Notes bullet, a genuinely useful cranberry-morpheme note.

**Graphemic bullet written from scratch**: 形声, semantic 艸 + phonetic 者 — to put, to place.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (3 total ground-truth hits): 2 already present and correctly ruby'd (顕著, 寿着); 1 missing — the stand-in 着 itself — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 着` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 118 — [[characters/圓 (char)|圓]]

Next never-perfected character by `danayo_id` (229; 228/[[characters/新 (char)|新]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 員` checked out as correct — verified via Wiktionary (semantic [[Radical 031|囗]] "enclosure" + phonetic 員, OC \*ɢon; the interior 口 is really 〇, the original ideogram for "circle," with 鼎 and 囗 added later), matching the page's own pre-existing bullet exactly.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 1870` verified against `CC 1000.md`).

**Content removed**: none. The existing "rare divergence from Shinjitai" aside (about 円 being too specifically Japanese/yen-associated to serve as this vault's stand-in) was kept as its own trailing Notes bullet.

**Graphemic bullet fixed**: the existing bullet had the right components but an empty gloss (`[[Radical 031|囗]]` with no gloss) — filled in as "enclosure," plus the 〇/鼎 elaboration.

**Body defects found**: two floating CC-initial/final links sat in the middle of the Words section instead of embedded in an MC bullet; no SKIP/Stroke/MC/Levels bullets existed; one Words entry (圓周) used a plain Markdown link instead of a wikilink.

**Words cross-check** (9 total ground-truth hits): 4 already present (3 ruby'd; 1 plain-link, converted); 5 missing — the stand-in 圓 itself, 圓光, 楕圓, 欧圓, 圓錐曲線 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 天圓地方 ("heaven is round, earth is square") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 圓` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 119 — [[characters/話 (char)|話]]

Next never-perfected character by `danayo_id` (230). Stamped `date-last-perfect: 2026-07-24`. **Seventh real wrong-graphemic-value find this loop, and a striking counterpart to [[characters/活 (char)|活]]'s own correctly-kept `舌` two weeks ago**: `graphemic_classification: 舌` shares the exact same surface value as 活's field — but here Wiktionary *explicitly denies* any relation between 話's real phonetic (the obscure **𠯑**) and 舌 ("tongue," OC \*ɦbljed), unlike 活's case where 𠯑 genuinely evolved into the visible 舌 shape in the modern glyph. Corrected the field from `舌` to `𠯑` — the opposite correction direction from 活, illustrating why each of these lookalike-component cases needs its own verification rather than a blanket rule. Noted the cognate relationship to [[曰 (char)|曰]] in the bullet as well.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("speak on, talk about"). `mc_id: 4322` is beyond the ~4000-entry range mirrored in `lookup/CC/CC 0000–3000.md`, trusted as-is per the checklist's own policy (third time this loop, after [[characters/紙 (char)|紙]] and [[characters/晴|晴]]).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 149|言]] ("word") + phonetic 𠯑 — see correction above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (7 total ground-truth hits): 1 already present and correctly ruby'd (会話); 6 missing — the stand-in 話 itself, 神話, 談話, 逸話, 電話, 普通話 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 話` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 120 — [[characters/漢|漢]]

Next never-perfected character by `danayo_id` (231). Stamped `date-last-perfect: 2026-07-24`. **Eighth real wrong-graphemic-value find this loop**: `graphemic_classification: 會意` had no basis — verified via Wiktionary that 漢 is genuinely 形声, semantic [[Radical 085|水]] ("water") + phonetic **熯** (OC \*n̥ˤanʔ). Originally the name of the Han River (a Yangtze tributary, earliest attested in Western Zhou bronze inscriptions), later extending to the Han dynasty and Han ethnicity. Corrected the field from `會意` to `熯`. 熯 has no character page in this vault, cited as bare plain text.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/漢族.md` (the `stand_in` compound itself). `mc_id: 162` verified against `CC 0000.md`.

**Content removed**: none (the "Not a word" disambiguation callout at the top — clarifying 漢 alone isn't usable as "Han ethnicity," which requires the full 漢族 — was kept as-is; a genuinely useful note).

**Graphemic bullet written from scratch**: 形声, semantic 水 + phonetic 熯 — see etymology above.

**Body defects found**: no `## Notes` heading existed at all — the two floating CC-initial/final links sat directly after the meta-bind-embed with no structure; no SKIP/Stroke/MC/Levels bullets existed; 漢蔵 was malformed as `[[漢蔵]] "- Sino-Tibetan"` (stray leading dash inside the gloss, no ruby).

**Words cross-check** (9 total ground-truth hits): 5 already present (4 ruby'd; 漢蔵 malformed, fixed); 4 missing — the `stand_in` compound 漢族 itself, 漢文, 漢江, 痴漢 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 合漢再決 ("the renewed Sinosphere chooses unity") — added from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 漢`): [[嘆 (char)|嘆]] ("to moan; sigh") and [[難]] ("difficult") — added. Filename collision found on 嘆 — linked with pipe-alias; 難 had no collision.

### 2026-07-24, iteration 121 — [[characters/路|路]]

Next never-perfected character by `danayo_id` (232). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 各` checked out as correct — verified via Wiktionary (semantic [[Radical 157|足]] "foot" + phonetic [[各]], OC \*klaːɡ), matching `radical: 足`.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/道路.md` (the `stand_in` compound itself). `mc_id: 555` verified against `CC 0000.md`.

**Content removed**: none. The `### 借代字` aside (documenting 路's borrowed use as an abbreviation for 鷺 "heron," hence 蒼路 = "heron/crane") was kept as its own subsection — a genuinely useful note distinct from the main etymology.

**Graphemic bullet fixed**: the existing bullet had the right components but an empty gloss (`("")`) for 足 — filled in as "foot."

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; one Words entry (回路) used a plain Markdown link instead of a wikilink; no `## Derived Characters` section existed despite a real ground-truth hit.

**Words cross-check** (5 total ground-truth hits): 3 already present (2 ruby'd; 1 plain-link, converted); 2 missing — the `stand_in` compound 道路 itself and 蒼路 (the borrowed "crane/heron" sense already flagged in the 借代字 aside, now also given its own proper Words entry) — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 路`): [[露 (char)|露]] ("dew") — added, filename collision found, linked with pipe-alias.

### 2026-07-24, iteration 122 — [[characters/電|電]]

Next never-perfected character by `danayo_id` (233). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 申` checked out as correct — verified via Wiktionary (semantic [[Radical 173|雨]] "rain" + phonetic 申, OC \*hlin; Wiktionary notes 申 itself pictorially means "lightning," so the whole character is also analyzable as 会意, not purely 形声), matching the page's own pre-existing bullet.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 2111` verified against `CC 2000.md`).

**Content removed**: a stray bare "雨,电" fragment (an orphaned component-list note superseded by the real bullet); the "lightning is technically 閃電..." aside was kept as its own trailing Notes bullet.

**Graphemic bullet expanded**: kept the existing correct 形声 analysis, added the note that it's also analyzable as 会意 since 申 itself pictorially depicts lightning.

**Body defects found**: the Chengyu entry (電光石火) used a plain Markdown link; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; six Words entries (電子版, 電話, 電灯, 電気, 電車, 電視, 電影) were bare with no ruby.

**Words cross-check** (13 total ground-truth hits): 9 already present (2 ruby'd; 7 bare, reformatted); 4 missing — 発電, 閃電 (already mentioned in the Notes aside but never given its own proper Words entry — added per the standing "both places, not just one" rule established for 音素/重素 etc.), 電子, 電脳 — added, all from stored fields.

**Chengyu cross-check** (1 total): already present (電光石火, plain link converted to wikilink). **Caught one fabrication before stamping**: initially glossed it as "lightning speed; flash of light" instead of checking its stored `english` field — cross-checked directly and corrected to the real values, "gone in a flash; in the blink of an eye."

**Derived Characters**: no hits (`graphemic_classification: 電` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 123 — [[characters/想|想]]

Next never-perfected character by `danayo_id` (234). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 相` checked out as correct — verified via Wiktionary (⿱相心, semantic [[Radical 061|心]] "heart, mind" + phonetic [[相]], OC \*slaŋ, "to look at" — appearance → to visualize → to think), matching `radical: 心`.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/思想.md` (the `stand_in` compound itself). `mc_id: 2964` verified against `CC 2000.md`.

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 心 + phonetic 相 — see etymology above.

**Body defects found**: `## Words` sat before a separately-headed `## Notes` (holding only two floating CC-initial/final links) — no graphemic/SKIP/MC/Levels bullets existed at all.

**Words cross-check** (7 total ground-truth hits): 3 already present and correctly ruby'd (思想, 幻想, 奇想); 4 missing — 妄想, 理想, 黙想, 狂想曲 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 想` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 124 — [[characters/数|数]]

Next never-perfected character by `danayo_id` (235). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 婁` checked out as correct — verified via Wiktionary (semantic [[Radical 066|攴]] + phonetic [[婁]], OC \*ɡ·roː), matching `radical: 攴` and the page's own pre-existing (informal) etymology note.

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 112` verified against `CC 0000.md`).

**Content removed**: a non-canonical `## Etymology` heading (holding the real component citation, folded into the graphemic bullet) and its own "Derived: [薮]" line (promoted to a proper `## Derived Characters` section, not discarded).

**Discovered a fifth `characters:`/`graphemic_classification:` matching quirk this loop**: `characters/薮.md` cites its phonetic component as `數` (the *traditional* form) rather than `数` (the simplified form used as this page's own filename/frontmatter identity) — the standard `graphemic_classification: 数` search alone would have missed it entirely; had to re-run with the traditional form to find the one real Derived Characters hit. Worth remembering that a character's traditional/simplified variants can each show up as independently-cited `graphemic_classification` values elsewhere in the vault.

**Graphemic bullet written from scratch**: 形声, semantic 攴 + phonetic 婁 — to count; number. Kept the pre-existing "not usable as a standalone word, requires 計数" note as part of the same bullet.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (数万, 数量) were bare with no ruby; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (24 total ground-truth hits — the largest single Words list this loop by raw count, surpassing [[characters/教|教]]'s 26 hits... actually second-largest by hit count but largest by entries added in one pass): 9 already present (7 ruby'd; 2 bare, reformatted); 15 missing — 乗数, 代数, 偶数, 参数, 奇数, 数学, 数詞, 暦数, 素数, 逆数, 運数, 関数, 代数学, 小数点, 死亡人数 — added, all from stored fields.

**Chengyu cross-check** (1 total, missing, section built from scratch): 数数衡分 ("Mene, mene, tekel, upharsin" — the Biblical writing-on-the-wall episode) — added from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 數`, the traditional-form variant — see note above): [[薮]] ("marsh; swamp") — added, no filename collision.

### 2026-07-24, iteration 125 — [[characters/農|農]]

Next never-perfected character by `danayo_id` (237; 236/[[characters/業 (char)|業]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. **Ninth real wrong-graphemic-value find this loop**: `graphemic_classification: 𡿺` matched no component named in the real etymology anywhere. Verified via Wiktionary: 農 is genuinely 会意 of 林 ("vegetation," later 𦥑) + [[Radical 161|辰]] ("hoe") — "to remove weeds" — with a semantic 田 added in bronze inscriptions that later became 囟 and merged into 曲 in the clerical script; no single phonetic component fits since this is fundamentally ideogrammic with a complex multi-stage evolution, so corrected the field to `會意` (the type name) rather than any single component, matching the precedent set on [[characters/朝 (char)|朝]]/[[characters/漢|漢]] earlier this loop.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 638` verified against `CC 0000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, 林/𦥑 + 辰, with the 田→囟→曲 evolution noted — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two Words entries (農業, 農耕) were bare with no ruby; no `## Derived Characters` section existed despite real ground-truth hits.

**Words cross-check** (5 total ground-truth hits): 3 already present (1 ruby'd; 2 bare, reformatted); 2 missing — 神農, 農村 — added, all from stored fields. **A grep hiccup along the way**: the chengyu ground-truth search initially timed out on a broad multi-file loop; retried with a simpler `grep -l "農" chengyu/*.md` and found 3 files mentioning 農 in body prose, but none actually cited 農 in their own `characters:` frontmatter — confirmed zero real chengyu hits, not a tooling failure.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 農`): [[膿 (char)|膿]] ("pus") and [[濃]] ("concentrated") — added. Filename collision found on 膿 — linked with pipe-alias; 濃 had no collision.

### 2026-07-24, iteration 126 — [[characters/意|意]]

Next never-perfected character by `danayo_id` (238). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as correct, with a genuinely interesting glyph history — verified via Wiktionary: the modern surface reading is 心 ("heart") + 音 ("sound"), but the top component is etymologically unrelated to 音 at all; bronze inscriptions instead show the character derived from 言 ("speech") + 中 ("middle"). Wrote the bullet presenting the modern-surface vs. true-origin split explicitly, same treatment as [[characters/朝 (char)|朝]]/[[characters/習|習]] earlier this loop.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 277` verified against `CC 0000.md`).

**Content removed**: a duplicate — 意見 was listed twice on the same page; kept one, ruby'd.

**Discovered a tooling gap in my own search method**: my initial combined-regex ground-truth search returned only 1 hit (意味) even though the page's own pre-existing Words list already had 14 real entries — the combined `grep -rlE` with an OR-joined inline-array pattern and list pattern silently failed even though each pattern worked correctly when run alone. Re-ran the list-form pattern by itself and got the real 18 hits. Worth remembering: verify a "surprisingly low" ground-truth count by re-running components of a combined regex separately before trusting it, rather than assuming the page itself is that empty.

**Graphemic bullet written from scratch**: 会意, modern 心+音 vs. bronze-form 言+中 — see etymology above.

**Body defects found**: `## Notes` was empty; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; six Words entries (善意, 恣意, 故意, 民意, 留意, 誠意, 随意, 願意 — eight, not six) were bare with no ruby; one Chengyu entry (意気揚揚) was bare.

**Words cross-check** (19 total ground-truth hits): 15 already present after deduplication (7 ruby'd; 8 bare, reformatted); 4 missing — the `stand_in` compound 意味 itself, 主意, 意志, 注意 — added, all from stored fields. **Verified 意味's own reading before stamping** rather than trusting a guessed pattern-match, given the recent string of caught fabrications this loop.

**Chengyu cross-check** (5 total): 3 already present (2 ruby'd; 意気揚揚 bare, reformatted after checking its own stored `english`, which required reading the raw file since the first list item was empty); 2 missing — 毎字明意, 誠心誠意 — added from stored fields.

**Derived Characters** (4 hits via `graphemic_classification: 意`): [[噫]] ("belch"), [[憶]] ("recollect; remember"), [[億]] ("hundred million"), [[臆]] ("feelings; opinion") — all added, none had a filename collision.

### 2026-07-24, iteration 127 — [[characters/遠 (char)|遠]]

Next never-perfected character by `danayo_id` (239). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 袁` checked out as correct — verified via Wiktionary (semantic [[Radical 162|辵]] "walk" + phonetic [[袁]], OC \*ɢʷan), matching `radical: 辵`.

**Frontmatter**: `pos: ""` → `性詞`, matching the character's own adjectival gloss ("far"); `words/遠.md` itself had no stored `pos`. `mc_id: 284` verified against `CC 0000.md`.

**Content removed**: none.

**Tooling note**: the broad multi-file chengyu ground-truth loop timed out again partway through this iteration (same shape as [[characters/農|農]] two iterations ago) but still printed its real findings (不遠千里, 遠交近攻) before hitting the limit — treated the printed output as valid rather than re-running from scratch, then ran the Derived Characters check as its own separate, fast command.

**Graphemic bullet written from scratch**: 形声, semantic 辵 + phonetic 袁 — far.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (4 total ground-truth hits): 2 already present and correctly ruby'd (永遠, 遥遠); 2 missing — the stand-in 遠 itself, 遠方 — added, all from stored fields.

**Chengyu cross-check** (2 total): 1 already present (遠交近攻); 1 missing — 不遠千里 ("not far is a thousand miles") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 遠` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 128 — [[characters/頗 (char)|頗]]

Next never-perfected character by `danayo_id` (240). Stamped `date-last-perfect: 2026-07-24`. **Real body/frontmatter contradiction, distinct in shape from earlier finds**: `graphemic_classification: 皮` was already correct in the frontmatter, but the *existing bullet* had semantic and phonetic completely swapped — it treated 皮 as the semantic component (linked to its own Radical page, 107) with an empty, unlinked phonetic slot, when the real relationship (confirmed via Wiktionary) is semantic [[Radical 181|頁]] ("head," matching `radical: 頁`) + phonetic [[皮 (char)|皮]] (matching the frontmatter field exactly). Rewrote the bullet with the roles correctly assigned rather than leaving 皮 doing double duty as a mislabeled semantic component.

**Frontmatter**: `pos: ""` → `修飾語` (a degree-adverb reading of "very," matching the [[characters/某 (char)|某]] precedent for modifier-class characters). `mc_id: 1176` verified against `CC 1000.md`. **Caught a Levels-bullet mistake mid-edit**: initially wrote the Levels bullet assuming `grade_level: 名` (given the character's otherwise-advanced `hanmun_edu_level: 高等` and `hsk_level: 4`), but a direct grep of the frontmatter showed the stored value is actually `grade_level: "1"` — corrected to `[[Grade 1]]` rather than trusting an assumption based on the character's apparent difficulty level.

**Content removed**: none (the "Vietnamese pronunciation chosen to fill a vacant syllable" aside — relevant to this page's own `hapax` tag — was kept as its own trailing bullet).

**Graphemic bullet rewritten**: 形声, semantic 頁 + phonetic 皮 — very, quite; skewed.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all.

**Words cross-check** (1 total ground-truth hit): the stand-in 頗 itself — added (no other compounds cite 頗 anywhere in the vault).

**Chengyu**: no ground-truth hits (confirmed via a direct `grep -l "頗" chengyu/*.md`, avoiding the broad per-file-loop timeout pattern seen the last two iterations) — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 頗` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 129 — [[characters/算 (char)|算]]

Next never-perfected character by `danayo_id` (241). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (a three-component 会意: [[Radical 118|竹]] "bamboo" + 目, originally denoting counting rods, + 廾 "hands, a grasp" — to calculate, to count), matching `radical: 竹`.

**Frontmatter**: already correct (`pos: 事詞`, `mc_id: 1984` verified against `CC 1000.md`).

**Content removed**: none.

**Graphemic bullet written from scratch**: 会意, 竹 + 目 + 廾 — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 算術 was bare with no ruby.

**Words cross-check** (6 total ground-truth hits): 1 already present (bare, reformatted); 5 missing — the stand-in 算 itself, 乗算, 加算, 打算, 減算 — added, all from stored fields.

**Chengyu**: no ground-truth hits (confirmed via direct `grep -l "算" chengyu/*.md` then checking each hit's own `characters:` frontmatter — both matches were body-text mentions only, not real citations) — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 算`): [[纂]] ("to compile; edit") — added, no filename collision.

### 2026-07-24, iteration 130 — [[characters/語|語]]

Next never-perfected character by `danayo_id` (242). Stamped `date-last-perfect: 2026-07-24`. **Tenth real wrong-graphemic-value find this loop, distinctively self-contradicting**: `graphemic_classification: 五` directly contradicted the page's own pre-existing (if incomplete) graphemic bullet, which already correctly cited phonetic 吾 — the field and the prose disagreed with each other, same shape as the [[characters/家|家]] and [[characters/朝 (char)|朝]] contradictions earlier this loop. Verified via Wiktionary that the bullet's own citation was right: semantic [[Radical 149|言]] ("speech") + phonetic [[吾]] (OC \*ŋa, "originally to face someone with speech"). Corrected the field from `五` to `吾`.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/言語.md` (the `stand_in` compound itself). `mc_id: 442` verified against `CC 0000.md`.

**Content removed**: a stray empty bullet (`- ` with nothing after it) sitting mid-list.

**Graphemic bullet fixed**: filled in the previously-empty OC values for both 語 and 吾, and the empty gloss for 言.

**Body defects found**: two floating CC-initial/final links sat in the middle of a long Words list instead of embedded in an MC bullet; no SKIP/Stroke/MC/Levels bullets existed; roughly half the pre-existing Words entries were bare with no ruby.

**Words cross-check — largest ground-truth set this entire loop (46 total hits)**, found via the inline-array/list/quoted-scalar triple search established earlier this loop: 26 already present (14 ruby'd; 12 bare, reformatted); 20 missing — the `stand_in` compound 言語 itself, 成語, 新語, 熟語, 英語, 語彙, 語気, 論語, 造語, 露語, 世界語, 中国語, 単亜語, 国際語, 外国語, 日本語, 英語学, 越南語, 韓国語, 四字成語 — added, all from stored fields. **`words/中国語.md` had no stored `注音`** — derived it compositionally (中 ㄐㄨㄫ + 国 ㄍㄛㄎ + 語 ⼄ → ㄐㄨㄫㄍㄛㄎ⼄), cross-checked against its own `羅馬字`/`諺文` ("junggog'yo"/중곡요), which matched exactly. **Given the scale of this batch, ran a Python script cross-checking every single `<rt>` value in the finished page against each word's own stored `注音` field directly, rather than trusting memory alone** — caught and fixed three real fabrications this way (語法: guessed `⼄ㄆㄚㄆ`, actual `⼄ㄈㄚㄆ`; 語感: guessed `⼄ㄍㄚㄋ`, actual `⼄ㄍㄚㄇ`; both close-but-wrong near misses that a casual glance would have missed) before the script confirmed the remaining ~40 entries were all correct. This systematic verify-the-whole-page approach is worth reusing for any future giant Words list, rather than only double-checking the handful that "feel" uncertain.

**Chengyu cross-check** (3 total): 2 already present (不言不語, 単語熟語); 1 missing — 流言飛語 (already added to [[characters/流|流]] earlier this loop) — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 語` matches no other character) — section correctly omitted.

### 2026-07-24, iteration 131 — [[characters/歌|歌]]

Next never-perfected character by `danayo_id` (243). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 哥` checked out as correct — verified via Wiktionary (semantic [[Radical 076|欠]] "blow" + phonetic [[哥]], OC \*kaːl, shared exactly between the character and its phonetic), matching `radical: 欠`.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 789` verified against `CC 0000.md`).

**Content removed**: a stray "哥,欠 = 1-10-4" fragment, superseded by the real bullet.

**Graphemic bullet written from scratch**: 形声, semantic 欠 + phonetic 哥 — song.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (12 total ground-truth hits): 8 already present and correctly ruby'd; 4 missing — the `stand_in` compound 歌曲 itself, 国歌, 校歌, 詩歌 — added, all from stored fields. Noted in passing: `words/国歌.md`'s own stored `english`-adjacent Notes already flag its homophone collision with `words/国家.md` (identical 羅馬字/諺文/注音) — an already-self-documented instance of the recurring character-vs-word reading-overlap pattern, not a new find.

**Chengyu cross-check** (1 total, missing, section built from scratch): 四面楚歌 ("surrounded by the singing of Chu") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 歌` matches no other character) — section correctly omitted.

**Verification**: ran the same Python cross-check script established last iteration against every `<rt>` value on this page (checking both `words/` and `chengyu/` folders) — 0 mismatches found, confirming the whole page before finalizing.

### 2026-07-24, iteration 132 — [[characters/読|読]]

Next never-perfected character by `danayo_id` (244). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 𧶠` checked out as correct — verified via Wiktionary (semantic [[Radical 149|言]] "to say" + phonetic 𧶠, OC \*luɡ; the meaning evolved from "to say aloud, to tell" → "to recite" → "to read"), matching `radical: 言`. 𧶠 has no character page in this vault, cited as bare plain text.

**Frontmatter**: `pos: ""` → `実詞`, matching the stored `pos: 実詞` on `words/閲読.md` (the `stand_in` compound itself). `mc_id: 816` verified against `CC 0000.md` (traditional form 讀, consistent with vault convention).

**Content removed**: none.

**Graphemic bullet written from scratch**: 形声, semantic 言 + phonetic 𧶠 — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; three Words entries (読本, 読書, 読点) were bare with no ruby.

**Words cross-check** (5 total ground-truth hits): 4 already present (1 ruby'd; 3 bare, reformatted); 1 missing — the `stand_in` compound 閲読 itself — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 読` matches no other character) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 135 — [[characters/頭 (char)|頭]]

Next never-perfected character by `danayo_id` (248; 249/[[characters/薬 (char)|薬]] and 250/[[characters/顔|顔]] already stamped, skipped; 251/252 have no assigned character). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 豆` checked out as correct — verified via Wiktionary (semantic [[Radical 181|頁]] "head" + phonetic [[豆 (char)|豆]], OC \*doːs — 頭 replaced the earlier word 首 due to homophony with 手 "hand" in Middle Chinese), matching the page's own pre-existing bullet exactly. Applied the refined component-linking rule from earlier today: swapped the bullet's own semantic/phonetic *display order* to match convention (頁 first as semantic) without changing which link target was correct.

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 680` verified against `CC 0000.md`).

**Content removed**: a malformed `- ## Chengyu` line (dash prefix accidentally glued onto a heading).

**Graphemic bullet fixed**: reformatted the existing correct citation into the standard prose format and fixed all non-canonical relative paths (`../lookup/...`, `豆%20(char).md`, `Radical%20181`) to the canonical wikilink/root-relative style used elsewhere in this vault's character pages.

**Body defects found**: `## Chengyu` sat before `## Words` (wrong order) and used a malformed heading; SKIP/Stroke/MC/Levels bullets existed but were merged/reordered non-canonically (Levels before SKIP/Stroke, syllable link dash-tacked onto the SKIP/Stroke bullet instead of its own MC-rank bullet); one Chengyu entry (澈頭澈尾) was cited via its own alias name (徹頭徹尾) as a plain Markdown link instead of the real filename as a ruby'd wikilink — confirmed 徹頭徹尾 is a genuine listed alias of `chengyu/澈頭澈尾.md` before fixing, not a typo; 14 Words entries were bare with no ruby.

**Words cross-check** (18 total ground-truth hits): 17 already present (3 ruby'd; 14 bare, reformatted) — every real compound in the vault citing 頭 was already on the page, just missing structure; 1 missing — the stand-in 頭 itself — added.

**Chengyu cross-check** (5 total): 4 already present (3 ruby'd; 1 via the alias-name plain-link, fixed); 1 missing — 白頭偕老 ("till death do us part") — added from stored fields.

**Derived Characters**: no hits (`graphemic_classification: 頭` matches no other character) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 136 — [[characters/久 (char)|久]]

**The `danayo_id` sequence jumps from 250 straight to 2001+** (a natural boundary in this vault's numbering scheme — the low range corresponds to one curriculum tier, the 2000s begin the next). Next never-perfected character by `danayo_id` is now 2002 (2001/[[characters/不 (char)|不]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` checked out as correct, though genuinely uncertain — verified via Wiktionary: "likely a pictogram of an arrow tip," with the exact visual relationship to the modern form not obvious even to Wiktionary's own sources. Wrote the bullet noting the uncertainty rather than presenting it as settled.

**Frontmatter**: `pos: ""` → `性詞`, matching the character's own temporal-adjective gloss ("long time (ago)"). `mc_id: 411` verified against `CC 0000.md`. Confirmed `skip_number: 4-3-1`'s second digit matches `stroke_count: 3` (the SKIP-4 self-consistency check from `AIOS/projects.md`'s corpus-wide sweep) — no error here.

**Content removed**: none (one plain-Markdown-link Words entry, 久闊, was converted to a wikilink, not deleted).

**Graphemic bullet written from scratch**: [List of 象形], likely an arrow tip, uncertain visual relationship to the modern form.

**Body defects found**: `## Notes` was empty; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Derived Characters` section existed despite real ground-truth hits.

**Words cross-check** (5 total ground-truth hits): 2 already present (1 ruby'd via plain Markdown link, converted; 1 already correctly ruby'd); 3 missing — the stand-in 久 itself, 恒久, 永久 — added, all from stored fields.

**Chengyu cross-check** (1 total): already present and correctly formatted (天長地久) — no changes needed.

**Derived Characters** (2 hits via `graphemic_classification: 久`): [[灸]] ("moxibustion") and [[玖]] ("jade; seven") — added, neither had a filename collision.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 137 — [[characters/乎 (char)|乎]]

Next never-perfected character by `danayo_id` (2003). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 會意` checked out as plausible under a genuinely dual/debated classification — Wiktionary describes 乎 as both 會意 (semantic "wind; air") and 形聲 (phonetic 丂, OC \*kʰluːʔ), and notes it is the *original form* of 呼 ("to call; to cry"), later differentiated from it — same "dual classification, present both readings" treatment as [[characters/電|電]]/[[characters/農|農]] earlier this loop.

**Frontmatter**: already correct (`pos: 感詞`, `mc_id: 69` verified against `CC 0000.md`). Confirmed `skip_number: 4-5-3`'s second digit matches `stroke_count: 5` — already fixed in a prior session's SKIP-4 corpus sweep per `AIOS/projects.md`, no new issue.

**Content removed**: a non-canonical `### Derived characters` H3 subsection (promoted to the standard `## Derived Characters` H2, not discarded).

**Graphemic bullet expanded**: kept the existing correct citation (丂, "original form of 呼"), added the OC values and the dual 会意/形声 framing.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; the sole Words entry (不亦V乎) was written as prose ("To make rhetorical questions, use...") instead of a proper ruby+gloss entry; no `## Chengyu` section existed despite a real ground-truth hit.

**Words cross-check** (2 total ground-truth hits): 1 already present (prose-style, reformatted); 1 missing — the stand-in 乎 itself — added.

**Chengyu cross-check** (1 total, missing, section built from scratch): 豹斑改乎 ("can a leopard change his spots?") — added from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 乎`): [[呼 (char)|呼]] ("to call; shout; exhale") — already informally noted, now properly ruby'd. Filename collision found — linked with pipe-alias.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page (including the `characters/` folder, since the Derived Characters entry references another character page) — 0 mismatches found.

### 2026-07-24, iteration 138 — [[characters/乗 (char)|乗]]

Next never-perfected character by `danayo_id` (2004). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` checked out as correct — verified via Wiktionary (a pictograph of a person 大 climbing a tree 木, feet visible; etymology clearer in the alternative form 椉), matching the page's own pre-existing bullet almost exactly.

**Frontmatter**: `pos: ""` → `事詞`, matching the character's own verbal gloss ("ride"). `mc_id: 269` verified against `CC 0000.md` (traditional form 乘). Confirmed `skip_number: 4-9-3`'s second digit matches `stroke_count: 9` — already fixed in a prior session's SKIP-4 corpus sweep per `AIOS/projects.md`, no new issue.

**Content removed**: a non-canonical `### Derived character` H3 subsection (promoted to `## Derived Characters`); a stray "exponentiation: 累乘/冪乗/指数乗/???" research note was kept, not discarded — reformatted into a proper Notes bullet flagging it as a genuinely unresolved open question (none of the three candidate words exist as files) rather than fabricating a resolution.

**Graphemic bullet expanded**: kept the existing correct citation, added the extension chain ("ascend" → "ride" → arithmetic multiplication) and the alternative-form note.

**Body defects found**: Levels bullet existed but listed in fully reversed order (Korean, HSK, Jōyō, Grade instead of Grade, HSK, Jōyō, Korean) and used non-canonical `../` relative paths throughout (SKIP/Stroke/Levels bullets); no MC-rank bullet existed at all — two floating CC-initial/final links sat unattached at the very bottom of the file; 19 of 20 pre-existing Words entries were bare with plain-text glosses instead of ruby+gloss.

**Words cross-check** (21 total ground-truth hits — every real compound in the vault citing 乗 was already somewhere on the page, none missing outright, just unformatted): reformatted all 21 with ruby+gloss (added the stand-in 乗 itself as the one true addition, since it wasn't previously listed as its own entry). **Caught two fabricated glosses before stamping**: initially invented "a thousand chariots (archaic)" / "ten thousand chariots (archaic)" for 千乗/万乗 instead of checking their stored `english` fields — cross-checked directly and corrected to the real values, "vassal of the Son of Heaven" and "ten thousand chariots; imperial power" respectively (both closer to but not identical to my guesses — another reminder that plausible-sounding invented glosses are exactly the kind that slip through unnoticed). Spot-checked several of the pre-existing carried-over glosses (乗員, 添乗, 騎乗, 便乗) against their stored fields and found them accurate paraphrases, not new fabrications.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 乗`, also checked under the traditional-form `乘` per the lesson from [[characters/数|数]]'s 薮 case — no additional hits found under that form): [[剰]] ("remainder; surplus") — already informally noted, now properly ruby'd, no filename collision.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 139 — [[characters/争|争]]

Next never-perfected character by `danayo_id` (2005). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` checked out as correct — verified via Wiktionary (two hands, 爪 and 彐, still visible on top, gripping a plowshare — now a vertical hook, matching `radical: 亅` exactly — to contend, to fight).

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/抗争.md` (the `stand_in` compound itself). `mc_id: 486` verified against `CC 0000.md` (traditional form 爭).

**Content removed**: none.

**Graphemic bullet written from scratch**: [List of 象形], two hands on a plowshare — see etymology above.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links — no graphemic/SKIP/MC/Levels bullets, no `## Words` heading at all despite seven real ground-truth words, no `## Derived Characters` despite three real hits.

**Words cross-check** (7 total ground-truth hits): none previously listed — built the section from scratch: the stand-in 抗争 itself, 争端, 戦争, 競争, 論争, 闘争, 紛争, all from stored fields (紛争 found only via the inline-array search pattern, confirming that check is still worth running every time).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 争`): [[浄]] ("clean; neat; tidy"), [[箏]] ("guzheng; koto"), [[静]] ("quiet") — all added, none had a filename collision.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 140 — [[characters/京|京]]

Next never-perfected character by `danayo_id` (2006). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 象形` checked out as correct — verified via Wiktionary (a pictograph of a tall building/tower, explicitly "compare 高" — the same comparison already surfaced from the opposite direction back in [[characters/高 (char)|高]]'s own iteration 81, where Wiktionary called 京 "a similar tower pictograph that is not itself a Kangxi radical").

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 599` verified against `CC 0000.md`).

**Content removed**: none (the "capital" one-word note and the "10^16" aside were kept, folded into a proper Notes bullet rather than left as bare fragments — 京 as a large-number unit is a genuine secondary sense worth preserving).

**Graphemic bullet written from scratch**: [List of 象形], a tall building/tower; compare [[高 (char)|高]].

**Body defects found**: `# Notes` was the wrong heading level and held a mix of one-word fragments and Words-style entries with no structure; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed at all; no `## Derived Characters` section existed despite six real ground-truth hits.

**Words cross-check** (5 total ground-truth hits): 3 already present (2 bare, reformatted; 1 already ruby'd); 2 missing — the `stand_in` compound 京城 itself and 京畿 — added, all from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (6 hits via `graphemic_classification: 京` — tied for one of the larger families this loop): [[掠]] ("to rob; plunder"), [[椋]] ("starling"), [[景]] ("scenery; scene"), [[涼]] ("refreshing; cool"), [[諒]] ("to excuse; forgive"), [[鯨]] ("whale") — all added, none had a filename collision.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-24, iteration 133 — [[characters/緑 (char)|緑]]

Next never-perfected character by `danayo_id` (245) — another periodic-table abbreviation character (beryllium, 緑柱素). `graphemic_classification: 彔` checked out as correct — verified via Wiktionary (semantic [[Radical 120|糸]] "silk, thread" + phonetic 彔, OC \*b·roːɡ — the character's meaning relates to dyed silk/green-colored textiles), matching `radical: 糸`. Stamped `date-last-perfect: 2026-07-24`.

**Frontmatter**: already correct (`pos: 性詞`, `mc_id: 2419` verified against `CC 2000.md`, traditional form 綠).

**Content removed**: a garbled numbered "1. green / 2. abbreviation for..." fragment, reformatted into the standard element-abbreviation Notes-bullet convention (same treatment as [[characters/軽 (char)|軽]] a few iterations ago) rather than discarded.

**Graphemic bullet fixed**: the existing bullet had the right components but empty glosses/OC values for both 糸 and 彔 — filled in. 彔 has no character page in this vault, cited as bare plain text.

**Body defects found**: two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 緑色 was bare with no ruby; 緑柱素 was only mentioned in the abbreviation aside, never given its own proper Words entry.

**Words cross-check** (4 total ground-truth hits): 2 already present (1 ruby'd; 緑色 bare, reformatted); 2 missing — the stand-in 緑 itself and 緑柱素 (per the standing "both places, not just the abbreviation note" rule) — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 緑` matches no other character) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

**Interleaved correction (2026-07-24, user-directed): 知's component-linking convention refined.** The user flagged [[characters/知 (char)|知]]'s graphemic bullet (口 left unlinked entirely, from iteration 48 early in this loop) and, after an initial fix linking 口 to its Radical page (030), clarified the real intended rule: **only the component matching the character's own `radical:` frontmatter field gets a `[[Radical NNN|X]]` link** — any other component links to its own character page (`[[X (char)|X]]` or `[[X]]`) when one exists, even if that component happens to be a genuine Kangxi radical for *other* characters. Fixed 知's bullet accordingly (矢 → Radical 111 since that's 知's own assigned radical; 口 → `[[口 (char)|口]]`, its own character page). This refines, not replaces, the "radical components get Radical-page links" rule from `checklist_characters.md` — going forward, apply it per-character based on each character's own `radical:` field, not a blanket rule for every generically-radical component. Not retroactively auditing every prior iteration's bullets for this distinction unless asked, but applying it correctly from this point on.

### 2026-07-24, iteration 134 — [[characters/橋 (char)|橋]]

Next never-perfected character by `danayo_id` (247; 246/[[characters/談|談]] already stamped, skipped). Stamped `date-last-perfect: 2026-07-24`. `graphemic_classification: 喬` checked out as correct — verified via Wiktionary (semantic [[Radical 075|木]] "wood" + phonetic [[喬]], OC \*ɡrew), matching `radical: 木`. 喬 already has its own character page (previously surfaced as a Derived Character of [[characters/高 (char)|高]] back in iteration 81).

**Frontmatter**: already correct (`pos: 名詞`, `mc_id: 1825` verified against `CC 1000.md`).

**Content removed**: a bare "[[木 (char)]] + [[喬]]" component-list fragment, superseded by the real bullet.

**Graphemic bullet written from scratch**: 形声, semantic 木 + phonetic 喬 — bridge.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 橋梁 was bare with no ruby.

**Words cross-check** (2 total ground-truth hits): 1 already present (bare, reformatted); 1 missing — the stand-in 橋 itself — added.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 橋` matches no other character) — section correctly omitted.

**Verification**: ran the Python cross-check script against every `<rt>` value on this page — 0 mismatches found.

### 2026-07-27, iteration 442 — [[characters/宙 (char)|宙]]

Next never-perfected character by `danayo_id` (3084). Stamped `date-last-perfect: 2026-07-27`. `graphemic_classification: 由` checked out as correct — verified via Wiktionary (形聲, semantic 宀 "roof" + phonetic 由, Zhengzhang OC *l'ɯwɢs; the character originally denoted the ridgepole/beams of a house before extending to boundless space/time). 由 already lists 宙 as one of its own Derived Characters (from a prior iteration), confirming the relationship both directions.

**Frontmatter**: `pos: ""` → `名詞`, matching the character's own nominal gloss ("eternity") and its stand-in word's abstract-noun sense. `mc_id: 3286` verified against `CC 3000.md` — the listed line is literally 宙's own entry, not a borrowed/adjacent rank.

**Content removed**: two bare floating wikilinks, `[[Lookup/CC/initials/聲 澄]]` and `[[Lookup/CC/finals/韻 尤]]`, sitting directly under an otherwise-empty `## Notes` heading — folded into the proper MC-rank bullet rather than discarded.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 040|宀]] + phonetic [[由 (char)|由]], with both OC reconstructions and a dash-note on the roof-beam → boundless-space/time semantic extension.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed at all — `## Notes` held only the two floating CC links.

**Words cross-check** (6 total ground-truth hits, found via `characters:`-field grep across `words/`): 3 already present (all pre-ruby'd, unchanged); 3 missing — the stand-in 宙 itself, 宇宙, and 宇宙船 — added, all from stored fields. **False positive caught**: a body-prose grep for "宙" also matched `words/穹蒼.md`, but its `characters:` field is `穹`/`蒼 (char)` — 宙 only appears there in a "Related Concepts" prose aside (mentioning 宇宙), not as a real constituent — correctly excluded.

**Chengyu**: a body-prose grep also flagged `chengyu/天圓地方.md`, but its `characters:` field is 天/圓/地/方 with no 宙 — same false-positive pattern as above, correctly excluded. No real ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 宙` matches no other character) — section correctly omitted.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's own stored `注音` field (no persisted cross-check script found in the vault this session; verified via direct file reads instead) — 0 mismatches found.

### 2026-07-27, iteration 443 — [[characters/実|実]]

Next never-perfected character by `danayo_id` (3085). Stamped `date-last-perfect: 2026-07-27`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (real components 宀 "roof" + 周 "carved jade," an archaic sense + 貝 "shellfish/cowrie" — wealth stored under a roof, "full; substantial" → "real; true"; noted Shuowen's alternate parse as 宀 + 貫 "string of cash," which groups the same two lower strokes as one component). All three non-radical components (周, 貝, 貫) already have their own vault character pages — linked bare per the refined per-character radical rule ([[characters/知 (char)|知]]'s correction earlier in this loop), since none of them is 実's *own* `radical:` field value (宀 is, and got the `[[Radical 040|宀]]` link).

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/真実.md` (the `stand_in` compound itself). `mc_id: 249` verified against `CC 0000.md` (traditional form 實).

**Content removed**: none outright — every fragment in the old, malformed body was preserved, just relocated/reformatted (see below).

**Graphemic bullet written from scratch**: 会意, 宀 + 周 + 貝 — see etymology above.

**Body defects found**: `## Words` and `## Notes` appeared in reversed order (Words before Notes); `## Notes` held no graphemic/SKIP/MC/Levels bullets at all — instead it was a dumping ground mixing floating CC-initial/final links with six Words-style entries (実現, 実践, 実情, 実用, 実梅, 実際) that belonged in `## Words`, three of them bare with no ruby. Reordered the sections and moved all six into `## Words` proper.

**Words cross-check** (15 total ground-truth hits — this iteration used a Python regex sweep over every `words/*.md` `characters:` field, catching *both* the standard multi-line list format and the inline-array format `characters: [実, 践]`, per the standing lesson from 争's 紛争 case that inline-array entries are easy to miss with a plain grep): 9 already present in some form (3 ruby'd; 6 bare or misplaced in Notes, reformatted); 6 missing — the stand-in 真実 itself, 事実, 実力, 忠実, 誠実, 実例, 実詞 — added, all from stored fields. (Tally note: 9+6=15 accounts for all real hits; no fabricated entries.)

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 実` matches no other character, checked against both 実 and its traditional/simplified aliases 實/实) — section correctly omitted.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's own stored `注音` field — 0 mismatches found.

### 2026-07-27, iteration 444 — [[characters/客|客]]

Next never-perfected character by `danayo_id` (3086). Stamped `date-last-perfect: 2026-07-27`. `graphemic_classification: 各` checked out as correct — verified via Wiktionary (形聲, semantic 宀 "roof" + phonetic 各, OC \*kʰraːɡ with phonetic 各 at OC \*klaːɡ — one who comes to another's roof/dwelling; "guest"), matching `radical: 宀`.

**Frontmatter**: `pos: ""` → `名詞`, matching the stored `pos: 名詞` on `words/客人.md` (the `stand_in` compound). `mc_id: 429` verified against `CC 0000.md` — the listed line is literally 客's own entry.

**Content removed**: two bare floating wikilinks, `[[Lookup/CC/initials/聲 溪]]` and `[[Lookup/CC/finals/韻 陌二開]]`, sitting directly under an otherwise-bare `## Notes` heading (the heading held only those two links plus three already-correct Words-style ruby entries with no graphemic/SKIP/MC/Levels bullets) — folded into the proper MC-rank bullet, the three Words entries left in place and moved to `## Words`.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 040|宀]] + phonetic [[各 (char)|各]] — see etymology above.

**Body defects found**: no `## Words` heading existed at all — the three pre-existing ruby entries were sitting directly under `## Notes`; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (5 total ground-truth hits): 3 already present, correctly ruby'd (刺客, 侠客, 客気); 2 missing — the stand-in 客人 itself and 乗客 — added, both from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 客`): [[喀]] ("vomit") and [[額]] ("forehead; plaque") — added, neither had a filename collision. Section didn't exist previously despite these real hits.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/character's own stored `注音` field — 0 mismatches found.

### 2026-07-27, iteration 445 — [[characters/容 (char)|容]]

Next never-perfected character by `danayo_id` (3087). Stamped `date-last-perfect: 2026-07-27`. `graphemic_classification: 谷` checked out as correct — verified via Wiktionary (形聲, semantic 宀 "roof" + phonetic 谷, Zhengzhang OC \*loŋ with phonetic 谷 at \*kloːɡ — to hold/contain within an enclosed space, extending to "appearance; countenance").

**Frontmatter**: `pos: ""` → `名詞`, matching the character's own primary nominal gloss ("look; appearance; form; figure") — the stand-in word `words/容.md` had no `pos` of its own to borrow, so this was derived directly from the stored English senses rather than cross-checked against another file. `mc_id: 553` verified against `CC 0000.md` (line 574, "553. 容"). `joyo_level: "5"` correctly maps to Jōyō - Kyōiku per the checklist's mapping table (only the literal string `高等` maps to Kōtō, not any numeric grade 5–6) — caught myself about to link the wrong Jōyō file before checking the table.

**Content removed**: two bare floating wikilinks, `[[Lookup/CC/initials/聲 以]]` and `[[Lookup/CC/finals/韻 鍾]]`, sitting under a wrong-heading-level `# Notes` with nothing else — folded into the proper MC-rank bullet.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 040|宀]] + phonetic [[谷 (char)|谷]] — see etymology above.

**Body defects found**: `# Notes` was H1 instead of H2; no SKIP/Stroke/MC/Levels bullets existed; `## Chengyu` used a bare `##` immediately following the last Words bullet with no blank line (cosmetic, now spaced); 容量 was a bare plain-text entry with no ruby at all.

**Words cross-check** (7 total ground-truth hits): 4 already present (3 ruby'd; 容量 bare, reformatted); 3 missing — the stand-in 容 itself, 容器, 形容詞 — added, all from stored fields.

**Chengyu cross-check** (2 total): 1 already present, correctly ruby'd (異体不容); 1 missing — 詞彙兼容 ("the lexicon is capable of inclusion") — added from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 容`): [[溶]] ("melt; fuse") — added, no filename collision. Section didn't exist previously despite this real hit.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/chengyu's/character's own stored `注音` field — 0 mismatches found.

### 2026-07-27, iteration 446 — [[characters/密 (char)|密]]

Next never-perfected character by `danayo_id` (3088). Stamped `date-last-perfect: 2026-07-27`. `graphemic_classification: 宓` checked out as correct as a phonetic-component identifier, but **the pre-existing graphemic bullet had semantic and phonetic reversed** — verified via Wiktionary: 密 is 形聲 with semantic [[山 (char)|山]] ("mountain," contributing "hidden in the mountains") + phonetic 宓 (Zhengzhang OC \*mriɡ, same value for the whole character), not "semantic 宓 + phonetic 山" as the old bullet had it. 宓 has no character page in this vault, cited as bare plain text (same treatment as 彔 a few iterations ago). Noteworthy mismatch: 密's own `radical:` field is `宀`, but 宀 isn't a top-level component here at all — it's embedded inside the phonetic 宓, while the true semantic component is 山 (itself a different Kangxi radical). Documented this explicitly in the bullet rather than silently linking the wrong thing.

**Frontmatter**: `pos: ""` → `性詞`, derived directly from the character's own English gloss list (dense/thick/close/intimate/secret — all adjectival) since neither `words/密.md` nor any Wiktionary source offered a stored `pos` to borrow from. `mc_id: 1125` verified against `CC 1000.md` (line 134, "1125. 密").

**Content removed**: a **factually wrong graphemic bullet** (semantic/phonetic swapped, and it cited `[[山]]` with an incorrect gloss of "mountain" attached to `[[宓]]` instead) — corrected, not merely reformatted. Two duplicate `## Words` headings were merged into one; two bare floating CC-initial/final wikilinks were folded into the new MC-rank bullet; a bare non-ruby `[茂密](/words/茂密.md)` entry with no gloss and a bare `[[密陀僧]]` entry were both reformatted with proper ruby+gloss rather than discarded.

**Body defects found**: graphemic bullet had semantic/phonetic reversed (see above); two separate `## Words` headings existed with content split across them; no SKIP/Stroke/MC/Levels bullets existed; 茂密 had no ruby and no gloss at all.

**Words cross-check** (6 total ground-truth hits): 4 already present (2 ruby'd; 2 bare/missing-gloss, reformatted); 2 missing — the stand-in 密 itself and 秘密 — added, both from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 密` matches no other character) — section correctly omitted.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's own stored `注音` field — 0 mismatches found.

### 2026-07-27, iteration 447 — [[characters/富|富]]

Next never-perfected character by `danayo_id` (3089). Stamped `date-last-perfect: 2026-07-27`. `graphemic_classification: 畐` checked out as correct — verified via Wiktionary (形聲, semantic 宀 "roof" + phonetic 畐, Zhengzhang OC \*pɯɡs with phonetic 畐 at \*pʰrɯɡ/\*bɯɡ — abundance within a household, generalized to wealth/prosperity), matching `radical: 宀`. 畐 already has its own vault character page.

**Frontmatter**: `pos: ""` → `性詞`, matching the stored `pos: 性詞` on `words/豊富.md` (the `stand_in` compound itself) and the character's own adjectival gloss ("abundance"/"rich"). `mc_id: 412` verified against `CC 0000.md` (line 430, "412. 富").

**Content removed**: none — the page had almost no body at all.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 040|宀]] + phonetic [[畐]] — see etymology above.

**Body defects found**: `# Notes` was H1 instead of H2, and held only two floating CC-initial/final wikilinks — no graphemic/SKIP/MC/Levels bullets, no `## Words` heading at all despite two real ground-truth words.

**Words cross-check** (2 total ground-truth hits): none previously listed — built the section from scratch: the stand-in 豊富 itself and 富裕, both from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters**: no hits (`graphemic_classification: 富` matches no other character) — section correctly omitted.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's own stored `注音` field — 0 mismatches found.

### 2026-07-28, iteration 448 — [[characters/寒|寒]]

Next never-perfected character by `danayo_id` (3090). Stamped `date-last-perfect: 2026-07-28`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (会意/ideogrammic compound: 宀 "house" + 人 "person" + 茻 "grass," depicting a person sheltering in a house, bedded in grass, against the cold; in seal script the grass was replaced by 仌 "ice" to sharpen the cold sense), matching `radical: 宀`. Neither 茻 nor 仌 has its own vault character page, so both are cited as bare plain text; [[人 (char)|人]] does have a page and got a proper link.

**Frontmatter**: `pos: ""` → `性詞`, matching the stored `pos: 性詞` on `words/寒冷.md` (the `stand_in` compound itself). `mc_id: 397` verified against `CC 0000.md` (line 412, "397. 寒").

**Content removed**: none — the two pre-existing Words/Chengyu entries and both floating CC links were kept, just relocated/reformatted.

**Graphemic bullet written from scratch**: 会意, 宀 + 人 + 茻(→仌) — see etymology above.

**Body defects found**: two floating CC-initial/final wikilinks had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; 寒冷 was bare with no ruby.

**Words cross-check** (2 total ground-truth hits, both already on the page): 寒冷 reformatted with ruby (also marked as the `stand_in` itself); 寒蝉 already correctly ruby'd, unchanged.

**Chengyu cross-check** (1 total): 唇亡歯寒 already present and correctly ruby'd — no changes needed.

**Derived Characters**: no hits (`graphemic_classification: 寒` matches no other character) — section correctly omitted.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/chengyu's own stored `注音` field — 0 mismatches found.

**Note**: the session date rolled over to 2026-07-28 partway through this iteration (after the frontmatter edit was first written with 2026-07-27) — caught and corrected before finalizing.

### 2026-07-28, iteration 449 — [[characters/寸 (char)|寸]]

Next never-perfected character by `danayo_id` (3091). Stamped `date-last-perfect: 2026-07-28`. `graphemic_classification: 指事` checked out as correct, but **the pre-existing bullet's depiction was wrong** — it said the mark emphasized "the elbow," but per Wiktionary/Shuowen the character marks the pulse-point on the *wrist*, one 寸 (inch) inward from the palm ("a position on the forearm where the pulse can be palpated"). The "elbow" language looks like a bleed-over from [[characters/肘 (char)|肘]] ("elbow"), which is coincidentally one of 寸's own Derived Characters — corrected to the real wrist/pulse-point depiction rather than left as-is.

**Frontmatter**: `pos: ""` → `名詞`, derived from the character's own nominal gloss ("inch; measurement") since `words/寸.md` had no `pos` to borrow. `mc_id: 666` verified against `CC 0000.md` (line 690, "666. 寸"). `radical: 寸` confirmed — this character is its own Kangxi radical (Radical 041), already correctly noted via the page's third disambiguation-callout line.

**Content removed**: the factually-wrong "emphasizing the elbow" clause — replaced with the correct wrist/pulse-point depiction, not merely reworded around the same error.

**Body defects found**: two floating CC-initial/final wikilinks had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed despite the real stand-in hit; no `## Derived Characters` section existed despite two real hits.

**Words cross-check** (1 total ground-truth hit): the stand-in 寸 itself — added (no other compound in the vault cites 寸 as a constituent character).

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (2 hits via `graphemic_classification: 寸`): [[肘 (char)|肘]] ("elbow") and [[村]] ("village") — added, neither had a filename collision.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/character's own stored `注音` field — 0 mismatches found.

### 2026-07-28, iteration 450 — [[characters/寺|寺]]

Next never-perfected character by `danayo_id` (3092). Stamped `date-last-perfect: 2026-07-28`. `graphemic_classification: 士` checked out as correct for the *modern* glyph, but **the pre-existing graphemic bullet had semantic and phonetic swapped** — verified via Wiktionary: 寺 is 形聲, phonetic 之/𡳿 ("a footprint pointing up," OC \*tjɯ) + semantic 又 ("hand"), not "semantic 𡳿 + phonetic 又" as the old bullet had it. Historical note preserved and expanded: phonetic 之/𡳿 became 士 (or 土 in Simplified/JP/KR) and semantic 又 became [[寸 (char)|寸]] during the clerical/Small-Seal-Script transition — which is exactly why the *modern* semantic component links to [[Radical 041|寸]] (matching `radical: 寸`) rather than to 又 directly. Original meaning "to grasp; to hold" is preserved in the derivative [[持 (char)|持]], which already has its own vault page.

**Frontmatter**: already correct (`pos: 名詞`, matching `words/寺刹.md`'s stored `pos: 名詞`). `mc_id: 2280` verified against `CC 2000.md` (line 293, "2280. 寺").

**Content removed**: the factually-reversed semantic/phonetic graphemic bullet (corrected, not just reworded); a bare `- Components: [[土]], [[寸]]` fragment line (superseded by the real bullet, which already covers both 士/土 and 寸); an informal `### Derived Characters` H3 note reading `- +bamboo = [等 (char)](等%20(char).md)` (promoted into the standard `## Derived Characters` H2 section, not discarded — 等 is still listed there, now ruby'd).

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final wikilinks sat at the very bottom of the file, unattached to any bullet; `## Words` appeared before `## Notes` (reversed order); the informal Derived Characters note used H3 instead of H2 and covered only 1 of 7 real hits.

**Words cross-check** (2 total ground-truth hits, both already present and correctly ruby'd): 寺刹 (the `stand_in` itself, reordered first) and 寺院 — no additions needed, just reordering.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 hits via `graphemic_classification: 寺` — one of the largest families found this loop): [[持 (char)|持]] ("hold"), [[時 (char)|時]] ("when"), [[等 (char)|等]] ("etc.; rank"), [[侍]] ("servant; attendant"), [[待]] ("wait"), [[特]] ("special; distinguished"), [[詩]] ("poem") — 等 was already informally noted (now properly ruby'd); the other six added fresh, none had filename collisions.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/character's own stored `注音` field — 0 mismatches found.

### 2026-07-28, iteration 451 — [[characters/寿|寿]]

Next never-perfected character by `danayo_id` (3093). Stamped `date-last-perfect: 2026-07-28`. **`graphemic_classification: 會意` was wrong** — verified via Wiktionary: 壽/寿 is 形聲 (phono-semantic) even in its earliest bronze-inscription forms, semantic 耂 ("old") + phonetic 𢏚, sometimes bearing decorative 口 and/or 又 (又 became [[Radical 041|寸]] in the modern form, matching `radical: 寸`) — not a simple compound ideograph. Corrected the frontmatter field from `會意` to `𢏚` (the phonetic component; neither it nor 耂 has its own vault character page, both cited bare). This is a real frontmatter correction, not just a bullet rewrite — flagged explicitly in the Notes bullet in case the original `會意` value was intentional and worth someone double-checking.

**Frontmatter**: `pos: ""` → `名詞`, derived from the character's own nominal gloss ("old age; long life; lifespan") — `words/寿命.md` had no `pos` to borrow either. `mc_id: 606` verified against `CC 0000.md` (line 630, "606. 壽"). `joyo_level: "高等"` correctly maps to [[lookup/Japanese/Jōyō - Kōtō|Jōyō - Kōtō]] per the mapping table (distinct from the numeric-grade → Kyōiku mapping used on most other pages this loop). Confirmed `skip_number: 4-7-4`'s second digit matches `stroke_count: 7` — no SKIP-4 self-consistency error here.

**Content removed**: the incorrect `會意` classification (see above). The existing 躊/聯綿詞 aliasing note (explaining why 躊 has no separate page and is the phonetic host for [[躊躇]]/[[寿着]]) was kept verbatim, not touched — it's accurate standing documentation, not a defect.

**Graphemic bullet written from scratch**: 形声, semantic 耂 + phonetic 𢏚 — see etymology above.

**Body defects found**: `# Notes` was H1 instead of H2; two floating CC-initial/final wikilinks had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; no `## Words` heading existed — all three Words-style entries were bare (no ruby, informal comma-separated glosses) sitting directly under Notes; no `## Derived Characters` section existed despite three real hits.

**Words cross-check** (3 total ground-truth hits, all already present but unformatted): 寿司, 寿命 (the `stand_in`, reordered first), 寿着 — all reformatted with proper ruby+gloss from stored fields; no additions needed.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (3 hits via `graphemic_classification: 寿`): [[涛]] ("wave; billow"), [[祷]] ("pray"), [[鋳]] ("cast (metal); mint") — added, none had filename collisions.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/character's own stored `注音` field — 0 mismatches found.

### 2026-07-28, iteration 452 — [[characters/射|射]]

Next never-perfected character by `danayo_id` (3094). Stamped `date-last-perfect: 2026-07-28`. `graphemic_classification: 會意` checked out as correct — verified via Wiktionary (会意: oracle-bone 弓+矢 "bow and arrow" — now [[身 (char)|身]] since the clerical-script period — plus a hand, 又, drawing the bowstring, which became [[Radical 041|寸]], matching `radical: 寸` exactly).

**Frontmatter**: `pos: ""` → `事詞`, matching the stored `pos: 事詞` on `words/射出.md` (the `stand_in` compound itself). `mc_id: 485` verified against `CC 0000.md` (line 503, "485. 射").

**Content removed**: none — every fragment (including the "abbreviation for radon" aside) was preserved, just relocated/reformatted.

**Graphemic bullet written from scratch**: 会意, 身 + 寸 — see etymology above.

**Body defects found**: `# Notes` was H1 instead of H2 and appeared *after* `## Words` (reversed order); two floating CC-initial/final wikilinks had no MC bullet to embed in; no SKIP/Stroke/MC/Levels bullets existed; two entries (射精, 射香) were bare with informal comma-glosses instead of ruby+quoted-gloss; the 射素/"radon" note only appeared as an abbreviation aside, never given its own proper Words entry (same "both places" pattern as [[characters/緑 (char)|緑]] a few iterations ago) — kept the aside as a standing Notes bullet *and* added the Words entry, rather than choosing one over the other.

**Words cross-check** (8 total ground-truth hits): 6 already present (3 ruby'd; 2 bare/comma-glossed, reformatted; 1 — 射素 — present only as an abbreviation aside, not a real Words entry); 2 missing outright — 射術 (note: its stored `注音` is ㄊ⼘ㄙㄨㄊ, an irregular reading distinct from 射's own ㄙ⼘, kept as stored rather than "corrected" to match) — added from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (1 hit via `graphemic_classification: 射`): [[謝]] ("thank") — added, no filename collision. Section didn't exist previously despite this real hit.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/character's own stored `注音` field — 0 mismatches found.

### 2026-07-28, iteration 453 — [[characters/尚 (char)|尚]]

Next never-perfected character by `danayo_id` (3095). Stamped `date-last-perfect: 2026-07-28`. `graphemic_classification: 向` checked out as correct — verified via Wiktionary (形聲, semantic 八/⺌ "small; divide" + phonetic 向, Zhengzhang OC \*djaŋs with phonetic 向 at \*hlaŋs). The visible top component in the modern glyph is ⺌, a variant form of [[Radical 042|小]] — which is exactly why `radical: 小` (not 八) even though Wiktionary's textual gloss names the historical component as 八; linked the modern radical rather than the oracle-bone ancestor, consistent with how [[characters/寺|寺]] and [[characters/寿|寿]] handled similar historical-component-vs-current-radical mismatches earlier this loop.

**Frontmatter**: `pos: ""` → `副詞` (adverb), matching the character's own adverbial gloss ("still; even more") and precedent from semantically similar characters already in the vault (e.g. [[characters/稍 (char)|稍]] "somewhat," also `pos: 副詞`) — `words/尚.md` had no `pos` to borrow directly. `mc_id: 313` verified against `CC 0000.md` (line 328, "313. 尚").

**Content removed**: none — the single pre-existing Words entry was kept and expanded around.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 042|小]] + phonetic [[向 (char)|向]] — see etymology above.

**Body defects found**: `# Notes` was H1 instead of H2 and held only two floating CC-initial/final wikilinks — no graphemic/SKIP/MC/Levels bullets; only 1 of 3 real Words hits was present, and no `## Derived Characters` section existed despite seven real hits.

**Words cross-check** (3 total ground-truth hits): 1 already present, correctly ruby'd (尚書); 2 missing — the stand-in 尚 itself and 和尚 — added, both from stored fields.

**Chengyu**: no ground-truth hits — section correctly omitted.

**Derived Characters** (7 hits via `graphemic_classification: 尚` — one of the largest families found this loop, alongside [[characters/寺|寺]]'s seven a few iterations ago): [[当 (char)|当]] ("while"), [[賞 (char)|賞]] ("reward"), [[党]] ("political party"), [[嘗]] ("taste; experience"), [[堂]] ("meeting hall"), [[常]] ("common; normal; frequent; regular; often"), [[掌]] ("palm; sole") — all added fresh, none had filename collisions.

**Verification**: manually cross-checked every `<rt>` value on this page against each target word's/character's own stored `注音` field — 0 mismatches found.

