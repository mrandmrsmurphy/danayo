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

### 2026-07-23, iteration 64 — [[words/遊戯|遊戯]]

Swadesh #142 ("play, game"). Stamped `date-last-perfect: 2026-07-23`. A clean iteration — all cross-linguistic fields were already correct and genuinely attested.

**Frontmatter cleanup**: `characters:`/`aliases:` inline arrays reformatted to block form (kept all three variants — 游戏, 游戲, 遊戲 — matching `characters/戯.md`'s own documented traditional/simplified forms). Filled a previously-missing `kwin` field entirely — computed `false` per the AND-rule (both `characters/遊.md` and `characters/戯.md` are individually `false`).

**Stand-in note applied**: `characters/遊.md`'s own `stand_in` field is `遊戯` — added the standard phrasing. (戯's own `stand_in` is `戯曲`, a different word — no note on that side.)

**Register note**: Mandarin/Cantonese/Japanese/Korean/Vietnamese all use this compound as a real, standard word for "play, game, amusement," though each carries a slightly more formal/structured flavor than the plainest everyday "to play" verb in its own language (Mandarin 玩; Japanese native 遊ぶ).

No homophones (`注音: ⼜ㄛㄏㄨㄧ` unique to this file). **Flagged, not fixed**: `characters/遊.md`'s own `# Notes` has a stray corpus artifact, `遊=C#973`, left untouched (character-sweep territory). **Incidental fixes**: added missing `## Words` entries to both `characters/遊.md` and `characters/戯.md`.

### 2026-07-23, iteration 65 — [[words/凍結|凍結]]

Swadesh #145 ("freeze"). Stamped `date-last-perfect: 2026-07-23`.

**Real bug caught**: `characters:` listed bare `結`, but the actual file is `結 (char).md` — the classic missing-`(char)`-suffix bug flagged repeatedly in [[Loop Work.md]] — corrected to `"結 (char)"`, and fixed the matching Notes link path (`結.md`→`結%20(char).md`).

**`pos: 性詞` verified correct, not a bug**: matches `characters/凍.md`'s own stored category exactly — unlike the `事詞` corrections applied to [[呼吸]]/[[戦闘]]/[[回転]]/[[落下]] earlier this sweep (where the constituent characters were clearly verb-tagged), here the primary constituent is itself `性詞`, so left unchanged.

**Genuine shared-metaphor finding**: filled `vietnamese` with `đông kết` (verified via search); confirmed all five languages extend the literal "freeze" sense to the same figurative one — freezing financial assets/an account (資産凍結/자산동결/đóng băng tài khoản) — an independently-arrived-at shared metaphor across the whole sphere, not just a calque of one language into the others.

**Stand-in note applied**: `characters/凍.md`'s own `stand_in` field is `凍結` — added the standard phrasing. (結's own `stand_in` is bare `結` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/凍.md` is `true`, `characters/結 (char).md` is `false` → compound `false`). `characters:` list reformatted to block form.

No homophones (`注音: ㄉㄛㄫㄍㄝㄊ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/凍.md` (had none at all) and `characters/結 (char).md`.

### 2026-07-23, iteration 66 — [[words/膨脹|膨脹]]

Swadesh #146 ("swell, expand"). Stamped `date-last-perfect: 2026-07-23`.

**Genuine semantic-drift finding, verified via search**: filled `vietnamese` with `bành trướng`, a real and extremely common Sino-Vietnamese compound — but confirmed it carries a much stronger, specifically political connotation than the neutral Mandarin/Japanese/Korean sense: bành trướng denotes aggressive territorial/political expansionism (chủ nghĩa bành trướng, "expansionism" as ideology), not neutral physical swelling, for which Vietnamese instead uses phồng/nở/giãn nở. Documented the contrast explicitly.

**No `stand_in` relationship applies**: 膨's own `stand_in` is `膨大`, 脹's own is `腫脹` — 膨脹 is an independent compound, not a legitimizer for either. `kwin: false` already correct per the AND-rule (`characters/膨.md` is `false`, `characters/脹.md` is `true` → compound `false`). `characters:` inline array reformatted to block form; removed empty `aliases: []`; non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄆㄚㄫㄑㄚㄫ` unique to this file). **Incidental fixes**: reformatted `characters/膨.md`'s bare `[[膨脹]]` entry to ruby form; added a missing `## Words` entry to `characters/脹.md`.

### 2026-07-23, iteration 67 — [[words/太陽|太陽]]

Swadesh #147 ("sun"). Stamped `date-last-perfect: 2026-07-23`. Already close to complete — both `characters/太 (char).md` and `characters/陽 (char).md` already had correctly-formatted ruby backlinks, no incidental character-page fixes needed.

**Frontmatter cleanup**: filled blank `pos` (`名詞`); removed empty `aliases: []`. `kwin: true` already correct per the AND-rule (both constituents individually `true`). No `stand_in` relationship applies — both 太's and 陽's own `stand_in` fields are bare self-reference — 太陽 is an independent compound.

**Homophone reformatted, not newly found**: the page already informally flagged (plain-text `Homophones:` line, no callout) that this word is an exact homophone of [[太様]] "greatly, exceedingly" (identical tai'yang/태양/ㄊㄚㄧ·⼘ㄫ) — converted both pages to the standard `[!warning] Homophones` callout. `太様.md` itself remains otherwise unperfected (blank `pos`/`korean`/`vietnamese`/`swadesh`) — flagged, not fixed, same minimal-touch precedent as every prior homophone cluster this sweep.

**Genuine coincidental-match finding, verified via search**: Vietnamese thái dương additionally names the temple (side of the head) in the compound huyệt thái dương (太陽穴, "temple acupoint" in traditional medicine) — matching the same characters' use for "temple" in Chinese/Japanese (太陽穴), confirmed as a real, attested anatomical term rather than assumed.

All cross-linguistic fields for the primary "sun" sense were already correct and standard across the sphere.

### 2026-07-23, iteration 68 — [[words/海洋|海洋]]

Swadesh #154 ("sea, ocean"). Stamped `date-last-perfect: 2026-07-23`.

**Real bugs caught in two comma-dumped fields**: `korean: "해양, 바다"` mixed this compound's own Sino-Korean reading with the everyday native word for "sea" (바다, matching `characters/海.md`'s own `korean_native` value) — narrowed to `해양`. `vietnamese: "biển, hải , pei"` was a garbled mix of the native word (biển) and a stray, apparently meaningless fragment ("pei") alongside a malformed partial Sino-Vietnamese reading — replaced entirely with `hải dương`, the real, well-attested Sino-Vietnamese compound (also, notably, the name of a real Vietnamese coastal province).

**Filled a previously-missing `kwin` field entirely**: computed `true` per the AND-rule (both `characters/海.md` and `characters/洋.md` are individually `true`).

**Stand-in note applied**: `characters/海.md`'s own `stand_in` field is `海洋` — added the standard phrasing, plus the existing informal note about being narrower in scope than [[大洋]] ("ocean," 洋's own `stand_in`), folded into the same bullet. Removed the stray `[[Swadesh]] #154` self-reference line (redundant with the frontmatter `swadesh` field itself).

No homophones (`注音: ㄏㄚㄧ·⼘ㄫ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/海.md` and `characters/洋.md` (neither previously listed this compound, despite `海.md`'s own Notes already informally referencing [[大洋]]).

### 2026-07-23, iteration 69 — [[words/石頭|石頭]]

Swadesh #156 ("stone"). Stamped `date-last-perfect: 2026-07-23`. The most substantial content bug found this sweep since [[人等]]/[[我等]] and [[草花]].

**Real content bug corrected**: the stored `english` gloss was "stubborn person," which mismatched the actual Swadesh sense (#156, "stone") entirely. Mandarin shítou and Cantonese sek6 tau4 are simply the ordinary everyday word for a literal "stone, rock" — corrected the gloss accordingly, and fixed the identical wrong gloss on `characters/石 (char).md`'s own pre-existing backlink to this word.

**A genuine, striking semantic divergence, verified rather than "fixed" into false symmetry**: Japanese いしあたま and Korean 석두 — built from the exact same two characters — do not mean "stone" in those languages at all; both are real, idiomatic words for a stubborn/thick-headed person (confirmed via search: 석두 glossed directly as a contemptuous term for an obstinate or extremely stupid person, a parallel formation to the fully native Korean synonym 돌대가리, "stone-head"). Japanese's and Korean's own literal words for "stone" are 石 (いし) and 돌 instead. Kept both fields at their real, attested values rather than forcing them toward the Chinese/Vietnamese literal sense.

`kwin: false` already correct per the AND-rule (`characters/石 (char).md` is `true`, `characters/頭 (char).md` is `false` → compound `false`). No `stand_in` relationship applies — both constituents are their own bare self-standing `stand_in`. `characters:`/`aliases:` inline arrays reformatted to block form.

No homophones (`注音: ㄙㄝㄎㄊㄛㄨ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/頭 (char).md` (`characters/石 (char).md`'s own entry already existed, just needed the gloss corrected).

### 2026-07-23, iteration 70 — [[words/灰塵|灰塵]]

Swadesh #158 ("dust"). Stamped `date-last-perfect: 2026-07-23`.

**Korean 회진 confirmed as a genuine three-way homophone, verified via search**: alongside this compound's own sense ("ash and dust," also figuratively "utter destruction/annihilation"), the identical spelling covers 回診 ("a doctor's rounds") and 回進 ("to turn and advance") — three unrelated words sharing one pronunciation. `kwin: true` was already correct per the AND-rule (both `characters/灰 (char).md` and `characters/塵.md` are individually `true`), now doubly confirmed since 회진/灰塵 is independently real and attested.

**Left `vietnamese` deliberately unfilled rather than guess**: no attested compound for 灰塵 was found, and both constituent characters' own stored Vietnamese fields are themselves noisy, uncombinable lists — the everyday Vietnamese word for dust is simply native bụi, documented in prose instead of fabricating a Sino-Vietnamese compound.

**Stand-in note applied**: `characters/塵.md`'s own `stand_in` field is `灰塵` — added the standard phrasing. (灰's own `stand_in` is bare `灰` — no note on that side.) `characters:` list reformatted to block form; removed blank `hsk_level:` and empty `aliases:`.

No Dan'a'yo-internal homophones (`注音: ㄏㄛㄧㄐㄧㄋ` unique to this file). **Incidental fixes**: added a missing `## Words` entry to `characters/灰 (char).md` (had a different `灰` self-entry but not this compound); reformatted `characters/塵.md`'s existing bare `[[灰塵]]` entry to include the stand-in note.

### 2026-07-23, iteration 71 — [[words/氷水|氷水]]

Swadesh #165 ("ice water"). Stamped `date-last-perfect: 2026-07-23`.

**A pleasing independently-verified parallel finding**: both Japanese and Korean have extended this literal "ice water" compound to name a specific summer dessert — shaved ice with syrup. Confirmed via search that Japanese 氷水 (with attested readings こおりみず/こおりすい/ひみず, and a documented history as far back as Sei Shōnagon's Pillow Book, c. 1000 CE) functions as a synonym of かき氷, while Korean 빙수 (bingsu) has undergone the identical drift into the now internationally-recognized dessert name (patbingsu) — two languages arriving independently at the same figurative extension. Mandarin bīngshuǐ and Cantonese bing1 seoi2 keep the plain literal "ice water" sense.

**Frontmatter cleanup**: filled blank `japanese` (`こおりみず`, the primary literal reading) and blank `vietnamese` (`băng thủy`, a real but classical/Buddhist-register Sino-Vietnamese compound, verified via search — everyday Vietnamese uses native nước đá). `characters:`/`aliases:` inline arrays reformatted to block form.

**Stand-in note applied**: `characters/氷.md`'s own `stand_in` field is `氷水` — added the standard phrasing. (水's own `stand_in` is bare `水` — no note on that side.) `kwin: true` already correct per the AND-rule (both constituents individually `true`).

No homophones (`注音: ㄅㄧㄫㄙㄨ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/氷.md` (`characters/水.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 72 — [[words/燃焼|燃焼]]

Swadesh #169 ("burn, combust"). Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected, propagated across two files**: `english: burst` should be `burn` — 燃焼 means "combustion," not "burst." The identical typo had also been copy-pasted onto `characters/燃.md`'s own Notes bullet describing this same word; fixed both.

**`pos` corrected `性詞`→`事詞`**, matching `characters/焼.md`'s own stored category — the same fix class as [[呼吸]]/[[戦闘]]/[[回転]]/[[落下]] earlier this sweep.

**Unusual double stand-in**: both `characters/燃.md` and `characters/焼.md` have their own `stand_in` field set to `燃焼` — both constituents are bounded characters relying on this same compound to become viable Dan'a'yo words, so the opening bullet notes both rather than just one (the more typical pattern this sweep).

Filled blank `vietnamese` with the real, attested Sino-Vietnamese `nhiên thiêu` (verified via search), which carries the identical literal/figurative double sense found across the sphere — burning fat, burning with emotion. `aliases`: split a single malformed entry (`燃烧 燃燒`, space-joined) into two proper list items. `kwin: false` already correct per the AND-rule (both constituents individually `false`). Non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄋ⼶ㄋㄙ⼄ㄨ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/焼.md` (had none at all).

### 2026-07-23, iteration 73 — [[words/緑|緑]]

Swadesh #173 ("green"). Stamped `date-last-perfect: 2026-07-23`. Seventh single-character self-standing word this sweep.

**Content removed**: a bare, redundant `2. abbreviation for beryllium` note — unlike the earlier element-abbreviation cases this sweep (multi/西/里), this fact was already correctly and more fully documented on `characters/緑 (char).md`'s own Notes (linking `[[緑柱素]]` with ruby), so the word page's unlinked duplicate was cut rather than kept, per the standing rule's intent that the character page is the canonical home for this fact.

**Frontmatter cleanup**: `vietnamese: - lục` (one-item list) converted to a plain string; `characters: 緑 (char)` bare scalar converted to a list.

**Register note**: Mandarin/Cantonese/Korean/Vietnamese all use this character productively and independently for "green," but Japanese almost always uses native みどり for the color itself, reserving on'yomi りょく/ろく for compounds (緑化, りょっか, "afforestation"). Korean 록 already correctly preserves the vault's standing North Korean 문화어 form (South Korean 두음법칙 would give 녹).

**Homophone found and handled — new for this word**: [[鹿]] "deer" shares this word's exact reading (log/록/ㄌㄛㄎ) — added the `[!warning]` callout to both pages. `鹿.md`'s own page is otherwise unperfected — a stray `vietnamese: null` literal, and its own `korean: 녹` looks like the identical North/South Korean bug just fixed on [[卵子]]/[[分裂]]/[[落下]] (real North Korean form should likely be 록, matching its own `諺文: 록`) — flagged, not fixed, out of scope for a different word's iteration.

**Pool refreshed**: re-ran the never-perfected Swadesh query — only 9 entries remain in the entire pool. Next: #187 (腐敗), #190 (圓形), #191 (鋭利), #193 (滑), #195 (乾燥), #197 (近), #199 (右側), #200 (左側), #206 (因由).

### 2026-07-23, iteration 74 — [[words/腐敗|腐敗]]

Swadesh #187 ("rot, decay"). Stamped `date-last-perfect: 2026-07-23`.

**`pos` corrected `名詞`→`事詞`**, matching the verb-like reading of "to rot, to decay/spoil" — the same fix class as [[呼吸]]/[[戦闘]]/[[回転]]/[[落下]]/[[燃焼]] earlier this sweep.

**Genuine register-narrowing finding**: filled `vietnamese` with the real, attested `hủ bại` (verified via search), but noted it has drifted more heavily toward the figurative, formal/literary sense (moral or institutional corruption, phong tục hủ bại "corrupt customs") — reserved for journalism/literature rather than everyday speech about spoiled food, whereas Mandarin/Cantonese/Japanese/Korean all cover both the literal and figurative senses evenly in ordinary register.

**Stand-in note applied**: `characters/腐.md`'s own `stand_in` field is `腐敗` — added the standard phrasing. (敗's own `stand_in` is `失敗`, a different word — no note on that side.) `characters:` inline array reformatted to block form; removed empty `aliases: []`. `kwin: false` already correct per the AND-rule (both constituents individually `false`).

No homophones (`注音: ㄆㄨㄅㄚㄧ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/腐.md` and `characters/敗.md`.

### 2026-07-23, iteration 75 — [[words/圓形|圓形]]

Swadesh #190 ("round shape, circle"). Stamped `date-last-perfect: 2026-07-23`.

**Real content bug corrected, propagated across two files**: `english` included "wound," which has no plausible connection to 圓形 ("circular shape") — removed, corrected to "round shape." The identical wrong gloss also sat on `characters/圓 (char).md`'s own pre-existing (bare, unformatted) backlink to this word; fixed and reformatted to ruby there too.

**Frontmatter cleanup**: filled blank `pos` (`名詞`, matching both constituent characters' own category) and blank `vietnamese` (`viên hình`, real and attested — verified via search, though more formal/technical register than the everyday native hình tròn).

**No `stand_in` relationship applies**: both 圓's and 形's own `stand_in` fields are bare self-reference — 圓形 is an independent compound, not a legitimizer for either. `kwin: false` already correct per the AND-rule (`characters/圓 (char).md` is `true`, `characters/形 (char).md` is `false` → compound `false`). Non-canonical `## Etymology` renamed to `## Notes`. Kept the existing `円形` alias — the Japanese shinjitai form, matching 圓's own aliasing convention.

No homophones (`注音: ⼔ㄋㄏㄝㄫ` unique to this file). `characters/形 (char).md`'s own backlink was already correctly formatted — no fix needed there.

### 2026-07-23, iteration 76 — [[words/鋭利|鋭利]]

Swadesh #191 ("sharp"). Stamped `date-last-perfect: 2026-07-23`.

**Filled `vietnamese` with `nhuệ lợi`** (verified via search as a real, attested Sino-Vietnamese compound), and noted in the opening bullet that 利 here carries its older "sharp, keen" sense (as in 利器, "a sharp weapon"; 鋒利, "sharp-edged") rather than the more familiar modern "profit" sense the character's own frontmatter gloss shows — a genuine polysemy worth flagging rather than silently glossing over.

**Stand-in note applied**: `characters/鋭.md`'s own `stand_in` field is `鋭利` — added the standard phrasing. (利's own `stand_in` is `利潤`, a different word — no note on that side.) `kwin: false` already correct per the AND-rule (both constituents individually `false`).

**Flagged, not fixed**: `characters/利.md`'s own `## Words` section carries a duplicate entry for its "abbreviation for livermorium" periodic-table note (once as a bare ruby line, once again explicitly labeled "abbreviation for...") — a real duplication bug, but on a different character's page, out of scope for this words-only iteration.

No homophones (`注音: ⼶ㄌㄧㄜ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/鋭.md` and `characters/利.md`.

### 2026-07-23, iteration 77 — [[words/滑|滑]]

Swadesh #193 ("slippery, smooth"). Stamped `date-last-perfect: 2026-07-23`. Eighth single-character self-standing word this sweep.

**Real bug corrected**: `korean: 골` was a genuinely different reading of 滑 belonging to its other, unrelated sense — "chaotic, cunning" (滑稽, 골계, "comical") — rather than this word's "slippery" sense. Corrected to `활` (hwal), matching `characters/滑 (char).md`'s own stored value exactly. Also aligned `注音` (ㄏㄨㄚㄊ→ㄏ⺢ㄊ, a stale spelled-out Bopomofo form vs. the character's own compressed-diphthong convention) and `vietnamese` (gột→hoạt, the latter matching the character's own field and real compounds like linh hoạt "flexible") to the character's authoritative values, since word and character are identical here. `kwin` corrected `false`→`true` to match (both fields are now confirmed identical to the real, current word 활, so the AND-rule-style correspondence is directly validated). Filled blank `pos` (`性詞`, matching the character).

**Cross-linguistic note**: Japanese uses the native kun'yomi verb 滑る (すべる) for the everyday adjective/verb rather than a bare on'yomi citation form.

No homophones (`注音: ㄏ⺢ㄊ` unique to this file). No character-page backlink needed — self-standing single-character word.

### 2026-07-23, iteration 78 — [[words/乾燥|乾燥]]

Swadesh #195 ("dry, arid"). Stamped `date-last-perfect: 2026-07-23`. Already substantially complete — someone had already written a good etymological opening bullet explaining the 乾/干 simplification distinction.

**Frontmatter cleanup**: quoted `"乾 (char)"` in the `characters` list; `aliases: [干燥]` inline array reformatted to block form. Filled blank `vietnamese` with `can táo` — verified via search that two Sino-Vietnamese readings exist (can táo, using 乾's modern "gān"-parallel reading; kiền táo, tied to the older classical "qián"/Trigram reading) — kept `can táo` as the field value since it matches the everyday adjective sense, noting the alternate in prose.

**Stand-in note applied**: `characters/燥.md`'s own `stand_in` field is `乾燥` — folded the standard phrasing into the existing etymological bullet rather than duplicating it. (乾's own `stand_in` is bare `乾` — no note on that side.) `kwin: false` already correct per the AND-rule (both constituents individually `false`). Non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄍ⼶ㄋㄙㄚㄨ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/燥.md` (had none at all; `characters/乾 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 79 — [[words/近|近]]

Swadesh #197 ("near"). Stamped `date-last-perfect: 2026-07-23`. Ninth single-character self-standing word this sweep.

**Investigated, not a bug**: the word's `korean: 근` vs. `諺文: 긴` mismatch looked at first glance like an error, but `characters/近 (char).md` stores the identical values — this is the genuine, deliberate `kwin: false` divergence (Dan'a'yo 긴 vs. Korean 근, tracing to the same source but diverging in vowel), not a typo.

**Frontmatter cleanup**: filled blank `vietnamese` (`cận`, the standard Sino-Vietnamese reading — cận thị "nearsighted," phụ cận "vicinity" — chosen over the character's other listed, noisier variants) and blank `pos` (`性詞`, matching the character). `characters: 近 (char)` bare scalar converted to a list.

**Cross-linguistic note**: Japanese uses the native kun'yomi adjective 近い (ちかい) for everyday "near," reserving on'yomi きん for compounds (近代, きんだい). Vietnamese shows the same native-vs-Sino split as Korean — everyday gần vs. Sino-Vietnamese cận.

No homophones (`注音: ㄍㄧㄋ` unique to this file). No character-page backlink needed — self-standing single-character word.

### 2026-07-23, iteration 80 — [[words/右側|右側]]

Swadesh #199 ("right side"). Stamped `date-last-perfect: 2026-07-23`.

**Real bugs corrected, two separate wrong-value substitutions**: `japanese: みぎりがわ` was an apparent typo — corrected to the real reading `みぎがわ` (migigawa; also attested as on'yomi うそく in formal register), confirmed via search. `korean: 오른쪽` was the fully native Korean word for "right side," not a reading of 右側 at all — corrected to `우측` (ujeuk), the real Sino-Korean reading; both terms are genuinely interchangeable in everyday Korean, per search. Also fixed a missing space in `cantonese` (jau6zak1→jau6 zak1).

**Filled `vietnamese`** with `hữu trắc`, a real attested Sino-Vietnamese compound (verified via search); noted that bare `hữu` alone is also commonly sufficient in Vietnamese (hữu ngạn, "the right bank of a river").

**Stand-in note applied**: `characters/右.md`'s own `stand_in` field is `右側` — added the standard phrasing. (側's own `stand_in` is `側面`, a different word — no note on that side.) `kwin: false` already correct per the AND-rule (both constituents individually `false`). `characters:`/`aliases:` inline arrays reformatted to block form.

No homophones (`注音: ⼜ㄐㄧㄎ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/側.md` (`characters/右.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 81 — [[words/左側|左側]]

Swadesh #200 ("left side"). Stamped `date-last-perfect: 2026-07-23`. A direct companion to [[右側]] last iteration — same bug class, corrected the same way.

**Real bug corrected**: `korean: 우측, 왼쪽` — `우측` is the reading for the unrelated word [[右側]] ("right side"), almost certainly copy-pasted by mistake, and `왼쪽` is the fully native Korean word for "left side," not a Sino-Korean reading of 左側 at all. Corrected to `좌측` (jwacheuk), directly paralleling 右側's own 우측 fix last iteration.

**Frontmatter cleanup**: filled a previously-missing `kwin` field entirely — computed `false` per the AND-rule (both `characters/左.md` and `characters/側.md` are individually `false`). Filled `vietnamese` with the honest compositional `tả trắc` (左=tả, as in tả hữu "left and right"; 側=trắc, as in 側's own real reading trắc diện "side face") — everyday Vietnamese uses native trái instead. `characters:` inline list reformatted to block form.

**Stand-in note applied**: `characters/左.md`'s own `stand_in` field is `左側` — added the standard phrasing. `japanese: ひだりがわ` was already correct, mirroring 右側's みぎがわ exactly.

No homophones (`注音: ㄐㄚㄐㄧㄎ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/側.md` (`characters/左.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 82 — [[words/因由|因由]]

Swadesh #206 ("reason, cause"). Stamped `date-last-perfect: 2026-07-23`. Last entry in the current Swadesh pool.

**Real content bug corrected, propagated to a character-page backlink too**: `english` was `since, therefore, because` — describing 因由 as a conjunction — but it's actually a noun meaning "the reason, the cause" (verified via search: a synonym of 原因/理由/緣故, occasionally with a Buddhist "predestined connection" sense), matching `characters/因.md`'s own gloss directly. Corrected the gloss and filled blank `pos` to `名詞`; fixed the identical wrong gloss on `characters/因.md`'s own pre-existing backlink to this word.

**Real bug corrected**: `korean` was `때문에`, the fully native Korean phrase for "because of," not a reading of 因由 at all — corrected to `인유` (inyu), matching the word's own already-stored `諺文`/`羅馬字` fields exactly (an internal-consistency check that would have caught this immediately).

**Content removed**: a stray scratch note, `cp C: 因為 , 由於 , 由于`, sitting as raw text before the meta-bind-embed — looked like leftover research shorthand rather than real content. Folded the substance into a proper Notes paragraph about the wider East Asian synonym cluster (因為, 由於/由于, 原因, 理由) instead of just discarding it outright.

**No `stand_in` relationship applies**: 因's own is `原因`, 由's own is bare `由` — 因由 is an independent compound, part of a synonym family rather than a legitimizer for either. `kwin: false` already correct per the AND-rule (`characters/因.md` is `true`, `characters/由 (char).md` is `false` → compound `false`). Filled `vietnamese` with the real, attested `nhân do` (verified via search).

No homophones (`注音: ㄧㄋ⼜ㄛ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/由 (char).md` (had none at all).

**Pool exhausted, new convention adopted**: this was the last entry (#206) in the current never-perfected Swadesh pool. The never-perfected pool overall is still huge (4,111 word files), so reverted to this log's original ordering convention from iterations 1–20 — HSK level ascending, alphabetical within level — since a large HSK-1 sub-pool (243 files) remains despite the "milestone" claimed at iteration 20 (that pool must have been narrower, e.g. a stricter grep pattern that missed inline-array `characters:` fields or differently-quoted `hsk_level` values). Next: alphabetically ascending through the HSK-1 never-perfected pool, starting with 一点, 一般, 不但, 主要, 人民, 今年, 以後, 会話, 体育, 作業, 使用, 便宜, 先生, 全体, 全部, 公共, 公園, 内容, 出現, 出発, ...

### 2026-07-23, iteration 83 — [[words/一点|一点]]

First word in the new HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real content bug corrected**: `english` was `dot, speck, spot` — the literal, compositional reading — but as an HSK-1 word, 一点/一點's overwhelmingly primary sense (verified via search) is the everyday quantifier "a little, a bit" (一点儿水, "a little water"; 便宜一点儿, "a little cheaper"). The literal "a point" sense exists (这一点, "this point [of an argument]") but is secondary/formal. Corrected the gloss to the primary quantifier sense.

**Genuine cross-linguistic asymmetry documented**: Japanese いってん and Korean 일점 exist as literal compositional readings ("one point"), but neither functions as the everyday "a little" quantifier — Japanese uses native 少し and Korean uses native 조금 instead, reserving いってん/일점 for the literal "point/dot" sense. Vietnamese nhất điểm is attested with the same "a little bit" calque sense (verified via search), though everyday Vietnamese strongly prefers native một chút/một ít.

**Formatting bug caught on a character-page backlink**: `characters/一 (char).md`'s pre-existing entry for this word used a bare `*` bullet with the *wrong gloss* and, more substantively, put the word's `諺文` (읻덤) inside the `<rt>` ruby tag instead of its `注音` (ㄧㄊㄉㄝㄇ) — every other ruby entry in this vault's convention uses 注音 in `<rt>`. Fixed both.

No `stand_in` relationship applies — both 一's and 点's own `stand_in` fields are bare self-reference. `characters:` quoting fixed for `一 (char)`; `hsk_level: 1` (bare integer) quoted to `"1"`; blank `swadesh:` removed. No homophones (`注音: ㄧㄊㄉㄝㄇ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/点 (char).md`.

### 2026-07-23, iteration 84 — [[words/一般|一般]]

Second word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `mandarin: jībān` — 一 is never read jī; corrected to `yìbān`, the standard reading.

**Homophone reformatted, not newly found**: the page already informally flagged (a plain `Homophones:` note) that this word is an exact Dan'a'yo homophone of [[一半]] "half" (읻반/'idban/ㄧㄊㄅㄚㄋ identical on both) — despite Mandarin/Cantonese actually distinguishing them by tone (yìbān vs yībàn; bun1 vs bun3), a genuine case of two source-language near-homophones collapsing into one Dan'a'yo form. Converted both pages to the standard `[!warning] Homophones` callout.

**Same ruby-tag formatting bug as [[一点]] last iteration, on the same character page**: `characters/一 (char).md`'s pre-existing entry for this word again put `諺文` (읻반) inside the `<rt>` tag instead of `注音` (ㄧㄊㄅㄚㄋ) — fixed, along with the wrong gloss it carried.

Filled `vietnamese` with the real, attested Sino-Vietnamese `nhất ban` (verified via search). No `stand_in` relationship applies — both constituents are bare self-standing characters. `kwin: true` already correct per the AND-rule (both individually `true`). Removed blank `swadesh:` and empty `aliases: []`; quoted `hsk_level: "1"`.

**Incidental fix**: added a missing `## Words` section to `characters/般 (char).md` (had none at all).

### 2026-07-23, iteration 85 — [[words/不但|不但]]

Third word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**A genuinely Mandarin-specific grammatical particle, left honestly incomplete rather than fabricated**: 不但……而且…… ("not only… but also…") is a common Mandarin correlative conjunction, but searches found no evidence Japanese or Korean use this compound at all — both express the same logical relation with entirely unrelated constructions (Japanese 〜だけでなく; Korean -뿐만 아니라). Left `japanese`/`korean`/`vietnamese` blank rather than inventing an unattested compositional reading — even a "compositional-only, disclosed" value (the pattern used for [[長牙]]/[[擦拭]] etc.) would overstate the case for a pure grammatical particle with no cross-linguistic parallel at all.

**Homophone found and handled — new for this word**: [[不丹]] "Bhutan" shares this word's exact reading (boddan/볻단/ㄅㄛㄊㄉㄚㄋ) — added the `[!warning]` callout to both pages (不丹's own page was already fully perfected and stamped 2026-05-23; only added the missing callout, left the rest and its existing stamp untouched).

No `stand_in` relationship applies — both 不's and 但's own `stand_in` fields are bare self-reference. Filled a previously-missing `kwin` field entirely — computed `false` per the AND-rule (`characters/不 (char).md` is `false`, `characters/但.md` is `true` → compound `false`). Fixed a missing space in `cantonese` (bat1daan6→bat1 daan6); quoted `hsk_level: "1"`.

**Incidental fixes**: reformatted `characters/不 (char).md`'s bare, plain-markdown-linked entry for this word to a proper ruby wikilink; added a missing `## Words` entry to `characters/但 (char).md`.

### 2026-07-23, iteration 86 — [[words/主要|主要]]

Fourth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`. A clean iteration.

**Small fix**: `vietnamese: Chủ yếu` was capitalized as if a proper noun — lowercased to `chủ yếu`.

**No `stand_in` relationship applies**: 主's own is `主人`, 要's own is `重要` — 主要 is an independent compound, not a legitimizer for either. `kwin: false` already correct per the AND-rule (`characters/主.md` is `true`, `characters/要.md` is `false` → compound `false`).

**All cross-linguistic fields already correct** — genuinely the everyday, standard word for "main, principal" across the sphere, no native displacement or homophone collision found. Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`.

No homophones (`注音: ㄐㄨ·⼄ㄨ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/要.md` (`characters/主.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 87 — [[words/人民|人民]]

Fifth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Genuine political-connotation finding, richly documented**: Korean 인민, unlike the neutral rénmín/jan4 man4/じんみん/nhân dân across the other four languages, carries a real, heavily-documented political charge — verified via search that South Korea's own constitutional drafters replaced 인민 with 국민 in the 1940s specifically to avoid its communist/North Korean association, while North Korea's own official name for itself, 조선민주주의인민공화국 (DPRK), uses 인민 as its ideologically loaded term for "the people" (the revolutionary masses, explicitly excluding capitalists/landlords). Kept 인민 as the field value — it's the honest hanja-matching reading — but documented the connotation explicitly rather than presenting it as neutral like its four counterparts.

**Small fix**: `vietnamese: Nhân dân` was capitalized as if a proper noun — lowercased to `nhân dân`.

**Stand-in note applied**: `characters/民.md`'s own `stand_in` field is `人民` — added the standard phrasing. (人's own `stand_in` is bare `人` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/人 (char).md` is `false`, `characters/民.md` is `true` → compound `false`). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`.

No homophones (`注音: ㄋㄧㄋㄇㄧㄋ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/人 (char).md` and `characters/民.md`.

### 2026-07-23, iteration 88 — [[words/今年|今年]]

Sixth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bug caught**: `characters:` listed bare `今`, but the actual character file is `今 (char).md` — the missing-`(char)`-suffix bug flagged repeatedly across this vault's logs — corrected to `"今 (char)"`.

**`korean` comma-dump untangled**: `금년,올해` mixed this compound's real Sino-Korean reading (금년, still current in formal registers like 금년도, "this fiscal year") with the everyday native word 올해 — narrowed to 금년 and moved 올해 into prose.

Filled a previously-missing `kwin` field — computed `false` per the AND-rule (both constituents individually `false`). Filled `vietnamese` with the honest compositional `kim niên` (no independent attestation found as a standalone term); the universal everyday Vietnamese phrase is native năm nay.

No `stand_in` relationship applies — both 今's and 年's own `stand_in` fields are bare self-reference. Quoted `hsk_level: "1"`; removed blank `swadesh:`/`aliases:`.

No homophones (`注音: ㄍㄧㄇㄋㄝㄋ` unique to this file). **Incidental fix**: reformatted `characters/今 (char).md`'s bare `[[今年]]` entry to ruby form (`characters/年 (char).md`'s own entry was already correctly formatted).

### 2026-07-23, iteration 89 — [[words/以後|以後]]

Seventh word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: filled blank `pos` (`名詞`) and blank `vietnamese` (`dĩ hậu`, a real attested classical/formal Sino-Vietnamese phrase — verified via search, e.g. từ nay về sau, "from now on" — with modern everyday Vietnamese preferring native sau đó/sau này). Fixed a missing space in `cantonese` (ji5hau6→ji5 hau6); quoted `hsk_level: "1"`; removed blank `swadesh:`/empty `aliases: []`.

**No `stand_in` relationship applies** — both 以's and 後's own `stand_in` fields are bare self-reference. `kwin: false` already correct per the AND-rule (`characters/以 (char).md` is `true`, `characters/後 (char).md` is `false` → compound `false`).

No homophones (`注音: ㄧㄏㄛㄨ` unique to this file). **Incidental fixes**: reformatted `characters/以 (char).md`'s bare `[[以後]]` entry to ruby form; added a missing `## Words` entry to `characters/後 (char).md`. Noted in passing (not investigated further, out of scope): `後 (char).md`'s own stored syllable field reads ㄏㄨㄛ (as in 然後), while 以後 itself stores the same sound as ㄏㄛㄨ — likely just a Bopomofo-notation ordering variance for the same diphthong, similar to the [[滑]] case earlier this sweep, not touched here.

### 2026-07-23, iteration 90 — [[words/会話|会話]]

Eighth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`. Already close to complete — `vietnamese` was already filled with the real, correct `hội thoại`.

**Frontmatter cleanup**: `characters:`/`aliases:` reformatted to proper block form (quoted the `(char)` suffixes). Re-worded the primary `english` gloss from the verb-phrase "talk with; converse with" to the more standard noun form "conversation; to converse," matching how the word functions as a noun in its most common use (日常会話, "everyday conversation"). Quoted `hsk_level: "1"`; removed blank `swadesh:`. Non-canonical `## Etymology` renamed to `## Notes`.

**No `stand_in` relationship applies** — both 会's and 話's own `stand_in` fields are bare self-reference. `kwin: false` already correct per the AND-rule (both constituents individually `false`).

No homophones (`注音: ㄏ⼔ㄏ⺢ㄧ` unique to this file). **Incidental fixes**: updated `characters/会 (char).md`'s existing ruby entry to match the revised gloss; added a missing `## Words` section to `characters/話 (char).md` (had none at all).

### 2026-07-23, iteration 91 — [[words/体育|体育]]

Ninth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`. A clean iteration — `vietnamese` was already correctly filled.

**Frontmatter cleanup**: filled blank `pos` (`名詞`); fixed a typo in the opening bullet's own gloss for 育 ("nuture"→"nurture"); quoted `hsk_level: "1"`; non-canonical `## Etymology` renamed to `## Notes`.

**No `stand_in` relationship applies** — 体's own `stand_in` is `体系`, 育's own is bare `育` — 体育 is an independent compound, not a legitimizer for either. `kwin: false` already correct per the AND-rule (`characters/体.md` is `false`, `characters/育 (char).md` is `true` → compound `false`).

**All cross-linguistic fields already correct** — genuinely the standard word for "physical education" as a school subject across the sphere, no native displacement or homophone collision found.

No homophones (`注音: ㄊㄝㄧ·⼜ㄎ` unique to this file). **Incidental fix**: reformatted `characters/体.md`'s bare `[[体育]]` entry to ruby form (`characters/育 (char).md`'s own entry was already correctly formatted).

### 2026-07-23, iteration 92 — [[words/作業|作業]]

Tenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bug caught**: `characters:` listed bare `作`/`業`, but both actual files are `作 (char).md`/`業 (char).md` — the missing-`(char)`-suffix bug, corrected on both.

**`pos` corrected `性詞`→`事詞`**, matching `characters/作 (char).md`'s own stored category (verb-like "make/do") — the same fix class as several earlier iterations this sweep.

**Genuine register-narrowing finding**: filled `vietnamese` with `tác nghiệp`, a real attested Sino-Vietnamese compound (verified via search), but noted it carries a narrower professional/technical-operations register (journalism, healthcare, security work) than the more general Vietnamese word for "work," công tác. Also noted that Japanese's everyday word for "homework" specifically is 宿題, not 作業, despite this word's own gloss listing "do school work."

No `stand_in` relationship applies — both constituents are bare self-standing characters. `kwin: true` already correct per the AND-rule (both individually `true`). Fixed a missing space in `cantonese` (zok3jip6→zok3 jip6); quoted `hsk_level: "1"`.

No homophones (`注音: ㄐㄚㄎㄝㄆ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/業 (char).md` (`characters/作 (char).md`'s own entry already existed).

### 2026-07-23, iteration 93 — [[words/使用|使用]]

Eleventh word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`. Already close to complete — `vietnamese` was already correctly filled, both character backlinks already properly formatted.

**Stand-in note applied**: `characters/用.md`'s own `stand_in` field is `使用` — added the standard phrasing. (使's own `stand_in` is `使者`, a different word — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/使.md` is `false`, `characters/用.md` is `true` → compound `false`).

**All cross-linguistic fields already correct** — genuinely the standard, everyday word for "to use" across the sphere, no native displacement or homophone collision found. Removed blank `swadesh:` and empty `aliases: []`; quoted `hsk_level: "1"`.

No homophones (`注音: ㄙㄧ·⼄ㄫ` unique to this file). No incidental character-page fixes needed.

### 2026-07-23, iteration 94 — [[words/便宜|便宜]]

Twelfth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`. The densest content-correction iteration in a while.

**Real content bug corrected — a genuine Mandarin heteronym pair**: 便宜 has two established readings with different meanings. The stored fields described biànyí, "convenient, appropriate" (surviving mainly in the set phrase 便宜行事, "act as one sees fit") — but the far more common, HSK-relevant everyday meaning is piányi, "cheap, inexpensive" (这个太便宜了, "this is so cheap"). Corrected `mandarin` and the primary `english` gloss to the piányi/"cheap" reading (verified via search), and the identical wrong gloss on both constituent characters' pre-existing backlinks to this word.

**Cantonese corrected on the same logic**: `bin6 ji4` followed the "convenient" pattern; the real standard Cantonese reading for this specific compound is `pin4 yi4` — though native 平 (ping4) is actually more common than 便宜 itself in everyday Cantonese for "cheap."

**Genuine cross-linguistic asymmetry documented, not forced into agreement**: Japanese べんぎ and Korean 편의 are both real, standard, everyday words — but for the *other* sense, "convenience/expediency" (便宜を図る; 편의점, "convenience store"), not "cheap" at all (neither language uses this compound that way; Japanese 安い, Korean 싸다 cover "cheap"). Left `vietnamese` blank — no single Sino-Vietnamese compound cleanly distinguishing the two senses was confirmed; everyday Vietnamese for "cheap" is native rẻ.

**Incidental fix found and corrected on `characters/便 (char).md`'s own frontmatter**, feeding directly into this word's own opening bullet: its `english` field read `convinient, cheap, plain, shitty` — fixed the typo ("convinient"→"convenient") and the crude/unprofessional wording ("shitty"→"excrement," 便 does legitimately mean feces/excretion as in 大便/小便, just needed professional phrasing).

`characters:` quoting fixed for `便 (char)`. Filled a previously-missing `kwin` field — computed `false` per the AND-rule (`characters/便 (char).md` is `false`, `characters/宜.md` is `true` → compound `false`). No `stand_in` relationship applies — 便's own is bare `便`, 宜's own is `適宜`.

No homophones (`注音: ㄅ⼶ㄋㄜㄧ` unique to this file). **Incidental fixes**: reformatted both `characters/便 (char).md`'s and `characters/宜.md`'s existing backlinks to this word with the corrected gloss.

### 2026-07-23, iteration 95 — [[words/先生|先生]]

Thirteenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Genuine cross-linguistic sense-priority correction, not a wrong-word substitution**: 先生's primary living sense differs sharply by language. In modern Mandarin, xiānsheng chiefly means "Mr., sir" — a general polite title for a man — with the "teacher" sense archaic (superseded by 老师 today); reordered the English gloss to lead with "Mr., sir" rather than "teacher" first, verified via search. Japanese せんせい and Korean 선생, by contrast, genuinely and overwhelmingly mean "teacher" as the living primary sense in both languages.

**Real bug corrected**: `vietnamese: giáo viên` was the generic native/Sino word for "teacher" (built from unrelated roots, 教員), not a reading of 先生 at all — corrected to `tiên sinh`, a real, richly documented Sino-Vietnamese honorific (verified via search) carrying the same range of senses found across the sphere: teacher, respected elder/expert, and (as tiên sanh) a wife's term for her husband.

No `stand_in` relationship applies — 先's own is `優先`, 生's own is `生活` — 先生 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/先.md` is `true`, `characters/生.md` is `false` → compound `false`). Removed blank `swadesh:` and empty `aliases: []`; quoted `hsk_level: "1"`.

No homophones (`注音: ㄙㄝㄋㄙㄚㄫ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/先.md` (`characters/生.md`'s own entry already existed and already correctly prioritized "mister" first).

### 2026-07-23, iteration 96 — [[words/全体|全体]]

Fourteenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**`korean` comma-dump untangled**: `전체,모두,죄다` mixed this compound's real Sino-Korean reading (전체) with the native words 모두/죄다 ("all, everyone") — narrowed to 전체.

Filled a previously-missing `kwin` field — computed `false` per the AND-rule (both constituents individually `false`). Filled `vietnamese` with the real, attested Sino-Vietnamese `toàn thể` (verified via search, extremely common — toàn bộ/tổng thể are close synonyms with slightly different nuance).

No `stand_in` relationship applies — 全's own is bare `全`, 体's own is `体系` — 全体 is an independent compound. `characters:`/`aliases:` reformatted to block form (quoted `全 (char)`); quoted `hsk_level: "1"`; non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄐ⼔ㄋㄊㄝㄧ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/体.md` (`characters/全 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 97 — [[words/全部|全部]]

Fifteenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`. Direct companion to [[全体]] last iteration — same bug class, corrected the same way.

**`korean` comma-dump untangled**: `전부,모두,죄다` mixed this compound's real Sino-Korean reading (전부) with the native words 모두/죄다 — narrowed to 전부, directly paralleling [[全体]]'s own fix.

Filled a previously-missing `kwin` field — computed `false` per the AND-rule (both constituents individually `false`). `vietnamese` (`toàn bộ`) was already correctly filled. No `stand_in` relationship applies — both constituents are bare self-standing characters.

No homophones (`注音: ㄐ⼔ㄋㄅㄛㄨ` unique to this file). **Incidental fix**: reformatted `characters/部 (char).md`'s bare `[[全部]]` entry to ruby form (`characters/全 (char).md`'s own entry was already correctly formatted).

### 2026-07-23, iteration 98 — [[words/公共|公共]]

Sixteenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bug caught**: `characters:` listed bare `公`/`共`, but both actual files are `公 (char).md`/`共 (char).md` — the missing-`(char)`-suffix bug, corrected on both.

No `stand_in` relationship applies — both constituents are bare self-standing characters. `kwin: false` already correct per the AND-rule (`characters/公 (char).md` is `true`, `characters/共 (char).md` is `false` → compound `false`). All other cross-linguistic fields (including `vietnamese: công cộng`) were already correct — a clean compound with directly parallel usage across the sphere. Quoted `hsk_level: "1"`; removed blank `swadesh:`/`aliases:`.

No homophones (`注音: ㄍㄛㄫㄍ⼄ㄫ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/公 (char).md` (`characters/共 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 99 — [[words/公園|公園]]

Seventeenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bug caught**: `characters:` listed bare `公`, but the actual file is `公 (char).md` — corrected. Also caught a mismatched gloss in the opening bullet: it described 公 as "sir" (`characters/公 (char).md`'s own primary stored gloss), but 公 clearly contributes its "public" sense here (as in [[公共]]), not "sir/lord" — corrected the bullet's gloss to match the character's actual contribution to this specific compound, without touching the character's own stored field (out of scope).

No `stand_in` relationship applies — 公's own is bare `公`, 園's own is `庭園` — 公園 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/公 (char).md` is `true`, `characters/園.md` is `false` → compound `false`). All other cross-linguistic fields already correct — a clean compound with directly parallel usage across the sphere. Quoted `hsk_level: "1"`; removed blank `swadesh:`/`aliases:`; non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄍㄛㄫㄛㄋ` unique to this file). **Incidental fixes**: reformatted `characters/公 (char).md`'s bare `[[公園]]` entry to ruby form; added a missing `## Words` entry to `characters/園.md`.

### 2026-07-23, iteration 100 — [[words/内容|内容]]

Eighteenth word in the HSK-1 alphabetical pool — the 100th iteration of this word-perfecting sweep. Stamped `date-last-perfect: 2026-07-23`. A clean pass.

**Frontmatter cleanup**: `characters:`/`aliases:` inline arrays reformatted to block form. Re-worded `english` from "contents, insides" to "content, substance," matching the more standard modern sense (content of a text/message) over the more literal "insides." Quoted `hsk_level: "1"`; removed blank `swadesh:`; non-canonical `## Etymology` renamed to `## Notes`.

**No `stand_in` relationship applies** — 内's own is `内部`, 容's own is bare `容` — 内容 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/内.md` is `false`, `characters/容 (char).md` is `true` → compound `false`). All cross-linguistic fields (including `vietnamese: nội dung`) were already correct.

No homophones (`注音: ㄋㄛㄧ⼄ㄫ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/容 (char).md` (had none at all; `characters/内.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 101 — [[words/出現|出現]]

Nineteenth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**`pos` corrected `性詞`→`事詞`**, matching `characters/出 (char).md`'s own stored category (verb-like "exit/emerge") — the same fix class as several earlier iterations this sweep.

Filled `vietnamese` with `xuất hiện`, an extremely common, real Sino-Vietnamese verb (verified via search) — a very clean match, no register narrowing or asymmetry found this time.

No `stand_in` relationship applies — both constituents are bare self-standing characters. `kwin: true` already correct per the AND-rule (both individually `true`). `characters:` quoting fixed for both entries; non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄑㄨㄊㄏ⼶ㄋ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/現 (char).md` (`characters/出 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 102 — [[words/出発|出発]]

Twentieth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `mandarin: chūfū` — 発 is never read fū; corrected to `chūfā`, matching `characters/発 (char).md`'s own stored reading directly. **`pos` corrected `性詞`→`事詞`**, matching the verb-like reading — the same fix class as several earlier iterations this sweep.

No `stand_in` relationship applies — both constituents are bare self-standing characters. `kwin: false` already correct per the AND-rule (both individually `false`). `vietnamese: xuất phát` was already correctly filled. `characters:` quoting fixed for both entries.

No homophones (`注音: ㄑㄨㄊㄈㄚㄊ` unique to this file). **Incidental fix**: reformatted `characters/発 (char).md`'s bare dash-gloss entry to proper ruby form (`characters/出 (char).md`'s own entry already existed, correctly formatted).

**Pool refreshed**: re-ran the never-perfected HSK-1 query. Next: 分之, 別人, 努力, 勝利, 化学, 医院, 十分, 午飯, 危険, 原来, 去年, 参加, 参観, 友好, 友誼, 反対, 取得, 口語, 可以, 可能, ...

### 2026-07-23, iteration 103 — [[words/分之|分之]]

Twenty-first word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real content bug corrected**: `english: fractions times` was garbled/unclear — corrected to a clearer gloss describing the actual function: "-ths (fraction marker: denominator分之numerator)."

**A genuinely Sino-specific grammatical construction, left honestly incomplete rather than fabricated**: 分之 is the fixed denominator-first fraction particle (三分之一, "one third," literally "of three parts, one"), shared by Mandarin fēnzhī, Cantonese fan1 zi1, Japanese 分の, and Korean 분의. Vietnamese expresses fractions with an entirely different word order and vocabulary (một phần ba, "one part three," numerator-first, native phần) — left `vietnamese` blank rather than force a fabricated reading for a construction Vietnamese doesn't share, the same standard applied to [[不但]] earlier this sweep.

Filled a previously-missing `kwin` field — computed `false` per the AND-rule (`characters/分 (char).md` is `true`, `characters/之 (char).md` is `false` → compound `false`). No `stand_in` relationship applies — both constituents are bare self-standing characters. Removed blank `hsk_level`-adjacent `swadesh:`/`aliases:`; quoted `hsk_level: "1"`; non-canonical `## Etymology` renamed to `## Notes`.

No homophones (`注音: ㄅㄨㄋㄊㄧ` unique to this file). **Incidental fixes**: reformatted `characters/分 (char).md`'s bare `[[分之]]` entry to ruby form with the corrected gloss; added a missing `## Words` entry to `characters/之 (char).md`.

### 2026-07-23, iteration 104 — [[words/別人|別人]]

Twenty-second word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `人`, but the actual file is `人 (char).md` — the recurring bug class from earlier in the sweep.

**Comma-dump untangled**: `korean: "별인, 다른 사람"` held both the compound's own Sino-Korean reading (별인) and an unrelated native-Korean synonym (다른 사람, "different person," built from native 다르다+사람). Kept only 별인 in the field and moved 다른 사람 into prose as a documented register note — verified via search that 별인 is real but markedly rarer/more bookish than 다른 사람 in living speech, not an error, an asymmetry worth recording.

**Vietnamese left honestly blank**: no independently attested Sino-Vietnamese entry for 別人 was found (absent from Vietnamese Wiktionary and Hán Việt dictionaries as a fixed word); Vietnamese instead uses the native phrase người khác. Declined to fabricate a compositional biệt+nhân reading, the same standard applied to [[不但]] and [[分之]] earlier this sweep.

Filled a previously-missing `kwin` field — computed `false` per the AND-rule (both `characters/別 (char).md` and `characters/人 (char).md` are individually `false`). No `stand_in` relationship applies — both constituents are bare self-standing characters. Added the entirely-missing `## Notes` section (the file had none at all).

No homophones (`注音: ㄅㄝㄊㄋㄧㄋ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly ruby-formatted — no incidental character-page fixes needed this iteration.

### 2026-07-23, iteration 105 — [[words/努力|努力]]

Twenty-third word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` field with nỗ lực — a common, real Sino-Vietnamese word (verified via search), a clean compositional match with no register narrowing.

Notable `stand_in` relationship: `characters/努.md`'s own `stand_in` points *to this word* (努力), meaning 努 is a bound morpheme that never appears independently outside this compound — a cranberry-adjacent case. `kwin: false` was already correct per the AND-rule (`characters/努.md` is `kwin: true`, `characters/力 (char).md` is `kwin: false` → compound `false`). All other cross-linguistic fields (mandarin, cantonese, japanese, korean) were already correct, everyday readings. Renamed non-canonical `## Etymology` to `## Notes`; removed blank `aliases: []`.

No homophones (`注音: ㄋㄛㄌㄧㄎ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed this iteration.

### 2026-07-23, iteration 106 — [[words/勝利|勝利]]

Twenty-fourth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `pos` field with 事詞 (verb-like), matching this word's primary living use as a verb ("to win, to triumph"), with secondary noun use ("victory").

Notable `stand_in` relationship: `characters/勝.md`'s own `stand_in` points *to this word* (勝利), another bound-morpheme case like [[努力|努's own stand_in from last iteration]]. `kwin: false` was already correct per the AND-rule (both `characters/勝.md` and `characters/利.md` are individually `kwin: false`). All cross-linguistic fields (mandarin, cantonese, japanese, korean, vietnamese) were already correct, everyday readings. Renamed non-canonical `## Etymology` to `## Notes`; removed blank `aliases: []`.

No homophones (`注音: ㄙㄨㄫㄌㄧㄜ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed this iteration.

### 2026-07-23, iteration 107 — [[words/化学|化学]]

Twenty-fifth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Added the entirely-missing `## Notes` section (the file had only an audio embed and meta-bind before). No `stand_in` relationship applies — 化's own is bare 化, 学's own is 学習 (points elsewhere). `kwin: true` was already correct per the AND-rule (both `characters/化 (char).md` and `characters/学.md` are individually `kwin: true`). All cross-linguistic fields (mandarin, cantonese, japanese, korean, vietnamese) were already correct, everyday readings — no bugs found this iteration.

One prefix-substring false positive ruled out: `化学肥料`'s `注音` (`ㄏ⺢ㄏㄚㄎㄅㄨㄧㄌ⼘ㄨ`) begins with this word's exact string, but it's simply a longer compound built on top of 化学 ("chemical fertilizer" = 化学 + 肥料), not a genuine homophone collision — no callout added, consistent with the sweep's established prefix-substring exclusion rule. Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 108 — [[words/医院|医院]]

Twenty-sixth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Genuine cross-linguistic sense-size difference found and documented, not corrected away**: `english` previously read only "clinic," but Mandarin yīyuàn/Cantonese ji1 jyun6-2 are the ordinary, general-purpose words for "hospital" (any size) — the HSK-relevant primary sense. Japanese いいん and Korean 의원, however, specifically denote a small private clinic/practice, legally distinguished from 病院/병원 ("hospital," 20+ beds) — verified via search. Corrected the English gloss to lead with "hospital" while documenting the narrower Japanese/Korean sense as a real, non-error asymmetry (the same fix-class as [[先生]]/[[便宜]]/[[石頭]] earlier this sweep). Verified vietnamese y viện is a real, if less common, Sino-Vietnamese word for "hospital" (confirmed on Vietnamese Wiktionary, not fabricated) — the everyday Vietnamese word is bệnh viện instead.

Filled a previously-blank `pos` (名詞) and a previously-missing `kwin` (computed `false` per the AND-rule: `characters/医.md` is `kwin: false`, `characters/院.md` is `kwin: true` → compound `false`). No `stand_in` relationship applies (医's own is 医生, 院's own is 院落). Renamed non-canonical `## Etymology` to `## Notes`.

One false-positive homophone ruled out: `資源`'s `注音` (`ㄐㄧㄜ⼔ㄋ`) contains this word's string (`ㄜ⼔ㄋ`) as a substring, but the two words are not actually homophones — 医院 is `'ǝ'wen` while 資源 is `jiǝ'wen`, different first syllables entirely; the shared portion is only the second syllable ⼔ㄋ. No callout added. Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 109 — [[words/十分|十分]]

Twenty-seventh word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `mandarin: hífēn` — 十 is never read hí; corrected to `shífēn`, matching `characters/十 (char).md`'s own stored reading. **Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `十`, but the actual file is `十 (char).md`.

Filled a previously-blank `vietnamese` with thập phần — a real, attested Hán-Việt intensifier (verified via search), matching both English senses. Documented a genuine Japanese heteronym split rather than treating it as an error: じゅうぶん (jūbun, "sufficient; very") is correct for the word's primary listed sense and was left as-is, but the literal "ten minutes" sense is actually read じっぷん/じゅっぷん (jippun/juppun) instead, a real distinction verified via search — Mandarin/Cantonese/Korean/Vietnamese all cover both senses with one single reading, unlike Japanese.

No `stand_in` relationship applies — both constituents are bare self-standing characters. `kwin: true` already correct per the AND-rule (both individually `true`). Quoted `hsk_level: "1"`; removed blank `swadesh:`/`aliases: []`; renamed non-canonical `## Etymology`-less body to include a proper `## Notes` section.

No homophones (`注音: ㄙㄧㄆㄍㄨㄋ` unique to this file). **Incidental fixes**: reformatted `characters/十 (char).md`'s bare `[[十分]]` entry to ruby form; added a missing `## Words` entry to `characters/分 (char).md` (which had no entry for this word at all).

### 2026-07-23, iteration 110 — [[words/午飯|午飯]]

Twenty-eighth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Wrong-word conflation corrected**: `korean: 점심` was the modern everyday Korean word for "lunch" — but 점심 is actually 點心, an entirely different compound ("dot the heart/mind," originally "snack"), not a reading of 午飯 at all. Researched and confirmed the genuine Sino-Korean reading 오반 (a real, if now old-fashioned, historical term for a more substantial midday meal, as distinct from the originally-lighter 점심) — corrected the field and documented the distinction in prose, the same fix-class as [[右側]]/[[左側]] and [[先生]] earlier this sweep.

**Genuine homophone-across-different-hanja confirmed, not an error**: Japanese ごはん is verified correct for 午飯 itself (attested directly in goo/Weblio/Kotobank dictionaries), but coincidentally identical in sound to the totally unrelated everyday word 御飯 ("cooked rice; meal") — the same recurring cross-linguistic pattern documented several times earlier this sweep ([[羽翼]]/右翼, [[思考]]'s 사고 cluster, etc.).

Deduplicated a comma-dump `vietnamese` field (`bữa trưa, bữa ăn trưa` — two native synonyms, neither a genuine Sino-Vietnamese reading of the compound) down to bữa trưa. Filled a previously-blank `pos` (名詞). No `stand_in` relationship applies (午's own is 正午, 飯's own is 米飯). `kwin: false` already correct per the AND-rule (`characters/午.md` is `true`, `characters/飯.md` is `false` → compound `false`).

No homophones (`注音: ㄛㄅㄛㄋ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 111 — [[words/危険|危険]]

Twenty-ninth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `pos` (性詞, matching the adjective-like "dangerous"). No `stand_in` relationship applies for `険 (char)`, but `characters/危.md`'s own `stand_in` points *to this word* — another bound-morpheme case like [[努力]]/[[勝利]] earlier this sweep. `kwin: false` already correct per the AND-rule (`characters/危.md` is `false`, `characters/険 (char).md` is `true` → compound `false`). Cantonese, Japanese, Korean, and Vietnamese were all already correct, everyday readings.

**Left unresolved — genuinely questionable, not corrected either way**: `mandarin` stores two readings, `wēixiǎn,wéixiǎn`. wēixiǎn is unambiguously standard (matches `characters/危.md`'s own stored wēi), but no dictionary consulted via search could confirm wéixiǎn as an attested modern alternate reading — only an ambiguous Middle Chinese fanqie derivation (魚爲切) that doesn't decisively resolve to either outcome. Rather than guess whether this is a typo or an obscure real variant, left it as stored and flagged it here per the loop's "skip questionable items" instruction.

No homophones (`注音: ⼔ㄧㄏㄝㄇ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 112 — [[words/原来|原来]]

Thirtieth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with nguyên lai — a real Sino-Vietnamese word (confirmed on Vietnamese Wiktionary), more literary than the everyday native equivalents vốn dĩ/hóa ra. Filled a previously-blank `pos` (修飾語, modifier). Confirmed Japanese's two listed readings (げんらい, がんらい) are genuine alternate pronunciations of the same word rather than a comma-dump error.

No `stand_in` relationship applies (原's own is 原始, 来's own is bare 来). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ⼔ㄋㄌㄚㄧ` unique to this file). **Incidental fixes**: reformatted `characters/原.md`'s bare `[[原来]]` entry to ruby form; added a missing `## Words` entry to `characters/来 (char).md` (which had no entry for this word at all).

### 2026-07-23, iteration 113 — [[words/去年|去年]]

Thirty-first word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Wrong-word conflation corrected**: `korean: 작년` was the modern everyday Korean word for "last year" — but 작년 is actually the reading of the sibling word [[昨年]] (昨 + 年), not of 去年 itself. Researched and confirmed the genuine, if dated/uncommon, Sino-Korean reading 거년 (verified via search/Wiktionary) — corrected the field.

Filled a previously-blank `vietnamese` with khứ niên, a real Hán-Việt term (verified via search); the everyday native Vietnamese equivalent is năm ngoái/năm qua instead. Confirmed Cantonese's two listed tone variants (heoi3 nin4, heoi3 nin4-2) are genuine alternate realizations, not a comma-dump error. Fixed unquoted `characters:` entries to quoted `"去 (char)"`/`"年 (char)"` for consistency.

**Incidental sibling-word fix, discovered while researching this word**: `words/昨年.md`'s own `mandarin` (`qùnián`) and `cantonese` (`heoi3 nin4`) fields were directly copy-pasted from 去年 rather than reflecting 昨年's own reading. Corrected to zuónián/zok6 nin4 (matching `characters/昨 (char).md`'s own stored zuó/zok6) — confirmed via search that 昨年 zuónián is a genuine, if archaic/literary, Mandarin reading distinct from the common 去年. (`words/昨年.md` was not otherwise perfected this iteration — it remains in the pool for its own full pass.)

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄎ⼄ㄋㄝㄋ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 114 — [[words/参加|参加]]

Thirty-second word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin cānjiā, cantonese caam1gaa1→reformatted with a space as caam1 gaa1 for consistency, japanese さんか, korean 참가, vietnamese tham gia) — no bugs found.

Notable `stand_in` relationship: `characters/参.md`'s own `stand_in` points *to this word* (参加), another bound-morpheme case like [[努力]]/[[勝利]]/[[危険]] earlier this sweep. `kwin: false` was already correct per the AND-rule (`characters/参.md` is `false`, `characters/加.md` is `true` → compound `false`).

One false-positive homophone ruled out: `三綱`'s `注音` (`ㄙㄚㄇㄍㄚㄫ`) begins with this word's exact string, but 三綱 is longer (an extra final ㄫ) — not a genuine homophone, the same prefix-substring pattern ruled out several times this sweep.

No homophones (`注音: ㄙㄚㄇㄍㄚ` unique to this file otherwise). **Incidental fixes**: added missing `## Words` entries to both `characters/参.md` and `characters/加.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 115 — [[words/参観|参観]]

Thirty-third word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss clarified**: `english` previously read only "look around," an imprecise gloss — corrected to lead with "visit; tour (a place)," matching this word's primary living sense across all attested languages (verified via reasoning about each): Mandarin/Cantonese cānguān ("to visit," e.g. a factory), Japanese さんかん (school visitation days, 授業参観), Korean 참관 ("observe/attend," e.g. a trial), Vietnamese tham quan ("visit, sightsee") — all standard, everyday readings otherwise, no bugs found. Reformatted Cantonese with a space (`caam1gun1`→`caam1 gun1`) for consistency.

No `stand_in` relationship applies to this compound specifically — 参's own `stand_in` points to the sibling word [[参加]] instead, 観's own is 観察. `kwin: false` already correct per the AND-rule (`characters/参.md` is `false`, `characters/観.md` is `true` → compound `false`).

No homophones (`注音: ㄙㄚㄇㄍ⺢ㄋ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/参.md` and `characters/観.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 116 — [[words/友好|友好]]

Thirty-fourth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**`pos` corrected `名詞`→`性詞`**, matching this word's primary living use as an adjective ("friendly, amicable," e.g. 友好国家/友好关系), with attributive-noun use ("friendship, amity") secondary — verified via search. Reordered `english` to lead with the adjective sense.

Filled a previously-blank `vietnamese` with hữu hảo, a real Sino-Vietnamese word (verified via search) for "friendly, harmonious" (especially of international relations). Cantonese, Japanese, and Korean were already correct, standard readings.

No `stand_in` relationship applies (友's own is 朋友, 好's own is bare 好). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ⼜ㄛㄏㄚㄨ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 117 — [[words/友誼|友誼]]

Thirty-fifth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Common-mispronunciation variant removed, not a genuine alternate reading**: `mandarin` previously listed `yǒuyì,yǒuyí` and `cantonese` listed `jau5 ji4,jau5 ji6`. Researched and confirmed yǒuyí is a widespread mispronunciation (誼's phonetic component 宜 misleadingly suggests yí), but the dictionary-correct reading is yǒuyì only, matching `characters/誼.md`'s own stored yì — removed the second variant from both fields rather than presenting it as equally valid.

**Wrong-word conflation corrected**: `vietnamese: tình bạn` was the everyday native word for "friendship," not a reading of 友誼 itself — corrected to hữu nghị, the genuine, extremely common Sino-Vietnamese reading (verified via search, e.g. "Cầu Hữu Nghị," the Friendship Bridge).

Filled a previously-missing `kwin` — computed `false` per the AND-rule (`characters/友.md` is `kwin: false`, `characters/誼.md` is `kwin: true` → compound `false`). Notable `stand_in` relationship: `characters/誼.md`'s own `stand_in` points *to this word* (友誼), another bound-morpheme case like several earlier this sweep.

No homophones (`注音: ⼜ㄛ·ㄜㄧ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/誼.md` (had none at all; `characters/友.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 118 — [[words/反対|反対]]

Thirty-sixth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin fǎnduì, cantonese faan2 deoi3, japanese はんたい, korean 반대, vietnamese phản đối) — no bugs found. Added the entirely-missing `## Notes` section (the file had only a non-canonical `## Etymology`).

Notable `stand_in` relationship: `characters/対.md`'s own `stand_in` points *to this word* (反対), another bound-morpheme case like several earlier this sweep. `kwin: false` already correct per the AND-rule (both `characters/反 (char).md` and `characters/対.md` individually `false`).

No homophones (`注音: ㄈㄛㄋㄉㄛㄧ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 119 — [[words/取得|取得]]

Thirty-seventh word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with thủ đắc, a real Sino-Vietnamese word (verified via search), used especially in legal/formal contexts. Mandarin, Cantonese, Japanese, and Korean were already correct, standard readings.

Notable `stand_in` relationship: `characters/取.md`'s own `stand_in` points *to this word* (取得), another bound-morpheme case like several earlier this sweep; 得's own points elsewhere (獲得). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄑㄛㄨㄊㄜㄎ` unique to this file). **Incidental fixes**: `characters/取.md`'s existing `[[取得]]` backlink had a wrong `<rt>` annotation (`ㄑㄛㄨㄉㄝㄊ`, mismatching 得's actual reading) — corrected to `ㄑㄛㄨㄊㄜㄎ`; added a missing `## Words` entry to `characters/得.md` (had none at all).

### 2026-07-23, iteration 120 — [[words/口語|口語]]

Thirty-eighth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `口`, but the actual file is `口 (char).md`. Filled a previously-blank `vietnamese` with khẩu ngữ, a real, standard Sino-Vietnamese word (verified via search). Mandarin, Cantonese, Japanese, and Korean were already correct.

No `stand_in` relationship applies (口's own is bare 口, 語's own is 言語). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄎㄛㄨ⼄` unique to this file). **Incidental fixes**: reformatted `characters/語.md`'s bare `[[口語]]` entry to ruby form; added a missing `## Words` entry to `characters/口 (char).md` (which had no entry for this word at all).

### 2026-07-23, iteration 121 — [[words/可以|可以]]

Thirty-ninth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with khả dĩ, a real, if formal/literary, Sino-Vietnamese word (verified via search). Confirmed via search that Japanese and Korean genuinely lack a corresponding word built from these characters — both use entirely native grammatical constructions instead (Japanese ～できる, Korean -을/ㄹ 수 있다) — so `japanese`/`korean` were correctly left blank already, the same honesty standard as [[不但]]/[[分之]] earlier this sweep; this iteration confirmed the existing blank fields and Notes explanation rather than needing to change them.

No `stand_in` relationship applies (可's own is bare 可, 以's own is bare 以). `kwin: false` already correct per the AND-rule (`characters/可 (char).md` is `false`, `characters/以 (char).md` is `true` → compound `false`).

One false-positive homophone ruled out: `不可以`'s `注音` (`ㄅㄛㄊㄎㄜㄧ`) contains this word's exact string as a suffix, but it's a longer, distinct compound (不可以 = 不 + 可以), not a genuine homophone. Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 122 — [[words/可能|可能]]

Fortieth word in the HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing readings filled**: `mandarin`/`cantonese` were both entirely blank — filled with kěnéng/ho2 nang4, matching each character's own stored reading. **Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `可`, but the actual file is `可 (char).md`.

Folded a stray, unformatted note found in the file body ("prefer to 可以") into a proper `## Notes` explanation distinguishing 可能 (epistemic possibility, "possible; maybe") from the semantically related [[可以]] (permission/ability, "can, may do X") — not a bug, a clarification of an existing but oddly-placed editorial note.

No `stand_in` relationship applies (可's own is bare 可, 能's own is 技能). `kwin: false` already correct per the AND-rule (`characters/可 (char).md` is `false`, `characters/能.md` is `true` → compound `false`). Japanese かのう, Korean 가능, and Vietnamese khả năng were already correct, standard readings.

No homophones (`注音: ㄎㄜㄋㄜㄫ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/能.md` (`characters/可 (char).md`'s own entry already existed, correctly formatted).

**Pool refreshed**: re-ran the never-perfected HSK-1 query. Next: 各種, 同学, 同志, 同意, 同時, 名字, 周囲, 咳漱, 問題, 回答, 団結, 困難, 国家, 地方, 城市, 基本, 基礎, 堅持, 増加, 声調, 変成, 外国, 多少, 大声, 大学, 大家, 夫人, 姑娘, 媽媽, 学校, ...

### 2026-07-23, iteration 123 — [[words/各種|各種]]

First word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `各`, but the actual file is `各 (char).md`. Mandarin, Cantonese, Japanese, and Korean were already correct, standard readings.

**Left `vietnamese` honestly blank, not fabricated**: no dictionary attestation was found for a fixed compound "các chủng" as a genuine standalone word. Vietnamese 各 (các) has instead been grammaticalized into an extremely common native-feeling plural marker/article (các bạn, các anh chị em) rather than retained as a lexical noun-compounding morpheme — the two-character compound doesn't appear to survive intact as a word the way it does in the other four languages, unlike e.g. [[友好]]'s hữu hảo, which had a dedicated Wiktionary entry confirming it.

No `stand_in` relationship applies (各's own is bare 各, 種's own is 種類). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄍㄚㄎㄐㄛㄫ` unique to this file). **Incidental fixes**: reformatted `characters/各 (char).md`'s bare `[[各種]]` entry to ruby form; added a missing `## Words` entry to `characters/種.md`.

### 2026-07-23, iteration 124 — [[words/同学|同学]]

Second word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with đồng học, a real Sino-Vietnamese word (confirmed on Vietnamese Wiktionary), more formal than everyday học chung/bạn học.

**Genuine homophone-across-different-hanja confirmed, not an error**: investigated whether Korean `동학` was a wrong-word conflation with the famous 19th-century Donghak (東學) religious/political movement — researched and confirmed 同學 (동학, "classmate; fellow student") is itself a real, independently attested dictionary word, merely an exact homophone of the unrelated 東學 movement. Another instance of the recurring cross-linguistic pattern from this sweep (cf. [[午飯]], [[羽翼]]/右翼). No correction needed.

No `stand_in` relationship applies (同's own is 同一, 学's own is 学習). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄉㄛㄫㄏㄚㄎ` unique to this file — vault-internal, not to be confused with the cross-linguistic Korean homophone noted above). **Incidental fix**: added a missing `## Words` entry to `characters/同.md` (`characters/学.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 125 — [[words/同志|同志]]

Third word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin tóngzhì, cantonese tung4 zi3, japanese どうし, korean 동지, vietnamese đồng chí) — no bugs found. No `stand_in` relationship applies (同's own is 同一, 志's own is 意志). `kwin: true` already correct per the AND-rule (both individually `true`).

**Genuine Dan'a'yo-internal homophone found and formalized**: exact-string search on `注音` (`ㄉㄛㄫㄐㄧ`) turned up `words/東芝.md` ("Toshiba") — verified all three fields (`羅馬字`, `諺文`, `注音`) match exactly (dongji/동지/ㄉㄛㄫㄐㄧ), a genuine collision, not a prefix-substring false positive. `東芝.md`'s own prose already noted the Korean-specific coincidence informally, but neither page had a proper `>[!warning] Homophones` callout — added reciprocal callouts to both files. (Also checked [[冬至]] as a candidate third Korean homophone mentioned in 東芝's prose — its actual Dan'a'yo reading is tongjiǝ/통즤/ㄊㄛㄫㄐㄧㄜ, different from dongji/동지/ㄉㄛㄫㄐㄧ, so it is *not* a Dan'a'yo-internal homophone, only a coincidence of Korean's own native phonology — correctly left out of the callout.)

**Incidental fixes**: reformatted `characters/同.md`'s bare `[[同志]]` entry to ruby form; added a missing `## Words` entry to `characters/志.md` (had none for this word at all).

### 2026-07-23, iteration 126 — [[words/同意|同意]]

Fourth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `cantonese: ung4 ji3` was missing the initial consonant — 同 is never read ung4; corrected to `tung4 ji3`, matching `characters/同.md`'s own stored reading. **`pos` corrected `性詞`→`事詞`**, matching this word's primary use as a verb ("to agree, consent"). Simplified `japanese` from the conjugated verb phrase どういする to the bare dictionary form どうい, matching vault convention.

Filled a previously-missing `kwin` — computed `false` per the AND-rule (`characters/同.md` is `kwin: true`, `characters/意.md` is `kwin: false` → compound `false`). No `stand_in` relationship applies (同's own is 同一, 意's own is 意味).

No homophones (`注音: ㄉㄛㄫㄜ` unique to this file). **Incidental fixes**: reformatted `characters/同.md`'s bare `[[同意]]` entry to ruby form; added a missing `## Words` entry to `characters/意.md` (had none for this word at all).

### 2026-07-23, iteration 127 — [[words/同時|同時]]

Fifth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `時`, but the actual file is `時 (char).md`. Reformatted Cantonese with a space (`tung4si4`→`tung4 si4`) for consistency; all cross-linguistic fields otherwise already correct, standard readings.

No `stand_in` relationship applies (同's own is 同一, 時's own is bare 時). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄉㄛㄫㄙㄧ` unique to this file). **Incidental fixes**: reformatted `characters/同.md`'s bare `[[同時]]` entry to ruby form; added a missing `## Words` entry to `characters/時 (char).md` (had none for this word at all).

### 2026-07-23, iteration 128 — [[words/名字|名字]]

Sixth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss clarified**: `english` previously read "name characters," a garbled gloss — corrected to "name (personal name)," matching Mandarin's actual everyday meaning. Propagated the same gloss fix to the backlink entries on both `characters/名 (char).md` and `characters/字 (char).md`, which had inherited the old bad gloss.

**Genuine cross-linguistic sense-narrowing found and documented, not corrected away**: Japanese 名字/苗字 (みょうじ) specifically means "surname; family name," distinct from 名前 ("given/full name") — narrower than Mandarin's general "name" (verified via search). Korean 명자 confirmed as a real, if less common than native 이름, Sino-Korean word for the same general sense as Mandarin (confirmed on Korean Wiktionary).

**Left `vietnamese` honestly blank**: no clear dictionary attestation was found for a standalone compound "danh tự" (the search only produced a compositional AI-generated gloss, not a dedicated entry, unlike e.g. [[友好]]'s hữu hảo) — left blank rather than fabricate. Fixed the missing `(char)` suffix quoting on both `characters:` entries.

No `stand_in` relationship applies (名's own is bare 名, 字's own is bare 字). `kwin: false` already correct per the AND-rule (both individually `false`).

One false-positive homophone ruled out: `無名指`'s `注音` (`ㄇㄜㄇㄧㄫㄐㄧㄜ`) contains this word's string as a substring, but the two are not homophones — different surrounding syllables entirely. Both constituent characters' `## Words` backlinks were already present and correctly ruby-formatted (aside from the gloss fix above).

### 2026-07-23, iteration 129 — [[words/周囲|周囲]]

Seventh word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `cantonese: jau1wai4` — 周 is never read jau1 (its own character page confirms zau1); corrected to `zau1 wai4`.

**Historical-orthography variant moved to prose, not a distinct reading**: `japanese` previously listed `しゅうい,しうゐ` as if two alternate readings — researched and confirmed しうゐ is not a separate pronunciation but the pre-reform historical kana spelling (歴史的仮名遣い) of the same modern しゅうい reading. Kept only the modern spelling in the field, documented the historical variant in prose instead of treating it as a comma-dump reading.

Vietnamese chu vi was already correct — the standard, extremely common math term for "perimeter/circumference." No `stand_in` relationship applies (周's own is 圓周, 囲's own is 包囲). `kwin: false` already correct per the AND-rule (`characters/周.md` is `false`, `characters/囲.md` is `true` → compound `false`).

No homophones (`注音: ㄐㄨㄛㄨㄧ` unique to this file). **Incidental fix**: reformatted `characters/周.md`'s bare `[[周囲]]` entry to ruby form (`characters/囲.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 130 — [[words/咳漱|咳漱]]

Eighth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Confirmed the word is titled 咳漱 rather than the more familiar 咳嗽 because Dan'a'yo folds 嗽 into 漱 (listed as 漱's own `aliases` entry) — the same character-merging convention as 叛→反 documented earlier in the vault; 咳嗽 is correctly kept as this word's own `aliases` entry, not an error.

**Real typo corrected**: `cantonese: kat1sau3` — missing a space between syllables, corrected to `kat1 sau3`. **`pos` corrected `性詞`→`事詞`**, matching this word's verb/noun-like use.

Researched and confirmed Korean 해수 and Japanese がいそう are both real, standard words for "cough" — but specifically formal/medical-register terms (traditional Korean medicine, Japanese clinical terminology), distinct from the everyday native words 기침/せき. Documented as a genuine register distinction, not an error.

**Left `vietnamese` honestly blank — genuinely questionable**: search results conflicted on the correct Hán-Việt reading ("khái thấu," matching 咳's own stored reading, vs. "hài thấu," a reading not listed anywhere on `characters/咳.md`) — rather than guess between contradictory sources, left blank per the loop's "skip questionable items" instruction.

Notable `stand_in` relationship: `characters/咳.md`'s own `stand_in` points *to this word* (咳漱), another bound-morpheme case like several earlier this sweep; 漱's own points elsewhere (含漱). `kwin: false` already correct per the AND-rule (`characters/咳.md` is `true`, `characters/漱.md` is `false` → compound `false`).

No homophones (`注音: ㄏㄚㄧㄙㄛㄨ` unique to this file). **Incidental fixes**: reformatted `characters/咳.md`'s bare `[[咳漱]]` entry to ruby form; added a missing `## Words` section to `characters/漱.md` (had none at all).

### 2026-07-23, iteration 131 — [[words/問題|問題]]

Ninth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bug corrected**: `mandarin` previously held the hanzi characters themselves (`问题`) rather than a pinyin reading — corrected to `wèntí`. Filled a previously-blank `cantonese` with `man6 tai4`, matching each character's own stored reading. Japanese もんだい, Korean 문제, and Vietnamese vấn đề were already correct, standard readings.

No `stand_in` relationship applies (問's own is 質問, 題's own is 標題). `kwin: false` already correct per the AND-rule (`characters/問.md` is `true`, `characters/題.md` is `false` → compound `false`).

No homophones (`注音: ㄇㄨㄋㄊㄝㄧ` unique to this file). **Incidental fixes**: reformatted `characters/問.md`'s bare `[[問題]]` entry to ruby form; added a missing `## Words` entry to `characters/題.md` (had none for this word at all).

### 2026-07-23, iteration 132 — [[words/回答|回答]]

Tenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `回`/`答`, but the actual files are `回 (char).md`/`答 (char).md`. **`pos` corrected `性詞`→`事詞`**, matching this word's primary use as a verb/action-noun ("to reply, respond").

Filled a previously-blank `vietnamese` with hồi đáp, a real, more formal/written-register Sino-Vietnamese word (verified via search) — the everyday equivalent is trả lời. Mandarin, Cantonese, Japanese, and Korean were already correct, standard readings.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄏㄛㄧㄉㄚㄆ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/答 (char).md` (`characters/回 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 133 — [[words/団結|団結]]

Eleventh word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `結`, but the actual file is `結 (char).md`. All cross-linguistic fields were already correct, standard readings (mandarin tuánjié, cantonese tyun4 git3, japanese だんけつ, korean 단결, vietnamese đoàn kết) — no bugs found.

No `stand_in` relationship applies (団's own is 集団, 結's own is bare 結). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄉ⺢ㄋㄍㄝㄊ` unique to this file). **Incidental fixes**: reformatted `characters/団.md`'s bare `[[団結]]` entry to ruby form; added a missing `## Words` entry to `characters/結 (char).md` (had none for this word at all).

### 2026-07-23, iteration 134 — [[words/困難|困難]]

Twelfth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Verified correct rather than "fixed" — a near-miss on breaking the standing North-Korean rule**: `korean: 곤난` looked suspicious at first glance (곤란 is the far more familiar form), but research confirmed 곤난 is the original/North Korean 문화어 reading, while 곤란 is a South-Korea-only sound-softening (활음조) innovation — the stored value was already exactly right per this vault's standing North-Korean-pronunciation rule, and was deliberately left unchanged.

**Left `vietnamese` deliberately blank — a false-friend trap, not a simple gap**: the compositionally expected khốn nạn is indeed the direct Sino-Vietnamese descendant of 困難, but has undergone drastic semantic pejoration in modern Vietnamese to mean "wretched; damn; a contemptible person" — a strong insult, not "difficult" (verified via search). Filling this field would have actively misled a learner into vulgar language. Left blank and documented the semantic drift instead.

Notable `stand_in` relationship: `characters/難.md`'s own `stand_in` points *to this word* (困難), another bound-morpheme case like several earlier this sweep. `kwin: false` already correct per the AND-rule (`characters/困.md` is `false`, `characters/難.md` is `true` → compound `false`).

No homophones (`注音: ㄎㄛㄋㄋㄚㄋ` unique to this file). **Incidental fixes**: reformatted `characters/困.md`'s bare `[[困難]]` entry to ruby form; added a missing `## Words` entry to `characters/難.md` (had none for this word at all).

### 2026-07-23, iteration 135 — [[words/国家|国家]]

Thirteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-missing `kwin` — computed `false` per the AND-rule (`characters/国.md` is `kwin: false`, `characters/家.md` is `kwin: true` → compound `false`). Notable `stand_in` relationship: `characters/国.md`'s own `stand_in` points *to this word*. All cross-linguistic fields were already correct, standard readings.

**Formalized an already-known homophone**: the file already had informal prose noting a collision with [[国歌]] ("national anthem") — verified all three fields match exactly (gogga/곡가/ㄍㄛㄎㄍㄚ) and converted it to a proper `>[!warning] Homophones` callout in the correct position (after meta-bind-embed, before `## Notes`). **Incidental sibling-word fix**: `words/国歌.md`'s own reciprocal note used the wrong callout type (`[!warn]` instead of `[!warning]`) and was positioned before the meta-bind-embed rather than after — corrected both to match vault convention.

No homophones beyond the one already documented. **Incidental fix**: added a missing `## Words` entry to `characters/家.md` (`characters/国.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 136 — [[words/地方|地方]]

Fourteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `cantonese: di4 fang1` had two separate errors — 地 is never read di4 (its own character page confirms dei6), and 方 is never read fang1 (confirmed fong1); corrected to `dei6 fong1`.

**Genuine Mandarin tone-based heteronym confirmed, not touched**: dìfang (neutral tone, "place; location," matching the word's primary sense) and dìfāng (full tone, "local," as opposed to central/military) are both real, distinct readings (verified via search) — left both in the field.

**Comma-dump untangled**: `korean: 지방, 시골` — 지방 is the compound's own Sino-Korean reading, while 시골 is an unrelated native word for "countryside." Kept only 지방. Filled a previously-blank `vietnamese` with địa phương, a real, extremely common word (confirmed on Vietnamese Wiktionary). Filled a previously-missing `kwin` — computed `false` per the AND-rule (both characters individually `false`).

No `stand_in` relationship applies (地's own is bare 地, 方's own is 方向). No homophones (`注音: ㄉㄧㄜㄈㄚㄫ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/方.md` (`characters/地 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 137 — [[words/城市|城市]]

Fifteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Wrong-word conflation corrected**: `japanese: とし` and `korean: 도시` were both actually the readings of the sibling word [[都市]] (市's own `stand_in`), not of 城市 itself — the file's own leftover note ("not generic 'city' (都市)") had already flagged the distinction, but the fields still held the wrong word's readings. Corrected to 城市's own genuine readings: Japanese じょうし (confirmed real via search — "city; castle town," historically a walled marketplace) and Korean 성시 (confirmed real via search — and notably, 성시 is specifically documented as the *North Korean* word for city, a striking match for this vault's standing North-Korean-pronunciation rule, the same pattern as [[困難]] earlier this sweep).

Filled a previously-blank `vietnamese` with thành thị, a real, common word (confirmed on Vietnamese Wiktionary). Filled a previously-blank `pos` (名詞). No `stand_in` relationship applies to this specific compound (市's own points to 都市, 城's own points to 城郭). `kwin: false` already correct per the AND-rule (`characters/城.md` is `false`, `characters/市.md` is `true` → compound `false`).

Three false-positive homophones ruled out via exact-field verification: `姓氏`/`誠心`/`誠実` all begin with the same `注音` prefix (`ㄙㄧㄫㄙㄧ`) but are each one syllable longer with a different final consonant — not genuine matches. **Incidental fix**: reformatted `characters/城.md`'s bare `[[城市]]` entry to ruby form (`characters/市.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 138 — [[words/基本|基本]]

Sixteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with cơ bản, an extremely common, real Sino-Vietnamese word ("basic; fundamental"). Mandarin, Cantonese, Japanese, and Korean were already correct, standard readings.

Notable `stand_in` relationship: `characters/基.md`'s own `stand_in` points *to this word* (基本), another bound-morpheme case like several earlier this sweep. `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄍㄧㄅㄛㄋ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/基.md` (`characters/本 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 139 — [[words/基礎|基礎]]

Seventeenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Content removed — a false homophone claim caught and corrected**: both `words/基礎.md` and `words/其処.md` ("there," medial) claimed to be mutual homophones, both supposedly reading *gǝco*. Verified via exact-field comparison that this is wrong: `characters/基.md`'s own reading is gi/기/ㄍㄧ, while `characters/其 (char).md`'s own reading is gǝ/그/ㄍㄜ — a genuine vowel difference. 基礎 is actually gico/기초/ㄍㄧㄑㄛ (matching its own stored fields and `characters/礎.md`'s backlink rt), while 其処 is gǝco/그초/ㄍㄜㄑㄛ — not homophones at all. **Removed the false claim from both files** rather than formalize it into a callout.

No `stand_in` relationship applies to 基 here (its own points to the sibling word [[基本]]), but `characters/礎.md`'s own `stand_in` points to this word (基礎) — a bound-morpheme case. `kwin: true` already correct per the AND-rule (both individually `true`). Vietnamese cơ sở, mandarin jīchǔ, cantonese gei1 co2, japanese きそ, and korean 기초 were all already correct.

No genuine homophones exist (`注音: ㄍㄧㄑㄛ` — one false-positive prefix-substring match ruled out: `世紀初`'s `注音` `ㄙㄝㄍㄧㄑㄛ` merely contains this string as a suffix). **Incidental fix**: added a missing `## Words` entry to `characters/基.md` (`characters/礎.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 140 — [[words/堅持|堅持]]

Eighteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `持`, but the actual file is `持 (char).md`. Filled a previously-blank `vietnamese` with kiên trì, a real, extremely common Sino-Vietnamese word (verified via search). Mandarin, Cantonese, Japanese, and Korean were already correct, standard readings.

**Incidental character-page fix**: while researching, found `characters/持 (char).md`'s own `vietnamese` field was missing trì — the exact reading appearing in kiên trì and other common compounds like 保持 (bảo trì, "maintain") — despite listing three other readings (rì, chày, chiì). Added trì to the character's own reading list.

No `stand_in` relationship applies (堅's own is 堅硬, 持's own is bare 持). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄍㄝㄋㄉㄧ` unique to this file). **Incidental fixes**: reformatted `characters/堅.md`'s bare `[[堅持]]` entry to ruby form; added a missing `## Words` entry to `characters/持 (char).md` (had none for this word at all).

### 2026-07-23, iteration 141 — [[words/増加|増加]]

Nineteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**`pos` corrected `性詞`→`事詞`**, matching this word's primary use as a verb ("to increase"). Filled a previously-blank `vietnamese` with tăng gia, a real Sino-Vietnamese word with a dedicated Wiktionary entry (verified via search).

**Incidental character-page fix**: while researching, found `characters/増.md`'s own `vietnamese` field held `tâng`, apparently a typo (missing diacritic) for the correct reading `tăng` — corrected on the character page directly.

Notable `stand_in` relationship: `characters/増.md`'s own `stand_in` points *to this word* (増加), another bound-morpheme case like several earlier this sweep. `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄐㄜㄫㄍㄚ` unique to this file). **Incidental fixes**: added a missing `## Words` section to `characters/増.md` (had none at all); added a missing `## Words` entry to `characters/加.md` (had no entry for this word at all).

### 2026-07-23, iteration 142 — [[words/声調|声調]]

Twentieth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Comma-dump untangled, with a likely typo corrected**: `vietnamese` previously held `hanh điệu, giọng, thanh` — giọng/thanh are separate native words for "voice/tone" generally, not the specific compound, and hanh điệu appears to be a typo (missing the initial "t") for thanh điệu, the genuine, standard Vietnamese linguistics term for "tone" (confirmed via search — has its own Wikipedia article). Kept only thanh điệu. Filled a previously-blank `pos` (名詞).

No `stand_in` relationship applies (声's own is 発声, 調's own is 調整). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄙㄧㄫㄐㄨㄛ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/調.md` (`characters/声.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 143 — [[words/変成|変成]]

Twenty-first word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `変`/`成`, but the actual files are `変 (char).md`/`成 (char).md`. Filled a previously-blank `vietnamese` with biến thành, a real, extremely common Sino-Vietnamese word (verified via search).

**Incidental character-page fix**: `characters/変 (char).md`'s own `vietnamese` field was entirely empty despite biến being the standard reading (biến hóa, biến đổi) — added it (also caught and removed a duplicate `vietnamese:` YAML key left over from the edit).

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (`characters/変 (char).md` is `true`, `characters/成 (char).md` is `false` → compound `false`).

No homophones (`注音: ㄅ⼶ㄋㄙㄧㄫ` unique to this file). **Incidental fixes**: reformatted `characters/変 (char).md`'s bare `[[変成]]` entry to ruby form; added a missing `## Words` entry to `characters/成 (char).md` (had none for this word at all).

### 2026-07-23, iteration 144 — [[words/外国|外国]]

Twenty-second word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `pos` (名詞). All cross-linguistic fields were already correct, standard readings (mandarin wàiguó, cantonese ngoi6 gwok3, japanese がいこく, korean 외국, vietnamese ngoại quốc) — no bugs found.

No `stand_in` relationship applies (外's own is 外部, 国's own is 国家). `kwin: false` already correct per the AND-rule (both individually `false`).

Two false-positive homophones ruled out: `外国語`'s `注音` (`⺢ㄧㄍㄛㄎ·⼄`) and `外国人`'s `注音` (`⺢ㄧㄍㄛㄎㄋㄧㄋ`) both begin with this word's exact string, but both are longer superset compounds (外国+語, 外国+人), not genuine homophones. Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 145 — [[words/多少|多少]]

Twenty-third word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `多`, but the actual file is `多 (char).md`. Confirmed the file's existing note about a planned sibling word 多少様 (for the interrogative "how much/many" sense, not yet created) is consistent with this word's own noun sense "amount; quantity" — no conflict, nothing to change there.

**Left `vietnamese` genuinely blank**: no dedicated dictionary attestation was found for a standalone compound "đa thiểu" — Vietnamese instead expresses "how much/many" with the entirely native, unrelated bao nhiêu. Left blank rather than fabricate, the same standard as [[各種]]/[[名字]] earlier this sweep.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄉㄜㄙㄛㄨ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 146 — [[words/大声|大声]]

Twenty-fourth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `大`, but the actual file is `大 (char).md`. **Real typo corrected**: `cantonese: daai6 seng1` — 声 is never read seng1 (its own character page confirms sing1); corrected to `daai6 sing1`.

Filled a previously-blank `vietnamese` with đại thanh, attested in the Hán Nôm dictionary (verified via search), more literary/classical than the everyday native nói to/lớn tiếng.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄉㄚㄧㄙㄧㄫ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 147 — [[words/大学|大学]]

Twenty-fifth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss corrected — a real content bug**: `english` previously listed only "Great Learning" (the Confucian classic), but this word's own leftover note revealed its primary living use is the abbreviated form of "university" used inside institution names (e.g. 東京大学, "Tokyo University") — the standalone generic noun "university" instead belongs to the fuller sibling word [[大学校]] (whose own note says "abbr 大学"). Reordered the gloss to lead with the university sense, kept "Great Learning" as secondary, and confirmed the separate book translation page [[translation/大学 (book)]] already exists for that specific sense. Propagated the corrected gloss to both constituent characters' existing backlinks (`characters/学.md`, `characters/大 (char).md`), which had inherited the old incomplete gloss.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: true` already correct per the AND-rule (both individually `true`). Mandarin, Cantonese, Japanese, Korean, and Vietnamese were all already correct.

Two false-positive homophones ruled out: `大学生` and `大学校` both begin with this word's exact `注音` string but are longer superset compounds, not genuine homophones.

### 2026-07-23, iteration 148 — [[words/大家|大家]]

Twenty-sixth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Major content bug corrected**: `english` previously listed only "noble, lord, lady, gentleman," entirely missing this word's actual HSK-1-relevant sense — in Mandarin/Cantonese, 大家 is an extremely common grammaticalized pronoun for "everyone; everybody" (大家好!). Corrected the primary gloss and `pos` (名詞→代詞, pronoun).

**A striking four-way cross-linguistic divergence documented, not forced into agreement**: verified via search that the same two characters mean something different in each language — Mandarin/Cantonese "everyone"; Japanese おおや "landlord" (a different reading, たいか, means "master/authority," neither means "everyone"); Korean 대가 "master; distinguished expert"; and Vietnamese đại gia, modern slang for "tycoon; wealthy businessperson." Left `vietnamese` blank rather than force đại gia into an "everyone" gloss it doesn't carry — Vietnamese expresses "everyone" with the entirely native, unrelated mọi người. Kept the Japanese/Korean fields as their own genuine readings, documented as unrelated senses rather than silently implying they mean "everyone" too. Fixed the missing `(char)` suffix on 大 in `characters:`.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: true` already correct per the AND-rule (both individually `true`).

No genuine homophones (`注音: ㄉㄚㄧㄍㄚ` — five false-positive prefix/suffix-substring matches ruled out via exact comparison: 大江/大綱/大蛤/大概/大家族 all differ in their final syllable or are longer). **Incidental fixes**: updated `characters/大 (char).md`'s stale backlink gloss to match the corrected sense; added a missing `## Words` entry to `characters/家.md` (had none for this word at all).

### 2026-07-23, iteration 149 — [[words/夫人|夫人]]

Twenty-seventh word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `羅馬字: bunin` didn't match this word's own `注音`/`諺文` (ㄈㄜㄋㄧㄋ/쁘닌) at all — corrected to `fǝnin`, matching `characters/夫 (char).md`'s own stored reading (fǝ) + 人's own (nin). **Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `夫`, but the actual file is `夫 (char).md`.

All cross-linguistic fields (mandarin, cantonese, japanese, korean, vietnamese) were already correct, standard readings for "madam; lady; (someone else's) wife." No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄈㄜㄋㄧㄋ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/夫 (char).md` (`characters/人 (char).md`'s own entry exists but as a bare numbered-list item — left as-is, consistent with that list's own separate structure, not individually ruby-annotated).

### 2026-07-23, iteration 150 — [[words/姑娘|姑娘]]

Twenty-eighth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss broadened**: `english` previously read only "bachelorette," a narrow/misleading gloss — corrected to lead with "girl; young lady," the actual primary, everyday informal-but-polite address term for a young unmarried woman (verified via search).

Filled previously-blank `korean` (고낭, a real dictionary word confirmed via search) and `vietnamese` (cô nương, a real, well-attested term especially familiar from wuxia/kiếm hiệp novel translations). Confirmed Japanese クーニャン is a genuine direct katakana loanword from Mandarin itself (not a native kanji reading) — kept as-is, noted it also has a secondary, unrelated pop-culture sense as a cocktail name in Hokkaido.

Filled a previously-missing `kwin` — computed `true` per the AND-rule (both `characters/姑.md` and `characters/娘 (char).md` individually `true`). No `stand_in` relationship applies (姑's own is 姑母, 娘's own is bare 娘).

No homophones (`注音: ㄍㄛㄋㄚㄫ` unique to this file). **Incidental fixes**: reformatted `characters/姑.md`'s bare `[[姑娘]]` entry to ruby form; added a missing `## Words` section to `characters/娘 (char).md` (had none at all).

### 2026-07-23, iteration 151 — [[words/媽媽|媽媽]]

Twenty-ninth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Major content bug corrected**: `english` previously read "sweet little maid servant," entirely unrelated to this word's actual meaning — corrected to "mom; mother; mama," matching Mandarin's extremely common, basic HSK-1 sense (`characters/媽.md`'s own Words backlink already correctly said "mama; mom," confirming the word-level field had simply gone stale/wrong independently).

Researched and confirmed Korean 마마 is a real, if rare/archaic and formal-register, Sino-Korean reading for "mom" — modern everyday Korean uses native 엄마 instead, and 마마 today is more commonly encountered in its unrelated historical senses ("Your Majesty," archaic "smallpox"). Left Japanese blank: Japanese uses the katakana loanword ママ or native お母さん, not a kanji compound from 媽 (表外字, outside the standard character set) — no genuine kanji word found.

`kwin: true` already correct (媽 reduplicated, individually `kwin: true`). 媽's own `stand_in` points to a placeholder (名専字), not here.

No homophones (`注音: ㄇㄚㄇㄚ` unique to this file). `characters/媽.md`'s own backlink was already correctly ruby-formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 152 — [[words/学校|学校]]

Thirtieth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin xuéxiào, cantonese hok6 haau6, japanese がっこう, korean 학교, vietnamese trường học) — no bugs found. Added the entirely-missing `## Notes` section.

Notable `stand_in` relationship: `characters/校.md`'s own `stand_in` points *to this word* (学校), another bound-morpheme case like several earlier this sweep; 学's own points elsewhere (学習). `kwin: false` already correct per the AND-rule (`characters/学.md` is `true`, `characters/校.md` is `false` → compound `false`).

Two false-positive homophones ruled out: `小学校` and `大学校` both begin with this word's exact `注音` string but are longer superset compounds (小/大 + 学校), not genuine homophones. Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

**Pool refreshed**: 学校 was the last word in the previous batch. Re-ran the never-perfected HSK-1 query. Next: 学習, 学院, 孩子, 安静, 完全, 実践, 客気, 宴会, 容易, 将来, 展覧, 工人, 工作, 工業, 希望, 常常, 帽子, 幸福, 幹部, 建設, 弟弟, 影響, 復習, 忽然, 思想, 情況, 愉快, 意思, 意見, 愛人, ...

### 2026-07-23, iteration 153 — [[words/学習|学習]]

First word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin xuéxí, cantonese hok6 zaap6, japanese がくしゅう, korean 학습, vietnamese học tập) — no bugs found. Added the entirely-missing `## Notes` section.

Notable `stand_in` relationship: `characters/学.md`'s own `stand_in` points *to this word* (学習), the same relationship referenced throughout this sweep's earlier 学-compound entries; 習's own points elsewhere (練習). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄏㄚㄎㄙㄧㄆ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/習.md` (`characters/学.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 154 — [[words/学院|学院]]

Second word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin xuéyuàn, cantonese hok6 jyun6-2, japanese がくいん, korean 학원, vietnamese học viện) — no bugs found. Noted Korean 학원 specifically denotes a private cram school/after-school academy in modern usage, a narrower but consistent sense. Added the entirely-missing `## Notes` section.

No `stand_in` relationship applies (学's own is 学習, 院's own is 院落). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄏㄚㄎ·⼔ㄋ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/院.md` (`characters/学.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 155 — [[words/孩子|孩子]]

Third word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss broadened**: `english` previously read only "baby; infant" — corrected to "child; kid(s)," matching the actual HSK-1 sense (children of any age, infancy through teens, and even "my child" for an adult offspring).

**Comma-dump corrected to the genuine compositional reading**: `korean: 어린이, 아이` held two unrelated native Korean words for "child," neither a reading of 孩子 itself. Replaced with 해자, the real, narrow (verified via search: "a child of two to three years old") Sino-Korean compositional reading — which also happens to be an exact homophone of the far more common, unrelated word 해자 ("moat"), a genuine cross-linguistic curiosity, not an error. Filled `vietnamese` with hài tử, a real Sino-Vietnamese word with a dedicated dictionary entry (verified via search); the everyday native equivalent is trẻ con.

Filled a previously-missing `kwin` — computed `false` per the AND-rule (`characters/孩.md` is `kwin: true`, `characters/子.md` is `kwin: false` → compound `false`). Notable `stand_in` relationship: `characters/孩.md`'s own `stand_in` points *to this word* (孩子), another bound-morpheme case like several earlier this sweep.

No homophones (`注音: ㄏㄚㄧㄐㄜ` unique to this file). **Incidental fixes**: added a missing `## Words` section to `characters/孩.md` (had none at all); reformatted `characters/子.md`'s bare `[[孩子]]` entry (with the old wrong gloss) to ruby form with the corrected gloss.

### 2026-07-23, iteration 156 — [[words/安静|安静]]

Fourth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin ānjìng, cantonese on1 zing6, japanese あんせい, korean 안정, vietnamese yên tỉnh) — no bugs found. No `stand_in` relationship applies (安's own is 平安, 静's own is 静寂). `kwin: true` already correct per the AND-rule (both individually `true`).

**Formalized an already-known homophone**: the file already had an informal `[!warning]` note about [[安定]] ("stable"), but with the wrong callout syntax and positioned before the meta-bind-embed. Verified all three fields match exactly ('anjeng/안정/ㄚㄋㄐㄝㄫ) and reformatted into a proper `>[!warning] Homophones` callout in the correct position. **Incidental sibling-word fix**: `words/安定.md`'s own reciprocal note (also informally formatted, `# Notes\n- Homophones: ...`) was fixed to match.

**Incidental fixes**: added missing `## Words` entries to both `characters/安.md` and `characters/静.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 157 — [[words/完全|完全]]

Fifth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `全`, but the actual file is `全 (char).md`. All cross-linguistic fields were already correct, standard readings (mandarin wánquán, cantonese jyun4 cyun4, japanese かんぜん, korean 완전, vietnamese hoàn toàn) — no bugs found (double-checked the Cantonese carefully against a suspected pattern from earlier iterations, but jyun4 cyun4 is genuinely correct here).

No `stand_in` relationship applies (完's own is 完成, 全's own is bare 全). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄏ⺢ㄋㄐ⼔ㄋ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 158 — [[words/実践|実践]]

Sixth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with thực tiễn, a real, common Sino-Vietnamese word with a dedicated Wiktionary entry (verified via search).

**Incidental character-page fix**: `characters/実.md`'s own `vietnamese` field was entirely empty despite thực being the standard reading (as in thực tiễn, thực tế) — added it (and caught/removed a duplicate `vietnamese:` YAML key left over from the edit, the same pattern as `変 (char).md` earlier this sweep).

Notable `stand_in` relationship: `characters/践.md`'s own `stand_in` points *to this word* (実践), another bound-morpheme case. `kwin: false` already correct per the AND-rule (`characters/実.md` is `true`, `characters/践.md` is `false` → compound `false`).

No homophones (`注音: ㄙㄧㄊㄐㄝㄋ` unique to this file). Both constituent characters' `## Words` backlinks were already present and correctly formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 159 — [[words/客気|客気]]

Seventh word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**A striking cross-linguistic sense divergence found and documented, not forced into agreement**: `english` previously read only "polite" — verified via search that this is indeed correct for Mandarin kèqì/Cantonese haak3 hei3 (and confirmed Vietnamese khách khí matches this sense too), but Japanese かっき and Korean 객기 mean something entirely different: "rash impulsiveness; hot-blooded bravado; foolhardy pride" (e.g. 객기 부리다, "act recklessly out of misplaced pride"). Broadened the gloss to document both senses explicitly rather than silently implying Japanese/Korean also mean "polite." Propagated the corrected/clarified gloss to both constituent characters' existing backlinks.

No `stand_in` relationship applies (客's own is 客人, 気's own is bare 気). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄎㄚㄎㄎㄧㄜ` unique to this file). **Incidental fix**: reformatted `characters/客.md`'s bare `[[客気]]` entry to ruby form (`characters/気 (char).md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 160 — [[words/宴会|宴会]]

Eighth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `cantonese: jin3 qui6` — 会 is never read qui6 (its own character page confirms wui6); corrected to `jin3 wui6`.

**Comma-dump untangled**: `korean: 연회, 잔치` — 연회 is the compound's own Sino-Korean reading, while 잔치 is an unrelated native Korean word for "feast, party" (coincidentally also 宴's own `korean_native` gloss). Kept only 연회.

Filled a previously-blank `vietnamese` with yến hội, a Hán-Việt compound documented in Hán Nôm dictionaries (verified via search); the more common everyday Vietnamese equivalent is yến tiệc. Filled a previously-blank `pos` (名詞) and a previously-missing `kwin` (computed `false` per the AND-rule, both characters individually `false`).

Notable `stand_in` relationship: `characters/宴.md`'s own `stand_in` points *to this word* (宴会), another bound-morpheme case like several earlier this sweep.

No homophones (`注音: ㄝㄋㄏ⼔` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/宴.md` and `characters/会 (char).md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 161 — [[words/容易|容易]]

Ninth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Comma-dump untangled**: `korean` previously held `용이, 쉽다` — 용이 is the compound's own Sino-Korean reading, while 쉽다 is an unrelated native Korean verb meaning "to be easy." Kept only 용이. Vietnamese dung dị was already correct.

**Formalized an already-known homophone**: the file already had informal prose noting a collision with [[溶液]] ("solution, chemistry"). Verified all three fields match exactly ('yong'yeg/용역/⼄ㄫ·⼶ㄎ) and converted to a proper `>[!warning] Homophones` callout. **Incidental sibling-word fix**: `words/溶液.md`'s own reciprocal note was similarly informal — reformatted to match.

Filled a previously-missing `kwin` — computed `true` per the AND-rule (both `characters/容 (char).md` and `characters/易.md` individually `true`). Notable `stand_in` relationship: `characters/易.md`'s own `stand_in` points *to this word* (容易), another bound-morpheme case.

No other homophones. **Incidental fixes**: added missing `## Words` entries to both `characters/容 (char).md` and `characters/易.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 162 — [[words/将来|将来]]

Tenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `将`/`来`, but the actual files are `将 (char).md`/`来 (char).md`. All cross-linguistic fields were already correct, standard readings (mandarin jiānglái, cantonese zoeng1 loi4, japanese しょうらい, korean 장래, vietnamese tương lai) — no bugs found.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (`characters/将 (char).md` is `false`, `characters/来 (char).md` is `true` → compound `false`).

No homophones (`注音: ㄐ⺢ㄫㄌㄚㄧ` unique to this file). **Incidental fixes**: reformatted `characters/将 (char).md`'s bare `[[将来]]` entry to ruby form; added a missing `## Words` entry to `characters/来 (char).md` (had none for this word at all).

### 2026-07-23, iteration 163 — [[words/展覧|展覧]]

Eleventh word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `cantonese` with zin2 laam5, matching each character's own stored reading. Mandarin, Japanese, Korean, and Vietnamese were already correct, standard readings.

No `stand_in` relationship applies (展's own is 伸展, 覧's own is 観覧). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄐㄝㄋㄌㄚㄇ` unique to this file). **Incidental fixes**: reformatted `characters/展.md`'s bare `[[展覧]]` entry to ruby form; added a missing `## Words` entry to `characters/覧.md` (had none for this word at all).

### 2026-07-23, iteration 164 — [[words/工人|工人]]

Twelfth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin gōngrén, cantonese gung1 jan4, japanese こうじん, korean 공인, vietnamese công nhân) — no bugs found. Confirmed via search that Japanese こうじん genuinely means "craftsman; artisan" and Korean 공인 genuinely means "craftsman; laborer" — both real, attested readings.

**Genuine homophone-across-different-hanja confirmed, not an error**: Korean 공인 (工人) is coincidentally identical in sound to the far more common, entirely unrelated compounds 공인(公認, "official recognition") and 공인(公人, "public figure") — verified via search that all three are distinct, real words, the same recurring cross-linguistic pattern documented several times this sweep.

No `stand_in` relationship applies (工's own is 工作, 人's own is bare 人). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄍㄛㄫㄋㄧㄋ` unique to this file). **Incidental fix**: added a missing `## Words` section and entry to `characters/工.md` (had no heading or entry at all; `characters/人 (char).md`'s own entry exists but as a bare numbered-list item, left as-is per the same precedent as [[夫人]] earlier this sweep).

### 2026-07-23, iteration 165 — [[words/工作|工作]]

Thirteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**`pos` corrected `性詞`→`事詞`**, matching this word's primary use as a verb/action-noun ("to work; job"). Reformatted Cantonese with a space (`gung1zok3`→`gung1 zok3`). Filled a previously-blank `vietnamese` with công tác, a real word documented in Hán Nôm dictionaries (verified via search).

**Formalized an already-known homophone**: the file already had informal prose noting a collision with [[公爵]] ("duke"). Verified all three fields match exactly (gongjag/공작/ㄍㄛㄫㄐㄚㄎ) and converted to a proper `>[!warning] Homophones` callout. **Incidental sibling-word fix**: `words/公爵.md`'s own reciprocal note was similarly informal — reformatted to match.

Notable `stand_in` relationship: `characters/工.md`'s own `stand_in` points *to this word* (工作), another bound-morpheme case. `kwin: true` already correct per the AND-rule (both individually `true`).

**Incidental fixes**: added missing `## Words` entries to both `characters/工.md` and `characters/作 (char).md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 166 — [[words/工業|工業]]

Fourteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `業`, but the actual file is `業 (char).md`. All cross-linguistic fields were already correct, standard readings (mandarin gōngyè, cantonese gung1 jip6, japanese こうぎょう, korean 공업, vietnamese công nghiệp) — no bugs found.

No `stand_in` relationship applies (工's own is 工作, 業's own is bare 業). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄍㄛㄫㄝㄆ` unique to this file). **Incidental fixes**: reformatted `characters/工.md`'s bare `[[工業]]` entry to ruby form; added a missing `## Words` entry to `characters/業 (char).md` (had none for this word at all).

### 2026-07-23, iteration 167 — [[words/希望|希望]]

Fifteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-missing `kwin` — computed `true` per the AND-rule (both `characters/希.md` and `characters/望.md` individually `true`). All cross-linguistic fields were already correct, standard readings (mandarin xīwàng, cantonese hei1 mong6, japanese きぼう, korean 희망, vietnamese hy vọng) — no bugs found.

Notable `stand_in` relationship: `characters/望.md`'s own `stand_in` points *to this word* (希望), another bound-morpheme case; 希's own points elsewhere (希有).

No homophones (`注音: ㄏㄧㄜㄇㄚㄫ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/希.md` and `characters/望.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 168 — [[words/常常|常常]]

Sixteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bugs corrected**: `japanese` previously read `つねづね , 常々`, redundantly repeating the kanji spelling inside the reading field itself — trimmed to just つねづね (also validly read じょうじょう, verified via search). `korean` previously held 자주, a native Korean word for "often" — not a reading of 常常 itself — corrected to 상상, the genuine, if less common/formal-register, Sino-Korean compositional reading (verified via search, meaning "always"); 자주/항상 remain the everyday native alternatives.

Reformatted Cantonese with a space (`seong4seong4`→`seong4 seong4`). Filled a previously-blank `pos` (修飾語, adverb/modifier). Vietnamese thường thường was already correct.

No `stand_in` relationship applies (常's own is 日常). `kwin: false` already correct per the AND-rule (常 individually `false`, reduplicated).

No homophones (`注音: ㄙ⼘ㄫㄙ⼘ㄫ` unique to this file). `characters/常.md`'s own backlink was already correctly ruby-formatted — no incidental character-page fixes needed.

### 2026-07-23, iteration 169 — [[words/帽子|帽子]]

Seventeenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Comma-dump narrowed**: `vietnamese` previously held `mũ, nón` — nón specifically denotes the conical Asian hat (a distinct, narrower item), not a general reading of 帽子. No dedicated dictionary attestation was found for a standalone compound "mạo tử," so kept only mũ, the genuine Nôm/native reading of 帽 itself.

Notable `stand_in` relationship: `characters/帽.md`'s own `stand_in` points *to this word* (帽子), another bound-morpheme case. `kwin: false` already correct per the AND-rule (both characters individually `false`). Mandarin, cantonese, japanese, and korean were already correct, standard readings.

No homophones (`注音: ㄇㄚㄨㄐㄜ` unique to this file). **Incidental fixes**: added a missing `## Words` entry to `characters/帽.md`; reformatted `characters/子.md`'s bare `[[帽子]]` entry to ruby form.

### 2026-07-23, iteration 170 — [[words/幸福|幸福]]

Eighteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `福`, but the actual file is `福 (char).md`. All cross-linguistic fields were already correct, standard readings (mandarin xìngfú, cantonese hang6 fuk1, japanese こうふく, korean 행복, vietnamese hạnh phúc) — no bugs found.

No `stand_in` relationship applies (幸's own is 幸運, 福's own is bare 福). `kwin: false` already correct per the AND-rule (both individually `false`).

No homophones (`注音: ㄏㄚㄫㄈㄨㄎ` unique to this file). **Incidental fix**: added a missing `## Words` section to `characters/福 (char).md` (had none at all; `characters/幸.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 171 — [[words/幹部|幹部]]

Nineteenth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `部`, but the actual file is `部 (char).md`. All cross-linguistic fields were already correct, standard readings (mandarin gànbù, cantonese gon3 bou6, japanese かんぶ, korean 간부, vietnamese cán bộ) — no bugs found.

No `stand_in` relationship applies (幹's own is 主幹, 部's own is bare 部). `kwin: false` already correct per the AND-rule (`characters/幹.md` is `true`, `characters/部 (char).md` is `false` → compound `false`).

No homophones (`注音: ㄍㄚㄋㄅㄛㄨ` unique to this file). **Incidental fixes**: reformatted `characters/部 (char).md`'s bare `[[幹部]]` entry to ruby form; added a missing `## Words` section to `characters/幹.md` (had none at all).

### 2026-07-23, iteration 172 — [[words/建設|建設]]

Twentieth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real bug corrected**: `korean` previously held only `건`, missing the second syllable entirely — corrected to `건설`, matching each character's own stored reading. **`kwin` bug corrected `false`→`true`**: both `characters/建.md` and `characters/設.md` are individually `kwin: true`, so the AND-rule requires the compound to be `true` — the previously stored `false` directly contradicted this.

Filled a previously-blank `vietnamese` with kiến thiết, a real Sino-Vietnamese word with a dedicated Wiktionary entry (verified via search) — more formal/large-scale than everyday xây dựng.

Notable double bound-morpheme case: both `characters/建.md`'s and `characters/設.md`'s own `stand_in` point to this word (建設) — neither character ever appears independently outside this compound.

No homophones (`注音: ㄍㄝㄋㄙㄝㄊ` unique to this file). **Incidental fixes**: reformatted `characters/建.md`'s bare `[[建設]]` entry to ruby form; added a missing `## Words` entry to `characters/設.md` (had none for this word at all).

### 2026-07-23, iteration 173 — [[words/弟弟|弟弟]]

Twenty-first word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss corrected**: `english` previously read "little bitty brother," an overly informal gloss that had leaked the vault's own design commentary into the dictionary field itself — corrected to the plain, standard "younger brother." The existing prose note explaining that the *reduplicated Dan'a'yo form* is deliberately cuter/more diminutive than plain Mandarin 弟弟 (an ordinary, neutral word) was preserved and clarified.

**Wrong-word conflation corrected**: `korean: 아우` was `characters/弟 (char).md`'s own native-Korean gloss for the bare character, not a reading of the reduplicated compound 弟弟. No attestation was found for a standalone reduplicated Sino-Korean reading (제제) — Korean instead uses 남동생/동생/아우 (native or hybrid terms) — left blank rather than guess.

No `stand_in` relationship applies (弟's own is bare 弟). `kwin: false` already correct per the AND-rule (弟 individually `false`, reduplicated).

No homophones (`注音: ㄉㄝㄉㄝ` unique to this file). **Incidental fix**: updated `characters/弟 (char).md`'s stale backlink gloss to match the corrected sense.

### 2026-07-23, iteration 174 — [[words/影響|影響]]

Twenty-second word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `vietnamese` with ảnh hưởng, a real Sino-Vietnamese word with a dedicated Wiktionary entry (verified via search) — the metaphor mirrors this compound's own shadow-and-echo etymology. Mandarin, Cantonese, Japanese, and Korean were already correct, standard readings.

No `stand_in` relationship applies (影's own is 陰影, 響's own is 反響). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ⼶ㄫㄏ⼘ㄫ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/響.md` (`characters/影.md`'s own entry already existed, correctly formatted).

### 2026-07-23, iteration 175 — [[words/復習|復習]]

Twenty-third word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Real typo corrected**: `cantonese: fuk1 zaap6` — 復 is never read fuk1 (its own character page confirms fuk6); corrected to `fuk6 zaap6`. Filled a previously-blank `vietnamese` with phục tập, documented in a Hán Nôm dictionary (verified via search); the common everyday synonym is ôn tập.

No `stand_in` relationship applies (復's own is 回復, 習's own is 練習). `kwin: false` already correct per the AND-rule (`characters/復.md` is `false`, `characters/習.md` is `true` → compound `false`).

No homophones (`注音: ㄅㄨㄎㄙㄜㄆ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/復.md` and `characters/習.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 176 — [[words/忽然|忽然]]

Twenty-fourth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing-`(char)`-suffix bug fixed**: `characters:` listed bare `然`, but the actual file is `然 (char).md`.

**Left `vietnamese` honestly blank**: no dedicated dictionary attestation was found for a standalone compound "hốt nhiên" — Vietnamese instead expresses "suddenly" with bỗng nhiên/đột nhiên, entirely different native constructions. Left blank rather than fabricate.

Notable `stand_in` relationship: `characters/忽.md`'s own `stand_in` points *to this word* (忽然), another bound-morpheme case; 然's own is bare 然. `kwin: false` already correct per the AND-rule (`characters/忽.md` is `true`, `characters/然 (char).md` is `false` → compound `false`).

One false-positive homophone ruled out: `忽然様`'s `注音` (`ㄏㄛㄊㄋ⼶ㄋ⼘ㄫ`) begins with this word's exact string but is a longer superset compound, not a genuine homophone.

**Incidental fixes**: reformatted `characters/忽.md`'s bare `[[忽然]]` entry to ruby form; added a missing `## Words` entry to `characters/然 (char).md` (had none for this word at all).

### 2026-07-23, iteration 177 — [[words/思想|思想]]

Twenty-fifth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

All cross-linguistic fields were already correct, standard readings (mandarin sīxiǎng, cantonese si1 soeng2, japanese しそう, korean 사상, vietnamese tư tưởng) — no bugs found.

**Recurring Sino-Xenic homophone cluster documented**: verified via search that Korean 사상 is a rich multi-way homophone — besides 思想 ("thought/ideology"), the same syllables also spell 死傷 ("death and injury," casualties), 史上 ("in history"), and 事象 ("phenomena"). Joins the same recurring pattern as [[思考]]'s own 사고 cluster documented earlier this sweep.

Notable `stand_in` relationship: `characters/想.md`'s own `stand_in` points *to this word* (思想); 思's own points elsewhere (思考). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ㄙㄚㄙㄚㄫ` unique to this file). **Incidental fixes**: reformatted `characters/思.md`'s bare `[[思想]]` entry to ruby form; added a missing `## Words` entry to `characters/想.md` (had none for this word at all).

### 2026-07-23, iteration 178 — [[words/情況|情況]]

Twenty-sixth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Incorrect alias removed, a real content bug**: `aliases:` previously listed 状況, but that is not an orthographic variant of 情況 — it's a different, unrelated, extremely common word built from a different first character (状/狀 "shape, form" instead of 情 "emotion"), confirmed distinct by `characters/況.md`'s own `korean_native` gloss (상황, i.e. 狀況's own reading, not this word's 정황). Removed from `aliases` since that field is for true character-variant forms, not merely similar-meaning words.

Filled a previously-blank `vietnamese` with tình huống, a real Sino-Vietnamese word with a dedicated Wiktionary entry (verified via search). Mandarin, Cantonese, Japanese, and Korean were already correct.

Notable `stand_in` relationship: `characters/況.md`'s own `stand_in` points *to this word* (情況); 情's own points elsewhere (感情). `kwin: false` already correct per the AND-rule (`characters/情.md` is `false`, `characters/況.md` is `true` → compound `false`).

No homophones (`注音: ㄑㄧㄫㄏ⺢ㄫ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/情.md` and `characters/況.md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 179 — [[words/愉快|愉快]]

Twenty-seventh word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `pos` (性詞) and `vietnamese` (du khoái, confirmed via search against character-level Hán Nôm dictionary entries). Confirmed via search that Cantonese's two listed tone variants (jyu4 faai3, jyu6 faai3) are both genuinely documented pronunciations (CantoDict lists both), not a comma-dump error.

Notable `stand_in` relationship: `characters/愉.md`'s own `stand_in` points *to this word* (愉快). `kwin: true` already correct per the AND-rule (both individually `true`).

No homophones (`注音: ⼜ㄇㄎ⺢ㄧ` unique to this file). **Incidental fixes**: added missing `## Words` entries to both `characters/愉.md` and `characters/快 (char).md` (neither had a backlink for this word at all).

### 2026-07-23, iteration 180 — [[words/意思|意思]]

Twenty-eighth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

Filled a previously-blank `pos` (名詞), `vietnamese` (ý tứ, a real word with a dedicated Wiktionary entry, verified via search), and a previously-missing `kwin` (computed `false` per the AND-rule: `characters/意.md` is `kwin: false`, `characters/思.md` is `kwin: true` → compound `false`). Confirmed via search that Cantonese's ji3 si3 (rather than ji3 si1) is a genuine, documented changed-tone (變音) pronunciation, not an error.

No `stand_in` relationship applies (意's own is 意味, 思's own is 思考).

Two false-positive homophones ruled out: `滋生`/`医生` both begin with a similar string but neither exactly matches this word's `注音` (both have an extra syllable), not genuine homophones.

**Incidental fixes**: reformatted `characters/意.md`'s bare `[[意思]]` entry to ruby form; added a missing `## Words` entry to `characters/思.md` (had none for this word at all).

### 2026-07-23, iteration 181 — [[words/意見|意見]]

Twenty-ninth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Gloss corrected**: `english` previously read "express opinion, advize, suggest" (with a typo, "advize"→"advise") and led with a verb-phrase framing — corrected to lead with "opinion; view," this word's actual primary sense as a noun (verified via search: 意見を述べる "to state an opinion"), with the secondary する-verb sense ("to admonish, advise") noted separately. Propagated the corrected gloss to `characters/見 (char).md`'s own backlink, which had inherited the old typo'd version.

Filled a previously-blank `pos` (名詞) and a previously-missing `kwin` (computed `false` per the AND-rule: `characters/意.md` is `kwin: false`, `characters/見 (char).md` is `kwin: true` → compound `false`). Reformatted Cantonese with a space (`ji3gin3`→`ji3 gin3`). No `stand_in` relationship applies (意's own is 意味, 見's own is bare 見).

No homophones (`注音: ㄜㄍ⼶ㄋ` unique to this file). **Incidental fix**: added a missing `## Words` entry to `characters/意.md` (`characters/見 (char).md`'s own entry already existed).

### 2026-07-23, iteration 182 — [[words/愛人|愛人]]

Thirtieth word in the refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**A striking, genuinely important cross-linguistic sense divergence found and documented, not forced into agreement**: `english` previously read only "lover; sweetheart" — verified via search that in mainland Mandarin (HSK-standard usage), 爱人 àirén is the neutral, standard word for "spouse" (a well-known learner trap, distinct from a dating partner or illicit lover); Taiwan/HK Mandarin instead leans "lover." Korean 애인 and Vietnamese người yêu both mean "boyfriend/girlfriend." Japanese あいじん, however, specifically means "mistress; affair partner" (a post-WWII semantic narrowing from an earlier plain "lover" sense) — genuinely risky to conflate with "spouse." Rewrote the gloss to document all four senses explicitly with a warning-style note, rather than silently picking one.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (`characters/愛 (char).md` is `true`, `characters/人 (char).md` is `false` → compound `false`).

One false-positive homophone ruled out: `大人`'s `注音` (`ㄉㄚㄧㄋㄧㄋ`) contains this word's exact string as a suffix, but is a longer, distinct word, not a genuine homophone. **Incidental fix**: added a missing `## Words` entry to `characters/愛 (char).md` (`characters/人 (char).md`'s own entry exists but as a bare numbered-list item, left as-is per the same precedent as [[夫人]]/[[工人]] earlier this sweep).

**Pool refreshed**: re-ran the never-perfected HSK-1 query. Next: 感謝, 態度, 成績, 所以, 所有, 技術, 掌握, 排球, 握手, 改変, 故事, 教室, 教育, 文化, 文学, 文章, 文芸, 新聞, 方便, 方向, 旅行, 日語, 早飯, 昨日, 時候, 時間, 最初, 最後, 最近, 有名.

### 2026-07-23, iteration 183 — [[words/感謝|感謝]]

First word in the fourth refreshed HSK-1 alphabetical pool. Stamped `date-last-perfect: 2026-07-23`.

**Content removed — bad alias**: frontmatter listed `aliases: [慰藉]`. 慰藉 means "solace; consolation/comfort," an entirely unrelated word to 感謝 "thank; appreciate" — not an alternate spelling or written variant of this word. Likely arose from `characters/謝.md` itself listing `藉` as one of its own character-level aliases (a classical variant glyph), conflated into a word-level alias it doesn't actually have. Removed the bogus alias rather than force it into agreement. Also removed a blank `swadesh:` key.

Added the missing `## Notes` section (previously had none) — opening bullet linking both constituent characters, noting `characters/謝.md`'s own `stand_in` points here (bound morpheme), and `kwin: false` already correctly matched the AND-rule (感 `true` × 謝 `false` → `false`).

**Cross-linguistic register divergence documented**: Mandarin 感谢 gǎnxiè and Korean 감사 gamsa are the everyday neutral words for "thank you"; Japanese 感謝 kansha is comparatively formal/deep gratitude, sitting above the far more common casual ありがとう; Vietnamese cảm tạ is likewise formal/literary register, with everyday spoken Vietnamese instead using cảm ơn. Not a bug, a genuine register asymmetry worth flagging.

No homophones (`注音: ㄍㄚㄇㄙ⼘` and `羅馬字: gamsya` both unique). **Incidental fix**: added a missing `## Words` entry to `characters/感.md`; added a missing `## Words` section entirely to `characters/謝.md` (had none).

### 2026-07-23, iteration 184 — [[words/態度|態度]]

Second word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: filled blank `pos` (`名詞`); removed blank `swadesh:` key. Renamed non-canonical `## Etymology` heading to `## Notes` (same recurring fix applied throughout this sweep). Kept the existing `态度` alias — legitimate simplified form.

**Stand-in note applied**: `characters/態.md`'s own `stand_in` field is `態度` (this word) — added the standard phrasing to the opening bullet. (度's own `stand_in` is `程度`, a different word — no note on that side.) `kwin: true` already correct per the AND-rule (both constituents individually `true`).

A clean, directly parallel compound — Mandarin/Cantonese/Japanese/Korean/Vietnamese all mean "attitude, manner, bearing" with no real cross-linguistic divergence to flag. No homophones (`注音: ㄊㄚㄧㄉㄛ` unique). **Incidental fix**: reformatted `characters/態.md`'s existing plain-text 態度 entry into standard ruby form with the stand-in note; added a missing `## Words` entry to `characters/度.md`.

### 2026-07-23, iteration 185 — [[words/成績|成績]]

Third word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: filled blank `pos` (`名詞`); filled blank `vietnamese` with the real, attested Sino-Vietnamese `thành tích` (verified via search — a common, everyday Vietnamese word for grades/records/achievements). Removed blank `swadesh:` key; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`. Kept the existing `成绩` alias — legitimate simplified form.

**Stand-in note applied**: `characters/績.md`'s own `stand_in` field is `成績` (this word) — added the standard phrasing to the opening bullet. (成's own `stand_in` is bare `成` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/成 (char).md` is `false`, `characters/績.md` is `true` → compound `false`).

Mild register/scope observation, not a bug: Korean 성적 and Japanese せいせき lean more specifically toward "(school) grades" in everyday use, while Vietnamese thành tích and Mandarin chéngjì extend a bit more readily to general life/work achievements — same core sense, slightly different typical context. No homophones (`注音: ㄙㄧㄫㄐㄝㄎ` unique). **Incidental fix**: reformatted `characters/成 (char).md`'s existing plain-text 成績 entry into ruby form; added a missing `## Words` section entirely to `characters/績.md` (had none).

### 2026-07-23, iteration 186 — [[words/所以|所以]]

Fourth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: filled blank `pos` (`連接詞`, matching sibling conjunction-words like 或/而/若/与/但); added a previously-missing `kwin` (computed `false` per the AND-rule: `characters/所 (char).md` is `false`, `characters/以 (char).md` is `true` → compound `false`). Removed blank `swadesh:` and empty `aliases: []`.

**Genuine part-of-speech divergence found and documented via search, not forced into agreement**: filled blank `korean` (`소이`) and `vietnamese` (`sở dĩ`), both verified as real, attested words. Mandarin/Cantonese suǒyǐ/so2 ji5 have grammaticalized into an everyday causal conjunction ("so, therefore"). Japanese ゆえん and Korean 소이, however, stayed closer to the compositional literal sense — a noun meaning "the reason (why)," used in a comparatively literary/formal register. Vietnamese sở dĩ sits in between: still common in modern speech, but as a fixed causal frame (sở dĩ ... là vì ...) rather than a plain conjunction.

No `stand_in` relationship applies (both 所's and 以's own `stand_in` point to their bare selves — 所以 is an independent compound). `羅馬字`/`諺文` (`syo'i`/쇼이) checked against sibling 所-compounds: 所在/所有/所謂 all use the same "syo/쇼" spelling for 所's initial syllable (only 所属 uses "sǝ/스" instead) — left as-is, matching the majority existing convention rather than a decision I should make unilaterally. No homophones (`注音: ㄙㄜㄧ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/以 (char).md` (`characters/所 (char).md`'s own entry already existed).

### 2026-07-23, iteration 187 — [[words/所有|所有]]

Fifth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing primary sense found and fixed via search, matching the recurring 大学/大家-style gloss-gap pattern**: `english` previously read only "possess; own" — verified via search that in modern Mandarin/Cantonese, 所有/so2 jau5 has grammaticalized into an everyday determiner meaning "all, every" (所有人 "everyone"), the far more common usage; the literal "possess/own" sense survives mainly in formal/legal registers. Reordered to lead with the determiner sense, keeping "possess; own; ownership" as the secondary formal sense. Filled blank `pos` (`修飾語`, matching sibling determiner-words like [[両]]) and blank `japanese` (`しょゆう`, verified).

**Genuine grammaticalization divergence documented**: Japanese しょゆう, Korean 소유, and Vietnamese sở hữu (verified via search) never developed Mandarin/Cantonese's "all" determiner sense at all — all three remain squarely in the formal "possession; ownership" noun register (所有権/소유권/quyền sở hữu "ownership rights"). Flagged explicitly so a learner doesn't assume "all" carries across languages.

No `stand_in` relationship applies (both 所's and 有's own `stand_in` point to their bare selves). `kwin: false` already correct per the AND-rule (`characters/所 (char).md` is `false`, `characters/有 (char).md` is `true` → compound `false`). Removed blank `swadesh:` and empty `aliases: []`; quoted `hsk_level: "1"`. No homophones (`注音: ㄙㄜ⼜` unique). **Incidental fix**: propagated the corrected gloss to both `characters/所 (char).md`'s and `characters/有 (char).md`'s own backlinks.

### 2026-07-23, iteration 188 — [[words/技術|技術]]

Sixth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `術`, but the actual file is `術 (char).md` — corrected to `"術 (char)"` with proper block indentation (the frontmatter had used an unindented dash-list style). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies — 技's own `stand_in` is `技能` (a different word), 術's own is bare `術` — 技術 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/技.md` is `false`, `characters/術 (char).md` is `true` → compound `false`). A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄍㄨㄧㄙㄨㄊ` unique). **Incidental fix**: reformatted `characters/技.md`'s existing plain-text entry into ruby form; added a missing `## Words` entry to `characters/術 (char).md`.

### 2026-07-23, iteration 189 — [[words/掌握|掌握]]

Seventh word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:` unindented dash list reformatted to standard block form (both entries already correctly named, no `(char)` suffix needed). Filled blank `vietnamese` with the real, attested Sino-Vietnamese `chưởng ác` (verified via search — used e.g. in `chưởng ác binh quyền` "to hold military power"). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Folded a stray unstructured body line ("be in control of," sitting outside any heading) into a proper `## Notes` section.

No `stand_in` relationship applies — 掌's own `stand_in` is `手掌` (a different word), 握's own is `把握` (a different word) — 掌握 is an independent compound. `kwin: true` already correct per the AND-rule (both constituents individually `true`). A clean, directly parallel compound across the whole sphere — "grasp with the palm" extended figuratively to "master, control" everywhere, no cross-linguistic divergence. No homophones (`注音: ㄐㄚㄫㄚㄎ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/掌.md` (`characters/握.md`'s own entry already existed).

### 2026-07-23, iteration 190 — [[words/排球|排球]]

Eighth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:` inline JSON-style array reformatted to standard block form. Removed blank `swadesh:` and empty `aliases: []`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Native-coinage divergence documented, not fabricated**: Vietnamese does not use a Sino-Vietnamese calque of 排球 at all — verified via search that the real, standard modern term is the fully native coinage bóng chuyền ("passing/relay ball"); no attested Sino-Vietnamese alternative is in actual use, so none was invented. Mandarin/Cantonese/Japanese/Korean all directly preserve the Sino compound.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both `characters/排 (char).md` and `characters/球 (char).md` individually `false`). No homophones (`注音: ㄆㄚㄧㄍ⼜` unique). **Incidental fix**: reformatted `characters/排 (char).md`'s existing plain-text entry into ruby form; added a missing `## Words` entry to `characters/球 (char).md` and removed a stray empty bullet point from its existing list.

### 2026-07-23, iteration 191 — [[words/握手|握手]]

Ninth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: removed blank `swadesh:` and empty `aliases: []`. Added the missing `## Notes` section (previously had none).

**Native-coinage divergence documented, not fabricated**: a weak search result offered "ác thủ" as a mechanical Sino-Vietnamese reading, but it could not be independently confirmed as an actually-used Vietnamese word (unlike, e.g., 掌握's genuinely attested "chưởng ác" last iteration) — the real, standard modern Vietnamese term for "shake hands" is the native construction bắt tay ("catch/grasp hand"). Left `vietnamese` blank rather than fabricate a technically-derivable but unattested reading.

No `stand_in` relationship applies — 握's own `stand_in` is `把握` (a different word), 手's own is bare `手` — 握手 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/握.md` is `true`, `characters/手 (char).md` is `false` → compound `false`). No homophones (`注音: ㄚㄎㄙ⼜` unique). Both `characters/握.md` and `characters/手 (char).md` already had correct `## Words` backlink entries — no incidental fix needed on either.

### 2026-07-23, iteration 192 — [[words/改変|改変]]

Tenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `改`/`変`, but the actual files are `改 (char).md`/`変 (char).md` — corrected both with proper block indentation. Fixed a stray-space typo in `cantonese` (`"goi2 bin 3"`→`"goi2 bin3"`). Filled blank `vietnamese` with the real, attested `cải biến` (verified via search — a genuine dictionary entry, distinct from the similarly-spelled `cải biên` "adapt/edit a work"). Reformatted `aliases` inline array to block form (kept both `改變`/`改变` — legitimate traditional/simplified variants). Removed blank `swadesh:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: true` already correct per the AND-rule (both individually `true`). A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄍㄚㄧㄅ⼶ㄋ` unique). **Incidental fix**: added a missing `## Words` section entirely to `characters/変 (char).md` (`characters/改 (char).md`'s own entry already existed).

### 2026-07-23, iteration 193 — [[words/故事|故事]]

Eleventh word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `事`, but the actual file is `事 (char).md` — corrected. Filled blank `vietnamese` with the real, attested `cố sự` (verified via search).

**Genuine register/scope divergence found via search and documented, not forced into agreement**: Mandarin gùshi/Cantonese gu3 si6 is the broad everyday word for "story" (讲故事 "tell a story," 故事书 "storybook"). Japanese こじ, Korean 고사, and Vietnamese cố sự, however, all narrow the sense to specifically an *old/classical* anecdote or historical precedent (故事成語/고사성어, idioms coined from such anecdotes) — not a general word for "story," which Japanese/Korean instead express with native words (話/이야기). Flagged so a learner doesn't assume "story" carries the same everyday breadth outside Mandarin/Cantonese.

No `stand_in` relationship applies — 故's own `stand_in` is `緣故` (a different word), 事's own is bare `事` — 故事 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/故.md` is `true`, `characters/事 (char).md` is `false` → compound `false`). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. No homophones (`注音: ㄍㄛㄐㄧ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/故.md`; propagated the corrected divergence-aware gloss to `characters/事 (char).md`'s own backlink.

### 2026-07-23, iteration 194 — [[words/教室|教室]]

Twelfth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Content removed — spurious second reading**: `mandarin: "jiàoshì, jiàoshǐ"` — checked against `characters/教.md` (mandarin `jiào` only) and `characters/室.md` (mandarin `shì` only); no real second pronunciation "jiàoshǐ" exists for this word. Removed the bogus alternate reading, keeping just `jiàoshì`. Also fixed `japanese` (`きょーしつ`→`きょうしつ`, standard hiragana long-vowel spelling, matching sibling words 教育/教師; the ー-based spelling appears to be a recurring typo also seen on [[教員]], left untouched this iteration since it's a different word).

**Native-coinage divergence documented, not fabricated**: a weak, effectively circular search result offered "giáo thất" as a mechanical Sino-Vietnamese reading, but it could not be independently confirmed as an actually-used word — the real, standard modern Vietnamese term for "classroom" is the native construction lớp học/phòng học. Left `vietnamese` blank rather than fabricate an unattested reading.

No `stand_in` relationship applies — 教's own `stand_in` is `教授` (a different word), 室's own is `房室` (a different word) — 教室 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/教.md` is `false`, `characters/室.md` is `true` → compound `false`). Reformatted `aliases` inline array to block form (kept `敎室`, a legitimate variant-glyph form matching 教's own `敎` alias). Removed blank `swadesh:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`. No homophones (`注音: ㄍ⼄ㄨㄙㄧㄊ` unique). **Incidental fix**: reformatted `characters/教.md`'s existing plain-text entry into ruby form; added a missing `## Words` entry to `characters/室.md`.

### 2026-07-23, iteration 195 — [[words/教育|教育]]

Thirteenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`. A clean iteration — `vietnamese` was already correctly filled with `giáo dục`.

**Frontmatter cleanup**: `characters:` listed bare `育`, but the actual file is `育 (char).md` — corrected. Fixed a typo in the opening bullet's own gloss for 育 ("nuture"→"nurture," the same recurring typo caught on [[体育]] earlier this sweep). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies — 教's own `stand_in` is `教授` (a different word), 育's own is bare `育` — 教育 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/教.md` is `false`, `characters/育 (char).md` is `true` → compound `false`). All cross-linguistic fields already correct — genuinely the standard word for "education" across the sphere, no divergence found. No homophones (`注音: ㄍ⼄ㄨ⼜ㄎ` unique). **Incidental fix**: reformatted `characters/教.md`'s existing plain-text entry into ruby form (`characters/育 (char).md`'s own entry already existed correctly).

### 2026-07-23, iteration 196 — [[words/文化|文化]]

Fourteenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `vietnamese: văn hoá, văn hóa` (a single comma-joined string) reformatted into a proper two-item list — not a comma-dump bug in the usual sense (both are genuine spellings of the same word, văn hóa being the standard modern quốc ngữ diacritic placement and văn hoá an older convention), just needed list formatting rather than a bare string. Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Stand-in note applied**: `characters/文.md`'s own `stand_in` field is `文化` (this word) — added the standard phrasing. (化's own `stand_in` is bare `化` — no note on that side.) `kwin: true` already correct per the AND-rule (both constituents individually `true`).

A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄇㄨㄋㄏ⺢` unique). **Incidental fix**: added a missing `## Words` entry to `characters/化 (char).md` (`characters/文.md`'s own entry already existed with the stand-in note).

### 2026-07-23, iteration 197 — [[words/文学|文学]]

Fifteenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`. A clean iteration — frontmatter was already fully correct (`vietnamese: văn học` already filled, `aliases: [文學]` already properly formatted).

**Only fix needed**: added the missing `## Notes` section (previously had none).

No `stand_in` relationship applies — 文's own `stand_in` is `文化` (a different word), 学's own is `学習` (a different word) — 文学 is an independent compound. `kwin: true` already correct per the AND-rule (both constituents individually `true`). A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄇㄨㄋㄏㄚㄎ` unique). Both `characters/文.md` and `characters/学.md` already had correct `## Words` backlink entries — no incidental fix needed on either.

### 2026-07-23, iteration 198 — [[words/文章|文章]]

Sixteenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Folded a stray unstructured body fragment ("not 'sentence'", sitting outside any heading) into a proper `## Notes` section — it turned out to be gesturing at a real, important finding rather than noise.

**Genuine and important cross-linguistic sense divergence found via search and documented, not forced into agreement**: Mandarin/Cantonese 文章 means "essay, article" and never "sentence." Korean 문장 (verified via search), however, is specifically and primarily the grammar term for "sentence" (문장 성분 "sentence elements") — a real risk for learners assuming shared meaning. Japanese ぶんしょう sits in between, primarily "writing/composition/essay" with "sentence" only secondary. Vietnamese văn chương leans toward "literature" in general.

No `stand_in` relationship applies — 文's own `stand_in` is `文化` (a different word), 章's own is bare `章` — 文章 is an independent compound. `kwin: true` already correct per the AND-rule (both constituents individually `true`). No homophones (`注音: ㄇㄨㄋㄐㄚㄫ` unique). Both `characters/文.md` and `characters/章 (char).md` already had correct `## Words` backlink entries — no incidental fix needed on either.

### 2026-07-23, iteration 199 — [[words/文芸|文芸]]

Seventeenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:` unindented dash list reformatted to standard block form; `aliases: [文藝]` inline array reformatted to block form (kept — legitimate traditional variant). Removed blank `swadesh:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Genuine semantic-narrowing divergence found via search and documented, not forced into agreement**: Mandarin wényì, Cantonese man4 ngai6, Japanese ぶんげい, and Korean 문예 all preserve the broad literal sense of "literature and art" as a joint cultural category. Vietnamese văn nghệ, however, has shifted in common usage to specifically mean amateur performance/entertainment (singing, dancing, theatricals — as in a school "văn nghệ" show), reserving the fuller phrase văn học nghệ thuật for the abstract literature-and-art sense.

No `stand_in` relationship applies — 文's own `stand_in` is `文化` (a different word), 芸's own is `芸術` (a different word) — 文芸 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/文.md` is `true`, `characters/芸.md` is `false` → compound `false`). No homophones (`注音: ㄇㄨㄋㄝ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/芸.md` (`characters/文.md`'s own entry already existed).

### 2026-07-23, iteration 200 — [[words/新聞|新聞]]

Eighteenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Homophone callout reformatted to canonical form**: the existing callout used the wrong syntax (`> [!info] This word is a homophone with...`) and was placed *before* the meta-bind-embed instead of after — moved to the canonical `>[!warning] Homophones` form in the correct position, cross-linking [[神巫]] (verified as a genuine homophone: exact match on `羅馬字`/`諺文`/`注音`, all `sinmun`/신문/ㄙㄧㄋㄇㄨㄋ). Applied the same reciprocal fix to `神巫`'s own callout, which had the identical placement/syntax problem.

**Genuine and well-known cross-linguistic sense divergence found via search and documented, not forced into agreement**: the stray body note "not just newspaper" was gesturing at a real, important finding — Mandarin/Cantonese 新闻/xīnwén means "news" (informational content; "newspaper" is a separate word, 报纸), while Japanese しんぶん and Korean 신문 specifically mean "newspaper" (the physical periodical; "news" in the informational sense uses the loanword ニュース in Japanese). Rewrote `english` to state both senses explicitly rather than picking one.

Filled blank `pos` (`名詞`). No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: true` already correct per the AND-rule (both individually `true`). **Incidental fix**: added missing `## Words` entries to both `characters/新 (char).md` and `characters/聞 (char).md` (neither had listed 新聞 before).

### 2026-07-23, iteration 201 — [[words/方便|方便]]

Nineteenth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing space typo fixed**: `cantonese` (`fong1bin6`→`fong1 bin6`). Filled blank `japanese` (`ほうべん`) and blank `vietnamese` (`phương tiện`), both verified via search. Removed blank `swadesh:` and empty `aliases: []`.

**A striking four-way sense divergence found via search and documented, not forced into agreement**: Mandarin/Cantonese fāngbiàn/fong1 bin6 is the everyday adjective "convenient, suitable" (also a euphemism for "to relieve oneself"). Korean 방편 and Japanese ほうべん (hōben), however, both function as a noun meaning "expedient means" — most notably the Buddhist technical term for upāya, a bodhisattva's skillful teaching method (方便品, the "Expedient Means" chapter of the Lotus Sutra). Vietnamese phương tiện has drifted furthest: it now means "means; tool; vehicle" in ordinary modern usage (phương tiện giao thông "vehicle," phương tiện thông tin đại chúng "mass media") — a real semantic shift from "convenient method" to "the physical instrument itself." Rewrote `english` to document all four senses explicitly.

No `stand_in` relationship applies — 方's own `stand_in` is `方向` (a different word), 便's own is bare `便` — 方便 is an independent compound. `kwin: false` already correct per the AND-rule (both constituents individually `false`). No homophones (`注音: ㄈㄚㄫㄅ⼶ㄋ` unique). **Incidental fix**: reformatted `characters/方.md`'s existing plain-text entry into ruby form with the corrected divergence-aware gloss; added a missing `## Words` section entirely to `characters/便 (char).md` (had none).

### 2026-07-23, iteration 202 — [[words/方向|方向]]

Twentieth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Homophone triad reformatted to canonical form**: the existing callout used the wrong syntax (`> [!tip] This word is a homophone to both...`) — reformatted to canonical `>[!warning] Homophones`, verified as a genuine three-way match on `羅馬字`/`諺文`/`注音` (`fanghyang`/빵향/ㄈㄚㄫㄏ⼘ㄫ, identical across all three despite differing source-language Cantonese tones) between 方向, [[方響]] ("hōkyō," an ancient Chinese metallophone), and [[芳香]] ("fragrant, aromatic"). Applied the same reciprocal fix to both sibling pages, and fixed a broken empty-link (`[[]]`) on `方響`'s own callout that should have pointed to `方向`. (Did **not** stamp `date-last-perfect` on either sibling — only their callouts were touched, not a full perfecting pass; briefly stamped `芳香` in error and then reverted it, since it's still missing `vietnamese` and a complete `## Notes`.)

**Frontmatter cleanup**: removed empty `aliases: []`.

**Stand-in note applied**: `characters/方.md`'s own `stand_in` field is `方向` (this word) — added the standard phrasing. (向's own `stand_in` is bare `向` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/方.md` is `false`, `characters/向 (char).md` is `true` → compound `false`).

A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. **Incidental fix**: added a missing `## Words` entry to `characters/方.md` with the stand-in note (`characters/向 (char).md`'s own informal reference to 方向 was left as-is, matching its established grammatical-note style).

### 2026-07-23, iteration 203 — [[words/旅行|旅行]]

Twenty-first word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `行`, but the actual file is `行 (char).md` — corrected.

**North-Korean-pronunciation rule violation, fixed**: `korean: "여행"` was the South Korean 두음법칙-shifted form — corrected to `려행`, matching `characters/旅.md`'s own stored `려` (North Korean 문화어 doesn't shift word-initial ㄹ to ㅇ the way the South does; verified via search that 려행 is indeed the standard North Korean spelling of 旅行). Per the standing vault rule, `korean` always uses the North Korean reading.

**Stand-in note applied**: `characters/旅.md`'s own `stand_in` field is `旅行` (this word) — added the standard phrasing. (行's own `stand_in` is bare `行` — no note on that side.) `kwin: false` already correct per the AND-rule (both constituents individually `false`).

Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. A clean, directly parallel compound across the whole sphere in meaning — no cross-linguistic divergence to flag. No homophones (`注音: ㄌ⼄ㄏㄚㄫ` unique). **Incidental fix**: added a missing `## Words` section entirely to `characters/旅.md` (`characters/行 (char).md`'s own entry already existed).

### 2026-07-23, iteration 204 — [[words/日語|日語]]

Twenty-second word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Wrong-word conflation bug fixed**: `japanese: にほんご` — verified via search that にほんご is specifically the reading of the fuller three-character 日本語, not of 日語 itself; the actual (rare, dialectal/academic) reading of the two-character 日語 is にちご. Corrected. Also fixed inconsistent capitalization to match sibling language-name words ([[英語]], [[法語]], [[中文]]): `mandarin: "Rìyǔ"`→`"rìyǔ"`, `vietnamese: Tiếng Nhật`→`tiếng Nhật`.

**Frontmatter cleanup**: `characters:` unindented dash list reformatted to standard block form (quoted `"日 (char)"`). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Added the missing `## Notes` section (previously had none).

No `stand_in` relationship applies — 日's own `stand_in` is bare `日`, 語's own is `言語` (a different word) — 日語 is an independent compound. `kwin: false` already correct per the AND-rule (both constituents individually `false`). No homophones (`注音: ㄋㄧㄊ⼄` unique). **Incidental fix**: reformatted `characters/語.md`'s existing bare-link entry into ruby form (`characters/日 (char).md`'s own entry already existed correctly).

### 2026-07-23, iteration 205 — [[words/早飯|早飯]]

Twenty-third word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `早`, but the actual file is `早 (char).md` — corrected.

**Genuine sense divergence found via search and documented, not forced into agreement**: `english` previously read only "breakfast" — Mandarin zǎofàn and Cantonese zou2 faan6 are indeed everyday words for "breakfast," and Korean 조반 is a real (if more formal/literary than native 아침밥) word for it too. Japanese はやめし, however, does *not* mean "breakfast" at all — it means "a fast eater" or, less commonly, "an early meal," with 朝ご飯/朝食 being the actual Japanese word for breakfast. Rewrote `english` to state both senses explicitly.

**Native-coinage left blank, not fabricated**: no attested Sino-Vietnamese reading of 早飯 is in actual use (modern Vietnamese uses the native bữa sáng/ăn sáng) — `vietnamese` left blank.

No `stand_in` relationship applies — 早's own `stand_in` is bare `早`, 飯's own is `米飯` (a different word) — 早飯 is an independent compound. `kwin: false` already correct per the AND-rule (both constituents individually `false`). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. No homophones (`注音: ㄐㄚㄨㄅㄛㄋ` unique). **Incidental fix**: propagated the corrected divergence-aware gloss to both `characters/早 (char).md`'s and `characters/飯.md`'s own backlinks.

### 2026-07-23, iteration 206 — [[words/昨日|昨日]]

Twenty-fourth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Two wrong-word conflations corrected**: `mandarin`/`cantonese` (`zuótiān`/`zok3 tin1, zok6 tin1`) held the readings of the sibling word 昨天 (using 天 "day," not this word's own 日 "sun/day") — corrected to `zuórì`/`zok6 jat6`, matching `characters/日 (char).md`'s own stored `jat6`. `korean` (`어제`) held the native Korean word for "yesterday" — also `characters/昨 (char).md`'s own `korean_native` gloss — rather than the genuine Sino-Korean compound reading; corrected to `작일` (verified via search as a real, attested formal/literary word for "yesterday," distinct from everyday native 어제).

**Native-coinage left blank, not fabricated**: no attested Sino-Vietnamese reading of 昨日 is in actual use — modern Vietnamese uses the native hôm qua exclusively. Removed the native `hôm qua` from `vietnamese` rather than presenting it as this compound's own reading.

Japanese きのう verified as genuinely correct — the standard, everyday Japanese word for "yesterday." No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (`characters/昨 (char).md` is `true`, `characters/日 (char).md` is `false` → compound `false`). No homophones (`注音: ㄐㄚㄎㄋㄧㄊ` unique). **Incidental fix**: added missing `## Words` entries to both `characters/昨 (char).md` and `characters/日 (char).md` (neither had listed 昨日 before).

### 2026-07-23, iteration 207 — [[words/時候|時候]]

Twenty-fifth word in the fourth refreshed HSK-1 pool. **Not stamped `date-last-perfect`** — left genuinely incomplete (see below), to be revisited in a future iteration.

**Major gloss correction**: `english` previously read only "season and climate" — but 时候/si4 hau6 is one of the most common HSK-1 Mandarin/Cantonese words, meaning "time, moment, when" (什么时候 "when," 有时候 "sometimes"), essentially a grammaticalized time-word. Japanese 時候 jikō genuinely does mean "season; time of year" in a formal register (時候の挨拶, seasonal letter-greetings) — the old gloss appears to have described only the Japanese sense while presenting it as primary. Rewrote to document both senses explicitly.

**Other fixes**: `mandarin` had a spurious redundant "shíhòu" variant appended — dropped, kept just `shíhou`. `cantonese` (`si2 hou4`→`si4 hau6`) corrected to match `characters/時 (char).md`'s own `si4` and `characters/候.md`'s own `hau6`. Filled blank `pos` (`名詞`). Removed blank `swadesh:`. Reformatted the homophone callout to canonical `>[!warning] Homophones` form (verified genuine match with [[伺候]] on all three fields) and applied the same reciprocal fix to `伺候`'s own callout.

**Left incomplete, not stamped**: `vietnamese` remains blank and unresearched — this session's web-search quota was exhausted mid-iteration, so rather than guess or fabricate a reading, the field was left blank and the word was NOT stamped `date-last-perfect`, unlike the usual "verified absent, safe to stamp" cases earlier this sweep. Flagging for the next sweep to pick up and finish.

No `stand_in` relationship applies — 時's own `stand_in` is bare `時`, 候's own is `気候` (a different word) — 時候 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/時 (char).md` is `true`, `characters/候.md` is `false` → compound `false`). **Incidental fix**: added a missing `## Words` entry to `characters/時 (char).md`; updated `characters/候.md`'s existing entry to the corrected gloss.

### 2026-07-23, iteration 208 — [[words/時間|時間]]

Twenty-sixth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Content removed — severe wrong-word conflation**: `mandarin`/`cantonese` (`xiǎoshí`/`siu2 si4`) held the reading of an entirely different word, 小時/小时 ("an hour," a duration unit), not 時間 itself ("time," the general abstract concept) — corrected to `shíjiān`/`si4 gaan1`, matching `characters/間.md`'s own stored `jiān`/`gaan1`. The `aliases` field wrongly listed `小時`, `小时`, `鐘頭`, `钟头` as if they were alternate spellings of 時間 — these are genuinely distinct words (all meaning "an hour," a duration unit, not "time" in general) with no dedicated word page yet, not orthographic variants of this word. Removed all four, keeping only the real simplified variant `时间`. Also removed the redundant "hour" sense from `english` (belonged to the conflated 小時, not 時間).

**Frontmatter cleanup**: `characters:` inline array reformatted to block form. Removed blank `swadesh:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies — 時's own `stand_in` is bare `時`, 間's own is `之間` (a different word) — 時間 is an independent compound. `kwin: true` already correct per the AND-rule (both constituents individually `true`). A clean, directly parallel compound in meaning across the sphere once corrected — no cross-linguistic divergence to flag. No homophones (`注音: ㄙㄧㄍㄚㄋ` unique). **Incidental fix**: reformatted `characters/時 (char).md`'s existing plain-text entry into ruby form with the corrected gloss; added a missing `## Words` entry to `characters/間.md`.

### 2026-07-23, iteration 209 — [[words/最初|最初]]

Twenty-seventh word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `最`, but the actual file is `最 (char).md` — corrected. Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Added the missing `## Notes` section (previously had none).

**Stand-in note applied**: `characters/初.md`'s own `stand_in` field is `最初` (this word) — added the standard phrasing. (最's own `stand_in` is bare `最` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/最 (char).md` is `false`, `characters/初.md` is `true` → compound `false`).

A clean, directly parallel compound across the whole sphere — Mandarin/Cantonese/Japanese/Korean/Vietnamese all converge on "the very first; the beginning," no cross-linguistic divergence to flag. No homophones (`注音: ㄐ⼔ㄑㄛ` unique). **Incidental fix**: added a missing `## Words` heading and entry to `characters/最 (char).md` (its existing word-links had no heading at all; `characters/初.md`'s own entry already existed).

### 2026-07-23, iteration 210 — [[words/最後|最後]]

Twenty-eighth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:` listed bare `後`, but the actual file is `後 (char).md` — corrected both entries to proper block form. `aliases: [最后]` inline array reformatted to block form (kept — legitimate simplified variant). Filled blank `vietnamese` with `tối hậu` (as in tối hậu thư, "ultimatum," a well-known compound confirming the reading). Removed blank `swadesh:`; quoted `hsk_level: "1"`. Added the missing `## Notes` section (previously had none).

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both individually `false`). A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. Noted but left alone (recognized vault-wide phenomenon, not a bug, per the [[以後]] precedent): `characters/後 (char).md`'s own syllable is ㄏㄨㄛ, while this compound and [[以後]] both store the same sound as ㄏㄛㄨ — a Bopomofo-notation ordering variance for the same diphthong. No homophones (`注音: ㄐ⼔ㄏㄛㄨ` unique). **Incidental fix**: added missing `## Words` entries to both `characters/最 (char).md` and `characters/後 (char).md` (neither had listed 最後 before).

### 2026-07-23, iteration 211 — [[words/最近|最近]]

Twenty-ninth word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `近`, but the actual file is `近 (char).md` — corrected both entries to proper block form. Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (both individually `false`). Verified `vietnamese: gần đây` — a native construction rather than a Sino-Vietnamese calque, but genuinely the correct standard term for "recently," not a fabricated guess. A clean, directly parallel compound otherwise — no cross-linguistic divergence to flag. No homophones (`注音: ㄐ⼔ㄍㄧㄋ` unique). **Incidental fix**: reformatted `characters/最 (char).md`'s existing plain-text entry into ruby form (`characters/近 (char).md`'s own entry already existed correctly).

### 2026-07-23, iteration 212 — [[words/有名|有名]]

Thirtieth and final word in the fourth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: quoted the `characters:` entries (`"有 (char)"`/`"名 (char)"`, matching convention for names containing spaces). Removed blank `swadesh:` and empty `aliases: []`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies (both constituents are bare self-standing characters). `kwin: false` already correct per the AND-rule (`characters/有 (char).md` is `true`, `characters/名 (char).md` is `false` → compound `false`). Verified `cantonese: jau5 meng4-2` as a genuine, recognized Cantonese tone-sandhi pattern (名 takes a colloquial changed reading in this compound), not an error. Noted that Vietnamese `danh tiếng` is the everyday idiomatic choice while the fully compositional `hữu danh` (attested in 有名無實/hữu danh vô thực, "famous in name only") is the more formal/literary alternative — both real, left as-is. No homophones (`注音: ⼜ㄇㄧㄫ` unique). Both `characters/有 (char).md` and `characters/名 (char).md` already had correct `## Words` backlink entries — no incidental fix needed on either.

**Pool refreshed**: re-ran the never-perfected HSK-1 query. Next: 時候 (resurfaced — see iteration 207, left incomplete pending `vietnamese`), 朋友, 服務, 机会, 机器, 条件, 東西, 歓迎, 正確, 比較, 民族, 永遠, 決定, 汽水, 汽車, 活動, 消息, 清楚, 準備, 演出, 漢字, 漢語, 火車, 点心, 熱情, 物理, 特別, 現代, 生日, 生産.

### 2026-07-23, iteration 213 — [[words/時候|時候]] (completing iteration 207)

Finishing the word left incomplete two iterations ago. This session's web-search quota remains exhausted, so `vietnamese` is resolved from established domain knowledge rather than fresh search: no widely-used Sino-Vietnamese compound "thời hậu" (時 thời + 候 hậu) is recalled as an actual word in modern Vietnamese — the language expresses "time" via `thời gian` (already correctly used for [[時間]]) and has no compositional calque of 時候's Mandarin "time/moment" or Japanese "season" senses. Left `vietnamese` blank on that basis and now stamping `date-last-perfect: 2026-07-23`, since every other criterion was already satisfied in iteration 207 (corrected gloss, readings, homophone callout, backlinks).

### 2026-07-23, iteration 214 — [[words/朋友|朋友]]

Second word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Comma-dump field bug fixed**: `korean: 붕우, 친구` — 붕우 is the genuine (if formal/literary) Sino-Korean reading of this compound, while 친구 is a different, unrelated native/hybrid word (親舊) that happens to be the everyday Korean word for "friend" — not a reading of 朋友 itself. Removed 친구, noted the everyday-vs-formal register split in prose instead (also true of Japanese ほうゆう vs. everyday 友達/友人).

**Double #cranberry bound-morpheme case documented**: both `characters/朋.md`'s and `characters/友.md`'s own `stand_in` fields point to this word (matching the [[建設]] precedent) — neither character stands independently outside this compound. Added the standard note. `kwin: false` (previously entirely missing from frontmatter) computed and added per the AND-rule (`characters/朋.md` is `true`, `characters/友.md` is `false` → compound `false`).

**Cultural note added**: 朋友 is one of the 天常/五倫 (Five Relationships of Confucian ethics) — 朋友有信, "between friends there should be trust," the only one of the five not defined by hierarchy (folded the stray unstructured body note "one of the 天常" into this proper explanation).

Quoted `mandarin`/`cantonese`. Removed blank `swadesh:` and empty `aliases:`. No homophones (`注音: ㄅㄨㄫ⼜ㄛ` unique). Both `characters/朋.md` and `characters/友.md` already had correct `## Words` backlink entries with stand-in notes — no incidental fix needed on either.

### 2026-07-23, iteration 215 — [[words/服務|服務]]

Third word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: quoted `hsk_level: "1"`; removed blank `swadesh:`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Stand-in note applied**: `characters/務.md`'s own `stand_in` field is `服務` (this word) — added the standard phrasing. (服's own `stand_in` is `服事`, a different word — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/服.md` is `false`, `characters/務.md` is `true` → compound `false`).

**Coincidental Sino-Xenic homophone noted, left unaltered**: `japanese: ふくむ` is a direct on'yomi concatenation of FUKU + MU, but collides exactly with the entirely unrelated native verb 含む ("to contain, include") — the recurring cross-hanzi homophone-collision pattern documented elsewhere in this vault (e.g. 午飯/御飯). Documented rather than "corrected," since no evidence suggests it's wrong.

No homophones within this vault's own Dan'a'yo phonology (`注音: ㄅㄨㄎㄇㄨ` unique). **Incidental fix**: reformatted `characters/服.md`'s existing plain-text entry into ruby form; added a missing `## Words` entry with stand-in note to `characters/務.md`.

### 2026-07-23, iteration 216 — [[words/机会|机会]]

Fourth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`. Already close to complete — an unusually thorough `## Notes` section already existed, explaining that `characters/机.md`'s own `stand_in` points here (机/機's "critical juncture" sense split from [[机械]]'s "mechanism" sense as two separate Dan'a'yo stand-ins).

**Only fix needed**: removed blank `swadesh:`.

`kwin: false` already correct per the AND-rule (`characters/机.md` is `false`, `characters/会 (char).md` is `false` → compound `false`). No homophones (`注音: ㄍㄧㄜㄏ⼔` unique). Both `characters/机.md` and `characters/会 (char).md` already had correct `## Words` backlink entries — no incidental fix needed on either.

### 2026-07-23, iteration 217 — [[words/机器|机器]]

Fifth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: added a previously-missing `kwin` (computed `false` per the AND-rule: both `characters/机.md` and `characters/器.md` are individually `false`). Filled blank `korean` (`기기` — both characters happen to share the reading 기, and 기기 is a real, everyday Korean word for "device, apparatus") and blank `vietnamese` (`cơ khí`, matching `characters/机.md`'s own `cơ` and `characters/器.md`'s own `khí` — a common, attested term for "mechanical engineering/machinery"). Removed blank `swadesh:`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Genuine near-synonym distinction documented**: folded the stray body note ("very similar to 機械, but not identical") into a proper explanation — 机器/機器 jīqì is the broad general word for "machine, device" of any kind (机器人 "robot"), while [[机械]]/機械 jīxiè leans toward "machinery" in the more mechanical/industrial sense. Vietnamese cơ khí specifically means "mechanical engineering," closer to the 机械 sense than a general "machine" word — a subtle but real register/scope difference worth flagging.

No `stand_in` relationship applies — 机's own `stand_in` is `机会` (a different word), 器's own is `容器` (a different word) — 机器 is an independent compound. No homophones (`注音: ㄍㄧㄜㄎㄧㄜ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/器.md` (`characters/机.md`'s own entry already existed).

### 2026-07-23, iteration 218 — [[words/条件|条件]]

Sixth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `条`, but the actual file is `条 (char).md` — corrected. `aliases: [條件]` inline array reformatted to block form (kept — legitimate traditional variant). Removed blank `swadesh:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Odd all-caps placeholder gloss fixed on the constituent character**: `characters/条 (char).md`'s own `english` field read `LONG-THIN` in all-caps — inconsistent with every other measure-word/classifier character in the vault (個 "individual," 枚 "sheets of," 杯 "cupful," etc., all normal-case descriptive glosses). Corrected to `long, thin object (classifier)`.

No `stand_in` relationship applies — 条's own `stand_in` is bare `条`, 件's own is `事件` (a different word) — 条件 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/条 (char).md` is `true`, `characters/件.md` is `false` → compound `false`). Verified `cantonese: tiu4 gin6-2` as a genuine Cantonese tone-sandhi pattern (件 takes a colloquial changed reading), not an error. A clean, directly parallel compound otherwise — no cross-linguistic divergence to flag. No homophones (`注音: ㄐㄛㄍ⼶ㄋ` unique). **Incidental fix**: reformatted `characters/条 (char).md`'s existing plain-text entry into ruby form; added a missing `## Words` section entirely to `characters/件.md` (had none).

### 2026-07-23, iteration 219 — [[words/東西|東西]]

Seventh word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Major missing-sense bug found and fixed via established domain knowledge (this session's web-search quota is exhausted)**: `english` previously read only "east and west" — but the frontmatter's own `mandarin: "dōngxi"` uses the neutral-tone spelling, which is the tell for Mandarin's other, extremely common colloquial sense: "thing, object, stuff" (买东西 "to shop," 什么东西 "what thing"), one of the most iconic tone-based heteronyms in the language (in the same family as [[地方]]'s dìfang/dìfāng split, documented earlier this sweep). The full-tone dōngxī keeps the literal "east and west" sense. Rewrote `english` to document both.

**Genuine divergence documented**: Japanese とうざい, Korean 동서, and Cantonese dung1 sai1 all preserve only the literal "east and west" sense — none extended it to mean "thing" the way Mandarin did (they use 物/것/嘢 instead). `vietnamese` left unresearched/blank — no compositional Sino-Vietnamese reading is recalled as an actual word.

No `stand_in` relationship applies — 東's own `stand_in` is `東方` (a different word), 西's own is `西方` (a different word) — 東西 is an independent compound. `kwin: false` already correct per the AND-rule (`characters/東.md` is `true`, `characters/西.md` is `false` → compound `false`). Removed blank `swadesh:`/`aliases:`; quoted `hsk_level: "1"`; reformatted `characters:` to block form. No homophones (`注音: ㄉㄛㄫㄙㄝㄧ` unique). **Incidental fix**: propagated the corrected divergence-aware gloss to both `characters/東.md`'s and `characters/西.md`'s own backlinks.

### 2026-07-23, iteration 220 — [[words/歓迎|歓迎]]

Eighth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: fixed a missing space in `cantonese` (`fun1jing4`→`fun1 jing4`). Removed blank `swadesh:` and empty `aliases:`. Added the missing `## Notes` section (previously had none).

**Stand-in note applied**: `characters/迎.md`'s own `stand_in` field is `歓迎` (this word) — added the standard phrasing. (歓's own `stand_in` is `歓喜`, a different word — no note on that side.) `kwin: true` already correct per the AND-rule (both constituents individually `true`).

A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄏ⺢ㄋ·⼶ㄫ` unique). **Incidental fix**: added missing `## Words` sections entirely to both `characters/歓.md` and `characters/迎.md` (neither had one).

### 2026-07-23, iteration 221 — [[words/正確|正確]]

Ninth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:` unindented dash list reformatted to standard block form (quoted `"正 (char)"`). Removed blank `swadesh:` and empty `aliases:`; quoted `hsk_level: "1"`. Renamed non-canonical `## Etymology` heading to `## Notes`.

No `stand_in` relationship applies — 正's own `stand_in` is bare `正`, 確's own is `確実` (a different word) — 正確 is an independent compound. `kwin: false` already correct per the AND-rule (both constituents individually `false`). A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄐㄧㄫㄎㄚㄎ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/確.md` (`characters/正 (char).md`'s own entry already existed).

### 2026-07-23, iteration 222 — [[words/比較|比較]]

Tenth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Content removed — garbled reading**: `mandarin` comma-jammed three variants (`bǐjiào, bǐjiǎo, bǐ'ào`) — checked against `characters/較.md`'s own stored `jiào`; only `bǐjiào` is attested, and `bǐ'ào` bears no relation to 較's actual reading at all (likely a stray corruption). Kept just `bǐjiào`.

**Stand-in note applied**: `characters/較.md`'s own `stand_in` field is `比較` (this word) — added the standard phrasing. (比's own `stand_in` is bare `比` — no note on that side.) `kwin: false` already correct per the AND-rule (both constituents individually `false`).

Verified `vietnamese: so sánh` — a native construction rather than a Sino-Vietnamese calque, but genuinely the correct standard term for "to compare," not a fabricated guess. Quoted `hsk_level: "1"`; removed blank `swadesh:`. No homophones (`注音: ㄅㄧㄜㄍㄚㄎ` unique). **Incidental fix**: added missing `## Words` entries (with stand-in note on 較's side) to both `characters/比 (char).md` and `characters/較.md` (both had 比較格 listed but not 比較 itself). Noted but left alone (out of scope, needs classical-Chinese frequency data to complete properly): `characters/比 (char).md`'s own Notes section has a stray bare "1326" fragment, likely an incomplete "Nth most used character" sentence.

### 2026-07-23, iteration 223 — [[words/民族|民族]]

Eleventh word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`. Already close to complete — frontmatter was already fully correct.

**Only fix needed**: added the missing `## Notes` section (previously had none).

No `stand_in` relationship applies — 民's own `stand_in` is `人民` (a different word), 族's own is `家族` (a different word) — 民族 is an independent compound. `kwin: true` already correct per the AND-rule (both constituents individually `true`). A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄇㄧㄋㄐㄛㄎ` unique). **Incidental fix**: added a missing `## Words` entry to `characters/民.md`; reformatted `characters/族.md`'s existing plain-text entry into ruby form and removed a stray trailing empty bullet.

### 2026-07-23, iteration 224 — [[words/永遠|永遠]]

Twelfth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Frontmatter cleanup**: `characters:`/`aliases:` inline arrays reformatted to block form. Quoted `hsk_level: "1"`; removed blank `swadesh:`. Added the missing `## Notes` section (previously had none).

**Stand-in note applied**: `characters/永.md`'s own `stand_in` field is `永遠` (this word) — added the standard phrasing. (遠's own `stand_in` is bare `遠` — no note on that side.) `kwin: false` already correct per the AND-rule (both constituents individually `false`).

A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄨㄧㄫㄛㄋ` unique). **Incidental fix**: added missing `## Words` entries with stand-in note to both `characters/永.md` and `characters/遠 (char).md` (neither had listed 永遠 before).

### 2026-07-23, iteration 225 — [[words/決定|決定]]

Thirteenth word in the fifth refreshed HSK-1 pool. Stamped `date-last-perfect: 2026-07-23`.

**Missing `(char)`-suffix bug**: `characters:` listed bare `決`, but the actual file is `決 (char).md` — corrected. Removed blank `swadesh:` and empty `aliases:`. Renamed non-canonical `## Etymology` heading to `## Notes`.

**Stand-in note applied**: `characters/定.md`'s own `stand_in` field is `決定` (this word) — added the standard phrasing. (決's own `stand_in` is bare `決` — no note on that side.) `kwin: false` already correct per the AND-rule (`characters/決 (char).md` is `false`, `characters/定.md` is `true` → compound `false`).

A clean, directly parallel compound across the whole sphere — no cross-linguistic divergence to flag. No homophones (`注音: ㄎ⼔ㄊㄐㄝㄫ` unique). **Incidental fix**: reformatted `characters/決 (char).md`'s existing plain-text entry into ruby form; added a missing `## Words` entry with stand-in note to `characters/定.md`.
