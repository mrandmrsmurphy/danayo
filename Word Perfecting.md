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

### 2026-09-05, iteration 3050 — [[words/自動詞|自動詞]]

No cranberry (none of the three constituents' own stand-ins point here). Pronunciation fields (jiǝdongsa/즤동사/ㄐㄧㄜㄉㄛㄫㄙㄚ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese (tự động từ, matching the established grammatical-term convention). Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自動車.

### 2026-09-05, iteration 3051 — [[words/自動車|自動車]]

No cranberry (none of the three constituents' own stand-ins point here). **Found and fixed two real bugs**: `羅馬字` missing 車's own -w- glide (jiǝdongca→jiǝdongcwa; 諺文/注音 had already stayed correct — rare single-field-only instance); `japanese` had じどうしや (small-kana error) instead of じどうしゃ. Fixed redlinked bare-character citations in `characters:` (動/車→disambiguated `(char)` filenames). Fixed cantonese's stray spaces. Filled blank vietnamese. `kwin: false` already correct. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自在.

### 2026-09-05, iteration 3052 — [[words/自在|自在]]

No cranberry (自's own stand-in is [[自身]], 在's own is [[在]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝjai/즤재/ㄐㄧㄜㄐㄚㄧ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed a redlinked bare-character citation (在→在 (char)). Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自得.

### 2026-09-05, iteration 3053 — [[words/自得|自得]]

No cranberry (自's own stand-in is [[自身]], 得's own is [[獲得]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had jiǝdug (d-initial, wrong vowel), mismatching 得's real t-initial reading (tǝg) — corrected to jiǝtǝg; `諺文`/`注音` had already stayed correct. Added missing `kwin: false` (AND-rule). Filled blank korean and vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自我.

### 2026-09-05, iteration 3054 — [[words/自我|自我]]

No cranberry (自's own stand-in is [[自身]], 我's own is [[我]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝ'a/즤아/ㄐㄧㄜ·ㄚ) already verified as the correct concatenation, including the null-onset syllable break — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space. Kept the existing thoughtful Definition/Function/Usage-Principle prose. Fixed a self-citation entirely missing from `characters/我 (char).md`'s own Words list, plus its missing 自我 citation. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自然.

### 2026-09-05, iteration 3055 — [[words/自然|自然]]

No cranberry (自's own stand-in is [[自身]], 然's own is [[然]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝnyen/즤년/ㄐㄧㄜㄋ⼶ㄋ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray space. Verified japanese しぜん uses 自's genuine alternate on'yomi シ (not ジ) — not a bug. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自由.

### 2026-09-05, iteration 3056 — [[words/自由|自由]]

No cranberry (自's own stand-in is [[自身]], 由's own is [[由]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `japanese` had じいう (vowel-insertion error) instead of the correct じゆう. Pronunciation fields (jiǝ'yuo/즤윳/ㄐㄧㄜ⼜ㄛ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自禁.

### 2026-09-05, iteration 3057 — [[words/自禁|自禁]]

No cranberry (自's own stand-in is [[自身]], 禁's own is [[禁止]]) — neither constituent legitimized by this word. Pronunciation fields (jiǝgim/즤김/ㄐㄧㄜㄍㄧㄇ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Translated a stray Chinese-language editorial note ("古代. 使用『自制』請.") into proper English Notes prose (archaic, prefer [[自制]]). Filled blank japanese/vietnamese, fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自立.

### 2026-09-05, iteration 3058 — [[words/自立|自立]]

No cranberry (自's own stand-in is [[自身]], 立's own is [[立]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝlib/즤립/ㄐㄧㄜㄌㄧㄆ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray space. Fixed a self-citation entirely missing from `characters/立 (char).md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自給.

### 2026-09-05, iteration 3059 — [[words/自給|自給]]

No cranberry (自's own stand-in is [[自身]], 給's own is [[補給]]) — neither constituent legitimized by this word. Pronunciation fields (jiǝgib/즤깁/ㄐㄧㄜㄍㄧㄆ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Verified mandarin zìjǐ uses 給's genuine literary jǐ reading (as in 供給) — not contamination from the coincidentally-homophonous 自己. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自足.

### 2026-09-05, iteration 3060 — [[words/自足|自足]]

No cranberry (自's own stand-in is [[自身]], 足's own is [[足]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝjog/즤족/ㄐㄧㄜㄐㄛㄎ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese (tự túc, matching the real idiom). Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自身.

### 2026-09-05, iteration 3061 — [[words/自身|自身]]

No cranberry (自's own stand-in is this exact compound, but 身's own is [[身体]]) — transitivity fails, though 自 is legitimized as an independent Dan'a'yo entry by this word (already documented in the existing Notes). Pronunciation fields (jiǝsin/즤신/ㄐㄧㄜㄙㄧㄋ) already verified as the correct concatenation — no bug. **Found and fixed a real bug**: `vietnamese` had mình, a native colloquial pronoun not decomposable from either constituent's own stored reading — corrected to tự thân, matching this word's specific ontic/intrinsic register. Added missing `kwin: false`, quoted pronunciation fields, kept the existing thoughtful Definition/Function/Usage-Principle prose. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 自転車.

### 2026-09-05, iteration 3062 — [[words/自転車|自転車]]

No cranberry (none of the three constituents' own stand-ins point here). **Found and fixed a real bug**: `羅馬字` missing 車's own -w- glide (jiǝjwenca→jiǝjwencwa), same single-field-only class as [[自動車]]'s earlier fix — `諺文`/`注音` had already stayed correct. Filled blank cantonese. Verified korean 자전거 (alternate 거 reading of 車, specific to this compound) and vietnamese xe đạp (a genuine native term) as real, not bugs. Fixed a missing "(stand-in for 転)" annotation and a completely missing 自転車 citation on `characters/転.md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 至日.

### 2026-09-05, iteration 3063 — [[words/至日|至日]]

No cranberry (至's own stand-in is [[至]] itself, 日's own is [[日]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝnid/즤닏/ㄐㄧㄜㄋㄧㄊ) already verified as the correct concatenation — no bug (至 and 自 coincidentally share the exact same syllable jiǝ/즤/ㄐㄧㄜ, confirmed genuine, not contamination). Added missing `kwin: false`. Filled a completely missing vietnamese field. Quoted pronunciation fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 至極.

### 2026-09-05, iteration 3064 — [[words/至極|至極]]

No cranberry (至's own stand-in is [[至]] itself, 極's own is [[極]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝgig/즤긱/ㄐㄧㄜㄍㄧㄎ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 至点.

### 2026-09-05, iteration 3065 — [[words/至点|至点]]

No cranberry (至's own stand-in is [[至]] itself, 点's own is [[点]] itself) — neither constituent legitimized by this word. Pronunciation fields (jiǝdem/즤덤/ㄐㄧㄜㄉㄝㄇ) already verified as the correct concatenation — no bug. Added missing `kwin: false`. Fixed cantonese's stray space and quoted pronunciation fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 致.

### 2026-09-05, iteration 3066 — [[words/致|致]]

Single-character stand-in word. Pronunciation fields (ciǝ/츼/ㄑㄧㄜ) already matched the character's own values — no bug. Added missing pos/japanese/vietnamese. Found a genuine homophone with [[遅]] ("late, slow") — gave it a full pass too since otherwise unperfected (fixed two literal-`"null"`-string bugs on korean/vietnamese, added missing pos/kwin/japanese), added reciprocal callouts. Checked the third ㄑㄧㄜ-reading character, 次 — its own `stand_in` is [[次第]], no third homophone. Fixed a self-citation entirely missing from `characters/致 (char).md`'s own Words list. Stamped `date-last-perfect: 2026-09-05` on both word pages.

Next: 致使.

### 2026-09-05, iteration 3067 — [[words/致使|致使]]

No cranberry (致's own stand-in is [[致]] itself, 使's own is [[使者]]) — neither constituent legitimized by this word. Pronunciation fields (ciǝsi/츼시/ㄑㄧㄜㄙㄧ) already verified as the correct concatenation — no bug. Added missing `kwin: false`. Filled blank japanese/korean/vietnamese, fixed cantonese's stray space, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 興.

### 2026-09-05, iteration 3068 — [[words/興|興]]

Single-character stand-in word. Pronunciation fields (hǝng/흥/ㄏㄜㄫ) already matched the character's own values — no bug. Added missing pos/japanese (おこ, native kun-reading), filled blank vietnamese. Fixed a missing "(stand-in for 興)" annotation on the char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 舌根.

### 2026-09-05, iteration 3069 — [[words/舌根|舌根]]

No cranberry (舌's own stand-in is [[舌]] itself, 根's own is [[根]] itself) — neither constituent legitimized by this word. **Found and fixed two real bugs**: `羅馬字`/`諺文` had a vowel mismatch on 根's syllable (sedgan/섣간→sedgǝn/섣근; `注音` had already stayed correct); `cantonese` had a tone error (sit6→sit3, matching 舌's own sit3). Fixed a wrong rt-annotation (ㄍㄨㄋ→ㄍㄜㄋ) and a missing self-citation on `characters/舌 (char).md`'s own Words list. Fixed a comma-joined `vietnamese` on `characters/根 (char).md` into a proper list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 舗.

### 2026-09-05, iteration 3070 — [[words/舗|舗]]

Single-character stand-in word. Pronunciation fields (pou/폿/ㄆㄛㄨ) already matched the character's own values — no bug. Added missing pos/japanese (ホ, on-reading since no native kun exists). No homophones. In passing, fixed the 19th empty-string field bug on `characters/舗 (char).md` (`hsk_level: ""` → "無"). Stamped `date-last-perfect: 2026-09-05`.

Next: 航空.

### 2026-09-05, iteration 3071 — [[words/航空|航空]]

No cranberry (航's own stand-in is [[航行]], 空's own is [[空]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `japanese` had かうくう instead of こうくう (koukuu). Pronunciation fields (hangkong/항콩/ㄏㄚㄫㄎㄛㄫ) already verified as the correct concatenation — no bug; `kwin: false` already correct. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 航空母艦.

### 2026-09-05, iteration 3072 — [[words/航空母艦|航空母艦]]

No cranberry (none of the four constituents' own stand-ins point here). **Found and fixed a real bug**: `japanese` had かうくうぼかん instead of こうくうぼかん, same class as [[航空]]'s earlier fix. Pronunciation fields (hangkongmouham/항콩못함/ㄏㄚㄫㄎㄛㄫㄇㄛㄨㄏㄚㄇ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray spaces. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 船尾.

### 2026-09-05, iteration 3073 — [[words/船尾|船尾]]

No cranberry (船's own stand-in is [[船舶]], 尾's own is [[尾]] itself) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had jwenmui, using 船's minority cross-word syllable (already flagged on `characters/船.md` as inconsistent between the majority swem-group and the [[艦船]]/[[宇宙船]] jwen-outliers) instead of this word's own already-correct `諺文`/`注音` (matching the majority swem group) — corrected to swemmui. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 船籍.

### 2026-09-05, iteration 3074 — [[words/船籍|船籍]]

No cranberry (船's own stand-in is [[船舶]], 籍's own is [[書籍]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had jwenjeg (船's minority cross-word syllable, same class as [[船尾]]'s just-fixed bug) instead of the correct swemjeg matching `諺文`/`注音`. Added missing `kwin: false`. Filled blank cantonese/korean/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 船舶.

### 2026-09-05, iteration 3075 — [[words/船舶|船舶]]

**Genuine `#cranberry`** (already correctly tagged): both 船's and 舶's own stand-ins point here (6th cranberry this session). Pronunciation fields (swembag/쉄박/ㄙ⼔ㄇㄅㄚㄎ) already correctly used 船's majority syllable — no bug here, unlike the jwen-mistakes just fixed on [[船尾]]/[[船籍]]. `kwin: false` already correct. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 艇.

### 2026-09-05, iteration 3076 — [[words/艇|艇]]

Single-character stand-in word. Pronunciation fields (deng/덩/ㄉㄝㄫ) already matched the character's own values — Dan'a'yo's d-initial legitimately diverges from Mandarin's t-initial (MC 定 derivation), not a bug. Added missing japanese/vietnamese. Found a genuine **three-way homophone group** with [[丁]] (already stamped but missing callouts and carrying a trailing-space/redundant-`品詞` issue, both fixed) and [[釘]] (still otherwise unperfected — gave it a full pass, fixed a literal-`"null"`-string vietnamese bug, added missing pos/kwin/japanese). Checked the other five ㄉㄝㄫ-reading characters (亭, 停, 庭, 廷, 挺) — no fourth homophone. Fixed missing self-citations on `characters/丁 (char).md` and `characters/釘 (char).md`. Stamped `date-last-perfect: 2026-09-05` on all three word pages.

Next: 艦船.

### 2026-09-05, iteration 3077 — [[words/艦船|艦船]]

No cranberry (艦's own stand-in is this exact compound, but 船's own is [[船舶]]) — transitivity fails, though 艦 is legitimized as an independent Dan'a'yo entry by this word. **Resolved the flagged `characters/船.md` discrepancy**: 艦船's own `諺文` had already correctly stored swem's hangul (쉄) all along, while `羅馬字`/`注音` alone had drifted to a different reading (jwen) — corrected to match, closing out one of the two flagged outliers ([[宇宙船]] remains to be checked). Fixed the wrong rt-tag and a duplicate citation on `characters/艦.md`'s own Words list. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 良好.

### 2026-09-05, iteration 3078 — [[words/良好|良好]]

No cranberry (良's own stand-in is this exact compound, but 好's own is [[好]] itself) — transitivity fails, though 良 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (lyanghau/량핫/ㄌ⼘ㄫㄏㄚㄨ) already verified as the correct concatenation — no bug; `kwin: false` already correct. **Found and fixed a real bug**: `korean` was 두음법칙-shifted (양호→량호), per the standing North-Korean-pronunciation rule. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 良月.

### 2026-09-05, iteration 3079 — [[words/良月|良月]]

No cranberry (良's own stand-in is [[良好]], 月's own is [[月]] itself) — neither constituent legitimized by this word. Pronunciation fields (lyang'wed/량웓/ㄌ⼘ㄫ·⼔ㄊ) already verified as the correct concatenation, including the null-onset syllable break — no bug; `kwin: false` already correct. Verified japanese よいつき (native よい+つき) and vietnamese tháng lương (native word order, like [[臘月]]) as genuine attested terms, not bugs. Fixed cantonese's stray space, removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 色金.

### 2026-09-05, iteration 3080 — [[words/色金|色金]]

No cranberry (色's own stand-in is [[色彩]], 金's own is [[金]] itself). Periodic-table neologism (chromium); pronunciation fields already correct; real-element-reading fields (mandarin gè, korean 크로뮴, japanese クロム, vietnamese crôm) legitimately non-compositional per established convention. Removed redundant `品詞`. Kept the existing thorough etymology essay. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 艶福.

### 2026-09-05, iteration 3081 — [[words/艶福|艶福]]

No cranberry (艶's own stand-in is [[艶]] itself, 福's own is [[福]] itself) — neither constituent legitimized by this word. Pronunciation fields already correct (the 福-family pug/fug bug was fixed out-of-sequence on 2026-09-04). `kwin: false` already correct. Filled blank pos. Fixed cantonese's stray space. No homophones. In passing, fixed the 20th empty-string field bug on `characters/艶 (char).md` (`hsk_level: ""` → "無"). Stamped `date-last-perfect: 2026-09-05`.

Next: 艾灸.

### 2026-09-05, iteration 3082 — [[words/艾灸|艾灸]]

No cranberry (灸's own stand-in is this exact compound, but 艾's own is [[艾草]]) — transitivity fails, though 灸 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields ('aigyu/애규/ㄚㄧㄍ⼜) already verified as the correct concatenation — no bug. Added missing `kwin: false`. Fixed a typo in english (muxibustion→moxibustion). Filled blank korean. Fixed cantonese's stray space and a missing "(stand-in for 灸)" annotation on the char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芝草.

### 2026-09-05, iteration 3083 — [[words/芝草|芝草]]

No cranberry (芝's own stand-in is the special `名専字` name-only marker; 草's own is [[草]] itself). Pronunciation fields (jicau/지찻/ㄐㄧㄑㄚㄨ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Kept the existing thorough Notes (Korean/Japanese homograph discussion). Quoted pronunciation fields. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芝麻醤.

### 2026-09-05, iteration 3084 — [[words/芝麻醤|芝麻醤]]

No cranberry (none of the three constituents' own stand-ins point here). Pronunciation fields (jimajang/지마장/ㄐㄧㄇㄚㄐㄚㄫ) already verified as the correct concatenation — no bug; `kwin: true` already correct. Filled blank vietnamese. Fixed cantonese's stray spaces. Kept the existing thorough Notes. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芦葦.

### 2026-09-05, iteration 3085 — [[words/芦葦|芦葦]]

**Genuine `#cranberry`** (already correctly tagged): both 芦's and 葦's own stand-ins point here (7th cranberry this session). Pronunciation fields (lohui/로휘/ㄌㄛㄏㄨㄧ) already verified as the correct concatenation — no bug; `kwin: false` already correct. **Found and fixed a real bug**: `japanese` listed る/ろ/あし, but る doesn't correspond to any documented reading — trimmed to ろ/あし. Verified korean 갈대/vietnamese sậy as genuine native terms, not bugs. Fixed cantonese's stray space and a missing "(stand-in for 葦)" annotation on the char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芬蘭.

### 2026-09-05, iteration 3086 — [[words/芬蘭|芬蘭]]

No cranberry (芬's own stand-in is [[芬芳]], 蘭's own is [[蘭花]]). **Found and fixed a real bug**: `羅馬字`/`諺文`/`注音` all had a p-initial reading (Punlan/푼란/ㄆㄨㄋㄌㄚㄋ), mismatching 芬's real f-initial — same ㄈ→ㅍ confusion class as the 福-family bug — corrected to funlan/뿐란/ㄈㄨㄋㄌㄚㄋ (also normalized stray capitalization). `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space. As a proper place name, real-language fields legitimately hold the attested name/transliteration. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芭蕉.

### 2026-09-05, iteration 3087 — [[words/芭蕉|芭蕉]]

No cranberry (芭's own stand-in is this exact compound, but 蕉's own is [[甘蕉]]) — transitivity fails, though 芭 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed a real bug**: `mandarin` had ājiāo, missing 芭's own b-initial entirely — corrected to bājiāo. Pronunciation fields (bajou/바좃/ㄅㄚㄐㄛㄨ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray space and a missing "(stand-in for 芭)" annotation on the char page. Kept the existing thoughtful three-way comparison Notes. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 花卉.

### 2026-09-05, iteration 3088 — [[words/花卉|花卉]]

No cranberry (卉's own stand-in is this exact compound, but 花's own is [[草花]]) — transitivity fails, though 卉 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (hwahui/화휘/ㄏ⺢ㄏㄨㄧ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space, a missing "(stand-in for 卉)" annotation, and a malformed nested-list `tags:` field on `characters/花.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 花店.

### 2026-09-05, iteration 3089 — [[words/花店|花店]]

No cranberry (花's own stand-in is [[草花]], 店's own is [[商店]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字`/`諺文` had a final -n instead of 店's real final -m (hwaden/화던→hwadem/화덤); `注音` had already stayed correct. `kwin: false` already correct. Filled blank vietnamese. Verified japanese はなや/korean 꽃집 as genuine real terms, not bugs. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 花弁.

### 2026-09-05, iteration 3090 — [[words/花弁|花弁]]

No cranberry (花's own stand-in is [[草花]], 弁's own is [[弁]] itself) — neither constituent legitimized by this word. Pronunciation fields (hwabyan/화뱐/ㄏ⺢ㄅ⼘ㄋ) already verified as the correct concatenation — no bug; `kwin: false` already correct. **Found and fixed a real bug**: `cantonese` had a stray space and wrong initial (faa1 faan6-2→faa1baan6), consistent with `korean` 화판 genuinely tracking the semantic donor 瓣's own reading rather than 弁's own stored value (same pattern as [[胰臓]]/膵). Filled blank vietnamese. No homophones. In passing, fixed the 21st empty-string field bug on `characters/弁 (char).md` (hsk_level). Stamped `date-last-perfect: 2026-09-05`.

Next: 花栗鼠.

### 2026-09-05, iteration 3091 — [[words/花栗鼠|花栗鼠]]

No cranberry (none of the three constituents' own stand-ins point here). Pronunciation fields (hwalidsyo/화릳쇼/ㄏ⺢ㄌㄧㄊㄙ⼄) already verified as the correct concatenation — no bug; `kwin: false` already correct. Fixed cantonese's stray spaces. Verified japanese シマリス/korean 다람쥐/vietnamese sóc chuột as genuine native terms, not bugs. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 花粉.

### 2026-09-05, iteration 3092 — [[words/花粉|花粉]]

No cranberry. **Found and fixed two real bugs**: `羅馬字`/`諺文` had the 粉/分-confusion misreading (hwabun/화분→hwafun/화뿐), the same class already fixed on [[粉]]/[[粉末]] but which had slipped through here — `注音` had already stayed correct. `kwin` was true, corrected to false per the AND-rule (粉 individually false). Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芳香族.

### 2026-09-05, iteration 3093 — [[words/芳香族|芳香族]]

No cranberry (none of the three constituents' own stand-ins point here). **Found and fixed a real bug**: `羅馬字`/`諺文` had a p-initial reading (panghyangjog/팡향족), mismatching 芳's real f-initial — same ㄈ→ㅍ confusion class as the 福-family bug — corrected to fanghyangjog/빵향족; `注音` had already stayed correct. `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray spaces. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芸人.

### 2026-09-05, iteration 3094 — [[words/芸人|芸人]]

No cranberry (芸's own stand-in is [[芸術]], 人's own is [[人]] itself) — neither constituent legitimized by this word. Pronunciation fields ('enin/어닌/ㄝㄋㄧㄋ) already verified as the correct concatenation, including the null-onset syllable break — no bug. Added missing `kwin: false`. Filled blank korean. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芸妓.

### 2026-09-05, iteration 3095 — [[words/芸妓|芸妓]]

No cranberry (妓's own stand-in is this exact compound, but 芸's own is [[芸術]]) — transitivity fails, though 妓 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields ('egi/어기/ㄝㄍㄧ) already verified as the correct concatenation, including the null-onset syllable break — no bug. Added missing `kwin: false`. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 芸術.

### 2026-09-05, iteration 3096 — [[words/芸術|芸術]]

No cranberry (芸's own stand-in is this exact compound, but 術's own is [[術]] itself) — transitivity fails, though 芸 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields ('esud/어숟/ㄝㄙㄨㄊ) already verified as the correct concatenation, including the null-onset syllable break — no bug; `kwin: false` already correct. Filled blank pos. Converted comma-joined mandarin (yìshù/yìshu, both genuinely attested, tracking donor 藝 not 芸's own yún) into a proper list. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 苔.

### 2026-09-05, iteration 3097 — [[words/苔|苔]]

Single-character stand-in word. Pronunciation fields (toi/퇴/ㄊㄛㄧ) already matched the character's own values — no bug. Added missing pos/japanese/kwin, filled `vietnamese: null`→đài. Checked the one other ㄊㄛㄧ-reading character, 跆 — its own `stand_in` is [[跆籍]], not a self-citation, so no homophone. Fixed a completely missing `## Words` section on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 苗族.

### 2026-09-05, iteration 3098 — [[words/苗族|苗族]]

No cranberry (苗's own stand-in is [[種苗]], 族's own is [[家族]]) — neither constituent legitimized by this word. **Found and fixed a real bug**: `羅馬字` had a wrong final consonant (myaujok→myaujog); `諺文`/`注音` had already stayed correct. `kwin: false` already correct. Filled blank japanese (ミャオ族)/vietnamese (Miêu tộc). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 苛刻.

### 2026-09-05, iteration 3099 — [[words/苛刻|苛刻]]

No cranberry (苛's own stand-in is this exact compound, but 刻's own is [[刻印]]) — transitivity fails, though 苛 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (hakug/하쿡/ㄏㄚㄎㄨㄎ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 苦土素.

### 2026-09-05, iteration 3100 — [[words/苦土素|苦土素]]

No cranberry. Periodic-table neologism (magnesium). Pronunciation fields (kotoso/코토소/ㄎㄛㄊㄛㄙㄛ) already verified as the correct concatenation — no bug; `kwin: false` already correct. **Found and fixed a real bug**: `japanese` had くどそ, a kana spelling of this word's own internal Dan'a'yo reading rather than a real Japanese term — corrected to マグネシウム, matching the established convention already followed by mandarin měi/korean 마그네슘/vietnamese magiê. Removed redundant `品詞`. No homophones. Stamped `date-last-perfect: 2026-09-05`. **Milestone: 3,100th logged iteration.**

Next: 苦悶.

### 2026-09-05, iteration 3101 — [[words/苦悶|苦悶]]

No cranberry (悶's own stand-in is this exact compound, but 苦's own is [[苦]] itself) — transitivity fails, though 悶 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (komon/코몬/ㄎㄛㄇㄛㄋ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space and a missing "(stand-in for 悶)" annotation. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 苦渋.

### 2026-09-05, iteration 3102 — [[words/苦渋|苦渋]]

No cranberry (渋's own stand-in is this exact compound, but 苦's own is [[苦]] itself) — transitivity fails, though 渋 is legitimized as an independent Dan'a'yo entry by this word. **Found and fixed two real bugs**: `japanese` had にがい (native "bitter," contaminated from 苦's own gloss) instead of the real compound reading くじゅう; `korean` had 쓰다 (native verb, same contamination) instead of the compositional 고삽. Pronunciation fields (kosib/코십/ㄎㄛㄙㄧㄆ) already verified as the correct concatenation — no bug. Converted comma-joined cantonese into a proper list. Filled blank vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 苦瓜.

### 2026-09-05, iteration 3103 — [[words/苦瓜|苦瓜]]

No cranberry (苦's own stand-in is [[苦]] itself, 瓜's own is [[胡瓜]]) — neither constituent legitimized by this word. Pronunciation fields (kogwa/코과/ㄎㄛㄍ⺢) already verified as the correct concatenation — no bug; `kwin: false` already correct. Verified japanese にがうり as genuinely compositional from both characters' own native readings (unlike [[苦渋]]'s contamination bug) — not a bug. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 苦痛.

### 2026-09-05, iteration 3104 — [[words/苦痛|苦痛]]

No cranberry (痛's own stand-in is this exact compound, but 苦's own is [[苦]] itself) — transitivity fails, though 痛 is legitimized as an independent Dan'a'yo entry by this word. Pronunciation fields (kotong/코통/ㄎㄛㄊㄛㄫ) already verified as the correct concatenation — no bug; `kwin: false` already correct. Filled blank vietnamese. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 英俊.

### 2026-09-05, iteration 3105 — [[words/英俊|英俊]]

No cranberry (英's own stand-in is [[英雄]], 俊's own is [[俊傑]]) — neither constituent legitimized by this word. **Found and fixed two real bugs**: `羅馬字`/`諺文` had a wrong final consonant on 俊's syllable (-ng instead of -n); `注音` had already stayed correct throughout. `japanese` had ひでとし (Hidetoshi), a Japanese given-name reading of the same characters, instead of the real word reading えいしゅん. Filled blank pos/vietnamese. Fixed cantonese's stray space and a missing citation on `characters/俊.md`'s own Words list. No genuine homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 英吉利.

### 2026-09-05, iteration 3106 — [[words/英吉利|英吉利]]

No cranberry (none of the three constituents' own stand-ins point here). Pronunciation fields ('enggidliǝ/엉긷릐/ㄝㄫㄍㄧㄊㄌㄧㄜ) already verified as the correct concatenation — no bug. Added missing `kwin: false`. Filled blank korean (영길리, a genuine historical parallel transliteration). As a proper place name, mandarin/japanese/vietnamese legitimately hold the real attested name. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 英語.

### 2026-09-05, iteration 3107 — [[words/英語|英語]]

No cranberry (英's own stand-in is [[英雄]], 語's own is [[言語]]) — neither constituent legitimized by this word. Pronunciation fields ('eng'yo/엉요/ㄝㄫ·⼄) already verified as the correct concatenation, including the null-onset syllable break — no bug; `kwin: false` already correct. Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 英語圏.

### 2026-09-05, iteration 3108 — [[words/英語圏|英語圏]]

No cranberry (none of the three constituents' own stand-ins point here; 圏's own stand-in is [[圏]] itself). Pronunciation fields ('eng'yogwen/엉요권/ㄝㄫ⼄ㄍ⼔ㄋ) already verified as the correct concatenation — no bug; `kwin: false` already correct (AND-rule). Fixed cantonese's stray spaces. Vietnamese left blank (no verifiable distinct real term). Removed blank hsk_level/swadesh. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 英語学.

### 2026-09-05, iteration 3109 — [[words/英語学|英語学]]

No cranberry (none of the three constituents' stand-ins point here). Pronunciation fields ('eng'yohag/엉요학/ㄝㄫ⼄ㄏㄚㄎ) already verified as the correct concatenation — no bug. Added missing `kwin: false` (AND-rule). Filled blank pos (名詞, matching other `-学` compounds), korean (영어학), vietnamese (Anh ngữ học). Fixed cantonese's stray spaces. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 英雄.

### 2026-09-05, iteration 3110 — [[words/英雄|英雄]]

英's own stand-in is this exact compound; 雄's own is [[雄]] itself — transitivity fails, no cranberry. Pronunciation fields ('eng'ung/엉웅/ㄝㄫㄨㄫ) already verified as the correct concatenation — no bug; `kwin: false` already correct (AND-rule). Filled blank pos (名詞). Fixed cantonese's stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

(Several already-stamped words follow alphabetically — 英語欄/英語辞典-type entries and 苹果 — skipped via the standard unstamped-scan.)

Next: 茄子.

### 2026-09-05, iteration 3111 — [[words/茄子|茄子]]

茄's own stand-in is this exact compound; 子's own is [[児子]] — transitivity fails, no cranberry. Pronunciation fields (gajǝ/가즈/ㄍㄚㄐㄜ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (true→false, AND-rule). Fixed cantonese's stray space (kept legitimate tone-sandhi notation). **Removed a stale false-homophone callout** with [[家事]] — the two words' own readings are genuinely different (ㄍㄚㄐㄜ vs ㄍㄚㄐㄧ); 家事's own page already documented the real (cross-system, not same-system) coincidence. No genuine homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 茅草.

### 2026-09-05, iteration 3112 — [[words/茅草|茅草]]

茅's own stand-in is this exact compound; 草's own is [[草]] itself — transitivity fails, no cranberry. Pronunciation fields (myaucau/먓찻/ㄇ⼘ㄨㄑㄚㄨ) already verified as the correct concatenation — no bug; kwin:false already correct. **Found and fixed a real bug**: japanese held みょう (only half the compound, 草's part entirely missing) — corrected to compositional みょうそう. Fixed cantonese stray space. Vietnamese left blank. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 茉莉.

### 2026-09-05, iteration 3113 — [[words/茉莉|茉莉]]

**Genuine `#cranberry`** (both 茉's and 莉's own stand-ins point here, full transitivity; tag already correctly present). Pronunciation fields (madlei/맏레/ㄇㄚㄊㄌㄝㄧ) already verified as the correct concatenation — no bug; kwin:false already correct. All other-language fields confirmed standard, compositional, and genuinely attested. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 茎.

### 2026-09-05, iteration 3114 — [[words/茎|茎]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing kwin (false). Filled blank japanese (くき). Added missing alias 莖. **Found a genuine homophone** with [[軽]] ("light, not heavy") — added reciprocal callout, gave 軽 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3115 — [[words/軽|軽]]

Single-character stand-in word (companion to 茎's homophone group). **Found and fixed a real `kwin` bug** (true→false, contradicted the character's own field). Filled blank pos/korean/japanese/vietnamese. Added missing aliases. Stamped `date-last-perfect: 2026-09-05`.

Next: 茜素.

### 2026-09-05, iteration 3116 — [[words/茜素|茜素]]

No cranberry (茜's own stand-in is [[茜草]], 素's is [[要素]]). Periodic-table neologism (rubidium). Pronunciation fields (censo/천소/ㄑㄝㄋㄙㄛ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Mandarin/cantonese/korean/japanese/vietnamese all confirmed real element-name terms, per established convention. Removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 茫然.

### 2026-09-05, iteration 3117 — [[words/茫然|茫然]]

No cranberry (茫's own stand-in is [[茫茫]], 然's is [[然]] itself). Pronunciation fields (mangnyen/망년/ㄇㄚㄫㄋ⼶ㄋ) already verified as the correct concatenation — no bug; kwin:false already correct. Other-language fields confirmed compositional (japanese ぼうぜん = BOU+ZEN). Fixed cantonese stray space, quoted hsk_level. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 茶.

### 2026-09-05, iteration 3118 — [[words/茶|茶]]

Single-character stand-in word (previously-flagged known gap: old bare-string `characters`, `vietnamese: null`, no pos/kwin/japanese). Pronunciation fields already matched the character's own values — no bug. Added missing kwin (false). Fixed `vietnamese: null` → trà (avoided chè, which means "dessert soup" in Southern usage). Filled blank japanese (ちゃ). **Found a genuine homophone** with [[者]] (agentive suffix "-er") — added reciprocal callout. Stamped `date-last-perfect: 2026-09-05`.

Next: 草原.

### 2026-09-05, iteration 3119 — [[words/草原|草原]]

No cranberry (草's own stand-in is [[草]] itself, 原's is [[原始]]). Pronunciation fields (cau'wen/찻원/ㄑㄚㄨ·⼔ㄋ) already verified as the correct concatenation, including the null-onset syllable break — no bug; kwin:false already correct. Other-language fields confirmed standard and compositional. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 草木.

### 2026-09-05, iteration 3120 — [[words/草木|草木]]

No cranberry (both 草's and 木's own stand-ins point to themselves). Pronunciation fields (caumog/찻목/ㄑㄚㄨㄇㄛㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Other-language fields confirmed standard and compositional. Filled blank vietnamese (thảo mộc, a real common word). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 荷担.

### 2026-09-05, iteration 3121 — [[words/荷担|荷担]]

担's own stand-in is this exact compound; 荷's own is [[荷物]] — transitivity fails, no cranberry. Pronunciation fields (hadam/하담/ㄏㄚㄉㄚㄇ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (true→false, AND-rule). Confirmed mandarin hèdān's tone alternation (hè "carry" vs hé "lotus") is genuine, not a bug. Filled blank cantonese/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 荷月.

### 2026-09-05, iteration 3122 — [[words/荷月|荷月]]

No cranberry (荷's own stand-in is [[荷物]], 月's is [[月]] itself). Pronunciation fields (ha'wed/하웓/ㄏㄚ·⼔ㄊ) already verified as the correct concatenation — no bug. Japanese はすつき confirmed genuine, matching the established poetic-month convention (native kun'yomi descriptor + つき, see 桃月/榴月/杏月/桂月/槐月). Fixed cantonese stray space, removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 荷物.

### 2026-09-05, iteration 3123 — [[words/荷物|荷物]]

荷's own stand-in is this exact compound; 物's own is [[物]] itself — transitivity fails, no cranberry. Pronunciation fields (hamud/하묻/ㄏㄚㄇㄨㄊ) already verified as the correct concatenation — no bug. Added missing `kwin: true` (AND-rule). Filled blank cantonese/korean/vietnamese (하물 confirmed a real Sino-Korean cargo term). Genuine homophone with [[何物]] already documented on both sides; standardized the callout format. Stamped `date-last-perfect: 2026-09-05`.

Next: 莱金.

### 2026-09-05, iteration 3124 — [[words/莱金|莱金]]

No cranberry (莱's own stand-in is [[蓬莱]], 金's is [[金]] itself). Periodic-table neologism (rhenium). Pronunciation fields (laigim/래김/ㄌㄚㄧㄍㄧㄇ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Mandarin/cantonese confirmed to match the real element name 铼; korean/japanese/vietnamese all genuine international transliterations. Removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 菊.

### 2026-09-05, iteration 3125 — [[words/菊|菊]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing kwin/pos/japanese. Checked two candidate homophones (掬, 鞠) — neither has its own independent word-level entry, so no genuine homophone. Stamped `date-last-perfect: 2026-09-05`.

Next: 菊月.

### 2026-09-05, iteration 3126 — [[words/菊月|菊月]]

No cranberry (both 菊's and 月's own stand-ins point to themselves). Pronunciation fields (gug'wed/국웓/ㄍㄨㄎ·⼔ㄊ) already verified as the correct concatenation — no bug. Japanese きくつき confirmed genuine, matching the poetic-month convention. Fixed cantonese stray space, removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 菜蔬.

### 2026-09-05, iteration 3127 — [[words/菜蔬|菜蔬]]

蔬's own stand-in is this exact compound; 菜's own is [[野菜]] — transitivity fails, no cranberry (already documented). Pronunciation fields (caisǝ/채스/ㄑㄚㄧㄙㄜ) already verified as the correct concatenation — no bug; kwin:false already correct. Other-language fields confirmed standard and compositional (korean 채소 also the real common word). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 菩薩.

### 2026-09-05, iteration 3128 — [[words/菩薩|菩薩]]

**Genuine `#cranberry`** (both 菩's and 薩's own stand-ins point here, full transitivity; tag already present). Pronunciation fields (bosad/보삳/ㄅㄛㄙㄚㄊ) already verified as the correct concatenation — no bug; kwin:true already correct. Mandarin/japanese/korean confirmed standard and attested. Filled blank vietnamese (bồ tát, a real standard term). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 華美.

### 2026-09-05, iteration 3129 — [[words/華美|華美]]

華's own stand-in is this exact compound; 美's own is [[美]] itself — transitivity fails, no cranberry. Pronunciation fields (hwami/화미/ㄏ⺢ㄇㄧ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Filled blank vietnamese (hoa mỹ, a real standard term). Fixed cantonese stray space, added simplified alias 华美. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 華麗.

### 2026-09-05, iteration 3130 — [[words/華麗|華麗]]

No cranberry (華's own stand-in is [[華美]], 麗's is [[秀麗]] — already documented). Pronunciation fields (hwale/화러/ㄏ⺢ㄌㄝ) already verified as the correct concatenation — no bug; kwin:false already correct. Other-language fields confirmed standard and compositional (korean/vietnamese also real attested terms). Filled blank cantonese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 菱.

### 2026-09-05, iteration 3131 — [[words/菱|菱]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/japanese, filled blank vietnamese. Checked two candidate homophones (凌, 陵) — neither independently legitimized, so no genuine homophone. Fixed a missing stand-in annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 菱形.

### 2026-09-05, iteration 3132 — [[words/菱形|菱形]]

No cranberry (both 菱's and 形's own stand-ins point to themselves). Pronunciation fields (lǝngheng/릉헝/ㄌㄜㄫㄏㄝㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Other-language fields confirmed standard and compositional. Filled blank vietnamese (lăng hình, compositional). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 萌芽.

### 2026-09-05, iteration 3133 — [[words/萌芽|萌芽]]

萌's own stand-in is this exact compound; 芽's own is [[新芽]] — transitivity fails, no cranberry (already documented). Pronunciation fields (mǝng'a/믕아/ㄇㄜㄫ·ㄚ) already verified as the correct concatenation — no bug; kwin:false already correct. Other-language fields confirmed standard and compositional (vietnamese already attested via hvdic). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 萎縮.

### 2026-09-05, iteration 3134 — [[words/萎縮|萎縮]]

萎's own stand-in is this exact compound; 縮's own is [[縮]] itself — transitivity fails, no cranberry (already documented). Pronunciation fields ('weisug/웨숙/⼔ㄧㄙㄨㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Mandarin's dual reading confirmed genuine (matches 萎's own), converted to list. Other fields confirmed compositional. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 萬物.

### 2026-09-05, iteration 3135 — [[words/萬物|萬物]]

萬's own stand-in is this exact compound; 物's own is [[物]] itself — transitivity fails, no cranberry. Pronunciation fields (monmud/몬묻/ㄇㄛㄋㄇㄨㄊ) already verified as the correct concatenation — no bug; kwin:false already correct. **Found and fixed a documentation bug**: this page's own `aliases` field wrongly listed [[万物]] as an alias — 万物 is actually a full independent word page (the 大字 anti-falsification orthographic counterpart), matching the established 萬/万 character-level precedent of NOT cross-aliasing; removed the wrong alias entry. Other fields confirmed standard and compositional. Fixed cantonese stray space. No genuine homophones (万物 duplicate excluded, intentional). Stamped `date-last-perfect: 2026-09-05`.

Next: 落下傘.

### 2026-09-05, iteration 3136 — [[words/落下傘|落下傘]]

No cranberry (none of the three constituents' stand-ins point here). Pronunciation fields (lakhasan/락하산/ㄌㄚㄎㄏㄚㄙㄚㄋ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Confirmed mandarin/cantonese legitimately track the real distinct term 降落伞. **Found and fixed two real bugs**: japanese らくかさん missing well-established 促音便 gemination → らっかさん; korean 낙하산 was 두음법칙-shifted → 락하산 (unshifted North Korean form, per standing rule). Fixed cantonese stray spaces. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 落花.

### 2026-09-05, iteration 3137 — [[words/落花|落花]]

No cranberry (落's own stand-in is [[落下]], 花's is [[草花]]). Pronunciation fields (laghwa/락화/ㄌㄚㄎㄏ⺢) already verified as the correct concatenation — no bug. Added missing kwin:true. **Found and fixed a real bug**: korean comma-joined "락화,낙화" mixed the correct unshifted form with a 두음법칙-shifted variant — trimmed to 락화. Japanese らっか confirmed genuine (real-world homograph coincidence with 落下, not a Dan'a'yo-internal homophone). Filled blank vietnamese (lạc hoa, a real classical term). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 葉.

### 2026-09-05, iteration 3138 — [[words/葉|葉]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. **Found and fixed a real bug**: korean 섭 (belonging to a different character) → 엽 (matching the character's own stored value). Added missing pos/kwin/japanese, filled blank vietnamese. Fixed a missing stand-in annotation on the char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 葛.

### 2026-09-05, iteration 3139 — [[words/葛|葛]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Fixed `vietnamese: null` → cát. Added missing pos/kwin/japanese. Fixed missing stand-in annotation on char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 葡萄.

### 2026-09-05, iteration 3140 — [[words/葡萄|葡萄]]

**Genuine `#cranberry`** (both 葡's and 萄's own stand-ins point here, full transitivity; tag already present). Pronunciation fields (bodau/보닷/ㄅㄛㄉㄚㄨ) already verified as the correct concatenation — no bug; kwin:false already correct. **Found and fixed a real bug**: cantonese "pu2 tao2" was invalid romanization matching neither character's own jyutping — corrected to pou4tou4. Other fields confirmed standard and compositional. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 葡萄牙.

### 2026-09-05, iteration 3141 — [[words/葡萄牙|葡萄牙]]

No cranberry (葡/萄's own stand-in is [[葡萄]], 牙's is [[長牙]]). Pronunciation fields (bodau'a/보닷아/ㄅㄛㄉㄚㄨ·ㄚ) already verified as the correct concatenation, including the null-onset syllable break — no bug; kwin:false already correct. As a proper place name, other-language fields legitimately hold the real attested name. Fixed cantonese stray spaces. In passing, fixed the 22nd empty-string field bug on `characters/牙.md` (pos). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 葺.

### 2026-09-05, iteration 3142 — [[words/葺|葺]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing kwin/japanese. Fixed a missing stand-in annotation on the char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蒙朧.

### 2026-09-05, iteration 3143 — [[words/蒙朧|蒙朧]]

朧's own stand-in is this exact compound; 蒙's own is [[蒙古]] — transitivity fails, no cranberry. Pronunciation fields (monglong/몽롱/ㄇㄛㄫㄌㄛㄫ) already verified as the correct concatenation — no bug; kwin:true already correct. Filled blank vietnamese (mông lung, a real common word). Other fields confirmed standard and compositional. Fixed missing stand-in annotation on 朧's char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蒲公英.

### 2026-09-05, iteration 3144 — [[words/蒲公英|蒲公英]]

No cranberry (蒲's own stand-in is [[香蒲]], 公's is [[公]] itself, 英's is [[英雄]]). Pronunciation fields (bogong'eng/보공엉/ㄅㄛㄍㄛㄫㄝㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Vietnamese/mandarin confirmed real standard terms; japanese たんぽぽ confirmed a legitimate real-term substitution (not compositional). Fixed cantonese stray spaces. Fixed a missing back-citation on `characters/公 (char).md`'s own Words list. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蒸汽.

### 2026-09-05, iteration 3145 — [[words/蒸汽|蒸汽]]

汽's own stand-in is this exact compound; 蒸's own is [[蒸]] itself — transitivity fails, no cranberry. Pronunciation fields (jingkiǝ/징킈/ㄐㄧㄫㄎㄧㄜ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese (chưng khí). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蒼海.

### 2026-09-05, iteration 3146 — [[words/蒼海|蒼海]]

No cranberry (蒼's own stand-in is [[蒼]] itself, 海's is [[海洋]]). **Found and fixed two real bugs**: 羅馬字 canghai was missing 蒼's own glide (諺文/注音 already correct) → cwanghai; japanese さうかい used obsolete historical kana → modern そうかい. kwin:false already correct. Filled blank vietnamese (thương hải, matching the idiom 滄海桑田). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蒼路.

### 2026-09-05, iteration 3147 — [[words/蒼路|蒼路]]

No cranberry (蒼's own stand-in is [[蒼]] itself, 路's is [[道路]]). Here 路 is a `借代字` for 鷺, so 蒼路 = 蒼鷺 "grey heron." **Found and fixed the same 蒼-glide bug as [[蒼海]]**: 羅馬字/諺文 canglo/창로 missing the glide (注音 already correct) → cwanglo/촹로. Confirmed japanese/korean/vietnamese are all real bird-name substitutions, not compositional. Filled blank cantonese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蒼鉛.

### 2026-09-05, iteration 3148 — [[words/蒼鉛|蒼鉛]]

No cranberry (both 蒼's and 鉛's own stand-ins point to themselves). Pronunciation fields already correct concatenation — this one did NOT have the glide bug seen on [[蒼海]]/[[蒼路]]. kwin:false already correct. **Found and fixed a real bug**: cantonese bit1 was the modern replacement-element reading, inconsistent with mandarin's own deliberately-historical cāngqiān — corrected to the parallel historical-binome cong1jyun4. Removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蓄.

### 2026-09-05, iteration 3149 — [[words/蓄|蓄]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/kwin/japanese. **Found a genuine homophone** with [[蹴]] ("kick") — added reciprocal callout, gave 蹴 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3150 — [[words/蹴|蹴]]

Single-character stand-in word (companion to 蓄's homophone group). Fixed `vietnamese: null` → xúc. Added missing pos/kwin/japanese. Stamped `date-last-perfect: 2026-09-05`.

Next: 蓬藁.

### 2026-09-05, iteration 3151 — [[words/蓬藁|蓬藁]]

蓬's own stand-in is this exact compound; 藁 is used as a `借代字` for the pageless 蒿, so 蓬藁 represents 蓬蒿 (already an alias). **Found and fixed two real bugs**: 羅馬字/諺文 (bonggao/봉, the latter truncated) both failed to match 注音's already-correct ㄅㄛㄫㄏㄚㄨ — corrected to bonghau/봉핫. **Found and fixed a real `kwin` bug** (true→false, AND-rule: 藁's own field is false). Confirmed mandarin/cantonese/japanese/korean all correctly use 蒿's own real reading, not 藁's — no bug there. Filled blank vietnamese (bồng cao). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蓮.

### 2026-09-05, iteration 3152 — [[words/蓮|蓮]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Fixed `vietnamese: null` → liên. Added missing pos/kwin/japanese. **Found a genuine homophone** with [[連]] ("mutual, successive") — added reciprocal callout, gave 連 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3153 — [[words/連|連]]

Single-character stand-in word (companion to 蓮's homophone group). All fields were already correctly filled; fixed double-spaced japanese, removed redundant 品詞. Fixed a missing stand-in annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 蕃息.

### 2026-09-05, iteration 3154 — [[words/蕃息|蕃息]]

蕃's own stand-in is this exact compound; 息's own is [[気息]] — transitivity fails, no cranberry. Pronunciation fields (fansig/빤식/ㄈㄚㄋㄙㄧㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese (phồn tức). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蕤素.

### 2026-09-05, iteration 3155 — [[words/蕤素|蕤素]]

No cranberry (蕤's own stand-in is [[萎蕤]], 素's is [[要素]]). Periodic-table neologism (thallium). Pronunciation fields (nuiso/뉘소/ㄋㄨㄧㄙㄛ) already verified as the correct concatenation — no bug. Real-language fields confirmed genuine element-name terms. Removed redundant 品詞. In passing, fixed the 23rd empty-string field bug (`characters/蕤.md` vietnamese) and added its missing kwin (false, computed from its own reading vs. Korean mismatch). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蕪青.

### 2026-09-05, iteration 3156 — [[words/蕪青|蕪青]]

蕪's own stand-in is this exact compound; 青's own is [[青]] itself — transitivity fails, no cranberry. Here 青 stands in for its own alias 菁, matching the classical etymology 蕪菁. Pronunciation fields (muceng/무청/ㄇㄨㄑㄝㄫ) already verified as the correct concatenation — no bug; kwin:true already correct. Japanese かぶら confirmed a legitimate real-term substitution (matching 蕪's own native reading). Filled blank vietnamese (vu thanh). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 薄命.

### 2026-09-05, iteration 3157 — [[words/薄命|薄命]]

No cranberry (薄's own stand-in is [[希薄]], 命's is [[運命]]). Pronunciation fields (bagmyeng/박명/ㄅㄚㄎㄇ⼶ㄫ) already verified as the correct concatenation — no bug; kwin:true already correct. Other-language fields confirmed standard and compositional (vietnamese matching the famous idiom hồng nhan bạc mệnh). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 薄弱.

### 2026-09-05, iteration 3158 — [[words/薄弱|薄弱]]

No cranberry (薄's own stand-in is [[希薄]], 弱's is [[弱]] itself). **Found and fixed a real bug**: 注音 had a wrong final consonant on 弱's syllable (ㄫ instead of ㄎ) — 羅馬字/諺文 had already stayed correct (reverse of the usual pattern). Fixed matching rt-tags on both `characters/薄.md` and `characters/弱 (char).md`. kwin:false already correct. Other fields confirmed standard and compositional. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 薄荷.

### 2026-09-05, iteration 3159 — [[words/薄荷|薄荷]]

No cranberry (薄's own stand-in is [[希薄]], 荷's is [[荷物]]). Pronunciation fields (bagha/박하/ㄅㄚㄎㄏㄚ) already verified as the correct concatenation — no bug; kwin:true already correct. Mandarin bòhe confirmed using 薄's special reading, genuine. **Found and fixed a real bug**: japanese はくか missing 促音便 gemination → はっか (same class as [[落下傘]]/落下). Korean/vietnamese confirmed real standard terms. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 薔薇.

### 2026-09-05, iteration 3160 — [[words/薔薇|薔薇]]

**Genuine `#cranberry`** (both 薔's and 薇's own stand-ins point here, full transitivity; tag already present). Pronunciation fields (cwangmiǝ/촹믜/ㄑ⺢ㄫㄇㄧㄜ) already verified as the correct concatenation — no bug; kwin:false already correct. Mandarin/korean/vietnamese confirmed standard and genuine. **Found and fixed a real bug**: japanese comma-joined ばら with しやうび, obsolete historical kana for しょうび — modernized, converted to list. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 薬.

### 2026-09-05, iteration 3161 — [[words/薬|薬]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Removed redundant 品詞. Checked three candidate homophones (約, 虐, 躍) — none independently legitimized, so no genuine homophone. Fixed a missing stand-in annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 薬丸.

### 2026-09-05, iteration 3162 — [[words/薬丸|薬丸]]

丸's own stand-in is this exact compound; 薬's own is [[薬]] itself — transitivity fails, no cranberry. Pronunciation fields ('yaghwan/약환/⼘ㄎㄏ⺢ㄋ) already verified as the correct concatenation — no bug. Added missing kwin:true. Filled blank japanese/korean/vietnamese — all real terms, but each in the reversed order (丸薬/환약/hoàn dược), matching this word's own already-listed reversed-order aliases. Fixed cantonese stray space (kept tone-sandhi notation). **Noted a romanization-style inconsistency** for future attention: `characters/薬 (char).md` and `words/薬.md` both use Yale-style cantonese "yeuk6" while this word correctly uses jyutping "joek6" for the same character — worth reconciling later. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 藍.

### 2026-09-05, iteration 3163 — [[words/藍|藍]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. **Found and fixed a real bug**: korean 남 (두음법칙-shifted) → 람 (unshifted, per standing rule). Fixed vietnamese null→lam. Added missing pos/kwin/japanese. Checked six candidate homophones — none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

Next: 藍木.

### 2026-09-05, iteration 3164 — [[words/藍木|藍木]]

No cranberry (both 藍's and 木's own stand-ins point to themselves). Pronunciation fields (lammog/람목/ㄌㄚㄇㄇㄛㄎ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Confirmed mandarin/korean legitimately use the reversed real-term order (木藍, already an alias), same pattern as [[薬丸]]. Japanese confirmed a genuine botanical-name substitution. Filled blank cantonese/vietnamese (reversed order). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 藍色.

### 2026-09-05, iteration 3165 — [[words/藍色|藍色]]

No cranberry (藍's own stand-in is [[藍]] itself, 色's is [[色彩]]). Pronunciation fields (lamsig/람식/ㄌㄚㄇㄙㄧㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Japanese confirmed genuine (native-reading compositional, matching -色 convention). **Found and fixed two real bugs**: korean 두음법칙-shifted form → 람색; vietnamese cây chàm (wrong sense, "plant" not "color") → màu chàm. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 藍領.

### 2026-09-05, iteration 3166 — [[words/藍領|藍領]]

No cranberry (藍's own stand-in is [[藍]] itself, 領's is [[領土]]). **Found and fixed two real bugs**: 羅馬字 lamlig missing 領's -ng final (諺文/注音 already correct) → lamling; cantonese leng5 didn't match 領's own ling5 → laam4ling5. kwin:false already correct. Japanese/korean confirmed genuine English-loanword substitutions. Filled blank vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蘇連.

### 2026-09-05, iteration 3167 — [[words/蘇連|蘇連]]

No cranberry (蘇's own stand-in is [[蘇生]], 連's is [[連]] itself). Pronunciation fields (solyen/소련/ㄙㄛㄌ⼶ㄋ) already verified as the correct concatenation — no bug; kwin:true already correct. Cantonese confirmed to legitimately use 聯's own reading (real term 蘇聯), just fixed the stray space. **Found and fixed a real bug**: japanese mixed katakana/hiragana (ソれん) → uniform katakana ソレン. Filled blank vietnamese (Liên Xô). Fixed a missing back-citation on `characters/蘇.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蘭月.

### 2026-09-05, iteration 3168 — [[words/蘭月|蘭月]]

No cranberry (蘭's own stand-in is [[蘭花]], 月's is [[月]] itself). Pronunciation fields (lan'wed/란웓/ㄌㄚㄋ·⼔ㄊ) already verified as the correct concatenation — no bug; kwin:false already correct. Korean already correctly unshifted. Japanese らんつき confirmed genuine, matching the on'yomi-only poetic-month precedent set by [[菊月]]. Fixed cantonese stray space, removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蘭花.

### 2026-09-05, iteration 3169 — [[words/蘭花|蘭花]]

蘭's own stand-in is this exact compound; 花's own is [[草花]] — transitivity fails, no cranberry. Pronunciation fields (lanhwa/란화/ㄌㄚㄋㄏ⺢) already verified as the correct concatenation — no bug. Added missing kwin:true. **Found and fixed a real bug**: japanese ランの花 (a phrase, not a word) → ラン, the standard word. Filled blank korean/vietnamese (hoa lan, real term, reversed order). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 虎.

### 2026-09-05, iteration 3170 — [[words/虎|虎]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/kwin/japanese. **Completed a three-way homophone group** with [[乎]]/[[呼]] (both already perfected and already anticipating this callout) — added the reciprocal callout here. In passing, fixed the 24th empty-string field bug (`characters/虎 (char).md` pos) and a missing self-citation on its own Words list. Stamped `date-last-perfect: 2026-09-05`.

Next: 虚.

### 2026-09-05, iteration 3171 — [[words/虚|虚]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/japanese, filled blank korean/vietnamese. **Found a genuine homophone** with [[許]] ("permit, allow") — added reciprocal callout, gave 許 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3172 — [[words/許|許]]

Single-character stand-in word (companion to 虚's homophone group). Fixed `vietnamese: null` → hứa. Added missing pos/kwin/japanese. Fixed a missing stand-in annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 虚偽.

### 2026-09-05, iteration 3173 — [[words/虚偽|虚偽]]

No cranberry (both 虚's and 偽's own stand-ins point to themselves). Pronunciation fields (hyo'wei/효웨/ㄏ⼄⼔ㄧ) already verified as the correct concatenation — no bug. Added missing kwin:false. Mandarin dual reading converted to list. **Found and fixed a real bug**: korean 허위의 had a stray genitive suffix — corrected to 허위. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 虱.

### 2026-09-05, iteration 3174 — [[words/虱|虱]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing japanese, filled blank vietnamese. In passing on `characters/虱 (char).md`: fixed bare-string aliases, removed redundant 品詞, fixed a missing self-citation, and properly integrated two dangling CC-lookup links into a formatted bullet. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 虹尊.

### 2026-09-05, iteration 3175 — [[words/虹尊|虹尊]]

No cranberry (虹's own stand-in is [[彩虹]], 尊's is [[尊厳]]; 尊 stands in for its own alias 鱒/鳟, matching the already-listed alias 虹鱒 and paralleling [[尊魚]]). Pronunciation fields (hongjon/홍존/ㄏㄛㄫㄐㄛㄋ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Mandarin/japanese confirmed genuine real terms. Fixed a stray space in korean, filled blank cantonese/vietnamese. Fixed a truncated rt-tag on `characters/尊.md`'s own citation. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 虹素.

### 2026-09-05, iteration 3176 — [[words/虹素|虹素]]

No cranberry (虹's own stand-in is [[彩虹]], 素's is [[要素]]). Periodic-table neologism (neon). Pronunciation fields (hongso/홍소/ㄏㄛㄫㄙㄛ) already verified as the correct concatenation — no bug. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Mandarin/cantonese confirmed to track the real modern element character 氖; korean/japanese/vietnamese all genuine transliterations. Removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蚊.

### 2026-09-05, iteration 3177 — [[words/蚊|蚊]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Filled blank pos/vietnamese. Homophone callout with [[紋]]/[[聞]] (the previously-flagged three-way group) already in place — re-verified with no additional matches (checked 吻/問/文). Fixed missing stand-in annotation on char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 蚊帳.

### 2026-09-05, iteration 3178 — [[words/蚊帳|蚊帳]]

帳's own stand-in is this exact compound; 蚊's own is [[蚊]] itself — transitivity fails, no cranberry. Pronunciation fields (munjwang/문좡/ㄇㄨㄋㄐ⺢ㄫ) already verified as the correct concatenation — no bug. Added missing kwin:false. **Found and fixed three real bugs**: mandarin typo (wénzhàn→wénzhàng); cantonese mis-transcribed vowel order (zeong3→zoeng3); japanese naive on'yomi instead of the real jukujikun reading (ぶんちょう→かや). Filled blank korean/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蚕箔.

### 2026-09-05, iteration 3179 — [[words/蚕箔|蚕箔]]

箔's own stand-in is this exact compound; 蚕's own is [[蚕]] itself — transitivity fails, no cranberry. Pronunciation fields (jambag/잠박/ㄐㄚㄇㄅㄚㄎ) already verified as the correct concatenation — no bug. Added missing kwin:false and pos. Filled blank japanese/korean (천박, a coincidental collision with the unrelated common word "vulgar"). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蛇.

### 2026-09-05, iteration 3180 — [[words/蛇|蛇]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Confirmed mandarin tā reflects a deliberate, already-documented vault choice (minority MC reading, anti-homophony) — not a bug, kept as-is. Removed redundant 品詞. Checked six candidate homophones — none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

Next: 蛋白.

### 2026-09-05, iteration 3181 — [[words/蛋白|蛋白]]

蛋's own stand-in is this exact compound; 白's own is [[白]] itself — transitivity fails, no cranberry. Pronunciation fields (danbag/단박/ㄉㄚㄋㄅㄚㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional (all also real common "protein" terms). Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蛍.

### 2026-09-05, iteration 3182 — [[words/蛍|蛍]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/kwin/japanese. **Found a genuine homophone** with [[迥]] ("distant, far") — added reciprocal callout, gave 迥 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3183 — [[words/迥|迥]]

Single-character stand-in word (companion to 蛍's homophone group). Added missing pos/kwin/japanese. Stamped `date-last-perfect: 2026-09-05`.

Next: 蛭.

### 2026-09-05, iteration 3184 — [[words/蛭|蛭]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/kwin/japanese. Fixed `vietnamese: null` → điệt. Homophone callout with [[直]]/[[膣]] (three-way group) already correctly in place — re-verified with no additional matches (checked 嫉/疾/質). Stamped `date-last-perfect: 2026-09-05`.

Next: 蛮人.

### 2026-09-05, iteration 3185 — [[words/蛮人|蛮人]]

蛮's own stand-in is this exact compound; 人's own is [[人]] itself — transitivity fails, no cranberry. Pronunciation fields (mannin/만닌/ㄇㄚㄋㄋㄧㄋ) already verified as the correct concatenation — no bug; kwin:false already correct. Mandarin/japanese confirmed real common terms; korean confirmed a coincidental homophone with an unrelated word. Filled blank cantonese/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蜘蛛.

### 2026-09-05, iteration 3186 — [[words/蜘蛛|蜘蛛]]

**Genuine `#cranberry`** (both 蜘's and 蛛's own stand-ins point here, full transitivity; tag already present). Pronunciation fields (jiju/지주/ㄐㄧㄐㄨ) already verified as the correct concatenation — no bug; kwin:true already correct. **Found and fixed two real bugs**: cantonese z1 zyu1 was malformed (missing a vowel) → zi1zyu1; japanese ちしゅ,ちちゅ was an inconsistent partial-on'yomi guess → くも, the real standard word for "spider." Korean/vietnamese confirmed compositional. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蜜月.

### 2026-09-05, iteration 3187 — [[words/蜜月|蜜月]]

No cranberry (蜜's own stand-in is [[蜂蜜]], 月's is [[月]] itself). **Found and fixed a real bug**: 羅馬字 mid'wet had a wrong final consonant on 月's syllable (諺文/注音 already correct) → mid'wed. **Found and fixed a real `kwin` bug** (true→false, AND-rule). Other fields confirmed standard and compositional (all real common terms). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蜜柑.

### 2026-09-05, iteration 3188 — [[words/蜜柑|蜜柑]]

柑's own stand-in is this exact compound; 蜜's own is [[蜂蜜]] — transitivity fails, no cranberry. Pronunciation fields (midgam/믿감/ㄇㄧㄊㄍㄚㄇ) already verified as the correct concatenation — no bug; kwin:true already correct. Fixed a typo in english ("mandarinn"→"mandarin"). Other fields confirmed standard and compositional. Filled blank vietnamese. Fixed cantonese stray space, missing back-citation on 柑.md. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蝉冠.

### 2026-09-05, iteration 3189 — [[words/蝉冠|蝉冠]]

No cranberry (蝉's own stand-in is [[蝉]] itself, 冠's is [[王冠]]). Pronunciation fields (sengwan/선관/ㄙㄝㄋㄍ⺢ㄋ) already verified as the correct concatenation — no bug; kwin:true already correct. Other fields confirmed standard and compositional. Filled blank vietnamese. Fixed cantonese stray space and a missing stand-in annotation on `characters/蝉 (char).md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蝎.

### 2026-09-05, iteration 3190 — [[words/蝎|蝎]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug; kwin:false already correct. Confirmed cantonese kit3 is a genuine irregular real-world reading, not a bug. Removed redundant 品詞, converted comma-joined vietnamese to a list. In passing on `characters/蝎 (char).md`: converted comma-joined vietnamese to list, added a missing Words section with self-citation, and properly integrated dangling CC-lookup links. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蝙蝠.

### 2026-09-05, iteration 3191 — [[words/蝙蝠|蝙蝠]]

**Genuine `#cranberry`** (both 蝙's and 蝠's own stand-ins point here, full transitivity; tag was already present on both char pages but missing from the word page — added here). Pronunciation fields (benfug/번뿍/ㄅㄝㄋㄈㄨㄎ) already verified as the correct concatenation — no bug. Added missing kwin:false. Mandarin dual reading converted to list. **Found and fixed a real bug**: cantonese bin2 didn't match 蝙's own bin1 — corrected. Split comma-joined korean (moved native 박쥐 to prose). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蝸牛.

### 2026-09-05, iteration 3192 — [[words/蝸牛|蝸牛]]

蝸's own stand-in is this exact compound; 牛's own is [[牛]] itself — transitivity fails, no cranberry. Pronunciation fields (gwanyu/과뉴/ㄍ⺢ㄋ⼜) already verified as the correct concatenation — no bug; kwin:false already correct. Mandarin dual reading converted to list. Japanese/vietnamese confirmed genuine real terms. Fixed cantonese stray space and a missing Words section on `characters/蝸.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 融.

### 2026-09-05, iteration 3193 — [[words/融|融]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug; kwin:true already correct. Added missing pos/japanese, filled blank vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 融化.

### 2026-09-05, iteration 3194 — [[words/融化|融化]]

No cranberry (both 融's and 化's own stand-ins point to themselves). Pronunciation fields ('yunghwa/융화/⼜ㄫㄏ⺢) already verified as the correct concatenation — no bug; kwin:true already correct. Other fields confirmed standard and compositional. Fixed an english typo, filled blank pos/vietnamese, fixed cantonese stray space, quoted hsk_level. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 融合.

### 2026-09-05, iteration 3195 — [[words/融合|融合]]

No cranberry (both 融's and 合's own stand-ins point to themselves) — closes out this previously-flagged known gap. Pronunciation fields ('yunggob/융곱/⼜ㄫㄍㄛㄆ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank pos/vietnamese, fixed cantonese stray space and a missing back-citation on `characters/合 (char).md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 融資.

### 2026-09-05, iteration 3196 — [[words/融資|融資]]

No cranberry (融's own stand-in is [[融]] itself, 資's is [[資本]]). **Found and fixed a real bug**: 羅馬字/諺文 'yongjiǝ/용즤 had a wrong vowel on 融's own syllable (注音 already correct) → 'yungjiǝ/융즤. kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 螳螂.

### 2026-09-05, iteration 3197 — [[words/螳螂|螳螂]]

**Genuine `#cranberry`** (both 螳's and 螂's own stand-ins point here, full transitivity; tag already present). Pronunciation fields (danglang/당랑/ㄉㄚㄫㄌㄚㄫ) already verified as the correct concatenation — no bug; kwin:true already correct. Vietnamese confirmed a genuine real-term substitution. **Found and fixed a real bug**: japanese たうらう used obsolete historical kana with the wrong on'yomi entirely → とうろう. Fixed cantonese stray space and a missing stand-in annotation on `characters/螂.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 螺旋.

### 2026-09-05, iteration 3198 — [[words/螺旋|螺旋]]

螺's own stand-in is this exact compound; 旋's own is [[旋転]] — transitivity fails, no cranberry. Pronunciation fields (laswen/라숸/ㄌㄚㄙ⼔ㄋ) already verified as the correct concatenation — no bug. Added missing kwin:false. Other fields confirmed standard and compositional (real common terms). Filled blank korean/vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 螺鈿.

### 2026-09-05, iteration 3199 — [[words/螺鈿|螺鈿]]

No cranberry (螺's own stand-in is [[螺旋]], 鈿's is a `名専字`). Pronunciation fields (laden/라던/ㄌㄚㄉㄝㄋ) already verified as the correct concatenation — no bug. Added missing kwin:false. Fixed an english typo (laquer→lacquer). Filled blank cantonese/korean/vietnamese. Fixed a missing Words section on `characters/鈿.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蟄.

### 2026-09-05, iteration 3200 — [[words/蟄|蟄]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing kwin/japanese. Fixed a missing stand-in annotation on the char page. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 蟹.

### 2026-09-05, iteration 3201 — [[words/蟹|蟹]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Added missing pos/kwin/japanese, fixed vietnamese null→giải. **Found a genuine homophone** with [[鞋]] ("shoe") — added reciprocal callout, gave 鞋 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3202 — [[words/鞋|鞋]]

Single-character stand-in word (companion to 蟹's homophone group). All other fields were already correctly filled; removed redundant 品詞. In passing, fixed the 25th empty-string field bug on `characters/鞋 (char).md` (hsk_level). Stamped `date-last-perfect: 2026-09-05`.

Next: 衆多.

### 2026-09-05, iteration 3203 — [[words/衆多|衆多]]

No cranberry (衆's own stand-in is [[大衆]], 多's is [[多]] itself). **Found and fixed three real bugs**: 羅馬字 jungda had a wrong vowel on 多's syllable (諺文/注音 already correct) → jungdǝ; japanese had a hidden zero-width space (しゅ​うた→しゅうた); korean 많은 was a native gloss, not the Sino-Korean reading (→중다). kwin:false already correct. Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衆議.

### 2026-09-05, iteration 3204 — [[words/衆議|衆議]]

No cranberry (衆's own stand-in is [[大衆]], 議's is [[議論]]). **Found and fixed a real bug**: 羅馬字 jung'wi was a recurrence of the resolved 義-family misreading (諺文/注音 already correct) → jung'ǝi. Added missing kwin:true. Other fields confirmed standard and compositional. Filled blank korean/vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衆議院.

### 2026-09-05, iteration 3205 — [[words/衆議院|衆議院]]

No cranberry (none of the three constituents' stand-ins point here). **Found and fixed the same 議-family 羅馬字 bug as [[衆議]]** (jung'wi'wen→jung'ǝi'wen; 諺文/注音 already correct). Added missing kwin:true. Mandarin/japanese confirmed real common terms. Filled blank korean/vietnamese. Fixed cantonese stray spaces (kept tone-sandhi notation). No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 行事.

### 2026-09-05, iteration 3206 — [[words/行事|行事]]

No cranberry (both 行's and 事's own stand-ins point to themselves). Pronunciation fields (hangji/항지/ㄏㄚㄫㄐㄧ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional (vietnamese hành sự also a real attested term). Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 行列.

### 2026-09-05, iteration 3207 — [[words/行列|行列]]

No cranberry (行's own stand-in is [[行]] itself, 列's is [[配列]]). Pronunciation fields (hangled/항럳/ㄏㄚㄫㄌㄝㄊ) already verified as the correct concatenation — no bug; kwin:false already correct. **Found and fixed a real bug**: japanese ぎやうれつ used obsolete historical kana → modern ぎょうれつ. Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 行動.

### 2026-09-05, iteration 3208 — [[words/行動|行動]]

No cranberry (both 行's and 動's own stand-ins point to themselves). Pronunciation fields (hangdong/항동/ㄏㄚㄫㄉㄛㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Fixed cantonese stray space and a missing back-citation on `characters/動 (char).md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 行星.

### 2026-09-05, iteration 3209 — [[words/行星|行星]]

No cranberry (both 行's and 星's own stand-ins point to themselves). Pronunciation fields (hangseng/항성/ㄏㄚㄫㄙㄝㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Japanese わくせい confirmed a legitimate real-term substitution (惑星, already an alias). Fixed cantonese stray space and a missing back-citation on `characters/星 (char).md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 街区.

### 2026-09-05, iteration 3210 — [[words/街区|街区]]

No cranberry (街's own stand-in is [[街道]], 区's is [[区域]]). Pronunciation fields (gyaiku/걔쿠/ㄍ⼘ㄧㄎㄨ) already verified as the correct concatenation — no bug. Added missing kwin:false. Mandarin/japanese confirmed real common terms. Filled blank cantonese/korean/vietnamese. Removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 街道.

### 2026-09-05, iteration 3211 — [[words/街道|街道]]

街's own stand-in is this exact compound; 道's own is [[道]] itself — transitivity fails, no cranberry. Pronunciation fields (gyaidau/걔닷/ㄍ⼘ㄧㄉㄚㄨ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衝.

### 2026-09-05, iteration 3212 — [[words/衝|衝]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Fixed vietnamese null→xung. Added missing pos/japanese. Genuine three-way homophone with [[塚]] (already perfected) and [[重]] (given a full pass too) — already documented on all pages. Checked four additional candidates, none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3213 — [[words/重|重]]

Single-character stand-in word (companion to 衝's homophone group). Added missing pos/japanese (real kun'yomi, correcting an unverifiable stored native reading), filled blank vietnamese. Fixed a missing self-citation on `characters/重 (char).md`. Stamped `date-last-perfect: 2026-09-05`.

Next: 衣服.

### 2026-09-05, iteration 3214 — [[words/衣服|衣服]]

No cranberry (衣's own stand-in is [[衣類]], 服's is [[服事]]). Pronunciation fields ('iǝbug/의북/ㄧㄜㄅㄨㄎ) already verified as the correct concatenation — no bug. Added missing kwin:false, pos. Split comma-joined korean (kept 의복, moved native 옷 to prose). Other fields confirmed standard and compositional. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衣襟.

### 2026-09-05, iteration 3215 — [[words/衣襟|衣襟]]

襟's own stand-in is this exact compound; 衣's own is [[衣類]] — transitivity fails, no cranberry. Pronunciation fields ('iǝgim/의김/ㄧㄜㄍㄧㄇ) already verified as the correct concatenation — no bug. Added missing kwin:false. Fixed three empty-string field bugs (korean/japanese/vietnamese all `""`) — filled with compositional readings. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衣類.

### 2026-09-05, iteration 3216 — [[words/衣類|衣類]]

衣's own stand-in is this exact compound; 類's own is [[種類]] — transitivity fails, no cranberry (already documented). Pronunciation fields ('iǝlui/의뤼/ㄧㄜㄌㄨㄧ) already verified as the correct concatenation — no bug; kwin:false already correct. All other fields were already correctly filled. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 表彰.

### 2026-09-05, iteration 3217 — [[words/表彰|表彰]]

No cranberry (表's own stand-in is [[表現]], 彰's is [[彰明]]). Pronunciation fields (byaucang/뱟창/ㄅ⼘ㄨㄑㄚㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 表明.

### 2026-09-05, iteration 3218 — [[words/表明|表明]]

No cranberry (表's own stand-in is [[表現]], 明's is [[明]] itself). Pronunciation fields (byaumyeng/뱟명/ㄅ⼘ㄨㄇ⼶ㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese, quoted hsk_level. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 表現.

### 2026-09-05, iteration 3219 — [[words/表現|表現]]

表's own stand-in is this exact compound; 現's own is [[現]] itself — transitivity fails, no cranberry. Pronunciation fields (byauhyen/뱟현/ㄅ⼘ㄨㄏ⼶ㄋ) already verified as the correct concatenation — no bug; kwin:false already correct. All other fields confirmed standard and compositional. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 表示.

### 2026-09-05, iteration 3220 — [[words/表示|表示]]

No cranberry (表's own stand-in is [[表現]], 示's is [[開示]]). Pronunciation fields (byauge/뱟거/ㄅ⼘ㄨㄍㄝ) already verified as the correct concatenation — no bug; kwin:false already correct. Confirmed 示's own divergent MC-derived syllable (ge/거/ㄍㄝ vs modern shì-like reflex) is genuine, matching the char page. Other fields confirmed standard and compositional. Filled blank vietnamese. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衰弱.

### 2026-09-05, iteration 3221 — [[words/衰弱|衰弱]]

衰's own stand-in is this exact compound; 弱's own is [[弱]] itself — transitivity fails, no cranberry. Pronunciation fields (sweinyag/쉐냑/ㄙ⼔ㄧㄋ⼘ㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Filled blank pos. Other fields confirmed standard and compositional. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 衰退.

### 2026-09-05, iteration 3222 — [[words/衰退|衰退]]

No cranberry (衰's own stand-in is [[衰弱]], 退's is [[退]] itself). Pronunciation fields (sweitiǝ/쉐틔/ㄙ⼔ㄧㄊㄧㄜ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Removed redundant 品詞. Fixed cantonese stray space and missing stand-in annotation. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 袂.

### 2026-09-05, iteration 3223 — [[words/袂|袂]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug; kwin:false already correct. Added missing japanese. Homophone callout with [[弥]] already correctly in place — re-verified, no additional matches. Fixed a missing stand-in annotation on the char page. Stamped `date-last-perfect: 2026-09-05`.

Next: 袋.

### 2026-09-05, iteration 3224 — [[words/袋|袋]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug; kwin:true already correct. Added missing pos/japanese. Homophone callout with [[大]]/[[台]] already correctly in place — re-verified, checked seven additional candidates, none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

Next: 袋鼠.

### 2026-09-05, iteration 3225 — [[words/袋鼠|袋鼠]]

No cranberry (袋's own stand-in is [[袋]] itself, 鼠's is [[熊鼠]]). Pronunciation fields (daisyo/대쇼/ㄉㄚㄧㄙ⼄) already verified as the correct concatenation — no bug; kwin:false already correct. Japanese/korean/vietnamese all confirmed genuine real-term substitutions. Fixed cantonese stray space and a missing back-citation on `characters/鼠.md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 袖.

### 2026-09-05, iteration 3226 — [[words/袖|袖]]

Single-character stand-in word — closes out the previously-flagged known gap. Pronunciation fields already matched the character's own values — no bug; kwin:false already correct. Added missing pos/japanese. Homophone callout with [[秀]] already correctly in place — re-verified, checked five additional candidates, none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

Next: 裁縫.

### 2026-09-05, iteration 3227 — [[words/裁縫|裁縫]]

裁's own stand-in is this exact compound; 縫's own is [[縫製]] — transitivity fails, no cranberry. Pronunciation fields (caibong/채봉/ㄑㄚㄧㄅㄛㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese. Removed redundant 品詞, fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 装置.

### 2026-09-05, iteration 3228 — [[words/装置|装置]]

No cranberry (both 装's and 置's own stand-ins point to themselves). Pronunciation fields (jwangci/좡치/ㄐ⺢ㄫㄑㄧ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank vietnamese (a coincidental collision with an unrelated word). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 裏面.

### 2026-09-05, iteration 3229 — [[words/裏面|裏面]]

裏's own stand-in is this exact compound; 面's own is [[表面]] — transitivity fails, no cranberry. **Found and fixed a real bug**: 注音 had a spurious null-onset separator and wrong vowel (羅馬字/諺文 already correct) → ㄌㄧㄇ⼶ㄋ. **Found and fixed a real `kwin` bug** (false→true). **Found and fixed two more real bugs**: japanese うちがわ (unrelated word 内側) → りめん (the real reading of 裏面 itself); korean 안 (unrelated native gloss) → 이면 (real Sino-Korean reading). Filled blank vietnamese. Fixed cantonese stray space and matching rt-tags on both character pages. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 補充.

### 2026-09-05, iteration 3230 — [[words/補充|補充]]

No cranberry (補's own stand-in is [[修補]], 充's is [[充填]]). Pronunciation fields (bocung/보충/ㄅㄛㄑㄨㄫ) already verified as the correct concatenation — no bug; kwin:true already correct. Other fields confirmed standard and compositional. Fixed cantonese stray space, quoted hsk_level. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 補助.

### 2026-09-05, iteration 3231 — [[words/補助|補助]]

No cranberry (補's own stand-in is [[修補]], 助's is [[援助]]). Pronunciation fields (bojo/보조/ㄅㄛㄐㄛ) already verified as the correct concatenation — no bug; kwin:true already correct. Mandarin/japanese/korean confirmed real common terms; vietnamese confirmed a legitimate real-term substitution. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 補給.

### 2026-09-05, iteration 3232 — [[words/補給|補給]]

給's own stand-in is this exact compound; 補's own is [[修補]] — transitivity fails, no cranberry (already documented). Pronunciation fields (bogib/보깁/ㄅㄛㄍㄧㄆ) already verified as the correct concatenation — no bug; kwin:false already correct. Filled blank cantonese/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 補習.

### 2026-09-05, iteration 3233 — [[words/補習|補習]]

No cranberry (補's own stand-in is [[修補]], 習's is [[練習]]). **Found and fixed a real bug**: 羅馬字/諺文 bosib/보십 didn't match 習's own sǝb/습 (注音 already correct) → bosǝb/보습. **Found and fixed a real `kwin` bug** (false→true, AND-rule). Other fields confirmed standard and compositional. Filled blank vietnamese, quoted hsk_level, fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 裸.

### 2026-09-05, iteration 3234 — [[words/裸|裸]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. **Found and fixed a real bug**: korean 나 (두음법칙-shifted) → 라 (unshifted, per standing rule). Added missing pos/kwin/japanese. Reformatted a malformed vietnamese string into a proper list. Checked five candidate homophones — none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

Next: 製作.

### 2026-09-05, iteration 3235 — [[words/製作|製作]]

製's own stand-in is this exact compound; 作's own is [[作]] itself — transitivity fails, no cranberry. Pronunciation fields (jejag/저작/ㄐㄝㄐㄚㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional (vietnamese chế tác also a real term). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 製品.

### 2026-09-05, iteration 3236 — [[words/製品|製品]]

No cranberry (製's own stand-in is [[製作]], 品's is [[品]] itself). Pronunciation fields (jepum/저품/ㄐㄝㄆㄨㄇ) already verified as the correct concatenation — no bug; kwin:false already correct. Mandarin/japanese/korean confirmed real common terms; vietnamese confirmed a legitimate real-term substitution. Fixed cantonese stray space and a missing stand-in annotation on `characters/品 (char).md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 複数.

### 2026-09-05, iteration 3237 — [[words/複数|複数]]

No cranberry (複's own stand-in is [[重複]], 数's is [[計数]]). Pronunciation fields (bugsu/북수/ㄅㄨㄎㄙㄨ) already verified as the correct concatenation — no bug; kwin:false already correct. **Found and fixed a real bug**: cantonese fuk1 sou3 didn't match 数's own sou2 (wrong tone) — corrected. Other fields confirmed standard and compositional. Filled blank vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 褐.

### 2026-09-05, iteration 3238 — [[words/褐|褐]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug. Fixed vietnamese null→hạt. Added missing pos/japanese. **Found a genuine homophone** with [[轄]] ("linchpin, control") — added reciprocal callout, gave 轄 a full pass too. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-05, iteration 3239 — [[words/轄|轄]]

Single-character stand-in word (companion to 褐's homophone group). Added missing japanese. Stamped `date-last-perfect: 2026-09-05`.

Next: 褐金.

### 2026-09-05, iteration 3240 — [[words/褐金|褐金]]

No cranberry (both 褐's and 金's own stand-ins point to themselves). Periodic-table neologism (holmium). Pronunciation fields (hadgim/핟김/ㄏㄚㄊㄍㄧㄇ) already verified as the correct concatenation — no bug; kwin:false already correct. Mandarin/cantonese confirmed to track the real modern element name 钬; korean/japanese/vietnamese all genuine transliterations. Removed redundant 品詞. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 褒.

### 2026-09-05, iteration 3241 — [[words/褒|褒]]

Single-character stand-in word. Pronunciation fields already matched the character's own values — no bug; kwin:false already correct. Confirmed the unusual-looking 諺文 팟 (vowel-final syllable with a batchim) is the vault's established consistent convention, matching both the character page and the syllable master page — not a bug. Added missing pos/japanese. Fixed vietnamese null→bao. Checked three candidate homophones — none independently legitimized. Stamped `date-last-perfect: 2026-09-05`.

Next: 西北.

### 2026-09-05, iteration 3242 — [[words/西北|西北]]

No cranberry (西's own stand-in is [[西方]], 北's is [[北方]]). Pronunciation fields (seibug/세북/ㄙㄝㄧㄅㄨㄎ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional (vietnamese tây bắc also a real region name). Fixed cantonese stray space, quoted hsk_level. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 西方.

### 2026-09-05, iteration 3243 — [[words/西方|西方]]

西's own stand-in is this exact compound; 方's own is [[方向]] — transitivity fails, no cranberry. Pronunciation fields (seifang/세빵/ㄙㄝㄧㄈㄚㄫ) already verified as the correct concatenation — no bug; kwin:false already correct. **Found and fixed a real bug**: cantonese xi1 fang1 was invalid jyutping — corrected to sai1fong1. Other fields confirmed standard and compositional. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 西洋.

### 2026-09-05, iteration 3244 — [[words/西洋|西洋]]

No cranberry (西's own stand-in is [[西方]], 洋's is [[大洋]]). **Found and fixed a real bug**: 注音 was missing the null-onset separator before 洋's own vowel-initial syllable (ㄙㄝㄧ⼘ㄫ→ㄙㄝㄧ·⼘ㄫ), matching the established convention already used on [[大洋]] — fixed the matching citations on both `characters/洋.md` and `characters/西.md`. kwin:false already correct. Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 西班牙.

### 2026-09-05, iteration 3245 — [[words/西班牙|西班牙]]

No cranberry (none of the three constituents' stand-ins point here). Pronunciation fields (seipan'a/세판아/ㄙㄝㄧㄆㄚㄋ·ㄚ) already verified as the correct concatenation, including the null-onset syllable break — no bug; kwin:false already correct. As a proper place name, other-language fields legitimately hold the real attested name/transliteration. Fixed cantonese stray spaces and a missing stand-in annotation on `characters/班 (char).md`. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 西班牙語.

### 2026-09-05, iteration 3246 — [[words/西班牙語|西班牙語]]

No cranberry (all four constituents separately legitimized elsewhere). **Found and fixed two real bugs**: 注音 was missing the null-onset separator before 牙's syllable (matching [[西班牙]]'s own established pattern) — fixed here and on the matching citations on `characters/班 (char).md`, `characters/牙.md`, and `characters/語.md`; aliases wrongly self-listed the headword as its own alias — removed. kwin:false already correct. Other fields confirmed genuine real attested terms. Fixed cantonese stray spaces. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 西瓜.

### 2026-09-05, iteration 3247 — [[words/西瓜|西瓜]]

No cranberry (西's own stand-in is [[西方]], 瓜's is [[胡瓜]]). Pronunciation fields (seigwa/세과/ㄙㄝㄧㄍ⺢) already verified as the correct concatenation — no bug. Added missing kwin:false. **Found and fixed a real bug**: japanese すいくわ used obsolete historical kana → modern すいか. Split comma-joined korean (moved native 수박 to prose). Filled blank vietnamese (real term). Fixed cantonese stray space. No homophones. Stamped `date-last-perfect: 2026-09-05`.

Next: 西端.

### 2026-09-05, iteration 3248 — [[words/西端|西端]]

No cranberry (西's own stand-in is [[西方]], 端's is [[末端]]). Pronunciation fields (seidwan/세돤/ㄙㄝㄧㄉ⺢ㄋ) already verified as the correct concatenation — no bug; kwin:false already correct. Other fields confirmed standard and compositional. Filled blank cantonese/vietnamese. No homophones. Stamped `date-last-perfect: 2026-09-05`.

### 2026-09-06, iteration 3249 — [[words/西部|西部]]
Verified concatenation (sei/세/ㄙㄝㄧ + bou/봇/ㄅㄛㄨ = seibou/세봇/ㄙㄝㄧㄅㄛㄨ) already matched stored fields — no bug. 西's own stand_in is 西方; 部's own stand_in is 部 itself — no cranberry. kwin AND-rule (西 false, 部 false → false) already correct. Fixed cantonese's stray space (sai1 bou6 → sai1bou6). Filled blank vietnamese (tây bộ, compositional). Removed blank hsk_level/swadesh. Fixed a missing "(stand-in for 部)" annotation on `characters/部 (char).md`'s own [[部]] citation. homophone_check.py found no independent homophones. Wrote Notes/Etymology sections.

### 2026-09-06, iteration 3250 — [[words/要約|要約]]
No cranberry (要's own stand-in is [[重要]], 約's own stand-in is [[約束]]). Pronunciation fields ('you'yag/욧약/⼄ㄨ⼘ㄎ) already matched the straightforward concatenation — no bug. kwin AND-rule (要 false, 約 true → false) already correct. Filled blank mandarin (yāoyuē, real legal term "offer"), cantonese (jiu3joek3), and vietnamese (yếu ước, compositional using each constituent's own established compound-context reading). Added missing simplified alias 要约. Converted characters to flow-style YAML. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3251 — [[words/要素|要素]]
No cranberry (要's own stand-in is [[重要]]; 素's own stand-in is [[要素]] itself, but transitivity fails since 要's doesn't match — one-sided legitimization, not cranberry). Pronunciation fields ('youso/욧소/⼄ㄨㄙㄛ) already matched the straightforward concatenation — no bug. kwin AND-rule (要 false, 素 true → false) already correct. **Found and fixed a real bug**: japanese had えうそ, obsolete historical kana — corrected to modern ようそ. Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3252 — [[words/覆蓋|覆蓋]]
**Genuine `#cranberry`** (both 覆's and 蓋's own stand-ins point to this exact compound — full transitivity). **Found and fixed a real bug**: 羅馬字/諺文 had puggai/푹개 instead of 覆's own fug/뿍 (注音 already correct — same failure class as the earlier 福-family voiced/voiceless confusion bug). Filled blank korean (복개) and vietnamese (phủ cái, compositional). Converted comma-joined cantonese into a proper list (all three attested real readings). Added missing kwin (false, AND-rule). Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3253 — [[words/覇権|覇権]]
No cranberry (覇's own stand-in is this exact compound; 権's own stand-in is [[権利]]). Pronunciation fields (bagwen/바권/ㄅㄚㄍ⼔ㄋ) already matched the straightforward concatenation — no bug. kwin AND-rule (覇 false, 権 true → false) already correct. Fixed cantonese stray space. Filled blank vietnamese (bá quyền, real standard term). Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3254 — [[words/規則|規則]]
No cranberry (規's own stand-in is [[規律]], 則's own stand-in is [[法則]]). Pronunciation fields (guijug/귀죽/ㄍㄨㄧㄐㄨㄎ) already matched the straightforward concatenation — no bug. kwin AND-rule (both false → false) already correct. **Found and fixed a real bug**: stray body text wrongly claimed this word was 則's stand-in legitimizer (same failure mode as 禍害's earlier fix) — removed, replaced with proper Notes. Fixed cantonese stray space, removed blank hsk_level/swadesh, and a typo ("principial"→"principle") on `characters/則.md`'s own citation. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3255 — [[words/視|視]]
Single-character stand-in word (視's own stand-in is 視 itself). Pronunciation fields (siǝ/싀/ㄙㄧㄜ) already matched the character's own stored reading — no bug. Added missing pos/kwin/japanese. homophone_check.py confirmed existing [[四]]/[[矢]] callouts complete — several other characters (師/死/氏/獅/私/肆/諡) share this syllable but none has its own independently legitimized word page.

### 2026-09-06, iteration 3256 — [[words/視覚|視覚]]
No cranberry (視's own stand-in is [[視]] itself, 覚's own stand-in is [[感覚]]). Pronunciation fields (siǝgag/싀각/ㄙㄧㄜㄍㄚㄎ) already matched the straightforward concatenation — no bug. kwin AND-rule (視 false, 覚 true → false) already correct. Fixed cantonese stray space; all other fields already correct and standard. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3257 — [[words/覚醒|覚醒]]
No cranberry (覚's own stand-in is [[感覚]], 醒's own stand-in is this exact compound). Pronunciation fields (gagseng/각성/ㄍㄚㄎㄙㄝㄫ) already matched the straightforward concatenation — no bug. **Added missing `kwin`** (true, AND-rule: both constituents individually true). Filled blank korean (각성) and vietnamese (giác tỉnh, compositional). Converted comma-joined cantonese into a proper list (both attested real readings). Removed blank hsk_level/swadesh. Fixed a grammar typo ("be disillusion"→"be disillusioned") propagated on both character pages' citations — caught and corrected an accidental duplicate line created while fixing `characters/覚.md`. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3258 — [[words/親切|親切]]
No cranberry (親's own stand-in is [[親戚]], 切's own stand-in is [[切]] itself). **Found and fixed two real bugs**: 羅馬字 had cincet instead of 切's own cinced (諺文/注音 already correct); vietnamese held the literal placeholder "2" — corrected to thân thiết (compositional, also the real standard term). kwin false already correct (AND-rule: 親 true, 切 false). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3259 — [[words/親戚|親戚]]
No cranberry (親's own stand-in is this exact compound, 戚's own stand-in is [[哀戚]]). Pronunciation fields (cinceg/친척/ㄑㄧㄋㄑㄝㄎ) already matched the straightforward concatenation — no bug. **Found and fixed two real bugs**: kwin was stored false despite both constituents individually true — corrected to true; korean had 차척 instead of compositional/real 친척. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3260 — [[words/親族|親族]]
No cranberry (親's own stand-in is [[親戚]], 族's own stand-in is [[家族]]). Pronunciation fields (cinjog/친족/ㄑㄧㄋㄐㄛㄎ) already matched the straightforward concatenation — no bug. kwin true already correct (AND-rule: both individually true). Fixed cantonese stray space; all other fields already correct and standard. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3261 — [[words/観測|観測]]
No cranberry (観's own stand-in is [[観察]], 測's own stand-in is [[測量]]). **Found and fixed a real bug**: 羅馬字 had gwancig instead of 測's own gwancǝg (諺文/注音 already correct). kwin true already correct (AND-rule: both individually true). Filled blank vietnamese (quan trắc, real standard scientific term) — in passing, added 観's own previously-blank vietnamese reading (quan) to `characters/観.md`. Fixed cantonese stray space, quoted hsk_level. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3262 — [[words/角逐|角逐]]
No cranberry (角's own stand-in is [[角]] itself, 逐's own stand-in is [[追逐]]). Pronunciation fields (gogdug/곡둑/ㄍㄛㄎㄉㄨㄎ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Converted comma-joined mandarin into a list (角 carries an irregular secondary jué reading here, kept alongside its own jiǎo). Fixed cantonese stray space. Filled blank vietnamese (giác trục, compositional). Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3263 — [[words/解|解]]
Single-character stand-in word (解's own stand-in is 解 itself). Pronunciation fields (gyai/걔/ㄍ⼘ㄧ) already matched the character's own stored reading — no bug. Added missing pos/japanese. Completed a genuine homophone callout already anticipated by [[佳]]'s own page (both share gyai/걔/ㄍ⼘ㄧ) — checked [[街]], which shares the same syllable but isn't independently legitimized, so no callout needed there. Fixed a missing "(stand-in for 解)" citation entirely absent from `characters/解 (char).md`'s own Words list.

### 2026-09-06, iteration 3264 — [[words/解剖|解剖]]
No cranberry (解's own stand-in is [[解]] itself, 剖's own stand-in is this exact compound). Pronunciation fields (gyaifou/걔뽓/ㄍ⼘ㄧㄈㄛㄨ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3265 — [[words/解放|解放]]
No cranberry (解's own stand-in is [[解]] itself, 放's own stand-in is [[釈放]]). **Found and fixed a real bug**: 羅馬字/諺文 had gyaibang/걔방 instead of 放's own gyaifang/걔빵 (注音 already correct — same failure class as the 福/覆蓋-family voiced/voiceless confusion bug). kwin false already correct (AND-rule). Filled blank pos (動詞). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3266 — [[words/解禁|解禁]]
No cranberry (解's own stand-in is [[解]] itself, 禁's own stand-in is [[禁止]]). Pronunciation fields (gyaigim/걔김/ㄍ⼘ㄧㄍㄧㄇ) already matched the straightforward concatenation — no bug. **Added missing `kwin`** (false, AND-rule). Fixed cantonese stray space; all other fields already correct and standard. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3267 — [[words/言語|言語]]
No cranberry (言's own stand-in is [[言]] itself, 語's own stand-in is this exact compound). Pronunciation fields ('en'yo/언요/ㄝㄋ·⼄) already matched the straightforward concatenation, including the correct null-onset separator dot — no bug. kwin false already correct (AND-rule). Mandarin/cantonese legitimately cite the same real term as [[語言]] (Mandarin/Cantonese have no reversed-order word); japanese/korean/vietnamese correctly reflect this word's own 言-then-語 order. **Found and fixed a real bug**: `aliases` wrongly listed [[語言]]/语言 as orthographic variants — 語言 is a distinct, separately-perfected word with its own different reading, not an alias; corrected to genuine simplified variant 言语. Fixed cantonese stray space, removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3268 — [[words/訃告|訃告]]
No cranberry (訃's own stand-in is this exact compound, 告's own stand-in is [[告訴]]). Pronunciation fields (fuogau/뿟갓/ㄈㄨㄛㄍㄚㄨ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3269 — [[words/計画|計画]]
No cranberry (計's own stand-in is this exact compound, 画's own stand-in is [[絵画]]). Pronunciation fields (geihwag/게확/ㄍㄝㄧㄏ⺢ㄎ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Confirmed the stored aliases (計劃/计划) are genuine real orthographic variants, unlike the false-alias bug just fixed on [[言語]]. Quoted hsk_level, removed blank swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3270 — [[words/討伐|討伐]]
No cranberry (討's own stand-in is [[討論]], 伐's own stand-in is this exact compound). Pronunciation fields (taufed/탓뻗/ㄊㄚㄨㄈㄝㄊ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). In passing, fixed an empty-string `pos: ""` bug on `characters/討.md`. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3271 — [[words/討論|討論]]
No cranberry (討's own stand-in is this exact compound, 論's own stand-in is [[理論]]). Pronunciation fields (taulon/탓론/ㄊㄚㄨㄌㄛㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space, removed blank swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3272 — [[words/記憶|記憶]]
**Genuine `#cranberry`** (both 記's and 憶's own stand-ins point to this exact compound — full transitivity). **Found and fixed a real bug**: 注音 was missing the null-onset separator dot before 憶's vowel-initial syllable (ㄍㄧㄧㄎ→ㄍㄧ·ㄧㄎ), matching the already-correct 羅馬字/諺文 — same failure class as 西洋's earlier fix. Fixed also on `characters/記.md` and `characters/憶.md`'s own citations, and added a missing "(stand-in for 憶)" annotation that was entirely absent from `characters/憶.md`. kwin false already correct (AND-rule). Filled blank vietnamese (ký ức). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3273 — [[words/記者|記者]]
No cranberry (記's own stand-in is [[記憶]], 者's own stand-in is [[者]] itself). Pronunciation fields (gica/기차/ㄍㄧㄑㄚ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Filled blank vietnamese (ký giả, real standard term). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3274 — [[words/記載|記載]]
No cranberry (記's own stand-in is [[記憶]], 載's own stand-in is [[載]] itself). Pronunciation fields (gijai/기재/ㄍㄧㄐㄚㄧ) already matched the straightforward concatenation — no bug. kwin true already correct (AND-rule). Filled blank vietnamese (ký tải, compositional, same ký- pattern as [[記者]]/[[記憶]]). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3275 — [[words/記録|記録]]
No cranberry (記's own stand-in is [[記憶]], 録's own stand-in is [[抄録]]). Pronunciation fields (gilog/기록/ㄍㄧㄌㄛㄎ) already matched the straightforward concatenation — no bug. kwin true already correct (AND-rule). **Found and fixed a real bug**: stray body text wrongly claimed this word was the stand-in for both 記 and 録 — neither is true (same failure mode as 規則's earlier fix). Filled blank vietnamese (ký lục). Fixed cantonese stray space. Removed blank hsk_level/swadesh. Confirmed stored aliases are genuine real orthographic variants. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3276 — [[words/訥|訥]]
Single-character stand-in word (訥's own stand-in is 訥 itself). Pronunciation fields (nod/녿/ㄋㄛㄊ) already matched the character's own stored reading — no bug. Added missing kwin/japanese, fixed bare-string characters format. Fixed a missing "(stand-in for 訥 (char))" annotation on `characters/訥 (char).md`'s own Words list. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3277 — [[words/訪問|訪問]]
No cranberry (訪's own stand-in is this exact compound, 問's own stand-in is [[質問]]). **Found and fixed a real bug**: 羅馬字/諺文 had pangmun/팡문 instead of 訪's own fangmun/빵문 (注音 already correct — same failure class as the 福/覆蓋/解放-family voiced/voiceless confusion bug). kwin false already correct (AND-rule). Fixed cantonese stray space, quoted hsk_level, removed blank swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3278 — [[words/設備|設備]]
No cranberry (設's own stand-in is [[建設]], 備's own stand-in is [[準備]]). Pronunciation fields (sedbiǝ/섣븨/ㄙㄝㄊㄅㄧㄜ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3279 — [[words/設置|設置]]
No cranberry (設's own stand-in is [[建設]], 置's own stand-in is [[置]] itself). Pronunciation fields (sedci/섣치/ㄙㄝㄊㄑㄧ) already matched the straightforward concatenation — no bug. kwin true already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3280 — [[words/設計|設計]]
No cranberry (設's own stand-in is [[建設]], 計's own stand-in is [[計画]]). **Found and fixed a real bug**: 注音 had ㄙㄝㄊㄐㄝㄧ instead of the correct ㄙㄝㄊㄍㄝㄧ (計's own 注音 is ㄍㄝㄧ) — unusually, 羅馬字/諺文 (sedgei/섣게) were already correct, the reverse of the usual failure direction. Fixed also on `characters/設.md` and `characters/計.md`'s own citations. kwin false already correct (AND-rule). Fixed cantonese stray space, quoted hsk_level, removed blank swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3281 — [[words/許可|許可]]
No cranberry (both 許's and 可's own stand-ins point to themselves). Pronunciation fields (hyokǝ/효크/ㄏ⼄ㄎㄜ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space. Filled blank vietnamese (hứa khả, compositional). homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3282 — [[words/訴訟|訴訟]]
No cranberry (訴's own stand-in is this exact compound, 訟's own stand-in is [[訟]] itself). Pronunciation fields (sosyong/소숑/ㄙㄛㄙ⼄ㄫ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Filled blank pos (動詞) and vietnamese (tố tụng, real standard term). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3283 — [[words/診断|診断]]
No cranberry (診's own stand-in is this exact compound, 断's own stand-in is [[割断]]). Pronunciation fields (jindwan/진돤/ㄐㄧㄋㄉ⺢ㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). **Found and fixed a real bug**: cantonese had the wrong tone (dyun3) not matching 断's own stored dyun6 — corrected both attested variants. Filled blank vietnamese (chẩn đoán, real standard term). Quoted hsk_level. Confirmed stored aliases are genuine real orthographic variants. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3284 — [[words/証人|証人]]
No cranberry (証's own stand-in is [[証明]], 人's own stand-in is [[人]] itself). Pronunciation fields (jingnin/징닌/ㄐㄧㄫㄋㄧㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space, removed blank hsk_level/swadesh. **Flagged (not fixed)**: `characters/人 (char).md` is in the same badly-degraded state as `characters/一 (char).md` (mixed list styles, missing rt tags including this word's own citation) — needs its own dedicated cleanup pass. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3285 — [[words/証券|証券]]
No cranberry (証's own stand-in is [[証明]], 券's own stand-in is [[券]] itself). Pronunciation fields (jingkon/징콘/ㄐㄧㄫㄎㄛㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3286 — [[words/証拠|証拠]]
No cranberry (証's own stand-in is [[証明]], 拠's own stand-in is [[依拠]]). Pronunciation fields (jinggyo/징교/ㄐㄧㄫㄍ⼄) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space, quoted hsk_level. Confirmed stored aliases are genuine real orthographic variants. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3287 — [[words/証明|証明]]
No cranberry (証's own stand-in is this exact compound, 明's own stand-in is [[明]] itself). Pronunciation fields (jingmyeng/징명/ㄐㄧㄫㄇ⼶ㄫ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3288 — [[words/評価|評価]]
No cranberry (評's own stand-in is this exact compound, 価's own stand-in is [[価格]]). Pronunciation fields (byengga/병가/ㄅ⼶ㄫㄍㄚ) already matched the straightforward concatenation — no bug. **Added missing `kwin`** (false, AND-rule). Filled blank vietnamese (bình giá, real standard term). Fixed cantonese stray space. Confirmed stored alias is a genuine real orthographic variant. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3289 — [[words/評論|評論]]
No cranberry (評's own stand-in is [[評価]], 論's own stand-in is [[理論]]). Pronunciation fields (byenglon/병론/ㄅ⼶ㄫㄌㄛㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Filled blank pos (名詞). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3290 — [[words/詞典|詞典]]
No cranberry (詞's own stand-in is [[単詞]], 典's own stand-in is [[事典]]). Pronunciation fields (saden/사던/ㄙㄚㄉㄝㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). **Found and fixed two real bugs**: vietnamese had tự điển (contaminated from sibling word [[字典]]'s own reading) instead of the real từ điển; aliases wrongly listed 辭典/辞典/辞書 as orthographic variants — 辭/辞 is a distinct character with its own separate Dan'a'yo reading (ci/치/ㄑㄧ, own stand-in [[辞職]]), same false-alias failure mode as [[言語]]'s earlier fix. Kept only the genuine simplified alias 词典. Fixed cantonese stray space, quoted hsk_level. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3291 — [[words/詞句|詞句]]
No cranberry (詞's own stand-in is [[単詞]], 句's own stand-in is [[句]] itself). Pronunciation fields (sagu/사구/ㄙㄚㄍㄨ) already matched the straightforward concatenation — no bug. **Found and fixed several real bugs**: kwin false→true (both constituents individually true, AND-rule); japanese/korean/vietnamese all held readings contaminated from the unrelated sibling term 語句 (built on 語 not 句) — corrected to compositional じく/사구/từ cú. Mandarin cíjù confirmed genuinely real and standard. Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3292 — [[words/詞彙|詞彙]]
No cranberry (詞's own stand-in is [[単詞]], 彙's own stand-in is [[彙]] itself). Pronunciation fields (sahu/사후/ㄙㄚㄏㄨ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). **Found and fixed a real bug**: cantonese had wui6, not matching 彙's own stored wai6 — corrected to ci4wai6. In passing, fixed a malformed comma-joined vietnamese field on `characters/彙 (char).md`. Japanese/korean correctly left blank (real term uses 語彙, not 詞彙) — already documented. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3293 — [[words/詠春拳|詠春拳]]
No cranberry (詠's own stand-in is [[詠]] itself, 春's own stand-in is [[春]] itself, 拳's own stand-in is [[拳骨]]). Pronunciation fields ('wingcungwen/윙춘권/ㄨㄧㄫㄑㄨㄋㄍ⼔ㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). All other-language fields confirmed standard, real-attested transliterations of this martial-art proper noun. Fixed cantonese stray spaces. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3294 — [[words/詣|詣]]
Single-character stand-in word (詣's own stand-in is 詣 itself). Pronunciation fields ('ei/에/ㄝㄧ) already matched the character's own stored reading — no bug. Added missing kwin/japanese. Completed a genuine homophone callout already anticipated by [[児]]'s own page (both share 'ei/에/ㄝㄧ). Checked [[羿]]/[[霓]], which share the syllable but aren't independently legitimized — no callout needed. homophone_check.py confirmed no other homophones.

### 2026-09-06, iteration 3295 — [[words/試験|試験]]
No cranberry (試's own stand-in is [[考試]], 験's own stand-in is this exact compound). Pronunciation fields (si'em/시엄/ㄙㄧ·ㄝㄇ) already matched the straightforward concatenation, including the correct null-onset dot — no bug. kwin false already correct (AND-rule). Korean 시험 legitimately diverges from the Dan'a'yo-internal assignment (real word vs. assigned syllable). Fixed cantonese stray space, removed redundant duplicate 品詞 field. In passing, fixed a missing "(stand-in for 験 (char))" annotation and a malformed non-ruby citation on `characters/験 (char).md`'s own Words list. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3296 — [[words/詩人|詩人]]
No cranberry (詩's own stand-in is [[詩歌]], 人's own stand-in is [[人]] itself). Pronunciation fields (sinin/시닌/ㄙㄧㄋㄧㄋ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard (already-thorough Notes kept). homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3297 — [[words/詩歌|詩歌]]
No cranberry (詩's own stand-in is this exact compound, 歌's own stand-in is [[歌曲]]). **Found and fixed two real bugs**: 羅馬字/諺文/注音 all had siga/시가/ㄙㄧㄍㄚ instead of the correct sigǝ/시그/ㄙㄧㄍㄜ (歌's own reading is gǝ/그/ㄍㄜ, not ga/가/ㄍㄚ) — fixed also on `characters/詩.md` and `characters/歌.md`'s own citations (caught and corrected an accidental duplicate line created while fixing 詩.md); kwin was stored true despite 歌 being individually false — corrected to false (AND-rule). Filled blank vietnamese (thi ca, real standard term). Fixed cantonese stray space, removed redundant duplicate 品詞. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3298 — [[words/詩経|詩経]]
No cranberry (詩's own stand-in is [[詩歌]], 経's own stand-in is [[経]] itself). Pronunciation fields (sigeng/시겅/ㄙㄧㄍㄝㄫ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space; all other fields already correct, real proper-noun transliterations. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3299 — [[words/該|該]]
Single-character stand-in word (該's own stand-in is 該 itself). Pronunciation fields (goi/괴/ㄍㄛㄧ) already matched the character's own stored reading — no bug. Added missing pos/japanese/kwin. **Found and fixed a real bug**: vietnamese held the literal string "null" — corrected to cai (compositional). homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3300 — [[words/詳細|詳細]]
No cranberry (詳's own stand-in is this exact compound, 細's own stand-in is [[細]] itself). Pronunciation fields (sangsei/상세/ㄙㄚㄫㄙㄝㄧ) already matched the straightforward concatenation — no bug. kwin true already correct (AND-rule). Filled blank vietnamese (tường tế, compositional). Fixed cantonese stray space. In passing, fixed a non-standard jyutping romanization (cheung4→coeng4) and converted malformed comma-joined mandarin/vietnamese/aliases fields into proper YAML lists on `characters/詳.md`. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3301 — [[words/誅殺|誅殺]]
No cranberry (誅's own stand-in is this exact compound, 殺's own stand-in is [[殺]] itself). Pronunciation fields (jusad/주삳/ㄐㄨㄙㄚㄊ) already matched the straightforward concatenation — no bug. **Added missing `kwin`** (true, AND-rule). Filled blank vietnamese (tru sát, compositional). Fixed cantonese stray space. In passing, fixed an empty-string `hsk_level: ""` bug on `characters/誅.md` (→ 無) and added it to `lookup/HSK/HSK No.md`. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3302 — [[words/誇示|誇示]]
No cranberry (誇's own stand-in is [[誇]] itself, 示's own stand-in is [[開示]]). Pronunciation fields (kwage/콰거/ㄎ⺢ㄍㄝ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Filled blank cantonese (kwaa1si6) and vietnamese (khoa thị, compositional). Fixed bare-string characters entry. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3303 — [[words/認証|認証]]
No cranberry (認's own stand-in is [[認識]], 証's own stand-in is [[証明]]). Pronunciation fields (ninjing/닌징/ㄋㄧㄋㄐㄧㄫ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Confirmed genuine homophone with [[人証]] (認's own reading coincidentally matches 人's own reading exactly). Filled blank vietnamese (nhận chứng, compositional). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py confirmed no other homophones.

### 2026-09-06, iteration 3304 — [[words/認識|認識]]
**Genuine `#cranberry`** (both 認's and 識's own stand-ins point to this exact compound — full transitivity). Pronunciation fields (ninsig/닌식/ㄋㄧㄋㄙㄧㄎ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space, quoted hsk_level, filled blank aliases (认识). Removed blank swadesh. In passing, fixed a missing "(stand-in for 識)" annotation and a malformed space-joined mandarin field on `characters/識.md`. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3305 — [[words/誓約|誓約]]
No cranberry (誓's own stand-in is [[盟誓]], 約's own stand-in is [[約束]]). Pronunciation fields (se'yag/서약/ㄙㄝ⼘ㄎ) already matched the straightforward concatenation — no bug (no null-onset dot needed before 約, consistent with the established precedent from [[公約]]/[[制約]]/[[条約]]). kwin true already correct (AND-rule). Fixed cantonese stray space; all other fields already correct and standard. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3306 — [[words/誕生|誕生]]
No cranberry (誕's own stand-in is this exact compound, 生's own stand-in is [[生活]]). Pronunciation fields (dansang/단상/ㄉㄚㄋㄙㄚㄫ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule); all other fields already correct and standard. Added missing aliases: []. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3307 — [[words/誘拐|誘拐]]
No cranberry (誘's own stand-in is [[誘発]], 拐's own stand-in is this exact compound). Pronunciation fields ('yuogwai/윳괘/⼜ㄛㄍ⺢ㄧ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Filled blank cantonese (jau5gwaai2) and vietnamese (dụ quải, compositional). Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3308 — [[words/誘発|誘発]]
No cranberry (誘's own stand-in is this exact compound, 発's own stand-in is [[発]] itself). Pronunciation fields ('yuofad/윳빧/⼜ㄛㄈㄚㄊ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Filled blank vietnamese (dụ phát, compositional). Fixed cantonese stray space. In passing, fixed a malformed comma-joined vietnamese field on `characters/発 (char).md`. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3309 — [[words/誘餌|誘餌]]
No cranberry (誘's own stand-in is [[誘発]], 餌's own stand-in is this exact compound). Pronunciation fields ('yuoni/윳니/⼜ㄛㄋㄧ) already matched the straightforward concatenation — no bug. **Added missing `kwin`** (false, AND-rule). Fixed cantonese stray space. Removed blank hsk_level/swadesh; other fields already thoroughly researched and documented. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3310 — [[words/語彙|語彙]]
No cranberry (語's own stand-in is [[言語]], 彙's own stand-in is [[彙]] itself). Pronunciation fields ('yohu/요후/⼄ㄏㄨ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). **Found and fixed two real bugs**: vietnamese held the literal empty string "" — corrected to ngữ vựng; aliases wrongly listed [[詞彙]] (a distinct separately-perfected word built on 詞, different reading) — corrected to genuine simplified 语汇, same false-alias pattern as [[言語]]'s earlier fix. Removed redundant duplicate 品詞. homophone_check.py found no independent homophones.

### 2026-09-06, iteration 3311 — [[words/語感|語感]]
No cranberry (語's own stand-in is [[言語]], 感's own stand-in is [[感触]]). Pronunciation fields ('yogam/요감/⼄ㄍㄚㄇ) already matched the straightforward concatenation — no bug. kwin false already correct (AND-rule). Fixed cantonese stray space. Removed blank hsk_level/swadesh. homophone_check.py found no independent homophones.

Next: 語族.

**[Milestone: 3,200th logged iteration.]**

**[Milestone: 3,170th logged iteration.]**
