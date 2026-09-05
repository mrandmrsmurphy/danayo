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

### 2026-09-05, iteration 2926 — [[words/繁華|繁華]]

No cranberry (繁's own stand-in is [[繁茂]], 華's is [[華美]]) — neither constituent legitimized by this word. Pronunciation fields (panhwa/판화/ㄆㄚㄋㄏ⺢) already verified as the correct concatenation — no bug. Filled blank vietnamese (phồn hoa, standard attested term). Removed blank hsk_level/swadesh/aliases, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 繊細.

### 2026-09-05, iteration 2927 — [[words/繊細|繊細]]

No cranberry (繊's own stand-in is this exact compound, but 細's own is [[細]] itself) — transitivity fails, though 繊 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (semsei/섬세/ㄙㄝㄇㄙㄝㄧ) already verified as the correct concatenation — no bug. Filled blank vietnamese (tiêm tế, standard attested term). **In passing**, fixed a malformed comma-joined `vietnamese` value on `characters/細 (char).md` ("tế, tới" → proper 2-item list). No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 繋辞.

### 2026-09-05, iteration 2928 — [[words/繋辞|繋辞]]

No cranberry (繋's own stand-in is this exact compound, but 辞's own is [[辞職]]) — transitivity fails, though 繋 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (heici/헤치/ㄏㄝㄧㄑㄧ) already verified as the correct concatenation — no bug. Mandarin/cantonese/vietnamese deliberately left blank, reconfirming the word's own pre-existing rationale (a Japanese/Korean-specific grammatical term with no attested reading elsewhere) — kept as-is rather than fabricated. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 織女星.

### 2026-09-05, iteration 2929 — [[words/織女星|織女星]]

No cranberry (none of the three constituents' `stand_in` points here). Pronunciation fields (jignǝseng/직느성/ㄐㄧㄎㄋㄜㄙㄝㄫ) already verified as the correct three-way concatenation — no bug. All other-language fields confirmed standard and genuinely attested. Filled blank vietnamese (chức nữ tinh, compositional and itself the standard term). Removed blank hsk_level/swadesh/aliases. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 繞.

### 2026-09-05, iteration 2930 — [[words/繞|繞]]

Single-character stand-in word. Pronunciation fields (nou/놋/ㄋㄛㄨ) already matched the character's own values — no bug. Added missing kwin/japanese (native まとう); pos/vietnamese were already correctly set. No homophones (no other character shares this syllable). Stamped `date-last-perfect: 2026-09-05`.

Next: 缺点.

### 2026-09-05, iteration 2931 — [[words/缺点|缺点]]

No cranberry (缺's own stand-in is [[欠缺]], 点's is [[点]] itself). Pronunciation fields (kweddem/퀃덤/ㄎ⼔ㄊㄉㄝㄇ) already verified as the correct concatenation — no bug. Fixed a comma-joined `korean` field ("결점, 흠" — a native gloss wrongly appended to the compositional reading) to just 결점. Added missing `kwin: false`. Removed blank hsk_level/swadesh, converted loose gloss text into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 罪.

### 2026-09-05, iteration 2932 — [[words/罪|罪]]

Single-character stand-in word. Pronunciation fields (joi/죄/ㄐㄛㄧ) already matched the character's own values — no bug. Added missing pos/kwin/japanese, filled `vietnamese: null` → tội. **In passing**, added a missing "(stand-in for 罪)" citation of 罪 itself, absent entirely from `characters/罪 (char).md`'s Words list. No homophones (no other character shares this syllable). Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 置換.

### 2026-09-05, iteration 2933 — [[words/置換|置換]]

No cranberry (both 置's and 換's own `stand_in` point to themselves). Pronunciation fields (cihwam/치홤/ㄑㄧㄏ⺢ㄇ) already verified as the correct concatenation — no bug. Filled blank vietnamese (trí hoán, standard attested mathematical term). Removed blank hsk_level/swadesh/aliases. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 罷免.

### 2026-09-05, iteration 2934 — [[words/罷免|罷免]]

No cranberry (罷's own stand-in is [[罷官]], 免's is [[免除]]). Pronunciation fields (baimyen/배면/ㄅㄚㄧㄇ⼶ㄋ) already verified as the correct concatenation — no bug. All fields already correctly filled (including korean, verified compositional and matching real attestation) — just cleanup: removed blank hsk_level/swadesh/aliases, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 罷官.

### 2026-09-05, iteration 2935 — [[words/罷官|罷官]]

No cranberry (罷's own stand-in is this exact compound, but 官's own is [[官人]]) — transitivity fails, though 罷 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (baigwan/배관/ㄅㄚㄧㄍ⺢ㄋ) already verified as the correct concatenation — no bug. Filled entirely-blank japanese/korean/vietnamese (compositional, all standard attested terms), added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 罹患.

### 2026-09-05, iteration 2936 — [[words/罹患|罹患]]

No cranberry (罹's own stand-in is this exact compound, but 患's own is [[患]] itself) — transitivity fails, though 罹 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (lihwam/리홤/ㄌㄧㄏ⺢ㄇ) already verified as the correct concatenation — no bug. Filled blank vietnamese (li hoạn, compositional and itself attested). Removed blank hsk_level/swadesh/aliases. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羅馬.

### 2026-09-05, iteration 2937 — [[words/羅馬|羅馬]]

No cranberry (羅's own stand-in is this exact compound, but 馬's own is [[馬]] itself) — transitivity fails, though 羅 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (loma/로마/ㄌㄛㄇㄚ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug**: word file had `kwin: true`, but the AND-rule requires false (羅 is individually `kwin: false`) — corrected. Fixed a comma-joined `vietnamese` string (three genuinely distinct attested forms — Roma, Rôma, La Mã) into a proper list, and a typo ("sually followed by" → proper Notes prose). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羅馬字.

### 2026-09-05, iteration 2938 — [[words/羅馬字|羅馬字]]

No cranberry (none of the three constituents' `stand_in` points here). Pronunciation fields (lomaji/로마지/ㄌㄛㄇㄚㄐㄧ) already verified as the correct three-way concatenation — no bug. Filled blank vietnamese (la mã tự, compositional). **In passing**, fixed `characters/字 (char).md`'s own citation of this word (non-standard `[text](path)` link format with a lowercase, singular gloss → proper ruby wikilink with the standard plural gloss). Removed blank hsk_level/swadesh/aliases. No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 羅馬語.

### 2026-09-05, iteration 2939 — [[words/羅馬語|羅馬語]]

No cranberry (none of the three constituents' `stand_in` points here). Pronunciation fields (loma'yo/로마요/ㄌㄛㄇㄚ·⼄) already verified as the correct three-way concatenation — no bug. Double-checked mandarin/cantonese/korean/japanese: all reflect the real, attested name for "Latin" in each language (拉丁語/lādīngyǔ etc., already correctly documented via the `aliases` field) rather than a compositional reading of the Dan'a'yo-internal coinage 羅馬語 itself — confirmed intentional, not a bug, matching the periodic-table-neologism pattern. Removed the redundant duplicate `品詞` field and a leading-space formatting bug on `japanese`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羊毛.

### 2026-09-05, iteration 2940 — [[words/羊毛|羊毛]]

No cranberry (羊's own stand-in is [[綿羊]], 毛's is [[毛]] itself). Pronunciation fields ('yangmau/양맛/⼘ㄫㄇㄚㄨ) already verified as the correct concatenation — no bug. Filled blank vietnamese (dương mao, compositional). Removed blank hsk_level/swadesh/aliases, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羊頭.

### 2026-09-05, iteration 2941 — [[words/羊頭|羊頭]]

No cranberry (羊's own stand-in is [[綿羊]], 頭's is [[頭]] itself). Pronunciation fields ('yangtou/양톳/⼘ㄫㄊㄛㄨ) already verified as the correct concatenation — no bug. Filled blank vietnamese (dương đầu, compositional). **In passing**, added a missing citation of 羊頭 to `characters/羊.md`'s own Words list (it had only been cited inside the chengyu section, not as its own regular word entry — `characters/頭 (char).md` already had it correctly). No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 羊駝.

### 2026-09-05, iteration 2942 — [[words/羊駝|羊駝]]

No cranberry (羊's own stand-in is [[綿羊]], 駝's is [[駝背]]). Pronunciation fields ('yangda/양다/⼘ㄫㄉㄚ) already verified as the correct concatenation — no bug. Double-checked korean/japanese/vietnamese: all directly transliterate "alpaca" (a New World species with no traditional term in those languages), confirmed genuine, not a bug. Removed redundant duplicate `品詞` field. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 美.

### 2026-09-05, iteration 2943 — [[words/美|美]]

Single-character stand-in word. Pronunciation fields (mi/미/ㄇㄧ) already matched the character's own values — no bug. Added missing pos/kwin/japanese (native うつくしい), filled `vietnamese: null` → mĩ. **In passing**, added a missing "(stand-in for 美)" annotation on `characters/美 (char).md`'s own bare self-citation. No homophones (no other character shares this syllable). Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 美国.

### 2026-09-05, iteration 2944 — [[words/美国|美国]]

No cranberry (美's own stand-in is [[美]] itself, 国's is [[国家]]). Pronunciation fields (migog/미곡/ㄇㄧㄍㄛㄎ) already verified as the correct concatenation — no bug. Double-checked japanese べいこく (built on the alias form 米国, which is already documented in `aliases:`) — confirmed genuine, not a bug. All other fields already correctly filled. Removed blank hsk_level/swadesh. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 美国人.

### 2026-09-05, iteration 2945 — [[words/美国人|美国人]]

No cranberry (none of the three constituents' `stand_in` points here). Pronunciation fields (migognin/미곡닌/ㄇㄧㄍㄛㄎㄋㄧㄋ) already verified as the correct three-way concatenation — no bug. Japanese アメリカ人 double-checked as genuine (loanword compound). Fixed a comma-joined `vietnamese` string (two genuinely distinct attested forms) into a proper list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 美徳.

### 2026-09-05, iteration 2946 — [[words/美徳|美徳]]

No cranberry (both 美's and 徳's own `stand_in` point to themselves). **Found and fixed a real bug**: `羅馬字`/`注音` had midug/ㄇㄧㄉㄨㄎ (徳 misread with a d-initial), mismatching 徳's real t-initial reading (tug/ㄊㄨㄎ) — 諺文 (미툭) had already been correct, the reverse of the usual "注音 stays correct" tell. Corrected to mitug/ㄇㄧㄊㄨㄎ, and propagated the fix to both `characters/美 (char).md`'s and `characters/徳 (char).md`'s own duplicate-wrong citations. All other fields already correctly filled. No homophones. Stamped `date-last-perfect: 2026-09-05` on all three files.

Next: 美洲.

### 2026-09-05, iteration 2947 — [[words/美洲|美洲]]

No cranberry (both 美's and 洲's own `stand_in` point to themselves). Pronunciation fields (mijuo/미줏/ㄇㄧㄐㄨㄛ) already verified as the correct concatenation — no bug. Filled blank japanese (びしゅう, compositional). Removed redundant duplicate `品詞` field, converted loose "Combines..." note into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羚羊.

### 2026-09-05, iteration 2948 — [[words/羚羊|羚羊]]

No cranberry (羚's own stand-in is this exact compound, but 羊's own is [[綿羊]]) — transitivity fails, though 羚 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (leng'yang/렁양/ㄌㄝㄫ·⼘ㄫ) already verified as the correct concatenation — no bug. Filled blank vietnamese (linh dương, standard attested term). **In passing**, added a missing citation of 羚羊 to `characters/羊.md`'s own Words list (羚's own page already had it correctly). Converted loose "See also" text into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 羞恥.

### 2026-09-05, iteration 2949 — [[words/羞恥|羞恥]]

No cranberry (羞's own stand-in is this exact compound, but 恥's own is [[恥辱]]) — transitivity fails, though 羞 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (suoci/숫치/ㄙㄨㄛㄑㄧ) already verified as the correct concatenation — no bug. All fields already correctly filled — just cleanup: removed blank hsk_level/swadesh/aliases, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羞辱.

### 2026-09-05, iteration 2950 — [[words/羞辱|羞辱]]

No cranberry (辱's own stand-in is this exact compound, but 羞's own is [[羞恥]]) — transitivity fails, though 辱 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (suonog/숫녹/ㄙㄨㄛㄋㄛㄎ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `japanese`/`korean` had くつじょく/굴욕, the real readings of the unrelated near-synonym 屈辱 (a different compound, different first character, no vault page) rather than 羞辱's own compositional readings — corrected to しゅうじょく/수욕. Removed the erroneous `屈辱` alias entry (it's a distinct word, not a variant spelling). Converted comma-joined `mandarin` to a proper list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 群島.

### 2026-09-05, iteration 2951 — [[words/群島|群島]]

No cranberry (群's own stand-in is [[群衆]], 島's is [[島]] itself). Pronunciation fields (guntau/군탓/ㄍㄨㄋㄊㄚㄨ) already verified as the correct concatenation — no bug. Fixed the `characters:` list citing bare "島" (a redlink, since the actual page is `島 (char).md`) → "島 (char)". Removed blank hsk_level/swadesh, fixed bare-array YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 羨慕.

### 2026-09-05, iteration 2952 — [[words/羨慕|羨慕]]

No cranberry (羨's own stand-in is this exact compound, but 慕's own is [[思慕]]) — transitivity fails, though 羨 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields ('iǝmo/의모/ㄧㄜㄇㄛ) already verified as the correct concatenation — no bug. All fields already correctly filled — just cleanup: removed blank hsk_level/swadesh, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 翅鞘.

### 2026-09-05, iteration 2953 — [[words/翅鞘|翅鞘]]

No cranberry (翅's own stand-in is [[魚翅]], 鞘's is [[刀鞘]]). Pronunciation fields (siso/시소/ㄙㄧㄙㄛ) already verified as the correct concatenation — no bug. Filled blank vietnamese (sí sao, compositional). Fixed unquoted mandarin/cantonese/korean strings (quoting convention). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 翌.

### 2026-09-05, iteration 2954 — [[words/翌|翌]]

Single-character stand-in word. Pronunciation fields ('ig/익/ㄧㄎ) already matched the character's own values — no bug. **Found and fixed two real bugs**: `pos` had been set to 格助詞 (a specific closed class of twelve case particles 翌 doesn't belong to) — corrected to 修飾語, matching the character page's own value and 翌's actual role as a temporal modifier; `japanese` had いき, which turned out not to be an attested reading of 翌 at all (confirmed via web search — real readings are ヨク on'yomi and あくる kun'yomi) — corrected to ヨク. Removed the redundant duplicate `品詞` field. **In passing**, fixed `characters/翌 (char).md`'s own citation (non-standard `[text](path)` link format, missing stand-in annotation) and an unquoted `hsk_level: 無`. No homophones (億/憶/抑/翼/臆 share the syllable at the character level only). Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 翌世紀.

### 2026-09-05, iteration 2955 — [[words/翌世紀|翌世紀]]

No cranberry (none of the three constituents' `stand_in` points here). Pronunciation fields ('igsegi/익서기/ㄧㄎㄙㄝㄍㄧ) already verified as the correct three-way concatenation — no bug. Filled blank vietnamese (dực thế kỷ, compositional). **In passing**, found and fixed two real bugs on `characters/世.md`: a double-space formatting bug in `諺文`, and a real bug where `vietnamese` stored "thế giới" (the full compound meaning "world," i.e. 世界's own value) instead of 世's own atomic reading "thế" — corrected. No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 翌年.

### 2026-09-05, iteration 2956 — [[words/翌年|翌年]]

No cranberry (both 翌's and 年's own `stand_in` point to themselves). Pronunciation fields ('ignen/익넌/ㄧㄎㄋㄝㄋ) already verified as the correct concatenation — no bug. Filled blank vietnamese (dực niên, compositional). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 翌週.

### 2026-09-05, iteration 2957 — [[words/翌週|翌週]]

No cranberry (翌's own stand-in is [[翌]] itself, 週's is [[週日]]). Pronunciation fields ('igjuo/익줏/ㄧㄎㄐㄨㄛ) already verified as the correct concatenation — no bug. Filled blank vietnamese (dực chu, compositional). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 習俗.

### 2026-09-05, iteration 2958 — [[words/習俗|習俗]]

No cranberry (習's own stand-in is [[練習]], 俗's is [[俗]] itself). **Found and fixed a real bug**: `羅馬字`/`注音` (and 諺文) had an i-vowel first syllable (sibsog/십속/ㄙㄧㄆㄙㄛㄎ), mismatching 習's real ǝ-vowel reading (sǝb/습/ㄙㄜㄆ, confirmed via `syllables/ㄙㄜㄆ.md`) — corrected to sǝbsog/습속/ㄙㄜㄆㄙㄛㄎ. The same wrong 注音 was independently duplicated on `characters/習.md`'s own citation, fixed there too. Also corrected `kwin` (false→true per AND-rule). Filled the two empty-string fields (`vietnamese: ""`, `swadesh: ""`) and removed the redundant duplicate `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 翠色.

### 2026-09-05, iteration 2959 — [[words/翠色|翠色]]

No cranberry (翠's own stand-in is this exact compound, but 色's own is [[色彩]]) — transitivity fails, though 翠 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (cuisig/취식/ㄑㄨㄧㄙㄧㄎ) already verified as the correct concatenation — no bug. Filled three empty-string fields (`cantonese: ""`, `korean: ""`, `vietnamese: ""` — all compositional), added missing `kwin: false`, removed redundant duplicate `品詞` field. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 翠金.

### 2026-09-05, iteration 2960 — [[words/翠金|翠金]]

Periodic-table neologism (terbium), rebuilt to match the established template from sibling elements like [[石素]]/[[紫素]]. No cranberry (neither 翠's nor 金's own `stand_in` points here). Pronunciation fields (cuigim/취김/ㄑㄨㄧㄍㄧㄇ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug**: word file had `kwin: false`, but the AND-rule requires true (both 翠 and 金 are individually `kwin: true`) — corrected. Mandarin tè/cantonese tik1 (the real element's own readings, via 铽) and korean/japanese/vietnamese international borrowings all confirmed as the expected pattern for chemical-element neologisms. Removed the redundant duplicate `品詞` field and replaced a long essay-style Notes section (headers, bold labels, a "Comparative CJKV forms" list) with the vault's standard concise neologism-Notes format. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 翻.

### 2026-09-05, iteration 2961 — [[words/翻|翻]]

Single-character stand-in word. **Found and fixed a real bug**: `羅馬字`/`諺文`/`注音` had pon/폰/ㄆㄛㄋ (p-initial), mismatching 翻's real f-initial reading (fon/뽄/ㄈㄛㄋ, per the vault's established ㄈ→ㅃ convention) — corrected. Added missing pos/kwin/japanese, filled `vietnamese: null` → phiên. This exposed a genuine Dan'a'yo homophone with [[反]] (already perfected, whose own Notes had independently fixed the identical p/f bug and flagged 販/返 as sharing the phonetic family without word pages) — added reciprocal callouts to both. No other collisions. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 翻訳.

### 2026-09-05, iteration 2962 — [[words/翻訳|翻訳]]

No cranberry (訳's own stand-in is this exact compound, but 翻's own is [[翻]] itself) — transitivity fails, though 訳 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `羅馬字`/`諺文` had pon'yeg/폰역 (p-initial), inheriting the same 翻/p-f confusion fixed on the previous word — `注音` (ㄈㄛㄋ⼶ㄎ) had stayed correct as the tell. Filled blank cantonese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 翻身.

### 2026-09-05, iteration 2963 — [[words/翻身|翻身]]

No cranberry (翻's own stand-in is [[翻]] itself, 身's is [[身体]]). **Found and fixed two real bugs**: inherited the same 翻 p/f confusion in `羅馬字`/`諺文` (`注音` stayed correct throughout, the tell); `cantonese` was garbled (saan1san1, missing a space and mismatching 翻's own faan1) — corrected to faan1 san1. Filled blank korean/vietnamese, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 老人学.

### 2026-09-05, iteration 2964 — [[words/老人学|老人学]]

No cranberry (none of the three constituents' `stand_in` points here). **Found and fixed a real bug**: `羅馬字`/`諺文` had lyau/럇 (a glide-inserted first syllable), mismatching 老's real lau/랏 — `注音` (ㄌㄚㄨㄋㄧㄋㄏㄚㄎ) had stayed correct throughout, the usual tell. Filled blank vietnamese (lão nhân học, standard attested term). Removed blank hsk_level/swadesh/aliases. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 老子.

### 2026-09-05, iteration 2965 — [[words/老子|老子]]

No cranberry (老's own stand-in is [[老]] itself, 子's is [[児子]]). **Found and fixed a real bug**: `羅馬字`/`諺文` had lyaujǝ/럇즈 (the same 老-syllable mismatch just fixed on [[老人学]]) — `注音` (ㄌㄚㄨㄐㄜ) had stayed correct throughout. All other fields already correctly filled. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 老師.

### 2026-09-05, iteration 2966 — [[words/老師|老師]]

No cranberry (老's own stand-in is [[老]] itself, 師's is [[教師]]). Pronunciation fields (lausiǝ/랏싀/ㄌㄚㄨㄙㄧㄜ) already verified as the correct concatenation — no bug (老's syllable was already correct here, unlike the previous two 老-words). Fixed `hsk_level: 1` (bare number → quoted string). Converted a loose "not a plain 'teacher'" note into proper Notes prose distinguishing 老師 from [[教師]]. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 老爺.

### 2026-09-05, iteration 2967 — [[words/老爺|老爺]]

No cranberry (爺's own stand-in is this exact compound, but 老's own is [[老]] itself) — transitivity fails, though 爺 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `羅馬字`/`諺文` had lyau'ya/럇야 (the third instance of the 老-syllable mismatch, after [[老人学]] and [[老子]]) — `注音` had stayed correct throughout. Filled blank vietnamese (lão gia, standard attested term). Converted a loose "Stand-in for [[爺]]" note into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 考察.

### 2026-09-05, iteration 2968 — [[words/考察|考察]]

No cranberry (察's own stand-in is this exact compound, but 考's own is [[考慮]]) — transitivity fails, though 察 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (kaucad/캇찯/ㄎㄚㄨㄑㄚㄊ) already verified as the correct concatenation — no bug. All fields already correctly filled — just cleanup: removed blank hsk_level/swadesh/aliases, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 考慮.

### 2026-09-05, iteration 2969 — [[words/考慮|考慮]]

**Genuine `#cranberry` case**: both 考's and 慮's own `stand_in` point to this exact compound. Pronunciation fields (kaulyo/캇료/ㄎㄚㄨㄌ⼄) already verified as the correct concatenation — no bug. Filled blank vietnamese (khảo lự, compositional). Removed blank hsk_level/swadesh, fixed bare-array `characters:`/`aliases:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 考試.

### 2026-09-05, iteration 2970 — [[words/考試|考試]]

No cranberry (試's own stand-in is this exact compound, but 考's own is [[考慮]]) — transitivity fails, though 試 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (kausi/캇시/ㄎㄚㄨㄙㄧ) already verified as the correct concatenation — no bug. All fields already correctly filled — just cleanup: removed blank swadesh, fixed bare-array `characters:`/`aliases:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 而後.

### 2026-09-05, iteration 2971 — [[words/而後|而後]]

No cranberry (both 而's and 後's own `stand_in` point to themselves). Pronunciation fields (nihuo/니훗/ㄋㄧㄏㄨㄛ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `japanese`/`korean` had native paraphrases (その後/그 후) rather than 而後's own attested readings — confirmed via web search that 而後 is genuinely read じご (jigo, using 而's on-reading ジ) in Japanese; corrected japanese to じご and korean to the paralleling compositional 이후. Converted a loose "archaic" comment into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 耐.

### 2026-09-05, iteration 2972 — [[words/耐|耐]]

Single-character stand-in word. Pronunciation fields (nai/내/ㄋㄚㄧ) already matched the character's own values — no bug. Added missing pos/kwin/japanese, filled `vietnamese: null` → nại. Completed the genuine Dan'a'yo homophone with [[乃]] (already perfected, had pre-emptively documented and anticipated this exact pairing) — reciprocal callout already in place, cross-referenced here. **In passing**, cleaned up a stray dangling numbered list left over on `words/乃.md`'s own page (duplicating its single `english:` gloss). No other collisions. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 耳根.

### 2026-09-05, iteration 2973 — [[words/耳根|耳根]]

No cranberry (both 耳's and 根's own `stand_in` point to themselves). **Found and fixed a real bug**: `羅馬字`/`諺文` had nigan/니간 (mismatching 根's real -ǝ- vowel reading, gǝn/근) — `注音` (ㄋㄧㄍㄜㄋ) had stayed correct throughout. All other fields already correctly filled. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 耳目.

### 2026-09-05, iteration 2974 — [[words/耳目|耳目]]

No cranberry (both 耳's and 目's own `stand_in` point to themselves). Pronunciation fields (nimug/니묵/ㄋㄧㄇㄨㄎ) already verified as the correct concatenation — no bug. Filled blank vietnamese (nhĩ mục, standard attested term). Removed blank hsk_level/swadesh/aliases. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 耶.

### 2026-09-05, iteration 2975 — [[words/耶|耶]]

Single-character stand-in word. Pronunciation fields ('ye/여/⼶) already matched the character's own values — no bug. Added missing pos/kwin/japanese (native か); vietnamese was already correctly filled. No homophones (叡/曳/裔/鋭 share the syllable at the character level only). **In passing**, fixed `characters/耶 (char).md`'s Derived Characters section (wrong `###` heading level, non-standard `[text](path)` link format, misplaced before `## Words`) — moved after Words and reformatted to proper ruby wikilinks. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 耽.

### 2026-09-05, iteration 2976 — [[words/耽|耽]]

Single-character stand-in word. Pronunciation fields (dom/돔/ㄉㄛㄇ) already matched the character's own values — no bug. Added missing kwin/japanese (native ふける); pos/vietnamese were already correctly set. **In passing**, added a missing "(stand-in for 耽)" annotation on `characters/耽 (char).md`'s own self-citation. No homophones (彤 shares the syllable at the character level only). Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 聊.

### 2026-09-05, iteration 2977 — [[words/聊|聊]]

Single-character stand-in word. Pronunciation fields (lyau/럇/ㄌ⼘ㄨ) already matched the character's own values — no bug. Added missing kwin/japanese (native いささか). Completed the genuine Dan'a'yo homophone with [[了]] (already perfected, had pre-emptively documented and anticipated this exact pairing, including a note on 了's own corpus-noise vietnamese candidates) — reciprocal callout already in place, cross-referenced here. No other collisions (寮/料/瞭/蓼/遼/陋 share the syllable at the character level only). Stamped `date-last-perfect: 2026-09-05`.

Next: 聖人.

### 2026-09-05, iteration 2978 — [[words/聖人|聖人]]

No cranberry (聖's own stand-in is [[神聖]], 人's is [[人]] itself). Pronunciation fields (singnin/싱닌/ㄙㄧㄫㄋㄧㄋ) already verified as the correct concatenation — no bug. Filled entirely-blank cantonese/vietnamese (compositional, both standard attested terms). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 聘.

### 2026-09-05, iteration 2979 — [[words/聘|聘]]

Single-character stand-in word. Pronunciation fields (ping/핑/ㄆㄧㄫ) already matched the character's own values — no bug. Added missing kwin/japanese (native めす); pos/vietnamese were already correctly set. No homophones (no other character shares this syllable). Stamped `date-last-perfect: 2026-09-05`.

Next: 聚集.

### 2026-09-05, iteration 2980 — [[words/聚集|聚集]]

No cranberry (聚's own stand-in is this exact compound, but 集's own is [[集合]]) — transitivity fails, though 聚 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (cuijib/취집/ㄑㄨㄧㄐㄧㄆ) already verified as the correct concatenation — no bug. Added missing `kwin: true` (entirely absent from the file). Converted a loose "Japanese conflates these two characters" comment into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 聞.

### 2026-09-05, iteration 2981 — [[words/聞|聞]]

Single-character stand-in word. Pronunciation fields (mun/문/ㄇㄨㄋ) already matched the character's own values — no bug. Added missing pos/kwin/japanese (native きく), filled `vietnamese: null` → văn. Completed the 3-way Dan'a'yo homophone group with [[紋]] and [[蚊]] (established earlier this sweep, reciprocal callout already in place) — re-verified complete with the fixed homophone script (吻/問/文 share the syllable at the character level only). **In passing**, added a missing "(stand-in for 聞)" annotation on `characters/聞 (char).md`'s own self-citation. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 聡明.

### 2026-09-05, iteration 2982 — [[words/聡明|聡明]]

No cranberry (聡's own stand-in is this exact compound, but 明's own is [[明]] itself) — transitivity fails, though 聡 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (congmyeng/총명/ㄑㄛㄫㄇ⼶ㄫ) already verified as the correct concatenation — no bug. Fixed the `characters:` list citing bare "明" (a redlink, since the actual page is `明 (char).md`) → "明 (char)". Removed blank hsk_level/swadesh, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 聴.

### 2026-09-05, iteration 2983 — [[words/聴|聴]]

Single-character stand-in word. Pronunciation fields (ceng/청/ㄑㄝㄫ) already matched the character's own values — no bug. Added missing pos/kwin/japanese (native きく); vietnamese left blank since no candidate is stored on the character page at all. Existing homophone callout with [[青]] re-verified as complete with the fixed homophone-check script (庁/錆/鯖 share the syllable at the character level only). **In passing**, added a missing "(stand-in for 聴)" self-citation, absent entirely from `characters/聴 (char).md`'s Words list. Stamped `date-last-perfect: 2026-09-05` on both files.

Next: 聴取.

### 2026-09-05, iteration 2984 — [[words/聴取|聴取]]

No cranberry (聴's own stand-in is [[聴]] itself, 取's is [[取得]]). Pronunciation fields (cengcou/청촛/ㄑㄝㄫㄑㄛㄨ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `cantonese` had teng1 ceoi2, mismatching 聴's real ting1 — corrected to ting1 ceoi2. Vietnamese deliberately left blank since 聴's own character page has no candidate stored at all. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 職業.

### 2026-09-05, iteration 2985 — [[words/職業|職業]]

No cranberry (職's own stand-in is this exact compound, but 業's own is [[業]] itself) — transitivity fails, though 職 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (jig'eb/직업/ㄐㄧㄎㄝㄆ) already verified as the correct concatenation — no bug. Fixed the `characters:` list citing bare "業" (a redlink, since the actual page is `業 (char).md`) → "業 (char)". Removed blank hsk_level/swadesh, fixed bare-array `characters:` YAML formatting. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肇造.

### 2026-09-05, iteration 2986 — [[words/肇造|肇造]]

No cranberry (肇's own stand-in is this exact compound, but 造's own is [[創造]]) — transitivity fails, though 肇 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (jaucau/잣찻/ㄐㄚㄨ·ㄑㄚㄨ) already verified as the correct concatenation — no bug. All other-language fields (including the pre-existing cantonese) confirmed standard and genuinely compositional. Filled blank vietnamese (triệu tạo, compositional), added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肉桂.

### 2026-09-05, iteration 2987 — [[words/肉桂|肉桂]]

No cranberry (桂's own stand-in is this exact compound, but 肉's own is [[肉]] itself) — transitivity fails, though 桂 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (nuggwei/눅궤/ㄋㄨㄎㄍ⼔ㄧ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `korean` had 계피, the real word for cinnamon but built from the unrelated compound 桂皮 rather than 肉桂's own compositional reading — corrected to 육계 (the real pharmacological Sino-Korean term). Filled blank vietnamese (nhục quế, standard attested term). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肉汁.

### 2026-09-05, iteration 2988 — [[words/肉汁|肉汁]]

No cranberry (both 肉's and 汁's own `stand_in` point to themselves). **Found and fixed two real bugs**: `羅馬字`/`諺文` had nugjib/눅집, mismatching 汁's real -ǝ- vowel reading (jǝb/즙) — `注音` (ㄋㄨㄎㄐㄜㄆ) had stayed correct throughout; `korean`/`vietnamese` had 그레이비 (an English loanword transliteration of "gravy") and nước chấm (an unrelated native Vietnamese dipping-sauce term) rather than 肉汁's own compositional readings — corrected to 육즙/nhục trấp. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肉湯.

### 2026-09-05, iteration 2989 — [[words/肉湯|肉湯]]

No cranberry (both 肉's and 湯's own `stand_in` point to themselves). Pronunciation fields (nugtang/눅탕/ㄋㄨㄎㄊㄚㄫ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `korean` had 국물, the everyday native word for "broth" rather than 肉湯's own compositional reading — corrected to 육탕. Filled blank japanese/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肋骨.

### 2026-09-05, iteration 2990 — [[words/肋骨|肋骨]]

No cranberry (肋's own stand-in is this exact compound, but 骨's own is [[骨]] itself) — transitivity fails, though 肋 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed two real bugs**: `羅馬字` had luggod (mismatching 肋's real -ǝ- vowel, lǝg — 諺文/注音 had already been correct, an unusual single-field-only instance of this bug); `kwin` was true, but the AND-rule requires false. Filled blank cantonese/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肌理.

### 2026-09-05, iteration 2991 — [[words/肌理|肌理]]

No cranberry (肌's own stand-in is [[肌膚]], 理's is [[理由]]). Pronunciation fields (giǝli/긔리/ㄍㄧㄜㄌㄧ) already verified as the correct concatenation — no bug. Fixed a comma-joined `japanese` string (きめ, きり — both genuine readings) into a proper list. Filled blank korean (기리, compositional and attested) and vietnamese (cơ lý), added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肌膚.

### 2026-09-05, iteration 2992 — [[words/肌膚|肌膚]]

No cranberry (肌's own stand-in is this exact compound, but 膚's own is [[皮膚]]) — transitivity fails, though 肌 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `羅馬字`/`諺文` had giǝpu/긔푸 (p-initial), mismatching 膚's real f-initial reading (fǝ/쁘) — `注音` (ㄍㄧㄜㄈㄜ) had stayed correct throughout, matching the ㄈ→ㅃ p/f-confusion class seen repeatedly this session. Filled blank korean/vietnamese, added missing `kwin: false`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肖像.

### 2026-09-05, iteration 2993 — [[words/肖像|肖像]]

No cranberry (肖's own stand-in is this exact compound, but 像's own is [[彫像]]) — transitivity fails, though 肖 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (syousyang/숏샹/ㄙ⼄ㄨㄙ⼘ㄫ) already verified as the correct concatenation — no bug. Fixed a blank `pos:` field (→ 名詞). Filled blank vietnamese (tiếu tượng, compositional). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肘.

### 2026-09-05, iteration 2994 — [[words/肘|肘]]

Single-character stand-in word. Pronunciation fields (jum/줌/ㄐㄨㄇ) already matched the character's own values — no bug. Added missing pos/kwin/japanese, filled `vietnamese: null` → khuỷu. Found a genuine homophone with [[朕]] ("we, royal") — an already-perfected but old (2026-03-29) pass that predates this session's homophone-check convention and had no callout at all; added reciprocal callouts to both, and while touching 朕.md also fixed a bare-string `characters:` field, removed a redundant duplicate `品詞`, and quoted several previously-unquoted string fields. **In passing**, fixed the 18th empty-string field bug on `characters/肘 (char).md` (`hsk_level: ""` → "無"). Stamped `date-last-perfect: 2026-09-05` on all three files.

Next: 股.

### 2026-09-05, iteration 2995 — [[words/股|股]]

Single-character stand-in word, old bare-string `characters:` format rewritten into current template. Pronunciation fields (go/고/ㄍㄛ) already matched the character's own values — no bug. Added missing pos/kwin/japanese (こ, on'yomi matching the same reading used on [[鼓]]). Re-verified the existing 3-way homophone group with [[鼓]] and [[錮]] (already fully cross-linked from 鼓's earlier perfecting pass, which had also confirmed no fourth homophone exists among the other ㄍㄛ-reading characters). Wrote full Notes covering the 會意 etymology and the 溝股/Pythagorean-Theorem citation. Stamped `date-last-perfect: 2026-09-05`.

Next: 肢体.

### 2026-09-05, iteration 2996 — [[words/肢体|肢体]]

No cranberry (肢's own stand-in is this exact compound, but 体's own is [[体系]]) — transitivity fails, though 肢 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (jetei/저테/ㄐㄝㄊㄝㄧ) already verified as the correct concatenation — no bug; `kwin: false` already correct per the AND-rule. Filled blank cantonese (zi1tai2) and vietnamese (chi thể, standard attested term). Removed blank `hsk_level`/`swadesh` (character-page-only fields, not standard on word pages), converted bare-array `characters:`/`aliases:` YAML to proper list formatting, renamed `## Etymology`→`## Notes`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肥大.

### 2026-09-05, iteration 2997 — [[words/肥大|肥大]]

No cranberry (肥's own stand-in is [[肥満]], 大's own is [[大]] itself) — neither constituent legitimized by this word. Pronunciation fields (buidai/뷔대/ㄅㄨㄧㄉㄚㄧ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule: 肥 is false despite 大 being true). Removed a stray space from `cantonese` (fei4 daai6→fei4daai6), quoted several previously-unquoted string fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肥桶.

### 2026-09-05, iteration 2998 — [[words/肥桶|肥桶]]

No cranberry (肥's own stand-in is [[肥満]], 桶's own is [[桶]] itself) — neither constituent legitimized by this word. Pronunciation fields (buitong/뷔통/ㄅㄨㄧㄊㄛㄫ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule: 肥 is false despite 桶 being true). Removed a stray space from `cantonese` (fei4 tung2→fei4tung2), quoted several previously-unquoted string fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肥満.

### 2026-09-05, iteration 2999 — [[words/肥満|肥満]]

No cranberry (肥's own stand-in is this exact compound, but 満's own is [[満]] itself) — transitivity fails, though 肥 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (buiman/뷔만/ㄅㄨㄧㄇㄚㄋ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule: 肥 is false despite 満 being true). Removed a stray space from `cantonese` (fei4 mun5→fei4mun5), quoted several previously-unquoted string fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肥育.

### 2026-09-05, iteration 3000 — [[words/肥育|肥育]]

No cranberry (肥's own stand-in is [[肥満]], 育's own is [[育]] itself) — neither constituent legitimized by this word. Pronunciation fields (bui'yug/뷔육/ㄅㄨㄧ·⼜ㄎ) already verified as the correct concatenation, including the null-onset syllable break — no bug. Added missing `kwin: false` (AND-rule: 肥 is false despite 育 being true). Removed a stray space from `cantonese` (fei4 juk6→fei4juk6), quoted several previously-unquoted string fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肥脊.

### 2026-09-05, iteration 3001 — [[words/肥脊|肥脊]]

No cranberry (肥's own stand-in is [[肥満]], 脊's own is [[脊椎]]) — neither constituent legitimized by this word. Pronunciation fields (buijeg/뷔적/ㄅㄨㄧㄐㄝㄎ) already verified as the correct concatenation — no bug. **Found and fixed two real bugs**: `cantonese` had zik1 instead of 脊's own zik3 (fei4 zik1→fei4zik3); `vietnamese` had tịch instead of 脊's own tích (phì tịch→phì tích). Added missing `kwin: false` (AND-rule). Kept the word's already-thorough existing Notes (documents 脊 standing in for its own alias 瘠 via the shared Dan'a'yo syllable). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肩甲骨.

### 2026-09-05, iteration 3002 — [[words/肩甲骨|肩甲骨]]

No cranberry (none of the three constituents' own stand-ins point here — 肩/甲/骨 all point to themselves). Pronunciation fields (gengabgod/건갑곧/ㄍㄝㄋㄍㄚㄆㄍㄛㄊ) already verified as the correct concatenation — no bug; `kwin: false` already correct per the AND-rule. **Found and fixed three real bugs**: `mandarin`/`cantonese`/`korean` were all truncated, missing 骨's own final syllable entirely (jiānjiǎ→jiānjiǎgǔ; gin1 gaap3→gin1gaap3gwat1; 견갑→견갑골). Fixed redlinked bare-character citations in `characters:` (肩/甲/骨→disambiguated `(char)` filenames — these bare names belong to the *word* pages, not the character pages). Filled blank vietnamese (kiên giáp cốt). Fixed `aliases`: removed 肩膀 (an unrelated near-synonym meaning "shoulder," not "shoulder blade") and corrected truncated 肩胛→肩胛骨 (the genuine modern-standard alternate spelling, using specialized 胛 in place of the phonetic loan 甲). Removed blank hsk_level/swadesh. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肩章.

### 2026-09-05, iteration 3003 — [[words/肩章|肩章]]

No cranberry (肩's own stand-in is [[肩]] itself, 章's own is [[章]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `諺文` had 겅장, an illegal cross-syllable nasal-place assimilation of 肩's own final ㄴ→ㅇ (forbidden per `grammar/文法 - 02音韻論.md` line 150) — corrected to the straight concatenation 건장; `羅馬字`/`注音` had already stayed correct throughout. `kwin: false` already correct per the AND-rule. Filled blank pos and vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`. **Tooling note**: the vault's filesystem is running unusually slow right now (~85s just to scan all of `words/`+`characters/` once) — `homophone_check.py` timed out and was killed twice before recognizing it wasn't hung, just slow; ran to completion fine in the background on the third attempt. Not an infinite loop — just budget more wall-clock time (backgrounded, don't kill early) if this recurs.

Next: 肪.

### 2026-09-05, iteration 3004 — [[words/肪|肪]]

Single-character stand-in word. Pronunciation fields (fang/빵/ㄈㄚㄫ) already matched the character's own values — no bug. Added missing pos/japanese (ボウ, on-reading since no native kun exists), filled `vietnamese: null`→phòng. Re-verified the genuine homophone with [[紡]] (already fully cross-linked from 紡's own retroactive-recheck pass), and confirmed no third homophone exists among the other ㄈㄚㄫ-reading characters (倣/坊/妨/放/方/芳/訪 — none has a self-pointing `stand_in`). Stamped `date-last-perfect: 2026-09-05`.

Next: 育.

### 2026-09-05, iteration 3005 — [[words/育|育]]

Single-character stand-in word. **Found and fixed a real bug**: `羅馬字` was missing the leading null-onset apostrophe (yug→'yug; 諺文/注音 already correct). Fixed a typo in `english` (nuture→nurture), added missing pos/japanese (そだつ, native kun-reading), filled `vietnamese: null`→dục, added missing `kwin: true`. Checked the one other ⼜ㄎ-reading character, 郁 — its `stand_in` is the special `名専字` (name-only) marker, not a real word, so no homophone. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 肺臓.

### 2026-09-05, iteration 3006 — [[words/肺臓|肺臓]]

No cranberry (肺's own stand-in is this exact compound, but 臓's own is [[内臓]]) — transitivity fails, though 肺 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed two real bugs**: `羅馬字`/`諺文` had pyejang/펴장 (p-initial), mismatching 肺's real f-initial reading (fe/뻐) — same ㄈ→ㅍ (should be ㅃ) failure class as the 福-family bug; `注音` had already stayed correct. `korean` had 폐장; 허파, wrongly appending 肺's own native gloss 허파 onto the correct compositional 폐장 — trimmed to just 폐장. Filled blank vietnamese (phế tạng). Added missing `kwin: false` (AND-rule: 肺 is false despite 臓 being true), removed a stray space from cantonese, converted bare-array YAML. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胃.

### 2026-09-05, iteration 3007 — [[words/胃|胃]]

Single-character stand-in word. Pronunciation fields (wi/위/ㄨㄧ) already matched the character's own values — no bug. Added missing pos/japanese (イ, on-reading since no native kun exists), filled `vietnamese: null`→vị. Checked the six other ㄨㄧ-reading characters (偉/囲/緯/謂/違/韋) — none has a self-pointing `stand_in` (韋's is the special `名専字` name-only marker), so no homophone. Stamped `date-last-perfect: 2026-09-05`.

Next: 胃炎.

### 2026-09-05, iteration 3008 — [[words/胃炎|胃炎]]

No cranberry (胃's own stand-in is [[胃]] itself, 炎's own is [[炎症]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had a spurious extra leading apostrophe ('wi'em) — 胃's own reading (wi) carries no null-onset marker, only 炎's own ('em) does — corrected to wi'em; `諺文`/`注音` had already stayed correct. Filled blank pos, korean (위염, the real attested medical term), and vietnamese (vị viêm). Added missing `kwin: false` (AND-rule: 炎 is false despite 胃 being true). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胃痛.

### 2026-09-05, iteration 3009 — [[words/胃痛|胃痛]]

No cranberry (胃's own stand-in is [[胃]] itself, 痛's own is [[苦痛]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had a spurious extra leading apostrophe ('witong), same class as 胃炎's fix two iterations ago — corrected to witong; `諺文`/`注音` had already stayed correct. `kwin: true` was already correct (both constituents individually true). Filled blank pos and vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胃癌.

### 2026-09-05, iteration 3010 — [[words/胃癌|胃癌]]

No cranberry (胃's own stand-in is [[胃]] itself, 癌's own is [[癌症]]) — neither constituent legitimized by this word. **Found and fixed two real bugs**: `羅馬字` had a spurious extra leading apostrophe ('wi'am), same class as 胃炎/胃痛's earlier fixes — corrected to wi'am; `諺文`/`注音` had already stayed correct. `mandarin` was comma-joined with a stray second value, wèiyán — the *pre-1962* reading of 癌 (documented on `characters/癌.md`: Mandarin ái was a deliberate 1962 change away from yán specifically to avoid clinical confusion with homophonous 炎, i.e. with [[胃炎]]), not a live alternate — trimmed to just wèi'ái. Filled blank vietnamese (vị nham). `kwin: true` already correct. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胃酸.

### 2026-09-05, iteration 3011 — [[words/胃酸|胃酸]]

No cranberry (胃's own stand-in is [[胃]] itself, 酸's own is [[酸]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had a spurious extra leading apostrophe ('wiswan), same recurring class as the last three 胃-compounds — corrected to wiswan; `諺文`/`注音` had already stayed correct. Filled blank pos and vietnamese. `kwin: false` already correct per the AND-rule. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胆嚢.

### 2026-09-05, iteration 3012 — [[words/胆嚢|胆嚢]]

**Genuine `#cranberry`**: both 胆's and 嚢's own stand-ins point here (3rd cranberry found this session, after [[程度]]/[[種類]]). Pronunciation fields (damnang/담낭/ㄉㄚㄇㄋㄚㄫ) already verified as the correct concatenation. **Found and fixed a real bug**: `kwin` was stored true, but the AND-rule requires false (胆 is individually false despite 嚢 being true). Filled blank vietnamese (đảm nang). Fixed a missing "(stand-in for 嚢)" annotation on `characters/嚢.md`'s own Words-list citation. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 背.

### 2026-09-05, iteration 3013 — [[words/背|背]]

Single-character stand-in word. Pronunciation fields (boi/뵈/ㄅㄛㄧ) already matched the character's own values — no bug. Added missing pos/japanese (せなか, native kun-reading), filled `vietnamese: null`→bối. Found a genuine **three-way homophone group** with [[杯]] (already perfected but missing its callout, now added) and [[陪]] (still otherwise unperfected — gave it a full pass too: fixed pos/kwin/japanese/vietnamese, fixed missing stand-in annotation on `characters/陪 (char).md`). All three coincide at boi/뵈/ㄅㄛㄧ and share the same Sino-Korean reading 배 as well. Checked the two other ㄅㄛㄧ-reading characters, 悖 and 賠 — neither has a self-pointing `stand_in` (悖's is the special `名専字` marker, 賠's own is [[賠償]]), so no fourth homophone. Stamped `date-last-perfect: 2026-09-05` on all three word pages.

Next: 背後.

### 2026-09-05, iteration 3014 — [[words/背後|背後]]

No cranberry (背's own stand-in is [[背]] itself, 後's own is [[後]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字`/`諺文`/`注音` all had a vowel-order transposition on 後's own syllable (hou/홋/ㄏㄛㄨ instead of the character's real huo/훗/ㄏㄨㄛ) — corrected to boihuo/뵈훗/ㄅㄛㄧㄏㄨㄛ. Flagged the same transposition on several other 後-citations (最後, 以後, 前後 on 後's own character page) for a future check when the sweep reaches them. `kwin: false` already correct. Filled blank vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 背景.

### 2026-09-05, iteration 3015 — [[words/背景|背景]]

No cranberry (背's own stand-in is [[背]] itself, 景's own is [[景色]]) — neither constituent legitimized by this word. Pronunciation fields (boigyeng/뵈경/ㄅㄛㄧㄍ⼶ㄫ) already verified as the correct concatenation — no bug; `kwin: false` already correct per the AND-rule. Removed a redundant `品詞` duplicate of `pos`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 背骨.

### 2026-09-05, iteration 3016 — [[words/背骨|背骨]]

No cranberry (背's own stand-in is [[背]] itself, 骨's own is [[骨]] itself) — neither constituent legitimized by this word. Pronunciation fields (boigod/뵈곧/ㄅㄛㄧㄍㄛㄊ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule: both constituents individually false). Filled blank cantonese and vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胎児.

### 2026-09-05, iteration 3017 — [[words/胎児|胎児]]

No cranberry (胎's own stand-in is this exact compound, but 児's own is [[児]] itself) — transitivity fails, though 胎 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `諺文` had 타에 (ㅏ vowel), mismatching 胎's real ㅐ-vowel reading (태) — corrected to 태에; `羅馬字`/`注音` had already stayed correct. Also cleaned a stray zero-width-space character embedded in `japanese`. Filled blank pos. `kwin: false` already correct per the AND-rule. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胎盤.

### 2026-09-05, iteration 3018 — [[words/胎盤|胎盤]]

No cranberry (胎's own stand-in is [[胎児]], 盤's own is [[盤]] itself) — neither constituent legitimized by this word. Pronunciation fields (taiban/태반/ㄊㄚㄧㄅㄚㄋ) already verified as the correct concatenation — no bug; `kwin: true` already correct. Filled blank pos and vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胞衣.

### 2026-09-05, iteration 3019 — [[words/胞衣|胞衣]]

No cranberry (胞's own stand-in is this exact compound, but 衣's own is [[衣類]]) — transitivity fails, though 胞 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (byau'iǝ/뱟의/ㄅ⼘ㄨㄧㄜ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule: 胞 is false despite 衣 being true). Filled blank vietnamese (bào y, the classical Sino-Vietnamese medical term). Confirmed japanese えな is a genuine irregular reading (熟字訓-type), not a bug. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胡志明市.

### 2026-09-05, iteration 3020 — [[words/胡志明市|胡志明市]]

No cranberry (none of the four constituents' own stand-ins point here). **Found and fixed a real bug**: `羅馬字`/`諺文` had ho/호 instead of 胡's real reading hou/홋 — corrected to houjimyengsi/홋지명시; `注音` had already stayed correct throughout. `kwin: false` already correct per the AND-rule. Filled blank cantonese. As a proper place name, mandarin/japanese/korean/vietnamese legitimately hold the real attested name/transliteration rather than a compositional gloss. Fixed a malformed plain-link citation (missing ruby/rt formatting) on `characters/胡.md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胡瓜.

### 2026-09-05, iteration 3021 — [[words/胡瓜|胡瓜]]

No cranberry (瓜's own stand-in is this exact compound, but 胡's own is [[胡乱]]) — transitivity fails, though 瓜 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `羅馬字` was missing 胡's own -u- glide (hogwa→hougwa) — a rare single-field-only instance, since `諺文`/`注音` had already stayed correct. `kwin: false` already correct. Converted `japanese`'s semicolon-joined value (きゅうり/きうり) into a proper list — both are genuine irregular readings, neither compositional. Kept `korean` 오이 as the real native word (matches 瓜's own `korean_native`), not a bug. Filled blank vietnamese (hồ qua). Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胡芦.

### 2026-09-05, iteration 3022 — [[words/胡芦|胡芦]]

No cranberry (胡's own stand-in is [[胡乱]], 芦's own is [[芦葦]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` was missing 胡's own -u- glide (holo→houlo), same single-field-only class as [[胡瓜]]'s fix — `諺文`/`注音` had already stayed correct. `kwin: false` already correct. Verified vietnamese hồ lô is a genuine attested loanword (not compositional from 芦's own "lư," but independently real) — not a bug. Fixed cantonese's stray space. Removed blank hsk_level/swadesh. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胡麻.

### 2026-09-05, iteration 3023 — [[words/胡麻|胡麻]]

No cranberry (胡's own stand-in is [[胡乱]], 麻's own is [[大麻]]) — neither constituent legitimized by this word. **Found and fixed several real bugs**: `羅馬字` missing 胡's -u- glide (homa→houma), 3rd occurrence of this exact bug in a row across the 胡-compounds ([[胡瓜]], [[胡芦]], now this). `mandarin`/`cantonese` had been contaminated with the alias 芝麻's own readings (hīma/zi1 ma2→húmá/wu4maa4). `korean` held a native phrase (참깨속) instead of the real Sino-Korean term 호마. Filled blank vietnamese (hồ ma). Japanese ごま (using 胡's alternate on'yomi GO) was already correct. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胰臓.

### 2026-09-05, iteration 3024 — [[words/胰臓|胰臓]]

No cranberry (胰's own stand-in is this exact compound, but 臓's own is [[内臓]]) — transitivity fails, though 胰 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields ('iǝjang/의장/ㄧㄜㄐㄚㄫ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Converted comma-joined vietnamese to a list. Verified that japanese すいぞう/korean 췌장/vietnamese tụy are all genuine attested readings tied to the alias spelling 膵臓 (a Japanese kokuji distinct from 胰) rather than compositional derivations or bugs — documented in Notes, not "fixed." Fixed a missing "(stand-in for 胰)" annotation on `characters/胰.md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 胸臆.

### 2026-09-05, iteration 3025 — [[words/胸臆|胸臆]]

No cranberry (臆's own stand-in is this exact compound, but 胸's own is [[胸部]]) — transitivity fails, though 臆 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (hyong'ig/횽익/ㄏ⼄ㄫㄧㄎ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank cantonese and vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 能力.

### 2026-09-05, iteration 3026 — [[words/能力|能力]]

No cranberry (能's own stand-in is [[技能]], 力's own is [[力]] itself) — neither constituent legitimized by this word. Pronunciation fields (nǝnglig/능릭/ㄋㄜㄫㄌㄧㄎ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Body was already unusually thorough — kept nearly all of it, just added the opening cranberry-check bullet and quoted pronunciation fields, fixed cantonese stray space. Fixed a missing "(stand-in for 力)" annotation on `characters/力 (char).md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 脊椎.

### 2026-09-05, iteration 3027 — [[words/脊椎|脊椎]]

**Genuine `#cranberry`**: both 脊's and 椎's own stand-ins point here (4th cranberry this session, after [[程度]]/[[種類]]/[[胆嚢]]). Pronunciation fields (jegcui/적취/ㄐㄝㄎㄑㄨㄧ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Converted comma-joined mandarin (jǐzhuī, jízhuī — a genuinely attested dual reading) and cantonese (matching zek3/zik3 variation) into proper lists. Filled blank vietnamese. Fixed a missing "(stand-in for 椎)" annotation on `characters/椎.md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 脚.

### 2026-09-05, iteration 3028 — [[words/脚|脚]]

Single-character stand-in word. Pronunciation fields (gyag/갹/ㄍ⼘ㄎ) already matched the character's own values — no bug. Added missing pos/japanese (あし, native kun-reading), filled `vietnamese: null`→cước. Fixed a missing "(stand-in for 脚)" annotation on the char page's own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 脚踝.

### 2026-09-05, iteration 3029 — [[words/脚踝|脚踝]]

No cranberry (踝's own stand-in is this exact compound, but 脚's own is [[脚]] itself) — transitivity fails, though 踝 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (gyaghwa/갹화/ㄍ⼘ㄎㄏ⺢) already verified as the correct concatenation — no bug; `kwin: false` already correct. Converted comma-joined japanese and vietnamese into proper lists — all real attested native terms, none compositional. Verified korean 발목 as a genuine real word (not a bug). Fixed cantonese stray space. Fixed a completely missing `## Words` section on `characters/踝.md` (added the stand-in citation). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 脱.

### 2026-09-05, iteration 3030 — [[words/脱|脱]]

Single-character stand-in word. Pronunciation fields (dwad/돧/ㄉ⺢ㄊ) already matched the character's own values — no bug. **Found and fixed two real bugs**: `korean` and `vietnamese` both held the literal string `"null"` — fixed to 탈 and thoát respectively. Added missing pos/japanese (ぬぐ, native kun-reading). Fixed a self-citation entirely missing from the char page's own Words list (only 脱稿 had been listed). Checked the one other ㄉ⺢ㄊ-reading character, 奪 — its own `stand_in` is [[奪取]], so no homophone. Stamped `date-last-perfect: 2026-09-05`.

Next: 脱稿.

### 2026-09-05, iteration 3031 — [[words/脱稿|脱稿]]

No cranberry (脱's own stand-in is [[脱]] itself, 稿's own is [[稿]] itself) — neither constituent legitimized by this word. Pronunciation fields (dwadgau/돧갓/ㄉ⺢ㄊㄍㄚㄨ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 脳.

### 2026-09-05, iteration 3032 — [[words/脳|脳]]

Single-character stand-in word. Pronunciation fields (nau/낫/ㄋㄚㄨ) already matched the character's own values — no bug. **Found and fixed two real bugs**: `korean` and `vietnamese` both held the literal string `"null"` — fixed to 뇌 and não. Added missing pos/japanese (なずき). Found a genuine homophone with [[悩]] ("angered, mad," already perfected but missing its callout) — added reciprocal callouts to both. No homophones beyond that. Stamped `date-last-perfect: 2026-09-05`.

Next: 脹脛.

### 2026-09-05, iteration 3033 — [[words/脹脛|脹脛]]

No cranberry (脹's own stand-in is [[腫脹]], 脛's own is [[脛骨]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `mandarin` had been contaminated with the alias 小腿's own reading (xiǎotuǐ) instead of the compositional zhàngjìng. Fixed cantonese's stray space (using 脛's own ging3 of its two stored candidates). Filled blank vietnamese. Verified japanese ふくらはぎ/korean 종아리 as genuine attested native terms, not bugs. Fixed a plain-link citation on `characters/脹.md` and a completely missing citation on `characters/脛.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 脾臓.

### 2026-09-05, iteration 3034 — [[words/脾臓|脾臓]]

No cranberry (脾's own stand-in is this exact compound, but 臓's own is [[内臓]]) — transitivity fails, though 脾 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (bijang/비장/ㄅㄧㄐㄚㄫ) already verified as the correct concatenation — no bug; `kwin: true` already correct. Filled blank vietnamese. Incorporated a stray body sentence about the TCM spleen/pancreas conflation into proper Notes prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 腎臓.

### 2026-09-05, iteration 3035 — [[words/腎臓|腎臓]]

No cranberry (腎's own stand-in is this exact compound, but 臓's own is [[内臓]]) — transitivity fails, though 腎 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `cantonese` had san6, mismatching 腎's own san5 (a tone error) — corrected to san5zong6. `kwin: true` already correct. Filled blank vietnamese. Re-verified the existing homophone with [[伸長]] — confirmed no third word shares this reading. Stamped `date-last-perfect: 2026-09-05`.

Next: 腕.

### 2026-09-05, iteration 3036 — [[words/腕|腕]]

Single-character stand-in word. Pronunciation fields ('wan/완/⺢ㄋ) already matched the character's own values — no bug. Added missing pos/japanese (うで, native kun-reading), filled `vietnamese: null`→oản. Re-verified the existing homophone with [[碗]] (already fully cross-linked). Checked the three other ⺢ㄋ-reading characters (玩, 翫, 頑) — none has a self-pointing `stand_in`, confirming no third homophone. Stamped `date-last-perfect: 2026-09-05`.

Next: 腫脹.

### 2026-09-05, iteration 3037 — [[words/腫脹|腫脹]]

No cranberry (脹's own stand-in is this exact compound, but 腫's own is [[腫瘍]]) — transitivity fails, though 脹 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (jongcang/종창/ㄐㄛㄫㄑㄚㄫ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `kwin` was false, but the AND-rule requires true (both constituents individually true). Fixed cantonese's stray space. Fixed a missing citation on `characters/腫.md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 腰部.

### 2026-09-05, iteration 3038 — [[words/腰部|腰部]]

No cranberry (腰's own stand-in is this exact compound, but 部's own is [[部]] itself) — transitivity fails, though 腰 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields ('youbou/욧봇/⼄ㄨㄅㄛㄨ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese (yêu bộ, using 腰's alternate reading). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 腰骨.

### 2026-09-05, iteration 3039 — [[words/腰骨|腰骨]]

No cranberry (腰's own stand-in is [[腰部]], 骨's own is [[骨]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `mandarin`/`cantonese`/`korean`/`vietnamese` had all been contaminated with the alias 髋骨's own readings (kuāngǔ/fun1 gwat1/관골; 볼기뼈/Xương chậu) instead of the compositional yāogǔ/jiu1gwat1/요골/yêu cốt — same class as [[脹脛]]'s earlier mandarin fix, but affecting all four fields here. Noted korean 요골 is a coincidental false friend (real word for "radius," unrelated). Japanese こしぼね was already correct. Pronunciation fields ('yougod/욧곧/⼄ㄨㄍㄛㄊ) already verified as the correct concatenation. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 腹.

### 2026-09-05, iteration 3040 — [[words/腹|腹]]

Single-character stand-in word — closes the previously-flagged known gap. Pronunciation fields (fug/뿍/ㄈㄨㄎ) already matched the character's own values — no bug. Added missing pos/japanese (はら, native kun-reading), filled `vietnamese: null`→phúc. Re-verified the existing 3-way homophone group with [[福]]/[[副]] (already fully cross-linked). Checked the three other ㄈㄨㄎ-reading characters (幅, 蝠, 覆) — none has a self-pointing `stand_in`, confirming no fourth homophone. Fixed a missing "(stand-in for 腹)" annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 腹部.

### 2026-09-05, iteration 3041 — [[words/腹部|腹部]]

No cranberry (腹's own stand-in is [[腹]] itself, 部's own is [[部]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had bugbou — an exact copy-paste of the unrelated word [[北部]]'s own reading — instead of the correct fugbou (腹's real f-initial); `諺文`/`注音` had already stayed correct. This meant the pre-existing "homophone of 北部" claim was spurious (北部 is bugbou/북봇/ㄅㄨㄎㄅㄛㄨ, genuinely different) — removed the false claim from both pages. Filled blank vietnamese. No genuine homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 膃肭.

### 2026-09-05, iteration 3042 — [[words/膃肭|膃肭]]

**Genuine `#cranberry`** (already correctly tagged): both 腽's and 肭's own stand-ins point here (5th cranberry this session, after [[程度]]/[[種類]]/[[胆嚢]]/[[脊椎]]). Pronunciation fields ('wabnud/왑눋/⺢ㄆㄋㄨㄊ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Added a completely missing vietnamese field (oát nạp, compositional). Fixed missing "(stand-in for X)" annotations on both `characters/腽.md` and `characters/肭.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 膣.

### 2026-09-05, iteration 3043 — [[words/膣|膣]]

Single-character stand-in word. Pronunciation fields (jid/짇/ㄐㄧㄊ) already matched the character's own values — no bug. Confirmed english "cunt" is intentional (char page explicitly documents this as the vulgar term, distinct from neutral [[陰道]]). **Found and fixed a real bug**: character page's `japanese_native: ちち` was unverifiable/almost certainly erroneous (no real dictionary attests ちち for this meaning) — corrected to `ø`, and set the word's own japanese to the on-reading チツ. Removed redundant `品詞`, normalized the header to the standard `>[!tip]` format. Fixed a self-citation entirely missing from the char page's own Words list. Re-verified the existing 3-way homophone group with [[直]]/[[蛭]] and confirmed no fourth homophone among the other ㄐㄧㄊ-reading characters (嫉, 疾, 質). Stamped `date-last-perfect: 2026-09-05`.

Next: 膿.

### 2026-09-05, iteration 3044 — [[words/膿|膿]]

Single-character stand-in word. Pronunciation fields (nong/농/ㄋㄛㄫ) already matched the character's own values — no bug. Added missing pos/japanese (う, native kun-reading), filled `vietnamese: null`→nung. Checked the two other ㄋㄛㄫ-reading characters (濃, 農) — neither has a self-pointing `stand_in`, confirming no homophone. Fixed a missing "(stand-in for 膿)" annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 臘月.

### 2026-09-05, iteration 3045 — [[words/臘月|臘月]]

No cranberry (臘's own stand-in is [[臘八]], 月's own is [[月]] itself) — neither constituent legitimized by this word. Pronunciation fields (lab'wed/랍웓/ㄌㄚㄆ·⼔ㄊ) already verified as the correct concatenation — no bug; `kwin: false` already correct. **Found and fixed a real bug**: `korean` had 납월, a 두음법칙-shifted (South Korean) form — corrected to 랍월 per the vault's standing North-Korean-pronunciation rule. Fixed cantonese's stray space, removed redundant `品詞`. Verified vietnamese tháng Chạp as a genuine attested native term, not a bug. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 臣民.

### 2026-09-05, iteration 3046 — [[words/臣民|臣民]]

No cranberry (臣's own stand-in is [[大臣]], 民's own is [[人民]]) — neither constituent legitimized by this word. Pronunciation fields (sinmin/신민/ㄙㄧㄋㄇㄧㄋ) already verified as the correct concatenation — no bug; `kwin: true` already correct. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自主.

### 2026-09-05, iteration 3047 — [[words/自主|自主]]

No cranberry (自's own stand-in is [[自身]], 主's own is [[主人]]) — neither constituent legitimized by this word. Pronunciation fields (jiǝju/즤주/ㄐㄧㄜㄐㄨ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自分.

### 2026-09-05, iteration 3048 — [[words/自分|自分]]

No cranberry (自's own stand-in is [[自身]], 分's own is [[分]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝbun/즤분/ㄐㄧㄜㄅㄨㄋ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule). Mandarin zìfèn uses 分's genuine alternate fèn tone (the "status/duty" sense) rather than the character's stored primary fēn — not a bug. Filled blank cantonese/korean/vietnamese. Verified japanese じぶん as the real, common Japanese word (broader meaning "oneself" than the narrower literary Chinese sense here) — not a bug. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自制.

### 2026-09-05, iteration 3049 — [[words/自制|自制]]

No cranberry (自's own stand-in is [[自身]], 制's own is [[抑制]]) — neither constituent legitimized by this word. Pronunciation fields (jiǝjei/즤제/ㄐㄧㄜㄐㄝㄧ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自動詞.
