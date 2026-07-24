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
