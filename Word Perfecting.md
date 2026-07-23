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

### 2026-07-22, iteration 33 — [[words/草花|草花]]

Swadesh #59 ("flower"). Stamped `date-last-perfect: 2026-07-22`. **The largest wrong-word conflation found this sweep since [[人等]]/[[我等]]/[[其人等]] — same bug class, fourth instance.**

**The conflation**: every cross-linguistic field (`mandarin: huāduǒ`, `korean: 꽃`, native Japanese `はな`, plus `aliases: [花朵]`) described 花朵 ("a flower/blossom," 花 + a flower-counting measure word), not the actual title compound 草花 ("grass-flower," flowering plants collectively, with a herbaceous connotation next to showier cultivated blooms) — 花朵 is not even a separate file anywhere in this vault. Corrected every field to describe 草花 itself, verified via Wiktionary and search rather than assumed: Mandarin **cǎohuā** (also, as a striking aside, the Beijing-region card-game name for the clubs ♣ suit); Japanese has two real readings, native **くさばな** (kusabana, kept as the field value) and on'yomi そうか (sōka); Korean **초화** (chohwa, Sino-Korean) next to the everyday native 꽃 that the old field wrongly held; Vietnamese **thảo hoa** (attested, also found reversed as 花草/hoa thảo). Removed the `花朵` alias entirely — it was never a legitimate alternate spelling of this word, same root-cause pattern as the other three X-等/-flower conflations.

**No internal derivation bug** — `羅馬字`/`諺文`/`注音` (`cauhwa`/찻화/ㄑㄚㄨㄏ⺢) already correctly matched both constituent characters' own fields; only the cross-linguistic layer was wrong. `kwin: false` already correct per the AND-rule (`characters/草 (char).md` is `false`, `characters/花.md` is `true` → compound `false`). Removed a blank `hsk_level:` field.

**Stand-in note applied**: `characters/花.md`'s own `stand_in` field is `草花` — added "— stand-in for [[花]], which cannot appear independently," even though 花 is an extremely common, independently-meaningful character in every source language; trusted the vault's own stored field (this is a Dan'a'yo-internal boundedness rule — 花's `boundedness: 100` — not a claim about the character's status in Chinese/Japanese/Korean/Vietnamese).

**Incidental fixes**: `characters/草 (char).md` had no backlink to this word at all — added a proper ruby entry. `characters/花.md` already listed `[[草花]]` bare — reformatted to ruby with gloss and the new stand-in note.

No homophones (`注音: ㄑㄚㄨㄏ⺢` unique to this file).

Next: #62 (皮膚), #67 (卵子), #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 34 — [[words/皮膚|皮膚]]

Swadesh #62 ("skin"). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter cleanup**: `characters: [皮, 膚]` (inline array) converted to block form. `korean: "피부, 살갗"` was a comma-dump of two different words — narrowed to `피부` (the real Sino-Korean reading of this specific compound) and moved `살갗` (the fully native, more literary alternative — which turns out to already be `characters/膚.md`'s own `korean_native` value) into the prose as commentary instead, same fix pattern as [[一切]]/[[知]] earlier in this sweep. Removed blank `hsk_level:` and empty `aliases: []`. Filled a previously-missing `kwin` field entirely (was absent, not just blank) — computed `false` per the AND-rule (`characters/皮.md` and `characters/膚.md` are both individually `false`).

**No internal derivation bug** — `羅馬字`/`諺文`/`注音` (`bipu`/비푸/ㄅㄧㄈㄜ) already matched both constituent characters' own fields exactly.

**Stand-in note applied**: `characters/膚.md`'s own `stand_in` field is `皮膚` — added "— stand-in for [[膚]], which cannot appear independently." (皮's own `stand_in` is `皮革`, a different word — no note on that side.)

**Vietnamese field filled**: `bì phu`, a real attested Sino-Vietnamese clinical/dermatological term (verified via search) — but noted in prose that the everyday Vietnamese word for skin is the native `da`, which even Vietnamese dermatology's own name for itself (`da liễu`) prefers over `bì phu`.

**No incidental character-page fixes needed** — both `characters/皮.md` and `characters/膚.md` already carried a correctly-formatted ruby backlink to this word. No homophones (`注音: ㄅㄧㄈㄜ` unique to this file).

Next: #67 (卵子), #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 35 — [[words/卵子|卵子]]

Swadesh #67 ("egg, ovum"). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter cleanup**: `characters:` unindented dash list reformatted to standard block indent. `cantonese: "leon2zi2"` was missing a space between syllables — fixed to `leon2 zi2`. Removed blank `hsk_level:` and an empty `aliases:` key.

**Real `korean` bug caught, tied directly to a standing vault rule**: the stored value `난자` (nanja) applies South Korean 두음법칙 (word-initial ㄹ→ㄴ shift), but `characters/卵.md`'s own `korean` field is `란`, per [[AIOS/memory/feedback_korean_reading_north|the vault's standing North Korean/문화어 rule]] — corrected the compound to `란자` (ranja) to match. First time this specific rule has needed enforcing on a *compound word* rather than a bare character field in this sweep.

**No internal Dan'a'yo derivation bug** — `羅馬字`/`諺文`/`注音` (`lanji`/란즈/ㄌㄚㄋㄐㄜ) already matched both constituent characters' own fields. `kwin: false` already correct per the AND-rule (`characters/卵.md` is `true`, `characters/子.md` is `false` → compound `false`).

**Stand-in note applied**: `characters/卵.md`'s own `stand_in` field is `卵子` — added "— stand-in for [[卵]], which cannot appear independently."

**Vietnamese field corrected, not just filled**: the stored `trứng` is the generic everyday native word for "egg" (including a food/chicken egg) — replaced with `noãn`, the real, precise Sino-Vietnamese biological term for the ovum/egg cell specifically (attested in both botany, the plant ovule, and human reproductive biology), matching this word's own precise "ovum" gloss rather than the general "egg" sense.

**Incidental fixes**: added a missing `## Words` backlink section to `characters/卵.md` (had none at all). On `characters/子.md`, initially added a new ruby entry without first checking whether one already existed in its very large pre-existing list — it did, as a bare `[[卵子]] - egg` line — caught the resulting duplicate immediately and removed the old bare copy, keeping the single ruby-formatted line. Worth remembering: check for an existing (even unformatted) entry before appending, not just at the top of the list.

No homophones (`注音: ㄌㄚㄋㄐㄜ` unique to this file).

Next: #70 (羽毛), #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 36 — [[words/羽毛|羽毛]]

Swadesh #70 ("feather"). Stamped `date-last-perfect: 2026-07-22`. A clean iteration — `羅馬字`/`諺文`/`注音` (`'umau`/우맛/ㄨㄇㄚㄨ) already matched both constituent characters' own fields, and `mandarin`/`cantonese`/`japanese`/`korean` were all already correctly filled.

**Frontmatter cleanup**: removed blank `hsk_level:` and empty `aliases: []`. `kwin: false` already correct per the AND-rule (`characters/羽.md` is `true`, `characters/毛 (char).md` is `false` → compound `false`).

**Stand-in note applied**: `characters/羽.md`'s own `stand_in` field is `羽毛` — added "— stand-in for [[羽]], which cannot appear independently." (毛's own `stand_in` is bare `毛` itself — no note on that side.)

**Vietnamese field filled**: `vũ mao`, a real attested Sino-Vietnamese compound (verified via search) — also found in the reversed order 毛羽 (mao vũ) in Vietnamese-Chinese dictionaries, the same free-word-order pattern already noted on [[介紹]]/紹介 and [[草花]]/花草 earlier in this sweep.

**Incidental fix**: `characters/羽.md` had no `## Words` section at all — added one with a proper ruby entry. `characters/毛 (char).md` already had a correctly-formatted ruby backlink — no fix needed there.

No homophones (`注音: ㄨㄇㄚㄨ` unique to this file).

Next: #71 (頭髪), #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 37 — [[words/頭髪|頭髪]]

Swadesh #71 ("hair"). Stamped `date-last-perfect: 2026-07-22`.

**Investigated, not a bug**: `mandarin: "tóufà, tóufǎ"` looked at first glance like the same comma-dump error class fixed repeatedly this sweep (一切, 知, 之間) — but this one turned out to be a genuine regional standard split, not an error. Verified via Wiktionary: 髮/发's own citation tone splits Mainland Putonghua **fà** (fourth tone, matching `characters/髪.md`'s own stored `mandarin: fà`) vs. Taiwan Guoyu **fǎ** (third tone) — both are real, standard, attested readings of the same character in different national standards. Reformatted the comma string into a proper YAML list (matching the [[主意]]/[柏] precedent for words with more than one genuinely valid Mandarin reading) rather than picking one and discarding the other.

**No internal Dan'a'yo derivation bug** — `羅馬字`/`諺文`/`注音` (`toubad`/톳받/ㄊㄛㄨㄅㄚㄊ) already matched both constituent characters' own fields. `kwin: false` already correct per the AND-rule (`characters/頭 (char).md` and `characters/髪.md` are both individually `false`). Removed a blank `hsk_level:` field; kept the existing `aliases: [頭髮]` (legitimate — 髮 is 髪's own documented traditional form).

**Stand-in note applied**: `characters/髪.md`'s own `stand_in` field is `頭髪` — added "— stand-in for [[髪]], which cannot appear independently." (頭's own `stand_in` is bare `頭` itself — no note on that side.)

**Vietnamese left as-is with added context**: kept `tóc` (the genuine everyday native word) as the field value, and noted in prose that the fuller native compound `đầu tóc` ("head-hair") is more common than the literal Sino-Vietnamese calque `đầu phát`, which is attested but rare — same native-vs-Sino-Xenic register pattern as several other iterations this sweep.

**Incidental fixes**: added missing `## Words` backlinks to both `characters/頭 (char).md` and `characters/髪.md` (the latter had no `## Words` section at all, just an empty `## Notes` before `## Chengyu`).

No homophones (`注音: ㄊㄛㄨㄅㄚㄊ` unique to this file).

Next: #74 (目), #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 38 — [[words/目|目]]

Swadesh #74 ("eye"). Stamped `date-last-perfect: 2026-07-22`. First single-character word since the original HSK-1 batch ([[一]]/[[七]]/[[天]]/[[小]]/[[道]]) — 目's own `stand_in` is bare `目` itself, so this word is the character standing alone, not a compound.

**Frontmatter cleanup**: `characters: 目 (char)` (bare scalar) converted to a proper list. Filled a previously-blank `vietnamese` field with `mục`, inherited directly from `characters/目 (char).md`'s own stored value (word and character are the same reading here). Non-canonical `# Notes` (empty) promoted to `## Notes` with real content.

**Homophone found and handled**: [[牧]] "shepherd; herd" shares 目's exact reading (ㄇㄨㄎ/mug/묵) — added the `[!warning]` callout to 目 and the reciprocal callout to 牧 (itself still otherwise unperfected — no `swadesh` field, a stray `vietnamese: null` literal, empty `# Notes` — flagged, not fixed, same minimal-touch precedent as every prior homophone cluster this sweep).

**Genuine register-narrowing finding, both directions**: unlike [[天]]/[[小]]/[[道]], which mostly kept native everyday readings as-is, 目 turned out to be the reverse case — the character is productive and independent in *compounds* across Mandarin/Cantonese/Korean/Vietnamese (題目, 目的, 科目, mục lục, mục tiêu) but is *not* how any of those languages say bare "eye" in everyday speech (Mandarin prefers 眼睛, Vietnamese prefers native mắt), with unbound 目 reserved for literary/classical registers (目不轉睛, 一目瞭然) or an extended "item/category" sense. Documented this asymmetry directly rather than treating the compositional readings as claims of standalone everyday usage.

Next: #77 (長牙), #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 39 — [[words/長牙|長牙]]

Swadesh #77 ("tusk, fang"). Stamped `date-last-perfect: 2026-07-22`. A dense iteration — several distinct findings stacked on one page.

**Genuine Mandarin heteronym found, not a bug**: verified that 長/长 in this compound's "tusk" noun sense reads *cháng* ("long"), while the identical written form 长牙 is also common as a verb meaning "to teethe" — there 長/长 instead reads *zhǎng* ("to grow"). Same characters, different grammatical function, distinguished only by tone/context. Confirmed the frontmatter's `mandarin: chángyá` already correctly targets the noun sense before treating anything else as settled.

**Cross-linguistic asymmetry, disclosed rather than force-corrected — same standard as [[男人]] earlier in this sweep**: `japanese: きば` and `korean: "송곳니"` were both wrong-word substitutions (きば is bare 牙 alone's own native reading; 송곳니 is a fully native Korean word for "canine tooth," not a reading of this compound at all). Corrected both to honest compositional readings — Japanese `ちょうが` (chōga), Korean `장아` (jang-a) — and documented in prose that none of Japanese, Korean, or Vietnamese actually use a 長牙-based compound as their real word for "tusk": Japanese says bare 牙 (きば), Korean says native 송곳니, Vietnamese says native `răng nanh` (kept as the honest compositional value `trường nha` in frontmatter, with the real native word disclosed in prose, same pattern).

**Aliases corrected — two separate problems**: removed a self-referential `長牙` alias (a word can't be its own alias, same slip as [[健康]]); removed `尖牙`, which is not an orthographic variant at all but a genuinely distinct, narrower concept — "canine tooth" (a sharp pointed tooth) rather than "tusk" (an elongated overgrown tooth, as in elephants/walruses) — flagged as a real near-synonym deserving its own future word file, not folded into this one. Kept `长牙`, the genuine simplified form.

No internal Dan'a'yo derivation bug (`羅馬字`/`諺文`/`注音`: `jang'a`/장아/ㄐㄚㄫ·ㄚ already matched both characters). `kwin: false` already correct per the AND-rule (`characters/長 (char).md` is `true`, `characters/牙.md` is `true`... wait — both `true` would predict `true`; double-checked: `characters/牙.md` is in fact `kwin: true`, and `characters/長 (char).md` is also `kwin: true` — the AND-rule would predict `true`, but the stored value is `false`. Left as-is rather than silently overriding, since the direct check (Dan'a'yo 장아 vs. the honest-compositional Korean 장아) shows no divergence either way at the level this word's Korean field can attest — flagging this as a possible discrepancy worth a second look rather than resolving it by guesswork, since the compound's Korean reading itself doesn't correspond to a real independent word to compare against.

Removed blank `hsk_level:`. **Stand-in note applied**: `characters/牙.md`'s own `stand_in` field is `長牙` — added "— stand-in for [[牙]], which cannot appear independently." No exact homophones (`注音: ㄐㄚㄫ·ㄚ` — two substring false-positives, 掌握/障碍, ruled out by comparing full stored `注音` values).

**Incidental fixes**: added `## Words` backlinks to both `characters/長 (char).md` (bare bullets, no heading — added inline) and `characters/牙.md` (no `## Words` section at all — added one).

Next: #79 (指甲), #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 40 — [[words/指甲|指甲]]

Swadesh #79 ("fingernail"). Stamped `date-last-perfect: 2026-07-22`. Another dense iteration.

**Mandarin has three genuine attested readings, not a comma-dump error**: `zhǐjia` (standard neutral-tone colloquial), `zhǐjiǎ` (formal citation-tone), `zhījia` (documented regional colloquial variant) — verified via search and reformatted into a proper YAML list, same treatment as [[頭髪]]'s Mainland/Taiwan split.

**The standout finding — a striking, almost certainly unintentional Korean homophone**: this compound's honest compositional reading is 지갑 (jigap), which is also, completely independently, the extremely common everyday Korean word for "wallet" (built from unrelated hanja 紙匣, "paper case"). Real spoken Korean doesn't use 指甲 as a word at all — the exclusive standard term is native 손톱 — so the collision is mostly theoretical, but flagged prominently in the prose given how common 지갑 "wallet" is; corrected the wrong stored field (`손톱`, the native word, was sitting in a field meant to hold this compound's own Sino-Korean reading) to the honest compositional value with the caveat attached.

**Japanese field corrected with an interesting root-cause finding**: `つめ` (tsume) was the old value — traced to `characters/甲 (char).md`'s own `japanese_native` list, which separately documents つめ as one of 甲's *own* alternate kun'yomi (alongside よろい "armor" and きのえ "first heavenly stem") — i.e. the word's field had quietly borrowed one constituent character's own bare reading rather than describing the compound. Corrected to the honest on'yomi-compositional しこう (shikō); real Japanese uses 爪 (also tsume, an unrelated character) as its actual word for fingernail.

**Vietnamese corrected, not merely filled**: replaced the native `móng tay` with the real, attested Sino-Vietnamese compound `chỉ giáp` (found in historical/Qing-dynasty nail-care register, e.g. 護甲 hộ giáp "nail guard") — noting `móng tay` in prose as the everyday native word instead.

**Homophone reformatted, not newly found**: the page already flagged (informally, via a non-standard `[!tip]` line positioned *before* the meta-bind-embed) that this word is a homophone of [[自家]] "one's own family" — verified the exact match (`注音`/`羅馬字`/`諺文` identical: ㄐㄧㄜㄍㄚㄆ/jiǝgab/즤갑), then converted both pages to the standard `[!warning] Homophones` callout in the correct position. `自家.md` had also been carrying a stale `date-last-perfect: 2026-03-13` stamp despite the malformed callout — same "stale/loosely-verified stamp" class of finding as [[漆]] and `characters/子.md` earlier this sweep; fixed only the callout, did not re-verify or re-stamp the rest of that page.

Removed blank `hsk_level:` and an empty `aliases:` key. No `stand_in` match on either constituent (指's own is `手指`, 甲's own is bare `甲`) — no stand-in note needed, this is an independent compound, not a legitimizer.

**Incidental fixes**: added missing `## Words` backlinks to both `characters/指.md` and `characters/甲 (char).md` (the latter had no `## Words` section at all).

Next: #84 (羽翼), #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 41 — [[words/羽翼|羽翼]]

Swadesh #84 ("wing"). Stamped `date-last-perfect: 2026-07-22`. Unlike the last several iterations, this one confirmed the compound is genuinely, richly attested everywhere — no wrong-word substitutions this time, only a wrongly-corrected-toward-native field and a stale `kwin`.

**The centerpiece finding — a real homophone collision, independently attested in two languages, not a vault error**: this compound's honest reading — Japanese うよく (uyoku), Korean 우익 (previously wrongly replaced with native `날개` in the frontmatter) — is a genuine, live homophone of the unrelated, far more common word 右翼 ("right wing," political/military; also うよく/우익), since 羽 and 右 happen to share identical Sino-Japanese and Sino-Korean readings. Verified via search that both 羽翼 ("wing; assistance," with a real chengyu 羽翼已成/已豐, "the wings have grown," i.e. one has become fully capable) and 右翼 are real, independently attested words in both languages, coexisting as true homophones rather than one crowding out the other — a pleasing parallel to the [[指甲]]/지갑 finding two iterations ago, except here *both* readings are real (there, only one side was).

**`kwin` corrected `false` → `true`**, the second confirmed active fix this sweep (after [[父親]]): both `characters/羽.md` and `characters/翼.md` are individually `true`, and — unlike [[長牙]]'s and [[指甲]]'s unattested compositional-only Korean fields — this compound's Korean reading is independently real and verified, so the AND-rule prediction could be directly confirmed rather than left flagged.

**Other fields**: filled blank `cantonese: jyu5 jik6` (compositional, parallel to the real Mandarin/Japanese/Korean attestation) and corrected `vietnamese` from native `cánh` to the real, attested Sino-Vietnamese `vũ dực`, which carries the identical literal-wing/figurative-assistance double meaning found across the whole sphere (verified via search, e.g. `tả dực`/`hữu dực`, "left/right flank"). `characters:` inline array converted to block form; removed empty `aliases: []`. **Stand-in note applied**: `characters/翼.md`'s own `stand_in` field is `羽翼` — the page already informally noted this as a bare "Stand-in for [[翼]]" line; wove it into the proper opening Notes bullet.

**Homophone false-positive investigated and correctly ruled out — a new class this time**: a raw `注音` grep also matched `words/域.md` (identical string `ㄨㄧㄎ`), but its own `羅馬字`/`諺文` (`wig`/윅, one syllable) diverge from 羽翼's (`'u'ig`/우익, two syllables) — the same Bopomofo string is evidently ambiguous between a w-glide-initial single syllable and a vowel-initial two-syllable sequence. Not a real pronunciation match, so no `[!warning]` callout — worth remembering as a distinct false-positive class from the plain prefix-substring collisions found on [[樹皮]] and [[長牙]] earlier this sweep.

**Incidental fixes**: added missing `## Words` backlinks to both `characters/羽.md` and `characters/翼.md` (the latter had none at all).

Next: #86 (腸管), #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 42 — [[words/腸管|腸管]]

Swadesh #86 ("intestine"). Stamped `date-last-perfect: 2026-07-22`.

**A third instance this sweep of the same striking Sino-Xenic homophone pattern** ([[羽翼]]/右翼, [[指甲]]/지갑): 腸's Sino-Japanese/Sino-Korean reading coincides exactly with 長 ("long, chief"), making 腸管 a genuine, live homophone of the unrelated, very common 長官 ("minister/director-general") — Japanese ちょうかん, Korean 장관. Verified both compounds are real, independently attested words in both languages; the stored `korean` field had been wrongly holding the native word `창자` ("intestines," `characters/腸.md`'s own `korean_native` value) instead of this compound's genuine Sino-Korean reading — corrected to `장관`.

**Vietnamese corrected**: replaced the comma-dumped `ruột, tràng` with the honest compositional Sino-Vietnamese `tràng quản`; noted in prose that `tràng` alone is thoroughly productive in real Vietnamese medical vocabulary (trực tràng "rectum," đại tràng "colon," tá tràng "duodenum") even though the exact two-syllable compound isn't independently confirmed, while `ruột` is the everyday native word for intestines.

**Aliases corrected**: kept `肠管` (genuine simplified form); removed `腸子`/`肠子` — not orthographic variants but a distinct, more colloquial compound (腸 + the noun-forming suffix 子, same pattern as [[種子]]/[[卵子]]) with no file of its own in this vault — flagged as a future word-creation candidate, same treatment as [[長牙]]'s 尖牙 finding two iterations ago.

**No internal Dan'a'yo derivation bug** — `羅馬字`/`諺文`/`注音` (`canggwan`/창관/ㄑㄚㄫㄍ⺢ㄋ) already matched both characters. `kwin: false` already correct per the AND-rule (`characters/腸.md` is `false`, `characters/管.md` is `true` → compound `false`). `characters:` inline-array-adjacent unindented list reformatted to standard block form; non-canonical `## Etymology` heading renamed to `## Notes`; removed blank `hsk_level:`.

**Stand-in note applied**: `characters/腸.md`'s own `stand_in` field is `腸管` — added "— stand-in for [[腸]], which cannot appear independently." (管's own `stand_in` is `導管`, a different word — no note on that side.) No homophones (`注音: ㄑㄚㄫㄍ⺢ㄋ` unique to this file).

**Incidental fixes**: reformatted `characters/腸.md`'s bare `[[腸管]]` entry to ruby form with the stand-in note; added a missing `## Words` backlink entry to `characters/管.md`.

Next: #87 (頚), #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 43 — [[words/頚|頚]]

Swadesh #87 ("neck"). Stamped `date-last-perfect: 2026-07-22`. Second single-character self-standing word this sweep (after [[目]]) — `characters/頚 (char).md`'s own `stand_in` is bare `頚` itself.

**Real `kwin` bug caught**: stored `true`, but should simply match `characters/頚 (char).md`'s own `kwin: false` exactly, since word and character are identical here — Dan'a'yo 깅 (ging) and Korean 경 (gyeong) diverge in vowel/coda, so `false` is correct. Corrected `true`→`false`.

**Frontmatter cleanup**: filled previously-blank `korean` (`경`) and `vietnamese` (`cảnh`, verified via search as the real Sino-Vietnamese reading — specifically the front of the neck, as opposed to 項/hạng for the nape) by inheriting/confirming against the character's own stored fields. `characters: 頚 (char)` bare scalar converted to a list.

**Register-narrowing finding**: Mandarin/Cantonese/Vietnamese all use this reading productively and independently for "neck," but Japanese and Korean both strongly prefer native words in everyday speech (くび, 목), reserving the Sino-Xenic reading for technical/medical compounds (頚椎/경추, "cervical vertebra").

No homophones (`注音: ㄍㄧㄫ` unique to this file). No character-page backlink needed — this is a self-standing single-character word, not a compound.

Next: #89 (胸部), #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 44 — [[words/胸部|胸部]]

Swadesh #89 ("chest"). Stamped `date-last-perfect: 2026-07-22`. A clean iteration.

**Frontmatter cleanup**: `characters:` unindented dash list reformatted to standard block indent. Removed blank `hsk_level:` and empty `aliases:`. Filled `vietnamese` with the honest compositional `hung bộ` — `hung` alone is confirmed real Sino-Vietnamese (胸襟 hung khâm, "breadth of mind"; 胸次 hung thứ) but the everyday, essentially universal word for the body part is native `ngực`, documented in prose.

**No internal Dan'a'yo derivation bug** — `羅馬字`/`諺文`/`注音` (`hyongbou`/횽봇/ㄏ⼄ㄫㄅㄛㄨ) already matched both characters. `kwin: false` already correct per the AND-rule (both constituents individually `false`).

**Stand-in note applied**: `characters/胸.md`'s own `stand_in` field is `胸部` — added "— stand-in for [[胸]], which cannot appear independently." (部's own `stand_in` is bare `部` — no note on that side.)

**Register-narrowing finding**: Mandarin/Cantonese/Japanese/Korean all use this compound as the standard clinical/formal register term, each alongside an everyday native alternative for casual speech (Japanese bare 胸/むね, Korean 가슴).

**Incidental fixes**: added missing `## Words` backlinks to both `characters/胸.md` (had none) and `characters/部 (char).md` (had a large bare, unformatted list with no ruby anywhere — added just this one entry in proper form, left the rest untouched as character-sweep territory).

No homophones (`注音: ㄏ⼄ㄫㄅㄛㄨ` unique to this file).

Next: #90 (心臓), #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 45 — [[words/心臓|心臓]]

Swadesh #90 ("heart, organ"). Stamped `date-last-perfect: 2026-07-22` (previously had no stamp at all).

**Frontmatter cleanup**: blank `pos:` filled to `名詞`; quoted `"心 (char)"` in the `characters` list for consistency. `kwin: true` already correct per the AND-rule (both `characters/心 (char).md` and `characters/臓.md` are individually `true`) — and here, unlike [[長牙]]/[[指甲]]'s ambiguous cases, this compound's Korean 심장 is an unambiguous, extremely common real word for "heart," so the AND-rule result is directly confirmed.

**Homophone reformatted, not newly found**: the page already informally flagged (via a misplaced `[!warning]`/`[!tip]` line before the meta-bind-embed, on both this page and its partner) that this word is an exact homophone of [[深長]] "long and deep; profound" (`注音`/`羅馬字`/`諺文` all identical: ㄙㄧㄇㄐㄚㄫ/simjang/심장) — converted both pages to the standard `[!warning] Homophones` callout in the correct position. `深長.md` itself remains otherwise unperfected (blank `pos`/`vietnamese`/`hsk_level`/`swadesh`, empty `aliases: []`) — flagged, not otherwise fixed, same minimal-touch precedent as every prior homophone cluster this sweep.

**Genuine Vietnamese doublet, not a bug**: kept the field value `tim` (concrete, anatomical "heart as an organ") as-is — `characters/心 (char).md`'s own `vietnamese` field separately lists both `tim` and `tâm` (the more abstract "heart/mind," as in tâm hồn "soul") as two historically distinct layers of borrowing from the same character, split by sense/register rather than being alternate spellings of one reading; documented this split explicitly rather than treating it as noise to collapse.

**Small fix**: the opening Notes bullet's character links used bare `characters/X.md` paths (missing the `../` prefix required from within `/words/`) — corrected to `../characters/`.

**Incidental fix**: `characters/臓.md` had an empty `## Words` section (heading present, no entries) — added the ruby backlink. `characters/心 (char).md` already had one, correctly formatted.

No `stand_in` match on either constituent (心's own is bare `心`, 臓's own is `内臓`) — this is an independent compound, not a legitimizer, so no stand-in note.

Next: #91 (肝臓), #99 (呼吸), #104 (思考), ...

### 2026-07-22, iteration 46 — [[words/肝臓|肝臓]]

Swadesh #91 ("liver"). Stamped `date-last-perfect: 2026-07-22` (previously unstamped).

**A fourth instance this sweep of the recurring Sino-Xenic homophone pattern, and the best-documented one yet**: Korean 간장 (gan-jang) is a genuine, dictionary-recognized homograph — Wiktionary lists it as two entirely separate etymological entries under the identical spelling: the everyday household word for "soy sauce" (native 간 + Sino 醬, "sauce") and this compound's own Sino-Korean medical reading for "liver" (from 肝臟/肝臓). Both are real, common words; noted that the bare native/Sino-Korean reading 간 alone is the more frequent everyday way to say "liver" outside clinical registers, alongside this fuller medical compound.

Confirmed `pos: 実詞` is a legitimate, established category in this vault (318 other files use it) rather than a typo for `名詞` as I first suspected — left unchanged. `kwin: true` already correct per the AND-rule (both `characters/肝.md` and `characters/臓.md` are individually `true`); `vietnamese: gan` already correctly matches one of `characters/肝.md`'s own attested readings (alongside `can`, `gang`). Non-canonical `## Etymology` heading and a stray informal "Stand-in for [[肝]]" line both folded into a single proper `## Notes` opening bullet with the standard stand-in phrasing (`characters/肝.md`'s own `stand_in` field is `肝臓`). Removed blank `hsk_level:`. Kept both aliases (`肝脏`, `肝臟`) — legitimate, matching `臓`'s own documented traditional/simplified variants.

No homophones (`注音: ㄍㄚㄋㄐㄚㄫ` unique to this file). **Incidental fixes**: reformatted `characters/肝.md`'s bare `[[肝臓]]` entry to ruby form with the stand-in note; added a missing `## Words` entry to `characters/臓.md`.

Next: #99 (呼吸), #104 (思考), ...

### 2026-07-23, iteration 47 — [[words/呼吸|呼吸]]

Swadesh #99 ("breathe"). Stamped `date-last-perfect: 2026-07-23`.

**Real `pos` bug caught**: stored `性詞` (quality/adjective-like), corrected to `事詞` (verb-like/"event"), matching `characters/呼 (char).md`'s own stored `pos: 事詞` — a word for "breathe" doesn't fit the adjective-like category.

**No internal Dan'a'yo derivation bug** — `羅馬字`/`諺文`/`注音` (`hohib`/호힙/ㄏㄛㄏㄧㄆ) already matched both characters. `kwin: false` already correct per the AND-rule (`characters/呼 (char).md` is `true`, `characters/吸 (char).md` is `false` → compound `false`).

**No `stand_in` relationship applies**: both constituent characters already have their own bare-character `stand_in` (each is its own legitimizer — 呼's is bare `呼`, 吸's is bare `吸`) — 呼吸 is an independent compound, not a legitimizer for either, so no stand-in note.

**All cross-linguistic fields were already correct** — genuinely the ordinary, everyday word for "breathe/respiration" in all five target languages, no native-word substitution to untangle this time (a contrast with most of the last several iterations). Quoted the `characters` list entry for `呼 (char)` for consistency (吸's was already quoted).

No homophones (`注音: ㄏㄛㄏㄧㄆ` unique to this file). **Incidental fix**: added a missing `## Words` backlink to `characters/吸 (char).md` (which already correctly preserves its "abbreviation for samarium" periodic-table note per the standing rule — untouched, just inserted above it).

Next: #104 (思考), ...

### 2026-07-23, iteration 48 — [[words/思考|思考]]

Swadesh #104 ("think"). Stamped `date-last-perfect: 2026-07-23`.

**The richest homophone cluster found this entire sweep, richer than the pairwise collisions on [[羽翼]]/右翼, [[指甲]]/지갑, [[腸管]]/長官, and [[肝臓]]/soy-sauce-간장**: Korean 사고 (sago) is a documented **five-way** homophone cluster with its own Korean Wikipedia disambiguation page — this word's own 思考 ("thinking") shares the identical spelling with 事故 (an accident — by far the most common everyday sense of 사고), 史庫 (historical archive), 社告 (company announcement), and 四苦 (the Buddhist "four sufferings"). Noted, but not independently re-verified to the same depth, that Japanese しこう is likewise known for unusually dense homophony (志向, 指向, 試行, 至高, among others).

**Small fix**: `cantonese: "s1 haau2"` was missing a vowel — corrected to `si1 haau2`, matching `characters/思.md`'s own stored `si1`. Filled blank `vietnamese` with the real, attested Sino-Vietnamese `tư khảo` (verified via search); the everyday native word is `suy nghĩ`. Removed empty `aliases: []` and blank `hsk_level:`.

**Stand-in note applied**: `characters/思.md`'s own `stand_in` field is `思考` — folded the informal "Stand-in for [[思]]" line into the proper opening bullet. (考's own `stand_in` is `考慮`, a different word — no note on that side.) Non-canonical `## Etymology` heading renamed to `## Notes`. `kwin: false` already correct per the AND-rule (`characters/思.md` is `true`, `characters/考.md` is `false` → compound `false`).

No Dan'a'yo-internal homophones (`注音: ㄙㄚㄎㄚㄨ` unique to this file). **Incidental fixes**: reformatted `characters/思.md`'s bare `[[思考]]` entry to ruby form with the stand-in note; added a missing `## Words` entry to `characters/考.md`.

**Pool refreshed**: re-ran the never-perfected Swadesh query. Next: #106 (恐怖), #111 (戦闘), #113 (打撃), #115 (分裂), #116 (刺), #121 (散歩), #123 (臥), #125 (立), #126 (回転), #127 (落下), #129 (持), #133 (擦拭), #138 (縫製), #139 (計数), #141 (唱歌), #142 (遊戯), #145 (凍結), #146 (膨脹), #147 (太陽), #154 (海洋), #156 (石頭), #158 (灰塵), #165 (氷水), #169 (燃焼), #173 (緑), ...

### 2026-07-23, iteration 49 — [[words/恐怖|恐怖]]

Swadesh #106 ("fear"). Stamped `date-last-perfect: 2026-07-23`.

**Genuine semantic-narrowing finding, not a bug — a real parallel to [[論理]] and [[一切]] earlier in this vault's history**: the Vietnamese field `khủng bố` matches the compositional reading of 恐 (khủng) + 怖 (bố) exactly, but modern Vietnamese has narrowed the compound specifically to "to terrorize" / "terrorism" (chủ nghĩa khủng bố, "terrorism"; kẻ khủng bố, "a terrorist") rather than the broad, everyday "fear, dread, horror" that Mandarin/Cantonese/Japanese/Korean all cover with this same compound (恐怖映画/공포영화, "horror movie"; 恐怖症, "-phobia"). Verified via search rather than assumed, and documented the contrast explicitly — the everyday Vietnamese word for general fear is the unrelated native `sợ hãi`.

**No internal Dan'a'yo derivation bug** — `羅馬字`/`諺文`/`注音` (`kongpo`/콩포/ㄎㄛㄫㄆㄛ) already matched both characters. `kwin: false` already correct per the AND-rule (`characters/恐.md` is `false`, `characters/怖.md` is `true` → compound `false`).

**Stand-in note applied**: `characters/怖.md`'s own `stand_in` field is `恐怖` — added "— stand-in for [[怖]], which cannot appear independently." (恐's own `stand_in` is `恐慌`, a different word — no note on that side.) `characters:` unindented dash list reformatted to block form; removed blank `hsk_level:` and an empty `aliases:` key; non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄎㄛㄫㄆㄛ` unique to this file). **Incidental fixes**: reformatted `characters/恐.md`'s bare `[[恐怖]]` entry to ruby form; added a missing `## Words` entry to `characters/怖.md`.

### 2026-07-23, iteration 50 — [[words/戦闘|戦闘]]

Swadesh #111 ("fight, combat"). Stamped `date-last-perfect: 2026-07-23`. Iteration 50 for this loop.

**Small fix**: `japanese: せんとー` mixed a katakana long-vowel bar into an otherwise-hiragana reading — corrected to standard `せんとう` (sentō). **`pos` corrected `性詞`→`事詞`**, the same fix class as [[呼吸]] a few iterations ago (a "fight/combat" word doesn't fit the quality/adjective-like `性詞` category).

**No `stand_in` relationship applies**: `characters/戦.md`'s own `stand_in` is `戦争`, `characters/闘.md`'s own is `闘争` — both constituents already have their own independent legitimizer compound, so 戦闘 is an independent word, not a stand-in for either.

**All cross-linguistic fields already correct** — genuinely the standard, unambiguous everyday word for "combat" in all five languages, no native displacement or homophone collision found. `characters:`/`aliases:` inline arrays reformatted to block form (kept both traditional aliases 戰鬪/戰鬥, matching `characters/闘.md`'s own documented variant forms). `kwin: false` already correct per the AND-rule (`characters/戦.md` is `true`, `characters/闘.md` is `false` → compound `false`).

No homophones (`注音: ㄐㄝㄋㄉㄛㄨ` unique to this file). **Incidental fixes**: reformatted both `characters/戦.md`'s and `characters/闘.md`'s existing bare `[[戦闘]]` entries to ruby form.

### 2026-07-23, iteration 51 — [[words/打撃|打撃]]

Swadesh #113 ("strike, hit"). Stamped `date-last-perfect: 2026-07-23`. Already close to complete — both `characters/打.md` and `characters/撃 (char).md` had correctly-formatted ruby backlinks to this word already, no incidental character-page fixes needed.

**Small fix**: `mandarin: "dǎjī, dǎjí"` carried a second tone variant, `dǎjí`, with no attestation found anywhere — removed, keeping only the standard `dǎjī`. `characters:`/`aliases:` inline arrays reformatted to block form (kept both traditional/simplified aliases 打擊/打击). Removed blank `hsk_level:`.

**Genuine semantic-narrowing finding, a direct parallel to [[恐怖]]'s khủng bố finding two iterations ago**: kept the field value `đánh` (the versatile everyday native Vietnamese verb "to hit," used in đánh nhau "to fight," đánh trống "to beat a drum"); documented in prose that the real Sino-Vietnamese cognate đả kích is attested but has narrowed specifically to a verbal/rhetorical register — "to attack, to criticize sharply" — rather than this word's physical-impact sense.

**Stand-in note applied**: `characters/打.md`'s own `stand_in` field is `打撃` — added "— stand-in for [[打]], which cannot appear independently." (撃's own `stand_in` is bare `撃` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/打.md` is `false`, `characters/撃 (char).md` is `false` → compound `false`).

No homophones (`注音: ㄉㄚㄍㄝㄎ` unique to this file).

### 2026-07-23, iteration 52 — [[words/分裂|分裂]]

Swadesh #115 ("split, divide"). Stamped `date-last-perfect: 2026-07-23`.

**Real `korean` bug caught, the same standing North Korean rule as [[卵子]]'s 란자 fix earlier this sweep**: stored `분열` applies South Korean 두음법칙-style regularization (렬→열); `characters/裂.md`'s own field is `렬`, and North Korean 문화어 orthography is confirmed (via search — a well-documented, named North/South spelling difference) to preserve `분렬`. Corrected `분열`→`분렬`.

**No `stand_in` relationship applies**: 分's own `stand_in` is bare `分` itself, 裂's own is `破裂` — 分裂 is an independent compound, not a legitimizer for either.

Filled `vietnamese` with the real, attested Sino-Vietnamese `phân liệt` (verified via search); the everyday native word for splitting/dividing generally is `chia` (or `chia rẽ` for a rift between people). Mandarin fēnliè, Cantonese fan1 lit6, and Japanese ぶんれつ were all already correct. Removed blank `hsk_level:` and an empty `aliases:` key.

No homophones (`注音: ㄅㄨㄋㄌㄝㄊ` unique to this file). **Incidental fixes**: added missing `## Words` backlinks to both `characters/分 (char).md` and `characters/裂.md` (the latter had no `## Words` section at all).

### 2026-07-23, iteration 53 — [[words/刺|刺]]

Swadesh #116 ("stab, thorn"). Stamped `date-last-perfect: 2026-07-23`. Third single-character self-standing word this sweep (after [[目]] and [[頚]]) — `characters/刺 (char).md`'s own `stand_in` is bare `刺` itself.

**Frontmatter cleanup**: `characters: 刺 (char)` bare scalar converted to a list; `vietnamese: - chích` (a one-item list) converted to a plain string for consistency with the rest of the corpus.

**Register-narrowing finding**: kept `chích`, one of three attested readings on `characters/刺 (char).md` (alongside `thứ`/`thích`) — documented in prose that `chích` specifically survives in the everyday Vietnamese verb for a sting or injection (chích thuốc, "to get a shot"), narrower than the general "stab" sense the character covers elsewhere. Mandarin/Cantonese/Korean/Japanese all use this character productively and independently, no other issues found.

No homophones (`注音: ㄑㄧㄎ` unique to this file). No character-page backlink needed — self-standing single-character word.

### 2026-07-23, iteration 54 — [[words/散歩|散歩]]

Swadesh #121 ("walk, stroll"). Stamped `date-last-perfect: 2026-07-23`.

**Real `korean` bug caught, with a genuine near-synonym collision underlying it**: the stored value `산책` is not a reading of 散歩/散步 at all — it's the distinct, near-synonymous compound 散策 ("a walking-stick stroll," from 策 "cane/plan," not 歩/步 "step"). Corrected to `산보`, the real Sino-Korean reading of *this* compound — and per search, North Korean 문화어 (and most of the rest of East Asia) actually prefers 산보 for "a walk," while South Korea has shifted toward 산책 as the more common everyday term; both are real, current, distinguished mainly by subtle distance/register nuance, not interchangeable spellings.

**`kwin` corrected `false`→`true`**, the third confirmed active fix this sweep (after [[父親]] and [[羽翼]]): both `characters/散.md` and `characters/歩.md` are individually `true`, and this compound's Korean reading is now a validated real word, so the AND-rule prediction is confirmed rather than left ambiguous.

**Homophone reformatted, not newly found**: the page already informally flagged that this word is an exact Dan'a'yo homophone of [[散布]] "scatter; spread" (identical sanbo/산보/ㄙㄚㄇㄅㄛ, despite Mandarin/Japanese distinguishing them, sànbù/さんぷ vs sànbù/さんぽ) — converted to the standard callout on both pages, also fixing 散布's non-standard `[!warn]` type. **Flagged, not fixed**: `散布.md`'s own `aliases` field lists `散布` as its own alias — a self-referential slip, same class as [[健康]]/[[長牙]] — out of scope for a words-only iteration on a different target.

**Stand-in note applied**: `characters/歩.md`'s own `stand_in` field is `散歩` — added the standard phrasing. (散's own `stand_in` is `散布`, its homophone partner — a coincidence, not a bug.) Filled `vietnamese` with `tản bộ` (real, attested, verified via search — distinguished from đi dạo by connoting a slower, purposeless leisure stroll).

**Incidental fixes**: added missing `## Words` backlinks to both `characters/散.md` and `characters/歩.md` (neither previously listed this compound).

### 2026-07-23, iteration 55 — [[words/臥|臥]]

Swadesh #123 ("lie down"). Stamped `date-last-perfect: 2026-07-23`. Fourth single-character self-standing word this sweep (after [[目]], [[頚]], [[刺]]).

**Frontmatter cleanup**: filled blank `vietnamese` (`ngoạ`, inherited from `characters/臥 (char).md`'s own field) and blank `pos` (`事詞`, a verb-like word); `characters: 臥 (char)` bare scalar converted to a list. `kwin: true` already correct on both word and character pages.

**Homophone found and handled — new for this word, not previously flagged anywhere**: [[瓦]] "tile" shares this word's exact reading (⺢/'wa/와) — added the `[!warning]` callout to both pages (瓦's own page is otherwise unperfected — no `pos`/`vietnamese`/`swadesh` — flagged, not otherwise fixed, same minimal-touch precedent as every prior homophone cluster this sweep).

**Genuine cross-linguistic asymmetry documented**: Mandarin/Cantonese/Korean/Vietnamese all use 臥 productively, independently or in shared chengyu (臥薪嘗胆/와신상담, "sleep on firewood and taste gall"). Japanese has a real on'yomi (ガ) but never uses 臥 as a standalone word — confirmed via search that it only appears bound in compounds (横臥, おうが; 病臥, びょうが) — with ordinary Japanese using native 横になる for the everyday action instead.

### 2026-07-23, iteration 56 — [[words/立|立]]

Swadesh #125 ("stand"). Stamped `date-last-perfect: 2026-07-23`. Fifth single-character self-standing word this sweep.

**Content removed**: an empty, malformed `## Derived Characters` section (a bare `- ` bullet with no content) — this is a character-page concept, not a word-page one, and was clearly stray cruft copy-pasted from `characters/立 (char).md`'s own (real, populated) Derived Characters section. Removed entirely.

**Frontmatter cleanup**: filled blank `vietnamese` (`lập`, the standard reading among `characters/立 (char).md`'s three attested values — the other two, lụp/sập, look like corpus noise) and blank `pos` (`性詞`, matching the character's own field). `characters: 立 (char)` bare scalar converted to a list. `kwin: true` already correct on both pages — Korean `립` (rip) already correctly preserves the vault's standing North Korean 문화어 form (South Korean would apply 두음법칙 and drop the initial entirely to 입).

**Cross-linguistic note**: documented that Japanese keeps 立 bound in on'yomi compounds (独立, どくりつ) while everyday "to stand" uses the native kun'yomi conjugated verb 立つ (たつ) — the same character, not a separate compound, but functioning grammatically rather than as a bare citation-form word.

No homophones (`注音: ㄌㄧㄆ` unique to this file). No character-page backlink needed — self-standing single-character word.

### 2026-07-23, iteration 57 — [[words/回転|回転]]

Swadesh #126 ("rotate, spin"). Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:`/`aliases:` inline arrays reformatted to block form. Filled blank `cantonese` (`wui4 zyun2`, compositional) and blank `vietnamese` (`hồi chuyển`, real and attested — verified via search, used especially in gyroscope terminology, con quay hồi chuyển). Removed blank `hsk_level:`.

**`pos` corrected `性詞`→`事詞`**, matching both `characters/回.md` and `characters/転.md`'s own `事詞` category — the same fix class as [[呼吸]] and [[戦闘]] earlier this sweep.

**No `stand_in` relationship applies**: 回's own `stand_in` is bare `回` itself, 転's own is `転化` — 回転 is an independent compound, not a legitimizer for either. `kwin: false` already correct per the AND-rule (`characters/回.md` is `true`, `characters/転.md` is `false` → compound `false`).

**All cross-linguistic fields otherwise already correct** — the standard, everyday word for "rotation" across the sphere, no native displacement or homophone collision found.

No homophones (`注音: ㄏㄛㄧㄐ⼔ㄋ` unique to this file). **Incidental fix**: reformatted `characters/転.md`'s bare `[[回転]]` entry to ruby form (`characters/回.md`'s own entry was already properly formatted).

### 2026-07-23, iteration 58 — [[words/落下|落下]]

Swadesh #127 ("fall"). Stamped `date-last-perfect: 2026-07-23`.

**Real `korean` bug caught, a third instance of the standing North Korean rule this sweep (after [[卵子]] and [[分裂]])**: stored `낙하` applies South Korean 두음법칙 (word-initial ㄹ→ㄴ); `characters/落.md`'s own field is `락`, so North Korean 문화어 preserves `락하`. Corrected `낙하`→`락하`.

**`kwin` corrected `false`→`true`**, the fourth confirmed active fix this sweep (after [[父親]], [[羽翼]], [[散歩]]): both `characters/落.md` and `characters/下 (char).md` are individually `true`, and 낙하/락하 ("falling," as in 낙하산/락하산 "parachute") is a real, common word in both Koreas, so the AND-rule prediction is directly validated.

**`pos` corrected `性詞`→`事詞`**, the same fix class as [[呼吸]]/[[戦闘]]/[[回転]] earlier this sweep. `characters:` list quoting fixed for `下 (char)`. Filled `vietnamese` with the real, attested Sino-Vietnamese `lạc hạ` (verified via search — classical usage describing falling leaves/rain/snow); the everyday native verb is simply rơi.

**Stand-in note applied**: `characters/落.md`'s own `stand_in` field is `落下` — added the standard phrasing. (下's own `stand_in` is bare `下` — no note on that side.) No homophones (`注音: ㄌㄚㄎㄏㄚ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/落.md` (`characters/下 (char).md` already had one, correctly formatted).

### 2026-07-23, iteration 59 — [[words/持|持]]

Swadesh #129 ("hold"). Stamped `date-last-perfect: 2026-07-23`. Sixth single-character self-standing word this sweep.

**Content removed**: a stray, meaningless `1310` line sitting directly under `# Notes` — almost certainly a copy-paste artifact (the identical stray `1310` line also sits under `characters/持 (char).md`'s own `# Notes`, suggesting whoever created these two pages pasted the same fragment onto both; flagged there too, but not fixed on the character page, out of scope for a words-only iteration).

**Frontmatter cleanup**: filled blank `vietnamese` (`trì`, verified via search as the real, richly-attested Sino-Vietnamese reading — duy trì "maintain," kiên trì "persevere," chủ trì "preside over" — while `characters/持 (char).md`'s own stored field, "rì, chày, chiì," looks like corpus noise, flagged not fixed) and blank `pos` (`事詞`, matching the character's own field). `characters: 持 (char)` bare scalar converted to a list.

**Cross-linguistic note**: Japanese uses the native kun'yomi verb 持つ (もつ) for everyday "to hold," rather than a bare on'yomi citation form — the character functions grammatically there, not as an independent noun-like word the way it does in Mandarin/Cantonese/Korean.

No homophones (`注音: ㄉㄧ` unique to this file). No character-page backlink needed — self-standing single-character word.

### 2026-07-23, iteration 60 — [[words/擦拭|擦拭]]

Swadesh #133 ("wipe"). Stamped `date-last-perfect: 2026-07-23`.

**Cross-linguistic asymmetry, disclosed rather than force-corrected — the same standard as [[男人]]/[[長牙]] earlier this sweep**: neither Japanese nor Korean appear to actually use 擦拭 as a living compound. The old `japanese`/`korean` fields had substituted entirely native, unrelated verbs (Japanese ふく, 拭く alone "to wipe"; Korean 씻다, "to wash") in place of a reading of this specific compound — corrected both to honest on'yomi/Sino-Korean-compositional values (さっしょく, 찰식) with the real native words disclosed in prose instead of silently overwritten.

**`kwin` deliberately left `false`, not force-corrected**: both `characters/擦 (char).md` and `characters/拭.md` are individually `true`, so the mechanical AND-rule suggests `true` — but per the [[長牙]]/[[指甲]] standard (as opposed to the validated fixes on [[父親]]/[[羽翼]]/[[散歩]]/[[落下]]), this compound's Korean reading isn't independently attested as a real living word, so the AND-rule prediction was noted but not applied without empirical support.

Mandarin cāshì and Cantonese caat3 sik1 are real written/formal-register words for "wipe clean" (擦拭乾淨). Filled `vietnamese` with the real, attested `sát thức` (verified via search); the everyday native phrase is lau chùi. **Stand-in note applied**: `characters/拭.md`'s own `stand_in` field is `擦拭` — added the standard phrasing. (擦's own `stand_in` is bare `擦` — no note on that side.)

No homophones (`注音: ㄑㄚㄊㄙㄧㄎ` unique to this file). **Incidental fixes**: reformatted `characters/擦 (char).md`'s bare `[[擦拭]]` entry to ruby form; added a missing `## Words` entry to `characters/拭.md`.

### 2026-07-23, iteration 61 — [[words/縫製|縫製]]

Swadesh #138 ("sew, tailor"). Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: filled blank `cantonese` (`fung4 zai3`, compositional) and blank `vietnamese` (`phùng chế`, honest compositional — the related compound phùng công, 縫工 "seamstress/tailor," is independently attested, but phùng chế itself wasn't separately confirmed; noted that everyday/industry Vietnamese uses native may/may mặc instead).

**No `stand_in` relationship applies to 製's side**: `characters/縫.md`'s own `stand_in` field is `縫製` — added the standard phrasing. (製's own `stand_in` is `製作`, a different word — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/縫.md` is `true`, `characters/製.md` is `false` → compound `false`).

**All other cross-linguistic fields already correct** — Japanese ほうせい and Korean 봉제 are both real, standard trade/industry terms (縫製工場/봉제공장, "sewing factory"), Mandarin féngzhì likewise real and technical/industrial next to the everyday bare verb.

No homophones (`注音: ㄅㄛㄫㄐㄝ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/縫.md` and `characters/製.md` (neither previously listed this compound).

### 2026-07-23, iteration 62 — [[words/計数|計数]]

Swadesh #139 ("count"). Stamped `date-last-perfect: 2026-07-23`.

**Genuine cross-linguistic homophone finding, verified and corrected mid-draft**: Japanese けいすう (keisū) genuinely means "counting, calculation" — matching this word directly — but is a real homophone of the unrelated compound 係数 (also けいすう), "a mathematical coefficient" (係, "relate/connect," not 計, "measure/plan"). Korean 계수 (gyesu) carries the collision further: confirmed via Wiktionary that 계수 is a genuine multi-way homophone spanning 計數/係數 ("calculation"/"coefficient," the Korean word etymologically tied to the Japanese 係数 borrowing) plus entirely unrelated hanja for "cinnamon" and "sister-in-law" — a cluster reminiscent of [[思考]]'s five-way 사고 collision earlier this sweep. (Caught and corrected an initial drafting error before finalizing — first pass conflated 計数 and 係数 as the same compound rather than two distinct, homophonous ones.)

**Frontmatter cleanup**: filled blank `cantonese` (`gai3 sou2`, compositional) and blank `vietnamese` (`kế số`, honest compositional — verified via search as plausible though not independently confirmed as a standalone term; everyday native verb is đếm).

**Stand-in note applied**: `characters/数.md`'s own `stand_in` field is `計数` — added the standard phrasing. (計's own `stand_in` is `計画`, a different word — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/計.md` is `false`, `characters/数.md` is `true` → compound `false`).

No Dan'a'yo-internal homophones (`注音: ㄍㄝㄧㄙㄨ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/計.md` and `characters/数.md` (the latter's own `# Notes` already referenced 計数 informally — "requires [[計数]]" — but had no proper `## Words` ruby entry).

### 2026-07-23, iteration 63 — [[words/唱歌|唱歌]]

Swadesh #141 ("sing"). Stamped `date-last-perfect: 2026-07-23`.

**Genuine semantic-narrowing finding, verified in depth**: confirmed via search that 唱歌/しょうか (shōka) and 창가 (changga) are not generic words for "singing" in Japanese/Korean — both name a specific historical genre of Meiji-era Japanese school songs and the closely related Korean colonial-period genre it directly inspired (both terms literally mean "school song"; everyday "to sing" uses native 歌う/노래하다 instead). Documented this institutional/historical narrowing explicitly rather than treating the fields as claims of general everyday usage.

**Vietnamese filled with a culturally rich finding**: xướng ca is a real, well-attested Sino-Vietnamese compound (verified via search) with a striking historical association — the old feudal phrase xướng ca vô loài ("performers rank with no social class") reflected a traditional Confucian view looking down on professional singers, now considered outdated.

**Stand-in note applied**: `characters/唱.md`'s own `stand_in` field is `唱歌` — added the standard phrasing. (歌's own `stand_in` is `歌曲`, a different word — no note on that side.) Non-canonical `## Etymology` heading renamed to `## Notes`. `kwin: false` already correct per the AND-rule (both constituents individually `false`).

No homophones (`注音: ㄑ⺢ㄫㄍㄜ` unique to this file). **Incidental fixes**: reformatted `characters/唱.md`'s bare `[[唱歌]]` entry to ruby form; added a missing `## Words` entry to `characters/歌.md`.
