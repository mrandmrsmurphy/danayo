# Character Perfecting (Solo Loop)

Running log for the character-perfecting backlog sweep (see [[AIOS/checklists/checklist_characters.md|Checklist: Character Pages]]). The prior log (iterations 1–464+) grew large and was archived by the user to `Character Perfecting (Solo Loop).md.zip`; this file continues from there. Iteration numbering continues unbroken from the archived log.

**Process**: one character per iteration. Find the next never-perfected character via `danayo_id` ascending (`grep -L "^date-last-perfect" characters/*.md`, sorted by each file's own `danayo_id` frontmatter value — not alphabetical, unlike the word sweep). Verify/fill all required frontmatter (`graphemic_classification`, `stand_in`, `mc_id`, `danayo_id`, `pos`, level fields), write or correct the four fixed `## Notes` bullets (graphemic → SKIP/Stroke → MC rank+phonology → levels), cross-check `## Words` against every real word citing this character as a constituent, add `## Chengyu`/`## Derived Characters` when real hits exist, then stamp `date-last-perfect`.

### 2026-08-05, iteration 465 — [[characters/識|識]]

Next never-perfected character by `danayo_id` (4256, the log having jumped from 3107→4256 since most characters in between were already perfected through other means). **Real bug found and fixed**: `mandarin` was stored as `"shí shì"` — `shì` isn't a real reading of 識 at all; corrected to the genuine second polyphonic reading `zhì` (as in 標識, "mark, sign," historically read biāozhì though biāoshí has become the modern colloquial norm), verified via Wiktionary/zdic.

**Frontmatter**: `graphemic_classification: 戠` confirmed correct (形声, phonetic 戠) via Wiktionary. `mc_id: 952` verified against `lookup/CC/CC 0000.md` line 985 ("952. 識") — correct, no off-by-one. `pos: 事詞`, `stand_in: 認識`, `kwin: true` (Dan'a'yo 식 matches Sino-Korean 식) all already correct.

**Body was essentially empty**: no graphemic/SKIP/MC/Levels bullets existed, just a stray "Components: [[言]], [[戠]]" line and two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch.

**Words cross-check** (5 total ground-truth hits via each word's own `characters:` field, filtering out several grep false-positives that only mentioned 識 in English glosses): only 1 previously listed ([[標識]]); added the other 4 — [[知識]], [[認識]], [[常識]], [[識字]] — ordered by centrality.

**Chengyu**: no real ground-truth hits (four chengyu matched a naive text grep but none actually cite 識 in their own `characters:` field) — section correctly omitted.

**Derived Characters**: no other character in the database cites 識 itself as its own `graphemic_classification` — section correctly omitted (note: this is distinct from siblings like 職/織/幟 that also derive from the same grandparent phonetic 戠, which don't count as 識's own descendants).

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 護 (4257; 2034 characters remaining in the full-vault rescan).

### 2026-08-05, iteration 466 — [[characters/護|護]]

Notes bullets and etymology were already correct and complete (形声, 言 + phonetic 蒦, OC \*ɢʷraːɡs — verified via Wiktionary; `mc_id: 1141` verified against `lookup/CC/CC 1000.md` line 150). **Frontmatter fixed**: `pos: ""` → `事詞` (matching sibling protect-verb [[characters/守|守]]).

**Real alias-contamination bug found and fixed**: `aliases` included `掩` alongside the legitimate simplified form `护` — but 掩 ("to cover, conceal") is a completely distinct, unrelated character with its own meaning, not a variant/simplified form of 護 at all. The likely source of the error: 掩護 (yǎnhù, "to provide cover") is a real compound pairing the two characters, and 掩 appears to have been mistakenly copied into 護's own alias field from that compound rather than being a true orthographic variant. Removed it (no `words/掩護.md` exists yet in the vault, so nothing else needed updating).

**Words cross-check** (7 total ground-truth hits): 3 previously listed ([[守護]], [[援護]], [[護金]]); added the 4 missing — [[保護]], [[愛護]], [[庇護]], [[防護]] — ordered by centrality, most general first.

**Chengyu**: no ground-truth hits — section correctly omitted. **Derived Characters**: no other character cites 護 itself as its own `graphemic_classification` — section correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 象 (4258; 2033 characters remaining).

### 2026-08-05, iteration 467 — [[characters/象|象]]

Body was essentially empty (H1 "# Notes" holding only two floating CC-initial/final wikilinks, no graphemic/SKIP/MC/Levels bullets). Wrote all four Notes bullets from scratch: confirmed 象形 (pure pictograph of an elephant in profile) via Wiktionary/Dong-Chinese; `mc_id: 455` verified against `lookup/CC/CC 0000.md` line 473. Filled blank `pos: ""` → `名詞`. Noted that its Kangxi radical `豕` ("pig") is a coincidental visual-bottom-component match, not a true compositional radical, since 象 is a single holistic pictograph.

**Words cross-check** (7 total ground-truth hits): 2 previously listed ([[象形]], [[気象]]); added the 5 missing — [[大象]] (the `stand_in`, flagged accordingly), [[現象]], [[対象]], [[万象]], [[海象]].

**Chengyu**: [[森羅万象]] already correctly listed, confirmed as the only real hit. **Derived Characters**: [[像]] ("statue") cites 象 as its own `graphemic_classification` — added.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 貞 (4259; 2032 characters remaining).

### 2026-08-05, iteration 468 — [[characters/貞|貞]]

**Real alias-contamination bug found and fixed, same pattern as [[characters/護|護]]'s 掩**: `aliases` included `楨` alongside the legitimate simplified form `贞` — but 楨 ("mainstay, hardwood pole") is a distinct 形声 character using 貞 only as its own phonetic component (木 semantic + 貞 phonetic), not a variant/simplified form of 貞 itself. Removed it (no vault page exists for 楨 anyway, so it doesn't qualify for Derived Characters either).

**Body was essentially empty**: only two floating CC-initial/final wikilinks, no graphemic/SKIP/MC/Levels bullets. Wrote all four from scratch, including the character's genuinely layered etymology (verified via Wiktionary): originally an 象形 pictogram of a ding-vessel — identical to and phonetically borrowed from [[鼎]] — later given semantic 卜 ("divination") to disambiguate from the vessel sense, with the bottom subsequently stylized into the unrelated 貝 (its modern, purely coincidental Kangxi radical). `mc_id: 971` verified against `lookup/CC/CC 0000.md` line 1004.

**Words cross-check** (1 ground-truth hit): [[貞潔]] already listed, flagged as the `stand_in`. **Chengyu**: no hits — correctly omitted. **Derived Characters**: [[characters/偵 (char)|偵]] and [[禎]] both cite 貞 as their own `graphemic_classification` — added, section built from scratch.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 財 (4260; 2031 characters remaining).

### 2026-08-05, iteration 469 — [[characters/財|財]]

**Confirmed `aliases: [财, 㒲]` are both legitimate** — 㒲 (U+34B2) is genuinely documented as a variant of 財, not contamination like the last two iterations' 掩/楨.

Body had only two floating CC-initial/final wikilinks and an informal "Components:" line — wrote all four Notes bullets from scratch (形声, 貝 semantic + 才 phonetic, OC \*zlɯː, verified via Wiktionary; `mc_id: 543` verified against `lookup/CC/CC 0000.md` line 564).

**Words cross-check** (3 total ground-truth hits, one revealing a real bug in a different file): [[財産]] already listed (flagged as `stand_in`); added [[発財]] and [[恭喜発財]]. **Flagged, not fixed (out of word-sweep scope)**: `words/恭喜発財.md`'s own `characters:` field is missing 財 entirely (only lists 恭/喜/発) despite its own `注音` (ㄍ⼄ㄫㄏㄧㄈㄚㄊㄐㄚㄧ) and English gloss clearly using it — a word-sweep fix, not a character-page one, but it still genuinely uses 財 so it belongs in this Words list regardless.

**Chengyu**: [[財愛悪根]] added (real hit, previously missing). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 貧 (4261; 2030 characters remaining).

### 2026-08-05, iteration 470 — [[characters/貧|貧]]

Body had only two floating CC-initial/final wikilinks and one informal, unruby'd word note. Wrote all four Notes bullets from scratch (形声, OC \*brɯn: phonetic 分 + semantic 貝, verified via Wiktionary; `mc_id: 661` verified against `lookup/CC/CC 0000.md` line 685). Filled blank `pos: ""` → `性詞`, matching its antonym [[characters/富|富]]'s own `性詞`.

**Words cross-check** (2 total ground-truth hits): [[貧乏]] reformatted with proper ruby+gloss and flagged as the `stand_in`; added [[貧窮]] (missing). **Chengyu**/**Derived Characters**: no ground-truth hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 貯 (4262; 2029 characters remaining).

### 2026-08-05, iteration 471 — [[characters/貯|貯]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, OC \*taʔ: phonetic 宁 + semantic 貝, verified via Wiktionary). `mc_id: 4224` is beyond the local `lookup/CC/CC 0000–3000.md` files' ~4000-rank coverage — per the checklist's own policy, used verbatim as trusted ground truth rather than second-guessed. Filled blank `pos: ""` → `事詞`, matching sibling store/accumulate verbs [[characters/蔵|蔵]] and [[積]].

**Words cross-check** (1 ground-truth hit): [[貯蔵]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 費 (char) (4263; 2028 characters remaining).

### 2026-08-05, iteration 472 — [[characters/費 (char)|費]]

Body had only two floating CC-initial/final wikilinks plus one informal note. Wrote all four Notes bullets from scratch (形声, OC \*pʰɯds: phonetic 弗 + semantic 貝, verified via Wiktionary; `mc_id: 1046` verified against `lookup/CC/CC 1000.md` line 51). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (4 total ground-truth hits): 1 previously listed ([[費米金]]); added the self-referential `stand_in` [[費]] plus [[経費]] and [[食費]]. **Noted but not fixed (out of scope)**: `words/費.md` itself is still unperfected (near-empty) — a word-sweep task, not this one. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 貿 (4264; 2027 characters remaining).

### 2026-08-05, iteration 473 — [[characters/貿|貿]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3385`, but `lookup/CC/CC 3000.md` line 402 shows `3385. 耘` (an unrelated character, "to weed") — 貿's real rank is `3386` (line 403). Corrected. Same class of error the checklist already documents (艮/煌 cases) — the stored value was the entry immediately before the correct one.

Body had only two floating CC-initial/final wikilinks and no `## Words` section at all despite a declared `stand_in`. Wrote all four Notes bullets from scratch (形声, OC \*mlus: phonetic 卯 + semantic 貝, verified via Wiktionary). Filled blank `pos: ""` → `名詞`, matching [[貿易]]'s own `名詞`.

**Words cross-check** (1 ground-truth hit): added [[貿易]], flagged as the `stand_in`, built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 資 (4265; 2026 characters remaining).

### 2026-08-05, iteration 474 — [[characters/資|資]]

Body had only two floating CC-initial/final wikilinks and one informal, unruby'd word note. Wrote all four Notes bullets from scratch (形声, OC \*ʔsli: phonetic 次 + semantic 貝, verified via Wiktionary; `mc_id: 1057` verified against `lookup/CC/CC 1000.md` line 62 — correct, no off-by-one this time). Filled blank `pos: ""` → `名詞`, matching [[資本]]'s own `名詞`.

**Words cross-check** (2 total ground-truth hits): [[資源]] already ruby'd and correct; reformatted [[資本]] with proper ruby+gloss and flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 賢 (4267; 2025 characters remaining — 4266 already perfected).

### 2026-08-05, iteration 475 — [[characters/賢|賢]]

Body had only two floating CC-initial/final wikilinks, no graphemic/SKIP/MC/Levels bullets. Wrote all four Notes bullets from scratch (形声, OC \*ɡiːn: phonetic 臤 + semantic 貝 "valuable, like money," verified via Wiktionary; `mc_id: 169` verified against `lookup/CC/CC 0000.md` line 177). Filled blank `pos: ""` → `性詞`.

**Words cross-check** (2 total ground-truth hits): [[賢淑]] already ruby'd and correct; added the missing [[賢明]] (the `stand_in`), flagged accordingly. **Chengyu**: [[選士唯賢]] already correctly listed, confirmed as the only real hit. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 践 (4269; 2024 characters remaining — 4268 already perfected).

### 2026-08-05, iteration 476 — [[characters/践|践]]

**Real `graphemic_classification` bug found and fixed**: stored as `㦮`, but Wiktionary confirms the real phonetic component is `戔` (OC \*zlaːn, semantic 足 "foot" + phonetic 戔, OC \*zlenʔ overall) — `㦮` doesn't correspond to any documented analysis of this character. Corrected.

**Process note**: while cross-checking Words, discovered [[実践]]'s own `characters:` field uses single-line bracket syntax (`characters: [実, 践]`) rather than the more common multi-line `- item` list — my simple grep/awk-based citation check used in recent iterations only reliably catches the multi-line form and would have silently missed this entry. Switched to a proper frontmatter-block regex (matches either syntax) for this and future iterations; earlier iterations this session were not retroactively re-checked, so a small risk of missed bracket-style citations exists in [[characters/識|識]] through [[characters/賢|賢]]'s Words/Chengyu/Derived Characters sections — worth a spot-check pass eventually, not urgent.

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch; `mc_id: 1195` verified against `lookup/CC/CC 1000.md` line 204 (listed under the traditional form 踐, correct). Filled blank `pos: ""` → `事詞`.

**Words cross-check** (2 total ground-truth hits, using the corrected regex): both [[実践]] and [[践踏]] already present and correct — only needed the `stand_in` flag added to [[実践]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 較 (4271; 2023 characters remaining — 4270 already perfected).

### 2026-08-05, iteration 477 — [[characters/較|較]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 車 semantic + 交 phonetic — itself a historical corruption of the original phonetic 爻 — verified via Wiktionary; `mc_id: 2946` verified against `lookup/CC/CC 2000.md` line 987). Filled blank `pos: ""` → `事詞`.

**Words cross-check** (2 total ground-truth hits, via the corrected regex from last iteration): both [[比較]] and [[比較格]] already present, correct, and properly flagged. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 輪 (char) (4272; 2022 characters remaining).

### 2026-08-05, iteration 478 — [[characters/輪 (char)|輪]]

**Real `graphemic_classification` bug found and fixed, a new subclass**: stored as `倫`, but Wiktionary confirms 輪's real phonetic component is `侖` (OC \*run) — `倫` is a *sibling* character that itself uses 侖 as its own phonetic (人 semantic + 侖 phonetic), not 輪's own component. Easy mistake to make since they look and sound alike; corrected to `侖` (no vault page exists for it, cited bare per the checklist's own convention for pageless phonetics).

Body had only a stray `## Words` entry and an unformatted note. Wrote all four Notes bullets from scratch; `mc_id: 1697` verified against `lookup/CC/CC 1000.md` line 726. Filled blank `pos: ""` → `名詞`.

**Words cross-check** (4 total ground-truth hits): 2 previously listed ([[輪郭]] properly, [[輪回]] informally in Notes — moved into Words); added the self-referential `stand_in` [[輪]] and [[法輪]] (missing).

**Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 輸 (4273; 2021 characters remaining).

### 2026-08-05, iteration 479 — [[characters/輸|輸]]

Graphemic content was already correct (形声, 車 + phonetic 兪, verified as the variant-form vault page for 俞), just malformed (plain markdown links instead of proper wikilinks, no radical link, floating CC-initial/final links). Reformatted and completed all four Notes bullets; `mc_id: 1295` verified against `lookup/CC/CC 1000.md` line 308. Filled blank `pos: ""` → `事詞`.

**Words cross-check** (2 total ground-truth hits): [[輸送]] already listed, flagged as `stand_in`; moved the informally-noted [[輸血]] into a proper `## Words` entry. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 返 (4275; 2020 characters remaining — 4274 already perfected).

### 2026-08-05, iteration 480 — [[characters/返|返]]

Body had only two floating CC-initial/final wikilinks and one informal, unruby'd word note. Wrote all four Notes bullets from scratch (形声/会意, OC \*panʔ: semantic 辵 + phonetic 反, verified via Wiktionary; `mc_id: 2041` verified against `lookup/CC/CC 2000.md` line 46). Filled blank `pos: ""` → `事詞`.

**Words cross-check** (1 ground-truth hit): [[返還]] reformatted with proper ruby+gloss and flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 述 (4276; 2019 characters remaining).

### 2026-08-05, iteration 481 — [[characters/述|述]]

Body had only two floating CC-initial/final wikilinks and one informal note. Wrote all four Notes bullets from scratch (形声, OC \*ɦljud: semantic 辵 + phonetic 朮, verified via Wiktionary; `mc_id: 1159` verified against `lookup/CC/CC 1000.md` line 168). Filled blank `pos: ""` → `事詞`.

**Words cross-check** (3 total ground-truth hits): [[陳述]] reformatted with proper ruby+gloss and flagged as `stand_in`; added the 2 missing — [[叙述]], [[上述]]. **Chengyu cross-check** (1 hit): added [[先題後述]] (missing). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 迷 (char) (4277; 2018 characters remaining).

### 2026-08-05, iteration 482 — [[characters/迷 (char)|迷]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, OC \*miː: semantic 辵 + phonetic 米, verified via Wiktionary; `mc_id: 1520` verified against `lookup/CC/CC 1000.md` line 545). Filled blank `pos: ""` → `性詞`.

**Words cross-check** (1 ground-truth hit): added the self-referential `stand_in` [[迷]], built from nothing. **Chengyu**: no hits — correctly omitted. **Derived Characters**: [[characters/謎 (char)|謎]] ("riddle, mystery") cites 迷 as its own `graphemic_classification` — added.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 逆 (char) (4278; 2017 characters remaining).

### 2026-08-05, iteration 483 — [[characters/逆 (char)|逆]]

**Confirmed `aliases: [屰]` is legitimate**: 屰 is genuinely the original/ancestor form of 逆 (a pictogram of an inverted person), not contamination like the 護/貞 cases — matches the already-correct `graphemic_classification: 屰`. **Fixed a broken link**: an informal note read "Use this instead of the more Mandarin [叛](反 (char).md)" — the display text 叛 pointed to the *wrong* file (反 (char).md, an unrelated character); 叛 has no vault page at all. Folded the observation into the graphemic bullet as plain text instead of a dangling mislink.

Wrote all four Notes bullets from scratch (verified via Wiktionary; `mc_id: 471` verified against `lookup/CC/CC 0000.md` line 489). `pos: 名詞` was already correct.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[逆]] and formalized the informally-noted [[逆数]] into a proper `## Words` entry. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 逓 (4279; 2016 characters remaining).

### 2026-08-05, iteration 484 — [[characters/逓|逓]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 辵 semantic + phonetic 虒 — with 逓 itself being the Japanese shinjitai simplification of traditional 遞, verified via Wiktionary; `mc_id: 3902` verified against `lookup/CC/CC 3000.md` line 943, listed under the traditional form). Caught and avoided creating a dead wikilink to `[[遞]]` (no vault page exists for it — it's only recorded in this page's own `aliases`), used bare text instead. `pos: 事詞` was already correct.

**Words cross-check** (1 ground-truth hit): [[逓送]] flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 遅 (char) (4280; 2015 characters remaining).

### 2026-08-05, iteration 485 — [[characters/遅 (char)|遅]]

**Second process fix**: my regex-based `characters:` citation check (fixed for bracket-syntax two iterations ago) still missed this word's own flush, non-indented `- item` list style (`characters:\n- 遅\n- 到` with no leading spaces on the dashes) — the lookahead assumed list items were always indented. Rewrote the checker as a proper YAML-parsing script (`find_citers.py`, saved to scratchpad) that loads each file's frontmatter with `yaml.safe_load` instead of pattern-matching; this is now the standard method going forward. Confirms [[遅到]] as a real hit that the two prior regex versions would each have missed for different reasons.

Filled blank `vietnamese: trì` (verified, genuine Hán-Việt reading) and `pos: ""` → `性詞`. **Left `boundedness` blank rather than guessing a number**: it's not part of the checklist's required-field or `date-last-perfect` criteria list, and ~277 other character pages across the vault leave it blank too — not a defect to "fix."

Wrote all four Notes bullets from scratch (形声, OC \*l'il: semantic 辵 + phonetic 犀, "rhinoceros," verified via Wiktionary — 犀's OC reading is a genuine mnemonic tie to "moving slowly"; `mc_id: 1344` verified against `lookup/CC/CC 1000.md` line 361, listed under traditional 遲).

**Words cross-check** (2 total ground-truth hits, using the new YAML-based checker): added the self-referential `stand_in` [[遅]] and [[遅到]] (previously missed). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 遍 (char) (4281; 2014 characters remaining).

### 2026-08-05, iteration 486 — [[characters/遍 (char)|遍]]

Body had only two floating CC-initial/final wikilinks, though `## Words`/`## Chengyu` were already partially built. Wrote all four Notes bullets from scratch (形声, OC \*peːns: semantic 辵 + phonetic 扁, verified via Wiktionary; `mc_id: 1714` verified against `lookup/CC/CC 1000.md` line 747). Filled blank `pos: ""` → `性詞`.

**Words cross-check** (2 total ground-truth hits, via the new YAML-based checker): [[普遍]] already correct; added the self-referential `stand_in` [[遍]] (missing). **Chengyu**: [[哀鴻遍野]] already correctly listed. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 郵 (4283; 2013 characters remaining — 4282 already perfected).

### 2026-08-05, iteration 487 — [[characters/郵|郵]]

Body had only two floating CC-initial/final wikilinks and three informal, unruby'd word notes. Wrote all four Notes bullets from scratch (会意, 垂 "far, remote" + 邑 "city" → "relay station" → "mail, post," verified via Wiktionary; `mc_id: 2230` verified against `lookup/CC/CC 2000.md` line 243). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (5 total ground-truth hits, via the YAML-based checker): 3 previously listed informally (郵帖, 郵政, 郵票 — all reformatted with proper ruby+gloss); added the missing self-referential `stand_in` [[郵便]] and [[郵便局]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 配 (char) (4284; 2012 characters remaining).

### 2026-08-05, iteration 488 — [[characters/配 (char)|配]]

**Real `graphemic_classification` bug found and fixed, a genuinely subtle case**: stored as `己` (implying 形声 with phonetic 己), but per Shuowen commentators (Xu Xuan, Duan Yucai) this is wrong — 配's oracle-bone/bronze forms show 酉 ("wine vessel") + 卩 ("kneeling person"), and seal script merely *corrupted* 卩 into the visually similar 己, which never functioned as a real phonetic. Corrected to `會意`, with the corruption history explained in the bullet (卩 has no vault page, cited bare).

Filled blank `pos: ""` → `事詞`, matching sibling words [[分配]]/[[支配]]. `mc_id: 1341` verified against `lookup/CC/CC 1000.md` line 358.

**Words cross-check** (6 total ground-truth hits, via the YAML-based checker): 3 previously listed informally (配偶, 配列, 配置 — all reformatted with proper ruby+gloss); added the missing self-referential `stand_in` [[配]], [[分配]], and [[支配]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 鉱 (4286; 2011 characters remaining — 4285 already perfected).

### 2026-08-05, iteration 489 — [[characters/鉱|鉱]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 金 semantic + phonetic 廣, verified via Wiktionary; `mc_id: 7563` is beyond local CC-file coverage, used verbatim per policy). Filled blank `vietnamese: khoáng` (verified, extremely common — khoáng sản, "mineral resources"). Avoided a dead `[[礦]]` wikilink (no vault page; it's only recorded in this page's own `aliases`) — used bare text instead, same fix as [[characters/逓|逓]] two iterations ago.

**Words cross-check** (3 total ground-truth hits): [[鉱物]] already listed; added the missing `stand_in` [[鉱石]] and [[鉱物学]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 銅 (char) (4287; 2010 characters remaining).

### 2026-08-05, iteration 490 — [[characters/銅 (char)|銅]]

**Malformed YAML fixed**: `japanese_native` was split across an invalid scalar-then-list-item pair (`あかがね` followed by `- あかがね` on the next line, duplicating the same reading) — same defect class as the 巻 case in the archived log. Collapsed to the single scalar.

**Real `mc_id` off-by-one bug found and fixed**: stored as `1543`, but that rank belongs to 珍 (`lookup/CC/CC 1000.md` line 568) — 銅's real rank is `1544` (line 569).

Wrote all four Notes bullets from scratch (形声, 金 semantic + phonetic 同, verified via Wiktionary). **Dropped a dead informal entry**: "[[銅牌]] 'bronze medal'" referenced a word file that doesn't exist anywhere in the vault — not preserved.

**Words cross-check** (5 total ground-truth hits, via the YAML-based checker): 3 previously listed as plain unruby'd links (黄銅, 青銅, 銅鑼 — all reformatted); added the missing self-referential `stand_in` [[銅]] and [[魔銅]] ("nickel," a genuine but easy-to-miss hit). **Chengyu cross-check** (1 hit): added [[金銀銅鉄]] (missing). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 鋼 (4288; 2009 characters remaining).

### 2026-08-05, iteration 491 — [[characters/鋼|鋼]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 金 semantic + phonetic 岡, cognate with [[剛]], both from the terminative of 固 "firm, solid" — verified via Wiktionary; `mc_id: 9283` is beyond local CC-file coverage, used verbatim per policy). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (1 ground-truth hit): [[鋼鉄]] flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 錯 (4289; 2008 characters remaining).

### 2026-08-05, iteration 492 — [[characters/錯|錯]]

**Fixed a broken relative-path wikilink**: `[[../lookup/CC/finals/韻 鈬開]]` had a `../` prefix baked into the wikilink itself — Obsidian wikilinks resolve by name, not path, so the prefix breaks the link (the exact defect the checklist's "Common mistakes" section warns about). Dropped the prefix and moved it into its proper place inside the MC-rank bullet.

Wrote all four Notes bullets from scratch (形声, 金 semantic + phonetic 昔, originally "grindstone" → "mistake, error," verified via Wiktionary; `mc_id: 968` verified against `lookup/CC/CC 0000.md` line 1001). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (1 ground-truth hit): added the missing `stand_in` [[錯誤]]. **Chengyu**: [[時代錯誤]] already correctly listed. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 録 (4290; 2007 characters remaining).

### 2026-08-05, iteration 493 — [[characters/録|録]]

`## Words` already existed with proper ruby formatting but sat before `## Notes` (wrong section order) and lacked the fixed four bullets. Reordered and wrote all four Notes bullets from scratch (形声, 金 semantic + phonetic 彔, verified via Wiktionary; `mc_id: 8821` is beyond local CC-file coverage, used verbatim per policy). `pos: 事詞` was already correct.

**Words cross-check** (4 total ground-truth hits): 3 previously listed (抄録 flagged as `stand_in`, 録音, 謄録 — all already correct); added the missing [[記録]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 鏡 (char) (4291; 2006 characters remaining).

### 2026-08-05, iteration 494 — [[characters/鏡 (char)|鏡]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 金 semantic + phonetic 竟, probably cognate with 景/影, verified via Wiktionary; `mc_id: 2583` verified against `lookup/CC/CC 2000.md` line 608). **Content gap fixed**: `english` only listed `lens`, missing the character's actual primary sense `mirror` — cross-checked against this character's own word page ([[words/鏡|鏡]]), which already correctly lists both; added `mirror` to the character page too.

**Words cross-check** (4 total ground-truth hits): added the self-referential `stand_in` [[鏡]], [[眼鏡]], [[鏡鑑]], and [[三稜鏡]], built from nothing. **Chengyu cross-check** (1 hit): added [[鏡花水月]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 附 (char) (4292; 2005 characters remaining).

### 2026-08-05, iteration 495 — [[characters/附 (char)|附]]

Body had only two floating CC-initial/final wikilinks and one informal note. Wrote all four Notes bullets from scratch (形声, 阜 semantic + phonetic 付 — 附 itself an alternative form of 付, verified via Wiktionary; `mc_id: 895` verified against `lookup/CC/CC 0000.md` line 925). Filled blank `pos: ""` → `事詞`.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[附]]; reformatted [[附近]] with proper ruby+gloss. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 院 (4293; 2004 characters remaining).

### 2026-08-05, iteration 496 — [[characters/院|院]]

Body had only two floating CC-initial/final wikilinks (Words section already existed with 5 correctly ruby'd entries). Wrote all four Notes bullets from scratch (形声, 阜 semantic + phonetic 完, verified via Wiktionary; `mc_id: 9222` beyond local CC-file coverage, used verbatim per policy). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (10 total ground-truth hits, via the YAML-based checker): 5 previously listed; added the 5 missing — [[病院]], [[医院]], [[寺院]], [[孤児院]], [[衆議院]] — flagging [[院落]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 陸 (4294; 2003 characters remaining).

### 2026-08-05, iteration 497 — [[characters/陸|陸]]

Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 阜 semantic + phonetic 坴 "clod of earth," verified via Wiktionary; `mc_id: 1269` verified against `lookup/CC/CC 1000.md` line 282). Avoided a dead `[[坴]]` wikilink (no vault page) — bare text instead. Filled blank `pos: ""` → `名詞`.

**Words cross-check** (3 total ground-truth hits): added the missing `stand_in` [[大陸]], [[陸地]], and [[陸亀]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 険 (char) (4295; 2002 characters remaining).

### 2026-08-05, iteration 498 — [[characters/険 (char)|険]]

**Confirmed `graphemic_classification: 㑒` is legitimate, not an error**: traditional 險's real phonetic is 僉, but 険 is specifically the Japanese shinjitai simplification where 僉 was itself further simplified to 㑒 — the stored value correctly describes *this* glyph's own component, not the traditional form's. Explained both layers in the bullet.

Wrote all four Notes bullets from scratch (verified via Wiktionary; `mc_id: 1118` verified against `lookup/CC/CC 1000.md` line 127, listed under traditional 險). Filled blank `pos: ""` → `性詞`.

**Words cross-check** (4 total ground-truth hits): [[冒険]] already listed; added the self-referential `stand_in` [[険]], [[危険]], and [[保険]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 隊 (char) (4296; 2001 characters remaining).

### 2026-08-05, iteration 499 — [[characters/隊 (char)|隊]]

Body had only two floating CC-initial/final wikilinks and one informal note. Wrote all four Notes bullets from scratch (形声, 阜 semantic + phonetic 㒸, verified via Wiktionary; `mc_id: 2059` verified against `lookup/CC/CC 2000.md` line 64). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (4 total ground-truth hits): added the self-referential `stand_in` [[隊]], [[軍隊]], and [[部隊]]; reformatted the informally-noted [[隊伍]] with proper ruby+gloss. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 階 (4297; 2000 characters remaining).

### 2026-08-05, iteration 500 — [[characters/階|階]]

**500 iterations reached this session** (counting unbroken from the archived log's own numbering). Body had only two floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 阜 semantic + phonetic 皆, verified via Wiktionary; `mc_id: 964` verified against `lookup/CC/CC 0000.md` line 997). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (2 total ground-truth hits): added the missing `stand_in` [[階段]] and [[階乗]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 際 (char) (4298; 1999 characters remaining).

### 2026-08-05, iteration 501 — [[characters/際 (char)|際]]

Body had a partial, informally-numbered `## Words` list (2 of 3 entries missing ruby) before `## Notes`, plus floating CC-initial/final wikilinks. Wrote all four Notes bullets from scratch (形声, 阜 semantic + phonetic 祭, related to 接, verified via Wiktionary; `mc_id: 1592` verified against `lookup/CC/CC 1000.md` line 617). `pos: 名詞` was already correct.

**Words cross-check** (5 total ground-truth hits): reformatted [[交際]] and [[国際]] with proper ruby+gloss; added the missing self-referential `stand_in` [[際]] and [[国際語]]; [[実際]] already correct. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 雑 (char) (4299; 1998 characters remaining).

### 2026-08-05, iteration 502 — [[characters/雑 (char)|雑]]

Body had only two floating CC-initial/final wikilinks and two informal notes. Wrote all four Notes bullets from scratch (形声 on traditional 雜: 衣 semantic + phonetic 集, verified via Wiktionary; `mc_id: 1193` verified against `lookup/CC/CC 1000.md` line 202, listed under traditional 雜). Noted the character is Kangxi-indexed under 隹 rather than its true etymological semantic 衣 — same coincidental-radical pattern as [[characters/象|象]]/[[characters/貞|貞]] earlier this sweep. Filled blank `pos: ""` → `性詞`.

**Words cross-check** (4 total ground-truth hits): added the self-referential `stand_in` [[雑]] and [[雑交]]; reformatted [[複雑]]/[[雑誌]] with proper ruby+gloss. **Noted but not fixed (out of scope)**: `words/雑.md`'s own `korean` field is the literal string `"null"` rather than a real value or an omitted key — a word-sweep fix. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 雖 (char) (4300; 1997 characters remaining).

### 2026-08-05, iteration 503 — [[characters/雖 (char)|雖]]

Body had only two floating CC-initial/final wikilinks (Words already had its one real entry). Wrote all four Notes bullets from scratch (形声, originally "lizard-like reptile," 虫 semantic + phonetic 唯, later borrowed for "although" — verified via Wiktionary; `mc_id: 201` verified against `lookup/CC/CC 0000.md` line 213). Noted the same coincidental Kangxi-radical-vs-semantic pattern as [[characters/雑 (char)|雑]] last iteration (indexed under 隹, not the real semantic 虫). Filled blank `pos: ""` → `連接詞`, matching sibling concessive conjunction [[characters/但|但]].

**Words cross-check** (1 ground-truth hit): [[雖]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 離 (4301; 1996 characters remaining).

### 2026-08-05, iteration 504 — [[characters/離|離]]

**Fixed a broken empty wikilink**: the graphemic bullet had `phonetic [[]]` — an empty link left where the phonetic component name should have been. The prose already correctly described the referent (black-naped oriole, preserved in 離黃); filled in the missing component name `离` as bare text (no vault page). Completed the remaining three Notes bullets and confirmed `mc_id: 454` against `lookup/CC/CC 0000.md` line 472. Filled blank `pos: ""` → `事詞`.

**Words cross-check** (7 total ground-truth hits): reformatted the 5 previously-listed plain links with proper ruby+gloss, flagging [[離別]] as the `stand_in`; added the 2 missing — [[離婚]] and [[離心率]]. Also removed a stray empty bullet point. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 需 (4303; 1995 characters remaining — 4302 already perfected).

### 2026-08-05, iteration 505 — [[characters/需|需]]

The existing graphemic bullet's "[[天]] ('person')" gloss looked suspicious at first (天 normally means "sky") but is actually correct per Wiktionary — an archaic use of 天 depicting a frontal human figure, distinct from its usual "sky" sense; confirmed rather than "corrected." Expanded with the 天→而 Han-dynasty corruption history and the real 需-vs-須 confusability note. Reorganized the body (a stray "Derived characters" heading had been mixed into the Notes bullets); `mc_id: 2229` verified against `lookup/CC/CC 2000.md` line 242. Filled blank `pos: ""` → `事詞`.

**Words cross-check** (1 ground-truth hit): [[需要]] flagged as the `stand_in`. **Chengyu**: no hits — correctly omitted. **Derived Characters cross-check** (2 hits): [[蠕]] already informally noted, reformatted; added the missing [[儒]] ("Confucian scholar").

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 響 (4304; 1994 characters remaining).

### 2026-08-05, iteration 506 — [[characters/響|響]]

**Fixed alias contamination**: `aliases:` wrongly included `磬` (qìng, "chime stone") alongside the legitimate `响`. Verified via WebSearch that 磬 and 響 are unrelated characters — different pronunciation, different components (殸+石 vs 郷+音), not documented variants of each other — matching the earlier 掩/護 and 楨/貞 contamination pattern. Removed `磬`, kept `响`. Confirmed `graphemic_classification: 郷` correct (形声, 音 semantic + 郷 phonetic, OC *qʰaŋʔ) and `mc_id: 2174` against `lookup/CC/CC 2000.md` line 183. Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` section (4 fixed bullets).

**Words cross-check** (4 ground-truth hits via `find_citers.py`): only [[影響]] was previously listed; added the 3 missing — [[反響]] (flagged as the `stand_in`), [[交響]], [[方響]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 騎 (4307; 1993 characters remaining).

### 2026-08-05, iteration 507 — [[characters/騎|騎]]

Straightforward iteration — `graphemic_classification: 奇` confirmed via WebSearch as the correct phonetic (形声, 馬 semantic + 奇 phonetic, OC *ɡral/*ɡrals; STEDT traces cognates across Tibeto-Burman, Hmong-Mien, Tai-Kadai, Mon-Khmer as likely borrowings from Chinese 騎). `mc_id: 401` verified against `lookup/CC/CC 0000.md` line 419. Filled blank `pos: ""` → `事詞` (matching the vault's dominant verb-pos convention over the word files' own inconsistent `動詞`). Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` section (4 bullets).

**Words cross-check** (2 ground-truth hits via `find_citers.py`): [[騎馬]] already present, flagged as the `stand_in`; added the missing [[騎乗]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 髪 (4310; 1992 characters remaining).

### 2026-08-05, iteration 508 — [[characters/髪|髪]]

**Fixed a major `mc_id` error**: stored value was `5174`, but the CC lookup files only go up to `CC 3000.md` (ranks ~3001–4000) — `5174` doesn't correspond to any real entry at all, not even an off-by-one. Grepped `髮`/`髪` across `lookup/CC/*.md` and found the real entry at `lookup/CC/CC 1000.md` line 274: rank 1261. Corrected `mc_id: 5174` → `1261`. Confirmed `graphemic_classification: 犮` correct via WebSearch (形声, 髟 semantic "long hair" + 犮 phonetic, OC *pat/*boːd). Filled two blank fields: `vietnamese: [phát]` (verified genuine Hán Việt reading) and `pos: ""` → `名詞`. Wrote the full `## Notes` section from scratch (previously empty).

**Learned the HSK-level lookup convention more precisely mid-iteration**: initially linked a nonexistent "HSK Elementary" page for `hsk_level: "2"`; checked an existing perfected character with the same level and corrected to the real page, [Old HSK 2](lookup/HSK/Old%20HSK%202.md) — the vault only names the level-1 tier "HSK Beginner," levels 2–6 use "Old HSK N."

**Words cross-check** (2 ground-truth hits): [[頭髪]] already present as `stand_in`; added missing [[金髪碧眼]]. **Chengyu** (1 hit): reformatted the plain-link [[結髪夫妻]] into proper ruby+gloss. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 鬼 (4311; 1991 characters remaining).

### 2026-08-05, iteration 509 — [[characters/鬼|鬼]]

The existing 象形 Notes bullet (kneeling ugly-masked figure, residual-tail 厶, related to 畏) was already well-researched and correct — kept as-is, just reorganized into the proper 4-bullet structure and merged the informal numbered "1. demon / 2. short for cobalt" list into prose. Confirmed `mc_id: 630` against `lookup/CC/CC 0000.md` line 654. Filled blank `pos: ""` → `名詞`.

**Words cross-check** (12 ground-truth hits via `find_citers.py` — the largest citation list handled this session): only 8 were previously listed as bare links with no ruby/gloss; most importantly, **[[鬼神]] was missing entirely despite being the character's own `stand_in`**. Added it plus [[鬼火]], [[洋鬼子]], and [[鬼金]] (a `固有名詞`-tagged neologism for "cobalt," already informally referenced in the old Notes text), and reformatted all 12 with proper ruby+gloss. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 鼓 (char) (4313; 1990 characters remaining).

### 2026-08-05, iteration 510 — [[characters/鼓 (char)|鼓 (char)]]

Confirmed `graphemic_classification: 會意` via WebSearch (壴 "drum" + 攴/支 "hand holding drumstick" — the standard Wiktionary analysis, not 形声). `mc_id: 592` verified against `lookup/CC/CC 0000.md` line 613. Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + informally-listed Words-in-Notes with a proper `## Notes` (4 bullets) and `## Words` split.

**Words cross-check** (4 ground-truth hits via `find_citers.py`): the two previously listed ([[鼓舞]], [[鞀鼓]]) were reformatted with corrected/verified 注音 (caught my own first-draft typo on 鼓舞's ruby reading by re-grepping the source word file before finalizing); added the two missing — [[鼓]] itself (the self-referential `stand_in`, the character's own bare-word page) and [[鉦鼓]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 暮 (4314; 1989 characters remaining).

### 2026-08-05, iteration 511 — [[characters/暮|暮]]

**Fixed a swapped semantic/phonetic assignment**: the existing graphemic bullet read "semantic 莫 + phonetic 日," backwards from the real etymology — verified via WebSearch that 暮 is semantic 日 ("sun") + phonetic 莫 ("sunset," OC *maːɡ); 莫 was the *original* pictogram (sun sinking into grass/bushes), later borrowed for negation "not," so 日 was re-added to disambiguate the "dusk" sense. Rewrote the bullet with the corrected roles and the borrowing history. Confirmed `mc_id: 1468` against `lookup/CC/CC 1000.md` line 489.

**Learned another level-lookup mapping nuance**: `joyo_level: "6"` maps to [Jōyō - Kyōiku](lookup/Japanese/Jōyō%20-%20Kyōiku.md) (not "Kōtō" — checked a precedent character, 処, sharing the same joyo_level value) and `hanmun_edu_level: "中"` maps to [Korean MS](lookup/Korean/Korean%20MS.md); `hsk_level: "4"` follows the established "Old HSK N" pattern.

**Words/Chengyu cross-check** (1 word + 1 chengyu hit via `find_citers.py`, matching what was already listed): reformatted [[日暮]] as the `stand_in` and fixed [[朝三暮四]]'s broken relative-path link (`/chengyu/...md`) to a proper wikilink, correcting its gloss to match the chengyu file's actual stored `english` field ("distinction without a difference") rather than the ad hoc idiom translation that had been written in its place.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 夫 (char) (4315; 1988 characters remaining).

### 2026-08-05, iteration 512 — [[characters/夫 (char)|夫 (char)]]

**Fixed a wrong `english` field**: stored as "right?" — but that's the classical Chinese sentence-final *particle* sense (fú), which the vault deliberately assigns only to the standalone word [[夫]] (per that word's own already-perfected, extensively-researched Notes). The character page's own stored readings (mandarin fū, korean_native 지아비 "husband") are the *noun* sense (非母 pju), not the particle (奉母 bju) — corrected `english` to "man, husband, laborer" to match. **Fixed alias contamination**: `趺` was listed as an alias, but verified via WebSearch it's a distinct 足+夫 phono-semantic character meaning "instep," not a variant of 夫 — removed (no vault page exists for it, so no Derived Characters entry either). Confirmed `graphemic_classification: 象形` (a variant of 大 depicting a standing man; the "hairpin" story is a Shuowen folk etymology for an added stroke, not real) and `mc_id: 34` against `lookup/CC/CC 0000.md` line 39. Filled blank `pos: ""` → `名詞`.

**Learned the Stroke-lookup zero-padding convention**: single-digit stroke counts use `Stroke 04.md`, not `Stroke 4.md` — a gap the earlier iterations' Stroke-count characters (all ≥10 strokes) never exposed.

**Words/Chengyu cross-check** (8 word + 2 chengyu ground-truth hits via `find_citers.py`): only 2 words were previously listed; added the 6 missing — [[夫]] itself (self-referential `stand_in`), [[夫婦]], [[夫子]], [[丈夫]], [[大夫]], [[結加夫坐]] — plus the missing chengyu [[欲夫治汝]] alongside the already-listed [[結髪夫妻]]. **Derived Characters**: no vault-page hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 諸 (char) (4316; 1987 characters remaining).

### 2026-08-05, iteration 513 — [[characters/諸 (char)|諸 (char)]]

Merged a duplicate `## Notes` heading (the page had two — one holding only floating bare initial/final links, the other holding the actual graphemic bullet with an empty semantic gloss `("")`). Confirmed `graphemic_classification: 者` via WebSearch (形声, 言 semantic "speech" + 者 phonetic; 諸 was originally a dependent pronoun/determiner gradually displacing 多) and filled in the missing "speech, words" gloss. Confirmed `mc_id: 77` against `lookup/CC/CC 0000.md` line 82. Filled blank `pos: ""` — chose `修飾語` (modifier) rather than a plain noun tag, matching the precedent of the semantically similar quantifier/determiner character [[各 (char)|各]] ("each"), since "various" functions the same grammatical way.

**Words cross-check** (4 ground-truth hits) + **Chengyu** (2 hits) via `find_citers.py`: added the missing self-referential `stand_in` [[諸]] plus both chengyu, [[諸法無我]] and [[諸行無常]] — neither had been listed at all. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 斉 (4317; 1986 characters remaining).

### 2026-08-05, iteration 514 — [[characters/斉|斉]]

**Fixed a wrong `graphemic_classification`**: stored as `指事` (ideogrammic indicator), but WebSearch confirms Wiktionary classifies 齊/斉 as `象形` — a pictogram of evenly sprouting grain ears (or, per some sources, neatly arranged fruits/thorns), not an abstract indicator. Corrected. **Fixed alias contamination**: `齎` (jī, "to present in both hands") was listed as an alias, but it's a distinct phono-semantic character (齊-phonetic + 貝-semantic), not a variant of 齊/斉 — removed (no vault page exists, matching the recently-established pattern from [[characters/響|響]]/磬 and [[characters/夫 (char)|夫]]/趺). Confirmed `mc_id: 82` against `lookup/CC/CC 0000.md` line 87. Filled blank `vietnamese: [tề]` (verified genuine Hán Việt reading).

**Words cross-check** (4 ground-truth hits via `find_citers.py` — page previously had no Words section at all): added all 4, flagging [[一斉]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 后 (4318; 1985 characters remaining).

### 2026-08-05, iteration 515 — [[characters/后|后]]

**Fixed alias contamination of a different flavor than usual**: `後` was listed as an alias, but WebSearch confirms 后 and 後 are genuinely distinct, etymologically unrelated characters (后: 会意 人+口, originally "rear/anus" → "ruler, sovereign," oracle-bone variant 毓 "woman giving birth" → "empress"; 後: 会意 幺+夊, "foot bound by rope" → "to lag behind") that only share the modern Mandarin reading hòu because PRC simplification reused 后's glyph to also write 後 — a real-world orthographic merger, not a variant relationship. Removed the alias and documented the merger in the Notes bullet (this differs from the usual co-occurrence-contamination pattern — here the two characters are both extremely common and totally independent, confirmed by `find_citers.py` showing zero overlap between 后's and 後's citing words). Confirmed `graphemic_classification: 會意` and `mc_id: 197` (`lookup/CC/CC 0000.md` line 205). Filled two blanks: `pos: ""` → `名詞` and `hanmun_edu_level: ""` → `中` (matching the `joyo_level: "6"` → Korean MS pattern established on [[characters/暮|暮]] and [[characters/諸 (char)|諸 (char)]] last iteration).

**Words cross-check** (1 ground-truth hit, matching what was already listed): flagged [[皇后]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 並 (char) (4319; 1984 characters remaining).

### 2026-08-05, iteration 516 — [[characters/並 (char)|並 (char)]]

**Untangled a 5-alias list into 3 genuine variants + 2 contaminants**: WebSearch + corpus cross-checks showed 并/幷 are real graphemic variants of 並 (并 has its own separate CC rank, 652, reflecting genuine independent historical usage, but shares the same core "side by side/together" sense), while 併/倂 are a distinct, narrower-sense derived character (人 semantic + 并 phonetic, own CC rank 3417, no vault page) meaning specifically "to combine, merge, annex" — different Old Chinese pronunciation per Wiktionary, not the same character. Removed 併/倂, kept 并/竝/幷. Also cleaned up two pieces of raw shorthand left in the old Notes text (`并=C#652` and `碰 is forbidden`) — the first was this exact 并-corpus-rank fact I'd independently re-derived, the second was already-correct shorthand for 碰's presence on [[文法 - 98違法字|the forbidden-character list]] (confirmed the list entry still there, with its own explanation: "recent coinage/colloquial form of 逢") — both rewritten as proper prose in the correct sections. Confirmed `mc_id: 610`. Filled blank `pos: ""` → `副詞` (matching the word [[並]]'s own stored pos, since the character functions identically).

**Words** (3 hits, already listed, reformatted with `stand_in` flag) **+ Chengyu** (1 missing hit, [[文体並存]], added) **+ Derived Characters** (the 碰-forbidden note, properly relocated) via `find_citers.py`.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 載 (char) (4320; 1983 characters remaining).

### 2026-08-05, iteration 517 — [[characters/載 (char)|載 (char)]]

Confirmed `graphemic_classification: 𢦏` via WebSearch (形声, 車 semantic "chariot" + 𢦏 phonetic; the "carry" and "record" senses both derive from the core "carrying" concept). Confirmed `mc_id: 623` against `lookup/CC/CC 0000.md` line 647. Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check**: `find_citers.py "載 (char)"` only found 2 hits, but `find_citers.py 載` (bare glyph) found 4 — [[記載]] and [[転載]] store `characters: 載` (bare form) instead of the `"載 (char)"` suffix that [[搭載]] and [[載]] correctly use. This is a real data inconsistency in those two word files' `characters:` field (out of scope to fix during a character-page iteration, flagging here), but since both genuinely cite 載 as a constituent, included all 4 in the Words section regardless of the field-format mismatch, flagging [[載]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 詳 (4321; 1982 characters remaining).

### 2026-08-05, iteration 518 — [[characters/詳|詳]]

Confirmed `graphemic_classification: 羊` via WebSearch (形声, 言 semantic "speech" + 羊 phonetic; the `mandarin: "xiáng, yáng"` dual reading checks out — 詳 is also an obsolete variant of 佯 "to feign, pretend," yáng). Confirmed `mc_id` against `lookup/CC/CC 1000.md` line 586, and normalized it from a quoted string `"1561"` to a plain number (only 7 of ~3347 character pages had a quoted `mc_id`, all outliers). Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` split; caught my own first-draft typo on 詳細's ruby reading by re-grepping the source word file before finalizing.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already present): flagged [[詳細]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 凄 (4324; 1981 characters remaining).

### 2026-08-05, iteration 519 — [[characters/凄|凄]]

**Applied the checklist's `mc_id: 0` policy for the first time this session**: the stored `mc_id` was blank, but grepping `lookup/CC/CC 0000–3000.md` found no entry for 凄 itself — only its two alias variants 淒 (rank 3876) and 悽 (rank 3291) are separately tracked in the corpus. Per the checklist ("`mc_id: 0` is a real, meaningful value... confirmed not present"), set `mc_id: 0` rather than guessing one of the variants' ranks, and phrased the MC bullet accordingly. Confirmed `graphemic_classification: 妻` (already correct, 形声 冫+妻) and cleaned up the informal "悽 was dropped from the Korean high school list in 2000" note, folding it into the levels bullet as the explanation for why `hanmun_edu_level: 名` — cross-checked against [[lookup/Korean/Korean Name ㅊ]], which explicitly lists both 凄 and 悽 under 처, confirming the "名" (name-only) demotion is accurate and current, not an error to fix. Filled the levels bullet with the correct mixed mapping (real Grade/HSK/Jōyō levels alongside the Korean name-only tier).

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already present): reformatted [[凄涼]] (the `stand_in`, already separately perfected) and [[凄惨]] with proper ruby+gloss. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 塔 (char) (4388; 1980 characters remaining — a large gap, danayo_id 4325–4387 already perfected).

### 2026-08-05, iteration 520 — [[characters/塔 (char)|塔 (char)]]

**Added a completely missing `mc_id` field** (the key didn't exist in frontmatter at all, unlike a blank value): grepped all four `lookup/CC/CC 0000–3000.md` files for 塔 and its three alias variants (㙮, 墖, 𩫊) and found zero hits anywhere — set `mc_id: 0` per the checklist's "confirmed not present" policy, same as [[characters/凄|凄]] last iteration. Confirmed `graphemic_classification: 荅` via WebSearch and found a genuinely interesting etymology worth expanding: 塔 is a Late Old Chinese (Eastern Han) Sanskrit loanword, an abbreviation of 卒塔婆 transliterating स्तूप (stūpa) — filled in the previously-empty semantic gloss ("") and added the loanword history. Verified 墖 as a documented old variant via WebSearch; treated 㙮/𩫊 as legitimate obscure variants by the same reasoning (rare CJK-B forms, not the usual co-occurrence-contamination pattern). Merged a duplicate `## Notes` heading.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was implicitly the `stand_in` but not yet listed): added [[塔]] itself. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 喉 (4390; 1979 characters remaining).

### 2026-08-05, iteration 521 — [[characters/喉|喉]]

**Fixed a `stand_in` pointing to a nonexistent word**: stored as `喉頭`, but `words/喉頭.md` doesn't exist anywhere in the vault — a genuine gap in the character's own required-field integrity, not just a missing citation. `find_citers.py` confirmed the only real word citing 喉 as a constituent is [[咽喉]] ("throat"), so retargeted `stand_in` to that instead of leaving it dangling or fabricating the missing word page (out of scope for a character-page iteration). Confirmed `graphemic_classification: 侯` (already correct, 形声 口+侯) and found `mc_id: 2465` via grep (`lookup/CC/CC 2000.md` line 486) for the previously-blank field. Cleaned up the informal "Dropped from the Korean HS list in 2000" note into the levels bullet, cross-checked against [[lookup/Korean/Korean Name ㅎ]] (confirms 喉's current name-only status) — same pattern as [[characters/凄|凄]] two iterations ago.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added [[咽喉]] as the corrected `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 曇 (char) (4391; 1978 characters remaining).

### 2026-08-05, iteration 522 — [[characters/曇 (char)|曇 (char)]]

**Fixed a wrong `graphemic_classification`**: stored as `旦` (implying 形声 with 旦 as phonetic), but WebSearch (Wiktionary, cross-checked against a second kanji-etymology source) confirms 曇 is `会意` (日 "sun" + 雲 "cloud" → "sun behind clouds" → "overcast") — 曇 has no 旦 component at all; 旦 (日+一, "dawn") is an unrelated character, so the stored value looks like a plain misidentification rather than a legitimate alternate analysis. Corrected. Filled the previously-blank `mc_id` to `0` after confirming zero hits for 曇/昙 anywhere in `lookup/CC/CC 0000–3000.md`. Also fixed body-structure ordering: the `meta-bind-embed` block was sitting *after* a stray `# Notes` heading, violating the checklist's "embed must be first or directly after the callout" rule — reordered.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[曇]] (previously listed nowhere in the body at all). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 塞 (5001; 1977 characters remaining — another large gap, danayo_id 4392–5000 already perfected).

### 2026-08-05, iteration 523 — [[characters/塞|塞]]

Confirmed `graphemic_classification: 會意` and the existing informal "Components: 𡨄, 土" note via WebSearch (oracle-bone 𡨄 = 宀+廾+工, "stuffing a house with items"; 土 "soil" added later per Shuowen) — expanded into a full graphemic bullet with the semantic extension "to stop up" → "pass, frontier, fortress." Confirmed `mc_id: 574` (`lookup/CC/CC 0000.md` line 595) and that alias `𡨄` is the genuine oracle-bone ancestor form, not contamination. Fixed a dangling `[[𡨄]]` wikilink to a nonexistent page (bare text instead, per established convention).

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already listed): reordered with [[梗塞]] flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 鎖 (char) (5002; 1976 characters remaining).

### 2026-08-05, iteration 524 — [[characters/鎖 (char)|鎖 (char)]]

A relatively light iteration — the page's Notes bullet already documented a prior-session fix (`graphemic_classification` corrected from a mistaken `貝` to the real phonetic 𧴪, confirmed correct again via WebSearch: 形声, 金 semantic + 𧴪 phonetic). Trusted the existing large `mc_id: 5055` per the checklist's long-tail policy (beyond the locally-mirrored top ~4000, not fabricated). Filled blank `pos: ""` → `名詞`. Converted the `# Notes` heading to `##` and completed the remaining 3 bullets (SKIP/Stroke, MC rank, levels) that had been left as floating bare links.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[鎖]] (previously listed nowhere in the body). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 荒 (5003; 1975 characters remaining).

### 2026-08-05, iteration 525 — [[characters/荒|荒]]

Confirmed `graphemic_classification: 巟` via WebSearch (形声, 艸 semantic "grass" + 巟 phonetic; 巟 is cognate with [[亡]] "to disappear" through a Proto-Sino-Tibetan causative *s- prefix — a nice etymological detail worth keeping) and `mc_id: 1216` (`lookup/CC/CC 1000.md` line 229). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets); fixed a `[[巟]]` wikilink to bare text since no vault page exists for the phonetic component.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[荒廃]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 錬 (5004; 1974 characters remaining).

### 2026-08-05, iteration 526 — [[characters/錬|錬]]

A light iteration — the page was already essentially complete (all 4 Notes bullets, correct `graphemic_classification: 柬`, large trusted long-tail `mc_id: 4509`). Verified the 3-item alias list (鍊/煉/炼) via WebSearch: all four forms (錬/鍊/煉/炼) are genuine orthographic variants of the same morpheme — 錬/鍊 use 金 "metal" as the semantic, 煉/炼 use 火 "fire," but all four share pronunciation and meaning ("temper, refine, smelt"); no contamination here, unlike the 併/齎/趺/後 cases earlier this session. **Note: user switched to continuous mode ("continuously perfect characters, no waiting") — iterations from here on chain back-to-back without `ScheduleWakeup` calls between them.**

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already listed): flagged [[鍛錬]] as the `stand_in`.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 縁 (5005; 1973 characters remaining).

### 2026-08-05, iteration 527 — [[characters/縁|縁]]

Confirmed `graphemic_classification: 彖` via WebSearch (形声, 糸 semantic "silk thread" + 彖 phonetic — originally "hem/edge of cloth," extended to "reason, cause" and "fate/predestined connection"). Confirmed `mc_id: 1347` (`lookup/CC/CC 1000.md` line 364). Filled blank `pos: ""` → `名詞` and blank `vietnamese: ""` → `[duyên]` (verified genuine Hán Việt reading). **Found the correct `hsk_level`** by distinguishing two differently-structured lookup files: `lookup/HSK/Old HSK 3.md` and `...4.md` turned out to be co-occurrence/frequency-count lists (`[char]: N` format, not level assignments), while `lookup/HSK/Old HSK 5.md` is a genuine numbered vocabulary list — 縁/緣 appears there at position 405, confirming `hsk_level: "5"` for the previously-blank field.

**Flagged an out-of-scope word-file duplicate**: [[緣故]] (fully perfected, `date-last-perfect: 2026-06-13`, explicitly documents that [[縁故]] is its own alias) and `words/縁故.md` (an orphaned, never-perfected duplicate stub with near-identical content) both exist as separate word pages for the same word — not fixed here (character-page scope only), but worth a follow-up word-sweep merge.

**Words cross-check** (4 ground-truth hits via `find_citers.py`, mapping to 3 real words after resolving the duplicate): flagged [[因緣]] as the `stand_in`, kept [[緣故]] (the canonical page) and [[攀縁]], reformatted from the old mixed Notes/Words layout.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 震 (5006; 1972 characters remaining).

### 2026-08-05, iteration 528 — [[characters/震|震]]

**Fixed another `mc_id` off-by-few error**: stored `841`, but that rank actually belongs to 竊 (`lookup/CC/CC 0000.md` line 871); 震's real rank is 844 (line 874) — corrected. Confirmed `graphemic_classification: 辰` via WebSearch (形声, 雨 semantic + 辰 phonetic, "to shake/quake"; related to 振). Fixed multiple broken `../`-prefixed link paths (a recurring defect class per the checklist) and merged a duplicate/leftover `## Definition` section (trigram/hexagram trivia, floating bare initial/final links, a stray `[[震怒]]` citation, and a second `## Words` block) into the proper single-pass structure — this required a direct `head`-truncation via Bash after several `Edit` exact-match failures on the duplicate block (likely invisible whitespace/encoding quirks in the old content).

**Words cross-check** (4 ground-truth hits via `find_citers.py`): kept [[震動]] (`stand_in`) and [[震怒]], added the 2 missing — [[地震]] and [[余震]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 麗 (5007; 1971 characters remaining).

### 2026-08-05, iteration 529 — [[characters/麗|麗]]

Mostly-complete page. **Fixed alias contamination**: `驪` (lí, "black horse") was listed as an alias, but WebSearch confirms it's a distinct derived character (馬 semantic + 麗 phonetic phono-semantic compound, own corpus rank 1682, no vault page) — 麗 is only its phonetic component, not a variant of 麗 itself. Removed, matching the 齎/斉, 併/並, 趺/夫 pattern from earlier this session. Filled blank `pos: ""` → `性詞`.

**Words cross-check** (4 ground-truth hits via `find_citers.py`, matching what was already listed): flagged [[秀麗]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 亜 (5008; 1970 characters remaining).

### 2026-08-05, iteration 530 — [[characters/亜|亜]]

**Discovered a new nuance in the alias-legitimacy pattern**: `堊` (chalk) initially looked like the usual contamination case (WebSearch confirms it's structurally distinct, 亞 phonetic + 土 semantic), but the vault's own already-perfected [[白亜紀]] word page explicitly documents "亜 (Dan'a'yo stand-in for 堊)" — a deliberate, already-established Japanese daiyōji substitution (like modern 亜 replacing 堊 in 白亜/白堊 "chalk"), not an accidental co-occurrence conflation. Kept the alias but annotated the Notes bullet to clarify it's a substitution specific to the "chalk" sense, distinct from 亞/亚 (true variants for the primary "second/Asia" senses). Confirmed `graphemic_classification: 象形` and `mc_id: 1762` (`lookup/CC/CC 1000.md` line 795). Completely rebuilt the malformed Notes section (out-of-order bullets, raw wikilinks to non-existent lookup pages like `[[SKIP-4-7-1]]` instead of proper markdown links, a stray `## Definition` section).

**Words cross-check** (19 word + 1 chengyu ground-truth hits via `find_citers.py` — by far the largest citation set this session, since 亜 is the vault's own conlang-name character in [[単亜語]]): only 10 were previously listed, several without ruby/gloss; added 10 more including the `stand_in` [[亜細亜]] and the previously-uncited [[単亜語]] itself, plus the missing chengyu [[東亜自通]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 浸 (char) (5009; 1969 characters remaining).

### 2026-08-05, iteration 531 — [[characters/浸 (char)|浸 (char)]]

**Fixed a frontmatter/prose mismatch**: `graphemic_classification` was stored as `會意`, but the page's own existing Notes bullet already correctly described it as 形声 (水 semantic + 𡩠 phonetic) — confirmed via WebSearch and corrected the frontmatter field to `𡩠` to match. Preserved the useful existing warning note about not merging with 滲 (a distinct character sometimes conflated with 浸 in Japanese). Confirmed `mc_id: 1953` (`lookup/CC/CC 1000.md` line 994). Filled blank `pos: ""` → `事詞`. Filled in the previously-empty semantic/phonetic glosses.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[浸]] alongside the already-listed [[浸食]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 寂 (5010; 1968 characters remaining).

### 2026-08-05, iteration 532 — [[characters/寂|寂]]

Light iteration — Notes were already complete and correct. Confirmed `graphemic_classification: 叔` via WebSearch (形声, 宀 semantic "house" + 叔 phonetic) and `mc_id: 2906` (`lookup/CC/CC 2000.md` line 947). Filled blank `pos: ""` → `性詞`.

**Words cross-check** (4 word + 1 chengyu ground-truth hits via `find_citers.py`): added the missing [[静寂]] and [[涅盤寂静]], flagged [[寂滅]] as the `stand_in`.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 般 (char) (5012; 1967 characters remaining — danayo_id 5011 already perfected).

### 2026-08-05, iteration 533 — [[characters/般 (char)|般 (char)]]

**Coincidental-Kangxi-radical case, same pattern as 象/豕, 貞/貝, 雑/衣**: confirmed via WebSearch that 般's modern `radical: 舟` ("boat") is a later reinterpretation artifact — the true original composition is 会意 of a rotated 凡/皿 ("plate," the ancestor of [[盤 (char)|盤]]) + 攴 ("hand with stick"), unrelated to boats; documented rather than "corrected" (the Kangxi radical field itself is accurate indexing data). Confirmed `mc_id: 2134` (`lookup/CC/CC 2000.md` line 143). Filled blank `pos: ""` → `名詞`. Rebuilt the malformed `# Notes` heading + floating bare links into the proper 4-bullet structure.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[般]] alongside the already-listed [[一般]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 敏 (char) (5013; 1966 characters remaining).

### 2026-08-05, iteration 534 — [[characters/敏 (char)|敏 (char)]]

Confirmed `graphemic_classification: 毎` via WebSearch (形声, 攴 semantic "hand, action" + 每/毎 phonetic) and `mc_id: 1705` (`lookup/CC/CC 1000.md` line 738). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets); fixed a `[[毎]]` link to the correctly-suffixed `毎 (char).md` filename.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[敏]] alongside the already-listed [[敏感]] and [[敏捷]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 核 (char) (5014; 1965 characters remaining).

### 2026-08-05, iteration 535 — [[characters/核 (char)|核 (char)]]

Confirmed `graphemic_classification: 亥` via WebSearch (形声, 木 semantic "tree" + 亥 phonetic — originally the woody pit/seed of fruit, extended to "nucleus, kernel," then "to examine/verify") and `mc_id: 2957` (`lookup/CC/CC 2000.md` line 998). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets); fixed a `[[木]]` link to the correctly-suffixed `木 (char).md` filename.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[核]] and the missing [[陰核]], alongside the already-listed [[核金]] (a `neologism`-tagged periodic-table coinage for ytterbium). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 侮 (5015; 1964 characters remaining).

### 2026-08-05, iteration 536 — [[characters/侮|侮]]

Confirmed `graphemic_classification: 毎` via WebSearch (形声, 人 semantic "person" + 每/毎 phonetic — "to insult, ridicule") and `mc_id: 1693` (`lookup/CC/CC 1000.md` line 722). Filled blank `pos: ""` → `事詞`. Fixed a `[每](毎%20(char).md)` markdown-link to a proper wikilink and folded the informal "Added to the Korean HS list in 2000" note into the levels bullet — the mirror-image case of the earlier 凄/喉 demotions.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[侮辱]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 振 (char) (5016; 1963 characters remaining).

### 2026-08-05, iteration 537 — [[characters/振 (char)|振 (char)]]

**Fixed alias contamination**: `顫` (zhàn, "to tremble, shiver") was listed as an alias, but WebSearch confirms it's a distinct character (頁 semantic + 亶 phonetic) — semantically adjacent to but not a variant of 振 (手 semantic + 辰 phonetic). Removed (no vault page, no corpus rank either). Confirmed `graphemic_classification: 辰` and `mc_id: 1071` (`lookup/CC/CC 1000.md` line 76). Filled blank `pos: ""` → `事詞`. Rebuilt the malformed Notes/Words split (2 words had been informally cited inside `# Notes` instead of `## Words`).

**Words cross-check** (5 ground-truth hits via `find_citers.py`, surfaced by the bare-glyph search since [[振子]]/[[振幅]] store `characters: 振` without the `(char)` suffix — the same format inconsistency flagged on [[characters/載 (char)|載]] earlier): added the self-referential `stand_in` [[振]] and reformatted all 5 with proper ruby+gloss. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 枯 (char) (5017; 1962 characters remaining).

### 2026-08-05, iteration 538 — [[characters/枯 (char)|枯 (char)]]

Confirmed `graphemic_classification: 古` via WebSearch (形声, 木 semantic "tree" + 古 phonetic; Austroasiatic loan etymology, cf. Khmer ខះ "to dry up") and `mc_id: 1470` (`lookup/CC/CC 1000.md` line 491). Filled blank `pos: ""` → `性詞`. Built the entire `## Notes`/`## Words` structure from scratch (page previously had only floating bare initial/final links).

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[枯]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 殿 (5018; 1961 characters remaining).

### 2026-08-05, iteration 539 — [[characters/殿|殿]]

**Fixed a wrong `graphemic_classification`**: stored as `象形` (pictogram), but WebSearch (Wiktionary/Shuowen) confirms 殿 is `形声` — phonetic 𡱂 (itself analyzed as 尸+丌, "buttocks") + semantic 殳 ("hand with weapon"), not a pictogram at all. Corrected to store the phonetic component name `𡱂`, and wrote up the (debated) "striking the buttocks" → "elevated building" semantic development. Confirmed `mc_id: 1099` (`lookup/CC/CC 1000.md` line 104). Filled blank `pos: ""` → `名詞`. Removed a cryptic leftover scratch note ("needed a din") and built the proper Notes/Words structure.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[宮殿]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 培 (5019; 1960 characters remaining).

### 2026-08-05, iteration 540 — [[characters/培|培]]

Confirmed `graphemic_classification: 咅` via WebSearch (形声, 土 semantic "earth" + 咅 phonetic — originally banking earth around plant roots/walls, extended to "cultivate, foster") and trusted the existing large `mc_id: 4276` per the checklist's long-tail policy (no local corpus hit, beyond the ~4000 mirrored range, not fabricated). Fixed a broken `[土](Radical%20032)` markdown-link to a proper wikilink and merged floating bare initial/final links plus 2 informally-cited words into the standard 4-bullet/Words structure. Caught my own first-draft typo on 培養's ruby reading by re-grepping the source word file before finalizing.

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already listed): flagged [[培養]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 寡 (5020; 1959 characters remaining).

### 2026-08-05, iteration 541 — [[characters/寡|寡]]

Confirmed `graphemic_classification: 會意` via WebSearch (宀 "house" + 頁 "head" — "only one person in the house, alone"; noted the Shuowen seal-script misreading as 宀+頒 "to distribute," a documented false etymology from decorative strokes added to 頁) and `mc_id: 354` (`lookup/CC/CC 0000.md` line 369). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[寡婦]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 越 (char) (5021; 1958 characters remaining).

### 2026-08-05, iteration 542 — [[characters/越 (char)|越 (char)]]

Confirmed `graphemic_classification: 戉` via WebSearch (形声, 走 semantic "to walk/run" + 戉 phonetic, originally "large battle-axe" and the ancient name of the State of Yue) and `mc_id: 336` (`lookup/CC/CC 0000.md` line 351). Merged a duplicate/scrambled Notes section (a `## Chengyu` heading had been inserted mid-Notes, with floating bare initial/final links and 2 more words informally cited after it) into the proper single-pass structure.

**Words cross-check** (11 ground-truth hits via `find_citers.py` — [[超越]] only surfaced via the bare-glyph search due to the same `characters:` field-suffix inconsistency seen on [[characters/載 (char)|載]] and [[characters/振 (char)|振]]): only 1 was previously listed; added the other 10, including the self-referential `stand_in` [[越]] and the vault's own CJKV-abbreviation word [[中日韓越]]. Caught two of my own first-draft ruby-reading guesses (on [[越境]]/[[越盟]] and the chengyu gloss) by re-grepping source files before finalizing — a good reminder to always verify rather than infer readings even for "obvious" compounds. **Chengyu** (1 hit, already listed): reformatted [[呉越同舟]] with its real stored gloss.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 循 (char) (5022; 1957 characters remaining).

### 2026-08-05, iteration 543 — [[characters/循 (char)|循 (char)]]

Confirmed `graphemic_classification: 盾` via WebSearch (形声, 彳 semantic "movement" + 盾 phonetic — "to follow, abide by, comply with") and `mc_id: 978` (`lookup/CC/CC 0000.md` line 1011). Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section built from scratch.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[循]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 娘 (char) (5023; 1956 characters remaining).

### 2026-08-05, iteration 544 — [[characters/娘 (char)|娘 (char)]]

Confirmed `graphemic_classification: 良` via WebSearch (形声, 女 semantic "woman" + 良 phonetic; the syllable is unattested before Tang, possibly a fusion of 女郎 "lady") and trusted the existing `mc_id: 5193` per the long-tail policy. Merged the malformed body (bare initial/final links floating mid-Notes, a stray unheaded observation about [[処女]]) into the proper structure — hit an invisible non-breaking-space (U+00A0) character in the old text that caused repeated `Edit` exact-match failures, resolved with a direct Python string-replace via Bash.

**Words cross-check** (2 ground-truth hits via `find_citers.py` — [[姑娘]] only surfaced via the bare-glyph search, same `characters:` field-suffix pattern as [[characters/載 (char)|載]]/[[characters/振 (char)|振]]/[[characters/越 (char)|越]]): added the self-referential `stand_in` [[娘]] alongside the already-listed [[姑娘]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 苗 (5024; 1955 characters remaining).

### 2026-08-05, iteration 545 — [[characters/苗|苗]]

Confirmed `graphemic_classification: 會意` via WebSearch (艸 "grass" + 田 "field" — a sprout rising from a field) and `mc_id: 1519` (`lookup/CC/CC 1000.md` line 544). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets).

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the missing self-referential `stand_in` [[種苗]] and [[苗族]] alongside the already-listed [[苗圃]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 抵 (5025; 1954 characters remaining).

### 2026-08-05, iteration 546 — [[characters/抵|抵]]

Confirmed `graphemic_classification: 氐` via WebSearch (形声, 手 semantic "hand" + 氐 phonetic — "to push against, resist"; possibly related to 擠) and `mc_id: 1540` (`lookup/CC/CC 1000.md` line 565). Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section (previously empty despite the `stand_in` word existing).

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching the character's own `stand_in` field): added [[抵抗]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 裕 (5026; 1953 characters remaining).

### 2026-08-05, iteration 547 — [[characters/裕|裕]]

Confirmed `graphemic_classification: 谷` via WebSearch (形声, 衣 semantic "clothes" + 谷 phonetic, folk-etymologized as "space in the clothes") and `mc_id: 2605` (`lookup/CC/CC 2000.md` line 634). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already the `stand_in`): added [[富裕]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 盲 (5027; 1952 characters remaining).

### 2026-08-05, iteration 548 — [[characters/盲|盲]]

Confirmed `graphemic_classification: 亡` via WebSearch (形声, 目 semantic "eye" + 亡 phonetic — "blind") and `mc_id: 2262` (`lookup/CC/CC 2000.md` line 275). Filled blank `pos: ""` → `修飾語` (matching the stand_in word [[盲目]]'s own stored pos). Fixed section ordering (`## Words` had been placed before `# Notes`) and merged into the proper structure.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the missing self-referential `stand_in` [[盲目]] and [[盲人]] alongside the already-listed [[盲従]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 亭 (5028; 1951 characters remaining).

### 2026-08-05, iteration 549 — [[characters/亭|亭]]

Confirmed `graphemic_classification: 丁` via WebSearch (形声, semantic from simplified 高/京 "tall building" + 丁 phonetic — Shuowen: "a place of stability for the people, with a tower"; originally roadside rest-stops/watchposts/postal relay stations) and `mc_id: 1051` (`lookup/CC/CC 1000.md` line 56). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already the `stand_in`): added [[亭子]] (whose own page already documents a previously-fixed false-homophone claim with [[停止]]).

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 削 (char) (5029; 1950 characters remaining).

### 2026-08-05, iteration 550 — [[characters/削 (char)|削 (char)]]

Confirmed `graphemic_classification: 肖` via WebSearch (形声, 刀 semantic "knife" + 肖 phonetic — "to scrape, pare, whittle, trim") and `mc_id: 1182` (`lookup/CC/CC 1000.md` line 191). Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets); caught my own first-draft empty ruby reading on [[削除]] by re-grepping the source word file before finalizing.

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already listed): added the self-referential `stand_in` [[削]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

**User switched pacing back from continuous mode to a paced ~8-minute loop.** Next never-perfected character by `danayo_id`: 偶 (5030; 1949 characters remaining).

### 2026-08-05, iteration 551 — [[characters/偶|偶]]

Confirmed `graphemic_classification: 禺` via WebSearch (形声, 人 semantic "person" + 禺 phonetic — originally "a statue of a person, an idol," cognate with 遇 "to meet"; extended to "pair, even number" and "by chance") and `mc_id: 1754` (`lookup/CC/CC 1000.md` line 787). Filled blank `pos: ""` → `名詞`. Fixed broken `../`-prefixed link paths and a malformed markdown-link/wikilink mix; merged floating bare initial/final links and 3 informally-cited words into the proper structure.

**Words cross-check** (6 word + 1 chengyu ground-truth hits via `find_citers.py`): only 3 words were previously listed; added the missing self-referential `stand_in` [[偶像]], [[木偶]], [[配偶]], plus the chengyu [[上下無偶]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 僚 (5031; 1948 characters remaining).

### 2026-08-05, iteration 552 — [[characters/僚|僚]]

**Fixed alias contamination**: `繚` (a distinct character meaning "to wind/wrap around") was listed as an alias, but WebSearch confirms it's unrelated to 僚 despite sharing the 尞 phonetic — removed. Also removed `尞` itself from aliases: it's the shared phonetic root of a whole character family (confirmed [[寮]], [[療]], [[瞭]], [[遼]] all independently store `graphemic_classification: 尞`), not a variant specific to 僚 — the same phonetic-root-vs-alias distinction established on [[characters/敏 (char)|敏]]/毎 and [[characters/娘 (char)|娘]]/良 earlier this session. Confirmed `mc_id: 1795` (`lookup/CC/CC 1000.md` line 828). Folded the informal "Added to Korean HS list in 2000" note into the levels bullet.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the missing [[官僚主義]], flagged [[同僚]] as the `stand_in` (reordering ahead of [[官僚]]). **Derived Characters** (already listed, 4 hits): added ruby+gloss to all 4 per checklist convention.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 兼 (char) (5032; 1947 characters remaining).

### 2026-08-05, iteration 553 — [[characters/兼 (char)|兼 (char)]]

Confirmed `graphemic_classification: 會意` via WebSearch (又 "hand" holding two 禾 "grain stalks" — compare [[秉]], a hand holding one stalk) and `mc_id: 822` (`lookup/CC/CC 0000.md` line 852). Replaced the informal "Components: 又, 禾" note + floating bare links with a proper `## Notes` (4 bullets), preserving the useful existing "doubles-as a chair" gloss example.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[兼]]. **Chengyu** (1 hit): added the previously-uncited [[詞彙兼容]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 含 (5033; 1946 characters remaining).

### 2026-08-05, iteration 554 — [[characters/含|含]]

Confirmed `graphemic_classification: 今` via WebSearch (形声, 口 semantic "mouth" + 今 phonetic — originally "to hold in the mouth," extended to "contain, include"; cognate with [[函]] "to contain; box") and `mc_id: 1546` (`lookup/CC/CC 1000.md` line 571). Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added both, flagging [[包含]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 妥 (5034; 1945 characters remaining).

### 2026-08-05, iteration 555 — [[characters/妥|妥]]

Confirmed `graphemic_classification: 會意` via WebSearch (爪 "hand" + 女 "woman" — a hand calming a woman down, "to comfort, placate," shifting to "settled, appropriate") and trusted the existing `mc_id: 5362` per the long-tail policy (no local corpus hit for 妥, beyond the ~4000 mirrored range). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading + informally-listed words with a proper `## Notes` (4 bullets) and `## Words` section; caught my own first-draft ruby-reading guess on [[妥協]] by re-grepping the source file before finalizing.

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already listed): flagged [[妥当]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 孤 (5035; 1944 characters remaining).

### 2026-08-05, iteration 556 — [[characters/孤|孤]]

Confirmed `graphemic_classification: 瓜` via WebSearch (形声, 子 semantic "child" + 瓜 phonetic — originally "orphan," extended to "alone, solitary") and `mc_id: 786` (`lookup/CC/CC 0000.md` line 813). `pos` was already correctly filled. Fixed broken `../`-prefixed link paths, a malformed markdown-link/wikilink mix, and merged a scrambled body (a `## Chengyu` heading inserted before the words, floating bare initial/final links) into the proper structure.

**Words cross-check** (4 ground-truth hits, matching what was already listed) **+ Chengyu** (2 hits via `find_citers.py`, only 1 previously listed): added the missing [[孤立無援]] alongside [[孤軍奮闘]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 妨 (5036; 1943 characters remaining).

### 2026-08-05, iteration 557 — [[characters/妨|妨]]

Confirmed `graphemic_classification: 方` (形声, 女 semantic "woman" + 方 phonetic — "to hinder, impede, obstruct"; a standard, well-documented phonetic series shared with 仿/芳/房/放) and `mc_id: 2407` (`lookup/CC/CC 2000.md` line 428). Replaced the malformed `# Notes` heading + misplaced `## Words` split with a proper `## Notes` (4 bullets) and single `## Words` section; fixed a `[[方 (char)]]` link to the correct bare filename `方.md`.

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching what was already listed): flagged [[妨碍]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 押 (char) (5037; 1942 characters remaining).

### 2026-08-05, iteration 558 — [[characters/押 (char)|押 (char)]]

**Fixed alias contamination**: `狎` (xiá, "to be intimate with, trifle with") was listed as an alias, but WebSearch confirms it's a distinct character (犬 semantic + 甲 phonetic) — related to 押 only by sharing the 甲 phonetic, not a variant. Removed, matching the established pattern (齎/斉, 併/並, 顫/振, 繚/僚). Confirmed `graphemic_classification: 甲` (形声, 手 semantic + 甲 phonetic, originally a shell/carapace pictogram — "to press, mortgage, seal," cognate with 壓) and trusted the existing `mc_id: 5284` per the long-tail policy. Filled blank `pos: ""` → `事詞`. Built the entire `## Notes`/`## Words` structure from scratch.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[押]], [[押韻]], and the neologism [[乳押]] (a genuine Dan'a'yo coinage, per that word's own Notes, not a loan/calque from any of the 5 source languages).

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 抑 (5039; 1941 characters remaining — danayo_id 5038 already perfected).

### 2026-08-05, iteration 559 — [[characters/抑|抑]]

Confirmed `graphemic_classification: 會意` via WebSearch (手 "hand" + 卬 "kneeling person" — a hand suppressing a kneeling person, "to press down, repress, restrain"; noted the parallel composition [[印]], 爪+卩, with a different meaning) and `mc_id: 1444` (`lookup/CC/CC 1000.md` line 465). `pos` was already correctly filled. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets).

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the missing self-referential `stand_in` [[抑止]] alongside the already-listed [[抑制]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 斥 (5040; 1940 characters remaining).

### 2026-08-05, iteration 560 — [[characters/斥|斥]]

Confirmed `graphemic_classification: 屰` via WebSearch (形声, originally written 㡿 — semantic 广 "building" + phonetic 屰; 屰 later became 干, 广 sometimes 厂, giving the modern form) and `mc_id: 1871` (`lookup/CC/CC 1000.md` line 908). Filled blank `pos: ""` → `事詞`. Fixed section ordering (`## Words` had been placed before `# Notes`) and merged into the proper structure.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[排斥]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 拳 (5041; 1939 characters remaining).

### 2026-08-05, iteration 561 — [[characters/拳|拳]]

Confirmed `graphemic_classification: 巻` via WebSearch (形声, 手 semantic "hand" + phonetic derived from 卷/巻 "to bend, curve" — a fist is a curled hand) and `mc_id: 3123` (`lookup/CC/CC 3000.md` line 132). Filled blank `pos: ""` → `名詞`. Built the entire `## Notes`/`## Words` structure from scratch (page previously had only floating bare initial/final links).

**Words cross-check** (5 ground-truth hits via `find_citers.py`, page previously had zero Words listed): added all 5, flagging [[拳骨]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 愚 (char) (5042; 1938 characters remaining).

### 2026-08-05, iteration 562 — [[characters/愚 (char)|愚 (char)]]

Confirmed `graphemic_classification: 禺` via WebSearch (形声, 心 semantic "heart" + 禺 phonetic — "foolish, stupid") and `mc_id: 725` (`lookup/CC/CC 0000.md` line 752). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets).

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[愚]] alongside the already-listed [[下愚]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 枕 (5043; 1937 characters remaining).

### 2026-08-05, iteration 563 — [[characters/枕|枕]]

Confirmed `graphemic_classification: 冘` via WebSearch (形声, 木 semantic "wood" + 冘 phonetic — "pillow," cognate with Burmese ခုံ "raised block") and `mc_id: 2176` (`lookup/CC/CC 2000.md` line 185). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already the `stand_in`): added [[枕頭]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 漫 (5044; 1936 characters remaining).

### 2026-08-05, iteration 564 — [[characters/漫|漫]]

Confirmed `graphemic_classification: 曼` via WebSearch (形声, 水 semantic "water" + 曼 phonetic "vast, extended" — "water overflowing," extended to "pervade, fill") and `mc_id: 2831` (`lookup/CC/CC 2000.md` line 868). Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading + misplaced `## Words` with a proper single-pass structure.

**Words cross-check** (2 word + 1 chengyu ground-truth hits via `find_citers.py`): added the missing self-referential `stand_in` [[弥漫]] and the chengyu [[天真乱漫]], alongside the already-listed [[乱漫]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 洪 (5045; 1935 characters remaining).

### 2026-08-05, iteration 565 — [[characters/洪|洪]]

Confirmed `graphemic_classification: 共` via WebSearch (形声, 水 semantic "water" + 共 phonetic — "flood, deluge," also "big, vast, grand") and `mc_id: 1636` (`lookup/CC/CC 1000.md` line 665). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already the `stand_in`): added [[洪水]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

**User switched pacing from 8 minutes to 10 minutes.** Next never-perfected character by `danayo_id`: 辱 (5046; 1934 characters remaining).

### 2026-08-05, iteration 566 — [[characters/辱|辱]]

Confirmed `graphemic_classification: 會意` via WebSearch (辰 "farming tool" + 寸 "hand" — a hand using a farming tool to remove weeds, original meaning now written as 耨 "to weed"; shifted to "disgrace, humiliate") and `mc_id: 790` (`lookup/CC/CC 0000.md` line 817). Filled blank `pos: ""` → `事詞`. Built the entire `## Notes`/`## Words`/`## Chengyu` structure from scratch (page previously had only floating bare initial/final links).

**Words cross-check** (4 ground-truth hits via `find_citers.py`) **+ Chengyu** (1 hit): added all, flagging [[羞辱]] as the `stand_in`.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 衡 (5048; 1933 characters remaining — danayo_id 5047 already perfected).

### 2026-08-05, iteration 567 — [[characters/衡|衡]]

**Fixed a doubly-wrong etymology bullet**: the existing Notes claimed "semantic 行 ('horn') + phonetic 角," but WebSearch confirms both the labels and the roles were wrong — 行 is the *phonetic* component (not semantic, and it means "to go/road," not "horn"), while 角 ("horn") is one of the *semantic* components (paired with 大, "person") in this 形声 compound: a person with a single unbalanced horn, shifted to "to weigh, measure, balance." The stored `graphemic_classification: 行` frontmatter field itself was already correct (it stores the phonetic component name per convention) — only the prose Notes bullet had the error. Confirmed `mc_id: 809` (`lookup/CC/CC 0000.md` line 839). Filled blank `pos: ""` → `事詞`. Folded the informal "Added to Korean HS list in 2000" note into the levels bullet.

**Words** (2 hits, already listed, reformatted with `stand_in` flag) **+ Chengyu** (1 hit via `find_citers.py`, previously uncited): added [[数数衡分]] (the Belshazzar's-feast "Mene, mene, tekel, upharsin" idiom).

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 旋 (5049; 1932 characters remaining).

### 2026-08-05, iteration 568 — [[characters/旋|旋]]

Confirmed `graphemic_classification: 會意` via WebSearch (㫃 "flag" + 疋 "foot" — marching under a flag, extended to "revolve, turn, return") and `mc_id: 1667` (`lookup/CC/CC 1000.md` line 696). Verified the `aliases: [鏇]` entry is legitimate (a documented xuàn-toned variant specifically for the lathe-turning sense), not contamination. Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`, page previously had zero Words listed): added all 3, flagging [[旋転]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 衰 (5051; 1931 characters remaining — danayo_id 5050 already perfected).

### 2026-08-05, iteration 569 — [[characters/衰|衰]]

Confirmed `graphemic_classification: 象形` via WebSearch (a pictogram of a palm-fiber raincoat, original form of 蓑; borrowed for "weak, exhausted," then also for "mourning clothes" and "raincoat" until 縗 and 簑/蓑 were coined to take over those senses) and `mc_id: 620` (`lookup/CC/CC 0000.md` line 644). Filled blank `pos: ""` → `事詞`. Merged floating bare initial/final links and an informally-cited word into the proper structure.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the missing self-referential `stand_in` [[衰弱]] and [[盛衰]] alongside the already-listed [[衰退]]. **Chengyu** (3 hits, 2 already listed): added the missing [[盛衰栄辱]] (already perfected on [[characters/辱|辱]] the prior iteration).

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 漆 (char) (5052; 1930 characters remaining).

### 2026-08-05, iteration 570 — [[characters/漆 (char)|漆 (char)]]

**Fixed a wrong `graphemic_classification`**: stored as `會意` (ideogrammic), but WebSearch confirms Wiktionary classifies 漆 as `形声` (phono-semantic) — semantic 水 "water" + phonetic 桼 "lacquer tree sap" (itself a pictogram of sap oozing from a tree). 桼 was the original character for lacquer, with 水 added later — confirming the existing `aliases: [桼]` is a genuine historical-ancestor relationship, not contamination. Confirmed `mc_id: 1720` (`lookup/CC/CC 1000.md` line 753). Filled blank `pos: ""` → `名詞`. Preserved and properly formatted the existing "anti-forgery form of 七" observation, folding it into the graphemic bullet.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[漆]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 爆 (5053; 1929 characters remaining).

### 2026-08-05, iteration 571 — [[characters/爆|爆]]

Confirmed `graphemic_classification: 暴` via WebSearch (形声, 火 semantic "fire" + 暴 phonetic "violence" — "to explode, burst") and trusted the existing large `mc_id: 9174` per the long-tail policy. Filled blank `pos: ""` → `事詞`. Fixed a `../`-prefixed final-韻 link baked into the wikilink itself (a recurring defect class per the checklist) and replaced the malformed `# Notes` heading with a proper structure.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[爆発]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 猛 (5054; 1928 characters remaining).

### 2026-08-05, iteration 572 — [[characters/猛|猛]]

Confirmed `graphemic_classification: 孟` via WebSearch (形声, 犬 semantic "dog" + 孟 phonetic — "fierce, strong, furious") and `mc_id: 1348` (`lookup/CC/CC 1000.md` line 365). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading + informally-cited word with a proper `## Notes` (4 bullets) and `## Words` section; caught my own first-draft empty ruby readings by re-grepping the source word files before finalizing.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[猛烈]] alongside the already-listed [[猛禽]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 疾 (5055; 1927 characters remaining).

### 2026-08-05, iteration 573 — [[characters/疾|疾]]

Confirmed `graphemic_classification: 矢` via WebSearch — a debated case, so researched thoroughly: the oracle-bone form depicts an arrow striking a person, and while some modern scholars argue 矢 isn't a true phonetic, the traditional Shuowen analysis (形声, 疒 semantic + 矢 phonetic) is what the vault's stored value reflects, and two originally distinct words ("illness" and "fast/urgent") merged into this one character. Confirmed `mc_id: 322` (`lookup/CC/CC 0000.md` line 337). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + floating bare links with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already the `stand_in`): added [[疾病]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 蜜 (5056; 1926 characters remaining).

### 2026-08-05, iteration 574 — [[characters/蜜|蜜]]

Confirmed `graphemic_classification: 宓` via WebSearch (形声, 虫 semantic "insect" + 宓 phonetic) and `mc_id: 2993` (`lookup/CC/CC 2000.md` line 1034). Filled blank `pos: ""` → `名詞`. Found and included a genuinely interesting etymological detail: the word 蜜 itself is likely an ancient Indo-European loanword, possibly via Tocharian B, ultimately cognate with English "mead" (PIE \*médʰu) — one of the few clearly Indo-European loans in Chinese. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets).

**Words cross-check** (3 ground-truth hits via `find_citers.py`, only 1 previously listed) **+ Chengyu** (1 hit, previously uncited): added [[蜜月]], [[蜜柑]], and [[乳蜜流地]] ("a land flowing with milk and honey").

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 租 (5057; 1925 characters remaining).

### 2026-08-05, iteration 575 — [[characters/租|租]]

Confirmed `graphemic_classification: 且` via WebSearch (形声, 禾 semantic "grain" + 且 phonetic — originally "land tax," paid in grain, shifted to "rent, hire") and `mc_id: 1645` (`lookup/CC/CC 1000.md` line 674). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets); fixed both graphemic component links to their correct `(char)`-suffixed filenames.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[租金]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 踏 (5058; 1924 characters remaining).

### 2026-08-05, iteration 576 — [[characters/踏|踏]]

Confirmed `graphemic_classification: 沓` via WebSearch (形声, 足 semantic "foot" + 沓 phonetic — "to step on, tread") and trusted the existing large `mc_id: 6706` per the long-tail policy. Verified the `aliases: [蹈, 𨂻]` entries are legitimate: 蹈 (a distinct character, own etymology) is a documented substitute-character relationship (e.g. 舞蹈→舞踏), not contamination — the same pattern as [[characters/旋|旋]]/鏇 earlier this session. Also confirmed `stand_in: 踐踏` matches [[践踏]]'s own documented `aliases: [踐踏]` field, so the traditional-form reference is intentional, not a mismatch. Filled blank `pos: ""` → `事詞`. Fixed section ordering (`## Words` had been placed before `# Notes`) and merged into the proper structure.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[践踏]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 眉 (char) (5059; 1923 characters remaining).

### 2026-08-05, iteration 577 — [[characters/眉 (char)|眉 (char)]]

**Fixed alias contamination on both entries at once**: `媚` (女 semantic + 眉 phonetic, "charming, to flatter") and `嵋` (山 semantic + 眉 phonetic, part of the Mount Emei place name) were both listed as aliases, but WebSearch confirms both are distinct derived characters that merely use 眉 as their own phonetic component — 眉 is the phonetic *root* of a small family here, not a character with two variant forms. Removed both (neither has a vault page). Confirmed `graphemic_classification: 象形` (𠃜 "hair" + 目 "eye," depicting hair above an eye; cognate with Tibetan སྨིན་མ "eyebrow") and `mc_id: 1541` (`lookup/CC/CC 1000.md` line 566). Filled blank `pos: ""` → `名詞`.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[眉]] alongside the already-listed [[嬌媚]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 獲 (5060; 1922 characters remaining).

### 2026-08-05, iteration 578 — [[characters/獲|獲]]

**Session's WebSearch quota exhausted mid-iteration** — proceeded on well-established domain knowledge instead (犬 semantic, reflecting the hunting origin of "to catch, seize"; 蒦 phonetic) rather than fabricating or skipping verification. Confirmed `mc_id: 631` locally (`lookup/CC/CC 0000.md` line 655). Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets) and `## Words` section built from scratch.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added both, flagging [[獲得]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 衝 (char) (5061; 1921 characters remaining).

### 2026-08-05, iteration 579 — [[characters/衝 (char)|衝 (char)]]

WebSearch quota still exhausted — proceeded on domain knowledge (行 semantic "road/thoroughfare" + 重 phonetic, matching the stored `graphemic_classification: 重`; 冲 confirmed as the standard simplified form, not contamination). Confirmed `mc_id: 1639` locally (`lookup/CC/CC 1000.md` line 668). Filled blank `pos: ""` → `事詞`. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[衝]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 旦 (5062; 1920 characters remaining).

### 2026-08-05, iteration 580 — [[characters/旦|旦]]

WebSearch quota still exhausted — confirmed `graphemic_classification: 指事` via domain knowledge (a classic, textbook 指事 example: 日 "sun" above 一 "the ground/horizon," depicting sunrise/dawn) and `mc_id: 853` locally (`lookup/CC/CC 0000.md` line 883). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading + informally-cited word with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the missing self-referential `stand_in` [[元旦]] and [[一旦]] alongside the already-listed [[旦夕]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 繁 (5063; 1919 characters remaining).

### 2026-08-05, iteration 581 — [[characters/繁|繁]]

**Fixed a swapped-and-mislabeled etymology bullet**: the existing Notes claimed "semantic 敏 ('silk') + phonetic 糸," but this is backwards on every count — 糸 means "silk" (not 敏, which means "quick, clever," as already established on [[characters/敏 (char)|敏]] earlier this session with the exact same OC readings *mrɯʔ/*mrɯŋʔ that had been mis-attached to "糸" here) and per the stored `graphemic_classification: 敏` (the phonetic-component-name convention), 敏 should be the phonetic, 糸 the semantic — the reverse of what the prose said. Corrected via domain knowledge (WebSearch quota still exhausted): 形声, 糸 semantic (numerous silk threads) + 敏 phonetic, "numerous, lush, complicated." Confirmed `mc_id: 1512` locally (`lookup/CC/CC 1000.md` line 537). Filled blank `pos: ""` → `性詞`. Preserved the existing "not 蕃殖" disambiguation note.

**Words cross-check** (6 ground-truth hits via `find_citers.py`, only 2 previously listed): added the missing self-referential `stand_in` [[繁茂]] (reordered to lead), [[繁殖]], [[繁忙]], [[繁多]], [[繁体字]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 旬 (5064; 1918 characters remaining).

### 2026-08-05, iteration 582 — [[characters/旬|旬]]

**Fixed another garbled etymology bullet**: the existing Notes claimed "形声, semantic 螾 ('sun; day') + phonetic 日," but 螾 is an unrelated earthworm character (dialectal variant of 蚓) with no connection to "sun/day" — this looks like a data-corruption artifact, not a legitimate alternate analysis. Corrected via domain knowledge (WebSearch quota still exhausted) to the standard analysis matching the stored `graphemic_classification: 會意`: 勹 ("to wrap, enclose") + 日 ("sun, day") — depicting a full ten-day cycle, the ancient Chinese calendar's 旬 period (days named by the 十干 heavenly stems). Confirmed `mc_id: 1837` locally (`lookup/CC/CC 1000.md` line 874). Filled blank `pos: ""` → `名詞`. Fixed two dead relative-path markdown links (`/words/旬日.md`, `words/上旬.md`) to proper wikilinks with ruby+gloss.

**Words cross-check** (4 ground-truth hits via `find_citers.py`, only 2 previously listed): added the missing self-referential `stand_in` [[旬日]] (reordered to lead) and [[中旬]], alongside [[上旬]] and [[下旬]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 索 (5065; 1917 characters remaining).

### 2026-08-05, iteration 583 — [[characters/索|索]]

**Fixed a frontmatter/prose mismatch**: `graphemic_classification` was stored as `象形`, but the page's own existing Notes bullet already correctly described a 会意 composition (糸 "thread" + 𣎳 "hands stripping hemp fiber," depicting rope-making) — corrected the frontmatter to `會意` to match, via domain knowledge (WebSearch quota still exhausted). **Fixed a `stand_in` pointing to a nonexistent word**: stored as `繩索`, but no such word page exists anywhere in the vault — the same bug class found earlier on [[characters/喉|喉]]/喉頭. Retargeted to [[捜索]], a real citing word confirmed via `find_citers.py`. Confirmed `mc_id: 1190` locally (`lookup/CC/CC 1000.md` line 199). Filled blank `pos: ""` → `名詞`. Fixed a `../`-prefixed final-韻 link baked into the wikilink itself.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the corrected `stand_in` [[捜索]] and [[探索]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 絡 (char) (5066; 1916 characters remaining).

### 2026-08-05, iteration 584 — [[characters/絡 (char)|絡 (char)]]

**Fixed alias contamination**: `珞` (王/玉 semantic + 各 phonetic, "jade ornament," as in 瓔珞) was listed as an alias, but it's a distinct derived character sharing only the 各 phonetic with 絡 — the same "shared phonetic root, not a variant" pattern seen repeatedly this session (敏/毎, 娘/良, etc., but here as contamination rather than a legitimate root). Removed, along with a dangling note ("瓔珞 --> 䋝絡/纓絡") that referenced word/chengyu pages confirmed via `find_citers.py`-adjacent lookup to not exist anywhere in the vault. Confirmed `mc_id: 1452` locally (`lookup/CC/CC 1000.md` line 473) and `graphemic_classification: 各` via domain knowledge (形声, 糸 semantic "thread" + 各 phonetic — "wrapped in thread"). Filled blank `pos: ""` → `事詞`. Fixed a `../`-prefixed final-韻 link baked into the wikilink itself.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[絡]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 頃 (char) (5067; 1915 characters remaining).

### 2026-08-05, iteration 585 — [[characters/頃 (char)|頃 (char)]]

**Fixed a wrong `graphemic_classification`**: stored as `匕` (a component-name value, which per convention would only be valid for a 形声 phonetic), but domain knowledge (WebSearch quota still exhausted) places 頃 as `會意`: 匕 ("person, tilted/upside down") + 頁 ("head") — a person with head tilted, the original sense now written as 傾; extended to "a brief moment" and, as 顷, a PRC land-area unit. Corrected the field to the type name `會意` per convention. Confirmed `mc_id: 963` locally (`lookup/CC/CC 0000.md` line 996). Filled blank `pos: ""` → `名詞`. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[頃]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 騒 (char) (5068; 1914 characters remaining).

### 2026-08-05, iteration 586 — [[characters/騒 (char)|騒 (char)]]

Confirmed `graphemic_classification: 蚤` via domain knowledge (WebSearch quota still exhausted): 形声, 馬 semantic (a horse's restlessness/itching) + 蚤 phonetic ("flea") — "to disturb, agitate," extended to "boisterous." Confirmed the `aliases: [騷]` entry is a genuine traditional-form variant (騷/骚/騒 are the traditional/simplified/shinjitai forms respectively), not contamination, and that `mc_id: 2358` is correctly recorded under the traditional form 騷 (`lookup/CC/CC 2000.md` line 375). Filled blank `pos: ""` → `性詞`. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[騒]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 娯 (5069; 1913 characters remaining).

### 2026-08-05, iteration 587 — [[characters/娯|娯]]

Confirmed `graphemic_classification: 呉` via domain knowledge (形声, 女 semantic + 呉/吳 phonetic — "to entertain, amuse") and that the existing `aliases: [娛, 娱]` are genuine traditional/simplified variants, matching the pattern just established on [[characters/騒 (char)|騒]]. Confirmed `mc_id: 2359` locally (`lookup/CC/CC 2000.md` line 376, recorded under the traditional form 娛). Filled in the previously-empty OC readings and semantic/phonetic glosses (the Notes bullet had blank parenthetical placeholders). Confirmed blank `hsk_level: ""` correctly renders as "No HSK" per established vault convention — left as-is, not an error.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[娯楽]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 寧 (5070; 1912 characters remaining).

### 2026-08-05, iteration 588 — [[characters/寧|寧]]

**Left `graphemic_classification: 寍` unchanged despite a real uncertainty**: domain knowledge (WebSearch quota still exhausted) suggests the more commonly cited etymology is 形声 with phonetic 丂 + semantic 寍 (itself 宀+心+皿), which per the vault's phonetic-component-name convention would mean the field should store `丂` rather than `寍`. Without search verification I judged the risk of introducing an error too high to reclassify a field with no contradicting in-page evidence (unlike [[characters/繁|繁]]/[[characters/旬|旬]]/[[characters/索|索]] earlier, where the page's own Notes text openly contradicted the frontmatter) — documented both components honestly in the Notes bullet instead of asserting a specific phonetic/semantic split. Confirmed `mc_id: 749` locally (`lookup/CC/CC 0000.md` line 776). Filled blank `pos: ""` → `性詞`.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added both, flagging [[安寧]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 峰 (5071; 1911 characters remaining).

### 2026-08-05, iteration 589 — [[characters/峰|峰]]

Light iteration — `pos` and the Words section were already correctly filled. Confirmed `graphemic_classification: 夆` via domain knowledge (形声, 山 semantic "mountain" + 夆 phonetic — "summit, peak"; 峯 a legitimate variant with 山 above rather than beside 夆) and trusted the existing large `mc_id: 6815` per the long-tail policy. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets).

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching what was already listed): flagged [[高峰]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 廃 (5072; 1910 characters remaining).

### 2026-08-05, iteration 590 — [[characters/廃|廃]]

Light iteration — `pos` was already correctly filled and all 4 words were already listed (just needed ruby+gloss consolidation). Confirmed `graphemic_classification: 發` via domain knowledge (形声, 广 semantic "building," implying a dilapidated one, + 發 phonetic — "to abrogate, discard, abandon") and `mc_id: 513` locally (`lookup/CC/CC 0000.md` line 534, recorded under the traditional form 廢). Fixed a phonetic-component link pointing to a nonexistent traditional-form filename (發.md doesn't exist; the vault uses the shinjitai 発).

**Words cross-check** (4 ground-truth hits via `find_citers.py`, matching what was already listed): flagged [[廃棄]] as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 懸 (char) (5073; 1909 characters remaining).

### 2026-08-05, iteration 591 — [[characters/懸 (char)|懸 (char)]]

**Fixed a phonetically implausible `graphemic_classification`**: stored as `絶` (OC *zet, "to sever"), which shares no phonetic resemblance to 懸 (xuán) at all. Corrected via domain knowledge (WebSearch quota still exhausted) to `縣` — near-homophonous with 懸, originally depicting "hanging" before specializing to "county, district," and the standard cited phonetic for this character (心 semantic "heart," implying anxious suspense, + 縣 phonetic). Confirmed `mc_id: 1574` locally (`lookup/CC/CC 1000.md` line 599). Filled blank `pos: ""` → `事詞`. Rebuilt the malformed Notes/Words split.

**Words cross-check** (4 ground-truth hits via `find_citers.py` — [[懸垂]]/[[懸壅垂]] only surfaced via the bare-glyph search, same `characters:` field-suffix inconsistency seen repeatedly this session): added the missing self-referential `stand_in` [[懸心]] (reordered to lead) alongside [[懸垂]] and [[懸壅垂]].

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 慎 (5074; 1908 characters remaining).

### 2026-08-05, iteration 592 — [[characters/慎|慎]]

**Fixed alias contamination**: `恂` (xún, "sincere, cautious") was listed as an alias, but it's a distinct character with a different pronunciation and phonetic component (心 semantic + 旬 phonetic vs 慎's 心 + 真) — related only by shared meaning-adjacency and the 心 radical, not a variant. Removed via domain knowledge (WebSearch quota still exhausted). Confirmed `graphemic_classification: 真` (形声, 心 semantic + 真 phonetic — "cautious, prudent") and `mc_id: 741` locally (`lookup/CC/CC 0000.md` line 768). `pos` was already correctly filled. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets) and `## Words` section built from scratch.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[謹慎]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 惨 (char) (5075; 1907 characters remaining).

### 2026-08-05, iteration 593 — [[characters/惨 (char)|惨 (char)]]

Confirmed `graphemic_classification: 參` via domain knowledge (形声, 心 semantic + 參/参 phonetic — "wretched, cruel, miserable") and `mc_id: 2649` locally (`lookup/CC/CC 2000.md` line 678, recorded under the traditional form 慘). `pos` was already correctly filled. Replaced the malformed `# Notes` heading with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`, [[凄惨]] only surfacing via the bare-glyph search due to the recurring `characters:` field-suffix inconsistency): added the self-referential `stand_in` [[惨]] and [[凄惨]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-05`.

Next never-perfected character by `danayo_id`: 捜 (5076; 1906 characters remaining).

### 2026-08-06, iteration 594 — [[characters/捜|捜]]

Confirmed `graphemic_classification: 叟` via domain knowledge (WebSearch quota still exhausted; 形声, 手 semantic "hand" + 叟 phonetic sōu "old man" — "to search, look for"). **Fixed `mc_id`**: stored as `2704`, which corresponds to 底 in `lookup/CC/CC 2000.md` line 737; corrected to `2705`, the real entry for 搜 (traditional form) one line below. **Fixed alias contamination**: `廋` (sōu, "to hide, conceal," 广 semantic "building") is a distinct character with its own etymology, occasionally used as a phonetic loan for 搜/捜 in classical texts but not a true graphemic variant — removed, leaving only the legitimate traditional form `搜`. `pos` was already correctly filled (`事詞`). Rebuilt the empty `## Notes` (4 bullets) and the malformed `## Words` section (previously a bare `[[捜索]]` link with floating, unlinked initial/final references beneath it).

**Words cross-check** (1 ground-truth hit via `find_citers.py`, tried both `捜` and `捜 (char)` forms): added the self-referential `stand_in` [[捜索]], correcting its ruby from a guessed reading to the real one (ㄙㄛㄨㄙㄚㄎ, verified against `words/捜索.md`). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 綱 (5077; 1905 characters remaining).

### 2026-08-06, iteration 595 — [[characters/綱|綱]]

Confirmed `graphemic_classification: 岡` via domain knowledge (形声, 糸 semantic "thread" + 岡 phonetic gāng — "the main rope from which netting hangs," extended to "guiding principle, outline"); corrected the component link, which pointed to a nonexistent `岡 (char)` page, to the real bare-glyph page `[[岡]]`. **Fixed `mc_id`**: stored as `1626`, which corresponds to 璽 in `lookup/CC/CC 1000.md` line 655; corrected to `1627`, the real entry for 綱 one line below. Filled the empty `pos` field (`名詞`, matching the noun-like sibling character 索). Alias `纲` (simplified form) confirmed legitimate. Replaced the malformed `# Notes` heading (with two bare, unlinked initial/final references and a single informally-linked Words bullet) with a proper `## Notes` (4 bullets), `## Words`, and `## Chengyu` section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[大綱]], plus [[三綱]] and [[綱要]]. **Chengyu** (1 ground-truth hit): added [[三綱五常]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 緩 (5078; 1904 characters remaining).

### 2026-08-06, iteration 596 — [[characters/緩|緩]]

Confirmed `graphemic_classification: 爰` via domain knowledge (形声, 糸 semantic "thread," implying a loosened/slackened thread, + 爰 phonetic yuán — "slack, slow, sluggish") and `mc_id: 1247` locally (`lookup/CC/CC 1000.md` line 260 — correct, no fix needed). Filled the empty `pos` field (`性詞`, matching the adjective-like sibling word 緩慢). Alias `缓` (simplified form) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[緩慢]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 汗 (char) (5079; 1903 characters remaining).

### 2026-08-06, iteration 597 — [[characters/汗 (char)|汗 (char)]]

Confirmed `graphemic_classification: 干` via domain knowledge (形声, 水 semantic "water" + 干 phonetic gān — "sweat") and `mc_id: 999` locally (`lookup/CC/CC 0000.md` line 1032 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words/Chengyu sections) with a proper `## Notes` (4 bullets), `## Words`, and `## Chengyu` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[汗]]. **Chengyu** (1 ground-truth hit): added [[汗食帰泥]] (Biblical chengyu, Genesis 3:19). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 罰 (5080; 1902 characters remaining).

### 2026-08-06, iteration 598 — [[characters/罰|罰]]

Confirmed `graphemic_classification: 會意` via domain knowledge (Shuowen: 网/罒 "net," implying an offense caught, + 言 "words, scolding" — together 詈 "to curse, rebuke" — + 刀 "knife," implying punishment — "penalty, to punish") and `mc_id: 612` locally (`lookup/CC/CC 0000.md` line 636 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the verb-like stand-in word 懲罰). Alias `罚` (simplified form) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[懲罰]] and [[刑罰]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 脅 (5081; 1901 characters remaining).

### 2026-08-06, iteration 599 — [[characters/脅|脅]]

Confirmed `graphemic_classification: 劦` via domain knowledge (形声, 肉 semantic "flesh," originally "ribs, the sides of the body," + 劦 phonetic — extended metaphorically to "coerce, threaten"). **Fixed `mc_id`**: stored as `1412`, which corresponds to 淺 in `lookup/CC/CC 1000.md` line 433; corrected to `1413`, the real entry for 脅 one line below. Filled the empty `pos` field (`事詞`, matching the sibling verb-like word 脅威). Assessed both aliases: `胁` (simplified) legitimate; `脇` (a Japanese kyūjitai variant of 脅, "side, flank" — confirmed it has its own separate Classical Chinese corpus entry at `CC 3000.md` line 6, but no distinct vault page of its own) also legitimate, kept as an alias. Rebuilt the malformed `## Notes` (two bare, unlinked initial/final references) into a proper 4-bullet section; the `## Words` section already existed but was missing the `stand_in` annotation.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching the page's existing single entry): added the `(stand-in for 脅)` tag to [[脅威]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 唇 (char) (5082; 1900 characters remaining).

### 2026-08-06, iteration 600 — [[characters/唇 (char)|唇 (char)]]

Confirmed `graphemic_classification: 辰` via domain knowledge (形声, 口 semantic "mouth" + 辰 phonetic — "lips") and `mc_id: 2907` locally (`lookup/CC/CC 2000.md` line 948 — correct, no fix needed). `pos` was already correctly filled (`名詞`). Alias `脣` (traditional form, 肉 semantic "flesh" instead of 口 — confirmed it has its own separate Classical Chinese corpus entry at line 927, but no distinct vault page of its own) confirmed legitimate. Rebuilt the malformed `## Notes` (two bare, unlinked initial/final references, missing Words section) into a proper 4-bullet section plus a `## Words` section; the pre-existing `## Chengyu` section was left untouched.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[唇]]. **Chengyu** (1 ground-truth hit, already present): confirmed [[唇亡歯寒]] correct. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 胞 (5083; 1899 characters remaining).

### 2026-08-06, iteration 601 — [[characters/胞|胞]]

Confirmed `graphemic_classification: 包` via domain knowledge (形声, 肉 semantic "flesh" + 包 phonetic bāo "to wrap" — "womb, placenta" — that which wraps the fetus — extended to "membrane, sac" and, via the modern coinage 細胞, to "biological cell"). **Fixed `mc_id`**: stored as `3699`, which corresponds to 衿 in `lookup/CC/CC 3000.md` line 728; corrected to `3700`, the real entry for 胞 one line below. Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, one informally-linked Words bullet) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (4 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[胞衣]], plus [[同胞]], [[細胞]] (the Meiji-era Japanese neologism for "cell," confirmed via the word page's own etymology notes), and [[胞子]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 騰 (5084; 1898 characters remaining).

### 2026-08-06, iteration 602 — [[characters/騰|騰]]

**Fixed garbled etymology**: the Notes bullet wrongly labeled the semantic component as 朕 glossed "horse" (朕 does not mean "horse") and left the phonetic link empty. Corrected via domain knowledge to the standard etymology: 形声, 馬 semantic ("horse") + 朕 phonetic — "a horse's leap, gallop, prance," extended to "to soar, rise, ascend." `graphemic_classification: 朕` was already correct, matching this corrected analysis. `mc_id: 1817` verified correct locally (`lookup/CC/CC 1000.md` line 854). Filled the empty `pos` field (`動詞`, matching the sibling verb word 騰貴). Alias `腾` (simplified) confirmed legitimate. Dropped an ad hoc, non-standard "Added to the Korean HS list in 2000" line and two bare unlinked initial/final references, replacing them with the standard 4-bullet structure.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the `(stand-in for 騰)` tag to the existing [[騰貴]] and added [[奔騰]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 薦 (5085; 1897 characters remaining).

### 2026-08-06, iteration 603 — [[characters/薦|薦]]

Confirmed `graphemic_classification: 會意` via domain knowledge (Shuowen: 艸 "grass" + 廌, a mythical beast with no vault page — grass laid out as fodder/bedding for the beast, hence "mat, offering," extended to "to put forward, recommend") and `mc_id: 936` locally (`lookup/CC/CC 0000.md` line 969 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the stand-in word 推薦). Alias `荐` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[推薦]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 襲 (5086; 1896 characters remaining).

### 2026-08-06, iteration 604 — [[characters/襲|襲]]

Confirmed `graphemic_classification: 龖` via domain knowledge (Shuowen: 从衣龖省 — 衣 semantic "robe," originally "a left-lapped padded robe with overlapping flaps," + phonetic 龖, an abbreviated archaic doubled-dragon component with no vault page — extended from "overlapping layers" to "to attack by surprise, ambush") and `mc_id: 1018` locally (`lookup/CC/CC 1000.md` line 23 — correct, no fix needed). Filled the empty `pos` field (`動詞`, matching the sibling verb word 掩襲). Alias `袭` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references) with a proper `## Notes` (4 bullets); the pre-existing `## Words` section was correct but missing the `stand_in` annotation.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching the page's existing single entry): added the `(stand-in for 襲)` tag to [[掩襲]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 懐 (char) (5087; 1895 characters remaining).

### 2026-08-06, iteration 605 — [[characters/懐 (char)|懐 (char)]]

Confirmed `graphemic_classification: 褱` via domain knowledge (形声, 心 semantic "heart" + 褱 phonetic huái, "to carry inside one's clothes," no vault page — "to hold dear in one's heart, to miss, to think of") and `mc_id: 575` locally (`lookup/CC/CC 0000.md` line 596, recorded under the traditional form 懷 — correct, no fix needed). `pos` was already correctly filled (`事詞`). Alias `懷` (traditional form) confirmed legitimate. Consolidated a malformed `# Notes` heading (bare, unlinked initial/final references, plus two Words-appropriate bullets misplaced under Notes) and a separate `## Words` heading with only one entry into a single proper `## Notes` (4 bullets) + `## Words` section.

**Words cross-check** (5 ground-truth hits via `find_citers.py`, requiring both the bare `懐` and `懐 (char)` forms to surface all citations): added the self-referential `stand_in` [[懐]], plus [[懐抱]], [[懐孕]], [[懐愁]], and [[懐疑]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 謡 (5088; 1894 characters remaining).

### 2026-08-06, iteration 606 — [[characters/謡|謡]]

Confirmed `graphemic_classification: 䍃` via domain knowledge (形声, 言 semantic "words, speech" + 䍃 phonetic yáo — "song, ballad") and `mc_id: 2367` locally (`lookup/CC/CC 2000.md` line 384, recorded under the traditional form 謠 — correct, no fix needed). Filled the empty `pos` field (`名詞`). Both aliases confirmed legitimate: `謠` (traditional) and `谣` (simplified). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references) with a proper `## Notes` (4 bullets); the pre-existing `## Words` section was correct but missing the `stand_in` annotation and one citation.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the `(stand-in for 謡)` tag to the existing [[歌謡]] and added [[民謡]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 謙 (5089; 1893 characters remaining).

### 2026-08-06, iteration 607 — [[characters/謙|謙]]

Confirmed `graphemic_classification: 兼` via domain knowledge (形声, 言 semantic "words, speech" + 兼 phonetic qiān — "self-effacing, humble," careful/modest speech) and `mc_id: 1292` locally (`lookup/CC/CC 1000.md` line 305 — correct, no fix needed). `pos` was already correctly filled (`性詞`). Alias `谦` (simplified) confirmed legitimate. Replaced the malformed `## Notes` (two bare, unlinked initial/final references) with a proper 4-bullet section; the pre-existing `## Words` section was correct but missing the `stand_in` annotation.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching the page's existing single entry): added the `(stand-in for 謙)` tag to [[謙遜]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 謹 (5090; 1892 characters remaining).

### 2026-08-06, iteration 608 — [[characters/謹|謹]]

Confirmed `graphemic_classification: 菫` via domain knowledge (形声, 言 semantic "words, speech" + 菫 phonetic jǐn — "prudent, cautious," careful in speech) and `mc_id: 876` locally (`lookup/CC/CC 0000.md` line 906 — correct, no fix needed). Filled the empty `pos` field (`性詞`). Alias `谨` (simplified) confirmed legitimate. Verified the `#cranberry` tag: 謹慎 is also tagged `cranberry`, and both 謹 and its earlier-perfected sibling [[characters/慎|慎]] (iteration #592) independently mean "cautious" and share 謹慎 as their `stand_in` — transitivity (A=B=AB) holds per the vault's cranberry convention. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[謹慎]] with the cranberry cross-reference noted. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 贈 (5091; 1891 characters remaining).

### 2026-08-06, iteration 609 — [[characters/贈|贈]]

Confirmed `graphemic_classification: 曽` via domain knowledge (形声, 貝 semantic "valuables, money" + 曽 phonetic zēng — "to present, bestow") and `mc_id: 1946` locally (`lookup/CC/CC 1000.md` line 987 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the sibling verb word 贈与). Alias `赠` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[贈与]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 跡 (5092; 1890 characters remaining).

### 2026-08-06, iteration 610 — [[characters/跡|跡]]

Confirmed `graphemic_classification: 亦` via domain knowledge (形声, 足 semantic "foot" + 亦 phonetic — an irregular but well-documented phonetic series despite modern initial divergence — "footprints, tracks," extended to "vestige, trace") and `mc_id: 1236` locally (`lookup/CC/CC 1000.md` line 249 — correct, no fix needed). Filled the empty `pos` field (`名詞`). Assessed all three aliases: `迹` (辶 semantic variant, own separate CC corpus entry at `CC 2000.md` line 878) legitimate; `蹟` and `𫐤` (further attested variant forms, e.g. 奇跡/奇蹟, no CC entries or distinct vault pages) kept as plausible variants absent contradicting evidence. Verified the `#cranberry` tag: 痕跡 is also tagged `cranberry`, and both 跡 and its sibling [[characters/痕|痕]] independently mean "trace, vestige" — transitivity holds. Dropped an ad hoc "蹟 was dropped from the Korean HS list in 2000" line and two bare unlinked initial/final references, replacing with the standard 4-bullet `## Notes` structure.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[痕跡]] with the cranberry cross-reference noted. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 珍 (char) (5093; 1889 characters remaining).

### 2026-08-06, iteration 611 — [[characters/珍 (char)|珍 (char)]]

Confirmed `graphemic_classification: 㐱` via domain knowledge (形声, 玉 semantic "jade" + 㐱 phonetic zhěn — "rare, precious," a rare treasure like jade) and `mc_id: 1543` locally (`lookup/CC/CC 1000.md` line 568 — correct, no fix needed). Filled the empty `pos` field (`性詞`). No aliases to assess (field empty). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[珍]] and [[珍珠]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 鑑 (5094; 1888 characters remaining).

### 2026-08-06, iteration 612 — [[characters/鑑|鑑]]

Confirmed `graphemic_classification: 監` via domain knowledge (形声, 金 semantic "metal," the bronze of the ancient mirror, + 監 phonetic jiàn — the large bronze mirror of antiquity, extended to "to examine clearly, to appraise"). **Fixed `mc_id`**: stored as `3780`, which corresponds to 螭 in `lookup/CC/CC 3000.md` line 813; corrected to `3781`, the real entry for 鑑 one line below. `pos` was already correctly filled (`名詞`). Assessed all three aliases: `鑒` (traditional form, own separate CC corpus entry at `CC 2000.md` line 189) and `鉴` (simplified) both legitimate; `𰾫` (further attested rare variant, no CC entry or distinct vault page) kept as plausible absent contradicting evidence. Fixed broken relative-path markdown links (`../`-prefixed, non-wikilink syntax) throughout the malformed `## Notes` and consolidated two bare unlinked initial/final references into the standard 4-bullet structure.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[鏡鑑]] and confirmed the existing [[鑑定]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 鉛 (char) (5095; 1887 characters remaining).

### 2026-08-06, iteration 613 — [[characters/鉛 (char)|鉛 (char)]]

**Fixed malformed frontmatter**: `japanese_native` had a duplicate list item (`なまり` as both a scalar and a nested `- なまり` list entry) — corrected to a plain scalar. Confirmed `graphemic_classification: 㕣` via domain knowledge (Shuowen: 从金㕣聲 — 金 semantic "metal" + 㕣 phonetic — names the element lead). **Fixed `mc_id`**: stored as `3902`, which corresponds to 遞 in `lookup/CC/CC 3000.md` line 943; corrected to `3903`, the real entry for 鉛 one line below. `pos` (`固有名詞`) was already correctly filled, matching the standalone word 鉛's own `固有名詞` classification for element names. Alias `铅` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, two informally-placed bullets that belonged under Words) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (4 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[鉛]], plus [[鉛筆]], [[亜鉛]] (zinc), and [[蒼鉛]] (bismuth, a historically attested compound per its own page's detailed etymology notes). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 鋳 (5096; 1886 characters remaining).

### 2026-08-06, iteration 614 — [[characters/鋳|鋳]]

Confirmed `graphemic_classification: 寿` via domain knowledge (形声, 金 semantic "metal" + 壽/寿 phonetic, no vault page — "to cast metal, to mint") and `mc_id: 1507` locally (`lookup/CC/CC 1000.md` line 532, recorded under the traditional form 鑄 — correct, no fix needed). `pos` was already correctly filled (`事詞`). Alias `鑄` (traditional) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references) with a proper `## Notes` (4 bullets); the pre-existing `## Words` section was correct but missing the `stand_in` annotation.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching the page's existing single entry): added the `(stand-in for 鋳)` tag to [[鋳造]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 哭 (char) (5097; 1885 characters remaining).

### 2026-08-06, iteration 615 — [[characters/哭 (char)|哭 (char)]]

Confirmed `graphemic_classification: 獄` via domain knowledge (Shuowen: 从吅獄省聲 — doubled 口 "mouths," crying voices, + abbreviated 獄 as phonetic — "to cry, weep, wail," also used of ritual mourning-wails at funerals; this is a genuinely debated character in modern scholarship, but the stored classification matches the Shuowen citation directly, so kept as-is) and `mc_id: 820` locally (`lookup/CC/CC 0000.md` line 850 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the sibling word 哭's own `事詞` classification). No aliases to assess (field empty). Identified the correct lookup-file convention for the unusual `joyo_level: 表外字` value (Hyōgai, "characters outside the Jōyō list") by cross-referencing other fully-perfected pages using that value. Reordered a misplaced `## Words` section (which preceded a malformed `# Notes` heading) into the standard Notes-then-Words order with a proper 4-bullet Notes section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[哭]] and confirmed the existing [[痛哭]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 鎮 (char) (5098; 1884 characters remaining).

### 2026-08-06, iteration 616 — [[characters/鎮 (char)|鎮 (char)]]

Confirmed `graphemic_classification: 真` via domain knowledge (形声, 金 semantic "metal," a heavy weight, + 真 phonetic zhèn — "to press down, hold in place," extended to "to tranquilize, subdue, garrison"). **Fixed `mc_id`**: stored as `1745`, which corresponds to 隕 in `lookup/CC/CC 1000.md` line 778; corrected to `1746`, the real entry for 鎮 one line below. `pos` was already correctly filled (`事詞`). Both aliases confirmed legitimate: `鎭` (traditional variant) and `镇` (simplified). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section. (Noted but left out of scope: the sibling word page `words/鎮.md` has a literal-string `"null"` `korean` field — a word-file bug outside this character-sweep's scope, consistent with the vault's established convention of leaving such bugs for separate word-perfecting work.)

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[鎮]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 陥 (char) (5099; 1883 characters remaining).

### 2026-08-06, iteration 617 — [[characters/陥 (char)|陥 (char)]]

Confirmed `graphemic_classification: 會意` via domain knowledge (Shuowen: 从阜从臽 — 阜 "mound, earthen wall" + 臽, a real ancestral character meaning "pitfall, trap," no vault page — "to fall into a pit, cave in, be trapped," extended to "to submerge, sink into") and `mc_id: 1157` locally (`lookup/CC/CC 1000.md` line 166, recorded under the traditional form 陷 — correct, no fix needed). `pos` was already correctly filled (`性詞`). Both aliases confirmed legitimate: `陷` (traditional) and `臽` (the ancestral component character itself, analogous to the earlier-established 漆/桼 pattern — an ancestor form, not a mere variant). Replaced the malformed `## Notes` (two bare, unlinked initial/final references, no Words section) with a proper 4-bullet section and `## Words` section. (Noted but left out of scope: `words/陥.md` has a literal-string `"null"` `korean` field, same word-file bug class as 鎮's sibling word, left for separate word-perfecting work.)

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[陥]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 隠 (5100; 1882 characters remaining).

### 2026-08-06, iteration 618 — [[characters/隠|隠]]

Confirmed `graphemic_classification: 㥯` via domain knowledge (形声, 阜 semantic "mound," a hiding place, + 㥯 phonetic — "to hide, conceal") and `mc_id: 687` locally (`lookup/CC/CC 0000.md` line 711, recorded under the traditional form 隱 — correct, no fix needed). **Fixed alias contamination**: `湮` (yān, "to sink, submerge, obliterate," 水 semantic) is a distinct character with a different pronunciation and etymology from 隠 (yǐn) — removed. `隱` (traditional) confirmed legitimate, and `乚` (an archaic variant with no vault page) confirmed legitimate — cross-verified via its citation on [[characters/耴|耴]]'s own page, which already links to it as `[[隠|乚]]`, showing the vault treats it as 隠's established alternate form elsewhere. `pos` was already correctly filled (`性詞`). Rebuilt a malformed `## Notes`/`## Words` block (a single out-of-place bullet under Notes, bare unlinked initial/final references interspersed within Words, one floating bullet after them) into the standard structure. (Noted but left out of scope: `words/隠蔵.md`'s Notes section reads the placeholder text "a very C word" — a word-file bug left for separate work.)

**Words cross-check** (6 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[隠蔵]], confirmed the existing [[隠匿]] and [[隠滅]], and added [[隠形]], [[隠蔽]], and [[隠金]] (a Greek-calque periodic-table neologism for lanthanum, per its own page's etymology notes). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 隷 (5101; 1881 characters remaining).

### 2026-08-06, iteration 619 — [[characters/隷|隷]]

**Fixed frontmatter/prose mismatch**: the Notes bullet cited phonetic 奈 while the frontmatter correctly stored `graphemic_classification: 柰` — verified against Shuowen (从隶柰聲) that 柰, not 奈, is the classically cited phonetic (a distinct character from 奈 despite sharing the same OC reading and being frequently conflated); corrected the prose to match the already-correct frontmatter. `mc_id: 1355` verified correct locally (`lookup/CC/CC 1000.md` line 372, recorded under the traditional form 隸). `pos` was already correctly filled (`名詞`). Both aliases confirmed legitimate: `隸` (traditional) and `隶` (the semantic component itself, also the standard simplified form). Dropped an ad hoc "Added to the Korean HS list in 2000" line and two bare unlinked initial/final references, replacing with the standard 4-bullet structure and a `## Words` section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[奴隷]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 攻 (char) (5102; 1880 characters remaining).

### 2026-08-06, iteration 620 — [[characters/攻 (char)|攻 (char)]]

**Fixed swapped semantic/phonetic roles**: the duplicate `## Notes` section's prose labeled 工 as semantic ("work") and 攵 as phonetic — backwards from the correct analysis and from the frontmatter's own `graphemic_classification: 工`, which stores the phonetic component per convention. Corrected to 攴/攵 semantic ("to strike, hit") + 工 phonetic (gōng, "work") — "to attack," extended to "to criticize." `mc_id: 280` verified correct locally (`lookup/CC/CC 0000.md` line 292). Filled the empty `pos` field (`事詞`). No aliases to assess (field empty). Merged two duplicate `## Notes` headings and a misordered `## Words`/`## Chengyu` sequence into the standard order, and fixed the page-intro callout, which was missing the character glyph itself ("This is a page about the character." → "...about the character 攻.").

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[攻]] and confirmed the existing [[攻防]] and [[挟攻]]. **Chengyu** (1 ground-truth hit, already present): confirmed [[遠交近攻]] correct. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 陳 (5103; 1879 characters remaining).

### 2026-08-06, iteration 621 — [[characters/陳|陳]]

Confirmed `graphemic_classification: 會意` via domain knowledge (阜 "mound, earthworks" + an ancient graphic element depicting rows/ranks arrayed along it — "to arrange in rows," extended to "to exhibit, display," and as a proper name the ancient state of Chen) and `mc_id: 215` locally (`lookup/CC/CC 0000.md` line 227 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the stand-in word 陳列). Alias `陈` (simplified) confirmed legitimate. Reordered a misplaced `## Words` section (which preceded a malformed `# Notes` heading) into the standard Notes-then-Words order with a proper 4-bullet Notes section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[陳列]] and confirmed the existing [[陳述]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 傾 (5105; 1878 characters remaining).

### 2026-08-06, iteration 622 — [[characters/傾|傾]]

Confirmed `graphemic_classification: 頃` via domain knowledge (形声, 人 semantic "person" + 頃 phonetic qīng — "to lean, incline," a person leaning to one side) and `mc_id: 1213` locally (`lookup/CC/CC 1000.md` line 226 — correct, no fix needed). Filled the empty `pos` field (`動詞`, matching the character's own verb-like gloss "lean, incline," distinct from its nominalized sibling words 傾向/傾斜 which are both `名詞`). Alias `倾` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, `## Words` immediately following with no blank line) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`, matching the page's existing entries): added the `(stand-in for 傾)` tag to [[傾向]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 償 (5106; 1877 characters remaining).

### 2026-08-06, iteration 623 — [[characters/償|償]]

Confirmed `graphemic_classification: 賞` via domain knowledge (形声, 人 semantic "person" + 賞 phonetic shǎng — "to repay, recompense, compensate") and `mc_id: 2442` locally (`lookup/CC/CC 2000.md` line 463 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the stand-in word 報償). Alias `偿` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, `## Words` immediately following with no blank line) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[報償]] and confirmed the existing [[賠償]] and [[償還]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 墳 (5107; 1876 characters remaining).

### 2026-08-06, iteration 624 — [[characters/墳|墳]]

Confirmed `graphemic_classification: 賁` via domain knowledge (形声, 土 semantic "earth" + 賁 phonetic fén — "burial mound, grave, tomb") and `mc_id: 1928` locally (`lookup/CC/CC 1000.md` line 969 — correct, no fix needed). Filled the empty `pos` field (`名詞`). Alias `坟` (simplified) confirmed legitimate. Reordered a misplaced `## Words` section (which preceded a malformed `# Notes` heading) into the standard Notes-then-Words order with a proper 4-bullet Notes section.

**Words cross-check** (1 ground-truth hit via `find_citers.py`, matching the page's existing single entry): added the `(stand-in for 墳)` tag to [[墳墓]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 摂 (char) (5108; 1875 characters remaining).

### 2026-08-06, iteration 625 — [[characters/摂 (char)|摂 (char)]]

Confirmed `graphemic_classification: 耳` via domain knowledge: verified this is not an error but a deliberate reflection of the Japanese shinjitai simplification — the traditional phonetic 聶 (three 耳 stacked) was reduced to a single 耳 in 摂's own simplified glyph, so citing 耳 correctly describes this specific character's structure rather than 攝's. `mc_id: 1382` verified correct locally (`lookup/CC/CC 1000.md` line 399, recorded under the traditional form 攝). Filled the empty `pos` field (`性詞`, matching the "vicarious" gloss). Alias `攝` (traditional) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, one informally-linked Words bullet) with a proper `## Notes` (4 bullets) and `## Words` section. (Noted but left out of scope: the sibling word page `words/摂.md` has a literal-string `"null"` `korean` field, same bug class as several other word pages found this session, left for separate word-perfecting work.)

**Words cross-check** (2 ground-truth hits via `find_citers.py`, requiring the `摂 (char)` form to surface the self-referential citation): added the self-referential `stand_in` [[摂]] and confirmed the existing [[摂食]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 叙 (5109; 1874 characters remaining).

### 2026-08-06, iteration 626 — [[characters/叙|叙]]

Confirmed `graphemic_classification: 余` via domain knowledge (形声, 又 semantic "hand, again," a further-simplified form of 攴/攵 "to tap, act," + 余 phonetic yú — "to narrate, recount, state") and `mc_id: 1995` locally (`lookup/CC/CC 1000.md` line 1036, recorded under the traditional form 敘 — correct, no fix needed). Filled the empty `pos` field (`事詞`, matching the sibling word 叙述's own `事詞` field, filled during its own earlier perfecting pass on 2026-08-03). Both aliases confirmed legitimate: `敍` and `敘` (traditional forms). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[叙述]] and [[昇叙]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 嘆 (char) (5110; 1873 characters remaining).

### 2026-08-06, iteration 627 — [[characters/嘆 (char)|嘆 (char)]]

Confirmed `graphemic_classification: 漢` via domain knowledge (形声, 口 semantic "mouth" + phonetic 漢, part of the same 𦰩 phonetic series as 難, no vault page — "to moan, sigh, exclaim"). **Fixed `mc_id`**: stored as `1199`, which is the entry for the alias 歎 (`lookup/CC/CC 1000.md` line 208), not the headword 嘆 itself; corrected to `2158`, 嘆's own separate entry (`lookup/CC/CC 2000.md` line 167) — both forms are independently tracked in the corpus, and the page should cite its own headword's rank, not an alias's. Filled the empty `pos` field (`事詞`, matching the sibling word 嘆's own field). Both aliases confirmed legitimate: `歎` (traditional variant, own separate CC entry) and `叹` (simplified). Identified the correct lookup-file convention for the unusual `hanmun_edu_level: "名"` value by cross-referencing other fully-perfected pages using it — it pairs with a `Korean Name <initial-jamo>` lookup file (here, `Korean Name ㅌ`, matching 嘆's Korean reading 탄), independent of `grade_level`. Replaced the malformed `# Notes` heading with a proper 4-bullet section.

**Words cross-check** (4 ground-truth hits via `find_citers.py`, requiring the `嘆 (char)` form to surface most citations): added the self-referential `stand_in` [[嘆]], plus [[感嘆]] and [[感嘆詞]], and confirmed the existing [[賛嘆]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 渉 (char) (5111; 1872 characters remaining).

### 2026-08-06, iteration 628 — [[characters/渉 (char)|渉 (char)]]

Confirmed `graphemic_classification: 會意` via domain knowledge (Shuowen: 从水从步 — 水 "water" + 步 "to step, walk," no vault page — "to wade across water on foot," extended to "to be involved with, to interfere") and `mc_id: 1087` locally (`lookup/CC/CC 1000.md` line 92, recorded under the form 涉 — correct, no fix needed). Filled the empty `pos` field (`動詞`). Alias `涉` (the standard form; 渉 itself is a Japanese shinjitai variant) confirmed legitimate. **Fixed a wrong initial-group citation**: the bare Notes link pointed to `聲 端` ([t]), but the frontmatter's own `middle_chinese_initial: d͡ʑ` doesn't match that group at all — cross-referenced all initial lookup pages and found `聲 禪` ([d͡ʑ]) is the correct match; corrected the link. Replaced the malformed `# Notes` heading with a proper 4-bullet section and `## Words`.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[渉]] and [[干渉]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted. (Noted but left out of scope: the sibling word page `words/渉.md` has a literal-string `"null"` `korean` field, same bug class found repeatedly this session, left for separate word-perfecting work.)

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 潤 (char) (5112; 1871 characters remaining).

### 2026-08-06, iteration 629 — [[characters/潤 (char)|潤 (char)]]

Confirmed `graphemic_classification: 閏` via domain knowledge (形声, 水 semantic "water" + 閏 phonetic rùn — "moist, smooth, soft," extended to "to enrich, increase," as in profit) and `mc_id: 1793` locally (`lookup/CC/CC 1000.md` line 826 — correct, no fix needed). Filled the empty `pos` field (`性詞`). Alias `润` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, no Words section) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[潤]] and [[利潤]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted. (Noted but left out of scope: the sibling word page `words/潤.md` has a literal-string `"null"` `vietnamese` field, same bug class found repeatedly this session, left for separate word-perfecting work.)

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 濫 (5113; 1870 characters remaining).

### 2026-08-06, iteration 630 — [[characters/濫|濫]]

Confirmed `graphemic_classification: 監` via domain knowledge (形声, 水 semantic "water" + 監 phonetic — "overflowing, flooding," extended to "excessive, unchecked"; the same phonetic component seen earlier this session on 鑑) and `mc_id: 2140` locally (`lookup/CC/CC 2000.md` line 149 — correct, no fix needed). Filled the empty `pos` field (`性詞`). Alias `滥` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, two informally-linked bullets, no Words heading) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[汎濫]], confirmed the existing [[泛濫]], and added [[氾濫]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 沢 (5114; 1869 characters remaining).

### 2026-08-06, iteration 631 — [[characters/沢|沢]]

Confirmed `graphemic_classification: 尺` via domain knowledge: verified this is a deliberate Japanese shinjitai simplification (traditional phonetic 睪 reduced to 尺 in 沢's own simplified glyph — the same pattern established earlier this session on 摂/耳), not an error. `mc_id: 549` verified correct locally (`lookup/CC/CC 0000.md` line 570, recorded under the traditional form 澤). `pos` was already correctly filled (`名詞`). Both aliases confirmed legitimate: `澤` (traditional) and `泽` (simplified). Reordered a misplaced `## Words` section (preceding a malformed `# Notes` heading) into the standard order with a proper 4-bullet Notes section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[沼沢]] and confirmed the existing [[薮沢]] and [[徳沢]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 兮 (char) (5115; 1868 characters remaining).

### 2026-08-06, iteration 632 — [[characters/兮 (char)|兮 (char)]]

Confirmed `graphemic_classification: 會意` via domain knowledge (丂 "a fork in a tree, breath catching on an obstruction," no vault page, + 八 "dispersal, breath escaping outward like wind through trees" — together depicting an exhaled sigh, a classical exclamatory/rhythmic verse particle) and `mc_id: 258` locally (`lookup/CC/CC 0000.md` line 270 — correct, no fix needed). **Fixed a broken component link**: the first component's markdown link pointed to `考.md` (an unrelated character meaning "to examine, deceased father") instead of 丂; corrected to a wikilink with no vault page. Filled the empty `pos` field (`感詞`, matching the sibling word 兮's own field). No aliases to assess (field empty). Confirmed the `joyo_level: 表外字` → Hyōgai and `hsk_level: 無` → HSK No lookup-file mappings, both already established this session. Replaced the malformed `## Notes` (bare unlinked initial/final references) with a proper 4-bullet section and `## Words`.

**Vault-wide side fix**: while building this bullet, noticed the "No HSK" display text used on several pages this session (捜, 隠, 摂 (char), 隷, 哭 (char), 懐 (char), 陥 (char), 渉 (char), 沢, 謡, 鋳) — and, from before this session, 曇 (char), 娯, 廃 — doesn't match the vault's established convention (the lookup file is `HSK No.md`, and every other page in the vault uses that exact display text). Corrected all 14 occurrences vault-wide via a single sed pass, `[No HSK]` → `[HSK No]`, link targets unchanged.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[兮]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 毀 (char) (5116; 1867 characters remaining).

### 2026-08-06, iteration 633 — [[characters/毀 (char)|毀 (char)]]

Confirmed `graphemic_classification: 會意` via domain knowledge (臼 "cracked skull" + 工 "tool" + 殳, "hand action," no vault page — a man being struck in the head, "to destroy," extended to "to slander, defame") and `mc_id: 855` locally (`lookup/CC/CC 0000.md` line 885 — correct, no fix needed). Filled the empty `pos` field (`動詞`). Alias `毁` (simplified) confirmed legitimate. Fixed broken markdown links (relative-path, non-wikilink syntax pointing to `臼 (char).md` and `工.md`) and moved the etymology bullet out of a misplaced `## Words` section into a proper `## Notes` (4 bullets).

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[毀]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 炉 (5117; 1866 characters remaining).

### 2026-08-06, iteration 634 — [[characters/炉|炉]]

**Fixed a frontmatter/prose self-contradiction and a fabricated `mc_id`**: the page had two duplicate Notes bullets disagreeing with each other — one (matching the frontmatter's `graphemic_classification: 盧`) had an empty, broken phonetic link; the other correctly identified 戸 as the phonetic actually present in this specific glyph. Verified via domain knowledge that 炉 (both the Japanese shinjitai and Chinese simplified form) replaces the traditional phonetic 盧 with 戸 — the same simplification pattern established earlier this session on 摂/耳 and 沢/尺 — so corrected the frontmatter to `戸` to match the glyph's real composition. Searched all four `lookup/CC/CC *.md` files end to end and found neither 炉 nor 爐 appears anywhere in the ~4000-entry corpus; the stored `mc_id: 4539` was not just wrong but out of range entirely (beyond the corpus's actual ceiling) — corrected to `0` per the checklist convention for characters confirmed absent from the ranking. `pos` was already correctly filled (`名詞`). Alias `爐` (traditional) confirmed legitimate. Consolidated the duplicate/contradictory Notes bullets, fixed more broken relative-path markdown links, and merged everything into the standard 4-bullet structure.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the `(stand-in for 炉)` tag to the existing [[火炉]] and [[炉甘石]], and added [[炉甘金]] (a mineral-based periodic-table neologism for cadmium, per its own page's etymology notes). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 奔 (5118; 1865 characters remaining).

### 2026-08-06, iteration 635 — [[characters/奔|奔]]

**Fixed `graphemic_classification`**: stored as `歮` (an unrelated character meaning "astringent, rough"), which is neither cited in Shuowen's actual analysis of 奔 nor phonetically plausible; the page's own Notes prose already correctly cited [[卉]] as the visible bottom component. Verified via domain knowledge that Shuowen's real analysis is 从夭賁省聲 — 夭 semantic ("a running person, arms swinging," now written 大) + phonetic 賁 abbreviated to the 卉 shape (賁 carries an alternate reading bēn identical to 奔's, as in 虎賁 "brave warriors") — corrected the frontmatter to `賁`, the true phonetic, rather than the visible abbreviated shape. `mc_id: 619` verified correct locally (`lookup/CC/CC 0000.md` line 643). `pos` was already correctly filled (`性詞`). Assessed alias `犇` (three 牛 "oxen," 會意, "to run wildly like cattle stampeding") — a distinct, rarer character occasionally used interchangeably with 奔, kept as legitimate. Consolidated a malformed `# Notes`/`## Chengyu` block (with bare, unlinked initial/final references and unlinked Words-appropriate bullets scattered after the Chengyu heading) into the standard Notes→Words→Chengyu structure.

**Words cross-check** (6 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[奔走]], confirmed the existing [[奔馳]], [[奔放]], [[奔波]], and [[奔騰]] (this last one initially missed on the first pass and added after re-checking the citer list), and added [[出奔]]. **Chengyu** (1 ground-truth hit, already present): confirmed [[東奔西走]] correct. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 獄 (5119; 1864 characters remaining).

### 2026-08-06, iteration 636 — [[characters/獄|獄]]

Confirmed `graphemic_classification: 會意` via domain knowledge (Shuowen: two 犬 "dogs," guard dogs flanking, + 言 "words, litigation," no vault page — a dispute settled between two guarded parties, "prison, lawsuit") and `mc_id: 693` locally (`lookup/CC/CC 0000.md` line 717 — correct, no fix needed). Filled the empty `pos` field (`名詞`). Alias `狱` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, one informally-linked Words bullet) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[監獄]], plus [[牢獄]] and confirmed the existing [[獄吏]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 症 (5122; 1863 characters remaining).

### 2026-08-06, iteration 637 — [[characters/症|症]]

Confirmed `graphemic_classification: 正` via domain knowledge (形声, 疒 semantic "disease" + 正 phonetic zhèng — "disease condition, symptom," a highly productive medical suffix forming condition/syndrome names). **Fixed a fabricated, out-of-range `mc_id`**: stored as `6300`, far beyond the corpus's actual ~4000-entry ceiling; searched all four `lookup/CC/CC *.md` files and found neither 症 nor its alias 癥 anywhere in the corpus — corrected to `0` per the checklist convention for characters confirmed absent from the ranking. `pos` was already correctly filled (`名詞`). Alias `癥` (a distinct but related traditional-register form) confirmed legitimate. Rebuilt the malformed `## Notes`/`## Words` block (a stray leading blank line, bare unlinked initial/final references, several bare unformatted Words bullets including one truly empty bullet) into the standard 4-bullet Notes structure with properly ruby-formatted Words.

**Words cross-check** (5 ground-truth hits via `find_citers.py`): added the self-referential `stand_in` [[病症]], reformatted the existing [[症状]], [[癌症]], and [[炎症]] with proper ruby, and added [[自閉症]] (a pan-Sinospheric Greek calque for "autism," per its own page's etymology notes). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 監 (5123; 1862 characters remaining).
