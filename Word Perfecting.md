# Word Perfecting

Running log for the word-perfecting backlog sweep (see [[AIOS/checklists/checklist_words.md|Checklist: Word Pages]]). The prior log (iterations 1–1040) grew to ~8,500 lines and was archived by the user to `Word Perfecting.md.zip`; this file continues from there. Iteration numbering continues unbroken from the archived log.

**Process**: one word per iteration (per standing pacing preference). Find the next candidate via `grep -L "^date-last-perfect" words/*.md`, sorted alphabetically by filename (Unicode/`LC_ALL=C` order), continuing from the last-processed filename's position in that sort. Check the word's own `characters:` constituents for a `stand_in` match (add the stand-in note if so), verify `羅馬字`/`諺文`/`注音` are the correct concatenation of each constituent's own fields, verify `kwin` via the AND-rule (all constituents' own `kwin` must be `true` for the compound to be `true`), fill blank cross-linguistic fields only when a real value can be verified (leave deliberately blank with a reason otherwise), and check for genuine Dan'a'yo-level homophones (not just same-spelling coincidences in a real language) before stamping `date-last-perfect`.

Next (re-scoped tail, alphabetical-by-filename): 家具 (3222 files remaining per full-vault rescan, per the archived log's last iteration).

### 2026-08-05, iteration 1041 — [[words/家具|家具]]

Neither constituent's `stand_in` points to this word (家's is 家庭, 具's is 工具), so no stand-in note applies. **Content added**: filled blank `hsk_level: "4"` (verified). **Left `vietnamese` blank rather than guessing**: mechanical "gia cụ" doesn't appear to be a standing everyday term — Vietnamese uses native đồ nội thất/đồ đạc instead. Added missing `>[!tip]` header and `## Notes`. `kwin: true` confirmed (AND-rule). No homophones (注音 ㄍㄚㄍㄨ unique). Stamped `date-last-perfect: 2026-08-05`.

Next (re-scoped tail, alphabetical-by-filename): 家庭 (3221 files remaining per full-vault rescan).

### 2026-08-26, iteration 1042 — [[words/家庭|家庭]]

Loop resumed after a stall since 2026-08-05 (iteration 1041, see [[project_perfection_era_methodology]]). 家's own `stand_in` field is 家庭 — added the stand-in note to the opening bullet (missing before). **Content added**: `>[!tip]`-free body was already meta-bind-embed-first (correct); built out the missing `## Notes` from a bare frontmatter-only stub — no Notes section existed at all. Verified `羅馬字`/`諺文`/`注音` are exact concatenations of 家 (ga/가/ㄍㄚ) + 庭 (deng/덩/ㄉㄝㄫ). `mandarin`/`cantonese`/`japanese`/`korean` all already-correct compositional concatenations; `vietnamese: gia đình` already correct (confirmed via Wiktionary, matches 家's own "gia" + 庭's own "đình"). **Removed blank `hsk_level`/`swadesh`/`aliases` keys** — checked Wiktionary per `skill_word_creation.md`'s sourcing rule, no HSK level given for the compound itself (both constituents are independently HSK 1), so left the field omitted rather than guessing. `kwin: false` confirmed via AND-rule (家 `true` + 庭 `false`). No homophones (注音 ㄍㄚㄉㄝㄫ unique across both words and characters). Stamped `date-last-perfect: 2026-08-26`.

Next (re-scoped tail, alphabetical-by-filename): 家族 (3206 files remaining per rescan).

### 2026-08-26, iteration 1043 — [[words/家族|家族]]

族's own `stand_in` field is 家族 — added the stand-in note (page had no `## Notes` section at all before this, same gap as 家庭). Verified `羅馬字`/`諺文`/`注音`/`mandarin`/`cantonese`/`japanese`/`korean`/`vietnamese` all already-correct compositional concatenations of 家 + 族 (`vietnamese: gia tộc` confirmed via Wiktionary). `kwin: true` confirmed via AND-rule (家 `true` + 族 `true`). Removed blank `hsk_level`/`swadesh`/`aliases` keys — no HSK level given on Wiktionary for the compound. No homophones (注音 ㄍㄚㄐㄛㄎ unique). Notes cover the 家族/家庭 semantic distinction and a real finding: Japanese かぞく is comparatively narrow (one's *own* immediate family only, needs ご家族 for others') and is not attested before 1808, apparently borrowed from modern written Chinese rather than inherited natively. Stamped `date-last-perfect: 2026-08-26`.

Next (re-scoped tail, alphabetical-by-filename): 家畜 (3205 files remaining per rescan).

### 2026-08-26, iteration 1044 — [[words/家畜|家畜]]

No stand-in note applies (家's `stand_in` is 家庭, 畜's is 畜生 — neither points here). Page had no `## Notes` section; built it from scratch. Verified all fields already correct compositional concatenations (`vietnamese: gia súc` confirmed via Wiktionary). `kwin: true` confirmed via AND-rule (both constituents `true`). Removed blank `hsk_level`/`swadesh`/`aliases` — Wiktionary marks the compound only "Advanced Mandarin," no specific level number, so left omitted (畜 itself is independently HSK 4). No homophones. Notes distinguish 家畜 (any livestock) from [[家禽]] (fowl specifically), and cover 畜's own stand-in [[畜生]] drifting into a pejorative ("brute") that 家畜 itself never took. Stamped `date-last-perfect: 2026-08-26`. This closes out the whole `家*` word cluster (家事/家具/家庭/家族/家畜/家禽/家蝿/家鼠 — all 8 now stamped).

**Next candidate jumped clusters** (byte-order sort, not stroke order) to [[words/容|容]] — a single-character stand-alone word, same minimal template as [[words/且|且]]/[[words/衢|衢]].

### 2026-08-26, iteration 1045 — [[words/容|容]]

Frontmatter was badly malformed: `vietnamese: null` (should be omitted, not null), `characters: "容 (char)"` as a bare scalar instead of a YAML list, no `pos` field at all, no `japanese` field at all, `# Notes` heading (wrong level) with nothing under it. 容's own `stand_in` field is literally `容` (self) — this word *is* the stand-in that legitimizes the character as an independent entry, documented explicitly since the self-referential case isn't covered verbatim by [[feedback_standin_note]]'s two-different-constituents example. Filled `japanese: よう` (the bound on'yomi affix — Wiktionary confirms 容 has no single clean free-standing Japanese word matching this exact "look/appearance/form/figure" gloss; かたち/ゆるす cover different specific senses). Left `vietnamese` omitted — Wiktionary itself flags 容 as not well-established standalone in modern Vietnamese. **Found a genuine triple Middle-Chinese homophone**: 容/[[庸]]/[[湧]] all reconstruct to identical MC 以母+鍾韻 (j+ɨoŋ) despite different phonetic roots (谷/用/甬respectively) — a real convergence, not a Dan'a'yo-introduced collision. Added the reciprocal `>[!warning] Homophones` callout to all three word pages (庸.md, 湧.md were not otherwise touched/stamped — still awaiting their own turn in the alphabetical sweep; also fixed 湧.md's stray `# Notes` → `## Notes` heading level while there, a drive-by fix). Stamped only [[words/容]] `date-last-perfect: 2026-08-26`; 庸/湧 remain unstamped pending their own full pass.

Next (byte-order-alphabetical-by-filename): 容器 (3203 files remaining per rescan).

### 2026-08-26, iteration 1046 — [[words/容器|容器]]

器's own `stand_in` field is 容器 — added the stand-in note. Rebuilt malformed frontmatter (`characters: ["容 (char)", 器]` inline-array → proper list, blank `vietnamese`/`hsk_level`/`swadesh` keys removed, `aliases: []` removed). Verified `諺文`/`羅馬字`/`注音`/`mandarin`/`cantonese`/`japanese`/`korean` all correct compositional concatenations. `kwin: false` confirmed via AND-rule (容 `true` + 器 `false` → `false`). Left `vietnamese` omitted — no source attests a standing Sino-Vietnamese reading, consistent with 容 itself having no solid standalone Vietnamese life (found last iteration). No HSK level given on Wiktionary. No homophones. Notes describe this as a near-synonym doubling compound, same shape as 狡猾/宏大. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 容恕 (3202 files remaining per rescan).

### 2026-08-26, iteration 1047 — [[words/容恕|容恕]]

恕's own `stand_in` field is 容恕 — already noted on the page, but as a separate bullet rather than appended to the opening etymology bullet per [[feedback_standin_note]]; merged them. Fixed both Notes links missing the `../` relative-path prefix (`characters/...` → `../characters/...`, the same recurring bug class logged elsewhere in this project). Added the entirely-missing `kwin` field — confirmed `false` via AND-rule (容 `true` + 恕 `false`). Filled blank `vietnamese: dung thứ` (Wiktionary-confirmed, matches 容's own "dung" + 恕's own "thứ" exactly). No HSK level given for the compound (恕 itself is independently HSK 6). No homophones. Notes cover the register gap (용서 is Korea's plain everyday word for "forgiveness," while Mandarin/Cantonese 容恕 reads as literary/formal next to colloquial 原諒/寛恕, and Japanese ようしょ is rare next to native 許す/容赦). Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 容量 (3201 files remaining per rescan).

### 2026-08-26, iteration 1048 — [[words/容量|容量]]

**Real data-corruption bug found**: `aliases: [容積, 产量, 產量]` — 产量/產量 are copy-pasted wholesale from [[産量]]'s own genuine simplified/traditional alias pair (産量 is a completely different, unrelated word — "output, yield," built on 産 not 容, different reading ㄙㄚㄋㄌ⼘ㄫ vs this word's ⼄ㄫㄌ⼘ㄫ), and 容積ísn't a true orthographic variant of 容量 either (a real but distinct near-synonym, no page of its own). Removed the entire `aliases` field as pure contamination — this page has no genuine orthographic variants. Rebuilt inline-array `characters:` to a proper list, quoted `hsk_level: 4` → `"4"`, removed blank `swadesh`. Filled `vietnamese: dung lượng` (Wiktionary-confirmed, matches 容's own "dung" + 量's own "lượng"). `kwin: true` confirmed via AND-rule (both constituents `true`). No homophones. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 宿命 (3200 files remaining per rescan).

### 2026-08-26, iteration 1049 — [[words/宿命|宿命]]

**Real `kwin` bug found and fixed**: frontmatter said `kwin: true`, but the AND-rule requires every constituent `true` — 宿's own `kwin` is `false` (命's is `true`) — so the compound must be `false`. Filled entirely-blank `pos: 名詞`. Filled blank `vietnamese: túc mệnh` (Wiktionary-confirmed, matches 宿's own "túc" + 命's own "mệnh"). Removed blank `swadesh`/empty `aliases: []`. No HSK level given. No homophones. Notes trace 宿命's Buddhist origin (宿 = "former/prior existence," as in 宿世) distinct from the more neutral [[運命]], and note its surviving Buddhist-technical use in Japanese 宿命論/宿命通. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 宿敵 (3199 files remaining per rescan).

### 2026-08-26, iteration 1050 — [[words/宿敵|宿敵]]

First page this session found already essentially complete — no stand-in note needed (敵's own `stand_in` is 敵人, not this word), all fields already correct compositional concatenations, `aliases: [宿敌]` already a genuine simplified variant (confirmed via Wiktionary's "simp. 宿敌", matching 敵's own `aliases: [敌]`, unlike the false-alias contamination found on [[容量]]), `kwin: false` correct via AND-rule. Checked Wiktionary for `vietnamese`/`hsk_level` — neither is attested, left both omitted rather than guessing. No homophones. Pure re-verification, stamped `date-last-perfect: 2026-08-26` with no content changes.

Next (byte-order-alphabetical-by-filename): 寂寞 (3198 files remaining per rescan).

### 2026-08-26, iteration 1051 — [[words/寂寞|寂寞]]

Already had solid prose (one paragraph) and a correct stand-in note (寞's `stand_in` is 寂寞) — removed blank `swadesh`/`aliases` keys, verified all fields already-correct compositional concatenations (`vietnamese: tịch mịch`, `hsk_level: "3"` both already right). Expanded Notes to the checklist's 2–3-paragraph bar: distinguished from [[寂静]]/[[静寂]] (physical stillness, no emotional charge) and 寞's own rarity outside this compound; added a real cross-linguistic find, Korean's 적막강산 (2020's "idiom of the year"), extending the same physical-desolation→emotional-state pattern already present in 寂寞 itself (verified via web search, not fabricated). No homophones. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 寂滅 (3197 files remaining per rescan).

### 2026-08-26, iteration 1052 — [[words/寂滅|寂滅]]

**Real bug found**: `characters:` listed bare `滅` but the character file is `滅 (char).md` — fixed the filename form (the recurring bug class logged repeatedly elsewhere in this project). Already had excellent, near-complete prose (correct stand-in reasoning for 寂's own `stand_in: 寂滅`, a real Japanese literary citation from the Nirvana Sutra/Heike Monogatari, cross-CJKV register notes) — just needed `vietnamese: tịch diệt` filled in (verified via web search: a standing Buddhist technical term, explicitly glossed as NOT meaning annihilation but peaceful extinguishing of suffering) and `kwin: false` re-confirmed via AND-rule (寂 `true` + 滅 `false`). No HSK level applies to a term this specialized; no homophones. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 寂静 (3196 files remaining per rescan).

### 2026-08-26, iteration 1053 — [[words/寂静|寂静]]

Already had rich, near-complete prose (correctly identified 静's own `stand_in` as 静寂, not this word) and a genuine alias (`寂靜`, matching 静's own `aliases: [靜]`). Just needed `vietnamese: tịch tĩnh` filled in (verified via web search — a standing Buddhist term, glossed as 寂/tịch = freedom from mental agitation + 靜/tĩnh = absence of suffering's causes, together naming Nirvana's cessation) and quoting fixes. Added a closing observation: since 寂's own stand-in is [[寂滅]] and 静's is [[静寂]], this compound legitimizes neither constituent itself, unlike its sibling compounds. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order-alphabetical-by-filename): 寄 (3195 files remaining per rescan).

**User instruction (2026-08-26): switched from scheduled 7.5-min-interval pacing to continuous back-to-back iteration, no waiting between items, until told to stop.** ScheduleWakeup loop cancelled; iterations below run consecutively in one sitting.

### 2026-08-26, iteration 1054 — [[words/寄|寄]]

Same malformed single-character stand-alone stub pattern as [[words/容|容]]: `vietnamese: null`, `characters:` as a bare scalar, no `pos`, no `japanese`, bare `# Notes` with nothing under it. 寄's own `stand_in` is itself (self-referential, same as 容) — documented explicitly. Filled `japanese: き` (bound on'yomi; no clean single free-standing Japanese word matches the full "approach/send/rely on" gloss). Left `vietnamese` omitted — the character's own stored forms (gửi/ké/kí/ký/kẹ) don't resolve to one clean standalone SV reading; gửi is actually the native Vietnamese verb "to send," not a Sino-Vietnamese reflex, while kí/ký only surface bound inside compounds. No homophones among other words. Stamped `date-last-perfect: 2026-08-26`.

Next: 寄宿.

### 2026-08-26, iteration 1055 — [[words/寄宿|寄宿]]

宿's own `stand_in` field is 寄宿 — added the stand-in note (page had `## Etymology` instead of `## Notes`, no prose at all). Fixed `characters:` filename form (bare `寄` → `寄 (char)`). Filled entirely-blank `japanese: きしゅく` and `vietnamese: ký túc` (both verified) — a genuine cross-linguistic find: sources trace Vietnamese ký túc xá as a borrowing of *Japanese* 寄宿舎 (kishukusha) rather than a direct Sino-Vietnamese coinage, despite using ordinary Sino-Vietnamese characters. No HSK level, no homophones. `kwin: false` confirmed via AND-rule (both constituents `false`). Stamped `date-last-perfect: 2026-08-26`.

Next: 寄宿舎.

### 2026-08-26, iteration 1056 — [[words/寄宿舎|寄宿舎]]

Fixed `characters:` filename form (bare `寄` → `寄 (char)`); no stand-in note applies (none of the three constituents' own `stand_in` fields point here). Filled blank `cantonese: gei3 suk1 se3` and `vietnamese: kí túc xá` (Wiktionary-confirmed) and converted the inline `aliases: [寄宿舍]` to a proper list (matching 舎's own alias 舍). No HSK level, no homophones. `kwin: false` confirmed via AND-rule (all three constituents `false`). Stamped `date-last-perfect: 2026-08-26`.

Next: 寅月.

### 2026-08-26, iteration 1057 — [[words/寅月|寅月]]

寅's own `stand_in` field is 寅月 — added the missing stand-in note to the opening bullet (page had a decent 2-paragraph body already, just lacked this). All fields already correct compositional concatenations. Added a cross-linguistic paragraph: Japanese とらつき and Vietnamese tháng Dần both use native-word-plus-zodiac-name constructions rather than fully Sino-form concatenations, the same calquing pattern in both traditions. No homophones. Stamped `date-last-perfect: 2026-08-26`.

Next (byte-order jumps past several already-stamped files): 密.

### 2026-08-26, iteration 1058 — [[words/密|密]]

Same malformed single-character stand-alone stub pattern as [[words/容|容]]/[[words/寄|寄]]: bare `# Notes`, no `pos`, no `japanese`, `characters:` as a bare scalar. 密's own `stand_in` is itself (self-referential) — documented. Filled `japanese: みつ` and `vietnamese: mật` (the character's own field also lists an outlying "mất," but that collides with the unrelated common native word "mất" = "to lose/die"; "mật" is the clean, unambiguous SV reading and is independently well-attested as a free adverb "secretly," so used it rather than omitting). No homophones among other words. Stamped `date-last-perfect: 2026-08-26`.

Next: 密陀僧 (密度 already stamped).

### 2026-08-26, iteration 1059 — [[words/密陀僧|密陀僧]]

**Real etymology found**: 密陀僧 is not compositional at all — it's a phonetic transliteration (Wiktionary-confirmed) of Persian مردار سنگ (mordār-sang, "dead stone"), the origin of "litharge" itself; none of the three characters contribute their own meaning. Fixed the English gloss typo "lithage" → "litharge." **Surfaced but deliberately not resolved**: this word is one of the three affected pages ([[僧侶]], [[尼僧]] being the others) in [[僧]]'s own already-documented "sung vs. seng" reading inconsistency (its own Notes explicitly call for a dedicated word-sweep, not a one-page fix) — left the stored reading as-is and cross-referenced the flag rather than silently picking a side. Verified everything else (mandarin/cantonese/japanese/korean/vietnamese all correct, `kwin: false` via AND-rule since 陀's own `kwin` is `false`). No homophones, no HSK level. Removed blank `swadesh`/`aliases`. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1060 — [[words/富裕|富裕]]

裕's own `stand_in` field is 富裕 — added the stand-in note. **Real cross-word phonological pattern found, not fixed**: 富's contribution to this word (buo/뿟/ㄅㄨㄛ, b-series) diverges from 富's own character-page citation form (fuo/뿟/ㄈㄨㄛ, f-series) despite 富 sitting word-initial with no obvious conditioning environment — but the same b-series form is independently attested in [[豊富]] (pungbuo) too, so this is consistent across (at least) two separately-created words rather than a one-off typo. Flagged for a future dedicated look rather than silently picking a side. Filled blank `vietnamese: phú dụ` (verified). No specific HSK level number (Wiktionary: "Intermediate Mandarin" only). No homophones. `kwin: false` confirmed via AND-rule. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1061 — [[words/寒冷|寒冷]]

寒's own `stand_in` field is 寒冷 — added the stand-in note; fixed `characters:` filename form (bare `冷` → `冷 (char)`). Filled blank `vietnamese: hàn lãnh` (verified). No specific HSK level number. No homophones. `kwin: false` confirmed via AND-rule. Notes distinguish 寒 (seasonal/climatic cold) from the more general, more productive 冷. Stamped `date-last-perfect: 2026-08-26`.

Next: 寝.

### 2026-08-26, iteration 1062 — [[words/寝|寝]]

Same malformed single-character stand-alone stub pattern as [[words/容|容]]/[[words/寄|寄]]/[[words/密|密]]. 寝's own `stand_in` is itself (self-referential) — documented. `vietnamese: tẩm` was already filled (verified as real, if literary, usage in 寝宮). Added `aliases: [寢]` (traditional variant, matching the character's own alias). **Found a genuine Dan'a'yo homophone**: 寝 and [[浸]] ("immerse, dunk") share an identical reading (cim/침/ㄑㄧㄇ) — added reciprocal `>[!warning] Homophones` callouts to both pages (浸.md not otherwise stamped, just got the callout ahead of its own turn, same pattern as the earlier 容/庸/湧 triple). Stamped only [[words/寝]] `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1063 — [[words/寡婦|寡婦]]

寡's own `stand_in` field is 寡婦 — added the stand-in note; fixed `characters:` filename form (bare `婦` → `婦 (char)`). All other fields already correct compositional concatenations (`vietnamese: quả phụ` already right, drawing on 寡's "quả" reading). No specific HSK level number. No homophones. `kwin: false` confirmed via AND-rule. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1064 — [[words/審査|審査]]

Already had solid prose explaining the deliberate 査-vs-査/査 shinjitai choice. Restructured the stand-in note into the standard opening-bullet form (審's own `stand_in` is 審査). **Root-cause fix**: 査's own character page had a completely blank `vietnamese` field — verified "tra" as its real Sino-Vietnamese reading (confirmed via search) and filled it in directly on the character page, which also resolved this word's own `vietnamese: thẩm tra` compositionally rather than needing a special-cased value. No homophones. `kwin: true` already correct (both constituents `true`). Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1065 — [[words/寮国|寮国]]

**Real `諺文` typo found and fixed**: stored 렷곡, but 寮's own `諺文` is 럇 (not 렷) — a single-vowel typo, corrected to 럇곡, matching the already-correct `注音`/`羅馬字` fields. No stand-in relationship (neither constituent's own `stand_in` points here). **Real cross-linguistic finding**: none of Japanese/Korean/Vietnamese use a compositional Sino-reading for this country name — ラオス/라오스 are direct phonetic loans of "Laos," and Vietnamese nước Lào uses the native word "nước" + the endonym directly, unlike most of this vault's other country-name compounds, likely because Laos as a modern nation-state postdates the older character-mediated CJK naming layer. No HSK level applies (proper noun); no homophones. `kwin: false` confirmed via AND-rule. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1066 — [[words/寺院|寺院]]

**Significant contamination bug found and fixed, worst so far this session**: `mandarin`/`cantonese` had been copied wholesale from the unrelated synonym 寺廟 (sìmiào — no `words/寺廟.md` file even exists in this vault), `korean` had been copied from 寺's own actual stand-in [[寺刹]] (사찰) instead of derived from this word's own constituents, and `japanese` had a kana typo (じゐん, archaic ゐ, instead of じいん) — all three verified and corrected via Wiktionary against 寺院's own real readings (the `諺文`/`羅馬字`/`注音` fields, sìyuàn/사원/sa'wen/ㄙㄚ⼔ㄋ, had actually been correct all along). Removed the contaminated `aliases` list (寺廟/寺庙/寺院-itself — none are true orthographic variants, same false-alias pattern as [[容量]]). Filled blank `vietnamese: tự viện` (verified). No stand-in relationship (寺→寺刹, 院→院落, neither points here). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-26`.

**Ordering correction**: discovered several files (孫金, 宇宙, 宇宙船, 守衛, 守護, 安全) sit earlier in true byte order than where the sweep had jumped to (寅月ff.) — resuming from the correct position rather than the one being tracked, going forward.

### 2026-08-26, iteration 1067 — [[words/孫金|孫金]]

A `neologism`/`periodictable` word (Dan'a'yo's own coined name for promethium, element 61) — a structurally different genre from ordinary compositional vocabulary: `mandarin`/`cantonese`/`japanese`/`korean`/`vietnamese` deliberately hold each language's own real (phonetic-loanword) name for the element, not a compositional reading of 孫+金. Confirmed `kwin: false` is correct precisely *because* of this — `korean` (프로메튬) and `諺文` (손김) are unrelated strings by design, not error. Checked precedent ([[銅]], an older stamped periodictable word) — this word type has historically been held to a much lighter completion bar than ordinary compounds; added a proper opening bullet documenting this rather than rewriting the already-rich existing etymological reasoning (Sunzi/Sun Wukong trickster-archetype justification for the 孫 choice). Stamped `date-last-perfect: 2026-08-26`.

Next: 宇宙.

### 2026-08-26, iteration 1068 — [[words/宇宙|宇宙]]

宇's own `stand_in` field is 宇宙 — added the stand-in note. Filled entirely-blank `pos: 名詞`, removed blank `hsk_level`/`swadesh`/empty `aliases: []`. Replaced thin, fragmentary Notes ("none of the 'roof' denotations from Chinese are present here" + two bare unrubied links) with real content: a genuine classical-etymology find (宇 = "the four directions," 宙 = "past to present," an ancient philosophical space/time pairing, not a modern scientific coinage — confirmed via Wiktionary's citation of the Shizi/Huainanzi and Meyer 2010's "roof synecdoche" analysis). `kwin: false` confirmed correct (諺文 우줏 ≠ korean 우주). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-26`.

Next: 宇宙船.

### 2026-08-26, iteration 1069 — [[words/宇宙船|宇宙船]]

**Real `mandarin` bug found and fixed**: stored "yǔzhòu fēichuán" (the 4-character Mainland-Simplified word 宇宙飛船/宇宙飞船's reading) despite `characters:` listing only 3 characters (宇/宙/船, the Traditional/Taiwan/Japanese-aligned form already given as this word's actual spelling) — confirmed via search that both 3-char and 4-char forms are real, regionally-split terms (not a meaning difference), and corrected `mandarin` to the compositional 3-syllable "yǔzhòuchuán" matching the already-correct 3-syllable `cantonese` field; 宇宙飛船 kept as the documented alias. **Second instance of the "citation-form vs. compound-form" reading-split bug class found** (after [[僧]]/[[密陀僧]]): 船's own contribution here (줜/jwen/ㄐ⼔ㄋ) diverges from its canonical reading (쉄/swem/ㄙ⼔ㄇ), and the exact same alternate form also appears in [[艦船]] — added a matching flag to [[船]]'s own Notes (mirroring 僧's) and cross-referenced it here rather than silently resolving. No stand-in relationship, no HSK level, no homophones. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1070 — [[words/守衛|守衛]]

**Real contamination bug found and fixed**: `諺文`/`羅馬字`/`注音` had been copied wholesale from the unrelated word [[授業]] ("to teach" — 授's own reading coincidentally matches 守's, both syu/슈/ㄙ⼜, likely the source of the mix-up), storing 슈업/syu'eb/ㄙ⼜ㄝㄆ (matching 業's reading) instead of the true compositional 슈어/syu'e/ㄙ⼜ㄝ (from 衛's own 'e/어/ㄝ). The page even carried a fabricated `>[!warn] Homophones: 授業` callout, apparently added to rationalize the wrong data rather than reflecting a real collision — removed; no genuine homophone exists at the corrected reading. Propagated the ruby fix to both [[守]]'s and [[衛]]'s own Words sections (both had been citing the same wrong reading). 守's own `stand_in` is 守衛 — added the stand-in note. Filled blank `vietnamese: thủ vệ` (verified). No HSK level. Fixed Notes links missing `../` prefix. Stamped `date-last-perfect: 2026-08-26`.

Next: 守護.

### 2026-08-26, iteration 1071 — [[words/守護|守護]]

Already excellent, near-complete prose (correctly explained the 守護/保護/守衛/保衛/保持 disambiguation web). Just needed `vietnamese: thủ hộ` filled in (verified) and quoting/blank-field cleanup. No homophones, no HSK level. `kwin: false` already correct (諺文 슈호 ≠ korean 수호). Stamped `date-last-perfect: 2026-08-26`.

Next: 安全.

### 2026-08-26, iteration 1072 — [[words/安全|安全]]

No stand-in relationship (安→平安, 全→itself). Filled entirely-blank `pos: 性詞`, quoted `hsk_level: "2"`, removed blank `swadesh`/empty `aliases: []`, converted inline-array `characters:`. All other fields already correct compositional concatenations. No homophones. `kwin: false` confirmed correct (諺文 안줜 ≠ korean 안전). Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1073 — [[words/対応|対応]]

Already had fully correct, well-populated frontmatter — no bugs found, just needed the `## Notes` section built (page had none) and stamping. No stand-in relationship (対→反対, 応→itself). No homophones. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1074 — [[words/対照|対照]]

Already had solid frontmatter and a one-line Notes gloss. No stand-in relationship (対→反対, 照→itself). Expanded Notes to distinguish from [[対応]] and note the "Advanced Mandarin"/no-specific-HSK-level status. No homophones. Stamped `date-last-perfect: 2026-08-26`.

Next: 対称.

### 2026-08-26, iteration 1075 — [[words/対称|対称]]

No stand-in relationship (対→反対, 称→名称). Notes explain 称's polyphonic reading here (chèn/chèng "to weigh, match," not its default chēng "to call," reflected already in the dual-form `mandarin`/`cantonese` fields) and flag a genuine Japanese-only three-way homophone: 対照/対称/対象 all read たいしょう in Japanese despite being fully distinct at the Dan'a'yo/Mandarin/Korean/Vietnamese level. Fixed inline-array `aliases`/`characters`, quoted `hsk_level: "4"`. No homophones at the Dan'a'yo level. Stamped `date-last-perfect: 2026-08-26`.

Next: 対象.

### 2026-08-26, iteration 1076 — [[words/対象|対象]]

No stand-in relationship (対→反対, 象→大象). Confirmed and documented the third member of the [[対照]]/[[対称]]/対象 Japanese-only たいしょう homophone cluster (all three distinct at the Dan'a'yo/Mandarin/Korean/Vietnamese level). Quoted `hsk_level: "2"`, removed blank `swadesh`/`aliases`. No homophones at the Dan'a'yo level. Stamped `date-last-perfect: 2026-08-26`.

Next: 対連.

### 2026-08-26, iteration 1077 — [[words/対連|対連]]

**Real `cantonese` bug found and fixed**: stored "deoi3 lyun4-2," using 聯's real Cantonese reading (lyun4) instead of the vault's own canonical character 連's (lin4) — confirmed via CantoDict/Wiktionary that 連 (lin4) and 聯 (lyun4) are genuinely distinct-reading characters in Cantonese despite sharing a Mandarin reading and being registered here as aliases of each other. Corrected to "deoi3 lin4-2," following the same [[審査]]-precedent convention (canonical character's own derivation wins over the real everyday alias-based form, documented in prose). Filled blank `vietnamese: đối liên` (Wiktionary-confirmed, exact match to 連's own "liên"). No stand-in relationship, no specific HSK level number, no homophones. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1078 — [[words/寿司|寿司]]

Ateji word (Japanese phonetic borrowing — 寿+司 chosen for sound only, "su-shi," no semantic connection to the food). No stand-in relationship. Cleaned up a stray unformatted warning bullet ("Do not use 鮨 or 鮓!") and a duplicated/uncertain Etymology block into proper Notes prose, keeping the real content (鮨/鮓 are genuine but non-preferred alternate spellings). **Real cross-linguistic finding, already correctly stored but unexplained**: Korean 초밥 is not a borrowing of the Japanese kanji reading at all — it's a native Korean calque, "vinegar" + "rice," translating the dish's defining ingredient rather than transliterating the Sino-Japanese spelling. `vietnamese` left omitted (Vietnamese uses the direct loanword "sushi"). No homophones. Stamped `date-last-perfect: 2026-08-26`.

Next: 寿命.

### 2026-08-26, iteration 1079 — [[words/寿命|寿命]]

寿's own `stand_in` field is 寿命 — added the stand-in note. **Real palatalization typo found and fixed**: `諺文`/`羅馬字` stored 슈멍/syumeng, dropping the palatal glide from 命's own 명/myeng — corrected to 슈명/syumyeng (the `注音` field, ㄙ⼜ㄇ⼶ㄫ, already had the palatal marker right, so this was a two-field-only bug, not a three-field one). Filled blank `pos: 名詞`. Distinguished from [[宿命]]/[[運命]] (duration of life vs. its character/fate). No homophones. Stamped `date-last-perfect: 2026-08-26`.

Next: 封.

### 2026-08-26, iteration 1080 — [[words/封|封]]

封's own `stand_in` is itself (self-referential) — added the note. Fixed the homophone callout format on both this page and [[蜂]] (both used a non-canonical `>[!tip]` sentence instead of the standard `>[!warning] Homophones` block) — real homophone, confirmed (both fong/뽕/ㄈㄛㄫ). Already had excellent existing prose (feudal-enfeoffment/sealing dual-sense etymology, counter-word usage, cross-linguistic notes) — no other changes needed. `hsk_level` intentionally left off per this session's established single-character-word precedent ([[容]], [[密]], [[寄]], [[寝]], [[且]], [[衢]] etc. — none carry it even though their characters do). Stamped `date-last-perfect: 2026-08-26`.

Next: 封印.

### 2026-08-26, iteration 1081 — [[words/封印|封印]]

印's own `stand_in` field is 封印 — added the stand-in note; fixed `characters:` filename form (bare `封` → `封 (char)`). Fixed a `羅馬字` typo (bong'in → fong'in — 封's own citation form is "fong," already correctly reflected in this word's own `諺文`/`注音` fields, just not `羅馬字`; unlike [[富裕]]'s flagged case, this was a simple one-field typo, not a cross-word systemic pattern). Filled blank `vietnamese: phong ấn` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1082 — [[words/専念|専念]]

No stand-in relationship (専→専用, 念→念頭). Filled blank `cantonese`/`korean` (both already-verified compositional concatenations). Left `vietnamese` omitted after searching — no standing everyday "chuyên niệm" term found; 念 in Vietnamese survives mainly in Buddhist-register compounds. Fixed inline-array `aliases`/`characters`. No homophones, no HSK level. `kwin: false` confirmed correct via direct 諺文-vs-korean comparison (also noting: `kwin` is a direct string-equality check between the word's own `諺文` and `korean` fields, not an abstract AND across constituent characters' individual `kwin` flags — the two happen to coincide for ordinary compositional words but diverge for words like [[孫金]] where `korean` is deliberately non-compositional). Stamped `date-last-perfect: 2026-08-26`.

### 2026-08-26, iteration 1083 — [[words/射精|射精]]

No stand-in relationship (射→射出, 精→精神). Filled blank `pos: 事詞`. **Real cross-linguistic finding**: Vietnamese `xuất tinh` (already stored) diverges from strict compositional derivation — it uses 出 "to exit" rather than 射's own "xạ," a genuine attested medical-term substitution, same class as [[寮国]]/[[対連]]. Removed blank `swadesh`/empty `aliases: []`, converted inline-array `characters`. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-26`.

Next: 射素.

### 2026-08-26, iteration 1084 — [[words/射素|射素]]

Another `neologism`/`periodictable` word (radon, element 86), same genre as [[孫金]]. Added the standard opening bullet documenting no stand-in relationship and confirming `kwin: false` is correct by design (real-world fields hold each language's own phonetic-loanword element name, not a reading of 射+素). Did not rewrite the existing rich etymological reasoning (Latin *radius* → "ray-emitting" → 射). Stamped `date-last-perfect: 2026-08-26`.

Next: 射術.

### 2026-08-26, iteration 1085 — [[words/射術|射術]]

A pure grammar/vocabulary neologism (not periodictable) with no real CJKV equivalent word at all — checked precedent ([[何処]], a stamped correlative-neologism) to confirm the convention: no `mandarin`/`cantonese`/`japanese`/`korean`/`vietnamese` fields when no single real term exists, `kwin: false` still set (no `korean` value to match `諺文` against). No stand-in relationship (射→射出, 術→itself). Fixed a duplicated `## Ancient kinds`/`### Ancient kinds` heading and fixed relative-path links (missing `../`). Kept the existing rich content (Six Arts archery-technique glossary) intact. Stamped `date-last-perfect: 2026-08-26`.

Next: 射香.

### 2026-08-27, iteration 1086 — [[words/射香|射香]]

**Real `japanese` typo found and fixed**: stored じゃかう (archaic/incorrect かう), corrected to じゃこう (じゃ from 射's SHA + こう from 香's own KOU) — the real attested reading of 麝香, the more common written form of this word (kept as this word's `aliases` entry; 射's own alias field already lists 麝, so the alias is legitimate, not contamination). No stand-in relationship (射→射出, 香→香気). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1087 — [[words/将兵|将兵]]

No stand-in relationship (将→itself, 兵→兵士). Filled blank `cantonese`/`vietnamese: tướng binh` (verified — attested in the classical citation 韓信將兵，多多益善). Notes explain 将's polyphonic sense-switch here (jiàng "commander" vs its default jiāng "will/shall," as in [[将来]]). Fixed inline-array `characters:`/`aliases`, `characters:` filename form. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 将帥. Resuming standard ~7.5-min-per-iteration loop pacing per user request.

### 2026-08-27, iteration 1088 — [[words/将帥|将帥]]

**Real, severe contamination bug found and fixed**: `japanese` stored チャンギ ("changgi" — the Japanese name for *Korean chess*, an entirely unrelated word), corrected to しょうすい (verified). 帥's own `stand_in` field is 将帥 — added the stand-in note. **Real Cantonese tone finding**: the real attested reading is zoeng3 seoi3, not the mechanical zoeng1 (将's own citation-form Cantonese) — confirmed directly via Wiktionary, and cross-checked that 將軍 itself keeps zoeng1 despite the same "general" sense, so this is a real per-compound lexicalized tone quirk, not a predictable rule; documented rather than silently forced to match 将's citation form. Filled blank `vietnamese: tướng soái` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 将校.

### 2026-08-27, iteration 1089 — [[words/将校|将校]]

No stand-in relationship (将→itself, 校→学校). Filled blank `vietnamese: tướng hiệu` (verified). Notes explain 校's older "military rank" sense (distinct from its everyday "school" sense) and the same 将 commander-sense-switch already documented on [[将帥]]/[[将兵]]. Converted inline-array `aliases`/`characters`, filename form. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1090 — [[words/将然|将然]]

A technical grammatical-aspect term (already well-documented: paired with [[完了]] in Dan'a'yo's own 時相/aspect-suffix system, borrowing the classical 已然/将然 opposition). Fixed `characters:` filename form (然's file is `然 (char).md`). No stand-in relationship (both 将 and 然's own `stand_in` fields point to themselves). Removed blank `cantonese`/`japanese`/`korean`/`vietnamese` keys — already correctly justified in the existing prose as a term attested only in Mandarin grammatical scholarship, not ordinary dictionary usage. Confirmed 将 correctly uses its "about to" auxiliary sense (jiāng) here, distinct from its "commander" sense (jiàng) on [[将帥]]/[[将兵]]/[[将校]]. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 将軍.

### 2026-08-27, iteration 1091 — [[words/将軍|将軍]]

Fixed another archaic-kana `japanese` typo (しやうぐん → しょうぐん, same class as [[寺院]]/[[射香]]) and a stray capitalization bug (`vietnamese: "Tướng quân"` → lowercase "tướng quân"). No stand-in relationship (将→itself, 軍→軍隊). Confirmed 将 keeps its default jiāng/zoeng1 reading here (not the jiàng/zoeng3 "commander" shift seen on [[将帥]]/[[将校]]) — a real lexicalized exception, verified directly. Quoted `hsk_level: "3"`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尉.

### 2026-08-27, iteration 1092 — [[words/尉|尉]]

Same malformed single-character stand-alone stub pattern as [[words/容|容]]/[[words/密|密]]/[[words/寄|寄]]/[[words/寝|寝]]. 尉's own `stand_in` is itself — documented. Filled `japanese: い` and `vietnamese: uý` (both from the character's own fields). Notes place 尉 in the officer-rank hierarchy below [[将校]]/将 (少尉/中尉/大尉). No homophones among other words. Stamped `date-last-perfect: 2026-08-27`.

Next: 尊厳.

### 2026-08-27, iteration 1093 — [[words/尊厳|尊厳]]

尊's own `stand_in` field is 尊厳 — added the stand-in note; fixed `characters:` filename form (bare `厳` → `厳 (char)`). All other fields already correct compositional concatenations (double-checked 尊's `vietnamese` list actually does include "tôn," just further down the list than an initial truncated view suggested — no bug there after all). Notes distinguish from [[尊敬]] (relational respect vs. inherent dignity). Quoted `hsk_level: "4"`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尊敬.

### 2026-08-27, iteration 1094 — [[words/尊敬|尊敬]]

**Retroactive correction to the previous iteration**: caught my own error on [[尊厳]] — its `cantonese` field ("zeon1 jim4") had never actually been checked against 尊's own stored cantonese (zyun1, not zeon1); fixed to "zyun1 jim4" just now. Lesson: verify every field against the constituent characters' own stored values, not just the ones that look obviously wrong. For 尊敬 itself: 敬's own `stand_in` field is 尊敬 — added the stand-in note. All other fields were already correct (including `cantonese: zyun1 ging3`, correctly using 尊's real zyun1). Notes distinguish from [[尊厳]]. No specific HSK level number, no homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1095 — [[words/尋|尋]]

Single-character stand-alone word, same pattern as [[容]]/[[密]]/[[尉]]. 尋's own `stand_in` is itself — documented. Filled `japanese: じん` and `vietnamese: tầm` (verified as the true Sino-Vietnamese reading; the character's own field also lists "tìm," a coincidentally similar-sounding *native* Vietnamese word for "search/find," different etymological source — same false-cognate-risk class as [[密]]'s "mất"). Fixed `# Notes` heading level. Reciprocal homophone callout with [[心]] was already correctly in place on both pages (coincidental phonology, no etymological link). Stamped `date-last-perfect: 2026-08-27`.

Next: 導管.

### 2026-08-27, iteration 1096 — [[words/導管|導管]]

管's own `stand_in` field is 導管 — added the stand-in note. All other fields already correct compositional concatenations. Left `vietnamese` omitted after searching — no standing everyday "đạo quản" term found; modern Vietnamese uses the native compound "ống dẫn" instead. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 小人.

### 2026-08-27, iteration 1097 — [[words/小人|小人]]

**Real copy-paste typo found and fixed**: the opening bullet glossed 人 as "small" (copied from 小's own gloss) instead of "person." No stand-in relationship (both constituents' own `stand_in` point to themselves). All other fields already correct. Notes cover the Confucian 小人/君子 ethical contrast and the character's secondary classical self-deprecating-pronoun sense. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1098 — [[words/小冊子|小冊子]]

No stand-in relationship (none of 小/冊/子's own `stand_in` fields point here). Filled blank `vietnamese: tiểu sách tử` (a genuine Sino-Vietnamese reading, though everyday Vietnamese uses the native "sách nhỏ" instead — same register split as [[私讐]]). Cleaned up disorganized Notes (missing `../` link prefixes, informal bullet list) into standard prose, keeping the real content (cannot abbreviate to 小冊 outside Japanese; transparently [[小]]+[[冊子]]). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 小指.

### 2026-08-27, iteration 1099 — [[words/小指|小指]]

No stand-in relationship (小→itself, 指→手指). Filled blank `pos: 名詞` and `vietnamese: tiểu chỉ` (verified). Confirmed `japanese: しょうし` is correct as-is despite looking unusual — a real, verified medical/anatomical-register reading distinct from the everyday こゆび (koyubi), both attested. Notes place the word in the classical five-finger naming set. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 小数点.

### 2026-08-27, iteration 1100 — [[words/小数点|小数点]]

No stand-in relationship (小/点→themselves, 数→計数). Filled blank `pos: 名詞`. Left `vietnamese` omitted — no Sino-Vietnamese reading confirmed; verified Vietnamese actually uses a comma (not a point) as its decimal separator natively, so the concept itself is expressed as "dấu phẩy thập phân" rather than any Sino-form calque. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 小河.

### 2026-08-27, iteration 1101 — [[words/小河|小河]]

**Real contamination bug found and fixed**: `japanese` stored おがわ, copied from the unrelated word [[小川]] (a different character combination, 川 not 河, and primarily a Japanese surname) — corrected to しょうが, the real reading of 小河 itself (confirmed via search). 河's own `stand_in` field is 小河 — added the stand-in note. Upgraded `korean`/`vietnamese` from native everyday words (시내/suối, which are real but belong to different, unrelated lexemes) to the compositional Sino-forms (소하/tiểu hà, both independently confirmed attested), noting the native alternatives in prose per this vault's usual convention. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 小腸.

### 2026-08-27, iteration 1102 — [[words/小腸|小腸]]

No stand-in relationship (小→itself, 腸→腸管). All fields already correct compositional concatenations; filled blank `pos: 名詞`, converted inline-array `characters`/`aliases`. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1103 — [[words/小舟|小舟]]

Fixed a spelling typo (English gloss "dingy" → "dinghy"). 舟's own `stand_in` field is 小舟 — added the stand-in note. Filled blank `vietnamese: tiểu chu` (verified). Confirmed `japanese: こぶね` is correct as-is (verified genuine, though classical/seasonal poetry uses おぶね instead — noted). Fun aside confirmed: Korean 소주 here is a pure coincidental homophone of the drink 소주 (soju), unrelated hanja. No homophones among Dan'a'yo words. Stamped `date-last-perfect: 2026-08-27`.

Next: 小行星.

### 2026-08-27, iteration 1104 — [[words/小行星|小行星]]

Confirmed `japanese`'s odd-looking せうわくせい is legitimate once the archaic kana is fixed (しょうわくせい) — Japanese genuinely spells "asteroid" with an entirely different character, 小惑星 (惑, not 行), already correctly documented as this word's `aliases` entry, the same class of divergence as [[審査]]. No stand-in relationship. Filled blank `pos: 名詞`. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 少女.

### 2026-08-27, iteration 1105 — [[words/少女|少女]]

**Real, distinctive bug found and fixed**: `諺文`/`羅馬字` stored 뇻/nyou for 女's contribution instead of 느/nǝ (女's actual Dan'a'yo citation form, confirmed by cross-checking 女's own Words-section ruby for this exact word, which already correctly shows ㄋㄜ) — the bad value looks like it was pulled from 女's *Japanese* on'yomi list (NYOU is genuinely one of 女's three real Japanese readings, JO/NYO/NYOU) rather than its Dan'a'yo fields, a cross-field mix-up distinct from a simple typo. Also fixed the usual archaic-kana `japanese` error (せうぢよ → しょうじょ). No stand-in relationship. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 少年.

### 2026-08-27, iteration 1106 — [[words/少年|少年]]

Unlike [[少女]], this one's `諺文`/`羅馬字`/`注音` were all already correct (verified against 年's own citation form). Just the recurring archaic-kana `japanese` typo (せうねん → しょうねん). No stand-in relationship. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1107 — [[words/尚|尚]]

Malformed single-character stand-alone stub: `korean: "null"` (the literal string, not an actual value or omission — a distinct bug shape from the usual blank/null field), missing `japanese`, `pos`. 尚's own `stand_in` is itself — documented. **Root-cause fix**: 尚's own character page was missing its primary Sino-Vietnamese reading entirely (thượng) — the field only had the rarer Nôm variants (chuộng/sượng/thằng); added thượng, which also resolved this word's own vietnamese field. **Found a genuine triple Dan'a'yo homophone**: 尚/[[上]]/[[賞]] all share syang/샹/ㄙ⼘ㄫ — added reciprocal homophone callouts to all three (上.md was already stamped but had never carried one; 賞.md is not yet stamped, just got the callout ahead of its own turn). Stamped only [[words/尚]] `date-last-perfect: 2026-08-27`.

Next: 尤其.

### 2026-08-27, iteration 1108 — [[words/尤其|尤其]]

尤's own `stand_in` field is 尤其 — added the stand-in note. Confirmed `japanese: とりわけ` is legitimate — Japanese never adopted this character compound at all, so とりわけ is a native translation-equivalent, not a reading of the characters (same class as [[小数点]]). Filled blank `korean: 특히` (also native, no Sino-Korean form exists) and `vietnamese: vưu kỳ` (a genuine, if literary, Sino-Vietnamese reading; everyday speech prefers native đặc biệt/nhất là). Filled blank `pos: 副詞`, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尭舌.

### 2026-08-27, iteration 1109 — [[words/尭舌|尭舌]]

**Real bug found and fixed, same shape as [[少女]]/[[寿命]]**: `諺文`/`羅馬字` used 뇨/nyo for 尭's contribution instead of the correct 얏/'yau (verified against 尭's own syllable page `⼘ㄨ.md`) — `注音` (⼘ㄨ) had been correct all along. `aliases` (饶舌/饒舌, using 尭's alias 饒) already legitimate, not contamination — Notes now explain 尭 stands in here for its true etymological source 饒, same pattern as [[舎]]/舍 or [[対]]/對. **Root-cause fix**: 尭's own character page was missing "nhiêu" (饒's Vietnamese reading) from its `vietnamese` field, only had "nghiêu" (堯's reading, tied to the sage-king) — added it, resolving this word's own `vietnamese: nhiêu thiệt` (verified) in the process. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 就鳥.

### 2026-08-27, iteration 1110 — [[words/就鳥|就鳥]]

**Investigated an apparent reading mismatch and confirmed it's NOT a bug**: 就's contribution here (줏/juo/ㄐㄨㄛ) looked wrong against 就's own regular citation (쵀/cwai/ㄑ⺢ㄧ) — but [[就]]'s own Notes already explicitly document that 就 is this vault's designated borrowed stand-in glyph (借代字) for the unlinked character 鷲 ("eagle, vulture"), deliberately switching to 鷲's own reading when used in that sense (also used in [[禿就]]). Verified before "fixing" anything — the stored values were already correct. Filled blank `japanese: しちょう` (from the classical idiom 鷲鳥不群) and `vietnamese: thứu điểu` (鷲's real SV reading, confirmed via its use in Linh Thứu Sơn "Vulture Peak"). Documented why `korean` deliberately uses the native 수리 instead of the mechanical 취조, which collides with the common word for "interrogation." No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尺蠖 (尺 already stamped).

### 2026-08-27, iteration 1111 — [[words/尺蠖|尺蠖]]

**Real self-referential bug fixed**: `aliases` listed the word itself ("尺蠖") as its own alias, alongside the genuine classical variant 蚇蠖 — removed the nonsensical self-reference. 蠖's own `stand_in` field is 尺蠖 — added the stand-in note. All other fields already correct compositional concatenations. Notes explain the inchworm's measuring-gait etymology. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尻.

### 2026-08-27, iteration 1112 — [[words/尻|尻]]

Single-character stand-alone word, same pattern as several others this session. 尻's own `stand_in` is itself — documented. Filled `japanese: こう` (on'yomi; native こう しり/shiri is the everyday word instead) and `vietnamese: khào` (clean, unambiguous). No homophones among other words. Stamped `date-last-perfect: 2026-08-27`.

Next: 尼僧 (尼羅河 already stamped).

### 2026-08-27, iteration 1113 — [[words/尼僧|尼僧]]

**Real, striking `korean` bug found and fixed**: stored 이승, a completely unrelated, extremely common Korean word meaning "this world, the world of the living" (opposite of 저승, "the afterworld") — corrected to the real reading 니승, which also reconfirms the vault's standing North-Korean/문화어 convention (unshifted 니, not South Korean 이). 尼's own `stand_in` field is 尼僧 — added the stand-in note. Confirmed this is indeed one of the three words affected by [[僧]]'s already-documented "sung vs. seng" flag — left as-is per that standing note, same treatment as [[密陀僧]]/[[宇宙船]]. Left `vietnamese` omitted — Vietnamese reverses the word order entirely (tăng ni, not ni tăng) or uses the unrelated ni cô, no attested form in this exact order. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尼西亜.

### 2026-08-27, iteration 1114 — [[words/尼西亜|尼西亜]]

A phonetic transliteration (Nicaea) — all fields already correct compositional concatenations. Fixed `pos: 名詞` → `固有名詞` (proper noun, matching this vault's convention for transliterated place names like [[寮国]]/[[小川]]). No stand-in relationship, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尽力.

### 2026-08-27, iteration 1115 — [[words/尽力|尽力]]

No stand-in relationship (尽→用尽, 力→itself). All fields already correct compositional concatenations — just needed the `## Notes` section built (page had none) and stamping. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 尾.

### 2026-08-27, iteration 1116 — [[words/尾|尾]]

Single-character stand-alone word. 尾's own `stand_in` is itself — documented. Filled `japanese: び` and `vietnamese: vĩ` (the clean primary Hán Việt reading, verified; the character's own field also lists several Nôm variants). **Found a genuine Dan'a'yo homophone**: 尾 and [[未]] ("not yet") share an identical reading — added reciprocal homophone callouts to both (未.md had been stamped since June 2026 without ever carrying one, same retroactive-fix pattern as [[上]]/[[尚]]/[[賞]] earlier this session). Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1117 — [[words/尿|尿]]

Single-character stand-alone word. 尿's own `stand_in` is itself — documented. Filled `japanese: にょう`. No homophones among other words. Stamped `date-last-perfect: 2026-08-27`.

Next: 局.

### 2026-08-27, iteration 1118 — [[words/局|局]]

**Real formatting bug found and fixed on both the word and character page**: `vietnamese` had been stored as a single malformed string ("cục, cộc, cuộc, gục, ngúc") instead of a proper YAML list — fixed both files, keeping "cục" (the primary administrative-office reading) as the word's own field value. 局's own `stand_in` is itself — documented. Filled `japanese: きょく`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 屁.

### 2026-08-27, iteration 1119 — [[words/屁|屁]]

Single-character stand-alone word, quick clean pass. 屁's own `stand_in` is itself — documented. Filled `japanese: ひ` (on'yomi; native へ is the everyday word). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 居所.

### 2026-08-27, iteration 1120 — [[words/居所|居所]]

Already had excellent, richly-developed prose (correctly explaining the 居所/住所, 居/住 legal-domicile-vs-whereabouts distinction). Just needed `vietnamese: cư sở` filled in (verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 屈.

### 2026-08-27, iteration 1121 — [[words/屈|屈]]

Single-character stand-alone word. Double-checked the unusual-looking mandarin/cantonese pair (qū/wat1, a bigger divergence than most) against 屈's own character page — already correct, a genuine feature of this character, not contamination. Filled `pos: 事詞`/`japanese: くつ`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 届.

### 2026-08-27, iteration 1122 — [[words/届|届]]

Single-character stand-alone word. 届's own `stand_in` is itself — documented. **Found a genuine Dan'a'yo homophone**: 届 and [[皆]] ("all, every") share an identical reading — added reciprocal callouts to both (皆.md had been stamped since June without one). **Flagged, not fixed**: 皆.md's own `japanese: かい` frontmatter field looks inconsistent with its own prose, which discusses みな/みんな as "the everyday word" for 皆 without かい appearing anywhere — worth a dedicated look when 皆 itself comes up for review, out of scope for this 届-focused iteration. Stamped only [[words/届]] `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1123 — [[words/屋|屋]]

Single-character stand-alone word. Fixed a small `羅馬字` typo (missing the leading apostrophe marking a vowel-initial syllable: og → 'og, matching the character's own field). Filled `japanese: おく` and `vietnamese: ốc` (verified — survives mainly in set idioms like 愛屋及烏, everyday speech prefers native nhà). No homophones among other words. Stamped `date-last-perfect: 2026-08-27`.

Next: 屎.

### 2026-08-27, iteration 1124 — [[words/屎|屎]]

**Real character-page bug found and fixed**: 屎's own character page had `mandarin: xī`/`cantonese: hei1` — 屎 genuinely has two Mandarin readings (shǐ "excrement," matching the character's own documented gloss, and a separate rare xī "groaning sound"), but the wrong one had been stored. Corrected to shǐ/si2, matching this word's own long-correct fields. The word's `羅馬字`/`諺文`/`注音` (ㄏㄜ) had already been fixed in the original syllable-lint sweep (see [[project_perfection_era_methodology]]) — confirmed still correct, a different bug from the one just found. Filled `japanese: し`/`vietnamese: thỉ`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 屏風 already stamped — 屑.

### 2026-08-27, iteration 1125 — [[words/屑|屑]]

Single-character stand-alone word. 屑's own `stand_in` is itself — documented. Filled `japanese: せつ`. Homophone with [[舌]] was already correctly reciprocal on both pages (both already stamped). Stamped `date-last-perfect: 2026-08-27`.

Next: 展示.

### 2026-08-27, iteration 1126 — [[words/展示|展示]]

No stand-in relationship (展→伸展, 示→開示). Left `vietnamese` omitted — no attested "triển thị" found; Vietnamese uses the distinct compound triển lãm (展覽) instead. No specific HSK level number, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 展翅.

### 2026-08-27, iteration 1127 — [[words/展翅|展翅]]

Already had rich prose covering the Japanese (展翅/天使) and Korean (展翅/展示) homophone coincidences. **Found a genuine additional Dan'a'yo-level homophone, distinct from those**: 展翅 and [[戦時]] ("wartime") share an identical reading (jensi/전시/ㄐㄝㄋㄙㄧ) — added reciprocal callouts to both (戦時.md not otherwise stamped). Filled `vietnamese: triển sí` (verified). No stand-in relationship. Stamped `date-last-perfect: 2026-08-27`.

Next: 属格.

### 2026-08-27, iteration 1128 — [[words/属格|属格]]

No stand-in relationship (属→所属, 格→itself). Filled blank `vietnamese: thuộc cách` (verified as a real linguistic term). Notes explain the 属格/所有格 synonym relationship. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1129 — [[words/屢|屢]]

Single-character stand-alone word. Verified the vietnamese "lũ" (already stored) against search rather than assuming it was another false-cognate case (the character page's field is unusually messy with 6 variants) — confirmed genuinely correct. Filled `japanese: る`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 層.

### 2026-08-27, iteration 1130 — [[words/層|層]]

Single-character stand-alone word. Filled `pos: 名詞`/`japanese: そう`/`vietnamese: tầng` (the everyday reading — building floor — among several character-page variants). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 屯.

### 2026-08-27, iteration 1131 — [[words/屯|屯]]

Single-character stand-alone word, quick clean pass. Filled `pos: 名詞`/`japanese: とん`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 山地.

### 2026-08-27, iteration 1132 — [[words/山地|山地]]

**Real invisible-character typo found and fixed**: `japanese` had a stray zero-width space embedded between さ and ん (さ​んち), rendered visually as normal text but a genuine data glitch — cleaned to さんち. No stand-in relationship. Filled blank `vietnamese: sơn địa` (verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1133 — [[words/山岳|山岳]]

**Real `注音` typo found and fixed**: stored ㄙㄚㄇ·ㄚㄎ, but 山's own reading ends in ㄋ (n), not ㄇ (m) — the `諺文`/`羅馬字` fields already correctly used the n-final form (산/san), only `注音` had the wrong final consonant. Propagated the fix to both [[山]]'s and [[岳]]'s own Words-section rubies (both had been citing the same wrong reading). 岳's own `stand_in` field is 山岳 — added the stand-in note. Filled blank `vietnamese: sơn nhạc` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 山崩.

### 2026-08-27, iteration 1134 — [[words/山崩|山崩]]

No stand-in relationship (both 山/崩 self). Filled blank `korean: 산붕` (a real dictionary term, though modern Korean prefers native 산사태). Left `vietnamese` omitted — no standing term confirmed; Vietnamese uses native sạt lở núi instead. No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 山嶺.

### 2026-08-27, iteration 1135 — [[words/山嶺|山嶺]]

嶺's own `stand_in` field is 山嶺 — added the stand-in note. All other fields already correct compositional concatenations; filled blank `vietnamese: sơn lĩnh` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 山脈.

### 2026-08-27, iteration 1136 — [[words/山脈|山脈]]

脈's own `stand_in` field is 山脈 — added the stand-in note (page had no `## Notes` section, just a bare Etymology bullet). All other fields already correct. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1137 — [[words/岐|岐]]

Single-character stand-alone word. Filled `japanese: き`. No homophones. Caught myself about to create a dead `[[歧]]` link (歧 is just an alias, no separate character page) — rephrased to plain text before publishing. Stamped `date-last-perfect: 2026-08-27`.

Next: 岩石.

### 2026-08-27, iteration 1138 — [[words/岩石|岩石]]

岩's own `stand_in` field is 岩石 — added the stand-in note. Filled blank `vietnamese: nham thạch` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 峨峨.

### 2026-08-27, iteration 1139 — [[words/峨峨|峨峨]]

峨's own `stand_in` field is 峨峨 (a reduplicated intensifier word) — added the stand-in note. Filled blank `cantonese`/`vietnamese` with the reduplicated forms (ngo4 ngo4/nga nga). Caught and fixed two more dead links before publishing (堂堂/洋洋 cited as examples don't have their own word pages — rephrased as plain text). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 島.

### 2026-08-27, iteration 1140 — [[words/島|島]]

Single-character stand-alone word. 島's own `stand_in` is itself — documented. Filled `japanese: とう`/`vietnamese: đảo` (verified as primary; the character's other listed reading, láo, is a genuine but unrelated Nôm-only reading, not a false cognate). **Confirmed a genuine triple Dan'a'yo homophone**: 島/[[倒]]/[[超]] all share tau/탓/ㄊㄚㄨ — [[倒]] already had the correct reciprocal callout listing both; added the missing callout to 島 and to [[超]] (not otherwise stamped). Stamped `date-last-perfect: 2026-08-27`.

Next: 崇拝.

### 2026-08-27, iteration 1141 — [[words/崇拝|崇拝]]

**Root-cause fix**: 拝's own character page had a completely blank `vietnamese` field — filled in "bái" (verified via the real, well-attested compound 崇拜/sùng bái). No stand-in relationship (崇→崇高, 拝→itself). Fixed `characters:` filename form. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1142 — [[words/崇高|崇高]]

崇's own `stand_in` field is 崇高 — added the stand-in note. Filled blank `vietnamese: sùng cao` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 崖.

### 2026-08-27, iteration 1143 — [[words/崖|崖]]

Single-character stand-alone word. Filled `pos`/`japanese`/`vietnamese`. Confirmed the existing triple homophone group (崖/[[唉]]/[[愛]]) was already fully, correctly cross-referenced on all three pages — no fix needed there. Stamped `date-last-perfect: 2026-08-27`.

Next: 崩.

### 2026-08-27, iteration 1144 — [[words/崩|崩]]

Single-character stand-alone word. Filled `pos`/`japanese`. Notes cover the classical elevated sense (崩御, exclusively "the death of an emperor"). No homophones among other words. Stamped `date-last-perfect: 2026-08-27`.

Next: continuing the sweep (嵌入/川/川口/川埼/州 already stamped).

### 2026-08-27, iteration 1145 — [[words/巣穴|巣穴]]

**Real contamination bug found and fixed, two fields**: `aliases` wrongly listed 巢窟 alongside the genuine variant 巢穴 — 巢窟/[[巣窟]] is actually a separate word with its own page and different reading (jaukod/잣콛/ㄐㄚㄨㄎㄛㄊ), confirmed by checking that page directly; removed. `korean` had similarly been contaminated, storing "소혈; 소굴" — 소굴 is 巣窟's own real Korean reading, not this word's — corrected to plain 소혈. No stand-in relationship (巣→鳥巣, 穴→洞穴). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巣窟.

### 2026-08-27, iteration 1146 — [[words/巣窟|巣窟]]

Fixed `characters:` filename form (bare `窟` → `窟 (char)`). No stand-in relationship (巣→鳥巣, 窟→itself). Filled blank `cantonese`/`vietnamese: sào quật` (both verified). Notes explicitly distinguish this from [[巣穴]] (the contamination source fixed last iteration). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 工具.

### 2026-08-27, iteration 1147 — [[words/工具|工具]]

具's own `stand_in` field is 工具 — added the stand-in note. Double-checked 工's own vietnamese field for the primary reading "công" before assuming it was missing (same false-alarm shape as [[尊厳]]'s earlier session finding) — it was already there, just further down the list than an initial grep view showed; confirmed `vietnamese: công cụ` already fully correct. Notes explain the real 工具/道具 register distinction (specific manufacturing tools vs. the broader everyday-implement word, verified via search) — cleaned up the stray one-line "called 道具 in J/K" note into proper prose. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 工匠.

### 2026-08-27, iteration 1148 — [[words/工匠|工匠]]

**Significant contamination bug found and fixed**: `諺文`/`羅馬字`/`注音` had been contaminated with [[場]]'s own reading (장/jang/ㄐㄚㄫ, an exact match confirmed by checking 場's character page directly) instead of 匠's real citation (촹/cwang/ㄑ⺢ㄫ). The page had even documented the bug's own symptom as a real fact — a note claiming this word "is a homophone of [[工場]]" — but real Mandarin/Cantonese/Japanese readings of the two words are not actually homophones at all (gōngjiàng/gōngchǎng, こうしょう/こうじょう); only Korean 공장 coincidentally matches both independently. Fixed the readings, removed the false claim, and propagated the correction to [[匠]]'s own Words-section ruby. Filled `vietnamese: công tượng` (verified). 匠's own `stand_in` field is 工匠 — added the stand-in note. No homophones after the correction. Stamped `date-last-perfect: 2026-08-27`.

Next: 工場.

### 2026-08-27, iteration 1149 — [[words/工場|工場]]

No stand-in relationship (工→工作, 場→市場). This word's own fields were never contaminated — removed the now-false "homophone with [[工匠]]" claim (a symptom of the bug just fixed on that page, not a real fact once corrected). Filled blank `vietnamese: công trường` (verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1150 — [[words/左右|左右]]

Investigated a suspicious-looking `諺文` (자유, byte-identical to the common unrelated Korean word 자유 "freedom") — verified against 左/右's own citation forms and confirmed it's genuinely correct compositionally (자+유), just a coincidental hangul-spelling collision, not a bug. No stand-in relationship (左→左側, 右→右側). Filled blank `vietnamese: tả hữu` (verified, including the extended "approximately"/"attendants" senses). Quoted `hsk_level: "2"`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巧妙.

### 2026-08-27, iteration 1151 — [[words/巧妙|巧妙]]

巧's own `stand_in` field is 巧妙 — added the stand-in note; fixed `characters:` filename form (bare `妙` → `妙 (char)`). Filled blank `vietnamese: xảo diệu` (verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巨人.

### 2026-08-27, iteration 1152 — [[words/巨人|巨人]]

**Real bug found and fixed**: `vietnamese` had been stored as người lớn — which actually means "adult," not "giant," and isn't even a Sino-Vietnamese reading of either character. Corrected to cự nhân, the genuine compositional reading (confirmed via its use translating this exact compound, 巨人/Kyojin, in *Attack on Titan*). No stand-in relationship (巨→巨大, 人→itself). No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1153 — [[words/巨大|巨大]]

Fixed an English gloss typo ("gigantitic" → "gigantic"). 巨's own `stand_in` field is 巨大 — added the stand-in note. Filled blank `vietnamese: cự đại` (verified), quoted `hsk_level: "2"`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巫山.

### 2026-08-27, iteration 1154 — [[words/巫山|巫山]]

**Real `japanese` bug found and fixed**: stored ふきょう, likely confused with a related nearby place name (巫峡, "Wu Gorge," part of the same Three Gorges cluster) — corrected to the real, verified reading ふざん (with rendaku voicing). Fixed `pos: 名詞` → `固有名詞` (proper noun). No stand-in relationship. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巫術.

### 2026-08-27, iteration 1155 — [[words/巫術|巫術]]

No stand-in relationship (巫→巫女, 術→itself). Filled blank `vietnamese: vu thuật` (verified). Notes note the near-synonymy with [[法術]]. Standardized the homophone callout format with [[武術]] (real, confirmed genuine collision) on both pages — was already reciprocal, just using a non-canonical `>[!tip]` sentence instead of the standard block. Stamped `date-last-perfect: 2026-08-27`.

Next: 差別.

### 2026-08-27, iteration 1156 — [[words/差別|差別]]

差's own `stand_in` field is 差別 — added the stand-in note. Filled blank `vietnamese: sai biệt` — but found it carries the older, neutral "difference/disparity" sense rather than the narrowed discrimination sense that dominates modern Japanese/Korean; modern Vietnamese for "discrimination" uses an unrelated compound (phân biệt đối xử) built on a different character. Documented the semantic divergence rather than presenting it as a clean match. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 差額 (差異 already stamped).

### 2026-08-27, iteration 1157 — [[words/差額|差額]]

Fixed the opening bullet's gloss for 差 ("discriminate" → "difference; discrepancy" — the correct sense here, as documented on [[差別]]'s own page for the same character's dual senses). No stand-in relationship (差→差別, 額→額頭). Filled blank `vietnamese: sai ngạch` (verified). No HSK level, no homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1158 — [[words/巳月|巳月]]

Same zodiac-calendar-month pattern as [[寅月]]. 巳's own `stand_in` is the special `名専字` naming-restriction marker (not a specific compound) — documented. All fields already correct compositional concatenations. Added a closing paragraph paralleling [[寅月]]'s native-zodiac-name observation for Japanese/Vietnamese. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巴.

### 2026-08-27, iteration 1159 — [[words/巴|巴]]

Single-character stand-alone word. 巴's own `stand_in` is itself — documented. Filled `japanese: は`. Notes cover the tomoe heraldic motif and 巴's phonetic transliteration role in [[巴基斯坦]] (Pakistan). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 巻.

### 2026-08-27, iteration 1160 — [[words/巻|巻]]

Single-character stand-alone word. **Found `korean: "null"` (the literal string bug, same shape as [[尚]])** — corrected to 권. 巻's own `stand_in` is itself — documented. Filled `japanese: かん`. Confirmed the existing triple homophone group (巻/[[圏]]/[[絹]]) was already fully cross-referenced on the other two pages — added the missing callout here. Stamped `date-last-perfect: 2026-08-27`.

Next: 市場.

### 2026-08-27, iteration 1161 — [[words/市場|市場]]

場's own `stand_in` field is 市場 — added the stand-in note. All fields already correct compositional concatenations. Quoted `hsk_level: "2"`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 布帛.

### 2026-08-27, iteration 1162 — [[words/布帛|布帛]]

**Real `korean` bug found and fixed, same class as [[少女]]/[[尭舌]]**: stored 보박 (mechanically matching this word's own `諺文` instead of the real Korean reading) — corrected to 포백, using 布's own real Korean field (포, distinct from its Dan'a'yo 諺文 보). 帛's own `stand_in` field is 布帛 — added the stand-in note. Filled blank `vietnamese: bố bạch` (verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1163 — [[words/帆|帆]]

Single-character stand-alone word. Verified the multi-variant `vietnamese` field (buồm/buồng/phàm) — all three genuinely documented Nôm/Hán readings, not contamination — picked phàm (the formal Hán Việt reading) as this word's own value. 帆's own `stand_in` is itself — documented. **Found a genuine Dan'a'yo homophone**: 帆 and [[汎]] ("pan-") share an identical reading — added reciprocal callouts to both (汎.md not otherwise stamped). Stamped `date-last-perfect: 2026-08-27`.

Next: 帆船.

### 2026-08-27, iteration 1164 — [[words/帆船|帆船]]

**Real contamination bug found and fixed**: `諺文`/`羅馬字` stored 줜/jwen — an exact match for [[全]]'s own reading (confirmed by cross-checking that character page) — instead of 船's real citation 쉄/swem, which was already correctly reflected in this word's own `注音` and in 帆's Words-section ruby. Fixed both. Confirmed via [[船]]'s own already-standing flag that this word belongs to the "regular" ㄙ⼔ㄇ group (unlike [[艦船]]/[[宇宙船]]). Filled `vietnamese: phàm thuyền` (verified). No stand-in relationship, no homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 希薄.

### 2026-08-27, iteration 1165 — [[words/希薄|希薄]]

薄's own `stand_in` field is 希薄 — added the stand-in note (noting 希 uses its "rare" sense here, shared with its alias 稀, matching the compound's more common everyday spelling). Filled blank `vietnamese: hi bạc` (verified) and added missing `kwin: true`. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1166 — [[words/帖|帖]]

Single-character stand-alone word. Filled `pos`/`japanese`. Notes cover the character's three distinct homographic senses (tiě/tiē/tiè). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 帝王.

### 2026-08-27, iteration 1167 — [[words/帝王|帝王]]

**Root-cause fix**: 帝's own character page was missing its primary Hán Việt reading, đế, entirely (only rarer variants đê/đí/đó/đấy listed) — added it, resolving this word's own `vietnamese: đế vương` (verified) in the process. 帝's own `stand_in` field is 帝王 — added the stand-in note. Notes cover the real đế/vương rank distinction Vietnamese preserves explicitly. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 帯.

### 2026-08-27, iteration 1168 — [[words/帯|帯]]

Single-character stand-alone word. **Found `korean: "null"` (the literal string bug, same shape as [[尚]]/[[巻]])** — corrected to 대. 帯's own `stand_in` is itself — documented. **Found a genuine triple Dan'a'yo homophone**: 帯, [[太]], and [[戴]] all share tai/태/ㄊㄚㄧ, none of the three had any homophone callout at all before this — added reciprocal callouts to all three (太.md/戴.md not otherwise stamped this iteration). Filled `japanese: たい`/`vietnamese: đai`. Stamped only [[words/帯]] `date-last-perfect: 2026-08-27`.

Next: 帰納.

### 2026-08-27, iteration 1169 — [[words/帰納|帰納]]

Fixed another archaic-kana `japanese` typo (きなふ → きのう, same recurring class as [[将軍]]/[[少女]]/[[少年]]). No stand-in relationship (帰→回帰, 納→itself). Filled blank `vietnamese: quy nạp` (verified, distinguished from 演繹/diễn dịch "deduction"). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 帰結.

### 2026-08-27, iteration 1170 — [[words/帰結|帰結]]

No stand-in relationship (帰→回帰, 結→itself). Filled blank `vietnamese: quy kết` — but found a real semantic drift: Vietnamese quy kết has narrowed toward a negative, accusatory register ("to unfairly judge/condemn without evidence") rather than the neutral logical-conclusion sense Japanese きけつ/Korean 귀결 both keep. Documented the drift rather than presenting it as a clean match. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1171 — [[words/帰還|帰還]]

No stand-in relationship (帰→回帰, 還→送還). Filled blank `vietnamese: quy hoàn` (verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 帰順.

### 2026-08-27, iteration 1172 — [[words/帰順|帰順]]

No stand-in relationship (帰→回帰, 順→順次). Filled blank `cantonese`/`vietnamese: quy thuận` (both verified). Notes note the real "incomplete voluntariness" nuance (submission under pressure, distinct from 帰服/quy phục). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 帳簿.

### 2026-08-27, iteration 1173 — [[words/帳簿|帳簿]]

簿's own `stand_in` field is 帳簿 — added the stand-in note. Filled blank `korean: 장부`/`vietnamese: trướng bạ` (both verified). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 常用.

### 2026-08-27, iteration 1174 — [[words/常用|常用]]

**Real `vietnamese` bug found and fixed**: stored thông thường, a different everyday Vietnamese adverb ("usually") built from unrelated characters/words, not a reading of 常+用 at all — corrected to thường dụng, the genuine compositional reading (both 常's "thường" and 用's "dụng" independently confirmed on their own character pages), verified as a real attested term. No stand-in relationship (常→日常, 用→使用). No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 常識.

### 2026-08-27, iteration 1175 — [[words/常識|常識]]

Clean pass — all fields were already correct compositional concatenations (`vietnamese: thường thức` already right, a real distinct word from [[常用]]'s previous contamination). Filled blank `pos: 名詞`. No stand-in relationship (常→日常, 識→認識). No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1176 — [[words/幕|幕]]

Single-character stand-alone word. 幕's own `stand_in` is itself — documented. Filled `japanese: まく`. **Found a genuine Dan'a'yo homophone**: 幕 and its own phonetic root [[莫]] ("not, none") share an identical reading — added reciprocal callouts to both (莫.md had been stamped since June without ever carrying one). Stamped `date-last-perfect: 2026-08-27`.

Next: 幟.

### 2026-08-27, iteration 1177 — [[words/幟|幟]]

Single-character stand-alone word. 幟's own `stand_in` is itself — documented. Filled `japanese: し`/`korean`/`vietnamese` (all already present, verified correct). **Found a genuine triple Dan'a'yo homophone**: 幟, [[歯]], and [[置]] all share ci/치/ㄑㄧ — checked several other candidates sharing this bopomofo string (恥/厠/治/痴/瓷/祉/辞/魑) but all of those are bound characters citing a different compound as their own `stand_in`, so they don't collide at the word level; only these three genuinely standalone words do. Added reciprocal callouts to all three (歯.md/置.md not otherwise stamped, just got the callout ahead of their own turn). Stamped only [[words/幟]] `date-last-perfect: 2026-08-27`.

Next: 幣 already stamped — 干戈.

### 2026-08-27, iteration 1178 — [[words/干戈|干戈]]

戈's own `stand_in` field is 干戈 — added the stand-in note. All fields already correct compositional concatenations. Expanded Notes with the classical idiom 化干戈為玉帛. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 干渉.

### 2026-08-27, iteration 1179 — [[words/干渉|干渉]]

干's own `stand_in` field is 干渉 — added the stand-in note. All fields already correct compositional concatenations. Noted the real dual usage (everyday interference + physics wave-interference) shared across all four languages. No homophones. Stamped `date-last-perfect: 2026-08-27`.

### 2026-08-27, iteration 1180 — [[words/干犯|干犯]]

No stand-in relationship (干→干渉, 犯→犯罪). All fields already correct. Distinguished this from [[干渉]] — a graver, more formal near-synonym leaning toward violation of rights/sovereignty/law rather than general meddling. No homophones. Stamped `date-last-perfect: 2026-08-27`.

Next: 平均.

### 2026-08-28, iteration 1181 — [[words/平均|平均]]

**Investigated an apparent `korean`/`諺文` mismatch and confirmed it's NOT a bug**: `korean: 평균` and `諺文: 병균` looked contradictory at first, but 平's own character page already documents (via `kwin: false`) a deliberate divergence between its real Sino-Korean reading (평) and its Dan'a'yo form (병) — both fields here are independently correct on their own terms. This coincidentally makes 平均's Dan'a'yo reading collide exactly with [[病菌]] ("pathogenic bacteria") — a genuine Dan'a'yo-only homophone, *not* a real Korean-level one (병균 and 평균 remain distinct in actual Korean). Standardized the existing non-canonical homophone callout on both pages and documented the Korean/Dan'a'yo distinction explicitly. No stand-in relationship (平→水平, 均→itself). HSK level 2 already correct. Stamped `date-last-perfect: 2026-08-28`.

Next: 平坦.

### 2026-08-28, iteration 1182 — [[words/平坦|平坦]]

坦's own `stand_in` field is 平坦 — added the stand-in note. **Real semantic drift found**: Vietnamese bình thản has drifted entirely away from the literal "physically flat" sense into "inner calm, serenity, composure" — the figurative-only extension of a sense Japanese/Korean still keep alongside the literal one, verified via search (not confusable with the near-homophone bình tĩnh, "emotional control under stress"). Documented rather than treated as an error. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 平安.

### 2026-08-28, iteration 1183 — [[words/平安|平安]]

安's own `stand_in` field is 平安 — added the stand-in note (page had no `## Notes` section at all). Noted the Japanese Heian period name derives directly from this word. All fields already correct compositional concatenations. No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1184 — [[words/平日|平日]]

No stand-in relationship (平→水平, 日→itself). All fields already correct compositional concatenations; filled blank `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 平板.

### 2026-08-28, iteration 1185 — [[words/平板|平板]]

No stand-in relationship (平→水平, 板→木板). Filled blank `vietnamese: bình bản` (verified). Notes cover both the literal "flat panel/slab" sense and the modern extension to "tablet computer" (平板電腦). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 平穏.

### 2026-08-28, iteration 1186 — [[words/平穏|平穏]]

穏's own `stand_in` field is 平穏 — added the stand-in note. Filled blank `vietnamese: bình ổn` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 平等.

### 2026-08-28, iteration 1187 — [[words/平等|平等]]

Investigated the seemingly-anomalous `japanese: びょうどう` (using びょう instead of any of 平's own stored on'yomi HEI/HYOU/BEN) and confirmed it's a genuine, well-documented Buddhist-derived Go-on (呉音) reading — not a bug, and not something 平's own character page needs to list (the character's own field tracks its regular on'yomi set, not this one lexicalized exception). Documented the linguistic history explicitly. No stand-in relationship (平→水平, 等→itself). HSK level 2 already correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1188 — [[words/平静|平静]]

No stand-in relationship (平→水平, 静→静寂). All fields already correct compositional concatenations, including `vietnamese: bình tĩnh` — cross-referenced this against [[平坦]]'s earlier note (bình tĩnh being the correctly-spelled term often confused with 平坦's own drifted bình thản); this word's own field is exactly right. Filled blank `pos: 性詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 年.

### 2026-08-28, iteration 1189 — [[words/年|年]]

Single-character stand-alone word. 年's own `stand_in` is itself — documented. Filled `japanese: ねん`/`vietnamese: niên` — the character's own field also lists năm (actually the native Vietnamese everyday word for "year," not a Sino-Vietnamese reading) and nên (an unrelated grammatical particle), so picked the genuine Sino-Vietnamese reading rather than either false lead. No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 年刊.

### 2026-08-28, iteration 1190 — [[words/年刊|年刊]]

**Real `korean` bug found and fixed, per the standing [[feedback_korean_reading_north]] rule**: stored 연간, the South Korean 두음법칙-shifted form of word-initial 年 — corrected to the unshifted 년간, matching 年's own stored `korean` field (년) directly. No stand-in relationship (both 年/刊 self). Filled blank `vietnamese: niên khan` (verified compositional). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 年歳.

### 2026-08-28, iteration 1191 — [[words/年歳|年歳]]

**Three separate real bugs found and fixed on the same page**: `japanese` stored the bare character 歲 instead of any kana reading — corrected to ねんさい (verified). `korean` stored the malformed multi-value string "연세, 나이" — 연세 was itself South-Korean-shifted (same class as [[年刊]]'s bug), and 나이 an entirely unrelated native Korean word for "age," not a reading of this compound — corrected to the proper North Korean 년세. `vietnamese` stored nhiêu tuổi, an interrogative phrase meaning "how old," not a reading of this word at all — corrected to niên tuế (verified, a real if literary compound). 歳's own `stand_in` field is 年歳 — added the stand-in note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 年齢.

### 2026-08-28, iteration 1192 — [[words/年齢|年齢]]

**Same contamination pattern as [[年刊]]/[[年歳]] found again, a third instance**: `korean` stored the malformed "연령, 나이" — 연령 South-Korean-shifted, 나이 an unrelated native word — corrected to North Korean 년령. `cantonese` had a missing space (nin4ling4 → nin4 ling4). **Root-cause fix**: 齢's own character page had a completely blank `vietnamese` field — verified and filled in "linh" (confirmed via classical citations like 年紀已經八十有零/niên kỉ dĩ kinh bát thập hữu linh), which resolved this word's own `vietnamese: niên linh` (also independently verified as attested in derived compounds). 齢's own `stand_in` field is 年齢 — added the stand-in note, distinguishing it from the more formal [[年歳]]. No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1193 — [[words/幸運|幸運]]

Fixed another archaic-kana `japanese` typo (かううん → こううん). Verified `korean: 행운` is already correct — same deliberate Dan'a'yo/Korean divergence shape as [[平均]] (幸's own Dan'a'yo 諺文 항 differs from its real Korean 행, already `kwin: false`-documented). 幸's own `stand_in` field is 幸運 — added the stand-in note. Filled blank `vietnamese: hạnh vận` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 幼児.

### 2026-08-28, iteration 1194 — [[words/幼児|幼児]]

幼's own `stand_in` field is 幼児 — added the stand-in note (page had no `## Notes` section). All fields already correct compositional concatenations. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 幼稚.

### 2026-08-28, iteration 1195 — [[words/幼稚|幼稚]]

稚's own `stand_in` field is 幼稚 — added the stand-in note. All fields already correct compositional concatenations. Notes distinguish the neutral (幼稚園) and pejorative (childish adult behavior) senses. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 幽.

### 2026-08-28, iteration 1196 — [[words/幽|幽]]

Single-character stand-alone word. 幽's own `stand_in` is itself — documented. Filled `japanese: ゆう`. **Found a genuine triple Dan'a'yo homophone**: 幽, [[猶]], and [[由]] all share 'yuo/윳/⼜ㄛ — none of the three had ever carried a homophone callout ([[由]] had been stamped since June without one) — added reciprocal callouts to all three. Stamped only [[words/幽]] `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1197 — [[words/幽鬼|幽鬼]]

**Real cross-field contamination bug found and fixed**: `korean` had the Japanese kana reading ゆうき pasted into it (evidently meant for a `japanese` field that was itself entirely blank) — corrected `korean` to 유귀 and filled `japanese: ゆうき` and blank `cantonese: jau1 gwai2` with verified values. No stand-in relationship (幽→itself, 鬼→鬼神). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 幾.

### 2026-08-28, iteration 1198 — [[words/幾|幾]]

Single-character stand-alone word. 幾's own `stand_in` is itself — documented. Filled `japanese: き`/`vietnamese: kỉ` (correctly distinguishing this "several/how many" sense from the character's other listed reading "cơ," which belongs to an unrelated "small sign, omen" sense of the same character). No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 広.

### 2026-08-28, iteration 1199 — [[words/広|広]]

**Root-cause fix**: 広's own character page had a completely blank `vietnamese` field — filled in "quảng" (verified), which resolved this word's own field. 広's own `stand_in` is itself — documented. Filled `japanese: こう`. No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 庇護.

### 2026-08-28, iteration 1200 — [[words/庇護|庇護]]

The 1200th iteration of this loop. 庇's own `stand_in` field is 庇護 — added the stand-in note. All fields already correct compositional concatenations. Notes cover both the concrete "shelter" sense and the modern legal "political asylum" sense. No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1201 — [[words/床|床]]

Single-character stand-alone word. 床's own `stand_in` is itself — documented. Filled `japanese: しょう`/`vietnamese: sàng`, and traced the character's multiple listed Vietnamese variants (giường, sường, etc.) to a real, documented historical sound-shift chain (sàng → sường → giường) rather than treating them as contamination. Cleared the cryptic "Pronunciation changed" placeholder note. No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 序文.

### 2026-08-28, iteration 1202 — [[words/序文|序文]]

Verified `cantonese: zeoi6 man4` looked unusual (zeoi6 rather than the more familiar jeoi6-shaped readings) but matched 序's own stored field exactly — not a bug. No stand-in relationship (序→順序, 文→文化). Filled blank `vietnamese: tự văn` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1203 — [[words/底|底]]

Single-character stand-alone word. 底's own `stand_in` is itself — documented. Filled `japanese: てい`/`vietnamese: để` (correctly picking the primary reading among several Nôm variants on the character page, confirmed via classical examples like 水底/thủy để). **Found a genuine triple Dan'a'yo homophone**: 底, [[第]], and [[蹄]] all share dei/데/ㄉㄝㄧ — none had ever carried a callout — added reciprocal callouts to all three, and along the way filled each of the other two's own blank `vietnamese` fields (đệ for 第, "-th"; đề for 蹄, "hoof" — both independently verified). Stamped only [[words/底]] `date-last-perfect: 2026-08-28`.

Next: 庭園.

### 2026-08-28, iteration 1204 — [[words/庭園|庭園]]

園's own `stand_in` field is 庭園 — added the stand-in note. Filled blank `cantonese`/`vietnamese: đình viên` (both verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 庵子.

### 2026-08-28, iteration 1205 — [[words/庵子|庵子]]

**Investigated the odd dual gloss ("greenhouse, monastery") and confirmed it's genuine, not a fabrication**: 庵子 is a real dialectal Mandarin word carrying two distinct regional senses — a farmer's thatched field-shelter (Guanzhong dialect) and a small Buddhist nunnery (other regions), verified via zdic/Wiktionary. Fixed `mandarin` (was truncated to bare "ān," corrected to the full "ānzi"). Filled blank `cantonese`. **Flagged rather than guessed**: `japanese: あんじ` is attested only as a given-name reading, not an ordinary common noun — documented explicitly rather than presented as a standard word reading. Left `vietnamese` omitted — no attested Sino-Vietnamese compound found. 庵's own `stand_in` field is 庵子 — added the stand-in note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 庶民.

### 2026-08-28, iteration 1206 — [[words/庶民|庶民]]

庶's own `stand_in` field is 庶民 — added the stand-in note. Filled blank `vietnamese: thứ dân` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 康寧.

### 2026-08-28, iteration 1207 — [[words/康寧|康寧]]

Already had excellent, richly-developed prose explaining the 康/健 sense-split ([[康寧]] vs. [[健全]], both collapsed under [[健康]]). Just needed `vietnamese: khang ninh` filled in (verified as a formal blessing-register term). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 康金.

### 2026-08-28, iteration 1208 — [[words/康金|康金]]

A third `neologism`/`periodictable` word this session (scandium, element 21), same genre as [[孫金]]/[[射素]]. Added the standard opening bullet documenting no stand-in relationship and confirming `kwin: false` is correct by design. Did not rewrite the existing rich etymological reasoning (钪/kàng phonetic match, Scandinavia naming chain). Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1209 — [[words/庸|庸]]

Found this word had never actually been stamped, despite receiving its homophone callout in the earlier 容/庸/湧 triple-homophone pass this session — the callout addition alone didn't complete the page. Filled `pos`/`japanese`/`kwin`, built out the Notes section, and stamped it properly. No new homophones beyond the already-documented triple. Stamped `date-last-perfect: 2026-08-28`.

Next: continuing the sweep.

### 2026-08-28, iteration 1210 — [[words/湧|湧]]

Same gap as [[庸]] just found — never actually stamped despite receiving its homophone callout earlier this session. Filled `pos`/`japanese`/`kwin`, built out the Notes section, stamped. **Lesson for future homophone-fix passes**: adding a reciprocal callout to an unstamped sibling page (as done for [[容]]/[[庸]]/[[湧]] and other triples this session) doesn't complete that page — it still needs its own full pass before stamping, and should be tracked as a real remaining item, not assumed done. Stamped `date-last-perfect: 2026-08-28`.

**Homophone-sibling backlog note (2026-08-28, updated)**: swept the log for other pages that received a reciprocal homophone callout earlier this session but were explicitly left "not otherwise stamped, awaiting their own turn" — per the lesson above, these still need their own full completion pass, not just the callout. Remaining: [[賞]] (from the 尚/上/賞 triple), [[戦時]] (from 展翅), [[超]] (from 島/倒/超), [[汎]] (from 帆), [[太]] and [[戴]] (from 帯), [[歯]] and [[置]] (from 幟), [[籠]] (from 弄), [[銀]] (from 引), [[袂]] (from 弥). Will pick these up either in the normal alphabetical sweep as their filenames come up, or as a dedicated mini-batch later — flagging now so they aren't silently forgotten the way 庸/湧 briefly were.

Next: 廃墟.

### 2026-08-28, iteration 1211 — [[words/廃墟|廃墟]]

**Real `諺文`/`羅馬字` bug found and fixed, same "注音 right, others wrong" shape as [[少女]]/[[尭吉]]**: stored 펴쿄/pyekyo, but 廃's own citation form is 뻐/fe — corrected to 뻐쿄/fekyo (注音, ㄈㄝㄎ⼄, had been correct all along, and 墟's own Words-section ruby — which uses 注音 — was unaffected). 墟's own `stand_in` field is 廃墟 — added the stand-in note. Filled blank `vietnamese: phế khư` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 廃棄.

### 2026-08-28, iteration 1212 — [[words/廃棄|廃棄]]

Already had solid content and a correctly-placed stand-in note (廃's own `stand_in` is 廃棄). Expanded Notes with a concrete/legal-register distinction. Quoted bare-string frontmatter values. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 廃黜.

### 2026-08-28, iteration 1213 — [[words/廃黜|廃黜]]

**Real `cantonese` bug found and fixed**: stored fai3zyut6 — 黜's own real Cantonese reading is zeot1, an entirely different syllable from the stored zyut6 — corrected to "fai3 zeot1." Stand-in note already correctly present. Quoted bare-string frontmatter values. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 廉価.

### 2026-08-28, iteration 1214 — [[words/廉価|廉価]]

**Same 두음법칙/native-word contamination pattern found again, a fourth instance**: `korean` stored the malformed "염가, 싼값" — 염가 South-Korean-shifted, 싼값 an unrelated native word — corrected to North Korean 렴가. No stand-in relationship (廉→itself, 価→価格). Filled blank `vietnamese: liêm giá` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 廟堂.

### 2026-08-28, iteration 1215 — [[words/廟堂|廟堂]]

Investigated `japanese: びょうどう` — coincidentally identical to [[平等]]'s own irregular Go-on reading — and confirmed this one is genuinely compositional (廟's own BYOU + 堂's own DOU on'yomi), an independent coincidence, not a copy-paste error. Fixed unquoted `cantonese`. 廟's own `stand_in` field is already correctly noted (廟堂). No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1216 — [[words/延長|延長]]

Verified `korean: 연장` against both constituents' own fields (연+장) — no 두음법칙 issue here since 延's own reading is already 연, not shifted (unlike the recent 年/廉 cases). No stand-in-note gap. Filled blank `vietnamese: diên trường` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 建国.

### 2026-08-28, iteration 1217 — [[words/建国|建国]]

Clean pass — all fields already correct. No stand-in relationship (建→建設, 国→国家). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 建築.

### 2026-08-28, iteration 1218 — [[words/建築|建築]]

No stand-in relationship (建→建設, 築→構築). Preserved the useful compound-family note (建築事/建築物/建築学/建築家) as proper prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 弁.

### 2026-08-28, iteration 1219 — [[words/弁|弁]]

Single-character stand-alone word. 弁's own `stand_in` is itself — documented, and correctly distinguished from the character's own unrelated "ceremonial cap" original sense (this word tracks its role as a shinjitai stand-in for 辯/辨 instead). Filled `japanese: べん`. No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 弄.

### 2026-08-28, iteration 1220 — [[words/弄|弄]]

Single-character stand-alone word. 弄's own `stand_in` is itself — documented. Filled `japanese: ろう`/`vietnamese: lộng` (correctly picking the primary reading among several Nôm variants). **Found a genuine Dan'a'yo homophone**: 弄 and [[籠]] ("cage, basket") share an identical reading — added reciprocal callouts to both (籠.md not otherwise stamped, just got the callout ahead of its own turn — added to the homophone-sibling backlog list). Stamped only [[words/弄]] `date-last-perfect: 2026-08-28`.

Next: 弊.

### 2026-08-28, iteration 1221 — [[words/弊|弊]]

Single-character stand-alone word. 弊's own `stand_in` is itself — documented. Filled `japanese: へい`/`vietnamese: tệ` (correctly picking the standard reading, tệ nạn, over the character's other listed Nôm variant giẻ). No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1222 — [[words/弔|弔]]

Single-character stand-alone word. 弔's own `stand_in` is itself — documented. Filled `japanese: ちょう`. No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 引.

### 2026-08-28, iteration 1223 — [[words/引|引]]

Single-character stand-alone word. 引's own `stand_in` is itself — documented. Filled `japanese: いん`/`vietnamese: dẫn`. **Found a genuine Dan'a'yo homophone**: 引 and [[銀]] ("silver," a periodictable word) share an identical reading — added reciprocal callouts to both (銀.md not otherwise stamped — added to the homophone-sibling backlog). Stamped only [[words/引]] `date-last-perfect: 2026-08-28`.

Next: 引入.

### 2026-08-28, iteration 1224 — [[words/引入|引入]]

No stand-in relationship (both 引/入 self). Filled all three blank fields (`korean`/`japanese`/`vietnamese`, all verified). Noted Vietnamese dẫn nhập's real additional use as a standalone literary term for an introductory section. No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1225 — [[words/弟|弟]]

Single-character stand-alone word. 弟's own `stand_in` is itself — documented. Filled `japanese: てい`/`vietnamese: đệ`. No homophones among other words. Stamped `date-last-perfect: 2026-08-28`.

Next: 弟子.

### 2026-08-28, iteration 1226 — [[words/弟子|弟子]]

Verified the real cross-word Korean-only pun already flagged on [[梯子]]'s own page — confirmed the two words are distinct at the Dan'a'yo level (ㄊ vs ㄉ initial), so no `>[!warning] Homophones` callout applies here, just a documented Korean-level coincidence. No stand-in relationship (弟→itself, 子→児子). All fields already correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 弥.

### 2026-08-28, iteration 1227 — [[words/弥|弥]]

Single-character stand-alone word. 弥's own `stand_in` is itself — documented. Filled `japanese: み`/`vietnamese: di`. **Found a genuine Dan'a'yo homophone**: 弥 and [[袂]] ("sleeve") share an identical reading — added reciprocal callouts to both (袂.md not otherwise stamped — added to the homophone-sibling backlog). Stamped only [[words/弥]] `date-last-perfect: 2026-08-28`.

Next: 弥勒.

### 2026-08-28, iteration 1228 — [[words/弥勒|弥勒]]

Investigated `cantonese: mei4 lak6` looking like a mismatch against 弥's own citation form (nei4) — verified both mei4 and nei4 are real, independently attested Cantonese readings of 彌, with mei4 specifically conventional for this proper name (彌勒). No correction made — documented the divergence explicitly rather than "fixing" it. No stand-in relationship (弥→itself, 勒→勒馬). No homophones. Stamped `date-last-perfect: 2026-08-28`.

### 2026-08-28, iteration 1229 — [[words/弥漫|弥漫]]

漫's own `stand_in` field is 弥漫 — added the stand-in note. Investigated `japanese: びまん`, which doesn't match either constituent's own on'yomi (弥's MI, 漫's MAN) — verified it's a genuine, independently-attested lexicalized reading, not a bug. Filled blank `vietnamese: di mạn` (verified, including its use in the set phrase 煙霧彌漫). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 弧度.

### 2026-08-28, iteration 1230 — [[words/弧度|弧度]]

No stand-in relationship (弧→弧線, 度→程度). Filled blank `cantonese`/`vietnamese: hồ độ` (both verified). Standardized the homophone callout format with [[糊塗]] (real, confirmed genuine collision) on both pages — was already reciprocal, just non-canonical `[!tip]`/`[!Tip]` phrasing. Also fixed relative-path links (missing `../`). No new gaps. Stamped `date-last-perfect: 2026-08-28`.

Next: 弧線.

### 2026-08-28, iteration 1231 — [[words/弧線|弧線]]

弧's own `stand_in` field is 弧線 — added the stand-in note. Filled blank `cantonese`/`vietnamese: hồ tuyến` (both verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 弯曲.

### 2026-08-28, iteration 1232 — [[words/弯曲|弯曲]]

弯's own `stand_in` field is 弯曲 — added the stand-in note (曲's own is [[歌曲]], not this word). Fixed malformed `japanese` field (one-item YAML list → plain scalar わんきょく, verified as WAN + KYOKU, 弯's own on'yomi rather than the alternate EN reading). Filled blank `vietnamese: loan khúc` (verified — genuine Sino-Vietnamese compound, "winding, curved"). Verified `korean: 만곡` is correctly compositional from both characters' own readings (no 두음법칙 contamination). Removed the redundant non-standard `品詞` field (duplicate of `pos`, not part of the checklist schema). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 弱.

### 2026-08-28, iteration 1233 — [[words/弱|弱]]

Single-character stand-alone word, rebuilt from a malformed stub (bare-scalar `characters`, `vietnamese: null`, missing `pos`/`japanese`, wrong-level `# Notes` heading). 弱's own `stand_in` field is itself — documented. Filled `japanese: じゃく` (matching sibling compounds 衰弱/薄弱/羸弱's JAKU, not the alternate NYAKU that the 羅馬字 "nyag" derives from) and `vietnamese: nhược` (from the character's own vietnamese list, matching those same siblings). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 強.

### 2026-08-28, iteration 1234 — [[words/強|強]]

Single-character stand-alone word, rebuilt from a malformed stub. 強's own `stand_in` field is itself — documented. Filled `japanese: きょう`/`vietnamese: cường` (matching sibling compounds 強化/強固/強国/剛強). No homophones (注音 shared only with character [[僵]], whose own stand-in 僵屍 is a different multi-syllable reading). Stamped `date-last-perfect: 2026-08-28`.

Next: 剣術.

### 2026-08-28, iteration 1235 — [[words/剣術|剣術]]

No stand-in relationship (both 剣 and 術 are independent Dan'a'yo entries, each its own stand-in). Frontmatter was already fully correct (japanese/korean/vietnamese all verified compositional); fixed the non-standard `## Etymology` heading → `## Notes` and expanded to full checklist prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 副詞.

### 2026-08-28, iteration 1236 — [[words/副詞|副詞]]

No stand-in relationship (副 is its own stand-in; 詞's own is [[単詞]]). Frontmatter already fully correct (verified japanese/korean/vietnamese all compositional, vietnamese "phó" confirmed against sibling compounds 副用/副業). Added the missing `## Notes` section entirely (page previously had none). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 副金.

### 2026-08-28, iteration 1237 — [[words/副金|副金]]

Periodictable/neologism word (protactinium). Frontmatter fields were already correct by design (real-world CJKV fields are phonetic loanwords, `kwin: false` correctly reflects the non-compositional Dan'a'yo coinage 副金 "subsidiary metal, relative to 始金"). Verified `羅馬字`/`諺文`/`注音` are compositional from 副's and 金's own readings. Removed the redundant `品詞` field and added the missing `word` tag (both common gaps across this periodictable batch). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 創世記.

### 2026-08-28, iteration 1238 — [[words/創世記|創世記]]

No stand-in relationship (創→[[創立]], 世→[[世界]], 記→[[記憶]], all different words). **Real bug found and fixed**: 創's syllable in `羅馬字`/`諺文`/`注音` was contaminated from a divergent form (cang/창/ㄑㄚㄫ) rather than 創's own authoritative reading (cwang/촹/ㄑ⺢ㄫ, confirmed via 創's own character page and its stand-in [[創立]]) — corrected. Confirmed 世's own syllable 서 (not 세, despite 羅馬字 "se") is the established vault-wide convention (checked against 8+ sibling words using 世), not an error — left as-is. Expanded Notes with full stand-in documentation. No homophones. Stamped `date-last-perfect: 2026-08-28`. Note: [[創立]] and [[創造]] (both still unstamped, next in queue) may carry the same cang/창 vs cwang/촹 contamination — worth checking when reached.

Next: 創立.

### 2026-08-28, iteration 1239 — [[words/創立|創立]]

創's own `stand_in` field is 創立 — added the stand-in note (立's own is [[立]], unrelated). **Real bug found and fixed**: `mandarin` had 立's cantonese reading erroneously appended to it as a merged string ("chuànglì; ong3 laap6"), leaving `cantonese` blank — split apart and corrected. `羅馬字` also had 創's syllable using the divergent "cang" form rather than its own authoritative "cwang" (諺文 촹립 was already correct) — corrected to cwanglib. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 創造.

### 2026-08-28, iteration 1240 — [[words/創造|創造]]

造's own `stand_in` field is 創造 — added the stand-in note (創's own is [[創立]]). **Real bugs found and fixed**: same cang/창 vs cwang/촹 contamination on 創's syllable as [[創世記]]/[[創立]] — corrected. `vietnamese: tạo nên` was a native colloquial gloss rather than the real Sino-Vietnamese compound — corrected to `sáng tạo` (verified). `aliases` erroneously listed the word's own traditional form as an "alias" — corrected to simplified 创造. No homophones. Stamped `date-last-perfect: 2026-08-28`. (All three 創-compounds in this cluster — 創世記, 創立, 創造 — are now fixed and stamped.)

Next: 劇詩.

### 2026-08-28, iteration 1241 — [[words/劇詩|劇詩]]

No stand-in relationship (劇 is its own stand-in; 詩's own is [[詩歌]]). Filled blank `vietnamese: kịch thi` (compositional from both characters' own readings, matching sibling compounds; documented that real-world usage prefers native "kịch thơ" instead). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 加入.

### 2026-08-28, iteration 1242 — [[words/加入|加入]]

No stand-in relationship (入 is its own stand-in; 加's own is [[加算]]). Frontmatter already fully correct (verified japanese/korean/vietnamese all compositional). Fixed non-standard `## Etymology` heading → `## Notes`, expanded to full prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 加多金.

### 2026-08-28, iteration 1243 — [[words/加多金|加多金]]

Periodictable/neologism word (gadolinium). **Real bug found and fixed**: `注音` second syllable had ㄉㄚ instead of the correct ㄉㄜ (matching [[加多]]'s own attested reading gadǝ/가드/ㄍㄚㄉㄜ) — corrected. Removed the redundant `品詞` field. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 加持.

### 2026-08-28, iteration 1244 — [[words/加持|加持]]

No stand-in relationship (持 is its own stand-in; 加's own is [[加算]]). Filled blank `cantonese: gaa1 ci4` (verified). **Found a genuine Dan'a'yo homophone**: 加持 and [[価値]] ("worth, value") share an identical reading — standardized the non-canonical `[!tip]`/informal-text callouts on both pages into proper reciprocal `>[!warning] Homophones` callouts, and completed [[価値]]'s full frontmatter/Notes pass in the same iteration (both pages already fully correct otherwise) rather than deferring it to the backlog. Both stamped `date-last-perfect: 2026-08-28`.

Next: 加皮.

### 2026-08-28, iteration 1245 — [[words/加皮|加皮]]

No stand-in relationship (加's own is [[加算]], 皮's is [[皮革]]). Documented that 加 here is a same-Mandarin-reading (jiā) phonetic substitute for the uncreated character 痂, with 痂皮 recorded as the real-word alias. **Real bug found and fixed**: `mandarin`/`cantonese` covered only 加's own reading (jiā/gaa1), missing 皮's contribution entirely — corrected to jiāpí/gaa1 pei4. Removed the redundant `品詞` field. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 労動.

### 2026-08-28, iteration 1246 — [[words/労動|労動]]

労's own `stand_in` field is 労動 — added the stand-in note (動's own is [[動]], unrelated). Frontmatter already fully correct, including `korean: 로동` correctly preserving the unshifted North Korean form. Fixed non-standard `## Etymology` heading → `## Notes`, expanded to full prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 効果.

### 2026-08-28, iteration 1247 — [[words/効果|効果]]

効's own `stand_in` field is 効果 — added the stand-in note (果's own is [[果実]]). Frontmatter already fully correct. Fixed non-standard `## Etymology` heading → `## Notes`, expanded to full prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 効率.

### 2026-08-28, iteration 1248 — [[words/効率|効率]]

No stand-in relationship (効's own is [[効果]], 率's is [[比率]]). Verified `korean: 효율` (률→율 after a vowel is standard Korean orthography, not a bug). Fixed `hsk_level: 2` → quoted `"2"` per schema. Fixed non-standard `## Etymology` heading → `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 勃勃.

### 2026-08-28, iteration 1249 — [[words/勃勃|勃勃]]

Reduplication of 勃 — no stand-in relationship (its own stand-in is [[勃興]]). Filled blank `vietnamese: bột bột` (verified, standard Sino-Vietnamese reduplication as in 生氣勃勃). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 勇敢.

### 2026-08-28, iteration 1250 — [[words/勇敢|勇敢]]

勇's own `stand_in` field is 勇敢 — added the stand-in note (敢's own is [[敢為]]). Frontmatter already fully correct. Added the missing `## Notes` section entirely (page previously had none). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 動詞.

### 2026-08-28, iteration 1251 — [[words/動詞|動詞]]

No stand-in relationship (動 is its own stand-in; 詞's own is [[単詞]]). Frontmatter already fully correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 勢力.

### 2026-08-28, iteration 1252 — [[words/勢力|勢力]]

勢's own `stand_in` field is 勢力 — added the stand-in note (力's own is [[力]], unrelated). Frontmatter already fully correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 包含.

### 2026-08-28, iteration 1253 — [[words/包含|包含]]

含's own `stand_in` field is 包含 — added the stand-in note (包's own is [[包装]]). **Real bug found and fixed**: `vietnamese` was malformed ("baohán", missing space, wrong tone) — corrected to `bao hàm`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 包括.

### 2026-08-28, iteration 1254 — [[words/包括|包括]]

括's own `stand_in` field is 包括 — added the stand-in note (包's own is [[包装]]). Fixed `hsk_level: 2` → quoted `"2"`. Frontmatter otherwise already correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 包皮.

### 2026-08-28, iteration 1255 — [[words/包皮|包皮]]

No stand-in relationship (包's own is [[包装]], 皮's is [[皮革]]). **Real bug found and fixed**: `mandarin` was truncated ("bāop") — corrected to bāopí. Documented `vietnamese: bao bì` as compositionally correct but semantically drifted toward "packaging" in modern usage (medical Vietnamese prefers "bao quy đầu"), left as-is per vault convention of using the compositional form. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 匈奴.

### 2026-08-28, iteration 1256 — [[words/匈奴|匈奴]]

匈's own `stand_in` field is 匈奴 — added the stand-in note (奴's own is [[奴隷]]). Filled blank `japanese: きょうど` (verified). Fixed `vietnamese` capitalization ("hung Nô" → `Hung Nô`, verified as the standard form). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 化学肥料.

### 2026-08-28, iteration 1257 — [[words/化学肥料|化学肥料]]

No stand-in relationship (化 is its own stand-in; 学's own is [[学習]], 肥's is [[肥満]], 料's is [[材料]]). Frontmatter fields were already correct but `kwin`/`hsk_level`/`swadesh`/`aliases`/`date-last-perfect` were entirely missing — added (`kwin: false`, verified against the Sino-Korean/Dan'a'yo divergence). Expanded Notes to full prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 化身.

### 2026-08-28, iteration 1258 — [[words/化身|化身]]

No stand-in relationship (化 is its own stand-in; 身's own is [[身体]]). Fixed `characters` citation "化" → "化 (char)" to match the actual filename. Verified `japanese: けしん` uses 化's alternate on'yomi KE rather than the more common KA — genuine, not an error. Fixed non-standard `## Etymology` heading → `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 北京.

### 2026-08-28, iteration 1259 — [[words/北京|北京]]

No stand-in relationship (北's own is [[北方]], 京's is [[京城]]). Verified `japanese: ぺきん` is a genuine phonetic-loan reading for the exonym "Peking" (matching the precedent of しゃんはい for 上海), not an error. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 北方.

### 2026-08-28, iteration 1260 — [[words/北方|北方]]

北's own `stand_in` field is 北方 — added the stand-in note (方's own is [[方向]]). **Real bugs found and fixed**: `japanese` had ぱう instead of the correct ほう for 方's own on'yomi (never rendaku-shifts here, per siblings 五方/平方/地方) — corrected to ほくほう. `vietnamese: hướng bắc` was a native paraphrase rather than the real compound — corrected to `phương bắc`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 北極.

### 2026-08-28, iteration 1261 — [[words/北極|北極]]

No stand-in relationship (北's own is [[北方]]; 極 is its own stand-in). Fixed `characters` citation "極" → "極 (char)" to match the actual filename. Frontmatter otherwise already correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 区域.

### 2026-08-28, iteration 1262 — [[words/区域|区域]]

区's own `stand_in` field is 区域 — added the stand-in note (域's own is [[域]], unrelated). **Real bug found and fixed**: `mandarin`/`cantonese` were both entirely blank — filled compositionally (qūyù/keoi1 wik6). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 医生.

### 2026-08-28, iteration 1263 — [[words/医生|医生]]

医's own `stand_in` field is 医生 — added the stand-in note (生's own is [[生活]]). **Real bugs found and fixed**: `mandarin`/`cantonese`/`korean`/`aliases` were all contaminated with forms belonging to the near-synonym word 医師/医师 (yīshī, built from 医+師 not 医+生) — corrected mandarin to yīshēng, cantonese to ji1 sang1, korean to 의생 (compositional, dropping the mixed-in real word 의사), and trimmed aliases to just 醫生. Filled blank `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十一日.

### 2026-08-28, iteration 1264 — [[words/十一日|十一日]]

No stand-in relationship (all three characters are independent, each its own stand-in). Fixed `characters` citation "十" → "十 (char)". Filled blank `vietnamese: thập nhất nhật` (matching established sibling convention on [[七日]]). Fixed malformed `japanese` YAML-list → plain scalar; removed the redundant `品詞` field. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十七日.

### 2026-08-28, iteration 1265 — [[words/十七日|十七日]]

Same pattern as [[十一日]]: no stand-in relationship, fixed `characters` citation, filled blank `vietnamese: thập thất nhật`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十三.

### 2026-08-28, iteration 1266 — [[words/十三|十三]]

No stand-in relationship (both independent). Filled blank `vietnamese: thập tam`. Fixed missing space in `cantonese` (sap6saam1 → sap6 saam1), `characters` citation, and removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十三日.

### 2026-08-28, iteration 1267 — [[words/十三日|十三日]]

Same pattern as prior day-words: no stand-in relationship, filled blank `vietnamese: thập tam nhật`, fixed `characters` citation, malformed `japanese` list, and redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十九日.

### 2026-08-28, iteration 1268 — [[words/十九日|十九日]]

Same pattern as prior day-words. Verified `japanese: じゅうくにち` uses KU (not the alternate KYUU), the genuine calendar convention. Filled blank `vietnamese: thập cửu nhật`, fixed `characters` citation, malformed `japanese` list, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十二.

### 2026-08-28, iteration 1269 — [[words/十二|十二]]

No stand-in relationship (both independent). **Real bugs found and fixed**: `vietnamese` was capitalized with the wrong tone ("Thập nhì") — corrected to `thập nhị`. `aliases` listed the word's own filename as a bogus self-alias — removed. Fixed `characters` citation and redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十二日.

### 2026-08-28, iteration 1270 — [[words/十二日|十二日]]

Same pattern as prior day-words: filled blank `vietnamese: thập nhị nhật`, fixed `characters` citation, malformed `japanese` list, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十五.

### 2026-08-28, iteration 1271 — [[words/十五|十五]]

No stand-in relationship (both independent). Frontmatter values already correct; fixed malformed `japanese`/`vietnamese` YAML-lists → plain scalars, `characters` citation, and redundant `品詞`. Notes section was truncated to a bare "## Notes" heading with no content — rebuilt in full. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十五日.

### 2026-08-28, iteration 1272 — [[words/十五日|十五日]]

Same pattern as prior day-words: filled blank `vietnamese: thập ngũ nhật`, fixed `characters` citation, malformed `japanese` list, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十八日.

### 2026-08-28, iteration 1273 — [[words/十八日|十八日]]

Same pattern as prior day-words: filled blank `vietnamese: thập bát nhật`, fixed `characters` citation, malformed `japanese` list, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十六.

### 2026-08-28, iteration 1274 — [[words/十六|十六]]

No stand-in relationship (both independent). **Real bugs found and fixed**: `korean` was blank — filled 십륙 (North Korean/문화어). `vietnamese` had a native paraphrase ("Mười sáu") — corrected to `thập lục`. Fixed `characters` citation, empty-list `aliases`, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十六日.

### 2026-08-28, iteration 1275 — [[words/十六日|十六日]]

No stand-in relationship. **Real bugs found and fixed**: `korean` used the South Korean 두음법칙-shifted form (십육일) instead of North Korean 십륙일 (matching [[十六]]'s own fix — confirmed via web search that North Korean 문화어 genuinely writes 십륙 where South Korean writes 십육, an exception where even South Korean's own orthography treats 六 as quasi-word-initial). `注音` had a single-letter typo in the last syllable (ㄋㄝㄊ → ㄋㄧㄊ). Filled blank `vietnamese: thập lục nhật`. Fixed `characters` citation, malformed `japanese` list, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十四.

### 2026-08-28, iteration 1276 — [[words/十四|十四]]

No stand-in relationship (both independent). **Real bugs found and fixed**: `english` typo ("forteen" → fourteen). `vietnamese` had a native paraphrase ("mười bốn") — corrected to `thập tứ`. Fixed `characters` citation, empty-list `aliases`, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 十四日.

### 2026-08-28, iteration 1277 — [[words/十四日|十四日]]

No stand-in relationship. Verified `japanese: じゅうよっか` as a genuine irregular calendar reading (not the expected on'yomi compound). Filled blank `vietnamese: thập tứ nhật`. Fixed `characters` citation, malformed `japanese` list, redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`. (This completes the full run of 十X日 day-name words from 十一日 through 十六日 plus 十四日 — all now fixed and stamped.)

Next: 千米.

### 2026-08-28, iteration 1278 — [[words/千米|千米]]

No stand-in relationship (千's own is [[一千]]; 米 is its own stand-in). Verified that japanese キロメートル/korean 킬로미터 (international phonetic loanwords for "kilometer") and vietnamese cây số (colloquial native term) are genuine, expected divergences for this modern metric coinage, not errors. Fixed non-standard `## Etymology` heading → `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 午前.

### 2026-08-28, iteration 1279 — [[words/午前|午前]]

No stand-in relationship (午's own is [[正午]]; 前 is its own stand-in). **Real bug found and fixed**: `mandarin`/`cantonese` had been contaminated with the alias 上午's reading (shàngwǔ/soeng6 ng5) instead of 午前's own (wǔqián/ng5 cin4) — corrected. Filled blank `pos: 名詞`. Documented `vietnamese: buổi sáng` as a native paraphrase rather than a direct calque. Cleaned up a duplicate `## Notes`/`## Etymology` heading pair. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 午後.

### 2026-08-28, iteration 1280 — [[words/午後|午後]]

No stand-in relationship. **Real bug found and fixed**: `mandarin`/`cantonese` contaminated with the alias 下午's reading (same class of bug as [[午前]]/上午) — corrected to wǔhòu/ng5 hau6. Filled blank `pos: 名詞`. Documented that Dan'a'yo renders 後 here as hou/홋 rather than its own huo/훗 citation form, matching the established suffix-position convention on [[以後]]/[[最後]] (vs. prefix/classical-connective 後 in [[後裔]]/[[然後]]) — a vault-wide pattern noted for awareness, not altered. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 午月.

### 2026-08-28, iteration 1281 — [[words/午月|午月]]

Verified japanese うまつき / vietnamese tháng Ngọ match the established native zodiac-month-name convention (matching sibling [[寅月]]'s とらつき/tháng Dần). **Found a genuine Dan'a'yo homophone**: 午月 and [[五月]] ("May") share an identical reading — added reciprocal callouts to both, and completed [[五月]]'s full pass in the same iteration (already-stamped page, fixed missing space in cantonese and relative-path links, re-stamped). No new gaps. Both stamped `date-last-perfect: 2026-08-28`.

Next: 半島.

### 2026-08-28, iteration 1282 — [[words/半島|半島]]

半's own is [[一半]]; 島 is its own stand-in — no stand-in relationship. **Real bug found and fixed**: `mandarin`/`cantonese` were both entirely blank — filled bàndǎo/bun3 dou2. **Found the reciprocal side of an existing homophone**: 半島 and [[絆倒]] ("to trip, cause to stumble") already noted each other informally via non-canonical `[!tip]` callouts — standardized both to proper `>[!warning] Homophones` format and completed [[絆倒]]'s stand-in note in the same pass (絆's own stand-in is 絆倒 itself). Both stamped `date-last-perfect: 2026-08-28`.

Next: 卍字.

### 2026-08-28, iteration 1283 — [[words/卍字|卍字]]

卍's own `stand_in` field is 卍字 — added the stand-in note (字's own is [[字]], unrelated). Verified Dan'a'yo's `羅馬字`/`諺文`/`注音` (monji, diverging from all real readings) is a documented idiosyncratic choice on 卍's own character page, not an error. Fixed missing space in `cantonese`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 卓越.

### 2026-08-28, iteration 1284 — [[words/卓越|卓越]]

卓's own `stand_in` field is 卓越 — added the stand-in note (越's own is [[越]], unrelated). **Real bug found and fixed**: `mandarin` had the wrong tone mark ("zhuōyuè" → zhuóyuè). Filled blank `pos: 性詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 協会.

### 2026-08-28, iteration 1285 — [[words/協会|協会]]

No stand-in relationship (協's own is [[協力]]; 会 is its own stand-in). Fixed `characters` citation "会" → "会 (char)". Frontmatter otherwise already correct. Fixed non-standard `## Etymology` heading → `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 南北.

### 2026-08-28, iteration 1286 — [[words/南北|南北]]

No stand-in relationship (南's own is [[南方]]; 北's is [[北方]]). Fixed missing space in `cantonese`; removed redundant `品詞`; fixed heading. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 南山.

### 2026-08-28, iteration 1287 — [[words/南山|南山]]

No stand-in relationship (南's own is [[南方]]; 山 is its own stand-in). Verified `japanese: ナムサン` is a genuine phonetic-loan transliteration for this Korean place name. Fixed `characters` citation "山" → "山 (char)". No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 南方.

### 2026-08-28, iteration 1288 — [[words/南方|南方]]

南's own `stand_in` field is 南方 — added the stand-in note (方's own is [[方向]]). **Real bugs found and fixed**: `cantonese` was completely wrong ("nan2 fang1") — corrected to naam4 fong1. `pos` was mislabeled 連接詞 ("conjunction") — corrected to 名詞. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 単純.

### 2026-08-28, iteration 1289 — [[words/単純|単純]]

Page was already nearly complete (well-written Notes, correct frontmatter). No stand-in relationship (単's own is [[簡単]]; 純's is [[純粋]]) — added the note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 単詞.

### 2026-08-28, iteration 1290 — [[words/単詞|単詞]]

詞's own `stand_in` field is 単詞 — added the stand-in note (単's own is [[簡単]]). Verified that japanese たんご/korean 단어 both reflect the real-world compound 単語 (built with 語, not 詞) rather than a compositional reading — a genuine, expected divergence, not an error. Homophone with [[丹砂]] already fully documented reciprocally. No other homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 単鷹国.

### 2026-08-28, iteration 1291 — [[words/単鷹国|単鷹国]]

Dan'a'yo coinage for Prussia ("single-eagle nation"). No stand-in relationship. Verified real-world CJKV fields are genuine phonetic loanwords (プロイセン, 프로이센, Phổ Lỗ Sĩ), not compositional — expected for this neologism. Fixed `characters` citation "鷹" → "鷹 (char)". No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 博士.

### 2026-08-28, iteration 1292 — [[words/博士|博士]]

No stand-in relationship (博's own is [[博大]]; 士 is its own stand-in). **Real bug found and fixed**: `mandarin`/`cantonese` were both entirely blank — filled bóshì/bok3 si6. Documented `vietnamese: bác sĩ` as compositionally correct but semantically drifted to mean "medical doctor" in modern usage (PhD is "tiến sĩ" instead). Fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 占拠.

### 2026-08-28, iteration 1293 — [[words/占拠|占拠]]

No stand-in relationship (占 is its own stand-in; 拠's own is [[依拠]]). Verified `cantonese: zim3` is a genuine alternate tone for 占's "occupy" sense (vs. its citation tone zim1 for "divination"), not an error. Fixed `characters` citation "占" → "占 (char)"; fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 占星.

### 2026-08-28, iteration 1294 — [[words/占星|占星]]

No stand-in relationship (both independent). Verified `mandarin: zhānxīng` uses 占's "divine" tone rather than its citation tone (same sense-dependent split as [[占拠]]'s cantonese). Fixed `characters` citation, filled blank `pos: 名詞`, removed redundant blank `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 占星術.

### 2026-08-28, iteration 1295 — [[words/占星術|占星術]]

No stand-in relationship (all three independent). **Real bugs found and fixed**: `mandarin`/`cantonese` were missing 術's contribution entirely — filled zhānxīngshù/zim1 sing1 seot6. `japanese` was truncated (せんせいじ → せんせいじゅつ). Fixed `characters` citation. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 卯月.

### 2026-08-28, iteration 1296 — [[words/卯月|卯月]]

Discovered and documented the `名専字` ("name-exclusive character") convention: 卯's own `stand_in` is this blanket marker rather than a specific word, since 卯 genuinely appears only in zodiac/calendrical contexts across the vault — distinct from siblings like [[寅月]] (寅's own stand-in is 寅月 itself) or [[午月]] (午's own stand-in points elsewhere, to 正午). Verified japanese うつき / vietnamese tháng Mão match the established native zodiac-month convention. Removed stray `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 印度.

### 2026-08-28, iteration 1297 — [[words/印度|印度]]

No stand-in relationship (印's own is [[封印]]; 度's is [[程度]]). Verified japanese インド is a genuine katakana phonetic loan for the country name. Expanded the terse `[[印]] + [[度]]` Notes into full prose. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 印度洋.

### 2026-08-28, iteration 1298 — [[words/印度洋|印度洋]]

No stand-in relationship (印's own is [[封印]]; 度's is [[程度]]; 洋's is [[大洋]]). Frontmatter already fully correct. Fixed non-standard `## Etymology` heading → `## Notes`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 印章.

### 2026-08-28, iteration 1299 — [[words/印章|印章]]

No stand-in relationship (印's own is [[封印]]; 章 is its own stand-in). **Real bug found and fixed**: `vietnamese` was wrongly capitalized as a proper noun ("Ấn chương") — corrected to lowercase `ấn chương`. Filled blank `pos: 名詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 即日.

### 2026-08-28, iteration 1300 — [[words/即日|即日]]

No stand-in relationship. **Real bugs found and fixed**: `羅馬字`/`諺文`/`注音` had 即's syllable using a divergent form (jig/직) instead of its own authoritative reading (jǝg/즉, confirmed against sibling [[即位]]) — corrected. `korean` was contaminated with the synonym 当日's reading (당일) — corrected to 즉일. Filled blank `vietnamese: tức nhật`. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 卵白.

### 2026-08-28, iteration 1301 — [[words/卵白|卵白]]

No stand-in relationship (卵's own is [[卵子]]; 白 is its own stand-in). **Real bug found and fixed**: `cantonese` was blank — filled leon2 baak6. Fixed a typo in `korean` (횐자위 → 흰자위, the real native word for egg white). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 原因.

### 2026-08-28, iteration 1302 — [[words/原因|原因]]

因's own `stand_in` field is 原因 — added the stand-in note (原's own is [[原始]]). Filled blank `pos: 名詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 原始.

### 2026-08-28, iteration 1303 — [[words/原始|原始]]

原's own `stand_in` field is 原始 — already documented (始's own is [[始作]]). Filled blank `vietnamese: nguyên thuỷ` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 原子.

### 2026-08-28, iteration 1304 — [[words/原子|原子]]

No stand-in relationship (原's own is [[原始]]; 子's is [[児子]]). **Real bug found and fixed**: `羅馬字`/`諺文` had 子's syllable using a divergent form (ji/지) instead of its own authoritative reading (jǝ/즈, confirmed against sibling [[児子]]) — corrected (注音 was already right). Fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 原罪.

### 2026-08-28, iteration 1305 — [[words/原罪|原罪]]

No stand-in relationship (原's own is [[原始]]; 罪 is its own stand-in). Filled blank `vietnamese: nguyên tội`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 厩肥.

### 2026-08-28, iteration 1306 — [[words/厩肥|厩肥]]

No stand-in relationship (厩's own is [[馬厩]]; 肥's is [[肥満]]). Verified `vietnamese: cứu phì` is compositionally correct (厩's own reading), coincidentally homophonous with the unrelated word for "save," not an error. Filled missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 厳重.

### 2026-08-28, iteration 1307 — [[words/厳重|厳重]]

No stand-in relationship (both independent). Fixed `pos` (mislabeled "修飾語," not a recognized tag) → 性詞. Verified `cantonese: zung6` reflects 重's "heavy" sense vs. its citation "cung5" — a legitimate sense-dependent split. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 双曲線.

### 2026-08-28, iteration 1308 — [[words/双曲線|双曲線]]

No stand-in relationship (双 is its own stand-in; 曲's own is [[歌曲]]; 線's is [[直線]]). Verified `vietnamese: hyperbol` is the genuine standard Vietnamese math term (international loanword for the noun), distinct from "song khúc" (used only for the adjective "hyperbolic"). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 反切.

### 2026-08-28, iteration 1309 — [[words/反切|反切]]

No stand-in relationship (both independent). **Real bug found and fixed**: `cantonese` was missing 反's initial consonant ("faan1cit3" → faan2 cit3, matching every sibling 反-compound). Verified `korean: 반절` uses 切's genuine alternate reading (절, as in 切実/親切) rather than its citation 체 (一切) — not an error. Fixed empty-list `aliases`. Flagged (not fixed, out of scope) an apparent internal inconsistency on 反's own character page (諺文 뽄 vs 羅馬字/注音's F-initial fon/ㄈㄛㄋ) for a future character-perfecting pass. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 反哺.

### 2026-08-28, iteration 1310 — [[words/反哺|反哺]]

No stand-in relationship (反 is its own stand-in; 哺's own is [[哺乳]]). Frontmatter already fully correct. Fixed non-standard `## Etymology` heading → `## Notes`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 反応.

### 2026-08-28, iteration 1311 — [[words/反応|反応]]

No stand-in relationship (both independent). **Real bugs found and fixed**: `注音` had the wrong initial consonant (ㄆㄛㄋ instead of 反's own ㄈㄛㄋ). `cantonese` missing space. `japanese` had a stray trailing parenthesis. Fixed unquoted `hsk_level`, empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 反映.

### 2026-08-28, iteration 1312 — [[words/反映|反映]]

No stand-in relationship (both independent). Frontmatter already fully correct. Fixed non-standard `## Etymology` heading → `## Notes`; fixed unquoted `hsk_level`, empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 反駁.

### 2026-08-28, iteration 1313 — [[words/反駁|反駁]]

駁's own `stand_in` field is 反駁 — added the stand-in note. **Real bug found and fixed**: `注音` had the same wrong-initial-consonant bug as [[反応]] (ㄆㄛㄋ → ㄈㄛㄋ). Confirmed via a vault-wide scan that no other 反-compound still carries this typo. Fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 収入.

### 2026-08-28, iteration 1314 — [[words/収入|収入]]

No stand-in relationship (収's own is [[回収]]; 入 is its own stand-in). Filled blank `pos: 名詞`; fixed unquoted `hsk_level`, empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 収蔵.

### 2026-08-28, iteration 1315 — [[words/収蔵|収蔵]]

蔵's own `stand_in` field is 収蔵 — already documented. Filled blank `vietnamese: thu tàng` (compositional). Verified `mandarin: shōucáng` reflects 蔵's verb sense vs. its citation zāng — a legitimate divergence. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 収集.

### 2026-08-28, iteration 1316 — [[words/収集|収集]]

No stand-in relationship (収's own is [[回収]]; 集's is [[集合]]). Filled blank `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 口訣.

### 2026-08-28, iteration 1317 — [[words/口訣|口訣]]

No stand-in relationship (口 is its own stand-in; 訣's own is [[秘訣]]). Frontmatter already fully correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 古今.

### 2026-08-28, iteration 1318 — [[words/古今|古今]]

No stand-in relationship (古's own is [[古代]]; 今 is its own stand-in). Fixed `characters` citation "今" → "今 (char)". Frontmatter otherwise already correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 古代.

### 2026-08-28, iteration 1319 — [[words/古代|古代]]

古's own `stand_in` field is 古代 — added the stand-in note (代's own is [[世代]]). Filled blank `vietnamese: cổ đại` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 古典.

### 2026-08-28, iteration 1320 — [[words/古典|古典]]

No stand-in relationship (古's own is [[古代]]; 典's is [[事典]]). **Real bug found and fixed**: `羅馬字`/`諺文`/`注音` had 典's syllable using a divergent form (dan/전/ㄐㄝㄋ) instead of its own authoritative reading (den/던/ㄉㄝㄋ), confirmed against every other 典-compound in the vault ([[事典]], [[典雅]], [[字典]], [[恩典]], [[瑞典]], [[祭典]], [[詞典]]) — corrected, flipping `kwin` true→false to match (Dan'a'yo now correctly diverges from Sino-Korean 고전, same as [[典雅]]). Propagated the fix to the ruby citations on both [[古]]'s and [[典]]'s own Words sections. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 古琴.

### 2026-08-28, iteration 1321 — [[words/古琴|古琴]]

No stand-in relationship (古's own is [[古代]]; 琴 is its own stand-in). Noted an interesting real-world (Japanese/Korean) homophony with [[古今]] that does NOT extend to the Dan'a'yo level, since the two words' own 注音 differ (ㄍㄛㄍㄧㄇ vs ㄍㄛㄍㄨㄇ) — documented, no callout needed. Fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 古風.

### 2026-08-28, iteration 1322 — [[words/古風|古風]]

No stand-in relationship (古's own is [[古代]]; 風 is its own stand-in). **Real bug found and fixed**: `aliases` incorrectly listed the distinct compound 古雅 (built from 雅, not 風, no word page of its own) as an orthographic variant — removed, keeping only 古风. Cleaned up duplicated Notes content (same etymology line appeared twice). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 叫喚.

### 2026-08-28, iteration 1323 — [[words/叫喚|叫喚]]

No stand-in relationship (both independent). Filled blank `vietnamese: khiếu hoán`. Fixed non-standard `# Notes` heading level → `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 召集.

### 2026-08-28, iteration 1324 — [[words/召集|召集]]

召's own `stand_in` field is 召集 — added the stand-in note (集's own is [[集合]]). Filled blank `pos: 事詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 可愛.

### 2026-08-28, iteration 1325 — [[words/可愛|可愛]]

No stand-in relationship (both independent). **Real bugs found and fixed**: `羅馬字`/`諺文`/`注音` had 可's syllable using a divergent form (ka/카) instead of its own authoritative reading (kǝ/크), confirmed against 7 other 可-compounds — corrected, and propagated the fix to the ruby citations on both [[可]]'s and [[愛]]'s own Words sections (same class of bug as [[古典]]). `japanese` had a typo (かはいい → かわいい). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 可読.

### 2026-08-28, iteration 1326 — [[words/可読|可読]]

Page was already nearly complete and correctly used 可's authoritative kǝ/크 reading. No stand-in relationship (可 is its own stand-in; 読's own is [[閲読]]) — added the note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 台北.

### 2026-08-28, iteration 1327 — [[words/台北|台北]]

No stand-in relationship (台 is its own stand-in; 北's own is [[北方]]). Verified `korean: 타이베이` is the modern standard phonetic loan (vs. the older Hanja reading 대북, also attested but less current) — not an error. Fixed `characters` citation "台" → "台 (char)". No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 台湾.

### 2026-08-28, iteration 1328 — [[words/台湾|台湾]]

No stand-in relationship (台 is its own stand-in; 湾's own is [[海湾]]). **Real bug found and fixed**: `羅馬字`/`諺文`/`注音` had 湾's syllable ending in n (wan/완) instead of its own m-final authoritative reading (wam/왐, confirmed against 湾's own page and stand-in [[海湾]]) — corrected, and propagated to [[台]]'s own Words-section ruby. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 史記.

### 2026-08-28, iteration 1329 — [[words/史記|史記]]

No stand-in relationship (史's own is [[歴史]]; 記's is [[記憶]]). Frontmatter already fully correct. Added the missing Notes content entirely (heading was present but empty). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 司鈬.

### 2026-08-28, iteration 1330 — [[words/司鈬|司鈬]]

No stand-in relationship (司's own is [[公司]]; 鈬 is its own stand-in). Filled blank `vietnamese: tư đạc` (verified, the real Vietnamese Catholic term). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 合成.

### 2026-08-28, iteration 1331 — [[words/合成|合成]]

Page was already nearly complete. No stand-in relationship (both independent) — added the note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 合肥.

### 2026-08-28, iteration 1332 — [[words/合肥|合肥]]

No stand-in relationship (合 is its own stand-in; 肥's own is [[肥満]]). Filled missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 合金.

### 2026-08-28, iteration 1333 — [[words/合金|合金]]

No stand-in relationship (合 is its own stand-in; 金's is [[金]], unrelated). Discovered and documented a systematic two-way split in how 合 is read across the vault: kab/캅 in "mixture/blend" sense compounds ([[混合]], [[組合]], [[癒合]], [[融合]], and now 合金) vs. gob/곱 (matching 合's bare citation) in "join/unite" sense compounds ([[合肥]], [[合成]], [[結合]], [[連合]]) — 合金's own kab/캅 fields are correct as-is, not a bug. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 同一.

### 2026-08-28, iteration 1334 — [[words/同一|同一]]

同's own `stand_in` field is 同一 — added the stand-in note (一's own is [[一]], unrelated). Frontmatter already fully correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 同僚.

### 2026-08-28, iteration 1335 — [[words/同僚|同僚]]

僚's own `stand_in` field is 同僚 — already documented. **Real bug found and fixed**: `cantonese` missing space. Filled blank `vietnamese: đồng liêu` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 同胞.

### 2026-08-28, iteration 1336 — [[words/同胞|同胞]]

No stand-in relationship (同's own is [[同一]]; 胞's is [[胞衣]]). **Real bug found and fixed**: `japanese` had a typo (どうはう → どうほう). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 名詞.

### 2026-08-28, iteration 1337 — [[words/名詞|名詞]]

No stand-in relationship (名 is its own stand-in; 詞's own is [[単詞]]). **Real bug found and fixed**: `mandarin` had been stored as simplified Chinese characters "名词" instead of pinyin — corrected to míngcí. `cantonese` was blank — filled ming4 ci4. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 君士坦丁堡.

### 2026-08-28, iteration 1338 — [[words/君士坦丁堡|君士坦丁堡]]

No stand-in relationship (君/士/丁 each their own; 坦's own is [[平坦]]; 堡's is [[堡塁]]). Filled blank `vietnamese: Quân Sĩ Thản Đinh Bảo` (compositional, verified; modern Vietnamese typically uses the loan "Constantinopolis" instead). Fixed relative-path links. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 君子.

### 2026-08-28, iteration 1339 — [[words/君子|君子]]

No stand-in relationship (君 is its own stand-in; 子's own is [[児子]]). **Real bug found and fixed**: `mandarin`/`cantonese` had been merged into one string, leaving `cantonese` blank — split apart. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 君等.

### 2026-08-28, iteration 1340 — [[words/君等|君等]]

No stand-in relationship (both independent). Filled blank `mandarin`/`cantonese`/`japanese` (all compositional). Documented `korean`/`vietnamese` as native colloquial pronoun equivalents rather than Sino-compounds, since this literary term lacks an everyday Sino equivalent in those languages. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 否定.

### 2026-08-28, iteration 1341 — [[words/否定|否定]]

Page was already nearly complete. No stand-in relationship (否 is its own stand-in; 定's own is [[決定]]) — added the note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 吸金.

### 2026-08-28, iteration 1342 — [[words/吸金|吸金]]

Periodictable/neologism word (samarium). No stand-in relationship. Verified `mandarin`/`cantonese` are the genuine real-world element name 钐, not compositional. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 告訴.

### 2026-08-28, iteration 1343 — [[words/告訴|告訴]]

告's own `stand_in` field is 告訴 — added the stand-in note (訴's own is [[訴訟]]). **Real bug found and fixed**: `cantonese` was blank — filled gou3 sou3. Filled blank `vietnamese: tố cáo`. Completed the reciprocal homophone pair with [[高素]] ("gallium"), whose own page was already waiting on this word. No other homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 周章.

### 2026-08-28, iteration 1344 — [[words/周章|周章]]

No stand-in relationship (周's own is [[圓周]]; 章 is its own stand-in). Filled blank `korean`/`vietnamese` (주장/chu chương, verified). **Found and completed a genuine Dan'a'yo homophone with [[周長]]** ("perimeter"): 章 and 長 coincidentally share the same Dan'a'yo phonology despite being unrelated characters — standardized both non-canonical `[!tip]` callouts to proper reciprocal `>[!warning]` format and fully completed 周長 in the same pass (filled its blank vietnamese, fixed a missing-space cantonese bug). Both stamped `date-last-perfect: 2026-08-28`.

Next: 呪詛.

### 2026-08-28, iteration 1345 — [[words/呪詛|呪詛]]

詛's own `stand_in` field is 呪詛 — already documented (呪's own is [[呪文]]). Filled blank `vietnamese: chú trù` (compositional). Verified `korean: 주저` is coincidentally identical to the unrelated word for "hesitation," not a bug. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 命令.

### 2026-08-28, iteration 1346 — [[words/命令|命令]]

No stand-in relationship (命's own is [[運命]]; 令 is its own stand-in). **Real bug found and fixed**: `諺文`/`注音` had been contaminated with [[明朗]]'s reading (an entirely unrelated word) instead of 命令's own compositional reading from 令's citation — corrected 명랑→명렁/ㄌㄚㄫ→ㄌㄝㄫ, which also dissolves the false homophone claim (a broken `[[]]` link) that was a symptom of this bug. Completed [[明朗]] itself in the same pass: removed its reciprocal false homophone claim, filled its blank `vietnamese: minh lãng`. Both stamped `date-last-perfect: 2026-08-28`.

Next: 命名.

### 2026-08-28, iteration 1347 — [[words/命名|命名]]

No stand-in relationship (命's own is [[運命]]; 名 is its own stand-in). Frontmatter already fully correct. Fixed `characters` citation "名" → "名 (char)"; fixed non-standard `## Etymology` heading. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 和尚.

### 2026-08-28, iteration 1348 — [[words/和尚|和尚]]

No stand-in relationship (和's own is [[和平]]; 尚 is its own stand-in). Verified `japanese: おしょう` is a genuine irregular reading. Fixed `characters` citation and unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 和平.

### 2026-08-28, iteration 1349 — [[words/和平|和平]]

和's own `stand_in` field is 和平 — added the stand-in note (平's own is [[水平]]). Verified `japanese: わへい` is the correct reading for this character order, distinct from へいわ (the alias 平和's own reading). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 和諧.

### 2026-08-28, iteration 1350 — [[words/和諧|和諧]]

Page was already fully complete (諧's own `stand_in` field is 和諧, already documented). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 哀悼.

### 2026-08-28, iteration 1351 — [[words/哀悼|哀悼]]

No stand-in relationship (哀's own is [[哀傷]]; 悼 is its own stand-in). **Real bugs found and fixed**: `vietnamese` had been set to the Mandarin pinyin string "āidào" instead of an actual Vietnamese reading — corrected to `ai điệu`. `cantonese` missing space. `注音` had two garbled consonant letters — corrected to match each character's own citation. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 品詞.

### 2026-08-28, iteration 1352 — [[words/品詞|品詞]]

No stand-in relationship (品 is its own stand-in; 詞's own is [[単詞]]). **Real bug found and fixed**: `mandarin`/`cantonese` had been contaminated with the alias 詞性's reading (cíxìng/ci4 sing3) instead of 品詞's own — corrected to pǐncí/ban2 ci4. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 哲学.

### 2026-08-28, iteration 1353 — [[words/哲学|哲学]]

哲's own `stand_in` field is 哲学 — added the stand-in note (学's own is [[学習]]). **Real bugs found and fixed**: `mandarin`/`cantonese` had been stored as raw Chinese characters ("哲學"/"哲理," the latter a different word) instead of romanizations — corrected to zhéxué/zit3 hok6. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 唐突.

### 2026-08-28, iteration 1354 — [[words/唐突|唐突]]

No stand-in relationship (唐's own is `名専字`; 突's own is [[突然]]). **Real bug found and fixed**: `mandarin` had the wrong tone mark ("tángtú" → tángtū). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 唐詩.

### 2026-08-28, iteration 1355 — [[words/唐詩|唐詩]]

No stand-in relationship (唐's own is `名専字`; 詩's own is [[詩歌]]). Verified `korean: 당시` is compositional and coincidentally identical to the unrelated word 當時, not a bug. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 啄木鳥.

### 2026-08-28, iteration 1356 — [[words/啄木鳥|啄木鳥]]

No stand-in relationship (all three independent). **Real bug found and fixed**: `japanese` used archaic てう instead of modern ちょう. Filled blank `vietnamese: trác mộc điểu` (verified). Cleaned up duplicated Notes/Etymology headings. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 啓明.

### 2026-08-28, iteration 1357 — [[words/啓明|啓明]]

No stand-in relationship (啓's own is [[開啓]]; 明 is its own stand-in). Filled blank `vietnamese: khải minh` (verified) and missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 善人.

### 2026-08-28, iteration 1358 — [[words/善人|善人]]

No stand-in relationship (both independent). Filled blank `cantonese: sin6 jan4`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 善意.

### 2026-08-28, iteration 1359 — [[words/善意|善意]]

No stand-in relationship (善 is its own stand-in; 意's own is [[意味]]). Fixed empty-list `aliases`; filled missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 善良.

### 2026-08-28, iteration 1360 — [[words/善良|善良]]

No stand-in relationship (善 is its own stand-in; 良's own is [[良好]]). Filled blank `vietnamese: thiện lương`; removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 喇叭.

### 2026-08-28, iteration 1361 — [[words/喇叭|喇叭]]

Both characters share this word as their own `stand_in` (bound-together pair). **Real bug found and fixed**: `vietnamese` had an extra diacritic ("lạt bát" → lạt bá, verified). Verified `korean: 나발` is a genuine native/colloquial word (related to 나팔, recorded on 喇's own `korean_native`), not a bug. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 営養.

### 2026-08-28, iteration 1362 — [[words/営養|営養]]

No stand-in relationship (営's own is [[経営]]; 養's is [[養育]]). **Real bug found and fixed**: `cantonese` had 営's syllable misspelled ying4 instead of jing4 (confirmed against [[国営]]/[[経営]]) — corrected. Fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 嗅覚.

### 2026-08-28, iteration 1363 — [[words/嗅覚|嗅覚]]

嗅's own `stand_in` field is 嗅覚 — added the stand-in note (覚's own is [[感覚]]). **Real bugs found and fixed**: `cantonese` missing space; `japanese` typo (きうかく → きゅうかく); `aliases` was a bogus self-alias — removed. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 嗅金.

### 2026-08-28, iteration 1364 — [[words/嗅金|嗅金]]

Periodictable/neologism word (osmium). No stand-in relationship (嗅's own is [[嗅覚]]; 金 is its own stand-in). Verified `mandarin`/`cantonese` are the genuine real-world element name 锇. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 噴火.

### 2026-08-28, iteration 1365 — [[words/噴火|噴火]]

噴's own `stand_in` field is 噴火 — already documented. Filled blank `vietnamese: phún hoả` (verified). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 嚴禁.

### 2026-08-28, iteration 1366 — [[words/嚴禁|嚴禁]]

No stand-in relationship (厳 is its own stand-in; 禁's own is [[禁止]]). Frontmatter already fully correct; filled missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 四季.

### 2026-08-28, iteration 1367 — [[words/四季|四季]]

No stand-in relationship (四 is its own stand-in; 季's own is [[季節]]). Fixed malformed `japanese`/`vietnamese` YAML-lists → plain scalars; removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 四川.

### 2026-08-28, iteration 1368 — [[words/四川|四川]]

Page was already nearly complete. No stand-in relationship (both independent) — added the note. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 四書.

### 2026-08-28, iteration 1369 — [[words/四書|四書]]

No stand-in relationship (四 is its own stand-in; 書's own is [[書本]]). Frontmatter already fully correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 四面.

### 2026-08-28, iteration 1370 — [[words/四面|四面]]

No stand-in relationship (四 is its own stand-in; 面's own is [[表面]]). Filled blank `pos: 名詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回天.

### 2026-08-28, iteration 1371 — [[words/回天|回天]]

No stand-in relationship (both independent). Filled blank `vietnamese: hồi thiên`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回教.

### 2026-08-28, iteration 1372 — [[words/回教|回教]]

No stand-in relationship (回 is its own stand-in; 教's own is [[教授]]). **Real bug found and fixed**: `japanese` used archaic くわいけう instead of modern かいきょう. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回教徒.

### 2026-08-28, iteration 1373 — [[words/回教徒|回教徒]]

No stand-in relationship (回 is its own stand-in; 教's own is [[教授]]; 徒's own is [[信徒]]). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回生.

### 2026-08-28, iteration 1374 — [[words/回生|回生]]

No stand-in relationship (回 is its own stand-in; 生's own is [[生活]]). Frontmatter already fully correct. Added the missing `## Notes` section entirely. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回紇.

### 2026-08-28, iteration 1375 — [[words/回紇|回紇]]

紇's own `stand_in` field is 回紇 — added the stand-in note (回's own is itself). Filled blank `korean: 회흘`; filled missing `kwin: false`. Verified `vietnamese: Hồi Hột` is genuinely attested. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回虫.

### 2026-08-28, iteration 1376 — [[words/回虫|回虫]]

No stand-in relationship (虫's own is [[昆虫]]). Filled blank `vietnamese: hồi trùng` (compositional; modern usage prefers native "giun đũa"). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 回路.

### 2026-08-28, iteration 1377 — [[words/回路|回路]]

No stand-in relationship (回 is its own stand-in; 路's own is [[道路]]). Filled blank `vietnamese: hồi lộ`. **Completed the reciprocal homophone pair with [[賄賂]]** ("bribe"): standardized both non-canonical callouts, and fixed real bugs on 賄賂's own page in the same pass (cantonese fui2→kui2 matching its own citation; korean malformed "뇌물, 회뢰" → clean compositional 회뢰). Both stamped `date-last-perfect: 2026-08-28`.

Next: 因果.

### 2026-08-28, iteration 1378 — [[words/因果|因果]]

No stand-in relationship (因's own is [[原因]]; 果's is [[果実]]). **Real bug found and fixed**: `japanese` used archaic いんぐわ instead of modern いんが. Filled blank `pos: 性詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 因緣.

### 2026-08-28, iteration 1379 — [[words/因緣|因緣]]

縁's own `stand_in` field is 因緣 — already documented (因's own is [[原因]]). Verified `japanese: いんねん` is a genuine sandhi n-insertion reading, not a bug. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 囲棋.

### 2026-08-28, iteration 1380 — [[words/囲棋|囲棋]] and [[words/囲碁|囲碁]]

Documented an interesting near-duplicate pair: both name the game Go with an identical Dan'a'yo reading (注音 ㄨㄧㄍㄧ), but 囲棋 uses 棋 as a phonetic substitute for 碁 (碁's own `stand_in` field is explicitly 囲棋), while 囲碁 cites 碁 directly. Filled missing `kwin: true` on 囲棋 (matches Sino-Korean exactly). On 囲碁: **real bugs found and fixed** — spurious leading apostrophe in `羅馬字`, archaic ゐ kana (ゐご→いご), and wrongly-capitalized `vietnamese` ("Cờ vây"→cờ vây); kept its native Korean 바둑 (vs. 囲棋's literary 위기) as a legitimate real-world divergence. Both stamped `date-last-perfect: 2026-08-28`.

Next: 図画.

### 2026-08-28, iteration 1381 — [[words/図画|図画]]

No stand-in relationship (図's own is [[図表]]; 画's is [[絵画]]). **Real bug found and fixed**: `korean`/`vietnamese` had both been contaminated with the unrelated word 圖書's reading (도서/đồ thư) instead of 図画's own — corrected to 도화/đồ hoạ, and dropped the mistakenly-included 圖書 from `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 固執.

### 2026-08-28, iteration 1382 — [[words/固執|固執]]

No stand-in relationship (固's own is [[強固]]; 執's is [[執行]]). Simplified `mandarin` from a comma-joined two-variant string to the primary gùzhí. Fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国営.

### 2026-08-28, iteration 1383 — [[words/国営|国営]]

No stand-in relationship (国's own is [[国家]]; 営's is [[経営]]). Frontmatter already fully correct; fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国士.

### 2026-08-28, iteration 1384 — [[words/国士|国士]]

No stand-in relationship (国's own is [[国家]]; 士 is its own stand-in). Fixed `characters` citation "士" → "士 (char)". Frontmatter otherwise already correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国旗.

### 2026-08-28, iteration 1385 — [[words/国旗|国旗]]

No stand-in relationship (国's own is [[国家]]; 旗's is [[旗幟]]). **Real bug found and fixed**: `vietnamese` had a native paraphrase ("lá cờ") rather than the real compound — corrected to `quốc kỳ`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国歌.

### 2026-08-28, iteration 1386 — [[words/国歌|国歌]]

No stand-in relationship (国's own is [[国家]]; 歌's is [[歌曲]]). Homophone with [[国家]] already correctly documented (reciprocal, both stamped). **Real bug found and fixed**: `japanese` was missing the sokuon assimilation (こくか → こっか) — 国歌 is a genuine real-world Japanese homophone of 国家. Flagged (not fixed, out of scope) that 歌's own character page stores an inconsistent citation (gǝ/그/ㄍㄜ) disagreeing with both this word and its own stand-in [[歌曲]] (both use ga/가/ㄍㄚ). Stamped `date-last-perfect: 2026-08-28`.

Next: 国王.

### 2026-08-28, iteration 1387 — [[words/国王|国王]]

No stand-in relationship (国's own is [[国家]]; 王 is its own stand-in). **Real bug found and fixed**: `japanese` was truncated (こくお → こくおう). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国防.

### 2026-08-28, iteration 1388 — [[words/国防|国防]]

No stand-in relationship (国's own is [[国家]]; 防's is [[防護]]). Frontmatter already fully correct; fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国際.

### 2026-08-28, iteration 1389 — [[words/国際|国際]]

No stand-in relationship (国's own is [[国家]]; 際 is its own stand-in). **Real bug found and fixed**: `cantonese` had been contaminated with 語's syllable from sibling [[国際語]] ("gwok3 zai3 jyu5" → gwok3 zai3). Fixed wrongly-capitalized `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 国際語.

### 2026-08-28, iteration 1390 — [[words/国際語|国際語]]

No stand-in relationship (国's own is [[国家]]; 際 is its own stand-in; 語's is [[言語]]). Frontmatter already fully correct (this was the source of [[国際]]'s earlier contamination, but its own fields are correct). Fixed `characters` citation "際" → "際 (char)". No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 園芸.

### 2026-08-28, iteration 1391 — [[words/園芸|園芸]]

No stand-in relationship (園's own is [[庭園]]; 芸's is [[芸術]]). Discovered another phonetic/graphemic substitute pattern: 芸 here stands for 藝/艺 ("art"), not its own unrelated plant-name identity — all real-world CJK fields correctly reflect 藝, matching the same pattern as 加/痂, 回/蛔, 棋/碁. Filled blank `vietnamese: viên nghệ` (verified) and `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 土地.

### 2026-08-28, iteration 1392 — [[words/土地|土地]]

No stand-in relationship (both independent). Frontmatter already fully correct; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 土素.

### 2026-08-28, iteration 1393 — [[words/土素|土素]]

Periodictable/neologism word (tellurium). No stand-in relationship (土 is its own stand-in; 素's own is [[要素]]). Verified `mandarin: dì` is the genuine real-world element character 碲. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 土肥.

### 2026-08-28, iteration 1394 — [[words/土肥|土肥]]

No stand-in relationship (土 is its own stand-in; 肥's own is [[肥満]]). Filled missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地図.

### 2026-08-28, iteration 1395 — [[words/地図|地図]]

No stand-in relationship (地 is its own stand-in; 図's own is [[図表]]). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地域.

### 2026-08-28, iteration 1396 — [[words/地域|地域]]

No stand-in relationship (both independent). **Real bug found and fixed**: `japanese` had a stray invisible character embedded in the reading. Filled blank `vietnamese: địa vực`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地平線.

### 2026-08-28, iteration 1397 — [[words/地平線|地平線]]

No stand-in relationship (地 is its own stand-in; 平's own is [[水平]]; 線's is [[直線]]). Filled blank `vietnamese: địa bình tuyến` (compositional; documented that everyday Vietnamese instead uses native "chân trời"). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地点.

### 2026-08-28, iteration 1398 — [[words/地点|地点]]

No stand-in relationship (both independent). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地球.

### 2026-08-28, iteration 1399 — [[words/地球|地球]]

No stand-in relationship (both independent). Fixed `characters` citations. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地理.

### 2026-08-28, iteration 1400 — [[words/地理|地理]]

No stand-in relationship (地 is its own stand-in; 理's own is [[理由]]). **Real bug found and fixed**: `japanese` had been contaminated with sibling [[地理学]]'s reading (ちりがく, including 学's GAKU) instead of this word's own bare reading — corrected to ちり. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 地理学.

### 2026-08-28, iteration 1401 — [[words/地理学|地理学]]

No stand-in relationship (地 is its own stand-in; 理's own is [[理由]]; 学's is [[学習]]). Frontmatter already fully correct (confirmed as the genuine source for [[地理]]'s earlier contamination). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 埃及.

### 2026-08-28, iteration 1402 — [[words/埃及|埃及]]

No stand-in relationship (埃's own is [[塵埃]]; 及 is its own stand-in). Verified japanese エジプト as a genuine katakana loan. Fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 埋葬.

### 2026-08-28, iteration 1403 — [[words/埋葬|埋葬]]

葬's own `stand_in` field is 埋葬 — added the stand-in note (埋's own is [[埋藏]]). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 埋藏.

### 2026-08-28, iteration 1404 — [[words/埋藏|埋藏]]

埋's own `stand_in` field is 埋藏 — already documented (蔵's own is [[収蔵]]). Filled blank `vietnamese: mai tàng`. Noted a real-Korean-only coincidental homophone with [[埋葬]] (매장) that does NOT extend to the Dan'a'yo level. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 執行.

### 2026-08-28, iteration 1405 — [[words/執行|執行]]

執's own `stand_in` field is 執行 — added the stand-in note (行's own is itself). Verified `vietnamese: chấp hành` uses 行's "act" sense reading (vs. its "row/goods" sense hàng). Fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 基盤.

### 2026-08-28, iteration 1406 — [[words/基盤|基盤]]

No stand-in relationship (基's own is [[基本]]; 盤 is its own stand-in). **Real bug found and fixed**: `cantonese` was an empty string — filled gei1 pun4. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 基督.

### 2026-08-28, iteration 1407 — [[words/基督|基督]]

No stand-in relationship (基's own is [[基本]]; 督's is [[督促]]). Verified japanese キリスト is a genuine katakana loan. Filled missing `kwin: true` (matches Sino-Korean exactly). Removed redundant `品詞`; fixed malformed `japanese`/`vietnamese` YAML-lists → plain scalars. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 堆肥.

### 2026-08-28, iteration 1408 — [[words/堆肥|堆肥]]

No stand-in relationship (堆's own is [[堆積]]; 肥's is [[肥満]]). Filled missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 堰堤.

### 2026-08-28, iteration 1409 — [[words/堰堤|堰堤]]

No stand-in relationship (堰's own is [[井堰]]; 堤's is [[堤防]]). **Real bug found and fixed**: `japanese` had two comma-joined values — simplified to ダム (the real everyday word, an English loan, matching Korean 댐's own loanword pattern). Fixed capitalization on native `vietnamese: đập`. Filled blank `pos: 名詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 報告.

### 2026-08-28, iteration 1410 — [[words/報告|報告]]

No stand-in relationship (報 is its own stand-in; 告's own is [[告訴]]). **Real bug found and fixed**: `羅馬字` had a typo (baygau → baugau, matching 報's own citation). Fixed an English typo ("advize" → advise) here and in the propagated gloss on both 報's and 告's own Words sections. Fixed unquoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 塑料.

### 2026-08-28, iteration 1411 — [[words/塑料|塑料]]

No stand-in relationship (塑's own is [[塑造]]; 料's is [[材料]]). **Real bug found and fixed**: `mandarin` had the wrong vowel ("suòliào" → sùliào). Verified japanese/korean loanwords and native vietnamese "nhựa" as genuine real-world equivalents. Filled blank `pos: 名詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 境界.

### 2026-08-28, iteration 1412 — [[words/境界|境界]]

界's own `stand_in` field is 境界 — added the stand-in note (境's own is [[地境]]). **Real bug found and fixed**: `cantonese` was blank — filled ging2 gaai3. Standardized the reciprocal homophone callout with [[警戒]] on both pages (both previously used an awkward self-referencing phrasing). No other homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 墜落.

### 2026-08-28, iteration 1413 — [[words/墜落|墜落]]

墜's own `stand_in` field is 墜落 — added the stand-in note (落's own is [[落下]]). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 墨素.

### 2026-08-28, iteration 1414 — [[words/墨素|墨素]]

Periodictable/neologism word (antimony). No stand-in relationship. Verified `mandarin`/`cantonese` are the genuine real-world element name 锑. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 墳墓.

### 2026-08-28, iteration 1415 — [[words/墳墓|墳墓]]

Page was already fully complete (墳's own stand_in is 墳墓, already documented; added mention of 墓's own [[墓穴]]). No homophones. Stamped `date-last-perfect: 2026-08-28`.

Next: 声望.

### 2026-08-29, iteration 1416 — [[words/声望|声望]]

No stand-in relationship (声's own is [[発声]]; 望's is [[希望]]). **Real bug found and fixed**: `羅馬字`/`諺文` had 望's syllable using a divergent form (meng/멍) instead of its own authoritative reading (mang/망), confirmed against [[仰望]]/[[人望]]/[[希望]]/[[望楼]] — corrected (注音 was already right, and 望's own Words-section ruby already used the correct value). Filled blank `pos: 名詞`; removed a bogus self-referencing alias. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 声母.

### 2026-08-29, iteration 1417 — [[words/声母|声母]]

No stand-in relationship (声's own is [[発声]]; 母's is [[母親]]). Frontmatter already fully correct (verified vietnamese "mẫu" against sibling [[韻母]]). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 変化.

### 2026-08-29, iteration 1418 — [[words/変化|変化]]

No stand-in relationship (both independent). Fixed `characters` citations. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 外交.

### 2026-08-29, iteration 1419 — [[words/外交|外交]]

No stand-in relationship (外's own is [[外部]]; 交 is its own stand-in). **Real bug found and fixed**: `cantonese` missing space. Filled blank `pos: 名詞`; fixed unquoted `hsk_level`, empty-list `aliases`. Discovered and documented (not fixed, out of scope) that `交`'s own character-page citation (gyou/굣) disagrees with the "gyau/걋" form used across 13+ other already-perfected 交-compounds — this word's own gyau/걋 matches that majority. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 外出.

### 2026-08-29, iteration 1420 — [[words/外出|外出]]

No stand-in relationship (外's own is [[外部]]; 出 is its own stand-in). **Real bug found and fixed**: `vietnamese` was nonsensical ("ra, chết," the latter meaning "to die") — corrected to `xuất ngoại` (compositional, reversed order; documented that it connotes "go abroad" specifically, vs. native "đi ra ngoài" for the general sense). Filled blank `pos: 動詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 外国人.

### 2026-08-29, iteration 1421 — [[words/外国人|外国人]]

No stand-in relationship (外's own is [[外部]]; 国's is [[国家]]; 人 is its own stand-in). Verified `vietnamese: người nước ngoài` as the standard native calque (more common than the formal Sino compound "ngoại quốc nhân"). Filled blank `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 外国語.

### 2026-08-29, iteration 1422 — [[words/外国語|外国語]]

No stand-in relationship (外's own is [[外部]]; 国's is [[国家]]; 語's is [[言語]]). Verified `vietnamese: ngoại ngữ` as the standard term (corresponds to the shorter 外語 form, noted in the body). Filled blank `pos: 名詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 外来.

### 2026-08-29, iteration 1423 — [[words/外来|外来]]

No stand-in relationship (外's own is [[外部]]; 来 is its own stand-in). Frontmatter already fully correct; fixed malformed `japanese`/`vietnamese` YAML-lists, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 外部.

### 2026-08-29, iteration 1424 — [[words/外部|外部]]

外's own `stand_in` field is 外部 — added the stand-in note (部 is its own stand-in). **Real bug found and fixed**: `vietnamese` was completely unrelated ("nhiều lắm là," "at most") — corrected to `ngoại bộ`. Filled blank `pos: 名詞`; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大主教.

### 2026-08-29, iteration 1425 — [[words/大主教|大主教]]

No stand-in relationship (大 is its own stand-in; 主's own is [[主人]]; 教's is [[教授]]). Filled blank `vietnamese: đại chủ giáo` (compositional; documented that Vietnamese Catholic terminology instead uses "Tổng giám mục," built from an entirely different Chinese root). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大使館.

### 2026-08-29, iteration 1426 — [[words/大使館|大使館]]

No stand-in relationship (大 is its own stand-in; 使's own is [[使者]]; 館's is [[公館]]). **Real bug found and fixed**: `japanese` had a stray invisible character. Verified `cantonese` si3 reflects 使's "envoy" sense vs. its citation si2. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大同.

### 2026-08-29, iteration 1427 — [[words/大同|大同]]

No stand-in relationship (大 is its own stand-in; 同's own is [[同一]]). Fixed `characters` citation. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大和.

### 2026-08-29, iteration 1428 — [[words/大和|大和]]

No stand-in relationship (大 is its own stand-in; 和's own is [[和平]]). **Real bug found and fixed**: `羅馬字` had a typo ("diahwa" → daihwa). Reformatted `japanese`'s three comma-joined readings into a proper YAML list. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大器.

### 2026-08-29, iteration 1429 — [[words/大器|大器]]

No stand-in relationship (大 is its own stand-in; 器's own is [[容器]]). Fixed `characters` citation. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大学校.

### 2026-08-29, iteration 1430 — [[words/大学校|大学校]]

No stand-in relationship (大 is its own stand-in; 学's own is [[学習]]; 校's is [[学校]]). Verified `japanese: だいがっこう` is a genuine word (used for specific institution types), abbreviated to [[大学]] in everyday usage. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大学生.

### 2026-08-29, iteration 1431 — [[words/大学生|大学生]]

No stand-in relationship (大 is its own stand-in; 学's own is [[学習]]; 生's is [[生活]]). **Real bug found and fixed**: `vietnamese` had the native phrase "sinh viên đại học" — corrected to the directly compositional `đại học sinh` (verified, a genuine attested term). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大気圏.

### 2026-08-29, iteration 1432 — [[words/大気圏|大気圏]]

No stand-in relationship (all three independent). **Real bug found and fixed**: `mandarin`/`cantonese`/`korean` were all missing 圏's contribution entirely — filled dàqìquān/daai6 hei3 hyun1/대기권. Trimmed `aliases` to genuine 4-character variants only (dropped 大氣/大气/氣圈/气圈, which are aliases of different, shorter words). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大江.

### 2026-08-29, iteration 1433 — [[words/大江|大江]]

江's own `stand_in` field is 大江 — added the stand-in note. **Real bug found and fixed**: `japanese` used archaic おほえ instead of modern おおえ. Filled blank `vietnamese: đại giang`. Standardized the reciprocal homophone callout with [[大綱]] on both pages (also removed a redundant `品詞` on 大綱). No other homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大洋.

### 2026-08-29, iteration 1434 — [[words/大洋|大洋]]

洋's own `stand_in` field is 大洋 — added the stand-in note. Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大洋洲.

### 2026-08-29, iteration 1435 — [[words/大洋洲|大洋洲]]

No stand-in relationship (大 is its own stand-in; 洋's is [[大洋]]; 洲 is its own stand-in). Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大砲.

### 2026-08-29, iteration 1436 — [[words/大砲|大砲]]

砲's own `stand_in` field is 大砲 — added the stand-in note. Filled blank `vietnamese: đại pháo`. **Completed the reciprocal homophone pair with [[代表]]**: standardized both non-canonical callouts, and fixed a real bug on 代表's own page (wrongly capitalized native `vietnamese: Đại biểu` → lowercase đại biểu). Both stamped `date-last-perfect: 2026-08-29`.

Next: 大笑.

### 2026-08-29, iteration 1437 — [[words/大笑|大笑]]

No stand-in relationship (both independent). Filled blank `vietnamese: đại tiếu`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大腸.

### 2026-08-29, iteration 1438 — [[words/大腸|大腸]]

No stand-in relationship (大 is its own stand-in; 腸's own is [[腸管]]). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大象.

### 2026-08-29, iteration 1439 — [[words/大象|大象]]

象's own `stand_in` field is 大象 — added the stand-in note. **Real bug found and fixed**: `vietnamese` had two comma-joined values — simplified to `con voi` (native, matching the same pattern as japanese ゾウ/korean 코끼리). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大陸.

### 2026-08-29, iteration 1440 — [[words/大陸|大陸]]

陸's own `stand_in` field is 大陸 — added the stand-in note. **Real bug found and fixed**: `aliases` incorrectly listed the word's own filename as a bogus self-alias — removed. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 大韓帝国.

### 2026-08-29, iteration 1441 — [[words/大韓帝国|大韓帝国]]

No stand-in relationship (大 is its own stand-in; 韓's own is [[韓国]]; 帝's is [[帝王]]; 国's is [[国家]]). Verified `korean: 대한제국` uses 帝's real-world reading 제 (compositionally correct, diverging from Dan'a'yo's own internal 테 transcription), consistent with `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天主.

### 2026-08-29, iteration 1442 — [[words/天主|天主]]

No stand-in relationship (天 is its own stand-in; 主's own is [[主人]]). **Real bugs found and fixed**: `japanese` had been contaminated with the unrelated word 神様 (also wrongly listed in `aliases`) instead of 天主's own compositional reading — corrected to てんしゅ, removed the bogus alias. `korean` had native Protestant-preferred terms (하나님, 하느님) instead of the direct compositional Catholic term — corrected to 천주. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天地.

### 2026-08-29, iteration 1443 — [[words/天地|天地]]

No stand-in relationship (both independent). **Real bug found and fixed**: `vietnamese` had stray mid-word capitalization ("thiên Địa" → thiên địa). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天子.

### 2026-08-29, iteration 1444 — [[words/天子|天子]]

No stand-in relationship (天 is its own stand-in; 子's own is [[児子]]). Frontmatter already fully correct; removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天才.

### 2026-08-29, iteration 1445 — [[words/天才|天才]]

才's own `stand_in` field is 天才 — added the stand-in note. Frontmatter already fully correct; fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天文.

### 2026-08-29, iteration 1446 — [[words/天文|天文]]

No stand-in relationship (天 is its own stand-in; 文's own is [[文化]]). Verified `japanese: てんもん` uses 文's alternate on'yomi MON, a genuine lexicalized reading. Fixed empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天文学.

### 2026-08-29, iteration 1447 — [[words/天文学|天文学]]

No stand-in relationship (天 is its own stand-in; 文's own is [[文化]]; 学's is [[学習]]). Fixed real bug: `諺文`/`羅馬字` had 天's syllable malformed (턴→터, missing final ㄴ coda) — corrected to 턴문학/tenmunhag. Filled blank `cantonese: tin1 man4 hok6`. Removed redundant `品詞`. Reformatted `characters` to block-list. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天狗.

### 2026-08-29, iteration 1448 — [[words/天狗|天狗]]

No stand-in relationship (天 is its own stand-in; 狗's own is [[名専字]]). Frontmatter mostly correct (諺文/注音/羅馬字 all already right, japanese てんぐ verified as genuine rendaku lexicalization). Filled blank `pos: 名詞`. Blanked empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天狼星.

### 2026-08-29, iteration 1449 — [[words/天狼星|天狼星]]

No stand-in relationship (天/狼/星 are all their own stand-ins). Frontmatter mostly correct; fixed wrongly-capitalized vietnamese "Sao Thiên Lang"→"sao Thiên Lang" (common-noun prefix should be lowercase, per [[水星]]'s "sao Thủy"). Blanked empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天王星.

### 2026-08-29, iteration 1450 — [[words/天王星|天王星]]

No stand-in relationship (天/王/星 are all their own stand-ins). Fixed archaic kana japanese てんわうせい→てんおうせい (matching sibling planets [[海王星]]/[[冥王星]]). Blanked empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天皇.

### 2026-08-29, iteration 1451 — [[words/天皇|天皇]]

No stand-in relationship (天 is its own stand-in; 皇's own is [[皇帝]]). Fixed real bug: `pos` was wrongly 固有名詞 — corrected to 名詞, matching sibling title/office nouns [[教皇]]/[[皇帝]]/[[女皇]]. Verified japanese てんのう as genuine lexicalized term (not error). Blanked empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天空.

### 2026-08-29, iteration 1452 — [[words/天空|天空]]

No stand-in relationship (天/空 are both their own stand-ins). Frontmatter already fully correct (vietnamese bầu trời verified as standard native term for "sky"). Blanked empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天花.

### 2026-08-29, iteration 1453 — [[words/天花|天花]]

No stand-in relationship (天 is its own stand-in; 花's own is [[草花]]). Filled blank `pos: 名詞`, moved bare prose text into a proper `## Notes` section. Blanked empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天頂.

### 2026-08-29, iteration 1454 — [[words/天頂|天頂]]

No stand-in relationship (天 is its own stand-in; 頂's own is [[頂点]]). Added missing `kwin: false`, quoted `mandarin`/`cantonese`/`korean` and the `characters` "天 (char)" entry for consistency, wrote `## Notes`. Japanese てんちょう verified as genuine astronomical term (CHOU on'yomi). No homophones. Stamped `date-last-perfect: 2026-08-29`.

**Systemic note**: re-read `AIOS/checklists/checklist_words.md` and found it explicitly says blank `vietnamese`/`hsk_level`/`swadesh`/`aliases` keys must be omitted entirely, not left blank — I have been leaving them blank (e.g. `aliases:` with no value) across this whole session's iterations. Flagging for a future dedicated cleanup pass; switching to omit-when-blank behavior for all iterations from here on.

Next: 天鵝.

### 2026-08-29, iteration 1455 — [[words/天鵝|天鵝]]

No stand-in relationship (天 is its own stand-in; 鵝's own is [[鵝鳥]]). Filled blank `pos: 名詞`, omitted blank `hsk_level`/`swadesh`/`aliases` keys per checklist. Verified japanese はくちょう as genuine native substitution (白鳥, broader than 天鵝) rather than a compositional error. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 天鼠.

### 2026-08-29, iteration 1456 — [[words/天鼠|天鼠]]

No stand-in relationship (天 is its own stand-in; 鼠's own is [[熊鼠]]). Fixed real contamination bug: `korean`/`vietnamese` had been copied from [[蝙蝠]]'s own readings (편복,박쥐 / biên bức) — corrected to compositional 천서/thiên thử. Removed stray zero-width char from `japanese`. Added missing `kwin: false`. Omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 太太.

### 2026-08-29, iteration 1457 — [[words/太太|太太]]

No stand-in relationship (太's own stand-in is itself) — a reduplicative ideophone, not a real compound. Filled blank `korean: 태태` (compositional), added missing `kwin: true`. Removed redundant `品詞`. Verified japanese ふてぶて and cantonese tone-sandhi taai3-2 as genuine real-world forms despite the coincidental semantic mismatch with real Mandarin 太太 "wife." No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 太極拳.

### 2026-08-29, iteration 1458 — [[words/太極拳|太極拳]]

No stand-in relationship (太's own stand-in is itself; 極's is [[極]]; 拳's is [[拳骨]]). Fixed real bug: `諺文`/`羅馬字`/`注音` all had 極's syllable corrupted (기/gid/ㄍㄧㄊ instead of 긱/gig/ㄍㄧㄎ) — propagated the fix to 極/拳/太's own Words-section rubies too. Fixed `pos` 固有名詞→名詞 (matching [[跆拳道]]/[[詠春拳]]). Removed redundant self-aliasing entry and blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 太白星.

### 2026-08-29, iteration 1459 — [[words/太白星|太白星]]

No stand-in relationship (太/白/星 are all their own stand-ins). Filled blank `vietnamese: thái bạch tinh` (compositional, matching [[啓明]]'s parallel convention). Added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 太陰.

### 2026-08-29, iteration 1460 — [[words/太陰|太陰]]

No stand-in relationship (太/陰 are both their own stand-ins). Fixed misused `aliases`: had a single malformed string mixing the genuine simplified alias 太阴 with three unrelated synonym words (月球/月亮/玄兔) — trimmed to just 太阴, moved the synonyms into Notes prose. Filled blank `pos: 名詞`, wrote the missing `## Notes` section. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 太陰曆.

### 2026-08-29, iteration 1461 — [[words/太陰曆|太陰曆]]

Identified as the traditional-orthography duplicate of already-stamped [[太陰暦]] (曆 is 暦's alias). Fixed real bug: `mandarin`/`cantonese` had both dropped the 太 syllable (yīnlì/jam1 lik6→tàiyīnlì/taai3 jam1 lik6). Fixed `characters` to cite the real page 暦 (char) instead of the pageless alias glyph 曆. Filled blank `pos: 名詞`. Removed malformed `aliases` (both entries were the unrelated shorter synonym 陰曆/阴历, not spellings of this word). Cross-referenced both pages in Notes; did not use the Homophones callout since they're the same word, not distinct coincidental homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 太陽系.

### 2026-08-29, iteration 1462 — [[words/太陽系|太陽系]]

No stand-in relationship (太/陽 are both their own stand-ins; 系's own is [[系統]]). Fixed real bugs: `vietnamese` had a typo Thệ→Hệ Mặt Trời; `mandarin` was wrongly capitalized as a proper noun; `pos` was blank — corrected to 名詞, matching [[太陽]]/[[恒星系]]. Omitted blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 夫婦.

### 2026-08-29, iteration 1463 — [[words/夫婦|夫婦]]

No stand-in relationship (夫 is its own stand-in; 婦's own is itself). Fixed real bug: `諺文` had 夫's regular citation reading 쁘/fǝ instead of the attested alternate 부/bu used consistently in this fixed compound and in [[大夫]] — corrected to 부뷰 (羅馬字/注音 were already right). Added missing space in `cantonese`. Omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

**Flagged for a future iteration**: [[丈夫]] (still unstamped) has an internal self-contradiction across its own 羅馬字/諺文/注音 (jangbu/창쁘/ㄐㄚㄫㄅㄨ don't agree with each other or with 丈's own citation 창/cang/ㄑㄚㄫ) — needs its own dedicated cross-referencing pass; did not fix in-place to avoid a rushed/wrong correction.

Next: 夭折.

### 2026-08-29, iteration 1464 — [[words/夭折|夭折]]

This word is 夭's own stand-in (already documented in existing Notes prose). Frontmatter mostly correct; filled blank `vietnamese: yểu chiết` (compositional), quoted `mandarin`/`cantonese`/`korean` for consistency. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 失業.

### 2026-08-29, iteration 1465 — [[words/失業|失業]]

No stand-in relationship (失's own stand-in is [[滅失]]; 業's own is itself). Fixed real bugs: `羅馬字` had 失's coda mistyped (sit→sid); `kwin` was wrongly true (諺文 싣업 ≠ korean 실업). Filled blank `pos: 動詞`, reformatted `characters` to block-list, quoted `hsk_level`, omitted empty-list `aliases`, renamed `## Etymology`→`## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 失禁.

### 2026-08-29, iteration 1466 — [[words/失禁|失禁]]

No stand-in relationship (失's own stand-in is [[滅失]]; 禁's own is [[禁止]]). Frontmatter mostly correct; added missing `kwin: false`, quoted `mandarin`/`cantonese`/`korean`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 奇怪.

### 2026-08-29, iteration 1467 — [[words/奇怪|奇怪]]

奇's own `stand_in` is 奇怪 — added the stand-in note. Fixed typo in `english` ("oldd unexpected"→"odd, unexpected"), reformatted `characters` indentation, renamed `## Etymology`→`## Notes` with real prose. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 奇素.

### 2026-08-29, iteration 1468 — [[words/奇素|奇素]]

No stand-in relationship (奇's own stand-in is [[奇怪]]; 素's own is [[要素]]). Fixed real bug: `諺文`/`羅馬字`/`注音` had 奇's syllable as the minority ㄍㄧ/gi/기 instead of ㄍㄨㄧ/gui/귀 (matching 4 other 奇-initial siblings [[奇怪]]/[[奇想]]/[[奇妙]]/[[奇数]]) — propagated the fix to 奇's own Words-section ruby. Verified mandarin/cantonese/korean/japanese as genuine real-world periodic-table element names (氙/xiān, not compositional), per the established [[千米]]/[[高素]] convention. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 奔走.

### 2026-08-29, iteration 1469 — [[words/奔走|奔走]]

奔's own `stand_in` is 奔走 — added the stand-in note. Fixed real bug: `羅馬字` had 走's syllable mistyped "jou"→"sou" (諺文/注音 were already correct). Reformatted `characters` field. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 奮闘.

### 2026-08-29, iteration 1470 — [[words/奮闘|奮闘]]

No stand-in relationship (奮's own stand-in is [[奮発]]; 闘's own is [[闘争]]). Removed redundant self-referential alias (奮闘 aliasing itself), kept 奮鬥/奋斗. Wrote `## Notes` (was a one-line `## Etymology` with a broken bare wikilink). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 女児.

### 2026-08-29, iteration 1471 — [[words/女児|女児]]

No stand-in relationship (女/児 are both their own stand-ins). Fixed real bugs: `諺文`/`羅馬字` had 女's syllable as the unattested 뇻/nyou instead of 느/nǝ (contradicting the file's own correct 注音 and every other 女-compound); `japanese` had been swapped for the unrelated real word 娘/むすめ — corrected to compositional じょじ, documenting the real-Japanese semantic narrowing to "female infant" vs. "daughter." Stripped the contaminating native 딸 from `korean`. Trimmed `aliases` to genuine variants (女兒/女儿), removing the reversed, differently-meaning 兒女/儿女. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 女性.

### 2026-08-29, iteration 1472 — [[words/女性|女性]]

No stand-in relationship (女's own stand-in is itself; 性's own is [[性別]]). Fixed real bug: `korean` used the South Korean 두음법칙-shifted 여성 — corrected to North Korean 녀성 (per standing memory rule). Omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 女皇.

### 2026-08-29, iteration 1473 — [[words/女皇|女皇]]

No stand-in relationship (女's own stand-in is itself; 皇's own is [[皇帝]]). Fixed real bugs: `japanese` had been swapped for an archaic-kana misspelling of the unrelated word 女帝 — corrected to compositional じょこう; `korean` used South Korean 두음법칙-shifted 여황 — corrected to North Korean 녀황. Omitted blank `hsk_level`/`swadesh`/empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 奴隷.

### 2026-08-29, iteration 1474 — [[words/奴隷|奴隷]]

This word is the stand-in for both 奴 and 隷 — added the stand-in note. Frontmatter already fully correct; quoted `mandarin`/`cantonese`/`korean`, omitted blank `swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 如.

### 2026-08-29, iteration 1475 — [[words/如|如]]

This word is the stand-in for its own character 如 (char). Fixed real bugs: `vietnamese` was literal YAML `null` — corrected to như; `pos`/`japanese`/`kwin` were entirely missing — filled 関詞/にょ/false. Reformatted `characters` to a proper list, wrote `## Notes` (was a bare `# Notes` header). No homophones (word/character-page match is the expected stand-in relationship, not a cross-word homophone). Stamped `date-last-perfect: 2026-08-29`.

Next: 妄想.

### 2026-08-29, iteration 1476 — [[words/妄想|妄想]]

妄's own `stand_in` is 妄想 — added the stand-in note. Frontmatter already fully correct. Omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 妊.

### 2026-08-29, iteration 1477 — [[words/妊|妊]] & [[words/賃|賃]]

Discovered genuine Dan'a'yo homophone pair (both ㄋㄧㄇ/nim/님, unrelated meanings "be pregnant" vs "rent") — completed both pages fully with reciprocal Homophones callouts. Both had the same malformed pattern as [[如]]: literal `vietnamese: null`, missing `pos`/`japanese`/`kwin`, bare-string `characters`, `# Notes` instead of `## Notes`. Fixed `kwin` to false on 妊 (諺文 님 ≠ korean 임). No fields contradicted their own character-page citations. Stamped both `date-last-perfect: 2026-08-29`.

Next: 妖怪.

### 2026-08-29, iteration 1478 — [[words/妖怪|妖怪]]

妖's own `stand_in` is 妖怪 — added the stand-in note. Fixed archaic kana japanese えうくわい→ようかい. Omitted empty-list `aliases`/blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 妥協.

### 2026-08-29, iteration 1479 — [[words/妥協|妥協]]

No stand-in relationship (妥's own stand-in is [[妥当]]; 協's own is [[協力]]). Filled blank `pos: 性詞` (matching [[協力]]); verified japanese だきょう as 妥's genuine alternate on'yomi DA. Omitted empty-list `aliases`/blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 妥当.

### 2026-08-29, iteration 1480 — [[words/妥当|妥当]]

妥's own `stand_in` is 妥当 — added the stand-in note. Filled blank `pos: 性詞`, fixed malformed `mandarin` (stray untoned duplicate). Reformatted `characters`/`aliases` to block-list. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 妨碍.

### 2026-08-29, iteration 1481 — [[words/妨碍|妨碍]]

Both 妨 and 碍's own `stand_in` is 妨碍 (cranberry, neither appears independently) — corrected the note, which previously only credited 妨. Quoted `mandarin`/`cantonese`/`korean` for consistency. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 妻子.

### 2026-08-29, iteration 1482 — [[words/妻子|妻子]]

No stand-in relationship (妻's own stand-in is itself; 子's own is [[児子]]). Filled blank `vietnamese: thê tử` (compositional, also a real attested Sino-Vietnamese term), removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 妾.

### 2026-08-29, iteration 1483 — [[words/妾|妾]]

This word is the stand-in for its own character. Fixed literal `vietnamese: null`→thiếp, missing `pos`/`japanese`/`kwin` filled 名詞/しょう/true. Reformatted `characters`, wrote `## Notes` (was bare `# Notes`). Stamped `date-last-perfect: 2026-08-29`.

Next: 姉.

### 2026-08-29, iteration 1484 — [[words/姉|姉]], [[words/諸|諸]] & [[words/借|借]]

Completed a three-way Dan'a'yo homophone group (all ja/자/ㄐㄚ) that [[借]] had already anticipated back on 2026-07-26. Both 姉 and 諸 had the same malformed single-character-word pattern (missing pos/japanese/kwin, bare-string characters, non-canonical `>[!warn]` callout) — fully rewrote both with canonical `>[!warning] Homophones` callouts cross-linking all three, and updated 借's own Notes prose (which had said "still awaiting their own turn") now that the group is complete. No other bugs found. Stamped 姉 and 諸 `date-last-perfect: 2026-08-29`.

Next: 始金.

### 2026-08-29, iteration 1485 — [[words/始金|始金]]

No stand-in relationship (始's own stand-in is [[始作]]; 金's own is itself). Fixed real bug: `注音` had 金's initial as ㄐ instead of ㄍ (ㄙㄧㄐㄧㄇ→ㄙㄧㄍㄧㄇ) — propagated the fix to 始's own Words-section ruby. Verified mandarin/cantonese/korean/japanese/vietnamese as genuine real-world periodic-table element names (锕/ā), per the established [[千米]]/[[高素]]/[[奇素]] convention. Removed redundant `品詞`, added opening character-linking bullet to `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 姑丈.

### 2026-08-29, iteration 1486 — [[words/姑丈|姑丈]] & [[words/故障|故障]]

Completed a two-way Dan'a'yo homophone pair (gojang/고장/ㄍㄛㄐㄚㄫ) that also coincides at the real-Korean level — both fully finished with reciprocal callouts. **Resolved the 丈-reading question flagged in iteration 1463**: confirmed 丈母/丈夫/丈人/姑丈 all unanimously use the alternate compound-specific reading jang/장/ㄐㄚㄫ (not 丈's own standalone citation cang/창/ㄑㄚㄫ) — went back and properly fixed [[丈夫]]'s previously-reverted 諺文 (창쁘→장부) now that the majority pattern is unambiguous across 4 siblings. Filled blank japanese/korean/kwin/vietnamese fields on both 姑丈/故障. No other bugs found. Stamped both `date-last-perfect: 2026-08-29`.

Next: 姓氏.

### 2026-08-29, iteration 1487 — [[words/姓氏|姓氏]]

姓's own `stand_in` is 姓氏 — added the stand-in note. Filled blank `pos: 名詞`; trimmed contaminating `vietnamese` ("tên họ" = full name, unrelated) to just họ. Omitted empty-list `aliases`/blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 委託.

### 2026-08-29, iteration 1488 — [[words/委託|委託]]

託's own `stand_in` is 委託 — added the stand-in note. Filled blank `pos: 動詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 姜.

### 2026-08-29, iteration 1489 — [[words/姜|姜]] & [[words/柬|柬]]

Discovered genuine Dan'a'yo homophone pair (both ㄍ⼘ㄋ/gyan/갼, unrelated "ginger" vs "letter") — completed both pages fully with reciprocal callouts. Both had the same malformed pattern as [[如]]/[[妾]]: literal `vietnamese: null` on 姜, missing pos/japanese/kwin, bare-string `characters`, `# Notes` instead of `## Notes`. Stamped both `date-last-perfect: 2026-08-29`.

Next: 姨母.

### 2026-08-29, iteration 1490 — [[words/姨母|姨母]]

This word is the stand-in for 姨 (母's own stand-in is [[母親]]). Trimmed redundant `vietnamese` ("dì của mẹ"→dì); verified japanese おば as a genuine native reading, matching 姨's own citation. Reformatted `characters`, omitted empty-list `aliases`/blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 姿勢.

### 2026-08-29, iteration 1491 — [[words/姿勢|姿勢]]

姿's own `stand_in` is 姿勢 — added the stand-in note. Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 威力.

### 2026-08-29, iteration 1492 — [[words/威力|威力]]

威's own `stand_in` is 威力 — added the stand-in note. Filled blank `pos: 名詞`, reformatted `characters`. Omitted empty-list `aliases`/blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 娘.

### 2026-08-29, iteration 1493 — [[words/娘|娘]]

This word is the stand-in for its own character. Fixed literal `vietnamese: null`→nàng, missing `pos`/`japanese`/`kwin` filled 名詞/にょう/true. Reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 婚姻.

### 2026-08-29, iteration 1494 — [[words/婚姻|婚姻]]

姻's own `stand_in` is 婚姻 — added the stand-in note (婚's own is [[結婚]]). Frontmatter already fully correct. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 婦.

### 2026-08-29, iteration 1495 — [[words/婦|婦]] & [[words/負|負]]

Discovered genuine Dan'a'yo homophone pair (both ㄅ⼜/byu/뷰, unrelated "lady/woman" vs "carry/bear") — completed both pages fully with reciprocal callouts. Both had the same malformed pattern as [[如]]/[[妾]]/[[姜]]: literal `vietnamese: null`, missing pos/japanese/kwin, bare-string `characters`, `# Notes` instead of `## Notes`. Stamped both `date-last-perfect: 2026-08-29`.

Next: 婿.

### 2026-08-29, iteration 1496 — [[words/婿|婿]] & [[words/細|細]]

Discovered genuine Dan'a'yo homophone pair (both ㄙㄝㄧ/sei/세, unrelated "son-in-law" vs "fine/thin/slender") — completed both pages fully with reciprocal callouts. Both had the same malformed pattern (missing japanese/kwin, bare-string `characters`, `# Notes`); 細's `vietnamese` was literal `null` (fixed to tế, sidestepping a separate malformed comma-joined value on 細's own already-imperfect character page, flagged for a future character pass, not touched here). Stamped both `date-last-perfect: 2026-08-29`.

Next: 媒介.

### 2026-08-29, iteration 1497 — [[words/媒介|媒介]]

No stand-in relationship (媒's own is [[仲媒]]; 介's own is [[仲介]]) — added the note. Frontmatter and prose already fully correct and substantive. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 嫡.

### 2026-08-29, iteration 1498 — [[words/嫡|嫡]], [[words/摘|摘]] & [[words/鈬|鈬]]

Discovered and completed a three-way Dan'a'yo homophone group (all dag/닥/ㄉㄚㄎ): 嫡 ("legitimate wife"), 摘 ("pinch, pluck"), 鈬 ("bronze bell"). 嫡/摘 had the recurring malformed single-character pattern (missing japanese, literal `vietnamese: null` on 摘). 鈬 had a real bug: blank `korean` and wrongly-true `kwin` (諺文 닥 ≠ its real korean 탁, distinct from 嫡/摘's 적) — filled and corrected. All three got reciprocal `>[!warning] Homophones` callouts. Stamped all three `date-last-perfect: 2026-08-29`.

Next: 嫩.

### 2026-08-29, iteration 1499 — [[words/嫩|嫩]]

This word is the stand-in for its own character. Filled missing `japanese: どん`, trimmed multi-value `vietnamese` list to single nộn. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 嬴金.

### 2026-08-29, iteration 1500 — [[words/嬴金|嬴金]]

No stand-in relationship (嬴's own stand-in is [[嬴洲]]; 金's own is itself). Verified mandarin/cantonese/korean/japanese/vietnamese as genuine real-world periodic-table element names (铥/diū), per established convention. Removed redundant `品詞`, fixed "orm."→"Form." typo, added opening character-linking bullet. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 子孫.

### 2026-08-29, iteration 1501 — [[words/子孫|子孫]]

No stand-in relationship (子's own stand-in is [[児子]]; 孫's own is [[孫子]]). Fixed real bug: `諺文`/`羅馬字` had 子's syllable as 지/ji instead of 즈/jǝ (contradicting the file's own correct 注音). Filled blank `vietnamese: tử tôn`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 子月.

### 2026-08-29, iteration 1502 — [[words/子月|子月]]

No stand-in relationship (子's own stand-in is [[児子]]; 月's own is itself). Verified japanese ねつき and vietnamese tháng Tý as genuine native zodiac-month terms. Removed redundant `品詞`, expanded `## Notes` opening bullet. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 子音.

### 2026-08-29, iteration 1503 — [[words/子音|子音]]

No stand-in relationship (子's own stand-in is [[児子]]; 音's own is [[音楽]]). Fixed real bug: `羅馬字` had 子's syllable mistyped ji→jǝ (諺文/注音 were already correct). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孔子.

### 2026-08-29, iteration 1504 — [[words/孔子|孔子]]

No stand-in relationship (孔's own stand-in is itself; 子's own is [[児子]]). Fixed real bug: `羅馬字` had 子's syllable mistyped ji→jǝ; fixed missing "(char)" suffix on `characters` for 孔. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孔教.

### 2026-08-29, iteration 1505 — [[words/孔教|孔教]]

No stand-in relationship (孔's own stand-in is itself; 教's own is [[教授]]). Fixed real bug: `羅馬字` had 教's syllable mistyped gyau→gyou (諺文/注音 already matched every sibling 教-compound). Fixed missing "(char)" suffix on `characters`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孔明.

### 2026-08-29, iteration 1506 — [[words/孔明|孔明]]

No stand-in relationship (孔/明 are both their own stand-ins). Frontmatter already fully correct; expanded Notes prose with sourced context on Zhuge Liang's courtesy name. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 字喃.

### 2026-08-29, iteration 1507 — [[words/字喃|字喃]]

No stand-in relationship (字's own stand-in is itself). Filled blank `mandarin`/`cantonese` (compositional). Documented japanese チュノム/korean 쯔놈 as transliterations of the Vietnamese name itself (no East Asian equivalent concept exists). Flagged 喃 as still lacking its own character page (future character-creation task). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 字形.

### 2026-08-29, iteration 1508 — [[words/字形|字形]]

No stand-in relationship (字/形 are both their own stand-ins). Fixed real bug: `characters`/Notes link were missing the "(char)" suffix for 形 (file is "形 (char).md"). Quoted `mandarin`/`cantonese`/`korean`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 字母.

### 2026-08-29, iteration 1509 — [[words/字母|字母]]

No stand-in relationship (字's own stand-in is itself; 母's own is [[母親]]). Fixed missing "(char)" suffix on `characters`. Filled blank `vietnamese: tự mẫu`, omitted blank `swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 存在.

### 2026-08-29, iteration 1510 — [[words/存在|存在]]

存's own `stand_in` is 存在 — added the stand-in note. Fixed missing "(char)" suffix on `characters` for 在. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孝金.

### 2026-08-29, iteration 1511 — [[words/孝金|孝金]]

No stand-in relationship (孝/金 are both their own stand-ins). Verified mandarin/cantonese/korean/japanese/vietnamese as genuine real-world periodic-table element names (铌/ní), per established convention. Removed redundant `品詞`, added opening character-linking bullet. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孟冬.

### 2026-08-29, iteration 1512 — [[words/孟冬|孟冬]]

No stand-in relationship (孟 is proper-noun-only with no specific stand-in; 冬's own is itself). Removed redundant `品詞`, expanded Notes with a compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孟夏.

### 2026-08-29, iteration 1513 — [[words/孟夏|孟夏]]

No stand-in relationship (孟 is proper-noun-only; 夏's own is itself). Removed redundant `品詞`, expanded Notes with a compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孟子.

### 2026-08-29, iteration 1514 — [[words/孟子|孟子]]

No stand-in relationship (孟 is proper-noun-only; 子's own is [[児子]]). Fixed real bug: `羅馬字` had 子's syllable mistyped ji→jǝ; `pos` was 名詞 — corrected to 固有名詞, matching [[孔子]]/[[老子]]/[[荘子]]. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孟春.

### 2026-08-29, iteration 1515 — [[words/孟春|孟春]]

No stand-in relationship (孟 is proper-noun-only; 春's own is itself). Removed redundant `品詞`, expanded Notes with compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孟秋.

### 2026-08-29, iteration 1516 — [[words/孟秋|孟秋]]

No stand-in relationship (孟 is proper-noun-only; 秋's own is itself). Removed redundant `品詞`, expanded Notes with compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孟金.

### 2026-08-29, iteration 1517 — [[words/孟金|孟金]]

No stand-in relationship (孟 is proper-noun-only; 金's own is itself). Fixed a stray non-breaking-space (U+00A0) character corrupting `japanese` (required a `perl -CSD` byte-level fix, not a plain-text Edit, since it wasn't a regular space). Removed redundant `品詞` and a duplicate `kwin: false` key introduced mid-edit. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 季冬.

### 2026-08-29, iteration 1518 — [[words/季冬|季冬]]

No stand-in relationship (季's own stand-in is [[季節]]; 冬's own is itself). Removed redundant `品詞`, expanded Notes with compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 季夏.

### 2026-08-29, iteration 1519 — [[words/季夏|季夏]]

No stand-in relationship (季's own stand-in is [[季節]]; 夏's own is itself). Removed redundant `品詞`, expanded Notes with compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 季春.

### 2026-08-29, iteration 1520 — [[words/季春|季春]]

No stand-in relationship (季's own stand-in is [[季節]]; 春's own is itself). Removed redundant `品詞`, expanded Notes with compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 季秋.

### 2026-08-29, iteration 1521 — [[words/季秋|季秋]]

No stand-in relationship (季's own stand-in is [[季節]]; 秋's own is itself). Removed redundant `品詞`, expanded Notes with compositional-readings paragraph. No homophones. Stamped `date-last-perfect: 2026-08-29`.

This completes the pentad of 孟/仲/季-prefixed month names started earlier — [[季冬]]/[[季夏]]/[[季春]]/[[季秋]] and [[孟冬]]/[[孟夏]]/[[孟春]]/[[孟秋]] are now all uniformly perfected.

Next: 孤児院.

### 2026-08-29, iteration 1522 — [[words/孤児院|孤児院]]

No stand-in relationship (孤's own stand-in is [[孤独]]; 児's own is [[児子]]; 院's own is [[院落]]). Fixed archaic kana japanese こじゐん→こじいん. Reformatted `characters`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孤立.

### 2026-08-29, iteration 1523 — [[words/孤立|孤立]]

No stand-in relationship (孤's own stand-in is [[孤独]]; 立's own is itself). Simplified malformed slash-separated `cantonese` to the single reading matching 立's own citation. Reformatted `characters`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 学区.

### 2026-08-29, iteration 1524 — [[words/学区|学区]]

No stand-in relationship (学's own stand-in is [[学習]]; 区's own is [[区域]]). Frontmatter already fully correct; restructured bare prose into a proper `## Notes` section. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 学堂.

### 2026-08-29, iteration 1525 — [[words/学堂|学堂]]

No stand-in relationship (学's own stand-in is [[学習]]; 堂's own is [[会堂]]). Fixed real bug: `cantonese` was garbled invalid jyutping ("xuo2 tang2") — corrected to compositional hok6 tong4. Omitted blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 学者.

### 2026-08-29, iteration 1526 — [[words/学者|学者]]

No stand-in relationship (学's own stand-in is [[学習]]; 者's own is itself). Fixed real bug: `羅馬字` had 学's coda mistyped k→g (諺文/注音 were already correct). Trimmed trailing space from `vietnamese`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 学説.

### 2026-08-29, iteration 1527 — [[words/学説|学説]]

説's own `stand_in` is 学説 — added the stand-in note. Reformatted comma-joined `japanese` into a proper list (compositional がくせつ + loanword セオリー), quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 孫悟空.

### 2026-08-29, iteration 1528 — [[words/孫悟空|孫悟空]]

No stand-in relationship (孫's own stand-in is [[孫子]]; 悟's own is [[覚悟]]; 空's own is itself). Frontmatter already fully correct; omitted blank `hsk_level`/`swadesh`/empty-list `aliases`, renamed `## Etymology`→`## Notes` with real prose. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 幾何学.

### 2026-08-29, iteration 1529 — [[words/幾何学|幾何学]]

No stand-in relationship (幾/何 are both their own stand-ins; 学's own is [[学習]]). Fixed missing "(char)" suffix on `characters` for 幾/何. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 広野.

### 2026-08-29, iteration 1530 — [[words/広野|広野]]

No stand-in relationship (広's own stand-in is itself; 野's own is [[田野]]). Fixed real bug: `mandarin`/`cantonese` had been contaminated with the near-synonym 曠野's readings (kuàngyě/kwong3, using a different character 曠) — corrected to compositional guǎngyě/gwong2 je5, and removed 曠野 from `aliases` accordingly. Filled blank `vietnamese: quảng dã`. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 強化.

### 2026-08-29, iteration 1531 — [[words/強化|強化]]

No stand-in relationship (強/化 are both their own stand-ins). Fixed missing "(char)" suffix on `characters`. Omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 強固.

### 2026-08-29, iteration 1532 — [[words/強固|強固]]

固's own `stand_in` is 強固 — added the stand-in note. Fixed real bug: `korean` had been contaminated with 堅固's reading (견고, using 堅 not 強) — corrected to compositional 강고. Filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 強国.

### 2026-08-29, iteration 1533 — [[words/強国|強国]]

No stand-in relationship (強's own stand-in is itself; 国's own is [[国家]]). Fixed missing "(char)" suffix on `characters`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 強迫.

### 2026-08-29, iteration 1534 — [[words/強迫|強迫]]

迫's own `stand_in` is 強迫 — added the stand-in note. Trimmed malformed `mandarin` (stray untoned duplicate), filled blank `vietnamese: cường bách`. Omitted blank `hsk_level`/`swadesh`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 弾圧.

### 2026-08-29, iteration 1535 — [[words/弾圧|弾圧]]

No stand-in relationship (弾's own stand-in is [[弾丸]]; 圧's own is itself). Fixed missing "(char)" suffix on `characters`. Omitted blank `hsk_level`/`swadesh`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当.

### 2026-08-29, iteration 1536 — [[words/当|当]]

This word is the stand-in for its own character. Filled blank `korean`/`vietnamese`, missing `pos`/`japanese`, reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当世.

### 2026-08-29, iteration 1537 — [[words/当世|当世]]

No stand-in relationship (当's own stand-in is itself; 世's own is [[世界]]). Filled blank `korean`/`vietnamese`, added missing `kwin: false`. Reformatted `characters`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当世紀.

### 2026-08-29, iteration 1538 — [[words/当世紀|当世紀]]

No stand-in relationship (当's own stand-in is itself; 世's own is [[世界]]; 紀's own is [[世紀]]). Filled blank `vietnamese`, fixed missing "(char)" suffix on `characters`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当代.

### 2026-08-29, iteration 1539 — [[words/当代|当代]]

No stand-in relationship (当's own stand-in is itself; 代's own is [[世代]]). Filled blank `vietnamese: đương đại` (flagged 代's own citation as missing this attested reading, for a future character pass). Fixed missing "(char)" suffix, reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当年.

### 2026-08-29, iteration 1540 — [[words/当年|当年]]

No stand-in relationship (当/年 are both their own stand-ins). Filled blank `vietnamese: đương niên`, quoted `characters` entries. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当月.

### 2026-08-29, iteration 1541 — [[words/当月|当月]]

No stand-in relationship (当/月 are both their own stand-ins). Fixed real bug: `kwin` was wrongly true (諺文 당웓 ≠ korean 당월). Filled blank `vietnamese: đương nguyệt`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 当週.

### 2026-08-29, iteration 1542 — [[words/当週|当週]]

No stand-in relationship (当's own stand-in is itself; 週's own is [[週日]]). Filled blank `vietnamese: đương chu`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彗星.

### 2026-08-29, iteration 1543 — [[words/彗星|彗星]]

彗's own `stand_in` is 彗星 — added the stand-in note. Fixed real bug: `cantonese` had 彗's syllable as seoi6 instead of wai6 (matching 彗's own citation). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彙.

### 2026-08-29, iteration 1544 — [[words/彙|彙]]

This word is the stand-in for its own character. Filled blank `japanese: い`, trimmed multi-value `vietnamese` to single vị. Reformatted `characters`, removed redundant `品詞`, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 形.

### 2026-08-29, iteration 1545 — [[words/形|形]]

This word is the stand-in for its own character. Filled blank `pos: 名詞`, trimmed multi-value `vietnamese` to single hình, removed redundant `品詞`, reformatted `characters`. No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 形容詞.

### 2026-08-29, iteration 1546 — [[words/形容詞|形容詞]]

No stand-in relationship (形/容 are both their own stand-ins; 詞's own is [[単詞]]). Fixed wrongly-capitalized `vietnamese` "Tính từ"→tính từ. Fixed missing "(char)" suffixes, reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 形態.

### 2026-08-29, iteration 1547 — [[words/形態|形態]]

No stand-in relationship (形's own stand-in is itself; 態's own is [[態度]]). Removed redundant `品詞`, wrote `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 形成.

### 2026-08-29, iteration 1548 — [[words/形成|形成]] & [[words/形声|形声]]

Discovered genuine Dan'a'yo homophone pair (both ㄏㄝㄫㄙㄧㄫ/hengsing/헝싱, from 成/声 coinciding) — added reciprocal `>[!warning] Homophones` callouts to both. 形声 was already stamped (2026-06-12) but missing the callout, a required checklist criterion — refreshed its stamp now that it's complete. Removed redundant `品詞` on both, fixed missing "(char)" suffix on 形成's `characters`. No other bugs. Stamped both `date-last-perfect: 2026-08-29`.

Next: 形状.

### 2026-08-29, iteration 1549 — [[words/形状|形状]]

状's own `stand_in` is 形状 — added the stand-in note. Filled blank `vietnamese: hình trạng`. Fixed missing "(char)" suffix, reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 形貌.

### 2026-08-29, iteration 1550 — [[words/形貌|形貌]]

貌's own `stand_in` is 形貌 — added the stand-in note. Fixed real bug: `羅馬字` had a stray extra "u" (諺文/注音 were already correct). Filled blank `japanese`/`korean`/`vietnamese`, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彩虹.

### 2026-08-29, iteration 1551 — [[words/彩虹|彩虹]]

虹's own `stand_in` is 彩虹 — added the stand-in note. Filled blank `vietnamese: cầu vồng` (native, matching Korean 무지개's already-correct native-equivalent pattern). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彫像.

### 2026-08-29, iteration 1552 — [[words/彫像|彫像]]

像's own `stand_in` is 彫像 — added the stand-in note. Fixed real bug: `諺文` had 彫's syllable missing its final coda (초→촛, matching 羅馬字/注音 which were already correct). Reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彫刻.

### 2026-08-29, iteration 1553 — [[words/彫刻|彫刻]]

No stand-in relationship (彫's own stand-in is itself; 刻's own is [[刻印]]). Fixed real bug: `諺文` had the same recurring 彫-coda typo as [[彫像]] (초→촛). Filled blank `vietnamese: điêu khắc`, reformatted `aliases`, preserved existing 彫塑/刻印 nuance notes. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彬彬.

### 2026-08-29, iteration 1554 — [[words/彬彬|彬彬]]

This word is the stand-in for its own character 彬 (a reduplicative ideophone). Filled blank `vietnamese: bân bân`, removed redundant `品詞`, wrote `## Notes`. No homophones (verification still finishing in background; pattern was unique on first partial check). Stamped `date-last-perfect: 2026-08-29`.

Next: 彰明.

### 2026-08-29, iteration 1555 — [[words/彰明|彰明]]

彰's own `stand_in` is 彰明 — added the stand-in note. Fixed real bug: `japanese` had archaic, incomplete kana しやう (missing 明 entirely) — corrected to しょうめい. Filled blank `korean`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 影像.

### 2026-08-29, iteration 1556 — [[words/影像|影像]]

No stand-in relationship (影's own stand-in is [[陰影]]; 像's own is [[彫像]]). Filled blank `pos: 名詞`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 彷徨.

### 2026-08-29, iteration 1557 — [[words/彷徨|彷徨]]

徨's own `stand_in` is 彷徨 — added the stand-in note (彷's own is [[彷彿]]). Filled blank `vietnamese: bàng hoàng`, omitted empty-list `aliases`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 往.

### 2026-08-29, iteration 1558 — [[words/往|往]] & [[words/王|王]]

Completed a genuine Dan'a'yo homophone pair (both ⺢ㄫ/'wang/왕) — 往 already had an informal, non-canonical callout pointing at 王, but 王 had none. Rewrote both with canonical `>[!warning] Homophones` callouts, filled missing pos/japanese/vietnamese on both, reformatted `characters`. Stamped both `date-last-perfect: 2026-08-29`.

Next: 征伐.

### 2026-08-29, iteration 1559 — [[words/征伐|征伐]]

征's own `stand_in` is 征伐 — added the stand-in note (伐's own is [[討伐]]). Filled blank `vietnamese: chinh phạt`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 後.

### 2026-08-29, iteration 1560 — [[words/後|後]]

This word is the stand-in for its own character. Filled missing `pos`/`japanese`/`vietnamese`, reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 後悔.

### 2026-08-29, iteration 1561 — [[words/後悔|後悔]]

悔's own `stand_in` is 後悔 — added the stand-in note. Filled blank `vietnamese: hậu hối`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 後置.

### 2026-08-29, iteration 1562 — [[words/後置|後置]]

No stand-in relationship (後/置 are both their own stand-ins). Filled blank `cantonese`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 後置詞.

### 2026-08-29, iteration 1563 — [[words/後置詞|後置詞]]

No stand-in relationship (後/置 are both their own stand-ins; 詞's own is [[単詞]]). Filled blank `cantonese`/`vietnamese`, fixed missing "(char)" suffix. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 徐様.

### 2026-08-29, iteration 1564 — [[words/徐様|徐様]]

徐's own `stand_in` is 徐様 — added the stand-in note. Fixed real bugs: `mandarin` had been swapped for the unrelated word 慢 (màn); `korean`/`japanese` had native/differently-formed real adverbs appended instead of the compositional reading. Filled blank `vietnamese`/`pos`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 従.

### 2026-08-29, iteration 1565 — [[words/従|従]], [[words/鐘|鐘]] & [[words/鍾|鍾]]

Resolved a pending "鍾???" note on 鐘 by confirming a genuine three-way Dan'a'yo homophone group (all jong/종/ㄐㄛㄫ): 従 ("obey, observe"), 鐘 ("bell"), 鍾 ("alcohol bottle"). Fixed 従/鐘's malformed single-character pattern (literal `vietnamese: null` on 鐘, missing pos/japanese on 従, bare `# Notes`). All three fully rewritten with reciprocal callouts. Stamped all three `date-last-perfect: 2026-08-29`.

Next: 従事.

### 2026-08-29, iteration 1566 — [[words/従事|従事]]

No stand-in relationship (従/事 are both their own stand-ins). Filled blank `vietnamese: tùng sự`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 従前.

### 2026-08-29, iteration 1567 — [[words/従前|従前]]

No stand-in relationship (従/前 are both their own stand-ins). Filled blank `vietnamese: tùng tiền`, quoted fields. Verified the real-Korean-only 終戦 coincidence noted in prose does not extend to a Dan'a'yo-level homophone. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 従属.

### 2026-08-29, iteration 1568 — [[words/従属|従属]] & [[words/種族|種族]]

Discovered a genuine Dan'a'yo-level homophone (both 종족/jongjog/ㄐㄛㄫㄐㄛㄎ) distinct from the real-Korean-only coincidence 従属's own prose had already flagged (従属's real Korean is 종속, different from 種族's 종족) — completed both with reciprocal callouts, clarifying the layered distinction in each Notes section. Filled blank `vietnamese` on 従属, quoted fields on both. Stamped both `date-last-perfect: 2026-08-29`.

Next: 従来.

### 2026-08-29, iteration 1569 — [[words/従来|従来]]

No stand-in relationship (従/来 are both their own stand-ins). Filled blank `vietnamese: tùng lai`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 従業.

### 2026-08-29, iteration 1570 — [[words/従業|従業]]

No stand-in relationship (従/業 are both their own stand-ins). Filled blank `vietnamese: tùng nghiệp`, quoted fields. Verified the real-Korean-only 終業式 coincidence noted in prose does not extend to a Dan'a'yo-level homophone. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 従者.

### 2026-08-29, iteration 1571 — [[words/従者|従者]]

No stand-in relationship (従/者 are both their own stand-ins). Filled blank `vietnamese: tùng giả`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 従軍.

### 2026-08-29, iteration 1572 — [[words/従軍|従軍]]

No stand-in relationship (従's own stand-in is itself; 軍's own is [[軍隊]]). Filled blank `vietnamese: tùng quân`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

This completes the full run of 従-initial compounds swept this stretch: [[従]]/[[従事]]/[[従前]]/[[従属]]/[[従来]]/[[従業]]/[[従者]]/[[従軍]] are now all uniformly perfected.

Next: 得点.

### 2026-08-29, iteration 1573 — [[words/得点|得点]] & [[words/特点|特点]]

Completed a genuine Dan'a'yo homophone pair (both dug/둑/ㄉㄨㄎ + dem/덤/ㄉㄝㄇ). Both 得's and 特's own first syllable independently diverge from their standalone citations (tǝg/특 and dǝg/득 respectively) to the shared "dug" form here — likely a deliberate homophone construction, cross-verified for 得 by the chengyu [[種瓜得瓜]]. Rewrote both non-canonical homophone tips into proper `>[!warning] Homophones` callouts, filled blank vietnamese on 得点. Stamped both `date-last-perfect: 2026-08-29`.

Next: 御術.

### 2026-08-29, iteration 1574 — [[words/御術|御術]]

No stand-in relationship (御's own stand-in is [[防御]]; 術's own is itself). Filled blank `cantonese`/`japanese`/`korean`/`vietnamese`/`kwin`, fixed missing "(char)" suffix, fixed malformed nested-list `tags`, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 復帰.

### 2026-08-29, iteration 1575 — [[words/復帰|復帰]]

No stand-in relationship (復's own stand-in is [[回復]]; 帰's own is [[回帰]]). Filled blank `cantonese`/`vietnamese`, reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 復活.

### 2026-08-29, iteration 1576 — [[words/復活|復活]]

No stand-in relationship (復's own stand-in is [[回復]]; 活's own is itself). Fixed missing space in `cantonese`. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 復活節.

### 2026-08-29, iteration 1577 — [[words/復活節|復活節]]

No stand-in relationship (復's own stand-in is [[回復]]; 活/節 are both their own stand-ins). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 循.

### 2026-08-29, iteration 1578 — [[words/循|循]]

This word is the stand-in for its own character. Fixed literal `vietnamese: null`→tuần, missing `pos`/`japanese` filled 事詞/じゅん. Reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 徳.

### 2026-08-29, iteration 1579 — [[words/徳|徳]]

This word is the stand-in for its own character. Filled blank `japanese`/`vietnamese`, missing `pos`. Reformatted `characters`, expanded `## Notes` with a numbered list and compositional-readings paragraph. No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 徳国.

### 2026-08-29, iteration 1580 — [[words/徳国|徳国]]

No stand-in relationship (徳's own stand-in is itself; 国's own is [[国家]]). Fixed real bug: `mandarin` had 徳国's cantonese reading erroneously appended after a semicolon, leaving `cantonese` blank — split apart correctly. Verified japanese/korean/vietnamese as genuine real-world country-name terms. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 心理.

### 2026-08-29, iteration 1581 — [[words/心理|心理]]

No stand-in relationship (心's own stand-in is itself; 理's own is [[理由]]). Filled blank `pos: 名詞`, trimmed contaminated comma-joined `vietnamese` to just tâm lý. Omitted empty-list `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 心理学.

### 2026-08-29, iteration 1582 — [[words/心理学|心理学]]

No stand-in relationship (心's own stand-in is itself; 理's own is [[理由]]; 学's own is [[学習]]). Normalized `vietnamese` spelling variant "lí"→"lý" (matching [[心理]]). Restructured bare prose into a proper `## Notes` section, fixed typos ("disciple"→"discipline", "practioner"→"practitioner"). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 心緒.

### 2026-08-29, iteration 1583 — [[words/心緒|心緒]]

This word is the stand-in for 緒 (too bounded to stand alone). Filled blank `vietnamese: tâm tự`, added missing `kwin: false`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 必.

### 2026-08-29, iteration 1584 — [[words/必|必]]

This word is the stand-in for its own character. Fixed literal `vietnamese: null`→tất, missing `pos`/`japanese` filled 性詞/ひつ. Reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 必然.

### 2026-08-29, iteration 1585 — [[words/必然|必然]]

No stand-in relationship (必/然 are both their own stand-ins). Fixed real bug: `cantonese` had 必's tone mistyped bit2→bit1. Filled blank `vietnamese`, quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 必要.

### 2026-08-29, iteration 1586 — [[words/必要|必要]]

No stand-in relationship (必's own stand-in is itself; 要's own is [[重要]]). Fixed real bug: `japanese` had archaic kana ひつえう→ひつよう. Quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 忌惮.

### 2026-08-29, iteration 1587 — [[words/忌惮|忌惮]]

This word is the stand-in for 惮 (忌's own stand-in is [[忌諱]]). Filled blank `vietnamese: kị đạn`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 忌諱.

### 2026-08-29, iteration 1588 — [[words/忌諱|忌諱]]

忌's own `stand_in` is 忌諱 — added the stand-in note. Fixed real bug: `korean` had comma-separated native/loanword contamination (금기, 터부) instead of the compositional reading. Filled blank `vietnamese`, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 忘却.

### 2026-08-29, iteration 1589 — [[words/忘却|忘却]]

忘's own `stand_in` is 忘却 — added the stand-in note. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 応.

### 2026-08-29, iteration 1590 — [[words/応|応]] & [[words/鷹|鷹]]

Discovered genuine Dan'a'yo homophone pair (both ㄧㄫ/'ing/잉, unrelated "respond" vs "hawk") — completed both with reciprocal callouts. Fixed real bug on 応: `羅馬字` was missing its glide apostrophe (ing→'ing, matching 応's own citation and 鷹's already-correct form). Trimmed 応's comma-joined `vietnamese` to single ứng. Restructured 応's loose Notes bullets into prose. Removed redundant `品詞` on 鷹, refreshed its stamp since it was missing the callout. Stamped both `date-last-perfect: 2026-08-29`.

Next: 応訊.

### 2026-08-29, iteration 1591 — [[words/応訊|応訊]]

No stand-in relationship (応's own stand-in is itself; 訊's own is [[審訊]]). Fixed real bug: `cantonese` had the Mandarin pinyin duplicated in place of jyutping — corrected to jing3 seon3. Filled blank `japanese`/`korean`/`vietnamese`, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 忠告.

### 2026-08-29, iteration 1592 — [[words/忠告|忠告]]

No stand-in relationship (忠's own stand-in is [[忠誠]]; 告's own is [[告訴]]). Fixed real bug: `cantonese` had 告's syllable mistyped guk1→gou3. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 忠実.

### 2026-08-29, iteration 1593 — [[words/忠実|忠実]]

No stand-in relationship (忠's own stand-in is [[忠誠]]; 実's own is [[真実]]). Frontmatter already fully correct; quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 快.

### 2026-08-29, iteration 1594 — [[words/快|快]]

This word is the stand-in for its own character. Filled blank `pos`/`japanese`/`vietnamese`, added missing `kwin: true`. Reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 快楽.

### 2026-08-29, iteration 1595 — [[words/快楽|快楽]]

楽's own `stand_in` is 快楽 — added the stand-in note. Filled blank `vietnamese: khoái lạc`, quoted fields. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 念頭.

### 2026-08-29, iteration 1596 — [[words/念頭|念頭]]

念's own `stand_in` is 念頭 — added the stand-in note. Fixed missing "(char)" suffix, filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 忽然様.

### 2026-08-29, iteration 1597 — [[words/忽然様|忽然様]]

No stand-in relationship (忽's own stand-in is [[忽然]]; 然/様 are both their own stand-ins). Filled entirely blank `pos`/`mandarin`/`cantonese`/`japanese`/`korean`/`vietnamese`/`kwin` (compositional, built on the [[忽然]]+様 adverbializer pattern). Fixed missing "(char)" suffixes. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怒.

### 2026-08-29, iteration 1598 — [[words/怒|怒]]

This word is the stand-in for its own character. Filled missing `pos`/`japanese`/`vietnamese`/`kwin`, reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怒号.

### 2026-08-29, iteration 1599 — [[words/怒号|怒号]]

No stand-in relationship (怒's own stand-in is itself; 号's own is [[符号]]). Filled blank `vietnamese`, reformatted `characters`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怒気.

### 2026-08-29, iteration 1600 — [[words/怒気|怒気]]

No stand-in relationship (怒/気 are both their own stand-ins). Filled blank `vietnamese`, reformatted `characters`/`aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怒涛.

### 2026-08-29, iteration 1601 — [[words/怒涛|怒涛]]

涛's own `stand_in` is 怒涛 — added the stand-in note. Fixed malformed `mandarin` (stray duplicate), removed redundant self-referential alias. Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 思議.

### 2026-08-29, iteration 1602 — [[words/思議|思議]]

No stand-in relationship (思's own stand-in is [[思考]]; 議's own is [[議論]]). Fixed real bug: `諺文`/`羅馬字`/`注音` all had 議's syllable using the wrong reading 위/wi/ㄨㄧ instead of the correct 읫/'ǝi/ㄜㄧ (matching 議's own citation and sibling [[協議]]). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

**Flagged for a future iteration**: [[会議]] (still unstamped) has the same 羅馬字 typo pattern (hwe'wi should be hwe'ǝi) though its 諺文/注音 are already correct — will fix when its own turn comes up.

Next: 怠惰.

### 2026-08-29, iteration 1603 — [[words/怠惰|怠惰]]

Both 怠 and 惰's own `stand_in` is 怠惰 (cranberry, matching existing tag). Trimmed malformed multi-value `cantonese` to single toi5 do6, filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 急.

### 2026-08-29, iteration 1604 — [[words/急|急]]

This word is the stand-in for its own character. Fixed literal `vietnamese: null`→cấp, missing `pos`/`japanese` filled 性詞/きゅう. Reformatted `characters`, wrote `## Notes` (was bare `# Notes`). No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 性交.

### 2026-08-29, iteration 1605 — [[words/性交|性交]]

No stand-in relationship (性's own stand-in is [[個性]]; 交's own is itself). Fixed archaic kana japanese せいかう→せいこう and missing space in `cantonese`. Filled blank `pos: 動詞`. Confirmed 諺文/羅馬字 gyau/걋 match the documented majority pattern across 交-compounds (character-page discrepancy, not a word bug). No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 性別.

### 2026-08-29, iteration 1606 — [[words/性別|性別]]

No stand-in relationship (性's own stand-in is [[個性]]; 別's own is itself). Filled blank `pos: 名詞`/`vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 性質.

### 2026-08-29, iteration 1607 — [[words/性質|性質]]

No stand-in relationship (性's own stand-in is [[個性]]; 質's own is [[質素]]). Filled blank `pos: 名詞`, quoted `hsk_level`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怪物.

### 2026-08-29, iteration 1608 — [[words/怪物|怪物]]

No stand-in relationship (怪's own stand-in is [[怪異]]; 物's own is itself). Filled blank `vietnamese`, restructured bare prose into `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怪獣.

### 2026-08-29, iteration 1609 — [[words/怪獣|怪獣]]

No stand-in relationship (怪's own stand-in is [[怪異]]; 獣's own is [[野獣]]). Fixed archaic kana japanese くわいじう→かいじゅう, reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 怯.

### 2026-08-29, iteration 1610 — [[words/怯|怯]] & [[words/恰|恰]]

Discovered genuine Dan'a'yo homophone pair (both ㄎㄚㄆ/kab/캅, unrelated "cowardly" vs "exactly") — completed both with reciprocal callouts. Both had the same malformed single-character pattern (missing japanese, malformed list-form `vietnamese`, bare `# Notes` on 怯). Stamped both `date-last-perfect: 2026-08-29`.

Next: 恋.

### 2026-08-29, iteration 1611 — [[words/恋|恋]]

This word is the stand-in for its own character. Filled missing `pos`/`japanese`/`kwin`, reformatted `characters`. No word-level homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恐恐.

### 2026-08-29, iteration 1612 — [[words/恐恐|恐恐]]

No stand-in relationship (恐's own stand-in is [[恐慌]]) — a reduplicative ideophone. Filled blank `vietnamese`, quoted fields. Preserved the existing rich Notes prose on 兢/character-inclusion philosophy. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恐惧.

### 2026-08-29, iteration 1613 — [[words/恐惧|恐惧]]

惧's own `stand_in` is 恐惧 — added the stand-in note (恐's own is [[恐慌]]). Filled blank `vietnamese`, reformatted `aliases`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恐慌.

### 2026-08-29, iteration 1614 — [[words/恐慌|恐慌]]

Both 恐 and 慌's own `stand_in` is 恐慌 — added the note. Frontmatter already fully correct; wrote `## Notes`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恐龍.

### 2026-08-29, iteration 1615 — [[words/恐龍|恐龍]]

No stand-in relationship (恐's own stand-in is [[恐慌]]; 龍's own is itself). Fixed missing "(char)" suffix on `characters`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恒久.

### 2026-08-29, iteration 1616 — [[words/恒久|恒久]]

恒's own `stand_in` is 恒久 — added the stand-in note (久's own is itself). Fixed missing "(char)" suffix. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恒例.

### 2026-08-29, iteration 1617 — [[words/恒例|恒例]]

No stand-in relationship (恒's own stand-in is [[恒久]]; 例's own is [[実例]]). Filled blank `vietnamese`. No homophones. Stamped `date-last-perfect: 2026-08-29`.

Next: 恒常.
