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
