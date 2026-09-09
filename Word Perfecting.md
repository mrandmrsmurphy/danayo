# Word Perfecting

Running log for the word-perfecting backlog sweep (see [[AIOS/checklists/checklist_words.md|Checklist: Word Pages]]). The first log (iterations 1–1040) grew to ~8,500 lines and was archived by the user to `Word Perfecting.md.zip`; a second log (iterations 1041–1782) was archived to `Word Perfecting 2.md.zip`; a third log (iterations 1783–2922) was archived to `Word Perfecting 3.md.zip`; a fourth log (iterations 2923–3555) was archived to `Word Perfecting 4.md.zip`. This file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one word per iteration (per standing pacing preference). Find the next candidate via `grep -L "^date-last-perfect" words/*.md`, sorted alphabetically by filename (Unicode/`LC_ALL=C` order), continuing from the last-processed filename's position in that sort. Check the word's own `characters:` constituents for a `stand_in` match (add the stand-in note if so), verify `羅馬字`/`諺文`/`注音` are the correct concatenation of each constituent's own fields, verify `kwin` via the AND-rule (all constituents' own `kwin` must be `true` for the compound to be `true`), fill blank cross-linguistic fields only when a real value can be verified (leave deliberately blank with a reason otherwise), and check for genuine Dan'a'yo-level homophones (not just same-spelling coincidences in a real language) before stamping `date-last-perfect`.

Next: 静寂.

### 2026-09-08, iteration 3556 — [[words/静寂|静寂]]
Legitimizing note added (静's own `stand_in` is [[静寂]] itself; 寂's own `stand_in` is [[寂滅]], so transitivity fails — no `#cranberry`). Pronunciation fields (jengjeg/정적/ㄐㄝㄫㄐㄝㄎ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched exactly — no bug. Confirmed `mandarin`'s two comma-joined tone variants (jìngjì, jìngjí) are both genuinely attested, not contamination. Both character pages already cited 静寂 correctly, 静's side with the `(stand-in for 静)` annotation. Filled blank `vietnamese: tĩnh tịch` — attested, mainly Buddhist register, noting Chinese/Vietnamese also freely reverse the order (寂静/tịch tĩnh, corresponding to the vault's own separate [[寂静]]). Removed blank `hsk_level`/`swadesh`, converted flow-style `aliases` to block-list. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 非常.

### 2026-09-08, iteration 3557 — [[words/非常|非常]]
No cranberry (非's own `stand_in` is itself, 常's is [[日常]] — neither points here). **Found and fixed a real bug**: `羅馬字`/`諺文` had been contaminated to `pisyang`/`피샹` instead of the correct concatenation of 非's own stored fields (`fi`/`삐`) — confirmed against the already-correct [[非洲]]/[[南非]], both correctly preserving `fi`/`삐`. `注音` had already stayed correct. `kwin: false` already correct (AND-rule, both constituents false). Filled blank `vietnamese: phi thường` — confirmed standard, everyday term. **Fixed a malformed citation** on `characters/非 (char).md` (bare "[[非常]] ..." text lacking ruby markup, unlike its siblings) and **added a missing citation** to `characters/常.md`'s `## Words` list. Quoted `hsk_level`, removed blank `swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 面田.

### 2026-09-08, iteration 3558 — [[words/面田|面田]]
No cranberry (面's own `stand_in` is [[表面]], 田's is [[田野]] — neither points here; 面/田 serve as phonetic transliteration characters standing in for the real 緬甸's own 緬/甸). **Found and fixed a real bug**: `注音` had a wrong glyph in its first syllable (ㄇ⼔ㄋ using ⼔, instead of 面's own stored ⼶) — corrected to ㄇ⼶ㄋㄉㄝㄋ, matching `羅馬字`/`諺文`'s already-correct myenden/면던. The same wrong-glyph bug had propagated into both `characters/面.md`'s and `characters/田.md`'s existing citations — fixed both. `kwin: false` already correct (AND-rule). Confirmed all five real-language fields (Miǎndiàn/min5din6/めんでん/면전/Miến Điện) are the real reading of the actual word 緬甸, per the same convention as the 露-transliteration family — めんでん and 면전 verified as real, historically dated (1798/1930) readings, now superseded by ミャンマー/미얀마 respectively but still correct as documented. Removed the redundant duplicate `品詞` field (kept `pos`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 革命.
