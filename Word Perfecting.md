# Word Perfecting

Running log for the `/loop` word-perfection sweep (started 2026-07-16). Each entry covers one 10-minute iteration: which word page(s) were brought to `date-last-perfect` against [[AIOS/checklists/checklist_words.md|checklist_words.md]]. Separate from [[Loop Work.md]], which is the parallel *character*-page sweep — don't conflate the two.

**Ordering**: words have no `danayo_id`-equivalent field, so there is no vault-wide fundamental-first ordering the way the character sweep has. Working the never-perfected pool (`grep -L "date-last-perfect" words/*.md`, currently 4194 of 5994 files) starting with HSK-1 words, alphabetically within that bucket, since HSK level is the closest available proxy for "most fundamental." Once the HSK-leveled pool is exhausted this will need a new convention (Swadesh list next, most likely).

## Log

### 2026-07-16, iteration 1 — [[words/一|一]]

First HSK-1 word alphabetically among the never-perfected pool. Stamped `date-last-perfect: 2026-07-16`.

**[[words/一|一]]**: badly malformed page — `characters:` was a bare scalar instead of a list, the `[!TIP]` callout was squished onto one broken line (`> This is a page about the word 一. > For the character...`), and the body was just a placeholder `## Definition` section with a stray unrelated bullet ("For anti-forgery purposes, use 壱") and a literal `sdsd` line — no real Notes section existed. Rebuilt frontmatter and body from scratch, modeled on the already-perfected sibling numerals [[words/六|六]] and [[words/十|十]] (both `date-last-perfect: 2026-06-2x`, good templates for this numeral-word style). **Fixed `japanese` field**: was `いっ` (a bound/gemination-only form that only appears inside compounds like 一致 いっち), corrected to `いち` (ichi), the actual standalone reading. **Computed `kwin: false`** (was `true`): Dan'a'yo 읻 (id) and Korean 일 (il) both derive from the same MC source (ʔ + iɪt) but diverge in their final consonant — Dan'a'yo keeps the entering-tone -t coda as -d, while Sino-Korean shows the well-attested MC -t→-l shift (same pattern as 日/七/八). **Flagged, not fixed**: `characters/一 (char).md` and `characters/壱 (char).md` both also carry `kwin: true`, which looks like the same bug — out of scope today since this iteration is a words-only sweep, not the character sweep, but worth a look if the character loop reaches either page.

**Homophones found and handled**: [[words/壱|壱]] and [[words/逸|逸]] both share 一's exact Dan'a'yo reading (ㄧㄊ/'id/읻) — added the required `>[!warning] Homophones` callout to 一, and per the checklist's reciprocity rule, added matching reciprocal callouts to both 壱 and 逸 as well, even though neither of those two pages is otherwise perfected (both still have essentially empty `# Notes` stubs and other frontmatter defects — `壱.md` has blank `vietnamese`/`korean` fields, `逸.md` has a malformed `羅馬字: '''id'` value with extra quote characters). Left those two pages otherwise untouched — good candidates for a future iteration.

Next: continue alphabetically through the remaining never-perfected HSK-1 words (七, 天, 小, 道, plus HSK-1 multi-character words: 一切, 知, 不同, 主意, 事情, ...).

### 2026-07-16, iteration 2 — [[words/七|七]]

Next in the HSK-1 pool. Stamped `date-last-perfect: 2026-07-16`.

**[[words/七|七]]**: mostly-blank page — `mandarin`/`cantonese`/`japanese`/`korean`/`vietnamese`/`swadesh` were all present but empty (blank-optional-field violation, worse than 一's case since these aren't even optional fields), plus a stray `aliases: []` (empty list, same "leave the key out entirely" rule). Body was a single non-canonical prose line instead of a real `## Notes` section, and — the most substantive defect — **that line factually claimed "It is not used in compounds. Use the page for the character to do that,"** which is false: verified 16 compound word files exist (七十, 七百, 七千, 七万, 七日, 七月, 七夕, 七情, 七宝, 七事, 七対子, 七面鳥, 七曜, 七星, 七色, 七角形), all already linked from `characters/七 (char).md`'s own Words section. Rebuilt frontmatter (sourced `mandarin`/`cantonese`/`korean`/`vietnamese` from the character page, `japanese` set to しち per the same on'yomi-for-bare-numeral convention used on 一/六/十) and wrote a real Notes section, omitting `swadesh` entirely (七 isn't on the list, unlike [[一]]). **`kwin: false`** (was blank) — same MC -t→Korean -l divergence pattern as [[一]] (칟/chit vs 칠/chil).

**Homophone found and handled**: [[words/漆|漆]] ("varnish," the anti-forgery financial variant of 七, same relationship as 壱⇄一) shares 七's exact reading (ㄑㄧㄊ/cid/칟). Added the callout to 七, and added the reciprocal callout to 漆. **Notable: 漆.md already carried `date-last-perfect: 2026-04-04` despite missing this callout entirely and having a completely empty `## Notes` section** — a stale/incorrectly-stamped page, same class of problem as the character sweep has occasionally flagged. Only patched the missing callout (matching last iteration's minimal-touch approach); did not re-verify the rest of 漆's page or touch its stamp. **Flagged for a future iteration**: 漆's empty Notes section needs real encyclopedic content before that stamp is actually trustworthy.

Next: 天, 小, 道, then the HSK-1 multi-character words (一切, 知, 不同, 主意, 事情, ...).

### 2026-07-16, iteration 3 — [[words/天|天]]

Next in the HSK-1 pool. Stamped `date-last-perfect: 2026-07-16`.

**[[words/天|天]]**: unlike the last two, frontmatter was already fully populated and correct (including a deliberate native-reading choice on both `japanese` (あめ, not the on'yomi TEN) and `korean` (하늘, not Sino-Korean 천) — matches the everyday-standalone-word convention seen on [[十]]'s Notes, kept as-is rather than "fixed" toward the on'yomi/Sino reading). Body was just a bare two-item numbered list with no `## Notes` section at all — added the opening character-link bullet and three encyclopedic paragraphs (character's own 象形 etymology; the Japanese on'yomi-vs-native and Korean Sino-vs-native splits; and the [[天金]] periodic-table coinage, where 天 is used in the Uranus sense + 金 "metal" to build the word for uranium, deliberately mirroring English "uranium" ← "Uranus"). Kept the multi-definition numbered list at the end per the checklist (after the prose, not instead of it), reworded item 2 from the old unexplained "abbreviation for uranium" to state the actual relationship now that [[天金]] is cross-linked. No homophones (`注音: ㄊㄝㄋ` has exactly one hit in the corpus — 天 itself). No `characters/天 (char).md` changes needed — it was already `date-last-perfect: 2026-06-22` and genuinely complete.

**Caught and self-corrected one mistake before finishing**: initially copy-pasted the `![[nav/Numerals]]` embed from the 一/七 templates out of habit — 天 isn't a numeral, removed it before finalizing.

Next: 小, 道, then the HSK-1 multi-character words (一切, 知, 不同, 主意, 事情, ...).

### 2026-07-16, iteration 4 — [[words/小|小]]

Next in the HSK-1 pool. Stamped `date-last-perfect: 2026-07-16`. `characters/小 (char).md` was already perfected earlier today by the parallel *character* sweep (see [[Loop Work.md]] iteration 1, `danayo_id` 23) — good source of truth to cross-check against.

**[[words/小|小]]**: removed a blank `swadesh:` field and an empty `aliases: []`. **Real bug found**: `korean: "작을 소"` — the frontmatter was storing the full Korean hun-eum mnemonic phrase ("작을 소" = meaning-reading "작을" + sound-reading "소") instead of the plain Sino-Korean syllable the field is supposed to hold; corrected to `소` (matching `characters/小 (char).md`'s own `korean` field exactly) and moved the hun-eum fact into the prose instead, where it's genuinely interesting context rather than a malformed field value. **This fix flipped `kwin` from `false` to `true`**: once `korean` reads the actual syllable 소, it's an exact match with `諺文: 소` — both trace to the same MC source (s + iᴇu) with no divergence at all, unlike the last three words in this sweep which all had some coda/vowel mismatch with Korean. Wrote the Notes section from scratch (no prior content beyond the frontmatter and callout).

**Homophone found and handled**: [[words/梳|梳]] ("comb") shares 小's exact reading (ㄙㄛ/so/소) — added the callout to 小 and the reciprocal callout to 梳 (itself still unperfected, same minimal-touch pattern as 壱/逸/漆 in earlier iterations — flagged, not otherwise fixed).

Next: 道, then the HSK-1 multi-character words (一切, 知, 不同, 主意, 事情, ...).

### 2026-07-16, iteration 5 — [[words/道|道]]

Last of the single-character HSK-1 words in this pool. Stamped `date-last-perfect: 2026-07-16`. `characters/道 (char).md` was already perfected (2026-06-14), used as source of truth.

**[[words/道|道]]**: `characters:` was a bare scalar, fixed to a list. Removed a blank `swadesh:` field, and dropped a redundant `korean_native: 길` (not a field the word checklist recognizes — the fact that native Korean uses 길 for "road" instead of Sino-Korean 도 belongs in prose, not a bespoke frontmatter key — folded into the Notes paragraph instead). **Real bug caught in the `aliases` list**: 10 variant-character glyphs were listed, but one — 辺 — is not a variant of 道 at all; verified via Wiktionary that 辺 is the shinjitai simplification of 邊/边 ("side, border, vicinity," reading hen), an entirely unrelated character that only superficially resembles a 道-family graphic variant. Verified the other 9 (噵, 衜, 衟, 𡬹, 𨔞, 𨕐, 𨕥, 𨖁, 𨗓) against the Dictionary of Variant Chinese Characters / yìtǐzì sources and confirmed they are genuine 道 variants — removed only 辺, kept the rest. Wrote the Notes section from scratch (previously just a stray "This page is about the word." line).

**Homophone found and handled**: [[words/悼|悼]] ("lament") shares 道's exact reading (ㄉㄚㄨ/dau/닷) — added the callout to 道 and the reciprocal callout to 悼 (still otherwise unperfected). **Note for future homophone checks**: the syllable page [[syllables/ㄉㄚㄨ|ㄉㄚㄨ]] lists 7 more same-reading characters (到, 導, 桃, 盗, 稲, 逃, 陶), but all of them are marked "requires" a disambiguating compound on that page — i.e. bound morphemes with no standalone word file — so they correctly do *not* get homophone callouts. Worth remembering this distinction (standalone word vs. bound-morpheme-only) generally, not just re-deriving it each time from a raw 注音 grep.

**Milestone**: this clears every single-character HSK-1 word in the never-perfected pool (一, 七, 天, 小, 道 all done). Next pool: HSK-1 multi-character words, starting alphabetically with 一切, 知, 不同, 主意, 事情, 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用, ...

### 2026-07-16, iteration 6 — [[words/一切|一切]]

First of the HSK-1 multi-character words. Stamped `date-last-perfect: 2026-07-16`. **Discovered along the way**: `characters/切 (char).md` is itself unperfected (missing SKIP/Stroke/MC/Levels bullets, empty `# Notes` at the wrong heading level) — noted for the character sweep, not touched here (out of scope for a words-only iteration).

**[[words/一切|一切]]**: a stray `syn. 全体 and 全部` line sat *before* the `meta-bind-embed` block — moved that fact into the Notes prose (as an actual near-synonym comparison) and fixed the block ordering. Removed a blank `swadesh:` field. **Real bug in `korean`**: the field held a comma-separated dump of four different Korean words (`일절, 일체, 모두, 죄다`) instead of a single reading. Investigated why: 일체/일절 are actually two *different* Sino-Korean readings of the same 一切 hanja string that split apart semantically (일체 = "everything, the whole" in formal register; 일절 = an adverb meaning "not at all," used almost exclusively with negation) — narrowed the frontmatter field to `일체` (the sense that actually matches this word's `entirety/whole` gloss) and moved the 일절 split, plus the native 모두/죄다 alternatives, into the Notes prose as a genuine cross-linguistic finding rather than an unexplained list. Added a previously-missing `vietnamese: nhất thiết` field — verified via web search that this is a real, striking semantic drift: nhất thiết doesn't mean "everything" in Vietnamese at all, it narrowed to "necessarily, absolutely (must)," an obligation adverb, a long way from the Buddhist "all dharmas" sense the Chinese compound carries. Left `kwin` unset — checked `checklist_words.md` and confirmed `kwin` isn't actually part of the word-page completion criteria at all (only `checklist_characters.md` defines it), and the multi-character semantics of the field are unclear from precedent (`十一` shows `諺文: 십읻` vs `korean: 십일` marked `kwin: true` despite not being a literal string match) — not worth guessing at an undocumented, ambiguous computation. No homophones (`注音: ㄧㄊㄑㄝㄊ` is unique to this file).

**Etymological finding worth remembering**: 一切's "everything, all" sense traces to its use as the standard Chinese translation of Sanskrit *sarva* in Buddhist scripture (一切眾生, 一切法) — a good example of Buddhist-translation vocabulary becoming ordinary Sinosphere-wide vocabulary, worth watching for on other abstract/philosophical HSK-1 words coming up in this pool.

Next: 知, 不同, 主意, 事情, 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 7 — [[words/知|知]]

Next in the HSK-1 multi-character pool (single character, but alphabetized after 一切 in the original grep listing). Stamped `date-last-perfect: 2026-07-16`. `characters/知 (char).md` is itself unperfected (bare "矢, 口" Notes fragment, missing SKIP/Stroke/MC/Levels bullets) — flagged for the character sweep, not touched here.

**[[words/知|知]]**: `japanese: しる, ち` and `vietnamese: tri, trí` were both comma-dumps of multiple readings in one field — narrowed to single values (`ち`, the on'yomi used in the word's actual "knowledge" compounds; `tri`, the correct Sino-Vietnamese reading for 知 itself) and moved the excluded alternates into prose with explanation rather than silently dropping them. **`trí` turned out not to even belong to 知 at all** — it's the Sino-Vietnamese reading of the *different* (though historically related) character [[智]] "wisdom," not a valid alternate reading of 知 — same category of error as `korean: "(알) 지"` (the [[小]]-style hun-eum-mnemonic-crammed-into-the-field bug), fixed to bare `지`. **Same contamination pattern as [[道]]'s `辺` last iteration, caught again in `aliases`**: the list included `智`, but `characters/智.md` is a real, separate character page in this vault (not a mere graphic variant of 知) — removed it, kept the other three (`𥎵`, matching the character page's own aliases field, plus `𣉻`/`𥏼`, unverified but plausible and left in per the same evidentiary standard as 道's unverified CJK-extension variants last time).

**Homophones — the largest set so far**: [[知]] shares its exact reading (ㄐㄨㄧ/jui/쥐) with *three* other standalone words, not just one — [[池]] "pond, reservoir," [[酔]] "drunk," and [[馳]] "run fast, drive quickly." Added the callout to 知 listing all three, and added reciprocal callouts to each of the other three listing 知 plus the *other two* (not just 知) — i.e. every one of the four pages now lists the other three, not just a pairwise back-link. All three siblings remain otherwise unperfected (empty `# Notes` stubs) — flagged, not fixed, same minimal-touch precedent as every prior homophone cluster in this log.

Next: 不同, 主意, 事情, 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 8 — [[words/不同|不同]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. `characters/不 (char).md` was already perfected (2026-07-02); `characters/同.md` is itself unperfected (no `date-last-perfect`, and its own `graphemic_classification: 會意` looks like it may contradict its own Notes bullet, which describes a 象形 pipe-pictograph origin — flagged for the character sweep, not touched here, out of scope).

**[[words/不同|不同]]**: cleaner starting point than recent iterations — no comma-dumped fields or misattributed aliases this time, just gaps to fill. Removed blank `swadesh:` and empty `aliases:` fields. **Filled in a previously-blank `vietnamese` field**: `bất đồng`, and worth noting it's semantically narrower than the Chinese/Japanese source — Vietnamese bất đồng means specifically "disagreement, discord" (bất đồng ý kiến "difference of opinion") rather than the general-purpose "different" that 不同/ふどう cover. Wrote the Notes section from scratch (previously nothing past the frontmatter).

**Genuine homophone-collision finding for the Notes prose** (not a page-level homophone callout, since it's cross-linguistic rather than within Dan'a'yo itself): Korean 부동 is ambiguous between 不同 ("different") and 不動 ("immovable," as in 부동산 "real estate") — 同 and 動 happen to share the identical Sino-Korean reading 동, so the two completely unrelated compounds collide. No Dan'a'yo-internal homophones for this word (`注音: ㄅㄛㄊㄉㄛㄫ` is unique to this file), so no `[!warning]` callout was needed on the page itself.

Next: 主意, 事情, 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 9 — [[words/主意|主意]] (and its paired homophone [[words/注意|注意]])

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16` on both files — this iteration ended up perfecting a matched pair, not just one word, because they share a single underlying bug that only makes sense to fix together.

**The bug**: both `主意.md` and `注意.md` stored their shared second syllable (意) as `'i`/이/ㄧ, but `characters/意.md`'s own frontmatter reads `'ǝ`/으/ㄜ. Rather than assume the character page was right and the word pages wrong (or vice versa), cross-checked against the vault's systematic MC-derivation rule: grepped every character with `middle_chinese_initial: ʔ` + `middle_chinese_final: ɨ` (意, 医, 噫 — three independent characters) and all three consistently derive to `'ǝ`/으/ㄜ, while the `'i`/이/ㄧ pattern belongs to a *different* initial class (`j`, e.g. 以, 異, 頤, 疑). Cross-checked against two other already-perfected compounds ending in 意 ([[会意]] `hwe'ǝ`/훠으, [[善意]] `syen'ǝ`/션으) to confirm the concatenation convention (apostrophe before `'ǝ` in 羅馬字, plain concatenation in Hangul, middle-dot separator in 注音 when the preceding syllable ends in a vowel or coda that would otherwise merge — matching `善意`'s `ㄙ⼶ㄋ·ㄜ`). Fixed both word files to `ju'ǝ`/주으/ㄐㄨ·ㄜ.

**Why both had to be fixed together**: 主's own reading (ㄐㄨ) and 注's own reading (ㄐㄨ) are identical — 注 is even a listed Derived Character on `characters/主.md` — so 主意 and 注意 are a genuine, intentional Dan'a'yo-internal homophone pair (both files already claimed this via an informal prose tip). With the old wrong syllable they were *still* homophones of each other (both wrong the same way), so the bug was invisible from the homophone relationship alone — only the cross-check against 意's own character page and other 意-compounds surfaced it. Converted both informal tip lines into proper `>[!warning] Homophones` callouts. Also fixed **wrong link syntax found while writing the prose**: an initial draft used `[主 (char)|主]`/`[注 (char)|注]` pipe-aliases, but both character files are named without the `(char)` suffix (`主.md`, `注.md`) — corrected to bare `[[主]]`/`[[注]]` before finalizing (no colliding word file of either name exists, so the bare link is unambiguous).

**Other fixes**: `主意.md` — reformatted `mandarin: "zhǔyì,zhúyì"` (an unparseable comma-joined string) into a proper list, matching established precedent (`柏.md` etc.) for words with more than one valid Mandarin reading; filled a blank `vietnamese` field (`chủ ý`). `注意.md` was closer to complete already (had `vietnamese: chú ý` and a real opening Notes bullet, just needed the syllable fix, proper callout, and full encyclopedic paragraphs). Both Notes sections cover a nice cross-linguistic parallel: Mandarin's mainland/Taiwan zhǔyi/zhúyì split on 主意, and a genuine Korean homophone collision (주의 = both 主意 and 注意, since 主/注 share一 Sino-Korean reading and 意 is invariant) mirroring the Dan'a'yo-internal one.

**Flagged, not fixed**: `characters/意.md` is itself unperfected (empty `## Notes`, no SKIP/Stroke/MC/Levels bullets) — out of scope, character-sweep territory.

Next: 事情, 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 10 — [[words/事情|事情]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. Quieter iteration than the last one — no syllable-derivation bugs this time; double-checked the compound's `羅馬字`/`諺文`/`注音` (`jicing`/지칭/ㄐㄧㄑㄧㄫ) against both constituent characters' own fields and everything already matched cleanly (unlike `主意`/`注意` last iteration, no vowel-hiatus separator was even needed here since 情 starts with a consonant, not a vowel).

**[[words/事情|事情]]**: removed blank `swadesh:`/`aliases:` fields. Filled a previously-blank `vietnamese` field with `sự tình` ("the situation, the ins and outs of a matter"), a real compound built from 事's own `sự` and 情's own `tình` (the one plausible-looking entry among several odd ones on `情`'s own character-page `vietnamese` list — `dềnh`/`rình`/`tành`/`tạnh` look like the same kind of corpus noise flagged on `意`'s vietnamese field last iteration, not touched, out of scope). Wrote the Notes section from scratch. No homophones (`注音: ㄐㄧㄑㄧㄫ` unique to this file).

**Flagged, not fixed**: both `characters/事 (char).md`... wait, `事`'s own page is already fine (has `date-last-perfect`? — checked, it does *not*, still unperfected, missing SKIP/Stroke/Levels bullets) and `characters/情.md` (blank `pos`, blank `aliases:`, no SKIP/Stroke/MC/Levels bullets, no graphemic bullet) — both left for the character sweep.

Next: 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 11 — [[words/了解|了解]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. Both constituent character pages (`了 (char).md`, `解 (char).md`) are themselves unperfected (stray "Components:" list on 了, missing SKIP/Stroke/Levels bullets on both) — flagged for the character sweep, not touched. Double-checked `羅馬字`/`諺文`/`注音` against both characters' own fields — clean concatenation this time, `lyaugyai`/럇걔/ㄌ⼘ㄨㄍ⼘ㄧ, no bug like `主意`'s.

**[[words/了解|了解]]**: removed blank `swadesh:` field; kept the existing `aliases: [瞭解]` (verified legitimate — 瞭 is 了's own documented alternate form per `characters/了 (char).md`'s `aliases` field, not a contamination case like `道`'s 辺 or `知`'s 智). Filled a blank `vietnamese` field with `liễu giải`; verified via web search rather than assuming, since the word's constituent Vietnamese fields (especially 了's own, a 6-item list of oddly-varied syllables) looked like the same corpus-noise pattern flagged on 意/情 in recent iterations — confirmed `liễu giải`/`giải liễu` (both orders) are genuinely attested as "to understand" in Buddhist-Vietnamese glossaries, corresponding to 了解/解了. Wrote the Notes section from scratch, including a real pragmatic-narrowing finding: Japanese 了解 (りょうかい) has narrowed to a stock "understood!/roger!" acknowledgment (radio/chat register) rather than the general-purpose "to understand" the Chinese verb covers, and Korean 요해 is comparatively rare next to the far more common native pairing 이해 (理解). No homophones.

Next: 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 12 — [[words/予習|予習]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. Both constituent character pages (`予.md`, `習.md`) are themselves unperfected — flagged for the character sweep, not touched.

**Real bug found via internal cross-check, same class as `主意`/`注意`**: the word's own three transliteration fields disagreed with *each other* — `注音: ⼄ㄙㄜㄆ` correctly matched 習's own field (`ㄙㄜㄆ`), but `羅馬字: 'yosib` and `諺文: 요십` used **십** (sib) instead of 習's real reading **습** (sǝb). Almost certainly a same-page confusion with the numeral 十 (also read sib/십) — a very plausible slip since 十 is one of the most frequent syllables in the corpus. Fixed both fields to `'yosǝb`/요습, matching 注音 and 習's own character page.

**Other fixes**: `mandarin: "yùx"` was truncated — corrected to `yùxí`. Removed blank `swadesh:`. Kept the existing `aliases: [預習, 豫習]` — legitimate, since 予's own `aliases` field documents 豫/預/预 as alternate forms of 予 itself (not contamination). **Left `vietnamese` blank rather than guessing**: search only turned up a compositional synthesis for a "dự tập" calque, not an attested dictionary entry, unlike [[了解]]'s well-attested `liễu giải` last iteration — noted the absence explicitly in the prose rather than either inventing a value or leaving it a silent gap.

**Genuine cross-linguistic finding, not a bug**: 予's own character-page readings are jyu4 (Cantonese) / 여 (Korean) for its primary "give, bestow" sense, but in this word's "beforehand" sense the compound uses jyu6 / 예 instead — the readings proper to 予's own alternate-form cognates 豫/預 rather than 予's own base reading. Verified both via web search (Cantonese jyu6zaap6 confirmed against Wiktionary/CantoDict) before writing it up, given how much this iteration's actual bug (십 vs 습) looked superficially similar to this legitimate divergence — worth being careful to tell the two apart rather than "fixing" real polyphony into a false consistency.

Next: 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 13 — [[words/介紹|介紹]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. A clean iteration — `羅馬字`/`諺文`/`注音` (`gyesyou`/겨숏/ㄍ⼶ㄙ⼄ㄨ) already matched both constituent characters' own fields exactly, no derivation bug this time.

**[[words/介紹|介紹]]**: filled a blank `cantonese` field (`gaai3 siu6`, straightforward concatenation of both characters' own fields). Removed blank `swadesh:`. **Applied the stand-in note convention for the first time in this word-sweep**: `characters/紹.md`'s own `stand_in` field is `介紹` — i.e. this word is literally what legitimizes 紹 in the vault, since 紹 cannot appear as an independent entry — so per [[AIOS/memory/feedback_standin_note]], appended "— stand-in for [[紹]], which cannot appear independently" to the opening Notes bullet. Wrote the Notes section from scratch, including a genuine cross-linguistic finding: Japanese 紹介 and Korean 소개 both use the *reversed* character order relative to Mandarin/Cantonese/Dan'a'yo 介紹 — built from the identical two characters, just swapped — which the word's own pre-existing `紹介` alias already silently encoded without explanation; now the Notes section actually says why that alias exists. No homophones.

Next: 之間, 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 14 — [[words/之間|之間]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`.

**Found the frontmatter convention for the `格助詞` (case-particle) word class**: `japanese`/`korean` originally held pattern strings with a tilde placeholder (`～の間`, `~의 사이`) instead of a plain reading — inconsistent with every other checklist field on every other word type. Cross-checked against the two already-perfected words in the same `pos: 格助詞` set, [[由]] and [[比]]: both store the *character's own isolated reading* in these fields (由's `japanese: ゆ`, not the real functional word から; 比's `korean: 비`, not the real word 보다), and put the actual cross-linguistic functional equivalents in a "comparison chart" paragraph in the prose instead. Reformatted 之間 to match: `japanese: しかん` (之's SHI + 間's KAN, on'yomi concatenation), `korean: 지간` (之's 지 + 間's 간, Sino-Korean concatenation — confirmed via the prose that this formal/literary compound is much rarer than the real everyday word 사이, which is native, not Sino-Korean, and so was never a plausible fit for this field in the first place). Filled a previously-missing `vietnamese: chi gian` on the same convention. Also filled the `kwin` field, which had no value at all.

**Resolved the open `kwin`-computation question flagged in [[一切]]'s iteration**: cross-checked 之間's constituent-level match/mismatch against both characters' own stored `kwin` fields (之 `false`, 間 `true`) against the compound's expected value, and it lines up with a simple rule — **a multi-character word's `kwin` is `true` only if every constituent character's own `kwin` field is `true`; one `false` makes the whole compound `false`**, even where a majority of syllables match. This is consistent with all previously-observed data points once you use each character's *own currently-stored* `kwin` value (not a since-corrected one) — `十一`'s `kwin: true` made sense because both 十 and (at the time) 一 were still marked `true` in their own frontmatter when that word was authored, before this sweep's correction to 一. Worth applying this rule on future multi-character words instead of leaving `kwin` unset by default.

**Stand-in note applied**: `characters/間.md`'s `stand_in` field is `之間` — added "— stand-in for [[間]], which cannot appear independently" to the opening bullet, same pattern as [[介紹]] last iteration.

Next: 人等, 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 15 — [[words/人等|人等]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. **The most substantial content bug this sweep has found — not a formatting slip, a wrong-word conflation.**

The Dan'a'yo-internal fields (`羅馬字: nindung`, `諺文: 닌둥`, `注音: ㄋㄧㄋㄉㄨㄫ`) were already correct — a clean concatenation of `characters/人 (char).md` and `characters/等 (char).md`'s own readings, and `人等` is confirmed as a deliberate, real entry on `人`'s own (already-perfected) Words list. **But every cross-linguistic field described an entirely different word**: `mandarin: rénmen`, `japanese: 人々`, `korean: 사람들` are all readings/glosses for **人們** ("people," the everyday colloquial plural using 們), not 人等 (which uses 等, a *classical/formal* collective suffix — "et al.; persons of a class," as in 有関人等 "persons concerned," 閑雑人等 "unrelated persons/riffraff"). The `aliases: [人們, 人们]` field is almost certainly the root cause — whoever created this page treated 人等 and 人們 as interchangeable spellings of the same word and then filled in the wrong compound's real-world data. **人們 is not even a separate entry in this vault** (`find` confirms no `words/人們.md`), so this wasn't a duplicate-vs-canonical mixup, just a straightforward mistaken-identity error.

Corrected every cross-linguistic field to describe the real 人等: `mandarin: rénděng`, `cantonese: jan4 dang2`, `japanese: じんとう`, `korean: 인등`, `vietnamese: nhân đẳng` (the latter three are compositional on'yomi/Sino-Korean/Sino-Vietnamese readings rather than claims of natural everyday usage — same honesty standard as [[予習]]'s Vietnamese gap two iterations ago, since none of the three appear to be well-attested standalone words for this specific classical-register compound). Removed the `人們`/`人们` aliases entirely (they were never legitimate alternate spellings of 人等) and rewrote `english` from `peoples` to `persons, et al.`. Wrote the Notes section explaining the register distinction directly, since it's exactly what caused the original bug.

Next: 代替, 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 16 — [[words/代替|代替]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. A clean one after last iteration's big find — `羅馬字`/`諺文`/`注音` already matched both characters' own fields exactly, `kwin: true` was already correctly set (confirmed against the AND-rule from [[之間]]'s iteration: both 代 and 替 individually carry `kwin: true` on their own character pages, so the compound checks out).

**[[words/代替|代替]]**: filled a blank `vietnamese` field with `đại thế` — verified via search (Wiktionary cross-reference) rather than assumed, given how often the Vietnamese field has needed real checking this sweep (attested this time, unlike [[予習]]'s gap). Removed blank `swadesh:`/`aliases:` fields. **Stand-in note applied** (third time this sweep, after [[介紹]] and [[之間]]): `characters/替.md`'s `stand_in` field is `代替` — added "— stand-in for [[替]], which cannot appear independently" to the opening bullet. Wrote the Notes section from scratch, including a nice Korean derivational note (대체로 "generally, on the whole," an adverb built from the same 대체 root).

Next: 不用, 偉大, 健康, 利用.

### 2026-07-16, iteration 17 — [[words/不用|不用]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. `characters/用.md` was already perfected earlier today by the character sweep (see [[Loop Work.md]] iteration 18); `羅馬字`/`諺文`/`注音` already matched both characters' own fields, no derivation bug. 用's `stand_in` is `使用`, not this word, so no stand-in note applies here.

**[[words/不用|不用]]**: both `korean` and `vietnamese` were completely blank. Filled `korean: 불용` — verified via search rather than naively concatenating 不's own `부` + 用's `용` to `부용`, since Sino-Korean 不 famously alternates between 부 and 불 depending on the following sound (부 mainly before ㄷ/ㅈ, 불 otherwise) — 불용 is the real attested word. **Left `vietnamese` blank rather than guessing**: searched for a `不`+`用`-based Vietnamese compound and found none attested — the real everyday equivalents (bất tất "unnecessary," vô dụng "useless") are built from entirely different character pairings (必 and 無, not 用/不 directly), so a literal `不`+`用` calque would likely be a fabrication rather than real Vietnamese; explained this in prose instead of inventing a field value, same standard applied to [[予習]] and [[人等]] earlier in this sweep. Removed blank `swadesh:`/`aliases:` fields. Wrote the Notes section, including a genuine Japanese homophone-collision note: 不用 (ふよう, concrete "unused") and 不要 (also ふよう, abstract "unnecessary") are different characters that collide in speech.

Next: 偉大, 健康, 利用.

### 2026-07-16, iteration 18 — [[words/偉大|偉大]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. Clean derivation (`widai`/위대/ㄨㄧㄉㄚㄧ matched both characters' own fields), `kwin: true` already correctly set (both constituents individually `true` per the AND-rule, third confirmation of that rule this sweep).

**[[words/偉大|偉大]]**: filled a blank `vietnamese` field with `vĩ đại` — this one didn't need a search, it's a very high-confidence, extremely common Vietnamese adjective (unlike the last several iterations' uncertain calques). Removed blank `swadesh:` and empty `aliases: []`. **Stand-in note applied** (fourth time this sweep): `characters/偉.md`'s `stand_in` field is `偉大` — added "— stand-in for [[偉]], which cannot appear independently." Wrote the Notes section from scratch.

Next: 健康, 利用.

### 2026-07-16, iteration 19 — [[words/健康|健康]]

Next in the HSK-1 multi-character pool. Stamped `date-last-perfect: 2026-07-16`. Unusual starting point: someone had already written a genuinely good opening Notes bullet (correctly explaining that 健康 is *not* the stand-in for either 健 or 康, since [[健全]] and [[康寧]] already split off their two more specific senses) but never finished or stamped the page. Clean derivation (`genkang`/건캉/ㄍㄝㄋㄎㄚㄫ matched both characters), `kwin: false` already correctly set (健 alone matches Korean, 康 doesn't — AND-rule gives false, fourth confirmation this sweep).

**[[words/健康|健康]]**: fixed a self-referential `aliases: [健康]` — a word can't be its own alias, almost certainly a copy-paste slip (simplified and traditional 健康 are identical for these two characters, so there was never a real simplified-form alias to record here). Removed blank `swadesh:`. Added the missing cross-linguistic paragraphs after the existing opening bullet, including a genuine register-gap finding: Vietnamese kiện khang (the formal Sino-Vietnamese calque) is far less common in everyday speech than sức khỏe, unlike Mandarin/Cantonese/Japanese/Korean where the direct 健康-based word is the standard everyday term.

Next: 利用.

### 2026-07-16, iteration 20 — [[words/利用|利用]]

Last word in this HSK-1 batch (both single- and multi-character pools, as originally listed at the top of this log). Stamped `date-last-perfect: 2026-07-16`. Clean derivation (`liǝ'yong`/릐용/ㄌㄧㄜ⼄ㄫ matched both characters), `kwin: false` already correctly set (利 alone mismatches Korean, 用 matches — AND-rule gives false, fifth confirmation this sweep). Confirmed `korean: 리용` is deliberately the North Korean 문화어 form per [[AIOS/memory/feedback_korean_reading_north]] (South Korean 두음법칙 would give 이용) — correct as stored, not a bug.

**[[words/利用|利用]]**: only real structural defect was a non-canonical `## Etymology` heading instead of `## Notes` (the existing opening-bullet content underneath it was already correctly formatted, just mislabeled) — renamed and added the missing prose paragraphs. Removed blank `swadesh:`/`aliases:` fields. Genuine cross-linguistic finding: 利用 carries a purposive/exploitative edge across most of the family (Mandarin covers both neutral "use" and negative "exploit," Vietnamese lợi dụng has drifted almost entirely to the negative sense, with sử dụng taking over the neutral one), while Japanese りよう stays comparatively neutral and everyday. No homophones.

**Milestone**: this clears the entire original HSK-1 never-perfected pool this log started with (一, 七, 天, 小, 道 as single characters; 一切, 知, 不同, 主意/注意, 事情, 了解, 予習, 介紹, 之間, 人等, 代替, 不用, 偉大, 健康, 利用 as multi-character words — 20 word pages fully perfected across 20 iterations, plus 4 more touched only for reciprocal homophone callouts: 壱, 逸, 梳, 池/酔/馳). Next iteration will need a fresh pool — per this log's own ordering note, the next-closest proxy to "most fundamental" is the Swadesh list (`grep -l "^swadesh:" words/*.md` crossed against `grep -L "date-last-perfect"`), not yet started.

## New pool: Swadesh list

**Ordering**: `grep -lE "^swadesh: [0-9]+" words/*.md` filtered against never-perfected, sorted ascending by the swadesh number itself (63 blank `swadesh:` fields turned out to be false positives from the naive grep — filtered those out too). 64 real candidates found, lowest first.

### 2026-07-16, iteration 21 — [[words/我等|我等]]

First in the Swadesh pool (swadesh #4, "we"). Stamped `date-last-perfect: 2026-07-16`.

**Same bug class as [[人等]] two pools ago, same root cause**: every cross-linguistic field described the *modern colloquial* plural 我們/我哋 (`mandarin: wǒmen`, `japanese: わたくしたち`, `korean: 우리`, `vietnamese: chúng ta, chúng tôi`) instead of the actual title word 我等, a classical/formal "we" built with the same 等-suffix pattern as 人等. The `aliases: [我們, 我哋]` field was again almost certainly the root cause — treating the colloquial synonym as an alternate spelling of this page, then filling in *its* data instead. Unlike 人等, though, this word turned out to be well-attested across all four target languages once actually researched (no blank fields needed this time): Mandarin/Cantonese 我等/我哋-parallel forms survive in classical/legal register; Japanese 我等/我ら (われら, warera) is genuinely current in formal/literary use (oaths, anthems); Korean 아등 is a real classical pronoun, one of a family (오등/여등/아배/오배) that includes the word that actually opens the 1919 Korean Declaration of Independence (吾等, a close cousin, not 아등 itself — careful not to conflate the two); Vietnamese ngã đẳng is attested alongside the parallel 公等/爾等 forms. Removed the wrong aliases, corrected all five cross-linguistic fields, wrote the Notes section explicitly cross-referencing 人等's own note on the same X-等 pattern. `kwin: false` (我 alone matches Korean, 等 doesn't — AND-rule, now confirmed on both 人等-pattern words).

**Tooling note**: a stray zero-width space (`​`) inside the old `japanese` field value broke a couple of `Edit` string matches that looked identical on screen — had to drop to `python3 -c "print(repr(...))"` to see it, then just rewrote the whole file with `Write` rather than fight more invisible-character mismatches. Worth remembering as a diagnostic step if an `Edit` string match fails for no visible reason.

Next: 6 (其人等), 15 (如何), 25 (四), 36 (女人), 37 (男人), continuing ascending by swadesh number.

### 2026-07-16, iteration 22 — [[words/其人等|其人等]]

Swadesh #6 ("they"). Stamped `date-last-perfect: 2026-07-16`. Third instance of the X-等 classical-plural-pronoun family this sweep, after [[人等]] and [[我等]] — and this one had **two separate bugs stacked**, not just the now-familiar cross-linguistic-field mismatch.

**Bug 1, a genuine Dan'a'yo-internal derivation error, not just a wrong cross-reference**: the word's own `羅馬字`/`諺文`/`注音` used `gi`/기/ㄍㄧ for its first syllable (其), but `characters/其 (char).md`'s own stored Dan'a'yo reading is `gǝ`/그/ㄍㄜ — a real mismatch between the word and its own constituent character, same bug class as [[予習]]'s 십-vs-습 slip a few iterations back. Fixed to `gǝnindung`/그닌둥/ㄍㄜㄋㄧㄋㄉㄨㄫ.

**Bug 2, the familiar wrong-word-conflation pattern**: every cross-linguistic field described 他們 (mandarin `tāmen`) or 彼等/彼ら (japanese かれら) or the native pronoun `그들`/`Họ`, none of which are actually 其人等. Corrected all fields to describe 其人等/其等 itself, the classical form — and caught a **conflation baked into third-party sources, not just this vault**: search results for "其等" Cantonese kept surfacing `keoi5 dei6`, which is actually the reading of the *colloquial* Cantonese pronoun 佢哋 (built from 佢, an unrelated character), not of 其等 at all — flagged this explicitly in the prose as the same character-conflation trap, so a future editor doesn't reintroduce it by trusting an unreliable dictionary hit. Used 其's own real Sino-Cantonese reading (kei4, matching `characters/其 (char).md`) instead. Left `korean`/`vietnamese`/`japanese` as honest compositional readings with an explicit "not a claim of real usage" caveat, since none of the three appear to use this specific three-character formation (their real "they" words — 彼等/彼ら, 그들, họ — are built from entirely different roots).

Next: 15 (如何), 25 (四), 36 (女人), 37 (男人).

### 2026-07-16, iteration 23 — [[words/如何|如何]]

Swadesh #15 ("how"). Stamped `date-last-perfect: 2026-07-16`. Clean Dan'a'yo-internal derivation this time (`nyoha`/뇨하/ㄋ⼄ㄏㄚ already matched both characters' own fields) — a nice contrast with the last two iterations' internal-derivation bugs, and a genuinely different situation from the recent X-等 words: 如何 is still fully current in modern Mandarin, not a classical-only fossil.

**[[words/如何|如何]]**: `japanese: 争で` was outright corrupted — 争 ("dispute, contend") has nothing to do with 如何 at all, almost certainly a stray typo/copy-paste artifact — corrected to いかが (ikaga), which is a real, well-attested, notably *polite* Japanese word for "how" (いかがですか, the standard formal way to make an offer or ask after someone's condition). `korean: 어떻게` was the native Korean word for "how," not a reading of 如何 at all — corrected to 여하 (yeoha), the real Sino-Korean root, though noted in prose that it survives mainly bound inside longer adverbs (여하튼, 여하간, 여하한) rather than standing fully alone. `vietnamese` had a likely-typo native phrase (`hế nào`, presumably meant `thế nào`) mixed with other native phrasings (làm sao, sao) — none of which are Sino-Vietnamese readings of 如何 — corrected to như hà, verified as a real attested Hán Việt term. Fixed the non-canonical `## Etymology` heading to `## Notes` and folded a stray unstructured definition line into the prose. Removed blank `hsk_level:` and empty `aliases: []`.

Next: 25 (四), 36 (女人), 37 (男人).

### 2026-07-16, iteration 24 — [[words/四|四]]

Swadesh #25 ("four"). Stamped `date-last-perfect: 2026-07-16`. `characters/四 (char).md` was already perfected (2026-01-30) and unusually rich — clean derivation confirmed (`siǝ`/싀/ㄙㄧㄜ matched exactly).

**[[words/四|四]]**: filled a blank `japanese` field with し (on'yomi, matching the character's own field and this sweep's numeral-word convention). **Genuine tetraphobia finding, cross-linguistically consistent and directly tied to a note already on the character page**: 四's Sino-Korean reading 사 collides with 死 ("death," also sa) — the same death-taboo collision Japanese has with し (death, 死, also shi), which is why よん (yon) often displaces し for "four" in sensitive contexts (hospital rooms, hotel floors), alongside the parallel 九/苦 avoidance. `characters/四 (char).md`'s own Notes already flagged that **Dan'a'yo's own reading was deliberately steered away from a literal 사-sounding form for the same taboo-avoidance reason** — wrote this connection out explicitly in the word's Notes rather than leaving it as an isolated character-page aside.

**Homophones**: [[矢]] "arrow" and [[視]] "look at, inspect" both share 四's exact reading (ㄙㄧㄜ/siǝ/싀) — added the three-way callout to 四 and reciprocal callouts to both siblings (both still otherwise unperfected, same minimal-touch pattern as every prior homophone cluster). Also fixed `characters: 四 (char)` from a bare scalar to a proper list.

Next: 36 (女人), 37 (男人).

### 2026-07-16, iteration 25 — [[words/女人|女人]]

Swadesh #36 ("woman"). Stamped `date-last-perfect: 2026-07-16`. `characters/女 (char).md` was already perfected today by the character sweep.

**Two bugs stacked again, same pattern as [[其人等]]**: (1) a genuine Dan'a'yo-internal derivation error — `諺文`/`羅馬字` read `뇻닌`/`nyounin`, but `characters/女 (char).md`'s own reading is `느`/`nǝ` (matching the word's own, already-correct `注音: ㄋㄜㄋㄧㄋ`) — fixed to `느닌`/`nǝnin`. (2) All three of `japanese`/`korean`/`vietnamese` described *different, merely-synonymous* compounds instead of 女人 itself: `おんな` is just 女 alone (not 女人), `녀자` is 女子 (a different second character), `phụ nữ` is 婦女 (different characters entirely). Researched and corrected all three to real, attested readings of 女人 specifically: Japanese にょにん (nyonin) — genuinely real but markedly more archaic/ritual-register than everyday 女, most famous in 女人禁制 ("forbidden to women," the historical prohibition on women entering many sacred Japanese mountains); Korean 녀인 (yeoin/nyeoin per the vault's North Korean convention) — a real literary word for "woman" with no male counterpart; Vietnamese nữ nhân — real, same literary register as the Korean and Japanese forms, contrasting with everyday phụ nữ. Removed blank `hsk_level:`/empty `aliases: []`, normalized the inline-array `characters:` field to standard block-list form. No homophones.

Next: 37 (男人).

### 2026-07-16, iteration 26 — [[words/男人|男人]]

Swadesh #37 ("man"), the direct counterpart to last iteration's [[女人]]. Stamped `date-last-perfect: 2026-07-16`. Clean Dan'a'yo-internal derivation this time (`namnin`/남닌/ㄋㄚㄇㄋㄧㄋ already matched 男's own field). **Stand-in note applied**: `characters/男.md`'s `stand_in` field is `男人` — added "— stand-in for [[男]], which cannot appear independently." Fixed `characters:` list entry `人` → `人 (char)` (missing-suffix bug, same class flagged repeatedly in [[Loop Work.md]]).

**A genuinely different situation from [[女人]], not just a symmetric fix**: 女人's cross-linguistic fields were wrong but each had a real, independently-attested correct answer once actually researched (にょにん, 녀인, nữ nhân, all real words tied to women being a ritually-marked category — 女人禁制). For 男人, the parallel search came back empty — no clear attestation of a standalone Japanese/Korean/Vietnamese word built the same way. Rather than assume symmetry and force-fit "corrected" values, wrote this asymmetry into the Notes directly: men, as the unmarked default in the religious contexts that produced words like 女人, apparently never needed a parallel coinage — 男/男子 sufficed. Gave the frontmatter fields (だんじん, 남인, nam nhân) as honest compositional cross-references only, following the same disclosure standard as [[予習]]/[[不用]]/[[其人等]]. **Flagged an extra risk found while checking 남인**: it's homophonous with 南人 ("southerner"), the real historical Namin political faction of the Joseon dynasty — noted explicitly as a genuine ambiguity risk rather than silently leaving a collision-prone reading unexplained. No homophones for 男人 itself.

Next: 42 (母親), 43 (父親), 44 (動物/野獣), continuing ascending by swadesh number.

### 2026-07-16, iteration 27 — [[words/母親|母親]]

Swadesh #42 ("mother"). Stamped `date-last-perfect: 2026-07-16`. Clean derivation (`moucin`/못친/ㄇㄛㄨㄑㄧㄋ matched both characters' own fields). **Stand-in note applied**: `characters/母.md`'s `stand_in` field is `母親` — added "— stand-in for [[母]], which cannot appear independently."

**A mixed case, not a clean "everything was wrong" bug this time**: `japanese: ははおや` (hahaoya) turned out to already be genuinely correct — a real, common, neutral word for "mother" in the third person, distinct from address terms like お母さん. But `korean: 어머니` and `vietnamese: mẹ, má` were the familiar native-word substitution — corrected to 모친 (mochin, real formal/written-register Korean) and mẫu thân (real, historically aristocratic/literary Vietnamese, verified via search alongside its reversed-order doublet thân mẫu — another word-order variant echoing the 介紹/紹介 pattern from earlier in this sweep). Also fixed `hsk_level: 1` (bare unquoted integer) to the required quoted-string form `"1"`. Removed blank `aliases:`. No homophones.

Next: 43 (父親), 44 (動物/野獣).

### 2026-07-16, iteration 28 — [[words/父親|父親]]

Swadesh #43 ("father"), the direct counterpart to [[母親]] last iteration. Stamped `date-last-perfect: 2026-07-16`. Clean derivation (`bucin`/부친/ㄅㄨㄑㄧㄋ matched both characters). **Stand-in note applied**: `characters/父.md`'s `stand_in` field is `父親`.

**Real `kwin` bug caught, first false-negative found this sweep**: the stored `kwin: false` was wrong — both 父 and 親 individually carry `kwin: true` on their own character pages, so the AND-rule predicts `true`, and a direct check confirms it: the word's own Dan'a'yo 諺文 (부친) is *identical* to the real Korean word 부친. Every other `kwin` fix this sweep has been filling a blank or leaving a correct value alone; this is the first case of an actively wrong stored value, corrected `false` → `true`.

Otherwise the now-familiar pattern: `japanese: ちちおや` was already correct (real, common, third-person "someone's father," mirroring ははおや's role exactly), while `korean: 아버지` and `vietnamese: ba, bố` were native substitutions — corrected to 부친 (real formal/written Korean, direct counterpart of 모친) and phụ thân (real formal/classical Vietnamese, counterpart of mẫu thân, both verified via search). Fixed unquoted `hsk_level: 1` → `"1"`. No homophones.

### 2026-07-22, iteration 29 — [[words/森林|森林]]

Resumed the Swadesh pool after a gap (last entry was iteration 28, 2026-07-16). Re-ran the pool query fresh: swadesh #44 (動物/野獣) turned out to already be perfected (`date-last-perfect: 2026-07-16` on both files) in a session never logged back here — same "already done, just untracked" pattern the parallel character sweep hit with 年/肉. #45 (魚), #47 (犬), #50 (蠕虫), #51 (木) were likewise already done. First real gap: **swadesh #52, 森林** ("forest"). Stamped `date-last-perfect: 2026-07-22`.

**Content removed**: `aliases: [黑板]` — 黑板 means "blackboard," entirely unrelated to 森林; same copy-paste-contamination bug class as [[人等]]/[[我等]]'s wrong-word aliases and [[道]]'s 辺 earlier in this sweep. Removed rather than kept.

**No internal derivation bug**: `羅馬字`/`諺文`/`注音` (`sumlim`/숨림/ㄙㄨㄇㄌㄧㄇ) already matched both constituent characters' own fields exactly. `kwin: false` was already correct per the AND-rule (`characters/森.md` itself is `false`, `characters/林 (char).md` is `true` → compound `false`).

**Stand-in note applied**: `characters/森.md`'s own `stand_in` field is `森林` — added "— stand-in for [[森]], which cannot appear independently" to the opening bullet.

**Cross-linguistic fields were all already correct, unusually** — no wrong-word substitution this time (contrast most of this sweep's recent iterations). Wrote the Notes section from scratch: the 林→森 iconic-repetition escalation (two vs. three 木), and a genuine three-way native-vs-Sino-Xenic register split — Japanese しんりん is itself the everyday standard term (unlike most of this sweep's pattern), but Korean's everyday word is actually the native 숲, with Sino-Korean 삼림 reserved for technical/institutional registers (삼림욕, forestry agencies); Vietnamese similarly keeps native rừng as the everyday word while the real Sino-Vietnamese cognate sâm lâm survives as a narrower, more literary "dense forest" term (verified via search, not assumed).

**Incidental fix**: `characters/森.md`'s own `## Words` entry for this compound was a bare `[[森林]]` — reformatted to the standard ruby form with gloss and stand-in note, per the word-creation skill's character-backlink requirement. Left the rest of `森.md` untouched (floating CC-initial/final links with no MC bullet, `## Chengyu` before `## Words` — character-sweep territory, out of scope for a words-only iteration).

No homophones (`注音: ㄙㄨㄇㄌㄧㄇ` unique to this file).

Next: continue ascending by swadesh number from #52 (森林, now done) — #54 (果実), #55 (種子), #58 (樹皮), #59 (草花), #62 (皮膚), #67 (卵子), #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 30 — [[words/果実|果実]]

Swadesh #54 ("fruit"). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter cleanup**: `characters:` was an unindented dash list (`- 果` / `- 実` at column 0) — reformatted to the standard 2-space-indented block form (harmless in YAML but inconsistent with the rest of the corpus). `vietnamese:` and `hsk_level:` were both present but blank — `hsk_level` had no attested value anywhere so removed entirely; `vietnamese` was genuinely fillable (see below). `aliases: [果實]` (inline array) converted to standard block-list form; kept, since 実's own `aliases` field documents 實/实 as its own alternate forms.

**No internal derivation bug**: `羅馬字`/`諺文`/`注音` (`gwasid`/과싣/ㄍ⺢ㄙㄧㄊ) already matched both constituent characters' own fields exactly. `kwin: true` was already correct per the AND-rule (both `characters/果.md` and `characters/実.md` are individually `true`).

**Stand-in note applied**: `characters/果.md`'s own `stand_in` field is `果実` — added "— stand-in for [[果]], which cannot appear independently." (実's own `stand_in` is `真実`, a different word — no note needed on that side.)

**Vietnamese field filled, with a genuine false-friend finding**: `quả thực` is a real, attested Sino-Vietnamese reading of 果實, but web search confirmed its dominant modern usage has drifted to an adverbial "indeed, in truth" sense (quả thực là..., built from the same literal components, 果 "result/indeed" + 實 "real/true") — the literal "fruit" sense survives but is secondary/literary, with `trái cây` as the real everyday word for fruit. Documented this explicitly in prose rather than silently filling the field and leaving the collision unexplained, same standard as [[不同]]'s 부동/不動 collision earlier in this sweep.

**Incidental fix**: both constituent character pages lacked a `## Words` backlink to this compound at all — `characters/果.md` had no `## Words` heading whatsoever (bare bullets sitting directly under the meta-bind-embed, with floating CC-initial/final links above them — character-sweep territory, left untouched), so added the heading plus a proper ruby entry; `characters/実.md` already had a `## Words` section (one entry, 真実) and just needed the new ruby line appended.

No homophones (`注音: ㄍ⺢ㄙㄧㄊ` unique to this file).

Next: #55 (種子), #58 (樹皮), #59 (草花), #62 (皮膚), #67 (卵子), #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 31 — [[words/種子|種子]]

Swadesh #55 ("seed"). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter cleanup**: `characters: [種, 子]` (inline array) converted to standard block-list form. `vietnamese:` and `hsk_level:` were both blank — `hsk_level` had no attested value so removed entirely; `vietnamese` was fillable (see below). `aliases: []` (empty list) removed entirely, per the standard blank-optional-field rule.

**No internal derivation bug**: `羅馬字`/`諺文`/`注音` (`jongji`/종지/ㄐㄛㄫㄐㄜ) already matched both constituent characters' own fields exactly. `kwin: false` was already correct per the AND-rule (`characters/種.md` is `true`, `characters/子.md` is `false` → compound `false`).

No `stand_in` note needed — 種's own `stand_in` is `種類`, 子's own is `児子`; neither points to this word.

**Vietnamese field filled, register-narrowing finding**: `chủng tử` is a real, attested Sino-Vietnamese compound (confirmed via search), but its actual modern usage has narrowed almost entirely to a Buddhist-philosophical technical term (the karmic "seed," Sanskrit bīja) — the everyday Vietnamese word for a literal plant seed is the unrelated native compound `hạt giống`. Documented explicitly in prose rather than silently filling the field, same standard as [[果実]]'s quả thực finding last iteration.

**Incidental fix**: `characters/種.md` had no `## Words` section at all (bare bullet under a wrongly-leveled `# Notes`, no heading) — added the section with a proper ruby entry. `characters/子.md` already listed `[[種子]]` in its very large existing `## Words` list, but bare/unformatted — reformatted just that one line to ruby form; left the rest of that page's substantial pre-existing mess (floating CC-initial/final links mid-list, inconsistent bare-vs-ruby entries throughout, multiple unlabeled `###` subsections) untouched despite the page already carrying `date-last-perfect: 2026-03-22` — a stale/loosely-verified stamp from before current standards, same class of finding as [[漆]]'s in iteration 2 of this sweep; flagged here, not re-litigated, since fixing all of 子's page is well outside a single words-only iteration's scope.

No homophones (`注音: ㄐㄛㄫㄐㄜ` unique to this file).

Next: #58 (樹皮), #59 (草花), #62 (皮膚), #67 (卵子), #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 32 — [[words/樹皮|樹皮]]

Swadesh #58 ("bark"). Stamped `date-last-perfect: 2026-07-22`. Already close to complete — `羅馬字`/`諺文`/`注音` (`subi`/수비/ㄙㄨㄅㄧ) already matched both constituent characters' own fields exactly, `vietnamese: vỏ cây` was already filled, and `characters/皮.md` already had a proper ruby backlink to this word — the cleanest starting point in a few iterations.

**Frontmatter cleanup**: non-canonical `## Etymology` heading renamed to `## Notes` (same fix applied repeatedly earlier this sweep, e.g. [[利用]], [[如何]]); removed a blank `hsk_level:` field.

**kwin: false already correct** per the AND-rule (`characters/樹.md` is `true`, `characters/皮.md` is `false` → compound `false`). No `stand_in` match on either side (樹's own is `樹木`, 皮's own is `皮革`) — no stand-in note needed.

**Homophone false-positive caught and ruled out**: a raw `注音` substring grep for `ㄙㄨㄅㄧ` also surfaced `words/水平.md`, but its actual full reading is `ㄙㄨㄅㄧㄫ` (subyeng) — one syllable longer, not an exact match — so no `[!warning]` callout applies; confirmed via each file's own stored `羅馬字`/`諺文`/`注音` rather than trusting the substring hit.

**Register-narrowing finding, not a bug**: kept `vỏ cây` (native Vietnamese) as the field value since it's the genuine everyday word, and added the real Sino-Vietnamese cognate `thụ bì` to the prose instead — verified via search that it survives mainly in traditional-medicine pharmacopoeia entries (naming a specific tree's bark as an ingredient, e.g. 海桐皮, 香加皮) rather than as a general "bark" word.

**Incidental fix**: `characters/樹.md`'s own `## Words` entry for this compound was bare (`[[樹皮]] "bark, plant-skin"`) — reformatted to ruby form.

Next: #59 (草花), #62 (皮膚), #67 (卵子), #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...
