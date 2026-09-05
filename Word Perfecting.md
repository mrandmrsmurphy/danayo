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
