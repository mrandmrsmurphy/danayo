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

### 2026-08-06, iteration 638 — [[characters/監|監]]

**Fixed a garbled etymology**: the Notes bullet read "会意 of 皿 ('a person with an emphasized eye')," an incomplete/malformed description missing the other two components. Corrected via domain knowledge to the standard analysis: 臣 ("an emphasized eye, looking down") + 人 ("a bent-over person") + 皿 ("a basin of water") — a person bending over a basin of water to see their reflection before bronze mirrors existed, "to observe closely," extended to "oversee, supervise." `mc_id: 1187` verified correct locally (`lookup/CC/CC 1000.md` line 196). `pos` was already correctly filled (`事詞`). Alias `监` (simplified) confirmed legitimate.

**Derived Characters expanded**: the page listed only [[鑑]] (already encountered as a citer of 監's phonetic role earlier this session). Grepped the whole vault for `graphemic_classification: 監` and found seven total phonetic-derivative characters — added [[濫]] (also already perfected this session), [[覧]], [[艦]], [[籃]], [[㽉]], [[塩 (char)|塩]], and [[藍 (char)|藍]].

**Words cross-check** (3 ground-truth hits via `find_citers.py`): added the `(stand-in for 監)` tag to the existing [[監督]], plus [[監獄]] and [[監禁]]. **Chengyu**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 采 (5124; 1861 characters remaining).

### 2026-08-06, iteration 639 — [[characters/采|采]]

Confirmed `graphemic_classification: 會意` via domain knowledge (爪 "a hand reaching down" + 木 "tree" — a hand picking fruit or leaves from a tree, "to pick, gather," extended metaphorically to "coloring, adornment," and thence to "demeanor, bearing, elegance") and `mc_id: 1007` locally (`lookup/CC/CC 1000.md` line 12 — correct, citing the headword's own entry rather than the alias 採's separate entry at `CC 2000.md` line 137, consistent with the convention established on 嘆 (char)). Filled the empty `pos` field (`名詞`). Assessed both aliases: `採` (a derived form with 手 replacing 爪, reinforcing "to pick") and `埰` (a rarer variant meaning "a fief, feudal estate," historically conflated with 采 in the sense of a lord's granted land) both kept as legitimate. Confirmed the `hanmun_edu_level: 名` → `Korean Name ㅊ` lookup-file mapping (matching 采's Korean reading 채), the same convention established on 嘆 (char) earlier this session. Replaced the malformed `# Notes` heading with a proper 4-bullet section and `## Words`.

**Words cross-check** (1 ground-truth hit via `find_citers.py`): added the self-referential `stand_in` [[風采]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 巡 (5125; 1860 characters remaining).

### 2026-08-06, iteration 640 — [[characters/巡|巡]]

Confirmed `graphemic_classification: 川` via domain knowledge (形声, 辵/辶 semantic "to walk," no vault page, + 川 phonetic, near-homophonous, evoking flowing/circling movement — "to patrol, make one's rounds, go on circuit") and `mc_id: 1251` locally (`lookup/CC/CC 1000.md` line 264 — correct, no fix needed). Filled the empty `pos` field (`事詞`). No aliases to assess (field empty). Replaced the malformed `# Notes` heading (missing bullets entirely, with the Words section and bare unlinked initial/final references misplaced above/below it) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (1 ground-truth hit via manual grep — `find_citers.py` and a subsequent verification script both hung on this iteration due to a slow-disk condition on the host machine, unrelated to the vault data itself; fell back to direct `grep -rl` searches across words/chengyu/characters, which is exact-string-safe and returned the same class of result this script normally produces): confirmed the existing self-referential [[巡回]] as the sole citer, added the `(stand-in for 巡)` tag. Also checked 巡's apparent hit in `chengyu/日月星辰.md` and confirmed it's a false positive — the character occurs only inside a Japanese example sentence in prose, not as a citing constituent. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 沈 (5126; 1859 characters remaining).

### 2026-08-06, iteration 641 — [[characters/沈|沈]]

Confirmed `graphemic_classification: 冘` via domain knowledge (形声, 水 semantic "water" + 冘 phonetic, no vault page — "to sink, submerge," extended to "deep, heavy (of mood), silent") and `mc_id: 1231` locally (`lookup/CC/CC 1000.md` line 244 — correct, citing 沈's own separate entry rather than the variant 沉's independent entry at `CC 1000.md` line 817). Filled the empty `pos` field (`事詞`). Assessed both aliases: `沉` (a standard variant form with its own separate CC entry, and the more common modern simplified rendering) confirmed legitimate; `瀋` assessed as the traditional form specific to 沈's secondary reading (Shěn, a surname and the historical short name for Shenyang, e.g. 瀋陽/沈陽) — a distinct-reading branch of the same glyph rather than a separate character, kept as legitimate. **Worked around a slow-disk hang** in `find_citers.py` (same host-machine condition affecting the previous iteration) by falling back to direct `grep -rl` searches; found and discarded three false-positive hits (`堆積.md`, `石油.md` — which mentions the historical figure 沈括 Shěn Kuò by name — and `不言不語.md`, which references the unrelated word 沈默 in prose) before confirming the real citer set. Consolidated a malformed `## Notes`/`## Words`/`## Chengyu` block (bare unlinked initial/final references, one bullet misplaced under Notes, one unformatted plain-link Words bullet) into the standard structure, and fixed an incorrect ruby on [[沈黙]] (ㄑㄧㄇㄇㄛㄎ → the word page's own correct ㄑㄧㄇㄇㄨㄎ).

**Words cross-check** (4 ground-truth hits via manual grep): added the self-referential `stand_in` [[沈没]], confirmed [[沈淀]], corrected and confirmed [[沈黙]], and confirmed [[沈菜]]. **Chengyu** (1 ground-truth hit, already present): confirmed [[沈魚落雁]] correct. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 稿 (char) (5127; 1858 characters remaining).

### 2026-08-06, iteration 642 — [[characters/稿 (char)|稿 (char)]]

Confirmed `graphemic_classification: 高` via domain knowledge (形声, 禾 semantic "grain, stalk," originally "straw," + 高 phonetic gāo — "straw," extended to "a rough draft," since early paper was made from straw pulp, and thence to "manuscript, copy") and `mc_id: 3577` locally (`lookup/CC/CC 3000.md` line 602 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Confirmed via grep that the word-level homophone callout between [[稿]] and [[高]] (documented on `words/高.md` as "a direct phonetic descendant") is already correctly present on `words/稿.md` — no character-page-level action needed, since that callout convention applies to word pages only. Discarded two false-positive citer hits (`words/草.md` and `words/高.md`, both mentioning 稿 only in prose/compound examples, not as a citing constituent). Replaced the malformed `# Notes` heading with a proper 4-bullet section and `## Words`.

**Words cross-check** (2 ground-truth hits via manual grep, working around the same slow-disk condition affecting `find_citers.py` this session): added the self-referential `stand_in` [[稿]] and [[脱稿]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 奴 (5128; 1857 characters remaining).

### 2026-08-06, iteration 643 — [[characters/奴|奴]]

**Fixed a component-name-vs-type-name category error**: `graphemic_classification` stored `女` (a component name, valid convention only for 形声), for a character that is actually `會意` — corrected to the type name, following the same fix pattern established earlier this session on 頃 (char). Confirmed via domain knowledge (Shuowen: 从女从又 — 女 "woman" + 又 "hand" — a woman seized by a hand, "captive, slave, servant"). `mc_id: 391` verified correct locally (`lookup/CC/CC 0000.md` line 406). `pos` was already correctly filled (`名詞`). No aliases to assess (field empty — `㚢` in the aliases list is a genuine rare variant, kept as-is absent contradicting evidence). **Fixed a `stand_in` pointing to a nonexistent word page**: stored as `奴僕`, which has no corresponding file anywhere in `words/`, the same bug class found earlier this session on 喉→喉頭 and 索→繩索; retargeted to the real citing word [[奴隷]] (already perfected this session at iteration #619). Discarded three false-positive citer hits (`引出.md`, `出谷記.md`, `石油.md`, all mentioning 奴 only in prose/compound examples).

**Words cross-check** (3 ground-truth hits via manual grep, working around the ongoing slow-disk condition affecting `find_citers.py`): retargeted the `stand_in` annotation to [[奴隷]], confirmed [[奴家]], and added [[匈奴]]. **Chengyu** (1 ground-truth hit): added [[引出奴家]] (a Biblical chengyu rendering the Exodus "house of bondage" formula, per its own page and `words/引出.md`'s cross-reference). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 琴 (char) (5129; 1856 characters remaining).

### 2026-08-06, iteration 644 — [[characters/琴 (char)|琴 (char)]]

Confirmed `graphemic_classification: 象形` via domain knowledge (a pictograph of the ancient qín zither, its body and strings stylized over time into the doubled 王/玉-like top) and `mc_id: 1396` locally (`lookup/CC/CC 1000.md` line 413 — correct, no fix needed). Filled the empty `pos` field (`名詞`). Assessed all nine aliases (the largest alias list encountered this session): checked every glyph for a vault page (none exists) and confirmed via domain knowledge that all are attested rare graphic variants of 琴 recorded in historical dictionaries — 珡 is the original unadorned pictographic form; 琹, 𤦡, 𤩟, 𨨖, 𩰔, 䦦, 䥅, 䥆 are further scribal variants — none a distinct character, all kept as legitimate. Discarded four false-positive citer hits (`古箏.md`, `提携.md`, `珠投猪前.md`, `空前絶後.md`, all mentioning 琴 only in prose/compound comparisons). Consolidated the malformed `# Notes` heading (bare unlinked initial/final references immediately followed by `## Words` with no blank line) into the standard structure.

**Words cross-check** (5 ground-truth hits via manual grep, working around the ongoing slow-disk condition affecting `find_citers.py`): added the self-referential `stand_in` [[琴]], confirmed the existing [[提琴]], and added [[古琴]] and [[錀琴]] (a phonetic-plus-semantic neologism for the element roentgenium). **Chengyu** (2 ground-truth hits): confirmed the existing [[焚琴煮鶴]] and added [[対牛弾琴]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 罷 (5130; 1855 characters remaining).

### 2026-08-06, iteration 645 — [[characters/罷|罷]]

Confirmed `graphemic_classification: 會意` via domain knowledge (网 "net," implying entrapment or a fault caught, + 能 "ability, capacity," no vault page — one whose ability has been caught short/exhausted, hence "to stop, cease, dismiss") and `mc_id: 645` locally (`lookup/CC/CC 0000.md` line 669 — correct, no fix needed). Filled the empty `pos` field (`事詞`). Alias `罢` (simplified) confirmed legitimate. Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, one informally-linked Words bullet) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via manual grep, working around the ongoing slow-disk condition affecting `find_citers.py`): added the self-referential `stand_in` [[罷官]] and confirmed the existing [[罷免]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 州 (char) (5132; 1854 characters remaining).

### 2026-08-06, iteration 646 — [[characters/州 (char)|州 (char)]]

Confirmed `graphemic_classification: 象形` via domain knowledge (a pictograph of an islet in a river — a bend of water 川/巛 with a dot/loop for the land within it — originally "river islet, sandbank," a sense later taken over by the derived form [[洲 (char)|洲]], with 州 itself specializing into "administrative division, province, state") and `mc_id: 407` locally (`lookup/CC/CC 0000.md` line 425 — correct, no fix needed). `pos` was already correctly filled (`名詞`). Alias `𠄓` (a rare ancient variant, no vault page) kept as legitimate absent contradicting evidence. Fixed a malformed `vietnamese` field (a single list item containing an embedded comma, `"châu, chu"`, instead of two separate list entries). Rewrote a casual, non-standard Notes bullet ("Somehow, this is [[SKIP-1-2-4]].") and consolidated everything into the standard 4-bullet structure, confirming both new lookup-file conventions encountered here (`Grade 3` and `Jōyō - Kyōiku`) exist in the vault.

**Words cross-check** (12 ground-truth hits after filtering ~30 raw grep matches down to real citations — the largest false-positive-filtering pass this session, since `州` is a substring shared by no other glyph but is heavily cross-referenced in prose by its near-homophone cluster 宙/洲/由 and by numerous 洲-suffixed continent/place words that don't actually cite 州 itself): added the self-referential `stand_in` [[州]], confirmed the existing [[九州]] and [[兗州]] and [[加州金]], and added all eight remaining historical "Nine Provinces" siblings — [[予州]], [[揚州]], [[徐州]], [[希州]], [[梁州]], [[荊州]], [[雍州]], [[青州]] — after finding they all genuinely cite 州 in their `characters:` frontmatter despite not surfacing in the initial informal Words list. **Chengyu**/**Derived Characters**: no real hits after filtering out two more prose-only false positives — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 笛 (5133; 1853 characters remaining).

### 2026-08-06, iteration 647 — [[characters/笛|笛]]

Confirmed `graphemic_classification: 由` via domain knowledge (形声, 竹 semantic "bamboo" + 由 phonetic — "flute, whistle," a bamboo wind instrument). **Fixed a fabricated, out-of-range `mc_id`**: stored as `5423`, far beyond the corpus's actual ~4000-entry ceiling; searched all four `lookup/CC/CC *.md` files and found 笛 appears nowhere in the corpus — corrected to `0`. Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Confirmed the `hanmun_edu_level: 名` → `Korean Name ㅈ` lookup-file mapping (matching 笛's Korean reading 적), the same convention established on 嘆/采 earlier this session, and the `joyo_level: "3"` → `Jōyō - Kyōiku (3)` mapping established on 州 (char) immediately prior. Dropped an ad hoc "Dropped from the Korean HS list in 2000" line and two bare unlinked initial/final references, replacing with the standard 4-bullet structure and a `## Words` section.

**Words cross-check** (2 ground-truth hits via manual grep, discarding a false-positive chengyu mention in `対牛弾琴.md` which cites an unrelated synonym idiom 對牛吹笛 in prose only): added the self-referential `stand_in` [[口笛]] and [[風笛]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 荷 (5134; 1852 characters remaining).

### 2026-08-06, iteration 648 — [[characters/荷|荷]]

Confirmed `graphemic_classification: 何` via domain knowledge (形声, 艸 semantic "grass, plant" + 何 phonetic, itself later specialized from "to carry" to the interrogative "what" — 荷 originally meant "lotus," extended via 何's older sense to "to carry, bear, load, luggage") and `mc_id: 2360` locally (`lookup/CC/CC 2000.md` line 377 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Discarded three false-positive citer hits (`何物.md`, `季夏.md` — neither actually cites 荷 — and `弱不禁風.md`, which quotes 荷花 only within an embedded classical poem). Replaced the malformed `# Notes` heading with a proper 4-bullet section.

**Words cross-check** (5 ground-truth hits via manual grep): added the self-referential `stand_in` [[荷物]], confirmed the existing [[荷蘭]], and added [[荷担]], [[荷月]], and [[薄荷]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 具 (5135; 1851 characters remaining).

### 2026-08-06, iteration 649 — [[characters/具|具]]

**Fixed frontmatter/prose contradiction**: `graphemic_classification` stored `指事`, directly contradicting the page's own Notes prose, which already correctly described `会意` (鼎 "cauldron" + 廾 "two hands" — two hands holding up a cauldron to prepare food, "to possess, prepare, equip," extended to "tool, implement"). Corrected the frontmatter to `會意` to match the already-correct prose. `mc_id: 654` verified correct locally (`lookup/CC/CC 0000.md` line 678). Filled the empty `pos` field (`名詞`) and fixed a typo in `english` (`impliment` → `implement`). No aliases to assess (field empty; dropped a stray, non-standard aside about an unrelated lookalike glyph 𥃲 that added no value). Discarded ten false-positive citer hits (以, 套, 仮面, 呼格, 処格, 剣道, 与格, 向格, 奪格, 混沌 — all mentioning 具格 only in prose comparisons within articles about unrelated grammatical cases, none citing 具 in their own frontmatter).

**Words cross-check** (4 ground-truth hits via manual grep): added the self-referential `stand_in` [[工具]], confirmed the existing [[具格]], and added [[家具]] and [[玩具]] (correcting a guessed ruby for the latter against the word page's actual 注音). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 炭 (char) (5136; 1850 characters remaining).

### 2026-08-06, iteration 650 — [[characters/炭 (char)|炭]]

**Resolved a frontmatter/prose phonetic mismatch**: frontmatter stored `graphemic_classification: 屵` while the Notes prose cited a different phonetic, 岸. Verified via domain knowledge that 屵 (OC \*ŋaːns) is the component actually present in 炭's glyph, while 岸 — sharing the same OC reading — is the fuller related character 屵 itself derives from; corrected the prose to cite 屵 as primary while noting the 岸 relationship, the same "component actually in the glyph vs. its fuller parent" pattern established earlier this session on 摂/耳 and 沢/尺. `mc_id: 2311` verified correct locally (`lookup/CC/CC 2000.md` line 328). `pos` was already correctly filled (`名詞`). No aliases to assess (field empty). This character completes the tan/탄/ㄊㄚㄋ three-way homophone cluster with [[characters/嘆 (char)|嘆]] (perfected earlier this session at iteration #627) and [[灘]] (still awaiting its own turn), both of which explicitly flagged 炭 as "still awaiting its own turn" on their own word pages. Discarded seven false-positive citer hits (石, 煤, 燐素, 白金, 栄養素, 虹霓, all mentioning 炭 only in prose comparisons or compound examples). Rebuilt the malformed Notes block (a stray numbered list mixed into the Notes section, one initial/final reference crammed onto a single line) into the standard 4-bullet structure with a `## Words` section.

**Words cross-check** (1 real ground-truth hit beyond self via manual grep): added the self-referential `stand_in` [[炭]] and [[炭素]] (the element carbon, a genuine established compositional word rather than a coinage, per its own page's notes). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 消 (char) (5137; 1849 characters remaining).

### 2026-08-06, iteration 651 — [[characters/消 (char)|消]]

Confirmed `graphemic_classification: 肖` via domain knowledge (形声, 水 semantic "water" + 肖 phonetic xiào — "to melt away (as ice in water), to vanish, to die out," extended to "to consume, use up") and `mc_id: 1281` locally (`lookup/CC/CC 1000.md` line 294 — correct, no fix needed). Filled the empty `pos` field (`事詞`). No aliases to assess (field empty). Identified a new `hanmun_edu_level` value not yet encountered this session, `中` (Korean middle-school level, per `AIOS/checklists/checklist_characters.md` line 211) → `Korean MS` lookup file, distinct from the `名`→`Korean Name X` and `高等`→`Korean HS` conventions already established. Discarded six false-positive citer hits (条, 某人, 敵人, 石灰, and chengyu 欣喜雀躍/鼠世桃源 — none actually cite 消 in their own frontmatter). Replaced the malformed `## Notes` heading (two bare, unlinked initial/final references) with a proper 4-bullet section.

**Words cross-check** (3 ground-truth hits via manual grep, matching the page's existing entries): added the self-referential `stand_in` [[消]] and confirmed [[消息]], [[消耗]], and [[消防局]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 予 (5138; 1848 characters remaining).

### 2026-08-06, iteration 652 — [[characters/予|予]]

Confirmed `graphemic_classification: 象形` via domain knowledge (a pictograph of a shuttle passing thread back and forth in weaving, "to give, hand over" — as a bound character, extended to "in advance, beforehand" via its 豫/預 phonetic-series relatives) and `mc_id: 563` locally (`lookup/CC/CC 0000.md` line 584 — correct, no fix needed). `pos` was blank; filled as `名詞` to match the stand-in word 予様's own field (the character's "beforehand" gloss is adverbial in function but the vault classifies both consistently as 名詞). Assessed all three aliases: `豫` (a distinct but closely related character, "pleased; in advance," sharing 予's OC reading and the "in advance" sense, historically interchanged) and `預`/`预` (traditional/simplified "in advance, to reserve," the same phonetic-series relationship) all kept as legitimate rather than contamination. Dropped a debugging-artifact line ("豫=C#1042") and a bare, unlinked component reference, replacing with the standard 4-bullet structure.

**Words cross-check** (7 ground-truth hits after filtering ~12 raw grep matches — discarding five false positives, `偏差`, `充当`, `天気`, `愛媛`, `其人等`, and three chengyu false positives, none of which actually cite 予, plus one further false positive `贈与` which cites the visually similar but distinct character 与 rather than 予): added the self-referential `stand_in` [[予様]], plus [[予定]], [[予州]] (a "Nine Provinces" sibling, matching the set built on [[characters/州 (char)|州]] earlier this session), [[予習]], [[猶予]], and confirmed the existing [[賜予]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-06`.

Next never-perfected character by `danayo_id`: 役 (5139; 1847 characters remaining).

### 2026-08-07, iteration 653 — [[characters/役|役]]

Confirmed `graphemic_classification: 會意` via domain knowledge (彳 "to walk, move," no vault page, + 殳 "a weapon/tool held in hand," no vault page — a person driven to move while bearing a tool or weapon, depicting forced labor or military service, "to serve, corvée labor") and `mc_id: 915` locally (`lookup/CC/CC 0000.md` line 948 — correct, no fix needed). Filled the empty `pos` field (`事詞`). No aliases to assess (field empty). Discarded four false-positive citer hits (俳優, 毎人, 官庁, and chengyu 乾坤一擲, none of which actually cite 役 in their own frontmatter — all mention it only in prose, e.g. 役者/役所). Replaced the malformed `## Notes` heading (two bare, unlinked initial/final references) with a proper 4-bullet section.

**Words cross-check** (1 real ground-truth hit via manual grep, matching the page's existing single entry): added the `(stand-in for 役)` tag to [[苦役]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 幕 (char) (5140; 1846 characters remaining).

### 2026-08-07, iteration 654 — [[characters/幕 (char)|幕]]

Confirmed `graphemic_classification: 莫` via domain knowledge (形声, 巾 semantic "cloth" + 莫 phonetic mù — "curtain, screen," extended to "a military headquarters/tent behind the curtain," and thence to "shogunate," 幕府) and `mc_id: 1999` locally (`lookup/CC/CC 1000.md` line 1040 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Fixed a broken final-韻 link (a stray `../`-prefix baked directly into the wikilink syntax, the same bug class found repeatedly earlier this session). Discarded four false-positive citer hits (鎌倉, 開張, and chengyu 尊王攘夷, none of which cite 幕 in their own frontmatter — all mention 幕府 only in prose). **Verified the `joyo_level` grade-number lookup convention**: briefly suspected the "(N)" grade-number suffix I'd been appending after `[[Jōyō - Kyōiku]]` on the last several iterations (州, 笛, 荷, 具, 消, 予, 役) was a self-introduced inconsistency, since `AIOS/checklists/checklist_characters.md` documents no such suffix and three spot-checked pre-existing pages (供, 傷, 刻) omit it — but a vault-wide grep found 19 other pre-existing, unrelated pages already using this exact `(N)` suffix pattern, confirming it as genuine (if checklist-undocumented) existing practice rather than an error; no correction needed, and 幕 itself now follows the same convention.

**Words cross-check** (1 real ground-truth hit via manual grep): added the self-referential `stand_in` [[幕]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 署 (5142; 1845 characters remaining).

### 2026-08-07, iteration 655 — [[characters/署|署]]

Confirmed `graphemic_classification: 者` via domain knowledge (形声, 网 semantic "net," implying an assigned post or division of duties, + 者 phonetic zhě — "to assign a post, to arrange," extended to "government office, department") and `mc_id: 1604` locally (`lookup/CC/CC 1000.md` line 633 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Discarded two false-positive citer hits (所属, 消防局, neither citing 署 in its own frontmatter). Replaced the malformed `# Notes` heading with a proper 4-bullet section and `## Words`.

**Words cross-check** (1 real ground-truth hit via manual grep): added the self-referential `stand_in` [[部署]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 垂 (5143; 1844 characters remaining).

### 2026-08-07, iteration 656 — [[characters/垂|垂]]

Confirmed `graphemic_classification: 象形` via domain knowledge (depicts drooping leaves and stems hanging down from a plant — "to hang down, dangle, droop," extended to "vertical," as a hanging line, and "to bequeath, pass down to posterity") and `mc_id: 1036` locally (`lookup/CC/CC 1000.md` line 41 — correct, no fix needed). Filled the empty `pos` field (`事詞`). No aliases to assess (field empty). Discarded three false-positive citer hits (眼瞼, 耳朶, 蛍火虫, none citing 垂 in their own frontmatter). Reordered a misplaced `## Words` section (preceding a malformed `# Notes` heading with a stray unlinked bullet) into the standard order with a proper 4-bullet Notes section.

**Words cross-check** (4 ground-truth hits via manual grep): added the `(stand-in for 垂)` tag to the existing [[垂掛]], confirmed [[垂直]], and added [[懸垂]] and [[懸壅垂]] (both already established as citers on [[characters/懸 (char)|懸]] earlier this session). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 姿 (5144; 1843 characters remaining).

### 2026-08-07, iteration 657 — [[characters/姿|姿]]

Confirmed `graphemic_classification: 次` via domain knowledge (形声, 女 semantic "woman," implying grace or bearing, + 次 phonetic cì — "manner, bearing, figure, appearance") and `mc_id: 3107` locally (`lookup/CC/CC 3000.md` line 116 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Discarded one false-positive citer hit (矯正, not citing 姿 in its own frontmatter). Replaced the malformed `# Notes` heading (two bare, unlinked initial/final references, two informally-linked Words bullets) with a proper `## Notes` (4 bullets) and `## Words` section.

**Words cross-check** (2 ground-truth hits via manual grep, matching the page's existing entries): added the `(stand-in for 姿)` tag to [[姿勢]] and confirmed [[姿態]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 潮 (5145; 1842 characters remaining).

### 2026-08-07, iteration 658 — [[characters/潮|潮]]

Confirmed `graphemic_classification: 朝` via domain knowledge (形声, 水 semantic "water" + 朝 phonetic zhāo — originally "the morning flood-tide," as distinct from 汐 "the evening tide," generalized to "tide" as a phenomenon). **Fixed a fabricated, out-of-range `mc_id`**: stored as `4549`, far beyond the corpus's actual ~4000-entry ceiling; searched all four `lookup/CC/CC *.md` files and confirmed 潮 appears nowhere in the corpus — corrected to `0`. Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Verified the `#cranberry` tag: 潮汐 is also tagged `cranberry`, pairing 潮 ("morning tide") with its sibling [[characters/汐|汐]] ("evening tide") — together spanning the full daily cycle as the combined sense "tide," consistent with the vault's existing tagging on both halves. Reordered a misplaced `## Words` section (preceding a malformed `# Notes` heading) into the standard order with a proper 4-bullet Notes section.

**Words cross-check** (2 ground-truth hits via manual grep): added the self-referential `stand_in` [[潮汐]] with the cranberry cross-reference noted, and [[風潮]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 誌 (5146; 1841 characters remaining).

### 2026-08-07, iteration 659 — [[characters/誌|誌]]

Confirmed `graphemic_classification: 志` via domain knowledge (形声, 言 semantic "words, speech" + 志 phonetic zhì — "to record, chronicle," extended to "symbolize, mark," and as a noun "magazine, journal") and `mc_id: 3312` locally (`lookup/CC/CC 3000.md` line 329, distinct from the alias 志's own separate entry at `CC 0000.md` line 397 — correct, no fix needed). Filled the empty `pos` field (`事詞`). Assessed both aliases: `志` (a legitimate alternate form in the "record" sense, e.g. 三國志, since 言 was added to 誌 later purely for disambiguating clarity — not contamination despite also being the stored phonetic component) and `𰵧` (a further attested rare variant with no vault page) both kept as legitimate. Discarded one false-positive citer hit (標識, which cites the unrelated character 識, not 誌). Replaced the malformed `# Notes` heading with a proper 4-bullet section and `## Words`.

**Words cross-check** (2 ground-truth hits via manual grep): added the self-referential `stand_in` [[標誌]] and [[雑誌]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 障 (5147; 1840 characters remaining).

### 2026-08-07, iteration 660 — [[characters/障|障]]

Confirmed `graphemic_classification: 章` via domain knowledge (形声, 阜 semantic "mound, earthworks" + 章 phonetic zhāng — "a defensive rampart," extended to "to shield, block, obstruct, barricade") and `mc_id: 2425` locally (`lookup/CC/CC 2000.md` line 446 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Discarded six false-positive citer hits (不安, 参入, 姑丈, 空中, 自閉症, and chengyu 魑魅罔両, none citing 障 in their own frontmatter). Replaced the malformed `# Notes` heading with a proper 4-bullet section and `## Words`.

**Words cross-check** (3 ground-truth hits via manual grep): added the self-referential `stand_in` [[障碍]], [[故障]], and [[白内障]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 蒸 (char) (5148; 1839 characters remaining).

### 2026-08-07, iteration 661 — [[characters/蒸 (char)|蒸]]

Confirmed `graphemic_classification: 烝` via domain knowledge (形声, 艸 semantic "plant," originally hemp stalks used as kindling, + 烝 phonetic zhēng — "to steam, rise as vapor," from burning stalks producing rising smoke/steam) and `mc_id: 2105` locally (`lookup/CC/CC 2000.md` line 114 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Fixed a component link pointing to a nonexistent `烝 (char)` page — corrected to the real bare-glyph page `[[烝]]`. Discarded three false-positive citer hits (人称, 汽水, 汽車, none citing 蒸 in their own frontmatter). Replaced the malformed `# Notes` heading with a proper 4-bullet section.

**Words cross-check** (3 ground-truth hits via manual grep): added the self-referential `stand_in` [[蒸]] and [[蒸汽]], and confirmed the existing [[蒸溜]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 憲 (5149; 1838 characters remaining).

### 2026-08-07, iteration 662 — [[characters/憲|憲]]

This page's Notes/SKIP/CC-rank bullets were already mostly correct and complete (a rarer case this session), needing only smaller fixes: filled the empty `pos` field (`名詞`); confirmed `graphemic_classification: 害` and `mc_id: 1082` both correct via domain knowledge and local lookup (`lookup/CC/CC 1000.md` line 87); fixed two broken component links (`[[心]]` and `[[害 (char)]]`, neither pointing to the pages that actually exist — corrected to `[[心 (char)|心]]` and `[[害]]` respectively). Alias `宪` (simplified) confirmed legitimate. Discarded four false-positive citer hits (攘夷, 法律, and chengyu 尊王攘夷/盛衰栄辱, none citing 憲 in their own frontmatter). Reordered the misplaced `## Words` heading (missing its own blank line separator) and corrected a wrong ruby on [[憲法]] (ㄏㄝㄋㄏㄚㄎ → the word page's own correct ㄏㄝㄋㄈㄚㄆ).

**Words cross-check** (2 ground-truth hits via manual grep, matching the page's existing entries): added the `(stand-in for 憲)` tag to [[憲法]] and confirmed [[立憲]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 担 (5150; 1837 characters remaining).

### 2026-08-07, iteration 663 — [[characters/担|担]]

Confirmed `graphemic_classification: 旦` via domain knowledge (形声, 手 semantic "hand" + 旦 phonetic dàn — "to carry on a pole across the shoulder," extended to "to shoulder, bear, take responsibility"). **Fixed a fabricated, wildly out-of-range `mc_id`**: stored as `9707`, far beyond the corpus's actual ~4000-entry ceiling; searched all four `lookup/CC/CC *.md` files and found 担 recorded only under its traditional form 擔 at `CC 3000.md` line 490 — corrected `mc_id` to `3469`. **Found and removed five fabricated Words entries**: 担架, 担当, 担保, 負担, and 分担 were listed as bare, unlinked bullets, but none of these word pages exist anywhere in `words/` — verified each individually before removing rather than assuming; per vault convention, creating the missing pages is out of scope for character-page work, so they were dropped rather than invented. Fixed two broken component links (`[[手]]` and `[[旦 (char)]]`, neither pointing to the pages that actually exist) — corrected to `[[Radical 064|手]]` and `[[旦]]`.

**Words cross-check** (2 real ground-truth hits via manual grep, down from the 6 originally listed): added the self-referential `stand_in` [[荷担]] and confirmed [[担任]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 納 (char) (5151; 1836 characters remaining).

### 2026-08-07, iteration 664 — [[characters/納 (char)|納]]

Confirmed `graphemic_classification: 内` via domain knowledge (形声, 糸 semantic "thread," implying admission/intake, + 内 phonetic nèi — "to receive, accept, admit," extended to "to pay dues, submit") and `mc_id: 899` locally (`lookup/CC/CC 0000.md` line 929 — correct, no fix needed). Filled the empty `pos` field (`事詞`). Alias `纳` (simplified) confirmed legitimate. Fixed a broken component link pointing to a nonexistent `内 (char)` page — corrected to the real bare-glyph page `[[内]]`. Discarded fourteen false-positive citer hits (丹金, 杜金, 灰色, 達金, 貢品, 邁金, 鹸素, 西博金, 居里金, 愛因金, 柏克金, 羅倫金, 美洲金, 莫斯素, and chengyu 李下瓜田/海闊天空 — the largest false-positive count this session, since 納 appears throughout the vault's periodic-table naming-convention prose without being an actual constituent of most of those compound names). Replaced the malformed `# Notes` heading with a proper 4-bullet section.

**Words cross-check** (2 real ground-truth hits beyond self via manual grep): added the self-referential `stand_in` [[納]] and [[帰納]], confirmed the existing [[田納素]]. **Chengyu**/**Derived Characters**: no real hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 縦 (char) (5152; 1835 characters remaining).

### 2026-08-07, iteration 665 — [[characters/縦 (char)|縦]]

Confirmed `graphemic_classification: 從` via domain knowledge (形声, 糸 semantic "thread," implying a loosened, unchecked thread, + 從 phonetic — "to release, let loose," extended to "unrestrained, arbitrary, selfish," and via a separate extension "lengthwise, vertical") and `mc_id: 1065` locally (`lookup/CC/CC 1000.md` line 70, recorded under the traditional form 縱 — correct, no fix needed). `pos` was already correctly filled (`性詞`). Alias `縱` (traditional) confirmed legitimate. Fixed a broken component link pointing to a nonexistent `從 (char)` page — the vault has no page for 從 at all, only its shinjitai variant 従; corrected to `[[従 (char)|從]]`. Discarded one false-positive citer hit (権謀, not citing 縦 in its own frontmatter). Replaced the malformed `## Notes` heading with a proper 4-bullet section.

**Words cross-check** (1 real ground-truth hit beyond self via manual grep): added the self-referential `stand_in` [[縦]], confirmed the existing [[縦縞]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 蚕 (char) (5153; 1834 characters remaining).

### 2026-08-07, iteration 666 — [[characters/蚕 (char)|蚕]]

**Fixed swapped semantic/phonetic roles and a fabricated `mc_id`**: the Notes prose labeled 天 as semantic ("insect" — 天 does not mean insect) while omitting the true semantic component 虫 entirely. Corrected via domain knowledge to the standard analysis: 虫 semantic ("insect") + 天 phonetic — though 天 is not sound-preserving here but a shape-based shinjitai/simplified substitution for the traditional phonetic 朁, the same simplification-substitution pattern established earlier this session on 摂/耳, 沢/尺, and 蒸/烝. `mc_id` was stored as `5680`, far beyond the corpus's actual ~4000-entry ceiling; corrected to `1906`, 蚕's real entry recorded under the traditional form 蠶 (`lookup/CC/CC 1000.md` line 947). Filled the empty `pos` field (`名詞`). Alias `蠶` (traditional) confirmed legitimate. Confirmed the `hanmun_edu_level: 名` → `Korean Name ㅊ` lookup-file mapping (matching 蚕's Korean reading 천), consistent with 采/嘆's precedent earlier this session. Dropped an ad hoc "Dropped from the Korean HS list in 2000" line and replaced with the standard 4-bullet structure.

**Words cross-check** (2 ground-truth hits via manual grep): added the self-referential `stand_in` [[蚕]] and [[蚕箔]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 宝 (5155; 1833 characters remaining).

### 2026-08-07, iteration 667 — [[characters/宝|宝]]

Confirmed `graphemic_classification: 缶` via domain knowledge (Shuowen: 从宀从玉从貝，缶聲 — 宀 "roof, house" + 玉 "jade" + 貝 "cowrie shell, money," valuables kept within a house, + phonetic 缶) and `mc_id: 778` locally (`lookup/CC/CC 0000.md` line 805, recorded under the traditional form 寶 — correct, no fix needed). Noted that 宝 (the simplified/shinjitai form) drops both 貝 and the 缶 phonetic shape entirely, retaining only 宀+玉 — the frontmatter field records 缶 as historically/etymologically the phonetic of the character's identity (via 寶), not as a shape visibly present in this specific simplified glyph, distinct from the 蚕/天 and 摂/耳 pattern where the substitute shape IS visibly present. Filled the empty `pos` field (`名詞`). Alias `寶` (traditional) confirmed legitimate. Discarded three false-positive citer hits (書道, 珊瑚, 軽歌劇, none citing 宝 in their own frontmatter). Rewrote a casual, non-standard Notes line ("Korean lists the meaning as 寶貝") into the standard 4-bullet structure.

**Words cross-check** (2 ground-truth hits via manual grep): added the self-referential `stand_in` [[宝物]], confirmed the existing [[七宝]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 盟 (5156; 1832 characters remaining).

### 2026-08-07, iteration 668 — [[characters/盟|盟]]

Confirmed `graphemic_classification: 明` via domain knowledge (形声, 皿 semantic "vessel," implying the blood-oath vessel used in covenant-swearing ceremonies, + 明 phonetic méng — "covenant, alliance, oath") and `mc_id: 708` locally (`lookup/CC/CC 0000.md` line 735 — correct, no fix needed). Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Discarded ten false-positive citer hits (血, 剣道, 国連, 弓道, 欧洲, 国民党, 連合, and chengyu Biblical Chengyu/尊王攘夷/遠交近攻, none citing 盟 in their own frontmatter). Replaced the malformed `# Notes` heading with a proper 4-bullet section.

**Words cross-check** (3 ground-truth hits via manual grep): added the self-referential `stand_in` [[連盟]], [[盟誓]], and [[越盟]]. **Chengyu** (1 ground-truth hit): added [[血誓盟約]] (a Biblical chengyu). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 汽 (5157; 1831 characters remaining).

### 2026-08-07, iteration 669 — [[characters/汽|汽]]

Confirmed `graphemic_classification: 気` via domain knowledge: verified this reflects 汽's real phonetic 气 (qì, an ancient pictograph of rising vapor/clouds), which has no standalone vault page — the vault instead points to its nearest existing page, [[気 (char)|気]] (the shinjitai form built on the same 气 root), the same "nearest existing relative" pattern already established this session (e.g. 従 standing in for 從 on 縦). **Fixed a fabricated, wildly out-of-range `mc_id`**: stored as `10366`, far beyond the corpus's actual ~4000-entry ceiling; searched all four `lookup/CC/CC *.md` files and confirmed 汽 appears nowhere in the corpus — corrected to `0`. Filled the empty `pos` field (`名詞`). No aliases to assess (field empty). Confirmed two lookup-file conventions already established this session: `hanmun_edu_level: 名` → `Korean Name ㄱ` (matching 汽's Korean reading 기) and the `joyo_level` grade-number suffix on `Jōyō - Kyōiku`. Discarded two false-positive citer hits (工廠, 火車, neither citing 汽 in its own frontmatter). Replaced the malformed `# Notes` heading with a proper 4-bullet section.

**Words cross-check** (4 ground-truth hits via manual grep): added the self-referential `stand_in` [[蒸汽]], confirmed the existing [[汽水]] and [[汽車]], and added [[汽油]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 社 (5158; 1830 characters remaining).

### 2026-08-07, iteration 670 — [[characters/嘱|嘱]]

Backfill iteration: the sweep's running pointer had already passed 嘱, but a fresh `grep -L` scan surfaced it at `danayo_id` 4322 — the lowest unperfected ID in the vault. Confirmed `graphemic_classification: 属` via Wiktionary (形声, ⿰口属: semantic 口 "mouth," the organ of spoken command + phonetic 属; 嘱 is the simplified/shinjitai form of 囑). **Filled the blank `mc_id`**: searched all four `lookup/CC/CC *.md` files under both 嘱 and traditional 囑 — absent from the corpus, so set to `0` per convention. All five modern readings verified against Wiktionary (zhǔ / juk1 / 촉 / SHOKU / chúc); `kwin: false` correct (Dan'a'yo 족 ≠ Sino-Korean 촉). Confirmed `hanmun_edu_level: 名` → `Korean Name ㅊ` (촉) per the convention established on 汽. Discarded two false-positive citer hits (足, 受託 — both mention 嘱 only in prose, neither cites it in frontmatter). Replaced the bare two-link `## Notes` stub with a proper 4-bullet section.

**Words cross-check** (1 ground-truth hit): confirmed [[嘱託]] as the sole constituent-citer and annotated it as stand-in. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none for 嘱 itself; the reverse direction (嘱 listed under [[属]]'s Derived Characters) was already in place.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 社 (5158; 1829 characters remaining).

### 2026-08-07, iteration 671 — [[characters/社|社]]

All five modern readings verified against Wiktionary (shè / se5 / 사 / SHA・JA / xã), as were the MC pair and composition. **Two field corrections**: filled the empty `pos` (`名詞`), and corrected `korean_native` from 토지신 ("earth god" — a gloss of the historical meaning) to 모일, the canonical 교육한자 훈 for 社 (모일 사), matching how the field stores the standard 훈 elsewhere (cf. 부탁할 on 嘱). **Two analyses documented, not changed**: Wiktionary classes 社 as 会意 （示 "altar" + 土 "soil"), so bullet 1 is written as 会意 with 土 noted as near-phonetic (OC \*l̥ʰaːʔ vs. 社 \*ɦljaːʔ, etymological doublet per Takashima) — consistent with the stored `graphemic_classification: 土`. And Wiktionary/Baxter give 社's fanqie initial as 常 （常者切）, but the vault merges 常 into 聲 船 (no 聲 常 page exists; 常 itself is listed under 聲 船), so `middle_chinese_initial: ʑ` / 聲 船 stands as vault-correct. `mc_id: 673` verified at `lookup/CC/CC 0000.md` line 697. `stroke_count: 8` / SKIP-1-5-3 follow the Kangxi-style count (礻 as full 示 = 5); 社 confirmed listed in `SKIP-1-5-3.md`. Discarded false-positive citers (交, 会, 偕者, 募集, 和諧, 嘱託, 基盤, 基礎, 妨害, 安寧, 思考, 東芝, 祭物, 通信, 事務所, 官僚主義 in words/; 尊敬父母, 愛偕者神, 成家立業, 欲求不満, 舎本逐末 in chengyu/ — all prose mentions, none citing 社 in frontmatter). Replaced the malformed `# Notes` heading with a proper 4-bullet section. **Side fix**: [[宝]]'s stroke link (`Stroke%208.md`) was broken — real file is zero-padded `Stroke 08.md`; corrected (same fix applied within 社's own bullets).

**Words cross-check** (8 ground-truth hits via frontmatter `characters:` lists — two formats exist in the vault, inline `[社, …]` and one-space `- 社`, both had to be searched): confirmed stand-in [[社会]]; added [[会社]], [[社交]], [[会社員]], [[社会学]], [[社会科学]]; ruby-ified the previously bare [[社会主義]] and [[社会科]] entries. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 勿 (5159; 1828 characters remaining).

### 2026-08-07, iteration 672 — [[characters/勿 (char)|勿]]

象形 analysis (blood on a knife; original character of 刎, OC \*mɯnʔ; jiajie for "do not," OC \*mɯd, since oracle bones) re-confirmed verbatim against Wiktionary, as were all readings (wù / mat6 / BUTSU・BOTSU・MOCHI / 말 물 / vật・vặt・vất — all three Vietnamese readings real). `mc_id: 585` verified at `lookup/CC/CC 0000.md` line 606. Initial kept as 聲 微 (traditional 字母 classification; Wiktionary gives 切韻-era 明, but 物韻 div-III closed labials are 微母 in 等韻 — same vault-internal convention pattern as the 船/常 merger noted on 社). **Three field fixes**: repaired the broken YAML (scalar-then-list `japanese_native`; comma-joined single-string `vietnamese` — split into proper three-item list); corrected `kwin: true → false` (Dan'a'yo 묻 ≠ Sino-Korean 물). Folded the stray "more emphatic than [[別]]" note into bullet 1 and replaced the CC stub links with the full 4-bullet section. `hanmun_edu_level: 中` → `Korean MS`; `joyo_level: 日本人名用漢字` → `Jinmeiyō`.

**Words cross-check** (1 ground-truth hit — nearly missed: [[勿]]'s own word file cites it as `- 勿 (char)`, with the disambiguator suffix, which plain `- 勿` greps miss): listed with the `[勿](words/勿.md)` path link. **Chengyu**: no hits — correctly omitted. **Derived Characters** (2 ground-truth hits via `graphemic_classification: 勿`): added [[没 (char)|没]] and [[物 (char)|物]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 烏 (5160; 1827 characters remaining).

### 2026-08-07, iteration 673 — [[characters/烏|烏]]

象形 classification confirmed via domain knowledge (pictograph of a crow — 鳥 minus the eye-stroke; the Shuowen's 孝鳥). `mc_id: 837` verified at `lookup/CC/CC 0000.md` line 867. `kwin: true` correct this time (Dan'a'yo 오 = Sino-Korean 오). Filled the empty `pos` (`名詞`). Replaced the malformed `# Notes` + stray unheaded word list with the proper 4-bullet Notes section; the three stray word entries ([[烏魯斉]], [[烏賊]], [[烏梅]]) were all real citers and were absorbed into the new Words section.

**Words cross-check** (7 ground-truth hits): the stray three plus the missing stand-in [[烏鳥]] itself, [[烏龍]], [[烏龍茶]], and [[烏龍麺]]. **Chengyu**: no hits — correctly omitted. **Derived Characters** (1 hit via `graphemic_classification: 烏`): added [[嗚]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 郡 (5162; 1826 characters remaining).

### 2026-08-07, iteration 674 — [[characters/郡 (char)|郡]]

All verified against Wiktionary: 形声 (semantic 邑 "city" + phonetic 君, OC \*ɡluns), readings (jùn / gwan6 / 군 / GUN・KUN / all five Hán Nôm tone variants quận・quặn・quấn・quẩn・quạnh — real, kept), MC pair (群 + 文, 渠運切). `mc_id: 232` verified at `lookup/CC/CC 0000.md` line 244. `kwin: true` correct (군 = 군). Filled the empty `pos` (`名詞`). `hsk_level: 無` → HSK link omitted from bullet 4. Replaced the malformed `# Notes` with the proper 4-bullet section. Discarded one false-positive chengyu hit (画龍点睛 — 郡 appears only in the source-title prose 《吳郡志》, not as a constituent).

**Words cross-check** (1 ground-truth hit — a third frontmatter format this time: scalar `characters: 郡 (char)`): listed [[郡]] itself as stand-in. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 裏 (5163; 1825 characters remaining).

### 2026-08-07, iteration 675 — [[characters/裏|裏]]

**Real bug found and fixed**: `mc_id: 2875` was wrong — 裏 is actually ranked 1646th, in `lookup/CC/CC 1000.md` line 675 (the stored value appears in none of the four CC files; corrected and bullet written with the true rank). **Repaired the unresolved `phonetic [[]]` link** in the graphemic bullet → `[[里 (char)|里]]` (OC \*rɯʔ, matching both the stored `graphemic_classification: 里` and the bullet's own OC annotation). The page's long essay on 裏's two semantic layers (interiority vs. lining/reversal) was kept intact — restructured so the four fixed bullets lead the Notes section, with the essay following as its own subsections; trailing CC stub links removed. `boundedness` left empty: the field appears nowhere in `checklist_characters.md`'s required-frontmatter template, so it neither blocks nor was fabricated. Readings (lǐ / leoi5 / 리 / RI / lí) and `kwin: true` (리 = 리) confirmed by inspection. Discarded the essay's table compounds (箱裏, 心裏, 夢裏, 夜裏, 宮裏, 裏衣, 裏話, 裏通, 裏表) — illustrative examples, not vault word files.

**Words cross-check** (2 ground-truth hits): stand-in [[裏面]] and [[足裏]] (the essay's lone real vault word). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 阿 (5164; 1824 characters remaining).

### 2026-08-07, iteration 676 — [[characters/阿 (char)|阿]]

Closest-to-complete page so far this run: graphemic bullet already correct in substance (形声, 阜 + 可, OC \*qaːl / \*kʰaːlʔ) but with an empty `""` semantic gloss (filled: "mound, hill") and a bare `[[可]]` link that resolves away from the character page (fixed to `[[可 (char)|可]]`). Filled the empty `pos` (`感詞`, matching the word page's own POS). `mc_id: 1089` verified at `lookup/CC/CC 1000.md` line 94. `kwin: true` correct (아 = 아). Folded the stray "Dropped from the Korean HS list in 2000" note into the levels bullet as the explanation for `hanmun_edu_level: 名` → `Korean Name ㅇ`. Added the missing SKIP/Stroke and MC-rank bullets; removed the trailing CC stub links. Readings (ā / aa3 / 아 / A / a・à) confirmed by inspection — all standard.

**Words cross-check** (3 ground-truth hits — all cited with the `(char)` suffix): stand-in [[阿]] itself (path-linked to `words/阿.md`), plus the missing [[阿鼻]]; confirmed [[阿僧祇]]. **Chengyu**: confirmed [[阿鼻叫喚]] (ruby-ified with gloss). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 卒 (5165; 1823 characters remaining).

### 2026-08-07, iteration 677 — [[characters/卒|卒]]

Verified against Wiktionary: 会意 (衣 "clothes" + identification mark — the tagged garment of conscripts; five oracle-bone forms documented), readings (zú / zeot1 / 졸 / SOTSU / tốt), both Guangyun readings (子聿切 術韻 "finish" — the vault's stored pair — and 臧没切 沒韻 "soldier"; they merge in all modern languages, noted parenthetically in bullet 3). `mc_id: 166` verified at `lookup/CC/CC 0000.md` line 174. `kwin: false` correct (줃 ≠ 졸). **Vietnamese caveat logged, not changed**: the stored 15-reading list is all real per Wiktionary's Hán/Nôm citations *except* `chụt`, which appears in none of them (likely a mis-transcription of `chút` or `chột`, both attested) — left in place per the don't-blank-unverifiable-long-tail-data principle, flagged here for the user's call. Replaced the malformed `# Notes` + stray word entry with the proper 4-bullet section.

**Words cross-check** (2 ground-truth hits): stand-in [[兵卒]] and the stray-listed [[卒業]]. **Chengyu**: no hits — correctly omitted. **Derived Characters** (4 hits via `graphemic_classification: 卒`): added [[粋]], [[翠]], [[酔 (char)|酔]], [[砕 (char)|砕]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 桃 (5166; 1822 characters remaining).

### 2026-08-07, iteration 678 — [[characters/桃|桃]]

形声 (木 + 兆) confirmed via domain knowledge; readings (táo / tou4 / 도 / TOU・もも / đào) all standard. `mc_id: 1555` verified at `lookup/CC/CC 1000.md` line 580. `kwin: false` correct (닷 ≠ 도). Filled the empty `pos` (`名詞`). The page had its word entries split across a malformed `# Notes` stub (桃果, 桃子, 桃金 — the last with an odd "abbreviation for" phrasing, normalized to the plain gloss "erbium") and a partial `## Words` (桃山, 桃色) — consolidated into one proper section. `joyo_level: 高等` → `Jōyō - Kōtō` (no grade-number suffix, unlike Kyōiku).

**Words cross-check** (7 ground-truth hits): confirmed the five pre-listed, added the missing [[桃月]] and [[桜桃]]. **Chengyu**: confirmed [[鼠世桃源]]. **Derived Characters**: no hits (its phonetic 兆 parents the series, not 桃 itself) — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 滴 (5167; 1821 characters remaining).

### 2026-08-07, iteration 679 — [[characters/滴 (char)|滴]]

Readings (dī / dik6 / 적 / TEKI・しずく / tích et al.) confirmed by inspection. **Phonetic documented, not changed**: the true phonetic of 滴 is 啇, which has no vault page — the vault records `graphemic_classification: 帝` (the graph 啇 descends from 帝) and does so consistently ([[摘 (char)|摘]] stores the same), so bullet 1 explains the 啇→帝 stand-in per the established 气→気 nearest-relative pattern. `mc_id: 5855` retained per the long-tail policy: absent from all four local CC files but beyond their ~4000-entry ceiling — unverifiable ≠ fabricated. Filled the empty `pos` (`事詞` — the vault's verb class, 484 uses vs. legacy 動詞's 13). `kwin: false` correct (덕 ≠ 적). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit — scalar `characters: "滴 (char)"` format): listed [[滴]] itself as stand-in. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 漏 (5168; 1820 characters remaining).

### 2026-08-07, iteration 680 — [[characters/漏 (char)|漏]]

**Real bug found and fixed**: `mc_id: 1667` was off by one — 漏 is ranked 1668th at `lookup/CC/CC 1000.md` line 697. 形声 (水 + 屚, the leaking-roof phonetic — no vault page, left unlinked like 啇 on 滴) and readings (lòu / lau6 / 루 / ROU / lậu et al.) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (롯 ≠ 루). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (3 ground-truth hits): confirmed [[滲漏]] and [[漏洩]], added the missing stand-in [[漏]] itself. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 慰 (5169; 1819 characters remaining).

### 2026-08-07, iteration 681 — [[characters/慰|慰]]

**Second off-by-one `mc_id` in a row**: stored `2330`, actual rank 2331 (`lookup/CC/CC 2000.md` line 348) — same one-low pattern as 漏 (1667→1668) last iteration, suggesting a batch of one-low ranks crept in somewhere upstream; worth a dedicated `lint CC`-style sweep later. 形声 （心 + 尉) and readings (wèi / wai3 / 위 / I・なぐさ / uý・ủi) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (외 ≠ 위). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (2 ground-truth hits): stand-in [[慰安]] (already stray-listed) plus the missing [[安慰]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 微 (5170; 1818 characters remaining).

### 2026-08-07, iteration 682 — [[characters/微|微]]

Verified against Wiktionary: the stored `graphemic_classification: 象形` is defensible but tells only part of the story — the oracle-bone core 𡵂 was indeed a pictograph (person with long flowing hair, borrowed for sound), with 攵 ("hand with tool" — combing fine hairs → "minute") added as semantic and 彳 later for the action sense; bullet 1 now tells the full three-stage story with both Kangxi-radical components linked per the radical-linking rule. Readings (wēi / mei4 / 미 / BI・かす / vi) all confirmed; `korean_native: 작을` matches the standard eumhun 작을 미. `mc_id: 452` verified at `lookup/CC/CC 0000.md` line 470. Fixed the `english` typo "miniture" → "miniature". Filled the empty `pos` (`性詞`). `kwin: false` correct (뮈 ≠ 미). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit): stand-in [[微小]]. **Chengyu**: no hits — correctly omitted. **Derived Characters** (2 hits): added [[徽]] and [[薇]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 腰 (5171; 1817 characters remaining).

### 2026-08-07, iteration 683 — [[characters/腰|腰]]

形声 (肉 + 要) confirmed via domain knowledge — with the nice detail that 要 was itself the original "waist" graph (figure with hands on hips), so 腰 is the re-disambiguated form. `mc_id: 1926` verified exactly (no off-by-one this time) at `lookup/CC/CC 1000.md` line 967. Readings (yāo / jiu1 / 요 / YOU・こし / yêu et al.) confirmed by inspection. Filled the empty `pos` (`名詞`). `kwin: false` correct (욧 ≠ 요). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (2 ground-truth hits): stand-in [[腰部]] and [[腰骨]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 薄 (5172; 1816 characters remaining).

### 2026-08-07, iteration 684 — [[characters/薄|薄]]

Filled the empty `pos` (`性詞`). Graphemic bullet kept its correct substance (形声, 艸 + 溥, OC \*baːɡ / \*pʰaːʔ~\*paːɡ) but with the empty `""` semantic gloss filled ("grass, plants") and `[[艹]]` converted to the radical link `[[Radical 140|艹]]` per the radical-linking rule. `mc_id: 640` verified at `lookup/CC/CC 0000.md` line 664. The stored 鈬合 final looked suspicious (薄 is 鐸開 in traditional taxonomy) but checks out as vault-internal: `韻 鈬合.md` documents 薄 explicitly — labial initials drop the w-glide, landing on ㄅㄚㄎ — so bullet 3 cites that split. `kwin: true` correct (박 = 박). Mandarin's two-reading storage `"báo bó"` correct (colloquial báo, literary bó). **Aliases flagged, not changed**: 鉑/铂 (platinum) are not orthographic variants of 薄 by any external standard — possibly a deliberate Dan'a'yo borrowing, so left in place for the user's call. Normalized the chengyu entry's odd path-link (`/chengyu/佳人薄命.md`) and dash gloss to the standard ruby-wikilink format. Removed the trailing CC stub links (one malformed as `[[../lookup/...]]` inside a wikilink).

**Words cross-check** (8 ground-truth hits): confirmed the five pre-listed ([[薄命]], [[薄弱]], [[薄荷]], [[薄膜]], [[菲薄]] — the first three ruby-ified), added the missing stand-in [[希薄]] itself plus [[浅薄]] and [[刻薄]]. **Chengyu**: confirmed [[佳人薄命]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 隔 (5173; 1815 characters remaining).

### 2026-08-07, iteration 685 — [[characters/隔 (char)|隔]]

**Two field fixes**: `graphemic_classification: 象形` contradicted the page's own (correct) 形声 bullet — semantic 阝（阜） + phonetic 鬲 — so the field was corrected to `鬲` (no vault page for 鬲; left unlinked in the bullet per the 啇/屚 pattern, which also resolves a would-be blocker: the old `[[鬲]]` was an unresolved component link). And **third one-low off-by-one `mc_id` of this run**: stored `2210`, actual 2211 (`lookup/CC/CC 2000.md` line 224) — after 漏 and 慰, the upstream one-low batch hypothesis is now three for three on the 2xxx-range pages; a `lint CC` sweep is increasingly warranted. `pos: 副用名詞` was already filled (unusual class — left as the user's classification). Folded the stray "Added to the Korean HS list in 2000" note into the levels bullet (mirror of 阿's "dropped" note). `kwin: false` correct (각 ≠ 격). Readings (gé / gaak3 / 격 / KAKU・へだ(てる) / cách) confirmed by inspection. Semantic gloss adjusted "wall" → "mound, earthen wall" with the proper `[[Radical 170|阝]]` link.

**Words cross-check** (7 ground-truth hits — all but 隔世紀 cited with the `(char)` suffix): the two pre-listed ([[間隔]] glossless, [[words/隔]] as a malformed link — both normalized) plus the missing [[隔年]], [[隔月]], [[隔日]], [[隔週]], [[隔世紀]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 埋 (5174; 1814 characters remaining).

### 2026-08-07, iteration 686 — [[characters/埋|埋]]

**Fourth one-low off-by-one `mc_id`**: stored `2090`, actual 2091 (`lookup/CC/CC 2000.md` line 96) — the pattern now covers every 2xxx-rank page touched this run (2090, 2210, 2330); a `lint CC` sweep of that range is definitely warranted. **Reclassified the phonetic**: `graphemic_classification: 貍` pointed at a character with no vault page — the written graph's actual phonetic is 里 (Wiktionary's analysis too), with 貍 belonging to the older Shuowen form 薶 (already recorded in `aliases`); corrected to `里`, documented in the bullet, and added 埋 to [[里 (char)|里]]'s Derived Characters (which listed 厘/浬/狸/理/裏/鯉 but not 埋 — the missing reverse link). Filled the empty `pos` (`事詞`). `kwin: false` correct (며 ≠ 매). Readings (mái / maai4 / 매 / MAI・BAI / mai et al.) confirmed by inspection. Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (2 ground-truth hits): stand-in [[埋藏]] (already stray-listed) plus [[埋葬]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 恐 (5175; 1813 characters remaining).

### 2026-08-07, iteration 687 — [[characters/恐|恐]]

Verified against Wiktionary: readings (kǒng / hung2 / 공 / KYOU / khủng — and `thứ` confirmed as a real Nôm reading), MC pair （溪 + 鍾， 丘隴切), and composition. **Corrected `graphemic_classification: 鞏 → 巩`**: Wiktionary analyzes the modern form as 心 semantic + 巩 phonetic （鞏 is 巩 + 革, one derivative too deep; neither has a vault page, so the bullet leaves 巩 as plain text per the 啇/屚 pattern). `pos: 事詞` was already filled. `kwin: false` correct (콩 ≠ 공). `mc_id: 432` verified at `lookup/CC/CC 0000.md` line 450 — exact, consistent with the off-by-ones being confined to the 2000-range. The page's sections were jumbled (a word under `## Chengyu`, CC stubs mid-list, 恐怖 orphaned at the bottom) — rebuilt in standard order.

**Words cross-check** (5 ground-truth hits): stand-in [[恐慌]] (orphan at the file's foot), [[恐怖]], [[恐惧]], [[恐龍]], [[恐恐]]. **Chengyu**: confirmed [[戦戦恐恐]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 召 (5176; 1812 characters remaining).

### 2026-08-07, iteration 688 — [[characters/召|召]]

形声 （口 + 刀） and readings (zhào / ziu6 / 소 / SHOU / triệu et al.) confirmed by inspection. `mc_id: 425` verified at `lookup/CC/CC 0000.md` line 443 — exact again (0xxx range stays clean). Stored initial 聲 船 stands (召's zhào reading is traditionally 澄母, shào 禪母; the vault merges that territory into 聲 船， same convention as 社）. Filled the empty `pos` (`事詞`). `kwin: false` correct (숏 ≠ 소). Replaced the malformed `# Notes` stub with the proper 4-bullet section; normalized the stray 召集 gloss's missing space ("summon,convene" → "summon, convene").

**Words cross-check** (1 ground-truth hit): stand-in [[召集]]. **Chengyu** (1 hit — a Biblical chengyu): added [[多召少選]]. **Derived Characters** (9 hits — the biggest series this run): added [[昭 (char)|昭]], [[沼]], [[詔]], [[招]], [[貂]], [[劭]], [[紹]], [[邵]], [[超 (char)|超]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 吐 (5178; 1811 characters remaining).

### 2026-08-07, iteration 689 — [[characters/吐 (char)|吐]]

**Fifth off-by-one `mc_id`, and it breaks the 2xxx-range theory**: stored `1523`, actual 1524 (`lookup/CC/CC 1000.md` line 549) — the one-low batch reaches into the 1xxx range too. **Two more field corrections**: `pos: 性詞 → 事詞` ("spit, vomit, cough up, spew" are verbs, not adjectives), and the old levels bullet's "HSK 3" matched neither the frontmatter (`"2"`) nor the lookups — verified the vault convention first: the stored level follows the `: N` constituent-listing (吐 has `[[吐 (char)]]: 1` in `Old HSK 2.md`, exactly like perfected 薄's `"2"` despite its numbered entry living in `Old HSK 5.md`), so the frontmatter stands and the bullet now links Old HSK 2. Old-format bullets (bare wikilinks for SKIP/Stroke/levels, CC stubs) rebuilt as the standard 4; Swadesh #96/97 note folded into bullet 1. `kwin: true` correct (토 = 토). Discarded one false-positive chengyu hit (文質彬彬 — 吐 appears only inside an example sentence, 談吐得體).

**Words cross-check** (2 ground-truth hits): stand-in [[吐]] itself and [[呕吐]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 拒 (5179; 1810 characters remaining).

### 2026-08-07, iteration 690 — [[characters/拒|拒]]

**Sixth one-low off-by-one `mc_id`**: stored `1809`, actual 1810 (`lookup/CC/CC 1000.md` line 847) — second hit in the 1xxx range after 吐. 形声 （手 + 巨） and readings (jù / keoi5 / 거 / KYO・KU / cự) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (교 ≠ 거). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit): stand-in [[抗拒]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 磨 (5180; 1809 characters remaining).

### 2026-08-07, iteration 691 — [[characters/磨 (char)|磨]]

**Seventh one-low off-by-one `mc_id`**: stored `2913`, actual 2914 (`lookup/CC/CC 2000.md` line 955). Also repaired the comma-joined single-string `vietnamese` ("ma, mài" → proper two-item list — same YAML flaw as 勿） and filled the empty `pos` (`事詞`). Bullet 2 carried the syllable link mid-line — moved to the end of bullet 3 per convention, with the rank text supplied. `kwin: true` correct (마 = 마). 形声 （石 + 麻） already correct. Both listed chengyu verified as real citers (both cite `- 磨 (char)` — the suffix form again, which my first chengyu grep pattern missed; pattern widened).

**Words cross-check** (3 ground-truth hits): confirmed [[磨耗]], added the missing stand-in [[磨]] itself and [[琢磨]]. **Chengyu**: confirmed [[磨穿鉄硯]] and [[切磋琢磨]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 穫 (5181; 1808 characters remaining).

### 2026-08-07, iteration 692 — [[characters/穫|穫]]

**Eighth one-low off-by-one `mc_id`**: stored `3063`, actual 3064 (`lookup/CC/CC 3000.md` line 69) — now confirmed in the 1xxx, 2xxx, and 3xxx ranges. (Mid-edit typo of mine — `3063-pla` — caught and corrected to 3064 in the same pass.) 形声 （禾 + 蒦； no vault page for 蒦, left unlinked) and readings (huò / wok6 / 확 / KAKU / hoạch) confirmed by inspection. Bullet 3 notes 穫 falls on the w-glide-*keeping* side of the 鈬合 split (non-labial ɣ → ㄏ⺢ㄎ), complementing 薄's labial glide-drop. Filled the empty `pos` (`事詞`). `kwin: true` correct (확 = 확). Removed the malformed `[[../lookup/...]]` CC stub.

**Words cross-check** (1 ground-truth hit): stand-in [[収穫]] (already listed). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 戚 (5182; 1807 characters remaining).

### 2026-08-07, iteration 693 — [[characters/戚|戚]]

Clean verification: `mc_id: 864` exact at `lookup/CC/CC 0000.md` line 894 (0xxx range still untouched by the off-by-one batch). 形声 （戉 semantic + 尗 phonetic — 尗 has a vault page, linked; the axe→grieving borrowing story explains the stored `慼` alias, now told in the bullet). Readings (qī / cik1 / 척 / SEKI・SOKU / thích) confirmed by inspection. Filled the empty `pos` (`性詞` — "grieving, sorrowful" are adjectives). `kwin: true` correct (척 = 척). Sections were transposed (Words above a malformed `# Notes`) — rebuilt in standard order.

**Words cross-check** (2 ground-truth hits): stand-in [[哀戚]] (already listed) plus the missing [[親戚]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 弄 (5183; 1806 characters remaining).

### 2026-08-07, iteration 694 — [[characters/弄 (char)|弄]]

**Ninth one-low off-by-one `mc_id`**: stored `2397`, actual 2398 (`lookup/CC/CC 2000.md` line 415). 会意 （廾 "two hands" + 玉 "jade" — toying with jade; both components linked as Kangxi radicals per the radical-linking rule) and readings (nòng / lung6 / 롱 / ROU / lộng et al.) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: true` correct (롱 = 롱). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit — scalar `"弄 (char)"` format): stand-in [[弄]] itself. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 替 (5184; 1805 characters remaining).

### 2026-08-07, iteration 695 — [[characters/替|替]]

**Tenth one-low off-by-one `mc_id`**: stored `2891`, actual 2892 (`lookup/CC/CC 2000.md` line 929). 会意 verified via Wiktionary （竝 "two figures side by side" + 曰 — two figures changing places; the 立→夫 simplification noted in the bullet). Readings (tì / tai3 / 체 / TAI・TEI / thế) and eumhun 바꿀 체 all confirmed. Filled the empty `pos` (`事詞`). `kwin: true` correct (체 = 체). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (2 ground-truth hits): added the missing stand-in [[代替]]; confirmed [[交替]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 摘 (5185; 1804 characters remaining).

### 2026-08-07, iteration 696 — [[characters/摘 (char)|摘]]

Readings (zhāi / zaak6 / 적 / TEKI・TAKU・CHAKU / trích) confirmed by inspection. The 帝-for-啇 phonetic stand-in documented in bullet 1 (cross-referencing 滴, where the pattern was established this run). `mc_id: 4839` retained per the long-tail policy — absent from all four local CC files but beyond their ceiling. Filled the empty `pos` (`事詞`). `kwin: false` correct (닥 ≠ 적). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit — scalar `"摘 (char)"` format): stand-in [[摘]] itself. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 升 (5186; 1803 characters remaining).

### 2026-08-07, iteration 697 — [[characters/升 (char)|升]]

象形 (dipper/ladle, cf. 斗) and readings (shēng / sing1 / 승 / SHOU・ます / thăng・thưng) confirmed by inspection. Filled the empty `pos` with `量詞` (matching the word page's own POS — 升 is a measure — rather than the generic 名詞）. `mc_id: 415` verified at `lookup/CC/CC 0000.md` line 433 — exact. `kwin: false` correct (숭 ≠ 승). Sections were transposed (Words above Notes); rebuilt in standard order, folding the "Dropped from the Korean HS list in 2000" note into the levels bullet (`hanmun_edu_level: 名` → `Korean Name ㅅ`, 승) and removing the CC stubs. Fixed my own fresh link before it landed: 斗's page is `斗 (char).md`, so the comparison link is `[[斗 (char)|斗]]`.

**Words cross-check** (3 ground-truth hits): added the missing stand-in [[升]] itself; confirmed [[百升]], [[晋升]]. (Discarded 昇天 — it cites `升天`, not 升.) **Chengyu**: no hits — correctly omitted. **Derived Characters** (1 hit): added [[昇]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 雷 (5187; 1802 characters remaining).

### 2026-08-07, iteration 698 — [[characters/雷 (char)|雷]]

会意 （雨 + 畾； 畾 has no vault page, left unlinked) and readings (léi / leoi4 / 뢰 / RAI・RUI・いかずち / lôi et al.) confirmed by inspection. `mc_id: 989` verified at `lookup/CC/CC 0000.md` line 1022 — exact. Filled the empty `pos` (`名詞`). `kwin: true` correct (뢰 = 뢰). Normalized 雷金's "abbreviation for" phrasing to the plain gloss "thorium" (same cleanup as 桃金 on 桃）. Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (5 ground-truth hits): added the missing stand-in [[雷]] itself and [[魚雷]]; confirmed [[雷電]], [[佛雷素]], [[雷金]]. **Chengyu**: no hits — correctly omitted. **Derived Characters** (2 hits): added [[儡]] and [[塁]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 欺 (5188; 1801 characters remaining).

### 2026-08-07, iteration 699 — [[characters/欺|欺]]

Clean verification: `mc_id: 1265` exact at `lookup/CC/CC 1000.md` line 278. 形声 （欠 + 其） and readings (qī / hei1 / 기 / GI・KI・あざむ / khi) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (키 ≠ 기). Sections were transposed (malformed `# Notes` above Words) — rebuilt in standard order. Discarded one false-positive chengyu hit (羊頭狗肉 — 欺 appears only inside the example sentence 欺世盜名）.

**Words cross-check** (2 ground-truth hits): stand-in [[欺瞞]] plus [[欺𥈞]], the alias variant with its own word file (same 注音 ㄎㄧㄇㄚㄋ, so the two entries cite each other's orthography — both listed). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 臭 (5189; 1800 characters remaining).

### 2026-08-07, iteration 700 — [[characters/臭 (char)|臭]]

Milestone iteration. 会意 （自 "nose" + 犬 "dog" — the keenest smeller) and readings (chòu / cau3 / 취 / SHUU・KYUU / xú・xó) confirmed by inspection. `mc_id: 1773` verified exact at `lookup/CC/CC 1000.md` line 806. Repaired two comma-joined YAML scalars (`japanese_native`, `vietnamese` — same flaw family as 勿 and 磨）. `kwin: false` correct (추 ≠ 취). Kept the bromine-formula note (moved out of bullet position into a standalone line after the four fixed bullets, [[Periodic Table]] link intact). Discarded one false-positive word hit (嗅金 — 臭 appears only in prose explaining the bromine assignment).

**Words cross-check** (4 ground-truth hits): added the missing stand-in [[臭]] itself, [[臭素]], and [[口臭]]; confirmed [[臭膣]]. **Chengyu**: no hits — correctly omitted. **Derived Characters** (1 hit): added [[嗅]] (note the divergent Dan'a'yo reading ㄏ⼜ vs. parent's ㄑㄨ — listed with its own syllable per convention).

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 珠 (5190; 1799 characters remaining).

### 2026-08-07, iteration 701 — [[characters/珠|珠]]

Clean verification: `mc_id: 1266` exact at `lookup/CC/CC 1000.md` line 279 — the very next line after 欺's 1265, both correct. 形声 （玉 + 朱） and readings (zhū / zyu1 / 주 / SHU・たま / châu et al.) confirmed by inspection. Filled the empty `pos` (`名詞`). `kwin: true` correct (주 = 주). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit): stand-in [[珍珠]]. **Chengyu** (1 hit — Biblical): added [[珠投猪前]]. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 渡 (5191; 1798 characters remaining).

### 2026-08-07, iteration 702 — [[characters/渡 (char)|渡]]

`pos: 事詞` was already filled. Clean `mc_id: 1665` at `lookup/CC/CC 1000.md` line 694. 形声 （水 + 度） and readings (dù / dou6 / 도 / TO・わたる・わたす / độ et al.) confirmed by inspection. Repaired two more comma-joined YAML scalars (`japanese_native`, `vietnamese` — four pages with this flaw so far this run: 勿, 磨, 臭, 渡）. `kwin: true` correct (도 = 도). Replaced the malformed `# Notes` stub with the proper 4-bullet section. Discarded two false-positive chengyu hits (呉越同舟 — 渡 inside the related-phrase 共渡難關； 五臓六府 — example sentence only).

**Words cross-check** (1 ground-truth hit): stand-in [[渡]] itself. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 悔 (5192; 1797 characters remaining).

### 2026-08-07, iteration 703 — [[characters/悔|悔]]

Clean verification: `mc_id: 1173` exact at `lookup/CC/CC 1000.md` line 182. 形声 （心 + 毎） and readings (huǐ / fui3 / 회 / KAI・く / hối et al.) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: true` correct (회 = 회). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit): stand-in [[後悔]] only. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 蛇 (5193; 1796 characters remaining).

### 2026-08-07, iteration 704 — [[characters/蛇 (char)|蛇]]

`pos: 名詞` was already filled. Clean `mc_id: 1243` at `lookup/CC/CC 1000.md` line 256. `kwin: true` correct (타 = 타). **Repaired a malformed YAML hybrid** — `japanese_native: へび` scalar followed by a duplicate `  - へび` list item (new flaw variant; fifth YAML repair this run). Restructured the notes into the standard 4-bullet format, preserving the page's rich existing content: the 它-original-pictogram / 蛇-derivative explanation merged into bullet 1 (stored `graphemic_classification: 象形` kept — both analyses documented), and the **ta**-over-**sa** anti-homophony rationale moved to a standalone paragraph after the bullets (same treatment as 臭's bromine note). The two raw `[[Lookup/CC/...]]` wiki-links were absorbed into bullet 3. Discarded two prose-only chengyu hits （魑魅罔両， 破頭傷足 — 蛇 in example prose) and one alternate-name mention （腹行食塵 — "蛇行食土" simplified alternate).

**Words cross-check** (1 ground-truth hit): stand-in [蛇](words/蛇.md) itself. **Chengyu** (1 hit): added [[画蛇添足]]. **Derived Characters** (4 hits): added [[舵]], [[拖]], [[陀]], [[駝]] — all cite `graphemic_classification: "蛇"` because 它 is folded into 蛇 here.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 挑 (5194; 1795 characters remaining).

### 2026-08-07, iteration 705 — [[characters/挑|挑]]

Clean verification: `mc_id: 2673` exact at `lookup/CC/CC 2000.md` line 702. 形声 （手 + 兆） and readings (tiāo / tiu1 / 도 / CHOU・TOU・いど / khiêu et al.) confirmed by inspection. Filled the empty `pos` (`事詞` — verbal gloss "challenge authority"; both citing word pages store the broad `実詞`, character-page verb-class convention wins). `kwin: false` correct (탓 ≠ 도). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (2 ground-truth hits): stand-in [[挑戦]] plus [[挑発]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 冠 (5195; 1794 characters remaining).

### 2026-08-07, iteration 706 — [[characters/冠|冠]]

Clean verification: `mc_id: 670` exact at `lookup/CC/CC 0000.md` line 694 (the `>` prefix is that file's uniform blockquote list format, not a defect). 会意 （冖 + 元 + 寸， 元 also phonetic — Wiktionary-confirmed analysis) and readings (guān / gun1 / 관 / KAN・かんむり / quan・quán) confirmed by inspection. Filled the empty `pos` (`名詞`). `kwin: true` correct (관 = 관). Replaced the stub notes with the proper 4-bullet section. Discarded two prose-only chengyu hits （李下瓜田 — 冠 inside the quoted 君子行 verse; 臥薪嘗胆 — example sentence 冠軍）. No derived characters.

**Words cross-check** (3 ground-truth hits): **added the missing stand-in [[王冠]]** (the Words section listed only 冠冕） and [[蝉冠]]; confirmed [[冠冕]]. **Chengyu**: no frontmatter hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 添 (5196; 1793 characters remaining).

### 2026-08-07, iteration 707 — [[characters/添|添]]

`mc_id: 7727` lies beyond the CC files' 4000-entry coverage (verified `lookup/CC/CC 3000.md` ends at 4000) — retained as real long-tail data per policy. 形声 （水 + 忝） and readings (tiān / tim1 / 첨 / TEN・そ / thiêm・thêm et al.) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (텀 ≠ 첨). Replaced the stub notes with the proper 4-bullet section. No derived characters.

**Words cross-check** (2 ground-truth hits): stand-in [[添加]] plus added [[添乗]]. **Chengyu** (1 hit): added [[画蛇添足]] (frontmatter-cited).

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 伸 (5197; 1792 characters remaining).

### 2026-08-07, iteration 708 — [[characters/伸|伸]]

Clean verification: `mc_id: 2210` exact at `lookup/CC/CC 2000.md` line 223. 形声 （人 + 申） and readings (shēn / san1 / 신 / SHIN・の / thân) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: true` correct (신 = 신). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (3 ground-truth hits): stand-in [[伸長]] plus [[伸展]], [[欠伸]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 傍 (5198; 1791 characters remaining).

### 2026-08-07, iteration 709 — [[characters/傍 (char)|傍]]

Clean verification: `mc_id: 2042` exact at `lookup/CC/CC 2000.md` line 47. 形声 （人 + 旁） and readings (bàng / bong6 / 방 / BOU・HOU・かたわ / bàng・phàng et al.) confirmed by inspection. Filled the empty `pos` (`修飾語` — matching the stand-in word page's own POS, per convention). `kwin: false` correct (팡 ≠ 방). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (1 ground-truth hit): stand-in [傍](words/傍.md) itself.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 偏 (5199; 1790 characters remaining).

### 2026-08-07, iteration 710 — [[characters/偏 (char)|偏]]

Clean verification: `mc_id: 1311` exact at `lookup/CC/CC 1000.md` line 328. `pos: 性詞` already filled. 形声 （人 + 扁） — the existing OC-annotated bullet was good; kept it (radical link display normalized 亻→人） — and readings (piān / pin1 / 편 / HEN・かたよ / thiên・xiên et al.) confirmed by inspection. `kwin: true` correct (편 = 편). Preserved the "added to Korean HS in 2000" note as a standalone line. **The words cross-check initially missed all citations** — my list-item grep pattern used `\b`, which BSD grep treats as a literal backspace, so `  - 偏 (char)` list items didn't match; re-ran with an unanchored pattern. No chengyu, no derived characters.

**Words cross-check** (3 ground-truth hits): stand-in [偏](words/偏.md), [[偏差]], [[偏重]] (the two body-listed words were confirmed as genuine frontmatter citers).

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 企 (5200; 1789 characters remaining).

### 2026-08-07, iteration 711 — [[characters/企|企]]

Clean verification: `mc_id: 3760` exact at `lookup/CC/CC 3000.md` line 793. 会意 （人 + 止 — a person on tiptoe, craning ahead) and readings (qǐ / kei5 / 기 / KI・くわだ / xí) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (커 ≠ 기). Replaced the malformed `# Notes` stub with the proper 4-bullet section; normalized the three bare `[[…]] "gloss"` word lines to ruby format with 注音 from the word pages. No chengyu, no derived characters.

**Words cross-check** (4 ground-truth hits): stand-in [[企劃]] plus [[企業]], [[企鵝]], [[企図]] — all four body-listed words confirmed as genuine frontmatter citers.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 催 (5202; 1788 characters remaining).

### 2026-08-07, iteration 712 — [[characters/催 (char)|催]]

`mc_id: 7336` lies beyond the CC files' 4000-entry coverage — retained as real long-tail data per policy (same as 添 7727). 形声 （人 + 崔） and readings (cuī / ceoi1 / 최 / SAI・もよう / thôi・thoi et al.) confirmed by inspection. Filled the empty `pos` (`事詞` — the stand-in word page stores legacy `動詞`; character-page verb-class convention wins). `kwin: true` correct (최 = 최). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (1 ground-truth hit): stand-in [催](words/催.md) itself.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 侵 (5203; 1787 characters remaining).

### 2026-08-07, iteration 713 — [[characters/侵|侵]]

Clean verification: `mc_id: 755` exact at `lookup/CC/CC 0000.md` line 782. 会意 （人 + hand-holding-broom) and readings (qīn / cam1 / 침 / SHIN・おか / xâm・xăm・xơm) confirmed by inspection. The stored `graphemic_classification: 浸` points at the phonetic-series relative [[浸 (char)|浸]] — kept, explained in bullet 1 (same stand-in convention as 滴's 帝-for-啇）. Filled the empty `pos` (`事詞`). `kwin: true` correct (침 = 침). Sections were transposed (Words above a malformed `# Notes`) — rebuilt in standard order; normalized the two bare `[[…]]` word lines to ruby format. No chengyu, no derived characters.

**Words cross-check** (3 ground-truth hits): stand-in [[侵入]] plus [[侵略]], [[侵犯]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 傲 (5204; 1786 characters remaining).

### 2026-08-07, iteration 714 — [[characters/傲|傲]]

Clean verification: `mc_id: 2127` exact at `lookup/CC/CC 2000.md` line 136. 形声 （人 + 敖） and readings (ào / ngou6 / 오 / GOU・おご / ngạo・ngão et al.) confirmed by inspection. Filled the empty `pos` (`性詞`). `kwin: false` correct (앗 ≠ 오). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (1 ground-truth hit): stand-in [[傲慢]] only.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 伯 (5205; 1785 characters remaining).

### 2026-08-07, iteration 715 — [[characters/伯|伯]]

Clean verification: `mc_id: 172` exact at `lookup/CC/CC 0000.md` line 180. 形声 （人 + 白） and readings (bó / baak3 / 백 / HAKU・HA / bá・bác) confirmed by inspection. Filled the empty `pos` (`名詞`). `kwin: false` correct (박 ≠ 백). Replaced the malformed `# Notes` stub with the proper 4-bullet section; normalized the two bare `[[…]]` word lines to ruby format. No chengyu, no derived characters.

**Words cross-check** (4 ground-truth hits): **added the missing stand-in [[伯父]]** (only 伯伯 and 伯爵 were listed) plus [[伯母]]; confirmed [[伯伯]], [[伯爵]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 孔 (5206; 1784 characters remaining).

### 2026-08-07, iteration 716 — [[characters/孔 (char)|孔]]

Clean verification: `mc_id: 230` exact at `lookup/CC/CC 0000.md` line 242. 会意 （丿 + 子 — fontanelle) and readings (kǒng / hung2 / 공 / KOU・あな / khổng・khủng et al.) confirmed by inspection. Filled the empty `pos` (`名詞`). `kwin: false` correct (콩 ≠ 공). Rebuilt the notes: dropped the `[List of 会意](../lookup/...)` navigation link (broken `../` prefix, not part of the standard bullet set), converted the plain `[丿](Radical%20004)` links to wiki-style `[[Radical 004|丿]]`. **Words section was missing 5 of 6 citers** — only 孔教 was listed. Derived bullet initially linked `[[吼]]`, which resolves to words/吼.md — corrected to `[[吼 (char)|吼]]`. No chengyu.

**Words cross-check** (6 ground-truth hits): stand-in [孔](words/孔.md), [[孔子]], [[孔教]], [[孔明]], [[瞳孔]], [[穿孔机]]. **Derived Characters** (1 hit): added [[吼 (char)|吼]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 幅 (5207; 1783 characters remaining).

### 2026-08-07, iteration 717 — [[characters/幅|幅]]

Clean `mc_id: 3027` at `lookup/CC/CC 3000.md` line 32. 形声 （巾 + 畐） and readings (fú / fuk1 / 폭 / FUKU・HYOKU・はば / bức) confirmed by inspection. **Fixed a wrong filled `pos`: stored 事詞， but all three citing word pages store 名詞 and the glosses ("breadth, width, range") are nominal — changed to 名詞.** `kwin: false` correct (뿍 ≠ 폭). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (3 ground-truth hits): stand-in [[幅度]], confirmed [[横幅]], **added the missing [[振幅]]**.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 征 (5208; 1782 characters remaining).

### 2026-08-07, iteration 718 — [[characters/征|征]]

Clean verification: `mc_id: 818` exact at `lookup/CC/CC 0000.md` line 848. 形声 （彳 + 正） and readings (zhēng / zing1 / 정 / SEI / chinh・trưng et al.) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: true` correct (정 = 정). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (1 ground-truth hit): stand-in [[征伐]] only.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 悠 (5210; 1781 characters remaining).

### 2026-08-07, iteration 719 — [[characters/悠|悠]]

Clean verification: `mc_id: 2462` exact at `lookup/CC/CC 2000.md` line 483. 形声 （心 + 攸； no vault page for the phonetic — plain text per convention) and readings (yōu / jau4 / 유 / YUU / du・đu) confirmed by inspection. Filled the empty `pos` (`性詞`). `kwin: false` correct (윳 ≠ 유). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (1 ground-truth hit): stand-in [[悠久]] only.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 抗 (5211; 1780 characters remaining).

### 2026-08-07, iteration 720 — [[characters/抗|抗]]

Clean verification: `mc_id: 2112` exact at `lookup/CC/CC 2000.md` line 121. 形声 （手 + 亢） and readings (kàng / kong3 / 항 / KOU・あらが / kháng) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: true` correct (항 = 항). Replaced the malformed `# Notes` stub with the proper 4-bullet section. (Self-caught slip: initially wrote 抗拒's ruby from inference as ㄏㄚㄫㄍㄝ — the word page stores ㄏㄚㄫㄍ⼄; corrected.) No chengyu, no derived characters.

**Words cross-check** (3 ground-truth hits): **added the missing stand-in [[抵抗]]** and [[抗争]]; confirmed [[抗拒]].

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 捉 (5212; 1779 characters remaining).

### 2026-08-07, iteration 721 — [[characters/捉|捉]]

`mc_id: 5169` lies beyond the CC files' 4000-entry coverage — retained as real long-tail data per policy (same as 添 7727, 催 7336). 形声 （手 + 足） and readings (zhuō / zuk1 / 착 / SOKU・SAKU・とら / tróc・chộp et al.) confirmed by inspection. Filled the empty `pos` (`事詞`). `kwin: false` correct (작 ≠ 착). Replaced the malformed `# Notes` stub with the proper 4-bullet section. No chengyu, no derived characters.

**Words cross-check** (1 ground-truth hit): stand-in [[捕捉]] only.

Stamped `date-last-perfect: 2026-08-07`.

### 2026-08-07, iteration 722 — [[characters/魄|魄]]

**Anomaly, not a straightforward next-in-sequence pick**: this file had `danayo_id:` and `mc_id: 0` blank/placeholder since its creation on 2026-05-26 (confirmed via `git log --follow`) — never a real ascending-order pick, and its blank `danayo_id` sorted it first in the `grep -L "^date-last-perfect"` scan ahead of the true next character (抄, 5213). Asked the user how to handle it; they chose to assign a fresh `danayo_id` now and fully perfect the page, resuming the true ascending sequence from 抄 next iteration. Assigned `danayo_id: 8817` (one past the current corpus max of 8816).

**Real `mc_id` bug found and fixed**: was `0` (never looked up); verified `1962` at `lookup/CC/CC 1000.md` line 1003.

**Real `middle_chinese_initial` bug found and fixed**: stored as plain `p`, but Cantonese `paak3` (Cantonese distinguishes b=unaspirated/p=aspirated) and the Zhengzhang OC reconstruction `*pʰraːɡ` (via Wiktionary) both confirm the aspirated initial `pʰ` (聲 滂) — corrected from the unaspirated `p` (聲 幫).

**Real broken-link bug found and fixed**: the pre-existing floating final-lookup link cited `韻 鐸開`, which doesn't exist anywhere in the vault; cross-checked against other perfected ɑk-final characters ([[楽]], [[落]], [[索]]) to find the vault's actual page name, `韻 鈬開`, and corrected it.

Filled blank `pos: ""` → `名詞`. `graphemic_classification: 白` (形声, 鬼 semantic + 白 phonetic) and all five readings confirmed correct via Wiktionary. Replaced the malformed body (a lone Notes bullet plus two floating, now-orphaned initial/final wikilinks) with the proper 4-bullet section, including Hyōgai/Old HSK 4/Korean Name ㅂ/Grade Advanced for the Levels bullet.

**Words cross-check** (1 ground-truth hit, after filtering out [[神霊]] as a text-only false positive not citing 魄 in its own `characters:` field): stand-in [[魂魄]] only. **Chengyu**/**Derived Characters**: no hits — both correctly omitted. **Note**: not a cranberry pair with [[魂 (char)|魂]] — 魂's own `stand_in` is 魂 itself, not 魂魄, so transitivity (A=B=AB) fails.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 抄 (5213; resuming ascending sequence).

### 2026-08-07, iteration 723 — [[characters/抄|抄]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3990`, but `lookup/CC/CC 3000.md` line 1031 shows `3990. 軺` (an unrelated character) — 抄's real rank is `3991` (line 1032). Corrected.

Body had only two floating CC-initial/final wikilinks and a `## Words` section placed before a bare `# Notes` heading (wrong order, wrong heading level). 形声 （手 semantic + 少 phonetic, OC \*sm̥ʰreːw/\*sm̥ʰreːws) and readings (chāo / caau1 / 초 / SHOU / sao·xao) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching sibling hand-radical action characters [[characters/抗|抗]]/[[characters/捉|捉]]). Rebuilt as the proper 4-bullet `## Notes` section followed by `## Words`.

**Words cross-check** (1 ground-truth hit): [[抄録]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 慕 (5214; 1781 characters remaining).

### 2026-08-07, iteration 724 — [[characters/慕|慕]]

Clean verification: `mc_id: 1305` exact at `lookup/CC/CC 1000.md` line 322. 形声 （心 + 莫, OC \*maːɡs) and readings (mù / mou6 / 모 / BO・した / mồ・mộ) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching the closest semantic sibling [[characters/憧|憧]], also a "long for/yearn" verb). Replaced the malformed body (Words placed above a bare `# Notes` heading, no bullets) with the proper 4-bullet `## Notes` section followed by `## Words`.

**Words cross-check** (2 ground-truth hits, filtering out [[綏靖]] as a text-only false positive not citing 慕 in its own `characters:` field): [[思慕]] already listed, flagged as the `stand_in`; added the missing [[羨慕]]. **Chengyu**: [[欲夫治汝]] matched a naive text grep but doesn't cite 慕 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 梨 (char) (5215; 1780 characters remaining).

### 2026-08-07, iteration 725 — [[characters/梨 (char)|梨]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3411`, but `lookup/CC/CC 3000.md` line 432 shows `3411. 闋` (an unrelated character) — 梨's real rank is `3412` (line 433). Corrected.

Body had only two floating CC-initial/final wikilinks and one informal, unruby'd word note. 形声 （木 semantic + 利 phonetic, OC \*ril) and readings (lí / lei4 / 리 / RI・なし / lê) confirmed via Wiktionary. Filled the empty `pos` (`名詞`). Wrote all four Notes bullets from scratch — noted the `joyo_level: "4"` maps to the `Jōyō - Kyōiku` lookup page (elementary-school kanji share one page regardless of grade number), matching the precedent at [[characters/敗|敗]].

**Words cross-check** (4 total ground-truth hits): only [[梨木]] previously listed; added the self-referential `stand_in` [[梨]] plus [[鳳梨]] and [[鰐梨]]. **Flagged, not fixed (out of scope)**: `words/梨木.md`'s own `characters:` field cites bare `梨` rather than `梨 (char)` — likely meant to cite the character page but technically resolves to the word page instead; a word-sweep fix, not a character-page one, but it still genuinely uses 梨 so it belongs in this Words list regardless. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 析 (5216; 1779 characters remaining).

### 2026-08-07, iteration 726 — [[characters/析|析]]

**Real `graphemic_classification` bug found and fixed**: stored as `斤` (a component name, the 形声-style encoding), but 析 is actually 會意 (木 "wood" + 斤 "axe" — to split wood, per Wiktionary), not 形声 — per convention (confirmed against [[characters/孔 (char)|孔]] and [[characters/床 (char)|床]]), 會意 characters store the literal type string, not a component name. Corrected `斤` → `會意`.

**Real alias-contamination bug found and fixed, same pattern as [[characters/護|護]]'s 掩 and [[characters/貞|貞]]'s 楨**: `aliases` included `皙`, `晰`, `晳` — all three mean "fair-skinned/clear" and belong to a wholly distinct semantic field from 析's "split, analyze" (Wiktionary lists 析's real variants as `㭊`/`扸`/`𣂔`, none of which have vault pages, and separately notes 析 is only an *obsolete form of 皙 under a different, unrelated etymology* — not a live alias relationship). Removed all three (no vault pages exist for any of them, so nothing else needed updating).

**Real `mc_id` off-by-one bug found and fixed**: stored as `1901`, but `lookup/CC/CC 1000.md` line 942 shows `1901. 痺` (an unrelated character) — 析's real rank is `1902` (line 943). Corrected.

`pos: 事詞` was already correct. Body had only two floating CC-initial/final wikilinks and an informal "Components:" line — wrote all four Notes bullets from scratch.

**Words cross-check** (3 ground-truth hits, filtering out [[回帰]] and [[分掌]] as text-only false positives not citing 析 in their own `characters:` field): all three already correctly listed ([[分析]], [[解析]], [[透析]]) — only needed the `stand_in` flag added to [[分析]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 斜 (5217; 1778 characters remaining).

### 2026-08-07, iteration 727 — [[characters/斜|斜]]

Clean verification: `mc_id: 3341` exact at `lookup/CC/CC 3000.md` line 358. 形声 （斗 semantic "ladle" + 余 phonetic, OC \*lja) and readings (xié / ce4 / 사 / SHA・なな / tà) confirmed via Wiktionary. Filled the empty `pos` (`性詞`, matching semantic sibling [[characters/偏 (char)|偏]], also a "slanted/biased" quality character). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (3 ground-truth hits, all three already listed): only needed the `stand_in` flag added to [[傾斜]]; confirmed [[斜坂]] and [[斜辺]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 援 (5218; 1777 characters remaining).

### 2026-08-07, iteration 728 — [[characters/援|援]]

Clean verification: `mc_id: 1210` exact at `lookup/CC/CC 1000.md` line 223. 形声 （手 semantic + 爰 phonetic, OC \*ɢʷan/\*ɢʷans) and readings (yuán / wun4 / 원 / EN / viện・vén・vẹn・vịn・vin・vờn) confirmed via Wiktionary — all six Vietnamese readings matched, none dropped. Filled the empty `pos` (`事詞`, matching semantic sibling [[characters/護|護]]). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Flagged, not fixed (out of scope)**: the declared `stand_in` (`援手`, "to lend a helping hand" — a real compound) has no `words/援手.md` page yet; a word-creation gap, not a character-page fix, so the `stand_in` field was left as-is and no page in the Words list carries the stand-in flag this iteration.

**Words cross-check** (5 total ground-truth hits): only [[援護]] previously listed; added the 4 missing — [[救援]], [[援助]], [[無援]], [[援交]] (abbreviation of 援助交際, included on its own linguistic merit despite the sensitive gloss). **Chengyu**: added [[孤立無援]] (real hit, previously missing). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 普 (5219; 1776 characters remaining).

### 2026-08-07, iteration 729 — [[characters/普|普]]

**Real `graphemic_classification` bug found and fixed, same pattern as [[characters/析|析]]**: stored as `竝` (a component name, the 形声-style encoding), but 普 is actually 會意 ([[並 (char)|竝]] "side by side" + 日 "sun," per Wiktionary — spread evenly like sunlight) — per convention, 會意 characters store the literal type string. Corrected `竝` → `會意`.

**Real `mc_id` off-by-one bug found and fixed**: stored as `2497`, but `lookup/CC/CC 2000.md` line 518 shows `2497. 兕` (an unrelated character) — 普's real rank is `2498` (line 519). Corrected.

Body had the Notes/Words sections merged into one malformed block (a `## Notes` heading with a component note, then SKIP/stroke on one crammed line, floating CC-initial/final wikilinks, then Words bullets with no `## Words` heading at all). Rebuilt as two proper sections. Filled the empty `pos` (`性詞`, matching semantic sibling [[characters/遍 (char)|遍]]).

**Words cross-check** (4 total ground-truth hits, filtering out 7 text-only false positives — [[補給]], [[単鷹国]], [[不断]], [[南海]], [[中文]], [[波及]], [[中国語]] — none of which cite 普 in their own `characters:` field): [[普及]] and [[普遍]] already correct; **added the missing stand-in [[普通]]**; reformatted [[普通話]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 途 (5220; 1775 characters remaining).

### 2026-08-07, iteration 730 — [[characters/途|途]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `2774`, but `lookup/CC/CC 2000.md` line 807 shows `2774. 筐` (an unrelated character) — 途's real rank is `2775` (line 808). Corrected.

形声 （辵 semantic "movement, road" + 余 phonetic, OC \*l'aː) and readings (tú / tou4 / 도 / TO・ZU / đồ) confirmed via Wiktionary; `graphemic_classification: 余` already correct. Filled the empty `pos` (`名詞`, matching sibling path/road noun [[characters/路|路]]). Replaced the malformed `# Notes` stub with the proper 4-bullet section.

**Words cross-check** (1 ground-truth hit, filtering out 4 text-only false positives — [[日暮]], [[光明]], [[荊棘]], [[暗中]] — none of which cite 途 in their own `characters:` field): [[途中]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 殊 (5221; 1774 characters remaining).

### 2026-08-07, iteration 731 — [[characters/殊|殊]]

Clean verification: `mc_id: 1112` exact at `lookup/CC/CC 1000.md` line 121. 形声 （歹 semantic "death, bone" + 朱 phonetic, OC \*djo — originally "to behead," extended to "different" then "special") and readings (shū / syu4 / 수 / SHU・JU / sù・thò・thù・thùa) confirmed via Wiktionary. Filled the empty `pos` (`性詞`, matching semantic siblings [[characters/奇|奇]]/[[characters/異|異]]/[[characters/独|独]]). Replaced the malformed `# Notes` stub (no `## Words` section at all despite a declared `stand_in`) with the proper 4-bullet section plus Words.

**Words cross-check** (1 ground-truth hit): added [[特殊]], flagged as the `stand_in`, built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 漠 (5222; 1773 characters remaining).

### 2026-08-07, iteration 732 — [[characters/漠|漠]]

**Real wrong-citation bug found and fixed**: the pre-existing `## Words` list included `[[薄膜]]` glossed "membrane; thin film" — but `words/薄膜.md`'s own `characters:` field cites `薄` and `膜`, not `漠` at all. The two characters share the Mandarin reading *mò* but are otherwise unrelated (漠 "desert" vs 膜 "membrane," different radicals/etymologies) — almost certainly a same-sound mix-up. Removed the bullet entirely.

**Real `mc_id` off-by-one bug found and fixed**: stored as `2630`, but `lookup/CC/CC 2000.md` line 659 shows `2630. 伺` (an unrelated character) — 漠's real rank is `2631` (line 660). Corrected.

形声 （水 semantic + 莫 phonetic, OC \*maːɡ) and readings (mò / mok6 / 막 / BAKU / mác・mạc) confirmed via Wiktionary; `graphemic_classification: 莫` already correct. Filled the empty `pos` (`名詞`). Rebuilt the Notes section (previously two floating CC-initial/final wikilinks with `## Words` crammed onto the same line as the second) into the proper 4-bullet form.

**Words cross-check** (1 ground-truth hit after removing the 薄膜 error and filtering out 2 more text-only false positives — [[茫茫]], [[瞭然]] — neither citing 漠 in their own `characters:` field): [[沙漠]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 燥 (5223; 1772 characters remaining).

### 2026-08-07, iteration 733 — [[characters/燥|燥]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1731`, but `lookup/CC/CC 1000.md` line 764 shows `1731. 戟` (an unrelated character) — 燥's real rank is `1732` (line 765). Corrected.

形声 （火 semantic + 喿 phonetic, OC \*saːwʔ/\*saːws) and readings (zào / cou3 / 조 / SOU / ráo・táo) confirmed via Wiktionary; `graphemic_classification: 喿` already correct. Filled the empty `pos` (`性詞`, matching antonym-pair sibling [[characters/乾|乾]], also a dry/wet quality character). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit): [[乾燥]] already listed and already flagged as the `stand_in` — no change needed. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 捕 (char) (5224; 1771 characters remaining).

### 2026-08-07, iteration 734 — [[characters/捕 (char)|捕]]

Clean verification: `mc_id: 1098` exact at `lookup/CC/CC 1000.md` line 103. 形声 （手 semantic + 甫 phonetic, OC \*baːs) and readings (bǔ / bou6 / 포 / HO・つか / buả・bõ・bố・bổ・bủa) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching near-synonym sibling [[characters/捉|捉]]). Rebuilt the malformed body (bare unruby'd Words links with a stray trailing empty bullet, two floating CC-initial/final wikilinks stuck after `## Words`) into the proper 4-bullet `## Notes` section plus a full `## Words`.

**Words cross-check** (7 total ground-truth hits, filtering out [[手]] as a text-only false positive not citing 捕 in its own `characters:` field): 4 previously listed as bare links ([[捕手]], [[捕鯨]], [[逮捕]], [[捕獲]] — all reformatted with proper ruby+gloss); added the self-referential `stand_in` [[捕]], plus the 2 missing [[捕捉]] and [[拿捕]]. **Chengyu**: [[修飾先行]] and [[先題後述]] matched a naive text grep but neither cites 捕 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 趣 (5225; 1770 characters remaining).

### 2026-08-07, iteration 735 — [[characters/趣|趣]]

Clean verification: `mc_id: 1587` exact at `lookup/CC/CC 1000.md` line 612. 形声 （走 semantic "walk" + 取 phonetic, OC \*sʰlos — hastening toward what interests one) and readings (qù / ceoi3 / 취 / SHU・SOKU・SOU / thú・xú) confirmed via Wiktionary. Filled the empty `pos` (`名詞`, matching the stand-in word [[趣味]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 ground-truth hits, both already listed): only needed the `stand_in` flag added to [[趣味]]; confirmed [[趣旨]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 迫 (5226; 1769 characters remaining).

### 2026-08-07, iteration 736 — [[characters/迫|迫]]

Clean verification: `mc_id: 1441` exact at `lookup/CC/CC 1000.md` line 462. 形声 （辵 semantic "movement" + 白 phonetic, OC \*praːɡ) and readings (pò / baak1 / 박 / HAKU・HYAKU・せま / bách・bích・bạch) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching the 2-of-3 majority among citing words [[逼迫]]/[[強迫]]). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, filtering out [[脅威]] and [[何事]] as text-only false positives not citing 迫 in their own `characters:` field): reformatted [[迫害]] with proper ruby+gloss (was a bare unruby'd link); confirmed [[逼迫]]; **added the missing stand-in [[強迫]]**. **Chengyu**: [[焚書坑儒]] matched a naive text grep but doesn't cite 迫 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 疲 (5227; 1768 characters remaining).

### 2026-08-07, iteration 737 — [[characters/疲|疲]]

**Confirmed `aliases: [罢, 㔥]` are both legitimate** — checked against Wiktionary before assuming contamination (given 罷/罢 normally means "to stop, dismiss," an unrelated sense); Wiktionary explicitly lists 罷／罢 and 㔥 as documented alternative forms of 疲 itself, so no fix needed here, unlike the 護/貞/析/普 alias-contamination cases in recent iterations.

Clean verification otherwise: `mc_id: 2317` exact at `lookup/CC/CC 2000.md` line 334. 形声 （疒 semantic "sickness" + 皮 phonetic, OC \*bral) and readings (pí / pei4 / 피 / HI・つか / bì・mệt) confirmed via Wiktionary. Filled the empty `pos` (`性詞`, matching the dominant quality-adjective pattern for state-describing characters this loop has used throughout, e.g. [[characters/慕|慕]]/[[characters/斜|斜]]/[[characters/燥|燥]]). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits): added both — [[疲労]] (the `stand_in`) and [[疲困]], neither previously listed at all. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 距 (5228; 1767 characters remaining).

### 2026-08-07, iteration 738 — [[characters/距|距]]

Clean verification: `mc_id: 1379` exact at `lookup/CC/CC 1000.md` line 396. 形声 （足 semantic "foot" + 巨 phonetic, OC \*ɡaʔ — originally a rooster's spur, extended to "distance") and readings (jù / keoi5 / 거 / KYO・けづめ / cự・cựa) confirmed via Wiktionary. Filled the empty `pos` (`名詞`, matching the stand-in word [[距離]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added [[距離]], flagged as the `stand_in`, built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 避 (char) (5229; 1766 characters remaining).

### 2026-08-07, iteration 739 — [[characters/避 (char)|避]]

Clean verification: `mc_id: 842` exact at `lookup/CC/CC 0000.md` line 872. 形声 （辵 semantic "movement" + 辟 phonetic, OC \*beɡs) and readings (bì / bei6 / 피 / HI・さ / tị) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching the citing word [[逃避]]'s own `事詞`; the `stand_in` word `words/避.md` itself has no `pos` field at all — a word-sweep gap, not fixed here). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[卑]] as a text-only false positive not citing 避 in its own `characters:` field): added the self-referential `stand_in` [[避]] and [[逃避]], neither previously listed. **Chengyu**: [[李下瓜田]], [[有備無患]], and [[殺姦窃偽]] all matched a naive text grep but none cite 避 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 遵 (5230; 1765 characters remaining).

### 2026-08-07, iteration 740 — [[characters/遵|遵]]

**Real alias-contamination bug found and fixed, same pattern as [[characters/析|析]]'s 皙/晰/晳**: `aliases` included `僎`, but Wiktionary lists 遵's real documented variants as `𢕰`/`𣦝` (neither has a vault page) and separately notes 僎 only as an unrelated *alternative meaning* ("master of ceremonies") sharing the glyph — not a variant spelling of 遵's "obey/follow" sense. Removed it (no vault page exists for 僎 either, so nothing else needed updating).

Clean verification otherwise: `mc_id: 1315` exact at `lookup/CC/CC 1000.md` line 332. 形声 （辵 semantic "movement" + 尊 phonetic, OC \*ʔsun) and readings (zūn / zeon1 / 준 / JUN・SHUN / tuân) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching the stand-in word [[遵守]]'s own `事詞`). Replaced the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): reformatted [[遵守]] with proper ruby+gloss, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 耐 (char) (5231; 1764 characters remaining).

### 2026-08-07, iteration 741 — [[characters/耐 (char)|耐]]

Clean verification: `mc_id: 3121` exact at `lookup/CC/CC 3000.md` line 130. 形声 （寸 semantic "hand, measure" + 而 phonetic, OC \*nɯːs) and readings (nài / noi6 / 내 / TAI・DOU・た / nài・nại・nề) confirmed via Wiktionary; `graphemic_classification: 而` and `pos: 性詞` both already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, filtering out [[刻苦]] and [[乃]] as text-only false positives not citing 耐 in their own `characters:` field): added the self-referential `stand_in` [[耐]]; confirmed [[忍耐]] already correct. **Chengyu**: [[意味深長]] matched a naive text grep but doesn't cite 耐 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 覆 (5232; 1763 characters remaining).

### 2026-08-07, iteration 742 — [[characters/覆|覆]]

**Real double alias-contamination bug found and fixed, same pattern as recent iterations**: `aliases` included `襾` and `复`. `襾` is 覆's own *semantic radical component*, not an orthographic variant of the whole character — a different category error from the usual same-sound mix-up. `复` is a documented simplified form of 覆, but per Wiktionary's own usage note, only for the unrelated "to return/reply" sense (i.e., where 覆 substitutes for 復/複) — not for the "cover/overturn" senses this page describes. Wiktionary's real variants for this sense are `覄`/`㠅`, neither with a vault page. Removed both `襾` and `复` (no vault pages exist for either, so nothing else needed updating).

**Real broken-link bug found and fixed**: the existing Notes bullet had an empty component link (`phonetic [[]]`) where the phonetic 復 belonged, and the semantic gloss was also blank (`[[Radical 146|襾]] ("")`) — filled both in.

`mc_id: 849` verified exact at `lookup/CC/CC 0000.md` line 879. 形声 confirmed via Wiktionary (襾 semantic "cover" + 復 phonetic); `graphemic_classification: 復` already correct. Filled the empty `pos` (`実詞`, matching the stand-in word [[覆蓋]]'s own `実詞`). Removed a stray irrelevant bullet ("Added to the Korean HS list in 2000") and rebuilt the section into the proper 4-bullet form plus `## Words`.

**Words cross-check** (1 ground-truth hit): added [[覆蓋]], flagged as the `stand_in`, built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 超 (char) (5233; 1762 characters remaining).

### 2026-08-07, iteration 743 — [[characters/超 (char)|超]]

Clean verification: `mc_id: 1361` exact at `lookup/CC/CC 1000.md` line 378. 形声 （走 semantic "run" + 召 phonetic, OC \*dews/\*djews) and readings (chāo / ciu1 / 초 / CHOU・こ / siêu・sêu・sếu・xiêu) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching near-synonym sibling [[characters/越 (char)|越]]). Replaced the malformed `# Notes` stub (one bare unruby'd Words bullet mixed in with floating CC-initial/final wikilinks) with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[倒]] and [[論理]] as text-only false positives not citing 超 in their own `characters:` field): added the self-referential `stand_in` [[超]]; reformatted [[超越]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**: [[古今東西]] and [[瑠璃清天]] both matched a naive text grep but neither cites 超 in its own `characters:` field — both correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 肝 (5234; 1761 characters remaining).

### 2026-08-07, iteration 744 — [[characters/肝|肝]]

Clean verification: `mc_id: 1237` exact at `lookup/CC/CC 1000.md` line 250. 形声 （肉 semantic "flesh" + 干 phonetic, OC \*kaːn) and readings (gān / gon1 / 간 / KAN・きも / can・gan・gang) confirmed via Wiktionary. Filled the empty `pos` (`名詞`, matching body-part sibling [[characters/脚 (char)|脚]]). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit, filtering out [[五官]] as a text-only false positive not citing 肝 in its own `characters:` field): [[肝臓]] already listed and already flagged as the `stand_in` — no change needed. **Chengyu**: [[因小失大]] and [[粉骨砕身]] both matched a naive text grep but neither cites 肝 in its own `characters:` field — both correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 逐 (5235; 1760 characters remaining).

**Note**: user switched from the 5-minute cron loop to continuous back-to-back processing (cron job `4d56f7d3` cancelled) — iterations from here proceed one after another without waiting for a timed trigger, until told to stop.

### 2026-08-07, iteration 745 — [[characters/逐|逐]]

**Real `graphemic_classification` bug found and fixed, same pattern as [[characters/析|析]] and [[characters/普|普]]**: stored as `豕` (a component name, the 形声-style encoding), but 逐 is actually 會意 (辵 "walk" + 豕 "pig" — chasing a pig, per Wiktionary), not 形声. Corrected `豕` → `會意`.

Clean verification otherwise: `mc_id: 797` exact at `lookup/CC/CC 0000.md` line 824. Readings (zhú / zuk6 / 축 / CHIKU・JIKU / chục・giục・trục) confirmed via Wiktionary. Filled the empty `pos` (`事詞`, matching near-synonym sibling [[characters/追 (char)|追]] and citing word [[角逐]]'s own `事詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, filtering out [[御術]], [[角]], [[五馭]] as text-only false positives not citing 逐 in their own `characters:` field): [[追逐]] already listed, flagged as the `stand_in`; added the 3 missing — [[駆逐]], [[角逐]], [[駆逐艦]]. **Chengyu**: [[舎本逐末]] already correctly listed, confirmed as the only real hit ([[保頭断尾]] and [[虎視耽耽]] were text-only false positives). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 郊 (5238; 1759 characters remaining).

### 2026-08-07, iteration 746 — [[characters/郊|郊]]

Clean verification: `mc_id: 734` exact at `lookup/CC/CC 0000.md` line 761. 形声 （邑 semantic "settlement" + 交 phonetic, OC \*kreːw) and readings (jiāo / gaau1 / 교 / KOU・まつる / giao) confirmed via Wiktionary; `pos: 名詞` already correct. Replaced the malformed body (informal "Components:" line mixed with floating CC-initial/final wikilinks) with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit, filtering out [[祭物]] and [[及第]] as text-only false positives not citing 郊 in their own `characters:` field): [[近郊]] already listed and already flagged as the `stand_in` — no change needed. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 硬 (char) (5239; 1758 characters remaining).

### 2026-08-07, iteration 747 — [[characters/硬 (char)|硬]]

Clean verification: `mc_id: 3081` exact at `lookup/CC/CC 3000.md` line 86. 形声 （石 semantic "stone" + 更 phonetic, OC \*ŋɡraːŋs) and readings (yìng / ngaang6 / 경 / KOU・GOU・かた / ngạnh) confirmed via Wiktionary. Filled the empty `pos` (`性詞`, matching the citing word [[堅硬]]'s own `性詞`). Rebuilt the malformed body (an informal "abbreviation for molybdenum" prose bullet outside `## Words`) into the proper 4-bullet `## Notes` section plus a full `## Words`.

**Words cross-check** (4 total ground-truth hits, filtering out [[堅持]], [[難金]], [[褐金]], [[簡潔]], [[翠金]], [[吸金]] as text-only false positives not citing 硬 in their own `characters:` field): [[硬直]] already listed; added the self-referential `stand_in` [[硬]], plus [[堅硬]] and [[硬金]] (the latter promoted from an informal prose note to a proper Words entry). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 肯 (char) (5240; 1757 characters remaining).

### 2026-08-07, iteration 748 — [[characters/肯 (char)|肯]]

Clean verification: `mc_id: 1049` exact at `lookup/CC/CC 1000.md` line 54; `pos: 事詞` and `graphemic_classification: 會意` both already correct. 會意 (abbreviated 冎 "bone" + 肉 "meat," per Wiktionary — meat attached to bone, extended to "willing") and readings (kěn / hang2 / 긍 / KOU・KAI・がえんじ / khẳng・khứng・khừng) confirmed. **Corrected an informal, wrong component note**: "Components: [[止]], [[月]]" — 止 isn't part of this character's real analysis at all; replaced with the genuine 冎+肉 breakdown (冎 kept as plain text, no vault page for it). Rebuilt into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[一定]] as a text-only false positive not citing 肯 in its own `characters:` field): added the self-referential `stand_in` [[肯]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 腐 (5241; 1756 characters remaining).

### 2026-08-07, iteration 749 — [[characters/腐|腐]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `2000`, but `lookup/CC/CC 1000.md` line 1041 shows `2000. 鋒` (an unrelated character) — 腐's real rank is `2001` (`lookup/CC/CC 2000.md` line 6). Corrected.

形声 （肉 semantic "flesh" + 府 phonetic, OC \*boʔ) and readings (fǔ / fu6 / 부 / FU / hủ) confirmed via Wiktionary; `graphemic_classification: 府` already correct. Filled the empty `pos` (`事詞`, matching the stand-in word [[腐敗]]'s own `事詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, filtering out [[四川]], [[汚吏]], [[豆]], [[老鼠人]] as text-only false positives not citing 腐 in their own `characters:` field): [[腐敗]], [[腐朽]], [[放腐]] already listed; **added the missing [[豆腐]]**. **Chengyu**: [[財愛悪根]], [[貪官汚吏]], and [[鼠世桃源]] all matched a naive text grep but none cite 腐 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 透 (char) (5242; 1755 characters remaining).

### 2026-08-07, iteration 750 — [[characters/透 (char)|透]]

`mc_id: 8799` lies beyond the CC files' 4000-entry coverage — retained as real long-tail data per policy (same as [[characters/貯|貯]] 4224, [[characters/捉|捉]] 5169, 添 7727, 催 7336). 形声 （辵 semantic "walk" + 秀 phonetic, OC \*l̥ʰoːs) and readings (tòu / tau3 / 투 / TOU・す / thấu) confirmed via Wiktionary; `graphemic_classification: 秀` already correct. Filled the empty `pos` (`事詞`, matching penetration-sense sibling [[characters/滲|滲]]). Replaced the malformed `# Notes` stub (bare unruby'd [[透視]] link mixed with two floating CC-initial/final wikilinks) with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (4 total ground-truth hits, filtering out [[天下]], [[他]], [[新字体]], [[無色]] as text-only false positives not citing 透 in their own `characters:` field): added the self-referential `stand_in` [[透]]; confirmed [[透析]] and [[滲透]]; reformatted [[透視]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 碑 (5244; 1754 characters remaining).

### 2026-08-07, iteration 751 — [[characters/碑|碑]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3228`, but `lookup/CC/CC 3000.md` line 241 shows `3228. 緦` (an unrelated character) — 碑's real rank is `3229` (line 242). Corrected.

形声 （石 semantic "stone" + 卑 phonetic, OC \*pre) and readings (bēi / bei1 / 비 / HI・いしぶみ / bi・bia・bây・bấy・bịa) confirmed via Wiktionary; `graphemic_classification: 卑` already correct. Filled the empty `pos` (`名詞`, matching the stand-in word [[墓碑]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit, filtering out [[殉難]] and [[鼻]] as text-only false positives not citing 碑 in their own `characters:` field): [[墓碑]] already listed, flagged as the `stand_in`. **Chengyu**: added [[指記二碑]] (real hit, previously missing; "Biblical Chengyu.md" is an index file with no `characters:` field, not a real chengyu entry). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 矛 (5245; 1753 characters remaining).

### 2026-08-07, iteration 752 — [[characters/矛|矛]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `2012`, but `lookup/CC/CC 2000.md` line 17 shows `2012. 弛` (an unrelated character) — 矛's real rank is `2013` (line 18). Corrected.

象形 (a bamboo spear with a ring in the middle, per Wiktionary) and readings (máo / maau4 / 모 / MU・BOU・ほこ / mâu・mấu) confirmed; `graphemic_classification: 象形` already correct. Filled the empty `pos` (`名詞`, matching the stand-in word [[長矛]]'s own `名詞`). Removed a stray irrelevant bullet ("Dropped from the Korean HS list in 2000") and rebuilt into the proper 4-bullet form — noting `hanmun_edu_level: 名` maps to [[Korean Name ㅁ]] (keyed by the first Hangul consonant of the Korean reading, 모).

**Words cross-check** (1 ground-truth hit, filtering out [[長]] as a text-only false positive not citing 矛 in its own `characters:` field): [[長矛]] already listed and already flagged as the `stand_in` — no change needed. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 霧 (char) (5246; 1752 characters remaining).

### 2026-08-07, iteration 753 — [[characters/霧 (char)|霧]]

**Real malformed-YAML bug found and fixed**: `japanese_native` was stored as a scalar `きり` immediately followed by a stray `- きり` list line — invalid frontmatter shape (only accidentally still parseable). Corrected to a proper single-item list. **Same class of bug in `vietnamese`**: stored as one comma-joined string `"vụ, mù"` instead of a proper two-item list — split into `[vụ, mù]` matching the field's documented list convention.

**Real `mc_id` off-by-one bug found and fixed**: stored as `2097`, but `lookup/CC/CC 2000.md` line 102 shows `2097. 菜` (an unrelated character) — 霧's real rank is `2098` (line 103). Corrected.

形声 （雨 semantic "rain" + 務 phonetic, OC \*moɡs) and readings (wù / mou6 / 무 / MU・BU・きり / vụ・mù) confirmed via Wiktionary; `graphemic_classification: 務`, `pos: 名詞`, and `aliases: [雾]` (confirmed genuine simplified form) all already correct. Replaced the malformed `# Notes` stub (bare unruby'd Words link mixed with floating CC-initial/final wikilinks) with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[霧]]; reformatted [[霧虹]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 項 (char) (5247; 1751 characters remaining).

### 2026-08-07, iteration 754 — [[characters/項 (char)|項]]

Clean verification: `mc_id: 684` exact at `lookup/CC/CC 0000.md` line 708. 形声 （頁 semantic "head" + 工 phonetic, OC \*koːŋ) and readings (xiàng / hong6 / 항 / KOU・GOU・うなじ / háng・hạng・hảng) confirmed via Wiktionary; `aliases: [项]` confirmed as the standard simplified form. Filled the empty `pos` (`名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out 6 text-only false positives — [[条]], [[桁]], [[頚]], [[行]], [[目]], [[注意]] — none citing 項 in their own `characters:` field): added the self-referential `stand_in` [[項]], built from nothing. **Chengyu**: [[四面楚歌]], [[意気揚揚]], and [[因小失大]] all matched a naive text grep but none cite 項 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 顧 (5248; 1750 characters remaining).

### 2026-08-07, iteration 755 — [[characters/顧|顧]]

Clean verification: `mc_id: 771` exact at `lookup/CC/CC 0000.md` line 798. 形声 （頁 semantic "head" + 雇 phonetic, OC \*kʷaːs) and readings (gù / gu3 / 고 / KO・かえり / cố) confirmed via Wiktionary; `aliases: [顾]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`, matching the stand-in word [[照顧]]'s own `事詞`) — also noted `hsk_level: "1"` maps to the `Old HSK 1` lookup page. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[鼓]] as a text-only false positive not citing 顧 in its own `characters:` field): added [[照顧]], flagged as the `stand_in`, built from nothing. **Chengyu**: [[対牛弾琴]] matched a naive text grep but doesn't cite 顧 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 奪 (5249; 1749 characters remaining).

### 2026-08-07, iteration 756 — [[characters/奪|奪]]

Clean verification: `mc_id: 831` exact at `lookup/CC/CC 0000.md` line 861. 會意 （衣 "clothing" + 雀 "bird" + 又 "hand" — a hand seizing a bird, per Wiktionary) and readings (duó / dyut6 / 탈 / DATSU・うば / sáo・xạo・đoạt) confirmed; `graphemic_classification: 會意` and `aliases: [夺]` (confirmed standard simplified form) already correct. Filled the empty `pos` (`事詞`, matching the stand-in word [[奪取]]'s own `事詞`). Replaced the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (3 total ground-truth hits, filtering out [[削]], [[終止格]], [[由]], [[与格]] as text-only false positives not citing 奪 in their own `characters:` field): [[掠奪]] and [[奪格]] already correct; reformatted [[奪取]] with proper ruby+gloss, flagged as the `stand_in` (initially mis-copied its 注音 from a similar-sounding neighbor — corrected to the word's own attested ㄉ⺢ㄊㄑㄛㄨ after checking). **Chengyu**: [[因小失大]] matched a naive text grep but doesn't cite 奪 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 姻 (5250; 1748 characters remaining).

### 2026-08-07, iteration 757 — [[characters/姻|姻]]

Clean verification: `mc_id: 2307` exact at `lookup/CC/CC 2000.md` line 324. 形声 （女 semantic "woman" + 因 phonetic, OC \*qin) and readings (yīn / jan1 / 인 / IN / nhân) confirmed via Wiktionary. Filled the empty `pos` (`名詞`, matching the stand-in word [[婚姻]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added [[婚姻]], flagged as the `stand_in`, built from nothing. **Chengyu**: [[欲夫治汝]] matched a naive text grep but doesn't cite 姻 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 賓 (5251; 1747 characters remaining).

### 2026-08-07, iteration 758 — [[characters/賓|賓]]

**Real `graphemic_classification` bug found and fixed**: stored as `丐` — but 丐 is a wholly unrelated character ("to beg," with its own vault page) — 賓's real phonetic per Wiktionary is the rare, obsolete component 𡧍 (no vault page; OC \*mpin overall). Corrected `丐` → `𡧍`, plain text with an explanatory note since it has no page of its own.

Clean verification otherwise: `mc_id: 547` exact at `lookup/CC/CC 0000.md` line 568. Readings (bīn / ban1 / 빈 / HIN / tân) confirmed; `aliases: [賔, 宾]` both confirmed as genuine documented variant/simplified forms. Filled the empty `pos` (`名詞`, matching the stand-in word [[来賓]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, filtering out [[皆名]], [[某名]], [[毎名]], [[礼]], [[五礼]] as text-only false positives not citing 賓 in their own `characters:` field): [[来賓]] and [[菲律賓]] already listed; added the missing [[嘉賓]]. **Chengyu**: [[白頭偕老]] matched a naive text grep but doesn't cite 賓 in its own `characters:` field — correctly omitted. **Derived Characters** (1 hit): added [[檳]], which cites 賓 as its own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 寛 (5252; 1746 characters remaining).

### 2026-08-07, iteration 759 — [[characters/寛|寛]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests genuine Hán-Việt readings `khoan, khoăn` — added.

Clean verification otherwise: `mc_id: 966` exact at `lookup/CC/CC 0000.md` line 999 (listed under the traditional form 寬, correct). 形声 （宀 semantic "house" + 萈 phonetic, OC \*ɡoːn) and readings (kuān / fun1 / 관 / KAN・くつろ) confirmed via Wiktionary; `graphemic_classification: 萈` and `aliases: [寬]` (traditional/shinjitai pair) already correct. Filled the empty `pos` (`性詞`, matching the stand-in word [[寬大]]'s own `性詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section — noting the blank `hsk_level` correctly means "not present in the Old HSK lists," not a gap to fill.

**Words cross-check** (1 ground-truth hit, filtering out [[慣用]] as a same-looking-but-different-character false positive — 慣, not 寛/寬 — not citing this character at all): [[寬大]] already listed and already flagged as the `stand_in` — no change needed. **Chengyu**: [[海闊天空]] matched a naive text grep but doesn't cite 寛/寬 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 尋 (char) (5253; 1745 characters remaining).

### 2026-08-07, iteration 760 — [[characters/尋 (char)|尋]]

Clean verification: `mc_id: 1483` exact at `lookup/CC/CC 1000.md` line 504. 會意 (with phono-semantic elements: two hands measuring a mat, 口 added for emphasis, per Wiktionary) and readings (xún / cam4 / 심 / JIN・たず / chầm・tìm・tùm・tầm) confirmed; `graphemic_classification: 會意` and `aliases: [寻]` (confirmed standard simplified form) already correct. Filled the empty `pos` (`事詞`, matching the "seek/catch" action-verb pattern used throughout this loop). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[審訊]] and [[心]] as text-only false positives not citing 尋 in their own `characters:` field): added the self-referential `stand_in` [[尋]], built from nothing. **Chengyu**: [[意味深長]] matched a naive text grep but doesn't cite 尋 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 弾 (5255; 1744 characters remaining).

### 2026-08-07, iteration 761 — [[characters/弾|弾]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests the genuine Hán-Việt reading `đạn` — added.

Clean verification otherwise: `mc_id: 2075` exact at `lookup/CC/CC 2000.md` line 80 (listed under the traditional form 彈, correct). 形声 （弓 semantic "bow" + 単 phonetic — the shinjitai-consistent form of 單, OC \*daːn/\*daːns — shooting a pellet via slingshot) and readings (dàn / daan6 / 탄 / DAN・TAN・ひ) confirmed via Wiktionary; `aliases: [彈]` (traditional/shinjitai pair) already correct; `pos: 名詞` already correct. Replaced the malformed `# Notes` stub (bare unruby'd Words link mixed with floating CC-initial/final wikilinks) with the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (3 total ground-truth hits): [[弾丸]] already the `stand_in` but unlisted — added with flag; reformatted [[弾圧]] with proper ruby+gloss (was a bare unruby'd link); added the missing [[榴弾]]. **Chengyu**: added [[対牛弾琴]] (real hit, previously missing; [[珠投猪前]] was a text-only false positive not citing 弾). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 澈 (5256; 1743 characters remaining).

### 2026-08-07, iteration 762 — [[characters/澈|澈]]

**Real graphemic-classification and etymology-contamination bug found and fixed**: `graphemic_classification: 會意` was wrong, and the existing Notes bullet described an unrelated 會意 breakdown ("鬲 + 又, a hand removing utensils after eating") — that's actually 徹's *own* separate etymology as an independent compound character, mistakenly copied onto 澈's page (the two are close phonetic relatives, which likely caused the mix-up). Per Wiktionary, 澈 is properly 形声 (水 semantic + 徹 phonetic, abbreviated) and is itself documented as an alternative form of 徹/彻 for the "clear, limpid" sense — corrected the classification and rewrote the etymology bullet accordingly.

**Real fabricated `mc_id` bug found and fixed**: stored as `1590`, which belongs to the wholly unrelated 睹 — but 澈 itself doesn't appear anywhere in the CC 0000–3000 corpus at all (confirmed by direct search). Corrected to `0`, matching the established policy for characters confirmed absent from the ranking (same as [[characters/症|症]]).

**Confirmed `aliases: [徹, 彻]` are legitimate** — Wiktionary documents 澈 as an alternative form of 徹/彻 specifically for this "clear, limpid" sense, not contamination.

Readings (chè / cit3 / 철 / TETSU・DECHI・きよ / triệt) confirmed via Wiktionary; `pos: 事詞` already correct. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit): [[清澈]] already listed, flagged as the `stand_in`. **Chengyu**: [[澈頭澈尾]] already correctly listed, reformatted with proper ruby+gloss (was a bare unruby'd link). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 怪 (5257; 1742 characters remaining).

### 2026-08-07, iteration 763 — [[characters/怪|怪]]

Clean verification: `mc_id: 1086` exact at `lookup/CC/CC 1000.md` line 91. 形声 （心 semantic "heart" + 圣 phonetic, OC \*kruːds) and readings (guài / gwaai3 / 괴 / KAI・あや / quái・quảy・quấy・quế) confirmed via Wiktionary. Filled the empty `pos` (`性詞`, matching the stand-in word [[怪異]]'s own `性詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (5 total ground-truth hits, filtering out [[槐樹]], [[火車]], [[様子]], [[妖物]] as text-only false positives not citing 怪 in their own `characters:` field): [[怪異]] already listed; reformatted [[怪獣]] with proper ruby+gloss (was a bare unruby'd link); added the 3 missing — [[怪物]], [[妖怪]], [[奇怪]]. **Chengyu**: [[波乱万丈]], [[天衣無縫]], and [[魑魅罔両]] all matched a naive text grep but none cite 怪 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 戯 (5259; 1741 characters remaining).

### 2026-08-07, iteration 764 — [[characters/戯|戯]]

**Real `mandarin` bug found and fixed**: stored as `hū`, but Wiktionary confirms the standard reading for this "play, game, trick" sense is `xì` — corrected (also matches the citing word [[戯曲]]'s own attested `xìqǔ`).

**Real `graphemic_classification` bug found and fixed**: stored as `虚` (a common character with its own vault page), but Wiktionary's real phonetic component is the obsolete, unrelated `䖒` (also read xī, which likely caused the substitution) — corrected, kept as plain text since 䖒 has no vault page.

`mc_id: 1299` verified exact at `lookup/CC/CC 1000.md` line 312 (listed under the traditional form 戲). Filled the empty `pos` (`名詞`, matching the stand-in word [[戯曲]]'s own `名詞`). Rebuilt the malformed body into the proper 4-bullet `## Notes` section. `aliases: [戲, 戱, 戏]` all confirmed as legitimate traditional/variant/simplified forms.

**Words cross-check** (2 total ground-truth hits, both already listed): reformatted [[戯曲]] with proper ruby+gloss, flagged as the `stand_in`; confirmed [[遊戯]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 掃 (5260; 1740 characters remaining).

### 2026-08-07, iteration 765 — [[characters/掃|掃]]

**Real `graphemic_classification` bug found and fixed, same pattern as [[characters/析|析]]/[[characters/普|普]]/[[characters/逐|逐]]**: stored as `帚` (a component name, the 形声-style encoding), but 掃 is actually 會意 (手 "hand" + 帚 "broomstick" — sweeping, per Wiktionary), not 形声. Corrected `帚` → `會意`.

**Real `mc_id` off-by-one bug found and fixed**: stored as `2737`, but `lookup/CC/CC 2000.md` line 770 shows `2737. 燿` (an unrelated character) — 掃's real rank is `2738` (line 771). Corrected.

Readings (sǎo / sou3 / 소 / SOU・は / tảo) confirmed via Wiktionary; `aliases: [扫]` confirmed as the standard simplified form. Filled the empty `pos` (`実詞`, matching the stand-in word [[掃除]]'s own `実詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, both already listed): reformatted [[掃除]] with proper ruby+gloss, flagged as the `stand_in`; confirmed [[掃帚]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 抜 (5261; 1739 characters remaining).

### 2026-08-07, iteration 766 — [[characters/抜|抜]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests the genuine Hán-Việt reading `bạt` — added.

Clean verification otherwise: `mc_id: 945` exact at `lookup/CC/CC 0000.md` line 978 (listed under the traditional form 拔). 形声 （手 semantic "hand" + 犮 phonetic, OC \*bruːd/\*boːd/\*bod) and readings (bá / bat6 / 발 / BATSU・HATSU・ぬ) confirmed via Wiktionary; `aliases: [拔]` confirmed as the traditional counterpart. Filled the empty `pos` (`事詞`, matching the stand-in word [[選抜]]'s own `事詞`). Rebuilt the malformed body (Words section placed before Notes, floating CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section followed by `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[造幣局]] and [[物]] as text-only false positives not citing 抜 in their own `characters:` field): added the missing stand-in [[選抜]]; confirmed [[抜擢]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 擁 (5262; 1738 characters remaining).

### 2026-08-07, iteration 767 — [[characters/擁|擁]]

Clean verification: `mc_id: 1929` exact at `lookup/CC/CC 1000.md` line 970. 形声 （手 semantic "hand" + 雍 phonetic, OC \*qoŋ/\*qoŋʔ) and readings (yōng / jung2 / 옹 / YOU / ủng) confirmed via Wiktionary; `aliases: [拥]` confirmed as the standard simplified form. Filled the empty `pos` (`実詞`, matching the stand-in word [[抱擁]]'s own `実詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added [[抱擁]], flagged as the `stand_in`, built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 拠 (5264; 1737 characters remaining).

### 2026-08-07, iteration 768 — [[characters/拠|拠]]

**Real malformed-YAML bug found and fixed, same pattern as [[characters/霧 (char)|霧]]**: `japanese_native` was stored as a scalar `よ` immediately followed by a stray `- よる` list line — corrected to a proper two-item list. (The `vietnamese` field, flagged and already fixed in a prior word-sweep pass per [[依拠]]'s own log note, was already a clean list — no further action needed there.)

Clean verification otherwise: `mc_id: 975` exact at `lookup/CC/CC 0000.md` line 1008 (listed under the traditional form 據). 形声 （手 semantic "hand" + 豦 phonetic, OC \*kas/\*ɡa) and readings (jù / geoi3 / 거 / KYO・KO・よ・よる / cớ・cứ) confirmed via Wiktionary; `graphemic_classification: 豦`, `pos: 事詞`, and `aliases: [據, 据]` (traditional/simplified pair) all already correct. Rebuilt the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) into the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (5 total ground-truth hits, filtering out [[占]] and [[隠滅]] as text-only false positives not citing 拠 in their own `characters:` field): added the missing stand-in [[依拠]]; reformatted [[拠点]] with proper ruby+gloss (was a bare unruby'd link); added the 3 missing — [[根拠]], [[占拠]], [[証拠]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 称 (5265; 1736 characters remaining).

### 2026-08-07, iteration 769 — [[characters/称|称]]

**Confirmed `aliases: [稱, 秤]` are both legitimate** — checked 秤 against Wiktionary before assuming contamination (given 秤 "scale, steelyard" looks like a distinct modern word); Wiktionary documents 秤 as an alternative form of 稱 specifically for the obsolete "steelyard" sense under the chèng pronunciation, not a mistaken import.

Clean verification otherwise: `mc_id: 274` exact at `lookup/CC/CC 0000.md` line 286 (listed under the traditional form 稱). 形声 （禾 semantic "grain" + 爯 phonetic, OC \*tʰjɯŋ/\*tʰjɯŋs — originally "to weigh," extended to "call, name, praise") and readings (chēng / cing1 / 칭 / SHOU・あ / hấng・xưng・xứng) confirmed via Wiktionary. Filled the empty `pos` (`名詞`, matching the stand-in word [[名称]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, filtering out [[代名詞]], [[出谷記]], [[代詞]] as text-only false positives not citing 称 in their own `characters:` field): added the missing stand-in [[名称]] and [[対称]]; confirmed [[人称]]. **Chengyu**: added [[勿妄称名]] (real hit, previously missing; "Biblical Chengyu.md" is an index file with no `characters:` field, not a real chengyu entry). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 稲 (5266; 1735 characters remaining).

### 2026-08-07, iteration 770 — [[characters/稲|稲]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests genuine Hán-Việt readings `đạo, đữu` — added.

Clean verification otherwise: `mc_id: 1974` exact at `lookup/CC/CC 1000.md` line 1015 (listed under the traditional form 稻). 形声 （禾 semantic "grain" + 舀 phonetic, OC \*l'uːʔ) and readings (dào / dou6 / 도 / TOU・いね) confirmed via Wiktionary; `graphemic_classification: 舀`, `pos: 名詞`, and `aliases: [稻]` all already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[禾]] and [[道]] as text-only false positives not citing 稲 in their own `characters:` field): [[水稲]] already the `stand_in` but unlisted — added with flag; added the missing [[禾稲]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 窮 (5267; 1734 characters remaining).

### 2026-08-07, iteration 771 — [[characters/窮|窮]]

**Real malformed-YAML bug found and fixed, same pattern as [[characters/霧 (char)|霧]] and [[characters/拠|拠]]**: `japanese_native` was stored as a scalar `きわ` immediately followed by a stray `- きわ-める,きわ-まる` list line combining two more readings into one comma-joined item — reformatted into a proper three-item list (`きわ-める`, `きわ-まる`, `きわ`).

Clean verification otherwise: `mc_id: 532` exact at `lookup/CC/CC 0000.md` line 553. 形声 （穴 semantic "cave, confinement" + 躬 phonetic, OC \*ɡuŋ) and readings (qióng / kung4 / 궁 / KYUU / cùng) confirmed via Wiktionary; `aliases: [穷]` confirmed as the standard simplified form; `pos: 性詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, both already listed, filtering out [[日暮]] and [[理屈]] as text-only false positives not citing 窮 in their own `characters:` field): confirmed [[貧窮]] (already flagged as `stand_in`) and [[窮僻]] — no changes needed. **Chengyu**: [[石山盈界]] and [[孤立無援]] both matched a naive text grep but neither cites 窮 in its own `characters:` field — both correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 奇 (5268; 1733 characters remaining).

### 2026-08-07, iteration 772 — [[characters/奇|奇]]

**Real alias-contamination bug found and fixed, same pattern as [[characters/護|護]]/[[characters/貞|貞]]/[[characters/析|析]]/[[characters/遵|遵]]**: `aliases` included `畸` and `綺` — but Wiktionary describes both only as *derived characters* that use 奇 as their own phonetic component, not as documented variants of 奇 itself (the real documented variants are `竒` and an unencoded composition, neither with a vault page). Removed both.

`mc_id: 827` verified exact at `lookup/CC/CC 0000.md` line 857; `graphemic_classification: 可` and `pos: 性詞` both already correct. 形声 （大 semantic "big" + 可 phonetic, OC \*kral/\*ɡral) and readings confirmed via Wiktionary. Rebuilt the malformed body (a crammed initials/finals bullet, an informal "abbreviation for xenon" note, and two bare unruby'd Words links) into the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (5 total ground-truth hits, filtering out [[様子]], [[妙]], [[偶数]], [[倚]] as text-only false positives not citing 奇 in their own `characters:` field): added the missing stand-in [[奇怪]]; reformatted [[奇妙]], [[奇数]] (bare links) and promoted the informal [[奇素]] note to a proper Words entry; confirmed [[奇想]]. **Chengyu**: [[波乱万丈]], [[唇亡歯寒]], and [[天衣無縫]] all matched a naive text grep but none cite 奇 in their own `characters:` field — all three correctly omitted. **Derived Characters** (4 hits): added [[寄 (char)|寄]], [[倚 (char)|倚]], [[椅]], [[騎]], all of which cite 奇 as their own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 糾 (char) (5270; 1732 characters remaining).

### 2026-08-07, iteration 773 — [[characters/糾 (char)|糾]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1759`, but `lookup/CC/CC 1000.md` line 792 shows `1759. 渭` (an unrelated character) — 糾's real rank is `1760` (line 793). Corrected (Notes prose updated to match).

**Confirmed `aliases: [丩, 纠, 糺]` are all legitimate** — unlike the recent 護/貞/析/遵/奇 contamination cases, Wiktionary confirms 丩 here is not just the phonetic component but 糾's own genuine original form (丩 "originally referred to this word" before 糸 was added as a semantic determiner) — a real exception to the usual pattern, not a bug.

Notes section was already well-formed (形声, 糸 semantic + 丩 phonetic, OC \*kriwʔ) from an earlier partial pass; `graphemic_classification: 丩` already correct. Filled the empty `pos` (`事詞`, matching the "twist/investigate" action-verb pattern e.g. [[characters/捉|捉]]). Built the empty `## Words` section from scratch.

**Words cross-check** (1 ground-truth hit, filtering out [[臼]], [[赳赳]], [[旧]] as text-only false positives not citing 糾 in their own `characters:` field): added the self-referential `stand_in` [[糾]]. **Chengyu**/**Derived Characters**: no hits — both correctly left empty/omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 紛 (char) (5271; 1731 characters remaining).

### 2026-08-07, iteration 774 — [[characters/紛 (char)|紛]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1601`, but `lookup/CC/CC 1000.md` line 630 shows `1601. 矯` (an unrelated character) — 紛's real rank is `1602` (line 631). Corrected.

形声 （糸 semantic "silk" + 分 phonetic, OC \*pʰɯn) and readings (fēn / fan1 / 분 / FUN / phân・phăn) confirmed via Wiktionary; `graphemic_classification: 分` and `aliases: [纷]` (standard simplified form) already correct. Filled the empty `pos` (`性詞`). Rebuilt the malformed body into the proper 4-bullet `## Notes` section plus `## Words`.

**Flagged, not fixed (out of scope)**: `words/紛.md`'s own `注音` (ㄆㄨㄋ) doesn't match the character's own attested reading (ㄈㄜㄋ) — likely a word-sweep data error; used the character's own correct reading for its self-referential Words citation instead of the word file's mismatched one.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[紛]] (per the `tags: [hapax]` marker, an established call on this page that 紛 counts as its own stand-in despite being bound); reformatted [[紛争]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 緒 (5272; 1730 characters remaining).

### 2026-08-07, iteration 775 — [[characters/緒|緒]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `2262`, but `lookup/CC/CC 2000.md` line 275 shows `2262. 盲` (an unrelated character) — 緒's real rank is `2263` (line 276). Corrected.

形声 （糸 semantic "silk" + 者 phonetic, OC \*ljaʔ — "thread end," extended to "beginning, state of mind") and readings (xù / seoi5 / 서 / SHO・CHO・お / tự) confirmed via Wiktionary; `graphemic_classification: 者` and `aliases: [緖, 绪]` (orthodox/kyūjitai and simplified forms respectively) already correct. Filled the empty `pos` (`名詞`, matching the stand-in word [[心緒]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, filtering out [[共]] and [[偕同]] as text-only false positives not citing 緒 in their own `characters:` field): [[心緒]] already listed and flagged as the `stand_in`; added the missing [[端緒]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 維 (5273; 1729 characters remaining).

### 2026-08-07, iteration 776 — [[characters/維|維]]

Clean verification: `mc_id: 922` exact at `lookup/CC/CC 0000.md` line 955. 形声 （糸 semantic "silk, cord" + 隹 phonetic, abbreviated from 唯, OC \*ɢʷi — the manipulation rope of a net, extended to "tie, maintain") and readings (wéi / wai4 / 유 / I・YUI / duy) confirmed via Wiktionary; `aliases: [维]` confirmed as the standard simplified form. Filled the empty `pos` (`実詞`, matching the stand-in word [[維持]]'s own `実詞`). Replaced the malformed body (an unlinked prose fragment plus floating CC-initial/final wikilinks) with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[持]], [[回紇]], [[治安]], [[合成]], [[保持]] as text-only false positives not citing 維 in their own `characters:` field): added the missing stand-in [[維持]], built from nothing. **Chengyu**: [[万物生長]], [[哀鴻遍野]], and [[磨穿鉄硯]] all matched a naive text grep but none cite 維 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 粛 (5274; 1728 characters remaining).

### 2026-08-07, iteration 777 — [[characters/粛|粛]]

**Real alias-contamination bug found and fixed, largest case yet**: `aliases` included `嘯`, `嘨`, `啸`, `歗`, `哨` alongside the legitimate `肅`/`肃` — but Wiktionary confirms these five all merely *share the same phonetic series* as 肅 (used in compounds like 嘯 "to whistle"), and are documented as **separate characters with their own entries**, not variants of 肅 itself. Double-checked the one with a vault page ([[哨]]) directly: its own `graphemic_classification` is `肖`, completely unrelated to 肅/粛 — confirming it was never actually derived from this character at all. Removed all five.

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests the genuine Hán Nôm reading `túc` — added.

**Flagged, not fixed (out of scope, but not added to Words either)**: `words/海粛.md` cites 粛 in its own `characters:` field, but its `mandarin: "hǎixiào"` and gloss "tsunami" both match 海嘯 (using 嘯, "to roar/whistle," not 粛/肅 "solemn") — almost certainly a wrong-character bug in the word file, likely downstream of the very alias contamination just removed. Unlike a genuine but under-cited real word, this citation doesn't reflect 粛's actual meaning, so it was excluded from the Words list rather than added as a "hit."

`mc_id: 1105` verified exact at `lookup/CC/CC 1000.md` line 114 (listed under the traditional form 肅); `graphemic_classification: 會意` and `pos: 性詞` both already correct (Shuowen's own analysis of 肅/粛 is itself disputed/unclear per Wiktionary, consistent with the type-string encoding already in place). Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 genuine ground-truth hit after excluding the flagged 海粛 mismatch, and filtering out [[厳然]] as a text-only false positive not citing 粛 in its own `characters:` field): [[厳粛]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 慮 (5276; 1727 characters remaining).

### 2026-08-07, iteration 778 — [[characters/慮|慮]]

Clean verification: `mc_id: 798` exact at `lookup/CC/CC 0000.md` line 825. 形声 （思 semantic "to think" + 虍 phonetic, OC \*qʰaː, overall \*ras) and readings (lǜ / leoi6 / 려 / RYO・ROKU・おもんぱか / lo・lợ・lự) confirmed via Wiktionary; `aliases: [虑]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[不安]] as a text-only false positive not citing 慮 in its own `characters:` field): added the missing stand-in [[考慮]] and [[憂慮]], both built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 触 (5277; 1726 characters remaining).

### 2026-08-07, iteration 779 — [[characters/触|触]]

Clean verification: `mc_id: 1537` exact at `lookup/CC/CC 1000.md` line 562 (listed under the traditional form 觸). 形声 （角 semantic "horn" + 蜀 phonetic, OC \*djoɡ) and readings (chù / zuk1 / 촉 / SHOKU・SOKU・さわ / xúc) confirmed via Wiktionary; `aliases: [觸]`, `graphemic_classification: 蜀`, and `pos: 事詞` all already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[味覚]] and [[言及]] as text-only false positives not citing 触 in their own `characters:` field): added the missing stand-in [[接触]] and [[感触]], both built from nothing. **Chengyu**: added [[一触即発]] (real hit, previously missing; "Misc. Chengyu.md" is an index file with no `characters:` field, not a real chengyu entry). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 訂 (char) (5278; 1725 characters remaining).

### 2026-08-07, iteration 780 — [[characters/訂 (char)|訂]]

`mc_id: 5273` lies beyond the CC files' 4000-entry coverage — 訂 doesn't appear anywhere in `lookup/CC/CC 0000.md` through `CC 3000.md` (neither does its own phonetic 丁, oddly, despite being common), but unlike [[characters/澈|澈]]'s recently-corrected fabricated value there's no verifiable evidence this one is wrong (no nearby unrelated character it could be confused with, since it's out of range) — retained as real long-tail data per policy (same as [[characters/貯|貯]], [[characters/捉|捉]], [[characters/透 (char)|透]]). 形声 （言 semantic "speech" + 丁 phonetic, OC \*teːŋ) and readings (dìng / ding3 / 정 / TEI・CHOU・ただ / dính・đính) confirmed via Wiktionary; `aliases: [订]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`, matching the citing word [[校訂]]'s own `事詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[訂]] and [[校訂]], both built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 貢 (5279; 1724 characters remaining).

### 2026-08-07, iteration 781 — [[characters/貢|貢]]

Clean verification: `mc_id: 751` exact at `lookup/CC/CC 0000.md` line 778. 形声 （貝 semantic "valuables" + 工 phonetic, OC \*koːŋs) and readings (gòng / gung3 / 공 / KOU・KU・みつ / cóng・cống・gúng・gỏng・xống) confirmed via Wiktionary; `aliases: [贡]` confirmed as the standard simplified form. Filled the empty `pos` (`名詞`, matching the stand-in word [[貢品]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, filtering out [[貿易]], [[希州]], [[柴棍]] as text-only false positives not citing 貢 in their own `characters:` field): [[貢品]] already listed and flagged as the `stand_in`; reformatted [[貢献]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-07`.

Next never-perfected character by `danayo_id`: 貫 (5280; 1723 characters remaining).

### 2026-08-08, iteration 782 — [[characters/貫|貫]]

**Real `graphemic_classification` bug found and fixed**: stored as `毌` (a component name, the 形声-style encoding), but Wiktionary's Glyph Origin section is explicit that 貫 is 象形 — "two 貝 (shell) strung together" — and calls the Shuowen's own compound-of-毌+貝 analysis a historical mistake. Corrected `毌` → `象形`.

Clean verification otherwise: `mc_id: 1400` exact at `lookup/CC/CC 1000.md` line 417. Readings (guàn / gun3 / 관 / KAN・WAN・つらぬ / quan・quen・quán) confirmed; `aliases: [贯]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`; the existing `動詞` tag on the citing word [[貫通]] predates the current taxonomy). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit): [[貫通]] already listed and flagged as the `stand_in` — no change needed. **Chengyu**: [[澈頭澈尾]] matched a naive text grep but doesn't cite 貫 in its own `characters:` field — correctly omitted. **Derived Characters** (1 hit): added [[慣]], which cites 貫 as its own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 輝 (5281; 1722 characters remaining).

### 2026-08-08, iteration 783 — [[characters/輝|輝]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3407`, but `lookup/CC/CC 3000.md` line 428 shows `3407. 糗` (an unrelated character) — 輝's real rank is `3408` (line 429). Corrected.

形声 （光 semantic "light" + 軍 phonetic, OC \*qʰul) and readings (huī / fai1 / 휘 / KI・KUN・かがや / huy) confirmed via Wiktionary; `aliases: [辉]` confirmed as the standard simplified form. Filled the empty `pos` (`性詞`, matching the stand-in word [[光輝]]'s own `性詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added [[光輝]], flagged as the `stand_in`, built from nothing. **Chengyu**: [[古今東西]] and [[日月星辰]] both matched a naive text grep but neither cites 輝 in its own `characters:` field — both correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 違 (5282; 1721 characters remaining).

### 2026-08-08, iteration 784 — [[characters/違|違]]

Clean verification: `mc_id: 939` exact at `lookup/CC/CC 0000.md` line 972. 形声 （辵 semantic "movement" + 韋 phonetic, OC \*ɢʷɯl) and readings (wéi / wai4 / 위 / I / vi) confirmed via Wiktionary; `aliases: [违]` confirmed as the standard simplified form; `pos: 事詞` already correct. Replaced the floating CC-initial/final wikilinks (with two bare unruby'd Words links crammed underneath) with the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (3 total ground-truth hits, filtering out [[反]], [[周魚]], [[意見]], [[公約]], [[不同]] as text-only false positives not citing 違 in their own `characters:` field): added the missing stand-in [[違反]]; reformatted [[違犯]] and [[違法]] with proper ruby+gloss (were bare unruby'd links). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 酔 (char) (5283; 1720 characters remaining).

### 2026-08-08, iteration 785 — [[characters/酔 (char)|酔]]

**Real malformed-YAML bugs found and fixed, same pattern as [[characters/霧 (char)|霧]]/[[characters/拠|拠]]/[[characters/窮|窮]]**: `japanese_native` was a scalar `よ` plus a stray `- よ-う` list line, and `vietnamese` was a single comma-joined item `"túy, xúy"` — both reformatted into proper lists.

Clean verification otherwise: `mc_id: 1600` exact at `lookup/CC/CC 1000.md` line 625 (listed under the traditional form 醉). 形声 （酉 semantic "alcoholic drink" + 卒 phonetic, OC \*ʔsuːd/\*sʰuːd/\*ʔsud, overall \*ʔsuds) and readings (zuì / zeoi3 / 취 / SUI・よ・よ-う / túy・xúy) confirmed via Wiktionary; `aliases: [醉]`, `graphemic_classification: 卒`, and `pos: 事詞` all already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[馳]], [[池]], [[酩酊]], [[知]] as text-only false positives not citing 酔 in their own `characters:` field): added the self-referential `stand_in` [[酔]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 釈 (5284; 1719 characters remaining).

### 2026-08-08, iteration 786 — [[characters/釈|釈]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests the genuine Hán Nôm reading `thích` — added.

Clean verification otherwise: `mc_id: 883` exact at `lookup/CC/CC 0000.md` line 913 (listed under the traditional form 釋). 形声 （釆 semantic "distinguish" + 睪 phonetic, OC \*neb/\*laːɡ/\*kuː, overall \*hljaɡ) and readings (shì / sik1 / 석 / SHAKU・EKI・とく) confirmed via Wiktionary; `aliases: [釋]` confirmed as the traditional counterpart. Filled the empty `pos` (`事詞`, matching the stand-in word [[解釈]]'s own `事詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, filtering out [[何様]] as a text-only false positive not citing 釈 in its own `characters:` field): [[希釈]] and [[解釈]] already listed (latter flagged as `stand_in`); added the 2 missing — [[釈放]] and the proper-noun compound [[釈珈文尼]] (Śākyamuni). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 鋭 (5285; 1718 characters remaining).

### 2026-08-08, iteration 787 — [[characters/鋭|鋭]]

Clean verification: `mc_id: 1516` exact at `lookup/CC/CC 1000.md` line 541 (listed under the traditional form 銳). 形声 （金 semantic "metal" + 兌 phonetic, OC \*lods/\*l'oːds) and readings (ruì / jeoi6 / 예 / EI・TAI・するど / duệ・nhuệ・nhọn) confirmed via Wiktionary; `aliases: [銳, 锐]` (traditional/simplified pair) and `pos: 性詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits): [[鋭利]] already listed and flagged as the `stand_in`; added the missing [[精鋭]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 閲 (5286; 1717 characters remaining).

### 2026-08-08, iteration 788 — [[characters/閲|閲]]

**Real `mc_id` bug found and fixed**: stored as `2307` — but that's actually [[characters/姻|姻]]'s own rank (used correctly there earlier this session); 閱's real rank is `2308` (`lookup/CC/CC 2000.md` line 325, immediately after 姻 at line 324) — a same-neighbor mix-up rather than the usual off-by-one-in-a-different-direction. Corrected.

形声 （門 semantic "door, gate" + 兌 phonetic, OC \*l'oːds, overall \*lod) and readings (yuè / jyut6 / 열 / ETSU・けみ / duyệt・dượt) confirmed via Wiktionary; `aliases: [閱, 阅]` (Japanese shinjitai/simplified pair) and `pos: 事詞` already correct. Removed a stray irrelevant bullet ("閱 was added to the Korean HS list in 2000") and rebuilt into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, both already listed): reformatted [[検閲]] with proper ruby+gloss (correcting a stray middle-dot in the rt text against the word's own attested 注音) and flagged as the `stand_in`; reformatted [[閲読]] (was a bare unruby'd link). **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 陣 (5287; 1716 characters remaining).

### 2026-08-08, iteration 789 — [[characters/陣|陣]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `2352`, but `lookup/CC/CC 2000.md` line 369 shows `2352. 編` (an unrelated character) — 陣's real rank is `2353` (line 370). Corrected.

Etymology is genuinely mixed (originally 會意 via 敶, but Wiktionary itself states 陳 functions as the modern phonetic series component) — kept the existing `graphemic_classification: 陳` as a defensible synchronic 形声 reading rather than forcing a type-string change, and noted the nuance in the Notes bullet. Readings (zhèn / zan6 / 진 / JIN・CHIN / chận・chặn・giận・trận・trặn) confirmed via Wiktionary; `aliases: [阵]` confirmed as the standard simplified form. Filled the empty `pos` (`名詞`, matching the stand-in word [[陣営]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) with the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[敵人]], [[行列]], [[地位]] as text-only false positives not citing 陣 in their own `characters:` field): added the missing stand-in [[陣営]] and [[陣地]]. **Chengyu**: [[弱不禁風]] matched a naive text grep but doesn't cite 陣 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 随 (5288; 1715 characters remaining).

### 2026-08-08, iteration 790 — [[characters/随|随]]

**Real `graphemic_classification` bug found and fixed**: stored as `迶` (a real, distinct Unicode character), but Wiktionary's Glyph Origin section explicitly names the true phonetic as the unencoded, extremely rare `𡐦` (a redlink even on Wiktionary itself) — corrected, kept as plain text since it has no vault page.

**Confirmed `aliases: [隨, 陏]` are both legitimate** — 隨 is the standard traditional form; 陏 is documented as a genuine (if since-abolished) "second-round simplification" (二简字) rather than contamination from an unrelated character, unlike the recent 護/貞/析/遵/奇/粛 cases.

`mc_id: 615` verified exact at `lookup/CC/CC 0000.md` line 639 (listed under the traditional form 隨); `pos: 事詞` already correct. Replaced the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) with the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (4 total ground-truth hits, filtering out [[堕天使]] and [[堕落]] as false positives from the visually similar but distinct character 堕): reformatted [[随行]] with proper ruby, flagged as the `stand_in`; confirmed [[随性]]; added the 2 missing — [[随意]] and [[追随]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 享 (5289; 1714 characters remaining).

### 2026-08-08, iteration 791 — [[characters/享|享]]

Clean verification: `mc_id: 1177` exact at `lookup/CC/CC 1000.md` line 186. 象形 (an ancestral shrine, originally identical to 饗 "banquet feast," per Wiktionary) and readings (xiǎng / hoeng2 / 향 / KYOU・う / hưởng) confirmed; `graphemic_classification: 象形` already correct. Filled the empty `pos` (`事詞`, matching the stand-in word [[享受]]'s own `事詞`). Rebuilt the malformed body (an unlinked prose etymology note mixed with floating CC-initial/final wikilinks, a bare unruby'd Words link) into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): reformatted [[享受]] with proper ruby+gloss, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 僅 (5290; 1713 characters remaining).

### 2026-08-08, iteration 792 — [[characters/僅|僅]]

**Real `graphemic_classification` bug found and fixed, subtle glyph-confusion case**: stored as `菫` (grass radical, "celery/aconite" — a real character with its own vault page), but Wiktionary's Glyph Origin names the true phonetic as `堇` (earth radical, "clay/drought," U+5807) — two visually near-identical but genuinely distinct characters. Corrected, kept as plain text since 堇 itself has no vault page (unlike 菫, which does and is now correctly excluded).

Clean verification otherwise: `mc_id: 2672` exact at `lookup/CC/CC 2000.md` line 701. Readings (jǐn / gan2 / 근 / KIN・わず / cẩn・ngẩn) confirmed via Wiktionary; `aliases: [仅]` confirmed as the standard simplified form. Filled the empty `pos` (`擬詞`, matching the stand-in word [[僅僅]]'s own tag for this limiting-adverb class). Rebuilt the malformed body (a bare unruby'd Words link mixed with floating CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[不但]] as a text-only false positive not citing 僅 in its own `characters:` field): reformatted [[僅僅]] with proper ruby+gloss, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 儀 (5291; 1712 characters remaining).

### 2026-08-08, iteration 793 — [[characters/儀|儀]]

Clean verification: `mc_id: 591` exact at `lookup/CC/CC 0000.md` line 612. 形声 （人 semantic "person" + 義 phonetic, OC \*ŋrals, overall \*ŋral) and readings (yí / ji4 / 의 / GI / nghe・nghi・nghè・nghì・nghỉ・ngơi) confirmed via Wiktionary; `aliases: [仪]` confirmed as the standard simplified form; `pos: 性詞` already correct. Replaced the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) with the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (4 total ground-truth hits, filtering out [[九経]], [[射術]], [[五射]], [[剣道]], [[失礼]] as text-only false positives not citing 儀 in their own `characters:` field): added the missing stand-in [[儀式]]; reformatted [[儀仗]] with proper ruby+gloss (was a bare unruby'd link, and initially mis-copied its 注音 from a similar-looking neighbor — corrected to the word's own attested ㄜㄧㄐㄚㄫ after checking); added the 2 missing — [[儀礼]] and [[地球儀]]. **Chengyu**: [[対牛弾琴]] matched a naive text grep but doesn't cite 儀 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 励 (5292; 1711 characters remaining).

### 2026-08-08, iteration 794 — [[characters/励|励]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3233`, but `lookup/CC/CC 3000.md` line 246 shows `3233. 刈` (an unrelated character) — 励's real rank is `3234` (line 247, listed under the traditional form 勵). Corrected. **Minor YAML normalization**: `japanese: REI` was a bare scalar instead of the standard single-item list — reformatted for consistency.

形声 （力 semantic "strength" + 厉 phonetic, traditional 厲, OC \*m·rads) and readings (lì / lai6 / 려 / REI・はげ / lệ) confirmed via Wiktionary; `aliases: [勵]` confirmed as the traditional counterpart, and `graphemic_classification: 厉` confirmed correct as-is (matches the vault's own canonical simplified-form filename for this component, [[厉 (char)|厉]]). `pos: 事詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, filtering out [[勉]] as a text-only false positive not citing 励 in its own `characters:` field): added the missing stand-in [[激励]]; reformatted [[勉励]] with proper ruby+gloss (was a bare unruby'd link); added the missing [[奨励]]. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 却 (char) (5293; 1710 characters remaining).

### 2026-08-08, iteration 795 — [[characters/却 (char)|却]]

**Real `graphemic_classification` bug found and fixed**: stored as `去` (a common, similarly-pronounced but wholly unrelated character with its own vault page, "to go/leave"), but Wiktionary's Glyph Origin names the true phonetic as the rare, unencoded `𧮫` (jué) — corrected, kept as plain text.

`mc_id: 9007` lies beyond the CC files' 4000-entry coverage — retained as real long-tail data per policy (same as [[characters/訂 (char)|訂]], [[characters/透 (char)|透]]). Readings (què / koek3 / 각 / KYAKU・かえ / khước) confirmed via Wiktionary; `aliases: [卻]` confirmed as the traditional counterpart. Filled the empty `pos` (`連接詞`, matching the contrastive-conjunction sibling [[characters/但 (char)|但]]). Minor YAML normalization: `japanese` was a bare scalar instead of a list. Rebuilt the body into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[却]] and [[忘却]], both built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 弔 (char) (5294; 1709 characters remaining).

### 2026-08-08, iteration 796 — [[characters/弔 (char)|弔]]

**Real `graphemic_classification` bug found and fixed**: stored as `象形`, but Wiktionary's Glyph Origin explicitly calls it 會意 — "an ideogram of 約 ('to bind, tie')," depicting a person with a corded arrow wound around the body. Corrected `象形` → `會意`.

**Real `mc_id` off-by-one bug found and fixed**: stored as `1570`, but `lookup/CC/CC 1000.md` line 595 shows `1570. 錄` (an unrelated character) — 弔's real rank is `1571` (line 596). Corrected.

**Verified, not changed**: a Wiktionary fetch initially suggested Cantonese `dik1` instead of the stored `diu3`, but that reading turned out to be tied to an obsolete secondary etymology ("to reach," "good"), not the mourn/condole sense this page covers — cross-checked against `words/弔.md`'s own long-attested `cantonese: diu3` and left unchanged, trusting the more specific, consistent source over an ambiguous fetch.

Readings otherwise (diào / 조 / CHOU・TEKI・とぶら / điếu) confirmed; `aliases: [吊]` confirmed as a genuine documented variant. Filled the empty `pos` (`事詞`, matching mourning-sense sibling [[characters/喪|喪]]). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added the self-referential `stand_in` [[弔]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 啓 (5295; 1708 characters remaining).

### 2026-08-08, iteration 797 — [[characters/啓|啓]]

**Real half-finished-fix bug found and completed**: the Notes section contained a stray, unattached number `1384` — investigation confirmed this is 啟's genuine CC frequency rank (`lookup/CC/CC 1000.md` line 401), meaning a prior pass had already looked up the correct value but never applied it to `mc_id` (still wrongly `7634`, nowhere near the CC corpus's actual range) nor cleaned up the leftover note. Corrected `mc_id` to `1384` and removed the orphaned number.

**Real `graphemic_classification` bug found and fixed, same pattern as [[characters/析|析]]/[[characters/普|普]]/[[characters/逐|逐]]/[[characters/掃|掃]]/[[characters/啓|啓 itself, sibling 却]]**: stored as `启` (a component name, the 形声-style encoding), but Wiktionary confirms 啟/啓 is 會意 — 戶 ("door") + 又/攴 ("hand"), a hand opening a door. Corrected `启` → `會意`.

Readings (qǐ / kai2 / 계 / KEI・ひら / khải・khới) confirmed via Wiktionary; `aliases: [啟, 启]` (traditional/simplified pair) confirmed legitimate. Filled the empty `pos` (`事詞`). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, both already listed, filtering out [[太白星]] and [[論理]] as text-only false positives not citing 啓 in their own `characters:` field): confirmed [[開啓]] (flagged as `stand_in`) and [[啓明]] — no changes needed. **Chengyu**/**Derived Characters**: no hits (an initial grep hit on the character's own file was a self-match artifact, not a real derived character) — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 哲 (5296; 1707 characters remaining).

### 2026-08-08, iteration 798 — [[characters/哲|哲]]

**Real malformed-YAML bug found and fixed**: `japanese_native` had `あきらか` duplicated (once as a bare scalar, once again inside the following list) — deduplicated into a clean two-item list (`あきらか`, `さとい`).

Clean verification otherwise: `mc_id: 2060` exact at `lookup/CC/CC 2000.md` line 65. 形声 （口 semantic "mouth" + 折 phonetic, OC \*l'eːl/\*ʔljed/\*ɦljed, overall \*ʔl'ed) and readings (zhé / zit3 / 철 / TETSU・あきらか・さとい / triết・chít・trết・trít) confirmed via Wiktionary; `aliases: [喆]` confirmed as a genuine documented variant; `pos: 名詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[分析]] and [[学位]] as text-only false positives not citing 哲 in their own `characters:` field): added the missing stand-in [[哲学]], built from nothing. **Chengyu**: [[哀鴻遍野]], [[対牛弾琴]], [[時代錯誤]], and [[色即是空]] all matched a naive text grep but none cite 哲 in their own `characters:` field — all four correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 泥 (char) (5298; 1706 characters remaining).

### 2026-08-08, iteration 799 — [[characters/泥 (char)|泥]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1978`, but `lookup/CC/CC 1000.md` line 1019 shows `1978. 技` (an unrelated character) — 泥's real rank is `1979` (line 1020). Corrected.

形声 （水 semantic "water" + 尼 phonetic, OC \*niːl) and readings (ní / nai4 / 니 / DEI・どろ / ne・nè・nê・nề・nể・nệ) confirmed via Wiktionary; `aliases: [坭]` confirmed as a genuine documented variant; `pos: 名詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, filtering out [[鰌魚]] and [[不丹]] as text-only false positives not citing 泥 in their own `characters:` field): added the self-referential `stand_in` [[泥]] and the missing [[拘泥]]; confirmed [[泥婆羅]]. **Chengyu**: added [[汗食帰泥]] (real hit, previously missing; "Biblical Chengyu.md" is an index file, [[詛地哀食]] and [[金銀銅鉄]] were text-only false positives). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 暁 (5299; 1705 characters remaining).

### 2026-08-08, iteration 800 — [[characters/暁|暁]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests the genuine Hán-Việt reading `hiểu` — added.

Clean verification otherwise: `mc_id: 1617` exact at `lookup/CC/CC 1000.md` line 646 (listed under the traditional form 曉). 形声 （日 semantic "sun" + 尭 phonetic, traditional 堯, OC \*hŋeːwʔ) and readings (xiǎo / hiu2 / 효 / GYOU・KYOU・あかつき) confirmed via Wiktionary; `aliases: [曉]` and `pos: 名詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added [[破暁]], flagged as the `stand_in`, built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 濃 (5301; 1704 characters remaining).

### 2026-08-08, iteration 801 — [[characters/濃|濃]]

**Real broken-link bug found and fixed**: the existing Notes bullet had an empty component link (`phonetic [[]]`) where 農 belonged — filled in.

`mc_id` 4765 lies beyond the CC files' 4000-entry coverage — 濃 itself doesn't appear anywhere in `lookup/CC/CC 0000.md` through `CC 3000.md` (its phonetic 農 does, at rank 638, but that's a distinct character's own rank) — retained as real long-tail data per policy, no evidence of fabrication found. 形声 （水 semantic + 農 phonetic, OC \*noŋ, phonetic itself \*nuːŋ) and readings (nóng / nung4 / 농 / NOU・JOU・こ / nông・nùng・nống・nồng) confirmed via Wiktionary; `graphemic_classification: 農` already correct; `aliases: [浓]` confirmed as the standard simplified form. Filled the empty `pos` (`性詞`, matching sibling [[characters/厚 (char)|厚]]). Removed a stray irrelevant bullet ("Dropped from the Korean HS list in 2000") and rebuilt into the proper 4-bullet form — noting `hanmun_edu_level: 名` maps to [[Korean Name ㄴ]] (keyed by the first Hangul consonant of the Korean reading, 농).

**Words cross-check** (1 ground-truth hit, filtering out [[厚]] as a text-only false positive not citing 濃 in its own `characters:` field): [[濃厚]] already listed and already flagged as the `stand_in` — no change needed. **Chengyu**: [[安心立命]] matched a naive text grep but doesn't cite 濃 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 塗 (5302; 1703 characters remaining).

### 2026-08-08, iteration 802 — [[characters/塗|塗]]

**Real `graphemic_classification` bug found and fixed**: stored as `余` — but that's actually the phonetic of the related, near-homophone character [[characters/途|途]] ("road, path"); Wiktionary confirms 塗's own real phonetic is `涂` (which also happens to double as the standard simplified form). Corrected `余` → `涂`.

Clean verification otherwise: `mc_id: 1280` exact at `lookup/CC/CC 1000.md` line 293. 形声 （土 semantic "earth" + 涂 phonetic, OC \*rlaː/\*l'aː) and readings (tú / tou4 / 도 / TO・ぬ / đồ) confirmed via Wiktionary; `pos: 事詞` already correct. Removed a stray irrelevant bullet ("added to the Korean HS list in 2000") and a malformed relative-markdown radical link, rebuilding into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[弧度]] as a same-romanization-coincidence false positive not citing 塗 in its own `characters:` field): added the missing stand-in [[塗抹]] and [[糊塗]]. **Chengyu**: [[粉骨砕身]] matched a naive text grep but doesn't cite 塗 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 涙 (char) (5303; 1702 characters remaining).

### 2026-08-08, iteration 803 — [[characters/涙 (char)|涙]]

**Real missing-content bug found and fixed**: `vietnamese` was empty, but Wiktionary attests the genuine Hán-Việt reading `lệ` — added.

**Real `mc_id` off-by-one bug found and fixed**: stored as `3842`, but `lookup/CC/CC 3000.md` line 879 shows `3842. 惙` (an unrelated character) — 涙's real rank is `3843` (line 880, listed under the traditional form 淚). Corrected.

形声 （水 semantic "water" + 戻 phonetic, traditional 戾, OC \*rɯːds/\*rɯːd, overall \*ruds) and readings (lèi / leoi6 / 루 / RUI・REI・なみだ) confirmed via Wiktionary; `graphemic_classification: 戻` and `aliases: [淚]` (shinjitai/traditional pair, same pattern as [[characters/弾|弾]]/単) already correct; `pos: 名詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit): added the self-referential `stand_in` [[涙]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 漸 (5304; 1701 characters remaining).

### 2026-08-08, iteration 804 — [[characters/漸|漸]]

Clean verification: `mc_id: 1314` exact at `lookup/CC/CC 1000.md` line 331. 形声 （水 semantic "water" + 斬 phonetic, OC \*zamʔ) and readings (jiàn / zim6 / 점 / ZEN・SEN・ZAN・すす / tiêm・tiềm・tiệm・tràn・trờm) confirmed via Wiktionary; `aliases: [渐]` confirmed as the standard simplified form. Filled the empty `pos` (`擬詞`, matching the stand-in word [[漸漸]]'s own tag for this gradual-adverb class). Replaced the floating CC-initial/final wikilinks (with a bare unruby'd Words bullet crammed underneath) with the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (2 total ground-truth hits): added the missing stand-in [[漸漸]]; reformatted [[漸近線]] with proper ruby+gloss (was a bare unruby'd link). **Chengyu**: [[意味深長]] matched a naive text grep but doesn't cite 漸 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 湿 (char) (5305; 1700 characters remaining).

### 2026-08-08, iteration 805 — [[characters/湿 (char)|湿]]

**Confirmed `graphemic_classification: 显` is legitimate, not a substitution error**: Wiktionary names the real phonetic as `㬎`, but the vault's own `[[顯|显]]` page lists `㬎` among its own aliases — same underlying character, canonical vault page name, consistent with how the vault already handles other variant-glyph citations.

**Flagged, not fixed (data genuinely inconsistent across the vault, not a clear single error)**: the character's own `注音`/`羅馬字` (`ㄙㄜㄆ`/sǝb) disagree with two of its three citing words. Initially assumed the character was wrong and started correcting it to match — but on rechecking, the citing words themselves split evenly: [[湿度]] and the self-referential [[湿]] both use `ㄙㄧㄆ`/sib, while [[除湿]] independently uses `ㄙㄜㄆ`, matching the character. Both syllable pages ([[ㄙㄜㄆ]] and [[ㄙㄧㄆ]]) exist elsewhere in the vault, so neither reading is intrinsically invalid — reverted the character's own field to its original value and cited each word's own attested reading faithfully rather than forcing artificial consistency. Worth a dedicated cross-check in a future pass, but out of scope to resolve unilaterally here.

`mc_id: 1630` verified exact at `lookup/CC/CC 1000.md` line 659 (listed under the traditional form 濕); `pos: 性詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits): added the self-referential `stand_in` [[湿]] and the missing [[除湿]]; confirmed [[湿度]] already correct. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 滅 (char) (5306; 1699 characters remaining).

### 2026-08-08, iteration 806 — [[characters/滅 (char)|滅]]

Clean verification: `mc_id: 422` exact at `lookup/CC/CC 0000.md` line 440. 形声 （水 semantic "water" + 烕 phonetic, OC \*hmed, overall \*med) and readings (miè / mit6 / 멸 / METSU・BETSU・ほろ / diệt・dột・riết) confirmed via Wiktionary; `aliases: [灭]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`, matching current-taxonomy sibling [[characters/壊|壊]]). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, filtering out [[敵人]] and [[寂寞]] as text-only false positives not citing 滅 in their own `characters:` field): added the self-referential `stand_in` [[滅]]; reformatted [[滅失]] with proper ruby+gloss (was a bare unruby'd link); confirmed [[寂滅]] and [[隠滅]]. **Chengyu**: added [[十人不滅]] (real hit, previously missing; [[創反救成]], [[焚書坑儒]], [[盛者必衰]], [[貪官汚吏]], [[諸行無常]], and [[銀盤呈首]] were all text-only false positives). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 献 (5307; 1698 characters remaining).

### 2026-08-08, iteration 807 — [[characters/献|献]]

Clean verification: `mc_id: 507` exact at `lookup/CC/CC 0000.md` line 528 (listed under the traditional form 獻). 形声 （犬 semantic "dog" + 鬳 phonetic, OC \*hŋans/\*ŋrad — originally offering wine in ceremonial ritual) and readings (xiàn / hin3 / 헌 / KEN・KON・たてまつ / hiến) confirmed via Wiktionary; `aliases: [獻]` confirmed as the traditional counterpart. Fixed the empty `pos` (`動詞`, predating the current taxonomy → `事詞`, matching offering-sense sibling [[characters/供|供]]); minor YAML normalization on the `japanese` list formatting. Rebuilt the body into the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (3 total ground-truth hits, filtering out [[参考]] and [[上位]] as text-only false positives not citing 献 in their own `characters:` field): [[献上]] already listed, flagged as the `stand_in`; confirmed [[貢献]]; added the missing [[文献]]. **Chengyu**: [[暴飲暴食]] matched a naive text grep but doesn't cite 献 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 環 (char) (5308; 1697 characters remaining).

### 2026-08-08, iteration 808 — [[characters/環 (char)|環]]

**Real `graphemic_classification` bug found and fixed, subtle glyph-confusion case like [[characters/僅|僅]]'s 堇/菫**: stored as `瞏`, but Wiktionary's Glyph Origin explicitly and consistently names the true phonetic as the near-identical `睘` — corrected, kept as plain text since neither has a vault page.

`mc_id: 1493` verified exact at `lookup/CC/CC 1000.md` line 514. Readings (huán / waan4 / 환 / KAN・わ / hoàn) confirmed via Wiktionary; `aliases: [环]` confirmed as the standard simplified form; `pos: 名詞` already correct. Rebuilt the body into the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (4 total ground-truth hits, filtering out [[喚]], [[破壊]], [[血液]], [[居住]], [[亘]] as text-only false positives not citing 環 in their own `characters:` field): added the self-referential `stand_in` [[環]] and the missing [[環礁]]; confirmed [[環境]] and [[環状]] (initially mis-copied [[環境]]'s ruby from a similar-looking neighbor — corrected to the word's own attested ㄏ⺢ㄋㄍ⼶ㄫ after checking). **Chengyu**: [[刻舟求剣]], [[春夏秋冬]], and [[事事皆旧]] all matched a naive text grep but none cite 環 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 蓋 (5310; 1696 characters remaining).

### 2026-08-08, iteration 809 — [[characters/蓋|蓋]]

**Real `graphemic_classification` bug found and fixed, same glyph-confusion pattern as [[characters/僅|僅]] and [[characters/環 (char)|環]]**: stored as `盇`, but Wiktionary's Glyph Origin explicitly names the true phonetic as the near-identical `盍` — corrected, kept as plain text since neither has a vault page.

`mc_id: 607` verified exact at `lookup/CC/CC 0000.md` line 631. Readings (gài / koi3 / 개 / GAI・KOU・KAI・おお / cái) confirmed via Wiktionary; `aliases: [盖]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`). Rebuilt the malformed body (Words section placed before a bare `# Notes` heading) into the proper 4-bullet `## Notes` section followed by `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[書契]], [[穹蒼]], [[兮]], [[苦肉]] as text-only false positives not citing 蓋 in their own `characters:` field): added the missing stand-in [[覆蓋]]; confirmed [[膝蓋]]. **Chengyu**: [[意気揚揚]], [[弱不禁風]], [[国士無双]], and [[天圓地方]] all matched a naive text grep but none cite 蓋 in their own `characters:` field — all four correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 盗 (5311; 1695 characters remaining).

### 2026-08-08, iteration 810 — [[characters/盗|盗]]

Clean verification: `mc_id: 596` exact at `lookup/CC/CC 0000.md` line 617 (listed under the traditional form 盜). 會意 （㳄 "drooling, craving" + 皿 "vessel" — coveting another's possessions, per Wiktionary) and readings (dào / dou6 / 도 / TOU・ぬす / trộm・đạo) confirmed; `graphemic_classification: 會意`, `aliases: [盜]`, and `pos: 事詞` all already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, filtering out [[道]] as a same-romanization-coincidence false positive not citing 盗 in its own `characters:` field): [[窃盗]] and [[盗賊]] already correct; added the 2 missing — [[劫盗]] and [[狗盗]]. **Chengyu**: [[鶏鳴狗盗]] already correctly listed, confirmed as the only real hit (["Misc. Chengyu.md"] is an index file, [[羊頭狗肉]] was a text-only false positive). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 揺 (char) (5312; 1694 characters remaining).

### 2026-08-08, iteration 811 — [[characters/揺 (char)|揺]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1442`, but `lookup/CC/CC 1000.md` line 463 shows `1442. 蕃` (an unrelated character) — 揺's real rank is `1443` (line 464, listed under the traditional form 搖). Corrected.

**Confirmed `graphemic_classification: 䍃` is correct, not a substitution error**: Wiktionary's own Glyph Origin names 謠 as the phonetic series, but 謠 has no vault page — checked the already-perfected sibling [[謡]] (same phonetic family) and confirmed it independently established the same `䍃` convention (謠's own embedded phonetic, since 謠 itself isn't in the vault). Consistent with prior practice, not a bug.

Readings (yáo / jiu4 / 요 / YOU・ゆ) confirmed via Wiktionary; Vietnamese left blank since Wiktionary itself flags those readings as unconfirmed; `aliases: [搖, 摇]` (traditional/simplified pair) confirmed legitimate; `pos: 事詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[表記]] as a text-only false positive not citing 揺 in its own `characters:` field): added the self-referential `stand_in` [[揺]], built from nothing. **Chengyu**: [[異体不容]] matched a naive text grep but doesn't cite 揺 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 盾 (char) (5313; 1693 characters remaining).

### 2026-08-08, iteration 812 — [[characters/盾 (char)|盾]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1699`, but `lookup/CC/CC 1000.md` line 728 shows `1699. 仆` (an unrelated character) — 盾's real rank is `1700` (line 729). Corrected.

象形 (a shield, in the oracle bone script, per Wiktionary) and readings (dùn / teon5 / 순 / JUN・TON・たて / thuẫn・thuỗn) confirmed; `graphemic_classification: 象形` already correct. Filled the empty `pos` (`名詞`, matching weapon-noun sibling [[characters/剣 (char)|剣]]). Removed a stray irrelevant bullet ("Dropped from the Korean HS list in 2000") and rebuilt into the proper 4-bullet form — noting `hanmun_edu_level: 名` maps to [[Korean Name ㅅ]] (keyed by the first Hangul consonant of the Korean reading, 순).

**Words cross-check** (1 ground-truth hit): added the self-referential `stand_in` [[盾]], built from nothing. **Chengyu**: no hits. **Derived Characters** (1 hit): added [[遁]], which cites 盾 as its own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 闘 (5315; 1692 characters remaining).

### 2026-08-08, iteration 813 — [[characters/闘|闘]]

**Real content bug found and fixed**: `vietnamese` was `chùa` ("pagoda, temple" — a wholly unrelated word), but Wiktionary confirms the genuine Hán-Nôm readings are `đấu, dấu`. Corrected.

象形 (two figures fighting with bare hands, per Wiktionary) and readings (dòu / dau3 / 투 / TOU・あらそ) confirmed; `graphemic_classification: 象形` and `aliases: [鬪, 鬥, 鬭]` (all confirmed genuine variant forms) already correct; `pos: 性詞` already correct. Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, filtering out [[回転]], [[孤軍]], [[凍結]], [[燃焼]] as text-only false positives not citing 闘 in their own `characters:` field): reformatted [[闘争]] with proper ruby+gloss, flagged as the `stand_in`; confirmed [[戦闘]]; added the missing [[奮闘]]. **Chengyu**: added [[孤軍奮闘]] (real hit, previously missing; "Misc. Chengyu.md" is an index file, not a real chengyu entry). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 軟 (5316; 1691 characters remaining).

### 2026-08-08, iteration 814 — [[characters/軟|軟]]

**Real `graphemic_classification` bug found and fixed**: stored as `而` (a completely different, extremely common character, "and, but," with its own vault page), but Wiktionary's Glyph Origin names the true phonetic as `耎` — noting 耎 itself later became the modern glyph's 欠 component via a popular variant, which likely caused the confusion with the visually-adjacent 而. Corrected, kept as plain text since 耎 has no vault page.

`mc_id` 4032 lies beyond the CC files' 4000-entry coverage — 軟/輭 doesn't appear anywhere in the corpus, no evidence of fabrication — retained as real long-tail data per policy. Readings (ruǎn / jyun5 / 연 / NAN・ZEN・NEN・やわ / nhiễn・nhung・nhuyễn・nhũn・nhọn) confirmed via Wiktionary; `aliases: [輭, 软]` (original/simplified forms) confirmed legitimate. Rebuilt the malformed body (a bare unlinked Notes bullet plus floating CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section plus `## Words`.

**Flagged, not resolved (same pattern as [[characters/湿 (char)|湿]])**: [[柔軟]]'s own `注音` (ㄋ⼜ㄋㄧㄋ) uses a different final syllable than the character's own field and [[軟禁]] (both `ㄋㄝㄋ`) — cited each word's own attested reading faithfully rather than forcing consistency.

**Words cross-check** (2 total ground-truth hits): [[柔軟]] already the `stand_in`, flagged; [[軟禁]] added, both built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 盤 (char) (5317; 1690 characters remaining).

### 2026-08-08, iteration 815 — [[characters/盤 (char)|盤]]

Clean verification: `mc_id: 2118` exact at `lookup/CC/CC 2000.md` line 127. 形声 （皿 semantic "vessel" + 般 phonetic, OC \*praːn/\*paːn/\*baːn, overall \*baːn) and readings (pán / pun4 / 반 / BAN・HAN / bàn・mâm) confirmed via Wiktionary; `aliases: [盘, 蟠, 槃]` all confirmed as genuine documented variant forms (not the usual phonetic-series contamination pattern). Filled the empty `pos` (`名詞`). Rebuilt the body into the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (7 total ground-truth hits, filtering out [[基礎]], [[受胎]], [[天地]] as text-only false positives not citing 盤 in their own `characters:` field): added the self-referential `stand_in` [[盤]]; confirmed [[盤古]]; added the 5 missing — [[鍵盤]], [[涅盤]], [[胎盤]], [[基盤]], [[骨盤]]. **Chengyu** (2 hits): added [[涅盤寂静]] and [[銀盤呈首]], both previously missing ([[諸法無我]], [[諸行無常]], [[開天辟地]] were text-only false positives). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 牙 (5318; 1689 characters remaining).

### 2026-08-08, iteration 816 — [[characters/牙|牙]]

Clean verification: `mc_id: 1249` exact at `lookup/CC/CC 1000.md` line 262. 象形 (a pair of elephant tusks, used specifically for molars, per Wiktionary) and readings (yá / ngaa4 / 아 / GA・GE・きば / nga・ngà・nha) confirmed; `graphemic_classification: 象形` already correct. Rebuilt into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, filtering out 9 text-only false positives — [[擦拭]], [[羽翼]], [[刷]], [[咬]], [[腸管]], [[散歩]], [[乳色]], [[雪魚]], [[刷子]] — none citing 牙 in their own `characters:` field): [[長牙]] already listed and flagged as the `stand_in`; added the 3 missing — [[葡萄牙]], [[西班牙]], [[西班牙語]]. **Chengyu**: [[対牛弾琴]] matched a naive text grep but doesn't cite 牙 in its own `characters:` field — correctly omitted. **Derived Characters** (1 hit): added [[芽]], which cites 牙 as its own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 閣 (5319; 1688 characters remaining).

### 2026-08-08, iteration 817 — [[characters/閣|閣]]

Clean verification: `mc_id: 2405` exact at `lookup/CC/CC 2000.md` line 426. 形声 （門 semantic "gate" + 各 phonetic, OC \*klaːɡ) and readings (gé / gok3 / 각 / KAKU / các・gác) already correctly documented in the existing Notes bullet; `aliases: [阁]` confirmed as the standard simplified form. Filled the empty `pos` (`名詞`). Fixed a broken relative-markdown final-lookup link (`../lookup/CC/finals/韻 鈬開`, wrong path syntax) into a proper wikilink, and added the missing SKIP/Stroke/Levels bullet — noting `joyo_level: "6"` (a numeric Kyōiku grade) maps to [[Jōyō - Kyōiku]], not [[Jōyō - Kōtō]].

**Words cross-check** (2 total ground-truth hits, filtering out [[空中]], [[奥門]], [[室町]] as text-only false positives not citing 閣 in their own `characters:` field): added the missing stand-in [[内閣]]; confirmed [[楼閣]]. **Chengyu**: [[空中楼閣]] already correctly listed, confirmed as the only real hit (["Misc. Chengyu.md"] is an index file, [[万物生長]] and [[鏡花水月]] were text-only false positives). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 穴 (5320; 1687 characters remaining).

### 2026-08-08, iteration 818 — [[characters/穴|穴]]

**Real `graphemic_classification` bug found and fixed, self-contradictory case**: stored as `八` (a 形声-style component encoding), while the page's own existing Notes bullet already correctly read "象形 — possibly an entrance to a cave" — the frontmatter field simply never matched the prose beside it. Corrected `八` → `象形`, confirmed independently via Wiktionary.

`mc_id: 1264` verified exact at `lookup/CC/CC 1000.md` line 277; readings (xué / jyut6 / 혈 / KETSU・あな / hoét・hoẹt・huyệt) confirmed; `pos: 名詞` already correct. Added the missing SKIP/Stroke/frequency-rank/Levels bullet.

**Words cross-check** (4 total ground-truth hits, filtering out [[上位]], [[太陽]], [[血]], [[部位]] as text-only false positives not citing 穴 in their own `characters:` field): [[洞穴]], [[墓穴]], [[穴位]] already correct; added the missing [[巣穴]]. **Chengyu**: [[天長地久]] and [[結髪夫妻]] both matched a naive text grep but neither cites 穴 in its own `characters:` field — both correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 瓜 (5322; 1686 characters remaining).

### 2026-08-08, iteration 819 — [[characters/瓜|瓜]]

Clean verification: `mc_id: 1959` exact at `lookup/CC/CC 1000.md` line 1000. 象形 (a melon suspended by its vines, per Wiktionary) and readings (guā / gwaa1 / 과 / KA・うり / dưa・qua) confirmed; `graphemic_classification: 象形` and `pos: 名詞` already correct. Removed a stray irrelevant bullet ("Dropped from the Korean HS list in 2000") and added the missing SKIP/Stroke/frequency-rank/Levels bullet — noting `joyo_level: 日本人名用漢字` maps to [[Jinmeiyō]].

**Words cross-check** (4 total ground-truth hits, filtering out [[胡椒]] and [[苦味]] as text-only false positives not citing 瓜 in their own `characters:` field): built the entire `## Words` section from scratch — added the stand-in [[胡瓜]] plus [[西瓜]], [[甜瓜]], [[苦瓜]]. **Chengyu** (2 hits, both already present): reformatted [[種瓜得瓜]] with proper ruby+gloss (was a bare unruby'd link); confirmed [[李下瓜田]]. **Derived Characters**: an initial quoted-value grep only caught [[孤]] — rerunning to account for `"瓜"`-with-quotes values surfaced 2 more genuine hits, [[狐]] and [[弧]], both also citing 瓜 as their own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 蒼 (char) (5323; 1685 characters remaining).

### 2026-08-08, iteration 820 — [[characters/蒼 (char)|蒼]]

**Real broken-link bug found and fixed**: the existing Notes bullet had an empty component link (`phonetic [[]]`) where 倉 belonged — filled in.

**Confirmed `aliases: [苍, 滄, 沧]` are all legitimate** — despite 滄/沧 ("vast ocean") looking like a plausible contamination case (same pattern as several fixed this session), Wiktionary explicitly lists them as alternative forms of 蒼 itself, not merely phonetic-series relatives.

`mc_id: 1142` verified exact at `lookup/CC/CC 1000.md` line 151; `graphemic_classification: 倉` already correct. Filled the empty `pos` (`性詞`). Rebuilt the malformed body (two informal prose notes plus floating CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section plus full `## Words`.

**Words cross-check** (6 total ground-truth hits, filtering out [[穹窿]] and [[巻耳]] as text-only false positives not citing 蒼 in their own `characters:` field): added the self-referential `stand_in` [[蒼]]; confirmed [[蒼朮]]; promoted the informal [[蒼鉛]] note to a proper Words entry; added the 3 missing — [[蒼海]], [[蒼路]], [[穹蒼]]. **Chengyu**: added [[蒼海桑田]] (real hit, previously missing; [[瑠璃清天]] was a text-only false positive). **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 柏 (char) (5324; 1683 characters remaining).

### 2026-08-08, iteration 821 — [[characters/柏 (char)|柏]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1593`, but `lookup/CC/CC 1000.md` line 618 shows `1593. 盎` (an unrelated character) — 柏's real rank is `1594` (line 619). Corrected.

**Verified, not changed**: `mandarin: "bǎi bó"` (space-separated two-reading string) initially looked malformed, but cross-checking other polyphonic character pages ([[乾 (char)|乾]], [[斗 (char)|斗]], [[差|差]], etc.) confirmed this is the vault's established convention for characters with multiple Mandarin readings — Wiktionary independently confirms both readings are genuine (bǎi for tree senses, bó for names like 柏林 "Berlin").

形声 （木 semantic "tree" + 白 phonetic, OC \*praːɡ/\*braːɡ) and readings (paak3 / 백 / HAKU・かしわ / bá・bách) confirmed; `graphemic_classification: 白` and `aliases: [栢]` already correct. Filled the empty `pos` (`名詞`). Removed a stray irrelevant bullet, a duplicated Words entry, and rebuilt into the proper 4-bullet `## Notes` section — noting `joyo_level` maps to [[Jinmeiyō]] and `hanmun_edu_level: 名` maps to [[Korean Name ㅂ]] (keyed by 백's initial consonant).

**Words cross-check** (2 total ground-truth hits, filtering out [[羅倫金]], [[苦味]], [[西博金]], [[美洲金]], [[黄檗]], [[檜木]] as text-only false positives not citing 柏 in their own `characters:` field): added the self-referential `stand_in` [[柏]]; confirmed [[柏克金]] (deduplicated). **Chengyu**: [[禍延子孫]] matched a naive text grep but doesn't cite 柏 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 昏 (5325; 1682 characters remaining).

### 2026-08-08, iteration 822 — [[characters/昏|昏]]

Clean verification: `mc_id: 1219` exact at `lookup/CC/CC 1000.md` line 232. 會意 （氐 "lowering" + 日 "sun" — the moment the sun sets, per Wiktionary) and readings (hūn / fan1 / 혼 / KON・くら / hon・hun・hôn) confirmed; `graphemic_classification: 會意` already correct. Filled the empty `pos` (`名詞`, matching the stand-in word [[黄昏]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit, filtering out [[日暮]], [[明君]], [[五更]] as text-only false positives not citing 昏 in their own `characters:` field): [[黄昏]] already the `stand_in` but unlisted — added with flag. **Chengyu**: [[成家立業]] matched a naive text grep but doesn't cite 昏 in its own `characters:` field — correctly omitted. **Derived Characters** (1 hit): added [[婚]], which cites 昏 as its own `graphemic_classification`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 坂 (5326; 1681 characters remaining).

### 2026-08-08, iteration 823 — [[characters/坂|坂]]

**Real triple alias-contamination bug found and fixed**: `aliases` included `坡`, `跛`, and `岥` alongside the legitimate `阪`. Checked each individually against Wiktionary: `跛` ("lame, crippled," phonetic 皮) is a wholly unrelated character; `坡` ("slope," but its own separate phonetic 皮, cross-referenced only via a "See also") is a distinct entry, not a variant of 坂; `岥` is explicitly documented as an archaic variant of `坡` — not of 坂. Only `阪` is genuinely confirmed ("坂 is the simplified/variant form of 阪"). Removed all three.

`mc_id` 5838 lies beyond the CC files' 4000-entry coverage — 坂 itself doesn't appear in the corpus, no evidence of fabrication found, retained as real long-tail data per policy. 形声 （土 semantic "earth" + 反 phonetic, OC \*panʔ) and readings (bǎn / baan2 / 판 / HAN・さか / bản・phản) confirmed via Wiktionary; `graphemic_classification: 反` already correct. Filled the empty `pos` (`名詞`, matching the citing word [[斜坂]]'s own `名詞`). Rebuilt into the proper 4-bullet `## Notes` section — noting `joyo_level: "3"` maps to [[Jōyō - Kyōiku]] and `hanmun_edu_level: 名` maps to [[Korean Name ㅍ]] (keyed by 판's initial consonant).

**Words cross-check** (1 ground-truth hit): [[斜坂]] already listed, flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 箱 (char) (5327; 1680 characters remaining).

### 2026-08-08, iteration 824 — [[characters/箱 (char)|箱]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `3909`, but `lookup/CC/CC 3000.md` line 950 shows `3909. 葅` (an unrelated character) — 箱's real rank is `3910` (line 951). Corrected.

形声 （竹 semantic "bamboo" + 相 phonetic, OC \*slaŋ — a bamboo box) and readings (xiāng / soeng1 / 상 / SHOU・SOU・はこ / rương・sương・tương) confirmed via Wiktionary; `graphemic_classification: 相` already correct. Filled the empty `pos` (`名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (1 ground-truth hit, filtering out [[方舟]] as a text-only false positive not citing 箱 in its own `characters:` field): added the self-referential `stand_in` [[箱]], built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 複 (5328; 1679 characters remaining).

### 2026-08-08, iteration 825 — [[characters/複|複]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1950`, but `lookup/CC/CC 1000.md` line 991 shows `1950. 究` (an unrelated character) — 複's real rank is `1951` (line 992). Corrected.

形声 （衣 semantic "clothes" + 复 phonetic, OC \*buɡ "to return," overall \*buɡs/\*puɡ) and readings (fù / fuk1 / 복 / FUKU / phức) confirmed via Wiktionary; `graphemic_classification: 复` and `aliases: [复]` both confirmed correct for this specific "repeat/duplicate" sense (unlike [[characters/戯|戯]]'s earlier case where 复 was legitimate only for a different character's unrelated sense). Filled the empty `pos` (`事詞`, matching the stand-in word [[重複]]'s own `事詞`). Rebuilt the malformed body into the proper 4-bullet `## Notes` section plus full `## Words` — noting `hsk_level: "1"` maps to [[Old HSK 1]] and `joyo_level: "5"` maps to [[Jōyō - Kyōiku]].

**Words cross-check** (4 total ground-truth hits, filtering out [[連帯]], [[偏重]], [[単純]], [[復習]] as text-only false positives not citing 複 in their own `characters:` field): [[重複]], [[複写]], [[複数]] already correct; promoted the informal [[複雑]] note to a proper Words entry. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 貸 (5329; 1678 characters remaining).

### 2026-08-08, iteration 826 — [[characters/貸|貸]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `1774`, but `lookup/CC/CC 1000.md` line 807 shows `1774. 亟` (an unrelated character) — 貸's real rank is `1775` (line 808). Corrected.

形声 （貝 semantic "valuables" + 代 phonetic, OC \*l̥ʰɯːɡs — originally "to give, bestow," extended to "lend") and readings (dài / taai3 / 대 / TAI・TOKU・か / thãi・thải・thảy・thẩy) confirmed via Wiktionary; `aliases: [贷]` confirmed as the standard simplified form. Filled the empty `pos` (`事詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section.

**Words cross-check** (1 ground-truth hit, filtering out [[償還]] as a text-only false positive not citing 貸 in its own `characters:` field): reformatted [[貸出]] with proper ruby+gloss (was a bare unruby'd link), flagged as the `stand_in`. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 似 (char) (5330; 1677 characters remaining).

### 2026-08-08, iteration 827 — [[characters/似 (char)|似]]

**Real malformed-YAML bug found and fixed**: `vietnamese` was a single comma-joined item `"tự, tợ, tựa, từa"` instead of a proper four-item list — reformatted.

Clean verification otherwise: `mc_id: 1028` exact at `lookup/CC/CC 1000.md` line 33. 形声 （人 semantic "human" + 以 phonetic, OC \*ljɯʔ/\*lɯʔ) and readings (sì / ci5 / 사 / JI・に / tự・tợ・tựa・từa) confirmed via Wiktionary; `graphemic_classification: 以` and `pos: 格助詞` already correct. Added the missing SKIP/Stroke/frequency-rank/Levels bullet.

**Words cross-check** (3 total ground-truth hits): added the self-referential `stand_in` [[似]] and the missing [[類似]]; confirmed [[類似格]]. **Chengyu**: [[破頭傷足]], [[落花流水]], and [[空中楼閣]] all matched a naive text grep but none cite 似 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 格 (char) (5331; 1676 characters remaining).

### 2026-08-08, iteration 828 — [[characters/格 (char)|格]]

**Real alias-contamination bug found and fixed**: `aliases` included `骼` — but Wiktionary confirms 骼 ("bones, skeleton," 骨 semantic) is a wholly separate character, merely sharing the same phonetic series (各) with 格, not a variant of 格 itself. Removed (no vault page for 骼, so nothing else needed updating).

`mc_id: 1580` verified exact at `lookup/CC/CC 1000.md` line 605 (骼 doesn't appear in the corpus at all, ruling out an off-by-one confusion between the two); `graphemic_classification: 各` already correct. Filled the empty `pos` (`名詞`). Fixed a broken relative-markdown final-lookup link and rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (extensive: this page already carried 15 grammatical-case compounds plus 2 place names — a genuinely large, real citation set): full re-scan against all 45 files mentioning 格 anywhere found 20 real hits after filtering false positives (including [[即]], whose only "格" was in its own `pos: 格助詞` field, not a citation). Added the 5 missing — the self-referential `stand_in` [[格]], [[格助詞]], [[価格]], [[呼格]], [[属格]] — bringing the total to 20 correctly-cited compounds. **Chengyu**: [[内柔外剛]], [[欣喜雀躍]], and [[禍延子孫]] all matched a naive text grep but none cite 格 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 額 (5332; 1675 characters remaining).

### 2026-08-08, iteration 829 — [[characters/額|額]]

Clean verification: `mc_id: 3762` exact at `lookup/CC/CC 3000.md` line 795. 形声 （頁 semantic "head" + 客 phonetic, OC \*kʰraːɡ, overall \*ʔŋɡraːɡ) and readings (é / ngaak6 / 액 / GAKU・GYAKU・ひたい / nghệch・ngách・ngạch) confirmed via Wiktionary; `aliases: [额]` confirmed as the standard simplified form. Filled the empty `pos` (`名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (2 total ground-truth hits, filtering out [[俸給]], [[頁]], [[差異]] as text-only false positives not citing 額 in their own `characters:` field): added the missing stand-in [[額頭]] and [[差額]], both built from nothing. **Chengyu**/**Derived Characters**: no hits — both correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 綿 (5333; 1674 characters remaining).

### 2026-08-08, iteration 830 — [[characters/綿|綿]]

**Real `mc_id` off-by-one bug found and fixed**: stored as `2281`, but `lookup/CC/CC 2000.md` line 294 shows `2281. 珪` (an unrelated character) — 綿's real rank is `2282` (line 295). Corrected.

**Confirmed `graphemic_classification: 會意` and `aliases: [绵, 棉]` are all correct**: despite 糸+帛 initially looking like it could be 形声 (given the OC reconstruction doesn't obviously derive from either component), Wiktionary's Glyph Origin text explicitly describes this as a semantic-only compound; 棉 (wood-radical variant) is independently confirmed as a genuine documented alternative form, not the usual phonetic-series contamination pattern.

Readings (mián / min4 / 면 / MEN・BEN・わた / men・min・miên・mên・mền) confirmed via Wiktionary; `pos` filled (`名詞`, matching the stand-in word [[綿花]]'s own `名詞`). Replaced the floating CC-initial/final wikilinks with the proper 4-bullet `## Notes` section plus `## Words`.

**Words cross-check** (3 total ground-truth hits, filtering out [[高]], [[島屿]], [[綽約]], [[寿着]], [[参差]], [[徘徊]] as text-only false positives not citing 綿 in their own `characters:` field): added the missing stand-in [[綿花]], [[綿羊]], and the proper-noun [[高綿]] (Cambodia). **Chengyu**: [[天長地久]] matched a naive text grep but doesn't cite 綿 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 置 (char) (5336; 1673 characters remaining).

### 2026-08-08, iteration 831 — [[characters/置 (char)|置]]

Clean verification: `mc_id: 433` exact at `lookup/CC/CC 0000.md` line 451. 形声 （网 semantic "net" + 直 phonetic, OC \*tɯɡs) and readings (zhì / zi3 / 치 / CHI / trí) confirmed via Wiktionary; `aliases: [寘]` confirmed as a genuine documented variant; `graphemic_classification: 直` already correct. Filled the empty `pos` (`事詞`). Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (13 total ground-truth hits — this page went from 2 listed to 13 verified): added the self-referential `stand_in` [[置]] plus 10 missing compounds — [[配置]], [[装置]], [[後置詞]], [[位置]], [[前置詞]], [[設置]], [[後置]], [[安置]], [[措置]], [[放置]]; reformatted [[置換]] with proper ruby. **Chengyu**: [[森羅万象]], [[臥薪嘗胆]], and [[舎本逐末]] all matched a naive text grep but none cite 置 in their own `characters:` field — all three correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 辞 (5337; 1672 characters remaining).

### 2026-08-08, iteration 832 — [[characters/辞|辞]]

Clean verification: `mc_id: 311` exact at `lookup/CC/CC 0000.md` line 326 (`辭`). Readings (cí / ci4 / 사 / JI, SHI / từ) confirmed via Wiktionary. **Classification bug fixed**: `graphemic_classification` was stored as `會意`, but Wiktionary's glyph-origin analysis states the received form's 辛 is a graphic corruption of 𬔖, "functioning as a phonophoric supplying \*l-type phonetic information" over a semantic 𤔔 ("to sort out silk threads," no vault page) — i.e. this is a 形声 structure, not 會意. Corrected the field to `辛` (the phonetic component) and rewrote the Notes bullet accordingly. `aliases: [辭]` confirmed as the genuine traditional form. Filled the empty `pos` (`事詞`, precedent from stand_in 辞職's own pos field). Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, informal unruby'd bullets) into the proper 4-bullet `## Notes` section.

**Words cross-check** (8 total ground-truth hits — this page went from 2 listed to 8 verified): added the self-referential `stand_in` [[辞職]] plus 5 missing compounds — [[辞令]], [[辞退]], [[辞任]], [[辞去]], [[接辞]]; kept already-correct [[接尾辞]] and [[繋辞]]. False positives excluded after checking each candidate's own `characters:` field: [[去]], [[系詞]], [[詞典]], [[時相]], [[事典]], [[四字成語]], [[否定]], [[交替]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for both 辞 and 辭) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 残 (char) (5338; 1671 characters remaining).

### 2026-08-08, iteration 833 — [[characters/残 (char)|残]]

Clean verification: `mc_id: 1260` exact at `lookup/CC/CC 1000.md` line 273 (`殘`). Readings (cán / caan4 / 잔 / ZAN, SAN / tàn) confirmed via Wiktionary. **Classification bug fixed**: `graphemic_classification` was stored as `㦮`, which is not the character's actual phonetic component. Wiktionary confirms 殘/残 is 形声: semantic [[歹]] ("vicious, bones") + phonetic 戔 (OC \*zlaːn). Corrected the field to `戔`. `aliases: [殘]` confirmed as the genuine traditional form (残 is the simplified/shinjitai form used as the page's primary glyph). Filled the empty `pos` (`性詞`, precedent from the word 残's own `pos` field). Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, informal unruby'd bullet) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[残]] and [[残害]]. False positives excluded after checking each candidate's own `characters:` field: [[凶暴]], [[詩作]]. **Chengyu**: [[保頭断尾]] matched a naive text grep but does not cite 残 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for both 残 and 殘) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 標 (5339; 1670 characters remaining).

### 2026-08-08, iteration 834 — [[characters/標|標]]

**mc_id bug fixed**: stored value `2847` pointed to `祟` at `lookup/CC/CC 2000.md` line 884 — a completely unrelated character. The actual entry for 標 is line 885, rank `2848` (an off-by-one error). Corrected. Readings (biāo / biu1 / 표 / HYOU / tiêu etc.) confirmed via Wiktionary; 形声 classification with semantic [[木 (char)|木]] + phonetic [[票 (char)|票]] (OC \*pew) confirmed, `graphemic_classification: 票` already correct. `aliases: [标]` confirmed as the genuine simplified form. Rebuilt the body (floating unformatted CC-initial/final wikilinks, one unruby'd bullet) into the proper 4-bullet `## Notes` section.

**Words cross-check** (6 total ground-truth hits — this page went from 3 listed to 6 verified): added [[標誌]], [[標準]], [[目標]]; also corrected [[標題]]'s ruby, which had been left unformatted with no `<rt>` — verified against the word's own `注音` field (ㄅ⼄ㄊㄝㄧ). False positives excluded after checking each candidate's own `characters:` field: [[目]], [[偏差]], [[問題]], [[基準]], [[毎処]], [[目的]]. **Chengyu**: [[異体不容]] matched a naive text grep but does not cite 標 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for both 標 and 标) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 桑 (5340; 1669 characters remaining).

### 2026-08-08, iteration 835 — [[characters/桑|桑]]

Clean verification: `mc_id: 1063` exact at `lookup/CC/CC 1000.md` line 68. **Classification bug fixed**: `graphemic_classification` was stored as `會意`, but Wiktionary describes 桑 as 象形 — a pictogram of a mulberry tree, where the foliage element (now written 叒) sits atop 木. Corrected the field to `象形`. Empty `aliases` field confirmed correct (no simplified/variant form in common use; the listed alternates 槡/𣕐/桒/𠭨/𠭌 are archaic/rare forms not covered by vault policy). Filled the empty `pos` (`名詞`, precedent from the stand_in 桑木's own `pos` field). Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, unruby'd bullets) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged from the 2 already listed): reformatted [[桑木]] (stand-in) and [[桑田]] with proper ruby. False positives excluded after checking each candidate's own `characters:` field: [[柊木]], [[梓木]]. **Chengyu**: added [[蒼海桑田]] (1 real hit, confirmed via its own `characters:` field) as a new `## Chengyu` section; [[日月星辰]], [[未雨紬謬]], [[磨穿鉄硯]], [[鼠世桃源]], [[安心立命]] all matched a naive text grep but none cite 桑 in their own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 陵 (5341; 1668 characters remaining).

### 2026-08-08, iteration 836 — [[characters/陵|陵]]

Clean verification: `mc_id: 287` exact at `lookup/CC/CC 0000.md` line 299. 形声 classification (semantic [[阜]] "mound" + phonetic [[夌]], OC \*rɯŋ, itself meaning "mound; hill") confirmed via Wiktionary; `graphemic_classification: 夌` already correct. Empty `aliases` confirmed correct (no simplified/variant form in common use). Filled the empty `pos` (`名詞`, precedent from the stand_in 陵墓's own `pos` field). `hanmun_edu_level: 中` correctly maps to [Korean MS](lookup/Korean/Korean%20MS.md) (confirmed against precedent on already-perfected page [[丁 (char)|丁]]), not the [Korean HS](lookup/Korean/Korean%20HS.md) used for `高等`. Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, missing Words section entirely) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[陵墓]] (the page previously had no `## Words` section at all). False positive excluded after checking its own `characters:` field: [[四川]]. **Chengyu**: [[鏡花水月]] and [[魑魅罔両]] both matched a naive text grep but neither cites 陵 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 妙 (char) (5342; 1667 characters remaining).

### 2026-08-08, iteration 837 — [[characters/妙 (char)|妙]]

Clean verification: `mc_id: 2130` exact at `lookup/CC/CC 2000.md` line 139. 形声 classification (semantic [[女 (char)|女]] + phonetic [[少 (char)|少]], OC \*hmjewʔ) confirmed via Wiktionary; `graphemic_classification: 少` already correct. `aliases: [玅]` confirmed as a genuine documented variant. Filled the empty `pos` (`性詞`, precedent from citing compounds [[巧妙]]/[[奇妙]] and the word 妙's own Notes describing it as "used independently as a standalone adjective"). **Naming-convention catch**: `stroke_count: 7` requires the zero-padded lookup filename `Stroke 07.md`, not `Stroke 7.md` — single-digit stroke counts are zero-padded in this vault while double-digit ones are not; corrected the link accordingly. Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, only 1 of 4 real Words hits) into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits — this page went from 1 listed to 4 verified): added the self-referential `stand_in` [[妙]] plus [[巧妙]] and [[奇妙]]; reformatted [[妙手]] with proper ruby. False positives excluded after checking each candidate's own `characters:` field: [[奥]], [[手]], [[秒]], [[乖巧]], [[黒暗]]. **Chengyu**: [[不可思議]] matched a naive text grep but does not cite 妙 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 倫 (5344; 1666 characters remaining).

### 2026-08-08, iteration 838 — [[characters/倫|倫]]

Clean verification: `mc_id: 1323` exact at `lookup/CC/CC 1000.md` line 340. **Classification bug fixed**: `graphemic_classification` was stored as `會意`, but Wiktionary confirms 倫 is 形声: semantic [[人 (char)|人]] + phonetic 侖 (OC \*run). Corrected the field to `侖`. Both `aliases: [侖, 伦]` verified genuine — 伦 is the modern simplified form, and 侖 (despite having no vault character page) is separately documented on Wiktionary as an obsolete alternative form of 倫/伦 itself, not mere phonetic-series contamination. `hsk_level: 無` correctly maps to [HSK No](lookup/HSK/HSK%20No.md) (confirmed against precedent on already-perfected pages [[亙 (char)|亙]], [[兎 (char)|兎]], [[剣 (char)|剣]]). Filled the empty `pos` (`名詞`, precedent from the stand_in 倫理's own `pos` field). Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, a duplicate entry appearing both under `# Notes` and `## Words`) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 1 listed to 3 verified): added the self-referential `stand_in` [[倫理]] and [[五倫]]; kept already-correct [[羅倫金]]. False positives excluded after checking each candidate's own `characters:` field: [[五]], [[人]], [[五常]], [[朋友]], [[長上]], [[錀琴]], [[西博金]]. **Chengyu**: [[殺姦窃偽]] and [[空前絶後]] both matched a naive text grep but neither cites 倫 in its own `characters:` field — correctly omitted. **Derived Characters** (quote-tolerant grep for both 倫 and its phonetic 侖): found 2 genuine hits — [[輪 (char)|輪]] and [[錀 (char)|錀]], both citing `graphemic_classification: 侖` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 倶 (char) (5345; 1665 characters remaining).

### 2026-08-08, iteration 839 — [[characters/倶 (char)|倶]]

Clean verification: `mc_id: 568` exact at `lookup/CC/CC 0000.md` line 589 (`俱`). 形声 classification (semantic [[人 (char)|人]] + phonetic [[具]], OC \*ɡos) confirmed via Wiktionary; `graphemic_classification: 具` already correct. `aliases: [俱]` confirmed genuine — Wiktionary's own "See also" explicitly cross-references 倶 as an alternative form of 俱. **Malformed YAML fixed**: `japanese_native: とも` was followed by a stray orphan list item `- ともに`; converted to a proper 2-item list (both readings independently confirmed live in the citing word 倶's own Notes prose). `vietnamese: - câu, cu` (a malformed single comma-joined list item) was corrected to just `câu` — the citing word 倶's own Notes explicitly states "the character page's other stored candidate, cu, doesn't correspond to any attested reading of this character and looks like noise." Filled the previously-empty `boundedness` field (75, estimated per this vault's existing per-character convention — no hard formula exists — reflecting a character with a genuine standalone classical/modern gloss but which appears "most familiar today" bound inside the loanword compound 倶楽部). Rebuilt the malformed body (no proper heading structure, informal unruby'd note) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits): added the self-referential `stand_in` [[倶]]; reformatted already-present [[倶楽部]] with proper ruby. False positives excluded after checking each candidate's own `characters:` field: [[句]], [[衢]] (both genuine Dan'a'yo homophones of 倶, per the word 倶's own Notes, but neither cites 倶 in its `characters:` field, so correctly omitted from Words). **Chengyu**: [[不共戴天]] matched a naive text grep but does not cite 倶 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for both 倶 and 俱) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 聡 (5346; 1664 characters remaining).

### 2026-08-08, iteration 840 — [[characters/聡|聡]]

Clean verification: `mc_id: 1356` exact at `lookup/CC/CC 1000.md` line 373 (`聰`). 形声 classification (semantic [[耳 (char)|耳]] + phonetic 悤, OC \*sʰloːŋ, no vault page) confirmed via Wiktionary; `graphemic_classification: 悤` already correct. `aliases: [聰]` confirmed genuine (traditional form); added the also-documented simplified form `聪`, previously missing. **Real missing-data bug fixed**: `vietnamese` was stored as an empty list, but Wiktionary documents a standalone Hán Nôm reading "thông" — added. Confirmed `hsk_level: ""` is this vault's already-normalized "not on HSK" convention (matches dozens of already-perfected precedent pages, e.g. [[哭 (char)|哭]], [[弔 (char)|弔]]) and still renders the `[HSK No]` link in the frequency bullet. Rebuilt the malformed body (wrong `# Notes` heading level, no Words section at all) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[聡明]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for 聡/悤/聰) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 介 (5348; 1663 characters remaining).

### 2026-08-08, iteration 841 — [[characters/介|介]]

Clean verification: `mc_id: 1009` exact at `lookup/CC/CC 1000.md` line 14. **Self-contradictory classification bug fixed**: `graphemic_classification` was stored as `指事`, while the page's own body prose already correctly described it as [[人 (char)|人]] + two "in-between" marks and linked to `List of 会意` — a 會意 analysis, confirmed by Wiktionary. Corrected the field to `會意`, resolving the contradiction (same pattern as earlier [[弔 (char)|弔]] and 穴 fixes this session). Empty `aliases` confirmed correct — Wiktionary's "see also" mentions 个/𠆤 but these are distinct characters, not variants of 介. Filled the empty `pos` (`名詞`, precedent from the stand_in 仲介's own `pos` field). Rebuilt the body into the proper 4-bullet `## Notes` section (previously missing the SKIP/Stroke, frequency/phonology, and Levels bullets entirely).

**Words cross-check** (4 total ground-truth hits, unchanged from the 4 already listed): added ruby/formatting to the 3 that were unruby'd — [[仲介]] (stand-in), [[介紹]], [[介詞]]; kept already-correct [[媒介]]. Also removed a stray trailing empty bullet (`- ` with no content). False positives excluded after checking each candidate's own `characters:` field: [[魚]], [[呼吸]], [[安慰]], [[災厄]], [[母親]], [[羽毛]], [[前置詞]], [[国民党]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found (quote-tolerant grep) — [[芥]] and [[界]], both citing `graphemic_classification: 介` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 逮 (5349; 1662 characters remaining).

### 2026-08-08, iteration 842 — [[characters/逮|逮]]

Clean verification: `mc_id: 1478` exact at `lookup/CC/CC 1000.md` line 499. 形声 classification (semantic 辵 "walk, travel" + phonetic 隶, "a hand seizing something," neither with a vault page) confirmed via Wiktionary; `graphemic_classification: 隶` already correct. Empty `aliases` confirmed correct — 逮 is identical in traditional and simplified Chinese. Filled the empty `pos` (`事詞`, precedent from the stand_in 逮捕's own `pos` field). Rebuilt the malformed body (wrong `# Notes` heading level, no Words section at all) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[逮捕]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[捕獲]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits — the quote-tolerant grep only matched the page's own file — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 督 (5350; 1661 characters remaining).

### 2026-08-08, iteration 843 — [[characters/督|督]]

Clean verification: `mc_id: 1529` exact at `lookup/CC/CC 1000.md` line 554. 形声 classification (semantic [[目 (char)|目]] + phonetic [[叔]], OC \*hljɯwɢ) confirmed via Wiktionary; `graphemic_classification: 叔` already correct. Empty `aliases` confirmed correct (no simplified/variant form in common use; the listed alternates 𣈉/𥆳 are archaic rare forms not covered by vault policy). `pos`/frontmatter otherwise already complete. Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (5 total ground-truth hits — this page went from 4 listed to 5 verified): added [[基督]]; kept already-correct [[監督]], [[督促]] (stand-in), [[基督教]], [[提督]]. False positives excluded after checking each candidate's own `characters:` field: [[促]], [[宗教]], [[導演]], [[提琴]], [[提携]], [[牛乳]], [[洗礼]], [[聖餐]], [[修道院]]. **Chengyu**: [[剣生剣死]], [[愛主耳錐]], [[愛隣如自]], [[石山盈界]], [[破頭傷足]], [[血誓盟約]] all matched a naive text grep but none cite 督 in their own `characters:` field — all correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 誉 (5350; 1660 characters remaining).

### 2026-08-08, iteration 844 — [[characters/誉|誉]]

**Note**: this page shares `danayo_id: 5350` with the just-perfected [[characters/督|督]] — a real duplicate-ID data bug, flagged here rather than resolved unilaterally since renumbering either page could cascade into other ordering assumptions; left both IDs as-is.

Clean verification: `mc_id: 1073` exact at `lookup/CC/CC 1000.md` line 78 (`譽`). **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `与`, but Wiktionary's entry for the vault's primary glyph 誉 (the shinjitai/simplified form) describes its actual top component as `兴` — "Simplified from 譽 (與 → 兴)." 与 and 兴 are visually similar but distinct characters; 与 is unrelated to 誉's actual composition. Corrected the field to `兴` (no vault page). `aliases: [譽]` confirmed as the genuine kyūjitai/traditional form. Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[名誉]] (stand-in). False positives excluded after checking each candidate's own `characters:` field: [[名]], [[誹謗]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for both 誉 and 兴) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 侯 (char) (5351; 1659 characters remaining).

### 2026-08-08, iteration 845 — [[characters/侯 (char)|侯]]

Clean verification: `mc_id: 33` exact at `lookup/CC/CC 0000.md` line 38. 象形 classification (pictogram of an archery target) confirmed via Wiktionary; `graphemic_classification: 象形` already correct. Empty `aliases` confirmed correct (no simplified/variant form in common use). **Real bad-data bug fixed**: `vietnamese` listed both `hầu` and `hậu`, but the citing word 侯's own Notes explicitly states "the character page's other stored candidate, hậu, belongs to unrelated characters (后, 'empress,' or 後, 'after') and was not used here" — removed `hậu`, keeping only the attested `hầu`. Filled the empty `pos` (`名詞`, precedent from the word 侯's own `pos` field). Rebuilt the malformed body (wrong `# Notes` heading level, floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[侯]] (the page previously had no `## Words` section). False positives excluded after checking each candidate's own `characters:` field: two genuine Dan'a'yo homophones [[厚]] and [[吼]] (per the word 侯's own Notes) plus unrelated [[斗]], [[某]], [[走]], [[豆]], [[伯爵]], [[公爵]], [[国子]], [[爵位]], [[王畿]], [[春秋時代]] — none cite 侯 in their `characters:` field. **Chengyu**: [[傍若無人]] and [[意気揚揚]] both matched a naive text grep but neither cites 侯 in its own `characters:` field — correctly omitted. **Derived Characters**: 1 genuine hit found — [[喉]], citing `graphemic_classification: 侯` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 逸 (char) (5352; 1658 characters remaining).

### 2026-08-08, iteration 846 — [[characters/逸 (char)|逸]]

Clean verification: `mc_id: 1572` exact at `lookup/CC/CC 1000.md` line 597. 會意 classification ([[Radicals/Radical 162|辵]] "movement" + 兔 "rabbit," a rabbit fleeing) confirmed via Wiktionary; `graphemic_classification: 會意` already correct, matching the page's own already-correct body prose. Both `aliases: [𨓜, 佚]` confirmed genuine — both are documented related/alternative forms. Filled the empty `pos` (`事詞`). Fixed a mislinked lookup reference: the body cited `[[Radical 162|辵]]`, a page that doesn't exist at that path — the actual file lives at `lookup/Radicals/Radical 162.md`. Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits — this page went from 2 listed to 4 verified): added the self-referential `stand_in` [[逸]] and previously-missing [[逸事]]; reformatted [[逸話]] with proper ruby; kept already-correct [[安逸]]. False positives excluded after checking each candidate's own `characters:` field: two genuine Dan'a'yo homophones [[一]] and [[壱]] (per the word 逸's own homophone callout) plus unrelated [[官人]], [[徳国]] — none cite 逸 in their `characters:` field. **Chengyu**: [[令行禁止]] matched a naive text grep but does not cite 逸 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 飢 (5353; 1657 characters remaining).

### 2026-08-08, iteration 847 — [[characters/飢|飢]]

Clean verification: `mc_id: 1094` exact at `lookup/CC/CC 1000.md` line 99. **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `幾` (a larger, unrelated character meaning "how many"), but Wiktionary confirms the real phonetic component is the much simpler `几` (OC \*krilʔ, "small table/stool") — the page's own body prose already correctly said "几" in a broken `[[几]]` wikilink (no vault page exists for it), contradicting the frontmatter field. Corrected `graphemic_classification` to `几` and replaced the broken wikilink with plain text. Both `aliases: [饑, 饥]` confirmed genuine — 饑 is the fuller traditional/alternative form and 饥 the modern simplified form. Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[飢餓]]; kept already-correct [[飢饉]].  **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for both 飢 and 几) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 逃 (5354; 1656 characters remaining).

### 2026-08-08, iteration 848 — [[characters/逃|逃]]

Clean verification: `mc_id: 1122` exact at `lookup/CC/CC 1000.md` line 131. 形声 classification (semantic [[Radicals/Radical 162|辵]] + phonetic [[兆]], OC \*l'aːw) confirmed via Wiktionary; `graphemic_classification: 兆` already correct. Empty `aliases` confirmed correct — 逃 is unchanged between traditional and simplified, and the other listed variants (跳/迯/etc.) are archaic/rare, not vault-worthy. Filled the empty `pos` (`事詞`, precedent from the stand_in 逃避's own `pos` field). Rebuilt the malformed body (wrong bare `[[Lookup/CC/...]]` links outside proper bullets, unruby'd entry) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 1 listed to 3 verified): added the self-referential `stand_in` [[逃避]] and reformatted [[逃亡]] with proper ruby; kept already-correct [[逃遁]]. False positive excluded after checking its own `characters:` field: [[道]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 廬 (5355; 1655 characters remaining).

### 2026-08-08, iteration 849 — [[characters/廬|廬]]

Clean verification: `mc_id: 1163` exact at `lookup/CC/CC 1000.md` line 172. 形声 classification (semantic 广 "roofed house," no vault page + phonetic [[盧]], OC \*ra) confirmed via Wiktionary; `graphemic_classification: 盧` already correct. `aliases: [庐]` confirmed as the genuine simplified form. Filled the empty `pos` (`名詞`, precedent from the stand_in 廬舎's own `pos` field). `hanmun_edu_level: 名` correctly maps to [Korean Name ㄹ](lookup/Korean/Korean%20Name%20ㄹ.md), keyed by the first consonant of the character's own Korean reading 려. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[廬舎]] (stand-in). False positives excluded after checking each candidate's own `characters:` field: [[六]], [[瀑布]]. **Chengyu**: [[禍延子孫]] matched a naive text grep but does not cite 廬 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 諾 (char) (5356; 1654 characters remaining).

### 2026-08-08, iteration 850 — [[characters/諾 (char)|諾]]

Clean verification: `mc_id: 1254` exact at `lookup/CC/CC 1000.md` line 267. 形声 classification (semantic [[言 (char)|言]] + phonetic [[若 (char)|若]], OC \*naːɡ) confirmed via Wiktionary; `graphemic_classification: 若` already correct. `aliases: [诺]` confirmed as the genuine simplified form. Filled the empty `pos` (`事詞` — an affirmative reply/consent, verbal in function). Normalized the CC-final link path (was written as a raw relative `../lookup/CC/finals/...` link instead of the standard wikilink form). Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[諾]]; kept already-correct [[諾貝金]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 鈴 (char) (5357; 1653 characters remaining).

### 2026-08-08, iteration 851 — [[characters/鈴 (char)|鈴]]

`mc_id: 4293` exceeds the vault's verifiable CC lookup range (`CC 3000.md` only covers ranks up to 4000... actually caps at exactly 4000; 4293 falls beyond it) — treated as legitimate long-tail data per standing policy, not flagged as an error. 形声 classification (semantic [[金 (char)|金]] + phonetic [[令 (char)|令]], OC \*reːŋ) confirmed via Wiktionary; `graphemic_classification: 令` already correct. `aliases: [铃]` confirmed as the genuine simplified form. Filled the empty `pos` (`名詞` — a concrete physical object). `hanmun_edu_level: 名` correctly maps to [Korean Name ㄹ](lookup/Korean/Korean%20Name%20ㄹ.md), keyed by the first consonant of the character's own Korean reading 령. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[鈴]] (the page previously had no `## Words` section). False positives excluded after checking each candidate's own `characters:` field: two homophone-adjacent [[令]] and [[零]] plus unrelated [[螟蛉]] — none cite 鈴 in their `characters:` field. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 牲 (5358; 1652 characters remaining).

### 2026-08-08, iteration 852 — [[characters/牲|牲]]

Clean verification: `mc_id: 1263` exact at `lookup/CC/CC 1000.md` line 276. 形声 classification (semantic [[牛 (char)|牛]] + phonetic [[生]], OC \*sreŋ) confirmed via Wiktionary; `graphemic_classification: 生` already correct. **Near-miss self-correction**: `vietnamese: chũa` initially looked like the same unrelated-word contamination bug found earlier this session on [[闘 (char)|闘]] (which had wrongly stored "pagoda/temple" chùa) — but Wiktionary's own entry for 牲 explicitly lists `chũa` as a genuine attested Nôm reading of this character, so it was correctly left in place; added the also-listed `xinh`, previously missing. Filled the empty `pos` (`名詞`, precedent from the stand_in 犠牲's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[犠牲]] (the page previously had no `## Words` section). **Chengyu**: added [[轄魚鳥牲]] (1 real hit, confirmed via its own `characters:` field) as a new `## Chengyu` section; [[舎本逐末]] and [[血誓盟約]] both matched a naive text grep but neither cites 牲 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 弊 (char) (5359; 1651 characters remaining).

### 2026-08-08, iteration 853 — [[characters/弊 (char)|弊]]

Clean verification: `mc_id: 1351` exact at `lookup/CC/CC 1000.md` line 368. Classification (semantic 廾 "both hands" + phonetic 敝, OC \*beds, "destroy, tatters" — Wiktionary describes it as a hybrid 形声/會意 case) confirmed via Wiktionary; `graphemic_classification: 敝` already correct. Both stored `vietnamese: [giẻ, tệ]` readings confirmed genuine and complete — no bug here despite superficially resembling the unrelated-reading contamination pattern found on other pages this session. Empty `aliases` confirmed correct (獘/毙 are archaic/semantically-diverged, not vault-worthy). Filled the empty `pos` (`性詞` — "evil, wrong" is adjectival). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[弊]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[郭清]]. **Chengyu**: [[磨穿鉄硯]] and [[貪官汚吏]] both matched a naive text grep but neither cites 弊 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 皿 (char) (5360; 1650 characters remaining).

### 2026-08-08, iteration 854 — [[characters/皿 (char)|皿]]

**mc_id bug fixed**: stored value `3320` pointed to `覿` at `lookup/CC/CC 3000.md` line 337 — a completely unrelated character. The actual entry for 皿 is line 338, rank `3321` (an off-by-one error). 象形 classification (pictogram of a footed vessel seen in profile) confirmed via Wiktionary; `graphemic_classification: 象形` already correct. **Vietnamese contamination bug fixed, caught via cross-reference rather than Wiktionary alone**: the character page stored 5 Vietnamese candidates (`mãnh, mạnh, mảng, mảnh, mịn`); a first-pass Wiktionary check seemed to support keeping all of them (its Hán Việt/Nôm sections list overlapping forms), but the citing word 皿's own Notes contains a prior deep-dive explicitly documenting that only `mãnh` is the confirmed Sino-Vietnamese reading for this specific "dish/container" sense — the other four "belong to unrelated homophone characters (mạnh 'strong,' mảnh 'fragment,' etc.), the same kind of stored-field contamination already documented multiple times elsewhere in this vault's history." Trusted the vault's own prior research over a surface Wiktionary read and removed the four contaminated entries. Filled the empty `pos` (`名詞`, precedent from the word 皿's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section — exactly as the word 皿's own Notes had already flagged this page as unperfected) into the proper 4-bullet `## Notes` section. **Self-caught error**: initially linked the frequency bullet's Grade tag using `joyo_level` (3) instead of `grade_level` (5) — corrected to [Grade 5] before finalizing.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[皿]] (the page previously had no `## Words` section). False positives excluded after checking each candidate's own `characters:` field: two genuine Dan'a'yo homophones [[明]] and [[鳴]] (per the word 皿's own callout) plus unrelated [[禾]], [[臼]], [[血]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[孟]], citing `graphemic_classification: 皿` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 壁 (char) (5361; 1649 characters remaining).

### 2026-08-08, iteration 855 — [[characters/壁 (char)|壁]]

Clean verification: `mc_id: 1539` exact at `lookup/CC/CC 1000.md` line 564. 形声 classification (semantic [[土 (char)|土]] + phonetic [[辟]], OC \*peːɡ) confirmed via Wiktionary; `graphemic_classification: 辟` already correct. **Malformed-field bug fixed, resolved using the citing word's own prior research**: `cantonese` was stored as the comma-joined string `"bek3, bik1, bik3"` — the citing word 壁's own Notes had already done the legwork identifying `bik1` as the standard literary reading (used in 壁虎, 壁畫) and the correct single field value, with `bek3` a restricted vernacular reading (tied specifically to 隔壁) and `bik3` a rare/marginal variant; corrected the field to `bik1`. The `vietnamese` list (`bích, bệch, bịch, vách`) was already in proper YAML-list form and, per that same word's Notes, all four are genuinely attested (bích = sole Hán Việt reading; vách = common Nôm doublet; bịch/bệch = marginal but genuine Nôm variants) — left unchanged. Also normalized `japanese: HEKI` (a bare scalar) to the standard single-item list form, and added the missing (previously absent, not merely empty) `aliases:` key. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits — this page went from 2 listed to 4 verified): added the self-referential `stand_in` [[壁]] and [[牆壁]] (using the corrected two-syllable ruby ㄑ⺢ㄫㄅㄝㄎ — 牆壁's own stored `注音` is a known, separately-flagged bug on that word page, single-syllable ㄅㄝㄎ instead of the compound form, per the word 壁's own homophone-check note); reformatted [[壁塁]] with proper ruby; kept already-correct [[壁虱]]. False positives excluded after checking each candidate's own `characters:` field: [[参入]], [[苦肉]]. **Chengyu**: [[意気揚揚]] matched a naive text grep but does not cite 壁 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 駅 (char) (5363; 1648 characters remaining).

### 2026-08-08, iteration 856 — [[characters/駅 (char)|駅]]

**Real missing-data bug fixed**: `mc_id` was empty; found the rank for its traditional form 驛 at `lookup/CC/CC 2000.md` line 858 — `2821` — and filled it in, noting in the bullet that this counts 驛's Classical Chinese frequency since 駅 itself is a modern Japanese shinjitai form. **Factual error fixed**: the body prose called 駅 "Japanese coined," but Wiktionary confirms it is explicitly *not* a kokuji — it's a shinjitai simplification of 驛 (睪 → 尺), the same imprecision echoed on the citing word 駅's own page (left uncorrected there, out of scope for this pass). 形声 classification (semantic [[馬 (char)|馬]] + phonetic [[尺 (char)|尺]]) confirmed; `graphemic_classification: 尺` already correct. Both `aliases: [驛, 驿]` confirmed genuine (traditional and simplified forms respectively). Filled the empty `boundedness` (50, estimated — no hard formula exists in this vault). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): kept already-correct [[駅]] (stand-in), now explicitly marked as such. False positive excluded after checking its own `characters:` field: [[䋇]] (a genuine Dan'a'yo homophone per the word 駅's own callout, sharing the 尺 phonetic series, but doesn't cite 駅 itself). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 4 genuine hits found (characters sharing phonetic 尺, matching the same phonetic series noted on the citing word's homophone explanation) — [[択]], [[沢]], [[鈬 (char)|鈬]], [[䋇 (char)|䋇]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 排 (char) (5364; 1647 characters remaining).

### 2026-08-08, iteration 857 — [[characters/排 (char)|排]]

Clean verification: `mc_id: 2459` exact at `lookup/CC/CC 2000.md` line 480. 形声 classification (OC \*brɯːl: semantic [[手 (char)|手]] + phonetic [[非 (char)|非]], OC \*pɯl) confirmed via Wiktionary; `graphemic_classification: 非` already correct. **Vietnamese contamination bug fixed**: 8 candidates were stored (`bài, bai, bày, bời, bay, bầy, vài, vời`); the citing word 排's own Notes explicitly identifies only `bài` as "the standard Sino-Vietnamese reading" — trimmed to that single value, consistent with the same contamination pattern already found and fixed on [[characters/皿 (char)|皿]] and [[characters/侯 (char)|侯]] this session. Normalized `japanese: HAI` (a bare scalar) to standard list form, and added the missing `aliases:` key (empty — 排 is unchanged between traditional and simplified). Deduplicated the body, which had the same etymology bullet written out twice (once well-formed, once with broken/raw markdown link syntax), and rebuilt into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits — this page went from 3 listed to 4 verified): added the self-referential `stand_in` [[排]] and previously-missing [[排水溝]]; kept already-correct [[排球]], [[排斥]]. False positive excluded after checking its own `characters:` field: [[計画]]. **Chengyu**: [[天衣無縫]] matched a naive text grep but does not cite 排 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 昇 (5365; 1646 characters remaining).

### 2026-08-08, iteration 858 — [[characters/昇|昇]]

**mc_id gap resolved with a documented judgment call**: `mc_id` was stored empty, and 昇 does not appear anywhere in the vault's CC lookup files (0–4000) under its own glyph. Wiktionary explicitly documents 昇 as "an alternative form of 升 ('to rise; to ascend')" — not an independent lexeme, just a graphic variant later specialized to the "rise" sense (in simplified Chinese, usage of 昇 is limited to personal names, with 升 being standard). Since the vault's corpus tracks only 升 (rank 415, on the already-perfected [[characters/升 (char)|升]]), assigned `mc_id: 415` to 昇 as well and flagged the resulting shared-rank duplication explicitly in the frontmatter/Notes rather than leaving the field empty — the same transparent-flag-don't-silently-resolve approach used for the [[characters/督|督]]/[[characters/誉|誉]] duplicate `danayo_id` earlier this session. 形声 classification (semantic [[日 (char)|日]] + phonetic [[升 (char)|升]], OC \*hljɯŋ) confirmed via Wiktionary; `graphemic_classification: 升` already correct. Normalized `japanese: SHOU` (bare scalar) to standard list form and `danayo_id: "5365"` (quoted string) to a bare number, matching every other perfected page's convention. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits — this page went from 2 listed to 4 verified): added the self-referential `stand_in` [[上昇]] and previously-missing [[昇天]] (using the word's own body-text gloss "ascend to heaven, to die," fuller than its truncated `english: die` frontmatter field); kept already-correct [[昇叙]], [[昇級]] (confirmed "Sheng Ji" is a legitimate proper-noun gloss for the card game, not an error — clarified as such in the Words entry). False positive excluded after checking its own `characters:` field: [[日]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 瞬 (5366; 1645 characters remaining).

### 2026-08-08, iteration 859 — [[characters/瞬|瞬]]

**mc_id left honestly unresolved**: stored empty, and — unlike [[characters/昇|昇]] earlier this iteration, which had a Wiktionary-documented equivalence to an already-ranked character — 瞬 has no such substitute; it simply does not appear anywhere in the vault's CC lookup files (`CC 0000` through `CC 3000`, covering ranks 1–4000), and no variant-equivalence to a ranked character is documented. Rather than fabricate a number, left the field empty and added an explicit "not found in available range, left unverified" note to the frequency bullet. 形声 classification (semantic [[目 (char)|目]] + phonetic [[舜]], OC \*hljuns) confirmed via Wiktionary; `graphemic_classification: 舜` already correct. Added the missing `aliases:` key (empty — 瞬 is unchanged between traditional and simplified; the listed variants 瞚/䀢/瞤/𥆧 are archaic, not vault-worthy). Rebuilt the malformed body (heading levels out of order, a bare unformatted mention of [[瞬間]] floating outside any list) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[一瞬]] and [[瞬間]] with proper ruby (the page previously had no real `## Words` section, just a stray inline mention). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 披 (char) (5467; 1644 characters remaining).

### 2026-08-08, iteration 860 — [[characters/披 (char)|披]]

Clean verification: `mc_id: 2226` exact at `lookup/CC/CC 2000.md` line 239. 形声 classification (semantic [[手 (char)|手]] + phonetic [[皮]], OC \*pʰral) confirmed via Wiktionary; `graphemic_classification: 皮` already correct. **Format-only fix, content confirmed genuine**: `vietnamese` was the malformed comma-joined string `"phơ, bờ, pha, phê, phi, phơi"` — unlike similar-looking cases fixed earlier this session ([[characters/皿 (char)|皿]], [[characters/侯 (char)|侯]], [[characters/排 (char)|排]]) where extra candidates turned out to be contamination from unrelated homophones, here Wiktionary's own Hán Nôm reading list for 披 directly attests all 6 forms — converted to a proper YAML list without removing any. Normalized `japanese: HI` (bare scalar) to standard list form, `danayo_id`/`mc_id` from quoted strings to bare numbers, and added the missing `aliases:` key (empty — no distinct simplified/variant form). Rebuilt the malformed body (wrong heading order, raw markdown links with an incorrect relative path for 披歴, an unformatted asterisk-bullet list) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, unchanged): added the self-referential `stand_in` [[披]] and reformatted [[披露]] and [[披歴]] with proper ruby (the latter's link was previously broken, pointing to a raw `../words/披歴` path instead of a wikilink). False positive excluded after checking its own `characters:` field: [[令和]]. **Chengyu**: [[羊衣餓狼]] matched a naive text grep but does not cite 披 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 惰 (6002; 1643 characters remaining).

### 2026-08-08, iteration 861 — [[characters/惰|惰]]

**mc_id bug fixed**: stored value `2235` pointed to `惶` at `lookup/CC/CC 2000.md` line 248 — a different character. The actual entry for 惰 is line 249, rank `2236` (an off-by-one error). 形声 classification (semantic [[Radicals/Radical 061|忄]] + abbreviated phonetic 隋, no vault page) confirmed via Wiktionary, matching the page's own already-correct body prose; `graphemic_classification: 隋` already correct. Both stored `vietnamese: [noạ, đoạ]` readings confirmed genuine and complete. Empty `aliases` confirmed correct. Rebuilt the body (floating CC-initial/final wikilinks outside any bullet, a stray numbered list instead of a proper Words entry) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, unchanged): added the self-referential `stand_in` [[怠惰]] and reformatted the "argon" abbreviation entry [[惰素]] with proper ruby (previously a raw, unlinked markdown reference); kept already-correct [[懶惰]]. False positives excluded after checking each candidate's own `characters:` field: [[炭素]], [[燐素]], [[高素]], [[佛雷素]], [[鹸素]] — all cite 素 but not 惰. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[楕]], citing `graphemic_classification: 隋` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 頚 (char) (6003; 1642 characters remaining).

### 2026-08-08, iteration 862 — [[characters/頚 (char)|頚]]

**mc_id bug fixed**: stored value `1671` pointed to `葛` at `lookup/CC/CC 1000.md` line 700 — a different character. The actual entry for 頸 (頚's traditional form) is line 701, rank `1672` (an off-by-one error). 形声 classification (semantic [[頁 (char)|頁]] + phonetic [[巠]], OC \*keːŋ) confirmed via Wiktionary, matching the page's own already-correct body prose; `graphemic_classification: 巠` already correct. Both `aliases: [頸, 颈]` confirmed genuine (traditional and simplified forms). **Duplicate-value bug fixed**: `japanese_native` listed `くび` twice (an accidental duplicate in a 2-item list); collapsed to a single value. **Likely-contamination bug fixed**: `vietnamese` was the malformed string `"nghỉnh, cảnh"` — the citing word 頚's own Notes does a careful reading-by-reading breakdown (Mandarin/Cantonese/Vietnamese all "use this character productively," Japanese/Korean prefer native words) and uses only `cảnh` throughout, never mentioning `nghỉnh`; Wiktionary's Vietnamese section could not be retrieved to independently confirm either way, so trusted the vault's own established single-value resolution (same reasoning applied to the [[characters/皿 (char)|皿]] and [[characters/侯 (char)|侯]] cases) and dropped `nghỉnh`. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[頚]] (stand-in), now explicitly marked as such. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits (quote-tolerant grep for 頚/巠/頸) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 溺 (char) (6004; 1641 characters remaining).

### 2026-08-08, iteration 863 — [[characters/溺 (char)|溺]]

**mc_id bug fixed**: stored value `1580` was a straight duplicate of [[characters/格 (char)|格]]'s own rank (verified earlier this session at `CC 1000.md` line 605) rather than 溺's actual entry, one line down at line 606, rank `1581`. Corrected. 形声 classification (semantic [[水 (char)|水]] + phonetic [[弱 (char)|弱]], OC \*neːwɢ) confirmed via Wiktionary; `graphemic_classification: 弱` already correct. **Vietnamese typo bug fixed**: of the 4 stored candidates (`niệu, ních, nịch, nịu`), Wiktionary's Hán Nôm list confirms exactly 3 — `nịch, niệu, nịu` — and explicitly does not include `ních` (a sắc-tone spelling, distinct from the confirmed nặng-tone `nịch`); removed `ních` as an unattested typo/duplicate-with-wrong-diacritic rather than a genuine fourth reading. Filled the empty `pos` (`事詞` — "to drown" is verbal). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[溺]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 憧 (6005; 1640 characters remaining).

### 2026-08-08, iteration 864 — [[characters/憧|憧]]

This page was in unusually good shape already (proper 4-bullet Notes, correctly-ruby'd Words section) — only real fixes were data gaps. `mc_id: 4100` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[Radicals/Radical 061|心]] + phonetic [[童]], OC \*doːŋ) confirmed via Wiktionary; `graphemic_classification: 童` and stored `vietnamese: sung` both already correct. **Real missing-data bug fixed**: `korean_native` was an empty string, but Wiktionary's Korean eumhun (음훈) gloss for this character is "그리워할 동" (geuriwohal dong, "to yearn/long for") — filled in `그리워할`.

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[憧憧]] (stand-in) and [[憧憬]], both already properly ruby'd and verified against their own `注音` fields. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 拭 (6006; 1639 characters remaining).

### 2026-08-08, iteration 865 — [[characters/拭|拭]]

**mc_id bug fixed**: stored value `3862` pointed to `纊` at `lookup/CC/CC 3000.md` line 899 — a different character. The actual entry for 拭 is line 900, rank `3863` (an off-by-one error). 形声 classification (semantic [[手 (char)|手]] + phonetic [[式]], OC \*hljɯɡ) confirmed via Wiktionary; `graphemic_classification: 式` already correct. **Vietnamese partly confirmed, partly pruned via cross-checking two independent sources**: of 3 stored candidates (`rị, thức, xức`), Wiktionary directly confirms `rị` as the sole Hán Nôm reading; `thức` is not on Wiktionary but IS independently confirmed by the citing word 擦拭's own Notes, which document its Vietnamese "sát thức" as "a real, attested Sino-Vietnamese compound (verified via search)" — composing 擦's sát + 拭's thức; `xức` has no supporting evidence from either source, so removed as an unconfirmed/likely-contaminated candidate (flagged here rather than silently dropped, in case evidence surfaces later). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[擦拭]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 曖 (6007; 1638 characters remaining).

### 2026-08-08, iteration 866 — [[characters/曖|曖]]

`mc_id: 5702` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[日 (char)|日]] + phonetic [[愛 (char)|愛]], OC \*qɯːds) confirmed via Wiktionary; `graphemic_classification: 愛` already correct. Both `aliases: [暧, 瞹]` confirmed genuine (simplified and alternative forms). **Phonetic-bleed-through contamination fixed**: `vietnamese` stored `[ái, áy]`; Wiktionary confirms only `áy` for 曖 itself, while `ái` is actually 愛's own well-known Sino-Vietnamese reading ("love") — the same character that supplies 曖's phonetic component. The citing word 曖昧's own Notes independently flag this exact confusion risk, warning that "the Chinese connotation of 'illicit love affair' perhaps arises from the first syllable's homophony with 'love' (愛)" — strong corroborating evidence that `ái` had bled in from the phonetic component rather than being 曖's own reading. Removed `ái`. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[曖昧]] (stand-in). False positive excluded after checking its own `characters:` field: [[唉]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 尉 (char) (6008; 1637 characters remaining).

### 2026-08-08, iteration 867 — [[characters/尉 (char)|尉]]

Clean verification: `mc_id: 256` exact at `lookup/CC/CC 0000.md` line 268. 會意 classification (𡰥 + [[Radicals/Radical 041|寸]] "hand" + [[火 (char)|火]] "fire," per Wiktionary's own "possibly" hedge) confirmed; `graphemic_classification: 會意` already correct. Empty `aliases` confirmed correct — the listed variants (叞/㷉/𤈫/熨) either archaic or (in 熨's case) a distinct pronunciation/meaning branch, not a vault-worthy alias of this specific "officer" sense. **Real missing-data bug fixed**: `korean_native` was an empty string; Wiktionary's Korean gloss for the 위 (wi) reading specifically is "벼슬" (byeoseul, "official position/rank") — filled in (the other listed gloss, "다리미 울"/darimi ul, belongs to a different reading, 울, not used in this vault's entry). Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[尉]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[九卿]]. **Chengyu**: [[焚書坑儒]] matched a naive text grep but does not cite 尉 in its own `characters:` field — correctly omitted. **Derived Characters**: 2 genuine hits found — [[熨]] and [[慰]], both citing `graphemic_classification: 尉` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 虐 (6009; 1636 characters remaining).

### 2026-08-08, iteration 868 — [[characters/虐|虐]]

Clean verification: `mc_id: 1428` exact at `lookup/CC/CC 1000.md` line 449. 會意 classification ([[虎 (char)|虎]] "tiger" + [[人 (char)|人]] "person" — a tiger about to eat a person) confirmed via Wiktionary; `graphemic_classification: 會意` already correct. Both stored `vietnamese: [ngước, ngược]` readings confirmed genuine and complete. Empty `aliases` confirmed correct. Filled the empty `pos` (`性詞`, precedent from the stand_in 暴虐's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[暴虐]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 尻 (char) (6010; 1635 characters remaining).

### 2026-08-08, iteration 869 — [[characters/尻 (char)|尻]]

Clean verification: `mc_id: 3578` exact at `lookup/CC/CC 3000.md` line 603. Classification confirmed via Wiktionary — 尻 began as an oracle-bone 象形 pictogram, later reanalyzed in seal script as 形声 (semantic [[Radicals/Radical 044|尸]] + phonetic [[九 (char)|九]], OC \*kuː), matching the page's own already-correct body prose; `graphemic_classification: 九` already correct. All four `aliases` (𡰼, 𡱧, 𡱂, 㞍) confirmed genuine per Wiktionary's own variant-forms list. Stored `vietnamese: khào` could not be independently confirmed or refuted (Wiktionary's Vietnamese section for this character is empty) — left as-is absent contrary evidence. Deduplicated the body, which repeated the same etymology point twice (once as a bare "List of 象形" link, once as a fuller prose bullet), and rebuilt into the proper 4-bullet `## Notes` section with a Words section added.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[尻]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 迭 (6011; 1634 characters remaining).

### 2026-08-08, iteration 870 — [[characters/迭|迭]]

**mc_id bug fixed**: stored value `2486` pointed to `碭` at `lookup/CC/CC 2000.md` line 507 — a different character. The actual entry for 迭 is line 508, rank `2487` (an off-by-one error). 形声 classification (semantic [[Radicals/Radical 162|辵]] + phonetic [[失]], OC \*l'iːɡ) confirmed via Wiktionary; `graphemic_classification: 失` already correct. **Vietnamese contamination bug fixed**: 7 candidates were stored (`dập, dật, dắt, dặt, dựt, giật, điệt`); Wiktionary's Hán Việt list for 迭 gives exactly `điệt, tuyển, dật` — kept the 2 confirmed matches, added the missing `tuyển`, and dropped the 4 unconfirmed candidates (dập, dắt, dặt, dựt, giật) as likely contamination, consistent with the pattern already fixed on [[characters/皿 (char)|皿]], [[characters/侯 (char)|侯]], and [[characters/排 (char)|排]] this session. Filled the empty `pos` (`動詞`, precedent from the stand_in 更迭's own `pos` field — confirmed this is a valid, common pos value elsewhere in the vault despite not appearing in this session's characters until now). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[更迭]] (stand-in). **Chengyu**: [[春夏秋冬]] matched a naive text grep but does not cite 迭 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 娠 (6012; 1633 characters remaining).

### 2026-08-08, iteration 871 — [[characters/娠|娠]]

**mc_id bug fixed**: stored value `3737` pointed to `癃` at `lookup/CC/CC 3000.md` line 770 — a different character. The actual entry for 娠 is line 771, rank `3738` (an off-by-one error). 形声 classification (semantic [[Radicals/Radical 038|女]] + phonetic [[辰]], OC \*djɯn) confirmed via Wiktionary, matching the page's own already-correct body prose; `graphemic_classification: 辰` already correct. Stored `vietnamese: thần` confirmed as the sole genuine Hán Việt reading. **Real missing-data bug fixed**: `korean_native` was an empty string; Wiktionary's Korean eumhun gloss is "아이 밸" (ai bael, "with child") — filled in. Rebuilt the malformed body (raw relative-path links instead of standard wikilinks, a stray CC-initial/final wikilink pair floating after the Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[妊娠]] (stand-in). False positive excluded after checking its own `characters:` field: [[中止]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 蹴 (char) (6013; 1632 characters remaining).

### 2026-08-08, iteration 872 — [[characters/蹴 (char)|蹴]]

**mc_id bug fixed**: stored value `3403` pointed to `佛` at `lookup/CC/CC 3000.md` line 424 — a different character. The actual entry for 蹴 is line 425, rank `3404` (an off-by-one error). 形声 classification (semantic [[Radicals/Radical 157|足]] + phonetic [[就 (char)|就]], OC \*zuɡs) confirmed via Wiktionary, matching the page's own already-correct body prose; `graphemic_classification: 就` already correct. Stored `vietnamese: xúc` confirmed as the sole genuine Hán Việt/Nôm reading. Filled the empty `pos` (`事詞` — "to kick" is verbal). Rebuilt the malformed body (raw markdown link with dash-separated gloss instead of a proper ruby bullet, a stray CC-initial/final wikilink pair floating after the Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, unchanged): added the self-referential `stand_in` [[蹴]]; reformatted [[蹴球]] with proper ruby (fixed the raw markdown-link/en-dash format); kept already-correct [[蹴鞠]]. False positive excluded after checking its own `characters:` field: [[足球]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 褐 (char) (6014; 1631 characters remaining).

### 2026-08-08, iteration 873 — [[characters/褐 (char)|褐]]

Clean verification: `mc_id: 2411` exact at `lookup/CC/CC 2000.md` line 432. **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `喝` (a common, unrelated character meaning "to shout/drink," pronounced hē), but Wiktionary confirms the real phonetic component is `曷` (no vault page) — corrected. **Phonetic-series contamination fixed**: `aliases: [竭]` — Wiktionary explicitly addresses this exact confusion, stating 竭 "shares the same phonetic component (曷)... but is not documented as an alternative or variant form of 褐"; removed. Stored `vietnamese: hạt` confirmed as the sole genuine Hán Nôm reading. Filled the empty `pos` (`性詞` — "brown, dull, dark" is adjectival). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[褐]]; kept already-correct "holmium" abbreviation entry [[褐金]]. False positives excluded after checking each candidate's own `characters:` field: [[栗色]], [[桃金]], [[核金]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing the corrected phonetic 曷) — [[渇 (char)|渇]] and [[蝎 (char)|蝎]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 酵 (6015; 1630 characters remaining).

### 2026-08-08, iteration 874 — [[characters/酵|酵]]

**mc_id sentinel cleared, left honestly unresolved**: stored as `0`, which isn't a valid rank in a 1-indexed corpus — read as a placeholder for "not found" rather than a real value. 酵 does not appear anywhere in the vault's CC lookup files (ranks 1–4000), and no variant-equivalence to an already-ranked character is documented (unlike [[characters/昇|昇]] earlier this session). Cleared to empty and added an explicit "not found in available range" note to the frequency bullet, matching the approach used for [[characters/瞬|瞬]]. 形声 classification (semantic [[酉]] + phonetic [[孝 (char)|孝]], OC \*qʰruːs) confirmed via Wiktionary; `graphemic_classification: 孝` already correct. All 4 stored `vietnamese` readings (`diếu, dáo, giáo, giếu`) confirmed genuine and complete. Filled the empty `pos` (`名詞`). Removed a stray personal placeholder comment ("I'm shocked its not old") that had been left in the Notes section instead of real content, and rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[酵母]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 狩 (6016; 1629 characters remaining).

### 2026-08-08, iteration 875 — [[characters/狩|狩]]

Clean verification: `mc_id: 1390` exact at `lookup/CC/CC 1000.md` line 407. 形声 classification (semantic [[犬 (char)|犬]] + phonetic [[守]], OC \*qʰljus) confirmed via Wiktionary; `graphemic_classification: 守` already correct. Stored `vietnamese: thú` confirmed as the sole genuine Hán Nôm reading. Filled the empty `pos` (`動詞`, precedent from the stand_in 狩獵's own `pos` field). Rebuilt the malformed body (Words section placed before Notes, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[狩獵]] (stand-in). False positive excluded after checking its own `characters:` field: [[蛍火虫]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 眺 (6017; 1628 characters remaining).

### 2026-08-08, iteration 876 — [[characters/眺|眺]]

`mc_id: 4897` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[目 (char)|目]] + phonetic [[兆]], OC \*l'eːwʔ) confirmed via Wiktionary; `graphemic_classification: 兆` already correct. Stored `vietnamese: thiếu` confirmed as the sole genuine Hán Nôm reading. Filled the empty `pos` (`事詞`, precedent from the stand_in 眺望's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[眺望]] (stand-in), verified its ruby exactly matches the word's own `注音` field. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 哺 (6018; 1627 characters remaining).

### 2026-08-08, iteration 877 — [[characters/哺|哺]]

**mc_id bug fixed**: stored value `3184` pointed to `謫` at `lookup/CC/CC 3000.md` line 193 — a different character. The actual entry for 哺 is line 194, rank `3185` (an off-by-one error). 形声 classification (semantic [[口 (char)|口]] + phonetic [[甫]], OC \*baːs) confirmed via Wiktionary; `graphemic_classification: 甫` already correct. **Vietnamese partly corrected**: of 9 stored candidates, Wiktionary's own (messy, duplicated) Hán Nôm list confirms 7 (`bu, bô, bú, bụ, pho, phò, phô`) and separately lists `bộ` (missing from the stored set) while explicitly not listing `bua` or `bù`; corrected to the 8 confirmed forms. The addition of `bộ` is independently corroborated by the citing word 反哺's own Vietnamese field "phản bộ," which uses `bộ` as 哺's contribution — strong cross-source confirmation. Filled the empty `pos` (`事詞`, precedent from the stand_in 哺乳's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, unruby'd Words entry) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added previously-missing [[反哺]]; reformatted [[哺乳]] (stand-in) with proper ruby, verified against its own `注音` field. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 潟 (6019; 1626 characters remaining).

### 2026-08-08, iteration 878 — [[characters/潟|潟]]

`mc_id: 9442` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy (this is a modern/place-name-driven character, plausibly rare in Classical Chinese proper). 形声 classification (semantic [[水 (char)|水]] + phonetic 舄, no vault page) confirmed via Wiktionary; `graphemic_classification: 舄` already correct. Stored `vietnamese: tích` confirmed as the sole genuine Hán Việt reading. **Unverifiable historical claim softened**: the body asserted 潟 was "added to the J[ō]y[ō] list in 2017 because of prefecture names," but the only major Jōyō revision that added prefecture-name kanji was 2010, not 2017 — unable to confirm the specific year either way via available sources, so rephrased to state the well-established fact (used in prefecture names, e.g. 新潟/Niigata) without asserting an unverified date. Filled the empty `pos` (`名詞`, precedent from the stand_in 潟湖's own `pos` field). Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[潟湖]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 裸 (char) (6020; 1625 characters remaining).

### 2026-08-08, iteration 879 — [[characters/裸 (char)|裸]]

**mc_id bug fixed**: stored value `3067` pointed to `袂` at `lookup/CC/CC 3000.md` line 72 — a different character. The actual entry for 裸 is line 73, rank `3068` (an off-by-one error). 形声 classification (semantic [[衣]] + phonetic [[果]], OC \*kloːlʔ) confirmed via Wiktionary; `graphemic_classification: 果` already correct. **Format-only fix, content confirmed genuine**: `vietnamese` was the malformed comma-joined string `"lỏa, loả, khỏa, khoả, lõa, loã"` — Wiktionary confirms all 6 as legitimate Hán Việt readings; converted to a proper YAML list without removing any. Preserved the existing body note about 赤裸 not being used as the stand-in (folded into the etymology bullet rather than left as a stray unattached sentence). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[裸]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 胎 (6021; 1624 characters remaining).

### 2026-08-08, iteration 880 — [[characters/胎|胎]]

**mc_id bug fixed**: stored value `2405` pointed to `閣` at `lookup/CC/CC 2000.md` line 426 — a different character. The actual entry for 胎 is line 427, rank `2406` (an off-by-one error). 形声 classification (semantic [[肉 (char)|肉]] + phonetic [[台 (char)|台]]) confirmed via Wiktionary; `graphemic_classification: 台` already correct. Stored `vietnamese: thai` confirmed as the sole genuine Hán Việt reading. **Real missing-data bug fixed**: `korean_native` was an empty string; Wiktionary's Korean eumhun components combine to "아이 밸" ("to conceive a child"), the same phrasing pattern already established on [[characters/娠|娠]] earlier this session — filled in. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (a Words section split across two locations — two entries under the `# Notes` heading, one properly under `## Words`) into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits — this page went from 3 listed to 4 verified): added previously-missing [[堕胎]]; kept already-correct [[胎児]] (stand-in), [[胎盤]], [[受胎]], all verified against their own `注音` fields. False positives excluded after checking each candidate's own `characters:` field: [[児]], [[受託]], [[堕落]], [[受賞]]. **Chengyu**: [[加哀痛産]] matched a naive text grep but does not cite 胎 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 箸 (char) (6022; 1623 characters remaining).

### 2026-08-08, iteration 881 — [[characters/箸 (char)|箸]]

**mc_id bug fixed**: stored value `2871` pointed to `軀` at `lookup/CC/CC 2000.md` line 908 — a different character. The actual entry for 箸 is line 909, rank `2872` (an off-by-one error). 形声 classification (semantic [[竹 (char)|竹]] + phonetic [[者 (char)|者]], OC \*das) confirmed via Wiktionary; `graphemic_classification: 者` already correct. `vietnamese` (4 candidates: chước, giạ, trứ, đũa) could not be independently confirmed or refuted — Wiktionary's Vietnamese section repeatedly returned truncated/empty content across multiple fetch attempts, and the citing word 箸's own field is null — left unchanged absent contrary evidence (unlike clear contamination cases elsewhere this session, there was no positive signal pointing to a specific wrong source). Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[箸]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 腕 (char) (6024; 1622 characters remaining).

### 2026-08-08, iteration 882 — [[characters/腕 (char)|腕]]

**mc_id bug fixed**: stored value `3621` pointed to `峨` at `lookup/CC/CC 3000.md` line 650 — a different character. The actual entry for 腕 is line 651, rank `3622` (an off-by-one error). 形声 classification (semantic [[肉 (char)|肉]] + phonetic [[宛]], OC \*qoːns) confirmed via Wiktionary; `graphemic_classification: 宛` already correct. Both `vietnamese: [oản, uyển]` readings confirmed genuine and complete. Empty `aliases` confirmed correct. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[腕]] (the page previously had no `## Words` section). **Chengyu**: [[焚琴煮鶴]] matched a naive text grep but does not cite 腕 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 酪 (6025; 1621 characters remaining).

### 2026-08-08, iteration 883 — [[characters/酪|酪]]

`mc_id: 4126` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. **Reversed semantic/phonetic bug fixed**: the body prose described [[酉]] as phonetic and [[各 (char)|各]] as semantic ("alcohol; fermented drink") — backwards. Wiktionary confirms 酉 ("alcohol; fermented drink") is the semantic component and 各 (OC \*klaːɡ) is the actual phonetic; `graphemic_classification: 各` in the frontmatter was already correct despite the body text's contradiction, so only the prose needed fixing. **Vietnamese content bug fixed**: stored `vietnamese: lộ` is not attested anywhere for 酪 — Wiktionary's sole listed Hán Việt reading is `lạc`; corrected. Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[乳酪]] and reformatted [[乾酪]] with proper ruby. False positive excluded after checking its own `characters:` field: [[鰐梨]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 痴 (6026; 1620 characters remaining).

### 2026-08-08, iteration 884 — [[characters/痴|痴]]

`mc_id: 8749` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[Radicals/Radical 104|疒]] + phonetic [[知 (char)|知]]) confirmed via Wiktionary; `graphemic_classification: 知` already correct. `aliases: [癡]` confirmed as the genuine kyūjitai/traditional form. **Vietnamese completed**: 2 of 3 Wiktionary-attested readings were stored (`se, si`); added the missing third, `sy`. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no proper Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added the self-referential `stand_in` [[痴漢]]; kept already-correct [[痴情]], verified against its own `注音` field. False positive excluded after checking its own `characters:` field: [[呆]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 窒 (6027; 1619 characters remaining).

### 2026-08-08, iteration 885 — [[characters/窒|窒]]

**mc_id bug fixed**: stored value `3052` pointed to `紳` at `lookup/CC/CC 3000.md` line 57 — a different character. The actual entry for 窒 is line 58, rank `3053` (an off-by-one error). 形声 classification (semantic [[Radicals/Radical 116|穴]] + phonetic [[至 (char)|至]], OC \*tjiɡs) confirmed via Wiktionary, filling in the semantic gloss ("hole, cavity") that had been left as an empty string in the body prose; `graphemic_classification: 至` already correct. **Vietnamese completed**: all 4 stored candidates (khỏng, rấp, rất, trất) confirmed genuine; added 4 further Wiktionary-attested readings that were missing (trật, rứt, thắt, chật). Rebuilt the malformed body (a "Daughter characters" list using non-standard indentation, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section, folding the daughter-character note into a proper `## Derived Characters` section.

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[窒息]] (stand-in), reformatted with confirmed ruby; added the "nitrogen" abbreviation entry [[窒素]], previously only a bare inline mention rather than a proper Words entry. False positives excluded after checking each candidate's own `characters:` field: [[紫素]], [[虹霓]], [[栄養素]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[膣 (char)|膣]] (matching the body's own pre-existing "daughter characters" note) — formalized into a proper section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 癒 (6028; 1618 characters remaining).

### 2026-08-08, iteration 886 — [[characters/癒|癒]]

`mc_id: 8346` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[Radicals/Radical 104|疒]] + phonetic [[愈]], OC \*loʔ) confirmed via Wiktionary; `graphemic_classification: 愈` already correct. All 3 stored `vietnamese` readings (`dú, dũ, rũ`) confirmed genuine (dũ is both Hán Việt and Nôm; dú and rũ are Nôm-only, both attested). Confirmed the empty `korean_native` is factually correct, not a gap — Wiktionary explicitly states no kun/native Korean reading exists for this character. Filled the empty `pos` (`事詞` — "to get well, recover" is verbal). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added the self-referential `stand_in` [[癒合]]; kept already-correct [[治癒]], verified against its own `注音` field. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits — the quote-tolerant grep only matched the page's own file — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 顎 (6029; 1617 characters remaining).

### 2026-08-08, iteration 887 — [[characters/顎|顎]]

**mc_id sentinel cleared, left honestly unresolved**: stored as `0` (an invalid placeholder, same pattern as [[characters/酵|酵]] earlier this session). 顎 does not appear anywhere in the vault's CC lookup files. Cleared to empty with an explicit "not found" note. 形声 classification (semantic [[頁 (char)|頁]] + phonetic 咢, OC \*ŋaːɡ, no vault page) confirmed via Wiktionary; `graphemic_classification: 咢` already correct. `aliases: [齶]` confirmed genuine; added two further Wiktionary-listed variants that were missing — 腭 (alternative form) and 颚 (simplified form). Stored `vietnamese: ngạc` could not be directly confirmed via Wiktionary (no Vietnamese section shown) but is well-established as the standard Sino-Vietnamese reading for this jaw/palate character family — left as-is. Removed the same stray personal placeholder comment ("I'm shocked its not old") found on 酵, and normalized a raw relative-path CC-final link. Rebuilt into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[下顎]] (the page previously had no `## Words` section), ruby verified against the word's own `注音` field after an initial self-caught typo (a stray middle dot) was corrected. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing phonetic 咢) — [[鰐]] and [[鄂]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 妊 (char) (6030; 1616 characters remaining).

### 2026-08-08, iteration 888 — [[characters/妊 (char)|妊]]

Clean verification: `mc_id: 3314` exact at `lookup/CC/CC 3000.md` line 331. 形声 classification (semantic [[女 (char)|女]] + phonetic [[壬]], OC \*njɯms) confirmed via Wiktionary; `graphemic_classification: 壬` already correct. Stored `vietnamese: nhâm` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`事詞` — "to be pregnant, conceive" is verbal). Rebuilt the malformed body (Words section placed before Notes, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added the self-referential `stand_in` [[妊]]; kept already-correct [[妊娠]]. False positive excluded after checking its own `characters:` field: [[中止]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 弥 (char) (6031; 1615 characters remaining).

### 2026-08-08, iteration 889 — [[characters/弥 (char)|弥]]

Clean verification: `mc_id: 1184` exact at `lookup/CC/CC 1000.md` line 193 (`彌`). **Phonetic-component naming bug fixed**: `graphemic_classification` was stored as `尔` — a simplified/variant glyph — but the actual phonetic component per Wiktionary (and the page's own body prose, which already linked to `characters/爾 (char).md`) is `爾`, which has its own vault character page while `尔` does not; corrected the frontmatter field to `爾` to match the linked component and vault convention of citing the page-bearing form. Both `aliases: [彌, 瀰]` confirmed genuine. **Real missing-data bug fixed**: `korean_native` was an empty string; Wiktionary's Korean eumhun gloss for the 미 (mi) reading used in this sense is "두루" ("all over, widespread") — filled in (the character's other gloss, "미륵"/mireuk, belongs to the unrelated Buddhist-Maitreya reading branch, already covered separately via the word [[弥勒]]). Filled the empty `pos` (`副詞` — "all the more, increasingly" is adverbial; confirmed as an established pos value elsewhere in the vault). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks between Notes bullets) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 2 listed to 3 verified): added the self-referential `stand_in` [[弥]]; kept already-correct [[弥漫]], [[弥勒]], both verified against their own `注音` fields. False positive excluded after checking its own `characters:` field: [[阿]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing the corrected phonetic 爾/尔) — [[祢]] and [[璽]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 痘 (6032; 1614 characters remaining).

### 2026-08-08, iteration 890 — [[characters/痘|痘]]

**mc_id sentinel cleared, left honestly unresolved**: stored as `0` (same invalid-placeholder pattern as [[characters/酵|酵]] and [[characters/顎|顎]] earlier this session). 痘 does not appear anywhere in the vault's CC lookup files. Cleared to empty with an explicit "not found" note. 形声 classification (semantic [[Radicals/Radical 104|疒]] + phonetic [[豆 (char)|豆]], OC \*doːs — described by Wiktionary as a disease causing bean-shaped skin eruptions) confirmed; `graphemic_classification: 豆` already correct. Stored `vietnamese: đậu` confirmed as the sole genuine Hán Nôm reading. **Typo bug fixed**: `english` list had `smallbox` instead of `smallpox` — corrected here and on the same typo's second occurrence in the citing word [[猿痘]]'s own etymology line. Filled the empty `pos` (`名詞`, precedent from the stand_in 痘痕's own `pos` field). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added previously-missing [[猿痘]]; kept already-correct [[痘痕]] (stand-in), verified against its own `注音` field. False positive excluded after checking its own `characters:` field: [[豆]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 瞳 (6033; 1613 characters remaining).

### 2026-08-08, iteration 891 — [[characters/瞳|瞳]]

`mc_id: 4067` exceeds the vault's verifiable CC lookup range (ranks 1–4000, confirmed against `CC 3000.md`'s final entry at rank 4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[目 (char)|目]] + phonetic [[童]], OC \*doːŋ) confirmed via Wiktionary; `graphemic_classification: 童` already correct. Both stored `vietnamese: [tròng, đồng]` readings confirmed genuine — Wiktionary explicitly identifies `tròng` as a documented chữ Nôm form for "eyeball," not unrelated-character contamination like several similar-looking cases fixed earlier this session. Filled the empty `pos` (`名詞`, precedent from the stand_in 瞳孔's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[瞳孔]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[眼睛]] (a genuine synonym per 瞳孔's own body note, but doesn't cite 瞳). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 垣 (char) (6034; 1612 characters remaining).

### 2026-08-08, iteration 892 — [[characters/垣 (char)|垣]]

**mc_id bug fixed**: stored value `1577` pointed to `庫` at `lookup/CC/CC 1000.md` line 602 — a different character. The actual entry for 垣 is line 603, rank `1578` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[土 (char)|土]] + phonetic [[亘 (char)|亘]]) confirmed via Wiktionary; `graphemic_classification: 亘` already correct. Stored `vietnamese: viên` confirmed as the sole genuine Hán Việt reading — cross-checked against the citing word 垣's own Notes, which independently confirm `viên` and explain it belongs to a legitimate shared-reading series with 圓/員/園, not a mix-up. Filled the empty `pos` (`名詞`, precedent from the word 垣's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[垣]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found — [[宣]] and [[桓]], both citing `graphemic_classification: 亘` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 箋 (6035; 1611 characters remaining).

### 2026-08-08, iteration 893 — [[characters/箋|箋]]

`mc_id: 9746` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `㦮`, but Wiktionary confirms the real phonetic component is `戔` (OC \*zlaːn, no vault page) — the same specific "㦮 substituted for 戔" error already caught and fixed on [[characters/残 (char)|残]] earlier this session, suggesting a systematic upstream data-entry mix-up between these two visually similar rare glyphs. Corrected the field to `戔`. `aliases: [笺]` confirmed as the genuine simplified form. Stored `vietnamese: tiên` confirmed as the sole genuine Hán Việt reading. **Typo bug fixed**: `english` list had `stationary` (meaning "unmoving") instead of the intended `stationery` (writing materials) — corrected here and on the same typo's occurrence in the citing word [[便箋]]'s own `english` field. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[便箋]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[孝廉]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits (quote-tolerant grep for 箋 and 戔 only matched [[残 (char)|残]] and [[践]], which share the *other* phonetic 戔-series but are not citing 箋 itself) — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 紺 (char) (6036; 1610 characters remaining).

### 2026-08-08, iteration 894 — [[characters/紺 (char)|紺]]

**mc_id bug fixed**: stored value `3799` pointed to `痾` at `lookup/CC/CC 3000.md` line 832 — a different character. The actual entry for 紺 is line 833, rank `3800` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[糸]] + phonetic [[甘 (char)|甘]], OC \*kɯːms) confirmed via Wiktionary; `graphemic_classification: 甘` already correct. `aliases: [绀]` confirmed as the genuine simplified form. All 3 stored `vietnamese` readings (`cám, tim, tím`) confirmed genuine Hán Nôm forms. Filled the empty `pos` (`性詞` — "navy blue" is adjectival/color-descriptive). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): **self-caught error**: initially used [[紺色]] as the `stand_in` entry, but the actual stand_in word is the bare [[紺]] itself (verified against the word's own page, which is used independently and explicitly notes it as a homophone/derived-character pair with [[甘]]) — corrected before finalizing; kept [[紺色]] as a second, non-stand-in entry. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted (though note: the word 紺's own homophone callout observes that 紺 is itself one of [[甘]]'s Derived Characters, an upstream relationship already documented on 甘's page).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 肌 (6037; 1609 characters remaining).

### 2026-08-08, iteration 895 — [[characters/肌|肌]]

**mc_id bug fixed**: stored value `1920` pointed to `坤` at `lookup/CC/CC 1000.md` line 961 — a different character. The actual entry for 肌 is line 962, rank `1921` (an off-by-one error). **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `幾` (a larger, unrelated character meaning "how many"), but Wiktionary confirms the real phonetic component is the much simpler `几` (OC \*krilʔ) — the exact same "幾ᐳ几" mix-up already caught and fixed on [[characters/飢|飢]] earlier this session (unsurprising, since 肌/飢 are themselves a phonetic-series pair sharing this same 几 component). Corrected the field to `几`. Stored `vietnamese: cơ` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[肌膚]] (stand-in) and [[肌理]], both verified against their own `注音` fields. False positives excluded after checking each candidate's own `characters:` field: [[梗塞]], [[白及]], [[筋肉]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[飢]], sharing the corrected phonetic 几 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 赦 (6038; 1608 characters remaining).

### 2026-08-08, iteration 896 — [[characters/赦|赦]]

Clean verification: `mc_id: 775` exact at `lookup/CC/CC 0000.md` line 802. **Classification bug fixed**: `graphemic_classification` was stored as `會意`, and the page's own body prose listed it under "List of 会意" as [[Radicals/Radical 155|亦]] + [[Radicals/Radical 066|攴]] — but Wiktionary's own etymology explicitly states the bronze-script form 𢼜 was itself already 形声 (phono-semantic): phonetic 亦 (OC \*laːɡ) + semantic 攴, and that "in later scripts, the phonetic component was replaced with 赤." The page had conflated a historical-development note with a 會意 classification, when the source it was citing actually says 形声 throughout. Corrected `graphemic_classification` to `赤` (the modern phonetic, confirmed by OC rhyme match: 赦 \*hljaɡs vs. 赤 \*kʰljaɡ) and rewrote the Notes bullet to describe the correct semantic/phonetic split, preserving the historical 亦→赤 phonetic-replacement note. Stored `vietnamese: xá` confirmed as the sole genuine Hán Việt reading. `pos`/other frontmatter fields already correct.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[赦免]] (stand-in). **Chengyu**: [[臥薪嘗胆]] matched a naive text grep but does not cite 赦 in its own `characters:` field — correctly omitted. **Derived Characters**: 1 genuine hit found — [[郝]], sharing the corrected phonetic 赤 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 腺 (6039; 1607 characters remaining).

### 2026-08-08, iteration 897 — [[characters/腺|腺]]

**mc_id sentinel cleared and root cause identified**: stored as `0` (same invalid-placeholder pattern as [[characters/酵|酵]], [[characters/顎|顎]], [[characters/痘|痘]] earlier this session). Unlike those cases, here Wiktionary confirms *why* no rank exists: 腺 is a genuine kokuji, coined by Japanese scholar Udagawa Genshin (rangaku era, late 1700s–early 1800s) as a translation for Dutch *klier* ("gland") — it has zero Classical Chinese attestation by definition, not merely an unranked long-tail character. Rewrote the frequency bullet to say so explicitly rather than leaving it looking like an unresolved gap. 形声 classification (semantic [[肉 (char)|肉]] + phonetic [[泉]]) confirmed; `graphemic_classification: 泉` already correct. Stored `vietnamese: tuyến` confirmed as the sole genuine Hán Việt reading. **Typo/imprecision fixed**: body said "technically gokuji" — corrected to the standard term "kokuji" (国字), with the etymological detail now properly sourced. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[腺体]] (stand-in). False positive excluded after checking its own `characters:` field: [[唾液]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 癖 (char) (6040; 1606 characters remaining).

### 2026-08-08, iteration 898 — [[characters/癖 (char)|癖]]

`mc_id: 10652` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[Radicals/Radical 104|疒]] + phonetic [[辟]], OC \*pʰeːɡ) confirmed via Wiktionary; `graphemic_classification: 辟` already correct. Stored `vietnamese: [phích, tịch]` could not be independently confirmed or refuted (Wiktionary's page omits a Vietnamese section entirely, and the citing word 癖's own field is null) — left unchanged absent contrary evidence, consistent with the same non-destructive approach used on [[characters/箸 (char)|箸]] earlier this session. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[癖]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 缶 (6041; 1605 characters remaining).

### 2026-08-08, iteration 899 — [[characters/缶|缶]]

**mc_id bug fixed**: stored value `2754` pointed to `蔥` at `lookup/CC/CC 2000.md` line 787 — a different character. The actual entry for 缶 is line 788, rank `2755` (an off-by-one error). **Real cross-field reading-inconsistency bug fixed**: the page mixed two different characters' readings — `mandarin: fǒu` and `cantonese: fau2` were 缶's own native readings, while `japanese: KAN`, `middle_chinese_initial/final: k/uɑn`, and the derived `羅馬字/諺文/注音` (gwan/관/ㄍ⺢ㄋ) all matched 罐's reading (MC \*kuɑnH per Wiktionary) instead. The citing word [[缶頭]]'s own Notes independently states the vault's actual policy: "Dan'a'yo 缶 is aliased to 罐; the CJKV readings follow 罐頭" — confirming `mandarin`/`cantonese`/`korean` should all have followed 罐 (guàn/gun3/관) rather than 缶's own (fǒu/fau2/부), which had been silently left inconsistent. Corrected all three fields to match 罐, and updated `hanmun_edu_level: 名`'s Korean-initial lookup link from [Korean Name ㅂ] to [Korean Name ㄱ] to match the corrected 관 reading. This mirrors real-world usage: modern Japanese 缶 is literally the simplified shinjitai substitute for kyūjitai 罐 (dropping the 雚 phonetic), carrying over its "kan/can" reading and meaning — confirmed via ja.wiktionary. 象形 classification confirmed via Wiktionary; already correct. All 3 `aliases` confirmed genuine (罐 as kyūjitai, 缻/𦈢 as classical variants). Rebuilt the body to explain the alias-reading relationship explicitly rather than leaving the inconsistency implicit.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[缶頭]] (stand-in), whose own body note was the very source that resolved this iteration's central bug. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found — [[䍃]] and [[宝]], both citing `graphemic_classification: 缶` — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 渋 (6042; 1604 characters remaining).

### 2026-08-08, iteration 900 — [[characters/渋|渋]]

**mc_id bug fixed**: stored value `3223` pointed to `瞢` at `lookup/CC/CC 3000.md` line 236 — a different character. The actual entry for 澀 (渋's traditional/kyūjitai form) is line 237, rank `3224` (an off-by-one error). **Classification nuance clarified**: Wiktionary describes 澀/渋 as a hybrid case — the phonetic-looking component 歰 is itself a 會意 compound (quadruplication of 止) that was later given a 水 semantic determiner to form 澀, and 歰 is independently documented as sharing 澀's exact OC reading (\*srɯb) and being usable as an interchangeable alternative form of it. `graphemic_classification: 歰` (already correct per vault convention of storing the sound-bearing component) was left as-is; rewrote the Notes bullet to reflect this hybrid 形声-adjacent/會意-derived etymology rather than a plain 形声 gloss. `aliases: [澀]` confirmed as the genuine traditional/kyūjitai form. **Real missing-data bug fixed**: `vietnamese` was empty; Wiktionary lists `sáp, xát` as Hán Việt readings — filled in. Cross-checked the stored `cantonese: gip3` against the citing word 苦渋's own field ("fu2 gip3, fu2 sap1"), which independently confirms gip3 as a genuine attested Cantonese reading in real compound usage — left unchanged rather than "corrected" to a more common-looking alternative. Confirmed `hanmun_edu_level: 無` correctly maps to [Korean Missing](lookup/Korean/Korean%20Missing.md) (precedent from already-perfected [[characters/哇 (char)|哇]] and others). Filled the empty `boundedness` (65, estimated — no hard formula exists in this vault). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[苦渋]] (stand-in), cross-referenced extensively above. **Chengyu**: [[少即是多]] matched a naive text grep but does not cite 渋 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 薫 (char) (6043; 1603 characters remaining).

### 2026-08-08, iteration 901 — [[characters/薫 (char)|薫]]

**mc_id bug fixed**: stored value `3356` pointed to `仄` at `lookup/CC/CC 3000.md` line 373 — a different character. The actual entry for 薰 (薫's traditional form) is line 374, rank `3357` (an off-by-one error). **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `黒` ("black" — a common, entirely unrelated character), but Wiktionary confirms the real phonetic component is `熏` (OC \*qʰun, itself an independently-existing character, not a mere variant) — corrected. **Alias contamination bug fixed, propagated fix applied to citing word too**: `aliases` listed `[薰, 熏, 燻, 爋, 𤋱]`, but Wiktionary's own "Alternative forms" section for 薰 lists only `薫` and `蘍` — 熏/燻/爋/𤋱 are separate characters in the same phonetic series (熏 being 薰's own phonetic component), not documented variants of 薰 itself. Corrected to `[薰, 蘍]`. The identical contamination (熏/燻 wrongly listed as aliases) was also found on the citing word [[薫]]'s own page and fixed there for consistency. **Real missing-data bug fixed**: `vietnamese` was stored empty; filled in with Wiktionary's sole listed reading `huân`. Filled the empty `pos` (`名詞`, precedent from the word 薫's own `pos` field). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[薫]] (stand-in), verified against its own `注音` field. False positives excluded after checking each candidate's own `characters:` field: [[勲]] and [[訓]] (both genuine Dan'a'yo homophones per the word 薫's own callouts, but neither cites 薫 itself) plus unrelated [[令和]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 遡 (6044; 1602 characters remaining).

### 2026-08-08, iteration 902 — [[characters/遡|遡]]

`mc_id: 5667` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[Radicals/Radical 162|辶]] + phonetic [[朔]], OC \*sŋraːɡ) confirmed via Wiktionary; `graphemic_classification: 朔` already correct. Both `aliases: [泝, 溯]` confirmed genuine — Wiktionary explicitly lists both as documented variant forms in the same phonetic series (溯 is the primary modern character; the original form was water-radical 㴑). **Malformed-field bug fixed**: `vietnamese` was stored as a single-item list `[ø]` — non-standard vault syntax (the `ø` "no reading" convention is normally used as a bare scalar on fields like `japanese_native`, never as a list item) — normalized to an empty field, consistent with Wiktionary showing no Vietnamese Hán Việt reading exists for this character. Also collapsed a duplicated `japanese_native` list (`さかのぼ` and `さかのぼ-る` were the same reading written twice) to the single canonical form. Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[追遡]] (stand-in) and [[遡及]], both verified against their own `注音` fields. False positive excluded after checking its own `characters:` field: [[坐位]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[塑]], sharing phonetic 朔 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 漬 (char) (6045; 1601 characters remaining).

### 2026-08-08, iteration 903 — [[characters/漬 (char)|漬]]

Clean verification: `mc_id: 3101` exact at `lookup/CC/CC 3000.md` line 110. 形声 classification (semantic [[水 (char)|水]] + phonetic [[責]], OC \*ʔsreːɡ) confirmed via Wiktionary; `graphemic_classification: 責` already correct. **Broken-link bug fixed**: the body's own etymology bullet had an empty `[[]]` wikilink where the phonetic component 責 should have been linked — filled in properly. `aliases: [渍]` confirmed as the genuine simplified form. **Vietnamese completed**: only `tứ` was stored; Wiktionary lists both `tí` and `tứ` as Hán Việt readings — added the missing `tí`. Cleaned up a garbled trailing fragment in the frequency/Levels bullets (stray leading spaces creating a malformed nested list, and a truncated "HSK______---" artifact). Rebuilt into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[漬]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 3 genuine hits found (sharing phonetic 責) — [[債]], [[績]], [[積]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 褒 (char) (6046; 1600 characters remaining).

### 2026-08-08, iteration 904 — [[characters/褒 (char)|褒]]

Clean verification: `mc_id: 1297` exact at `lookup/CC/CC 1000.md` line 310. 形声 classification (semantic [[Radicals/Radical 145|衣]] + phonetic [[保]], OC \*puː) confirmed via Wiktionary; `graphemic_classification: 保` already correct. **Wrong-radical-number bug fixed**: the body linked 衣 to `Radical 120`, but 衣 (clothing) is actually Kangxi radical 145 — corrected the link (both radical pages exist in the vault, so this was a real citation error, not a missing-page gap). `aliases: [襃]` confirmed as the genuine traditional variant. Stored `vietnamese: bao` confirmed as the sole genuine Hán Việt reading. Collapsed a duplicated `japanese_native` list (`ほ` and `ほ-める` were redundant partial/full forms of the same reading) to the single canonical form. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[褒]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[堡]], sharing phonetic 保 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 渦 (6047; 1599 characters remaining).

### 2026-08-08, iteration 905 — [[characters/渦|渦]]

**mc_id sentinel cleared, left honestly unresolved**: stored as `0` (same invalid-placeholder pattern as several earlier this session). 渦 does not appear anywhere in the vault's CC lookup files. Cleared to empty with an explicit "not found" note. 形声 classification (semantic [[水 (char)|水]] + phonetic [[咼]], OC \*kʰʷroːl) confirmed via Wiktionary; `graphemic_classification: 咼` already correct. `aliases: [涡]` confirmed as the genuine simplified form. Stored `vietnamese: oa` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`名詞`, precedent from the stand_in 渦流's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[渦流]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 5 genuine hits found (sharing phonetic 咼) — [[鍋 (char)|鍋]], [[禍]], [[窩]], [[過 (char)|過]], [[蝸]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 訃 (6048; 1598 characters remaining).

### 2026-08-08, iteration 906 — [[characters/訃|訃]]

`mc_id: 5231` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[言 (char)|言]] + phonetic [[卜]], OC \*poːɡ) confirmed via Wiktionary; `graphemic_classification: 卜` already correct. `aliases: [讣]` confirmed as the genuine simplified form. Stored `vietnamese: phó` independently cross-confirmed via the citing word [[訃告]]'s own Vietnamese field "phó cáo" (訃's phó + 告's cáo) — no Wiktionary Vietnamese section was available directly, but this compositional match provides solid corroboration. Filled the empty `pos` (`名詞`, precedent from the stand_in 訃告's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[訃告]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 魅 (6049; 1597 characters remaining).

### 2026-08-08, iteration 907 — [[characters/魅|魅]]

This page already had a well-formed Notes/Words/Chengyu skeleton — main gap was the missing 4-bullet Notes content. Clean verification: `mc_id: 3582` exact at `lookup/CC/CC 3000.md` line 607. 形声 classification (semantic [[鬼]] + phonetic [[未 (char)|未]], OC \*mɯds) confirmed via Wiktionary; `graphemic_classification: 未` already correct. Stored `vietnamese: mị` confirmed as the sole genuine Hán Việt reading. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section, preserving the already-correct Words/Chengyu content.

**Real ruby bug found and fixed on a citing word page**: [[魑魅]]'s own stored `注音` was `ㄇㄧㄜ` — missing the first syllable entirely (魑's own reading is ㄑㄧ, confirmed against `characters/魑.md`); the already-perfected chengyu [[魑魅罔両]] independently uses the correct full compound reading `ㄑㄧㄇㄧㄜㄇㄚㄫㄌ⼘ㄫ`, confirming the two-syllable form `ㄑㄧㄇㄧㄜ` is right. Corrected 魑魅's `注音` directly (same category of fix as the earlier 猿痘/便箋/薫 word-page corrections this session) and added it as a new Words entry.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added the newly-fixed [[魑魅]]; kept already-correct [[魅惑]] (stand-in). False positive excluded after checking its own `characters:` field: [[惑]]. **Chengyu**: kept already-correct [[魑魅罔両]]; [[Misc. Chengyu]] matched a naive text grep but has no `characters:` field at all — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 軸 (char) (6050; 1596 characters remaining).

### 2026-08-08, iteration 908 — [[characters/軸 (char)|軸]]

**mc_id bug fixed**: stored value `2287` pointed to `椎` at `lookup/CC/CC 2000.md` line 300 — a different character. The actual entry for 軸 is line 301, rank `2288` (an off-by-one error). Hybrid 形声/會意 classification (semantic [[車 (char)|車]] + phonetic [[由 (char)|由]], OC \*l'ɯwɢ, "the axle that passes through a cartwheel") confirmed via Wiktionary; `graphemic_classification: 由` already correct. `aliases: [轴]` confirmed as the genuine simplified form. Stored `vietnamese: trục` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[軸]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 欧 (6051; 1595 characters remaining).

### 2026-08-08, iteration 909 — [[characters/欧|欧]]

Clean verification: `mc_id: 2104` exact at `lookup/CC/CC 2000.md` line 113 (`歐`). 形声 classification (semantic [[欠 (char)|欠]] + phonetic 區/[[区]], OC \*qoː) confirmed via Wiktionary; `graphemic_classification: 区` (the shinjitai component, consistent with the vault's shinjitai main glyph and a dedicated 区.md page) already correct. `aliases: [歐]` confirmed as the genuine traditional form. Stored `vietnamese: âu` confirmed as the sole genuine Hán Việt reading. Rebuilt the malformed body (Words entries scattered before/after/mixed with floating CC-initial/final wikilinks, several unruby'd) into the proper 4-bullet `## Notes` section.

**Words cross-check** (4 total ground-truth hits, unchanged from the 4 already present but now fully verified/reformatted): added ruby to [[欧洲]] and [[欧圓]] (previously bare wikilinks); corrected the `stand_in` designation to [[欧羅巴]] (matching the frontmatter's own `stand_in` field, which had been listed alongside the others without being marked as such); kept already-correct [[欧金]] (europium abbreviation). False positives excluded after checking each candidate's own `characters:` field: [[洲]], [[諸語]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 7 genuine hits found (sharing phonetic 区/區) — [[枢 (char)|枢]], [[殴]], [[鴎 (char)|鴎]], [[駆 (char)|駆]], [[呕]], [[䝙]], [[𧦅]] — added as a new `## Derived Characters` section (previously absent), the largest phonetic family found this session.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 釜 (6052; 1594 characters remaining).

### 2026-08-08, iteration 910 — [[characters/釜|釜]]

**mc_id bug fixed**: stored value `2242` pointed to `剋` at `lookup/CC/CC 2000.md` line 255 — a different character. The actual entry for 釜 is line 256, rank `2243` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[金 (char)|金]] + phonetic [[父]], OC \*baʔ) confirmed via Wiktionary; `graphemic_classification: 父` already correct. Stored `vietnamese: phủ` confirmed as the sole genuine Hán Việt reading. Confirmed `hanmun_edu_level: 無` correctly maps to [Korean Missing](lookup/Korean/Korean%20Missing.md). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[大釜]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[大夫]] (a genuine Dan'a'yo homophone of 大釜 per that word's own callout, but doesn't cite 釜 itself). **Chengyu**: [[乾坤一擲]] matched a naive text grep but does not cite 釜 in its own `characters:` field — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing phonetic 父) — [[斧]] and [[布]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 錠 (char) (6053; 1593 characters remaining).

### 2026-08-08, iteration 911 — [[characters/錠 (char)|錠]]

`mc_id: 9038` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[金 (char)|金]] + phonetic [[定]], OC \*deːŋs) confirmed via Wiktionary; `graphemic_classification: 定` already correct. `aliases: [锭]` confirmed as the genuine simplified form. Stored `vietnamese: đĩnh` could not be independently confirmed or refuted (Wiktionary's page has no Vietnamese section, and the citing word 錠's own field is null) — left unchanged absent contrary evidence. Confirmed the empty `korean_native` is factually correct, not a gap — Wiktionary's own Korean section is incomplete/untranslated for this character. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[錠]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 稽 (6054; 1592 characters remaining).

### 2026-08-08, iteration 912 — [[characters/稽|稽]]

Clean verification: `mc_id: 787` exact at `lookup/CC/CC 0000.md` line 814. 形声 classification confirmed via Wiktionary, with a genuinely unusual etymology: the modern form's semantic side is 𥝌 ("bent, stunted tree") + 尤, phonetic [[旨]], while the original form 𩒨 instead paired the same phonetic 旨 with semantic [[頁 (char)|頁]] ("head"); `graphemic_classification: 旨` already correct — rewrote the Notes bullet to capture both forms rather than oversimplifying. All 6 stored `vietnamese` readings (`ghe, ghê, khẻ, khẽ, khể, kê`) confirmed genuine and exhaustive per Wiktionary's own list. **Unconfirmed alias flagged, not removed**: `aliases: [𥡴]` — Wiktionary's own alternative-forms list for 稽 (𥠻, 𥡞, 䭫, 䭬, 𩒨, 乩) does not include 𥡴, and a targeted second check confirmed 𥡴 doesn't appear anywhere on the page; however, absence from one source isn't strong enough contrary evidence for a rare CJK Extension B character (unlike clear cases like 熏/燻 being independently-attested distinct characters), so left unchanged rather than deleted — flagged here for future verification. Filled the empty `pos` (`事詞`, precedent from the stand_in 稽古's own body sense). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[稽古]] (stand-in). False positive excluded after checking its own `characters:` field: [[滑]]. **Chengyu**: [[臥薪嘗胆]] matched a naive text grep but does not cite 稽 in its own `characters:` field — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 唄 (char) (6055; 1591 characters remaining).

### 2026-08-08, iteration 913 — [[characters/唄 (char)|唄]]

**Real conflated-sense bug fixed, resolved using the citing word's own prior research**: the character page stored `mandarin: bei` and `english: ugh` and `pos: 感詞` — this described the completely unrelated modern colloquial Mandarin sentence-final particle 呗 (bei, "well, of course, I guess"), a purely Mandarin-internal innovation with no cross-linguistic reflex. The citing word [[唄]]'s own Notes had already caught and corrected this exact bug on the word page, documenting: "this entry previously stored `mandarin: bei` and glossed the word as 'ugh'... conflated the two unrelated senses; corrected to represent the Buddhist-chant sense the Dan'a'yo reading actually derives from" (bai/baai6/패/bái/バイ, all reflexes of MC \*braːds). Applied the same correction to the character page: `mandarin: bei→bài`, `english: ugh→[Buddhist chant, hymn]`, `pos: 感詞→名詞` (a noun, not an interjection). **Etymological detail corrected**: the body claimed the character transliterates Sanskrit "pathaka," but Wiktionary's own entry identifies the actual (if "phonologically and semantically problematic") association as Sanskrit *bhāṇaka* ("chanter, reciter") — corrected to match, consistent with the word 唄's own already-accurate phrasing. 形声 classification (semantic [[Radicals/Radical 030|口]] + phonetic [[貝]], OC \*paːds) confirmed; `graphemic_classification: 貝` already correct. `aliases: [呗]` confirmed as the genuine simplified form (shared across both senses of the character). Stored `vietnamese: bái` confirmed as the sole genuine Hán Việt reading. `mc_id: 0` cleared to empty — the body's own pre-existing note ("Not found in Classical Chinese!") already correctly explained why, so this was preserved and reformatted into the frequency bullet rather than left as a raw exclamation. Rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[唄]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[倍]] (a genuine Dan'a'yo homophone per the word 唄's own three-way homophone callout, but doesn't cite 唄 itself). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing phonetic 貝) — [[敗]] and [[狽]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 骸 (6056; 1590 characters remaining).

### 2026-08-08, iteration 914 — [[characters/骸|骸]]

Clean verification: `mc_id: 1807` exact at `lookup/CC/CC 1000.md` line 844. 形声 classification (semantic [[骨 (char)|骨]] + phonetic [[亥]], OC \*ɡɯːʔ) confirmed via Wiktionary; `graphemic_classification: 亥` already correct. Stored `vietnamese: hài` confirmed as the sole genuine Hán Việt reading. Rebuilt the malformed body (Words section placed before Notes, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added previously-missing [[骸骨]]; kept already-correct [[死骸]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 7 genuine hits found (sharing phonetic 亥) — [[劾]], [[咳]], [[該 (char)|該]], [[核 (char)|核]], [[刻]], [[垓]], [[孩]] — added as a new `## Derived Characters` section (previously absent), tying [[characters/欧|欧]]'s earlier record for the largest phonetic family found this session.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 墜 (6057; 1589 characters remaining).

### 2026-08-08, iteration 915 — [[characters/墜|墜]]

Clean verification: `mc_id: 1909` exact at `lookup/CC/CC 1000.md` line 950. 形声 classification (semantic [[土 (char)|土]] + phonetic [[隊 (char)|隊]], OC \*l'uːds) confirmed via Wiktionary; `graphemic_classification: 隊` already correct. `aliases: [坠]` confirmed as the genuine simplified form. Both stored `vietnamese: [truỵ, đụi]` readings confirmed genuine. Filled the empty `pos` (`性詞`, precedent from the stand_in 墜落's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section. Also removed a stray leftover editorial fragment ("V seems too far") found on the citing word [[墜落]]'s own page, unrelated to any real content.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[墜落]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 札 (char) (6059; 1588 characters remaining).

### 2026-08-08, iteration 916 — [[characters/札 (char)|札]]

**mc_id bug fixed**: stored value `2183` pointed to `雙` at `lookup/CC/CC 2000.md` line 192 — a different character. The actual entry for 札 is line 193, rank `2184` (an off-by-one error, the same recurring pattern found throughout this session). **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `乙` (yǐ, "second" — U+4E59, a common character), but a targeted follow-up check confirmed Wiktionary's actual cited phonetic is the visually near-identical but distinct `乚` (yǐn — U+4E5A, no vault page) — corrected. Empty `aliases` confirmed correct (札 is unchanged between traditional and simplified). `vietnamese: giạt` could not be independently confirmed (Wiktionary lists only `trát, trớt`) but also wasn't contradicted by any source — left unchanged rather than deleted, per this session's established non-destructive standard for unconfirmed-but-uncontradicted data. Filled the empty `pos` (`名詞`). Confirmed `joyo_level: "4"` (a numeric grade) correctly maps to [Jōyō - Kyōiku](lookup/Japanese/Jōyō%20-%20Kyōiku.md). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[札]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 巣 (6060; 1587 characters remaining).

### 2026-08-08, iteration 917 — [[characters/巣|巣]]

**mc_id bug fixed**: stored value `1568` pointed to `杞` at `lookup/CC/CC 1000.md` line 593 — a different character. The actual entry for 巢 (巣's traditional form) is line 594, rank `1569` (an off-by-one error). 象形 classification (a baby bird 巛 in a nest 田, atop a tree 木) confirmed via Wiktionary; `graphemic_classification: 象形` already correct. `aliases: [巢]` confirmed as the genuine traditional form. **Real missing-data bug fixed**: `vietnamese` was stored empty; Wiktionary lists `sào` as the sole Hán Việt reading — filled in. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, only 1 of 5 real Words hits) into the proper 4-bullet `## Notes` section.

**Words cross-check** (5 total ground-truth hits — this page went from 1 listed to 5 verified): added the self-referential `stand_in` [[鳥巣]] and previously-missing [[巣穴]], [[巣窟]], [[精巣]]; reformatted already-present [[蜂巣]] with proper ruby. False positives excluded after checking each candidate's own `characters:` field: [[蜂]], [[蜂蜜]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — 巣's classification is 象形 (a type string), not a phonetic component cited by other characters, so no such section applies.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 肘 (char) (6061; 1586 characters remaining).

### 2026-08-08, iteration 918 — [[characters/肘 (char)|肘]]

**mc_id bug fixed**: stored value `2577` pointed to `杵` at `lookup/CC/CC 2000.md` line 602 — a different character. The actual entry for 肘 is line 603, rank `2578` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[肉 (char)|肉]] + phonetic [[寸 (char)|寸]], originally bare 寸 before 肉 was added to distinguish it from the homograph 寸) confirmed via Wiktionary; `graphemic_classification: 寸` already correct. **Alias nuance clarified rather than removed**: `aliases: [肱]` — unlike several clear phonetic-series-contamination cases fixed earlier this session, Wiktionary here explicitly documents 肱 as "an alternative spelling" specifically in Japanese usage, even while noting it's fundamentally a distinct character with its own "upper arm" meaning — kept the alias but rewrote the Notes bullet to capture this nuance rather than presenting it as a plain interchangeable variant. Both stored `vietnamese: [khuỷu, trửu]` readings confirmed genuine. Removed a stray placeholder comment ("um, what?") left in the body instead of real content. Rebuilt into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[肘]] (stand-in), now explicitly marked as such. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[酎]], sharing phonetic 肘 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 晶 (6063; 1585 characters remaining).

### 2026-08-08, iteration 919 — [[characters/晶|晶]]

`mc_id: 5745` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 會意 classification (triplication of [[日 (char)|日]], "bright, limpid") confirmed via Wiktionary; `graphemic_classification: 會意` already correct. Stored `vietnamese: tinh` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`名詞`, precedent from the stand_in 水晶's own `pos` field). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits, unchanged): added the self-referential `stand_in` [[水晶]]; kept already-correct [[液晶]] and the "zirconium" abbreviation [[晶金]]. False positives excluded after checking each candidate's own `characters:` field: [[森林]], [[綏靖]], [[重素]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — 晶's classification is 會意 (a type string), not a phonetic component cited by other characters, so no such section applies.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 捻 (char) (6064; 1584 characters remaining).

### 2026-08-08, iteration 920 — [[characters/捻 (char)|捻]]

`mc_id: 7476` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[手 (char)|手]] + phonetic [[念]], OC \*nɯːms) confirmed via Wiktionary; `graphemic_classification: 念` already correct. **Large-scale Vietnamese contamination fixed**: 9 candidates were stored (`niêm, niết, niệm, niệp, nuốm, ném, núm, nạm, nắm`); Wiktionary confirms exactly 2 genuine Hán Việt readings — `niệm` and `niệp` — trimmed the other 7 as likely contamination, one of the largest such over-stuffed Vietnamese fields found this session. Filled the empty `pos` (`事詞` — "to twist" is verbal). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added the self-referential `stand_in` [[捻]]; kept already-correct [[絞捻]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 棺 (char) (6066; 1583 characters remaining).

### 2026-08-08, iteration 921 — [[characters/棺 (char)|棺]]

**mc_id bug fixed**: stored value `1541` pointed to `眉` at `lookup/CC/CC 1000.md` line 566 — a different character. The actual entry for 棺 is line 567, rank `1542` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[木 (char)|木]] + phonetic [[官]], OC \*koːn) confirmed via Wiktionary; `graphemic_classification: 官` already correct. Stored `vietnamese: quan` could not be independently confirmed or refuted (Wiktionary's Vietnamese section content wasn't retrievable, and the citing word 棺's own field is null) — left unchanged absent contrary evidence, consistent with this session's established non-destructive standard. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[棺]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 敷 (char) (6067; 1582 characters remaining).

### 2026-08-08, iteration 922 — [[characters/敷 (char)|敷]]

**mc_id bug fixed**: stored value `2520` pointed to `稚` at `lookup/CC/CC 2000.md` line 545 — a different character. The actual entry for 敷 is line 546, rank `2521` (an off-by-one error). **Two compounded classification bugs fixed**: (1) the body prose had the semantic/phonetic roles reversed, describing [[尃]] as semantic and [[Radicals/Radical 066|攵]] as phonetic — Wiktionary confirms the opposite: 攵 ("hand with whip; action") is semantic and 尃 (OC \*pʰa, "distribute") is phonetic; (2) `graphemic_classification` was stored as `旉`, but Wiktionary shows 旉 is not the phonetic component at all — it's actually documented as a **variant form of 敷 itself** ("This character is a variant form of 敷"), not of 尃. Corrected `graphemic_classification` to `尃` (which has its own vault page) and moved `旉` into `aliases` where it belongs as a genuine variant glyph. Both stored `vietnamese: [phô, phu]` readings confirmed genuine. **Broken-link cleanup**: the Words section cited [[座敷]] and [[敷布]] as plain unruby'd entries, but neither word page exists anywhere in the vault (`ls` confirmed both absent) — removed both dead links rather than leaving broken references. Rebuilt into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit — down from 3 listed, 2 of which were broken links to nonexistent pages): kept the self-referential `stand_in` [[敷]], now properly ruby'd. False positive excluded after checking its own `characters:` field: [[番]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing phonetic 尃) — [[博]] and [[縛]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 彰 (6068; 1581 characters remaining).

### 2026-08-08, iteration 923 — [[characters/彰|彰]]

**mc_id bug fixed**: stored value `1979` pointed to `泥` at `lookup/CC/CC 1000.md` line 1020 — a different character. The actual entry for 彰 is line 1021, rank `1980` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[Radicals/Radical 059|彡]] + phonetic [[章 (char)|章]], OC \*kjaŋ) confirmed via Wiktionary; `graphemic_classification: 章` already correct. Stored `vietnamese: chương` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`事詞`, precedent from the stand_in 彰明's own body sense). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits — this page went from 1 listed to 2 verified): added previously-missing [[表彰]]; kept already-correct [[彰明]] (stand-in), verified against its own `注音` field. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 澄 (6070; 1580 characters remaining).

### 2026-08-08, iteration 924 — [[characters/澄|澄]]

**mc_id bug fixed**: stored value `3551` pointed to `荔` at `lookup/CC/CC 3000.md` line 576 — a different character. The actual entry for 澄 is line 577, rank `3552` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[水 (char)|水]] + phonetic [[登 (char)|登]], OC \*tɯːŋ) confirmed via Wiktionary; `graphemic_classification: 登` already correct. **Vietnamese contamination fixed**: 3 candidates were stored (`chừng, trừng, xừng`); Wiktionary confirms exactly 2 genuine readings (`trừng, chừng`) — trimmed the unconfirmed `xừng`. Filled the empty `pos` (`性詞`, precedent from the stand_in 澄清's own `pos` field). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[澄清]] (stand-in). False positives excluded after checking each candidate's own `characters:` field: [[宙]], [[長]], [[垂直]], [[清澈]]. **Chengyu**: [[一目瞭然]] and [[種瓜得瓜]] both matched a naive text grep but neither cites 澄 in its own `characters:` field — correctly omitted. **Derived Characters**: 4 genuine hits found (sharing phonetic 登) — [[橙]], [[鄧]], [[灯 (char)|灯]], [[証]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 汰 (6071; 1579 characters remaining).

### 2026-08-08, iteration 925 — [[characters/汰|汰]]

`mc_id: 4497` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[水 (char)|水]] + phonetic [[太 (char)|太]], OC \*tʰaːds) confirmed via Wiktionary; `graphemic_classification: 太` already correct. **Vietnamese completed**: 5 of 6 Wiktionary-attested readings were stored (`thái, thãi, thải, thảy, thẩy`, combining Hán Việt and Nôm); added the missing sixth, `sưởi`. Filled the empty `pos` (`事詞` — "to scour, weed out" is verbal). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[陶汰]] (stand-in). False positive excluded after checking its own `characters:` field: [[漏洩]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits — the quote-tolerant grep only matched the page's own file — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 膜 (6072; 1578 characters remaining).

### 2026-08-08, iteration 926 — [[characters/膜|膜]]

**mc_id bug fixed**: stored value `3953` pointed to `隃` at `lookup/CC/CC 3000.md` line 994 — a different character. The actual entry for 膜 is line 995, rank `3954` (an off-by-one error). 形声 classification (semantic [[Radicals/Radical 130|⺼]] + phonetic [[莫 (char)|莫]], OC \*maːɡ) confirmed via Wiktionary; `graphemic_classification: 莫` already correct. **Vietnamese completed**: only `mô` was stored; Wiktionary lists both `mô` and `màng` — added the missing `màng`. Rebuilt the malformed body (raw relative-path links, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[薄膜]] (stand-in), verified against its own `注音` field. False positive excluded after checking its own `characters:` field: [[細胞]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 8 genuine hits found (sharing phonetic 莫) — [[模]], [[漠]], [[寞]], [[募]], [[幕 (char)|幕]], [[慕]], [[暮]], [[墓]] — added as a new `## Derived Characters` section (previously absent), the largest phonetic family found this session, surpassing the earlier 7-character ties on [[characters/欧|欧]] and [[characters/骸|骸]].

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 崖 (char) (6073; 1577 characters remaining).

### 2026-08-08, iteration 927 — [[characters/崖 (char)|崖]]

Clean verification: `mc_id: 2615` exact at `lookup/CC/CC 2000.md` line 644. 形声 classification (semantic [[山 (char)|山]] + phonetic [[厓]], OC \*ŋreː) confirmed via Wiktionary; `graphemic_classification: 厓` already correct. **Vietnamese contamination fixed**: 3 candidates were stored (`day, giay, nhai`); Wiktionary confirms exactly 2 genuine readings (`nhai, day`) via two independent targeted checks — trimmed the unconfirmed `giay`. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[崖]] (the page previously had no `## Words` section). False positives excluded after checking each candidate's own `characters:` field: two genuine Dan'a'yo homophones [[唉]] and [[愛]] (per the word 崖's own callout, but neither cites 崖 itself) plus unrelated [[白亜]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[涯 (char)|涯]], sharing phonetic 厓 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 帆 (char) (6074; 1576 characters remaining).

### 2026-08-08, iteration 928 — [[characters/帆 (char)|帆]]

`mc_id: 8613` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[巾]] + phonetic [[凡 (char)|凡]], OC \*bom) confirmed via Wiktionary; `graphemic_classification: 凡` already correct. **Malformed scalar-field bug fixed, propagated fix applied to citing word too**: `mandarin` was stored as the two-value string `"fān fán"` — Wiktionary confirms both readings exist, but fān is the standard noun ("sail") reading matching this page's sense, while fán is a Taiwan-specific verb reading ("to sail") documented as a distinct sense; corrected to the single scalar `fān` and added a Notes clause explaining the excluded verb reading rather than silently dropping the information. The identical malformed value was also found on the citing word [[帆]]'s own page and fixed there for consistency. All 3 stored `vietnamese` readings (`buồm, buồng, phàm`) confirmed genuine. Filled the empty `pos` (`名詞`). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[帆]]; kept already-correct [[帆船]]. **Chengyu**: added [[一帆風順]] (1 real hit, confirmed via its own `characters:` field) as a new `## Chengyu` section; [[Misc. Chengyu]] matched a naive text grep but has no `characters:` field at all — correctly omitted. **Derived Characters**: 4 genuine hits found (sharing phonetic 凡) — [[鳳]], [[風 (char)|風]], [[釩]], [[汎 (char)|汎]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 嫉 (6075; 1575 characters remaining).

### 2026-08-08, iteration 929 — [[characters/嫉|嫉]]

**mc_id bug fixed**: stored value `2687` pointed to `倨` at `lookup/CC/CC 2000.md` line 716 — a different character. The actual entry for 嫉 is line 717, rank `2688` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[女 (char)|女]] + phonetic [[疾]], OC \*zid) confirmed via Wiktionary; `graphemic_classification: 疾` already correct. Stored `vietnamese: tật` confirmed as the sole genuine Hán Việt reading. **Unverifiable historical claim removed**: the body asserted the character was "much more specific" in ancient times, meaning "a wife's jealousy of her husband" — two independent targeted Wiktionary checks found no support for this claim anywhere on the character's page, which gives only the broad general senses "to envy" and "to hate, resent" with no historical note narrowing it to spousal jealousy; removed the unsupported claim rather than presenting it as fact (the same standard applied earlier this session to the unverified 2017-Jōyō-date claim on [[characters/潟|潟]]). Filled the empty `pos` (`性詞`, precedent from the stand_in 嫉妬's own `pos` field). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[嫉妬]] (stand-in). **Chengyu**: [[波乱万丈]] matched a naive text grep but does not cite 嫉 in its own `characters:` field — correctly omitted. **Derived Characters**: no genuine hits — the quote-tolerant grep only matched the page's own file — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 斑 (6076; 1574 characters remaining).

### 2026-08-08, iteration 930 — [[characters/斑|斑]]

`mc_id: 4165` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. **Classification bug fixed**: `graphemic_classification` was stored as `會意`, with the body describing components as [[玨]] + [[文]] (two ideograph pieces) — but Wiktionary gives a single, definitive classification: 形声 (phono-semantic), semantic 文 ("pattern") + abbreviated phonetic 班 (OC \*praːn), with no mention of 玨 anywhere in the glyph-origin text. Corrected `graphemic_classification` to `班` (which has its own vault page, unlike the nonexistent 玨) and rewrote the Notes bullet accordingly. Stored `vietnamese: ban` confirmed as the sole genuine Hán Việt reading. `pos`/other frontmatter fields already correct.

**Words cross-check** (2 total ground-truth hits, unchanged): added the self-referential `stand_in` [[斑点]]; kept already-correct [[斑鳩]]. **Chengyu**: added [[豹斑改乎]] (1 real hit, confirmed via its own `characters:` field) as a new `## Chengyu` section; [[Biblical Chengyu]] matched a naive text grep but has no `characters:` field at all — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 隙 (char) (6077; 1573 characters remaining).

### 2026-08-08, iteration 931 — [[characters/隙 (char)|隙]]

**mc_id bug fixed**: stored value `1894` pointed to `阜` at `lookup/CC/CC 1000.md` line 931 — this is actually 隙's own semantic radical, not 隙 itself (an unusual variant of the recurring off-by-one pattern, where the shifted rank happened to land exactly on the character's own component). The actual entry for 隙 is line 932, rank `1895`. **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `間` (a common, unrelated character meaning "between, interval"), but Wiktionary confirms the real phonetic component is the rare `𡭴` (Taiwan variant 𡮂; no vault page for either) — corrected. Stored `vietnamese: khích` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[隙]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[喫]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 梗 (6078; 1572 characters remaining).

### 2026-08-08, iteration 932 — [[characters/梗|梗]]

**mc_id bug fixed**: stored value `3033` pointed to `藺` at `lookup/CC/CC 3000.md` line 38 — a different character. The actual entry for 梗 is line 39, rank `3034` (an off-by-one error). 形声 classification (semantic [[木 (char)|木]] + phonetic [[更 (char)|更]], OC \*kraːŋʔ) confirmed via Wiktionary; `graphemic_classification: 更` already correct. **Vietnamese contamination resolved via the citing word's own prior deep research, not a shallow source check**: 11 candidates were stored; a first-pass Wiktionary fetch appeared to support keeping all of them (its Nôm-reading table listed `gánh, ngáng, ngánh, chành` alongside the rest), but the citing word [[花梗]]'s own Notes had already done careful groupwise analysis, explicitly stating these same four are "unrelated native words with no real connection to 梗" — distinct from the genuinely-attested `cạnh`/`ngạnh` (separate "edge"/"barb" senses), `cánh` (used in 桔梗), and `cành`/`ngành`/`nhánh`/`nhành` (legitimate native/Nôm "branch" doublets). Trusted this vault's own targeted domain research over the noisier external table and trimmed to the 7 confirmed readings, removing `gánh, ngáng, ngánh, chành`. Filled the empty `pos` (`名詞`, precedent from the word 花梗's own `pos` field). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 2 listed to 3 verified): added the self-referential `stand_in` [[花梗]]; kept already-correct [[桔梗]] and [[梗塞]]. False positive excluded after checking its own `characters:` field: [[要塞]]. **Chengyu**: [[珠投猪前]] matched a naive text grep but does not cite 梗 in its own `characters:` field — correctly omitted. **Derived Characters**: 1 genuine hit found — [[硬 (char)|硬]], sharing phonetic 更 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 妖 (6079; 1571 characters remaining).

### 2026-08-08, iteration 933 — [[characters/妖|妖]]

Clean verification: `mc_id: 1354` exact at `lookup/CC/CC 1000.md` line 371. 形声 classification (semantic [[女 (char)|女]] + phonetic [[夭]], OC \*qrow) confirmed via Wiktionary; `graphemic_classification: 夭` already correct. **Vietnamese contamination fixed**: 4 candidates were stored (`yêu, èo, ẻo, ẽo`); Wiktionary confirms exactly 2 genuine readings (`yêu, èo`) — trimmed the 2 unconfirmed near-homographs (`ẻo, ẽo`), which differ only by tone mark from the confirmed `èo`, a plausible tone-diacritic corruption pattern. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 0 listed to 3 verified): added the self-referential `stand_in` [[妖怪]], [[妖物]], and [[妖精]] (the page previously had no `## Words` section). False positives excluded after checking each candidate's own `characters:` field: [[怪物]], [[火車]], [[魔女]]. **Chengyu**: [[魑魅罔両]] matched a naive text grep but does not cite 妖 in its own `characters:` field — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing phonetic 夭) — [[沃]] and [[笑 (char)|笑]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 肢 (6080; 1570 characters remaining).

### 2026-08-08, iteration 934 — [[characters/肢|肢]]

**mc_id bug fixed**: stored value `2605` pointed to `裕` at `lookup/CC/CC 2000.md` line 634 — a different character. The actual entry for 肢 is line 635, rank `2606` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[肉 (char)|肉]] + phonetic [[支 (char)|支]], OC \*kje) confirmed via Wiktionary, which also notes 肢 was "originally the same word as 支"; `graphemic_classification: 支` already correct. Stored `vietnamese: chi` could not be independently confirmed (Wiktionary's page omits a Vietnamese section) but is consistent with the expected phonetic derivation from 支 and wasn't contradicted by any source — left unchanged. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[肢体]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 肪 (char) (6081; 1569 characters remaining).

### 2026-08-08, iteration 935 — [[characters/肪 (char)|肪]]

`mc_id: 9251` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[肉 (char)|肉]] + phonetic [[方 (char)|方]], OC \*paŋ/\*baŋ) confirmed via Wiktionary; `graphemic_classification: 方` already correct. **Vietnamese completed**: only `phòng` was stored; Wiktionary lists both `phòng` and `phương` — added the missing `phương`.

**Real reading-mismatch bug found and fixed on the citing word page**: the word [[肪]] (this character's own `stand_in`, meant to directly carry the same reading) was stored with `羅馬字: pang`, `諺文: 팡`, `注音: ㄆㄚㄫ` — using a ㄆ (aspirated p-) initial, while the character's own frontmatter (and this character's `middle_chinese_initial: f`, matching 聲 非) consistently derives to `fang/빵/ㄈㄚㄫ`. Independently corroborated by [[脂肪]]'s own already-correct `注音` (`ㄐㄧㄜㄈㄚㄫ`), which uses the ㄈ-initial form for 肪. Corrected the word page's `羅馬字`/`諺文`/`注音` to match the character's own values.

**Words cross-check** (2 total ground-truth hits, unchanged): kept the now-corrected [[肪]] (stand-in) and already-correct [[脂肪]]. False positives excluded after checking each candidate's own `characters:` field: [[傍]], [[脂膏]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 10 genuine hits found (sharing phonetic 方) — [[房 (char)|房]], [[妨]], [[彷]], [[芳]], [[坊]], [[訪]], [[旁]], [[紡 (char)|紡]], [[防]], [[放]] — added as a new `## Derived Characters` section (previously absent), the largest phonetic family found this session, surpassing [[characters/膜|膜]]'s 8-character record.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 嗅 (6082; 1568 characters remaining).

### 2026-08-08, iteration 936 — [[characters/嗅|嗅]]

`mc_id: 6158` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[口 (char)|口]] + phonetic [[臭 (char)|臭]], OC \*qʰlus) confirmed via Wiktionary; `graphemic_classification: 臭` already correct. Stored `vietnamese: khứu` confirmed as the sole genuine Hán Nôm reading. Fixed [[嗅覚]]'s Words entry, which was previously an unruby'd bare wikilink — added proper ruby verified against the word's own `注音` field. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): kept the now-properly-formatted [[嗅覚]] (stand-in) and already-correct "osmium" abbreviation [[嗅金]]. False positives excluded after checking each candidate's own `characters:` field: [[五官]], [[味覚]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits — the quote-tolerant grep only matched the page's own file — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 沼 (6084; 1567 characters remaining).

### 2026-08-08, iteration 937 — [[characters/沼|沼]]

**mc_id bug fixed**: stored value `3383` pointed to `爍` at `lookup/CC/CC 3000.md` line 400 — a different character. The actual entry for 沼 is line 401, rank `3384` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[水 (char)|水]] + phonetic [[召]], OC \*djews) confirmed via Wiktionary; `graphemic_classification: 召` already correct. **Large-scale Vietnamese contamination trimmed, with a caveat**: 6 candidates were stored (`chiểu, chĩu, chẻo, trẻo, xẻo, xẽo`); Wiktionary's own Vietnamese section for 沼 lists only `trẻo` — and even flags that single reading as needing translation confirmation, i.e. this character's Vietnamese attestation is thin overall. Trimmed to the one directly-sourced reading rather than keeping the unconfirmed 5, but flagging the residual uncertainty here rather than presenting `trẻo` as fully settled.

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[沼沢]] (stand-in) and the "lutetium" abbreviation [[沼金]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 8 genuine hits found (sharing phonetic 召) — [[紹]], [[詔]], [[招]], [[劭]], [[昭 (char)|昭]], [[超 (char)|超]], [[貂]], [[邵]] — added as a new `## Derived Characters` section (previously absent), tying [[characters/膜|膜]]'s 8-character mark (both still below [[characters/肪 (char)|肪]]'s session-record 10).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 沃 (6085; 1566 characters remaining).

### 2026-08-08, iteration 938 — [[characters/沃|沃]]

**mc_id bug fixed**: stored value `1615` pointed to `忿` at `lookup/CC/CC 1000.md` line 644 — a different character. The actual entry for 沃 is line 645, rank `1616` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[水 (char)|水]] + phonetic [[夭]], OC \*qoːwɢ) confirmed via Wiktionary; `graphemic_classification: 夭` already correct. **Vietnamese contamination fixed**: 4 candidates were stored (`dạt, rày, óc, ốc`); Wiktionary confirms exactly 1 genuine reading (`óc`) — trimmed the other 3, none corroborated by the citing word 肥沃's own field (which uses a completely different native phrase, "màu mỡ," for this compound).

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[肥沃]] (stand-in) and the "iodine" abbreviation [[沃素]]. False positive excluded after checking its own `characters:` field: [[梗塞]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — [[笑 (char)|笑]] and [[妖]] share the same phonetic 夭 as siblings, but neither cites 沃 itself as a phonetic component, so no such section applies (same reasoning as the earlier [[characters/箋|箋]]/戔 case this session).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 炊 (char) (6086; 1565 characters remaining).

### 2026-08-08, iteration 939 — [[characters/炊 (char)|炊]]

**mc_id bug fixed**: stored value `2721` pointed to `歛` at `lookup/CC/CC 2000.md` line 754 — a different character. The actual entry for 炊 is line 755, rank `2722` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[火 (char)|火]] + abbreviated phonetic [[吹 (char)|吹]], OC \*kʰjol) confirmed via Wiktionary; `graphemic_classification: 吹` already correct. Stored `vietnamese: [sôi, xuy, xôi]` could not be independently confirmed or refuted (Wiktionary's page lacks a populated Vietnamese section, and the citing word 炊's own field is null) — left unchanged absent contrary evidence. Filled the empty `pos` (`事詞` — "to cook" is verbal). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[炊]] (the page previously had no `## Words` section). False positive excluded after checking its own `characters:` field: [[吹]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits — the quote-tolerant grep only matched the page's own file — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 膝 (6087; 1564 characters remaining).

### 2026-08-08, iteration 940 — [[characters/膝|膝]]

**mc_id bug fixed**: stored value `2216` pointed to `組` at `lookup/CC/CC 2000.md` line 229 — a different character. The actual entry for 膝 is line 230, rank `2217` (an off-by-one error, the same recurring pattern found throughout this session). **Sibling-vs-phonetic confusion bug fixed**: `graphemic_classification` was stored as `漆` ("lacquer"), but Wiktionary confirms 膝's actual phonetic component is the rarer, bound `桼` (OC \*sʰiɡ; no vault page) — and critically, 漆 itself is built the same way (semantic 木 + phonetic 桼, confirmed by checking [[characters/漆 (char)|漆]]'s own already-correct `graphemic_classification: 桼`), meaning 膝 and 漆 are phonetic *siblings* sharing 桼, not one being the phonetic of the other. Corrected the field to `桼`. Stored `vietnamese: tất` could not be independently confirmed or refuted (Wiktionary's Vietnamese section is incomplete, and the citing word 膝蓋's own field has no Vietnamese value at all) — left unchanged absent contrary evidence. Rebuilt the malformed body (Words section placed before Notes, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[膝蓋]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — [[characters/漆 (char)|漆]] shares the same phonetic 桼 as a sibling, but doesn't cite 膝 itself as a phonetic component, so no such section applies (same reasoning as the earlier [[characters/箋|箋]]/戔 and [[characters/沃|沃]]/夭 cases this session).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 凹 (char) (6088; 1563 characters remaining).

### 2026-08-08, iteration 941 — [[characters/凹 (char)|凹]]

`mc_id: 9390` far exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. **Classification bug fixed**: `graphemic_classification` was stored as `洼`, but Wiktionary gives a single definitive classification for 凹 — 象形 (pictogram, "a dented, sunken surface"), with no phono-semantic analysis at all. Corrected the field to `象形`. **Alias completeness fixed**: `aliases: [窪]` was already a genuine documented alternative form (per Wiktionary's Japanese-etymology note), but 洼 — the exact value that had been misplaced into `graphemic_classification` — is itself independently confirmed as the modern simplified Chinese form of 窪; added it to `aliases` where it belongs rather than discarding it outright. **Vietnamese completed**: only `ao` was stored; Wiktionary lists both `ao` (Hán Việt) and `lõm` (Nôm) — added the missing `lõm`; `ao`'s specific attestation was independently corroborated by the citing word [[凹]]'s own detailed Notes (ao địa, ao đột bất bình). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 2 listed to 3 verified): added the self-referential `stand_in` [[凹]]; reformatted already-present [[凹凸]] and [[凹版]] with proper ruby, both verified against their own `注音` fields. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — 凹's classification is 象形 (a type string), not a phonetic component cited by other characters, so no such section applies.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 融 (char) (6089; 1562 characters remaining).

### 2026-08-08, iteration 942 — [[characters/融 (char)|融]]

Clean verification: `mc_id: 1372` exact at `lookup/CC/CC 1000.md` line 389. 形声 classification (semantic 鬲 "cauldron," no vault page + phonetic [[虫]]/traditional 蟲, OC \*l'uŋ) confirmed via Wiktionary; `graphemic_classification: 蟲` already correct, matching the page's own already-correct body prose. Both `aliases: [螎, 𧖓]` confirmed as genuine documented variant forms. Stored `vietnamese: dung` confirmed as the sole genuine Hán Nôm reading. **Minor propagated fix**: the citing word [[融]]'s own `羅馬字` was stored as `yung`, missing the leading glottal-stop marker used consistently on this character's own `'yung` — corrected for consistency. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (6 total ground-truth hits — this page went from 3 listed to 6 verified): added the self-referential `stand_in` [[融]] plus previously-missing [[溶融]] and [[金融]]; kept already-correct [[融合]], [[融資]], [[融化]]. False positives excluded after checking each candidate's own `characters:` field: [[危机]], [[綏靖]]. **Chengyu**: [[結髪夫妻]], [[混然一体]], [[生机勃勃]] all matched a naive text grep but none cite 融 in their own `characters:` field — all correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 凸 (char) (6090; 1561 characters remaining).

### 2026-08-08, iteration 943 — [[characters/凸 (char)|凸]]

**mc_id sentinel cleared, left honestly unresolved**: stored as `0` (same invalid-placeholder pattern found several times this session). 凸 does not appear anywhere in the vault's CC lookup files. Cleared to empty with an explicit "not found" note. 象形 classification (a pictogram of a protruding surface) confirmed via Wiktionary; `graphemic_classification: 象形` already correct — the natural pictographic counterpart to [[characters/凹 (char)|凹]] ("concave"), perfected earlier this session. **Vietnamese completed**: only `đột` was stored; Wiktionary lists both `đột` (Hán Nôm) and `trồi` (Nôm) — added the missing `trồi`. Filled the empty `pos` (`性詞` — "convex" is adjectival).

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[凸]] (stand-in) and added previously-missing [[凹凸]]. False positives excluded after checking each candidate's own `characters:` field: [[凹]], [[凹版]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — 凸's classification is 象形 (a type string), not a phonetic component cited by other characters, so no such section applies.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 硫 (6091; 1560 characters remaining).

### 2026-08-08, iteration 944 — [[characters/硫|硫]]

**mc_id sentinel cleared, left honestly unresolved**: stored as `0` (same invalid-placeholder pattern found several times this session). 硫 does not appear anywhere in the vault's CC lookup files. Cleared to empty with an explicit "not found" note. **Sibling-vs-phonetic confusion bug fixed**: `graphemic_classification` was stored as `㐬`, but Wiktionary's own etymology text literally names "abbreviated phonetic 流" (not 㐬) as 硫's phonetic component — confirmed via a second targeted verbatim-quote check. 㐬 is instead the phonetic underlying 流 itself (confirmed by checking [[流]]'s own `graphemic_classification: 㐬`), making 硫 and 流 phonetic-family relatives one level removed, not directly sharing the same immediate component. Corrected the field to `流`. `aliases: [磂]` confirmed as the genuine documented alternative form. Stored `vietnamese: lưu` confirmed as the sole genuine Hán Việt reading. Cleaned up a stray trailing numbered-list fragment ("1. sulphur") left outside any proper section, and rebuilt the body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[硫黄]] (stand-in). False positives excluded after checking each candidate's own `characters:` field: [[墨素]], [[燐素]], [[重素]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — [[流]] shares the deeper phonetic 㐬 as a distant relative, but doesn't cite 硫 itself as a phonetic component, so no such section applies.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 匠 (6092; 1559 characters remaining).

### 2026-08-08, iteration 945 — [[characters/匠|匠]]

**mc_id bug fixed**: stored value `1679` pointed to `焚` at `lookup/CC/CC 1000.md` line 708 — a different character. The actual entry for 匠 is line 709, rank `1680` (an off-by-one error, the same recurring pattern found throughout this session). **Classification left as genuinely contested, not force-resolved**: Wiktionary documents two competing analyses — the traditional Shuowen 會意 (匚 "box" + 斤 "axe," a craftsman's toolbox) and a modern-scholarship 形声 reanalysis (Zhengzhang 2003, Baxter–Sagart 2014) treating 匚 as phonetic and 斤 as semantic — without clearly favoring either, unlike the earlier 貫/賓 cases this session where Shuowen's folk etymology was explicitly called mistaken. Kept `graphemic_classification: 會意` (already stored) and documented both theories in the Notes bullet rather than unilaterally picking a side. Stored `vietnamese: tượng` confirmed as the sole genuine Hán Việt reading. **Self-caught ruby error**: initially wrote the Words entry for [[工匠]] using 匠's own character reading (ㄑ⺢ㄫ) instead of the actual two-syllable compound reading (ㄍㄛㄫㄐㄚㄫ) — caught by cross-checking the word's own `注音` field before finalizing. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[工匠]] (stand-in), corrected as above. False positive excluded after checking its own `characters:` field: [[工場]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 衷 (6093; 1558 characters remaining).

### 2026-08-08, iteration 946 — [[characters/衷|衷]]

**mc_id bug fixed**: stored value `2818` pointed to `啼` at `lookup/CC/CC 2000.md` line 855 — a different character. The actual entry for 衷 is line 856, rank `2819` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[衣]] + phonetic [[中 (char)|中]], OC \*tuŋ/\*tuŋs) confirmed via Wiktionary; `graphemic_classification: 中` already correct. Stored `vietnamese: trung` confirmed as the sole genuine Hán Việt reading. Filled the empty `pos` (`名詞`). Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (2 total ground-truth hits, unchanged): kept already-correct [[衷情]] (stand-in) and [[折衷]], both verified against their own `注音` fields. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 頒 (6094; 1557 characters remaining).

### 2026-08-08, iteration 947 — [[characters/頒|頒]]

**mc_id bug fixed**: stored value `2788` pointed to `滇` at `lookup/CC/CC 2000.md` line 821 — a different character. The actual entry for 頒 is line 822, rank `2789` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[頁 (char)|頁]] + phonetic [[分 (char)|分]]) confirmed via Wiktionary; `graphemic_classification: 分` already correct. `aliases: [颁]` confirmed as the genuine simplified form. Stored `vietnamese: ban` confirmed as the sole genuine Hán Việt reading. **Typo bug fixed**: `english` had a run-on entry `"bestow publish"` missing a list separator — split into proper separate `bestow` and `publish` items. Filled the empty `pos` (`事詞`). Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[頒布]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 8 genuine hits found (sharing phonetic 分) — [[扮 (char)|扮]], [[盆 (char)|盆]], [[芬]], [[粉 (char)|粉]], [[雰]], [[盼]], [[貧]], [[紛 (char)|紛]] — added as a new `## Derived Characters` section (previously absent), tying [[characters/膜|膜]] and [[characters/沼|沼]]'s 8-character mark (still below [[characters/肪 (char)|肪]]'s session-record 10).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 頬 (char) (6095; 1556 characters remaining).

### 2026-08-08, iteration 948 — [[characters/頬 (char)|頬]]

Clean verification: `mc_id: 2879` exact at `lookup/CC/CC 2000.md` line 916 (`頰`). 形声 classification (semantic [[頁 (char)|頁]] + phonetic 夾/[[夹]], OC \*kreːb) confirmed via Wiktionary; `graphemic_classification: 夹` (the shinjitai component, consistent with the vault's shinjitai main glyph and a dedicated 夹.md page) already correct. Both `aliases: [頰, 颊]` confirmed genuine (traditional and simplified forms). Stored `vietnamese: giáp` confirmed as the sole genuine Hán Việt reading. Collapsed a duplicated `japanese_native` list (`ほお` written twice) to the single canonical form. **Real data-corruption bug found and fixed on the citing word page**: [[頬]]'s own `korean` field was the literal string `"null"` (not an actual empty value, but the word "null" itself) and its `諺文` (`겊`) diverged from the character's own `諺文` (`겁`) despite representing the identical reading — corrected both to match the character's own frontmatter. Deduplicated the malformed body (two separate `## Notes` headings, the second containing entirely broken empty `[[]]` wikilinks and an incomplete OC placeholder) into a single proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[頬]] (stand-in), corrected as above. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no hits — correctly omitted.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 塁 (6097; 1555 characters remaining).

### 2026-08-08, iteration 949 — [[characters/塁|塁]]

**mc_id bug fixed**: stored value `2013` pointed to `矛` at `lookup/CC/CC 2000.md` line 18 — a different character. The actual entry for 壘 (塁's traditional form) is line 19, rank `2014` (an off-by-one error, the same recurring pattern found throughout this session). **Glyph-confusion bug fixed**: `graphemic_classification` was stored as `雷` (a common, visually similar character, "thunder"), but Wiktionary confirms the real phonetic component is `畾` (three 田 stacked, OC \*ruːl; no vault page) — corrected. `aliases: [壘]` confirmed as the genuine traditional form. **Vietnamese completed**: only `luỹ` was stored; Wiktionary lists both `luỹ` and `lũy` as alternate diacritic-placement spellings of the same reading — added the missing `lũy`. Rebuilt the malformed body (floating unformatted CC-initial/final wikilinks, no Words section) into the proper 4-bullet `## Notes` section.

**Words cross-check** (3 total ground-truth hits — this page went from 0 listed to 3 verified): added the self-referential `stand_in` [[壁塁]] plus previously-missing [[堡塁]] and [[本塁打]] (the page previously had no `## Words` section). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 1 genuine hit found — [[累]], sharing the corrected phonetic 畾 — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 峡 (6098; 1554 characters remaining).

### 2026-08-08, iteration 950 — [[characters/峡|峡]]

**Real broken stand_in bug fixed**: `stand_in` was stored as `名専字` — a string with no corresponding word file anywhere in the vault (`ls` confirmed absent) and no coherent meaning as a real compound. Searched for words actually citing 峡 and found the genuine candidate: [[海峡]] ("strait, channel"), whose own reading (ㄏㄚㄧㄏㄚㄆ) correctly incorporates 峡's own ㄏㄚㄆ. Corrected `stand_in` to `海峡`. `mc_id` exceeds/falls outside the vault's verifiable CC lookup range (峽 not found in `CC 0000`–`CC 3000`) — left empty with an explicit note rather than guessed. 形声 classification (semantic [[山 (char)|山]] + phonetic [[夹]]/traditional 夾, OC \*ɡreːb) confirmed via Wiktionary; `graphemic_classification: 夹` already correct. `aliases: [峽]` confirmed as the genuine traditional form. **Vietnamese contamination fixed**: stored `[hiệp, kẽm]` — `kẽm` (meaning "zinc," an unrelated word) is not attested anywhere for this character and was removed; added the two Wiktionary-confirmed readings that were missing, `hệp` and `siệp`. Rebuilt the malformed body into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit): added the corrected `stand_in` [[海峡]] (the page previously had no real `## Words` section, just the broken stand_in reference). False positive excluded after checking its own `characters:` field: [[谷]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 5 genuine hits found (sharing phonetic 夾/夹) — [[狭]], [[鋏 (char)|鋏]], [[頬 (char)|頬]], [[侠]], [[挟 (char)|挟]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 挟 (char) (6099; 1553 characters remaining).

### 2026-08-08, iteration 951 — [[characters/挟 (char)|挟]]

Clean verification: `mc_id: 1492` exact at `lookup/CC/CC 1000.md` line 513 (`挾`). 形声 classification (semantic [[手 (char)|手]] + phonetic [[夹]]/traditional 夾, OC \*ɡeːb) confirmed via Wiktionary; `graphemic_classification: 夹` already correct. `aliases: [挾]` confirmed as the genuine traditional form. **Vietnamese completed**: only `giáp, hiệp` were stored; Wiktionary lists 4 readings total (`xáp, hiệp, giáp, rơi`) — added the 2 missing (`xáp, rơi`). **Same "null"-string bug found again, on the citing word page**: [[挟]]'s own `korean` field was the literal string `"null"` — the identical data-corruption pattern just fixed on [[characters/頬 (char)|頬]]'s citing word last cycle — corrected to `협` matching the character's own `korean` field. Filled the previously-missing Words section.

**Words cross-check** (3 total ground-truth hits — this page went from 2 listed to 3 verified): added the self-referential `stand_in` [[挟]] (corrected as above); kept already-correct [[挟攻]] and [[挟撃]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: no genuine hits — [[characters/峡|峡]], [[characters/頬 (char)|頬]], and others share the same phonetic 夾/夹 as siblings, but none cite 挟 itself as a phonetic component.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 掘 (char) (6100; 1552 characters remaining).

### 2026-08-08, iteration 952 — [[characters/掘 (char)|掘]]

**mc_id bug fixed**: stored value `2149` pointed to `咨` at `lookup/CC/CC 2000.md` line 158 — a different character. The actual entry for 掘 is line 159, rank `2150` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[手 (char)|手]] + phonetic [[屈 (char)|屈]], OC \*ɡlud/\*ɡlod) confirmed via Wiktionary; `graphemic_classification: 屈` already correct. **Large Vietnamese list verified genuine, not contamination**: all 7 stored candidates (`oặt, quát, quạt, quất, quật, quặt, quịt`) exactly match Wiktionary's own 7-reading list — a case of legitimately extensive Nôm variation, same pattern as [[characters/梗|梗]] earlier this session, confirming a large Vietnamese field isn't automatically suspect. Filled the previously-missing Words section.

**Words cross-check** (1 total ground-truth hit): added the self-referential `stand_in` [[掘]] (the page previously had no `## Words` section, only a `## Chengyu` section). False positive excluded after checking its own `characters:` field: [[墓穴]]. **Chengyu**: kept already-correct [[臨渇掘井]], verified against its own `注音` field; [[有備無患]] matched a naive text grep but does not cite 掘 in its own `characters:` field — correctly omitted. **Derived Characters**: 2 genuine hits found (sharing phonetic 屈) — [[堀]] and [[窟 (char)|窟]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 堪 (char) (6101; 1551 characters remaining).

### 2026-08-08, iteration 953 — [[characters/堪 (char)|堪]]

**mc_id bug fixed**: stored value `1574` pointed to `懸` at `lookup/CC/CC 1000.md` line 599 — a different character. The actual entry for 堪 is line 600, rank `1575` (an off-by-one error, the same recurring pattern found throughout this session). Hybrid 形声/會意 classification (semantic [[土 (char)|土]] + phonetic [[甚]], OC \*kʰluːm — "originally a heavy mountain/earthen protrusion," later "to endure") confirmed via Wiktionary; `graphemic_classification: 甚` already correct. **Vietnamese contamination resolved via the citing word's own prior deep research, overriding a shallower Wiktionary read**: a first-pass Wiktionary fetch appeared to support all 3 stored candidates (`kham, khom, khăm`) as "Hán Việt/Nôm readings," but the citing word [[堪]]'s own Notes had already done specific research identifying `khom` and `khăm` as unrelated native Vietnamese words (khom = "to stoop, bend"; khăm = "a mean trick") — "not Sino-Vietnamese doublets" of 堪 at all, merely coincidental near-homophones. Trusted this vault's own targeted research over the noisier external listing and trimmed to the single confirmed reading `kham`, consistent with the same reasoning pattern used on [[characters/梗|梗]] earlier this session.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[堪]] (stand-in), whose own body note was the very source that resolved this iteration's central Vietnamese question. False positive excluded after checking its own `characters:` field: [[勘 (char)|勘]] (a genuine Dan'a'yo homophone per that word's own three-way callout, but doesn't cite 堪 itself). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 3 genuine hits found (sharing phonetic 甚) — [[斟]], [[勘 (char)|勘]], [[湛]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 粋 (6102; 1550 characters remaining).

### 2026-08-08, iteration 954 — [[characters/粋|粋]]

**mc_id bug fixed**: stored value `3152` pointed to `貺` at `lookup/CC/CC 3000.md` line 161 — a different character. The actual entry for 粹 (粋's traditional form) is line 162, rank `3153` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[米 (char)|米]] + phonetic [[卒]], OC \*suds) confirmed via Wiktionary; `graphemic_classification: 卒` already correct. `aliases: [粹]` confirmed as the genuine traditional form. Confirmed the empty `vietnamese` field is a genuine data gap, not a bug — neither Wiktionary nor the citing word [[純粋]]'s own field has any Vietnamese value for this character, so left empty rather than fabricated. Filled the empty `boundedness` (65, estimated — no hard formula exists in this vault).

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[純粋]] (stand-in). **Chengyu**: [[焚琴煮鶴]] matched a naive text grep but does not cite 粋 in its own `characters:` field — correctly omitted. **Derived Characters**: 3 genuine hits found (sharing phonetic 卒) — [[酔 (char)|酔]], [[砕 (char)|砕]], [[翠]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 爽 (6103; 1549 characters remaining).

### 2026-08-08, iteration 955 — [[characters/爽|爽]]

**mc_id bug fixed**: stored value `2055` pointed to `鹹` at `lookup/CC/CC 2000.md` line 60 — a different character. The actual entry for 爽 is line 61, rank `2056` (an off-by-one error, the same recurring pattern found throughout this session). 會意 classification ([[大 (char)|大]] "big" + 㸚, no vault page — "bright") confirmed via Wiktionary; `graphemic_classification: 會意` already correct. All 4 stored `vietnamese` readings (`sượng, sảng, sửng, sững`) confirmed genuine and exhaustive per Wiktionary's own list. Rebuilt the malformed body (Words section placed before Notes, floating unformatted CC-initial/final wikilinks) into the proper 4-bullet `## Notes` section.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[爽快]] (stand-in). **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — 爽's classification is 會意 (a type string), not a phonetic component cited by other characters, so no such section applies.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 紡 (char) (6104; 1548 characters remaining).

### 2026-08-08, iteration 956 — [[characters/紡 (char)|紡]]

**mc_id bug fixed**: stored value `3377` pointed to `恙` at `lookup/CC/CC 3000.md` line 394 — a different character. The actual entry for 紡 is line 395, rank `3378` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[糸]] + phonetic [[方 (char)|方]], OC \*pʰaŋʔ) confirmed via Wiktionary; `graphemic_classification: 方` already correct. All 3 stored `vietnamese` readings (`phưởng, vướng, vưởng`) confirmed genuine and exhaustive per Wiktionary's own list.

**Real reading-mismatch bug found and fixed on the citing word page, the same pattern as [[characters/肪 (char)|肪]] two cycles ago**: the word [[紡]] (this character's own `stand_in`) was stored with `羅馬字: pang`, `諺文: 팡`, `注音: ㄆㄚㄫ` — a ㄆ (aspirated p-) initial, while the character's own frontmatter (with `middle_chinese_initial: fʰ`, matching 聲 敷) consistently derives to `fang/빵/ㄈㄚㄫ`. Independently corroborated by [[紡錘]]'s own already-correct `注音` (`ㄈㄚㄫㄑㄨㄧ`), which uses the ㄈ-initial form. Corrected the word page's `羅馬字`/`諺文`/`注音` to match the character's own values.

**Words cross-check** (2 total ground-truth hits, unchanged): kept the now-corrected [[紡]] (stand-in) and already-correct [[紡錘]]. False positive excluded after checking its own `characters:` field: [[傍]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: none applicable — [[characters/肪 (char)|肪]], [[characters/防|防]], [[characters/放|放]], and others share the same phonetic 方 as siblings, but none cite 紡 itself as a phonetic component.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 紳 (6105; 1547 characters remaining).

### 2026-08-08, iteration 957 — [[characters/紳|紳]]

**mc_id bug fixed**: stored value `3051` pointed to `踈` at `lookup/CC/CC 3000.md` line 56 — a different character. The actual entry for 紳 is line 57, rank `3052` (an off-by-one error, the same recurring pattern found throughout this session — and coincidentally adjacent to [[characters/窒|窒]]'s own rank 3053, fixed earlier this session). 形声 classification (semantic [[糸]] + phonetic [[申 (char)|申]], OC \*hlin) confirmed via Wiktionary; `graphemic_classification: 申` already correct. Both stored `vietnamese: [thang, thân]` readings confirmed genuine and exhaustive per Wiktionary's own list. Confirmed the empty `korean_native` is factually correct, not a gap — Wiktionary explicitly flags this entry as needing translation, with no eumhun gloss provided. Filled the empty `pos` (`名詞`).

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[紳士]] (stand-in). False positive excluded after checking its own `characters:` field: [[士]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 5 genuine hits found (sharing phonetic 申) — [[坤]], [[神 (char)|神]], [[伸]], [[呻]], [[電]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 締 (char) (6107; 1546 characters remaining).

### 2026-08-08, iteration 958 — [[characters/締 (char)|締]]

`mc_id: 4937` exceeds the vault's verifiable CC lookup range (ranks 1–4000) — treated as legitimate long-tail data per standing policy. 形声 classification (semantic [[糸]] + phonetic [[帝 (char)|帝]], OC \*teːɡs) confirmed via Wiktionary; `graphemic_classification: 帝` already correct. `aliases: [缔]` confirmed as the genuine simplified form. Stored `vietnamese: [rế, đế, đề]` could not be independently confirmed or refuted (Wiktionary's page has no Vietnamese section, and the citing word 締's own field is null) — left unchanged absent contrary evidence. Filled the empty `pos` (`事詞`).

**Words cross-check** (2 total ground-truth hits — this page went from 0 listed to 2 verified): added the self-referential `stand_in` [[締]] and [[締切]] (the page previously had no `## Words` section). False positives excluded after checking each candidate's own `characters:` field: [[剃]], [[大麻]]. **Chengyu**: no hits — correctly omitted. **Derived Characters**: 7 genuine hits found (sharing phonetic 帝) — [[蹄 (char)|蹄]], [[嫡 (char)|嫡]], [[啼]], [[滴 (char)|滴]], [[摘 (char)|摘]], [[諦 (char)|諦]], [[敵]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 呈 (char) (6108; 1545 characters remaining).

### 2026-08-08, iteration 959 — [[characters/呈 (char)|呈]]

**mc_id bug fixed**: stored value `3622` was a straight duplicate of [[characters/腕 (char)|腕]]'s own rank (verified earlier this session at `CC 3000.md` line 651), not 呈's actual entry, one line down at line 652, rank `3623`. **Sibling-vs-phonetic confusion bug fixed**: `graphemic_classification` was stored as `廷`, but Wiktionary confirms 呈's actual phonetic is the rare `𡈼` — and critically, 廷 itself is built the same way (semantic 廴 + phonetic 𡈼), meaning 呈 and 廷 are phonetic *siblings*, not one being the phonetic of the other (the same category of bug as the earlier [[characters/膝|膝]]/漆 and [[characters/硫|硫]]/流 cases this session). Corrected the field to `𡈼`, which has its own vault page. **Note**: [[characters/廷|廷]]'s own `graphemic_classification` is currently self-referentially stored as `廷` — an apparent bug on that page too, flagged here for its own future turn rather than fixed out-of-scope.

**Vietnamese carefully reconciled from two sources**: the citing word [[呈]]'s own deep-dive Notes had already researched this character's Vietnamese field in detail, confirming `chiềng, chường, rềnh, triềng, trành, xình` as genuinely attested (though colloquial/reduplicative rather than formal Hán Việt) while explicitly flagging `chiệng` as "a tone-mark corruption of chiềng... dropped as noise." Removed `chiệng` per that finding. Independently, Wiktionary's own Nôm list additionally confirmed 3 further genuine readings not yet on the character page (`chành, dành, rình`) — added them, since the word's research (which predates these) never flagged them as invalid. Net effect: 10 readings total, down from the original 8 minus the confirmed-corrupt `chiệng` plus 3 confirmed additions.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[呈]] (stand-in), whose own Notes were central to resolving the Vietnamese question above. False positive excluded after checking its own `characters:` field: [[鼎]] (a genuine Dan'a'yo homophone per that word's own callout, but doesn't cite 呈 itself). **Chengyu**: added [[銀盤呈首]] (1 real hit, confirmed via its own `characters:` field) as a new `## Chengyu` section; [[万物生長]] matched a naive text grep but does not cite 呈 in its own `characters:` field — correctly omitted. **Derived Characters**: none applicable — [[聴 (char)|聴]] shares the same phonetic 𡈼 as a sibling, but doesn't cite 呈 itself as a phonetic component.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 腎 (6109; 1544 characters remaining).

### 2026-08-08, iteration 960 — [[characters/腎|腎]]

**mc_id bug fixed**: stored value `1437` pointed to `熊` at `lookup/CC/CC 1000.md` line 458 — a different character. The actual entry for 腎 is line 459, rank `1438` (an off-by-one error, the same recurring pattern found throughout this session). 形声 classification (semantic [[肉 (char)|肉]] + phonetic 臤, OC \*ɡiːn, no vault page) confirmed via Wiktionary; `graphemic_classification: 臤` already correct. `aliases: [肾]` confirmed as the genuine simplified form. **Vietnamese contamination fixed**: stored `[thận, trớn]`; Wiktionary confirms only `thận` — `trớn` (meaning "momentum, impetus," an unrelated native word) was not corroborated anywhere and was removed.

**Words cross-check** (1 total ground-truth hit, unchanged): kept already-correct [[腎臓]] (stand-in). False positives excluded after checking each candidate's own `characters:` field: [[五官]], [[伸長]] (a genuine Dan'a'yo homophone of 腎臓 per that word's own callout, but doesn't cite 腎 itself). **Chengyu**: no hits — correctly omitted. **Derived Characters**: 3 genuine hits found (sharing phonetic 臤) — [[堅]], [[賢]], [[緊]] — added as a new `## Derived Characters` section (previously absent).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 舶 (6110; 1544 characters remaining).

### 2026-08-08, iteration 961 — [[characters/舶|舶]]

`mc_id: 0` confirmed genuine (舶 not found anywhere in ranks 1–4000 across `CC 0000`–`CC 3000`) — left as-is with the existing explicit note. 形声 classification confirmed via Wiktionary (semantic [[Radical 137|舟]] "boat" + phonetic [[白 (char)|白]], OC \*braːɡ); fixed the phonetic-component link, which was a plain markdown link `[白 (char)](白 (char).md)` instead of the standard wikilink `[[白 (char)|白]]` even though the target page exists. **Vietnamese fixed**: Wiktionary lists both `bạc` and `bách` as genuine Hán Nôm readings for 舶; only `bách` was stored — added the missing `bạc`. **English gloss fixed**: stored `oceanliner` (implies a specific passenger-liner type of ship) was replaced with Wiktionary's actual gloss `oceangoing ship`, matching the existing Notes bullet's own wording ("an oceangoing vessel").

**Missing `## Words` section added**: the file had no Words section at all despite `stand_in: 船舶` being set — added <ruby>[[船舶]]<rt>ㄙ⼔ㄇㄅㄚㄎ</rt></ruby> "boat, ship" (stand-in for 舶), the only word citing 舶 (confirmed via grep). Cross-checked the `#cranberry` tag against [[船舶]]'s own Notes, which already documents the transitivity reasoning (shared `korean_native` 배, 舶 has no independent life elsewhere, 船's extra productivity doesn't branch into a different sense) — left unchanged, still valid. **Chengyu**: no hits. **Derived Characters**: no hits (no other character cites 舶 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 繭 (6111; 1543 characters remaining).

### 2026-08-08, iteration 962 — [[characters/繭 (char)|繭]]

This page was essentially unbuilt — a single-hash `# Notes` heading with two bare wikilinks and no SKIP/stroke/rank/Words content at all. Built out the full standard structure. **mc_id off-by-one fixed**: stored `2886` pointed one entry early in `lookup/CC/CC 2000.md`; the actual line for 繭 is rank `2887`. 會意 classification confirmed via Wiktionary: [[糸]] ("silk") + [[虫]] ("insect") + an abbreviated, pageless 黹 ("needlework") — depicting a cocoon unwound into silk thread; `graphemic_classification: 會意` already correct (no phonetic to point at). **Vietnamese fixed**: Wiktionary lists three genuine Hán Việt/Nôm readings — `kiển`, `kiền`, `kén` — only two were stored; added the missing `kiển` (also referenced independently in [[繭]]'s own word-page Notes, which discusses it alongside kén).

Fixed the malformed `# Notes` heading to `## Notes`. Added the entirely-missing SKIP/stroke bullet, CC-rank/initials/finals bullet, and Grade/HSK/Jōyō/Korean bullet — all lookup targets verified to exist. Added the entirely-missing `## Words` section: <ruby>[[繭]]<rt>ㄍ⼶ㄇ</rt></ruby> "cocoon" (stand-in for 繭) — the only word citing this character, matching `stand_in` and the `#hapax` tag. **Chengyu**: no hits. **Derived Characters**: no hits (繭 is 會意, not a phonetic donor to any other character) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 茎 (6112; 1542 characters remaining).

### 2026-08-08, iteration 963 — [[characters/茎 (char)|茎]]

`mc_id: 2153` confirmed correct (matches 莖's actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 140|艸]] ("grass, plant") + phonetic [[巠]] (OC \*keːŋ, page exists); `graphemic_classification: 巠` already correct. Vietnamese `[hành, kinh]` confirmed complete against Wiktionary — no change. The stored ㄎ initial outcome (vs. the expected ㄏ for 匣-initial characters) is a documented minority case: the `聲 匣` lookup page already names 茎 as one of only three ㄎ exceptions (alongside 劦/雇), so no fix needed there — just cited it explicitly in the Notes per the CC-initials-minority-outcome standing rule. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** (no SKIP/stroke/rank/lookup bullets) — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added both genuine citing words (verified via grep): <ruby>[[茎]]<rt>ㄎㄧㄫ</rt></ruby> (stand-in) and <ruby>[[陰茎]]<rt>ㄧㄇㄎㄧㄫ</rt></ruby> "penis". **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 茎/莖 as its own phonetic) — correctly has no section.

**Fixed corrupted data on the citing word page** [[茎]] (words/茎.md): `vietnamese: null` and `korean: "null"` were literal string placeholders rather than real data or a proper empty/ø marker — corrected to `hành` (the genuine Hán Việt reading, corroborated by the real compound 陰莖/âm hành "penis") and `경` respectively; also filled its empty `pos` field to `名詞`. Left [[陰茎]]'s own empty `vietnamese` field alone (genuinely unresearched, not corrupted) since deep-filling citing words' own content is out of scope for the character-perfecting pass.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 艇 (6113; 1541 characters remaining).

### 2026-08-08, iteration 964 — [[characters/艇 (char)|艇]]

`mc_id: 6475` confirmed as legitimate long-tail data (艇 not found anywhere in the verifiable `CC 0000`–`CC 3000` range, ranks 1–4000) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[Radical 137|舟]] ("boat") + phonetic [[廷]] (OC \*l'eːŋ, page exists); `graphemic_classification: 廷` already correct. Vietnamese `[đĩnh]` confirmed complete against Wiktionary — no change. (Note: 廷's own page still carries the self-referential `graphemic_classification: 廷` bug flagged during the 呈 iteration — out of scope here since 廷 is a separate, not-yet-due character.) Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added the sole genuine citing word (verified via grep): <ruby>[[艇]]<rt>ㄉㄝㄫ</rt></ruby> "dinghy, rowboat, boat" (stand-in for 艇). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 艇 as its own phonetic) — correctly has no section.

**Fixed corrupted data on the citing word page** [[艇]] (words/艇.md): `vietnamese: null` was a literal string placeholder — corrected to `đĩnh` (the genuine Hán Việt reading); also filled its empty `pos` field to `名詞`. This is the same `vietnamese: null`/missing-`pos` corruption pattern just fixed on [[茎]]'s word page last iteration — worth watching for on upcoming characters too.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 賄 (6114; 1540 characters remaining).

### 2026-08-08, iteration 965 — [[characters/賄|賄]]

**mc_id off-by-one fixed**: stored `2319` → actual rank in `CC 2000.md` is `2320`. 形声 classification confirmed via Wiktionary: semantic [[貝]] ("cowry, money") + phonetic [[有 (char)|有]]; `graphemic_classification: 有` already correct. Vietnamese `[hối]` confirmed complete against Wiktionary — no change.

**Broken `stand_in` fixed**: stored `財物` does not exist anywhere in the vault as a word file, and no reference to it exists outside this one field — the same "phantom stand-in" bug pattern found earlier on 峡 (`名専字`). Grepped for genuine citing words: the only real hit is [[賄賂]] ("bribe," characters: 賄+賂) — repointed `stand_in` to `賄賂`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[賄賂]]<rt>ㄏㄛㄧㄌㄛ</rt></ruby> "bribe" (stand-in for 賄); the other grep hit, [[回路]], was confirmed a false positive (a homophone note only, doesn't cite 賄 in its `characters:` field). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 賄 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 賂 (6115; 1539 characters remaining).

### 2026-08-08, iteration 966 — [[characters/賂|賂]]

**mc_id off-by-one fixed**: stored `1404` → actual rank in `CC 1000.md` is `1405`. 形声 classification confirmed via Wiktionary: semantic [[貝]] ("cowry, money") + phonetic [[各 (char)|各]]; `graphemic_classification: 各` already correct. Vietnamese `[lộ]` confirmed complete against Wiktionary — no change. Filled the empty `pos` field to `事詞`, matching sibling character [[賄]]'s own pos (both halves of the same compound).

**Broken `stand_in` fixed**: stored `饋遺` does not exist anywhere in the vault — another phantom stand-in, same pattern as [[賄]] and 峡 before it. The genuine citing word, confirmed via grep, is [[賄賂]] ("bribe") — the same compound already serving as [[賄]]'s own stand_in from last iteration. Verified this dual-stand_in pattern is an established, common convention in this vault (e.g. 飢餓, 謹慎, 鴛鴦, 責任 — dozens of compound pairs where neither character has independent life outside the one shared word) — not an anomaly requiring further scrutiny.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[賄賂]]<rt>ㄏㄛㄧㄌㄛ</rt></ruby> "bribe" (stand-in for 賂). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 賂 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 賭 (6116; 1538 characters remaining).

### 2026-08-08, iteration 967 — [[characters/賭|賭]]

`mc_id: 7691` confirmed as legitimate long-tail data (賭 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[貝]] ("cowry, money") + phonetic [[者 (char)|者]]; `graphemic_classification: 者` already correct. Vietnamese `[đổ]` confirmed complete against Wiktionary — no change. `stand_in: 賭博` confirmed genuine (the word file exists and correctly cites 賭). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[賭博]]<rt>ㄉㄛㄅㄚㄎ</rt></ruby> "gamble" (stand-in for 賭). **Chengyu**: one grep hit, [[乾坤一擲]], confirmed a false positive — 賭 appears only inside a Japanese example sentence in that page's body, not in its `characters:` field — correctly excluded. **Derived Characters**: no hits (nothing cites 賭 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 踪 (6117; 1537 characters remaining).

### 2026-08-08, iteration 968 — [[characters/踪|踪]]

**mc_id off-by-one fixed**: stored `3739` → actual rank in `CC 3000.md` is `3740`. **Glyph/sibling-confusion bug found and fixed**: stored `graphemic_classification: 宗` looked plausible (宗 is zōng, matching 踪's modern Mandarin reading exactly), but Wiktionary's actual etymology names the phonetic as 從/従 (OC \*zloŋ, "follow") — confirmed independently by Middle Chinese finals: 踪's own stored final `ɨoŋ` matches [[従 (char)|從]]'s final `ɨoŋ` exactly, while 宗's own final is `uoŋ`, a mismatch. Corrected to `從` (displayed via the vault's [[従 (char)|從]] page, following the same convention already used on [[縦 (char)|縦]]'s own citation of this same phonetic).

**Vietnamese contamination fixed**: stored `[tung, tông]` — Wiktionary confirms only `tung` as 蹤/踪's genuine Hán Việt/Nôm reading; `tông` is not attested for this character at all, but is one of 宗's own four stored readings (`tong, tung, tôn, tông`) — almost certainly contamination introduced alongside the wrong-donor `graphemic_classification` bug above. Trimmed to just `tung`. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, including an explanatory clause on the 宗-vs-從 phonetic confusion. The `## Words` section already existed with the correct entry ([[踪影]]) but was missing the "(stand-in for 踪)" suffix — added. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 踪 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 轄 (6118; 1536 characters remaining).

### 2026-08-08, iteration 969 — [[characters/轄 (char)|轄]]

`mc_id: 4541` confirmed as legitimate long-tail data (轄 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[車 (char)|車]] ("cart") + phonetic [[害]]; `graphemic_classification: 害` already correct. **Vietnamese incomplete, fixed**: stored `[hạt, hợt]`; Wiktionary lists five genuine Hán Nôm readings — added the missing `hặt`, `hách`, `hoách`. Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[轄]]<rt>ㄏㄚㄊ</rt></ruby> (stand-in for itself). **Chengyu**: 2 grep hits, 1 genuine — added <ruby>[[轄魚鳥牲]]<rt>ㄏㄚㄊ·⼄ㄑㄛㄨㄙㄚㄫ</rt></ruby> "Rule fish, birds, life" as a new `## Chengyu` section; [[欲夫治汝]] was a false positive (轄 appears only inside a quoted Bible verse in its body, not in its `characters:` field). **Derived Characters**: no hits — correctly has no section.

**Fixed corrupted data on the citing word page** [[轄]] (words/轄.md): `vietnamese: null` was a literal string placeholder — corrected to `hạt` (the first-listed/primary Hán Việt reading); also filled its empty `pos` field to `事詞`. Same `vietnamese: null`/missing-`pos` corruption pattern as [[茎]] and [[艇]] two iterations ago — now confirmed as a recurring, not isolated, data-quality issue worth flagging on every remaining character.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 遜 (6119; 1535 characters remaining).

### 2026-08-08, iteration 970 — [[characters/遜|遜]]

`mc_id: 2239` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 162|辵]] ("to walk") + phonetic [[孫]]; `graphemic_classification: 孫` already correct. Vietnamese `[tốn]` confirmed complete. **English gloss expanded**: stored only `inferior` (a secondary/literary sense), missing the primary sense `humble, modest` — added both, corroborated by the already-cited word [[謙遜]] ("humility, modesty").  Filled the empty `pos` field to `性詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, drawing on [[遜色]]'s own Notes (which already traces 遜's relationship to 孫 and the "yield precedence" semantic development) for the etymological gloss. **`## Words` section already existed** with both genuine citing words — [[謙遜]] (correctly un-tagged, since its own Notes confirm it's actually the stand-in for [[謙]], not for 遜) and [[遜色]] (missing its "(stand-in for 遜)" tag — added). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 遜 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 滋 (6120; 1534 characters remaining).

### 2026-08-08, iteration 971 — [[characters/滋|滋]]

`mc_id: 1654` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 085|水]] ("water") + phonetic 茲, which the vault pages under its variant glyph [[玆]] (matching MC initial/final `t͡s`/`ɨ` exactly, corroborating the shared phonetic); `graphemic_classification: 玆` already correct. Vietnamese `[tư]` confirmed complete. Filled the empty `pos` field to `性詞` (matching the pos of its own stand-in word).

**Repaired a half-written Notes bullet**: the semantic gloss was a dangling empty string `("")` and the phonetic link was a bare, targetless `[[]]` — filled in properly as `[[Radical 085|水]] ("water") + phonetic [[玆]]`. **Removed an unsupported historical claim**: "added to the J jr list in 2017 because of prefecture names" had no corroboration on Wiktionary, and is actively contradicted by 滋's own stored `joyo_level: "4"` — a *kyōiku* (elementary-school-taught) grade, whereas the real 2010 Jōyō reform's prefecture-name additions (阜, 埼, 梨, 潟, etc.) all landed at 高等/non-kyōiku level in this vault's own classification. Same standard applied to [[潟]]'s unverified "2017 Jōyō" claim earlier in this project — removed rather than kept as unverified fact.

**`## Words` section was entirely missing** — added <ruby>[[滋生]]<rt>ㄐㄜㄙㄚㄫ</rt></ruby> "grow, multiply, thrive" (stand-in for 滋); the other grep hit, [[令和]], was confirmed a false positive (滋 appears only inside a quoted classical passage). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 滋 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 虹 (6121; 1533 characters remaining).

### 2026-08-08, iteration 972 — [[characters/虹|虹]]

**mc_id off-by-one fixed**: stored `2676` → actual rank in `CC 2000.md` is `2677`. 形声 classification confirmed via Wiktionary: semantic [[虫]] ("insect, creature") + phonetic [[工]]; `graphemic_classification: 工` already correct. **Vietnamese incomplete, fixed**: English Wiktionary's Vietnamese section was truncated/empty in fetches, so cross-checked Vietnamese Wiktionary directly — it lists `hống`, `hồng`, `vồng` as genuine readings; only `hồng` and `vồng` were stored — added the missing `hống`. Filled the empty `pos` field to `名詞`.

**`## Notes` was badly malformed** — a mix of a bare numbered gloss list, an inline neon-abbreviation aside with a malformed non-wikilink ruby, the two bare CC lookup links, and two Words-type ruby bullets all jumbled into one section with no proper 4-bullet structure. Rebuilt cleanly: standard Notes bullets, then a proper `## Words` section with all four genuine citing words (verified via grep) — <ruby>[[彩虹]]</ruby> (stand-in), <ruby>[[虹霓]]</ruby> "neon; neon light", <ruby>[[虹素]]</ruby> "neon", <ruby>[[虹尊]]</ruby> "rainbow trout". **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 虹 as its own phonetic) — correctly has no section.

**Fixed a citing word bug found in passing**: [[虹尊]]'s own `注音` was stored as just `ㄏㄛㄫ` (虹's syllable alone), missing 尊's own syllable `ㄐㄛㄋ` — corrected to the full compound `ㄏㄛㄫㄐㄛㄋ`, matching the two-syllable convention used on its sibling [[虹霓]].

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 閥 (6122; 1532 characters remaining).

### 2026-08-08, iteration 973 — [[characters/閥|閥]]

`mc_id: 5828` confirmed as legitimate long-tail data (閥 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[門]] ("door, gate") + phonetic [[伐]]; `graphemic_classification: 伐` already correct. Vietnamese `[phiệt]` confirmed complete. `stand_in: 閥族` confirmed genuine (word exists, correctly cites 閥). Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section already existed** with the correct single entry but was missing its "(stand-in for 閥)" suffix — added. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 閥 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 侶 (6123; 1531 characters remaining).

### 2026-08-08, iteration 974 — [[characters/侶|侶]]

`mc_id: 4625` confirmed as legitimate long-tail data (侶 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[Radical 009|人]] ("person") + phonetic [[呂]]; `graphemic_classification: 呂` already correct. Vietnamese `[lứa, lữ]` confirmed complete. `stand_in: 伴侶` confirmed genuine (already perfected, correctly cites 侶). Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added both genuine citing words (verified via grep): <ruby>[[伴侶]]<rt>ㄅㄚㄋㄌ⼄</rt></ruby> "companion, partner, mate" (stand-in for 侶) and <ruby>[[僧侶]]<rt>ㄙㄨㄫㄌ⼄</rt></ruby> "Buddhist monk". **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 侶 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 偵 (6124; 1530 characters remaining).

### 2026-08-08, iteration 975 — [[characters/偵 (char)|偵]]

`mc_id: 5621` confirmed as legitimate long-tail data (偵 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声/会意 classification confirmed via Wiktionary: semantic [[Radical 009|人]] ("person") + phonetic [[貞]]; `graphemic_classification: 貞` already correct.

**Vietnamese contamination fixed**: stored `[rình, trinh, triệng]`; the citing word [[偵]]'s own Notes already contain specific prior research on exactly these three candidates — `trinh` confirmed as the genuine Hán Việt reading (attested in trinh sát/偵察, trinh thám/偵探), `rình` flagged as a native Vietnamese verb ("to lurk, watch stealthily," semantically adjacent but not Hán Việt), and `triệng` flagged as "likely corpus noise." Trimmed to just `trinh`, trusting that specific analysis over Wiktionary's undifferentiated three-reading list — the same precedent established on 呈/梗/堪 earlier this project. Filled the empty `pos` field to `動詞`, matching the word page's own pos.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format (using `HSK No` for the genuinely-empty `hsk_level`, per the convention on already-perfected characters like [[娯]]). **`## Words` section was entirely missing** — added <ruby>[[偵]]<rt>ㄊㄧㄫ</rt></ruby> "spy" (stand-in for 偵). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 偵 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 槽 (6125; 1529 characters remaining).

### 2026-08-08, iteration 976 — [[characters/槽|槽]]

`mc_id: 6071` confirmed as legitimate long-tail data (槽 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[木]] ("wood") + phonetic [[曹]]; `graphemic_classification: 曹` already correct. Vietnamese `[tào, tàu, tầu]` confirmed complete — English Wiktionary's fetch only surfaced `tàu`, so cross-checked Vietnamese Wiktionary directly, which confirmed all three (Hán Việt `tào`; Nôm `tầu, tàu, tào`) — no change needed. `stand_in: 料槽` confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section already existed** with both genuine citing words but the stand-in, [[料槽]], was missing its "(stand-in for 槽)" tag — added, and reordered it first (ahead of [[浴槽]]) to match the usual stand-in-first convention. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 槽 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 刹 (6126; 1528 characters remaining).

### 2026-08-08, iteration 977 — [[characters/刹|刹]]

`mc_id: 0` confirmed genuine (刹/剎 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[刀]] ("knife") + phonetic [[杀]] (from 殺); `graphemic_classification: 杀` already correct. Vietnamese `[sát]` confirmed complete.

**Reading-mismatch bug found and fixed**: stored `mandarin: "shā"` belongs to an entirely different, unrelated sense of 剎/刹 — "to brake a car" (刹車, shāchē), derived from 煞/殺 via a separate etymology. Every other field on this page (english "moment," `stand_in: 刹那`, the [[寺刹]] Words entry, Vietnamese `sát`, the stored MC initial/final) corresponds to the *other* etymology — 剎/刹 as a purpose-built Sanskrit transliteration character (a clipping of 剎多羅/*kṣetra*, and via 剎那/*kṣaṇa* "moment") — whose correct Mandarin reading is `chà`, not `shā`. Corrected the `mandarin` field; both citing words ([[刹那]]: `chànà`, [[寺刹]]: `sìchà`) already had the right reading, so no propagation was needed elsewhere. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, incorporating the Sanskrit-transliteration origin story (already researched on [[寺刹]]'s own page) and explicitly flagging the unrelated `shā` "brake" homograph so the mismatch doesn't recur. **`## Words` section was missing its own stand-in entry** — added <ruby>[[刹那]]<rt>ㄑㄚㄊㄋㄚ</rt></ruby> "moment, instant, split second" (stand-in for 刹); [[寺刹]] was already correctly present. **Chengyu**: no hits. **Derived Characters**: no hits (an initial grep hit on [[殺 (char)|殺]] was a false positive — matched only because 殺's own `graphemic_classification` happens to also be `杀`, not because it cites 刹) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 剤 (6127; 1527 characters remaining).

### 2026-08-08, iteration 978 — [[characters/剤|剤]]

**mc_id off-by-one fixed**: stored `3359` → actual rank in `CC 3000.md` is `3360`. 形声 classification confirmed via Wiktionary: semantic [[刀]] ("knife") + phonetic 齊, which the vault pages under its shinjitai glyph [[斉]]; `graphemic_classification: 斉` already correct. Vietnamese `[tễ, xẻ]` confirmed complete. `stand_in: 薬剤` confirmed genuine (already perfected, correctly cites 剤 and notes it "cannot appear independently"). Filled the empty `pos` field to `名詞` and the entirely-blank `boundedness` field to `90`, matching its fully-bound status.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section already existed** with the correct single entry but was missing its "(stand-in for 剤)" tag — added. **Chengyu**: no hits. **Derived Characters**: initial grep for characters citing `斉` (剤's own phonetic donor) surfaced [[済 (char)|済]] and [[𦜝]], but these are phonetic-family *siblings* sharing the same ultimate donor 斉 — not characters citing 剤 itself; the correct check (grep for citations of 剤 specifically) returned zero hits, so no section was added, per the sibling-vs-derived distinction established earlier this project. A separate grep hit, [[含漱]], was also a false positive (剤 appears only in a Japanese usage note in its body).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 喩 (6128; 1526 characters remaining).

### 2026-08-08, iteration 979 — [[characters/喩|喩]]

`mc_id: 1890` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[口 (char)|口]] ("mouth") + phonetic [[兪]]; `graphemic_classification: 兪` already correct. **Vietnamese was entirely empty, filled**: Wiktionary distinguishes a tight Hán Việt set (`dụ, du`) from a much broader, noisier Nôm list (dụ, dầu, dẫu, dỗ, nhủ, rủ, dẩu — several of which read as unrelated native verbs like "to coax/scold"); populated with just the two genuine Hán Việt readings, consistent with this project's standing policy of not importing Wiktionary's undifferentiated Nôm tables wholesale. Filled the empty `pos` field to `名詞` and the blank `boundedness` to `90`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, including the vault-policy note (already documented on [[兪]]'s own page) that this whole phonetic family gets a deliberate -m-final Dan'a'yo reading to cut down homophony. **`## Words` section was entirely missing** — added <ruby>[[比喩]]<rt>ㄅㄧㄜ⼜ㄇ</rt></ruby> "metaphor" (stand-in for 喩); a grep hit on [[兪]] was a false positive (喩 only appears there in a list of phonetic descendants). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 喩 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 斬 (6129; 1525 characters remaining).
