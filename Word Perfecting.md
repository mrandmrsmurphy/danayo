# Word Perfecting

Running log for the word-perfecting backlog sweep (see [[AIOS/checklists/checklist_words.md|Checklist: Word Pages]]). The first log (iterations 1–1040) grew to ~8,500 lines and was archived by the user to `Word Perfecting.md.zip`; a second log (iterations 1041–1782) grew large in turn and was archived to `Word Perfecting 2.md.zip`; a third log (iterations 1783–2922) grew large again and was archived to `Word Perfecting 3.md.zip`. This file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one word per iteration (per standing pacing preference). Find the next candidate via `grep -L "^date-last-perfect" words/*.md`, sorted alphabetically by filename (Unicode/`LC_ALL=C` order), continuing from the last-processed filename's position in that sort. Check the word's own `characters:` constituents for a `stand_in` match (add the stand-in note if so), verify `羅馬字`/`諺文`/`注音` are the correct concatenation of each constituent's own fields, verify `kwin` via the AND-rule (all constituents' own `kwin` must be `true` for the compound to be `true`), fill blank cross-linguistic fields only when a real value can be verified (leave deliberately blank with a reason otherwise), and check for genuine Dan'a'yo-level homophones (not just same-spelling coincidences in a real language) before stamping `date-last-perfect`. Exact-match homophone checks use the `homophone_check.py` script in the scratchpad (see memory for its correct 3-argument invocation).

Next: 繁忙.

### 2026-09-05, iteration 2923 — [[words/繁忙|繁忙]]

No cranberry (忙's own stand-in is this exact compound, but 繁's own is [[繁茂]]) — transitivity fails, though 忙 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (panmang/판망/ㄆㄚㄋㄇㄚㄫ) already verified as the correct concatenation — no bug. Filled blank vietnamese (phồn mang, standard attested term). **In passing**, added a missing "(stand-in for 忙)" annotation on `characters/忙.md`'s own Words-list citation. No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 繁殖.

### 2026-09-05, iteration 2924 — [[words/繁殖|繁殖]]

No cranberry (殖's own stand-in is this exact compound, but 繁's own is [[繁茂]]) — transitivity fails, though 殖 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (pansig/판식/ㄆㄚㄋㄙㄧㄎ) already verified as the correct concatenation — no bug. Fixed `hsk_level: 3` (bare number → quoted string). Filled blank vietnamese (phồn thực, standard attested term). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 繁茂.

### 2026-09-05, iteration 2925 — [[words/繁茂|繁茂]]

No cranberry (繁's own stand-in is this exact compound, but 茂's own is [[茂密]]) — transitivity fails, though 繁 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (panmou/판못/ㄆㄚㄋㄇㄛㄨ) already verified as the correct concatenation — no bug. Filled blank vietnamese (phồn mậu, standard attested term). Removed blank hsk_level/swadesh/aliases, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 繁華.
