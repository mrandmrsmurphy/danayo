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
