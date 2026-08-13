# Character Perfecting (Solo Loop)

Running log for the character-perfecting backlog sweep (see [[AIOS/checklists/checklist_characters.md|Checklist: Character Pages]]). The prior logs (iterations 1–464 and 465–981) grew large and were archived to `Character Perfecting (Solo Loop).md.zip` and `Character Perfecting (Solo Loop) 2.md.zip` respectively; this file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one character per iteration. Find the next never-perfected character via `danayo_id` ascending (`grep -L "^date-last-perfect" characters/*.md`, sorted by each file's own `danayo_id` frontmatter value — not alphabetical, unlike the word sweep). Verify/fill all required frontmatter (`graphemic_classification`, `stand_in`, `mc_id`, `danayo_id`, `pos`, level fields), write or correct the four fixed `## Notes` bullets (graphemic → SKIP/Stroke → MC rank+phonology → levels), cross-check `## Words` against every real word citing this character as a constituent, add `## Chengyu`/`## Derived Characters` when real hits exist, then stamp `date-last-perfect`.

Next never-perfected character by `danayo_id`: 旨 (6131; 1523 characters remaining).

### 2026-08-08, iteration 982 — [[characters/旨|旨]]

`mc_id: 1800` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). Vietnamese `[chỉ]` confirmed complete. `aliases: [𠮛]` confirmed genuine (Wiktionary lists 𠮛 among 旨's ancient alternative forms, consistent with the ancient original glyph 𠤔). `stand_in: 主旨` confirmed genuine. Filled the empty `pos` field to `名詞`.

**Contested classification resolved, not just documented**: stored `graphemic_classification: 匕` implied Shuowen's 形聲 analysis (phonetic 匕 + semantic 甘 "delicious"). But Wiktionary lists 會意 (匕 "spoon" + originally 甘, "eating something delicious") as the *primary* modern analysis, and the OC evidence sides clearly with it: 匕's own reading is \*pilʔ/\*pijʔ (labial p-), which cannot plausibly be the phonetic source of 旨's \*kjiʔ (velar k-) — the same standard applied earlier this project to reject Shuowen folk etymologies on 貫/賓. Corrected `graphemic_classification` to the literal type-name `會意`. Also noted that the character's modern Kangxi radical 日 ("sun") is a coincidental later corruption of the original semantic component 甘 ("sweet, delicious") — the same "radical drifted, meaning didn't" pattern seen on 前/象 earlier in this project.

**`## Notes` had only two floating CC-lookup links and an informal "Components:" line** — rebuilt to the standard 4-bullet format incorporating the etymology dispute above. **`## Words` section already had all 4 genuine entries** (all four already perfected on their own pages) but the stand-in, [[主旨]], was missing its "(stand-in for 旨)" tag — added. **Chengyu**: one grep hit, [[造人像形]], confirmed a false positive (旨 appears only inside a quoted classical clause, not in its `characters:` field) — correctly excluded. **Derived Characters**: 4 genuine hits found (all confirmed citing 旨 as their own phonetic) — [[指]], [[脂]], [[稽]], [[詣 (char)|詣]] — added as a new section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 脊 (6132; 1522 characters remaining).

### 2026-08-08, iteration 983 — [[characters/脊|脊]]

**mc_id off-by-one fixed**: stored `2001` → actual rank in `CC 2000.md` is `2002`. 形声 classification confirmed via Wiktionary: originally a fish-spine pictogram, later given semantic [[肉 (char)|肉]] ("flesh") + phonetic [[朿]]; `graphemic_classification: 朿` already correct. Vietnamese `[tích]` confirmed complete. `stand_in: 脊椎` confirmed genuine (already perfected). Filled the empty `pos` field to `名詞`.

**Confirmed both `aliases` entries as legitimate 借代字, not bugs**: `瘠` and `鶺` are both etymologically distinct characters from 脊 (瘠 = 疒 + phonetic 脊, "thin, emaciated"; 鶺 = 鳥 + phonetic 脊, "wagtail," confirmed via Wiktionary) — same substitute-character pattern already established this project on [[斬 (char)|斬]]'s 塹 alias. The existing `### 借代字` subsection already documented 瘠's reasoning; extended it with the same treatment for 鶺 (not yet used in any vault word, but the phonetic relationship is confirmed).

**`## Notes` had only two floating CC-lookup links** — rebuilt to the standard 4-bullet format ahead of the existing 借代字 subsection. **`## Words` was missing its own stand-in entry** — added <ruby>[[脊椎]]<rt>ㄐㄝㄎㄑㄨㄧ</rt></ruby> (stand-in for 脊); [[肥脊]] was already correctly present. **Chengyu**: one grep hit, [[保頭断尾]], confirmed a false positive (脊 appears only in illustrative body prose about a *different* etymology, not in its `characters:` field); a similar false-positive hit on [[漏洩]] was likewise just a body-prose mention. **Derived Characters**: no hits (脊's only phonetic relationships are the 借代字 aliases above, a distinct category) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 脂 (6133; 1521 characters remaining).

### 2026-08-08, iteration 984 — [[characters/脂|脂]]

**mc_id off-by-one fixed**: stored `2378` → actual rank in `CC 2000.md` is `2379`. 形声 classification confirmed via Wiktionary: semantic [[Radical 074|月]] ("meat") + phonetic [[旨]]; `graphemic_classification: 旨` already correct. **Vietnamese cross-checked and confirmed complete despite a discrepancy between sources**: English Wiktionary's fetch added a third reading `mạnh`, but Vietnamese Wiktionary (the more authoritative source for this) lists only `chi`/`chỉ` — trusted the latter and left the stored `[chi, chỉ]` unchanged. `stand_in: 脂肪` confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` had a malformed structure** — the semantic/phonetic bullet existed but the SKIP/stroke/rank/levels bullets were entirely missing, and the two CC-lookup wikilinks were stranded after the `## Words` section instead of belonging to Notes. Rebuilt to the standard 4-bullet format. **`## Words` formatting fixed**: [[脂肪]] had no ruby/reading at all (just a bare link + dash-gloss) — reformatted with proper ruby and tagged as the stand-in; [[脂膏]] was already correctly formatted and confirmed to *not* need the stand-in tag (its own Notes say it's actually the stand-in for [[膏]], not for 脂). **Chengyu**: no hits. **Derived Characters**: no hits. A wide grep for "脂" also surfaced [[比]], [[水]], [[矢]], [[至]], [[鼻]], [[雖]], and [[石油]] — all confirmed false positives, where 脂 appears only as the name of the Middle Chinese rime class 脂A/脂B in phonological discussion, or in a historical quotation, never in an actual `characters:` field.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 岐 (6134; 1520 characters remaining).

### 2026-08-08, iteration 985 — [[characters/岐 (char)|岐]]

`mc_id: 982` confirmed correct (matches the traditional form 歧's actual rank in `CC 0000.md`, no off-by-one — 岐 is itself a simplified variant of 歧, so the CC corpus records the traditional spelling). 形声 classification confirmed via Wiktionary: semantic [[山]] ("mountain") + phonetic [[支 (char)|支]]; `graphemic_classification: 支` already correct. `aliases: [歧]` confirmed genuine (Wiktionary explicitly states 岐 is "the second-round simplified form of 歧"). Vietnamese `[kì]` confirmed complete. `stand_in: 岐` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format (using `HSK No` and `Jōyō - Kyōiku` for the empty `hsk_level` and grade-4 kyōiku `joyo_level`, per the conventions established on [[娯]] and [[滋]] respectively). **`## Words` section was entirely missing** — added <ruby>[[岐]]<rt>ㄍㄝ</rt></ruby> "fork (in road)" (stand-in for 岐). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 岐 as its own phonetic) — correctly has no section.

**Fixed corrupted data on the citing word page** [[岐]] (words/岐.md): `vietnamese: null` was a literal string placeholder — corrected to `kì`; also filled its empty `pos` field to `名詞`. Same recurring corruption pattern as several prior iterations.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 尿 (6136; 1519 characters remaining).

### 2026-08-08, iteration 986 — [[characters/尿 (char)|尿]]

`mc_id: 5597` confirmed as legitimate long-tail data (尿 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 會意 classification confirmed via Wiktionary: seal-script 尾 ("tail") + 水 ("water"), with 尾 later simplifying into the modern radical 尸; `graphemic_classification: 會意` already correct. Vietnamese `niệu` left unchanged — Vietnamese Wiktionary's own page for this character was an unhelpful stub, but `niệu` is a well-attested standard reading (e.g. 泌尿/tiết niệu, "urology"), so the existing value was trusted rather than second-guessed on a stub source. `stand_in: 尿` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[尿]]<rt>ㄋ⼘ㄨ</rt></ruby> "urine, urinate" (stand-in for 尿). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 尿 as its own phonetic) — correctly has no section.

**Fixed corrupted data on the citing word page** [[尿]] (words/尿.md): `vietnamese: null` was a literal string placeholder — corrected to `niệu`; also filled its empty `pos` field to `名詞`. Same recurring corruption pattern as several prior iterations.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 殴 (6137; 1518 characters remaining).

### 2026-08-08, iteration 987 — [[characters/殴|殴]]

`mc_id: 4677` confirmed as legitimate long-tail data (殴/毆 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[殳]] ("action, weapon") + phonetic [[区]]; `graphemic_classification: 区` already correct. `aliases: [毆]` confirmed genuine (traditional form). Vietnamese `[ẩu]` confirmed complete. `stand_in: 殴打` confirmed genuine.

**Malformed `japanese_native` YAML fixed**: the field was split across a scalar value (`なぐ`) followed by an orphaned list item (`- なぐる`) at the same indentation as `japanese`'s own list — invalid structure that also didn't match the vault's stem-okurigana convention (e.g. [[倒 (char)|倒]]'s `たお-れる`). Corrected to a proper single-item list: `japanese_native: [なぐ-る]`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[殴打]]<rt>ㄛㄨㄉㄚ</rt></ruby> "strike, batter" (stand-in for 殴). **Chengyu**: no hits. **Derived Characters**: an initial grep for characters citing `区` (殴's own phonetic donor) surfaced 8 hits ([[枢 (char)|枢]], [[駆 (char)|駆]], [[鴎 (char)|鴎]], [[䝙]], [[呕]], [[欧]], [[𧦅]]), but these are all phonetic-family *siblings* sharing the same donor 区 — not characters citing 殴 itself; the correct check (citations of 殴 specifically) returned zero hits, so no section was added, same sibling-vs-derived distinction as [[剤]] two iterations ago.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 砲 (6138; 1517 characters remaining).

### 2026-08-08, iteration 988 — [[characters/砲|砲]]

**mc_id sentinel-`0` resolved via variant form**: stored literal `0` looked like the standard "not found" placeholder, but 砲's own variant `炮` (石→火 semantic swap, same word — confirmed via Wiktionary as genuine alternative forms, matching the already-stored `aliases: [炮]`) has a real CC entry at rank `2719`; filled that in rather than leaving it as a sentinel, same logic as earlier variant-form mc_id fills this project (e.g. [[舶]]). 形声 classification confirmed via Wiktionary: semantic [[石 (char)|石]] ("stone") + phonetic [[包]]; `graphemic_classification: 包` already correct.

**Vietnamese contamination fixed**: stored `[bác, pháo]`; both English and Vietnamese Wiktionary confirm only `pháo` as a genuine reading for 砲 — `bác` isn't attested anywhere for this character (likely confusion with the unrelated native word or a different homophonous character) — removed. `stand_in: 大砲` confirmed genuine. Filled the empty `pos` field to `名詞` and the blank `boundedness` to `80`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, including the 石→火 semantic-swap story behind the 炮 variant. **`## Words` section was entirely missing** — added <ruby>[[大砲]]<rt>ㄉㄚㄧㄅ⼘ㄨ</rt></ruby> "cannon, gun" (stand-in for 砲); a grep hit on [[代表]] was a false positive (its own page cross-references 大砲 only as a homophone note, not in its `characters:` field). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 砲 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 昧 (6139; 1516 characters remaining).

### 2026-08-08, iteration 989 — [[characters/昧 (char)|昧]]

**mc_id off-by-one fixed**: stored `1534` → actual rank in `CC 1000.md` is `1535`. 形声 classification confirmed via Wiktionary: semantic [[日 (char)|日]] ("sun, day") + phonetic [[未 (char)|未]]; `graphemic_classification: 未` already correct. Vietnamese `[muội, mội]` confirmed complete. `stand_in: 昧` (self) confirmed genuine. Filled the empty `pos` field to `性詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` was missing its own stand-in entry** — added <ruby>[[昧]]<rt>ㄇㄚㄧ</rt></ruby> (stand-in for itself); [[曖昧]] was already correctly present. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 昧 as its own phonetic) — correctly has no section.

**Completed a homophone cross-reference left pending from an earlier iteration**: [[呆]]'s own page (grep hit while checking citing words) already lists 昧 and [[苺]] as homophones and explicitly notes "the reciprocal half of this callout will be completed on each when it comes up" — added the matching `>[!warning] Homophones` callout to [[昧]]'s own word page pointing back to 呆 and 苺 (苺 still pending its own turn). **Fixed corrupted data on the same citing word page**: `vietnamese: null` was a literal string placeholder — corrected to `muội`; also filled its empty `pos` field to `性詞`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 靴 (6140; 1515 characters remaining).

### 2026-08-08, iteration 990 — [[characters/靴|靴]]

`mc_id: 8825` confirmed as legitimate long-tail data (靴/鞾 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[Radical 177|革]] ("leather") + phonetic [[化 (char)|化]]; `graphemic_classification: 化` already correct. Vietnamese `[ngoa]` confirmed complete. `stand_in: 長靴` confirmed genuine. Filled the empty `pos` field to `名詞`.

**Fixed a malformed Notes bullet**: `- 形声, OC \*hʷa): semantic...` was missing its opening parenthesis (comma where `(OC` should have started) — rebuilt the whole `## Notes` section to the standard 4-bullet format, fixing this alongside adding the missing SKIP/stroke/rank/levels bullets. **`## Words` section already had the correct entry** but was missing its "(stand-in for 靴)" tag — added. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 靴 as its own phonetic) — correctly has no section. A grep hit on [[長]] was a false positive (靴 appears only as an example compound, 長靴, in illustrative body prose — not in its own `characters:` field).

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 爪 (6141; 1514 characters remaining).

### 2026-08-08, iteration 991 — [[characters/爪 (char)|爪]]

`mc_id: 1942` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 象形 classification confirmed via Wiktionary: a pictogram of a grabbing hand — despite the "claw" gloss, it actually depicts a human hand, not an animal's; `graphemic_classification: 象形` already correct. Vietnamese `[trảo, trảu, trẩu, vuốt]` confirmed complete (matches Wiktionary's set exactly, different order only). `stand_in: 爪` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` was missing its own stand-in entry** — added <ruby>[[爪]]<rt>ㄐ⺢ㄨ</rt></ruby> (stand-in for itself). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 爪 as its own phonetic) — correctly has no section. A grep hit on [[指甲]] was a false positive (爪 appears only as an illustrative Japanese-vocabulary aside in body prose, not in its `characters:` field).

**Fixed corrupted data on the citing word page** [[爪]] (words/爪.md): `vietnamese: null` was a literal string placeholder — corrected to `trảo` (the first-listed/primary Hán Việt reading, matching the pattern used for other characters with multiple stored candidates); also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 狭 (6142; 1513 characters remaining).

### 2026-08-08, iteration 992 — [[characters/狭|狭]]

`mc_id: 2187` confirmed correct (matches the traditional form 狹's actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[犬 (char)|犬]] ("dog") + phonetic [[夹]] ("to press between"); `graphemic_classification: 夹` already correct. **Vietnamese incomplete, fixed**: stored `[hiệp, hẹp]`; Wiktionary lists a third genuine reading `hệp` — added. **Japanese incomplete/misleading, fixed**: stored `japanese_native: さ` gave only a bound-root reading with no okurigana and omitted the actual common word for "narrow," せまい — added `せま-い` (matching the vault's stem-okurigana convention) alongside the existing `さ`.

**Investigated `stand_in: 名専字` and flagged rather than force-resolved**: this sentinel is documented in the checklist as "restricted to proper names, no standalone Dan'a'yo use," but 狭 is a common, productive adjective in every daughter language (せまい, 狭量, 偏狭), not remotely name-restricted — the same category of bug already fixed on [[峡]] earlier this project. Unlike 峡's case, though, no genuine unused compound is sitting around to repoint to: the only word citing 狭, [[狭窄]], explicitly documents itself in its own Notes as rescuing *窄*, not 狭. Left the sentinel in place (can't fabricate a word during character-page perfecting) but documented the discrepancy directly on the page as a flag for whoever eventually coins a proper stand-in word for 狭.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format plus the flag bullet above. **`## Words`**: [[狭窄]] was already correctly present, un-tagged (correctly, since it's not actually 狭's own stand-in). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 狭 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 曜 (6143; 1512 characters remaining).

### 2026-08-08, iteration 993 — [[characters/曜|曜]]

**mc_id off-by-one fixed**: stored `2876` → actual rank in `CC 2000.md` is `2877`. 形声 classification confirmed via Wiktionary: semantic [[日 (char)|日]] ("sun") + phonetic [[翟]]; `graphemic_classification: 翟` already correct. Vietnamese `[diệu]` confirmed complete — English Wiktionary added a Nôm "rọi," but Vietnamese Wiktionary (the more authoritative source) lists only `diệu`, so the addition was rejected. `stand_in: 曜日` confirmed genuine.

**`## Notes` had only two floating CC-lookup links** — rebuilt to the standard 4-bullet format (using `Jōyō - Kyōiku` for the grade-2 `joyo_level`, per the [[滋]]/[[岐]] convention). **`## Words` massively expanded**: only [[七曜]] was previously listed. A wide grep for "曜" surfaced 16 hits; 8 were false positives (曜 mentioned only in body prose about weekday etymology on [[日]], [[月]], [[木]], [[水]], [[火]], [[金]], [[土星]], [[棕枝主日]] — none in their own `characters:` fields). The remaining 8 are all genuine: added the missing stand-in [[曜日]] and all seven day-of-week compounds — [[日曜日]], [[月曜日]], [[火曜日]], [[水曜日]], [[木曜日]], [[金曜日]], [[土曜日]] — each already perfected on its own page, so readings were pulled directly from their own `注音` fields. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 曜 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 券 (6144; 1511 characters remaining).

### 2026-08-08, iteration 994 — [[characters/券 (char)|券]]

`mc_id: 3332` confirmed correct (matches actual rank in `CC 3000.md`, no off-by-one). Vietnamese `[khoán]` confirmed complete. `stand_in: 券` (self) confirmed genuine.

**Sibling-vs-true-phonetic bug found and fixed**: stored `graphemic_classification: 巻` cited the shinjitai of 卷 ("scroll") as the phonetic donor. But Wiktionary's actual etymology for 券 names the phonetic as 𠔉 (a rare, pageless component also behind 卷's own compound: 卷 = phonetic 龹/𠔉 + semantic 卩) — meaning 巻/卷 is a phonetic-family *sibling* of 券, not its direct donor, the same distinction already established this project on [[踪]] (宗 vs 從) and [[剤]]/[[殴]] (siblings of 斉/区). The already-perfected citing word [[券]] itself corroborates this, describing 券 as merely "related to 巻" rather than derived from it. Corrected `graphemic_classification` to the bare, pageless `𠔉`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, explaining the 𠔉/巻 sibling relationship. **`## Words` section was entirely missing** — added <ruby>[[券]]<rt>ㄎㄛㄋ</rt></ruby> (stand-in for itself) and <ruby>[[証券]]<rt>ㄐㄧㄫㄎㄛㄋ</rt></ruby> "security"; a grep hit on [[割引]] was a false positive (券 appears only inside the illustrative compound 割引券 in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 券 as its own phonetic) — correctly has no section. Filled the empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 枚 (6145; 1510 characters remaining).

### 2026-08-08, iteration 995 — [[characters/枚 (char)|枚]]

`mc_id: 1449` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). Vietnamese `[mai]` confirmed complete — Wiktionary's Hán Việt entry matches exactly; its accompanying Nôm list (may, môi, moi, muồi, mồi, mui, mòi, muôi, mái, mói) is the noisy, undifferentiated kind this project has repeatedly declined to import wholesale, so it was left out. `stand_in: 枚` (self) confirmed genuine, `pos: 量詞` already correct.

**Contested classification investigated and left as documented alternative, not force-resolved**: Wiktionary lists 枚 under both 會意 (木 "wood" + 攵 "hand with stick") and a competing 形聲 analysis (Zhengzhang: phonetic 文, OC \*mɯn — a close match to 枚's own \*mɯːl — later visually corrupted into 攵). Unlike the clear-cut [[旨]] case (where OC evidence flatly ruled out the minority reading) or the sibling-donor mixups on [[踪]]/[[券]], this is a genuine two-sided scholarly split with real phonetic plausibility on both readings — and the already-perfected citing word [[枚]] independently committed to the 會意 prose. Kept `graphemic_classification: 會意` and documented the 形聲/文 alternative in the Notes instead, following the same standard set on [[匠]] earlier this project.

**`## Notes` had only a components list and two floating CC-lookup links** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[枚]]<rt>ㄇㄛㄧ</rt></ruby> (stand-in for itself). **Chengyu**: one grep hit, [[天真乱漫]], confirmed a false positive (references 袁枚, a historical person's name, not the character itself). **Derived Characters**: no hits. Three more grep hits — [[毎]], [[煤]], [[杯]] — were also false positives, mentioning 枚 only in already-reciprocal homophone callouts or phonological comparison prose, not as citations.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 筋 (6146; 1509 characters remaining).

### 2026-08-08, iteration 996 — [[characters/筋|筋]]

`mc_id: 1369` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 會意 classification confirmed via Wiktionary: [[竹 (char)|竹]] ("bamboo") + 𠛧 ("peel") — sinew likened to peeled bamboo's stringy texture, with the modern 力 bottom component a corruption of 刀; `graphemic_classification: 會意` already correct. Vietnamese `[cân, gân]` confirmed complete. `stand_in: 筋肉` confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[筋肉]]<rt>ㄍㄧㄋㄋㄨㄎ</rt></ruby> "muscles" (stand-in for 筋); a grep hit on [[肉]] was a false positive (筋 appears only inside the illustrative compound 筋肉/kinniku in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 筋 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-08`.

Next never-perfected character by `danayo_id`: 矮 (6147; 1508 characters remaining).

### 2026-08-09, iteration 997 — [[characters/矮 (char)|矮]]

This page was already largely built (`mc_id: 9899` confirmed as legitimate long-tail data, not found anywhere in `CC 0000`–`CC 3000`; 形声 classification — semantic [[Radical 111|矢]] "arrow" + phonetic [[委]] — already correct and already documented; `stand_in: 矮` self-reference already correct).

**Vietnamese contamination fixed**: stored `[nuỵ, oải, ải]`; both English and (attempted) Vietnamese Wiktionary confirm only `ải` as a genuine reading — corroborated independently by the citing word [[矮行星]]'s own attested `vietnamese: ải hành tinh`. Trimmed to just `ải`. Filled the empty `pos` field to `性詞`.

**`## Words` was missing its own stand-in entry** — added <ruby>[[矮]]<rt>⺢ㄧ</rt></ruby> "short (person)" (stand-in for 矮); [[矮行星]] was already correctly present. Also fixed a stray relative-path link (`../lookup/Korean/...`) in the existing levels bullet to match the file's other absolute-style links. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 矮 as its own phonetic) — correctly has no section. A grep hit on [[小行星帯]] was a false positive (矮 appears only inside the illustrative compound 矮行星 in body prose).

**Filled blank fields on the citing word page** [[矮]] (words/矮.md): `vietnamese:` was blank (not the usual `null`-string corruption, just genuinely unfilled) — filled with `ải`; also filled the empty `pos` field to `性詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 辦 (6148; 1507 characters remaining).

### 2026-08-09, iteration 998 — [[characters/辦|辦]]

`mc_id: 3567` confirmed correct (matches actual rank in `CC 3000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[力 (char)|力]] ("strength") + phonetic 辡 (no vault page); `graphemic_classification: 辡` already correct. **Vietnamese incomplete, fixed**: stored `[biện]` only; Wiktionary clearly distinguishes and labels a second genuine reading, Nôm `bạn` — added (unlike the usual undifferentiated noisy Nôm lists this project has declined to import, this one was specifically singled out and labeled, so trusted). `stand_in: 辦理` confirmed genuine. Filled the empty `pos` field to `事詞`.

**`## Notes` was a malformed mix** — two bare CC-lookup links followed by two un-ruby'd Words-style bullets, with no SKIP/stroke/rank/levels content at all. Rebuilt cleanly: standard 4-bullet Notes, then a proper `## Words` section with all three genuine citing words (verified via grep) — <ruby>[[辦理]]</ruby> (stand-in), <ruby>[[辦公室]]</ruby> "office", <ruby>[[辦公]]</ruby> "do business, handle business". **Chengyu**: one grep hit, [[東奔西走]], confirmed a false positive (辦 appears only inside a quoted example sentence in body prose). **Derived Characters**: no hits (nothing cites 辦 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 鞋 (6149; 1506 characters remaining).

### 2026-08-09, iteration 999 — [[characters/鞋 (char)|鞋]]

`mc_id: 0` confirmed genuine (鞋 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[Radical 177|革]] ("leather") + phonetic [[圭]]; `graphemic_classification: 圭` already correct. Vietnamese `[giày, hài]` confirmed complete. `stand_in: 鞋` (self) confirmed genuine; the citing word [[鞋]] was already fully perfected with no bugs found.

**Deduplicated a near-identical repeated Notes bullet**: the same 形声 etymology sentence appeared twice back-to-back, with the second copy additionally malformed (stray leading space, missing opening parenthesis, curly quotes instead of straight). Merged into one clean bullet and completed the standard 4-bullet format (SKIP/stroke/rank/levels bullets were entirely missing). **`## Words` section was entirely missing** — added <ruby>[[鞋]]<rt>ㄏ⼘ㄧ</rt></ruby> "shoe" (stand-in for 鞋); no other word cites 鞋 (two grep hits, [[双]] and [[水晶]], were false positives — 鞋 appears only in illustrative example compounds, 一双鞋 and 水晶鞋, in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 鞋 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 嗚 (6150; 1505 characters remaining).

### 2026-08-09, iteration 1000 — [[characters/嗚|嗚]]

`mc_id: 1840` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[口 (char)|口]] ("mouth") + phonetic [[烏]] (an onomatopoeia for sobbing); `graphemic_classification: 烏` already correct. **Vietnamese contamination fixed**: stored 7-reading list `[o, u, ô, ú, ọ, ỏ, ố]`; Wiktionary confirms only 6 of these (`ô, o, ọ, ỏ, u, ú`) — `ố` is not attested anywhere for this character and was removed. `stand_in: 嗚咽` confirmed genuine (already perfected). Filled the empty `pos` field to `感詞` (interjection/exclamation class, fitting an onomatopoeic sobbing sound).

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[嗚咽]]<rt>ㄛㄝㄋ</rt></ruby> "sob, whimper" (stand-in for 嗚), the only word citing this character. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 嗚 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 姦 (6151; 1504 characters remaining).

### 2026-08-09, iteration 1001 — [[characters/姦|姦]]

`mc_id: 648` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 會意 classification confirmed via Wiktionary: triplication of [[女 (char)|女]] ("woman"); `graphemic_classification: 會意` already correct. Vietnamese `[gian]` confirmed complete via Vietnamese Wiktionary (English Wiktionary's fetch was truncated before reaching the Vietnamese section). `stand_in: 姦淫` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` had only two floating CC-lookup links plus one informal bullet** — rebuilt to the standard 4-bullet format, using `Korean HS` rather than a `Korean Name` link since `hanmun_edu_level: 高等` maps to the high-school Korean-education lookup category (per the convention already established on [[丸]]), not the given-name category used for `hanmun_edu_level: 名` characters. **`## Words` section formalized**: converted the informal bullet into a proper ruby entry, tagged as the stand-in. **`## Chengyu` section was entirely missing**: found one genuine hit, [[殺姦窃偽]] ("murder, adultery, theft, lying") — added; [[Biblical Chengyu]] was a false positive (it's an index/list page, not an actual chengyu entry with its own `characters:` field), and [[出谷記]] was also a false positive (quotes the phrase in body text only). **Derived Characters**: no hits (nothing cites 姦 as its own phonetic — it's 會意, not 形聲) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 屢 (6152; 1503 characters remaining).

### 2026-08-09, iteration 1002 — [[characters/屢 (char)|屢]]

`mc_id: 2131` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 044|尸]] ("body") + phonetic [[婁]]; `graphemic_classification: 婁` already correct. Vietnamese `[cũ, luã, lú, lũ, rũ, rủ]` confirmed complete (matches Wiktionary's set exactly). `stand_in: 屢` (self) confirmed genuine. Filled the empty `pos` field to `副詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[屢]]<rt>ㄌㄨ</rt></ruby> (stand-in for itself), the only genuine citing word (a grep hit on [[朽木糞牆]] was a false positive, quoting 屢 only in an illustrative example sentence). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 屢 as its own phonetic) — correctly has no section.

**Fixed corrupted/inconsistent data on the citing word page** [[屢]] (words/屢.md): `vietnamese: null` was a literal string placeholder — corrected to `lũ`; also filled its empty `pos` field to `副詞`. Separately, `korean: "누"` didn't match the character's own `korean: "루"` (a real onset mismatch, ㄴ vs ㄹ, contradicting the character's own `kwin: true` claim that Dan'a'yo exactly matches Sino-Korean) — corrected to `루`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 桜 (6153; 1502 characters remaining).

### 2026-08-09, iteration 1003 — [[characters/桜 (char)|桜]]

`mc_id: 5888` confirmed as legitimate long-tail data (桜/櫻 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[木 (char)|木]] ("tree") + phonetic [[嬰]]; `graphemic_classification: 嬰` already correct. Vietnamese `[anh]` confirmed complete. `stand_in: 桜` (self) confirmed genuine, `pos: 名詞` already correct. Filled the blank `boundedness` to `90`.

**Malformed `japanese_native` YAML fixed**: same corruption pattern as [[殴]] a few iterations ago — the field was split across a scalar value (`さくら`) and an orphaned duplicate list item (`- さくら`) at the same indentation as `japanese`'s own list. Corrected to a proper single-item list.

**`## Notes` had only two floating CC-lookup links plus one informal bullet** — rebuilt to the standard 4-bullet format. **`## Words` was missing its own stand-in entry** — added <ruby>[[桜]]<rt>ㄚㄫ</rt></ruby> (stand-in for itself); [[桜桃]] was already correctly present, formalized into a proper ruby entry. **Chengyu**: one grep hit, [[落花流水]], confirmed a false positive (桜 appears only in illustrative aesthetic-imagery prose). **Derived Characters**: no hits (nothing cites 桜 as its own phonetic) — correctly has no section. A grep hit on [[造幣局]] was also a false positive (body prose about a cherry-blossom path at the Japan Mint).

**Fixed corrupted data on the citing word page** [[桜]] (words/桜.md): both `vietnamese: null` and `korean: "null"` were literal string placeholders — corrected to `anh` and `앵` respectively; also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 嫌 (6154; 1501 characters remaining).

### 2026-08-09, iteration 1004 — [[characters/嫌|嫌]]

**mc_id off-by-one fixed**: stored `2122` → actual rank in `CC 2000.md` is `2123`. 形声 classification confirmed via Wiktionary: semantic [[女 (char)|女]] ("woman") + phonetic [[兼 (char)|兼]]; `graphemic_classification: 兼` already correct. **Vietnamese contamination fixed**: stored `[hem, hiềm, hèm, hềm]`; Wiktionary confirms only the first three — `hềm` isn't attested and was removed. `stand_in: 嫌悪` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**Investigated `aliases: [厭, 魘, 魇]` and confirmed all three legitimate 借代字**, same substitute-character pattern as [[斬 (char)|斬]]/塹 and [[脊]]/瘠,鶺: [[倦厭]]'s own Notes already document 嫌 standing in for 厭 (sharing the syllable ㄏㄝㄇ, with the real-world readings following 厭's own values); [[夢嫌]]'s own Notes likewise document 嫌 standing in for 魘/魇 ("nightmare incubus"). Built a new `### 借代字` subsection on 嫌's own page (this vault's usual place for documenting the relationship, per the precedent set on [[脊]]) summarizing both, since it had none before despite two citing words already relying on it.

**`## Notes` was a single malformed one-line bullet** (both CC-lookup links crammed onto one line with no SKIP/stroke/rank/levels content) — rebuilt to the standard 4-bullet format. **`## Words`**: all three genuine entries were already present; added the missing "(stand-in for 嫌)" tag to [[嫌悪]]. **Chengyu**: one grep hit, [[李下瓜田]], confirmed a false positive (嫌 appears only in body prose about a related classical concept, 避嫌). **Derived Characters**: no hits (nothing cites 嫌 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 餅 (6155; 1500 characters remaining).

### 2026-08-09, iteration 1005 — [[characters/餅 (char)|餅]]

**mc_id off-by-one fixed**: stored `3919` → actual rank in `CC 3000.md` is `3920`. 形声 classification confirmed via Wiktionary: semantic [[食 (char)|食]] ("food") + phonetic 並/并 (OC \*peŋ, matching 餅's own \*peŋʔ almost exactly); `graphemic_classification: 并` already correct, linked to the vault's [[並 (char)|并]] page (并 has no page of its own, matching the 従/從-style convention of citing the more standard glyph while linking to whichever page actually exists). Vietnamese `[bánh, bính]` confirmed complete via Vietnamese Wiktionary (English Wiktionary's fetch claimed no readings at all — an incomplete summary, not a real gap). `stand_in: 餅` (self) confirmed genuine.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, using `Korean Missing` for `hanmun_edu_level: 無` (per the convention on [[冉]]). **`## Words` section was entirely missing** — added <ruby>[[餅]]<rt>ㄅㄧㄫ</rt></ruby> (stand-in for itself); three grep hits ([[柏]], [[麺包]], [[中秋節]]) were all false positives, mentioning 餅 only in illustrative compounds (柏餅, 月餅) or a cross-reference aside in body prose, never in a `characters:` field. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 餅 as its own phonetic) — correctly has no section.

**Fixed corrupted data on the citing word page** [[餅]] (words/餅.md): both `vietnamese: null` and `korean: "null"` were literal string placeholders — corrected to `bánh` and `병` respectively; also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 型 (6156; 1499 characters remaining).

### 2026-08-09, iteration 1006 — [[characters/型|型]]

`mc_id: 6698` confirmed as legitimate long-tail data (型 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[土 (char)|土]] ("earth") + phonetic [[刑]] — literally "an earthen mold"; `graphemic_classification: 刑` already correct. Vietnamese `[hình]` confirmed complete. `stand_in: 型式` confirmed genuine (already perfected). Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[型式]] was already correctly present, missing only its "(stand-in for 型)" tag — added. **Chengyu**: one grep hit, [[舎本逐末]], confirmed a false positive (型 appears only inside 典型 in an illustrative example sentence). **Derived Characters**: no hits (nothing cites 型 as its own phonetic) — correctly has no section. Two more grep hits, [[普及]] and [[血液]], were also false positives (型 appears only in illustrative compounds — 普及型, 血液型 — in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 勺 (6157; 1498 characters remaining).

### 2026-08-09, iteration 1007 — [[characters/勺 (char)|勺]]

`mc_id: 2644` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one).

**Classification bug found and fixed**: stored `graphemic_classification: 象形` — Wiktionary's exact glyph-origin text instead names this 指事 (ideogram): "wine (丶) in a ladle (勹)," a two-part indicative construction rather than a single pictographic depiction. Corrected to `指事`. (Note: the already-perfected citing word [[勺]] also asserts "象形" in its own body prose — flagged here but not rewritten, since fixing already-perfected word-page prose is outside character-page-perfecting scope.)

**Vietnamese contamination fixed**: stored `[chước, duộc, giuộc, thược]`; the citing word [[勺]]'s own Notes already researched and explicitly flagged three of these as "unrelated... corpus noise," keeping only `chước` as the genuine Hán Việt reading — trimmed the character page to match, trusting that specific research over an unconfirmed broader list (same precedent as [[偵]]/[[梗]]/[[堪]]/[[呈]] earlier this project). Also fixed a typo in the `english` field: `laddle` → `ladle`. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format (using `Jinmeiyō` for the `joyo_level: 日本人名用漢字` category). **`## Words`**: [[叉勺]] was already present; added the missing self-reference stand-in entry, <ruby>[[勺]]<rt>ㄐ⺢ㄎ</rt></ruby>. **`## Derived Characters` was entirely missing**: 6 genuine hits found (all confirmed citing 勺 as their own phonetic) — [[的]], [[豹]], [[約]], [[釣]], [[酌]], [[灼]] — added as a new section. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 暦 (6158; 1497 characters remaining).

### 2026-08-09, iteration 1008 — [[characters/暦 (char)|暦]]

`mc_id: 1522` confirmed correct (matches the traditional form 曆's actual rank in `CC 1000.md`, no off-by-one). Vietnamese `[lịch]` confirmed complete (Wiktionary's accompanying Nôm list — rếch, rích, rịch — was left out as the usual undifferentiated noise). `stand_in: 暦` (self) confirmed genuine. Filled the blank `boundedness` to `90`.

**Investigated `graphemic_classification: 秝` and confirmed NOT a bug**: Wiktionary's actual etymology names the phonetic as 厤 (itself built from 秝), which at first looked like the same sibling-vs-donor mixup fixed on [[踪]]/[[券]]/[[殴]]/[[剤]] — but critically, 秝 and 厤 share the *exact same* Old Chinese reading (\*reːɡ), and 秝 is a direct ancestor of 厤 rather than a phonetically-divergent cousin. Citing the ultimate root carries zero phonetic loss here, unlike those earlier cases, so left unchanged and documented the two-step derivation in the Notes.

**`## Notes` had only two floating CC-lookup links plus one informal bullet** — rebuilt to the standard 4-bullet format. **`## Words` massively expanded**: only the informal [[暦数]] mention existed. Added the missing self-reference stand-in and four more genuine citing words found via grep — [[太陽暦]], [[太陰暦]], [[太陰太陽暦]], [[陰暦年]]. **Flagged, not resolved**: [[太陰曆]] appears to be a near-exact duplicate of [[太陰暦]] (identical reading and gloss, "lunar calendar," differing only in shinjitai vs traditional headword) — left out of the Words list as likely redundant, but not merged/deleted since consolidating word pages is outside character-page-perfecting scope. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 暦/秝 as its own phonetic) — correctly has no section.

**Filled a blank field on the citing word page** [[暦]] (words/暦.md): empty `pos` → `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 契 (6159; 1496 characters remaining).

### 2026-08-09, iteration 1009 — [[characters/契|契]]

**mc_id off-by-one fixed**: stored `1778` → actual rank in `CC 1000.md` is `1779`. 形声/會意 classification confirmed via Wiktionary: phonetic 㓞 ("to engrave," no vault page) + semantic [[大 (char)|大]] ("person"); `graphemic_classification: 㓞` already correct.

**Vietnamese contamination fixed, including a literal duplicate**: stored a 9-item list `[khế, khè, khé, khía, khít, khẻ, khẽ, khế, khịt]` with `khế` appearing twice. The citing word [[契机]]'s own Notes already documented that `khế` was deliberately added as the character's "most common Sino-Vietnamese reading" (via 契約/khế ước) — but the other 7 entries (khè, khé, khía, khít, khẻ, khẽ, khịt) are uncorroborated by any source checked and read as native-word noise. Trimmed to just `khế`.

**`## Notes` had only two floating CC-lookup links plus three informal Words-style bullets** — rebuilt cleanly: standard 4-bullet Notes, then a proper `## Words` section with the stand-in [[契約]] (tagged) plus [[書契]] and [[契机]], both already perfected. **`## Derived Characters` was entirely missing**: 3 genuine hits found (all confirmed citing 契 as their own phonetic) — [[偰]], [[喫 (char)|喫]], [[楔]] — added as a new section. **Chengyu**: one grep hit, [[白頭偕老]], confirmed a false positive (契 appears only inside a quoted classical poem, 死生契闊). Two more grep hits, [[書法]] and [[楔子]], were also false positives (mentioning 契 only via the already-confirmed 書契 or in etymology prose about [[楔]] itself).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 暇 (6160; 1495 characters remaining).

### 2026-08-09, iteration 1010 — [[characters/暇|暇]]

`mc_id: 2017` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[日 (char)|日]] ("sun") + phonetic [[叚]]; `graphemic_classification: 叚` already correct. **Vietnamese incomplete, fixed**: stored `[há, hạ, hả]`; Wiktionary's full list has 7 minor tonal/vowel variants of the same syllable (hạ, hả, há, hã, he, hẻ, hẽ) with no indication any are noise or unrelated — added the missing four. `stand_in: 閑暇` and its `#cranberry` tag left unchanged (pre-existing, not re-litigated without cause). Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[閑暇]]<rt>ㄏㄚㄋㄏㄚ</rt></ruby> "freetime, leisure" (stand-in for 暇, `#cranberry`) and <ruby>[[休暇]]<rt>ㄏ⼜ㄏㄚ</rt></ruby> "vacation"; a grep hit on [[寸]] was a false positive (暇 appears only inside the illustrative idiom 寸暇 in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 暇 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 冥 (6161; 1494 characters remaining).

### 2026-08-09, iteration 1011 — [[characters/冥 (char)|冥]]

`mc_id: 1191` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 會意 classification confirmed via Wiktionary: [[Radical 014|冖]] ("cloth cover") over 日 ("sun") + 廾 ("two hands," later corrupted to 六); `graphemic_classification: 會意` already correct. **Vietnamese contamination fixed**: stored `[minh, mênh, mưng]`; the citing word [[冥]]'s own Notes had already researched and explicitly flagged `mênh` and `mưng` as "unrelated... corpus noise," confirming only `minh` as genuine — trimmed to just `minh`, same precedent as [[偵]]/[[勺]]/[[呈]] earlier this project. `stand_in: 冥` (self) confirmed genuine. Filled the empty `pos` field to `性詞`.

**Investigated `aliases: [溟, 暝, 瞑, 慏]` and confirmed all four legitimate phonetic derivatives**: unlike [[嫌]]'s aliases (already actively used by real citing words), none of these four are cited by any vault word yet — but each is independently confirmed via Wiktionary as a genuine 冥-phonetic compound sharing the identical Old Chinese reading \*meːŋ (溟 "dark sea," 瞑 "close eyes," 慏 unglossed; 暝 "night," explicitly called "a variant form of 冥" by Wiktionary itself). Noted this in the Notes rather than building a full `### 借代字` subsection, since that format is reserved for aliases already in active use by real compounds.

**`## Notes` had only two floating CC-lookup links** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing self-reference stand-in entry; [[冥王]] and [[冥金]] were already correctly present. **`## Derived Characters` was entirely missing**: one genuine hit, [[螟]] (confirmed citing 冥 as its own phonetic) — added. **Chengyu**: no hits. Two grep hits, [[北海]] and [[黒金]], were false positives (冥 appears only in illustrative classical quotations/etymology asides in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 豚 (6162; 1493 characters remaining).

### 2026-08-09, iteration 1012 — [[characters/豚 (char)|豚]]

`mc_id: 2201` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). 會意 classification confirmed via Wiktionary: [[肉 (char)|肉]] ("meat") + [[豕 (char)|豕]] ("pig"); `graphemic_classification: 會意` already correct. Vietnamese `[đồn]` confirmed complete — the citing word [[豚]]'s own Notes already researched this exact reading ("đồn (also độn)... specifically denoting a piglet"), resolving an initial Wiktionary-fetch ambiguity between đồn/độn. `stand_in: 豚` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**Deduplicated a jumbled `## Words`/`## Notes` split**: the file had a premature `## Words` section (with just one entry) sitting *before* a `# Notes` heading that itself had one more informal Words-style bullet buried inside it. Merged and rebuilt cleanly: standard 4-bullet Notes, then a single proper `## Words` section with all four genuine citing words (verified via grep) — the stand-in [[豚]], [[豚肉]] "pork", [[豚井]] "butadon", and [[海豚]] "dolphin". A grep hit on [[肉]] was a false positive (豚 appears only inside the illustrative compound 豚肉 in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 豚 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 銃 (6163; 1492 characters remaining).

### 2026-08-09, iteration 1013 — [[characters/銃 (char)|銃]]

`mc_id: 0` confirmed genuine (銃 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[金 (char)|金]] ("metal") + phonetic [[充]]; `graphemic_classification: 充` already correct. Vietnamese `[súng, xúng]` confirmed complete. `stand_in: 銃` (self) confirmed genuine. `korean_native: "총"` being identical to the Sino-Korean `korean` field looked suspicious at first, but left unchanged — Korean has no distinct native word for "gun" (a relatively late technology), so the fully-naturalized Sino-Korean term filling both roles is plausible, not a bug. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[銃]]<rt>ㄑㄨㄫ</rt></ruby> (stand-in for itself), the only word citing this character (no grep hits at all for Chengyu, Derived Characters, or any other citing word).

**Fixed corrupted data on the citing word page** [[銃]] (words/銃.md): `vietnamese: null` was a literal string placeholder — corrected to `súng` (the primary reading); also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 殉 (6164; 1491 characters remaining).

### 2026-08-09, iteration 1014 — [[characters/殉|殉]]

**mc_id off-by-one fixed**: stored `2974` → actual rank in `CC 2000.md` is `2975`. 形声 classification confirmed via Wiktionary: semantic [[歹]] ("death") + phonetic [[旬]]; `graphemic_classification: 旬` already correct. Vietnamese `[tuẫn]` confirmed complete. `stand_in: 殉難` confirmed genuine (already perfected, correctly documented as standing in for both 殉 and 難). Filled the empty `pos` field to `事詞`.

**`## Notes`/`## Words` were jumbled together** (an empty Notes heading, then a Words section, then two stranded CC-lookup links after it) — rebuilt cleanly: standard 4-bullet Notes, then a proper `## Words` section with the stand-in tagged. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 殉 as its own phonetic) — correctly has no section. A grep hit on [[受難]] was a false positive (殉 appears only inside the illustrative compound 殉難 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 濯 (6165; 1490 characters remaining).

### 2026-08-09, iteration 1015 — [[characters/濯|濯]]

**mc_id off-by-one fixed**: stored `2390` → actual rank in `CC 2000.md` is `2391`. 形声 classification confirmed via Wiktionary: semantic [[水 (char)|水]] ("water") + phonetic [[翟]]; `graphemic_classification: 翟` already correct. **Vietnamese contamination fixed**: stored `[dập, trạc]`; Wiktionary confirms only `trạc` as a genuine Hán Nôm reading for 濯 — `dập` (a common native Vietnamese word, "to crush/press/stamp") isn't attested anywhere and was removed. `stand_in: 洗濯` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[洗濯]]<rt>ㄙㄝㄋㄉㄚㄎ</rt></ruby> "launder, rinse, wash" (stand-in for 濯). **Chengyu**: one grep hit, [[焚琴煮鶴]], confirmed a false positive (濯 appears only inside a quoted classical passage). **Derived Characters**: no hits (nothing cites 濯 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 鈍 (6166; 1489 characters remaining).

### 2026-08-09, iteration 1016 — [[characters/鈍|鈍]]

**mc_id off-by-one fixed**: stored `3557` → actual rank in `CC 3000.md` is `3558`. 形声 classification confirmed via Wiktionary: semantic [[金 (char)|金]] ("metal") + phonetic [[屯 (char)|屯]]; `graphemic_classification: 屯` already correct.

**Vietnamese contamination fixed**: stored `[nhọn, nhụt, độn]` — `nhọn` means "sharp, pointed," the literal *antonym* of 鈍 ("dull, blunt"), an unmistakable data error; removed. Kept `nhụt` and `độn` (both semantically consistent with dullness — `độn` corroborated via the common expression 愚鈍/ngu độn, "stupid, dull-witted").

**Confirmed the same `名専字` discrepancy already flagged on [[狭]]**: `stand_in: 名専字` claims 鈍 is restricted to proper names, but it's a common, productive adjective (鈍感, 遅鈍, 鈍器, 鈍痛) in every daughter language. Unlike [[峡]]'s case, no existing vault word cites 鈍 at all (the sole grep hit, [[凶器]], mentions 鈍器 only in body prose) — so there's no compound to repoint to. Documented the discrepancy on the page rather than fabricating a word.

**`## Notes` had only two floating CC-lookup links plus an informal Components line** — rebuilt to the standard 4-bullet format plus the flag bullet above. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 郭 (6167; 1488 characters remaining).

### 2026-08-09, iteration 1017 — [[characters/郭 (char)|郭]]

`mc_id: 821` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 會意 classification confirmed via Wiktionary: "tall building" + [[邑]] ("city"); `graphemic_classification: 會意` already correct. `aliases: [廓]` confirmed genuine 借代字 (already actively used by [[郭清]] and [[輪郭]], both of which explicitly document 郭 standing in for 廓). **Vietnamese incomplete, fixed**: stored `[quách]` only; Wiktionary's clearly-differentiated Hán Việt/Nôm split adds a second genuine reading, `quắt` — added. `stand_in: 郭` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**Fixed a malformed relative-path link** in the CC-finals lookup (`../lookup/CC/finals/韻 鈬合` → `lookup/CC/finals/韻 鈬合`, matching the file's other absolute-style links) while rebuilding `## Notes`/`## Words` from a jumbled, wrongly-ordered stub into the standard structure. **`## Words` expanded**: added the missing self-reference stand-in and [[城郭]] (a genuine hit missed before); [[郭清]] and [[輪郭]] were already present. **`## Derived Characters` was entirely missing**: one genuine hit, [[漷]] (confirmed citing 郭 as its own phonetic) — added. **Chengyu**: three grep hits ([[万物生長]], [[天衣無縫]], [[李下瓜田]]) all confirmed false positives (郭 appears only as part of historical/legendary personal names — 郭老, 郭翰, 郭茂倩 — never in a `characters:` field). Two more grep hits, [[城市]] and [[城郭]]'s own reciprocal mention, were likewise resolved correctly (城市 references 城郭 only in prose about a different character's stand_in).

**Fixed corrupted data on the citing word page** [[郭]] (words/郭.md): `vietnamese: null` was a literal string placeholder — corrected to `quách`; also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 賜 (6168; 1487 characters remaining).

### 2026-08-09, iteration 1018 — [[characters/賜|賜]]

`mc_id: 307` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[貝]] ("shell, money") + phonetic [[易 (char)|易]]; `graphemic_classification: 易` already correct. Vietnamese `[tứ]` confirmed complete. `stand_in: 賜予` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[賜予]] was already present but missing ruby formatting — reformatted to `<ruby>...<rt>ㄙㄝ⼄</rt></ruby>`. **`## Chengyu` section was entirely missing**: found one genuine hit, [[孝親天賜]] ("Honor your parents, that heaven may gift you") — added; [[創反救成]] and [[論功行賞]] were false positives (賜 appears only in quoted Biblical/classical text). **Derived Characters**: no hits (nothing cites 賜 as its own phonetic) — correctly has no section. Two more grep hits, [[予習]] and [[出谷記]], were also false positives (mentioning 賜予 or 孝親天賜 only as asides in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 廷 (6169; 1486 characters remaining).

### 2026-08-09, iteration 1019 — [[characters/廷|廷]]

**Resolved the self-referential `graphemic_classification` bug flagged during the [[呈]] iteration**: stored `graphemic_classification: 廷` was nonsensically self-pointing. Wiktionary confirms the true phonetic is 𡈼 (semantic [[Radical 054|廴]] "to move forward" + phonetic 𡈼, no vault page) — the same true donor already correctly cited on [[呈]]'s own page. Corrected, and noted on the page that this is distinct from 呈's own relationship to 𡈼 despite the visual similarity between 廷 and 呈. `mc_id: 710` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). Vietnamese `[đình]` confirmed complete. `stand_in: 朝廷` confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` expanded**: [[朝廷]] was already present (tagged as stand-in); added the missing [[宮廷]] "royal court, palace" (already perfected, genuinely citing 廷). **`## Derived Characters` was entirely missing**: 3 genuine hits found (all confirmed citing 廷 as their own phonetic, independent of 廷's own now-corrected donor) — [[庭]], [[挺]], [[艇 (char)|艇]] — added. **Chengyu**: one grep hit, [[論功行賞]], confirmed a false positive (廷 appears only inside the compound 朝廷 in quoted example sentences). Two more grep hits, [[今朝]] and [[宮殿]], were also false positives (mentioning 朝廷/宮廷 only as comparative asides in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 妃 (6170; 1485 characters remaining).

### 2026-08-09, iteration 1020 — [[characters/妃|妃]]

`mc_id: 1691` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one).

**Classification bug found and fixed**: stored `graphemic_classification: 己` implied a 形聲 analysis with 己 as phonetic — but Wiktionary presents only a single, uncontested 會意 analysis ([[女 (char)|女]] "woman" + 卩 "a kneeling man"), with no competing 形聲 reading offered anywhere. OC evidence rules 己 out decisively too: 己's own reading (\*kɯʔ, velar k-) has nothing in common with 妃's \*pʰɯl. Corrected to the literal type-name `會意`.

Vietnamese `[phi]` confirmed complete. `stand_in: 王妃` confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[王妃]]<rt>⺢ㄫㄈㄧ</rt></ruby> "queen, queen consort" (stand-in for 妃). **Chengyu**: two grep hits, [[天長地久]] and [[沈魚落雁]], both confirmed false positives (妃 appears only as part of the historical figure's name 楊貴妃/Yang Guifei). **Derived Characters**: no hits (nothing cites 妃 as its own phonetic — consistent with it being 會意, not 形聲) — correctly has no section. A grep hit on [[王位]] was also a false positive (王妃 mentioned only as a cross-linked aside in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 遂 (6171; 1484 characters remaining).

### 2026-08-09, iteration 1021 — [[characters/遂|遂]]

`mc_id: 157` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 162|辵]] ("to move forward") + phonetic 㒸 (no vault page); `graphemic_classification: 㒸` already correct. Vietnamese `[toại]` confirmed complete. `stand_in: 既遂` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**Confirmed `aliases: [隧]` is a legitimate 借代字**, matching the pattern established on [[斬 (char)|斬]]/塹 and [[嫌]]'s aliases: the citing word [[遂道]] (aliased 隧道) already documents 遂 standing in for 隧 ("tunnel"). Built a new `### 借代字` subsection documenting this, since none existed despite the relationship already being in active use.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format plus the 借代字 subsection. **`## Words` section was entirely missing** — added the stand-in [[既遂]] and [[遂道]] "tunnel". **Chengyu**: two grep hits, [[国士無双]] and [[尊王攘夷]], both confirmed false positives (遂 appears only as part of the historical figure's name 毛遂, or inside the verb-conjugation やり遂げる in body prose). **Derived Characters**: no hits (nothing cites 遂 as its own phonetic) — correctly has no section. A grep hit on [[某様]] was also a false positive (遂 appears only inside やり遂げた, an illustrative example verb form).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 朱 (6172; 1483 characters remaining).

### 2026-08-09, iteration 1022 — [[characters/朱|朱]]

`mc_id: 784` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one).

**Classification bug found and fixed**: stored `graphemic_classification: 象形` — Wiktionary instead classifies this as 指事 (ideogram): a tree ([[木 (char)|木]]) with an extra dot-like stroke marking its center, the same indicative-mark pattern as [[本 (char)|本]] ("root") and [[末]] ("tip"). Corrected to `指事`.

**Vietnamese simplified**: stored an 8-item undifferentiated list (`chau, cho, choa, chu, châu, chõ, chẩu, chọ`) mixing Hán Việt with Nôm-looking noise; Wiktionary cleanly differentiates two Hán Việt readings (`chu, châu`, the latter corroborated by [[朱色]]'s own attested `chu sắc`) from a much larger separate Nôm list — trimmed to just the two Hán Việt readings. Filled the empty `pos` field to `名詞`.

**`stand_in: 朱砂` investigated and confirmed NOT broken**: no word file named exactly `朱砂.md` exists, which looked like the same phantom-stand_in bug fixed earlier on [[賄]]/[[賂]]/峡 — but [[朱沙]] (a real, already-existing word) lists `朱砂` as its own alias, so the reference resolves correctly via that alias rather than being broken.

**`## Notes`/`## Words` were jumbled** (stray CC-links, an informal tin-abbreviation aside, Notes/Words out of order) — rebuilt cleanly: standard 4-bullet Notes (using `Korean MS` for `hanmun_edu_level: 中`, matching the [[共]] precedent), then `## Words` with the stand-in [[朱沙]] plus [[朱色]] and [[朱錫]]. **`## Derived Characters` was entirely missing**: 8 genuine hits found (all confirmed citing 朱 as their own phonetic) — [[株 (char)|株]], [[侏]], [[殊]], [[洙]], [[珠]], [[蛛]], [[邾]], [[誅]] — added. **Chengyu**: 7 grep hits, all confirmed false positives (朱 appears only as part of the historical figure Zhu Xi/朱熹 or Zhu Ziqing/朱自清's name, never in a `characters:` field).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 簿 (6173; 1482 characters remaining).

### 2026-08-09, iteration 1023 — [[characters/簿|簿]]

`mc_id: 1960` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[竹 (char)|竹]] ("bamboo") + phonetic [[溥]]; `graphemic_classification: 溥` already correct. `stand_in: 帳簿` confirmed genuine. Filled the empty `pos` field to `名詞`.

**Malformed Vietnamese entry fixed**: stored `[bạ, bạ/bộ, bộ, bợ]` had a slash-combined duplicate item (`bạ/bộ`) alongside its own already-separated components — same class of formatting bug as seen on other fields elsewhere this project (e.g. 帆's mandarin). Deduplicated to the clean 3-item list `[bạ, bộ, bợ]`, matching Wiktionary exactly.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[帳簿]]<rt>ㄐ⺢ㄫㄅㄛ</rt></ruby> "account book, ledger" (stand-in for 簿), the only word citing this character (a grep hit on [[出勤]] was a false positive, mentioning 出勤簿 only in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 簿 as its own phonetic) — correctly has no section.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 謁 (6174; 1481 characters remaining).

### 2026-08-09, iteration 1024 — [[characters/謁 (char)|謁]]

`mc_id: 901` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one).

**Glyph-confusion classification bug found and fixed**: stored `graphemic_classification: 喝` — Wiktionary instead names the true phonetic as 曷 (no vault page); 喝 (口+曷, "to shout") is itself a derivative of 曷, not 謁's direct donor. Corrected to `曷`, noting the visual-confusion risk directly in the Notes.

Vietnamese `[yết, ét]` confirmed complete. `stand_in: 謁` (self) confirmed genuine. Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[謁]]<rt>ㄝㄊ</rt></ruby> (stand-in for itself), the only word citing this character. **`## Derived Characters` was entirely missing**: one genuine hit, [[靄]] (confirmed citing 謁 as its own phonetic) — added. **Chengyu**: no hits.

**Fixed corrupted data on the citing word page** [[謁]] (words/謁.md): `vietnamese: null` was a literal string placeholder — corrected to `yết`; also filled its empty `pos` field to `事詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 蛍 (6175; 1480 characters remaining).

### 2026-08-09, iteration 1025 — [[characters/蛍 (char)|蛍]]

`mc_id: 7511` confirmed as legitimate long-tail data (蛍/螢 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is.

**Glyph-confusion classification bug found and fixed**: stored `graphemic_classification: 炎` ("flame") — Wiktionary instead names the true phonetic as 熒 ("fluorescent, to shine," no vault page), whose OC reading \*ɡʷeːŋ matches 蛍's own \*ɡʷeːŋ exactly; 炎 (yán) is phonetically unrelated. Corrected to `熒`, the same visual-confusion pattern as [[謁 (char)|謁]]'s 曷/喝 mixup last iteration.

Vietnamese `[huỳnh]` confirmed complete. `stand_in: 蛍` (self) confirmed genuine, `pos: 名詞` already correct. Filled the blank `boundedness` to `65`.

**`## Notes`/`## Words` were jumbled**: an informal "abbreviation for yttrium" aside sat in Notes, while Words had bare unformatted bullets ("also called a [[蛍火虫]]", "[[蛍光]] - florescence"). Rebuilt cleanly: standard 4-bullet Notes, then a proper `## Words` section with all four genuine citing words (verified via grep, all already perfected) — the stand-in [[蛍]], [[蛍火虫]] "firefly," [[蛍光]] "fluorescence," and [[蛍金]] "yttrium." **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 憎 (6176; 1479 characters remaining).

### 2026-08-09, iteration 1026 — [[characters/憎|憎]]

`mc_id: 1647` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[心 (char)|心]] ("heart") + phonetic 曾; `graphemic_classification: 曽` already correct (the vault's shinjitai page for this same phonetic). Vietnamese `[tăng]` confirmed complete. `stand_in: 憎悪` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[憎悪]]<rt>ㄐㄜㄫㄚㄎ</rt></ruby> "hate, loathe" (stand-in for 憎), the only word citing this character. **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 憎 as its own phonetic) — correctly has no section. Two grep hits, [[七情]] and [[仇恨]], were false positives (憎 appears only in a philosophical enumeration and a cross-linked aside in body prose, never in a `characters:` field).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 遣 (6177; 1478 characters remaining).

### 2026-08-09, iteration 1027 — [[characters/遣 (char)|遣]]

`mc_id: 404` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 會意 classification confirmed via Wiktionary: originally 𠳋 in oracle bone script (two 又 "hand" + 𠂤 "army"), with [[Radical 162|辵]] added later in bronze inscriptions; `graphemic_classification: 會意` already correct. Vietnamese `[khiến, khiển]` confirmed complete. `stand_in: 遣` (self) confirmed genuine, `pos: 事詞` already correct.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[遣]]<rt>ㄎㄝㄋ</rt></ruby> (stand-in for itself), the only word citing this character (a grep hit on [[周囲]] was a false positive, mentioning 仮名遣い, an unrelated compound, only in body prose). **Chengyu**: no hits. **Derived Characters**: no hits (nothing cites 遣 as its own phonetic — consistent with it being 會意) — correctly has no section.

**Filled missing fields on the citing word page** [[遣]] (words/遣.md): `vietnamese` was entirely absent — added `khiển` (the Hán Việt reading); also filled the empty `pos` field to `事詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 涯 (6179; 1477 characters remaining).

### 2026-08-09, iteration 1028 — [[characters/涯 (char)|涯]]

**mc_id off-by-one fixed**: stored `3758` → actual rank in `CC 3000.md` is `3759`. 形声 classification confirmed via Wiktionary: semantic [[水 (char)|水]] ("water") + phonetic [[厓]]; `graphemic_classification: 厓` already correct. Vietnamese `[rượi, nhai, nhười, rười, nhầy]` confirmed complete (matches Wiktionary's set exactly, different order only). `stand_in: 涯` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[涯]]<rt>⼘ㄧ</rt></ruby> (stand-in for itself). **Chengyu**/**Derived Characters**: no hits for either. A grep hit on [[孟加拉]] was a false positive (涯 appears only inside a historical book title, 瀛涯勝覽, in body prose).

**Completed a homophone cross-reference left pending from an earlier iteration**: [[刈]]'s own page already lists 涯 as a homophone and explicitly notes "the reciprocal half of this callout will be completed when it comes up" — added the matching `>[!warning] Homophones` callout to [[涯]]'s own word page pointing back to 刈. Also filled its previously-blank `vietnamese` (→ `nhai`) and empty `pos` (→ `名詞`) fields.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 篤 (6180; 1476 characters remaining).

### 2026-08-09, iteration 1029 — [[characters/篤|篤]]

`mc_id: 1255` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). **Investigated `graphemic_classification: 竹` and confirmed NOT a bug**: this looked suspicious since it's identical to the `radical` field, but Wiktionary independently confirms 竹 genuinely is 篤's phonetic donor (OC \*tuɡ, an unusually close match to 篤's own \*tuːɡ despite the modern zhú/dǔ divergence) — a coincidence of 竹 doing double duty as both the Kangxi radical and the phonetic component, not an error. `stand_in: 純篤` confirmed genuine (already perfected).

**Vietnamese contamination fixed**: stored `[dóc, dốc, giốc, đốc]`; Wiktionary's Hán Việt/Nôm lists together cover `đốc, dốc, dóc` (plus others not stored) but never `giốc` — removed as unattested. Filled the empty `pos` field to `性詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, including a note on the coincidental radical/phonetic overlap. **`## Words`**: [[純篤]] was already present, missing only its "(stand-in for 篤)" tag — added. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 僧 (6181; 1475 characters remaining).

### 2026-08-09, iteration 1030 — [[characters/僧|僧]]

`mc_id: 7714` confirmed as legitimate long-tail data (僧 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[人 (char)|人]] ("person") + phonetic [[曽 (char)|曾]]; `graphemic_classification: 曽` already correct — the character was specifically coined to transliterate Sanskrit संघ (saṃgha) via 僧伽/sōgya, using this existing phono-semantic pattern rather than acquiring the sense organically. Vietnamese `[tăng]` confirmed complete. `stand_in: 僧家` confirmed genuine.

**Found and flagged (not force-resolved) a significant cross-word reading inconsistency**: the character and two of its citing words ([[僧家]], [[阿僧祇]]) use ㄙㄜㄫ (seng), matching `kwin: true`/Sino-Korean 승 and the regular outcome shared by its entire phonetic family (曽/増/憎/層/謄/騰/贈, confirmed all landing in the ㄜㄫ group via the `韻 登開` lookup page). But three other citing words — [[僧侶]] (whose own `kwin: false` was already explicitly reasoned through in an earlier pass), [[尼僧]], and [[密陀僧]] — all instead use ㄙㄨㄫ (sung); [[僧伽]] is even internally self-contradictory (諺文/羅馬字 give sung-pattern 숭갸/sunggya, but its own 注音 gives seng-pattern ㄙㄜㄫㄍ⼘). Left the character's own well-supported reading unchanged and documented the full inconsistency directly on the page — resolving it needs a dedicated word-sweep pass across all six compounds, not a character-page fix.

**`## Notes` mixed an informal etymology aside with two bare CC-lookup links and unformatted Words-style bullets** — rebuilt cleanly: standard 4-bullet Notes (with the flag bullet above), then a proper `## Words` section with all 6 genuine citing words found via grep (each ruby annotation using that word's own stored 注音, not overridden) — the stand-in [[僧家]], [[僧侶]], [[僧伽]], [[阿僧祇]], [[尼僧]], and [[密陀僧]]. **Chengyu**: one grep hit, [[画龍点睛]], confirmed a false positive (mentions the painter 張僧繇's name, not a citation). **Derived Characters**: no hits (nothing cites 僧 as its own phonetic) — correctly has no section. A grep hit on [[獅子]] was also a false positive (僧伽羅 listed only as an unrelated alias).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 稚 (6182; 1474 characters remaining).

### 2026-08-09, iteration 1031 — [[characters/稚|稚]]

`mc_id: 2520` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 115|禾]] ("rice") + phonetic [[屖]] (later substituted with 隹 in the Han dynasty); `graphemic_classification: 屖` already correct. **Vietnamese contamination fixed**: stored `[trĩ, trẻ, trẽ]`; Vietnamese Wiktionary confirms only `trĩ` (Hán Việt) and `trẻ` (Nôm) — `trẽ` isn't attested and was removed. `stand_in: 幼稚` confirmed genuine (already perfected). Filled the empty `pos` field to `性詞`.

**Removed an unsupported historical claim**: "Dropped from the Korean HS list in 2000" had no corroboration found anywhere and was stated as bare fact with no citation — removed, same standard applied to [[潟]]'s unverified "2017 Jōyō" claim and [[滋]]'s fabricated Jōyō-reform note earlier this project.

**`## Notes` was malformed** (the removed claim sitting between the etymology bullet and two floating CC-lookup links) — rebuilt to the standard 4-bullet format. **`## Words`**: [[幼稚園]] was already present; added the missing stand-in entry [[幼稚]]. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 禅 (6183; 1473 characters remaining).

### 2026-08-09, iteration 1032 — [[characters/禅 (char)|禅]]

`mc_id: 1474` confirmed correct (matches the traditional form 禪's actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[示 (char)|示]] ("to show, spirit") + phonetic 單.

**Glyph-mismatch bug found and fixed**: stored `graphemic_classification: 单` used the *Chinese* simplified form of 單, but the vault's actual page for this component is filed under `単.md`, the distinct *Japanese* shinjitai form (单 and 単 are different Unicode characters despite near-identical appearance) — consistent with 禅 itself being the shinjitai spelling. Corrected to `単`.

**Vietnamese incomplete, fixed**: stored `[thiền, xèng]`; Wiktionary's clearly-differentiated Hán Việt list adds two more genuine readings, `thiện` and `thuyền` — added. `stand_in: 禅` (self) confirmed genuine, `pos: 名詞` already correct.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[禅]]<rt>ㄙㄝㄋ</rt></ruby> (stand-in for itself), the only word citing this character. **Chengyu**: two grep hits, [[単刀直入]] and [[森羅万象]], both confirmed false positives (禅 appears only inside body-prose references to Chan/Zen Buddhism, e.g. 禅宗語録, never in a `characters:` field). **Derived Characters**: no hits (nothing cites 禅 as its own phonetic) — correctly has no section. A grep hit on [[無形]] was also a false positive (禅 mentioned only as an aside on Chan literature).

**Fixed corrupted data on the citing word page** [[禅]] (words/禅.md): both `vietnamese: null` and `korean: "null"` were literal string placeholders — corrected to `thiền` and `선` respectively; also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 矯 (6184; 1472 characters remaining).

### 2026-08-09, iteration 1033 — [[characters/矯|矯]]

**mc_id off-by-one fixed**: stored `1600` → actual rank in `CC 1000.md` is `1601`. 形声 classification confirmed via Wiktionary: semantic [[矢 (char)|矢]] ("arrow") + phonetic [[喬]]; `graphemic_classification: 喬` already correct. **Vietnamese contamination fixed**: stored 7-item list included `quéo`, which is not attested by Wiktionary's 6-item list (kiểu, kẻo, kẽo, khéo, kéo, kĩu) — removed. `stand_in: 矯正` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[矯正]] was already present, missing only its "(stand-in for 矯)" tag — added. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 儒 (6185; 1471 characters remaining).

### 2026-08-09, iteration 1034 — [[characters/儒|儒]]

`mc_id: 715` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[Radical 009|亻]] ("human") + phonetic [[需]]; `graphemic_classification: 需` already correct. Vietnamese `[nho, nhu, nhô]` confirmed complete. `stand_in: 儒家` confirmed genuine (already perfected).

**Confirmed `aliases: [孺]` is a legitimate phonetic-family alias, not yet in active use**: Wiktionary confirms 孺 (子 "child" + the same phonetic 需) shares 儒's exact reading, but no vault word currently cites it — same "not yet used" category as [[冥]]'s aliases, noted in prose rather than a full 借代字 subsection.

**`## Notes`/`## Words`/`## Chengyu` had stray blank lines and informal unformatted bullets** — rebuilt cleanly: standard 4-bullet Notes, then `## Words` expanded from 2 to 4 entries (added the missing stand-in tag on [[儒家]] plus two new genuine hits, [[儒教]] and [[侏儒]], found via a wide grep), then the existing `## Chengyu` entry ([[焚書坑儒]]) reformatted in place. Filtered out 7 grep false positives ([[坑]], [[尚書]], [[百家]], [[検閲]], [[不言不語]], [[七情]], [[諸子百家]]) — all mention 儒/儒家/儒教/焚書坑儒 only as illustrative compounds or aliases in body prose, never in their own `characters:` fields. **Derived Characters**: no hits (nothing cites 儒 as its own phonetic) — correctly has no section.

**Fixed two bugs found on citing word pages while cross-checking**: [[侏儒]]'s `vietnamese: chu,nhu` was a comma-joined string instead of a proper list — reformatted to `[chu, nhu]`. [[儒学]]'s `aliases` field was garbled (`[儒學, 儒教 a, d 孔教]`, with stray "a, d" characters splitting what should have been two clean entries) — corrected to `[儒學, 儒教, 孔教]`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 爵 (6186; 1470 characters remaining).

### 2026-08-09, iteration 1035 — [[characters/爵|爵]]

`mc_id: 372` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). Vietnamese `[tước]` confirmed complete. `stand_in: 男爵` confirmed genuine. The existing `### 借代字` documentation for [[且爵]] (standing in for 嚼, itself needed because 咀嚼's other half 咀 is too obscure for the Dan'a'yo set) was already correct — reformatted only.

**Classification bug found and fixed, with a documented conflict**: stored `graphemic_classification: 會意` — Wiktionary instead presents an uncontested 象形 analysis (a sparrow-shaped wine vessel, with variant forms adding a holding hand) and explicitly states no alternative classification is given. Corrected to `象形`. Notably, the already-perfected citing word [[爵位]] asserts "爵 is a 会意 character" in its own prose — left that word page's prose untouched (out of scope) but flagged the conflict directly on the character page for a future word-sweep pass to reconcile.

**`## Notes`/`## Words` were jumbled** (the 借代字 note mixed with bare CC-lookup links) — rebuilt cleanly: standard 4-bullet Notes, the 借代字 subsection, then `## Words` expanded from 3 to 5 entries — tagged [[男爵]] as the stand-in and added two genuine hits found via grep, [[伯爵]] "earl, count" and [[公爵]] "duke". Filtered out 8 grep false positives ([[論功行賞]], [[公]], [[侯]], [[上位]], [[学位]], [[工作]], [[王位]]) — all mention 爵/爵位/男爵/公爵 only as illustrative asides or homophone notes in body prose, never in their own `characters:` fields. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 拂 (6187; 1469 characters remaining).

### 2026-08-09, iteration 1036 — [[characters/拂 (char)|拂]]

**mc_id off-by-one fixed**: stored `2019` → actual rank in `CC 2000.md` is `2020`. 形声 classification confirmed via Wiktionary: semantic [[Radical 064|扌]] ("hand") + phonetic [[弗]]; `graphemic_classification: 弗` already correct. Vietnamese `[phất, phắt, phớt, phứt, phựt]` confirmed complete (matches Wiktionary's set exactly). `stand_in: 拂` (self) confirmed genuine. Filled the empty `pos` field to `事詞`.

**Fixed a malformed Notes bullet** (missing opening parenthesis: `形声: OC \*pʰɯd):` → `形声 (OC \*pʰɯd):`) while rebuilding `## Notes` to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[拂]]<rt>ㄈㄨㄊ</rt></ruby> (stand-in for itself), the only word citing this character (a grep hit on [[佛]] was a false positive, mentioning 拂 only as a comparison example for its own contaminated Vietnamese field). **Chengyu**/**Derived Characters**: no hits for either.

**Reading-mismatch bug fixed on the citing word page** [[拂]] (words/拂.md): its own `羅馬字`/`諺文` (`pud`/`푿`, a plain-ㅍ transcription) diverged from the character's own established `fud`/`뿓` (using tensed ㅃ to approximate the non-Korean /f/ sound) despite representing the identical bare-character word — corrected to match. Also filled the blank `vietnamese` (→ `phất`) and missing `pos` (→ `事詞`) fields.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 募 (6188; 1468 characters remaining).

### 2026-08-09, iteration 1037 — [[characters/募|募]]

**mc_id off-by-one fixed**: stored `2088` → actual rank in `CC 2000.md` is `2089`. 形声 classification confirmed via Wiktionary: semantic [[力 (char)|力]] ("strength, effort") + phonetic [[莫 (char)|莫]]; `graphemic_classification: 莫` already correct. Vietnamese `[mộ]` confirmed complete. `stand_in: 募集` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[募集]] was already present, missing only its "(stand-in for 募)" tag — added. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 庶 (6189; 1467 characters remaining).

### 2026-08-09, iteration 1038 — [[characters/庶|庶]]

`mc_id: 554` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: phonetic [[石 (char)|石]] + semantic [[火 (char)|火]] (石 corrupted to 𲟁 in small seal script); `graphemic_classification: 石` already correct despite initially looking suspicious (石 "stone" seems visually/semantically unrelated to 庶, but Wiktionary directly confirms it as the phonetic donor). Vietnamese `[thứ, thừa, xứa]` confirmed complete. `stand_in: 庶民` confirmed genuine (already perfected).

**Confirmed `aliases: [鷓]` is a legitimate phonetic-family alias, not yet in active use**: Wiktionary confirms 鷓 (鳥 "bird" + this same phonetic, used only in 鷓鴣 "partridge") shares 庶's exact reading, but no vault word currently cites it — same "not yet used" category as [[冥]]/[[儒]]'s aliases.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[庶民]]<rt>ㄙ⼄ㄇㄧㄋ</rt></ruby> (stand-in for 庶). **`## Derived Characters` was entirely missing**: 3 genuine hits found (all confirmed citing 庶 as their own phonetic) — [[度]], [[蹠]], [[遮]] — added. **Chengyu**: no hits. A grep hit on [[左学]] was a false positive (庶 appears only inside a quoted classical passage, 殷人養國老於右學養庶老於左學).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 岳 (6190; 1466 characters remaining).

### 2026-08-09, iteration 1039 — [[characters/岳|岳]]

`mc_id: 2505` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). Vietnamese `[nhạc]` confirmed complete. `stand_in: 山岳` confirmed genuine (already perfected).

**Classification investigated, kept unchanged after finding the alternatives unreliable**: Wiktionary's own machine-summarized etymology was internally inconsistent across fetches — one pass named 丘 as phonetic, another named an archaic 羋-type glyph, and 嶽 (this character's own traditional alias) separately gets analyzed with phonetic 獄 — three different, mutually exclusive candidates from the same source. None is phonetically plausible against 岳's own ŋ-initial reading (丘 is k-initial, 羋 is m-initial, 獄 is a different rhyme entirely), so no genuine 形聲 analysis holds up. Left `graphemic_classification: 會意` unchanged (semantic doubling of mountain-shaped elements) and documented the unreliable/conflicting alternative claims directly on the page rather than picking one arbitrarily.

Filled the empty `pos` field to `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[山岳]]<rt>ㄙㄚㄇ·ㄚㄎ</rt></ruby> (stand-in for 岳). **Chengyu**/**Derived Characters**: no hits for either. Three grep hits — [[鄂国]], [[丈人]], [[白亜]] — were false positives (岳 appears only inside the personal name 岳飛/岳王 or the place-name aside 白岳山 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 寝 (6191; 1465 characters remaining).

### 2026-08-09, iteration 1040 — [[characters/寝 (char)|寝]]

`mc_id: 1076` confirmed correct (matches the traditional form 寢's actual rank in `CC 1000.md`, no off-by-one).

**Glyph-confusion classification bug found and fixed**: stored `graphemic_classification: 浸` ("to soak") — Wiktionary's own etymology names the archaic, pageless 𠬶 ("broom and hand") as the traditional phonetic, not 浸 at all. Neither is directly usable, but [[侵]] (OC \*sʰim, near-identical to 寢's own \*sʰimʔ, differing only by tone) is both phonetically excellent and already has a vault page — and 浸 is itself simply 氵+侵, meaning the stored value cited a derivative-of-the-derivative rather than either the true archaic donor or the closer phonetic match. Corrected to `侵`, with both the archaic and substitute reasoning documented on the page.

Vietnamese `tẩm` left unchanged (Wiktionary's Vietnamese section was truncated in every fetch attempt, but no contradicting evidence was found either). `stand_in: 寝` (self) confirmed genuine. Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[寝]]<rt>ㄑㄧㄇ</rt></ruby> (stand-in for itself), the only word citing this character. **Chengyu**/**Derived Characters**: no hits for either.

**Fixed corrupted data on the citing word page** [[寝]] (words/寝.md): both `vietnamese: null` and `korean: "null"` were literal string placeholders — corrected to `tẩm` and `침` respectively; also filled its empty `pos` field to `事詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 粧 (6192; 1464 characters remaining).

### 2026-08-09, iteration 1041 — [[characters/粧|粧]]

`mc_id: 7565` confirmed as legitimate long-tail data (粧/妝 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is.

**Investigated `graphemic_classification: 庄` and confirmed NOT a bug**: 妝 (the character 粧 is popularly a variant of) is analyzed with phonetic 爿, which looked like a mismatch at first — but Wiktionary gives 粧 *itself* an independent phono-semantic analysis: semantic [[米 (char)|米]] ("rice," referencing rice powder as face powder) + phonetic 庄 (no vault page), treating it as more than a bare graphic substitution of 妝. `graphemic_classification: 庄` already correct.

Vietnamese `[chang, trang]` confirmed complete. `stand_in: 化粧` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞` and the blank `boundedness` to `65`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[化粧]]<rt>ㄏ⺢ㄐ⺢ㄫ</rt></ruby> "put on make-up" (stand-in for 粧), the only word citing this character. **Chengyu**/**Derived Characters**: no hits for either.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 壌 (6193; 1463 characters remaining).

### 2026-08-09, iteration 1042 — [[characters/壌|壌]]

`mc_id: 1599` confirmed correct (matches the traditional form 壤's actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[土 (char)|土]] ("earth") + phonetic 襄 (no vault page); `graphemic_classification: 襄` already correct. `stand_in: 壌土` confirmed genuine (already perfected).

**Vietnamese was entirely empty, filled**: Wiktionary confirms `nhưỡng` as the genuine Hán Việt reading — added. Filled the blank `boundedness` to `65`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[壌土]] was already present, missing only its "(stand-in for 壌)" tag — added. **Chengyu**/**Derived Characters**: no hits for either — both correctly omitted.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 浦 (6194; 1462 characters remaining).

### 2026-08-09, iteration 1043 — [[characters/浦 (char)|浦]]

**mc_id off-by-one fixed**: stored `2505` (coincidentally identical to [[岳]]'s own genuine rank, fixed two iterations ago) → actual rank in `CC 2000.md` is `2506`. 形声 classification confirmed via Wiktionary: semantic [[Radical 085|氵]] ("water") + phonetic [[甫]]; `graphemic_classification: 甫` already correct. **Malformed Vietnamese entry fixed**: `[phố, phổ]` was crammed into a single comma-joined list item — split into two proper entries (both confirmed genuine by Wiktionary). `stand_in: 浦` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**Duplicate `## Notes` heading merged**: the file had two separate `## Notes` sections (an empty one with two bare CC-lookup links, followed by a second with the actual etymology bullet) — merged into one, rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added the stand-in [[浦]] and [[新嘉浦]] "Singapore" (a genuine hit found via grep). **`## Derived Characters` was entirely missing**: one genuine hit, [[蒲]] (confirmed citing 浦 as its own phonetic) — added. **Chengyu**: no hits. Two grep hits, [[盛者必衰]] and [[東芝]], were false positives (浦 appears only inside place names — 壇ノ浦, 芝浦 — in body prose).

**Fixed two bugs found on citing word pages**: [[浦]] (words/浦.md) had the recurring `vietnamese: null` corruption — corrected to `phố`; also filled its empty `pos` field to `名詞`. [[新嘉浦]]'s `tags` field had a malformed double-dash entry (`- - neologism`) — corrected to a clean list.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 勃 (6195; 1461 characters remaining).

### 2026-08-09, iteration 1044 — [[characters/勃|勃]]

`mc_id: 1226` confirmed correct (matches actual rank in `CC 1000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: phonetic 孛 (no vault page) + semantic [[力 (char)|力]] ("power"); `graphemic_classification: 孛` already correct. Vietnamese `[bột]` confirmed complete. `stand_in: 勃興` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Words`/`## Notes` were reversed and jumbled** (Words appeared before Notes, with an informal bullet stranded inside Notes) — rebuilt cleanly: standard 4-bullet Notes, then `## Words` with the stand-in [[勃興]] (tagged) and [[勃勃]]. **`## Chengyu` section was entirely missing**: found one genuine hit, [[生机勃勃]] ("Vital Thriving," citing 勃 twice via reduplication) — added; [[Biblical Chengyu]] was a false positive (an index page, not an actual chengyu entry). **`## Derived Characters` was entirely missing**: one genuine hit, [[哱]] (confirmed citing 勃 as its own phonetic) — added; a second candidate, [[悖]], was excluded after its own `graphemic_classification` turned out to be corrupted (`形声`, the classification-type label itself rather than an actual phonetic component) — out of scope to fix today, since 悖 isn't yet due in the backlog. Two more grep hits, [[日暮]] and [[生机]], were false positives (勃 appears only inside the illustrative idiom 朝氣蓬勃 or the example compound 生機勃勃 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 撤 (6197; 1460 characters remaining).

### 2026-08-09, iteration 1045 — [[characters/撤 (char)|撤]]

`mc_id: 4802` confirmed as legitimate long-tail data (撤 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[手 (char)|手]] ("hand") + abbreviated phonetic 徹 (no vault page); `graphemic_classification: 徹` already correct. Vietnamese `[triệt, trẹt, trê, trệt, trịt]` confirmed complete (matches Wiktionary's set exactly). `stand_in: 撤` (self) confirmed genuine. Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[撤]]<rt>ㄉㄝㄊ</rt></ruby> (stand-in for itself), the only word citing this character. **Chengyu**/**Derived Characters**: no hits for either.

**Fixed corrupted data on the citing word page** [[撤]] (words/撤.md): `vietnamese: null` was a literal string placeholder — corrected to `triệt`; also filled its empty `pos` field to `事詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 扇 (6199; 1459 characters remaining).

### 2026-08-09, iteration 1046 — [[characters/扇|扇]]

**mc_id off-by-one fixed**: stored `2947` → actual rank in `CC 2000.md` is `2948`. 會意 classification confirmed via Wiktionary: [[戸 (char)|戶]] ("door") + [[羽 (char)|羽]] ("feather") — a door-shaped feathered fan; `graphemic_classification: 會意` already correct. Vietnamese `[phiến, thiên]` left unchanged — no corroborating or contradicting evidence found (both English and Vietnamese Wiktionary lacked readings for this entry). `stand_in: 扇子` confirmed genuine (already perfected).

**Confirmed `aliases: [煽]` is a legitimate phonetic-family alias, not yet in active use**: Wiktionary confirms 煽 (火 "fire" + this same phonetic) shares 扇's near-identical reading, but no vault word currently cites it — same "not yet used" category as [[冥]]/[[儒]]/[[庶]]'s aliases.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[扇子]]<rt>ㄙ⼶ㄋㄐㄜ</rt></ruby> (stand-in for 扇). **Chengyu**/**Derived Characters**: no hits for either. A grep hit on [[梯子]] was a false positive (扇子 mentioned only as an illustrative example of the noun-suffix 子 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 彫 (6201; 1458 characters remaining).

### 2026-08-09, iteration 1047 — [[characters/彫|彫]]

**mc_id off-by-one fixed**: stored `2808` → actual rank in `CC 2000.md` is `2809`. 形声 classification confirmed via Wiktionary: semantic [[彡]] ("patterns, ornamentation") + phonetic [[周 (char)|周]]; `graphemic_classification: 周` already correct. `aliases: [雕]` confirmed genuine (彫 is explicitly the Japanese form, 雕 the Chinese form, of the same character). Vietnamese `[điêu, đêu]` confirmed complete.

**Broken `stand_in` fixed**: stored `彫塑` does not exist anywhere in the vault as a word file — another phantom stand-in, same pattern as [[賄]]/[[賂]]/[[峡]] before it. Grepped for genuine citing words: [[彫像]] "statue, image" and [[彫刻]] "carve, sculpt" both exist and are already perfected; repointed `stand_in` to [[彫刻]] (matching 彫's own core "carve, engrave" sense and `pos: 事詞` exactly, vs. 彫像's narrower noun sense).

**`## Notes` had two floating CC-lookup links plus two informal Words-style bullets** — rebuilt cleanly: standard 4-bullet Notes, then a proper `## Words` section with both genuine citing words, [[彫刻]] tagged as the stand-in. **Chengyu**/**Derived Characters**: no hits for either. Two grep hits, [[石像]] and [[朽木糞牆]], were false positives (彫 appears only in illustrative comparison/example prose).

**Fixed a structural bug and a typo on the citing word page** [[彫刻]] (words/彫刻.md): a comparison note (彫塑 vs 刻印) was floating directly under `## Etymology` with no heading of its own — added a `## Notes` heading above it; also fixed "engrace" → "engrave" in the Etymology line.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 昆 (6202; 1457 characters remaining).

### 2026-08-09, iteration 1048 — [[characters/昆 (char)|昆]]

`mc_id: 988` confirmed correct (matches actual rank in `CC 0000.md`, no off-by-one). 象形 classification confirmed via Wiktionary: a pictogram of an insect's body and legs — the top is not semantically "sun/day" despite the modern radical assignment; `graphemic_classification: 象形` already correct. Replaced the informal "Components: [[日]], [[比]]" line (misleadingly implying a two-part compound) with an accurate description of the single pictograph. Vietnamese `[con, côn, gon]` confirmed complete. `stand_in: 昆` (self) confirmed genuine.

**Confirmed all three `aliases` entries are legitimate**: 蜫 and 䖵 are genuine variant forms (identical OC \*kuːn reading), and [[錕]] is a genuine phonetic derivative (金 + this phonetic, used in 錕鋙) — none yet cited by any vault word, same "not yet used" category as [[冥]]/[[儒]]/[[庶]]/[[扇]]'s aliases.

**`## Notes` was a bare two-link stub plus the misleading components line** — rebuilt to the standard 4-bullet format. **`## Words` was missing its own stand-in entry**; added it alongside the two already-present genuine entries, [[昆虫]] and [[昆布]]. **`## Derived Characters` was entirely missing**: 3 genuine hits found (all confirmed citing 昆 as their own phonetic) — [[棍]], [[混]], [[鯤]] — added. **Chengyu**: no hits.

**Fixed corrupted data on the citing word page** [[昆]] (words/昆.md): `vietnamese: null` was a literal string placeholder — corrected to `côn`; also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 朽 (6204; 1456 characters remaining).

### 2026-08-09, iteration 1049 — [[characters/朽|朽]]

**mc_id off-by-one fixed**: stored `1981` → actual rank in `CC 1000.md` is `1982`. **Investigated `graphemic_classification: 考` and confirmed NOT a bug**: Wiktionary's own etymology names the true phonetic as 丂 (no vault page), which looked like the usual sibling-donor mixup — but 丂 and [[考]] are documented as genuine *variant forms of each other*, sharing the identical OC reading \*kʰluːʔ (unlike the earlier 踪→宗 case, where the substituted sibling had a genuinely different sound). Citing 考 carries zero phonetic loss, so left unchanged and documented the reasoning, matching the [[寝]]→侵 precedent from a few iterations ago.

Vietnamese `[hủ]` confirmed complete. `stand_in: 腐朽` confirmed genuine (already perfected) — its own doubled Vietnamese reading `hủ hủ` is not a duplication bug, since both 腐 and 朽 independently read `hủ`, verified against 腐's own stored field. Filled the empty `pos` field to `性詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[腐朽]] was already present, missing only its "(stand-in for 朽)" tag — added. **`## Chengyu`**: [[朽木糞牆]] was already correctly present, confirmed genuine. **Derived Characters**: no hits (nothing cites 朽 as its own phonetic) — correctly has no section. A grep hit on [[千年]] was a false positive (朽 appears only inside the illustrative phrase 千年不朽 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 柄 (6205; 1455 characters remaining).

### 2026-08-09, iteration 1050 — [[characters/柄 (char)|柄]]

**mc_id off-by-one fixed**: stored `1880` → actual rank in `CC 1000.md` is `1881`. 形声 classification confirmed via Wiktionary: semantic [[木 (char)|木]] ("wood") + phonetic [[丙 (char)|丙]]; `graphemic_classification: 丙` already correct. Vietnamese `bính` left unchanged after a source conflict — Vietnamese Wiktionary's own fetch gave "binh" (no diacritic) instead, but the character's own homophone [[丙]] independently confirms `bính` as the reading for this exact Dan'a'yo syllable group, so the existing value was trusted over the single conflicting fetch. `stand_in: 柄` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added the stand-in [[柄]] and a genuine hit found via grep, [[柄国]] "to rule (literary)". **Chengyu**/**Derived Characters**: no hits for either.

**Completed a homophone cross-reference left pending from two earlier iterations**: [[丙]] and [[坪]] both already list 柄 as a homophone (all three share byeng/병/ㄅ⼶ㄫ) and explicitly note the reciprocal callout was still pending — added the matching `>[!warning] Homophones` callout to [[柄]]'s own word page pointing back to both. **Fixed corrupted data on the same citing word page**: `vietnamese: null` was a literal string placeholder — corrected to `bính`; also filled its empty `pos` field to `名詞`.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 伺 (6206; 1454 characters remaining).

### 2026-08-09, iteration 1051 — [[characters/伺|伺]]

`mc_id: 2630` confirmed correct (matches actual rank in `CC 2000.md`, no off-by-one). 形声 classification confirmed via Wiktionary: semantic [[人 (char)|人]] ("person") + phonetic [[司 (char)|司]]; `graphemic_classification: 司` already correct. Vietnamese `[tí, tứ]` left unchanged — no corroborating or contradicting evidence found (Wiktionary omits Vietnamese for this character entirely), and the citing word [[伺候]]'s own attested `tứ hầu` independently confirms `tứ` as genuinely in use. `stand_in: 伺候` confirmed genuine (already perfected, and its Notes already document the polyphonic cì/sì distinction cleanly).

**`## Notes` had an informal "Components:" line plus two floating CC-lookup links** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[伺候]]<rt>ㄙㄧㄏㄛㄨ</rt></ruby> (stand-in for 伺), the only word citing this character. **Chengyu**/**Derived Characters**: no hits for either. Three grep hits — [[虎視耽耽]], [[様子]], [[時候]] — were all false positives (伺 appears only in a quoted classical phrase, an illustrative Japanese example 様子を伺う, or a homophone-note aside).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 泌 (6207; 1453 characters remaining).

### 2026-08-09, iteration 1052 — [[characters/泌|泌]]

`mc_id: 5806` confirmed as legitimate long-tail data (泌 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. 形声 classification confirmed via Wiktionary: semantic [[水 (char)|水]] ("water") + phonetic [[必 (char)|必]]; `graphemic_classification: 必` already correct. **Vietnamese incomplete, fixed**: stored `[tiết]` only; Wiktionary lists a second genuine reading, `tất` — added. `stand_in: 分泌` confirmed genuine (already perfected). Filled the empty `pos` field to `事詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: [[分泌]] was already present, missing only its "(stand-in for 泌)" tag — added. **Chengyu**/**Derived Characters**: no hits for either. Two grep hits, [[分掌]] and [[唾液]], were false positives (泌 appears only inside the illustrative compound 分泌 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 氾 (6208; 1452 characters remaining).

### 2026-08-09, iteration 1053 — [[characters/氾|氾]]

**mc_id significantly wrong, fixed**: stored `2701` → actual rank in `CC 2000.md` is `2766`, a 65-rank gap far larger than the usual off-by-one pattern — corrected regardless of magnitude, since the ground truth (`CC 2000.md` line 799, "2766. 氾") is unambiguous.

**Classification bug found and fixed**: stored `graphemic_classification: 象形` — Wiktionary instead gives an uncontested 形聲 analysis: semantic [[水 (char)|水]] ("water") + phonetic 𢎘 (no vault page). Corrected to `𢎘`.

**Malformed `mandarin` field fixed**: stored `"fán fàn"` crammed two distinct, unrelated readings into one field — `fán` names a place in Henan and a surname, while `fàn` (the reading actually used in the stored `english: overflow` sense, and independently confirmed by the citing word [[氾濫]]'s own `mandarin: fànlàn`) is a variant of 泛. Corrected to just `fàn`, noting the excluded `fán` sense in the Notes, same pattern as the earlier [[帆]] fix.

Vietnamese `[phiếm]` confirmed complete. `stand_in: 氾濫` confirmed genuine (already perfected).

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` section was entirely missing** — added <ruby>[[氾濫]]<rt>ㄈㄚㄇㄌㄚㄇ</rt></ruby> (stand-in for 氾). **`## Derived Characters` was entirely missing**: 2 genuine hits found (both confirmed citing 氾 as their own phonetic) — [[範]], [[犯]] — added. **Chengyu**: one grep hit, [[五風十雨]], confirmed a false positive (氾 appears only inside a cited classical work's title, 氾論訓, not in its own `characters:` field).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 殖 (6209; 1451 characters remaining).

### 2026-08-09, iteration 1054 — [[characters/殖|殖]]

**mc_id off-by-one fixed**: stored `1770` → actual rank in `CC 1000.md` is `1771`. 形声 classification confirmed via Wiktionary: semantic [[歹]] ("death, decay") + phonetic [[直 (char)|直]]; `graphemic_classification: 直` already correct. Vietnamese `[thực]` confirmed complete. `stand_in: 繁殖` confirmed genuine (already perfected).

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` expanded**: added the missing stand-in [[繁殖]] and a genuine hit found via grep, [[養殖]] "cultivate, breed"; [[殖民]] was already present. Filled the empty `pos` field to `事詞`. **Chengyu**/**Derived Characters**: no hits for either. A grep hit on [[様式]] was a false positive (cross-references 養殖 only as its own homophone, doesn't cite 殖 itself).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 坑 (6210; 1450 characters remaining).

### 2026-08-09, iteration 1055 — [[characters/坑 (char)|坑]]

**mc_id off-by-one fixed**: stored `3185` → actual rank in `CC 3000.md` is `3186`. 形声 classification confirmed via Wiktionary: semantic [[土 (char)|土]] ("earth") + phonetic [[亢]]; `graphemic_classification: 亢` already correct.

**Vietnamese contamination fixed, using research already done on the citing word**: stored `[ganh, khanh]`; the citing word [[坑]]'s own Notes (found while perfecting [[儒]] two iterations ago) had already investigated `ganh` and flagged it as "likely spurious" — no regular MC sound-change path connects it, and the real Vietnamese words ganh/gánh/gành have no plausible semantic link to "pit." Removed it, and added two genuine Hán Việt readings Wiktionary lists but weren't yet stored, `khâng` and `khuâng`.

`stand_in: 坑` (self) confirmed genuine. Filled the empty `pos` field to `名詞`.

**`## Notes`/`## Chengyu` had two floating CC-lookup links** — rebuilt `## Notes` to the standard 4-bullet format. **`## Words` section was entirely missing** — added the stand-in [[坑]] and a genuine hit, [[坑道]] "tunnel". **`## Chengyu`**: [[焚書坑儒]] was already correctly present (confirmed genuine during the [[儒]] iteration). **Derived Characters**: no hits. Two grep hits, [[尚書]] and [[検閲]], were false positives (already identified during the 儒 iteration as mentioning 焚書坑儒 only in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 怖 (6211; 1449 characters remaining).

### 2026-08-09, iteration 1056 — [[characters/怖|怖]]

**mc_id off-by-one fixed**: stored `2539` → actual rank in `CC 2000.md` is `2540`. 形声 classification confirmed via Wiktionary: semantic [[心 (char)|心]] ("heart") + phonetic [[布 (char)|布]]; `graphemic_classification: 布` already correct. **Vietnamese contamination fixed**: stored `[bố, phố]`; Wiktionary confirms only `bố` (also independently corroborated by the citing word [[恐怖]]'s own attested `khủng bố`) — `phố` (the reading properly belonging to 浦, "riverbank") isn't attested for 怖 and was removed. `stand_in: 恐怖` confirmed genuine (already perfected, already correctly tagged). Filled the empty `pos` field to `性詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **Chengyu**/**Derived Characters**: no hits for either. Two grep hits, [[焚書坑儒]] and [[打撃]], were false positives (怖 appears only inside the illustrative compound 恐怖 in body prose).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 棋 (6212; 1448 characters remaining).

### 2026-08-09, iteration 1057 — [[characters/棋|棋]]

**mc_id off-by-one fixed**: stored `3871` → actual rank in `CC 3000.md` is `3872`. 形声 classification confirmed via Wiktionary: semantic [[木 (char)|木]] ("wood") + phonetic [[其 (char)|其]]; `graphemic_classification: 其` already correct.

**Vietnamese contamination fixed, trusting existing deep research over the raw Wiktionary Nôm list**: stored `[cơi, cờ, cời, kè, kì]`. Wiktionary's own Nôm table adds a further candidate (`cài`) and would seem to support most of these — but the citing word [[将棋]]'s own Notes had already explicitly investigated `cơi`, `cời`, and `kè` and rejected all three as "unrelated Nôm phonetic-loan readings for different native words" (to poke a fire, a betel-nut tray, to pair up closely). Trusted that specific, reasoned research over Wiktionary's undifferentiated table — trimmed to just `cờ` and `kì`, the two [[将棋]] treats as genuine.

`stand_in: 将棋` confirmed genuine (already perfected) but was missing from `## Words` entirely — added, alongside the already-present [[囲棋]]. Filled the empty `pos` field to `名詞`.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **Chengyu**: three grep hits ([[切磋琢磨]], [[天圓地方]], [[日月星辰]]) all confirmed false positives (棋 appears only inside classical quotations/idiom fragments, never in a `characters:` field). **Derived Characters**: no hits. A grep hit on [[囲碁]] was also a false positive (that word is built on the distinct character 碁, not 棋).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 巾 (6213; 1447 characters remaining).

### 2026-08-09, iteration 1058 — [[characters/巾|巾]]

**mc_id off-by-one fixed**: stored `1557` (which is actually 敕) → actual rank in `CC 1000.md` line 583 is `1558`. **Classification confirmed**: `graphemic_classification: 象形` already correct — Wiktionary confirms 巾 is a pictogram of a hanging piece of cloth (OC *krɯn), matching the existing Notes gloss.

**Vietnamese contamination fixed**: stored `[cân, khân, khăn, vầy]`. Wiktionary's Hán Nôm table lists only `cân, khân, khăn` — no support anywhere for `vầy` (confirmed via a targeted re-fetch of the Vietnamese section specifically), and no citing word offers any research justifying it either. Removed as unsupported.

**`korean_native: 수건`** verified as correct despite being a Sino-Korean-derived form rather than a native word — confirmed via Korean Wiktionary that the traditional 훈음 (hun-eum) for 巾, attested back to the 訓蒙字會, glosses it as 슈건/수건 ("towel"); there is no separate native Korean word for this concept, so the dictionary tradition uses this form as the hun.

Filled empty `pos` → `名詞`. **`## Notes` was a single bare `# Notes` heading with two dangling initial/final links** — rebuilt to the standard 4-bullet format (all SKIP/Stroke/Grade/HSK/Jōyō/Korean-Name lookup pages confirmed to exist). **`## Words` was entirely missing** — added the sole genuine citing word, stand-in [[手巾]]. A broad grep for other characters containing 巾 as a radical (帯, 幕, 幣, 帖, 帆, 幟, 帚, 帛, 席, 常, 幅, 布, 帥, 帳, 幌, 希, 師, 帽, 幡, 市, 帝, 帰, 幇, 沛, 肺, 飾) confirmed none cite 巾 itself as their `graphemic_classification` — all false positives (semantic radical only, not phonetic derivation) — so **Chengyu** and **Derived Characters** are both correctly empty.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 冶 (6214; 1446 characters remaining).

### 2026-08-09, iteration 1059 — [[characters/冶|冶]]

**mc_id off-by-one fixed**: stored `1926` (actually 腰) → actual rank in `CC 1000.md` line 968 is `1927`.

**Classification corrected, force-resolved against stored value**: stored `graphemic_classification: 台` (形声, claiming shared OC \*lɯ with both 冶 and its supposed phonetic donor 台). Re-verified against Wiktionary, which explicitly analyzes 冶 as **會意** (呂 "metal ingots" + 刀 "ladle" + 口 decorative, depicting metal-casting), and is explicit that the simplified 刀+口 component only *resembles* 台 after graphic evolution — a coincidental shape, not a true phonetic donation. Cross-checked the OC reconstructions directly: 冶 is Zhengzhang \*laːʔ while 台 is \*lɯ — different rime class and coda, ruling out a real phonetic relationship (this is not a case of an acceptable near-identical-OC substitute donor). Changed `graphemic_classification` to `會意` and rewrote the Notes bullet accordingly, linking [List of 会意](lookup/List%20of%20会意.md) and noting the coincidental-resemblance detail so a future reader isn't tempted to "fix" it back to 台.

**Cross-page consistency fix**: [[characters/台 (char)|台]] (already perfected 2026-07-20) listed 冶 in its own `## Derived Characters` section on the strength of the old (incorrect) classification. Removed that entry now that 冶 is confirmed not to derive from 台; left 台's `date-last-perfect` stamp untouched since this was a narrow cross-reference correction, not a full re-perfecting pass.

Vietnamese `[dã]` confirmed correct against Wiktionary (sole Hán Nôm reading, no contamination). Filled empty `pos` → `事詞` (action/verb sense, "to smelt, cast metal," matching the pattern used for other action characters like [[殖]]).

**`## Words`**: both existing entries ([[鍛冶]], [[冶錬]]) confirmed as genuine citations via their `characters:` frontmatter; added the missing "(stand-in for 冶)" tag to the [[鍛冶]] bullet per convention. **Chengyu**: one grep hit ([[朽木糞牆]]) confirmed a false positive — 冶 appears there only inside the proper name 公冶長 in the idiom's classical-origin citation, not as a constituent. **Derived Characters**: none (no other character cites 冶 as its own `graphemic_classification`).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 辣 (char) (6215; 1445 characters remaining).

### 2026-08-09, iteration 1060 — [[characters/辣 (char)|辣]]

**`mc_id: 0` confirmed genuine, not a bug** — grepped all four `CC 0000.md`–`CC 3000.md` files and 辣 appears in none of them, confirming it as a later/vernacular-period character outside the top-4000 Classical Chinese frequency list (a legitimate sentinel, same pattern documented for other 0-valued characters this backlog). **Classification confirmed**: `graphemic_classification: 剌` matches Wiktionary's 形聲 analysis (semantic 辛 "acrid" + phonetic 剌). **Vietnamese** `[lát, lướt, lượt, lạt, nhạt, nhợt]` confirmed against Wiktionary's own Hán Việt + Nôm listing — an exact match, no contamination.

Filled empty `pos` → `性詞` (quality/adjective sense — "spicy, cruel" — matching the citing word [[辛辣]]'s own `性詞`).

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` was missing the character's own reflexive stand-in**: `stand_in: 辣` points to [[辣]] (words/辣.md, the single-character word using this same glyph — not yet perfected in its own right, out of scope here) — added it alongside the already-present [[辛辣]]. While there, fixed the recurring `vietnamese: null` corruption on [[辣]]'s own word page, replacing it with the confirmed Hán Việt reading `lạt`.

Two grep hits outside `## Words` confirmed false positives: [[四川]] (辣 appears only in body prose "麻辣," not in its `characters:` field — that word cites only 四 and 川) and — no Chengyu or Derived Characters hits at all.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 殻 (6216; 1444 characters remaining).

### 2026-08-09, iteration 1061 — [[characters/殻|殻]]

This page arrived mid-repair: a prior iteration (while researching [[穀]]'s phonetic family) had already caught and fixed a self-referential `graphemic_classification` bug (`殻` pointing to itself) to the correct `㱿`, but left an inline "**Corrected here**" note in the Notes prose instead of finishing the standard format, and the page had never been stamped. Completed the pass this cycle:

**Re-verified the classification fix was correct** against Wiktionary's IDS breakdown for 殼 (⿰ split between a phonetic stack `士+冖+一+几` and 殳 on the right) — confirms semantic [[Radical 079|殳]] ("weapon, to strike") + phonetic 㱿, matching what was already in the file. (An initial WebFetch summary of Wiktionary's prose garbled this as "semantic 几," but the IDS structure itself resolves the ambiguity: 几 is embedded inside the phonetic stack, not a separate semantic component.) Removed the leftover inline "Corrected here" annotation now that the fix is finalized and logged here instead.

**`mc_id: 4300` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 殻/殼/壳 appears in none of them, consistent with a value beyond the verifiable 1–4000 range — left unverified per established policy rather than guessed at.

**Malformed YAML fixed**: `japanese_native` had a stray extra list item (`から` as a scalar, then a dangling `- から` on the next line) — collapsed to the single scalar `から`. **`boundedness` was empty** — filled to `90`; the sole citing word [[貝殼]] (already perfected) explicitly states in its own Notes that 殻 "cannot appear independently," and no other word cites it.

**Vietnamese** `[xác]` and **`korean_native: 내려칠`** ("to strike down") both confirmed against Wiktionary/Korean Wiktionary — the latter is a valid variant of 殼's documented dual hun (껍질 "shell" / 치다 "to strike"), left as-is.

**`## Notes` rebuilt** to the standard 4-bullet format (all SKIP/Stroke/Grade/HSK/Jōyō/Korean-Name lookup pages confirmed to exist). **`## Words`**: added the missing "(stand-in for 殻)" tag to the existing [[貝殼]] entry — confirmed the only genuine citation via `characters:` frontmatter grep. **Chengyu**: no hits. **Derived Characters**: no other character cites `㱿` as its own `graphemic_classification`, so none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 踊 (6217; 1443 characters remaining).

### 2026-08-09, iteration 1062 — [[characters/踊|踊]]

**mc_id off-by-one fixed**: stored `3253` (actually 譙) → actual rank in `CC 3000.md` line 267 is `3254`. **Classification confirmed**: `graphemic_classification: 甬` matches Wiktionary's 形聲 analysis (semantic 𧾷/足 "feet" + phonetic 甬, matching OC \*loŋʔ exactly).

**Vietnamese contamination fixed**: stored `[dũng, giỏng, thõng]`. English Wiktionary's entry for 踊 has no Vietnamese section at all, and a Hán Việt dictionary (hvdic.thivien.net) confirms only a single reading, `dũng`, with no mention of `giỏng` or `thõng` anywhere. No citing word offered any research to corroborate the extra two. Trimmed to `[dũng]`.

Filled `korean_native: ''` → `뛰다` ("to jump," the native gloss half of the character's documented dual hun-eum 뛰다/무용, per Korean Wiktionary). Filled empty `pos` → `事詞`.

**`## Words`**: the existing [[踊躍]] entry confirmed as the sole genuine citation via its `characters:` frontmatter — added the missing "(stand-in for 踊)" tag. **Chengyu**: no hits. **Derived Characters**: no other character cites 踊 as its own `graphemic_classification`, so none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 雰 (6218; 1442 characters remaining).

### 2026-08-09, iteration 1063 — [[characters/雰|雰]]

**`mc_id: 5187` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 雰 appears in none of them, consistent with a value beyond the verifiable 1–4000 range. **Classification confirmed**: `graphemic_classification: 分` matches Wiktionary's 形聲 analysis (semantic 雨 "rain" + phonetic 分, OC \*pʰɯn vs. 分's \*pɯn — same rime, differing only by aspiration, a normal phonetic-series relationship). **Vietnamese** `[phân]` confirmed as the sole Hán Nôm reading per Wiktionary, no contamination.

Filled `korean_native: ""` → `안개` ("fog/mist," the native half of the character's documented dual hun-eum 안개/눈이 날리다 per Korean Wiktionary). Filled empty `pos` → `名詞`. Confirmed `hsk_level: ""` is a genuine, valid empty state (210 other perfected characters in this vault share it) rather than a gap — used the `[HSK No]` lookup-link convention in the levels bullet accordingly.

**`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words` cross-check surfaced a second genuine citation**: besides the already-listed stand-in [[雰囲気]] (the Japanese-coined 3-character form, 雰+囲+気), [[雰囲]] (a distinct, not-yet-perfected 2-character word corresponding to Mandarin's native 氛围/雰围, per its own `氛囲気` alias and `fēnwéi` reading) also genuinely cites 雰 as a constituent — added it. Flagging for whoever perfects [[雰囲]] in the word-sweep: it lists [[雰囲気]] as one of its own `aliases`, which is backwards/confusing (aliases should be spelling variants of the *same* word, not a reference to a related-but-distinct compound) — left untouched as out of scope for character-page perfecting. One grep hit on [[厳粛]] confirmed a false positive (雰 appears only in body-prose example text, not its `characters:` field). **Chengyu**: no hits. **Derived Characters**: no other character cites 雰 as its own `graphemic_classification`, so none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 溝 (char) (6219; 1441 characters remaining).

### 2026-08-09, iteration 1064 — [[characters/溝 (char)|溝]]

**mc_id off-by-one fixed**: stored `1501` (actually 津) → actual rank in `CC 1000.md` line 527 is `1502`. **Classification confirmed**: `graphemic_classification: 冓` matches Wiktionary's 形聲 analysis exactly (semantic 氵/水 "water" + phonetic 冓, OC \*koː). **Vietnamese** `[câu]` confirmed as the sole Hán Nôm reading, no contamination. `korean_native: 도랑` confirmed against Korean Wiktionary's documented hun (도랑/개천).

**Sibling-vs-derived check, correctly excluded**: a grep for 冓 in `graphemic_classification` surfaced [[構]], [[購]], [[講]] — all cite 冓 directly as their *own* phonetic donor (siblings sharing a common ancestor with 溝), not derivations of 溝 itself. Excluded from Derived Characters per the established rule; none apply here.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 1 entry to 6** after a full grep cross-check: added the reflexive stand-in [[溝]] (the word page for the bare character) plus four other genuine citations that were entirely missing — [[一溝]] (the classical large-number unit 10³²), [[交溝]] ("copulate," aliased elsewhere as 交媾 — confirming the character's own `媾` alias is genuinely in active use, not a documentation-only variant), [[溝涜]] ("ditch, gutter"), and [[排水溝]] ("gutter, culvert"). One grep hit on [[一]] confirmed a false positive (no 溝 in its `characters:` field). **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 婆 (6220; 1440 characters remaining).

### 2026-08-09, iteration 1065 — [[characters/婆|婆]]

**`mc_id: 6004` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 婆 appears in none of them. **Classification confirmed**: `graphemic_classification: 波` matches Wiktionary's 形聲 analysis (semantic 女 "woman" + phonetic 波, OC \*baːl).

**Vietnamese contamination fixed**: stored `[bà, bờ]`. Wiktionary lists only `bà` (Sino-Vietnamese), with no mention of `bờ` anywhere; neither citing word ([[乾達婆]], [[鬼婆]]) offered corroborating research. Trimmed to `[bà]`.

**`korean_native` precision fix**: `할머니` (the modern everyday word for "grandmother") → `할미`, the actual dictionary hun-eum gloss per Korean Wiktionary (할미/늙은 여자) — matching the convention used elsewhere in this vault of citing the traditional hun form rather than the modern colloquial synonym.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 1 entry to 4**: added the stand-in [[婆婆]] (already perfected, confirmed genuine — an earlier grep hiccup in this session briefly suggested the file didn't exist, but re-running from the correct working directory confirmed it does) plus two other genuine citations that were missing, [[乾達婆]] ("Gandharva") and [[鬼婆]] ("hag"). Five grep hits ([[孫孫]], [[四川]], [[祖母]], [[外祖母]], [[不丹]]) confirmed false positives — none cite 婆 in their own `characters:` field. **Chengyu**: two hits ([[一刀両断]], [[朽木糞牆]]) both confirmed false positives (婆 appears only inside classical-quotation body prose, not as a constituent). **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 購 (6221; 1439 characters remaining).

### 2026-08-09, iteration 1066 — [[characters/購|購]]

**mc_id off-by-one fixed**: stored `2821` (actually 驛) → actual rank in `CC 2000.md` line 859 is `2822`. **Classification confirmed**: `graphemic_classification: 冓` matches Wiktionary's 形聲 analysis (semantic 貝 "shell, money" + phonetic 冓, OC \*koːs). **Vietnamese** `[cấu]` confirmed as the sole Hán Nôm reading, no contamination.

**`cranberry` tag verified, not a bug**: `stand_in: 購買` — checked [[買 (char)|買]]'s own `stand_in` field and confirmed it's also `購買`, satisfying the transitivity condition (A=購, B=買, AB=購買 all share the one stand-in word) that licenses the tag.

**`korean_native` precision fix**: `살` (a conjugated stem form of 사다, "to buy") → `사다`, the dictionary-citation form matching Korean Wiktionary's documented hun and the convention used elsewhere for verb-sense characters (e.g. [[踊]]'s `뛰다`).

Filled empty `pos` → `事詞`. **`## Notes` was a bare stub** — rebuilt to the standard 4-bullet format; confirmed the homophone group with [[溝 (char)|溝]] (both read ㄍㄛㄨ) is already fully documented on the [[syllables/ㄍㄛㄨ|ㄍㄛㄨ]] syllable page, so no additional callout needed on this character page. **`## Words`**: both existing entries ([[購買]], [[購入]]) confirmed genuine via `characters:` frontmatter grep — added the missing "(stand-in for 購)" tag to [[購買]]. One grep hit on [[因小失大]] confirmed a false positive (購 appears only in body-prose example text, not the idiom's own citation). **Derived Characters**: none (no character cites 購 as its own `graphemic_classification`).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 串 (char) (6222; 1438 characters remaining).

### 2026-08-09, iteration 1067 — [[characters/串 (char)|串]]

**`mc_id: 8213` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 串 appears in none of them. **Classification confirmed**: `graphemic_classification: 象形` matches Wiktionary (pictogram of objects strung together).

**Etymological complexity researched**: 串 carries two distinct historical readings tracing to different cognates — chuàn (OC \*kʰjons, cognate with 穿 "pierce through," the "skewer/string together" sense used on this page) and guàn (OC \*kroːns, cognate with 貫 "penetrate, string of cash"). Documented both in the Notes rewrite.

**Vietnamese contamination fixed**: stored `[quán, xiên, xuyên, xuyến]`. The already-perfected word page [[串]] (2026-07-26) had already done the deep-dive research here and explicitly settled on exactly two attested Hán Việt/Nôm readings — `quán` (older, classical) and `xuyến` (the sense-appropriate reading for "string together, skewer," as in 一 xuyến châu, nhất xuyến) — with no mention of `xiên` or `xuyên` anywhere. Trimmed the character page to match: `[quán, xuyến]`.

**`korean`/`korean_native` both `곶` verified as intentional, not a duplication bug**: per Korean Wiktionary, 串's *regular* Sino-Korean on-reading would be 관 (matching the 貫-cognate guàn etymology), but in real-world Korean usage the character survives almost exclusively via the exceptional native-gloss reading 곶 (used in place names for "cape, headland" — an unrelated sense from "skewer"). Left both fields as-is; did not attempt to resolve the pre-existing "**Pronunciation is altered**" flag (shared verbatim with the [[串]] word page, which explicitly chose to retain it unexplained rather than guess) — noted in the Notes rewrite that this newly-researched chuàn/guàn split is the most likely referent, without overriding the word page's established caution.

Filled empty `pos` → `名詞`. **`## Notes` rebuilt** to the standard format around the above research. **`## Words`**: added the missing "(stand-in for 串)" tag to the existing [[串]] entry (a phantom-stand_in scare turned out to be a false alarm — a working-directory grep hiccup briefly suggested the word file didn't exist; re-running confirmed it does, already perfected). **`## Derived Characters`** was entirely missing despite a genuine hit: [[患 (char)|患]] (already perfected) cites 串 directly as its own `graphemic_classification` — added. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 焦 (char) (6223; 1437 characters remaining).

### 2026-08-09, iteration 1068 — [[characters/焦 (char)|焦]]

**mc_id off-by-one fixed**: stored `1438` (actually 腎) → actual rank in `CC 1000.md` line 460 is `1439`.

**Classification researched and confirmed, contested case resolved in favor of the stored value**: Wiktionary traces 焦's *deep* history to a 形聲 compound (semantic 隹 "bird" + phonetic 小, OC \*smewʔ, for an unrelated "small bird" sense), where 小 graphically corrupted into 火 during the Warring States period and the graph was repurposed by phonetic loan for today's "burnt, scorched" meaning — the original phonetic link is no longer visible or operative. Per this vault's own documented policy ([[lookup/List of 会意|List of 会意]]: "treat hidden or obsolete phonetic links as irrelevant unless productive"), kept `graphemic_classification: 會意`, describing the modern, transparent 隹+火 ("bird over fire") reading, and documented the etymological wrinkle in prose rather than silently discarding it.

**Vietnamese** `[tiêu]` confirmed as the sole Hán Nôm reading, no contamination. **`korean_native` precision fix**: `탈` (a conjugated stem of 타다, "to burn") → `타다`, the dictionary-citation form matching Korean Wiktionary's documented hun (그을리다/타다) — same pattern as the [[購]] and [[踊]] fixes earlier this stretch.

Filled empty `pos` → `性詞` (quality/adjective sense, "burned, scorched").

**`## Notes` was a bare stub with three dangling word-links** — rebuilt to the standard format. **`## Words` expanded from 3 to 5**: added the reflexive stand-in [[焦]] and the previously-missing [[三焦]] ("triple burner"), alongside the three already-listed ([[焦明]], [[焦点]], [[焦思]]). One grep hit on [[不安]] and [[六府]] confirmed false positives (no 焦 in their `characters:` fields). **Chengyu**: one hit ([[臥薪嘗胆]]) confirmed a false positive — 焦 appears there only inside a classical-quotation body text as part of the separate word 焦思, not the idiom's own citation. **`## Derived Characters` was entirely missing despite two genuine hits**: [[礁]] ("reef") and [[蕉]] ("banana, plantain") both cite 焦 directly as their own `graphemic_classification` — added both.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 艶 (char) (6224; 1436 characters remaining).

### 2026-08-09, iteration 1069 — [[characters/艶 (char)|艶]]

**`mc_id: 4351` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 艶 nor its traditional form 豔 appears in any of them. **Classification confirmed**: `graphemic_classification: 盍` matches Wiktionary's 形聲 analysis for 豔 (semantic 豐 "abundant" + phonetic 盍, itself a corruption of 盇).

**Vietnamese contamination fixed**: stored `[diễm, dém]`. The already-perfected word page [[艶]] (2026-05-15) had already settled on a single reading, `diễm`, with no mention of `dém` anywhere; Wiktionary itself lists `diệm`/`diễm` but not `dém` either. Trimmed to match the word page's settled research: `[diễm]`.

**`korean_native` precision fix**: `고울` (an adnominal/modifier conjugation of 곱다) → `곱다`, matching the literal infinitive-form gloss text as printed on Korean Wiktionary's own page for this character — consistent with the same sourcing method used for the [[購]], [[踊]], and [[焦 (char)|焦]] fixes earlier this stretch (verified this is the right call by specifically re-checking Wiktionary's literal printed gloss text rather than a paraphrase, after briefly worrying the earlier fixes might have been reversing a legitimate traditional citation-form convention).

Filled empty `pos` → `性詞`. **`boundedness` was empty** — filled to `65`, calibrated against nine other vault characters whose word pages likewise describe them as a "Standalone form" ([[雁]], [[薫]], [[亦]], [[訓]], [[閻]], [[塩]], [[凸]], [[岸]] all cluster at 65–75).

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format (neither phonetic 盍 nor semantic 豐 has its own character page in this vault, so both are left as plain text rather than broken wikilinks). **`## Words`**: both existing entries ([[艶]], [[艶福]]) confirmed genuine — added the missing "(stand-in for 艶)" tag and reading to [[艶福]]. Two grep hits ([[塩]], [[閻]]) confirmed false positives — 艶 appears only inside their homophone-callout cross-references, not their own `characters:` fields. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 阻 (6225; 1435 characters remaining).

### 2026-08-09, iteration 1070 — [[characters/阻|阻]]

**mc_id off-by-one fixed**: stored `1647` (actually 憎) → actual rank in `CC 1000.md` line 677 is `1648`. **Classification confirmed**: `graphemic_classification: 且` matches Wiktionary's 形聲 analysis (semantic 阝/阜 "mound, hill" + phonetic 且).

**Vietnamese expanded**: stored `[chở, trở]`, both confirmed. Wiktionary's own Hán Việt/Nôm split additionally lists `giở` ("to open up") as a distinct, explicitly-differentiated Nôm reading with no corroborating-or-contradicting research from either citing word ([[阻止]], [[阻碍]], neither has Vietnamese filled in yet) — added per the established policy of trusting Wiktionary's differentiated list when nothing else signals otherwise.

**`korean_native` corrected, not just a citation-form mismatch**: stored `험할` (from 험하다, "dangerous, steep, rugged") — a different semantic domain entirely from this character's actual meaning. Korean Wiktionary's literal printed gloss is `막히다` ("to be blocked, obstructed"), which both matches the character's real sense and follows the same infinitive-form sourcing convention as recent fixes. Replaced.

Filled empty `pos` → `事詞`. **Broken wikilink fixed**: the Notes bullet's phonetic component was written as `[[且]]`, but 且 has no character page in this vault — corrected to plain text, matching the no-page-exists convention used elsewhere; also filled in `[[阝]]`'s dangling empty gloss `("")` → `("mound, hill")` and properly linked it to [[Radical 170]].

**Sibling-vs-derived check, correctly excluded**: a grep for `且` in `graphemic_classification` surfaced nine characters ([[助]], [[査]], [[狙]], [[疽]], [[粗]], [[租]], [[組]], [[祖]], [[詛]]) — all cite 且 directly as their own phonetic donor (siblings of 阻 via a shared ancestor), not derivations of 阻 itself. None belong in Derived Characters.

**`## Notes` was a malformed partial stub** (missing SKIP/Stroke/levels bullets, two dangling initial/final links left outside the `## Words` section) — rebuilt to the standard 4-bullet format. **`## Words`**: [[阻碍]]'s ruby tag was oddly written as `/阻礙/阻害` (alias/cross-language forms dumped inline rather than as a clean gloss) — replaced with a proper gloss; added the missing stand-in [[阻止]]. One grep hit on [[梗塞]] confirmed a false positive (阻 appears only in body-prose example text "阻塞," not its own `characters:` field). **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 診 (6226; 1434 characters remaining).

### 2026-08-09, iteration 1071 — [[characters/診|診]]

**mc_id off-by-one fixed**: stored `2240` (actually 渙) → actual rank in `CC 2000.md` line 254 is `2241`. **Classification confirmed**: `graphemic_classification: 㐱` matches Wiktionary's 形聲 analysis (semantic 言 "speech" + phonetic 㐱). **Vietnamese** `[chẩn]` confirmed as the sole Hán Việt reading, no contamination.

**`korean_native` corrected, categorical error not just a citation-form mismatch**: stored `진찰할`, itself derived from Sino-Korean 診察 — not a native gloss at all, the wrong category of value for this field. Korean Wiktionary's literal printed hun is `보다` ("to see, look at" — examining a patient by looking/questioning), a genuine native word; replaced.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with no `## Words` section at all** — rebuilt to the standard format, confirming [[㐱]] has its own character page in this vault (linked properly rather than left as plain text).

**Sibling-vs-derived check, correctly excluded**: a grep for `㐱` in `graphemic_classification` surfaced [[参]] and [[珍 (char)|珍]] — both cite 㐱 directly as their own phonetic donor (siblings of 診 via a shared ancestor), not derivations of 診 itself. None belong in Derived Characters. Two grep hits ([[灰塵]], [[健康]]) confirmed false positives — 診 appears only inside body-prose compound examples (回診, 健康診斷), not either word's own `characters:` field. Added the missing stand-in [[診断]] to `## Words`. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 痕 (6227; 1433 characters remaining).

### 2026-08-09, iteration 1072 — [[characters/痕|痕]]

**`mc_id: 7145` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 痕 appears in none of them. **Classification confirmed**: `graphemic_classification: 艮` matches Wiktionary's 形聲 analysis (semantic 疒 "sickness" + phonetic 艮). **Vietnamese** `[ngân, ngấn, ngần, ngẩn, ngằn]` confirmed as an exact match to Wiktionary's combined Hán Việt/Nôm list, no contamination.

**`cranberry` tag re-verified**: `stand_in: 痕跡` — cross-checked [[跡]] (already perfected 2026-08-06), whose own page explicitly documents "#cranberry with [[痕]] — both independently mean 'trace, vestige,' transitivity holds." Confirmed correct.

**`korean_native: 흔적` checked against the actual literal source rather than assumed buggy by pattern-matching**: this looked structurally identical to the [[診]] and [[購]] `korean_native` bugs fixed earlier this stretch (a Sino-Korean-derived form rather than a "native" word) — but ko.wiktionary has no page for 痕, and English Wiktionary's own Korean/Hanja section literally prints the citation gloss as "흔적 흔" (heunjeok heun). Confirmed genuine as-is; left untouched. (Korean hun-eum citations can legitimately use a Sino-Korean word when no true native gloss exists — this is such a case, unlike 診's, where the stored value didn't match the source at all.)

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format.

**Sibling-vs-derived check, correctly excluded**: a grep for `艮` in `graphemic_classification` surfaced seven characters ([[恨 (char)|恨]], [[根 (char)|根]], [[銀 (char)|銀]], [[眼]], [[艱]], [[限]], [[齦]]) — all cite 艮 directly as their own phonetic donor (siblings of 痕 via a shared ancestor), not derivations of 痕 itself. None belong in Derived Characters. Added the missing citation [[痘痕]] ("pockmark, scar") to `## Words` alongside the existing stand-in [[痕跡]]. One grep hit on [[天衣無縫]] confirmed a false positive (痕 appears only in body-prose example text "斧鑿之痕," not the idiom's own citation).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 湧 (char) (6228; 1432 characters remaining).

### 2026-08-09, iteration 1073 — [[characters/湧 (char)|湧]]

**mc_id long-tail flag overturned — a real ranking exists**: stored `4540` looked like a standard long-tail sentinel, but grepping all four `CC 0000`–`CC 3000` files turned up its simplified variant `涌` at rank 2620 in `CC 2000.md`. Since 涌 is documented as 湧's own alias (same lexeme, variant glyph), the character genuinely does have a verified top-4000 ranking recorded under that spelling — corrected `mc_id` to `2620` rather than leaving the incorrect placeholder.

**Sibling-vs-true-donor, corrected in favor of the true donor**: stored `graphemic_classification: 勇`. Wiktionary's etymology for 涌/湧 names the phonetic component as 甬 directly (OC \*loŋʔ, exact match), not 勇 — and while 勇 does share an identical OC reading with 甬 (itself derived from 甬, OC \*loŋʔ, making it a technically "safe" same-OC substitute), the true donor 甬 has its own well-documented character page in this vault and was trivially available, so corrected to `甬` rather than settling for the sibling — matching the precedent set by the earlier 踪 (宗→從) correction this backlog. Confirmed [[勇]]'s own page doesn't cite 湧/涌 anywhere, so no cross-reference cleanup was needed on that end.

**Vietnamese contamination fixed**: stored `[dũng, dộng, rụng]`. Wiktionary's own Hán Nôm list for 涌 is `[dũng, dõng, dòng]` — only `dũng` overlaps; `dộng` and `rụng` don't match anything in the source (confirmed via a verbatim re-quote of the Vietnamese section to rule out transcription mismatch). No citing word offered corroborating research (the sole citation, [[湧]], carried the recurring `vietnamese: null` corruption bug instead — fixed to `dũng`, the primary reading, matching the pattern used for other single-character stand-in words this backlog). Replaced the character page's list to match Wiktionary exactly.

**`korean_native` left empty, deliberately**: no hun gloss is documented on Wiktionary for either 湧 or 涌 (only the bare sound reading 용 appears on both pages) — left blank rather than guess at a plausible-sounding native gloss like 솟다, per the vault's omit-don't-fabricate convention.

Filled empty `pos` → `事詞`. Confirmed `hanmun_edu_level: ""` is a genuine valid empty state (67 other perfected characters share it). **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format; confirmed the homophone group with [[用]], [[勇]], [[容 (char)|容]], [[庸 (char)|庸]], [[溶]], [[踊]], and [[甬]] is already fully documented on the [[syllables/⼄ㄫ|⼄ㄫ]] syllable page, so no additional callout needed here. **`## Words`**: added the missing "(stand-in for 湧)" tag to the sole genuine citation, [[湧]]. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 酷 (6229; 1431 characters remaining).

### 2026-08-09, iteration 1074 — [[characters/酷|酷]]

**mc_id off-by-one fixed**: stored `2324` (actually 謬) → actual rank in `CC 2000.md` line 342 is `2325`. **Classification confirmed**: `graphemic_classification: 告` matches Wiktionary's 形聲 analysis (semantic 酉 "wine" + phonetic 告). **Vietnamese** `[khốc]` confirmed as the sole Hán Nôm reading, no contamination.

**`korean_native` corrected, with a methodology note**: stored `독할` (from 독하다, "toxic/harsh"). Wiktionary's literal printed hun for 酷 is `심할` (from 심하다, "severe/intense") — replaced to match exactly. Notably, this citation is printed in the *adnominal* form (심할), not the infinitive (심하다) — confirming that Wiktionary's citation-form convention varies per character rather than following one rule, which is why each `korean_native` fix this backlog has checked the literal printed source directly rather than applying a blanket infinitive-vs-modifier assumption.

Filled empty `pos` → `性詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 酷)" tag to the existing [[苛酷]] entry. One grep hit on [[刻薄]] confirmed a false positive: 酷 appears only inside that word's own `aliases` field (酷薄, an alternate spelling of the same 刻+薄 word), not as a real constituent of 刻薄 itself. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 雇 (6230; 1430 characters remaining).

### 2026-08-09, iteration 1075 — [[characters/雇|雇]]

**`mc_id: 4407` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 雇 nor its alias 僱 appears in any of them. **Classification confirmed**: `graphemic_classification: 戸` matches Wiktionary's 形聲 analysis (semantic 隹 "bird" + phonetic 戸). **Vietnamese** `[cố]` confirmed as the sole Hán Nôm reading, no contamination.

**Etymology researched and corrected from an initial oversimplification**: 雇 originally meant "a migratory bird" — the "to employ, hire" sense in modern use actually belongs to a distinct, further-derived character, 僱 (亻+雇, itself phonetic on 雇), for which 雇 now serves as the standard simplified/merged form (matching why 僱 is already listed as this page's `aliases`). An initial draft framed this as a 假借 (phonetic loan) of the same character, but Wiktionary treats "bird" and "employ" as two separate etymological entries rather than one borrowed sense — corrected the Notes wording to reflect that more precisely.

Filled `korean_native: ""` → `품팔다`, matching Wiktionary's literal printed hun "품 팔 고" (a two-syllable gloss, "to sell one's labor," i.e. to work for hire — rendered here as the standalone dictionary verb). Filled empty `pos` → `事詞`.

**Sibling-vs-derived check, correctly excluded**: a grep for `戸` in `graphemic_classification` surfaced [[所 (char)|所]], [[肩 (char)|肩]], [[扈]], [[炉]], [[芦]] — all cite 戸 directly as their own phonetic donor (siblings of 雇), not derivations of 雇 itself. None belong in Derived Characters. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard format. **`## Words`**: added the missing "(stand-in for 雇)" tag to [[雇用]] and moved the dangling [[雇員]] link into a proper `## Words` entry with its reading. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 酬 (6231; 1429 characters remaining).

### 2026-08-09, iteration 1076 — [[characters/酬|酬]]

**`mc_id: 2333` verified correct as-is** — a rare clean pass: checked against `CC 2000.md` line 350 and confirmed 酬 itself sits at rank 2333, no off-by-one this time. **Classification confirmed**: `graphemic_classification: 州` matches Wiktionary's 形聲 analysis (semantic 酉 "wine vessel" + phonetic 州, no character page exists for 州 in this vault). **Vietnamese** `[thò, thù]` confirmed as an exact match to Wiktionary's Hán Nôm list, no contamination.

**`korean_native` corrected**: stored `갚을` (from 갚다, "to repay") — a plausible extended-sense gloss, but not what's actually printed. Korean Wiktionary's literal hun is the multi-word phrase `잔을 돌리다` ("to pass a cup around," the concrete drinking-ritual origin of the character, matching its 酉 semantic component) — replaced to match exactly; confirmed multi-word korean_native values are an established vault pattern (e.g. [[刊 (char)|刊]]'s `책 펴낼`, [[曇]]'s `날이 흐리다`), so this isn't a formatting departure.

Filled empty `pos` → `名詞` (matching the stand-in word [[報酬]]'s own `名詞`).

**`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format, tracing the semantic development from the literal drinking-ritual sense through to the modern "reward, recompense" gloss. **Sibling-vs-derived check, correctly excluded**: [[洲 (char)|洲]] cites 州 directly as its own phonetic donor (a sibling of 酬), not a derivation of 酬 itself — excluded from Derived Characters. Added the missing "(stand-in for 酬)" tag and corrected ruby reading to [[報酬]] (initial guess ㄅㄛㄨ... was wrong; verified against the word's own frontmatter and fixed to the actual ㄅㄚㄨㄙㄨㄛ). **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 艦 (6232; 1428 characters remaining).

### 2026-08-09, iteration 1077 — [[characters/艦|艦]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, neither 艦 nor its alias 舰 appears in any of them — a modern/late character genuinely absent from the Classical corpus, not a guess. **Classification confirmed**: `graphemic_classification: 監` matches Wiktionary's 形聲 analysis (semantic 舟 "boat" + phonetic 監). **Vietnamese** `[hạm]` and **`korean_native: 싸움배`** both confirmed as exact matches to Wiktionary/Korean Wiktionary, no fixes needed.

Filled empty `pos` → `名詞`. **Stray leftover text removed**: the Notes stub opened with "I'm shocked its not old" — the same kind of orphaned scratch-note text found and removed from [[描]] earlier in this backlog — deleted along with rebuilding the section to the standard 4-bullet format.

**`## Words` expanded dramatically, from 1 entry to 8**: a full grep cross-check surfaced seven genuine citations that were entirely missing — [[戦艦]] (battleship), [[軍艦]] (warship), [[母艦]] (mother ship), [[潜水艦]] (submarine), [[航空母艦]] (aircraft carrier), [[旗艦]] (flagship), and [[駆逐艦]] (destroyer) — alongside the already-listed stand-in [[艦船]] (added its missing tag; also corrected an initial ruby-reading guess for it after verifying against the word's own frontmatter). Three grep hits ([[水位]], [[連合]], [[提督]]) confirmed false positives — none cite 艦 in their own `characters:` fields.

**Sibling-vs-derived check, correctly excluded**: a grep for `監` in `graphemic_classification` surfaced seven characters ([[塩 (char)|塩]], [[藍 (char)|藍]], [[㽉]], [[濫]], [[籃]], [[覧]], [[鑑]]) — all cite 監 directly as their own phonetic donor (siblings of 艦), not derivations of 艦 itself. None belong in Derived Characters. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 胆 (6233; 1427 characters remaining).

### 2026-08-09, iteration 1078 — [[characters/胆|胆]]

**`mc_id: 2315` verified correct as-is**: checked `CC 2000.md` line 332 and confirmed the traditional form 膽 sits at rank 2315 — the same "recorded under an alias spelling" pattern seen with [[湧 (char)|湧]]/涌, but here already correctly stored (no fix needed, unlike that earlier case).

**Classification corrected, a genuine bug not a sibling-substitute**: stored `graphemic_classification: 旦`. Wiktionary's etymology for 膽 names the phonetic component as 詹 (OC \*tjam), not 旦 — and checking 旦's own OC (\*taːns) confirmed it does NOT share a compatible reading with 詹 (different rime class and coda entirely, -aːn vs -am), ruling out the "acceptable same-OC substitute" exception used elsewhere this backlog. Corrected to `詹` (no character page exists for it in this vault, left as plain text). Re-ran the Derived Characters grep under the corrected value: the four characters previously surfaced by the old `旦` value ([[但 (char)|但]], [[亶]], [[坦]], [[担]]) are unrelated to 胆 entirely once the bug is fixed — none cite 詹, so Derived Characters is empty.

**`korean_native` corrected, unrelated-word bug**: stored `옷 벗을` ("to take off clothes" — a modifier form of 옷을 벗다, with no discernible connection to "gall bladder/bravery," likely a copy-paste error from an unrelated page). Korean Wiktionary's literal hun is `쓸개` ("gall bladder") — replaced.

**Vietnamese contamination fixed**: stored `[đưỡn, đảm]`; Wiktionary confirms only `đảm`, with no support anywhere for `đưỡn` and no citing-word research to corroborate it. Trimmed.

Filled empty `pos` → `名詞`. **`## Notes` was a bare stub with a dangling `## Chengyu` heading and no `## Words` section** — rebuilt to the standard format, adding the missing stand-in [[胆嚢]] to a proper `## Words` section ahead of the already-present Chengyu entry. Three grep hits ([[臥]], [[六府]], [[臥平]]) confirmed false positives — 胆/膽 appears only in body-prose examples in each, not their own `characters:` fields. The existing [[臥薪嘗胆]] chengyu entry was re-confirmed genuine (胆 is a real constituent per that page's own frontmatter).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 緻 (6234; 1426 characters remaining).

### 2026-08-09, iteration 1079 — [[characters/緻|緻]]

**`mc_id: 4846` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 緻 appears in none of them.

**Classification researched, sibling-vs-true-donor kept as documented substitute**: Wiktionary names the precise phonetic component as 𦤶 (OC \*diɡs, an exact match to 緻's own reading), a rare character with no page in this vault — not the stored `致`. However, checked 致's own OC (\*tiɡs) and found it differs from 𦤶/緻 only by the expected regular voicing alternation (a very common Old Chinese active/passive-type pattern), and 致 is already documented as this page's own `aliases` entry with its own independent, fully-perfected character page ([[致 (char)|致]], perfected 2026-07-30, its own distinct `stand_in`). Given the near-identical OC and 致's ready availability and already-established alias relationship, kept `graphemic_classification: 致` as an acceptable substitute rather than pointing to the pageless, obscure 𦤶 — documented the nuance explicitly in the Notes rather than silently keeping it unexplained.

**Aliases relationship double-checked against "alias = parent form" expectations**: 緻 lists 致 as an alias, which would normally suggest 致 shouldn't be used independently — but 致's own page shows it fully independent (own `graphemic_classification: 至`, own `stand_in: 致`). Concluded this is the same 借代字 (documented substitute-character) pattern seen elsewhere this backlog (e.g. 脊/瘠+鶺, 遂/隧): 致 can graphemically substitute for 緻 in some compounds while also standing fully on its own — not a rule violation.

**`korean_native` corrected**: stored `빽빽할` (from 빽빽하다, "dense/packed") — a plausible-sounding but unattested gloss. Korean Wiktionary's literal hun is `배다` (context: closely-packed/permeated, matching the "closely-woven fabric" sense) — replaced to match the actual source.

Confirmed `pos: 性詞` was already correctly filled (no change needed — first character processed this backlog to arrive with `pos` already set). **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the missing "(stand-in for 緻)" tag to the sole genuine citation, [[精緻]]. **Chengyu**: no hits. **Derived Characters**: none (the only `graphemic_classification: 致` hit was 緻's own self-match).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 蔑 (char) (6235; 1425 characters remaining).

### 2026-08-09, iteration 1080 — [[characters/蔑 (char)|蔑]]

**`mc_id: 2221` verified correct as-is**: checked `CC 2000.md` line 234, confirmed 蔑 itself sits at that rank — another clean pass, no off-by-one. **Classification confirmed**: `graphemic_classification: 會意` matches Wiktionary exactly (𦰋 "person" + 戈 "dagger-axe," a weapon striking a person's leg — "to obliterate," extended to "scorn"; no character page exists for 𦰋 in this vault). Noted that the `radical: 艸` field is a Kangxi dictionary-indexing radical only, unrelated to the true 會意 components — didn't force a spurious semantic link to it in the Notes.

**Vietnamese reconciled against Wiktionary's differentiated Hán Việt/Nôm split**: stored `[miết, miệt, mít, mút, mệt, mốt, một, vạt]` (8 values). Wiktionary explicitly separates Sino-Vietnamese (`miệt, vạt`) from Nôm (`miết, một, mốt, mét, mệt, mít, mết`) — `mút` appears in neither list with no citing-word research to corroborate it (removed), while `mét` and `mết` were both missing (added). Result: `[miệt, vạt, miết, một, mốt, mét, mệt, mít, mết]`, matching the source's full 9-reading list exactly.

Filled `korean_native: ''` → `업신여길`, matching Wiktionary's literal printed hun (업신여길 멸) exactly. Filled empty `pos` → `事詞`.

**`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the missing "(stand-in for 蔑)" tag to the sole genuine citation, [[蔑]] — whose own word page carried the recurring `vietnamese: null` corruption bug, fixed to `miệt` (the Sino-Vietnamese reading specific to the "scorn" sense this word glosses, as opposed to `vạt`'s unrelated "garment flap" sense). One grep hit on [[軽視]] confirmed a false positive (蔑 appears only in body-prose example text "蔑視," not its own `characters:` field). **`## Derived Characters` was entirely missing despite a genuine hit**: [[襪]] ("sock, stocking") cites 蔑 directly as its own `graphemic_classification` — added. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 腫 (6236; 1424 characters remaining).

### 2026-08-09, iteration 1081 — [[characters/腫|腫]]

**mc_id off-by-one fixed**: stored `1862` (actually 協) → actual rank in `CC 1000.md` line 900 is `1863`. **Classification confirmed**: `graphemic_classification: 重` matches Wiktionary's 形聲 analysis (semantic 肉 "flesh" + phonetic 重). **Vietnamese** `[sõng, sũng, thuỗn, thõng, thũng, thủng]` confirmed as an exact match to Wiktionary's six-reading Sino-Vietnamese list (just different ordering), no contamination.

**`korean_native` corrected**: stored `종기` — itself Sino-Korean (腫氣), not a native gloss. Korean Wiktionary's literal printed hun is `부스럼` ("boil, sore" — a genuine native word) — replaced.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format.

**Sibling-vs-derived check, correctly excluded**: a grep for `重` in `graphemic_classification` surfaced six characters ([[動 (char)|動]], [[衝 (char)|衝]], [[鍾 (char)|鍾]], [[種]], [[童]], [[董]]) — all cite 重 directly as their own phonetic donor (siblings of 腫), not derivations of 腫 itself. None belong in Derived Characters. Added the missing "(stand-in for 腫)" tag to the existing [[腫瘍]] entry. One grep hit on [[膨脹]] confirmed a false positive — 腫 appears only inside that word's own cross-reference note about [[脹]]'s `stand_in` (腫脹), not as a constituent of 膨脹 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 剖 (6237; 1423 characters remaining).

### 2026-08-09, iteration 1082 — [[characters/剖|剖]]

**mc_id off-by-one fixed**: stored `2119` (actually 觴) → actual rank in `CC 2000.md` line 129 is `2120`. **Classification confirmed**: `graphemic_classification: 咅` matches Wiktionary's 形聲 analysis (semantic 刂/刀 "knife" + phonetic 咅).

**Vietnamese corrected**: stored `[bõ, mổ, phẫu]`. Wiktionary's Hán Nôm list is `[phẩu, bo, mổ, phẫu]` — `bõ` was a diacritic transcription error for `bo` (re-verified with a second verbatim quote to rule out a fetch mistake), and `phẩu` was missing entirely. Corrected to match the source exactly.

**`korean_native` citation-form fix**: stored `쪼갤` (adnominal form) — Korean Wiktionary's literal printed hun is the infinitive-pair `쪼개다, 가르다` ("to split, to divide") — replaced to match exactly, keeping both glosses per the multi-word `korean_native` precedent used elsewhere in this vault.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format.

**Sibling-vs-derived check, correctly excluded**: a grep for `咅` in `graphemic_classification` surfaced six characters ([[倍 (char)|倍]], [[培]], [[菩]], [[賠]], [[部 (char)|部]], [[陪 (char)|陪]]) — all cite 咅 directly as their own phonetic donor (siblings of 剖), not derivations of 剖 itself. None belong in Derived Characters. Added the missing "(stand-in for 剖)" tag to the existing [[解剖]] entry. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 股 (char) (6238; 1422 characters remaining).

### 2026-08-09, iteration 1083 — [[characters/股 (char)|股]]

**mc_id off-by-one fixed**: stored `1484` (actually 箕) → actual rank in `CC 1000.md` line 505 is `1485`.

**Classification researched in depth, confirmed correct as stored**: Wiktionary's own account is unusually explicit here — 股 was originally written 夃 (OC \*kaːʔ, "thigh," no page in this vault), whose form later graphically corrupted into something resembling [[殳]], with [[肉]] added as a semantic determiner. Shuowen (the classical dictionary) mistakenly analyzed the result as 形聲 (semantic 肉 + phonetic 殳), but modern scholarship explicitly rejects this since 殳 is only a graphic descendant of 夃, never a genuine sound-bearing phonetic. The vault's stored `graphemic_classification: 會意` already matches the scholarly-correct account, not Shuowen's outdated one — documented this history in the Notes rewrite so a future pass doesn't "fix" it back to 形聲/殳.

**Vietnamese** `[cổ, cỗ]` and **`korean_native: 넓적다리`** both confirmed as exact matches to Wiktionary/Korean Wiktionary, no fixes needed.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[股]] and the previously-unlisted [[溝股]] ("Pythagorean Theorem," already confirmed genuine during [[溝 (char)|溝]]'s own iteration earlier this backlog). While there, fixed the recurring `vietnamese: null` corruption on [[股]]'s own word page, replacing it with the primary confirmed reading `cổ`. Five grep hits ([[錮]], [[奔騰]], [[数学]], [[募集]], [[鼓]]) confirmed false positives — none cite 股 in their own `characters:` fields. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 縫 (6240; 1421 characters remaining).

### 2026-08-09, iteration 1084 — [[characters/縫|縫]]

**mc_id off-by-one fixed**: stored `3131` (actually 謨) → actual rank in `CC 3000.md` line 141 is `3132`. **Classification confirmed**: `graphemic_classification: 逢` matches Wiktionary's 形聲 analysis (semantic 糸 "thread" + phonetic 逢).

**Vietnamese expanded**: stored `[phùng]`, confirmed correct. A Hán Việt dictionary lookup surfaced a second attested reading, `phúng` — the noun "seam" sense, cleanly corresponding to the character's own two Middle Chinese readings (bjowng "to sew" vs. bjowngH "a seam") — added.

**`korean_native` citation-form fix**: stored `꿰맬` (adnominal form, missing the second gloss) — Korean Wiktionary's literal printed hun is the two-verb infinitive pair `꿰매다, 깁다` ("to sew, to mend") — replaced to match exactly.

Confirmed `pos: 事詞` was already correctly filled (no change needed). **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 1 to 2**: added the previously-missing [[裁縫]] ("tailor clothing") alongside the already-listed stand-in [[縫製]]. **Sibling-vs-derived check, correctly excluded**: [[蓬]] cites 逢 directly as its own phonetic donor (a sibling of 縫), not a derivation of 縫 itself — excluded from Derived Characters. **Chengyu**: re-confirmed the existing [[天衣無縫]] entry as genuine (縫 is a real constituent per that idiom's own `characters:` field).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 泡 (6242; 1420 characters remaining).

### 2026-08-09, iteration 1085 — [[characters/泡|泡]]

**`mc_id: 6321` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 泡 appears in none of them. **Classification confirmed**: `graphemic_classification: 包` matches Wiktionary's 形聲 analysis (semantic 水 "water" + phonetic 包). **`korean_native: 거품`** confirmed as an exact match to Korean Wiktionary's printed hun (거품 포).

**Vietnamese contamination fixed**: stored `[bào, bàu, bầu]`. A Hán Việt dictionary lookup (hvdic.thivien.net) documents exactly three readings for 泡 — `bào` (the customary/most common reading, per an explicit dictionary usage note), `phao`, and `pháo` — with no support anywhere for `bàu` or `bầu`, and no citing-word research to corroborate them either (the sole citation, [[泡沫]], doesn't fill in Vietnamese at all). Replaced to match the dictionary's three-reading list.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 泡)" tag to the sole genuine citation, [[泡沫]].

**Sibling-vs-derived check, correctly excluded**: a grep for `包` in `graphemic_classification` surfaced eight characters ([[飽 (char)|飽]], [[鞄 (char)|鞄]], [[鮑 (char)|鮑]], [[抱]], [[疱]], [[砲]], [[胞]], [[跑]]) — all cite 包 directly as their own phonetic donor (siblings of 泡), not derivations of 泡 itself. None belong in Derived Characters. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 溶 (6243; 1419 characters remaining).

### 2026-08-09, iteration 1086 — [[characters/溶|溶]]

**`mc_id: 4080` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 溶 nor its aliases 熔/鎔 appears in any of them. **Classification confirmed**: `graphemic_classification: 容` matches Wiktionary's 形聲 analysis (semantic 水 "water" + phonetic 容).

**Vietnamese contamination fixed**: stored `[dung, giong, ròng]`. Wiktionary confirms only `dung`, with no support anywhere for `giong` or `ròng` and no citing-word research to corroborate them (checked all three existing citations — [[溶化]], [[溶融]], [[溶岩]] — none fill in Vietnamese for the character itself). Trimmed to `[dung]`.

**`korean_native` citation-form fix**: stored `녹을` (adnominal, single gloss) — Korean Wiktionary's literal printed hun is the two-part infinitive `녹다, 질펀히 흐르다` ("to melt/dissolve, to flow in a mushy manner") — replaced to match exactly.

Filled empty `pos` → `事詞`. **`## Notes` was a bare stub with two dangling word-links** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 2 to 4**: added the missing stand-in [[溶化]] and a previously-unlisted genuine citation, [[溶液]] ("solution," chemistry), alongside the already-present [[溶融]] and [[溶岩]]. Three grep hits ([[抽出]], [[冶錬]], [[容易]]) confirmed false positives — none cite 溶 in their own `characters:` fields. **Chengyu**: no hits. **Derived Characters**: none (the only `graphemic_classification: 容` hit was 溶's own self-match).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 窟 (char) (6244; 1418 characters remaining).

### 2026-08-09, iteration 1087 — [[characters/窟 (char)|窟]]

**mc_id off-by-one fixed**: stored `3629` (actually 繅) → actual rank in `CC 3000.md` line 659 is `3630`. **Classification confirmed**: `graphemic_classification: 屈` matches Wiktionary's 形聲 analysis (semantic 穴 "hole, cave" + phonetic 屈). **Vietnamese** `[quật]` confirmed as the sole Hán Việt reading, no contamination.

**`korean`/`korean_native` both `굴` re-verified as intentional, not a duplication bug**: Korean Wiktionary's own eumhun template literally prints both the hun and eum as `굴 굴` — a rare but genuine case where the native Korean word for "cave" happens to coincide exactly with the character's Sino-Korean on-reading (parallel to the [[痕]] case earlier this backlog, where an apparent duplicate turned out to be exactly what the source printed).

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format.

**`## Words` expanded from 1 to 3**: added the reflexive stand-in [[窟]] and a previously-missing genuine citation, [[巣窟]] ("den, hangout"), alongside the already-listed [[洞窟]]. Two grep hits ([[洞穴]], [[巣穴]]) confirmed false positives — both cite the visually-similar 穴, not 窟. **Sibling-vs-derived check, correctly excluded**: [[掘 (char)|掘]] and [[堀]] both cite 屈 directly as their own phonetic donor (siblings of 窟), not derivations of 窟 itself — excluded from Derived Characters. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 駄 (char) (6245; 1417 characters remaining).

### 2026-08-09, iteration 1088 — [[characters/駄 (char)|駄]]

**Resolved a long-standing open question flagged on the page**: the Notes stub read only "WTF Shinjitai?" — researched and confirmed 駄 is not a modern Japan-only invention: Wiktionary explicitly states it is a genuine ancient Chinese variant of the traditional form 馱, just now serving as the standard Japanese shinjitai. Replaced the flag with this sourced answer, on both the character page and the identical stray note found on the citing word page [[駄]] (word).

**`mc_id: 8588` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 駄 nor its alias 馱 appears in any of them.

**Sibling-vs-true-donor, corrected in favor of the true donor**: stored `graphemic_classification: 大`. 駄's own Wiktionary etymology names the phonetic component as 太 specifically (OC \*tʰaːds) — though the traditional form 馱's separate Wiktionary entry names 大 instead (OC \*daːds), the two accounts are effectively describing the same near-identical reading (太 is itself a graphic differentiation of 大, differing only by the regular voicing alternation). Since 駄's own direct, specific etymology names 太, and 太 has its own well-documented character page in this vault, corrected `graphemic_classification` to `太` rather than the less-precise 大, following the same true-donor-over-sibling preference used for [[湧 (char)|湧]] (勇→甬) and [[胆]] (旦→詹) earlier this backlog.

**Vietnamese filled from the documented alias/parent form**: the field was completely empty. 駄's own Wiktionary page provided no Vietnamese data, but its alias 馱's page confirmed two readings, `đà` and `thồ` — filled in via the established alias-inheritance convention, since 駄 and 馱 are graphic variants of the same word.

**`korean_native: 실을` left as-is, unconfirmed**: no Korean Wiktionary page exists for 駄 at all (confirmed via a direct language-section check), so there was no source to verify or correct this pre-existing value against — left untouched per the omit-don't-fabricate policy (nothing to fabricate a replacement from, and no contrary evidence to remove it).

Filled empty `pos` → `事詞` and empty `boundedness` → `90` (matching the pattern for other characters whose sole genuine citation is a reflexive self-stand-in word, e.g. [[辣 (char)|辣]], [[溝 (char)|溝]]).

**`## Notes` rebuilt** to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 駄)" tag to the sole genuine citation, [[駄]] (word) — whose own page also carried the recurring `vietnamese: null` corruption, fixed to `thồ` (the reading specific to "carrying a pack," matching this word's exact sense). Two grep hits ([[舵]], [[一刻千金]]) confirmed false positives — 駄/馱 appears only in a homophone-callout cross-reference and a body-prose example ("無駄"), not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[汰]] cites 太 directly as its own phonetic donor (now a sibling of 駄 under the corrected classification), not a derivation of 駄 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 遮 (6246; 1416 characters remaining).

### 2026-08-09, iteration 1089 — [[characters/遮|遮]]

**mc_id off-by-one fixed**: stored `2258` (actually 遯) → actual rank in `CC 2000.md` line 272 is `2259`. **Classification confirmed**: `graphemic_classification: 庶` matches Wiktionary's 形聲 analysis (semantic 辵 "to move" + phonetic 庶).

**Vietnamese contamination fixed**: stored `[dà, già]`. A Hán Việt dictionary lookup (hvdic.thivien.net) confirms only a single reading, `già`, with no support anywhere for `dà` and no citing-word research to corroborate it (the sole citation, [[遮蔽]], doesn't fill in Vietnamese). Trimmed to `[già]`.

**`korean_native: 가릴` left as-is, unconfirmed**: repeated attempts to fetch the Korean 훈음 section for 遮 (via English Wiktionary and a direct ko.wiktionary lookup, which 404'd) were unsuccessful — the source page consistently truncates before the Korean section. Left the pre-existing value untouched rather than guess at a replacement with no source either confirming or contradicting it.

Filled empty `pos` → `事詞` (matching the stand-in word [[遮蔽]]'s own `事詞`). **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 遮)" tag to the existing [[遮蔽]] entry. Three grep hits ([[某物]], [[夜]], [[陽傘]]) confirmed false positives — none cite 遮 in their own `characters:` fields. **Sibling-vs-derived check, correctly excluded**: [[度]] and [[蹠]] both cite 庶 directly as their own phonetic donor (siblings of 遮), not derivations of 遮 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 紋 (char) (6247; 1415 characters remaining).

### 2026-08-09, iteration 1090 — [[characters/紋 (char)|紋]]

**`mc_id: 7695` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 紋 nor its alias 纹 appears in any of them. **Classification confirmed**: `graphemic_classification: 文` matches Wiktionary's 形聲 analysis (semantic 糸 "thread" + phonetic 文). **Vietnamese** `[vân, văn, vằn, vện]` and **`korean_native: 무늬`** both confirmed as exact matches to Wiktionary/Korean Wiktionary, no fixes needed. Confirmed `pos: 名詞` was already correctly filled.

**`## Notes` was informal prose (not the standard bulleted format) with unlinked references and no SKIP/Stroke/levels bullets** — rebuilt to the standard 4-bullet format, preserving the useful content about compound-specific senses (指紋 "fingerprint," 声紋 "voice signature") within the etymology bullet rather than losing it.

**`## Words`**: added the missing reflexive stand-in [[紋]] (word) alongside the already-listed [[皺紋]] ("wrinkles"). Its own word page carried the recurring `vietnamese: null` corruption bug — fixed to `văn`, the reading paralleling 文's own. Two grep hits ([[夜叉]], [[縦縞]]) confirmed false positives — neither cites 紋 in its own `characters:` field. **Chengyu**: no hits. **Derived Characters**: none (no character cites 紋 itself as `graphemic_classification`).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 籠 (char) (6248; 1414 characters remaining).

### 2026-08-09, iteration 1091 — [[characters/籠 (char)|籠]]

**mc_id off-by-one fixed**: stored `2733` (actually 煙) → actual rank in `CC 2000.md` line 767 is `2734`. **Classification confirmed**: `graphemic_classification: 龍` matches Wiktionary's 形聲 analysis (semantic 竹 "bamboo" + phonetic 龍).

**Vietnamese heavily contaminated, reconciled against a differentiated dictionary source**: stored `[lung, luông, luồng, lồng, rong, ruồng, trông]` (7 values). A Hán Việt dictionary (hvdic.thivien.net) explicitly separates classical Hán Việt (`lung, lộng`) from Nôm loans (`lồng, luông, ruồng`) — only `lung`, `luông`, `lồng`, and `ruồng` from the stored list survive; `luồng`, `rong`, and `trông` have no support anywhere, and `lộng` was missing entirely. Replaced with the dictionary's full five-reading list: `[lung, lộng, lồng, luông, ruồng]`.

**`korean_native` corrected after resolving conflicting fetch results**: stored `대바구니` ("bamboo basket" — plausible but unconfirmed). After several inconsistent attempts to pin down the literal Korean Wiktionary source, one direct fetch of the ko.wiktionary page itself returned a specific eumhun gloss, `농, 새장` ("cage, birdcage") — replaced to match, following the established practice of trusting a literal-source hit over a plausible-sounding guess, even where (as with [[窟 (char)|窟]] earlier this backlog) the result is unusual (here, the hun `농` happens to coincide with one of the character's own eum readings).

**`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 1 to 4**: added the reflexive stand-in [[籠]] and two previously-missing genuine citations, [[鳥籠]] ("birdcage") and [[灯籠]] ("lantern"), alongside the already-listed [[籠球]] ("basketball"). **Sibling-vs-derived check, correctly excluded**: a grep for `龍` in `graphemic_classification` surfaced six characters ([[寵]], [[瀧]], [[聾]], [[朧]], [[龐]], [[龔]]) — all cite 龍 directly as their own phonetic donor (siblings of 籠), not derivations of 籠 itself. None belong in Derived Characters. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 窯 (char) (6249; 1413 characters remaining).

### 2026-08-09, iteration 1092 — [[characters/窯 (char)|窯]]

**`mc_id: 6273` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 窯 nor its aliases 窑/窰 appears in any of them.

**Classification researched, competing-but-equivalent phonetic accounts, kept as documented**: 窯's own Wiktionary etymology names phonetic 羔 (OC \*kluː, no character page in this vault), but the stored value 䍃 (OC \*law per its own page) is nearly OC-identical and has independent textual support — 䍃's own Wiktionary entry explicitly lists 窰 (this page's own alias) among its derived characters. Since [[䍃]] already has a fully-documented character page in this vault and 羔 does not, kept `graphemic_classification: 䍃` and documented the alternate 羔 account in the Notes rather than switching to a pageless reference.

**Vietnamese expanded**: stored `[dao]`, confirmed correct. A Hán Việt dictionary lookup surfaced a second reading, `diêu` (explicitly noted as "also read as Diêu," prominent in compounds like 窯子) — added.

Filled `korean_native: ""` → `가마, 오지그릇`, matching Korean Wiktionary's literal printed hun ("kiln, earthenware") exactly. Filled empty `pos` → `名詞`.

**`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[窯]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `dao`. One grep hit on [[石灰]] confirmed a false positive (窯 appears only in body-prose example text "石灰窯," not its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: [[揺 (char)|揺]], [[謡]], [[遥]] all cite 䍃 directly as their own phonetic donor (siblings of 窯), not derivations of 窯 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 沸 (6250; 1412 characters remaining).

### 2026-08-09, iteration 1093 — [[characters/沸|沸]]

**mc_id off-by-one fixed**: stored `2344` (actually 銷) → actual rank in `CC 2000.md` line 362 is `2345`. **Classification confirmed**: `graphemic_classification: 弗` matches Wiktionary's 形聲 analysis (semantic 水 "water" + phonetic 弗). **Vietnamese** `[phí, phất]` confirmed as an exact match to Wiktionary's Hán Việt list, no contamination.

**`korean` field double-checked, no bug found**: an initial English-Wiktionary summary suggested two sound readings ("비, 불"), which would have meant a missing value — but a direct ko.wiktionary fetch confirmed only one genuine sound reading, `비` (matching what was already stored), and the "불" was an artifact of the summarization rather than a real second reading.

**`korean_native` citation-form fix**: stored `끓을` (adnominal form) — Korean Wiktionary's literal printed hun is the infinitive `끓다` ("to boil") — replaced to match exactly.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the missing "(stand-in for 沸)" tag to the sole genuine citation, [[煮沸]]. **Sibling-vs-derived check, correctly excluded**: a grep for `弗` in `graphemic_classification` surfaced four characters ([[佛 (char)|佛]], [[拂 (char)|拂]], [[費 (char)|費]], [[彿]]) — all cite 弗 directly as their own phonetic donor (siblings of 沸), not derivations of 沸 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 掲 (char) (6251; 1411 characters remaining).

### 2026-08-09, iteration 1094 — [[characters/掲 (char)|掲]]

**`mc_id: 2472` verified correct as-is**: checked `CC 2000.md` line 493 and confirmed the traditional form 揭 sits at that rank — another "recorded under an alias" clean pass, no fix needed.

**Classification corrected, the same known bug pattern found again**: stored `graphemic_classification: 喝`. This is the identical glyph-confusion already caught and fixed on [[謁 (char)|謁]] earlier this backlog: 喝 is itself phono-semantic on phonetic 曷 (OC \*ɡaːd), making it a sibling rather than a true donor, and its own OC (\*qraːds/\*qʰoːb/\*qʰaːd) doesn't match 揭's attested family (\*kad, \*ɡad, \*kʰrad, etc.) nearly as well as 曷 does directly. Corrected to `曷` (no character page in this vault), reusing the exact phrasing convention established on 謁's own page for this same 喝-vs-曷 distinction.

**Vietnamese filled from empty**: 揭's own Wiktionary page confirms a single reading, `yết` — added.

**`korean_native` formatting fix**: `높이들` (missing a space) → `높이 들`, matching the literal spacing of Korean Wiktionary's printed eumhun ("높이 들 게"). Filled empty `boundedness` → `90` (matching the single-reflexive-citation pattern used for [[辣 (char)|辣]], [[溝 (char)|溝]], [[窯 (char)|窯]] earlier this backlog).

**`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[掲]] (word) — whose own page carried *two* corruption bugs at once: the recurring `vietnamese: null` (fixed to `yết`) and a literal-string `korean: "null"` (fixed to `게`, matching the character's own confirmed reading). One grep hit on [[尊王攘夷]] confirmed a false positive (掲 appears only in body-prose example text "掲げた," not the idiom's own citation). **Sibling-vs-derived check, correctly excluded**: [[蝎 (char)|蝎]], [[褐 (char)|褐]], [[謁 (char)|謁]], [[渇 (char)|渇]] all cite 曷 directly as their own phonetic donor (siblings of 掲 under the corrected classification), not derivations of 掲 itself.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 唆 (6252; 1410 characters remaining).

### 2026-08-09, iteration 1095 — [[characters/唆|唆]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, 唆 appears in none of them. **Classification confirmed**: `graphemic_classification: 夋` matches Wiktionary's 形聲 analysis (semantic 口 "mouth" + phonetic 夋). **Vietnamese** `[toa]` confirmed as the sole reading, no contamination.

**`korean_native` citation-form fix**: stored `부추길` (adnominal, single gloss) — Korean Wiktionary's literal printed hun is the two-verb infinitive pair `부추기다, 꼬드기다` ("to incite, to instigate") — replaced to match exactly.

Filled empty `pos` → `事詞`. **Section order was malformed** (`## Words` appeared before a bare `# Notes` stub) — rebuilt into the standard order and 4-bullet Notes format. Added the missing "(stand-in for 唆)" tag to the existing [[教唆]] entry. **Sibling-vs-derived check, correctly excluded**: [[酸 (char)|酸]], [[俊]], [[峻]] all cite 夋 directly as their own phonetic donor (siblings of 唆), not derivations of 唆 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 遭 (6253; 1409 characters remaining).

### 2026-08-09, iteration 1096 — [[characters/遭|遭]]

**`mc_id: 1100` verified correct as-is**: checked `CC 1000.md` line 105, confirmed 遭 itself sits at that rank — a clean pass, no off-by-one. **Classification confirmed**: `graphemic_classification: 曹` matches Wiktionary's 形聲 analysis (semantic 辵 "to move" + phonetic 曹). **Vietnamese** `[tao]` and **`korean_native: 만날`** both confirmed as exact matches to Wiktionary/Korean Wiktionary, no fixes needed.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 遭)" tag to the existing [[遭遇]] entry. Two grep hits ([[挫折]], [[剣生剣死]]) confirmed false positives — 遭 appears only in body-prose example text in each ("遭受挫折," "終遭反噬"), not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[槽]], [[漕]], [[糟]] all cite 曹 directly as their own phonetic donor (siblings of 遭), not derivations of 遭 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 頑 (6254; 1408 characters remaining).

### 2026-08-09, iteration 1097 — [[characters/頑|頑]]

**mc_id off-by-one fixed**: stored `2589` (actually 壑) → actual rank in `CC 2000.md` line 615 is `2590`. **Classification confirmed**: `graphemic_classification: 元` matches Wiktionary's 形聲 analysis (semantic 頁 "head" + phonetic 元).

**Vietnamese contamination fixed, directly flagged by the source**: stored `[ngoan, ngoãn]`. Wiktionary explicitly labels `ngoãn` as unrelated/spurious (the linked page doesn't exist) — removed, leaving `[ngoan]`. **`korean_native: 완고할`** confirmed as an exact match to Korean Wiktionary's printed hun, no fix needed.

Filled empty `pos` → `性詞` (matching the stand-in word [[頑固]]'s own `性詞`). **Section order was malformed** (a bare `# Notes` stub followed by an unheaded `## Words`) — rebuilt into the standard order and 4-bullet Notes format. Added the missing "(stand-in for 頑)" tag to the existing [[頑固]] entry. One grep hit on [[珠投猪前]] confirmed a false positive (頑 appears only inside a classical-quotation body text, not the idiom's own citation). **Sibling-vs-derived check, correctly excluded**: [[冠]], [[完]], [[玩]], [[翫]], [[阮]] all cite 元 directly as their own phonetic donor (siblings of 頑), not derivations of 頑 itself.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 療 (6255; 1407 characters remaining).

### 2026-08-09, iteration 1098 — [[characters/療|療]]

**mc_id off-by-one fixed**: stored `3564` (actually 叫) → actual rank in `CC 3000.md` line 590 is `3565`. **Classification confirmed**: `graphemic_classification: 尞` matches Wiktionary's 形聲 analysis (semantic 疒 "sickness" + phonetic 尞). **`korean_native: 고칠`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese contamination fixed**: stored `[liệu, rệu]`. Wiktionary confirms only `liệu`, and the citing word [[治療]]'s own compound reading ("trị liệu") corroborates it as the standard form — no support anywhere for `rệu`. Trimmed to `[liệu]`.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 療)" tag to the existing [[治療]] entry. Two grep hits ([[医学]], [[普及]]) confirmed false positives — 療 appears only in body-prose compound examples ("医療," "普及医療") in each, not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[僚]], [[寮]], [[瞭]], [[遼]] all cite 尞 directly as their own phonetic donor (siblings of 療), not derivations of 療 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 畳 (char) (6256; 1406 characters remaining).

### 2026-08-09, iteration 1099 — [[characters/畳 (char)|畳]]

**`mc_id: 3563` verified correct as-is**: checked `CC 3000.md` line 588 and confirmed the traditional form 疊 sits at that rank — another "recorded under an alias" clean pass, no fix needed. **Classification confirmed**: `graphemic_classification: 會意` matches Wiktionary exactly (畾 "piled-up fields" + 宜, "to pile up, stack"; no character page exists for 畾 in this vault, though [[宜]] has one). Noted that `radical: 田` is a Kangxi dictionary-indexing radical only (畾 contains 田 three times), not one of the true 會意 components — didn't force a spurious link to it in the Notes.

**Vietnamese filled from empty**: added `[điệp, đệp, xếp]` per Wiktionary's combined Hán Việt/Nôm list.

**`korean_native` corrected, unrelated-word bug**: stored `거듭` ("repeatedly, again" — a plausible-sounding but unrelated adverb). Korean Wiktionary's literal printed hun gives two glosses, `겹치다, 포개다` ("to overlap/stack," "to pile up") — replaced to match the actual meaning.

**Completed a reciprocal homophone callout**: [[喋]] (already perfected) explicitly flagged that it shares its reading (덥/ㄉㄝㄆ) with [[畳]] and that "the reciprocal half of this callout will be completed when it comes up" — added the matching `>[!warning] Homophones` callout to the word page [[畳]] now that its turn arrived. While there, fixed that same word page's two corruption bugs: `vietnamese: null` → `điệp` and literal-string `korean: "null"` → `첩`.

Confirmed `pos: 名詞` was already correctly filled (matches the vault's chosen primary sense, the Japanese "tatami mat" noun, even though the character's pan-Chinese core sense is more verb-like "to overlap/stack" — left as-is, a deliberate prior choice, not a bug). Filled empty `boundedness` → `75`.

**`## Notes` was a bare two-link stub with an unheaded `## Words`** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[畳]] (word) alongside the already-listed [[折畳]] and [[重畳]]. Two grep hits ([[単字]], [[合成]]) confirmed false positives — neither cites 畳 in its own `characters:` field. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 駐 (6257; 1405 characters remaining).

### 2026-08-09, iteration 1100 — [[characters/駐|駐]]

**`mc_id: 4039` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 駐 nor its alias 驻 appears in any of them. **Classification confirmed**: `graphemic_classification: 主` matches Wiktionary's 形聲 analysis (semantic 馬 "horse" + phonetic 主). **Vietnamese** `[trú]` and **`korean_native: 머무를`** both confirmed as exact matches to Wiktionary, no fixes needed.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 駐)" tag to the existing [[駐屯]] entry. One grep hit on [[某処]] confirmed a false positive (駐 appears only in body-prose example text "駐紮," not its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: [[柱 (char)|柱]], [[住]], [[注]] all cite 主 directly as their own phonetic donor (siblings of 駐), not derivations of 駐 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`. Iteration 1100 milestone reached.

Next never-perfected character by `danayo_id`: 奥 (char) (6258; 1404 characters remaining).

### 2026-08-09, iteration 1101 — [[characters/奥 (char)|奥]]

**`mc_id: 2369` verified correct as-is**: checked `CC 2000.md` line 386, confirmed the traditional form 奧 sits at that rank.

**Classification corrected, a genuine error matching neither of the two documented accounts**: stored `graphemic_classification: 象形` (pictographic) — but Wiktionary gives only two competing analyses for 奧, and neither is 象形: the accepted modern one is 會意 (匊 "rice" + 𠬞 "hands," concealing/storing rice in a house), while Shuowen's alternate 形聲 reading is explicitly flagged as "not widely accepted." Corrected to `會意`. This is independently corroborated by the already-perfected word page [[奥]] (2026-08-02), whose own etymology prose describes "the character shows hands setting something down inside 宀 'roof'" — the same hands+enclosure composition.

**Vietnamese** `[áo]` and **`korean_native: 깊을`** both confirmed as exact matches to Wiktionary, no fixes needed (already correctly filled; `pos: 性詞` also already correct).

**`## Notes`/`## Words` were malformed** (Notes contained a dangling word-link, Words came after it with no heading separation) — rebuilt into proper order and the standard 4-bullet Notes format. **`## Words` expanded from 3 to 6**: added the reflexive stand-in [[奥]] and a previously-missing genuine citation, [[深奥]] ("abstruse"), alongside the three already-listed ([[奥秘]], [[奥門]], [[奥斯曼]], [[奥加素]]; also removed a redundant duplicate "abbreviation for oganesson" line for [[奥加素]] that repeated the entry immediately above it). Nine grep hits (the periodic-table words [[羅倫金]], [[田納素]], [[莫斯素]], [[居里金]], [[愛因金]], [[丹金]], [[柏克金]], [[西博金]], [[美洲金]], plus [[臼]]) confirmed false positives — none cite 奥/奧 in their own `characters:` fields (likely matched via cross-references to 奥加素/oganesson in body prose). One chengyu hit ([[切磋琢磨]]) also a false positive (奧 appears only inside the classical citation title 淇奧, not the idiom's own citation).

**`## Derived Characters` was entirely missing despite a genuine hit**: [[襖]] ("coat, jacket") cites 奧 (this page's alias) directly as its own `graphemic_classification` — added.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 捨 (char) (6259; 1403 characters remaining).

### 2026-08-09, iteration 1102 — [[characters/捨 (char)|捨]]

**mc_id off-by-one fixed**: stored `2581` (actually 竦) → actual rank in `CC 2000.md` line 607 is `2582`. **Classification confirmed, spelling variant not a bug**: Wiktionary names phonetic 舍, while this page stores 舎 — but these are just traditional/shinjitai script variants of the identical character (same OC, same everything), and [[舎]] (not 舍) is the one with a dedicated page in this vault, matching the vault's established shinjitai-preference convention (cf. [[駄 (char)|駄]] earlier this backlog). No change needed. **Vietnamese** `[xả]` confirmed as the sole reading, no contamination.

**`korean_native` citation-form fix**: stored `버릴` (adnominal, single gloss) — Korean Wiktionary's literal printed hun is the two-verb infinitive pair `버리다, 베풀다` ("to discard/abandon, to bestow/offer") — replaced to match exactly.

**`joyo_level: "6"` double-checked, not a field-swap bug**: this looked unusual next to `hanmun_edu_level: 高等` (most characters processed this backlog show `joyo_level: 高等` instead), but the checklist confirms `"1"`–`"6"` are legitimate Kyōiku-kanji grade values, distinct from `高等` (Jōyō-Kōtō) — 捨 is simply taught earlier in Japan (grade-school Kyōiku kanji) than most characters seen this stretch. Used the correct `[Jōyō - Kyōiku]` and `[Korean HS]` lookup links in the levels bullet accordingly (verified both pages exist), rather than the more common `Jōyō - Kōtō`/`Korean Name` links used elsewhere.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words` expanded from 0 to 2**: added the reflexive stand-in [[捨]] and a previously-missing genuine citation, [[四捨五入]] ("rounding"). A broad grep for 捨/舍/舎 surfaced many false positives ([[宿舎]], [[寄宿舎]], [[校舎]], [[精舎]], [[夫]], [[卸]]) that all cite the phonetic donor 舎 itself (or are unrelated), not 捨 — carefully isolated by checking each word's own `characters:` field specifically for 捨 rather than trusting the raw grep. Five chengyu hits ([[勿貪隣物]], [[色即是空]], [[阿鼻叫喚]], [[鼠世桃源]], [[舎本逐末]]) likewise all confirmed false positives on the same basis. **Derived Characters**: none (no character cites 捨 itself as `graphemic_classification`).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 賃 (char) (6260; 1402 characters remaining).

### 2026-08-09, iteration 1103 — [[characters/賃 (char)|賃]]

**`mc_id: 4278` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 賃 nor its alias 赁 appears in any of them. **Classification confirmed**: `graphemic_classification: 任` matches Wiktionary's 形聲 analysis (semantic 貝 "shell, money" + phonetic 任). **Vietnamese** `[nhẫm]` confirmed as the sole reading, no contamination.

**`korean_native` expanded**: stored `품삯` ("wages," half of the full citation) — Korean Wiktionary's literal printed hun combines two glosses, `품을 팔다, 품삯` ("to sell one's labor, wages") — expanded to include both.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[賃]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `nhẫm`. One grep hit on [[俸給]] confirmed a false positive (賃 appears only in body-prose example text "賃金," not its own `characters:` field). **Chengyu**: no hits. **Derived Characters**: none (no character cites 賃 itself as `graphemic_classification`).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 絹 (char) (6261; 1401 characters remaining).

### 2026-08-09, iteration 1104 — [[characters/絹 (char)|絹]]

**mc_id off-by-one fixed**: stored `3982` (actually 詿) → actual rank in `CC 3000.md` line 1024 is `3983`.

**Classification corrected, a genuine glyph-confusion bug**: stored `graphemic_classification: 月`. Wiktionary names the true phonetic component as 肙 (OC \*qʷeːns, closely matching 絹's own \*kʷens) — 月's own OC (\*ŋod) shares nothing with either, ruling out any same-OC-substitute exception. This is the same kind of visual-corruption bug already caught twice this backlog (謁 and 掲, both 喝→曷): the modern printed form of 肙 happens to resemble 月, but they're unrelated. Corrected to `肙` (no character page in this vault).

**Vietnamese expanded**: stored `[quyến]` — Wiktionary confirms both `quyên` and `quyến` as Sino-Vietnamese readings; added the missing `quyên`.

**`korean_native` corrected to match the literal source**: stored `명주` (itself Sino-Korean 明紬, "silk") — Korean Wiktionary's literal printed hun is `비단` (Sino-Korean 匹緞, "silk fabric/satin"). Both are Sino-Korean-derived (no purely native Korean word for silk exists, similar to the [[窟 (char)|窟]]/[[痕]] pattern), but only `비단` matches what's actually printed — replaced.

Filled empty `pos` → `名詞`. Confirmed `hsk_level: 無` is a distinct, valid sentinel from empty-string (264 other characters share it) — used the `[HSK No]` lookup link accordingly. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[絹]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `quyến`. Three grep hits ([[糸線]], [[圏]], [[倉鼠]]) confirmed false positives — none cite 絹 in their own `characters:` fields. **Chengyu**: no hits. **Derived Characters**: none — re-checked under the corrected `肙` value specifically (not the old, buggy `月`), confirming no other character in this vault cites it.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 搭 (6263; 1400 characters remaining).

### 2026-08-09, iteration 1105 — [[characters/搭|搭]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, 搭 appears in none of them. **Classification confirmed**: `graphemic_classification: 荅` matches Wiktionary's 形聲 analysis (semantic 手 "hand" + phonetic 荅).

**Vietnamese contamination fixed**: stored `[ráp, tháp, thắp, đáp, đắp]` (5 values). A Hán Việt dictionary (hvdic.thivien.net) confirms only two genuine Sino-Vietnamese readings, `tháp` and `đáp`, with no support anywhere for `ráp`, `thắp`, or `đắp`, and neither citing word ([[搭乗]], [[搭載]]) offers corroborating research. Trimmed to `[tháp, đáp]`.

**`korean_native: 탈` left as-is, unconfirmed**: no Wiktionary Korean data could be located for 搭 (the ko.wiktionary page has no 훈/음 section for it at all) — left the pre-existing value untouched per the omit-don't-fabricate policy, same as [[駄 (char)|駄]]'s and [[遮]]'s unconfirmed fields earlier this backlog.

Filled empty `pos` → `事詞`. **`## Notes` had a dangling word-link mixed into the stub** — rebuilt to the standard 4-bullet format (using `[Korean Missing]` since `hanmun_edu_level: 無`).

**`## Words`**: added the missing "(stand-in for 搭)" tag to [[搭乗]] and added the previously-missing [[搭載]]. **Flagging a likely duplicate word pair for the word-sweep**: [[搭乘]] (not yet perfected) appears to be a near-exact duplicate of the already-perfected [[搭乗]] — same reading (tabsung/탑숭), same gloss, and 搭乘 even lists 搭乗 as its own alias, but 乗/乘 are just shinjitai/traditional script variants of the identical character, so these look like two separate pages for what should be one word (parallel to the [[雰囲]]/[[雰囲気]] situation flagged earlier in this backlog, though that pair turned out to be genuinely distinct — this one looks like a straightforward duplicate). Left both untouched as out of scope for character-page perfecting; only counted [[搭乗]] toward this page's `## Words`. One chengyu hit ([[一刀両断]]) confirmed a false positive (搭 appears only in body-prose text "粘粘搭搭," not the idiom's own citation). **Sibling-vs-derived check, correctly excluded**: [[塔 (char)|塔]] cites 荅 directly as its own phonetic donor (a sibling of 搭), not a derivation of 搭 itself.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 棒 (6264; 1399 characters remaining).

### 2026-08-09, iteration 1106 — [[characters/棒|棒]]

**`mc_id: 4346` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 棒 nor its alias 棓 appears in any of them. **Classification confirmed**: `graphemic_classification: 奉` matches Wiktionary's 形聲 analysis (semantic 木 "wood" + phonetic 奉). **`cranberry` tag re-verified**: `stand_in: 棍棒` — checked [[棍]]'s own `stand_in` field and confirmed it's also `棍棒`, satisfying transitivity.

**Vietnamese contamination fixed**: stored `[búng, bọng, bổng, bộng, vóng, vổng]` (6 values). Wiktionary's list is `[vổng, bọng, bộng, bổng, búng]` — `vóng` has no support anywhere (distinct from the confirmed `vổng`), and no citing-word research corroborates it. Trimmed to the confirmed five.

**`korean_native` corrected**: stored `막대` ("stick, rod" — plausible but unattested). Korean Wiktionary's literal printed hun is `몽둥이` ("club, cudgel") — replaced to match the actual source.

Confirmed `pos: 名詞` was already correctly filled. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format, adding the missing "(stand-in for 棒)" tag and cranberry note to the existing [[棍棒]] entry. **Sibling-vs-derived check, correctly excluded**: [[捧 (char)|捧]] and [[俸]] both cite 奉 directly as their own phonetic donor (siblings of 棒), not derivations of 棒 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 絵 (6265; 1398 characters remaining).

### 2026-08-09, iteration 1107 — [[characters/絵|絵]]

**`mc_id: 5213` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 絵 nor its alias 繪 appears in any of them. **Classification value normalized to match vault convention**: stored `graphemic_classification: 會` (traditional) pointed to a page that doesn't exist under that name — the vault's actual page is the shinjitai form [[会 (char)|会]] (confirmed same character: mandarin huì, korean 회). Corrected the field to `会` to match, following the same shinjitai-preference precedent as [[捨 (char)|捨]]/舎 and [[駄 (char)|駄]]/太 earlier this backlog. **`korean_native: 그림`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese contamination fixed**: stored `[gói, gối]`. Wiktionary's Hán Nôm list is `[hội, gói, cởi]` — `gối` has no support anywhere (distinct from the confirmed `cởi`), and `hội` was missing entirely. Corrected to match the source: `[hội, gói, cởi]`.

Filled empty `pos` → `事詞` and empty `boundedness` → `90`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 絵)" tag to the existing [[絵画]] entry.

**Sibling-vs-derived check, methodology note**: an initial broad grep for `會`/`会` in `graphemic_classification` returned several hundred false positives, because it matched the type-name string `會意` as a substring on every 會意-classified character in the vault — re-ran with an exact-value anchor (`^graphemic_classification: "會"$` etc.) and found only [[桧]], a genuine sibling (also cites 会/會 directly), correctly excluded from Derived Characters. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 竟 (char) (6266; 1397 characters remaining).

### 2026-08-09, iteration 1108 — [[characters/竟 (char)|竟]]

**`mc_id: 1029` verified correct as-is**: checked `CC 1000.md` line 34, confirmed 竟 itself sits at that rank. **Classification confirmed**: `graphemic_classification: 會意` matches Wiktionary/Shuowen's analysis (音 "sound" + 儿 "person," "a person has finished speaking" → "to end, finish"). Noted `radical: 立` is a Kangxi dictionary-indexing radical only, unrelated to the true 會意 components. **`korean_native: 다할`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese expanded**: stored `[cánh, cạnh]` — Wiktionary's list adds a third reading, `giạnh`, missing from the stored set — added.

Filled empty `pos` → `副詞` (matching the stand-in word [[畢竟]]'s own `副詞` — an adverbial usage, distinct from most characters processed this backlog).

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format (using `[Hyōgai]`/`[Korean HS]` since `joyo_level: 表外字` and `hanmun_edu_level: 高等`). **`## Words`**: added the reflexive stand-in [[竟]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `cánh`. One grep hit on [[某事]] and one chengyu hit on [[安心立命]] both confirmed false positives (竟 appears only in body-prose example text in each, not either page's own `characters:` field).

**`## Derived Characters` was entirely missing despite two genuine hits**: using a precise exact-match grep this time (learning from last iteration's substring-match pitfall), found [[鏡 (char)|鏡]] ("mirror, lens") and [[境]] ("boundary, border") both cite 竟 directly as their own `graphemic_classification` — added both.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 碗 (char) (6267; 1396 characters remaining).

### 2026-08-09, iteration 1109 — [[characters/碗 (char)|碗]]

**`mc_id: 8239` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 碗 appears in none of them. **Classification confirmed**: `graphemic_classification: 宛` matches Wiktionary's 形聲 analysis (semantic 石 "stone" + phonetic 宛). **`korean_native: 사발`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese contamination fixed, directly flagged by the source**: stored `[oản, uyển]`. Wiktionary explicitly labels `uyển` as an unrelated/spurious, obsolete reading — removed, leaving `[oản]`.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[碗]] (word) — whose own page had an empty (not corrupted, just unfilled) `vietnamese` field, filled to `oản` to match the character's confirmed reading. **Sibling-vs-derived check, correctly excluded**: [[腕 (char)|腕]] and [[婉]] both cite 宛 directly as their own phonetic donor (siblings of 碗), not derivations of 碗 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 穿 (char) (6268; 1395 characters remaining).

### 2026-08-09, iteration 1110 — [[characters/穿 (char)|穿]]

**mc_id off-by-one fixed**: stored `1417` (actually 蘭) → actual rank in `CC 1000.md` line 439 is `1418`. **Classification confirmed**: `graphemic_classification: 會意` matches Wiktionary (穴 "cave" + 牙 "tooth," a tooth boring through; no character page exists for 牙's specific role here in this vault... actually [[牙]] itself may have a page but wasn't linked since it's the plain-radical sense — left as plain text per the pattern used for other pageless 會意 components this backlog).

**Vietnamese corrected, not just trimmed**: stored `[xoen, xuyên]` — `xoen` doesn't match anything in a Hán Việt dictionary lookup (hvdic.thivien.net), which instead confirms `[xuyên, xuyến]`. Replaced entirely to match the dictionary's two-reading list.

**`korean_native: 뚫을` left as-is, unconfirmed**: multiple attempts to retrieve a clean 훈음 citation from both English and Korean Wiktionary came back empty or garbled (one response conflated Korean hun-eum terminology with Japanese kun'yomi) — left the pre-existing value untouched, consistent with the omit-don't-fabricate policy applied to [[駄 (char)|駄]] and [[搭]] earlier this backlog.

Filled empty `pos` → `事詞`. **Notes/Words/Chengyu sections existed but in nonstandard compressed format** (single-line Notes with inline bullet separators, missing blank lines between sections) — reformatted to the standard 4-bullet Notes layout and properly spaced sections, adding readings to the previously bare [[穿山甲]]/[[穿孔机]] links and the missing stand-in [[穿]] (word) entry. Its own word page carried the recurring `vietnamese: null` corruption, fixed to `xuyên`. One additional chengyu grep hit, [[臨渇掘井]], confirmed a false positive (doesn't cite 穿 in its own `characters:` field) — the already-listed [[磨穿鉄硯]] re-confirmed genuine. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 禽 (6269; 1394 characters remaining).

### 2026-08-09, iteration 1111 — [[characters/禽|禽]]

**`mc_id: 933` verified correct as-is, with a formatting note**: initial grep attempts against `CC 0000.md` (ranks 1–1000) failed silently because that file uses a different blockquote list format (`> 933. 禽`) than the plain-numbered format (`933. 禽`) used in `CC 1000.md`–`CC 3000.md` — re-ran with the correct pattern and confirmed 禽 itself sits at rank 933. Worth remembering for future low-rank characters in this backlog. **Classification confirmed**: `graphemic_classification: 今` matches Wiktionary's 形聲 analysis (semantic 离, originally a net-pictogram + phonetic 今). **Vietnamese** `[cầm]` confirmed as the sole reading, no contamination.

**`korean_native` corrected**: stored `새` ("bird" — a common, plausible but unattested native word). Korean Wiktionary's literal printed hun is `날짐승` ("winged creature") — replaced to match exactly.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format, noting the character's semantic broadening from "net-caught animal" to "bird" specifically. **`## Words` expanded from 2 to 3**: added the missing "(stand-in for 禽)" tag to [[禽鳥]] and a previously-missing genuine citation, [[猛禽]] ("bird of prey"). Four grep hits ([[御術]], [[五馭]], [[鳥]], and chengyu [[波乱万丈]]) confirmed false positives — none cite 禽 in their own `characters:` fields. **Sibling-vs-derived check, correctly excluded**: [[金 (char)|金]], [[龕 (char)|龕]], [[貪 (char)|貪]], [[含]], [[吟]] all cite 今 directly as their own phonetic donor (siblings of 禽), not derivations of 禽 itself.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 播 (6270; 1393 characters remaining).

### 2026-08-09, iteration 1112 — [[characters/播|播]]

**`mc_id: 2132` verified correct as-is**: checked `CC 2000.md` line 141, confirmed 播 itself sits at that rank. **Classification confirmed**: `graphemic_classification: 番` matches Wiktionary's 形聲 analysis (semantic 手 "hand" + phonetic 番). **`korean_native: 뿌릴`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese contamination fixed**: stored `[bá, bạ, bớ, bợ, bứ, phăng, vá, vả, vớ]` (9 values). Wiktionary's list is `[vá, bá, bạ, phăng, vả, vớ, bợ]` — `bớ` and `bứ` have no support anywhere (distinct from the confirmed `bợ`), and no citing-word research corroborates them. Trimmed to the confirmed seven.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the missing "(stand-in for 播)" tag to [[播種]] and a previously-missing genuine citation, [[伝播]] ("propagate, disseminate," already perfected). One grep hit on [[放送局]] confirmed a false positive (播 appears only in body-prose example text "播送," not its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: [[翻 (char)|翻]], [[幡]], [[潘]], [[蕃]] all cite 番 directly as their own phonetic donor (siblings of 播), not derivations of 播 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 拐 (6273; 1392 characters remaining).

### 2026-08-09, iteration 1113 — [[characters/拐|拐]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, 拐 appears in none of them. **Classification confirmed**: `graphemic_classification: 冎` matches Wiktionary's 形聲 analysis (semantic 手 "hand" + phonetic 冎). **Vietnamese** `[quay, quày, quái, quải, quảy, quầy, quẩy]` confirmed as an exact match to Wiktionary's seven-reading list (just different ordering), no contamination.

**Resolved a long-standing open question flagged on the page**: the Notes stub read only "I'm shocked its not old" — researched and confirmed 拐 genuinely is an ancient character, with a pre-Middle-Chinese Old Chinese reconstruction (\*ɡʷroːlʔ), not a later coinage despite its modern-sounding "kidnap" sense. Replaced the flag with this sourced answer, the same resolution pattern used for [[駄 (char)|駄]]'s "WTF Shinjitai?" note earlier this backlog.

**`korean_native` corrected**: stored `후릴` (plausibly from 후리다, "to snatch away" — a reasonable guess but unattested). Korean Wiktionary's literal printed hun is `속일`/속이다 ("to deceive") — replaced.

Filled empty `pos` → `事詞`. **`## Notes` had the stray note mixed with dangling links** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 拐)" tag to the sole genuine citation, [[誘拐]]. One grep hit on [[骨]] confirmed a false positive (cites 冎 directly, not 拐 — a sibling, not this word). **Sibling-vs-derived check, correctly excluded**: [[骨 (char)|骨]] and [[咼]] both cite 冎 directly as their own phonetic donor (siblings of 拐), not derivations of 拐 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 圏 (char) (6274; 1391 characters remaining).

### 2026-08-09, iteration 1114 — [[characters/圏 (char)|圏]]

**mc_id off-by-one fixed**: stored `3578` (actually 尻) → actual rank in `CC 3000.md` line 604 is `3579` (recorded under the traditional form 圈). **Classification confirmed, shinjitai convention re-verified**: Wiktionary names phonetic 卷 (traditional), but this vault's dedicated page is the shinjitai [[巻 (char)|巻]] (confirmed same character: mandarin juàn, korean 권, danayo_id 3105) — matching the established shinjitai-preference pattern from [[捨 (char)|捨]]/舎, [[絵]]/会, [[駄 (char)|駄]]/太. No change needed.

**Vietnamese filled from empty**: added the full Wiktionary list `[khuyên, quyên, quyền, quyển, khoen]`. Noted that the already-perfected word page [[圏]] narrows to just `quyển` for its own specific abstract "zone/sphere" sense (distinguishing it from `khuyên`'s concrete "ring, circle" sense) — but since the character page covers the whole polysemous character rather than one word's narrow sense, kept the full source list here, consistent with how other polysemous characters were handled earlier this backlog (e.g. [[蔑 (char)|蔑]], [[棒]]).

**Completed a second reciprocal homophone callout while here**: [[圏]] (word)'s own notes already documented sharing its reading (gwen/권) with both [[巻]] and [[絹]], flagged as "awaiting their own turn" — but [[絹]] was already perfected in iteration 1104 without its own reciprocal added. Added the missing `>[!warning] Homophones` callout to [[絹]]'s page now (listing both [[圏]] and [[巻]]); [[巻]] itself remains unperfected so its own reciprocal is still pending.

`korean_native: 우리` confirmed as an exact match to Korean Wiktionary's printed hun (a homograph of the pronoun "we," here meaning "pen, enclosure"). Confirmed `pos: 名詞` was already correctly filled. Filled empty `boundedness` → `65`.

**`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words` expanded from 0 to 4**: added the reflexive stand-in [[圏]] and three previously-missing genuine citations — [[文化圏]] ("cultural sphere"), [[英語圏]] ("Anglosphere"), [[大気圏]] ("atmosphere"). Three grep hits ([[兜]], [[首都]], [[交遊]]) confirmed false positives — none cite 圏/圈 in their own `characters:` fields. **Sibling-vs-derived check, correctly excluded**: [[倦]] and [[拳]] both cite 巻 directly as their own phonetic donor (siblings of 圏), not derivations of 圏 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 噴 (6275; 1390 characters remaining).

### 2026-08-09, iteration 1115 — [[characters/噴|噴]]

**`mc_id: 5984` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 噴 nor its alias 喷 appears in any of them. **Classification confirmed**: `graphemic_classification: 賁` matches Wiktionary's 形聲 analysis (semantic 口 "mouth" + phonetic 賁). **`korean_native: 뿜을`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese contamination fixed**: stored `[phun, phùn, phún]`. Wiktionary's list is `[phun, phún, phôn]` — `phùn` has no support anywhere (distinct from the confirmed `phôn`), and no citing-word research corroborates it. Corrected to match the source exactly.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 噴)" tag to the sole genuine citation, [[噴火]]. **Sibling-vs-derived check, correctly excluded**: [[墳]] and [[奔]] both cite 賁 directly as their own phonetic donor (siblings of 噴), not derivations of 噴 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 嚇 (char) (6276; 1389 characters remaining).

### 2026-08-09, iteration 1116 — [[characters/嚇 (char)|嚇]]

**`mc_id: 5539` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 嚇 nor its alias 吓 appears in any of them. **Classification confirmed**: `graphemic_classification: 赫` matches Wiktionary's 形聲 analysis (semantic 口 "mouth" + phonetic 赫).

**Vietnamese and Korean cross-checked against the already-perfected word page's deep research**: Wiktionary's raw entry lists a second Vietnamese reading, `hạ` (flagged by Wiktionary itself as having "unconfirmed status"), and a second Korean reading, `혁`. The citing word [[嚇]] (word)'s own extensive prior research explicitly resolves both: `혁`/hyeok belongs to a completely different, unrelated "furious, rage" sense of the same graph (different Middle Chinese tone class) — not this page's "scare, frighten" sense — and makes no mention of `hạ` at all. Left `korean: 하` and `vietnamese: [hách]` untouched, trusting the deeper existing research over the raw Wiktionary list.

**`korean_native` — a demonstrably wrong value removed, not fixed**: stored `웃음소리` ("sound of laughter") — completely unrelated to either of 嚇's two documented senses (scare/threaten, or furious/rage). Unlike the "plausible but unconfirmed" fields left as-is elsewhere this backlog ([[駄 (char)|駄]], [[搭]], [[遮]]), this value is clearly wrong, not just unverified — but repeated attempts to find a replacement (ko.wiktionary 404s, no accessible Korean-language source) came up empty. Cleared the field to blank rather than either keep a known-wrong value or fabricate a replacement.

**`## Notes` was a bare stub with unlinked component names** — rebuilt to the standard 4-bullet format (both 口 and 赫 checked for character pages; only 口 has one). **`## Words`**: added the missing "(stand-in for 嚇)" tag to the sole genuine citation, [[嚇]] (word). **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 慌 (6277; 1388 characters remaining).

### 2026-08-09, iteration 1117 — [[characters/慌|慌]]

**`mc_id: 5617` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, 慌 appears in none of them. **Classification confirmed**: `graphemic_classification: 荒` matches Wiktionary's 形聲 analysis (semantic 心 "heart" + phonetic 荒). **Vietnamese** `[hoang, hoảng]` confirmed as an exact match to Wiktionary, no contamination.

**`korean_native: 어리둥절할` left as-is, unconfirmed**: no Korean Wiktionary page exists for 慌 (404), and the English Wiktionary entry gives only the sound reading with no hun — left the pre-existing (plausible, semantically apt) value untouched per the omit-don't-fabricate policy.

Filled empty `pos` → `性詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the missing "(stand-in for 慌)" tag to the sole genuine citation, [[恐慌]]. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 控 (6278; 1387 characters remaining).

### 2026-08-09, iteration 1118 — [[characters/控|控]]

**mc_id off-by-one fixed**: stored `3126` (actually 璣) → actual rank in `CC 3000.md` line 136 is `3127`. **Classification confirmed**: `graphemic_classification: 空` matches Wiktionary's 形聲 analysis (semantic 手 "hand" + phonetic 空).

**Vietnamese contamination fixed**: stored `[khống, xang]`. Wiktionary confirms only `khống`, with no support anywhere for `xang` and no citing-word research to corroborate it (the sole citation, [[控訴]], leaves Vietnamese unfilled). Trimmed to `[khống]`.

**`korean_native` expanded**: stored `당길` (adnominal, single gloss) — Korean Wiktionary's literal printed hun combines four glosses, `당기다, 고하다, 치다, 때리다` ("to pull, to inform, to strike, to hit") — expanded to include all four. **`korean: 공` left as the sole value**: Wiktionary lists a second reading, `강`, but with no documented sense-distinction to justify adding it (unlike the clear-cut cases like [[嚇 (char)|嚇]] where a citing word's own research explicitly separated two senses) — left as-is, matching the citing word [[控訴]]'s own `공소` reading.

**`## Notes` had unlinked component names mixed with a dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 控)" tag to the existing [[控訴]] entry. **Sibling-vs-derived check, correctly excluded**: [[腔]] cites 空 directly as its own phonetic donor (a sibling of 控), not a derivation of 控 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 款 (char) (6279; 1386 characters remaining).

### 2026-08-09, iteration 1119 — [[characters/款 (char)|款]]

**mc_id off-by-one fixed**: stored `2454` (actually 梅) → actual rank in `CC 2000.md` line 476 is `2455`.

**Classification corrected, a subtle etymology-conflation bug**: stored `graphemic_classification: 柰`, which Wiktionary's own prose does mention — but only as the phonetic of 款's *older, distinct ancestor character* 歀 (a different reading, kuài, "desire"), not of the modern 款 (kuǎn) itself. Shuowen's account for the actual modern character names phonetic 窾 (OC \*kʰloːnʔ), an exact match to 款's own reading — while 柰's OC (\*naːds) doesn't match 款 at all. The two accounts describe different characters that later graphically merged into one glyph. Corrected `graphemic_classification` to `窾` (no character page in this vault) and documented the conflation explicitly in the Notes so it isn't miscorrected back.

**Vietnamese** `[khoản]` and **`korean_native: 항목`** both confirmed as exact matches to Wiktionary/Korean Wiktionary, no fixes needed.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[款]] (word) — whose own page had an empty (unfilled, not corrupted) `vietnamese` field, filled to `khoản`. Three grep hits ([[償還]], [[踊躍]], and chengyu [[大同小異]]) confirmed false positives — 款 appears only in body-prose example text in each, not any of their own `characters:` fields. **Derived Characters**: none found under the corrected `窾` value.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 迅 (6280; 1385 characters remaining).

### 2026-08-09, iteration 1120 — [[characters/迅|迅]]

**mc_id off-by-one fixed**: stored `3296` (actually 訛) → actual rank in `CC 3000.md` line 310 is `3297`. **Classification confirmed**: `graphemic_classification: 卂` matches Wiktionary's 形聲 analysis (semantic 辵 "to move" + phonetic 卂, no character page exists for it in this vault). **Vietnamese** `[tấn]` confirmed via a Hán Việt dictionary lookup (Wiktionary's own page had no Vietnamese section at all), no contamination.

**`korean_native: 빠를` left as-is, unconfirmed**: no Korean Wiktionary page exists for 迅 (404) — left the pre-existing, semantically apt value untouched per the omit-don't-fabricate policy.

Filled empty `pos` → `性詞`. **Section order was malformed** (`## Words` appeared before the initials/finals links with no proper Notes heading) — rebuilt into the standard order and 4-bullet Notes format. Added the missing "(stand-in for 迅)" tag to the existing [[迅速]] entry. One grep hit on [[速様]] confirmed a false positive (doesn't cite 迅 in its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: [[虱 (char)|虱]] and [[訊]] both cite 卂 directly as their own phonetic donor (siblings of 迅), not derivations of 迅 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 鍵 (char) (6282; 1384 characters remaining).

### 2026-08-09, iteration 1121 — [[characters/鍵 (char)|鍵]]

**Spurious alias removed**: `aliases` included `騫`, but Wiktionary's own 鍵 entry makes no mention of any relationship to 騫 whatsoever (騫 is an unrelated classical word meaning "high, lofty" / "deficient"), 騫 has no character page of its own in this vault, and no citing word anywhere uses it. Notably, 騫 *does* appear at rank 1897 in `CC 1000.md` — but attributing that rank to 鍵 via a spurious alias would have been worse than leaving `mc_id` as an honest long-tail placeholder, so removed the alias rather than "importing" an unrelated character's frequency rank.

**`mc_id: 4371` confirmed genuine long-tail data** (re-verified after removing the spurious alias): grepped all four `CC 0000`–`CC 3000` files for 鍵/键 specifically, neither appears in any of them. **Classification confirmed**: `graphemic_classification: 建` matches Wiktionary's 形聲 analysis (semantic 金 "metal" + phonetic 建). **Vietnamese** `[kiện]` and **`korean_native: 열쇠`** both confirmed as exact matches to Wiktionary, no fixes needed.

**Completed a three-way reciprocal homophone callout**: [[見]] and [[乾]] (both already perfected) each explicitly flagged sharing their reading (gyen/견/ㄍ⼶ㄋ) with [[鍵]], "still awaiting its own turn" — added the matching `>[!warning] Homophones` callout to [[鍵]] (word) now, completing the three-way group. While there, fixed that same word page's recurring `vietnamese: null` corruption, replacing it with `kiện`.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words` expanded from 0 to 2**: added the reflexive stand-in [[鍵]] and a previously-missing genuine citation, [[鍵盤]] ("keyboard"). Two grep hits ([[見]], [[乾]]) were expected — both cite 鍵 only inside their own homophone callouts, not as constituents, already accounted for above. **Sibling-vs-derived check, correctly excluded**: [[健]] cites 建 directly as its own phonetic donor (a sibling of 鍵), not a derivation of 鍵 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 鍋 (char) (6283; 1383 characters remaining).

### 2026-08-09, iteration 1122 — [[characters/鍋 (char)|鍋]]

**`mc_id: 10623` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 鍋 nor its alias 锅 appears in any of them. **Classification confirmed**: `graphemic_classification: 咼` matches Wiktionary's 形聲 analysis (semantic 金 "metal" + phonetic 咼). **Vietnamese** `[oa]` confirmed as the sole reading, no contamination.

**`korean_native` corrected**: stored `노구솥` (a specific, plausible but unattested compound word for "portable cauldron"). Korean Wiktionary's literal printed hun is the two-gloss `솥, 냄비` ("cauldron, pan") — replaced to match exactly.

**Malformed markup cleaned up throughout**: the page had raw double-bracket wikilinks used for non-existent targets (`[[SKIP-1-8-9]]`, `[[Stroke 17]]`, `[[ㄍ⺢]]`) instead of proper markdown links to the actual lookup files, a malformed OC-notation bullet (stray unmatched parenthesis), and a non-standard tip-callout phrasing — all rebuilt to the standard format. Filled empty `pos` → `名詞`.

**`## Words`**: added the reflexive stand-in [[鍋]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `oa`. Two grep hits ([[鰌魚]], [[餃子]]) confirmed false positives — 鍋 appears only in body-prose example text in each ("柳川鍋," "鍋貼"), not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[過 (char)|過]], [[渦]], [[禍]], [[窩]], [[蝸]] all cite 咼 directly as their own phonetic donor (siblings of 鍋), not derivations of 鍋 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 舗 (char) (6284; 1382 characters remaining).

### 2026-08-09, iteration 1123 — [[characters/舗 (char)|舗]]

**`mc_id: 9626` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 舗 nor its aliases 舖/铺 appears in any of them. **Classification confirmed**: `graphemic_classification: 甫` matches Wiktionary's 形聲 analysis for the traditional form 舖 (semantic 舍 "house" + phonetic 甫); noted that this vault's shinjitai page graphically simplifies 舍 to resemble [[舌 (char)|舌]] (matching the stored `radical: 舌`), described both layers in the Notes.

**Vietnamese YAML corruption fixed**: stored as a single malformed scalar `"hô, phố, pho"` (comma-joined string, not a proper list) instead of a YAML list, and `hô` itself was a typo missing the leading consonant — Wiktionary confirms `[phô, phố, pho]`. Rebuilt as a proper list with the corrected spelling.

**`korean_native: 펼` left as-is, unconfirmed**: no Korean Wiktionary page exists for 舖 (404) — left the pre-existing, semantically plausible value (from 펼치다, "to spread out/display," a common conceptual root for "shop, stall") untouched per the omit-don't-fabricate policy.

Filled empty `boundedness` → `90` (matching the single-reflexive-citation, `#hapax`-tagged pattern used for similar characters this backlog). **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[舗]] (word) — whose own page had three separate bugs, all fixed: `羅馬字` was malformed as `poㄩ` (mixing romanization with a stray zhuyin character) → corrected to `pou`; `korean` was empty → filled to `포`; `vietnamese` was empty → filled to `phô`. Two grep hits ([[商店]], and chengyu [[瑠璃清天]]) confirmed false positives — neither cites 舗 in its own `characters:` field (the latter's body prose merely mentions a variant phrasing, 瑠璃舗天, in passing discussion; the idiom's own title and citations use 清, not 舗). **Sibling-vs-derived check, correctly excluded**: ten characters ([[捕 (char)|捕]], [[浦 (char)|浦]], [[傅]], [[圃]], [[哺]], [[尃]], [[溥]], [[補]], [[輔]], [[黼]]) all cite 甫 directly as their own phonetic donor (siblings of 舗), not derivations of 舗 itself.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 釣 (6285; 1381 characters remaining).

### 2026-08-09, iteration 1124 — [[characters/釣|釣]]

**mc_id off-by-one fixed**: stored `2243` (actually 釜) → actual rank in `CC 2000.md` line 257 is `2244`. **Classification confirmed**: `graphemic_classification: 勺` matches Wiktionary's 形聲 analysis (semantic 金 "metal" + phonetic 勺, no character page exists for it in this vault). **Vietnamese** `[điếu]` confirmed as the sole reading, no contamination.

**`korean_native` citation-form fix**: stored `낚시질할` (an elaborated adnominal form of 낚시질하다) — Korean Wiktionary's literal printed hun is the simpler base form `낚시` ("fishing") — replaced to match exactly.

Confirmed `pos: 事詞` was already correctly filled. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 釣)" tag to [[釣漁]], alongside the already-listed [[釣竿]]. **Sibling-vs-derived check, correctly excluded**: [[灼]], [[的]], [[約]], [[豹]], [[酌]] all cite 勺 directly as their own phonetic donor (siblings of 釣), not derivations of 釣 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 厘 (char) (6287; 1380 characters remaining).

### 2026-08-09, iteration 1125 — [[characters/厘 (char)|厘]]

**mc_id long-tail flag overturned — a real ranking exists**: stored `4376` looked like a standard long-tail sentinel, but grepping all four `CC 0000`–`CC 3000` files turned up the traditional form 釐 at rank 1517 in `CC 1000.md`. Verified via Wiktionary that 厘 is explicitly documented as "the simplified and variant traditional form of 釐" — a genuine same-word relationship (unlike the spurious 騫 alias caught on [[鍵 (char)|鍵]] a few iterations ago) — so corrected `mc_id` to `1517`.

**Classification cross-checked against two competing accounts, kept as stored**: 厘's own etymology names phonetic 里 (OC \*rɯʔ, an excellent match to 厘's own \*rɯ), while the fuller traditional-form 釐's etymology instead analyzes it as semantic 里 + phonetic 𠩺 (an obscure, pageless component). Since 里's OC fits either role well and is already the stored, well-documented value with its own character page, kept `graphemic_classification: 里` and documented both accounts in the Notes.

**Vietnamese** `[li, ly]` confirmed as an exact match to Wiktionary, no fixes needed. **`korean_native` filled from empty**: 釐's Etymology 1 hun-eum entry covers both this character's "centi-/measurement unit" sense and a separate "govern, manage" sense under one reading — filled with `다스릴`, the literal printed gloss.

**`pos` filled by cross-referencing the already-perfected stand-in word**: rather than guessing a category for this measure-prefix character, checked [[厘]] (word)'s own already-set `pos: 修飾語` ("modifier") and matched it, since a plain 名詞/事詞 guess would have been wrong for this kind of unit-prefix character.

**`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[厘]] (word). One grep hit on [[里 (char)|里]] (word) confirmed a false positive — it cites 厘 only inside its own homophone callout, not as a constituent (both [[厘]] and [[里 (char)|里]] (word) are part of an already-partially-documented three-way homophone group with [[浬]], which remains unperfected and out of scope here). **Sibling-vs-derived check, correctly excluded**: [[浬 (char)|浬]], [[狸 (char)|狸]], [[埋]], [[理]], [[裏]], [[鯉]] all cite 里 directly as their own phonetic donor (siblings of 厘), not derivations of 厘 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 酢 (6288; 1379 characters remaining).

### 2026-08-09, iteration 1126 — [[characters/酢|酢]]

**`mc_id: 3029` verified correct as-is**: checked `CC 3000.md` line 34, confirmed 酢 itself sits at that rank. **Classification confirmed**: `graphemic_classification: 乍` matches Wiktionary's 形聲 analysis (semantic 酉 "wine vessel" + phonetic 乍). **Vietnamese** `[thố, tạc]` confirmed as matching Wiktionary's list (just reordered), no contamination.

**Investigated an apparent korean/諺文 mismatch, concluded it's the expected `kwin: false` pattern, not a bug**: `korean: 초` didn't match the Dan'a'yo-derived `諺文: 작`/`羅馬字: jag`/`注音: ㄐㄚㄎ` at all — initially suspected a data-entry error. But cross-checking the citing word [[食酢]] showed the identical pattern (`korean: 식초` vs. its own Dan'a'yo `諺文: 식작`), and ko.wiktionary directly confirms `초` (hun `식초`, "vinegar") as the real modern Sino-Korean reading. This is the documented `kwin: false` case: Dan'a'yo's own systematically-derived reading (`작`, from the MC fanqie 在各切 directly) deliberately diverges from actual modern Korean pronunciation (`초`) — both fields are correct, just recording two different things by design.

**`korean_native` corrected, a duplicate-value bug (not the legitimate 痕/窟-style coincidence)**: stored `초` — merely repeating the sound reading rather than giving the gloss. ko.wiktionary's literal hun is `식초` ("vinegar," the actual Korean word) — replaced.

**Malformed CC-finals link fixed**: the raw wikilink `[[../lookup/CC/finals/韻 鈬開]]` used a relative-path prefix that doesn't belong in Obsidian link syntax. Verified `韻 鈬開.md` is this vault's own genuine (if non-standard-looking) filename for the checked-tone rhyme class Wiktionary calls 鐸 — not a typo needing correction to "鐸" — just rebuilt as a proper markdown link.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 酢)" tag to the sole genuine citation, [[食酢]]. **Sibling-vs-derived check, correctly excluded**: [[作 (char)|作]], [[昨 (char)|昨]], [[炸]], [[祚]], [[窄]], [[詐]] all cite 乍 directly as their own phonetic donor (siblings of 酢), not derivations of 酢 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 賠 (6289; 1378 characters remaining).

### 2026-08-09, iteration 1127 — [[characters/賠|賠]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, neither 賠 nor its alias 赔 appears in any of them. **Classification confirmed**: `graphemic_classification: 咅` matches Wiktionary's 形聲 analysis (semantic 貝 "shell, money" + phonetic 咅).

**Vietnamese contamination fixed**: stored `[bù, bồi]`. A Hán Việt dictionary lookup confirms only `bồi` as the standard reading, with no support anywhere for `bù`. Independently corroborated by a chance mention in [[駝背]]'s own prior research, which explicitly notes "bồi belongs to different characters entirely (賠, 陪, 培)" — confirming the association. Trimmed to `[bồi]`.

**`korean_native` normalized**: stored `물어줄` (no space) — Korean Wiktionary's literal printed hun has a space, `물어 줄` (물다 "to pay" + 주다 "to give") — normalized to match exactly.

Filled empty `pos` → `事詞` (matching the stand-in word [[賠償]]'s own `事詞`). **`## Notes` was a bare two-link stub with no `## Words` heading separation** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 賠)" tag to the existing [[賠償]] entry. Two grep hits ([[駝背]], [[報償]]) confirmed false positives — 賠 appears only in body-prose comparative discussion in each, not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[倍 (char)|倍]], [[部 (char)|部]], [[陪 (char)|陪]], [[剖]], [[培]], [[菩]] all cite 咅 directly as their own phonetic donor (siblings of 賠), not derivations of 賠 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 咽 (6290; 1377 characters remaining).

### 2026-08-09, iteration 1128 — [[characters/咽|咽]]

**mc_id off-by-one fixed**: stored `2275` (actually 梓) → actual rank in `CC 2000.md` line 289 is `2276`. **Classification confirmed**: `graphemic_classification: 因` matches Wiktionary's 形聲 analysis for the "throat" etymology (semantic 口 "mouth" + phonetic 因).

**Reading mismatch found and fixed — a genuine cross-sense bug**: 咽 is polysemous with distinct pronunciation-and-sense pairs (throat/인 vs. choke-sob/열), and this page's `english: pharynx` and (broken) `stand_in` both target the throat sense — yet `korean` was stored as `열`, the *other* etymology's reading. Confirmed via the already-perfected [[咽喉]] ("throat"), which uses `인` for 咽's own part. Corrected `korean: 열` → `인`, and filled the empty `korean_native` with the matching throat-sense hun, `목구멍`.

**Broken/phantom `stand_in` fixed**: `stand_in: 咽頭` pointed to a word file that doesn't exist anywhere in the vault. Repointed to [[咽喉]] (already perfected, genuinely cites 咽, and matches the character's own "throat/pharynx" sense).

**Vietnamese contamination fixed**: stored `[nhiết, nhăng, nhằn, yến, yết, ịt]` (6 values). Wiktionary confirms `[yết, nhằn, ịt, nhiết, yến]` — `nhăng` has no support anywhere (distinct from the confirmed `nhằn`), and is independently contradicted by [[咽喉]]'s own research, which specifically cites `yết` (not `nhăng`) as "咽's own yết variant reading." Removed.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format, explicitly noting the character's cross-sense polysemy so a future pass doesn't "fix" the reading back. **`## Words`**: the corrected stand-in [[咽喉]] plus a genuine second citation, [[嗚咽]] ("sob, whimper" — using the *other*, choke-sense etymology of this same polysemous character, left as-is since both senses are legitimately attested in this vault). **Sibling-vs-derived check, correctly excluded**: [[姻]] and [[恩]] both cite 因 directly as their own phonetic donor (siblings of 咽), not derivations of 咽 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 貼 (char) (6291; 1376 characters remaining).

### 2026-08-09, iteration 1129 — [[characters/貼 (char)|貼]]

**`mc_id: 5410` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 貼 nor its alias 贴 appears in any of them. **Classification confirmed**: `graphemic_classification: 占` matches Wiktionary's 形聲 analysis (semantic 貝 "shell, money" + phonetic 占). **`korean_native: 붙일`** confirmed as an exact match to Wiktionary's printed hun.

**Vietnamese expanded**: stored `[thiếp]`, confirmed correct as the primary Hán Việt reading. A Hán Việt dictionary lookup surfaced a second, explicitly-labeled genuine Nôm reading, `thiệt` — added.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[貼]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `thiếp`. One grep hit on [[餃子]] confirmed a false positive (貼 appears only in body-prose example text "鍋貼," not its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: eight characters ([[帖 (char)|帖]], [[点 (char)|点]], [[粘 (char)|粘]], [[鮎 (char)|鮎]], [[怗]], [[店]], [[砧]], [[站]]) all cite 占 directly as their own phonetic donor (siblings of 貼), not derivations of 貼 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 粗 (6292; 1375 characters remaining).

### 2026-08-09, iteration 1130 — [[characters/粗|粗]]

**mc_id off-by-one fixed**: stored `3008` (actually 貍) → actual rank in `CC 3000.md` line 14 is `3009`. **Classification confirmed**: `graphemic_classification: 且` matches Wiktionary's 形聲 analysis (semantic 米 "rice, grain" + phonetic 且). **Vietnamese** `[sồ, thô, to, xồ]` confirmed as an exact match to Wiktionary's list (just different ordering), no contamination.

**`korean_native` completeness fix**: stored `거칠` — an incomplete verb stem missing its final conjugation, not a standalone word. Korean Wiktionary's literal printed hun is the properly-conjugated adjectival form `거친` ("rough, coarse") — corrected.

Filled empty `pos` → `性詞`. **`## Notes` was a bare two-link stub with `## Words` unseparated** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 粗)" tag to the existing [[粗糙]] entry. **Sibling-vs-derived check, correctly excluded**: a grep for `且` in `graphemic_classification` surfaced nine characters ([[助]], [[査]], [[狙]], [[疽]], [[祖]], [[租]], [[組]], [[詛]], [[阻]]) — all cite 且 directly as their own phonetic donor (siblings of 粗), not derivations of 粗 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 猫 (char) (6293; 1374 characters remaining).

### 2026-08-09, iteration 1131 — [[characters/猫 (char)|猫]]

**`mc_id: 6393` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 猫 nor its alias 貓 appears in any of them. **Classification confirmed**: `graphemic_classification: 苗` matches Wiktionary's 形聲 analysis (semantic 犬 "dog, animal" + phonetic 苗). **`korean_native: 고양이`** confirmed as an exact match to Wiktionary's printed hun.

**`japanese_native` corrected, a genuine on'yomi/kun'yomi mix-up**: stored `びょう` — but this is actually one of the character's own *on'yomi* readings (Kan-on びょう), not a native kun'yomi reading at all. Wiktionary confirms the true kun'yomi is `ねこ` (neko, "cat") — corrected, independently corroborated by the already-perfected stand-in word [[猫]] (word), whose own `japanese: ねこ` field already had it right.

**Vietnamese expanded**: stored `[mèo, meo]` (both genuine Nôm readings) — Wiktionary also lists a Hán Việt reading, `miêu`, missing from the stored set — added.

**`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 2 to 3**: added the missing "(stand-in for 猫)" tag to the reflexive [[猫]] (word) entry and a previously-missing genuine citation, [[熊猫]] ("panda"). One grep hit on [[匹]] confirmed a false positive (猫 appears only in body-prose example text "二匹の猫," not its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: [[描]] cites 苗 directly as its own phonetic donor (a sibling of 猫), not a derivation of 猫 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 粘 (char) (6294; 1373 characters remaining).

### 2026-08-09, iteration 1132 — [[characters/粘 (char)|粘]]

**`mc_id: 8493` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 粘 nor its alias 黏 appears in any of them. **Classification confirmed**: `graphemic_classification: 占` matches Wiktionary's 形聲 analysis (semantic 米 "rice" + phonetic 占). **`korean_native: 붙을`** confirmed as an exact match to Wiktionary's printed hun.

**Vietnamese expanded**: stored `[chiêm, dính, niêm]` (all three genuine). Wiktionary's Hán Việt/Nôm split additionally lists `rơm` and `nem` as documented (not spurious-flagged) Nôm readings — added both, matching the full five-reading source list.

Confirmed `pos: 性詞` was already correctly filled. **`## Notes` had unlinked component names mixed with a dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[粘]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `niêm`. One chengyu hit ([[一刀両断]]) confirmed a false positive (粘 appears only in body-prose text "粘粘搭搭," not the idiom's own citation — the same body-prose line already excluded during [[搭]]'s own iteration). **Sibling-vs-derived check, correctly excluded**: eight characters ([[帖 (char)|帖]], [[貼 (char)|貼]], [[点 (char)|点]], [[鮎 (char)|鮎]], [[店]], [[怗]], [[砧]], [[站]]) all cite 占 directly as their own phonetic donor (siblings of 粘), not derivations of 粘 itself.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 滑 (char) (6295; 1372 characters remaining).

### 2026-08-09, iteration 1133 — [[characters/滑 (char)|滑]]

**`mc_id: 1496` verified correct as-is**: checked `CC 1000.md` line 517, confirmed 滑 itself sits at that rank. **Classification confirmed**: `graphemic_classification: 骨` matches Wiktionary's 形聲 analysis (semantic 水 "water" + phonetic 骨).

**Vietnamese deliberately left untouched after checking prior research**: Wiktionary's raw list is `[gột, cốt, hoạt]`, which would normally suggest expanding the stored `[hoạt]` — but the already-perfected word page [[滑]] explicitly documents having *removed* `gột` in a prior pass, since it belongs to 滑's other, unrelated "chaotic, comical" sense (Korean 골, not this sense's 활) rather than the "slippery" sense this page covers. Left as `[hoạt]`, matching that deliberate prior narrowing rather than reintroducing the cross-sense reading.

**`korean`/`korean_native` cross-checked against the same cross-sense split, confirmed already correct**: 滑 has two Korean readings for two different senses (활 "slippery" vs. 골 "comical") — the stored `활`/`미끄러울` already correctly match the "slippery" sense (독립적으로 corroborated by [[滑]] (word)'s own prior fix, which explicitly corrected `골`→`활` for the same reason). No change needed.

**`japanese_native` YAML corruption fixed**: stored as a malformed two-item list, `すべ` and `すべ-る` (the verb すべる apparently split across two list entries) — collapsed to the single correct value `すべる`, confirmed as the intended reading by [[滑]] (word)'s own notes ("Japanese uses the native kun'yomi verb 滑る (すべる)").

**Malformed markup cleaned up throughout**: relative-path links (`../lookup/...`), a redundant duplicate initials/finals line, and raw un-rendered wikilinks below the visible Notes bullets — all consolidated into the standard 4-bullet format with proper vault-root-relative links.

**`## Words` expanded from 1 to 3**: added the reflexive stand-in [[滑]] (word) and a previously-missing genuine citation, [[滑鼠]] ("mouse, computer"), alongside the already-listed [[狡猾]]. One grep hit on [[唉]] confirmed a false positive (滑 appears only in unrelated body-prose discussion, not its own `characters:` field). **Derived Characters**: none (no character cites 滑 itself as `graphemic_classification`). **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 託 (6296; 1371 characters remaining).

### 2026-08-09, iteration 1134 — [[characters/託|託]]

**`mc_id: 1267` verified correct as-is**: checked `CC 1000.md` line 280, confirmed 託 itself sits at that rank. **Classification corrected, a clear-cut error**: stored `graphemic_classification: 象形` (pictographic) — but 託 is unambiguously 形聲 per Wiktionary (semantic 言 "speech" + phonetic 乇, OC \*l̥ʰaːɡ), with no pictographic account offered anywhere; 象形 doesn't fit a phono-semantic compound at all. Corrected to `乇` (no character page in this vault). **Vietnamese** `[thác]` confirmed as the sole reading, no contamination.

**`korean_native` corrected, an unrelated-word bug**: stored `밀` (from 밀다, "to push" — no connection to "entrust, request" at all). Korean Wiktionary's literal printed hun is `부탁하다` ("to request, ask a favor") — replaced.

**`## Notes`/`## Words` were in reversed order with a malformed relative-path link** — rebuilt into the standard order and 4-bullet format (confirmed `韻 鈬開.md` is this vault's genuine filename, per the precedent established during [[酢]]'s own iteration, not a typo). **`## Words` expanded from 2 to 3**: added the missing "(stand-in for 託)" tag and a previously-missing genuine citation, [[委託]] ("entrust, trust"), alongside the already-listed [[嘱託]] and [[受託]]. One grep hit on [[受賞]] confirmed a false positive (託 appears only in body-prose discussion of a different word series, not its own `characters:` field). **Sibling-vs-derived check, correctly excluded**: [[宅]] cites 乇 directly as its own phonetic donor (a sibling of 託), not a derivation of 託 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 袖 (char) (6297; 1370 characters remaining).

### 2026-08-09, iteration 1135 — [[characters/袖 (char)|袖]]

**mc_id off-by-one fixed**: stored `2775` (actually 途) → actual rank in `CC 2000.md` line 809 is `2776`. **Classification confirmed**: `graphemic_classification: 由` matches Wiktionary's 形聲 analysis (semantic 衣 "clothing" + phonetic 由). **Vietnamese** `[tụ]` confirmed via a Hán Việt dictionary lookup (Wiktionary's own page had no Vietnamese data) and **`korean_native: 소매`** confirmed via a direct ko.wiktionary fetch (Wiktionary's combined page had no Korean data either) — both already correct, no fixes needed.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[袖]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `tụ`. **Sibling-vs-derived check, correctly excluded**: [[宙 (char)|宙]], [[油 (char)|油]], [[軸]], [[抽]], [[紬]], [[笛]], [[釉]], [[迪]] all cite 由 directly as their own phonetic donor (siblings of 袖), not derivations of 袖 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 醒 (6298; 1369 characters remaining).

### 2026-08-09, iteration 1136 — [[characters/醒|醒]]

**mc_id off-by-one fixed**: stored `3676` (actually 黷) → actual rank in `CC 3000.md` line 706 is `3677`. **Classification confirmed**: `graphemic_classification: 星` matches Wiktionary's 形聲 analysis (semantic 酉 "wine" + phonetic 星). **`korean_native: 깰`** confirmed as an exact match to Wiktionary's printed hun.

**Vietnamese contamination fixed**: stored `[tảnh, tỉnh]`. Wiktionary confirms only `tỉnh` (Sino-Vietnamese), with no support anywhere for `tảnh`. Trimmed.

**Broken/phantom `stand_in` fixed**: `stand_in: 清醒` pointed to a word file that doesn't exist anywhere in the vault. Repointed to [[覚醒]] ("sober up, awaken"), the genuine citing word found via a full grep sweep.

Filled empty `pos` → `性詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the corrected stand-in [[覚醒]]. One grep hit on [[星 (char)|星]] confirmed a non-issue — it's the reverse relationship, already correctly documented (星's own Derived Characters section lists 醒 as a child, not a citation of 醒 citing 星 as a word constituent). Two chengyu hits ([[一目瞭然]], [[諸行無常]]) confirmed false positives — 醒 appears only inside a classical book-title citation and unrelated body prose respectively, not either idiom's own citation. **Derived Characters**: none (no character cites 醒 itself as `graphemic_classification`).

Stamped `date-last-perfect: 2026-08-09`.

Next never-perfected character by `danayo_id`: 傘 (6300; 1368 characters remaining).

### 2026-08-10, iteration 1137 — [[characters/傘|傘]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, neither 傘 nor its alias 伞 appears in any of them. **Classification confirmed**: `graphemic_classification: 象形` matches Wiktionary (a pictogram of an open umbrella); noted `radical: 人` is a Kangxi dictionary-indexing radical only, not a compositional element of the pictogram.

**Vietnamese contamination fixed**: stored `[tàn, tán, tản]`. A Hán Việt dictionary confirms only `[tán, tản]`, with no support anywhere for `tàn` — independently corroborated by the stand-in word [[雨傘]]'s own `vietnamese: vũ tản`, which uses `tản`, not `tàn`. Trimmed. **`korean_native: 우산`** confirmed as an exact match to Korean Wiktionary's printed hun (itself Sino-Korean-derived, matching the [[痕]]/[[窟 (char)|窟]] pattern of legitimate Sino-Korean hun citations).

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words` expanded from 0 to 3**: added the stand-in [[雨傘]] and two previously-missing genuine citations, [[落下傘]] ("parachute") and [[陽傘]] ("parasol"). Confirmed two grep hits ([[折畳]], [[落下]]) as false positives — 傘 appears only in body-prose compound examples in each, not either page's own `characters:` field. Noted in passing (no action needed): [[山]] (word)'s own research already documents 傘 as one of six characters (刪, 傘, 散, 産, 珊, 山) sharing the identical Dan'a'yo/Korean syllable ㄙㄚㄋ/산 — none besides 山 have standalone word pages, so no reciprocal homophone callout applies here. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 縄 (char) (6301; 1367 characters remaining).

### 2026-08-10, iteration 1138 — [[characters/縄 (char)|縄]]

**`mc_id: 1339` verified correct as-is**: checked `CC 1000.md` line 356, confirmed the traditional form 繩 sits at that rank. **Classification confirmed**: `graphemic_classification: 黽` matches Wiktionary's 形聲 analysis (semantic 糸 "thread" + phonetic 黽, no character page in this vault).

**Cross-language field-mixing bug found and fixed**: `korean_native` was stored as `なわ` — which is Japanese (nawa, a kun'yomi reading), not Korean at all. Meanwhile `japanese_native` held a malformed two-item list, `[ただ, なわ]`, where `ただ` turned out to be a truncated fragment of a second genuine kun'yomi reading. Fetching 縄's own Japanese section confirmed both true kun'yomi readings are `なわ` and `ただす` — reassigned `japanese_native` to the proper list `[なわ, ただす]` (fixing the truncation), and filled `korean_native` with the actual Korean hun, `노끈` ("rope, cord"), confirmed via a direct ko.wiktionary fetch.

**Vietnamese YAML corruption fixed**: stored as a single malformed comma-joined scalar, `"thằng, thừng, xằng"`. A Hán Việt dictionary lookup confirms only `thằng` as the reading for this "rope" sense (a second reading, `mẫn`, belongs to a distinct "careful, meticulous" sense and was not carried over); `thừng` turned out to be a word appearing *inside* the dictionary's own definition text for `thằng` ("dây thừng," rope) rather than a separate attested reading, and `xằng` has no support anywhere. Rebuilt as a clean single-item list.

**Cleaned up an orphaned scratch note**: `[[Radical 205]] is part of it` was leftover shorthand (黽 is Kangxi radical 205) from an earlier partial edit — replaced with the standard 4-bullet Notes format incorporating that fact properly. Filled empty `boundedness` → `90`.

**`## Words`**: added the reflexive stand-in [[縄]] (word) — whose own page had an empty (unfilled, not corrupted) `vietnamese` field, filled to `thằng`. Two grep hits ([[条]], [[書契]]) confirmed false positives — 縄/繩 appears only in body-prose classifier/historical examples in each, not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[蝿]] cites 黽 directly as its own phonetic donor (a sibling of 縄), not a derivation of 縄 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 繊 (6302; 1366 characters remaining).

### 2026-08-10, iteration 1139 — [[characters/繊|繊]]

**`mc_id: 2343` verified correct as-is**: checked `CC 2000.md` line 360, confirmed the traditional form 纖 sits at that rank. **Classification confirmed**: `graphemic_classification: 韱` matches Wiktionary's 形聲 analysis (semantic 糸 "thread, silk" + phonetic 韱, no character page in this vault). **`korean_native: 가늘`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese filled from empty**: added the full Wiktionary list `[tiêm, tươm, thin, thên]`.

Filled empty `pos` → `性詞` and empty `boundedness` → `90`. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 繊)" tag to the existing [[繊細]] entry. One grep hit on [[合成]] confirmed a false positive (繊 appears only in body-prose example text "合成繊維," not its own `characters:` field). **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 准 (6303; 1365 characters remaining).

### 2026-08-10, iteration 1140 — [[characters/准|准]]

**mc_id off-by-one fixed**: stored `2760` (actually 莎) → actual rank in `CC 2000.md` line 794 is `2761`. **Classification confirmed**: `graphemic_classification: 隼` matches Wiktionary's 形聲 analysis (semantic 冫 "ice" + phonetic 隼).

**Vietnamese contamination fixed**: stored `[chuẩn, chõn, chỏn, chốn, chổn, chủn, trốn]` (7 values). Wiktionary's list is `[chuẩn, chốn, chổn, chõn, chủn, trốn]` (6 values, same set minus `chỏn`) — `chỏn` has no support anywhere and no citing-word research corroborates it. Removed.

**`korean_native` filled with a caveat**: no direct hun exists for the "allow, permit" sense specifically — Korean Wiktionary's entry for the traditional form 準 documents multiple senses under two different readings (준: "level, standard, rule" / 절: "bridge of the nose," unrelated). Filled with `법도` ("law, standard"), the closest documented gloss under the matching `준` reading, tracing the semantic path from "level/standard" to this page's "permit" sense — flagged here as an inference rather than a direct hun-to-sense match, unlike most other `korean_native` fixes this backlog.

**Major structural issue found, flagged rather than resolved**: this vault has **two separate, independently-existing character pages for what the frontmatter itself claims is one character** — `characters/准.md` (this page, danayo_id 6303) lists `準` as its own alias, while `characters/準.md` (a *different*, already-existing page, danayo_id 4167, mc_id 1803, `stand_in: 標準`) reciprocally lists `准` as *its* alias. Both pages are actively cited by real, distinct words (this page's own [[准許]] vs. 準's [[準線]], [[標準]], [[基準]], [[準備]]) — a genuine conflict between the "alias = parent form, never used independently" convention and the reality that both forms are in independent, real use. Did not attempt to merge or delete either page; left both untouched for the user to resolve, and only counted [[准許]] (which specifically cites `准`) toward this page's own `## Words`.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. Ten grep hits ([[偏差]], [[精度]], [[外貨]], [[原則]], [[皆時]], [[堕胎]], [[指標]], [[表記]], [[凶器]], [[関詞]]) and three chengyu hits ([[臨渇掘井]], [[有備無患]], [[重文軽武]]) all confirmed false positives — none cite either 准 or 準 in their own `characters:` fields. **Derived Characters**: none found under `隼` beyond 准/準 themselves.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 粒 (6304; 1364 characters remaining).

### 2026-08-10, iteration 1141 — [[characters/粒|粒]]

**mc_id off-by-one fixed**: stored `3275` (actually 沂) → actual rank in `CC 3000.md` line 289 is `3276`. **Classification confirmed**: `graphemic_classification: 立` matches Wiktionary's 形聲 analysis (semantic 米 "rice, grain" + phonetic 立). **Vietnamese** `[lép, lạp]` confirmed as an exact match to Wiktionary's list (just reordered), no contamination.

**`korean_native` corrected**: stored `낟알` (a plausible two-syllable compound also meaning "grain") — Korean Wiktionary's literal printed hun is the single syllable `알` — replaced to match exactly.

Filled empty `pos` → `名詞`. **`## Notes`/`## Words` were in reversed order** — rebuilt into the standard order and 4-bullet format. Added the missing "(stand-in for 粒)" tag to [[粒子]], alongside the already-listed [[顆粒]]. **Sibling-vs-derived check, correctly excluded**: [[拉 (char)|拉]], [[泣 (char)|泣]], [[翌]], [[颯]], [[位]] all cite 立 directly as their own phonetic donor (siblings of 粒), not derivations of 粒 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 犠 (6305; 1363 characters remaining).

### 2026-08-10, iteration 1142 — [[characters/犠|犠]]

**`mc_id: 1954` verified correct as-is**: checked `CC 1000.md` line 995, confirmed the traditional form 犧 sits at that rank.

**Classification cross-checked, kept as a close-match sibling**: Wiktionary's etymology for 犧 names phonetic 羲 (OC \*hŋral, an exact match), not the stored 義 — but 義's own OC (\*ŋrals) is a close variant of the same root, differing mainly by a regular aspiration/coda alternation, and 義 already has its own page in this vault while 羲 does not. Kept `graphemic_classification: 義`, documented both accounts in the Notes (matching the [[窯 (char)|窯]]/䍃-vs-羔 precedent from earlier this backlog, rather than the more clear-cut corrections like [[絹 (char)|絹]]'s 月→肙, since here the OC values genuinely are close rather than unrelated).

**Vietnamese contamination fixed, a clear unrelated-word bug**: stored `[nghé]` — actually a completely unrelated Vietnamese word meaning "buffalo calf," with no connection to "sacrifice." A Hán Việt dictionary confirms `[hi, hy]` as the genuine readings, directly corroborated by the dictionary's own example "hi sinh 犧牲" (sacrifice) matching this page's exact stand-in compound. Replaced entirely.

**`korean`/`korean_native` verified, not touched**: 犧 carries two Korean readings for two different senses (희 vs 사, the second undocumented here) — confirmed `희`/`희생` already match the "sacrifice" sense via both Korean Wiktionary's own hun-eum entry and the stand-in word [[犠牲]]'s own `korean: 희생` field. **`cranberry` tag re-verified**: checked [[牲]]'s own `stand_in` and confirmed it's also `犠牲`, satisfying transitivity.

Filled empty `pos` → `名詞` and empty `boundedness` → `90`. **Duplicate `## Notes` heading with a garbled, empty-bracket second copy** — consolidated into a single standard 4-bullet section. **Sibling-vs-derived check, correctly excluded**: [[儀]] and [[議]] both cite 義 directly as their own phonetic donor (siblings of 犠), not derivations of 犠 itself. One chengyu hit ([[舎本逐末]]) confirmed a false positive (犠 appears only in body-prose example text "犧牲," not the idiom's own citation).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 袋 (char) (6306; 1362 characters remaining).

### 2026-08-10, iteration 1143 — [[characters/袋 (char)|袋]]

**`mc_id: 0` confirmed genuine**: grepped all four `CC 0000`–`CC 3000` files, 袋 appears in none of them. **Classification confirmed**: `graphemic_classification: 代` matches Wiktionary's 形聲 analysis (semantic 衣 "clothing" + phonetic 代). **Vietnamese** `[đại, đãy]` and **`korean_native: 자루`** both confirmed as exact matches to Wiktionary, no fixes needed.

Filled empty `pos` → `名詞`. **`## Notes` had three dangling word-links with no proper headings** — rebuilt to the standard 4-bullet format. **`## Words` expanded from 3 to 4**: added the reflexive stand-in [[袋]] (word) alongside the already-listed [[袋鼠]], [[袋熊]], [[樹袋熊]]. Confirmed the existing `>[!warning] Homophones` callout on [[袋]] (word) — already complete, part of a three-way group with [[台]] and [[大]] (both already perfected, each with matching reciprocal callouts of their own) — no further homophone action needed. While there, fixed [[袋]] (word)'s recurring `vietnamese: null` corruption, replacing it with `đại`.

Three grep hits ([[台]], [[大]], [[套]]) and one chengyu hit ([[有備無患]]) confirmed false positives beyond the already-handled homophone callouts — none cite 袋 in their own `characters:` fields (套 and 有備無患 mention it only in body-prose examples). **Sibling-vs-derived check, correctly excluded**: [[戴 (char)|戴]], [[玳]], [[貸]], [[黛]] all cite 代 directly as their own phonetic donor (siblings of 袋), not derivations of 袋 itself.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 穏 (6307; 1361 characters remaining).

### 2026-08-10, iteration 1144 — [[characters/穏|穏]]

**`mc_id: 9217` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 穏 nor its alias 穩 appears in any of them. **Classification confirmed**: `graphemic_classification: 㥯` matches Wiktionary's 形聲 analysis (semantic 禾 "grain" + phonetic 㥯, no character page in this vault). **`korean_native: 편안할`** confirmed as an exact match to Wiktionary's printed hun.

**Vietnamese expanded**: stored `[ỉn, ỏn, ủn]` (all three genuine). Wiktionary's list adds two more confirmed readings, `ổn` and `ón`, missing from the stored set — added, matching the full five-reading source list.

Confirmed `pos: 性詞` was already correctly filled; filled empty `boundedness` → `75`. **`## Notes`/`## Words` had inverted order and inconsistent heading levels** — rebuilt into the standard order and 4-bullet format. **`## Words` expanded from 2 to 4**: added the missing "(stand-in for 穏)" tag to [[平穏]] and a previously-missing genuine citation, [[安穏]] ("peaceful, quiet"), alongside the already-listed [[不穏]] and the abbreviation note for [[不穏素]] ("astatine"). One grep hit on [[不安]] and one chengyu hit ([[尊敬父母]]) confirmed false positives — neither cites 穏/穩 in its own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[隠]] cites 㥯 directly as its own phonetic donor (a sibling of 穏), not a derivation of 穏 itself. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 砕 (char) (6308; 1360 characters remaining).

### 2026-08-10, iteration 1145 — [[characters/砕 (char)|砕]]

**`mc_id: 2805` verified correct as-is**: checked `CC 2000.md` line 842, confirmed the traditional form 碎 sits at that rank. **Classification confirmed**: `graphemic_classification: 卒` matches Wiktionary's 形聲 analysis (semantic 石 "stone" + phonetic 卒). **`korean_native: 부술`** confirmed as an exact match to Wiktionary's printed hun.

**Vietnamese filled deliberately narrow, not the full raw list**: Wiktionary's Vietnamese section for 碎 is unusually large — 3 differentiated Hán Việt readings (toái, tỏa, tối) plus a 15-item undifferentiated Nôm table including clearly semantically-unrelated words (tuổi "age," túi "bag/pocket," among others). Per the established policy of distrusting Wiktionary's raw undifferentiated Nôm tables when they conflate loosely-associated native words, and with no citing-word research available to narrow the list further, filled only the three explicitly-labeled Hán Việt readings rather than the full 18-item combined set.

Filled empty `pos` → `事詞` and empty `boundedness` → `90`. **`## Notes` had malformed non-vault-style links** (`[石](Radical%20112)`, `[卒](卒.md)`) — rebuilt to the standard 4-bullet format with proper wikilinks.

**`## Words`/`## Chengyu`**: added the reflexive stand-in [[砕]] (word) — whose own page carried *two* corruption bugs, both fixed: recurring `vietnamese: null` → `toái`, and literal-string `korean: "null"` → `쇄`. Added a genuine chengyu citation, [[粉骨砕身]] ("to have one's body smashed to pieces"), confirmed via its own `characters:` field. Two grep hits ([[骨]], [[石灰]]) confirmed false positives — 砕/碎 appears only in body-prose quotations in each, not either page's own `characters:` field. **Sibling-vs-derived check, correctly excluded**: [[酔 (char)|酔]], [[粋]], [[翠]] all cite 卒 directly as their own phonetic donor (siblings of 砕), not derivations of 砕 itself.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 挿 (6309; 1359 characters remaining).

### 2026-08-10, iteration 1146 — [[characters/挿|挿]]

**`mc_id: 4965` confirmed genuine long-tail data**: grepped all four `CC 0000`–`CC 3000` files, neither 挿 nor its aliases 插/揷 appears in any of them. **Classification confirmed**: `graphemic_classification: 臿` matches Wiktionary's 形聲 analysis (semantic 手 "hand" + phonetic 臿, no character page in this vault).

**Vietnamese completely replaced, a wholesale wrong-set bug**: stored `[xép, xấp, xẹp]` — none of which match anything in Wiktionary's Vietnamese section, which lists only `sáp`. Directly corroborated by the citing word [[挿入]]'s own `vietnamese: sáp nhập`, using `sáp` for 挿's part. Replaced the stored set entirely with `[sáp]`.

**`korean_native: 꽂을` left as-is, unconfirmed**: no hun could be located for the traditional form 插 either (ko.wiktionary's structure was present but the gloss text itself didn't render) — left the pre-existing, semantically apt value untouched per the omit-don't-fabricate policy.

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with one dangling word-link** — rebuilt to the standard 4-bullet format. **`## Words`**: added the missing "(stand-in for 挿)" tag to the sole genuine citation, [[挿入]]. **Chengyu**: no hits. **Derived Characters**: none.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 撲 (char) (6310; 1358 characters remaining).

### 2026-08-10, iteration 1147 — [[characters/撲 (char)|撲]]

**mc_id off-by-one fixed**: stored `2958` (actually 沾) → actual rank in `CC 2000.md` line 1000 is `2959`. **Classification confirmed**: `graphemic_classification: 菐` matches Wiktionary's 形聲 analysis (semantic 手 "hand" + phonetic 菐, no character page in this vault). **Vietnamese** `[buộc, phác, phốc, vọc, vục]` confirmed as an exact match to Wiktionary's five-reading list (just reordered), no contamination.

**`korean_native` citation-form fix**: stored `칠` (adnominal, from 치다) — Korean Wiktionary's literal printed hun is the infinitive `치다` ("to hit, strike") — replaced to match exactly.

Confirmed `pos: 事詞` was already correctly filled. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[撲]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `phốc`. **Sibling-vs-derived check, correctly excluded**: [[僕]] cites 菐 directly as its own phonetic donor (a sibling of 撲), not a derivation of 撲 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 盆 (char) (6311; 1357 characters remaining).

### 2026-08-10, iteration 1148 — [[characters/盆 (char)|盆]]

**mc_id off-by-one fixed**: stored `2057` (actually 犁) → actual rank in `CC 2000.md` line 63 is `2058`. **Classification confirmed**: `graphemic_classification: 分` matches Wiktionary's 形聲 analysis (semantic 皿 "vessel" + phonetic 分). **`korean_native: 동이`** confirmed as an exact match to Korean Wiktionary's printed hun.

**Vietnamese expanded**: stored `[buồn, bòn, bồn, dồn, vồn]` (all five genuine). Wiktionary's combined Hán Việt/Nôm list adds two more confirmed readings, `bùn` and `bộn`, missing from the stored set — added, matching the full seven-reading source list.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub** — rebuilt to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[盆]] (word) — whose own page had an empty (unfilled, not corrupted) `vietnamese` field, filled to `bồn` — alongside the already-listed [[盆栽]] ("bonsai"). **Sibling-vs-derived check, correctly excluded**: eight characters ([[扮 (char)|扮]], [[紛 (char)|紛]], [[粉 (char)|粉]], [[盼]], [[芬]], [[貧]], [[雰]], [[頒]]) all cite 分 directly as their own phonetic donor (siblings of 盆), not derivations of 盆 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 畝 (char) (6313; 1356 characters remaining).

### 2026-08-10, iteration 1149 — [[characters/畝 (char)|畝]]

**`mc_id: 1376` verified correct as-is**: checked `CC 1000.md` line 393, confirmed 畝 itself sits at that rank.

**Classification corrected, an inverted case from the usual pattern**: stored `graphemic_classification: 每` had a near-perfect OC match to 畝 itself (\*mɯːʔ vs \*mɯʔ), but no character page of its own — while Wiktionary's actual documented component, 久 (OC \*kʷlɯʔ, a much rougher match, replacing an earlier 又), *does* have a page in this vault. Unlike most corrections this backlog (where the true donor also had the better OC match), here the true donor's OC is the worse fit — but since 久 is both the explicitly-attested graphic component and already has vault infrastructure, corrected to `久` anyway, documenting the OC tension directly in the Notes so a future pass understands the reasoning rather than "fixing" it back to 每.

**Vietnamese** `[mẩu, mẫu]` and **`korean_native: 이랑`** both confirmed as exact matches to Wiktionary (which also documents two Korean sound readings, 무/묘, sharing this one hun — no korean field change needed since `묘` already matches the character's own stored 諺文/羅馬字).

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[畝]] (word) — whose own page carried the recurring `vietnamese: null` corruption, fixed to `mẫu`. **Sibling-vs-derived check, correctly excluded** (re-checked under the corrected `久` value): [[玖]] and [[灸]] both cite 久 directly as their own phonetic donor (siblings of 畝), not derivations of 畝 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 罵 (6314; 1355 characters remaining).

### 2026-08-10, iteration 1150 — [[characters/罵|罵]]

**`mc_id: 2197` verified correct as-is**: checked `CC 2000.md` line 206, confirmed 罵 itself sits at that rank — no fix needed.

**Classification, Vietnamese, and korean_native all confirmed correct as-is** against Wiktionary: `graphemic_classification: 馬` is the documented 形聲 phonetic (semantic [[Radical 122|网]] "net," implying entrapment/accusation, + phonetic [[馬 (char)|馬]]); the stored `vietnamese: [mà, mạ, mắng, mựa]` is an exact match to Wiktionary's Hán Việt (mạ) + Nôm (mựa, mắng, mà) split, no contamination; `korean_native: 꾸짖을` is an exact match to Wiktionary's literal printed hun "꾸짖을 매."

Filled empty `pos` → `事詞`. **`## Notes` was a bare two-link stub with no citation-count bullet or level bullet** — rebuilt to the standard 4-bullet format. **`## Words`**: the existing [[痛罵]] entry (the character's `stand_in` compound, since 罵 alone is too bound to stand as a Dan'a'yo word) tagged "(stand-in for 罵)"; its own page checked and found already complete and correctly formatted, no corruption. **Derived-Characters check**: 罵 is itself a *child* of [[馬 (char)|馬]], not a parent — confirmed [[馬 (char)|馬]]'s own `## Derived Characters` section already lists 罵 alongside its true siblings [[碼 (char)|碼]] and [[媽]], so no section needed on 罵's own page. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 填 (char) (6316; 1354 characters remaining).

### 2026-08-10, iteration 1151 — [[characters/填 (char)|填]]

**`mc_id: 2019` verified correct as-is**: checked `CC 2000.md` line 19, confirmed 填 itself sits at that rank.

**Classification corrected**: stored `graphemic_classification: 眞` (traditional form) → `真` (the form with its own vault page, [[真 (char)|真]] listing 眞 among its own `aliases`) — same shinjitai/simplified-form-preference pattern applied previously to [[捨]]→舎, [[絵]]→会, [[圏]]→巻, [[駄]]→太. Wiktionary confirms 形聲: semantic [[Radical 032|土]] + phonetic 真/眞.

**Vietnamese** `[điền, đền]` **confirmed correct as-is**: exact match to Wiktionary's Hán Việt (điền) + Nôm (đền) split, also independently corroborated by the citing word [[填]] (word page)'s own deep prior research distinguishing đền as an Old Sino-Vietnamese doublet layer rather than noise.

**`korean_native: 메울` confirmed correct as-is**: Wiktionary's Korean section for 填 gives only bare readings (전/진) with no gloss, but the sibling entry 塡 (the Kangxi-orthodox alias form) documents the Middle Korean citation 뎐訓 from *Sinjeung Yuhap* (新增類合, 1576) glossing this character as "to fill up" — matching 메울 (attributive of 메우다, "to fill") precisely. No fix needed.

`pos: 事詞` was already filled. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard format, citing the traditional-form/alias relationship directly in the etymology bullet. **`## Words`**: added the reflexive stand-in [[填]] (word) alongside the existing genuine citation [[充填]]; both citing word pages checked and found already fully perfected with no corruption. **Broken-link bug found and fixed** on [[充填]] (word): both its tip callout and Notes body linked to the nonexistent `characters/填.md` instead of the real `characters/填 (char).md` — repointed both. **Derived-Characters check**: nothing in the vault cites 填 itself as a phonetic donor; 填 is a sibling (not parent) of [[鎮 (char)|鎮]] and [[慎]], all deriving from 真 — no `## Derived Characters` section needed on 填's own page. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 弁 (char) (6317; 1353 characters remaining).

### 2026-08-10, iteration 1152 — [[characters/弁 (char)|弁]]

**Unusual case**: 弁 is a genuine independent classical character (會意, "hands placing a ceremonial cap on someone's head," OC \*brons) whose own original meaning ("a cap") is completely unrelated to this page's stored fields. In Japan, 弁 additionally serves as the shinjitai stand-in for **three separate** traditional characters — 辯 "debate," 辨 "distinguish," 瓣 "petal/valve" — all listed correctly in `aliases`. This vault page tracks 弁 specifically in that collapsed stand-in role (`english: [discuss, distinguish]`), not the cap sense.

**`mc_id: 910` verified correct as-is, a genuine "recorded under alias" case**: rank 910 in `CC 0000.md` belongs to 辯 (the "debate" donor), not 弁 itself — but 弁 itself *does* independently appear at rank 1983 in `CC 1000.md`, carrying its unrelated "cap" meaning. Kept 910/辯 since it correctly tracks the classical frequency of the actual meaning this page represents, rather than switching to 弁's own rank for a sense this page doesn't cover.

**`graphemic_classification: 辡` confirmed correct as-is**: verified against all three donor etymologies — 辯 (semantic 言 + phonetic 辡), 辨 (phonetic 辡 + semantic 刀), 瓣 (phonetic 辡 + semantic 瓜) — all genuinely share 辡 as their phonetic. 辡 has no vault page (not in the forbidden-character list either — simply uncreated), so left unlinked in the Notes prose.

**`korean_native: 분별할` confirmed correct as-is, sourced from a *different* donor than `mc_id`**: this exact hun ("분별할 변") is 辨's own literal printed eumhun, not 辯's (which is "말씀 변," "speech") — a deliberate/valid choice since 분별할 directly matches this page's "distinguish" sense while 辯 covers "discuss." `korean: 변` is shared identically by both 辯 and 辨 regardless.

**Vietnamese expanded** `[biền]` → `[biện, biền]`: biện is independently and heavily corroborated — listed for 弁 itself, for 辯, for 辨, *and* for 瓣 — making it clearly the dominant cross-donor reading; kept biền too since it's also explicitly listed for 弁 itself with no contradicting evidence.

Rebuilt the malformed `# Notes` stub (single-hash heading, containing only a stray leftover scratch numeral "1180" — likely an old, since-corrected mc_id guess — plus two bare CC links) into the standard 4-bullet format, documenting the three-donor stand-in relationship directly. **`## Words`**: added the reflexive stand-in [[弁]] (word) and the existing [[花弁]] "flower petal" citation. **Bugs fixed on [[弁]] (word)**: literal `vietnamese: "null"` corrected to `biện`; its own Notes carried the identical stray "1180" scratch text under a malformed `# Notes` heading — replaced with a proper citation of the character page. [[花弁]] (word) checked: its blank (not corrupted) `vietnamese` field left as-is, no supporting source found this pass — deferred to that word's own turn in the word-perfecting loop. **Derived-Characters check**: [[辦]] cites 辡 as its own direct phonetic donor — a sibling, not a child of 弁 — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 屈 (char) (6318; 1352 characters remaining).

### 2026-08-10, iteration 1153 — [[characters/屈 (char)|屈]]

**`mc_id: 923` verified correct as-is**: checked `CC 0000.md` line 956, confirmed 屈 itself sits at that rank.

**Notes prose etymology bullet was doubly wrong, corrected**: the existing text read "semantic 出 ('tail') + phonetic 尾" — but Wiktionary confirms it's backwards on every count: the true semantic component is 尾 "tail" (which became 尸 in clerical script, matching the stored `radical: 尸`), the true phonetic is 出 (OC \*kʰljuds/\*kʰljud, which the old note had mislabeled onto 尾), and 出 itself means "to exit," not "tail." The stored `graphemic_classification: 出` field was already correct throughout — only the prose description was garbled. Linked to [[尾 (char)|尾]] (has a vault page) rather than the pageless 尸.

**`korean_native` citation-form mismatch found and fixed**: stored `"굽힐"` (adnominal of 굽히다, transitive "to bend [something]") corrected to `"굽을"` (adnominal of 굽다, the actual base verb in Wiktionary's literal printed eumhun "굽을 굴") — same citation-form-mismatch pattern seen previously.

**Vietnamese** `[khuất, quất]` **confirmed correct as-is**, exact match to Wiktionary.

Filled empty `pos` → `事詞`. **`## Notes`/`## Words` had run together with no blank-line separation** — reformatted to standard spacing and rebuilt to the full 4-bullet format. **`## Words`**: added the reflexive stand-in [[屈]] (word) alongside the existing [[理屈]] citation (already fully perfected, no changes needed there). **Bug fixed on [[屈]] (word)**: literal `vietnamese: "null"` corrected to `khuất`; its empty `# Notes` stub filled with the standard character citation. **False positives correctly excluded**: [[羞辱]] (its `屈辱` alias doesn't use 屈 as a component), [[空虚]] (mentions 屈 only in prose discussing the *Daodejing*), [[受理]] (mentions [[理屈]] only as a cross-reference example) — none are genuine citations. **Derived-Characters check**: [[拙]] and [[黜]] both cite 出 directly as their own phonetic donor — siblings of 屈, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 飼 (6319; 1351 characters remaining).

### 2026-08-10, iteration 1154 — [[characters/飼|飼]]

**`mc_id: 8488` outside the vault's verifiable range**: this vault only maintains CC frequency lookup pages for the top 4000 classical characters (`CC 0000`–`CC 3000`); 8488 falls beyond that, so it cannot be checked against any lookup page one way or the other — documented this explicitly in the Notes rather than silently treating it as verified.

**Classification, Vietnamese, and korean_native all confirmed correct as-is** against Wiktionary: `graphemic_classification: 司` is the documented 形聲 phonetic (semantic [[Radical 184|食]] "food" + phonetic [[司]]); `vietnamese: tự` matches both the Hán Việt and Nôm readings given (identical); `korean_native: 기를` matches the literal printed eumhun "기를 사" exactly.

**`## Notes` was a bare two-link stub under a malformed `# Notes` heading (missing `## Words`, though a `## Words` section already existed further down)** — rebuilt to the standard 4-bullet format. **`## Words`**: tagged the existing [[飼養]] citation "(stand-in for 飼)"; its own page checked and found already fully perfected (`date-last-perfect: 2026-07-12`), no corruption. **Derived-Characters check**: [[伺]], [[嗣]], [[祠]], [[詞]] all cite 司 directly as their own phonetic donor — siblings of 飼, not children — correctly excluded; confirmed nothing in the vault derives from 飼 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 仲 (6320; 1350 characters remaining).

### 2026-08-10, iteration 1155 — [[characters/仲|仲]]

**`mc_id: 328` verified correct as-is**: checked `CC 0000.md` line 343, confirmed 仲 itself sits at that rank.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 中` is the documented 形聲 phonetic (semantic [[Radical 009|人]] + phonetic [[中 (char)|中]]); `vietnamese: trọng` matches Wiktionary's sole listed reading. **`korean_native: 버금` left as-is despite Wiktionary's own Korean entry for 仲 being incomplete** (no eumhun listed there) — "버금" ("next, second-in-rank") is well-established outside Wiktionary as this character's traditional gloss and matches its core meaning ("second-born among siblings; an intermediary between first and last") precisely, so kept without a contradicting source to justify a change.

Filled empty `pos` → `名詞`. **`## Notes` was a bare two-link stub under a malformed `# Notes` heading with no `## Words` section** — rebuilt to the standard 4-bullet format. **`## Words`**: this character has an unusually large family of six genuine citations — tagged the existing stand-in [[仲介]] (`#cranberry`, already verified transitivity-holding in an earlier iteration) plus [[仲媒]], [[仲春]], [[仲夏]], [[仲秋]], [[仲冬]] (the four mid-season month names), all checked and found already fully perfected with no corruption. **False positives correctly excluded**: [[冬]], [[中秋節]], [[孝廉]], [[令和]], [[攘夷]] (all mention 仲 only in prose, e.g. as part of the historical names 董仲舒/管仲 or the word 仲間), and four chengyu ([[切磋琢磨]], [[三綱五常]], [[尊王攘夷]], [[令行禁止]]) that likewise only mention 仲 via those same proper names — none are genuine compositional citations. **Derived-Characters check**: nothing in the vault cites 仲 itself as a phonetic donor. **Chengyu**: no genuine hits (see above).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 届 (char) (6321; 1349 characters remaining).

### 2026-08-10, iteration 1156 — [[characters/届 (char)|届]]

**`mc_id: 5908` outside the vault's verifiable range**: confirmed neither 届 nor its traditional alias 屆 appears anywhere in `CC 0000`–`CC 3000`, so this value (like [[飼]]'s in the prior iteration) cannot be checked against a lookup page — documented explicitly rather than assumed.

**Classification, Vietnamese, and korean_native all confirmed correct as-is**: `graphemic_classification: 凷` is the documented 形聲 phonetic (semantic [[Radical 044|尸]] "body" + phonetic 凷, pageless in this vault and not on the forbidden-character list — simply uncreated); `vietnamese: giới` matches Wiktionary's sole listed Hán Việt reading; `korean_native: 이를` (adnominal of 이르다, "to arrive") fits the "arrive; deliver" sense precisely even though Wiktionary's own Korean entry for 屆 lists no eumhun to check against directly. Confirmed 屆 (the alias) is genuinely the Kangxi/kyūjitai traditional form and 届 its Japanese shinjitai, per Wiktionary's explicit note.

`pos: 性詞` was already filled. **`## Notes` was a bare two-link stub with no `## Words` section** — rebuilt to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[届]] (word) — the only genuine citation found. **Double bug fixed on [[届]] (word)**: both `vietnamese: "null"` and literal `korean: "null"` corrected to `giới` and `계` respectively; its empty `# Notes` stub filled with the standard character citation. **Derived-Characters check**: nothing in the vault cites 凷 itself as a phonetic donor besides 届. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 拉 (char) (6324; 1348 characters remaining).

### 2026-08-10, iteration 1157 — [[characters/拉 (char)|拉]]

**`mc_id: 4449` outside the vault's verifiable range**: 拉 does not appear in any of `CC 0000`–`CC 3000`, so this value cannot be checked against a lookup page.

**Classification confirmed correct as-is**: `graphemic_classification: 立` is the documented 形聲 phonetic (semantic [[Radical 064|手]] + phonetic [[立 (char)|立]]). **`korean_native: 끌` confirmed correct as-is**: the raw Wiktionary wikitext gives the eumhun as 끌다 ("to pull"); since 끌다 is an ㄹ-final stem, its adnominal form contracts to the identical bare syllable 끌 — no fix needed.

**Vietnamese drastically narrowed, a severe case of the undifferentiated-Nôm-table pattern**: stored `[dập, giập, loạt, lấp, lắp, lợp, rấp, rắp, sắp, sụp, xập, xệp, đập]` — thirteen entries, all drawn from a single Nôm dictionary-citation pile spanning **21** total variants in the raw source — while the one explicitly-labeled Hán Việt reading, **lạp**, was entirely absent from the stored list. Replaced with just `[lạp]`, corroborated by the two genuine Sino-Vietnamese-register citing words already in the vault ([[拉金]] "rutherfordium," [[拉麺]] "ramen," both modern scientific/loan compounds that would use the Hán Việt register, not a native Nôm reading).

**Real bug found and fixed on [[拉]] (word)**: `korean: "납"` was the South Korean 두음법칙-shifted form of this reading — corrected to `랍` (North Korean/문화어 form, matching this vault's standing convention and the character page's own already-correct field); also filled its blank `vietnamese` → `lạp` and its empty `# Notes` stub.

`pos: 事詞` was already filled. Rebuilt `## Notes`/`## Words` to the standard format. **`## Words`** expanded from one entry to four: added the reflexive stand-in [[拉]], plus two newly-found genuine citations [[拉金]] and [[拉麺]], alongside the existing [[孟加拉]]. **False positives correctly excluded**: [[羅馬語]], [[麺]], [[不丹]], [[蛍金]], [[巴基斯坦]], [[泥婆羅]] (grep hits from prose mentions, none actually compose with 拉 in their `characters` field) and one chengyu, [[遠交近攻]] (mentions 拉攏 only in modern-commentary prose). **Derived-Characters check**: [[泣]], [[翌]], [[颯]], [[位]], [[粒]], [[笠]], [[雴]] all cite 立 directly as their own phonetic donor — siblings of 拉, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 擦 (char) (6325; 1347 characters remaining).

### 2026-08-10, iteration 1158 — [[characters/擦 (char)|擦]]

**`mc_id: 0` confirmed correct as-is**: 擦 does not appear in `CC 0000`–`CC 3000` and has no `aliases` to check either — a genuine late/vernacular character absent from Classical Chinese usage, consistent with the `0` sentinel.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 察` is the documented 形聲 phonetic (semantic [[Radical 064|手]] + phonetic [[察 (char)|察]]); `vietnamese: [sát, xát, xớt]` is an exact match to Wiktionary's full reading set (sát doing double duty as both the Hán Việt and one of the Nôm readings). **`korean_native: 문지를` left as-is**: Wiktionary's own `{{ko-hanja}}` template has a genuinely empty eumhun field, but 문지를 (adnominal of 문지르다, "to rub") is the well-established traditional gloss for this character and fits the "wipe, scrub, rub" sense precisely — kept without a contradicting source.

Filled empty `pos` → `事詞`. **`# Notes` was malformed**: a bare two-link CC-citation stub under the wrong heading level, with a stray `## Words`-style bullet ([[擦拭]]) appended directly underneath it instead of living in its own `## Words` section — split apart and rebuilt to the standard format. **`## Words`**: added the reflexive stand-in [[擦]] alongside the existing [[擦拭]] (already fully perfected, `date-last-perfect: 2026-07-23`, no changes needed). **Bug fixed on [[擦]] (word)**: literal `vietnamese: "null"` corrected to `sát`; empty `# Notes` stub filled with the standard character citation. **Derived-Characters check**: nothing in the vault cites 擦 itself as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 那 (char) (6326; 1346 characters remaining).

### 2026-08-10, iteration 1159 — [[characters/那 (char)|那]]

**`mc_id` off-by-one fixed**: stored `3625` pointed to 酇 (the line immediately before); 那 itself sits at rank 3626 in `CC 3000.md` — corrected.

**Notes prose etymology bullet was doubly wrong, same pattern as [[屈]] two iterations ago**: the existing text read "semantic 冄 ('city') + phonetic 邑" — reversed on both counts. Wiktionary confirms semantic is [[邑]] ("city," originally a state name) and phonetic is [[冉]] (OC \*njam/\*njamʔ); the stored `graphemic_classification: 冉` field itself was already correct throughout, only the prose was garbled (and used the variant glyph 冄 instead of 冉).

**Vietnamese `[na, nà, ná, nả]` and `korean_native: 어찌` both confirmed correct as-is**, exact matches to the raw Wiktionary wikitext templates.

**`aliases: [哪]` investigated and kept, an unusual but legitimate case**: Wiktionary states 哪 was "written as 那 before the 20th century" (a genuine historical graphical identity) even though 哪's own etymology is a separate fusion of 奈何 rather than a direct descendant of 那 — a split-apart-by-modern-convention case rather than a spurious alias; no vault page exists for 哪 independently, so no conflict.

Filled empty `pos` → `代詞`. **`## Notes`/`## Words` were badly malformed**: a garbled etymology bullet, a non-standard markdown link (`[支那](/words/支那.md)` instead of the ruby+wikilink format) with an English gloss appended outside the ruby tags, and a stray empty bullet — all rebuilt to the standard format. **`## Words`** expanded from one entry to four: added the reflexive stand-in [[那]], plus two newly-found genuine citations [[刹那]] and [[印度支那]], alongside the corrected [[支那]] entry. **Bug fixed on [[那]] (word)**: blank `vietnamese` field filled → `na`; empty `# Notes` stub filled with the standard character citation. **False positives correctly excluded**: 23 other correlative-pronoun words (彼/其/何/此-series) that don't cite 那 in their `characters` field, plus eight chengyu, all grep hits from 那 used as a plain demonstrative "that" within example-sentence prose rather than as a genuine citation. **Derived-Characters check**: [[髯]] cites 冉 directly as its own phonetic donor — a sibling, not a child of 那 — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 喫 (char) (6327; 1345 characters remaining).

### 2026-08-10, iteration 1160 — [[characters/喫 (char)|喫]]

**`mc_id: 9302` outside the vault's verifiable range**: neither 喫 nor its alias 吃 appears in `CC 0000`–`CC 3000`.

**Classification confirmed correct as-is**: `graphemic_classification: 契` is the documented 形聲 phonetic (semantic [[Radical 030|口]] + phonetic 契).

**Vietnamese drastically narrowed on the strength of the citing word's own prior deep research**: initially cross-checked against raw Wiktionary and removed the unsupported `khè` (5 of 6 remaining), but the citing word [[喫]] (word) — already fully perfected on 2026-07-27 — had gone considerably further, explicitly documenting that `khế`/`khịa`/`khịt` are unrelated Nôm phonetic-loan readings for other native words (not Sino-Vietnamese doublets of 喫) and that `ngật` belongs etymologically to the *separate* character 吃's original "to stutter" sense, only superficially conflated because 吃 later absorbed 喫's "eat" meaning in modern usage. Per the standing rule to trust a citing word's own deep research over raw dictionary data, narrowed the field to just `[khiết]` — also independently confirming my `khè` removal was correct (that word's Notes call it "unattested... looks like noise or a transcription error"). **`korean_native: 먹을` left as-is**: Wiktionary's literal eumhun is the dual "먹을/마실 끽" (eat/drink); kept the already-stored "먹을" half rather than inventing a multi-value format never used elsewhere in this vault for this field.

Filled empty `pos` → `事詞` and blank `boundedness` → `80` (no reliable literal source for this heuristic field; matched the majority value among comparable self-standing 事詞 characters processed this sweep). **`# Notes` was a bare two-link stub under the wrong heading level** — rebuilt to the standard format, with 吃 left unlinked (pageless in this vault) rather than as a broken wikilink. **`## Words`**: added the reflexive stand-in [[喫]] alongside the existing [[喫驚]] citation. **Derived-Characters check**: [[偰]] and [[楔]] both cite 契 directly as their own phonetic donor — siblings of 喫, not children — correctly excluded. **Chengyu**: no genuine hits ([[詛地哀食]]'s 吃 is a Bible-quotation prose mention, not a citation).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 剰 (6328; 1344 characters remaining).

### 2026-08-10, iteration 1161 — [[characters/剰|剰]]

**YAML corruption fixed**: `japanese_native` was malformed — a scalar value `あま` immediately followed by an orphaned list item `- あまる` under the same key. Kept `あま` (the verb stem, matching this vault's established convention of storing 連用形 stems rather than dictionary forms, e.g. [[喫]]'s の from のむ) and removed the stray duplicate.

**`mc_id: 0` confirmed correct as-is**: neither 剰 nor its aliases 剩/賸 appear in `CC 0000`–`CC 3000`.

**Classification confirmed correct as-is, same shinjitai-preference pattern as [[填]]**: Wiktionary's etymology names the traditional 乘 as the phonetic donor, but the stored `graphemic_classification: 乗` correctly points to the form with an actual vault page ([[乗 (char)|乗]], which lists 乘 among its own `aliases`). **Vietnamese `thặng` confirmed correct as-is** — independently corroborated by [[乗]] (word)'s own prose, which explicitly attributes `thặng` to "the derived character [[剰]]." **`korean_native: 남다` left as-is**: Wiktionary provides no eumhun for 剩 at all; this vault does have ~40 other characters using the infinitive `-다` citation form (a legitimate minority pattern, not necessarily wrong), so left unchanged rather than force-converting to the more common adnominal form without a contradicting source.

Filled blank `boundedness` → `80` (matched the majority value among comparable compound-stand_in characters). **Notes etymology bullet was malformed** — a bare, broken relative link (`[乗 (char)](乗%20(char).md)`) followed by stray `+ ||` — rebuilt to the standard format along with the missing SKIP/Stroke, CC-rank, and Grade/HSK/Jōyō/Korean-level bullets. **`## Words`**: the existing [[剰余]] citation (stand-in, already fully perfected on 2026-08-03) tagged "(stand-in for 剰)" — no other genuine citations found. **False positives correctly excluded**: [[乗]] (word) mentions 剰 only in cross-referencing prose about Vietnamese readings, and two chengyu ([[欲求不満]], [[天地不仁]]) use 剩/剰 only as an ordinary verb "remain" within prose, not as citations. **Derived-Characters check**: nothing in the vault cites 剰 itself as a phonetic donor. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 帽 (6329; 1343 characters remaining).

### 2026-08-10, iteration 1162 — [[characters/帽|帽]]

**`mc_id: 5673` outside the vault's verifiable range**: 帽 does not appear in `CC 0000`–`CC 3000` and has no aliases to check.

**Classification confirmed correct as-is**: `graphemic_classification: 冒` is the documented 形聲 phonetic (semantic [[Radical 050|巾]] + phonetic [[冒]]).

**Vietnamese expanded**: stored `[mão, mũ, mạo]` was missing `mào`, the fourth reading Wiktionary explicitly lists as this character's own differentiated Nôm form — added, reordering to group the two Hán Việt readings (mão, mạo) before the two Nôm (mũ, mào). Independently corroborated by [[帽子]] (word)'s own prior deep research, which already narrowed *its* Vietnamese field to just `mũ` after finding no attestation for a Sino-Vietnamese "mạo tử" compound — consistent with, not contradicting, the character's own broader four-reading set.

**`japanese_native` corrected**: stored `おお` was the verb stem of おおう ("to cover") — but Wiktionary's own kun'yomi entry for that reading is a redlink (`帽う`, page does not exist), meaning even Wiktionary doesn't have a real attestation for this as a genuine reading of 帽. Replaced with `ずきん` (zukin, "hood; cap"), the solidly-attested primary kun'yomi noun reading. **`korean_native: 모자` left as-is despite looking unusual** (a two-morpheme Sino-Korean compound word rather than a typical single native gloss) — Wiktionary provides no eumhun at all to check against, and this reflects a known pattern where loanword-derived concepts without an old native-Korean equivalent get glossed by their standard compound word in some hanja dictionaries; left unchanged without a contradicting source.

Filled empty `pos` → `名詞`. Rebuilt `## Notes` to the standard 4-bullet format, including the 冃→冒 historical-graphic-evolution note. **`## Words`**: tagged the existing [[帽子]] citation "(stand-in for 帽)"; both it and [[笠帽]] checked and found already fully perfected, no corruption. **False positives correctly excluded**: [[錐子]], [[種子]], [[梯子]] all mention 帽子 only as an example within their own `子`-suffix discussions, not as genuine citations. **Derived-Characters check**: [[瑁]] cites 冒 directly as its own phonetic donor — a sibling, not a child of 帽 — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 戴 (char) (6330; 1342 characters remaining).

### 2026-08-10, iteration 1163 — [[characters/戴 (char)|戴]]

**`mc_id: 1279` verified correct as-is**: checked `CC 1000.md` line 292, confirmed 戴 itself sits at that rank.

**Real classification bug found and fixed**: stored `graphemic_classification: 代` matched nothing in Wiktionary's etymology for 戴 at all — the actual phonetic candidates are 弋, 𢦏, or 之 (with 異 as semantic, possibly also phonetic). Checking the vault's own [[代]] page revealed the likely source of the confusion: 代's *own* `graphemic_classification` is 弋 — meaning 代 is itself a phonetic derivative of 弋, not a component of 戴 at all, and was probably substituted in error since it superficially "contains" 弋. Corrected to `弋` (kept pageless/unlinked in prose, per the [[弁]]/[[届]] precedent, rather than substituting an unrelated derived character). Confirmed via the Derived-Characters sweep below that 代 is in fact a *sibling* of 戴 (both ultimately trace to 弋), not its donor — independent corroboration of the fix.

**Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `[dải, trải, đái]` is an exact match (reordered) to Wiktionary; `korean_native: 일` matches the literal eumhun "일 대" exactly; `japanese_native: いただ` is the correct stem of the attested kun'yomi いただく.

Filled empty `pos` → `事詞`. Rebuilt `## Notes` to the standard 4-bullet format, including the oracle-bone pictograph origin and the 異/弋 reanalysis. **`## Words`**: added the reflexive stand-in [[戴]] alongside the existing [[佩戴]] (already fully perfected, no changes needed). **Bug fixed on [[戴]] (word)**: literal `vietnamese: "null"` corrected to `dải`; empty `# Notes` stub filled with the standard character citation. **New `## Chengyu` section added**: [[不共戴天]] genuinely cites 戴 (char) in its `characters` field — its own Notes discuss 戴天 ("to bear heaven above one's head") directly; [[不遠千里]]'s hit was a false positive (蒙子 quote naming a person, 戴不勝). **Derived-Characters check**: [[鳶 (char)|鳶]], [[代]], [[式]] all cite 弋 directly as their own phonetic donor — siblings of 戴, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 瞭 (6331; 1341 characters remaining).

### 2026-08-10, iteration 1164 — [[characters/瞭|瞭]]

**YAML bug fixed**: `mandarin: liào liǎo` was a single malformed scalar with two space-joined readings — normalized to the single primary reading `liǎo` ("clear, understanding"), matching this vault's established single-scalar convention for the `mandarin` field; the secondary reading `liào` ("to gaze at," as in 瞭望) documented in prose instead rather than force-fit into a never-before-used list format for this field.

**`mc_id: 4892` outside the vault's verifiable range, genuinely ambiguous**: 瞭 itself doesn't appear in `CC 0000`–`CC 3000`, but unusually its aliases 了 (rank 3820) and 亮 (rank 2852) *do* both independently appear — yet neither is a clean numeric match to 4892 and both are equally plausible semantic donors (了 via 明了/明瞭 "clear, understand"; 亮 via "bright, clear"), so left as-is rather than guessing which alias it should be "recorded under" without a forcing signal.

**Classification and japanese_native confirmed correct as-is**: `graphemic_classification: 尞` matches Wiktionary's documented 形聲 phonetic (semantic [[Radical 109|目]] + phonetic 尞, pageless in this vault); `japanese_native: あきらか` is an exact match to the attested kun'yomi.

**Vietnamese expanded**: added `liệu`, the fifth reading Wiktionary lists that was missing from the stored four. **`korean_native` filled** (was an explicit empty string): Wiktionary's own eumhun field is empty, so used the well-established traditional hanja gloss `밝을` ("bright"), matching the "clear, clear-sighted" sense — unverifiable against this vault's usual source but not contradicted by it either.

Filled empty `pos` → `性詞`. **Notes and Words sections were reversed and malformed** (`## Words` appearing before a bare `# Notes` stub) — rebuilt in correct order to the standard format, explicitly noting the unusual semantic-equivalent (not orthographic-variant) nature of the `了`/`亮` aliases. **`## Words`** expanded from one entry to two: added the stand-in [[明瞭]] (already independently perfected, and notably itself pronounced two ways — míngliǎo or míngliàng, the latter borrowing the 亮-alias reading, corroborating that alias's genuine phonetic kinship) alongside the existing [[瞭然]]. **New `## Chengyu` section added**: [[一目瞭然]] genuinely cites 瞭 in its `characters` field. **Derived-Characters check**: [[僚]], [[寮]], [[療]], [[遼]] all cite 尞 directly as their own phonetic donor — siblings of 瞭, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 鍛 (6332; 1340 characters remaining).

### 2026-08-10, iteration 1165 — [[characters/鍛|鍛]]

**`mc_id` off-by-one fixed**: stored `3904` pointed to 萋 (the line immediately before); 鍛 itself sits at rank 3905 in `CC 3000.md` — corrected.

**Classification, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 段` is the documented 形聲 phonetic (semantic [[Radical 167|金]] + phonetic [[段 (char)|段]]); `korean_native: 불릴` is an exact match to the literal eumhun "불릴 단"; `japanese_native: きた` is the correct stem of the attested kun'yomi きたえる.

**Vietnamese expanded**: added `đoán`, the reading Wiktionary lists alongside the already-stored `đoàn`, with no differentiation given between the two.

Rebuilt `## Notes` to the standard 4-bullet format, including the Proto-Sino-Tibetan/Burmese cognate note. **`## Words`**: tagged the existing [[鍛錬]] citation "(stand-in for 鍛)"; both it and [[鍛冶]] checked and found already fully perfected, no corruption. **False positive correctly excluded**: [[冶錬]] mentions 鍛 only in cross-referencing prose about how it "legitimately spans both senses" of 冶錬's two derived compounds, not as a genuine citation of its own. **Derived-Characters check**: nothing else in the vault currently cites 段 as a phonetic donor besides 鍛 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 玩 (6333; 1339 characters remaining).

### 2026-08-10, iteration 1166 — [[characters/玩|玩]]

**`mc_id` off-by-one fixed**: stored `2256` pointed to 儲 (the line immediately before); 玩 itself sits at rank 2257 in `CC 2000.md` — corrected.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 元` is the documented 形聲 phonetic (semantic [[Radical 096|玉]] "jade" + phonetic [[元]]); `vietnamese: ngoạn` matches Wiktionary's sole listed reading.

**Two real bugs found and fixed**: `korean_native` was `희롱할` ("to tease/mock") — the raw Wiktionary eumhun template gives only `즐기다`/`즐길` ("to enjoy"), with no support anywhere for "희롱할"; corrected to `즐길`. `japanese_native` was `もちあそ`, a typo for the correct stem of the attested kun'yomi もてあそぶ — corrected to `もてあそ` (も-て-あ-そ, not も-ち-あ-そ).

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, malformed) to the standard 4-bullet format. **`## Words`**: tagged the existing [[玩具]] citation "(stand-in for 玩)". **Bugs fixed on [[玩具]] (word)**: `korean` was a comma-dump (`완구, 장난감`, the second being an unrelated native-Korean synonym) — trimmed to the compositional `완구`; blank `pos` filled → `名詞`. **False positives correctly excluded**: [[遊戯]] and [[意味深長]] both mention 玩/玩味/玩索 only in comparative/illustrative prose, not as genuine citations. **Derived-Characters check**: [[冠]], [[完]], [[翫]], [[阮]], [[頑]] all cite 元 directly as their own phonetic donor — siblings of 玩, not children — correctly excluded (noting [[翫]] is a historically-related variant of 玩 itself but already has its own independent vault page with a different `stand_in`, an existing structural decision left undisturbed rather than merged). **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 椅 (6334; 1338 characters remaining).

### 2026-08-10, iteration 1167 — [[characters/椅|椅]]

**`mc_id: 5829` outside the vault's verifiable range**: 椅 does not appear in `CC 0000`–`CC 3000` and has no aliases to check.

**Classification confirmed correct as-is**: `graphemic_classification: 奇` is the documented 形聲 phonetic (semantic [[Radical 075|木]] + phonetic [[奇]]). **`korean_native: 의자` confirmed correct as-is, an explicit literal match rather than an inferred one**: unlike [[帽]]'s 모자 case last iteration (kept only by absence of a contradicting source), Wiktionary's raw eumhun template for 椅 literally reads "의자(椅子) 의" — the compound word IS the printed gloss, independently corroborating that this vault's compound-as-hun pattern is a genuine, sourced convention rather than just an unverifiable guess.

**Vietnamese expanded**: added `y`, the fourth reading Wiktionary lists that was missing from the stored three (`ghế`, `kỉ`, `ỷ`).

**Malformed Notes bullet fixed**: the semantic-component gloss was an empty string (`("")`) instead of "wood, tree" — filled in; the whole `## Notes`/`## Words` block was otherwise reduced to a single garbled bullet plus two bare CC links (missing SKIP/Stroke, CC-rank, and Grade/HSK/Jōyō/Korean-level bullets, and citing a garbled 注音 `ㄨㄧㄐㄧ` instead of the correct `ㄜㄧㄐㄜ`) — rebuilt entirely to the standard 4-bullet format with the correct ruby. **`## Words`**: tagged the existing [[椅子]] citation "(stand-in for 椅)"; already fully perfected, no corruption. **False positives correctly excluded**: [[燕子]], [[錐子]], [[双子]], [[楔子]], [[折畳]], [[梯子]], [[安楽]], [[於]] all mention 椅子 only as an example within their own `子`-suffix or unrelated discussions, not as genuine citations. **Derived-Characters check**: [[倚 (char)|倚]], [[寄 (char)|寄]], [[埼]], [[騎]] all cite 奇 directly as their own phonetic donor — siblings of 椅, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 喝 (char) (6335; 1337 characters remaining).

### 2026-08-10, iteration 1168 — [[characters/喝 (char)|喝]]

**Multiple real bugs found and fixed, an unusually messy source page**:
- `graphemic_classification` was stored as `"會意"` — a *classification type label*, not a component citation. Wiktionary confirms 喝 is actually 形聲 (semantic [[Radical 030|口]] + phonetic 曷) — corrected to `曷`.
- `mandarin: hē` was the reading for 喝's *other*, unrelated sense ("to drink," Etymology 1) — this character's own stored `english: [yell, shout]` belongs to the separate reading `hè` (Etymology 2, "to shout; scold; brag"). Corrected to `hè`. Independently and exactly corroborated by the citing word [[喝]] (word)'s own prior research, which had already made and documented this identical correction on its own page.
- `aliases: [曷]` was cleared: Wiktionary documents 喝's one genuine alternative form as 欱 (specific to the unrelated "drink" sense, Etymology 1, so not applicable here either) — 曷 is simply the phonetic donor (already captured via the classification fix above), most likely duplicated into `aliases` by the same data-entry confusion that produced the `graphemic_classification` bug.
- **`mc_id` investigated and deliberately left unchanged, a case where the "recorded under alias" pattern does NOT apply**: 曷 independently ranks 1218 in `CC 1000.md`, tempting a substitution — but since 曷 is a wholly separate classical word (the interrogative "what; why"), not a genuine same-word alias of 喝 (same reasoning as [[戴]]/[[代]] two iterations ago), its rank was not borrowed; `喝` itself doesn't appear in any CC list, so `4648` remains documented as unverifiable.

**Vietnamese corrected in both directions**: initially cross-checked against the raw Wiktionary template and swapped the unsupported `ái` for the two additional readings `kháo`/`ha` — but the citing word [[喝]] (word) had already independently verified via deeper research that `ái` **is** genuinely attested for this specific sense ("ái thái," an alternate rendering of 喝采) even though absent from Wiktionary's undifferentiated character-level template — restored it per the standing rule to trust a citing word's own deeper research over raw dictionary data. Final set: `[hát, ái, hét, hít, hết, kệ, ạc, ặc, kháo, ha]`. **`korean_native: 꾸짖을` confirmed correct as-is**, matching Etymology 2's "to scold" sense.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard format, explicitly flagging the hē/hè sense split. **`## Words`**: added the reflexive stand-in [[喝]] — already independently fully perfected (2026-07-27), no further changes needed there. **False positives correctly excluded**: [[杯]] and [[酩酊]] both use 喝 only in the unrelated "drink" sense within prose; [[単刀直入]] and [[焚琴煮鶴]] both mention 喝/喝道 only within quoted prose, not as genuine citations. **Derived-Characters check**: [[掲 (char)|掲]], [[渇 (char)|渇]], [[蝎 (char)|蝎]], [[褐 (char)|褐]], [[謁 (char)|謁]] all cite 曷 directly as their own phonetic donor — siblings of 喝, not children — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 紹 (6336; 1336 characters remaining).

### 2026-08-10, iteration 1169 — [[characters/紹|紹]]

**`mc_id: 1248` verified correct as-is**: checked `CC 1000.md` line 261, confirmed 紹 itself sits at that rank.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 召` is the documented 形聲 phonetic (semantic [[Radical 120|糸]] + phonetic [[召]]); `vietnamese: [chão, thiệu]` is an exact match (reordered) to Wiktionary. **`korean_native: 이을` left as-is**: Wiktionary's eumhun field is genuinely empty, but "이을" ("to link, continue") fits the etymological "to continue; to link up" sense precisely — kept without a contradicting source.

Filled empty `pos` → `事詞`. **`# Notes` was a bare two-link stub under the wrong heading level** — rebuilt to the standard 4-bullet format. **`## Words`**: tagged the existing [[介紹]] citation "(stand-in for 紹)"; already fully perfected (2026-07-16), no corruption. **False positives correctly excluded**: [[安慰]], [[呼吸]], [[羽毛]], [[母親]] all mention 介紹/紹介 only as a comparison example for the "reversed compound word order" phenomenon discussed elsewhere in this sweep, not as genuine citations. **Derived-Characters check**: [[昭 (char)|昭]], [[超 (char)|超]], [[劭]], [[招]], [[沼]], [[詔]], [[貂]], [[邵]] all cite 召 directly as their own phonetic donor — siblings of 紹, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 搬 (6337; 1335 characters remaining).

### 2026-08-10, iteration 1170 — [[characters/搬|搬]]

**`mc_id: 0` confirmed correct as-is**: 搬 does not appear in `CC 0000`–`CC 3000` and has no aliases — a genuine late/vernacular character.

**Classification confirmed correct as-is**: `graphemic_classification: 般` is the documented 形聲 phonetic (semantic [[Radical 064|手]] + phonetic [[般 (char)|般]]). **Vietnamese narrowed**: removed `bâng`, unsupported anywhere in Wiktionary's reading set `[ban, bàn (Hán Việt), bưng (Nôm)]`. **`korean_native: 옮길` left as-is**: Wiktionary's eumhun field is genuinely empty, but "옮길" ("to move, transfer") fits the "convey" sense precisely — kept without a contradicting source.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[搬送]] citation "(stand-in for 搬)". **Real bugs fixed on [[搬送]] (word)**: blank `cantonese` filled by composing from its constituents (bun1 + sung3 → `bun1 sung3`); it had no `## Notes` section at all — added the standard etymology line. `vietnamese` left blank rather than guessed at (no quick confirmed source found). **Derived-Characters check**: [[盤 (char)|盤]] and [[磐]] both cite 般 directly as their own phonetic donor — siblings of 搬, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 飾 (6338; 1334 characters remaining).

### 2026-08-10, iteration 1171 — [[characters/飾|飾]]

**Real classification bug found and fixed, similar to [[喝]] two iterations ago**: stored `graphemic_classification: 會意` was a type label, not a component — and the wrong type besides: Wiktionary confirms 飾 is 形聲 (semantic [[巾]] "cloth" + phonetic 飤), not 會意. Chased one level further: 飤 has no vault page, but Wiktionary explicitly states "this character is a variant form of 飼" — and [[飼]] (perfected earlier this sweep) does have a page, so corrected `graphemic_classification` to `飼` per the established same-word-alias-substitution pattern (as with [[填]]→真, [[剰]]→乗). Documented the Kangxi radical/etymological-semantic divergence directly in the Notes (dictionary radical 食 vs. true semantic 巾).

**`mc_id: 880` and korean_native/Vietnamese all confirmed correct as-is**: checked `CC 0000.md` line 910, confirmed 飾 sits at that rank; `vietnamese: sức` and `korean_native: 꾸밀` are both exact matches to the raw Wiktionary templates.

**Real `stand_in` bug found and fixed**: stored `裝飾` (traditional form) doesn't correspond to any file — the actual word page is `装飾.md` (shinjitai), which itself lists 裝飾 among its own `aliases`. Corrected `stand_in` to `装飾` per the standing alias-points-to-parent-form rule.

Filled empty `pos` → `事詞`. Reordered Notes/Words/Chengyu into standard order (was Notes→Chengyu→Words). **`## Words`**: tagged the [[装飾]] citation "(stand-in for 飾; alias: 裝飾)"; [[修飾語]] and the existing `## Chengyu` entry [[修飾先行]] both verified as genuine citations, already fully perfected. **~50 false positives correctly excluded**: the overwhelming majority of the initial grep hits were words whose `pos`/`品詞` value is the grammatical label `修飾語` ("modifier") — a substring match on 飾, not a genuine citation — filtered out by checking the `characters` field specifically. **Derived-Characters check**: nothing in the vault currently cites 飾 (or its corrected donor 飼) as a further phonetic donor.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 瓶 (char) (6339; 1333 characters remaining).

### 2026-08-10, iteration 1172 — [[characters/瓶 (char)|瓶]]

**`mc_id: 4170` outside the vault's verifiable range**: 瓶 does not appear in `CC 0000`–`CC 3000` and has no aliases.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 并` is the documented 形聲 phonetic (semantic [[Radical 098|瓦]] + phonetic 并, pageless in this vault); `vietnamese: bình` matches Wiktionary's sole reading. **`korean_native: 병` confirmed correct as-is, a self-identical case**: identical to the `korean` field, matching the established pattern (cf. [[窟]]'s 굴=굴) where a Sino-Korean loanword became the ordinary everyday word with no separate native counterpart — Wiktionary's Korean entry gives no other gloss to contradict this.

**Completed a pending reciprocal homophone callout**: [[並]] (word)'s own page (perfected 2026-07-26) explicitly noted "the reciprocal half of this callout will be completed when it comes up" for its exact Dan'a'yo-reading match with [[瓶]] (beng/벙/ㄅㄝㄫ) — added the matching `>[!warning] Homophones` callout to [[瓶]] (word) now that its turn arrived. **Bugs fixed on [[瓶]] (word)**: blank `korean` and `vietnamese` fields filled (`병`, `bình`, matching the character page); malformed `# Notes` stub replaced with the standard citation plus the homophone cross-reference note.

Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[瓶]]. **Derived-Characters check**: [[餅 (char)|餅]], [[屏]], [[拼]] all cite 并 directly as their own phonetic donor — siblings of 瓶, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 麺 (char) (6340; 1332 characters remaining).

### 2026-08-10, iteration 1173 — [[characters/麺 (char)|麺]]

**`mc_id: 10656` outside the vault's verifiable range**: neither 麺 nor its aliases 麵/麪 appear in `CC 0000`–`CC 3000`.

**Classification, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 面` verified against the traditional donor [[麵]]'s own etymology (形聲: semantic 麥/[[麦]] + phonetic [[面]]); `korean_native: 국수` ("noodles," a genuine native Korean word) fits the character's own extended "noodles" sense; `japanese_native: むぎこ` is an exact match to the attested kun'yomi.

**Vietnamese expanded**: stored `[miến]` was missing two of the three readings Wiktionary lists on the traditional-form page 麵 (`diện`, `mì`, `miến`) — added `diện` and `mì`.

Rebuilt `## Notes` (malformed: a bare components list plus a stray `## Words`-style bullet appended directly underneath with no proper heading) to the standard format, including the shinjitai/traditional-form relationship. **`## Words`** expanded from one entry to five: added the reflexive stand-in [[麺]], plus three newly-found genuine citations [[拉麺]], [[冷麺]], [[烏龍麺]], alongside the existing [[麺包]]. **Bugs fixed on [[烏龍麺]] (word)**: blank `pos` filled → `名詞`; had no `## Notes` section at all — added one explaining the "black dragon noodles" literal rendering and the udon-loanword pronunciation pattern shared with Korean 우동. **False positives correctly excluded**: [[書面]], [[白粉]], [[芝麻醤]], [[冷]] don't cite 麺 in their `characters` field. **Derived-Characters check**: nothing else in the vault currently cites 面 as a phonetic donor besides 麺 itself. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 禍 (6341; 1331 characters remaining).

### 2026-08-10, iteration 1174 — [[characters/禍|禍]]

**`mc_id: 459` verified correct as-is**: checked `CC 0000.md` line 477, confirmed 禍 itself sits at that rank.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 咼` is the documented 形聲 phonetic (semantic [[Radical 113|示]] + phonetic [[咼]]); `vietnamese: [hoạ, vạ]` matches Wiktionary. **`korean_native: 재앙` left as-is**: Wiktionary's eumhun field is genuinely empty, but "재앙" ("disaster, calamity") is the well-established traditional gloss — kept without a contradicting source.

Filled empty `pos` → `名詞`. Rebuilt `## Notes`/`## Words` (reversed order, wrong heading level, malformed) to the standard format. **`## Words`** expanded from two entries to three: tagged the existing [[引禍]] citation, added [[禍害]] (already fully perfected), and added the reflexive stand-in [[禍事]]. **New `## Chengyu` section added**: [[招災引禍]] and [[禍延子孫]] both genuinely cite 禍 in their `characters` field; [[呉越同舟]]'s hit was a false positive (quoted classical proverb in prose). **Bugs fixed on [[禍事]] (word)**: blank `cantonese` filled by composition (wo6 + si6 → `wo6 si6`); had no `## Notes` section at all — added the standard citation. **False positive correctly excluded**: [[招災]] mentions 禍/引禍/招災引禍 only in cross-referencing prose, not as a genuine citation. **Derived-Characters check**: [[過 (char)|過]], [[鍋 (char)|鍋]], [[渦]], [[窩]], [[蝸]] all cite 咼 directly as their own phonetic donor — siblings of 禍, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 屯 (char) (6342; 1330 characters remaining).

### 2026-08-10, iteration 1175 — [[characters/屯 (char)|屯]]

**`mc_id: 930` verified correct as-is**: checked `CC 0000.md` line 963, confirmed 屯 itself sits at that rank.

**Classification confirmed correct as-is**: `graphemic_classification: 象形` matches Wiktionary's glyph origin (a swollen sprout/bud emerging, original form of 芚). **`korean_native: 진칠` confirmed correct as-is**, exact match to the literal eumhun "진칠 둔" (correctly the "village/camp/station" sense, not the unrelated "difficult" sense 준 also listed on the same page).

**Vietnamese drastically narrowed, another severe undifferentiated-list case**: stored 16 entries, all drawn from Wiktionary's own single undifferentiated 14-item reading list (no Hán Việt/Nôm split given at all in the source) — plus two entries (`giùn`, `rùn`) with no support anywhere. Narrowed to just `[truân]`, the one reading that phonetically parallels the Sino-Mandarin/Cantonese cognate pattern (tún/tyun4) rather than reading as a native Vietnamese word; the rest read as scribal Nôm phonetic loans unrelated to this character's core "village; camp" meaning.

Filled empty `pos` → `名詞`. Rebuilt `## Notes` to the standard format, preserving the existing pictographic-origin description and Korean-HS-list-addition note. **`## Words`**: added the reflexive stand-in [[屯]] alongside the existing [[駐屯]]. **New `## Derived Characters` section added**: [[春 (char)|春]], [[沌]], [[純]], [[鈍]], [[頓]] all cite 屯 as their own phonetic donor — genuine children, not siblings, since 屯 (unlike most donors handled this sweep) is itself 象形 rather than another 形聲 character's derivative. **Bugs fixed on [[屯]] (word)**: blank `vietnamese` filled → `truân`; empty `# Notes` stub filled with the standard citation. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 沙 (char) (6343; 1329 characters remaining).

### 2026-08-10, iteration 1176 — [[characters/沙 (char)|沙]]

**`mc_id: 1146` verified correct as-is**: checked `CC 1000.md` line 155, confirmed 沙 itself sits at that rank.

**`graphemic_classification: 會意` confirmed correct as-is — an important distinction from the [[喝]]/[[飾]] bugs two and five iterations ago**: those were miscategorized (wrongly labeled 會意 when actually 形聲). Here Wiktionary genuinely confirms 沙 is 會意 (水 "water" + 少 "dots" — sand scattered on a shoreline), and checking the vault's own precedent ([[与]] (char), also genuine 會意) confirmed that storing the bare type label is the *correct*, established convention for true semantic-only compounds — not a bug pattern to correct on sight.

**`korean_native: 모래` confirmed correct as-is**, exact match to the raw Wiktionary template.

**Vietnamese expanded**: stored `[nhểu, sa, sà, xoà]` was missing two of Wiktionary's six readings — the second Hán Việt reading `sá` and the Nôm reading `xa` — added both.

Filled empty `pos` → `名詞`. **`# Notes` mixed etymology, CC links, and four `## Words`-style bullets together under one malformed heading** — separated and rebuilt into proper `## Notes`/`## Words` sections. **`## Words`** expanded from four entries to nine: added the reflexive stand-in [[沙]], plus four newly-found genuine citations [[黄沙]], [[丹砂]], [[朱沙]], [[珈沙]], alongside the four already present. **Bugs fixed on [[沙]] (word)**: blank `vietnamese` filled → `sa`; empty `# Notes` stub filled with the standard citation. **`aliases` (裟/砂/娑/䓾) checked for Derived-Characters implications**: none have their own vault pages, so no `## Derived Characters` section applies. **False positive correctly excluded**: [[盛者必衰]] mentions 沙羅双樹 only within a quoted *Heike Monogatari* passage, not as a genuine citation.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 崩 (char) (6344; 1327 characters remaining).

### 2026-08-10, iteration 1177 — [[characters/崩 (char)|崩]]

**`mc_id: 726` verified correct as-is**: checked `CC 0000.md` line 753, confirmed 崩 itself sits at that rank.

**Classification confirmed correct as-is**: `graphemic_classification: 朋` is the documented 形聲 phonetic (semantic [[Radical 046|山]] + phonetic [[朋]]). **`korean_native: 무너질` left as-is**: Wiktionary's eumhun field is empty, but "무너질" ("to collapse") fits the "crumble, disintegrate, fall apart" sense precisely.

**Vietnamese expanded**: stored `[băng]` was missing three of Wiktionary's four undifferentiated readings — added `bẵng`, `bâng`, `bông`.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[崩]] alongside the two newly-found genuine citations [[山崩]] and [[雪崩]]. **Bug fixed on [[崩]] (word)**: literal `vietnamese: "null"` corrected to `băng`; empty `# Notes` stub filled with the standard citation. **False positive correctly excluded**: [[山]] mentions 山崩 only as one example within its own large compound-family discussion, not as a genuine citation. **Derived-Characters check**: [[棚 (char)|棚]] and [[硼]] both cite 朋 directly as their own phonetic donor — siblings of 崩, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 慄 (char) (6346; 1326 characters remaining).

### 2026-08-10, iteration 1178 — [[characters/慄 (char)|慄]]

**`mc_id: 2316` verified correct as-is**: checked `CC 2000.md` line 333, confirmed 慄 itself sits at that rank.

**`aliases: [栗]` investigated and confirmed genuine, a useful contrast with the [[喝]]/曷 false-alias bug several iterations ago**: 栗 here is not just the phonetic donor mistakenly duplicated in — Wiktionary explicitly states "trad. 慄 / simp. 栗," meaning 慄 and 栗 (in this specific "tremble" sense) are genuinely the same word across script reforms, simplified Chinese having collapsed it onto the unrelated "chestnut" character. `graphemic_classification: 栗` confirmed correct as-is (matches the documented 形聲 phonetic).

**Vietnamese expanded**: stored `[lật, rất]` was missing `trật`, the third reading Wiktionary lists among 慄's Nôm forms. **`korean_native: 떨릴` left as-is**: Wiktionary provides no native gloss, but "떨릴" ("to tremble") fits the sense precisely.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format, documenting the traditional/simplified relationship directly. **`## Words`**: added the reflexive stand-in [[慄]] — the only citation found in the vault. **Bug fixed on [[慄]] (word)**: literal `vietnamese: "null"` corrected to `lật`; empty `# Notes` stub filled with the standard citation. **Derived-Characters check**: nothing else in the vault currently cites 栗 as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 玄 (char) (6347; 1325 characters remaining).

### 2026-08-10, iteration 1179 — [[characters/玄 (char)|玄]]

**`mc_id: 659` verified correct as-is**: checked `CC 0000.md` line 683, confirmed 玄 itself sits at that rank.

**Real classification bug found and fixed**: stored `graphemic_classification: 象形` — Wiktionary's raw glyph-origin template is explicitly `{{liushu|i}}` (ideogrammic, not pictographic): "two interwoven threads 幺 with a distinguishing mark 亠 on top." Corrected to `指事`, confirmed as an established bare-type-label convention in this vault (cf. [[上]], [[六]], [[下]]).

**Real spurious-alias bug found and fixed, a second instance of the [[喝]]/曷 pattern**: `aliases: [眩]` — Wiktionary confirms 眩 is simply a 形聲 *derivative* of 玄 (semantic 目 + phonetic 玄, "dizzy"), never described as a variant or same word as 玄 itself. Cleared the field; 眩 has no vault page, so it was excluded from the new Derived Characters section below rather than force-linked.

**Vietnamese and korean_native confirmed correct as-is**: `vietnamese: huyền` matches Wiktionary's sole reading; `korean_native: 검을` ("black") fits the character's original color-term sense precisely despite no eumhun being given directly.

Rebuilt `## Notes`/`## Words` (a bare radical citation plus four unrubied, unglossed bullets) to the standard format. **`## Words`** expanded from four entries to six: added the reflexive stand-in [[玄]] (word) — already independently fully perfected 2026-08-02, and whose own Notes explicitly flagged this character page as "largely unperfected... for the separate character-perfection sweep," confirming this was the correct pending task — plus the newly-found [[玄暈]], alongside properly-rubied versions of the existing four. **New `## Derived Characters` section added**: [[弦 (char)|弦]], [[牽]], [[舷]] all cite 玄 directly as their own phonetic donor. **False positives correctly excluded**: [[米]], [[太陰]], [[南亜]], [[九数]], [[臼]], [[九族]], [[五色]], [[禾]], [[五方]], [[黒暗]], [[巴基斯坦]], [[才媛]], [[県]], [[懸]], [[深淵]] don't cite 玄 in their `characters` field; five chengyu hits were likewise all false positives.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 戒 (6348; 1324 characters remaining).

### 2026-08-10, iteration 1180 — [[characters/戒|戒]]

**`mc_id: 832` verified correct as-is**: checked `CC 0000.md` line 862, confirmed 戒 itself sits at that rank. **Classification confirmed correct as-is**: `graphemic_classification: 會意` matches Wiktionary (戈 "halberd" + 廾 "hands," a bare type-label consistent with this vault's established 會意 convention).

**Real spurious-alias bug found and fixed, a third instance of the pattern**: `aliases: [誡, 誨]` — 誡 confirmed genuine (Wiktionary explicitly calls it "the second-round simplified form of 戒"), but 誨 is a wholly unrelated, independently-etymologized character (形聲: semantic 言 + phonetic 每, meaning "to teach/instruct") with no documented variant relationship to 戒 at all. Removed 誨 (no vault page exists for it either).

**Vietnamese narrowed**: stored `[giái, giới]` — the raw Wiktionary template lists only `giới`, with `giái` unsupported anywhere; removed. **`korean_native: 경계할` confirmed correct as-is**, exact match to the literal eumhun "경계할 계."

Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`** expanded from five entries to six: tagged the existing [[警戒]] stand-in and added the newly-found genuine citation [[破戒]]. **New `## Derived Characters` section added**: [[械]] cites 戒 directly as its own phonetic donor. **False positives correctly excluded**: seven chengyu hits, all likely Ten-Commandments-adjacent prose mentions (誡命/十誡), none citing 戒/誡 in their own `characters` field.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 惑 (char) (6349; 1323 characters remaining).

### 2026-08-10, iteration 1181 — [[characters/惑 (char)|惑]]

**A clean cycle — `mc_id: 803`, classification, Vietnamese, and korean_native all confirmed correct as-is**: checked `CC 0000.md` line 833, confirmed 惑 itself sits at that rank; `graphemic_classification: 或` matches Wiktionary (semantic [[Radical 061|心]] + phonetic [[或 (char)|或]]); `vietnamese: hoặc` and `korean_native: 미혹할` are both exact matches to Wiktionary.

Rebuilt `## Notes` (bare two-link stub) to the standard 4-bullet format, including the exact-homophone relationship with [[或]] — already correctly documented and reciprocally cross-linked on both [[惑]] (word, perfected 2026-07-11) and [[或]] (word)'s own pages, no action needed there. **`## Words`**: added the reflexive stand-in [[惑]] alongside the existing [[魅惑]]. **False positives correctly excluded**: [[行星]] and [[小行星]] list 惑星/小惑星 only as `aliases`, not `characters`, citations; [[流言飛語]]'s hit was 惑わされて used as an ordinary verb in an example sentence. **Derived-Characters check**: [[域 (char)|域]] and [[国]] both cite 或 directly as their own phonetic donor — siblings of 惑, not children — correctly excluded; nothing derives from 惑 itself. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 拓 (6350; 1322 characters remaining).

### 2026-08-10, iteration 1182 — [[characters/拓|拓]]

**Unusually complex multi-etymology case, investigated rather than force-corrected**: 拓 graphically collapses two originally distinct Middle Chinese words — (1) 척/tuò "to expand, open up, pioneer" (used in [[開拓]], kāituò/개척) and (2) 탁/tà, OC \*tʰaːɡ, "to inscribe, take a rubbing; to push, shove" (used in 拓本, tàběn/탁본). The stored `mandarin: tà`/`korean: 탁`/`middle_chinese_*` fields all track etymology (2) specifically, while `english`/`stand_in: 開拓` draw from etymology (1) — an apparent mismatch at first glance. Resolved by checking [[開拓]] (word)'s own already-populated data: its Dan'a'yo-derived 諺文/羅馬字 for 拓 (탁/tag) already matches the character page's current phonology exactly, while its `korean: 개척` (real Sino-Korean, using 척) diverges — confirming this vault deliberately derives 拓's Dan'a'yo syllable from the 탁/etymology-2 Middle Chinese ancestry regardless of which sense dominates the `stand_in`, a divergence pattern analogous to a `kwin: false` case but baked into the phonology fields themselves rather than a boolean flag. Left `mandarin`/`korean`/`middle_chinese_*` untouched to preserve consistency with [[開拓]]'s already-established derivation; documented the full tension explicitly in the Notes instead of guessing at a "fix" that would have broken that consistency.

**`korean_native` corrected within this same investigation**: stored `열` matched neither etymology's literal eumhun — corrected to `박을`, the literal hun tied specifically to the 탁/etymology-2 reading this page's phonology actually derives from (Wiktionary: `{{ko-hanja|박다|박을|탁}}`).

**Vietnamese corrected**: removed `đo` (unsupported anywhere in Wiktionary's reading set); added `tháp` and `chích`, both genuinely listed Hán Việt readings.

**`mc_id: 4343` outside the vault's verifiable range**: 拓 doesn't appear in `CC 0000`–`CC 3000`.

Filled empty `pos` → `事詞`. **Fixed a malformed relative-path link** (`[[../lookup/CC/finals/韻 鈬開]]`, missing the vault-standard `Lookup/CC/finals/` prefix format) and rebuilt the whole `## Notes` to the standard format, preserving the existing "Korean Name List vs Korean HS" categorization note. **`## Words`**: added the reflexive stand-in [[開拓]] (not yet through its own turn in the word-perfecting loop, left otherwise untouched). **Derived-Characters check**: [[妬]], [[庶]], [[橐]], [[碩]] all cite 石 directly as their own phonetic donor — siblings of 拓, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 怠 (6351; 1321 characters remaining).

### 2026-08-10, iteration 1183 — [[characters/怠|怠]]

**`mc_id` off-by-one fixed**: stored `1421` pointed to 溢 (the line immediately before); 怠 itself sits at rank 1422 in `CC 1000.md` — corrected.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 台` is the documented 形聲 phonetic (semantic [[Radical 061|心]] + phonetic [[台 (char)|台]]); `vietnamese: đãi` matches Wiktionary's sole reading. **`korean_native: 게으를` left as-is**: Wiktionary's eumhun field is empty, but "게으를" ("lazy") is the well-established traditional gloss.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[怠惰]] citation "(stand-in for 怠)" and explicitly confirmed the `#cranberry` transitivity — [[惰]]'s own `stand_in` also points to 怠惰, satisfying A=B=AB. **False positive correctly excluded**: [[臨渇掘井]] uses 怠らない as an ordinary verb in commentary prose, not a genuine citation. **Derived-Characters check**: [[苔 (char)|苔]], [[始]], [[治]], [[殆]], [[胎]], [[跆]], [[飴]], [[鮐]] all cite 台 directly as their own phonetic donor — siblings of 怠, not children — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 恭 (6352; 1320 characters remaining).

### 2026-08-10, iteration 1184 — [[characters/恭|恭]]

**A clean cycle — `mc_id: 779`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 806, confirmed 恭 itself sits at that rank; `graphemic_classification: 共` matches Wiktionary (semantic [[Radical 061|心]] + phonetic [[共 (char)|共]]); `vietnamese: cung`, `korean_native: 공손할`, and `japanese_native: うやうや` are all exact matches.

Filled empty `pos` → `性詞`. **`# Notes` had four unrubied, unglossed-format bullets crammed under the wrong heading alongside bare CC links** — rebuilt to the standard 4-bullet format, then properly rubied and re-cited all four existing Words entries ([[恭敬]] tagged as the stand-in, [[恭喜]], [[恭賀]], [[恭喜発財]]), all checked and found free of corruption. **False positive correctly excluded**: [[巧言]] mentions 足恭 only in Confucian-commentary prose, not as a genuine citation. **Derived-Characters check**: [[拱 (char)|拱]], [[供]], [[哄]], [[洪]] all cite 共 directly as their own phonetic donor — siblings of 恭, not children — correctly excluded. **Chengyu**: no hits (恭喜発財 lives in `words/`, not `chengyu/`, per its existing categorization).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 芳 (6353; 1319 characters remaining).

### 2026-08-10, iteration 1185 — [[characters/芳|芳]]

**`mc_id: 1913` verified correct as-is**: checked `CC 1000.md` line 954, confirmed 芳 itself sits at that rank.

**Classification, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 方` is the documented 形聲 phonetic (semantic [[Radical 140|艸]] + phonetic [[方 (char)|方]]); `korean_native: 꽃다울` matches the literal eumhun "꽃다울 방" exactly; `japanese_native: かんば` is the correct stem of the attested kun'yomi かんばしい.

**Vietnamese expanded**: added `phưng`, the second reading Wiktionary lists (`phương, phưng (phức)`) alongside the already-stored `phương`.

`pos: 性詞` was already filled. Rebuilt `## Notes` (bare two-link stub) to the standard 4-bullet format. **`## Words`** expanded from one entry to three: added the reflexive stand-in [[芳香]] and the newly-found [[芳香族]], alongside the existing [[芬芳]]. **False positives correctly excluded**: [[方向]] and [[方響]] don't cite 芳 in their `characters` field. **Derived-Characters check**: [[房 (char)|房]], [[紡 (char)|紡]], [[肪 (char)|肪]], [[坊]], [[妨]], [[彷]], [[旁]], [[放]], [[訪]], [[防]] all cite 方 directly as their own phonetic donor — siblings of 芳, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 幽 (char) (6354; 1318 characters remaining).

### 2026-08-10, iteration 1186 — [[characters/幽 (char)|幽]]

**`mc_id: 868` verified correct as-is**: checked `CC 0000.md` line 898, confirmed 幽 itself sits at that rank.

**Real classification bug found and fixed, a fourth instance of the type-mislabel pattern**: stored `graphemic_classification: 會意` — Wiktionary's raw glyph-origin template is explicitly `ls=psc` (phono-semantic compound), with phonetic 𢆶 and semantic 山 (originally 火 in oracle bone script). Corrected to `𢆶` (pageless in this vault, kept unlinked per established convention). Confirmed the stored `radical: 幺` remains correct — Wiktionary's own sort key (`sort=幺06`) matches, another Kangxi-radical-vs-etymological-semantic divergence like [[飾]]'s.

**Vietnamese and korean_native/japanese_native all confirmed correct as-is**: `vietnamese: [u, ù]` matches Wiktionary exactly; `korean_native: 그윽할` fits "quiet, secluded" precisely despite no eumhun being given directly; `japanese_native: かす` is the correct stem of the attested kun'yomi かすか.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[幽]] alongside the newly-found [[幽鬼]]. **Bug fixed on [[幽]] (word)**: blank `vietnamese` filled → `u`; empty `# Notes` stub filled with the standard citation. **False positive correctly excluded**: [[空前絶後]] mentions 幽州 (a place name) only within a poem-title citation, not as a genuine character citation. **Derived-Characters check**: nothing else in the vault cites 𢆶 or 幽 itself as a phonetic donor. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 雅 (6355; 1317 characters remaining).

### 2026-08-10, iteration 1187 — [[characters/雅|雅]]

**`mc_id: 1337` verified correct as-is**: checked `CC 1000.md` line 354, confirmed 雅 itself sits at that rank. **Classification confirmed correct as-is**: `graphemic_classification: 牙` matches Wiktionary (semantic [[Radical 172|隹]] + phonetic [[牙 (char)|牙]]).

**Two real bugs found and fixed**: `vietnamese` had an unsupported second entry `nhả` — the raw Wiktionary template lists only `nhã`; removed. `korean_native` was `바를` ("correct, upright") — semantically unrelated to "elegant, refined, graceful" and matching neither of Wiktionary's two literal eumhun entries (`맑을`/"clear, pure" or `아담할`/"neat, quaint"); corrected to `아담할`, the closer semantic fit to this character's own stored `english: graceful`.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, one bare bullet mixed with CC links) to the standard format. **`## Words`**: tagged the existing [[雅楽]] citation and added the reflexive stand-in [[典雅]]. **New `## Chengyu` section added**: [[信達雅化]] genuinely cites 雅 in its `characters` field; five other chengyu hits were all false positives (prose mentions). **Derived-Characters check**: [[耶 (char)|耶]], [[芽]], [[邪]] all cite 牙 directly as their own phonetic donor — siblings of 雅, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 蔽 (6356; 1316 characters remaining).

### 2026-08-10, iteration 1188 — [[characters/蔽|蔽]]

**A clean cycle — `mc_id: 1127` and classification confirmed correct as-is**: checked `CC 1000.md` line 136, confirmed 蔽 itself sits at that rank; `graphemic_classification: 敝` matches Wiktionary (semantic [[Radical 140|艸]] + phonetic 敝, pageless in this vault).

**Vietnamese expanded**: added `phất`, the second Hán Việt reading Wiktionary lists alongside the already-stored `tế`. **`korean_native: 덮을` left as-is**: Wiktionary provides no eumhun for any of this character's three Korean readings (폐/별/불), but "덮을" ("to cover") fits the "cover, hide, conceal" sense precisely. **`japanese_native: おお` confirmed correct as-is**, exact stem match to the attested kun'yomi おおう.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[隠蔽]] alongside the newly-found [[遮蔽]]. **False positives correctly excluded**: [[詩作]] and [[壅]] don't cite 蔽 in their `characters` field. **Derived-Characters check**: [[幣 (char)|幣]], [[弊 (char)|弊]], [[撇 (char)|撇]], [[鼈 (char)|鼈]], [[瞥]] all cite 敝 directly as their own phonetic donor — siblings of 蔽, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 陶 (6357; 1315 characters remaining).

### 2026-08-10, iteration 1189 — [[characters/陶|陶]]

**`mc_id: 1032` verified correct as-is**: checked `CC 1000.md` line 37, confirmed 陶 itself sits at that rank. **Classification confirmed correct as-is**: `graphemic_classification: 匋` matches Wiktionary (semantic [[Radical 170|阜]] + phonetic 匋, pageless in this vault, also 陶's own original form).

**Real spurious-alias bug found and fixed, a fifth instance of the pattern**: `aliases: [匋, 淘]` — 匋 confirmed genuine (explicitly 陶's own original form), but 淘 is a distinct sibling character (semantic 氵 "water" + the same phonetic 匋) never described as a variant of 陶 — Wiktionary explicitly separates them ("淘 and 陶 are presented as distinct characters rather than variants"). Removed 淘 (no vault page exists for it either).

**Vietnamese expanded**: added `giao`, the second Hán Việt reading Wiktionary lists alongside the already-stored `đào`. **`korean_native: 질그릇` confirmed correct as-is**, matching the literal eumhun "질그릇 도" (pottery vessel) almost exactly.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, two `## Words`-style bullets crammed underneath) to the standard 4-bullet format. **`## Words`** expanded from two entries to four: added the reflexive stand-in [[陶器]] and the newly-found [[陶瓷]], alongside the existing [[陶瓷器]] and [[陶汰]]. **False positives correctly excluded**: [[漏洩]] and [[道]] don't cite 陶 in their `characters` field; [[鼠世桃源]]'s hit was the author name 陶淵明 in prose. **Derived-Characters check**: nothing else in the vault currently cites 匋 as a phonetic donor. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 拙 (6358; 1314 characters remaining).

### 2026-08-10, iteration 1190 — [[characters/拙|拙]]

**`mc_id: 2268` verified correct as-is**: checked `CC 2000.md` line 281, confirmed 拙 itself sits at that rank. **Classification confirmed correct as-is**: `graphemic_classification: 出` matches Wiktionary's raw `ls=psc` template (semantic [[Radical 064|扌]] + phonetic [[出 (char)|出]]).

**Vietnamese drastically narrowed, another severe undifferentiated-list case**: stored 12 entries (2 with zero support anywhere: `choẹt`, `xọt`), all drawn from Wiktionary's own 10-item undifferentiated Nôm pile — while the one explicitly-labeled Hán Việt reading, `chuyết`, sat buried inside that same pile rather than being called out. Narrowed to just `[chuyết]`, independently corroborated by the citing word [[拙劣]] (already perfected), whose own `vietnamese: chuyết liệt` confirms this is the genuine reading. **`korean_native: 옹졸할` left as-is**: Wiktionary's eumhun field is empty; "옹졸할" ("narrow-minded, petty") is a plausible secondary/extended sense of this character in Korean pedagogical tradition, kept without a contradicting source.

Filled empty `pos` → `性詞`. Rebuilt the reversed/malformed `## Words`/`## Notes` (Words appearing before a bare two-link Notes stub) into the standard order and format. **`## Words`**: tagged the existing [[拙劣]] citation "(stand-in for 拙)" — the only citation found. **Derived-Characters check**: [[屈 (char)|屈]] and [[黜]] both cite 出 directly as their own phonetic donor — siblings of 拙, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 醜 (6359; 1313 characters remaining).

### 2026-08-10, iteration 1191 — [[characters/醜|醜]]

**`mc_id: 1368` verified correct as-is**: checked `CC 1000.md` line 385, confirmed 醜 itself sits at that rank.

**Notes prose etymology bullet was doubly wrong, same pattern as [[屈]]/[[那]] earlier this sweep**: the existing text read "semantic 酉 ('ghost, demon') + phonetic 鬼" — reversed and mislabeled on every count. Wiktionary confirms semantic is [[鬼 (char)|鬼]] ("ghost, demon" — the actual etymological reasoning, "demons are ugly") and phonetic is [[Radical 164|酉]] (OC \*luʔ); the stored `graphemic_classification: 酉` field itself was already correct throughout, only the prose was garbled.

**Real spurious-alias bug found and fixed, a sixth instance of the pattern**: `aliases: [丑, 麤, 麁]` — 丑 confirmed genuine (Wiktionary explicitly names it 醜's simplified form), but 麤 ("distant; coarse; variant of 粗") and 麁 (a variant of 麤 itself) are both unrelated characters, connected to 醜 only via a documented *Korean lexical substitution* (identical pronunciation/similar semantics, not shared identity) — not genuine variants. Removed both (neither has a vault page). Also noted in the Notes that 丑 itself carries a second, much older, unrelated "earthly branch; ox" sense with its own separate vault page ([[丑]]) — a legitimate polysemy-across-simplification case, not a duplicate-page conflict like [[准]]/[[準]] flagged earlier this sweep.

**Vietnamese expanded**: added `xâu`, the seventh reading Wiktionary lists that was missing from the stored six. **`korean_native: 추할` confirmed correct as-is**, matching the literal eumhun ("ugly looking, homely; disgraceful").

`pos: 性詞` was already filled. Rebuilt `## Notes` to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[醜悪]] alongside the existing [[醜陋]]. **Careful disambiguation on the 丑-citation sweep**: [[丑月]] cites "丑" in its `characters` field, but this points to 丑's own separate earthly-branch-sense page, not to 醜's simplified-form alias relationship — correctly excluded from 醜's own Words section. [[地支]], [[跳梁]], [[季冬]], [[十干]] don't cite either character in their `characters` field; [[跳梁跋扈]]'s hit was 丑 used in yet a third sense (the clown/buffoon 丑角 role) within prose. **Derived-Characters check**: [[酒]] cites 酉 directly as its own component — a sibling, not a child of 醜 — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 恋 (char) (6360; 1312 characters remaining).

### 2026-08-10, iteration 1192 — [[characters/恋 (char)|恋]]

**`mc_id` off-by-one fixed, a "recorded under alias" case**: stored `3590` pointed to 憒 (the line immediately before); 恋 itself doesn't appear in the CC lists directly, but its alias 戀 sits at rank 3591 in `CC 3000.md` — corrected to 3591, genuinely recorded under the traditional-form alias (unlike the [[戴]]/代 or [[喝]]/曷 false-alias cases, 戀 is confirmed as the direct same-word traditional form via Wiktionary's own shinjitai note).

**Real korean_native bug found and fixed**: stored `그릴` (from 그리다, "to draw/long for") doesn't match the literal Wiktionary eumhun at all — the raw template gives "사모할" (from 사모하다, "to yearn for, adore"). Corrected.

**Real spurious-alias bug found and fixed, a seventh instance of the pattern**: `aliases: [戀, 㜻]` — 戀 confirmed genuine (explicitly the traditional/shinjitai pair), but 㜻 is explicitly "a variant form of 孌" (a different character meaning "lovely, docile"), not of 戀/恋 at all — merely built using 戀 as its own phonetic component. Removed (neither 㜻 nor 孌 has a vault page).

**Vietnamese expanded**: added `luýnh`, the Nôm reading Wiktionary lists alongside the already-stored Hán Việt `luyến`. **Classification confirmed correct as-is**: `graphemic_classification: 䜌` matches Wiktionary (semantic [[Radical 061|心]] + phonetic 䜌, pageless in this vault).

Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[恋]] — the only citation found. **Double bug fixed on [[恋]] (word)**: both `vietnamese: "null"` and literal `korean: "null"` corrected to `luyến` and `련` respectively; empty `# Notes` stub filled with the standard citation. **False positives correctly excluded**: [[思慕]] and three chengyu hits don't cite 恋/戀 in their `characters` field. **Derived-Characters check**: [[変 (char)|変]], [[弯]], [[栾]], [[蛮]], [[鵉]] all cite 䜌 directly as their own phonetic donor — siblings of 恋, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 邪 (6361; 1311 characters remaining).

### 2026-08-10, iteration 1193 — [[characters/邪|邪]]

**A clean cycle — `mc_id: 350`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 365, confirmed 邪 itself sits at that rank; `graphemic_classification: 牙` matches Wiktionary (semantic [[Radical 163|邑]] + phonetic [[牙 (char)|牙]]); `vietnamese: [tà, tá]`, `korean_native: 간사할` (matching Korean sense #1 "cunning, sly, crafty"), and `japanese_native: よこし` (stem of よこしま) are all exact matches to the raw Wiktionary data.

`pos: 性詞` was already filled. Rebuilt `## Notes` (a malformed bare-components bullet mixed with CC links) to the standard 4-bullet format. **`## Words`**: tagged the existing [[邪心]] citation "(stand-in for 邪)" — already fully perfected, no corruption. **New `## Chengyu` section added**: [[邪心常悪]] genuinely cites 邪 in its `characters` field; [[天長地久]] and [[天真乱漫]] were false positives. **Derived-Characters check**: [[耶 (char)|耶]], [[芽]], [[雅]] all cite 牙 directly as their own phonetic donor — siblings of 邪, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 蓄 (char) (6362; 1310 characters remaining).

### 2026-08-10, iteration 1194 — [[characters/蓄 (char)|蓄]]

**A clean cycle — `mc_id: 1859`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 1000.md` line 896, confirmed 蓄 itself sits at that rank; `graphemic_classification: 畜` matches Wiktionary (semantic [[Radical 140|艸]] + phonetic [[畜]]); `vietnamese: súc`, `korean_native: 모을` (no eumhun given but fits "store, save, hoard, gather" precisely), and `japanese_native: たくわ` (exact stem of たくわえる) all confirmed.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[蓄]] alongside the existing [[蓄積]]. **Bug fixed on [[蓄]] (word)**: literal `vietnamese: "null"` corrected to `súc`; empty `# Notes` stub filled with the standard citation. **False positive correctly excluded**: [[意味深長]] mentions 含蓄 only in Confucian-aesthetics commentary prose. **Derived-Characters check**: nothing else in the vault currently cites 畜 as a phonetic donor. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 誓 (6363; 1309 characters remaining).

### 2026-08-10, iteration 1195 — [[characters/誓|誓]]

**A clean cycle — `mc_id: 1761`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 1000.md` line 794, confirmed 誓 itself sits at that rank; `graphemic_classification: 折` matches Wiktionary (semantic [[Radical 149|言]] + phonetic [[折 (char)|折]]); `vietnamese: [thề, thệ]`, `korean_native: 맹세할`, and `japanese_native: ちか` all confirmed.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, one bare bullet mixed with CC links) to the standard format. **`## Words`**: added the reflexive stand-in [[盟誓]] alongside the existing [[誓約]]. **New `## Chengyu` section added**: [[血誓盟約]] genuinely cites 誓; [[Biblical Chengyu]] (an index page) and [[勿妄称名]] were false positives. **Derived-Characters check**: [[哲]] and [[逝]] both cite 折 directly as their own phonetic donor — siblings of 誓, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 疫 (6364; 1308 characters remaining).

### 2026-08-10, iteration 1196 — [[characters/疫|疫]]

**`mc_id` collision bug fixed**: stored `1859` was an exact duplicate of the value just assigned to [[蓄]] two iterations ago — 疫 itself sits at rank 1860 in `CC 1000.md`, immediately after 蓄, suggesting a simple off-by-one/adjacent-row slip during original data entry. Corrected.

**Real `japanese_native` bug found and fixed**: stored `ø` (this vault's placeholder for "no native kun'yomi exists," confirmed by checking several other genuinely on'yomi-only characters using the same value) — but Wiktionary lists two real kun'yomi for 疫 (え, えやみ). Corrected to `えやみ` ("plague, pestilence"), the fuller and more directly matching reading.

**Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 役` matches Wiktionary (semantic [[Radical 104|疒]] + abbreviated phonetic [[役 (char)|役]]); `vietnamese: dịch` matches Wiktionary's sole reading. **`korean_native: 전염병` left as-is**: no eumhun given, but this compound-as-hun ("epidemic, contagious disease") fits the [[帽]]/[[椅]] pattern seen earlier this sweep, even without direct literal confirmation this time.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, malformed) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[疫病]] alongside the newly-found [[防疫]]. **Derived-Characters check**: nothing else in the vault currently cites 役 as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 壇 (char) (6365; 1307 characters remaining).

### 2026-08-10, iteration 1197 — [[characters/壇 (char)|壇]]

**`mc_id` off-by-one fixed**: stored `1741` pointed to 湛 (the line immediately before); 壇 itself sits at rank 1742 in `CC 1000.md` — corrected. **Classification confirmed correct as-is**: `graphemic_classification: 亶` matches Wiktionary (semantic [[Radical 032|土]] + phonetic [[亶]]).

**Self-correction mid-iteration — two initial "fixes" reverted after finding contradicting prior research**: first changed `vietnamese: đườn` → `đường` (matching Wiktionary's raw template) and `japanese_native: ø` → `たいら` (Wiktionary lists three kun'yomi) — but the citing word [[壇]] (word, perfected 2026-07-27) had already done deeper independent research explicitly validating `đườn` as a genuine (if semantically unrelated — "to lie sprawled out") Nôm rebus loan, and explicitly stating Japanese has "no dedicated native kun'yomi" in practice despite what dictionaries list. Reverted both per the standing rule to trust a citing word's own deep prior research over raw dictionary data when they conflict.

**Real korean_native bug found and fixed, not contradicted by the citing word's research**: stored `단` (self-identical to the `korean` field) didn't match the literal eumhun "제단 단" ("altar platform") — corrected to `제단`.

Filled empty `pos` → `名詞`. Rebuilt `## Notes` to the standard 4-bullet format, preserving the existing 亶→云/坛 and 曇→云/壜 simplification-collision explanation. **`## Words`**: added the reflexive stand-in [[壇]] — the only citation found; its existing reciprocal homophone callout with [[但]] confirmed already complete on both pages. **Derived-Characters check**: [[擅]] and [[檀]] both cite 亶 directly as their own phonetic donor — siblings of 壇, not children — correctly excluded. **Chengyu**: no genuine hits (three false-positive prose mentions).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 妄 (6366; 1306 characters remaining).

### 2026-08-10, iteration 1198 — [[characters/妄|妄]]

**`mc_id: 986` verified correct as-is**: checked `CC 0000.md` line 1019, confirmed 妄 itself sits at that rank. **Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 亡` matches Wiktionary (semantic [[女 (char)|女]] + phonetic [[亡 (char)|亡]]); `vietnamese: [vòng, vọng]` matches Wiktionary's set.

**Real korean_native bug found and fixed**: stored `망령될` ("senile, deranged") doesn't match the literal eumhun "허망할 망" ("vain, absurd, false") — corrected to `허망할`, also a closer match to this character's own stored `english: [delusion, vain]`. **`japanese_native: みだ` confirmed correct as-is**, exact stem match to the attested kun'yomi みだりに.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, malformed) to the standard 4-bullet format. **`## Words`** expanded from one entry to two: added the reflexive stand-in [[妄想]] alongside the existing [[瞻妄]]. **New `## Chengyu` section added**: [[勿妄称名]] genuinely cites 妄 in its `characters` field. **False positives correctly excluded**: [[出谷記]], [[菲薄]], [[五戒]] don't cite 妄 in their `characters` field; [[Biblical Chengyu]] is an index page. **Derived-Characters check**: [[忙]], [[忘]], [[望]], [[盲]], [[罔]], [[茫]], [[虻]], [[芒]] all cite 亡 directly as their own phonetic donor — siblings of 妄, not children — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 泊 (6368; 1305 characters remaining).

### 2026-08-10, iteration 1199 — [[characters/泊|泊]]

**`mc_id: 3426` verified correct as-is**: checked `CC 3000.md` line 447, confirmed 泊 itself sits at that rank. **Classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 白` matches Wiktionary (semantic [[水 (char)|水]] + phonetic [[白 (char)|白]]); `vietnamese: bạc`, `korean_native: 머무를`, and `japanese_native: と` all confirmed.

**Real cross-sense `mandarin` bug found and fixed**: stored `pō` is the reading tied to this character's *other*, unrelated "lake" sense (湖泊, 梁山泊) — but this page's own `english: lie at anchor` and `stand_in: 停泊` both document the "to moor; to anchor" sense, which reads `bó`. The stored `middle_chinese_initial: b` (voiced) independently corroborates `bó` over `pō` (a standard voiced-initial → 2nd-tone correspondence). Corrected.

Filled empty `pos` → `事詞`. **Fixed a malformed relative-path link** (`[[../lookup/CC/finals/韻 鈬合]]`) and rebuilt `# Notes` (wrong heading level) to the standard 4-bullet format, documenting the pō/bó sense split directly. **`## Words`**: tagged the existing [[停泊]] citation "(stand-in for 泊)" — already corruption-free. **Derived-Characters check**: [[拍 (char)|拍]], [[柏 (char)|柏]], [[百 (char)|百]], [[伯]], [[帛]], [[珀]], [[碧]], [[習]], [[舶]], [[迫]], [[魄]] all cite 白 directly as their own phonetic donor — siblings of 泊, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 舟 (6369; 1304 characters remaining).

### 2026-08-10, iteration 1200 — [[characters/舟|舟]]

**`mc_id: 1137` verified correct as-is**: checked `CC 1000.md` line 146, confirmed 舟 itself sits at that rank. **Classification and Vietnamese confirmed correct as-is**: `graphemic_classification: 象形` matches Wiktionary (a pictograph of a boat); `vietnamese: [chu, châu]` matches Wiktionary's set. **`korean_native: 배` confirmed correct as-is**, matching "boat, ship" exactly.

**Real `japanese_native` bug found and fixed, same pattern as [[疫]]**: stored `ø` ("no native kun'yomi"), but Wiktionary lists ふね/ふな. Corrected to `ふね`. Unlike [[壇]]'s reversed case two iterations ago, this fix was independently *corroborated* rather than contradicted: the stand-in word [[小舟]] is itself pronounced こぶね (kobune), directly confirming ふね/ぶね is a genuinely productive native reading.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[小舟]] (also fixed its own blank `pos` → `名詞` while there) alongside the newly-found [[方舟]]. **New `## Chengyu` section added**: [[呉越同舟]] and [[刻舟求剣]] both genuinely cite 舟; [[乾坤一擲]]'s hit was a false positive. **False positives correctly excluded**: [[剣]], [[受賞]], [[前]], [[龍]] don't cite 舟 in their `characters` field. **Derived-Characters check**: nothing in the vault currently cites 舟 as a phonetic donor.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 翼 (6370; 1303 characters remaining).

### 2026-08-10, iteration 1201 — [[characters/翼|翼]]

**A clean cycle — `mc_id: 1056`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 1000.md` line 61, confirmed 翼 itself sits at that rank; `graphemic_classification: 異` matches Wiktionary (semantic [[Radical 124|羽]] + phonetic [[異]]); `vietnamese: dực` matches the raw Wiktionary template exactly; `korean_native: 날개` matches the literal eumhun "날개 익" exactly; `japanese_native: つばさ` matches the primary listed kun reading exactly.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: the existing [[羽翼]] citation (stand-in) was already correctly tagged and is the only genuine citation in the vault. **Derived-Characters check**: nothing else in the vault currently cites 異 as a phonetic donor. **Chengyu**: no genuine hits (two false-positive prose mentions).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 蜂 (char) (6371; 1302 characters remaining).

### 2026-08-10, iteration 1202 — [[characters/蜂 (char)|蜂]]

**`mc_id: 2804`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 2000.md` line 841, confirmed 蜂 itself sits at that rank; `graphemic_classification: 夆` matches Wiktionary (semantic [[Radical 142|虫]] + phonetic 夆, pageless in this vault); `vietnamese: [ong, phong]`, `korean_native: 벌`, and `japanese_native: はち` all exact matches to the raw Wiktionary data.

**`aliases: [蚌]` investigated and confirmed genuine, unlike the pattern-matching temptation to flag it as spurious**: 蚌's *primary* sense is completely unrelated ("bivalve mollusc, clam"), which at first glance looked like another instance of this sweep's recurring spurious-alias bug — but Wiktionary's own 蚌 entry documents a separate, explicit Etymology 3: "a variant form of 蜂," with a direct cross-reference note ("for pronunciation and definitions of 蚌 – see 蜂"). Kept as-is, a genuine polysemous-character alias analogous to [[丑]]'s relationship to [[醜]] earlier this sweep.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, `## Words` bullets missing ruby annotation) to the standard format. **`## Words`** expanded from two entries to three: added the reflexive stand-in [[蜂]] (already independently fully perfected, no corruption) alongside the properly-rubied [[蜂蜜]] and [[蜂巣]]. **False positive correctly excluded**: [[封]] doesn't cite 蜂 in its `characters` field (it's the word [[蜂]]'s own documented homophone instead). **Derived-Characters check**: [[峰]], [[逢]], [[鋒]] all cite 夆 directly as their own phonetic donor — siblings of 蜂, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 鹿 (char) (6372; 1301 characters remaining).

### 2026-08-10, iteration 1203 — [[characters/鹿 (char)|鹿]]

**`mc_id: 984` verified correct as-is**: checked `CC 0000.md` line 1017, confirmed 鹿 itself sits at that rank. **Classification and korean_native confirmed correct as-is**: `graphemic_classification: 象形` matches Wiktionary (a pictograph of a deer); `korean_native: 사슴` matches the literal eumhun exactly.

**Vietnamese expanded**: added `lê`, the second reading Wiktionary lists alongside the already-stored `lộc`.

**`japanese_native: か` checked but deliberately left unchanged, avoiding a repeat of the [[壇]] mistake**: initially suspected this was another `ø`-placeholder-style gap needing correction to しか (the ordinary standalone word for "deer") — but checked the citing word [[鹿]] (word, perfected 2026-08-03) *before* editing this time, and its own deep research explicitly states the stored `か` is correct as a bound reading confined to compounds like 鹿の子 (kanoko), while しか is the free-standing word used elsewhere, not a correction target for this field. Left untouched.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format, correctly linking [Grade 6](lookup/Grade%206.md) (this character's stored `grade_level`) and [Jōyō - Kyōiku](lookup/Japanese/Jōyō%20-%20Kyōiku.md) (matching `joyo_level: "4"` — self-corrected a slip where I'd initially conflated the two distinct grade fields and linked "Grade 4" instead). **`## Words`**: added the reflexive stand-in [[鹿]] alongside the newly-found [[鹿砦]]. **New `## Derived Characters` section added**: [[麓]] cites 鹿 directly as its own phonetic donor. **False positives correctly excluded**: [[緑]], [[嘉賓]] don't cite 鹿 in their `characters` field; [[沈魚落雁]]'s hit was 麋鹿 in a quoted Zhuangzi passage.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 祥 (6373; 1300 characters remaining).

### 2026-08-10, iteration 1204 — [[characters/祥|祥]]

**`mc_id` off-by-one fixed**: stored `1022` pointed to 幣 (the line immediately before); 祥 itself sits at rank 1023 in `CC 1000.md` — corrected.

**Classification, Vietnamese, and japanese_native all confirmed correct as-is**: `graphemic_classification: 羊` matches Wiktionary (semantic [[Radical 113|示]] + phonetic [[羊 (char)|羊]] — originally written simply as 羊, with 示 added later); `vietnamese: tường` matches Wiktionary's sole reading; `japanese_native: きざ` is the correct stem of the attested kun'yomi きざし. **`korean_native: 복` left as-is**: Wiktionary's eumhun field is empty; "복" ("fortune, blessing") is a plausible noun-form gloss for "auspicious," kept without a contradicting source.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format, including the "originally just 羊" etymological note. **`## Words`**: tagged the existing [[吉祥]] citation "(stand-in for 祥)" — already fully perfected, no corruption. **Derived-Characters check**: [[姜 (char)|姜]], [[様 (char)|様]], [[洋]], [[翔]], [[詳]], [[羌]], [[養]] all cite 羊 directly as their own phonetic donor — siblings of 祥, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 菌 (6374; 1299 characters remaining).

### 2026-08-10, iteration 1205 — [[characters/菌|菌]]

**`mc_id` off-by-one fixed**: stored `3644` pointed to 嫪 (the line immediately before); 菌 itself sits at rank 3645 in `CC 3000.md` — corrected.

**Classification, Vietnamese, and korean_native all confirmed correct as-is**: `graphemic_classification: 囷` matches Wiktionary (semantic [[Radical 140|艸]] + phonetic 囷, pageless in this vault); `vietnamese: khuẩn` and `korean_native: 버섯` both exact matches.

**Real `japanese_native` bug found and fixed, same `ø`-placeholder pattern as [[疫]]/[[舟]]**: checked the citing word [[細菌]] (already perfected) for any prior research on this point first (per the [[壇]]/[[鹿]] lesson) — found none contradicting it, so corrected `ø` → `きのこ`, matching Wiktionary's attested kun'yomi.

**Incidental bug fixed on an unrelated citing word encountered mid-sweep**: [[椎菌]] (word)'s own `japanese` field was a comma-dump mixing a reading with a kanji spelling (`しいたけ, 椎茸`) — trimmed to the reading alone, `しいたけ`.

Filled empty `pos` → `名詞`. Rebuilt `## Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`** expanded from one entry to three: tagged the existing [[細菌]] stand-in and added the newly-found [[病菌]] and [[椎菌]]. **Derived-Characters check**: nothing else in the vault currently cites 囷 as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 淡 (6375; 1298 characters remaining).

### 2026-08-10, iteration 1206 — [[characters/淡|淡]]

**`mc_id` off-by-one fixed**: stored `2802` pointed to 竽 (the line immediately before); 淡 itself sits at rank 2803 in `CC 2000.md` — corrected.

**Real spurious-alias bug found and fixed, an eighth and ninth instance of the pattern in one go**: `aliases: [澹, 毯]` — neither is a genuine variant of 淡. 澹 is explicitly documented as merely "related to 淡" (a cognate with overlapping "insipid" sense but its own distinct pronunciation and identity), and 毯 ("carpet, rug") is simply a sibling sharing the same phonetic donor 炎, with zero semantic connection. Removed both (neither has a vault page); documented the cognate/sibling distinction directly in the Notes.

**Classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 炎` matches Wiktionary (semantic [[水 (char)|水]] + phonetic [[炎]]); `vietnamese: [vạm, đượm, đạm, đặm]` matches Wiktionary's full set; `korean_native: 맑을` matches the literal eumhun exactly; `japanese_native: あわ` is the correct stem of the attested kun'yomi あわい.

Filled empty `pos` → `性詞`. Rebuilt the malformed `# Notes`/`## Words` (an etymology-less stub, a stray bullet under the wrong heading, and one properly-rubied entry) into the standard format. **`## Words`** expanded from one entry to four: tagged the existing [[清淡]] stand-in, added the newly-found [[淡水]], and properly incorporated the existing [[淡紫]] and [[淡麻]]. **Derived-Characters check**: [[痰 (char)|痰]], [[啖]], [[談]] all cite 炎 directly as their own phonetic donor — siblings of 淡, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 酌 (6376; 1297 characters remaining).

### 2026-08-10, iteration 1207 — [[characters/酌|酌]]

**`mc_id: 1753` verified correct as-is**: checked `CC 1000.md` line 786, confirmed 酌 itself sits at that rank. **Classification and japanese_native confirmed correct as-is**: `graphemic_classification: 勺` matches Wiktionary (semantic [[Radical 164|酉]] + phonetic [[勺 (char)|勺]]); `japanese_native: く` is the correct stem of the attested kun'yomi くむ.

**Real korean_native bug found and fixed**: stored `따를` (from 따르다, "to pour") doesn't match the literal eumhun "술 부을 작" — Wiktionary specifically uses 붓다 ("to pour," a different but near-synonymous verb), giving `부을`. Corrected; checked both citing words first for any contradicting prior research (per the [[壇]]/[[鹿]] lesson) and found none. **`vietnamese: [chuốc, chước]` left unverifiable but unchanged**: 酌 has no Vietnamese section on Wiktionary at all, so neither confirmed nor contradicted.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[酌酒]] stand-in and [[斟酌]] citations — both already corruption-free. **Derived-Characters check**: [[灼]], [[的]], [[豹]], [[釣]], [[約]] all cite 勺 directly as their own phonetic donor — siblings of 酌, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 卓 (6377; 1296 characters remaining).

### 2026-08-10, iteration 1208 — [[characters/卓|卓]]

**`mc_id: 1225` verified correct as-is**: checked `CC 1000.md` line 238, confirmed 卓 itself sits at that rank. **`graphemic_classification: 會意` confirmed correct as-is**, matching this vault's established bare-type-label convention (cf. [[与]], [[沙]]).

**Both aliases investigated and confirmed genuine — a clean result after the recent run of spurious-alias bugs**: 㔬 is explicitly Wiktionary's documented "ancient variant" of 卓; 龺 is confirmed via a chain ("龺 is a variant form of 𠦝, which is in turn a variant form of 卓") — both legitimate, no removal needed.

**Malformed YAML fixed**: `vietnamese` was a single comma-joined string (`"trác, chác, giạt"`) instead of a proper list — converted to a true YAML list, and added the missing fourth reading `chắc` that Wiktionary lists alongside the other three. **`korean_native: 높을` confirmed correct as-is**, exact match to the literal eumhun. **`japanese_native` corrected**: stored the full dictionary form `すぐれる` instead of the stem — trimmed to `すぐれ`, matching this vault's established verb-stem convention (checked the two citing words first for contradicting research, per the [[壇]]/[[鹿]] lesson; found none).

Rebuilt `# Notes` (wrong heading level, one bare unrubied bullet) to the standard 4-bullet format. **`## Words`**: tagged the existing [[卓越]] stand-in. **New `## Derived Characters` section added**: [[悼 (char)|悼]], [[桌 (char)|桌]], [[綽]] all cite 卓 directly as their own phonetic donor — genuine children, discovered because [[桌]] (word)'s grep hit initially looked like a false positive (a different character containing 卓 visually) but its own `graphemic_classification: 卓` confirmed the real derivation. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 肖 (6378; 1295 characters remaining).

### 2026-08-10, iteration 1209 — [[characters/肖|肖]]

**`mc_id: 1081` verified correct as-is**: checked `CC 1000.md` line 86, confirmed 肖 itself sits at that rank.

**Notes prose etymology bullet was doubly wrong, same pattern as [[屈]]/[[那]]/[[醜]] earlier this sweep**: the existing text read "semantic 小 ('meat') + phonetic 肉" — reversed on the roles AND wrong on 小's gloss (小 means "small," not "meat"). Wiktionary confirms semantic is [[Radical 130|肉]] ("flesh," written as 月 and merged in form with the moon radical) and phonetic is [[小 (char)|小]] (OC \*smewʔ); the stored `graphemic_classification: 小` field itself was already correct throughout.

**Real spurious-alias bug found and fixed, a tenth instance of the pattern**: `aliases: [霄]` — Wiktionary confirms 霄 ("sky, clouds") is simply a 形聲 *child* of 肖 (semantic 雨 + phonetic 肖), explicitly "not variant forms of each other." Removed (no vault page exists for 霄).

**Vietnamese and korean_native confirmed correct as-is**: `[tiêu, tiếu]` matches Wiktionary; `korean_native: 닮을` fits the "resemble" sense precisely, corroborated by the Japanese kun'yomi にる ("to resemble"). **`japanese_native: あやか` left as-is despite being a less semantically-central choice than にる/かたどる**: all three are genuine attested kun'yomi with no source favoring one over another, so left unchanged rather than substituted on judgment alone.

Filled empty `pos` → `名詞`. Rebuilt `## Notes`/`## Words`/`### Derived Characters` (all malformed and mixed together under one heading) into proper separate, standard-format sections. **`## Derived Characters`** expanded dramatically, from one entry ([[硝]], correctly identified even in the original malformed version) to ten: [[削 (char)|削]], [[消 (char)|消]], [[稍 (char)|稍]], [[哨]], [[梢]], [[宵]], [[硝]], [[趙]], [[鞘]], [[逍]] all genuinely cite 肖 as their own phonetic donor. **`## Words`**: tagged the existing [[肖像]] stand-in citation. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 遷 (6379; 1294 characters remaining).

### 2026-08-10, iteration 1210 — [[characters/遷|遷]]

**`mc_id: 470` verified correct as-is**: checked `CC 0000.md` line 488, confirmed 遷 itself sits at that rank.

**Real classification bug found and fixed, a different flavor from this sweep's usual swap/mislabel pattern**: stored `graphemic_classification: 四` ("four") matched nothing in Wiktionary's etymology and even contradicted the page's own existing (correct) Notes prose, which already named 䙴 as the phonetic — corrected to `䙴`.

**Both aliases confirmed genuine**: 䙴 is the documented phonetic-donor variant; 迁 is explicitly the Mainland-China simplified form (16 strokes traditional/Korean vs. 15 strokes simplified/Japanese).

**Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `vietnamese: thiên`, `korean_native: 옮길` (exact eumhun match), and `japanese_native: うつ` (correct shared stem of うつる/うつす) all verified against the raw Wiktionary templates.

Filled empty `pos` → `事詞`. Rebuilt `## Notes` to the standard 4-bullet format, fixing an incomplete OC-reconstruction citation (`OC ` with nothing after it) along the way. **`## Words`**: tagged the existing [[遷移]] stand-in "(stand-in for 遷)" and added a proper ruby annotation to the previously bare [[遷怒]] link. **Derived-Characters check**: nothing in the vault currently cites 䙴 or 遷 itself as a further phonetic donor. **Chengyu**: no genuine hits (six false-positive hits, all likely 司馬遷/Sima Qian name mentions in historical commentary).

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 廉 (char) (6380; 1293 characters remaining).

### 2026-08-10, iteration 1211 — [[characters/廉 (char)|廉]]

**`mc_id: 744` verified correct as-is**: checked `CC 0000.md` line 771, confirmed 廉 itself sits at that rank. **Classification and korean_native confirmed correct as-is**: `graphemic_classification: 兼` matches Wiktionary (semantic [[Radical 053|广]] + phonetic [[兼 (char)|兼]]); `korean_native: 청렴할` matches the literal eumhun "청렴 렴" closely.

**Vietnamese narrowed**: removed `lèm`, unsupported anywhere in Wiktionary's reading set `[liêm, rèm]`. **`japanese_native` filled, same `ø`-placeholder pattern as several earlier this sweep**: checked the citing word [[廉]] (word, perfected 2026-07-26) first for contradicting research — found none, only on'yomi discussion — so filled with `いさぎよ` (stem of いさぎよい, "pure/honorable"), the closest semantic match to this character's own `english: [upright, honest]` among Wiktionary's four listed kun'yomi.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, a stray `## Words`-style bullet mixed in) into the standard format. **`## Words`** expanded from two entries to four: tagged the existing [[廉]] and [[孝廉]] entries, and added the newly-found [[廉価]] (previously stranded as a bare Notes bullet) and [[低廉]]. **False positive correctly excluded**: [[貪官汚吏]] mentions 廉 only within prose idioms (為官不廉, 清官廉吏), not as a genuine citation. **Derived-Characters check**: [[鎌 (char)|鎌]], [[嫌]], [[謙]] all cite 兼 directly as their own phonetic donor — siblings of 廉, not children — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 祈 (6381; 1292 characters remaining).

### 2026-08-10, iteration 1212 — [[characters/祈|祈]]

**`mc_id: 1869` verified correct as-is**: checked `CC 1000.md` line 906, confirmed 祈 itself sits at that rank. **Classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 斤` matches Wiktionary (semantic [[Radical 113|示]] + phonetic [[斤 (char)|斤]]); `vietnamese: kì`, `korean_native: 빌`, and `japanese_native: いの` all exact matches.

**Real spurious-alias bug found and fixed, an eleventh instance of the pattern**: `aliases: [沂]` — 沂 ("a river in Shandong") is simply a sibling sharing the same phonetic donor 斤 with 祈, never described as a variant. Removed (no vault page exists for 沂).

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[祈祷]] citation "(stand-in for 祈)" and explicitly confirmed the `#cranberry` transitivity — [[祷]]'s own `stand_in` also points to 祈祷, satisfying A=B=AB. **Derived-Characters check**: [[近 (char)|近]] and [[欣]] both cite 斤 directly as their own phonetic donor — siblings of 祈, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 韻 (6382; 1291 characters remaining).

### 2026-08-10, iteration 1213 — [[characters/韻|韻]]

**`mc_id: 6497` outside the vault's verifiable range**: neither 韻 nor its alias 韵 appear in `CC 0000`–`CC 3000`. **Classification, `middle_chinese_initial: ø`, Vietnamese, and korean_native all confirmed correct as-is**: `graphemic_classification: 員` matches Wiktionary (semantic [[Radical 180|音]] + phonetic [[員]]); the null initial matches Wiktionary's own "initial 云 (null)" citation; `vietnamese: [vần, vận]` matches; `korean_native: 운` (self-identical to the `korean` field) has no eumhun to check against but fits the established self-identical-loanword pattern (cf. [[瓶]], [[椅]]).

**Real `japanese_native` bug found and fixed, same `ø`-placeholder pattern seen repeatedly this sweep**: checked the stand-in word [[押韻]] first for contradicting research — found none — then filled `ø` → `ひびき` ("resonance, echo"), matching Wiktionary's attested kun'yomi.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, a stray bullet mixed with CC links) to the standard 4-bullet format. **`## Words`** expanded from one entry to four: added the reflexive stand-in [[押韻]] and the newly-found [[音韻]], alongside the properly-rubied [[韻母]] and the previously-stranded [[韻図]]. **Chengyu**: no genuine hits (two false positives). **Derived-Characters check**: [[圓 (char)|圓]] and [[損]] both cite 員 directly as their own phonetic donor — siblings of 韻, not children — correctly excluded. Both `aliases` (韵, 𱂐) confirmed as genuine documented variant forms, no removal needed.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 畏 (char) (6383; 1290 characters remaining).

### 2026-08-10, iteration 1214 — [[characters/畏 (char)|畏]]

**`mc_id: 650` verified correct as-is**: checked `CC 0000.md` line 674, confirmed 畏 itself sits at that rank.

**Real classification bug found and fixed, a fifth instance of the wrong-type-label pattern this sweep**: stored `graphemic_classification: 會意` — Wiktionary's raw glyph-origin template is explicitly `ls=psc` (phono-semantic compound): "semantic 卜 (later corrupted to 止) + phonetic 鬼." Corrected to `鬼`.

**Vietnamese narrowed**: stored `[hoay, hoáy, uý, ối]` had one unsupported entry (`ối`, no support anywhere) and a redundant orthographic-variant spelling (`uý`/`úy`, same word); replaced with the exact three-item set Wiktionary lists: `[úy, hoáy, hoay]`. **`korean_native: 두려워할` and `japanese_native: おそ` both confirmed correct as-is** (no eumhun given for Korean, but the stored gloss fits precisely; the Japanese value is the correct stem of the attested primary kun'yomi おそれる).

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format, including the oracle-bone "ghost holding a stick" imagery and the 威-derivation note. **`## Words`**: added the reflexive stand-in [[畏]] — the only citation found. **Bug fixed on [[畏]] (word)**: literal `vietnamese: "null"` corrected to `úy`; empty `# Notes` stub filled with the standard citation. **Derived-Characters check**: [[塊 (char)|塊]], [[傀]], [[愧]], [[槐]], [[魁]] all cite 鬼 directly as their own phonetic donor — siblings of 畏, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 翁 (char) (6384; 1289 characters remaining).

### 2026-08-10, iteration 1215 — [[characters/翁 (char)|翁]]

**`mc_id: 1689` verified correct as-is**: checked `CC 1000.md` line 718, confirmed 翁 itself sits at that rank. **Classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 公` matches Wiktionary (semantic [[Radical 124|羽]] + phonetic [[公 (char)|公]] — originally "feathers," later loaned for "old man"); `vietnamese: [òng, ông, ồng, ổng]` matches Wiktionary's full Hán Việt + Nôm set; `korean_native: 늙은이` fits despite no eumhun being given; `japanese_native: おきな` matches the primary attested kun'yomi exactly.

**Real spurious-alias bug found and fixed, a twelfth instance of the pattern**: `aliases: [鶲]` — Wiktionary's own page for 翁 lists 鶲 under "Derived Characters," not as a variant; 鶲 is simply a 形聲 *child* of 翁 (a flycatcher-bird name), unrelated in meaning. Removed (no vault page exists for it).

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`** expanded from zero properly-formed entries to three: added the reflexive stand-in [[翁]] and the newly-found [[信天翁]] and [[白頭翁]]. **Bug fixed on [[信天翁]] (word)**: blank `pos` filled → `名詞`. **False positive correctly excluded**: [[壅]] doesn't cite 翁 in its `characters` field. **Derived-Characters check**: [[松 (char)|松]], [[訟 (char)|訟]], [[甕]], [[頌]] all cite 公 directly as their own phonetic donor — siblings of 翁, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 邦 (6385; 1288 characters remaining).

### 2026-08-10, iteration 1216 — [[characters/邦|邦]]

**A clean cycle — `mc_id: 947`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 980, confirmed 邦 itself sits at that rank; `graphemic_classification: 丰` matches Wiktionary (semantic [[Radical 163|邑]] + phonetic 丰, pageless in this vault); `vietnamese: [vâng, bang, bương]`, `korean_native: 나라` (exact eumhun match), and `japanese_native: くに` all confirmed.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`** expanded from one entry to three: added the reflexive stand-in [[連邦]] and the newly-found [[万邦]], alongside the properly-rubied [[邦畿]]. **Derived-Characters check**: [[封 (char)|封]] and [[奉]] both cite 丰 directly as their own phonetic donor — siblings of 邦, not children — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 葬 (6386; 1287 characters remaining).

### 2026-08-10, iteration 1217 — [[characters/葬|葬]]

**A clean cycle — `mc_id: 502`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 523, confirmed 葬 itself sits at that rank; `graphemic_classification: 茻` confirmed as a genuine component (茻 "thick grass" + [[死 (char)|死]] "dead person," a true 會意 with no phonetic borrowing) — noting this vault stores a specific component rather than the bare `會意` type label for this character, unlike [[与]]/[[沙]]/[[卓]], but both conventions coexist and neither is wrong; `vietnamese: táng`, `korean_native: 장사지낼`, and `japanese_native: ほうむ` all confirmed against the raw Wiktionary data.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[埋葬]] stand-in citation — the only one found, already corruption-free. **Derived-Characters check**: [[莽]] cites 茻 directly as its own component — a sibling, not a child of 葬 — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 拘 (6387; 1286 characters remaining).

### 2026-08-10, iteration 1218 — [[characters/拘|拘]]

**`mc_id: 1383` verified correct as-is**: checked `CC 1000.md` line 400, confirmed 拘 itself sits at that rank. **Classification, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 句` matches Wiktionary (semantic [[Radical 064|扌]] + phonetic [[句 (char)|句]]); `korean_native: 잡을` matches the literal eumhun exactly; `japanese_native: かか` is the correct stem of the attested primary kun'yomi かかわる.

**Vietnamese narrowed**: removed `khú`, unsupported anywhere in the raw Wiktionary template (`reading=câu` only).

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, two stray unrubied bullets) to the standard 4-bullet format — caught and corrected my own initial mistake of guessing at 注音 values for [[拘束]] and [[拘泥]] instead of checking their actual pages first (`ㄍㄨㄙ⼄ㄎ`/`ㄍㄨㄋㄝㄧ`, not the values I'd first guessed). **`## Words`** expanded from two entries to three: tagged the existing [[拘束]] stand-in and [[拘泥]], and added the newly-found [[拘禁]]. **False positive correctly excluded**: [[海闊天空]] doesn't cite 拘 in its `characters` field. **Derived-Characters check**: [[局 (char)|局]], [[苟 (char)|苟]], [[鉤 (char)|鉤]], [[狗]], [[駒]] all cite 句 directly as their own phonetic donor — siblings of 拘, not children — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 赴 (char) (6388; 1285 characters remaining).

### 2026-08-10, iteration 1219 — [[characters/赴 (char)|赴]]

**`mc_id` off-by-one fixed**: stored `1530` pointed to 崔 (the line immediately before); 赴 itself sits at rank 1531 in `CC 1000.md` — corrected.

**Classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 卜` matches Wiktionary (semantic [[Radical 156|走]] + phonetic [[卜 (char)|卜]]); `vietnamese: phó` matches Wiktionary's sole reading; `korean_native: 다다를` matches the first of two listed eumhun entries ("다다를 부," reach/arrive) exactly; `japanese_native: おもむ` is the correct stem of the attested kun'yomi おもむく.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[赴]] — the only citation found. **Bug fixed on [[赴]] (word)**: blank `vietnamese` filled → `phó`; empty `# Notes` stub filled with the standard citation. **Derived-Characters check**: [[朴]] and [[訃]] both cite 卜 directly as their own phonetic donor — siblings of 赴, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 疎 (6389; 1284 characters remaining).

### 2026-08-10, iteration 1220 — [[characters/疎|疎]]

**`mc_id: 762`, a genuine "recorded under alias" case, confirmed correct as-is**: 疎 itself doesn't appear in any CC list, but its alias 疏 sits at rank 762 in `CC 0000.md` — confirmed genuine since Wiktionary explicitly states "this character is a variant form of 疏," the same word.

**`graphemic_classification: 疋` investigated and kept, an unusual case where the vault's headword and the true etymological form diverge**: Wiktionary's page for 疎 itself names a different, obscure construction (semantic 𤴔 + phonetic 束) — but 疏 (the form this page is anchored to via alias/mc_id, and whose reading this whole page documents) has its own well-attested etymology with phonetic [[疋 (char)|疋]], which also happens to be 疎's own Kangxi radical and already has vault infrastructure. Kept `疋`, matching the primary/documented form rather than 疎's own rarer alternate construction; explained the tension directly in the Notes.

**Vietnamese drastically narrowed, another severe undifferentiated-list case**: stored 9 entries, all drawn from Wiktionary's own 12-item undifferentiated Nôm pile, with the one labeled Hán Việt reading (`sơ`) missing from the stored set entirely. Narrowed to `[sơ]`.

**Real korean_native bug found and fixed**: stored `소통할` ("to communicate") doesn't match the literal eumhun "성길" (from 성기다, "to be sparse") — corrected, also a much closer match to this character's own `english: [loose, neglect]`. **`japanese_native: うと` confirmed correct as-is**, a valid shared stem of two of Wiktionary's five listed kun'yomi (うとむ/うとい).

Filled empty `pos` → `性詞` and blank `boundedness` → `80`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard format. **`## Words`**: tagged the existing [[疎忽]] stand-in citation — already corruption-free. **Derived-Characters check**: [[楚]] and [[胥]] both cite 疋 directly as their own phonetic donor — siblings, not children — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 頻 (char) (6390; 1283 characters remaining).

### 2026-08-10, iteration 1221 — [[characters/頻 (char)|頻]]

**`mc_id: 3070` verified correct as-is**: checked `CC 3000.md` line 75, confirmed 頻 itself sits at that rank. **`graphemic_classification: 會意` confirmed correct as-is**, matching Wiktionary (originally written [[瀕]] — 頁 near water's edge — with the water radical later dropped to distinguish "frequent" from 瀕's "on the verge" sense) and this vault's established bare-type-label convention.

**Vietnamese narrowed**: removed `tằn`, unsupported anywhere in Wiktionary's reading set `[tần, từng]`. **`korean_native: 자주` and `japanese_native: しき` both confirmed correct as-is**: no eumhun given for Korean but "자주" ("frequently") fits precisely; the Japanese value is a valid shared stem of two attested kun'yomi (しきる/しきりに).

**Fixed a stray leftover scratch-text bug, found on both the character page and its citing word**: `# Notes` held only the orphaned fragment "needed pim" (evidently an old to-do note about the romanization) instead of real content — removed and rebuilt properly on both [[頻 (char)]] and [[頻]] (word).

Filled empty `pos` → `修飾語`. **`## Words`**: added the reflexive stand-in [[頻]] — the only citation found. **Bug fixed on [[頻]] (word)**: literal `vietnamese: "null"` corrected to `tần`. **Derived-Characters check**: nothing in the vault currently cites 頻 as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 駆 (char) (6391; 1282 characters remaining).

### 2026-08-10, iteration 1222 — [[characters/駆 (char)|駆]]

**`mc_id: 1345`, a genuine "recorded under alias" case, confirmed correct as-is**: 駆 itself doesn't appear in any CC list, but its traditional alias 驅 sits at rank 1345 in `CC 1000.md` — matches precisely since Wiktionary explicitly documents 駆 as the modern shinjitai form of 驅. **`graphemic_classification: 区` confirmed correct as-is**: Wiktionary's etymology names the traditional 區 as phonetic, but the vault's stored value correctly uses 区 (the form with an actual vault page, matching the established shinjitai-preference pattern, e.g. [[填]]→真, [[剰]]→乗).

**Blank Vietnamese filled**: `[xúi, khu, xù]`, matching Wiktionary's undifferentiated three-item set (no larger pile to narrow this time). **`korean_native: 몰` and `japanese_native: か` both confirmed correct as-is**: the eumhun "몰 구" matches exactly; か is a valid shared stem of both attested kun'yomi かける/かる.

Filled empty `pos` → `事詞` and blank `boundedness` → `80`. Rebuilt `# Notes` (wrong heading level, malformed) to the standard 4-bullet format, with 驅 left as plain unlinked text (pageless in this vault) rather than a broken wikilink. **`## Words`** expanded from two entries to three: added the reflexive stand-in [[駆]], alongside the existing [[駆逐]] and [[駆逐艦]]. **Bugs fixed on [[駆]] (word)**: blank `pos`/`品詞`/`vietnamese` all filled; empty `## Notes` (previously a bare header) filled with the standard citation. **Derived-Characters check**: [[枢 (char)|枢]], [[䝙]], [[鴎 (char)|鴎]], [[呕]], [[欧]], [[殴]], [[𧦅]] all cite 区 directly as their own phonetic donor — siblings of 駆, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 庸 (char) (6392; 1281 characters remaining).

### 2026-08-10, iteration 1223 — [[characters/庸 (char)|庸]]

**`mc_id: 1093` verified correct as-is**: checked `CC 1000.md` line 98, confirmed 庸 itself sits at that rank. **`graphemic_classification: 用` confirmed correct as-is**: Wiktionary's raw glyph-origin template documents both 同 and 用 as valid phonetic candidates (`{{Han compound|庚|同|...}}`, "formed from 庚 plus 同 / 用"); 用 is one of the two explicitly named options.

**Vietnamese and korean_native both confirmed correct as-is**: `[dong, dông, dung, giông]` matches Wiktionary's set exactly; `korean_native: 쓸` ("to use") has no eumhun to check against but aligns with both the phonetic donor 用's own meaning and one of the character's extended senses.

**Real `japanese_native` bug found and fixed, same `ø`-placeholder pattern seen repeatedly this sweep**: checked the two citing words first for contradicting research — found none — then filled `ø` → `なみ` ("ordinary, common"), the closest of Wiktionary's three listed kun'yomi (なみ/つね/もちいる) to this character's own `english: [commonplace, ordinary, mediocre]`.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format, noting the 鏞-"large bell" original sense. **`## Words`**: added the reflexive stand-in [[庸]] alongside the newly-found [[中庸]]. **Bug fixed on [[庸]] (word)**: literal `vietnamese: "null"` corrected to `dung`; empty `# Notes` stub filled with the standard citation. **Derived-Characters check**: [[甬]] cites 用 directly as its own phonetic donor — a sibling, not a child of 庸 — correctly excluded. **Chengyu**: no genuine hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 顕 (6393; 1280 characters remaining).

### 2026-08-10, iteration 1224 — [[characters/顕|顕]]

**`mc_id: 639`, a genuine "recorded under alias" case, confirmed correct as-is**: 顕 itself doesn't appear in any CC list, but its traditional alias 顯 sits at rank 639 in `CC 0000.md` — matches precisely since Wiktionary explicitly documents 顕 as the modern shinjitai form of 顯. **`graphemic_classification: 絲` confirmed correct as-is**: 顯 is genuinely 會意 (日 "sun" + 絲 "silk" + 頁 "head," no phonetic borrowing) — 絲 is one of its three real components, matching the same specific-component-over-bare-type-label convention seen on [[葬]] (茻) two iterations ago.

**Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `hiển`, `나타날` (exact eumhun match), and `あきらか` (first listed kun'yomi) all verified against the raw Wiktionary data.

Filled empty `pos` → `性詞`. Rebuilt `# Notes` (wrong heading level, a stray unheaded `## Words`-style bullet mixed in) into properly separated standard-format sections, preserving the pre-existing `## Chengyu` entry [[形助顕理]]. **`## Words`** expanded from one entry to three: tagged the existing [[顕著]] stand-in and [[顕示]] (self-corrected a guessed-wrong 注音 for the latter after checking its actual page, following the same discipline established after a similar slip on [[拘]]), and added the newly-found [[顕現]]. **False positives correctly excluded**: [[獅子国]], [[南亜]], [[液晶]], [[巴基斯坦]] don't cite 顕/顯 in their `characters` field; [[世間罪盛]]'s hit was a prose mention. **Derived-Characters check**: nothing else in the vault currently cites 絲 as a component.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 凝 (6394; 1279 characters remaining).

### 2026-08-10, iteration 1225 — [[characters/凝|凝]]

**`mc_id` off-by-one fixed**: stored `2125` pointed to 怯 (the line immediately before); 凝 itself sits at rank 2126 in `CC 2000.md` — corrected.

**Classification, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 疑` matches Wiktionary (semantic [[Radical 015|冫]] + phonetic [[疑 (char)|疑]]); `korean_native: 엉길` fits "congeal, coagulate" precisely despite no eumhun being given; `japanese_native: こ` is the correct shared stem of both attested kun'yomi こる/こらす.

**Vietnamese expanded**: added `ngững` and `ngờ`, the two additional Nôm readings Wiktionary lists alongside the already-stored Hán Việt `ngưng` and Nôm `ngừng`.

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[凝結]] stand-in citation — the only one found, already corruption-free. **Derived-Characters check**: [[擬 (char)|擬]] cites 疑 directly as its own phonetic donor — a sibling, not a child of 凝 — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 暫 (6395; 1278 characters remaining).

### 2026-08-10, iteration 1226 — [[characters/暫|暫]]

**`mc_id` off-by-one fixed**: stored `3335` pointed to 迴 (the line immediately before); 暫 itself sits at rank 3336 in `CC 3000.md` — corrected. **Classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `graphemic_classification: 斬` matches Wiktionary (semantic [[日 (char)|日]] + phonetic [[斬 (char)|斬]]); `vietnamese: tạm`, `korean_native: 잠깐` (exact eumhun match), and `japanese_native: しばら` (correct stem of しばらく) all confirmed.

Rebuilt the malformed `## Notes` (a bare components list mixed with CC links, missing the etymology/OC-reconstruction detail) to the standard 4-bullet format. **`## Words`**: tagged the existing [[暫時]] stand-in citation — the only one found, already corruption-free. **Derived-Characters check**: [[慙]] and [[漸]] both cite 斬 directly as their own phonetic donor — siblings of 暫, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 携 (6396; 1277 characters remaining).

### 2026-08-10, iteration 1227 — [[characters/携|携]]

**`mc_id: 2522`, a genuine "recorded under alias" case, confirmed correct as-is**: 携 itself doesn't appear in any CC list, but its traditional alias 攜 sits at rank 2522 in `CC 2000.md` — matches precisely since Wiktionary explicitly documents 攜 as the original/traditional form of the Japanese shinjitai 携. **`graphemic_classification: 巂` confirmed correct as-is**, matching Wiktionary (semantic [[Radical 064|扌]] + phonetic 巂, pageless in this vault).

**Vietnamese and japanese_native both confirmed correct as-is**: `huề` matches Wiktionary's sole reading; `たずさ` is the correct shared stem of both attested kun'yomi たずさえる/たずさわる. **`korean_native: 가질` left as-is**: Wiktionary's page for 攜 has no Korean section at all, so neither confirmed nor contradicted.

Rebuilt `## Notes` (bare two-link stub) to the standard 4-bullet format, documenting the shinjitai/alias relationship directly. **`## Words`**: tagged the existing [[携帯]] stand-in citation; both it and [[提携]] checked and found already corruption-free. **Derived-Characters check**: nothing else in the vault currently cites 巂 as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 鉢 (char) (6397; 1276 characters remaining).

### 2026-08-10, iteration 1228 — [[characters/鉢 (char)|鉢]]

**`mc_id: 0` confirmed correct as-is**: neither 鉢 nor any of its three aliases (盋, 钵, 缽) appear in `CC 0000`–`CC 3000`.

**Real classification bug found and fixed**: stored `graphemic_classification: 犮` matched nothing in Wiktionary's etymology and directly contradicted the page's own existing Notes bullet ("Components: 金, 本") — corrected to `本`, the genuine phonetic donor (semantic 金 + phonetic [[本 (char)|本]]).

**All three aliases investigated and confirmed genuine — a clean result**: 缽 (traditional) and 钵 (simplified) are both explicitly documented variant/simplification relationships; 盋 is separately confirmed as "a variant form of 缽" in its own right — no spurious entries this time.

**Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `bát` matches Wiktionary's sole reading; `korean_native: 바리때` matches the literal gloss "바리때 발" exactly; `japanese_native: ø` is genuinely correct this time — Wiktionary explicitly states this character has no native kun'yomi, only on'yomi はち/はつ (unlike several other `ø`-placeholder bugs found and fixed earlier this sweep).

Filled blank `boundedness` → `90`. Rebuilt `## Notes` (a bare components list mixed with CC links) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[鉢]] — the only citation found. **Bug fixed on [[鉢]] (word)**: blank `vietnamese` filled → `bát`; empty `# Notes` stub filled with the standard citation. **Derived-Characters check**: nothing else in the vault currently cites 本 as this specific phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 傑 (6397; 1275 characters remaining).

### 2026-08-10, iteration 1229 — [[characters/傑|傑]]

**`mc_id: 2255` verified correct as-is**: checked `CC 2000.md` line 268, confirmed 傑 itself sits at that rank — a stray leftover scratch note ("桀=C#866") evidently explored an alternate alias-based candidate that was never used; removed as noise. **Classification and both aliases confirmed correct as-is**: `graphemic_classification: 桀` matches Wiktionary (semantic [[Radical 009|人]] + phonetic 桀, pageless in this vault, explicitly "the same word" as 傑); 杰 independently confirmed as a genuine simplified/variant form.

**Real korean_native bug found and fixed**: stored `뛰어날` ("to excel, be outstanding") doesn't match the literal eumhun — the raw template gives `호걸` ("hero") twice over, as both the hun and the reading gloss. Corrected; checked citing words first for contradicting research (per the [[壇]]/[[鹿]] lesson) and found only independent confirmation that 호걸 is a genuine Korean word (via [[豪傑]]'s own `korean` field), not a contradiction. **Vietnamese and japanese_native both confirmed correct as-is**: `kiệt` matches Wiktionary's sole reading; `すぐ` is the correct stem of the attested kun'yomi すぐれる.

Filled empty `pos` → `性詞`. Rebuilt `## Notes` (stray scratch text mixed with bare CC links) to the standard 4-bullet format. **`## Words`** expanded from one entry to four: added the reflexive stand-in [[傑出]], and the newly-found [[俊傑]] and [[豪傑]], alongside the existing [[傑作]]. **Derived-Characters check**: nothing else in the vault currently cites 桀 as a phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 詠 (char) (6398; 1274 characters remaining).

### 2026-08-10, iteration 1230 — [[characters/詠 (char)|詠]]

**`mc_id: 2714`, classification, `middle_chinese_initial: ø`, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 2000.md` line 747, confirmed 詠 itself sits at that rank; `graphemic_classification: 永` matches Wiktionary (semantic [[Radical 149|言]] + phonetic [[永]]); the null MC initial matches Wiktionary's own "初 (null)" citation; `vietnamese: [vạnh, vẳng, vịnh]` was already appropriately narrowed from Wiktionary's much larger 7-item undifferentiated Nôm pile (no further action needed); `korean_native: 읊을` fits despite no eumhun being given; `japanese_native: うた` is the correct stem of one of four attested kun'yomi (うたう).

Filled empty `pos` → `事詞`. Rebuilt `# Notes` (wrong heading level, a stray unheaded `## Words`-style bullet) into properly separated standard-format sections. **`## Words`**: added the reflexive stand-in [[詠]] alongside the existing [[詠春拳]] (self-corrected a guessed-wrong 注音 after checking its actual page). **Bug fixed on [[詠]] (word)**: literal `vietnamese: "null"` corrected to `vịnh`; empty `# Notes` stub filled with the standard citation. **Self-corrected a linking error**: initially linked 永 as `[[永 (char)|永]]`, but the actual file is `永.md` (no `(char)` suffix) — fixed to `[[永]]`. **False positive correctly excluded**: [[古今東西]] doesn't cite 詠 in its `characters` field. **Derived-Characters check**: [[泳 (char)|泳]] cites 永 directly as its own phonetic donor — a sibling, not a child of 詠 — correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 菊 (char) (6399; 1273 characters remaining).

### 2026-08-10, iteration 1231 — [[characters/菊 (char)|菊]]

**`mc_id: 4551` outside the vault's verifiable range**: 菊 does not appear in `CC 0000`–`CC 3000` and has no aliases. **Classification, Vietnamese, and korean_native all confirmed correct as-is**: `graphemic_classification: 匊` matches Wiktionary (semantic [[Radical 140|艸]] + phonetic 匊, pageless in this vault); `vietnamese: cúc` matches Wiktionary's sole reading; `korean_native: 국화` matches the literal eumhun exactly. **`japanese_native: ø` confirmed genuinely correct, a second clean case after [[鉢]]**: Wiktionary explicitly lists only on'yomi (きく) and nanori (あき/ひ) for this character, no kun'yomi at all.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: added the reflexive stand-in [[菊]] alongside the newly-found [[菊月]]. **Bug fixed on [[菊]] (word)**: literal `vietnamese: "null"` corrected to `cúc`; empty `# Notes` stub filled with the standard citation. **False positive correctly excluded**: [[季秋]] doesn't cite 菊 in its `characters` field. **Derived-Characters check**: [[鞠]] cites 匊 directly as its own phonetic donor — a sibling, not a child of 菊 — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 欄 (6400; 1272 characters remaining).

### 2026-08-10, iteration 1232 — [[characters/欄|欄]]

**`mc_id: 5151` outside the vault's verifiable range**: 欄 does not appear in `CC 0000`–`CC 3000` and has no aliases. **`graphemic_classification: 䦨` investigated and confirmed correct as-is, another shinjitai/pageless-preference case**: Wiktionary's primary etymology names 闌 as the phonetic donor, but 闌 has no vault page while [[䦨]] (explicitly documented as "a corrupted form of 闌," same OC ancestry) does — matching the established pattern (cf. [[填]]→真, [[剰]]→乗).

**Vietnamese narrowed**: removed `lườn`, unsupported anywhere in Wiktionary's five-item reading set. **`korean_native: 난간` and `japanese_native: てすり` both confirmed correct as-is**: the eumhun matches exactly; てすり is one of four genuinely attested kun'yomi.

Filled empty `pos` → `名詞`. Rebuilt `# Notes` (wrong heading level, a stray unheaded `## Words`-style bullet) into properly separated standard-format sections. **`## Words`**: tagged the existing [[欄杆]] stand-in citation — already corruption-free. **Derived-Characters check**: [[蘭]] cites 䦨 directly as its own phonetic donor — a sibling, not a child of 欄 — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 刃 (6401; 1271 characters remaining).

### 2026-08-10, iteration 1233 — [[characters/刃|刃]]

**`mc_id: 1389` verified correct as-is**: checked `CC 1000.md` line 406, confirmed 刃 itself sits at that rank.

**Real classification bug found and fixed**: stored `graphemic_classification: 象形` directly contradicted the page's own existing Notes bullet ("[List of 指事]") and Wiktionary (指事: a knife 刀 with an emphasis mark on the blade) — corrected to `指事`.

**`aliases: [仞]` investigated, a genuinely borderline case kept rather than removed**: 仞's *primary* modern meaning is an unrelated unit of length — at first glance another instance of this sweep's spurious-alias pattern — but Wiktionary's own definitions list for 仞 explicitly documents an "obsolete" secondary usage as an alternate form for "blade," specifically naming 刃. Kept, with the nuance documented directly in the Notes, distinguishing it from the fully-unrelated cases removed elsewhere this sweep (cf. [[醜]]/麤, [[翁]]/鶲).

**Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: `[nhẫn, nhấn, nhận]` matches Wiktionary; `korean_native: 칼날` ("blade edge") fits despite no eumhun being given; `japanese_native: は` matches the first listed kun'yomi exactly.

Filled empty `pos` → `名詞`. Rebuilt `## Notes` to the standard 4-bullet format — also corrected the Korean lookup link from `Korean HS` to [Korean Name ㄴ](lookup/Korean/Korean%20Name%20ㄴ.md), matching this vault's established `hanmun_edu_level: 名` convention and the page's own note that 刃 was dropped from the Korean HS list in 2000. **`## Words`**: tagged the existing [[刀刃]] stand-in citation. **New `## Derived Characters` section added**: [[忍]] cites 刃 directly as its own phonetic donor. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 倹 (char) (6403; 1270 characters remaining).

### 2026-08-10, iteration 1234 — [[characters/倹 (char)|倹]]

**`mc_id: 1296`, a genuine "recorded under alias" case, confirmed correct as-is**: 倹 itself doesn't appear in any CC list, but its traditional alias 儉 sits at rank 1296 in `CC 1000.md` — matches precisely since Wiktionary explicitly documents 倹 as the shinjitai form of 儉. **`graphemic_classification: 㑒` confirmed correct as-is, another shinjitai/pageless-preference case**: Wiktionary's etymology for 儉 names the traditional 僉 as phonetic, but 㑒 (an unofficial extended shinjitai of 僉, sharing its role) has a vault page while 僉 doesn't — matching the established pattern.

**Malformed YAML fixed**: `japanese_native` was a scalar (`つづまやか`, the historical variant spelling) followed by an orphaned list item (`つずまやか`, the modern standard spelling) — corrected to the single clean modern value `つずまやか`.

**Vietnamese and korean_native both confirmed correct as-is**: `[kiệm, cợm, hiếm, thiếu]` matches Wiktionary's set exactly (already properly formatted, per an earlier fix documented on the citing word [[倹素]]'s own page); `korean_native: 검소할` matches the eumhun "검소하 검" closely.

Filled blank `boundedness` → `80`. Rebuilt `# Notes` (wrong heading level, bare two-link stub) to the standard 4-bullet format. **`## Words`**: tagged the existing [[倹素]] stand-in citation — already fully perfected, no corruption. **Derived-Characters check**: [[㪘 (char)|㪘]], [[剣 (char)|剣]], [[険 (char)|険]], [[験 (char)|験]], [[鹸 (char)|鹸]], [[検]], [[瞼]] all cite 㑒 directly as their own phonetic donor — siblings of 倹, not children — correctly excluded. **Chengyu**: no hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 偽 (char) (6404; 1269 characters remaining).

### 2026-08-10, iteration 1235 — [[characters/偽 (char)|偽]]

**A clean cycle — `mc_id: 1144`, classification, both aliases, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 1000.md` line 153, confirmed 偽 itself sits at that rank; `graphemic_classification: 為` matches Wiktionary (semantic [[Radical 009|人]] + phonetic [[為 (char)|為]]); traditional 僞 and simplified 伪 both confirmed genuine; `vietnamese: nguỵ`, `korean_native: 거짓`, and `japanese_native: いつわ` all confirmed. **Homophone check**: confirmed [[委]] (word)'s own reciprocal callout with [[偽]] (word) was already completed on both sides — no action needed.

Rebuilt `# Notes` (wrong heading level, one bare bullet) to the standard format. **`## Words`** expanded from one entry to three: added the reflexive stand-in [[偽]] and the newly-found [[虚偽]], alongside the properly-rubied [[偽善]] — self-corrected two guessed-wrong 注音/stand-in-tag mistakes mid-edit after checking the actual pages (an initial mix-up mistakenly tagged [[偽善]] as the `stand_in`, when the field is actually self-referencing 偽 itself). **New `## Chengyu` section added**: [[殺姦窃偽]] genuinely cites 偽; two other hits were false positives. **Derived-Characters check**: nothing else in the vault currently cites 為 as a phonetic donor.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 促 (char) (6405; 1268 characters remaining).

### 2026-08-10, iteration 1236 — [[characters/促 (char)|促]]

**`mc_id: 2587` verified correct as-is** (`CC 2000.md` line 612, 促 itself). **`graphemic_classification: 足` confirmed**: 形聲, semantic [[Radical 009|人]] ("person") + phonetic [[足]] (OC \*ʔsoɡ, "foot") — "a person's feet moving quickly," hence "to hurry; to urge on."

**Vietnamese spurious-item removed**: stored `[thúc, xóc, xúc]`, but raw Wiktionary lists only xúc and thúc; checked the citing word [[促]] (word)'s own prior research first (the 壇/鹿 lesson) and found it explicitly corroborating the same conclusion — xóc is "an unrelated native word" and was deliberately excluded there. Narrowed to `[xúc, thúc]`, matching both Wiktionary and the citing word's own documented reasoning. **korean_native (재촉할) and japanese_native (うなが, matching kun'yomi うながす) both left as-is** — consistent with Wiktionary, no contradiction found; a second kun'yomi せまる ("to approach") exists but is an unrelated secondary sense outside this character's documented scope (hurry/rush/hasten) and was not added.

Rebuilt `## Notes` (two bare wikilinks with no bullet formatting, missing SKIP/stroke/level lines) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in entry [[促]] (the character's own `stand_in` field is self-referencing) alongside the existing [[督促]] citation. **Derived-Characters/Chengyu check**: no other page cites 促 as a phonetic donor; no Chengyu citations found.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 隆 (char) (6406; 1267 characters remaining).

### 2026-08-10, iteration 1237 — [[characters/隆 (char)|隆]]

**`mc_id: 1135` verified correct as-is** (`CC 1000.md` line 144, 隆 itself). **Wrong-component classification bug**: `graphemic_classification` stored `夅` (a pageless component that is itself 降's own phonetic donor, one step too deep), but Wiktionary's etymology names 隆's direct phonetic as [[降]] ("phono-semantic compound: phonetic 降 + semantic 生, with 𡕒 later dropped") — and 降 has its own vault page. Corrected to `降`, and the Notes bullet now links the true semantic component [[生]] directly rather than the Kangxi radical index.

**Spurious-alias removed**: `窿` was listed as an alias, but its own Wiktionary etymology shows it's a phonetic-donor *child* of 隆 (semantic 穴 + phonetic 隆), not a genuine variant — not among Wiktionary's eight listed alternative forms for 隆 either. Removed, keeping only the confirmed-genuine `𨺓`.

**`korean_native` wrong-gloss bug**: stored `높을` ("high"), but the raw `{{ko-hanja}}` eumhun is 클 (keul, "big; great") — corrected to `클`. **`japanese_native` ø-placeholder bug**: Wiktionary lists real kun'yomi (さかん, たかい, historical たかし, なかだか); chose さかん (盛ん, "thriving, prosperous") as the best match for this character's documented sense scope (prosperous/plentiful/abundant), leaving the unrelated "high" and onomatopoeic senses out. Filled blank `pos` → `性詞`.

Rebuilt `## Notes` (wrong heading level, two bare CC-link stubs, no other content) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in entry [[隆]] alongside the existing, already-perfected [[穹窿]] citation. **Citing word page `words/隆.md` was badly corrupted** — `vietnamese: null` literal-string bug, missing `pos`/`kwin`/`date-last-perfect`, scalar `characters` field instead of a list, wrong Notes heading level, and no Notes content — fully rebuilt to match standard word-page conventions.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 銘 (char) (6408; 1266 characters remaining).

### 2026-08-10, iteration 1239 — [[characters/雌|雌]]

**mc_id off-by-one fixed**: stored `1963` actually belongs to 歙 (`CC 1000.md` line 1004); 雌 itself sits at rank 1964 (line 1005) — corrected. **`graphemic_classification: 此` field confirmed correct** (phonetic per Wiktionary: phonetic 此 OC \*sʰeʔ + semantic 隹), but **the Notes prose had semantic/phonetic reversed** (the b2 pattern seen before on 屈/那/醜/肖) — it read "semantic 此 + phonetic 隹," backwards from the field itself; corrected the prose to match, and filled in 此's empty gloss ("this").

**Two genuine aliases added**: Wiktionary's own "alternative forms" list gives 䳄 and 𲍵 for 雌 (previously empty) — same category as 隆's confirmed-genuine 𨺓 alias precedent. Filled blank `pos` → `名詞`, matching the stand-in word [[雌性]]'s own `pos`. Vietnamese (`thư`), korean_native (`암컷`), and japanese_native (`め`) all confirmed correct as-is against Wiktionary.

Rebuilt `## Notes` (wrong heading placement — Words appeared before Notes — bare unlinked CC lines, no SKIP/stroke/level bullet) to the standard format. Since `hanmun_edu_level: 名` and the existing "dropped from Korean HS list in 2000" note both signal this is a name-use hanja rather than a standard-curriculum one, the levels bullet links [Korean Name ㅈ] (confirmed 雌 is listed there) instead of a Korean HS page — same pattern established on [[刃]]. **Derived-Characters check**: 些/柴/紫/砦 all derive from 此 directly as their own phonetic donor (siblings of 雌, not children of it) — correctly no Derived-Characters section added. **`## Words`**: existing [[雌性]] citation confirmed accurate and already fully perfected; no other citations found; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 隣 (char) (6410; 1264 characters remaining).

### 2026-08-10, iteration 1240 — [[characters/隣 (char)|隣]]

**`mc_id: 1150` confirmed legitimate** under the "recorded under alias" pattern (pattern d): 隣 doesn't appear independently in any `CC` list, but rank 1150 belongs to its traditional alias 鄰 (`CC 1000.md` line 159) — left as-is, Notes phrased accordingly. **`graphemic_classification: 粦` confirmed correct** (pageless phonetic component, semantic [[Radical 170|阜]]). **Genuine alias added**: Wiktionary's own alternative-forms row also lists simplified 邻 alongside already-stored traditional 鄰 — added. Vietnamese (`lân`), korean_native (`이웃`), and japanese_native (`とな`, stem of となり) all confirmed correct as-is.

Filled blank `pos` → `性詞` (Statives — "expected to modify," matching "neighboring; next door"). **Checked `checklist_characters.md` before touching the blank `boundedness` field and confirmed it isn't one of the 10 tracked completion criteria at all** — left blank rather than fabricating a value, per the explicit precedent already documented in `Loop Work.md` (継's iteration caught the same near-mistake).

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines with no bullet formatting) to the standard 4-bullet format. **`## Words` expanded from empty to three entries**: reflexive stand-in [[隣]], plus newly-found [[隣人]] and [[隣国]]. **New `## Chengyu` section**: [[勿貪隣物]] genuinely cites 隣. **Citing word page `words/隣.md` was corrupted** — `vietnamese: null` literal-string bug, scalar `characters` field, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content — fully rebuilt. `words/隣人.md` and `words/隣国.md` checked; both are stub-quality but not corrupted (blank fields, not `null` literals) — left alone as out of scope for character-level perfecting.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 躍 (char) (6412; 1263 characters remaining).

### 2026-08-10, iteration 1242 — [[characters/頼|頼]]

**`mc_id: 1426` confirmed legitimate** under the "recorded under alias" pattern: 頼 doesn't appear independently in any `CC` list, but rank 1426 belongs to its traditional alias 賴 (`CC 1000.md` line 447) — left as-is, Notes phrased accordingly. **`graphemic_classification: 剌` confirmed correct** (pageless phonetic component; semantic [[Radical 154|貝]]). **Genuine alias added**: simplified 赖, alongside the already-stored traditional 賴.

**`korean_native` wrong-gloss bug**: stored `의뢰할`, but that's actually the *Sino-Korean* reading of the compound 依頼 (의뢰) dressed up as a native gloss — not a genuine native/vernacular word at all. The raw eumhun is 힘입을 (himibeul, "to receive benefit/strength from") — corrected. **Vietnamese pile expanded**: stored only `lại`, but Wiktionary's Hán Nôm table lists two more genuine readings, `nái` and `trái` — the sole citing word [[依頼]] doesn't address Vietnamese at all, no contradiction found — added. Filled blank `pos` → `事詞`, matching [[依頼]]'s own stored `pos`.

Rebuilt `## Notes` (a stray `### Derived Characters` subsection nested under Notes instead of its own top-level section, two floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **The `### Derived Characters` entry `[[獺]]` was removed**: verified via Wiktionary that 獺 genuinely derives from 賴/頼's phonetic component, but 獺 has no vault page at all (confirmed by search) — per the checklist, this section only lists descendants that already exist in the database, so a broken link to a non-existent page doesn't belong here. **`## Words`**: added the existing [[依頼]] stand-in citation (already fully perfected, no corruption) to a Words section that previously didn't exist at all; no other citations or Chengyu hits found.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 賦 (char) (6414; 1261 characters remaining).

### 2026-08-10, iteration 1243 — [[characters/賦 (char)|賦]]

**`mc_id: 706` verified correct as-is** (`CC 0000.md` line 733, blockquote format, 賦 itself). **`graphemic_classification: 武` confirmed correct** (semantic [[Radical 154|貝]] + phonetic 武). **Genuine alias added**: 䝾, independently verified via its own Wiktionary page ("this character is a variant form of 賦" / "賦 is the orthodox traditional form of 䝾") — added alongside the already-stored simplified 赋.

**`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi みつぎ (mitsugi, "tribute; tax") — added as-is (already a bare noun, no okurigana to strip). Vietnamese (`phú`) and korean_native (`부세`) both confirmed correct as-is. Filled blank `pos` → `名詞`. **Self-corrected an unsupported etymological claim mid-edit**: initially wrote that the "prose-poetry" sense was a literary extension of the "tribute" sense, but re-checked Wiktionary's full definitions list and confirmed no such connection is documented between the two senses — revised the Notes bullet to present them as separate, unrelated senses instead of inventing a causal link.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in entry [[賦]] to a Words section that didn't exist at all. **Checked citing word `words/賦.md` for corruption**: found it uses `品詞` instead of `pos` — confirmed via corpus-wide grep (863 other word pages use the same field name) that this is simply words' own separate schema convention, not a bug; left untouched. Its blank-content `# Notes` section is a completeness gap belonging to the separate word-perfecting checklist, not the corruption patterns this loop fixes — left alone as out of scope. **Derived-Characters/Chengyu check**: nothing else in the vault cites 賦; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 侍 (char) (6415; 1260 characters remaining).

### 2026-08-10, iteration 1244 — [[characters/侍|侍]]

**A clean cycle — `mc_id: 538`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 559 (blockquote format), confirmed 侍 itself sits at that rank; `graphemic_classification: 寺` matches Wiktionary (semantic [[Radical 009|人]] + phonetic [[寺]]); `vietnamese: thị`, `korean_native: 모실`, and `japanese_native: さむらい` all confirmed (Wiktionary lists no aliases/variants either — the blank `aliases` field is correct as-is). Filled blank `pos` → `名詞`, matching the stand-in word [[侍者]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from empty to two entries**: the reflexive stand-in [[侍者]] and the newly-found [[侍奉]]. **Citing word `words/侍奉.md` had a stray leftover debug paragraph** ("Real content bug found and fixed: `korean` had the syllables reversed...") — a self-note fragment that had leaked into the page's actual Notes content from a prior session, matching the established "stray leftover scratch text" pattern (seen before on 頻, 傑) — removed, leaving only the genuine etymology/gloss prose. **Derived-Characters/Chengyu check**: nothing else in the vault cites 侍; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 賊 (char) (6417; 1259 characters remaining).

### 2026-08-10, iteration 1245 — [[characters/賊|賊]]

**`mc_id: 464` verified correct as-is** (`CC 0000.md` line 482, blockquote format). **`graphemic_classification: 則` confirmed correct**: Wiktionary's etymology gives phonetic 則 (matching the stored field) + originally semantic 戈 ("weapon"), with the modern form later reinterpreted as [[Radical 154|貝]] + 戎 — noted both layers in the Notes bullet since the character's own `radical` field (貝) reflects only the later reinterpretation, not the original semantic component.

**English Wiktionary's page for 賊 kept truncating mid-fetch** (unusually long etymology/compounds section) — worked around it by querying the Japanese, Korean, and Vietnamese Wiktionaries directly instead. **Confirmed `japanese_native: ø` is genuinely correct** (not the placeholder bug): `ja.wiktionary.org` explicitly lists only on'yomi (ゾク/ソク) with no kun'yomi at all — same "genuinely has none" pattern as 鉢/菊. **korean_native (도둑) confirmed correct** via `ko.wiktionary.org`'s own 훈 field. Vietnamese (`giặc`, `tặc`) could not be directly re-confirmed (the vi.wiktionary fetch didn't surface a reading table), but no contradicting evidence turned up either — left unchanged rather than guessing.

**Two genuine aliases added**: 戝 (independently verified via its own Wiktionary page — "this character is a variant form of 賊") and 𧵪, alongside the already-stored simplified 贼. Filled blank `pos` → `名詞`, matching the stand-in word [[盗賊]]'s own `pos`.

Rebuilt `## Notes` (misplaced `## Words` section ahead of two floating unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from one entry to two**: tagged the existing [[盗賊]] as the reflexive stand-in and added the newly-found [[烏賊]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 賊; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 貳 (char) (6418; 1258 characters remaining).

### 2026-08-10, iteration 1246 — [[characters/貳 (char)|貳]]

**`mc_id: 1301` verified correct as-is** (`CC 1000.md` line 318). **`graphemic_classification: 弍` field confirmed correct** (phonetic, matching Wiktionary), but **the Notes prose had semantic/phonetic reversed AND a broken empty link**: it read "semantic [[弍]] + phonetic [[]]" — backwards, with the phonetic link entirely blank — corrected to "semantic [[Radical 154|貝]] + phonetic [[弍]]".

**`korean_native` truncation bug**: stored `두`, but the raw 훈 (via `ko.wiktionary.org`) is `둘` ("two") — the stored value was missing its final consonant, corrected. Vietnamese confirmed correct as content (`nhị/nhì/nhẹ`), reordered to match Wiktionary's own primary-first presentation (`nhị` moved first). japanese_native (`そえ`) left as-is — matches one of two genuine kun'yomi, chosen over `ふたつ` as the better fit for this page's documented sense ("disloyal; betray") rather than the base numeral sense. Filled blank `pos` → `性詞`.

**A large stray leftover paragraph was found duplicated on both the character page and its citing word page** `words/貳.md`: a rambling draft note about the SKIP-code derivation (explicitly deriving "SKIP-3-3-8" mid-paragraph — contradicted by both the stored `skip_number: 3-3-9` frontmatter and the `SKIP-3-3-9.md` lookup page, which already lists 貳 as a member) had leaked into both pages' Notes sections, alongside a bare, unlinked prose blurb about a non-existent word "貳臣" sitting where `## Words` should be. Removed from both pages (used a small Python script to strip the line cleanly after the Edit tool repeatedly failed to match it — the paragraph contained a U+2013 en-dash immediately followed by a U+00A0 non-breaking space, invisible in the rendered text but not matching a plain hyphen+space). **Fully rebuilt `words/貳.md`** to match standard word-page conventions (was also missing `pos`/`date-last-perfect`, had a scalar `characters` field and a blank `vietnamese`).

Rebuilt `## Notes` to the standard 4-bullet format; since `hanmun_edu_level: 名` and the existing "dropped from Korean MS list in 2000" note both flag this as a name-use hanja, the levels bullet links [Korean Name ㅇ] (confirmed 貳 is listed there) instead of a Korean MS/HS page. **`## Words`**: rebuilt with the reflexive stand-in entry [[貳]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 貳; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 貪 (char) (6419; 1257 characters remaining).

### 2026-08-10, iteration 1247 — [[characters/貪 (char)|貪]]

**A clean cycle — `mc_id: 912`, classification, alias, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 945 (blockquote format); `graphemic_classification: 今` matches Wiktionary (phonetic [[今]] + semantic [[Radical 154|貝]], a 形聲/會意 hybrid); `vietnamese: tham`, `korean_native: 탐낼`, and `japanese_native: むさぼ` all confirmed; the single stored alias 贪 (simplified) matches, no other variants listed. Filled blank `pos` → `性詞`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, two bare/inconsistently-ruby'd Words entries sitting in the Notes section) to the standard 4-bullet format. **`## Words` expanded to three entries**: added the missing reflexive stand-in [[貪]], and moved the existing [[貪官]] (fixed to proper ruby formatting, was a bare link) and [[貪林]] citations into their own section. **New `## Chengyu` section**: [[勿貪隣物]] (already known from 隣's iteration) and the newly-found [[貪官汚吏]] both genuinely cite 貪. **Citing word `words/貪.md` was corrupted** — `vietnamese: null` literal-string bug, scalar `characters` field, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content — fully rebuilt. `words/貪官.md` and `words/貪林.md` checked, no corruption found.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 販 (char) (6420; 1256 characters remaining).

### 2026-08-10, iteration 1248 — [[characters/販|販]]

**mc_id off-by-one fixed**: stored `2894` actually belongs to 籥 (`CC 2000.md` line 931); 販 itself sits at rank 2895 (line 932) — corrected. **`graphemic_classification: 反` confirmed correct** (semantic [[Radical 154|貝]] + phonetic 反). **`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi あきなう (akinau, "to trade") — stored as the stem あきな.

**Vietnamese pile expanded**: stored only `phán`, but Wiktionary's own Hán Nôm table lists a second genuine reading, `phiến` — the sole citing word [[販売]] doesn't address Vietnamese at all, no contradiction found — added. korean_native (`팔`) confirmed correct via `ko.wiktionary.org`'s own 훈 field (팔다/사다/장사). Filled blank `pos` → `事詞`, matching [[販売]]'s own stored `pos`. **`#cranberry` tag and shared `stand_in: 販売` re-verified**: both 販 and its partner [[売]] independently store `stand_in: 販売` (transitivity holds, A=B=AB) — confirmed consistent, no fix needed.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words`**: added the missing [[販売]] citation, phrased to note the shared cranberry stand-in relationship. **Derived-Characters/Chengyu check**: nothing else in the vault cites 販; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 譜 (char) (6421; 1255 characters remaining).

### 2026-08-10, iteration 1249 — [[characters/譜|譜]]

**`mc_id: 4358` confirmed as a trusted long-tail value per checklist policy**: not present in any of the four `CC 0000`–`CC 3000` lookup files (which only mirror the top ~4000 ranks) — per the documented policy, a large existing value like this is treated as ground truth from the fuller source ranking rather than "corrected" to blank; MC bullet phrased accordingly, matching the [[欄]] precedent. **`graphemic_classification: 普` confirmed correct** (semantic [[Radical 149|言]] + phonetic 普).

**`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi しるす ("to record") and つづく ("to continue") — chose しるす (stem しる) as the better fit, since "record/register" is the common thread across this character's documented senses (musical score, genealogy). Vietnamese (`phả`/`phổ`) and korean_native (`족보`) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the stand-in word [[楽譜]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from empty to two entries**: the existing stand-in [[楽譜]] and the newly-found [[族譜]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 譜; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 堕 (char) (6422; 1254 characters remaining).

### 2026-08-10, iteration 1250 — [[characters/堕|堕]]

**A real, long-standing conflation bug found and fixed**: `graphemic_classification` stored `随` (a wholly different, unrelated character meaning "to follow," with its own distinct etymology and phonetic donor 𡐦) instead of `隋` (the true phonetic component per Wiktionary — homophonous with 随 but graphemically and etymologically separate, the Sui-dynasty-name character). The page's own leftover joke note — "With apologies to the dynasty, the characters are conflated" — was a stale, unresolved acknowledgment of exactly this bug, left in place rather than fixed. Cross-checking the citing word [[堕天使]]'s own Notes confirmed a *prior* session had already caught and fixed the same underlying mix-up for the `vietnamese` field (was `tuỳ`, 随's reading — corrected to `đọa`, 堕's genuine reading) but never touched `graphemic_classification`, and [[堕落]]'s Notes had been hedging with "phonetic 随/隋" rather than committing. Confirmed via Wiktionary that 隋 is genuinely documented as the shared ancient form behind not just 墮/堕 itself but also its phonetic siblings 惰/隳/橢 (all independently verified, not spurious) — so all five stored aliases (隋, 墮, 惰, 隳, 橢) are correct as-is. Fixed the field to `隋`, rewrote the Notes bullet to explain the resolved conflation explicitly, and updated [[堕落]]'s own hedge to the resolved "phonetic 隋."

**`mc_id: 1579` confirmed legitimate** under the "recorded under alias" pattern (墮, `CC 1000.md` line 604; 堕 doesn't appear independently). Vietnamese (`đọa`) and korean_native (`떨어질`) both confirmed correct as-is — left the Vietnamese list at its already-narrowed single value rather than re-expanding it, respecting [[堕天使]]'s explicit prior research rather than re-litigating a settled call.

Rebuilt `## Notes` (non-standard format mixing bare wikilinks, a stray joke aside, and a floating uncredited word-list) to the standard 4-bullet format. **`## Words` expanded from two entries (one unruby'd) to three**: [[堕落]], [[堕胎]] (fixed to proper ruby formatting), and the newly-found [[堕天使]]. False positives ([[天]], [[腹行食塵]], [[創反救成]]) correctly excluded via exact `characters:` field check.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 謀 (char) (6423; 1253 characters remaining).

### 2026-08-10, iteration 1251 — [[characters/謀 (char)|謀]]

**A clean cycle — `mc_id: 331`, classification, alias, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 346 (blockquote format); `graphemic_classification: 某` matches Wiktionary (semantic [[Radical 149|言]] + phonetic 某); `vietnamese: mưu` and `korean_native: 꾀` both confirmed; `japanese_native: たばか` initially looked like it might not match Wiktionary's listed kun'yomi (はかる/はかりごと), but a direct check of `ja.wiktionary.org` confirmed たばかる is genuinely a third listed kun'yomi — left as-is. **Considered and rejected adding 籌 as an alias**: Wiktionary lists it as an occasional Japanese-only ateji substitution for one specific reading (謀 read as はかりごと), not a genuine cross-linguistic variant of the same word — doesn't meet the bar for a true alias, unlike the 隋-family precedent on [[堕]]. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong callout wording, non-standard heading spacing, an empty semantic gloss, two floating unlinked CC-name lines, Words entries scattered before/after/between Notes content) to the standard format. **`## Words` expanded from three entries (two unruby'd/unlinked) to four**: added the reflexive stand-in [[謀]], and fixed [[謀求]] (was a bare unlinked string) to proper ruby formatting alongside the already-correct [[権謀]] and [[参謀]]. **Citing word `words/謀.md` was corrupted** — `vietnamese: null` literal-string bug, scalar `characters` field, missing `pos`/`kwin`/`date-last-perfect`, generic non-naming callout text, wrong Notes heading, no content — fully rebuilt. **Derived-Characters check**: nothing else in the vault cites 謀; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 誘 (char) (6424; 1252 characters remaining).

### 2026-08-10, iteration 1252 — [[characters/誘|誘]]

**`mc_id: 1657` verified correct as-is** (`CC 1000.md` line 686). **`graphemic_classification: 秀` confirmed correct** (semantic [[Radical 149|言]] + phonetic 秀). **Six genuine alternative-form aliases added**: 䛻 (independently verified via its own Wiktionary page — explicitly "alternative form of 誘/诱"), plus 㕗/唀/𥤃/𦎙/𦎅 from the same "alternative forms" listing, trusted per the established precedent from 隆/雌/賦/賊's own alternative-form additions.

Vietnamese confirmed correct as content (all four stored readings match Wiktionary's set exactly), reordered to put the Hán Việt reading `dụ` first, matching Wiktionary's own presentation order. korean_native (`꾈`) confirmed correct — verified the root verb is 꾀다 (not 꾀하다), so the attributive form 꾈 is the right conjugation, matching the vault's established modifier-form convention. japanese_native (`いざな`) confirmed correct, matching one of three genuine kun'yomi. Filled blank `pos` → `動詞`, matching the stand-in word [[誘発]]'s own stored `pos` (this vault's character-level `pos` field allows `動詞` per `checklist_characters.md`'s own example list, distinct from the word-level 品詞 taxonomy).

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, Words entries embedded directly in Notes) to the standard 4-bullet format. **`## Words` expanded from two entries (one unruby'd) to four**: added the reflexive stand-in [[誘発]] tag, fixed [[誘拐]] to proper ruby formatting, and added the newly-found [[誘餌]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 誘; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 詐 (char) (6425; 1251 characters remaining).

### 2026-08-10, iteration 1253 — [[characters/詐|詐]]

**`mc_id: 981` verified correct as-is** (`CC 0000.md` line 1014, blockquote format). **`graphemic_classification: 乍` confirmed correct** (semantic [[Radical 149|言]] + phonetic 乍). **Vietnamese contamination bug removed**: stored `[cha, dối, trá]`, but Wiktionary's Hán Nôm table lists only `trá` and `cha` — `dối` doesn't appear anywhere in 詐's own reading data; the sole citing word [[詐取]] doesn't attest it either and explicitly notes Vietnamese instead reaches for unrelated compounds (gian lận, lừa đảo) for this sense — removed as spurious contamination, narrowed to `[trá, cha]`.

korean_native (`속일`) confirmed correct via `ko.wiktionary.org`'s own 훈 field (속이다 → attributive 속일, matching the vault's modifier-form convention). japanese_native (`いつわ`) confirmed correct, matching the sole listed kun'yomi いつわる. Filled blank `pos` → `事詞`, matching [[詐取]]'s own stored `pos`. `hsk_level` is genuinely blank (character isn't in the vault's HSK list) — omitted the HSK link in the levels bullet rather than guessing one, per the [[銘]] precedent.

Rebuilt `## Notes` (Words section placed before a wrong-heading-level Notes section with two bare unlinked CC-name lines) to the standard 4-bullet format. **`## Words`**: tagged the existing [[詐取]] as the reflexive stand-in citation. **Derived-Characters/Chengyu check**: nothing else in the vault cites 詐 as a phonetic donor; one Chengyu grep hit ([[羊衣餓狼]]) was a false positive on exact `characters:` field check, correctly excluded.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 訟 (char) (6426; 1250 characters remaining).

### 2026-08-10, iteration 1254 — [[characters/訟 (char)|訟]]

**`mc_id: 1188` verified correct as-is** (`CC 1000.md` line 197). **`graphemic_classification: 公` confirmed correct** (semantic [[Radical 149|言]] + phonetic [[公 (char)|公]]). **Genuine alias added**: 吅, independently verified via its own Wiktionary page ("this character is recorded... as an ancient form of 訟"), alongside the already-stored simplified 讼.

**`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi あらそう ("to dispute") and うったえる ("to sue/accuse") — chose うったえる (stem うった) as the better match for this page's documented sense ("sue"). korean_native (`송사할`) confirmed correct via `ko.wiktionary.org`'s own 훈 field (송사하다 → attributive 송사할). Vietnamese (`tụng`) confirmed correct as-is. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (missing SKIP/stroke/level bullets, one malformed graphemic bullet using bare relative-path links instead of proper wikilinks, two floating unlinked CC-name lines) to the standard 4-bullet format. **`## Words` expanded from empty to two entries**: the reflexive stand-in [[訟]] and the newly-found [[訴訟]]. **Citing word `words/訟.md` was corrupted** — blank `vietnamese`, scalar `characters` field, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content — fully rebuilt. **Self-caught a curly-quote contamination**: an Edit call had somehow introduced curly quotes (" ") in place of straight ASCII quotes across the 注音 field and several Notes/Words strings — caught on the final verification Read and fixed with a small script before finalizing. **Derived-Characters/Chengyu check**: nothing else in the vault cites 訟; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 乞 (char) (6427; 1249 characters remaining).

### 2026-08-10, iteration 1255 — [[characters/乞 (char)|乞]]

**`mc_id: 1253` verified correct as-is** (`CC 1000.md` line 266). **Wrong-classification bug fixed**: stored `graphemic_classification: 一`, which doesn't correspond to any real component of 乞 or a valid TYPE label — Wiktionary describes 乞 as "a variant of 气 (OC \*kʰɯds), distinguished to indicate a phonetically borrowed meaning 'to beg,'" a graphic differentiation that doesn't fit 形聲 (no genuine separate phonetic component) or 象形/會意. Reclassified as 指事 per this vault's own `List of 指事.md` guidance ("if a base form is modified by a stroke... if the stroke points to a feature → 指事") — the closest fit among the four available categories for a stroke-level differentiation marking an abstract/borrowed distinction from a pageless parent form.

**Vietnamese contamination confirmed and fixed — a `壇/鹿`-lesson case**: stored `[gật, khất, khắt]`; Wiktionary's own Hán Nôm table actually lists four raw candidates (`khất, khắt, gật, khật`), but checking the citing word [[乞]] (word)'s own prior deep research FIRST revealed it had already explicitly diagnosed `gật` ("to nod") and `khắt` (part of khắt khe, "strict, harsh") as belonging to unrelated words and deliberately excluded them — narrowed to just `khất`, the sole genuine Hán Việt reading; did not add the fourth raw candidate `khật` either, trusting the citing word's already-settled research over the raw undifferentiated pile. korean_native (`빌`) and japanese_native (`こ`) both independently confirmed correct by that same citing-word research. Filled blank `pos` → `動詞`, matching [[乞]]'s own stored `pos`.

Rebuilt `## Notes` (single bare fact bullet, no other content) to the standard format (指事 opening format, per the checklist). **`## Words` expanded from one entry (unruby'd) to two**: added the reflexive stand-in [[乞]] and fixed [[乞丐]] to a proper wikilink. **New `## Derived Characters` section**: [[紇]] and [[迄]] both genuinely cite 乞 as their own phonetic donor — a Chengyu grep hit ([[安心立命]]) was a false positive, correctly excluded via exact `characters:` field check.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 蛮 (char) (6428; 1248 characters remaining).

### 2026-08-10, iteration 1256 — [[characters/蛮|蛮]]

**`mc_id: 1129` confirmed legitimate** under the "recorded under alias" pattern (traditional 蠻, `CC 1000.md` line 138; 蛮 doesn't appear independently). **`graphemic_classification: 䜌` confirmed correct** (semantic [[Radical 142|虫]] + pageless phonetic 䜌).

**Vietnamese contamination fixed**: stored `[man, manh]`; `manh` doesn't appear anywhere in Wiktionary's own Hán Nôm table (`man, mán, mơn`) and doesn't match any documented variant spelling — no citing word addresses Vietnamese at all, so treated as a stray corruption and corrected to the genuine three-item set `[man, mán, mơn]`. **Considered and rejected adding 滿/满 as an alias**: Wiktionary lists them as "alternative forms" but explicitly ties them to the unrelated sense "quite" — doesn't meet the bar for a genuine same-word alias, matching the established spurious-alias discipline. korean_native (`오랑캐`) and japanese_native (`えびす`) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the stand-in word [[蛮人]]'s own `pos`.

Rebuilt `## Notes` (Words section preceding a one-bullet Notes section with floating unlinked CC-name lines) to the standard 4-bullet format; since `hanmun_edu_level: 名` and the existing "dropped from Korean HS list in 2000" note both flag this as a name-use hanja, the levels bullet links [Korean Name ㅁ] (confirmed 蛮/蠻 is listed there) instead of Korean HS. **`## Words` expanded from one entry to two**: added the missing reflexive stand-in [[蛮人]] alongside the existing [[蛮夷]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 蛮; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 荘 (char) (6430; 1247 characters remaining).

### 2026-08-10, iteration 1257 — [[characters/荘|荘]]

**`mc_id: 714` confirmed legitimate** under the "recorded under alias" pattern (traditional 莊, `CC 0000.md` line 741; 荘 doesn't appear independently). **`graphemic_classification: 壮` confirmed correct**: Wiktionary's etymology names the phonetic as traditional 壯, but 壮 (its own shinjitai) is the paged form in this vault — kept per the established shinjitai/pageless-donor preference, same precedent as [[剰]]/[[倹]]/[[欄]].

**`korean_native` wrong-gloss bug fixed**: stored `장중할` ("dignified/solemn"), but the raw 훈 via `ko.wiktionary.org` is 씩씩하다/깨끗하다 ("vigorous"/"clean") — no mention of 장중하다 at all; corrected to `씩씩할`. Vietnamese (`trang`, already narrowed from Wiktionary's larger five-item pile) and japanese_native (`おごそ`, matching one of five genuine kun'yomi) both confirmed correct as-is; `pos: 名詞` was already correctly filled in.

Rebuilt `## Notes` (two bare unlinked CC-name lines, no other content) to the standard 4-bullet format, noting the character's own separate shinjitai status (of traditional 莊, aliased alongside simplified 庄) distinctly from its phonetic component's shinjitai status (壮, of traditional 壯) to avoid conflating the two relationships. `hsk_level` is genuinely blank — omitted the HSK link rather than guessing one. **`## Words` expanded from one entry to two**: added the missing reflexive stand-in [[別荘]] alongside the existing [[荘子]]; four other grep hits ([[別野]], [[化粧]], [[別字]], [[混沌]]) were false positives, correctly excluded via exact `characters:` field check. **Derived-Characters/Chengyu check**: nothing else in the vault cites 荘; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 潜 (char) (6431; 1246 characters remaining).

### 2026-08-10, iteration 1258 — [[characters/潜|潜]]

**`mc_id: 1597` confirmed legitimate** under the "recorded under alias" pattern (traditional 潛, `CC 1000.md` line 622; 潜 doesn't appear independently). **`graphemic_classification: 朁` confirmed correct** (semantic [[Radical 085|水]] + pageless phonetic 朁). **Two genuine aliases added**: 濳 and 汘, both independently verified via their own Wiktionary pages ("variant form of 潛" and "second-round simplified form of 潛" respectively), alongside the already-stored traditional 潛.

**`japanese_native: かく` investigated and confirmed correct, reversing an initial suspicion**: my first instinct was that this looked like a truncation bug (かくれる's naive stem would be かくれ, dropping only the final る), but checking `ja.wiktionary.org`'s own official okurigana notation directly showed "かく-れる" — meaning かく (not かくれ) is the vault-convention-matching stem, with れる as the marked okurigana. Left unchanged. Vietnamese (`tiềm/tèm/tỉm`) and korean_native (`잠길`, confirmed via `ko.wiktionary.org`'s own 훈 "물에 잠기다") both confirmed correct as-is.

Rebuilt `## Notes` (wrong heading level, two floating unlinked CC-name lines, a stray leftover numbered-list draft mixing a bare sense gloss with an unformatted word mention) to the standard 4-bullet format. **`## Words` expanded from one entry to four**: added the reflexive stand-in [[潜在]], and the newly-found [[潜素]] (krypton) and [[潜水艦]] (submarine), alongside the existing [[潜伏]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 潜; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 履 (char) (6432; 1245 characters remaining).

### 2026-08-10, iteration 1259 — [[characters/履 (char)|履]]

**A clean cycle — `mc_id: 996`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 1029 (blockquote format); `graphemic_classification: 會意` confirmed as the correct bare-TYPE-label choice (Wiktionary itself hedges between 會意 and a "possibly phono-semantic" reading, but leads with the ideogrammic-compound analysis — no clean phonetic candidate exists); `vietnamese: [giày, giầy, lí]` matches Wiktionary's set; `korean_native: 밟을` confirmed directly via `ko.wiktionary.org`'s own 훈 field (밟다), despite one intermediate fetch surfacing a different-looking gloss ("신," "shoe") that turned out not to be the primary hoon; `japanese_native: は` confirmed as the correct stem of はく (one of three genuine kun'yomi). Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 會意 format — linked both the modern visible components ([[Radical 044|尸]] + [[復]]) and briefly noted the older four-part Shuowen analysis (尸+彳+夊+舟) that the modern form simplifies. **`## Words`**: added the missing reflexive stand-in [[履]] to a Words section that didn't exist at all. **Citing word `words/履.md` was corrupted** — `vietnamese: null` literal-string bug, scalar `characters` field, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content — fully rebuilt. **Derived-Characters/Chengyu check**: nothing else in the vault cites 履; two Chengyu grep hits ([[戦戦恐恐]], [[李下瓜田]]) were false positives, correctly excluded via exact `characters:` field check.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 恥 (char) (6433; 1244 characters remaining).

### 2026-08-10, iteration 1260 — [[characters/恥|恥]]

**`mc_id: 1053` verified correct as-is** (`CC 1000.md` line 58). **`graphemic_classification: 耳` confirmed correct** (phonetic 耳 + semantic [[Radical 061|心]]). **`japanese_native` truncation bug fixed**: stored bare `は`, but the genuine kun'yomi (はじ, はじる, はじらう, はずかしい) all require at minimum はじ — corrected to the bare noun はじ ("shame"), too short to be a valid stem of any listed reading on its own.

**Considered and rejected adding 辱/羞 as aliases**: Wiktionary's Japanese "Alternative forms" list groups 耻 (genuine simplified form, already stored), 辱, 羞, and 恥じ (a mere okurigana-inflected form of 恥 itself) together undifferentiated — checked 辱's own Wiktionary page and confirmed it has a wholly independent etymology (會意 of 辰+寸) with no documented variant relationship to 恥; 辱 and 羞 are near-synonym characters occasionally interchangeable in Japanese usage, not genuine orthographic variants of the same word — correctly excluded, matching the earlier [[謀]]/[[籌]] precedent. Vietnamese (`sỉ`/`xỉ`) and korean_native (`부끄러울`, confirmed via `ko.wiktionary.org`'s own 훈 부끄러워하다) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the stand-in word [[恥辱]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from one entry to four**: added the reflexive stand-in [[恥辱]], and newly-found [[恥骨]] and [[羞恥]], alongside the existing [[無恥]]; five other grep hits ([[厚]], [[骨]], [[低廉]], [[侮辱]], [[厚顔]]) were false positives, correctly excluded via exact `characters:` field check. **New `## Chengyu` section**: [[厚顔無恥]] genuinely cites 恥.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 羅 (char) (6434; 1243 characters remaining).

### 2026-08-10, iteration 1261 — [[characters/羅|羅]]

**`mc_id: 1494` verified correct as-is** (`CC 1000.md` line 515). **`graphemic_classification: 會意` confirmed correct** (网 "net" + [[維]] "bird tied with string" — a bird-catching net; bare TYPE label, matching this vault's established convention for 會意 characters without a clean single phonetic candidate). Vietnamese (`la`/`là`, re-confirmed directly via `vi.wiktionary.org`), korean_native (`벌릴` — plausible as a secondary "arrange in a row" sense of 羅, e.g. 羅列; left unchanged despite one incomplete fetch surfacing only "그물, net" since character-level glosses commonly cover multiple senses and no contradiction was found), and japanese_native (`うすもの`, matching 羅's documented "thin silk gauze" sense) all confirmed/left correct as-is. **Investigated but did not add two obscure "alternative forms" (𦋝, 𦌴)**: unlike prior successful spot-checks (隆/雌/賦/賊/誘), the verification fetch 404'd — left unadded rather than trusting an unverifiable claim. Filled blank `pos` → `性詞`, matching the stand-in word [[羅馬]]'s own `pos`.

**Major citation-discovery correction**: an initial broad `grep -l "羅"` across `words/` matched all 6013 word files — turned out every word page's frontmatter includes a `羅馬字:` (romanization) field, which contains 羅 as a substring; switched to a properly anchored pattern matching only the `characters:` YAML list, which correctly surfaced 11 genuine citations (up from the 6 already visible in the page's existing malformed content): the existing [[新羅]]/[[羅馬]]/[[魔羅]]/[[泥婆羅]]/[[尼羅河]]/[[羅倫金]], plus newly-found [[森羅]], [[欧羅巴]], [[羅馬字]], [[羅馬語]], and [[沙羅双樹]].

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, five bare/inconsistently-ruby'd Words-like entries embedded directly in Notes, a separate `## Words` section with only one more entry) to the standard 4-bullet format, consolidating into one `## Words` section (11 entries, including the reflexive stand-in tag on [[羅馬]]). **New `## Derived Characters` section**: [[蘿]], [[鑼]], and [[邏]] all genuinely cite 羅 as their own phonetic donor (via the same corrected search pattern). Existing `## Chengyu` entry ([[森羅万象]]) confirmed accurate.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 霊 (char) (6435; 1242 characters remaining).

### 2026-08-10, iteration 1262 — [[characters/霊|霊]]

**A real, unnoticed homophone-conflation bug found and fixed**: `graphemic_classification` stored `零` — but that's an entirely different, unrelated character ("zero," semantic 雨 + phonetic 令 per its own Wiktionary etymology), sharing only the same radical (雨) and same Mandarin reading (líng) as coincidence, not lineage. 靈/霊's actual documented phonetic is 霝 (an ancient character, pageless in this vault). Corrected the field to `霝` and made the non-relationship to [[零 (char)|零]] explicit in the Notes bullet to prevent the mix-up recurring. **`mc_id: 621` confirmed legitimate** under the "recorded under alias" pattern (traditional 靈, `CC 0000.md` line 645; 霊 doesn't appear independently).

**Vietnamese pile resolved from blank**: field was empty; Wiktionary's raw Hán Nôm table lists seven undifferentiated candidates (`linh, lanh, lẻng, leng, lênh, liêng, lình`), but two citing words ([[神霊]]: `thần linh`, [[霊芝]]: `Nấm linh chi`) already independently corroborate `linh` as the genuine standard reading — filled with just `[linh]`. korean_native (`신령`, a confirmed self-identical-gloss pattern matching precedent) and japanese_native (`たま`, one of four genuine kun'yomi) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the stand-in word [[霊魂]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, two bare/inconsistently-formatted Words entries sitting in Notes) to the standard 4-bullet format; `hsk_level` is genuinely blank, so the HSK link was omitted. **`## Words` expanded from two entries to six**: added the reflexive stand-in [[霊魂]], plus newly-found [[神霊]], [[霊芝]], and [[霊鬼]], alongside the existing [[霊長類]] and [[霊柩]] (all found via the properly-anchored `characters:`-field search pattern established last iteration on [[羅]]). **Derived-Characters/Chengyu check**: nothing else in the vault cites 霊; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 媒 (char) (6436; 1241 characters remaining).

### 2026-08-10, iteration 1263 — [[characters/媒|媒]]

**`mc_id: 2753` verified correct as-is** (`CC 2000.md` line 786). **`graphemic_classification: 某` confirmed correct** (semantic [[Radical 038|女]] + phonetic 某). **Vietnamese contamination fixed**: stored a six-item pile `[mai, moi, môi, mối, mồi, mụ]`, but Wiktionary's own Hán Nôm table lists only three genuine readings (`môi, mối, mai`) — no citing word addressed the three extras, narrowed to the confirmed three, dropping `moi`, `mồi`, `mụ`. korean_native (`중매`, a confirmed self-identical-gloss pattern) and japanese_native (`なこうど`, the primary listed kun'yomi) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the stand-in word [[仲媒]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from two entries to three**: added the missing reflexive stand-in [[仲媒]] alongside the existing [[媒体]] and [[媒介]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 媒; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 畜 (char) (6437; 1240 characters remaining).

### 2026-08-10, iteration 1264 — [[characters/畜|畜]]

**`mc_id: 813` verified correct as-is** (`CC 0000.md` line 843, blockquote format). **`graphemic_classification: 象形` confirmed correct**: Wiktionary explicitly labels the TYPE as Pictogram (象形) despite the compound-looking "玄 + 田" depiction — trusted the explicit type label. Notes rebuilt in the standard 象形 format, linking the character's own Kangxi radical 田 within the depiction per the checklist's radical-linking rule.

**`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi たくわえる, やしなう, かう — chose かう ("to keep/raise animals") as the most direct match for "livestock." **Vietnamese pile expanded**: stored `[súc, sục]`, but Wiktionary's own Hán Nôm table lists a third genuine reading, `húc` — no citing word ([[家畜]], [[畜生]]) addresses it either way — added. korean_native (`짐승`) left unchanged despite one fetch surfacing a different-looking gloss (가축, itself Sino-Korean) — treated as the same "incomplete fetch, not necessarily wrong" situation as [[羅]]'s 벌릴, since 짐승 is a well-attested standard native gloss for this character with no direct contradiction found. `pos: 事詞` was already correctly filled in.

**`## Words` expanded from empty to two entries**: the reflexive stand-in [[畜生]] and [[家畜]]. **New `## Derived Characters` section**: [[蓄 (char)|蓄]] genuinely cites 畜 as its own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 誇 (char) (6438; 1239 characters remaining).

### 2026-08-10, iteration 1241 — [[characters/躍|躍]]

**mc_id off-by-one fixed**: stored `2339` actually belongs to 探 (`CC 2000.md` line 356); 躍 itself sits at rank 2340 (line 357) — corrected. **`graphemic_classification: 翟` confirmed correct** (semantic [[Radical 157|足]] + phonetic 翟). **Both aliases confirmed genuine**: simplified 跃, and 趯 verified via its own Wiktionary page ("this character is a variant form of 躍," sharing the same pronunciation/definitions, not a phonetic-sibling child).

**Vietnamese pile expanded**: stored only `dược`, but Wiktionary's own Hán Việt/Nôm reading tables list a second genuine Nôm reading, `vược` — no citing-word research contradicted this ([[踊躍]], [[雀躍]], [[跳躍]] don't address Vietnamese at all) — added. korean_native (`뛸`) and japanese_native (`おど`, stem of おどる) both confirmed correct as-is. Filled blank `pos` → `性詞`, matching all three citing compounds' own stored `pos`.

Rebuilt `## Notes` (misplaced `## Chengyu` section ahead of two floating unlinked CC-name lines, no SKIP/stroke/level bullet) to the standard format. **`## Words` expanded from empty to three entries**: [[踊躍]], [[雀躍]], and the reflexive stand-in [[跳躍]]. **`## Chengyu`**: the existing bare `[[欣喜雀躍]]` link (no ruby, no gloss) reformatted to the standard ruby+注音+gloss form; a second grep hit ([[海闊天空]]) was a false positive on exact `characters:` field check, correctly excluded. **Derived-Characters check**: nothing else in the vault cites 躍 as a phonetic donor.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 頼 (char) (6413; 1262 characters remaining).

### 2026-08-10, iteration 1238 — [[characters/銘|銘]]

**mc_id off-by-one fixed**: stored `2301` actually belongs to 誨 (`CC 2000.md` line 318); 銘 itself sits at rank 2302 (line 319) — corrected. **`graphemic_classification: 名` confirmed**: Wiktionary's etymology is semantic 金 ("metal") + phonetic 名 (OC \*meŋ, "name") — "to engrave in metal."

**`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi しるす (shirusu, "to inscribe") — stored as the stem しる. **Vietnamese narrowed pile expanded, not narrowed**: stored only `minh`, but Wiktionary's own Hán Nôm reading table lists a second genuine reading, `triệu` — no citing-word research contradicted this (銘 has no standalone word page; the only citation, [[銘文]], doesn't address Vietnamese at all) — added. **korean_native (새길) confirmed correct as-is** against the raw eumhun. Filled blank `pos` → `名詞` (character functions as a noun, "inscription," matching its stand-in [[銘文]]'s own `pos`).

Rebuilt `## Notes` (wrong heading level, only two bare CC-link lines, no other content) to the standard 4-bullet format — `hsk_level` is genuinely blank (character isn't in the vault's HSK list), so the levels bullet omits an HSK link rather than guessing one. **`## Words`**: existing [[銘文]] citation confirmed accurate, no other citations found. **Derived-Characters/Chengyu check**: nothing else in the vault cites 銘 as a phonetic donor; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 雌 (char) (6409; 1265 characters remaining).

### 2026-08-10 — Log gap notice

**A documentation gap was discovered in this log**: this file's narrative entries stop here (after 銘, iteration 1238), but a direct check of `characters/*.md` frontmatter confirms the actual perfecting work continued uninterrupted and was correctly saved for every character from 雌 (danayo_id 6409) through 誇 (char) (danayo_id 6438) — 27 characters in total, all correctly stamped `date-last-perfect: 2026-08-10`: 雌, 隣, 躍, 頼, 賦, 侍, 賊, 貳, 貪, 販, 譜, 堕, 謀, 誘, 詐, 訟, 乞, 蛮, 荘, 潜, 履, 恥, 羅, 霊, 媒, 畜, and 誇. The character pages themselves are trustworthy; only the prose log entries documenting *how* each was fixed failed to persist to this file, most likely due to a session/compaction artifact. Rather than fabricate detailed after-the-fact narratives for 27 cycles from imperfect memory, this gap is logged honestly here instead. The bug patterns applied across this stretch were consistent with the rest of this log (mc_id off-by-ones and "recorded under alias" cases, spurious/genuine alias verification, `ø` japanese_native fixes, Vietnamese pile narrowing/expansion per citing-word research, korean_native gloss corrections, and citation sweeps) — notably including two real conflation bugs (隆's 夅→降 and 霊's 零→霝) caught and fixed the same way as this log's other entries.

Next never-perfected character by `danayo_id`: 伴 (char) (6439; 1238 characters remaining).

### 2026-08-10, iteration 1266 — [[characters/伴|伴]]

**`mc_id: 6255` confirmed as a trusted long-tail value per checklist policy**: not present in any of the four `CC 0000`–`CC 3000` lookup files — treated as ground truth rather than "corrected," MC bullet phrased accordingly (matching the [[欄]]/[[譜]] precedent). **`graphemic_classification: 半` confirmed correct** (semantic [[Radical 009|亻]] + phonetic 半).

**Vietnamese contamination fixed**: stored a four-item pile `[bạn, bọn, gạn, vạn]`, but Wiktionary lists only one genuine reading (`bạn`, both Hán Việt and Nôm) — both citing words ([[同伴]]: đồng bạn, [[伴侶]]: bạn lữ) independently corroborate `bạn` alone, with no support for the other three — narrowed accordingly. korean_native (`짝`) and japanese_native (`ともな`, stem of ともなう) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the stand-in word [[同伴]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, empty semantic gloss, two floating unlinked CC-name lines) to the standard 4-bullet format. **`## Words` expanded from empty to two entries**: the reflexive stand-in [[同伴]] and [[伴侶]]. **Derived-Characters/Chengyu check**: nothing else in the vault cites 伴; no Chengyu hits.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 淫 (char) (6440; 1237 characters remaining).

### 2026-08-10, iteration 1267 — [[characters/淫 (char)|淫]]

**A real component-substitution bug found and fixed**: `graphemic_classification` stored `壬`, but Wiktionary's etymology names the true phonetic as 㸒 (pageless) — 壬 is merely a graphic sub-component *of* 㸒 itself (㸒 = 爫 + 壬 structurally) and carries a wholly unrelated reading of its own (rén, not yín), so it can't stand in as "the phonetic" the way a shinjitai/simplified same-reading substitute could. Corrected to `㸒`, with the non-equivalence to [[壬]] made explicit in the Notes bullet. **`mc_id: 724` verified correct as-is** (`CC 0000.md` line 751, blockquote format).

**Vietnamese pile drastically narrowed**: stored an 11-item pile (`dâm, dầm, dẫm, giâm, giầm, râm, rầm, sầm, đầm, đẫm, đằm`) that only partially overlapped with Wiktionary's own 8-item Hán Nôm table and included several items absent from it entirely; the citing word [[姦淫]] (`gian dâm`) independently corroborates `dâm` as the genuine Hán Việt reading — narrowed to just `[dâm]`. korean_native (`음란할`) left unchanged despite the raw eumhun literally reading 음탕하다 rather than 음란하다 — treated as within-tolerance synonym variation (both mean "lewd/licentious," unlike [[荘]]'s genuinely distinct-meaning case) rather than a clear error. japanese_native (`ひた`, stem of ひたす) confirmed correct. **Two genuine aliases added**: 婬 (independently verified — "alt. form 淫") and 滛. Filled blank `pos` → `性詞`.

Rebuilt `## Notes` (wrong heading level, one bare Words entry sitting in Notes) to the standard 4-bullet format; `hanmun_edu_level: 無` correctly links [Korean Missing] per the checklist's mapping table. **`## Words` expanded from one entry to three**: added the reflexive stand-in [[淫]] and newly-found [[姦淫]], alongside the existing [[淫靡]]. **Citing word `words/淫.md` was corrupted** (blank `vietnamese`, scalar `characters`, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content) — fully rebuilt. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 審 (char) (6441; 1236 characters remaining).

### 2026-08-10, iteration 1268 — [[characters/審|審]]

**`mc_id: 893` verified correct as-is** (`CC 0000.md` line 923, blockquote format). **`graphemic_classification: 會意` confirmed correct** (bare TYPE label; components 宀 + 釆 + 田, with the 田 component's own derivation debated between two theories — both noted). **`japanese_native: つぶさ` investigated and confirmed correct**: initial suspicion it might be wrong since one fetch surfaced only つまびらか, but a direct `ja.wiktionary.org` check confirmed つぶさ-に is genuinely listed as a second kun'yomi — left unchanged.

**Vietnamese pile drastically narrowed**: stored a 10-item pile (`săm, sẩm, sặm, thăm, thấm, thẩm, thẫm, thắm, thẳm, thủm`); direct Wiktionary Vietnamese-section fetches kept truncating (page too long, same failure mode as [[賊]] earlier), so relied on citing-word corroboration instead — both [[審査]] (`thẩm tra`) and [[審訊]] (`thẩm vấn`) independently use `thẩm`, confirming it as the genuine reading — narrowed to `[thẩm]` alone. korean_native (`살필`) confirmed correct. Filled blank `pos` → `事詞`, matching [[審査]]'s own stored `pos`.

Rebuilt `## Notes` (misplaced `## Words` section ahead of a wrong-heading-level Notes section with two floating unlinked CC-name lines) to the standard 會意 format, linking the Kangxi-radical components ([[Radical 040|宀]], [[Radical 102|田]]) per the checklist's radical-linking rule. **`## Words` expanded from one entry to two**: tagged the existing [[審査]] as the reflexive stand-in and added the newly-found [[審訊]]. **Self-corrected a guessed-wrong 注音 mid-edit**: initially guessed `ㄙㄧㄇㄒㄧㄋ` for 審訊 instead of checking its actual page — caught immediately, verified the real value (`ㄙㄧㄇㄙㄧㄋ`), fixed. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-10`.

Next never-perfected character by `danayo_id`: 幣 (char) (6442; 1235 characters remaining).

### 2026-08-11, iteration 1269 — [[characters/幣 (char)|幣]]

**`mc_id: 1022` verified correct as-is** (`CC 1000.md` line 27). **`graphemic_classification: 敝` confirmed correct** (phonetic 敝 + semantic [[Radical 050|巾]]), but **a spurious alias removed**: `aliases` also listed 敝 itself — but Wiktionary explicitly identifies 敝 only as the phonetic component, never as a variant/alias of 幣 (敝 is an unrelated word, "worn out; dilapidated") — removed, keeping only the genuine simplified 币.

**`korean_native` wrong-gloss bug**: stored `화폐`, which is itself just the Sino-Korean reading of the compound 貨幣 dressed up as a native gloss (the same pattern as [[頼]]'s 의뢰할 mistake) — the raw 훈 via `ko.wiktionary.org` is 비단 ("silk") or 돈 ("money"); corrected to `돈`, matching this page's own "cash" sense. Vietnamese (`tệ`/`giẻ`, reordered to lead with the Hán Việt reading) and japanese_native (`ぬさ`) both confirmed correct as content. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from one entry to three**: added the reflexive stand-in [[幣]] and newly-found [[貨幣]], alongside the existing [[造幣局]]. **Citing word `words/幣.md` was corrupted** — `vietnamese: null` literal-string bug, scalar `characters` field, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, and a stray leftover fragment ("1284") dangling at the end of the file — fully rebuilt. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 帥 (char) (6443; 1234 characters remaining).

### 2026-08-11, iteration 1270 — [[characters/帥|帥]]

**`mc_id: 795` verified correct as-is** (`CC 0000.md` line 822, blockquote format). **`graphemic_classification: 堆` investigated and confirmed correct, not a bug**: Wiktionary names 𠂤 as 帥's actual phonetic donor, but 堆's own etymology explicitly states "the original form is 𠂤" — a genuine documented lineage (not mere homophone coincidence, unlike the [[隆]]/[[霊]]/[[淫]] conflation bugs found earlier), and 堆 is the vault-paged form while 𠂤 has none — kept per the established shinjitai/pageless-donor-preference precedent, with the reasoning spelled out explicitly in the Notes bullet this time to head off future confusion.

**Vietnamese pile expanded from a clean, labeled source**: stored `[soái, suý]`; Wiktionary's own Hán Việt reading section (not a messy Nôm pile, but a clean three-item labeled list: primary + two variants) includes a third genuine reading, `suất` — added. **`japanese_native` ø-placeholder bug fixed**: sole kun'yomi ひきいる ("to lead") — stored as the stem ひきい. korean_native (`장수`) confirmed correct. Filled blank `pos` → `名詞`, matching the stand-in word [[将帥]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words`**: tagged the existing [[将帥]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 弦 (char) (6444; 1233 characters remaining).

### 2026-08-11, iteration 1271 — [[characters/弦 (char)|弦]]

**`mc_id: 1291` verified correct as-is** (`CC 1000.md` line 304). **`graphemic_classification: 玄` confirmed correct** (semantic [[Radical 057|弓]] + phonetic 玄). Vietnamese (`huyền`), korean_native (`활시위`, "bowstring" — matches the definition directly), and japanese_native (`つる`, sole kun'yomi) all confirmed correct as-is. Confirmed genuine alias 絃 already stored; three further "alternative forms" (𢎺, 𢏸, 𢏛) couldn't be independently verified (both spot-check fetches 404'd) — left unadded rather than trusting an unverifiable claim. Filled blank `pos` → `名詞`.

**Reconsidered the `hanmun_edu_level` levels-bullet note mid-edit**: the page's own pre-existing "dropped from the Korean HS list in 2000" note conflicted with the stored `hanmun_edu_level: 高等` (which maps to a Korean HS link per the mapping table); trusted the current field value as the source of truth and linked Korean HS, dropping the now-superseded historical note rather than fabricating a resolution between them.

Rebuilt `## Notes` (wrong heading level, no other content) to the standard 4-bullet format. **`## Words` expanded from empty to six entries**: the reflexive stand-in [[弦]], plus newly-found [[上弦]], [[下弦]], [[正弦]], [[正弦波]], and [[余弦]]. **Found and fixed a missing-field bug on citing word `words/余弦.md`**: its own Notes prose explicitly referenced "注音 ⼄ㄏㄝㄋ" but the frontmatter `注音` field itself was entirely absent — added. **Citing word `words/弦.md` was corrupted** (`vietnamese: null`, scalar `characters`, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content) — fully rebuilt. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 宰 (char) (6445; 1232 characters remaining).

### 2026-08-11, iteration 1272 — [[characters/宰|宰]]

**A real wrong-type-label bug found and fixed**: `graphemic_classification` stored `辛`, mimicking a 形聲 phonetic-component reference, but Wiktionary explicitly classifies 宰 as 會意 (宀 "house" + 乂 "to govern") — the modern form's lower component only visually resembles 辛 through graphic evolution and carries no phonetic value or etymological link to it at all. Corrected the field to the bare TYPE label `會意`, and made the non-relationship to [[辛]] explicit in the Notes bullet (both [[乂]] and [[辛]] have their own vault pages, linked accordingly). **`mc_id: 814` verified correct as-is** (`CC 0000.md` line 844, blockquote format).

**`korean_native` wrong-gloss bug**: stored `재상` — itself the Sino-Korean compound 宰相 ("chancellor") dressed as a native gloss, the same recurring pattern as [[頼]]/[[幣]] — the raw 훈 via `ko.wiktionary.org` is 우두머리 ("chief, head") / 지휘 감독하다 ("to command, supervise"); corrected to `감독할`, matching this page's own "superintend" sense. **`japanese_native` ø-placeholder bug fixed**: Wiktionary kun'yomi つかさどる ("to administer") — stored as the stem つかさど. **Vietnamese narrowed**: stored `[tẻ, tể, tỉa]`, Wiktionary lists only `tể`; both citing words ([[主宰]]: chủ tể, [[宰相]]: tể tướng) independently corroborate — narrowed to `[tể]` alone.

Rebuilt `## Notes` (wrong heading level, one bare unlinked Words entry sitting in Notes) to the standard 會意 format. **Self-corrected two guessed-wrong 注音 values mid-edit**: initially guessed garbled Bopomofo for both [[主宰]] and [[宰相]] instead of checking their actual pages — caught immediately, verified the real values, fixed both. **`## Words`**: tagged the existing [[主宰]] as the reflexive stand-in, alongside [[宰相]]. **New `## Chengyu` section**: [[主宰万物]] genuinely cites 宰. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 慨 (char) (6446; 1231 characters remaining).

### 2026-08-11, iteration 1273 — [[characters/慨 (char)|慨]]

**mc_id off-by-one fixed**: stored `2767` actually belongs to 娣 (`CC 2000.md` line 800); 慨 itself sits at rank 2768 (line 801) — corrected. **`graphemic_classification: 既` confirmed correct** (semantic [[Radical 061|心]] + phonetic 既). Vietnamese (`khái`/`khới`) and korean_native (`분개할`, confirmed via `ko.wiktionary.org`) both confirmed correct as-is. japanese_native (`なげ`, stem of なげく) confirmed correct. **Genuine dual-etymology alias added**: 嘅, independently verified — Wiktionary documents two etymologies for it, one an unrelated Cantonese/Hakka grammatical particle, the other explicitly "a variant form of 慨" — added per the established nuanced-alias precedent (like [[誇]]'s 侉). Filled blank `pos` → `性詞`, matching [[憤慨]]/[[慷慨]]'s own stored `pos`.

**Broken pageless link caught and dropped**: the existing Notes cited `[[感慨]]` as a Words entry, but no such word page exists anywhere in the vault (confirmed via directory listing) — dropped rather than kept as a dead link.

Rebuilt `## Notes` (wrong heading level, misplaced `## Words` section with one bare/unruby'd entry and one broken link, floating unlinked CC-name lines) to the standard 4-bullet format. **`## Words` rebuilt to three genuine entries**: the reflexive stand-in [[慨]], the existing [[憤慨]], and [[慷慨]] (fixed to proper ruby formatting). No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 懲 (char) (6447; 1230 characters remaining).

### 2026-08-11, iteration 1274 — [[characters/懲|懲]]

**mc_id off-by-one fixed**: stored `2193` actually belongs to 擯 (`CC 2000.md` line 202); 懲 itself sits at rank 2194 (line 203) — corrected. **`graphemic_classification: 徴` investigated and confirmed correct, not a bug**: Wiktionary names 徵 (traditional) as the phonetic donor, but independently confirmed 徴 is genuinely its Japanese shinjitai (same reading/meaning, not a false-homophone conflation like the recent [[隆]]/[[霊]]/[[淫]] bugs) — kept per the established shinjitai-preference precedent, reasoning spelled out in the Notes bullet.

**Vietnamese narrowed**: stored `[trằng, trừng]`, Wiktionary lists only `trừng`; the citing word [[懲罰]] (`trừng phạt`) corroborates — narrowed to `[trừng]` alone. **`japanese_native: こ` investigated and confirmed correct**: looked like a possible truncation at first glance, but a direct check of `ja.wiktionary.org`'s official okurigana notation confirmed all three kun'yomi (こ-りる, こ-らす, こ-らしめる) genuinely share the bare stem こ — left unchanged, same lesson as [[審]]'s つぶさ and [[潜]]'s かく. korean_native (`징계할`) confirmed correct. Filled blank `pos` → `事詞`, matching [[懲罰]]'s own stored `pos`.

Rebuilt `## Notes` (wrong heading level, one bare unlinked Words entry sitting in Notes, floating unlinked CC-name lines) to the standard 4-bullet format. **Self-corrected a guessed-wrong 注音 mid-edit**: initially guessed `ㄑㄧㄫㄆㄚㄊ` for 懲罰 instead of checking its actual page — caught immediately, verified the real value (`ㄑㄧㄫㄅㄝㄊ`), fixed. **`## Words`**: tagged the existing [[懲罰]] as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 悩 (char) (6448; 1229 characters remaining).

### 2026-08-11, iteration 1275 — [[characters/悩 (char)|悩]]

**`mc_id: 7693` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 𡿺` confirmed correct** (semantic [[Radical 061|忄]] + phonetic [[𡿺]], which has its own vault page and was linked directly).

**Vietnamese filled from blank**: Wiktionary lists `não, náo`; the citing word [[苦悩]] (`khổ não`) corroborates `não` as genuine — filled with both. **Genuine variant alias added**: 㛴, independently verified ("this character is a variant form of 惱"), alongside the already-stored traditional 惱. korean_native (`괴로워할`) and japanese_native (`なや`, stem of なやむ) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching [[苦悩]]'s own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format; `hsk_level` is genuinely blank, so the HSK link was omitted. **`## Words` expanded from one entry to two**: added the missing reflexive stand-in [[悩]] (`stand_in: 悩` is self-referencing) alongside the existing [[苦悩]]. **Citing word `words/悩.md` had a double corruption**: both `vietnamese: null` AND `korean: "null"` literal-string bugs in the same file — fully rebuilt. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 徐 (char) (6450; 1228 characters remaining).

### 2026-08-11, iteration 1276 — [[characters/徐|徐]]

**`mc_id: 889` verified correct as-is** (`CC 0000.md` line 919, blockquote format). **`graphemic_classification: 余` confirmed correct** (semantic [[Radical 060|彳]] + phonetic 余). **Vietnamese pile completed rather than narrowed**: stored 7 of Wiktionary's 9 genuine Hán Nôm items (từ, chờ, chừa, giờ, thờ, trờ, xờ) — unlike the usual contamination cases, every stored item WAS genuine, just two were missing (chừ, dờ); added both rather than narrowing, since this was under-coverage, not contamination. korean_native (`천천히 할`) and japanese_native (`おもむ`) both confirmed correct as-is. Filled blank `pos` → `性詞`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words` expanded from empty to two entries**: the reflexive stand-in [[徐様]] and newly-found [[徐州]]. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 窃 (char) (6452; 1227 characters remaining).

### 2026-08-11, iteration 1277 — [[characters/窃|窃]]

**A real wrong-component bug found and fixed, an unusual variant of the pattern**: `graphemic_classification` stored `粝` ("unpolished rice," reading lì — wholly unrelated in both meaning and pronunciation to 窃/竊's qiè), while the true phonetic donor 禼 not only exists but already has its own vault page. Unlike prior cases where the pageless true phonetic justified a same-reading substitute, here there was no justification at all — 禼 was directly available and simply wasn't used. Corrected to `禼`. **`mc_id: 841` confirmed legitimate** under the "recorded under alias" pattern (traditional 竊, `CC 0000.md` line 871; 窃 doesn't appear independently).

Vietnamese (`thiết`), korean_native (`훔칠`), and japanese_native (`ぬす`, stem of ぬすむ) all confirmed correct as-is. Filled blank `pos` → `動詞`, matching the stand-in word [[窃取]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, a malformed graphemic bullet with a stray closing parenthesis and no OC/gloss, floating unlinked CC-name lines) to the standard 4-bullet format. **`## Words`**: tagged the existing [[窃取]] as the reflexive stand-in, alongside [[窃盗]]. **New `## Chengyu` section**: [[殺姦窃偽]] (already known from [[偽]]'s earlier iteration) genuinely cites 窃. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 矢 (char) (6453; 1226 characters remaining).

### 2026-08-11, iteration 1278 — [[characters/矢 (char)|矢]]

**A clean cycle — `mc_id: 925`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 0000.md` line 958 (blockquote format); `graphemic_classification: 象形` matches Wiktionary (pictogram of an arrow); `vietnamese: thỉ` already correctly narrowed from Wiktionary's 8-item Nôm pile — left as-is; `korean_native: 화살` is a confirmed self-identical-gloss pattern (matches the eumhun exactly); `japanese_native: や` matches one of two genuine kun'yomi. **Considered and rejected 箭 as an alias**: Wiktionary lists it as an "alternative spelling" for the concept "arrow," but its own etymology page confirms it's an independent 形聲 character (竹+前) — a Classical Chinese synonym for 矢, not a graphemic variant. `pos: 名詞` was already correctly filled in.

Rebuilt `## Notes` (wrong heading level, a "Components:"-style bullet mimicking 會意 format for what is actually a 象形 character, floating unlinked CC-name lines) to the standard 象形 format. Corrected `joyo_level: "2"` to route to [Jōyō - Kyōiku] rather than Kōtō (numeric grade levels map differently from the 高等 string per the checklist's table) and `hsk_level: "無"` to [HSK No]. **`## Words`**: added the missing reflexive stand-in [[矢]] — the existing, already-perfected citing word page `words/矢.md` had explicitly flagged the character page's own incompleteness in its own Notes, confirming this was overdue. **New `## Derived Characters` section**: [[疾]] genuinely cites 矢 as its own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 汝 (char) (6454; 1225 characters remaining).

### 2026-08-11, iteration 1279 — [[characters/汝 (char)|汝]]

**`mc_id: 686` verified correct as-is** (`CC 0000.md` line 710, blockquote format). **`graphemic_classification: 女` confirmed correct** (semantic [[Radical 085|水]] + phonetic 女). **`japanese_native` wrong-value bug fixed**: stored `い`, but `ja.wiktionary.org` confirms the genuine kun'yomi are なんじ and なれ — い doesn't appear among them at all; corrected to `なんじ`.

**Vietnamese pile drastically narrowed using deep prior research already on the citing word**: stored a 10-item pile; the citing word [[汝]] (word)'s own Notes contain an extensive phonological derivation explicitly settling on `nhữ` as the correct Sino-Vietnamese reading (with full 魚韻→ữ reasoning after the palatal 日母 initial) — narrowed the character page to match, `[nhữ]` alone. korean_native (`너`) confirmed correct via `ko.wiktionary.org`. **Considered, added, then self-reversed a 女-as-alias addition mid-cycle**: Wiktionary's "Alternative forms" list included 女 unqualified (unlike 你/爾 which carry explicit "cognate, different dialect" labels), but on reflection this reflects a Classical Chinese phonetic-loan (通假) usage of 女 for "you," not a genuine orthographic variant of the same lexeme like this vault's other confirmed aliases — reverted the addition rather than let a shaky justification stand. `pos: 代詞` was already correctly filled in.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `joyo_level: 日本人名用漢字` to [Jinmeiyō], `hsk_level: 無` to [HSK No], and `hanmun_edu_level: 中` to [Korean MS] per the checklist's mapping table. **`## Words`**: tagged the existing [[汝]] (word) citation as the reflexive stand-in. **New `## Chengyu` section**: [[欲夫治汝]] genuinely cites 汝. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 週 (char) (6455; 1224 characters remaining).

### 2026-08-11, iteration 1280 — [[characters/週|週]]

**`mc_id: 6704` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 周` confirmed correct** (semantic [[Radical 162|辵]] + phonetic 周; 週 is explicitly a 後起字 coined later than its phonetic root, kept semantically distinct from 周's own "circumference" sense per this vault's stated one-meaning-per-character policy, already noted in the page's own pre-existing prose).

**`japanese_native` malformed-YAML AND wrong-content bug fixed**: stored a comma-joined scalar `"めぐる, なぬか"` instead of a proper list; `ja.wiktionary.org` directly shows 週 has **no kun'yomi listed at all** (only on'yomi しゅ/しゅう) — めぐる is 周's own reading bleeding across from the phonetic-relation, and なぬか ("the 7th day") has no documentation tying it to 週 anywhere — corrected to `ø`, the established "genuinely has none" value (same pattern as [[鉢]]/[[菊]]/[[賊]]). Vietnamese (`chu`/`châu`) and korean_native (`돌`) both confirmed correct as-is.

**Major citation-discovery correction, and one false positive caught**: the properly-anchored `characters:`-field search (per the [[羅]] precedent) surfaced 17 genuine citations against the 12 already loosely present in the old Words section — 6 newly found ([[前週]], [[当週]], [[翌週]], [[連週]], [[週中]], [[週期表]]) — but also caught that the existing "[[週期]]" entry was a **false positive**: that word page's own `characters:` field cites 周, not 週, despite the superficial name match — removed rather than kept.

Rebuilt `## Notes` (wrong heading level, no SKIP/stroke/level bullets, floating unlinked CC-name lines) to the standard 4-bullet format; `joyo_level: "2"` routes to [Jōyō - Kyōiku], and `hanmun_edu_level: 名` routes to [Korean Name ㅈ] (confirmed 週 is listed there) rather than a standard Korean MS/HS page. **`## Words` rebuilt to 16 entries**, tagging the existing [[週日]] as the reflexive stand-in and fixing several bare/unruby'd entries to proper formatting along the way. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 磁 (char) (6456; 1223 characters remaining).

### 2026-08-11, iteration 1281 — [[characters/磁|磁]]

**`mc_id: 6225` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 玆` investigated and confirmed correct, not a bug**: Wiktionary names 兹 as the direct phonetic donor, but independently confirmed 玆 is a genuine documented variant of the same word (兹 is itself a simplified variant of 茲, and 玆 shares Etymology 2 with 茲 too) — kept per the shinjitai/variant-preference precedent, since 玆 is the vault-paged form.

**`japanese_native` ø-placeholder bug fixed**: Wiktionary lists two genuine kun'yomi (じしゃく, やきもの) — chose じしゃく, matching this page's "magnetism" sense directly. **korean_native investigated and left unchanged**: `자석` looked at first like the same Sino-Korean-compound-disguised-as-native pattern seen on [[頼]]/[[幣]]/[[宰]], but a direct `ko.wiktionary.org` check confirmed 자석 genuinely IS presented as this character's own dictionary 훈 — a legitimate case where a modern/technical concept lacks an older pure-native gloss, unlike those prior bugs. Vietnamese (`từ`) confirmed correct. Filled blank `pos` → `名詞`, matching the stand-in word [[磁性]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, one Words-like entry with imprecise "abbreviation for" phrasing sitting in Notes) to the standard 4-bullet format, routing `hsk_level: "1"` to [HSK Beginner] and `hanmun_edu_level: 名` to [Korean Name ㅈ] (confirmed 磁 is listed there) per the checklist's mapping table. **`## Words`**: tagged the existing [[磁性]] as the reflexive stand-in, alongside the constructed-neologism [[磁金]] (neodymium), rephrased more accurately from "abbreviation for" to "constructed periodic-table name." No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 映 (char) (6458; 1222 characters remaining).

### 2026-08-11, iteration 1282 — [[characters/映 (char)|映]]

**`mc_id: 6913` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 央` confirmed correct** (semantic [[Radical 072|日]] + phonetic 央).

**Two malformed-YAML bugs fixed**: both `vietnamese` (`"ánh, tử"`) and `japanese_native` (`"うつ-る,うつ-す,は-える"`, raw Wiktionary okurigana notation pasted directly with hyphens intact) were comma-joined scalar strings instead of proper lists — converted both to lists, stripping the japanese_native stems down to うつ (shared by both うつる and うつす) and は (from はえる) per the established stem convention. **`korean_native` corrected for precision**: stored `비출` (from 비추다, transitive "to shine upon"), but the raw eumhun via Wiktionary is specifically 비칠 (from 비치다, "to be reflected/shine") — corrected to match the literal source exactly.

Rebuilt `## Notes` (non-standard bullet order/formatting, a malformed graphemic bullet with a stray unmatched parenthesis, plain-text SKIP/Stroke bullet not matching the standard link format) to the standard 4-bullet format. **`## Words` expanded from empty to two entries**: the reflexive stand-in [[映]] and the newly-found [[反映]]. **Citing word `words/映.md` was corrupted** (blank `vietnamese`, scalar `characters`, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content) — fully rebuilt. **Self-caught a curly-quote contamination** in the character page's Notes/Words prose on the final verification Read — fixed with a small script before finalizing, same recurring issue as [[訟]]. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 裁 (char) (6459; 1221 characters remaining).

### 2026-08-11, iteration 1283 — [[characters/裁|裁]]

**mc_id off-by-one fixed**: stored `2003` actually belongs to 諡 (`CC 2000.md` line 8); 裁 itself sits at rank 2004 (line 9) — corrected. **`graphemic_classification: 𢦏` confirmed correct** (semantic [[Radical 145|衣]] + pageless phonetic 𢦏). Vietnamese (`tài`/`trài`, reordered to lead with the Hán Việt reading), korean_native (`마를`), and japanese_native (`さば`, stem of さばく) all confirmed correct as-is. Filled blank `pos` → `事詞`, matching the stand-in word [[裁縫]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words`**: tagged the existing [[裁縫]] as the reflexive stand-in, with its gloss corrected to match the citing word's own stored English ("tailor clothing") rather than a paraphrase. **Self-caught a broken wikilink mid-edit**: initially linked the pageless phonetic 𢦏 as `[[𢦏]]`, then verified no such vault page exists and fixed it to bare-text-with-"no character page" phrasing, matching established convention. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 操 (char) (6461; 1220 characters remaining).

### 2026-08-11, iteration 1284 — [[characters/操|操]]

**`mc_id: 846` verified correct as-is** (`CC 0000.md` line 876, blockquote format). **`graphemic_classification: 喿` confirmed correct** (semantic [[Radical 064|手]] + phonetic [[喿]], which has its own vault page and was linked directly). **Vietnamese pile completed rather than narrowed**: stored 4 of Wiktionary's 5 genuine Hán Nôm items — missing only `thảo`, which the sole citing word [[操作]] doesn't contradict — added. korean_native (`잡을`) and japanese_native (`あやつ`, stem of あやつる) both confirmed correct as-is. Filled blank `pos` → `事詞`, matching [[操作]]'s own stored `pos`.

Rebuilt `## Notes` (a duplicated `## Notes` heading with the actual content buried under the second copy, floating unlinked CC-name lines in between) to the standard 4-bullet format. **`## Words`**: tagged the existing [[操作]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 乳 (char) (6462; 1219 characters remaining).

### 2026-08-11, iteration 1285 — [[characters/乳|乳]]

**A real wrong-type-label bug found and fixed**: `graphemic_classification` stored `孚`, mimicking a 形聲 phonetic-component reference, but Wiktionary explicitly classifies 乳 as 象形 (a pictogram of a kneeling woman breastfeeding a child, resembling [[母]]) — 孚 only appears in a structural shape-decomposition note (⿰孚乚), never as a documented phonetic. Corrected to the bare TYPE label `象形`. **`mc_id: 1826` verified correct as-is** (`CC 1000.md` line 863).

**Spurious alias removed**: `奶` was listed as an alias, but Wiktionary explicitly treats it as an independent word with its own (uncertain) etymology, only noting it as a regional Eastern Min alternative character for a similar concept — not a genuine variant of 乳. **Vietnamese pile completed rather than narrowed**: stored 4 of Wiktionary's 7 genuine Hán Nôm items — multiple citing words ([[乳房]]: nhũ phòng, [[乳頭]]: Núm vú, [[乳酪]]: nhũ lạc) corroborate `nhũ`/`vú` as heavily used, with no evidence against the 3 missing items (nhỏ, nhủ, nhả) — added. korean_native (`젖`) and japanese_native (`ちち`) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching [[牛乳]]'s own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, `## Words` misplaced ahead of Notes) to the standard 象形 format. **`## Words` expanded from three entries to eight**: tagged the existing [[牛乳]] as the reflexive stand-in, and added five newly-found citations ([[乳房]], [[乳頭]], [[乳酪]], [[乳押]], [[哺乳]]) alongside the existing [[乳液]]/[[乳色]]. **New `## Chengyu` section**: [[乳蜜流地]] genuinely cites 乳. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 優 (char) (6463; 1218 characters remaining).

### 2026-08-11, iteration 1286 — [[characters/優|優]]

**A clean cycle — `mc_id: 1399`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 1000.md` line 416; `graphemic_classification: 憂` matches Wiktionary (semantic [[Radical 009|亻]] + phonetic 憂); `vietnamese: ưu`, `korean_native: 넉넉할`, and `japanese_native: やさ` all confirmed. `pos: 性詞` was already correctly filled in.

**Citation search caught an inline-array format the standard regex missed**: the usual `characters:`-field pattern didn't catch [[優先]], whose frontmatter uses inline-array syntax `characters: [優, 先]` rather than a YAML block list — broadened the search pattern to also match `\[優,` and found it, plus [[優秀]] (the stand-in word itself), [[俳優]], [[女優]], and [[男優]].

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, a malformed graphemic bullet with an empty semantic gloss) to the standard 4-bullet format. **`## Words` expanded from one entry to six**: added the reflexive stand-in [[優秀]], plus [[優先]], [[俳優]], [[女優]], and [[男優]], alongside the existing [[優等]]. Existing `## Chengyu` entry ([[優柔不断]]) confirmed accurate. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 憤 (char) (6464; 1217 characters remaining).

### 2026-08-11, iteration 1287 — [[characters/憤|憤]]

**mc_id off-by-one fixed**: stored `1904` actually belongs to 諂 (`CC 1000.md` line 945); 憤 itself sits at rank 1905 (line 946) — corrected. **`graphemic_classification: 奔` investigated closely and confirmed correct, a genuinely nuanced case**: Wiktionary's primary etymology line for 憤 names 賁 as the phonetic (賁 itself composed of 卉+貝), but 賁's own etymology explicitly documents that it was historically borrowed to write 奔, and Wiktionary's own phonetic-derivation table names 奔 specifically as the component for this bɯn-reading family — matching 憤's OC \*bɯnʔ far more precisely than 賁's own primary readings. Kept `奔` (both 奔 and 賁 have vault pages, so this wasn't a pageless-preference case) and documented the layered relationship explicitly in the Notes bullet rather than silently picking one.

Vietnamese (`phẫn`), korean_native (`분할`), and japanese_native (`いきどお`, stem of いきどおる) all confirmed correct as-is. **Both stored aliases reconfirmed genuine**: 忿 is explicitly documented as a 2nd-round-simplification form (not just a look-alike), alongside standard simplified 愤. Filled blank `pos` → `性詞`, matching the stand-in word [[憤慨]]'s own `pos`.

Rebuilt `## Notes` (misplaced `## Words` section ahead of a wrong-heading-level Notes with floating unlinked CC-name lines and one bare Words-like entry) to the standard 4-bullet format. **`## Words`**: tagged the existing [[憤慨]] as the reflexive stand-in and fixed [[憤怒]] to proper ruby formatting. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 亘 (char) (6465; 1216 characters remaining).

### 2026-08-11, iteration 1288 — [[characters/亘 (char)|亘]]

**`mc_id: 5459` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 會意` confirmed correct** for the character's chosen archaic "whirlpool" sense (二 + 囘). **Spurious alias removed**: `咺` was listed as an alias, but Wiktionary explicitly places it under 亘's *Derived characters* section (using 亘 as its own phonetic donor), never as a variant — removed (no vault page exists for it, so no Derived-Characters entry either).

**A textbook 壇/鹿-lesson case, checked before editing**: the sole citing word [[亘]] (word)'s own deep prior research explicitly warns that five of the six stored Vietnamese items (`cẳng, cẵng, cứng, gắng, hẵng`) are "implausible near-homophone candidates," having already independently verified the genuine three-reading set as `cắng, hoàn, tuyên` — narrowed the character page to match exactly, discarding the pile rather than trusting Wiktionary's own (less carefully vetted) Nôm table. **`korean_native` corrected for precision**: stored `뻗칠` (a close synonym), but the raw eumhun via `ko.wiktionary.org` is specifically 걸치다 ("to span/extend over") — corrected to `걸칠`, matching the literal source despite the character's own chosen sense being unrelated ("whirlpool," not "extend") — same precedent as [[賦]]'s 부세. japanese_native (`わた`) independently confirmed correct by that same citing word's own research. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (missing entirely — no heading, only floating unlinked CC-name lines) to the standard 會意 format, explicitly noting the character's multi-etymology history (obsolete whirlpool sense vs. the visually-merged 亙 "extend" sense that dominates modern usage) per the citing word's own explanation, and routing `hsk_level: 無`/`joyo_level: 日本人名用漢字`/`hanmun_edu_level: 名` to [HSK No]/[Jinmeiyō]/[Korean Name ㄱ] respectively. **`## Words`**: added the missing reflexive stand-in [[亘]]. **New `## Derived Characters` section**: [[垣 (char)|垣]], [[宣]], and [[桓]] all genuinely cite 亘 as their own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 吏 (char) (6466; 1215 characters remaining).

### 2026-08-11, iteration 1289 — [[characters/吏|吏]]

**`mc_id: 224` verified correct as-is** (`CC 0000.md` line 236, blockquote format). **`graphemic_classification: 會意` confirmed correct** (a hand holding a flag/document, representing an official envoy). **Vietnamese contamination fixed**: stored `[lưỡi, lại]`; `lưỡi` belongs to an unrelated homophone sense ("tongue/blade") not documented anywhere in 吏's own etymology — both citing words ([[官吏]]: quan lại, [[汚吏]]: ô lại) independently corroborate `lại` alone as the genuine reading for this "official" sense — narrowed accordingly.

**`japanese_native` ø-placeholder bug fixed**: Wiktionary lists a genuine kun'yomi つかさ ("official, one in charge") — added. korean_native (`벼슬아치`) confirmed correct. Filled blank `pos` → `名詞`, matching [[官吏]]'s own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, noting the phonetic relationship to [[史]] mentioned in Wiktionary's own etymology. **`## Words` expanded from one entry to two**: added the missing reflexive stand-in [[官吏]] alongside the existing [[汚吏]]. **New `## Chengyu` section**: [[貪官汚吏]] (already known from [[貪]]'s earlier iteration) genuinely cites 吏. **New `## Derived Characters` section**: [[使]] independently verified as genuinely deriving from 吏 as both its semantic and phonetic component (not mere visual resemblance).

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 損 (char) (6467; 1214 characters remaining).

### 2026-08-11, iteration 1290 — [[characters/損|損]]

**A clean cycle — `mc_id: 878`, classification, and Vietnamese all confirmed correct as-is**: checked `CC 0000.md` line 908 (blockquote format); `graphemic_classification: 員` matches Wiktionary (semantic [[Radical 064|手]] + phonetic [[員]]); all five stored Vietnamese items (`tỏn, tốn, tổn, tủn, vin`) matched Wiktionary's own set exactly, just reordered to lead with `tốn` per Wiktionary's own presentation order. korean_native (`덜`) confirmed correct.

**`japanese_native` ø-placeholder bug fixed**: Wiktionary lists three genuine kun'yomi (そこなう, そこねる, へる) — stored as the shared stem そこな. Filled blank `pos` → `事詞`, matching the stand-in word [[損失]]'s own `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, `## Words` misplaced ahead of Notes) to the standard 4-bullet format. **`## Words`**: tagged the existing [[損失]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 肩 (char) (6468; 1213 characters remaining).

### 2026-08-11, iteration 1291 — [[characters/肩 (char)|肩]]

**mc_id off-by-one fixed**: stored `1683` actually belongs to 湖 (`CC 1000.md` line 712); 肩 itself sits at rank 1684 (line 713) — corrected. **A real wrong-type-label bug found and fixed**: `graphemic_classification` stored `戸`, mimicking a 形聲 phonetic-component reference, but Wiktionary's own etymology explicitly labels the character 象形 in its main-entry prose while its "Alternative forms" table separately calls all three script variants 會意 — since the character genuinely combines two components (戶, a shape drawing of a shoulder + 月/肉, "flesh") rather than being a single unbroken pictorial image, and 戶 here contributes shape/meaning rather than sound, classified as `會意` (matching the more structurally accurate of the two conflicting Wiktionary labels, following this vault's established "bare TYPE label" convention for 會意 characters without one single clean phonetic).

Vietnamese (`khiên`/`kiên`) left unchanged — no independent Vietnamese Wiktionary page was reachable to re-verify, and no citing word addresses it either way. korean_native (`어깨`) and japanese_native (`かた`, confirmed as 肩's sole listed kun'yomi via `ja.wiktionary.org`) both confirmed correct. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, one bare Words-like entry sitting in Notes) to the standard 會意 format. **`## Words` expanded from one entry to three**: added the reflexive stand-in [[肩]] and newly-found [[肩甲骨]], alongside the existing [[肩章]]. **Citing word `words/肩.md` was corrupted** (`vietnamese: null`, scalar `characters`, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content) — fully rebuilt. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 凍 (char) (6469; 1212 characters remaining).

### 2026-08-11, iteration 1292 — [[characters/凍|凍]]

**Blank `mc_id` filled in**: no rank was ever stored; found 凍 at `CC 2000.md` line 34, filled with `2029`. **`graphemic_classification: 東` confirmed correct** (semantic [[Radical 015|冫]] + phonetic 東). **Genuine simplified alias added**: 冻, alongside investigating and correctly excluding 涷 (an unrelated separate character meaning "rainstorm," despite superficial resemblance and a "See also" cross-reference on its own Wiktionary page).

**Two malformed-YAML bugs fixed**: `japanese` (bare scalar `TOU`) and `japanese_native` (bracket-list-with-hyphenated-okurigana `[こお-る,こご-える]`) were both non-standard formats — converted to proper lists, stemmed to こお/こご. **Vietnamese pile completed rather than narrowed**: stored 5 of Wiktionary's 6 genuine items — missing only `đúng` — added; the citing word [[凍結]] independently corroborates `đông` as genuine.

Rebuilt `## Notes` (non-standard bracket-style component links, floating unlinked CC-name lines) to the standard 4-bullet format. **`## Words`**: tagged the existing [[凍結]] citation as the reflexive stand-in (already correctly tagged). No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

### 2026-08-11 — Sorting-bug discovery: 警 (danayo_id 6470) processed out of sequence

**A real backlog-scanning bug discovered and fixed**: every "find next never-perfected character" scan this entire session used `sort -n` on `danayo_id` values extracted verbatim from frontmatter — but [[警]]'s `danayo_id` is stored as a quoted string `"6470"` rather than a bare integer. The leading quote character caused `sort -n` to treat it as `0`, so 警 spuriously sorted to the top of every listing regardless of its true numeric position, and was repeatedly (correctly, by manual judgment each time) skipped as an apparent anomaly in favor of the next visibly-sequential character. This masked the fact that 警's real position (6470) was simply the next character after 6469 — the moment the backlog advanced past 6469 with no other lower IDs remaining, the skip-6470-and-continue heuristic would have created a permanent gap. Fixed by stripping quote characters before sorting (`sed 's/danayo_id: *//; s/"//g'`) — recommend this stripped-sort approach be used for all future backlog scans in this loop, since other quoted `danayo_id` values may exist elsewhere in the corpus and could reproduce the same silent-skip failure mode.

### 2026-08-11, iteration 1293 — [[characters/警|警]]

**Blank `mc_id` filled in**: no rank was ever stored; found 警 at `CC 2000.md` line 466, filled with `2445`. **`graphemic_classification: 敬` confirmed correct** (semantic [[Radical 149|言]] + phonetic 敬; cognate with [[驚]], this sense being its endoactive). **Vietnamese contamination fixed**: stored a malformed comma-joined scalar `"cảnh, khểnh"`; `khểnh` doesn't appear anywhere in Wiktionary's own reading data, and the citing word [[警戒]] (`cảnh giác`) corroborates `cảnh` alone as genuine — removed the contamination and converted to a proper list.

**`japanese` malformed-YAML bug fixed**: bare scalar `KEI` converted to a proper list. **`japanese_native` truncation-to-stem fix**: full reading いましめる shortened to the stem いまし, matching vault convention. korean_native (`경계할`) confirmed correct. `pos: 性詞` was already correctly filled in.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format. **`## Words`**: tagged the existing [[警戒]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 膨 (char) (6667; 1210 characters remaining).

### 2026-08-11, iteration 1294 — [[characters/膨|膨]]

**`mc_id` confirmed genuinely absent, left blank per checklist policy**: 膨 doesn't appear in any of the four `CC 0000`–`CC 3000` lookup files — this is the "not yet checked / not independently sourceable" case, distinct from a trusted large existing value, so correctly left blank rather than guessed. **`graphemic_classification: 彭` confirmed correct** (semantic [[Radical 130|肉]] + phonetic 彭).

**Two malformed-YAML bugs fixed**: `japanese` (bare scalar `BOU`) and `japanese_native` (comma-joined raw-okurigana string `ふく-らむ,ふく-れる`) both converted to proper form, the latter stemmed to ふく (the shared stem of both ふくらむ and ふくれる). korean_native (`부를`, attributive of 부르다 "to be full/swollen," confirmed via `ko.wiktionary.org`'s own 훈 배부르다) and Vietnamese (`bành`) both confirmed correct as-is.

**A genuine gap discovered and flagged rather than silently worked around**: the character's own `stand_in: 膨大` field points to a word page that does not exist anywhere in this vault — confirmed via direct file search, and 膨 has no `aliases` that could explain the filename mismatch (ruling out the usual "check aliases before flagging missing" false-positive pattern). Word creation is out of scope for this character-perfecting loop, so this is flagged here for a future word-creation pass rather than fixed inline.

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, a Words-entry embedded directly in Notes) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅍ] (confirmed 膨 is listed there). **`## Words`**: existing [[膨脹]] citation confirmed accurate and moved to its own section. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 仇 (char) (7002; 1209 characters remaining).

### 2026-08-11, iteration 1295 — [[characters/仇|仇]]

**A clean cycle — `mc_id: 1244`, classification, korean_native, and Vietnamese all confirmed correct as-is**: checked `CC 1000.md` line 257; `graphemic_classification: 九` matches Wiktionary (semantic [[Radical 009|人]] + phonetic [[九 (char)|九]]); `korean_native: 원수` and `vietnamese: cừu` both confirmed. **Genuine alias added**: 㐜, independently verified via its own Wiktionary page ("this character is a variant form of 仇"); considered and rejected 讎/雠, which Wiktionary explicitly ties to a separate "resentment" sense rather than presenting as unqualified variants. **japanese_native expanded**: added the second genuine kun'yomi かたき alongside the already-stored あだ. Filled blank `pos` → `名詞`.

**`## Words` expanded from two entries to three**: tagged the existing [[仇恨]] as the reflexive stand-in, and added the newly-found [[仇敵]], alongside [[世仇]]. **New `## Chengyu` section**: [[世仇宿敵]] genuinely cites 仇. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

**Style-consistency issue discovered and flagged**: a corpus-wide grep found this session's own edits have been writing the traditional-form label `形聲` in the Notes graphemic bullet, while the vault's dominant, pre-existing convention (1489 instances vs. 121, and every one of those 121 traces to a `date-last-perfect: 2026-08-*` stamp from this session) uses the simplified `形声`. This is a self-introduced inconsistency across roughly 48+ pages perfected earlier in this session — not something to mass-correct mid-loop, but noted here so future iterations in this loop revert to `形声` (matching [[誇]]'s original, correctly-preserved `形声` bullet, left untouched this cycle since it predates the switch) and so a future dedicated cleanup pass can normalize the affected pages if desired.

Next never-perfected character by `danayo_id`: 勾 (char) (7003; 1208 characters remaining).

### 2026-08-11, iteration 1296 — [[characters/勾|勾]]

**`mc_id: 2219` verified correct as-is** (`CC 2000.md` line 232). **`graphemic_classification: 會意` confirmed correct**: Wiktionary describes 勾 as a graphic variant of 句, its 口 component transformed into 厶 — a genuine structural derivation, kept as the bare TYPE label since 句 has no vault page. **Spurious alias removed**: `冓` was listed as an alias, but independently verified via its own Wiktionary page to be an entirely unrelated character (original form of 遘, "to meet") with no documented connection to 勾 whatsoever — removed.

Vietnamese (`câu`/`cấu`/`cú`, reordered to match Wiktionary's presentation) and korean_native (`글귀`) both confirmed correct as content; japanese_native (`かぎ`) confirmed as one of four genuine kun'yomi. Filled blank `pos` → `事詞`, matching the stand-in word [[勾引]]'s own `pos`. **Fixed a pre-existing typo**: `english: entince` → `entice`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard format — the graphemic bullet uses the bare `會意` TYPE label without an OC-reconstruction parenthetical, since 勾's own etymology is a graphic-variant derivation (not a phono-semantic compound), so no OC gloss belongs in this bullet. **`## Words`**: tagged the existing [[勾引]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 丐 (char) (7004; 1207 characters remaining).

### 2026-08-11, iteration 1297 — [[characters/丐|丐]]

**`mc_id: 3375` verified correct as-is** (`CC 3000.md` line 392). **A real wrong-type-label bug found and fixed**: `graphemic_classification` stored `象形`, but Wiktionary's own etymology never assigns a formal type label to 丐 itself, describing it only as "a corruption of 匄, original meaning unknown" — however 匄 (丐's own documented original form) is independently classified 會意 (⿹勹亡, "tip of a blade inside a knife"). Since 丐 is explicitly a later graphic corruption of that same character rather than an independent new pictograph, corrected to `會意` and traced the lineage explicitly in the Notes bullet.

**Spurious alias removed**: `丏` was listed as an alias, but independently verified via its own Wiktionary page to be a wholly unrelated character ("to conceal," "parapet," a surname) connected to 丐 only by a "See also" navigation link (visual/adjacency resemblance, not genuine variant status) — removed. **Vietnamese pile completed rather than narrowed**: stored 2 of Wiktionary's 4 genuine Hán Nôm/Nôm items (`cái, gái`) — added the 2 missing (`cưới, gáy`); the citing word [[乞丐]] (`khất cái`) independently corroborates `cái` as genuine. korean_native (`빌`) confirmed correct; japanese_native (`こ`, stem of こう) confirmed correct via direct `ja.wiktionary.org` check. **Fixed a pre-existing typo**: `english: begger` → `beggar`.

Rebuilt `## Notes` (two bare unlinked CC-name lines, no other content) to the standard format, preserving the existing `>[!TIP] Requires 乞丐` callout (a required-compound note distinct from the standard word-disambiguation callout) and routing `hanmun_edu_level: 無` to [Korean Missing] per the checklist's mapping table. **`## Words`**: added the missing reflexive stand-in tag to the existing [[乞丐]] citation, which had been sitting only in the callout with no Words-section entry at all. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 忽 (char) (7005; 1206 characters remaining).

### 2026-08-11, iteration 1298 — [[characters/忽|忽]]

**`mc_id: 1214` verified correct as-is** (`CC 1000.md` line 227). **`graphemic_classification: 勿` field confirmed correct** (phonetic, matching Wiktionary), but **the Notes prose had semantic/phonetic reversed** (the b2 pattern seen earlier this session on 屈/那/醜/肖/雌) — it read "semantic [[勿]] ('heart') + phonetic [[心]]," backwards and with the wrong gloss attached to the wrong character; corrected to "semantic [[心]] + phonetic [[勿]]."

**Genuine multi-etymology alias added**: 芴, independently verified — Wiktionary documents it as "an ancient form of 忽" in one etymology while also having unrelated standalone senses (fluorene, a plant name) in others, matching the established nuanced-alias precedent (like [[誇]]'s 侉). Considered and rejected 窟 (also listed nearby): confirmed via its own page to have zero documented connection to 忽. **japanese_native expanded**: added ゆるがせ (matching the "neglect" sense, attested by [[疎忽]]) alongside the already-stored たちま (matching the "sudden" sense). Vietnamese items `hốt`/`hớt` left as-is — `hốt` confirmed via Wiktionary, `hớt` neither confirmed nor contradicted by any citing word, so left rather than guessed at. korean_native (`갑자기`) confirmed correct. Filled blank `pos` → `性詞`.

Rebuilt `## Notes` (a duplicate bare `[[勿]] + heart` line directly below the malformed graphemic bullet, floating unlinked CC-name lines, three Words-like entries embedded in Notes) to the standard 4-bullet format. **`## Words`**: tagged the existing [[忽然]] as the reflexive stand-in, fixed [[忽然様]] to proper ruby formatting, alongside the existing [[疎忽]]. **New `## Chengyu` check**: none found. **New `## Derived Characters` section**: [[惚]] genuinely cites 忽 as its own phonetic donor.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 冗 (char) (7006; 1205 characters remaining).

### 2026-08-11, iteration 1299 — [[characters/冗 (char)|冗]]

**mc_id off-by-one fixed**: stored `3706` actually belongs to 郛 (`CC 3000.md` line 739); 冗 itself sits at rank 3707 (line 740) — corrected. **`graphemic_classification: 儿` confirmed correct** (Wiktionary: 會意 of 宀/冖 "roof" + 儿 "person" — a person idling indoors). **Two genuine variant aliases added**: 宂 and 冘, both independently verified via their own Wiktionary pages ("variant form of 冗" and "obsolete form of 冗" respectively).

**A textbook 壇/鹿-lesson case, checked before editing**: the sole citing word [[冗]] (word)'s own deep prior research explicitly diagnoses the stored 4-item Vietnamese pile (`nhõng, nhùng, nhũng, nũng`) as containing three "tonal near-misses" and "corpus noise," settling on `nhũng` alone as genuine — narrowed the character page to match exactly. That same research also explicitly confirms `korean_native: 한가로울` is correct (matches native gloss 한가롭다) — left unchanged. **`japanese_native` ø-placeholder bug fixed**: Wiktionary's sole kun'yomi むだ ("wasteful, futile") — added. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`. **Blank `hanmun_edu_level` filled**: confirmed 冗 appears in no Korean lookup list at all — filled with `無` (genuinely absent), routing to [Korean Missing].

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 會意 format, linking the Kangxi radical [[Radical 014|冖]] per the checklist's radical-linking rule. **`## Words`**: added the missing reflexive stand-in [[冗]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 夭 (char) (7007; 1204 characters remaining).

### 2026-08-11, iteration 1300 — [[characters/夭|夭]]

**mc_id off-by-one fixed**: stored `1455` actually belongs to 膚 (`CC 1000.md` line 476); 夭 itself sits at rank 1456 (line 477) — corrected. **A real wrong-type-label bug found and fixed**: `graphemic_classification` stored `象形`, but Wiktionary explicitly classifies 夭 as `指事` (a figure bending/leaning forward as if running) — corrected.

**A real cross-sense content bug found and fixed, more significant than usual**: the character's own `english: [gentle, tender]` field documented the character's *other* homographic sense, while its own `stand_in` ([[夭折]], "to die young") and `korean_native` (일찍 죽다, "to die young") both target the entirely different "premature death" sense — a genuine internal inconsistency, not merely a translation nuance. Corrected `english` to `[to die young, premature death]` to match the sense this page's own stand-in and Korean gloss actually document, and updated `japanese_native` from わか (stem of わかい, "young" — the wrong sense) to わかじに (the genuine kun'yomi meaning specifically "dying young").

**Vietnamese YAML fixed**: was a single comma-joined string; converted to a proper 6-item list matching Wiktionary's set exactly (no contamination found, all six genuine, sense not distinguished by Wiktionary itself so left un-narrowed). **Also fixed the citing word `words/夭折.md`**: its own prose explicitly stated the character's "graphemic root 象形 sense is 'gentle, tender'" and glossed [[夭]] as "gentle, tender; young" — both now-stale claims inherited from the character page's pre-fix values — updated to match the corrected 指事 classification and "die young" sense.

Rebuilt `## Notes` (empty Notes section, a misplaced Words entry, a plain-text "derived characters" list at the bottom, floating unlinked CC-name lines) to the standard 指事 format, routing `hanmun_edu_level: 名` to [Korean Name ㅇ] (confirmed 夭 is listed there). **`## Words`**: tagged the existing [[夭折]] as the reflexive stand-in. **New `## Derived Characters` section, filtering false positives**: of the six characters plain-text-listed as derived (沃, 妖, 殀, 忝, 笑, 喬), verified only [[沃]] and [[妖]] genuinely cite 夭 as their `graphemic_classification`; 忝 and 喬 actually cite different phonetics (天, 高) despite the note's claim, and 殀/笑/喬(乔)/飫(饫) have no vault pages at all — excluded all false positives and pageless candidates.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 禾 (char) (7009; 1203 characters remaining).

### 2026-08-11, iteration 1301 — [[characters/禾 (char)|禾]]

**`mc_id: 1318` verified correct as-is** (`CC 1000.md` line 335). **`graphemic_classification: 象形` confirmed correct** (Wiktionary: pictogram of a plant stalk, similar in shape to but unrelated to [[來]]). This character had been explicitly flagged as genuinely unperfected by the citing word [[禾]] (word)'s own prior research — the fourth in a documented series after [[玄]]/[[皿]]/[[矢]] — confirming this was a real overdue gap, not a false alarm.

Vietnamese (`hoà`), korean_native (`벼`), and japanese_native (`いね`) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`. **A genuine content bug found and fixed on a second citing word, `words/禾稲.md`**: its `korean` field held `사루`, an unrecognizable value with no compositional or attested basis — corrected to `화도`, the plain compositional reading of its two constituent characters (화+도). **Also fixed a formatting corruption on the same page**: a stray plain-text fragment ("unhusked rice") was sitting outside any heading, before a misnamed `## Etymology` header — consolidated into a proper `## Notes` section.

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, one bare Words-like entry sitting in Notes) to the standard 象形 format. **`## Words`**: added the missing reflexive stand-in [[禾]] alongside the existing [[禾稲]]. **New `## Derived Characters` section**: [[委 (char)|委]], [[和]], and [[科]] all independently confirmed to genuinely cite 禾 as their own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 呻 (char) (7010; 1202 characters remaining).

### 2026-08-11, iteration 1302 — [[characters/呻|呻]]

**`mc_id: 4273` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 申` confirmed correct** (semantic [[口]] + phonetic 申). **A real wrong-gloss bug found and fixed**: `korean_native` stored `읊조릴` ("to recite; to chant/intone"), a completely different semantic field from this character's documented "groan" sense — the raw eumhun via `ko.wiktionary.org` is 끙끙거리다 ("to groan") — corrected to the attributive `끙끙거릴`.

**Four genuine unqualified alternative-form aliases added**: 𣢘, 㕥, 𠲳, 𤶴, all listed by Wiktionary without any sense-restriction qualifier (unlike prior cases like [[忽]]'s excluded 窟), trusted per the established precedent from [[誘]]'s six-item alternative-forms addition. Vietnamese (`thân`) and japanese_native (`うめ`, stem of うめく) both confirmed correct as-is. `pos: 事詞` was already correctly filled in.

Rebuilt `## Notes` (a bare "Components:" bullet mimicking 會意 format for what is actually a 形聲 character, floating unlinked CC-name lines) to the standard 4-bullet format. **Self-caught a level-routing error mid-edit**: initially wrote the Jōyō link as [Jōyō - Kōtō], then rechecked the stored field and found `joyo_level: 表外字` — corrected the link to [Hyōgai] to match. **`## Words`**: added the missing reflexive stand-in [[呻吟]]. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 孕 (char) (7011; 1201 characters remaining).

### 2026-08-11, iteration 1303 — [[characters/孕|孕]]

**mc_id off-by-one fixed**: stored `2934` actually belongs to 熾 (`CC 2000.md` line 975); 孕 itself sits at rank 2935 (line 976) — corrected. **A real wrong-type-label bug found and fixed, self-contradicting within the page's own pre-existing Notes**: `graphemic_classification` stored `乃`, mimicking a 形聲 phonetic-component reference, but the page's own existing Notes bullet already explicitly called this a "Pictogram (象形)" — the frontmatter field directly contradicted the page's own prose. Confirmed via Wiktionary that 乃 functions purely pictorially here (depicting the pregnant torso), not as a phonetic donor at all — corrected the field to the bare TYPE label `象形`.

**Genuine variant alias added**: 㚺, independently verified ("this character is a variant form of 孕"). **Malformed YAML fixed**: `japanese_native` was a scalar (`はら`) followed by an orphaned list item (`はらむ`, the full form of the same stem) — corrected to the single clean stem value. Vietnamese (`dựng`, already correctly narrowed from Wiktionary's 8-item Nôm pile) and korean_native (`임신할`) both confirmed correct as-is. **`stand_in: 懷孕` investigated and confirmed not a bug**: the actual word-page filename is the shinjitai `懐孕.md`, but it explicitly lists `懷孕` among its own `aliases` — a legitimate traditional/shinjitai naming variance, not a missing-word gap.

Rebuilt `## Notes` (misplaced `## Words` section ahead of Notes, a duplicated 象形 declaration across two separate bullets, floating unlinked CC-name lines) to the standard 象形 format, linking both depicted components ([[乃 (char)|乃]], [[Radical 039|子]]). **`## Words`**: tagged the existing [[懐孕]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 叱 (char) (7012; 1200 characters remaining).

### 2026-08-11, iteration 1304 — [[characters/叱|叱]]

**`mc_id: 2460` verified correct as-is** (`CC 2000.md` line 481). **`graphemic_classification: 七` confirmed correct** (semantic [[口]] + phonetic [[七 (char)|七]]). **Genuine alias added**: 咜, independently verified ("this character is a variant form of 叱"), alongside the already-stored shinjitai-successor 𠮟 (which Wiktionary confirms officially replaced 叱 in the 2010 Jōyō reform, though 叱 remains in common use).

Vietnamese (`sất, sứt, sớt`, reordered to lead with the Hán Việt reading, corroborated by the citing word [[叱責]]'s own `sất trách`) and korean_native (`꾸짖을`) both confirmed correct as content; japanese_native (`しか`, stem of しかる) confirmed as one of four genuine kun'yomi. Filled blank `pos` → `事詞`, matching the established precedent from [[罵]] (a similar "scold" character) rather than the citing word's own broader `実詞` category. `hsk_level` is genuinely blank (character isn't in the vault's HSK list) — omitted the HSK link rather than guessing one.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines, no other content) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅈ] (confirmed 叱 is listed there). **`## Words`**: tagged the existing [[叱責]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 詛 (char) (7014; 1199 characters remaining).

### 2026-08-11, iteration 1305 — [[characters/詛|詛]]

**mc_id off-by-one fixed**: stored `2251` actually belongs to 閻 (`CC 2000.md` line 264); 詛 itself sits at rank 2252 (line 265) — corrected. **A real content bug found and fixed**: `stand_in` stored `呪術` ("magic technique"), a word page that doesn't exist anywhere in the vault — confirmed via direct file search that the actual, genuinely-citing word page is `呪詛.md` (呪+詛, a one-character typo away) — corrected the field to `呪詛`. **`graphemic_classification: 且` confirmed correct** (semantic [[Radical 149|言]] + phonetic 且). **Genuine variant alias added**: 謯, independently verified.

Vietnamese (`chú, thư, trù, trớ`) and korean_native (`저주할`, confirmed via `ko.wiktionary.org`) both confirmed correct as content; japanese_native (`のろ`, stem of のろう) confirmed as the sole genuine kun'yomi. Filled blank `pos` → `名詞`, matching [[呪詛]]'s own stored `pos`. **Two blank level fields filled based on absence evidence**: `joyo_level` (was blank) → `表外字`, confirmed via absence from every Japanese lookup list; `hsk_level` left genuinely blank (also absent from HSK lists, so no link guessed).

**Also fixed a malformed-YAML corruption on the citing word `words/呪詛.md`**: `vietnamese: ""` (a literal empty-string scalar) — corrected to a proper blank field.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅈ] (confirmed 詛 is listed there). **`## Words`**: tagged the corrected [[呪詛]] citation as the reflexive stand-in. **New `## Chengyu` section**: [[詛地哀食]] genuinely cites 詛. No derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 臼 (char) (7016; 1198 characters remaining).

### 2026-08-11, iteration 1306 — [[characters/臼 (char)|臼]]

**`mc_id: 2374` verified correct as-is** (`CC 2000.md` line 391). **`graphemic_classification: 象形` confirmed correct** (Wiktionary: pictogram of a mortar, compare the original form of 舂). This character had been explicitly flagged as genuinely unperfected by the citing word [[臼]] (word)'s own prior research — the fifth in a documented series after [[玄]]/[[皿]]/[[矢]]/[[禾]].

**Considered and deliberately rejected adding 旧 as an alias, despite Wiktionary listing it unqualified**: independently verified that 旧 is indeed a documented graphical variant of 臼 (later repurposed as the shinjitai of unrelated 舊 "old" via a homophonic/phonetic-component connection) — a genuine but risky case, since 旧's overwhelming modern usage means "old," not "mortar." Unlike [[誘]]/[[呻]]'s obscure, uncontested alternative-form additions, adding 旧 here would misrepresent a live, dominant-meaning character as interchangeable with this one — treated with the same caution as [[汝]]'s excluded 女, and left out.

Vietnamese (`cối` genuine/living, `cữu` confirmed by the citing word as a genuine but unrelated-classical-sense reading — kept, not removed) and korean_native (`절구`) both confirmed correct; japanese_native (`うす`) confirmed as the dominant genuine kun'yomi. `pos: 名詞` was already correctly filled in.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 象形 format, routing `hanmun_edu_level: 名` to [Korean Name ㄱ] (confirmed 臼 is listed there). **`## Words`**: added the missing reflexive stand-in [[臼]]. **New `## Derived Characters` section**: [[旧 (char)|旧]] and [[舅]] both independently confirmed to genuinely cite 臼 as their own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 亦 (char) (7017; 1197 characters remaining).

### 2026-08-11, iteration 1307 — [[characters/亦 (char)|亦]]

**`mc_id: 120` verified correct as-is** (`CC 0000.md` line 128, blockquote format). **`graphemic_classification: 指事` confirmed correct** (Wiktionary: a human figure with emphasis marks on the armpits, original form of 腋 "armpit," later phonetically borrowed for "too; also"). Vietnamese (`diệc`), korean_native (`또`), and japanese_native (`また`) all confirmed correct as-is. **Genuine alias added**: 𠅃, independently verified ("an ancient form of 亦"); a second candidate 𡗕 couldn't be verified (404) and was left unadded. Filled blank `pos` → `副詞`, matching the citing word [[亦]] (word)'s own stored `pos`.

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, a Words entry sitting ahead of Notes) to the standard 指事 format. **`## Words` expanded from one entry to two**: tagged the existing [[亦]] as the reflexive stand-in and added the newly-found grammar-construction word [[不亦V乎]]. **New `## Derived Characters` section**: [[夜 (char)|夜]] and [[跡]] both independently confirmed to genuinely cite 亦 as their own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 伎 (char) (7018; 1196 characters remaining).

### 2026-08-11, iteration 1308 — [[characters/伎|伎]]

**`mc_id: 2547` verified correct as-is** (`CC 2000.md` line 572). **`graphemic_classification: 支` confirmed correct** (semantic [[Radical 009|人]] + phonetic 支). Vietnamese (`kĩ`/`kỹ`, tone-mark spelling variants of the same Hán Việt reading, old vs. new orthography — same pattern as [[禾]]'s hòa/hoà), korean_native (`재간`), and japanese_native (`わざ`) all confirmed correct as-is. `pos: 名詞` was already correctly filled in.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㄱ] (confirmed 伎 is listed there). **`## Words`**: the existing [[伎倆]] citation was missing its gloss entirely (a checklist rule-9 violation) — added "skill, ability; underhanded trick, ploy" from the citing word's own stored `english` field, and tagged it as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 扱 (char) (7019; 1195 characters remaining).

### 2026-08-11, iteration 1309 — [[characters/扱 (char)|扱]]

**`mc_id: 4434` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 及` confirmed correct** (semantic [[Radical 064|手]] + phonetic 及). **A clean cycle otherwise**: the 15-item Vietnamese pile, korean_native (`미칠`), and japanese_native (`あつか`, stem of あつかう) all confirmed to match Wiktionary's own data exactly — a genuinely large, entirely-attested Nôm set rather than contamination, left untouched. Noted the real Chinese/Japanese sense divergence (broader "gather, receive, seize" vs. this page's narrower Japanese-dominant "handle; deal with") directly in the Notes bullet. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㄱ] (confirmed 扱 is listed there); `hsk_level` is genuinely blank, so the HSK link was omitted. **`## Words`**: added the missing reflexive stand-in [[扱]] to a Words section that didn't exist at all. **Citing word `words/扱.md` was corrupted** (`vietnamese: null`, scalar `characters`, missing `pos`/`kwin`/`date-last-perfect`, wrong Notes heading, no content) — fully rebuilt. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 肛 (char) (7020; 1194 characters remaining).

### 2026-08-11, iteration 1310 — [[characters/肛|肛]]

**`mc_id: 8173` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 工` confirmed correct** (semantic [[Radical 130|肉]] + phonetic 工). **Vietnamese pile expanded using the citing word's own deep prior research**: stored only `[dom, giang]`; the citing word [[肛門]]'s own Notes explicitly document five competing genuine Hán Việt readings (cương, giang, khang, soang, xoang) all glossing to "anus," plus the separately-attested native doublet `dom` — expanded to the full six-item set rather than narrowing, since this was under-coverage, not contamination (same pattern as [[徐]]'s completion).

**`japanese_native` ø-placeholder bug fixed**: Wiktionary's sole kun'yomi はれる ("to swell") — added as the stem はれ. **Two genuine variant aliases added**: 疘 and 㠮, both independently verified. korean_native (`항문`) confirmed correct. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅎ] (confirmed 肛 is listed there) and `hsk_level: 無` to [HSK No] per the mapping table. **Self-caught an omission on the final verification Read**: the levels bullet had been built without the [HSK No] link despite `hsk_level: 無` being a real, mapped value (not blank) — added it. **`## Words`**: tagged the existing [[肛門]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 砧 (char) (7021; 1193 characters remaining).

### 2026-08-11, iteration 1311 — [[characters/砧|砧]]

**`mc_id: 0` confirmed correct as-is per checklist policy**: this is the "confirmed not present in the MC usage ranking at all" state, not a placeholder — left as `0` and phrased the MC bullet accordingly rather than treating it as an error. **`graphemic_classification: 占` confirmed correct** (semantic [[Radical 112|石]] + phonetic [[占 (char)|占]]). **Vietnamese contamination fixed**: stored `[chiêm, châm, chỉm]`, but Wiktionary lists only `châm` — the two extras don't appear in any source or citing word, narrowed to `[châm]` alone. **Two genuine dual-etymology aliases added**: 碪 and 椹, both independently verified as variant forms of 砧 specifically (each also carrying an unrelated second-etymology sense, matching the established nuanced-alias precedent).

korean_native (`다듬잇돌`) and japanese_native (`きぬた`) both confirmed correct as-is. `pos: 名詞` was already correctly filled in, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅊ] (confirmed 砧 is listed there), `joyo_level: 日本人名用漢字` to [Jinmeiyō], and `hsk_level: 無` to [HSK No]. **`## Words`**: tagged the existing [[鉄砧]] citation as the reflexive stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 旱 (char) (7022; 1192 characters remaining).

### 2026-08-11, iteration 1312 — [[characters/旱|旱]]

**A clean cycle — `mc_id: 1077`, classification, Vietnamese, korean_native, and japanese_native all confirmed correct as-is**: checked `CC 1000.md` line 82; `graphemic_classification: 干` matches Wiktionary (semantic [[Radical 072|日]] + phonetic [[干]]); `vietnamese: [hạn, khan]`, `korean_native: 가물`, and `japanese_native: ひでり` all confirmed exactly. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, floating unlinked CC-name lines, a Words-like entry sitting in Notes) to the standard 4-bullet format, noting the cognate relationship to pageless 乾 ("dry"). **`## Words`**: tagged the existing [[旱災]] citation as the reflexive stand-in, self-corrected a guessed 注音 by checking the actual page rather than assuming. **New `## Derived Characters` section**: [[悍]] genuinely cites 旱 as its own phonetic donor. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 倚 (char) (7023; 1191 characters remaining).

### 2026-08-11, iteration 1313 — [[characters/倚 (char)|倚]]

**mc_id error fixed (a rarer two-off case)**: stored `1526` actually belongs to 殃; 倚 itself sits at rank 1528 (`CC 1000.md` line 553) — corrected. **`graphemic_classification: 奇` confirmed correct** (semantic [[Radical 009|人]] + phonetic 奇). **Vietnamese contamination fixed using the citing word's own deep prior research**: stored `[ấy, ỉa, ỷ]`; the citing word [[倚]] (word)'s own Notes explicitly diagnose both `ấy` ("that," a native demonstrative) and `ỉa` (a vulgar native word for "to defecate") as unrelated and deliberately excluded, settling on `ỷ` alone as the genuine Hán Việt reading (attested in ỷ lại) — narrowed the character page to match exactly.

**Two genuine multi-etymology aliases added**: 猗 and 𠋣, both independently verified as documented variant forms of 倚 specifically. korean_native (`의지할`) and japanese_native (`よ`, stem of よる) both confirmed correct as-is. Filled blank `pos` → `動詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅇ] (confirmed 倚 is listed there). **`## Words`**: added the missing reflexive stand-in [[倚]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 吻 (char) (7024; 1190 characters remaining).

### 2026-08-11, iteration 1314 — [[characters/吻|吻]]

**`mc_id: 4767` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 勿` confirmed correct** (semantic [[Radical 030|口]] + phonetic 勿). **A real wrong-reading bug found and fixed**: `japanese_native` stored `くちわき`, but Wiktionary's sole listed kun'yomi is `くちさき` — a one-character transcription error (わ vs さ) — corrected.

Vietnamese (`vẩn, vẫn, vặt`, already a deliberate narrowing from Wiktionary's much larger 11-item raw pile, left as-is since the remaining 8 unusual tonal variants had no corroborating evidence either way) and korean_native (`입술`) both confirmed correct as content. **Genuine variant alias added**: 脗, independently verified. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (an empty semantic gloss, a redundant bare "from [[勿]]" line duplicating the graphemic bullet, floating unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅁ] (confirmed 吻 is listed there). **Self-corrected a guessed-wrong 注音 mid-edit**: initially guessed `ㄐㄝㄆㄇㄨㄋ` for [[接吻]] instead of checking its actual page — caught immediately, verified the real value (`ㄐㄛㄆㄇㄨㄋ`), fixed. **`## Words`**: added the missing reflexive stand-in [[接吻]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 吼 (char) (7025; 1189 characters remaining).

### 2026-08-11, iteration 1315 — [[characters/吼 (char)|吼]]

**`mc_id: 7936` confirmed as a trusted long-tail value per checklist policy** (not present in any `CC 0000`–`CC 3000` lookup file). **`graphemic_classification: 孔` confirmed correct** (semantic [[口]] + phonetic 孔). **Vietnamese contamination fixed using the citing word's own deeper research, which went beyond even raw Wiktionary's own list**: stored `[hống, hổng, khỏng, khống, rống]`; the citing word [[吼]] (word)'s own Notes explicitly diagnose `hổng, khỏng, khống` as "corpus noise" and confirm both `hống` (the Hán Việt reading) and `rống` (a rare case where the native and classical readings converge) as genuine — narrowed the character page to exactly `[hống, rống]`, trusting this dictionary-sourced verification over Wiktionary's own broader four-item Nôm list.

**Genuine multi-etymology alias added**: 吽, independently verified ("variant form of 吼," alongside an unrelated Buddhist-mantra-syllable sense). korean_native (`울부짖을`) and japanese_native (`ほ`, stem of ほえる) both confirmed correct as-is. `pos: 事詞` was already correctly filled in.

Rebuilt `## Notes` (a "Components:"-style bullet mimicking 會意 format for what is actually a 形聲 character, floating unlinked CC-name lines) to the standard 4-bullet format, routing `hanmun_edu_level: 名` to [Korean Name ㅎ] (confirmed 吼 is listed there). **`## Words`**: added the missing reflexive stand-in [[吼]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 亨 (char) (7026; 1188 characters remaining).

### 2026-08-11, iteration 1316 — [[characters/亨|亨]]

**`mc_id: 1739` verified correct as-is** (`CC 1000.md` line 772). **`graphemic_classification: 象形` confirmed correct** (Wiktionary: pictogram of an ancestral shrine). **Deliberately rejected treating 享/烹 as aliases** despite Wiktionary stating 亨 "functions as an alternative form of both": both are distinct, dominant modern characters with their own well-established meanings ("to enjoy," "to boil/cook") — the same shared-ancient-origin trap as [[亘]]'s excluded 旧, documented explicitly in the Notes bullet with a link to [[享]]'s own vault page (found to actually have one, correcting an initial "pageless" assumption before finalizing).

Vietnamese left narrowed to `[hanh]` alone — the citing word [[亨通]]'s own research corroborates `hanh` specifically for this "go smoothly" sense, while Wiktionary's other listed readings (hưởng, phanh) belong to the 享/烹-adjacent senses, not this page's own. korean_native (`형통할`) and japanese_native (`とお`, stem of とおる) both confirmed correct. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare unlinked CC-name lines) to the standard 象形 format. **`## Words`**: added the missing reflexive stand-in [[亨通]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 忌 (char) (7027; 1187 characters remaining).

### 2026-08-11, iteration 1317 — [[characters/忌|忌]]

**`mc_id: 1008` verified correct as-is** (`CC 1000.md`). **`graphemic_classification: 己` confirmed correct** (semantic [[Radical 061|心]] + phonetic [[己]]). **Vietnamese expanded, not narrowed**: stored set was missing the plain Hán Việt reading `kí` itself alongside the already-present Nôm-adjacent variants (`kị, kỵ, cạy, cậy, cữ, kiêng`) — added.

**Two genuine variant aliases added** after independent Wiktionary verification: 坖, 㤅 (both unqualified "variant form of 忌" with no competing modern sense — the liberal-precedent pattern, not the shared-ancient-origin trap). A third candidate, 𢗂, was correctly left unadded after its Wiktionary page returned a 404.

Rebuilt the graphemic `## Notes` bullet, which was missing both the character's own OC reconstruction (`*ɡɯs`) and the phonetic component's OC gloss (`*kɯʔ`) — added both to match the standard format. **New bug type discovered and fixed: broken relative paths on a suffix-less filename.** 忌.md (no "(char)" suffix, living directly in `characters/`) had `../lookup/...` and `../syllables/...` links in its MC-ordinal bullet — the `../` prefix is only correct for files nested one level deeper; suffix-less files live at the same depth as suffixed ones and need bare `lookup/...`/`syllables/...`, confirmed by cross-referencing the already-correct pattern on [[砧]]. Also filled in the missing ordinal-rank sentence itself ("1008th most used character in Classical Chinese..."), which had been omitted entirely.

**`## Words`** rebuilt from a single bare entry to three: tagged the existing [[忌諱]] as the reflexive stand-in (注音 verified from its own page, not guessed), kept the existing [[忌惮]], and added a newly-found [[禁忌]] (注音 also verified from its own page). No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 巫 (7028; 1187 characters remaining).

### 2026-08-11, iteration 1318 — [[characters/巫|巫]]

**`mc_id: 1178` verified correct as-is** (`CC 1000.md` line 187). **`graphemic_classification: 象形` confirmed correct**, but the existing Notes bullet asserted a single unqualified origin ("two pieces of jade crossed over each other... for sacrifices") when en.Wiktionary's actual Etymology section states the glyph origin is explicitly **"Uncertain,"** listing five unrelated hypotheses (cognate with 舞 "dance," cognate with 母 "female," Tibetan loan, cognate with 誣, Old Persian *maguš* loan) and no jade/sacrifice claim at all. Cross-checked zh.Wiktionary, which does attest a two-stacked-jade theory (among competing 工-based and 人-based theories) — rewrote the bullet to present it honestly as one of several unsettled proposals, matching the vault's own established "origin uncertain" house style (cf. [[丙 (char)|丙]]).

Filled blank `pos` → `名詞` (巫 is a concrete common noun, "shaman," not an eventive/stative). korean_native (`무당`), japanese_native (`かんなぎ`, one of two attested kun'yomi), and vietnamese (`vu`) all confirmed correct as-is. **Alias research**: checked all three variant forms Wiktionary lists (𢀣, 𢍮, 𠮎) — two 404, and the third (𢍮) is explicitly labeled an *ancient/ancestral* form rather than a synchronic interchangeable variant, so none were added, consistent with the discipline of not treating historical predecessor glyphs as usable aliases.

**`## Notes` was missing three of its four standard bullets entirely** (SKIP, MC-ordinal, levels) — added all three, routing `hanmun_edu_level: 名` + `諺文: 무` to [Korean Name ㅁ] and `joyo_level: 表外字` to [Hyōgai]. **New `### Derived Characters` section added**: [[誣]] (confirmed via exact `graphemic_classification: 巫` match).

**`## Words` rebuilt from three malformed/non-wikilink entries to four proper ruby entries**: reflexive stand-in tagged on [[巫女]] (注音 verified from its own page), [[巫術]] and [[神巫]] converted from broken `[text](/words/...)` link syntax to proper `<ruby>[[wikilink]]` format (both 注音 verified against their own pages), and [[巫山]] (a place name, "Wushan") converted from a bare gloss-only bullet to the standard ruby format. **New bug type found and fixed on two citing word pages**: [[巫女]] and [[巫山]] both used broken `../characters/...` relative paths in their own Notes/Etymology sections (words/ and characters/ are sibling directories — the correct link has no `../` prefix, confirmed against already-correct sibling word pages) — fixed both.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 坊 (7029; 1186 characters remaining).

### 2026-08-11, iteration 1319 — [[characters/坊|坊]]

**Real `mc_id` bug found and fixed**: stored `mc_id: 3749` actually points to a different character entirely (`CC 3000.md` line 782 = 錡); 坊's true ranking is **3750** (line 783) — a genuine off-by-one, not a trusted long-tail value, corrected. **`graphemic_classification: 方` confirmed correct** (形聲: semantic 土 + phonetic 方, exact OC match `*paŋ`), cross-verified against the phonetic component's own already-perfected page ([[方 (char)|方]], same `middle_chinese_initial: f` / `middle_chinese_final: ʉɐŋ`).

**`english` expanded, not narrowed**: stored set was just `[workshop]`, but Wiktionary documents 坊 as genuinely polysemous even within a single overlapping pronunciation (lane/alley, store, workshop, paifang-arch, surname) — added `lane; alley` and `quarter; neighborhood` (the latter corroborated by the existing, already-correct `korean_native: 동네` "neighborhood"). **`japanese` expanded**: ja.Wiktionary lists three on'yomi (呉音 ボウ, 漢音 ホウ, and a bound 慣用音 ボッ that only surfaces before certain morphemes, e.g. 坊っちゃん) — added the missing 漢音 `HOU`; left the geminate 慣用音 unadded, consistent with how no other vault page encodes bound contracted on'yomi as a standalone reading. `japanese_native: ø` (no kun'yomi) and `vietnamese: [phương, phường]` both confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines with no other bullets at all — SKIP/MC-ordinal/levels bullets were entirely missing) to the standard 4-bullet format, routing `joyo_level: 高等` to [Jōyō - Kōtō] and `hanmun_edu_level: 名` + `諺文: 빵` to [Korean Name ㅂ]. **`## Words`**: added the missing reflexive stand-in [[作坊]] (注音 verified from its own page) to a Words section that didn't exist at all. No Chengyu hits; no derived characters (checked via exact `graphemic_classification: 坊` match, none found).

**Same `../characters/` broken-relative-path bug as last cycle found on the citing word page** ([[作坊]]) and fixed — now confirmed a recurring pattern worth watching for on any word page not yet touched this session.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 呆 (char) (7031; 1185 characters remaining).

### 2026-08-11, iteration 1320 — [[characters/呆 (char)|呆]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy (not present in `CC 0000`–`CC 3000`). **`graphemic_classification: 會意` confirmed correct** (Wiktionary: ideogram, 口 "mouth" + 木 "tree" — dull, wooden → stupid).

**Major Vietnamese narrowing, driven by the citing word's own scholarly research**: stored set was `[dại, ngai, ngãi, ngóc, ngố, ngốc]` (matching vi.Wiktionary's raw, undifferentiated 8-reading dump). But the citing word page [[呆]]'s own Notes contain extensive prior research explicitly distinguishing **`ngai`** as the sole genuine Hán Việt reading (attested in real compounds paralleling Mandarin/Chinese usage: si ngai 癡呆, ngai trệ 呆滯, ngai bản 呆板) from the other five, which that research identifies as Nôm loan-character readings unrelated by regular phonetic derivation (citing Trần Văn Chánh specifically on `ngốc`, the most commonly mislabeled one) — narrowed the character page to `[ngai]` alone, trusting the word's deeper documented research over the raw Wiktionary list, the same pattern as prior narrowing cases.

**Two genuine variant aliases**: kept existing 獃; added 騃 after independent verification (Wiktionary: explicit alt-form-of-呆 sense, described as its predominant modern meaning despite an unrelated obsolete "quick" sense under a separate etymology). A third candidate, 𤶗, was correctly left unadded after a 404.

`korean_native` (`어리석을`) and `japanese_native` (`ほけ`, stem of ほける) both confirmed correct — matching the citing word's own careful documentation. `japanese` (`BOU, GAI, HOU`) also confirmed correct as the citing word's vetted subset, deliberately not expanded with Wiktionary's fuller raw on'yomi/kun'yomi noise (あきれる, ぼける, etc.), consistent with trusting curated citing-word research over raw dictionary lists. Filled blank `pos` → `性詞` (matching the citing word's own stored `pos`). **`english` expanded**: `[confused]` alone → added `foolish` and `wooden; rigid`, both directly drawn from the citing word's own documented senses (呆板 "rigid, wooden").

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets at all) to the standard 4-bullet format, using the citing word's own rich etymological prose for the graphemic bullet. Routed `hanmun_edu_level: 無` to **[Korean Missing]** — the first character this session to use that particular mapped value (distinct from the more commonly-seen `hsk_level: 無` → [HSK No]). **`## Words`**: added the missing reflexive stand-in [[呆]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

**Same `../characters/` broken-relative-path bug found and fixed on the citing word page** ([[呆]]) — now the third consecutive cycle with this exact pattern.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 杆 (char) (7032; 1184 characters remaining).

### 2026-08-11, iteration 1321 — [[characters/杆 (char)|杆]]

**`mc_id: 6224` confirmed as a trusted long-tail value** per checklist policy (beyond this vault's `CC 0000`–`CC 3000` range, same pattern as [[棍]]'s `mc_id: 9656`). **`graphemic_classification: 干` confirmed correct** (形聲: semantic 木 + phonetic 干, exact OC match `*kaːn`, cross-verified against sibling phonetic-series pages [[干]] and [[肝]]). **`aliases: 桿` confirmed correct** (Wiktionary: traditional/simplified pair, covering all pole/rod senses).

**Vietnamese narrowed to genuine Hán Việt only**: stored `[can, cán, cơn]` mixed Wiktionary's two true Hán Việt readings with one Nôm-only reading (`cơn`, glossed "burst, fit, bout" — an unrelated native word, not this character's Sino-Vietnamese derivation); narrowed to `[can, cán]`.

Filled three blank fields: `pos` → `名詞`; `korean_native` (blank) → `지레` ("lever," matching ko.Wiktionary's 훈 gloss and paralleling `japanese_native: てこ`, itself confirmed correct); `hanmun_edu_level` (blank) → `無` after directly checking the Korean 한문교육용기초한자 (1800-character) list on ko.Wikipedia and confirming 杆 is absent from both the MS and HS sub-lists. `joyo_level` (blank) → `表外字` (ja.Wiktionary explicitly labels it 表外漢字, non-Jōyō/non-Jinmeiyō). **`english` expanded**: `[rod]` alone → added `pole` and `lever`, both directly attested senses.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format, routing the two newly-filled fields to [Korean Missing] and [Hyōgai]. **`## Words`**: added the missing reflexive stand-in [[杆]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters found citing 杆 as their own phonetic (杆 is itself the derived character, already correctly listed on [[干]]'s own Derived Characters section).

**Citing word page [[杆]] (`words/杆.md`) had a `vietnamese: null` literal-string corruption** (the fourth citing-word bug pattern, distinct from the `../characters/` relative-path bug seen the last three cycles) — fixed to the genuine reading `can`. Its `## Notes` section was also entirely empty under a wrong-level heading — rebuilt with the standard character-gloss bullet.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 沫 (char) (7033; 1183 characters remaining).

### 2026-08-11, iteration 1322 — [[characters/沫 (char)|沫]]

**Real `mc_id` off-by-one bug found and fixed** (the second in three cycles): stored `mc_id: 2583` points to a different character entirely (`CC 2000.md` line 608 = 鏡); 沫's true ranking is **2584** (line 609), corrected. **`graphemic_classification: 末` confirmed correct** (形聲, exact OC match `*maːd` on both semantic-compound sides, cross-verified against [[末]]'s own stored MC readings).

**Genuine variant alias added**: 沬, independently verified as an explicit "variant form of 沫" on both en- and zh-Wiktionary; zh-Wiktionary confirms 沬's own competing senses (wash-face, twilight) are themselves marked obsolete/abandoned in standard Chinese, so this does NOT trigger the shared-ancient-origin trap (cf. [[亨]]'s excluded 享/烹) — the situation is inverted, with 沫 dominant and 沬 the obsolete one, matching the more liberal precedent instead. Note: Wiktionary's raw "variant forms" list also included several clearly-unrelated common characters (漂, 粕, 渤, 批, etc.) — evidently extraction noise from an adjacent table, not real variants — correctly excluded without individual verification given the implausibility.

**Vietnamese narrowed to genuine Hán Việt only**: stored `[mát, mướt, mượt, mạt]` mixed one true Hán Việt reading (`mạt`) with three Nôm-only readings; narrowed to `[mạt]` after confirming the Hán Việt/Nôm split directly on Wiktionary's own labeled table. **`japanese` and `japanese_native` both expanded**: ja.Wiktionary lists three on'yomi (呉音 マチ + マツ, 漢音 バツ) where only two were stored — added the missing `MACHI`; and three kun'yomi (あわ, しぶき "splash," つばき "saliva") where only one was stored — expanded to all three, corroborated by adding `saliva` to `english` (matching the character's own attested Etymology-1 sense). `joyo_level: 日本人名用漢字` confirmed correct (Jinmeiyō). Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, three of four standard bullets missing entirely) to the standard format. **`## Words`**: the character's own `stand_in: 沫` field pointed to the word [[沫]] itself, but no reflexive entry existed at all in the Words list, only the unrelated compound [[泡沫]] — added the missing stand-in entry. No Chengyu hits; no derived characters.

**The reflexive stand-in word page [[沫]] (`words/沫.md`) had the same `vietnamese: null` corruption as last cycle's [[杆]]** — fixed to `mạt`; its `## Notes` was also entirely empty under a wrong-level heading — rebuilt with the standard gloss bullet. [[泡沫]] (the other citing word) was already clean.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 苛 (7034; 1182 characters remaining).

### 2026-08-11, iteration 1323 — [[characters/苛|苛]]

**`mc_id: 1660` verified correct as-is** (`CC 1000.md` line 689). **`graphemic_classification: 可` confirmed correct** (形聲, semantic 艸 + phonetic 可, OC `*ɡaːl` vs. phonetic's own `*kʰaːlʔ`, cross-verified against sibling phonetic-series pages [[呵]] and [[奇]]). Vietnamese (`hà`), korean_native (`가혹할`), japanese (`KA, GA`), and japanese_native (`いじ`, stem of いじめる) all confirmed correct as-is — no contamination found. `joyo_level: 高等` confirmed correct after directly checking [Jōyō - Kōtō] and finding 苛 listed there (line 73; added to Jōyō in 2010, a secondary-school-taught addition rather than an elementary Kyōiku kanji).

Filled blank `pos` → `性詞`, matching both citing words' own stored `pos`. Rebuilt `## Notes` (two bare floating unlinked CC-name lines, a stray unformatted word-mention with no ruby/注音/tag sitting where a bullet should be, all other standard bullets missing) to the standard 4-bullet format. **`## Words`**: promoted the stray [[苛刻]] mention into a proper ruby entry and tagged it as the reflexive stand-in (`stand_in: 苛刻`, 注音 verified from its own page), kept the existing [[苛酷]]. No Chengyu hits; no derived characters.

**Same `../characters/` broken-relative-path bug found and fixed on both citing word pages** ([[苛刻]], [[苛酷]]) — now confirmed as a widespread pre-existing pattern across many older word pages, not isolated incidents.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 狙 (7035; 1181 characters remaining).

### 2026-08-11, iteration 1324 — [[characters/狙|狙]]

**`mc_id: 3446` verified correct as-is** (`CC 3000.md` line 467). **`graphemic_classification: 且` confirmed correct** (形聲, semantic 犭 + phonetic 且; MC Baxter `tshjo` and OC Zhengzhang `*sʰa, *sʰas` both confirmed against Wiktionary directly, matching the already-stored `middle_chinese_initial: t͡sʰ` / `middle_chinese_final: ɨʌ`).

**Real bug found and fixed: an invalid alias.** The stored `aliases: [雎]` was checked against both en- and zh-Wiktionary, neither of which calls 雎 a variant/alternative form of 狙 at all — 雎 is a wholly distinct character with its own dominant meaning (the bird name 雎鳩 "osprey," the historical figure 范雎, a river name, a surname), sharing only the same 且 phonetic series. The two characters were conflated because a citing word, [[狙鳩]] ("osprey," properly 雎鳩), uses 狙 as a graphemic stand-in glyph for the pageless 雎 — a completely different relationship (glyph substitution for a missing character) from the `aliases:` field's defined purpose ("simplified, historical, regional variants" of the *same* character, per `checklist_characters.md`). Removed the invalid alias; the substitution relationship remains correctly documented on [[狙鳩]]'s own `aliases: [雎鳩, 雎鸠]` field, where it belongs.

**`english` expanded**: Wiktionary documents 狙 as genuinely polysemous under a *single* etymology — "monkey; ape" and "to lie in wait for, to watch for" (the latter a natural semantic extension of stealthy simian behavior, not a homographic collision like [[夭]]'s prior cross-sense bug) — added `monkey; ape`, ordered last since the operative Dan'a'yo sense (matching `pos`/`stand_in`) is the ambush sense. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos` (not the naive nominal-noun assumption "monkey" might suggest). Vietnamese (`thư`), korean_native (`원숭이`, "monkey" — the other sense), japanese (`SHO, SO`), and japanese_native (`ねら`, stem of ねらう) all confirmed correct as-is.

Rebuilt `## Notes` (a bare non-standard `雎=C#2850` debug-looking fragment, two floating unlinked CC-name lines, standard bullets otherwise missing) to the standard 4-bullet format. **`## Words`**: tagged the existing [[狙撃]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word pages fixed**: [[狙撃]] had no `## Notes` section at all — added the standard compositional gloss bullet (also catching that its second component's filename has a "(char)" suffix — `撃 (char).md` — not bare `撃.md`). [[狙鳩]] had the same recurring `../characters/` broken-relative-path bug seen in prior cycles — fixed.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 枢 (char) (7036; 1180 characters remaining).

### 2026-08-11, iteration 1325 — [[characters/枢 (char)|枢]]

**`mc_id: 2155` verified correct as-is** — initially looked like a bug (the `CC 2000.md` entry at that rank is plain-text `樞`, not `枢`), but confirmed this is expected and correct: 枢 is a simplified-form primary page whose traditional alias 樞 is what the Classical Chinese corpus (necessarily written in traditional characters) actually ranks, the same convention already established for [[国]] (whose `mc_id: 30` likewise ranks its own traditional alias 國, confirmed via `CC 0000.md`'s own linked entry). Documented this reasoning explicitly in the new MC-ordinal bullet ("as its traditional form 樞") for future clarity. **`graphemic_classification: 区` confirmed correct** (形聲, semantic 木 + phonetic 区/區; OC \*kʰjo self vs. phonetic's own primary-sense OC \*kʰo, both confirmed directly on Wiktionary) — also trimmed a spurious second OC value (`*qoː`) from the phonetic gloss that didn't match any of 區's actual attested readings, apparently miscopied from an unrelated character.

korean_native (`지도리`), japanese (`SUU, SHU`), and japanese_native (`からくり`) all confirmed correct as-is; vietnamese (`[khu, xu]`, already a deliberate narrowing from Wiktionary's undifferentiated 9-item raw list) left as-is, no Hán Việt/Nôm split available to further verify against. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (correct OC gloss but wrong heading format, two floating unlinked CC-name lines, and two stray unformatted word-mentions with no ruby/注音/tags misplaced into what should have been the Words section) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[枢]], promoted the two stray Notes-section word mentions ([[枢机]], [[枢机卿]]) into proper ruby entries, and kept the existing [[枢紐]]. No Chengyu hits; no derived characters.

**Citing word page [[枢]] (`words/枢.md`) had a double corruption** matching the earlier-session [[悩]] precedent exactly: both `vietnamese: null` and `korean: "null"` literal-string bugs — fixed to `khu` (matching the character page's own primary Hán Việt candidate) and `추` respectively; its empty `## Notes` under a bare heading was also filled with the standard gloss bullet. **The recurring `../characters/` broken-relative-path bug was found and fixed on all three other citing words** ([[枢紐]], [[枢机]], [[枢机卿]]) — now the fifth consecutive cycle surfacing this pattern.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 呪 (7037; 1179 characters remaining).

### 2026-08-11, iteration 1326 — [[characters/呪|呪]]

**`mc_id: 7688` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 祝` investigated in depth and confirmed correct, but for a subtler reason than a plain 形聲 compound**: zh-Wiktionary shows 呪's literal glyph is ⿰口兄 (mouth + 兄), and en-Wiktionary's etymology explicitly calls it "a graphic differentiation (分化): variant form of 祝" rather than a fresh phono-semantic compound. Checked 兄's own MC (x/wɣiæŋ) against 祝's own MC (t͡ɕ/ɨuk, nearly identical to 呪's own t͡ɕ/ɨu) — 祝 is by far the better phonetic match, confirming 呪 functions as 祝 with 示 swapped for 口 to visually distinguish the "curse" sense from 祝's "to pray," not as an independent compound freshly built on 兄. Rewrote the Notes bullet to state this honestly (分化 of 祝) rather than implying a literal-glyph phonetic relationship that doesn't hold up phonetically.

**Vietnamese narrowed, with a missing dominant reading added**: stored `[huênh, huếnh]` — two Nôm-only, semantically unrelated readings — while vi.Wiktionary's own labeled table shows the actual Hán Việt reading `chú` (also independently attested as a Nôm reading) was entirely missing; narrowed to `[chú]` alone. **`japanese` expanded**: ja.Wiktionary lists three on'yomi (呉音 しゅ, 漢音 しゅう, 慣用音 じゅ) where only two were stored; added the missing `SHU`. `joyo_level: 高等` confirmed correct (added to Jōyō in 2010, already listed on [Jōyō - Kōtō] line 433). korean_native (`빌`, "to pray/invoke" — a plausible bridge sense connecting 祝's origin and 呪's ritual-invocation modern use) and japanese_native (`まじな`, stem of まじなう) left as-is.

Filled blank `boundedness` → `90`, matching the pattern of other characters whose `stand_in` is a two-character compound (cf. [[忌]], [[巫]], both also 90). Rebuilt `## Notes` (two bare floating unlinked CC-name lines, a non-standard "Components: [[口]], [[兄]]" bullet reflecting the literal-but-phonetically-misleading glyph breakdown) to the standard format. **`## Words`**: tagged the existing [[呪文]] as the reflexive stand-in, added the missing [[呪詛]] (注音 verified from its own page). No Chengyu hits; no derived characters.

**Citing word page fixes**: [[呪文]] had the same recurring `../characters/` broken-relative-path bug — fixed (two occurrences in one line). [[呪詛]] had no `## Notes` section at all — added the standard compositional gloss bullet, also flagging it as the stand-in for [[詛]] per that character's own `stand_in: 呪詛` field.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 妬 (7038; 1178 characters remaining).

### 2026-08-11, iteration 1327 — [[characters/妬|妬]]

**Real `mc_id` bug found and fixed** (now the third confirmed instance this session): stored `mc_id: 3655` points to a different character (`CC 3000.md` line 684 = 豳); 妬's true rank is **3656** (line 685) — note the vault's CC corpus lists 妬 and its variant 妒 as two *separate* entries at different ranks (2088 and 3656 respectively), confirming they're tracked as distinct glyphs in the frequency data even though they're the same character. **`graphemic_classification: 石` confirmed correct** (形聲, semantic 女 + phonetic 石, OC \*taːɡs vs. phonetic's own \*djaɡ, both confirmed on Wiktionary).

**Genuine variant alias added**: 妒 — Wiktionary explicitly states 妬 is "the Japanese form" while 妒 is "the simplified and traditional Chinese form" of the same character; since 妒 has no separate vault page, added as an alias here, following the same asymmetric-primary-form precedent as [[国]]/國 and [[枢 (char)|枢]]/樞.

**Vietnamese narrowed to genuine Hán Việt only**: stored `[đo, đó, đú, đố, đủ]` mixed one confirmed Hán Việt reading (`đố`, cross-verified on both 妬's and 妒's own Wiktionary pages) with Nôm variants and two forms (`đo`, `đủ`) that appear on neither page at all — narrowed to `[đố]` alone, corroborated by the citing word [[嫉妬]]'s own documented `vietnamese: tật đố`. **`japanese` expanded**: ja.Wiktionary lists two on'yomi (呉音 ツ, 漢音 ト) where only one was stored — added the missing `TSU`. `joyo_level: 高等` confirmed correct (added to Jōyō in 2010, already listed on [Jōyō - Kōtō] line 754).

**Routing bug caught before finalizing**: initially routed `hanmun_edu_level: 名` to [Korean Name ㅈ] by copy-habit from recent cycles, but caught that the routing key is the character's own `korean` field (`투`, initial ㅌ) — not the Dan'a'yo `諺文` (`도`, initial ㄷ) — confirmed against the working precedent on [[苛]] (routed by its `korean` field `가`, not its differently-initialed `諺文` `하`); corrected to [Korean Name ㅌ] and verified 妬 is actually listed there.

Filled blank `pos` → `性詞` (matching the citing word's own `pos`), blank `hsk_level` → `無` (confirmed absent from Wiktionary's HSK data), and blank `boundedness` → `90` (two-character `stand_in`, matching the established pattern). Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted etymology fragment) to the standard 4-bullet format, folding the ancient-sense nuance into the graphemic bullet's prose. **`## Words`**: added the missing reflexive stand-in [[嫉妬]] (注音 verified from its own page) to a Words section that didn't exist at all. Confirmed the `cranberry` tag's transitivity holds ([[嫉]] shares the identical `stand_in: 嫉妬`). One Chengyu false positive excluded ([[勿貪隣物]] merely mentions 妬 in prose, not in its `characters:` field); no derived characters.

**Citing word page [[嫉妬]] had the recurring `../characters/` broken-relative-path bug** — fixed (two occurrences).

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 宛 (7039; 1177 characters remaining).

### 2026-08-11, iteration 1328 — [[characters/宛|宛]]

**`mc_id: 1119` verified correct as-is** (`CC 1000.md` line 128). **`graphemic_classification: 夗` confirmed correct** (形聲, semantic 宀 + phonetic 夗, exact OC match `*qonʔ` on both sides, exact MC match too, cross-verified against [[夗]]'s own stored MC). Note: 宛 is heavily polysemous across six separate etymologies (wǎn "as if/crooked," yuān a place name, and four rarer variant-of readings for 蘊/鬱/黦/豌) — confirmed the stored fields all correctly track only Etymology 1 (wǎn), matching the citing word [[宛然]]'s own documented sense, with no cross-sense contamination.

**`japanese` expanded**: ja.Wiktionary lists two on'yomi (呉音 オン, 漢音 エン) where only one was stored; added the missing `ON`. **`japanese_native` filled from a wrongly-stored `ø`**: real kun'yomi exist matching this exact sense (あたかも "as if," さながら "just as," among others) — set to `あたか`, the stem of あたかも, directly matching the stored `english: as if`. Vietnamese (`[uyển, uốn]`) and korean_native (`완연할`) both confirmed correct as-is. Filled blank `pos` → `副詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **New `### Derived Characters` section added**: [[婉]], [[碗 (char)|碗]], [[腕 (char)|腕]] (all confirmed via exact `graphemic_classification: 宛` match). **`## Words`**: tagged the existing [[宛然]] as the reflexive stand-in. No Chengyu hits.

**Citing word page [[宛然]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 劾 (7040; 1176 characters remaining).

### 2026-08-11, iteration 1329 — [[characters/劾|劾]]

**Real `mc_id` off-by-one bug found and fixed** (the fourth confirmed instance this session): stored `mc_id: 1746` points to a different character (`CC 1000.md` line 779 = 鎮); 劾's true rank is **1747** (line 780), corrected. **`graphemic_classification: 亥` confirmed correct** (形聲, phonetic 亥 + semantic 力, exact MC match, OC \*ɡɯːɡs vs. phonetic's own \*ɡɯːʔ, both from the same root series).

**Vietnamese narrowed with one narrowing and one addition net**: stored `[hạch, hặc, hếch, hệch]` mixed two plausible Sino-Vietnamese doublets with two unrelated Nôm-noise readings (`hếch, hệch`, unattested anywhere and resembling an unrelated native word "to grin/bare teeth"); narrowed to `[hạch, hặc]` — both retained despite Wiktionary listing only `hặc` directly, because the citing word [[参劾]]'s own compositional research independently documents `hạch` in `tham hạch`, corroborating it as a genuine parallel Sino-Vietnamese reading rather than noise.

**`japanese` expanded**: ja.Wiktionary lists two on'yomi (呉音 がい, 漢音 かい) where only one was stored; added the missing `KAI`. **`japanese_native` filled from a wrongly-stored `ø`**: real kun'yomi exist matching this exact sense (しらべる "to investigate/examine," among others); set to `しらべ`, the stem, directly matching the "accuse/investigate" sense. Filled blank `pos` → `事詞`.

**Missing-word citation found and removed, not fabricated**: the pre-existing `## Words` list cited `[[弾劾]]` ("impeach") with no ruby/注音 at all — checked for a word page under that name and any alias variants of its constituent characters, found none exist anywhere in the vault (genuinely missing, not a citation-vs-alias mismatch); rather than inventing an unverified 注音 or leaving a dangling bare wikilink, removed the citation entirely as out of scope for character-perfecting (word creation is a separate process) and added the verified reflexive stand-in [[参劾]] in its place.

Rebuilt `## Notes` (a non-standard "Components:" bullet, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. No Chengyu hits; no derived characters.

**Citing word page [[参劾]] had the recurring `../characters/` broken-relative-path bug** — fixed (two occurrences).

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 帖 (char) (7041; 1175 characters remaining).

### 2026-08-11, iteration 1330 — [[characters/帖 (char)|帖]]

**`mc_id: 5410` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 占` confirmed correct** (形聲, semantic 巾 + phonetic 占, OC \*tʰeːb vs. phonetic's own \*tjems, a plausible if drifted phonetic-series match, consistent with Wiktionary's own compound template).

**Real cross-reading bug found and fixed**: 帖 is triply homographic across Mandarin tones — tiē "submissive" (Etym. 1), tiě "note, invitation, card" (Etym. 2), tiè "copybook, model" (Etym. 3) — but the stored `mandarin: tiē` named the *wrong* tone/sense entirely, contradicting the page's own `english: [invitation, card]`, which belongs to tiě. Confirmed the correct tone directly on zh-Wiktionary ("请帖/帖子... 发音2... tiě") and corrected the field; documented the three-way homography explicitly in the new Notes bullet to prevent future confusion.

**Vietnamese narrowed to the sole attested reading**: stored `[thiêm, thiếp, thiệp, thếp]` — only `thiếp` is attested on Wiktionary's own Hán Nôm table; the other three had no support anywhere (including the citing word page, which offered no research either) — narrowed to `[thiếp]` alone. `japanese` (`JOU, CHOU`) and `japanese_native` (`かきもの`) both confirmed already-complete against ja.Wiktionary's full reading list — no expansion needed, a rarer clean-verification outcome this session. korean_native (`문서`, "document") confirmed as a reasonable match for the invitation/card/document sense.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[帖]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

**Citing word page [[帖]] (`words/帖.md`) had a triple bug**: the same `vietnamese: null` corruption seen repeatedly this session (fixed to `thiếp`), the *same* wrong-tone `mandarin: tiē` bug independently duplicated (fixed to `tiě`), and an entirely empty `## Notes` under a wrong-level heading (filled with the standard gloss bullet).

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 祀 (7042; 1174 characters remaining).

### 2026-08-11, iteration 1331 — [[characters/祀|祀]]

**`mc_id: 565` verified correct as-is** (`CC 0000.md` line 586). **`graphemic_classification: 巳` confirmed correct** (形聲, semantic 示 + phonetic 巳, exact OC and MC match on both sides, `*ljɯʔ` / `z, ɨ`). **Genuine variant alias added**: 禩, independently verified as an unqualified "variant form of 祀" with no competing modern meaning (Japanese lists it as Hyōgai with no definition of its own).

Vietnamese (`tự`), korean_native (`제사`), japanese (`SHI, JI`), japanese_native (`まつ`, stem of まつる/まつり), `joyo_level: 表外字`, and `hanmun_edu_level: 高等` (confirmed listed on [Korean HS] line 325) all confirmed correct as-is — an unusually clean page overall, only the alias and a few blanks needed attention. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[祭祀]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

**Citing word page [[祭祀]] had no `## Notes` section at all** — added the standard compositional gloss bullet, also flagging it as the stand-in for [[祀]] per that character's own `stand_in: 祭祀` field.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 旺 (7043; 1173 characters remaining).

### 2026-08-11, iteration 1332 — [[characters/旺|旺]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy (not present in `CC 0000`–`CC 3000`). **`graphemic_classification: 王` confirmed correct**, but with a genuinely interesting nuance documented in the new Notes bullet: Wiktionary shows 旺 is a reanalysis — the original character was 暀 (日 + phonetic 往), later simplified/reinterpreted as 日 + 王, with 王's own OC (`*ɢʷaŋ`) an exact match to 旺's own (`*ɢʷaŋs`), confirming 王 is indeed the correct phonetic to cite for the *current* glyph, not a mistake.

**Alias research**: the existing `aliases: [𫞂]` was verified as a genuine (if now-archaic per Chinese-context wording) variant; checked three additional Wiktionary-listed forms (暀, 𣈧, 𣇭) and excluded all three as explicitly-labeled *ancient/obsolete* predecessor forms rather than live synchronic variants — same discipline established with [[巫]]'s excluded 𢍮 earlier this session.

**Real cross-reading bug found and fixed**: `japanese_native` was stored as `うつくし` ("beautiful," stem of うつくしい) — a real but tangential kun'yomi of 旺 unrelated to the character's documented "flourish/prosper" sense — corrected to `さかん` (stem of さかん, "thriving," directly matching `english`). Vietnamese (`vượng`), korean_native (`왕성할`), and `japanese: [OU]` (single reading, already complete — 呉音 and 漢音 coincide) all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, misplaced after the Words section, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[興旺]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[興旺]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 斧 (7044; 1172 characters remaining).

### 2026-08-11, iteration 1333 — [[characters/斧|斧]]

**`mc_id: 1628` verified correct as-is** (`CC 1000.md` line 657). **`graphemic_classification: 父` confirmed correct** (形聲, phonetic 父 + semantic 斤, OC \*paʔ vs. phonetic's own \*baʔ, a plausible voiced/voiceless phonetic-series pair).

**Alias research, both candidates excluded**: 鈇 was checked and found to have its own distinct dominant modern meaning (the Chinese name for the chemical element flerovium, Fl-114) — the same shared-modern-meaning trap as [[亨]]'s excluded 享/烹, so not added despite being labeled "a variant form of 斧" for its classical sense; 𤕑 returned a 404 and was likewise not added.

**Vietnamese typo fixed**: stored `[buá, búa, phủ]` contained a near-duplicate — `buá` misplaces the diacritic (Vietnamese tone marks the vowel nucleus; the correct spelling of this word is `búa`, already separately present in the same list) — removed the malformed duplicate, keeping `[búa, phủ]` (both independently confirmed: `búa` Nôm, `phủ` Hán Việt). korean_native (`도끼`), japanese (`FU`), and japanese_native (`おの`) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: promoted the stray [[斧子]] mention into the properly-tagged reflexive stand-in. One Chengyu false positive excluded ([[天衣無縫]] merely mentions 斧鑿 in an illustrative example sentence, not in its `characters:` field); no derived characters.

**Citing word page [[斧子]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 洩 (7046; 1171 characters remaining).

### 2026-08-11, iteration 1334 — [[characters/洩|洩]]

**`mc_id: 1300` confirmed correct as-is**, referring to the vault's own alias 泄 in the CC corpus (`CC 1000.md` line 313) — same asymmetric-primary-form pattern as [[国]]/國 and [[枢 (char)|枢]]/樞, documented explicitly in the new MC-ordinal bullet.

**Real `graphemic_classification` bug found and fixed**: stored `世`, but Wiktionary's glyph-origin template for 洩 itself explicitly names **曳** as the phonetic component (氵+曳), not 世 — 世 is actually the phonetic of the *other* variant spelling 泄 (氵+世), a genuinely different literal composition despite both characters sharing the same meaning. Confirmed via an exact OC match: 洩's own OC \*leds is identical to 曳's own \*leds, while 世's OC is unrelated — corrected the field to 曳.

**Real bad-alias bug found and fixed**: stored `aliases: [渫, 泄]`. Checked 渫 directly — neither en- nor zh-Wiktionary calls it a variant of 洩; zh-Wiktionary's own 異體字 section instead lists **泄** as a variant of **渫** (the relationship running the opposite direction from what the alias implied), and 渫 has its own primary sense "to dredge" with five independent tonal readings. Removed 渫 from `aliases`. This alias was also propagated into two other places, both corrected: the citing word [[漏洩]]'s own prose falsely claimed "洩, 泄, and 渫 are all listed as aliases" (corrected to accurately describe only the 洩/泄 relationship, with a note on the removal); and [Korean Name ㅅ]'s own list had `[渫](characters/洩.md)` — a link erroneously implying 渫 resolves to 洩's own page — corrected to the vault's standard pageless-character convention, a bare `[[渫]]` wikilink (matching neighboring unresolved entries like `[[褻]]`, `[[蔎]]` in the same line).

**Vietnamese expanded**: stored `[dáy, dịa, tiết]` was missing `duệ`, a genuine second Hán Việt reading confirmed directly on Wiktionary's own labeled Hán Việt/Nôm split — added, reordered with the two Hán Việt readings first.

**Real cross-reading bug found and fixed**: `japanese_native` was `の` (stem of のびる, "to extend/stretch" — a real but tangential kun'yomi of 洩 unrelated to the documented "vent/leak" sense) — corrected to `もれ` (stem of もれる, "to leak," directly matching `english`), the same category of fix as [[旺]]'s うつくし→さかん correction last cycle. Filled blank `joyo_level` → `表外字` (confirmed via ja.Wiktionary) and blank `pos` → `事詞`, matching the citing word's own stored `pos`. `japanese: [EI, SETSU]` confirmed already complete (両方 呉音/漢音 present).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[漏洩]] as the reflexive stand-in. No Chengyu hits; no derived characters (checked via exact `graphemic_classification: 曳` match — only 洩 itself qualifies).

**Citing word page [[漏洩]] had the recurring `../characters/` broken-relative-path bug** — fixed, in addition to the stale-alias-claim correction above.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 昌 (7047; 1170 characters remaining).

### 2026-08-11, iteration 1335 — [[characters/昌|昌]]

**`mc_id: 700` verified correct as-is** (`CC 0000.md` line 724). **`graphemic_classification: 會意` confirmed correct** (Wiktionary: associative compound, 日 "sun" + 口 "mouth," the mouth referencing being roused at dawn by shouts/songs; 口 later evolved to 曰 in Warring States script). Vietnamese (`xương`, confirmed the sole genuine Hán Việt reading against Wiktionary's own labeled split — a Nôm-only `xang` correctly left out), korean_native (`창성할`), japanese (`SHOU`), japanese_native (`さかん`, matching [[旺]]'s corrected reading from two cycles ago), `joyo_level: 日本人名用漢字` (confirmed on [Jinmeiyō]), and `hanmun_edu_level: 中` (confirmed on [Korean MS]) all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, a stray unlinked syllable-page mention, two bare floating unlinked CC-name lines, misplaced after the Words section) to the standard 4-bullet format. **New `### Derived Characters` section added**: [[唱]] (confirmed via exact `graphemic_classification: 昌` match). **`## Words`**: tagged the existing [[昌盛]] as the reflexive stand-in. No Chengyu hits.

**Citing word page [[昌盛]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 炒 (char) (7048; 1169 characters remaining).

### 2026-08-11, iteration 1336 — [[characters/炒 (char)|炒]]

**`mc_id: 7495` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 少` confirmed correct** (形聲, semantic 火 + phonetic 少, per Wiktionary's own compound template, despite the two characters' OC reconstructions having diverged significantly over time — a known feature of some phonetic series, not treated as disqualifying).

**Extensive alias research on a 12-candidate Wiktionary variant list**: individually verified each — five confirmed genuine and added (煼, 㷅, 𩱦, 𩱈, 㶤, all unqualified "variant/alternative/non-classical form of 炒" with no competing modern meaning); one excluded as an explicitly-labeled ancient form (焣, matching this session's established ancient-form exclusion discipline); six returned 404 and were left unadded (𢐨, 𤑵, 𤌽, 𤌉, 𤊛, 𤊝).

Vietnamese (`[sao, xào, xáo]`), korean_native (`볶을`), japanese (`SOU, SHOU`), and japanese_native (`い`, stem of いる/いためる) all confirmed correct as-is, matching Wiktionary's own reading lists exactly. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[炒]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

**Citing word page [[炒]] (`words/炒.md`) had the recurring `vietnamese: null` corruption** — fixed to `xào` (the standard modern verb for stir-frying, e.g. rau xào); its empty `## Notes` under a wrong-level heading was also filled with the standard gloss bullet.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 枝 (7049; 1168 characters remaining).

### 2026-08-11, iteration 1337 — [[characters/枝|枝]]

**`mc_id: 1103` verified correct as-is** (`CC 1000.md` line 112). **`graphemic_classification: 支` confirmed correct** (形聲, semantic 木 + phonetic 支, exact OC and MC match on both sides, `*kje` / `t͡ɕ, iᴇ`). **Deliberately did not add 支 itself as an alias** despite Wiktionary listing it as an "alternative form": 支 has its own robust, dominant modern meanings (to support, a productive classifier, the Earthly Branches) and its own pre-existing vault page — the same shared-modern-meaning exclusion pattern as [[亨]]'s excluded 享/烹.

**Real typo bug found and fixed**: `english: [foilage]` — a misspelling of "foliage," and also not the character's actual core sense — corrected to `[branch, twig]`, matching Wiktionary's actual definitions exactly. **`japanese` expanded**: ja.Wiktionary lists two 呉音 (ギ, シ) and two 漢音 (キ, シ) on'yomi; only `SHI` and `KI` were stored, missing the 呉音-only `GI` — added.

Vietnamese (`[che, chi]`), korean_native (`가지`), and japanese_native (`えだ`) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

**Self-caught routing error before finalizing**: initially miswrote the levels bullet linking `joyo_level: "5"` to a fabricated "Grade 5" path built from the `Jōyō - Kyōiku` filename, and dropped the separate `grade_level: 先進` → [Grade Advanced] link entirely — caught by re-checking the routing table (`grade_level` and `joyo_level` are independent scales; a numeric `joyo_level` routes to the single shared `[[lookup/Japanese/Jōyō - Kyōiku]]` page, not a per-grade file) and corrected to include both links properly. **Also self-caught an ordinal-suffix typo** ("1103th" → "1103rd") by spot-checking existing pages' convention before finalizing.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[枝葉]] as the reflexive stand-in. One Chengyu false positive excluded ([[天長地久]] merely quotes 連理枝 in a poetic couplet, not in its `characters:` field); no derived characters.

**Citing word page [[枝葉]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-11`.

Next never-perfected character by `danayo_id`: 呵 (7050; 1167 characters remaining).

### 2026-08-12, iteration 1338 — [[characters/呵|呵]]

**`mc_id: 2758` verified correct as-is** (`CC 2000.md` line 791). **`graphemic_classification: 可` confirmed correct** (形聲, semantic 口 + phonetic 可, same OC pattern independently confirmed on [[苛]] two cycles ago). **Cross-sense Korean field investigated and confirmed correct, not a bug**: ko.Wiktionary's primary listed reading is 가 (for the "to scold"/alternate-form-of-訶 sense), but the stored `korean: 하` correctly targets the *operative* onomatopoeic-laughter sense instead — corroborated by the citing word [[呵呵]]'s own attested Korean reading 하하, and by the separate chengyu [[呵呵大笑]] using 가가대소 (the 가 reading) for its own more classical/formal register — both readings genuinely attested, just sense-differentiated, the same category of finding as [[帖]]'s multi-tone investigation.

**Alias reconsidered and restored after a genuine investigation reversal**: initially removed `aliases: [哈]` on the reasoning that 哈 is an extremely dominant modern character with broad independent usage (matching the shared-modern-meaning exclusion pattern used for [[亨]]'s 享/烹 and [[斧]]'s 鈇) — but then discovered [Korean Name ㅎ]'s own pre-existing entry displays this exact character *as* `[哈](characters/呵.md)`, confirming the vault's own naming-hanja infrastructure already treats 哈 as this character's registered form for the 하 reading. Re-evaluated: unlike 享/烹 or 鈇 (whose alternate senses are wholly unrelated to the shared character), 哈's own dominant modern sense is itself "ha" (laughter) — the *same* core sense as 呵's operative one here, not a competing one — so restored 哈 to `aliases`, matching the more liberal precedent (cf. [[誘]], [[呻]], [[忌]]'s additions) rather than the exclusion trap.

**Real bugs found and fixed**: the existing graphemic Notes bullet had an empty semantic gloss (`("")`, now filled with "mouth") and the character's own polysemy folded in as prose. `korean_native` was blank — filled with `웃을` (verb-stem gloss, "to laugh," matching ko.Wiktionary's own 훈 "껄껄 웃다"). `japanese_native` was `か` — actually an on'yomi-looking value, not a real kun'yomi stem; ja.Wiktionary's actual kun'yomi are しかる ("to scold") and わらう ("to laugh") — corrected to `わら`, matching the operative sense (the same category of cross-reading fix as [[旺]] and [[洩]] in recent cycles). Filled blank `joyo_level` → `表外字` (confirmed via ja.Wiktionary).

Rebuilt `## Notes` (a floating non-standard "Not a word" fragment, two bare unlinked CC-name lines) to the standard 4-bullet format. **New `## Chengyu` section added**: [[呵呵大笑]] (confirmed via exact `characters:` field match, both citation and the reflexive [[呵呵]] word page already used correct bare `characters/`-relative links — no path bug this cycle, a nice change of pace). No derived characters.

Stamped `date-last-perfect: 2026-08-12`. (Note: this iteration crossed the day boundary — vault stamp correctly reflects today's actual date, not the prior day's default some earlier entries in this log used.)

Next never-perfected character by `danayo_id`: 艾 (7051; 1166 characters remaining).

### 2026-08-12, iteration 1339 — [[characters/艾|艾]]

**`mc_id: 1868` verified correct as-is** (`CC 1000.md` line 905). **`graphemic_classification: 乂` confirmed correct** (形聲, semantic 艸 + phonetic 乂, OC \*ŋaːds vs. phonetic's own \*ŋads, a close match differing only in vowel length).

**Vietnamese typo fixed**: stored `[nghề, nghễ, nghệ, ngải]` included `nghề` ("profession, trade" — an entirely unrelated, extremely common Vietnamese word, almost certainly a diacritic-slip duplicate of the genuine `nghễ`) alongside vi.Wiktionary's actual three confirmed readings (`ngải, nghệ, nghễ`) — removed the spurious fourth entry.

**Real typo bug found and fixed**: `japanese: [GAI, GEI]` — `GEI` does not correspond to any attested reading; ja.Wiktionary's actual on'yomi are 呉音 ガイ(GAI)/ゲ(GE), 漢音 ガイ(GAI) — corrected to `[GAI, GE]`. **Real cross-sense bug found and fixed**: `japanese_native` was `おさ` (stem of おさめる, "to govern" — belonging to a wholly different, obsolete etymology of this character) rather than a reading matching the operative "mugwort" sense; corrected to `よもぎ` (mugwort itself, directly matching `english`/`korean_native`), the same category of fix as recent [[旺]]/[[洩]]/[[呵]] corrections.

**New bug type found and fixed: broken relative paths on a suffix-less filename**, same pattern as [[忌]] earlier this session — 艾.md (no "(char)" suffix) had `../lookup/...` and `../syllables/...` links throughout its Notes bullets; corrected to bare `lookup/...`/`syllables/...`. Also added the missing MC-ordinal-rank sentence, which had been omitted entirely (the bullet jumped straight to "Ancient..." with no rank stated).

**`## Words`**: tagged the existing [[艾草]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[艾草]] had the same `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 坦 (7052; 1165 characters remaining).

### 2026-08-12, iteration 1340 — [[characters/坦|坦]]

**`mc_id: 3594` verified correct as-is** (`CC 3000.md` line 619). **`graphemic_classification: 旦` confirmed correct** (形聲, semantic 土 + phonetic 旦, OC \*tʰaːnʔ vs. phonetic's own \*taːns, a plausible aspirated/tone-variant phonetic-series match). **Genuine variant alias added**: 憻, independently verified as an unqualified "variant form of 坦" with no competing modern meaning.

**Vietnamese narrowed with one addition**: stored `[ngẩn, thưỡn, thản, đất, đật, đắt, đứt]` mixed two genuine readings (`thản` Hán Việt, corroborated by the citing word [[平坦]]'s own `vietnamese: bình thản`; `đất` Nôm) with four unrelated common Vietnamese words that had no support anywhere (`ngẩn` "dazed," `đật`/`đắt` "expensive," `thưỡn` unclear) — narrowed the noise out and added the missing second Hán Việt reading `thán`, confirmed directly on Wiktionary's own list; kept `đứt` (also independently attested as Nôm). Final set: `[thản, thán, đất, đứt]`.

korean_native (`평탄할`), japanese (`TAN`), japanese_native (`たいら`), and `joyo_level: 日本人名用漢字` (confirmed on [Jinmeiyō] line 435) all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[平坦]] to a Words section that only had two unrelated transliteration compounds ([[君士坦丁堡]] "Constantinople," [[巴基斯坦]] "Pakistan"). No Chengyu hits; no derived characters.

**All three citing word pages had the recurring `../characters/` broken-relative-path bug** — fixed on [[平坦]], [[君士坦丁堡]], and [[巴基斯坦]] (the latter two each had four occurrences in a single compositional-etymology bullet).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 爬 (7053; 1164 characters remaining).

### 2026-08-12, iteration 1341 — [[characters/爬|爬]]

**Real bad-alias-and-mc_id bug found and fixed, discovered together**: stored `aliases: [匍]` and `mc_id: 3600`. Checked 匍 directly — its own Wiktionary page never mentions 爬 at all; 匍 is a bound morpheme used only in 匍匐 ("to crawl"), and its own documented variant relationship is to an entirely different character, 撫 ("to stroke, pat"). The apparent "asymmetric primary form" pattern (which would have made `mc_id: 3600` defensible, ranking via an alias, as seen with [[国]]/國 and [[枢 (char)|枢]]/樞) does not actually hold here — 匍 is simply not 爬's alias at all, just a semantically-similar but distinct character that happened to get conflated (same category of error as [[洩]]'s 渫 two cycles ago). Removed the invalid alias and reset `mc_id` to `0` (confirmed 爬 itself does not appear anywhere in `CC 0000`–`CC 3000`).

**`graphemic_classification: 巴` confirmed correct** (形聲, semantic 爪 + phonetic 巴, OC \*braː vs. phonetic's own \*praː, a plausible voiced/voiceless phonetic-series pair). **Genuine variant alias added**: 𧿆, independently verified as an unqualified "variant form of 爬" with no ancient/archaic labeling.

**`japanese` expanded**: ja.Wiktionary lists 呉音 べ(BE) and 漢音 は(HA); only `HA` was stored — added the missing `BE`. Vietnamese (`[ba, bà, bò]`), korean_native (`긁을`, "to scratch" — independently confirmed as a genuine second gloss alongside "to climb" on ko.Wiktionary, not an error), japanese_native (`か`, stem of かく), and `joyo_level: 表外字` all confirmed correct as-is. Filled blank `pos` → `事詞` (an eventive "to crawl," not a naive noun reading).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: promoted the stray [[爬虫]] mention into a proper ruby entry and added the missing reflexive stand-in [[爬行]]. No Chengyu hits; no derived characters.

**Citing word page fixes**: [[爬行]] had no `## Notes` section at all — added the standard compositional gloss bullet, flagging it as the stand-in for [[爬]]. [[爬虫]] had the recurring `../characters/` broken-relative-path bug — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 乖 (7054; 1163 characters remaining).

### 2026-08-12, iteration 1342 — [[characters/乖|乖]]

**`mc_id: 1912` verified correct as-is** (`CC 1000.md` line 953). **`graphemic_classification: 象形` confirmed correct** against the vault's own [List of 象形] (already listed there), despite Wiktionary's glyph origin describing it as two combined graphic elements per Xu Shen — trusted the vault's pre-established categorization rather than second-guessing it from a borderline description.

**Significant cross-sense discovery, documented rather than "fixed" as an error**: 乖 has undergone a genuine semantic inversion — classically "perverse, contrary, to rebel, to diverge" (still the sense preserved in `korean_native: 어그러질` and `japanese_native`'s そむく/もとる kun readings, both left as-is since no positive-sense equivalent exists in either language's dictionaries), while modern colloquial Mandarin flipped the meaning to its near-opposite, "well-behaved, obedient, docile" — which is the sense this vault's own citing word [[乖巧]] documents and uses. Unlike [[夭]]'s prior cross-sense *bug* (which was a wrong-homograph documentation error), this is a real, single-character diachronic meaning-flip with both senses genuinely, separately attested across different languages — added an explanatory Notes bullet rather than "correcting" either field, since both are independently true of the same character at different points/registers.

**Vietnamese expanded**: stored `[quai, quay]` was missing `quái`, the second genuine Hán Việt reading confirmed on Wiktionary's own labeled Hán Việt/Nôm split — added. **`japanese` expanded**: ja.Wiktionary lists 呉音 ケ(KE) and 漢音 カイ(KAI); only `KAI` was stored — added the missing `KE`. (Also double-checked a conflicting "常用字" category tag against the page's own explicit "表外漢字" classification line and trusted the more specific statement — `joyo_level: 表外字` confirmed correct as-is.)

**Genuine variant alias added**: 𠂯, independently verified as an unqualified "variant form of 乖" with no ancient/archaic labeling; a second candidate, 𠁰, was correctly excluded as an explicitly-labeled ancient form, and a third, 𦮃, returned a 404. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[乖巧]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[乖巧]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 祉 (7055; 1162 characters remaining).

### 2026-08-12, iteration 1343 — [[characters/祉|祉]]

**Real `mc_id` off-by-one bug found and fixed** (the fifth confirmed instance this session): stored `mc_id: 2372` points to a different character (`CC 2000.md` line 389 = 暗); 祉's true rank is **2373** (line 390), corrected. **`graphemic_classification: 止` confirmed correct** (形聲, semantic 示 + phonetic 止, OC \*kʰlɯʔ vs. phonetic's own \*kjɯʔ, a close rime match).

**Real copy-paste contamination bug found and fixed**: `korean_native` was stored as `복` — but that's not a native gloss of 祉 at all, it's literally [[福 (char)|福]]'s own Sino-Korean reading (福's own `korean` field is also `복`), evidently bled over from the compound [[福祉]] during original data entry. Confirmed the real native gloss via ko.Wiktionary's own 훈: `행복` ("happiness") — corrected. **`japanese_native` filled from a wrongly-blanked `ø`**: Wiktionary lists a genuine kun'yomi さいわい ("happiness/good fortune") that had been omitted entirely — set to `さいわ`, the stem, directly matching `english`.

`japanese: [SHI, CHI]` (both attested readings already present) and vietnamese (`chỉ`, unverifiable directly on Wiktionary but phonetically regular and uncontradicted) both confirmed correct/reasonable as-is. `joyo_level: 高等` confirmed correct (listed on [Jōyō - Kōtō] line 393). Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[福祉]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[福祉]] had a `vietnamese: ""` literal-empty-string corruption** (distinct from the more common `null`-string pattern seen elsewhere this session) — normalized to a proper blank YAML value rather than fabricating an unresearched Vietnamese reading, consistent with prior-session precedent on [[呪詛]].

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 姪 (7056; 1161 characters remaining).

### 2026-08-12, iteration 1344 — [[characters/姪|姪]]

**Real `mc_id` off-by-one bug found and fixed** (the sixth confirmed instance this session): stored `mc_id: 3559` points to a different character (`CC 3000.md` line 584 = 陝); 姪's true rank is **3560** (line 585), corrected. **`graphemic_classification: 至` confirmed correct** (形聲, semantic 女 + phonetic 至, OC \*diːɡ/\*diɡ vs. phonetic's own \*tjiɡs, a plausible voiced/voiceless coda-matching pair).

**Vietnamese narrowed with one addition**: stored `[diệt, điệt, đẹt]` mixed the one genuine reading (`điệt`, corroborated by the citing word [[姪女]]'s own `vietnamese: điệt nữ`) with two apparent typo/contamination entries — `diệt` ("to destroy, exterminate," an unrelated common word, almost certainly a corrupted `điệt`) and `đẹt` (unattested) — narrowed and added the second genuine reading `điết`, both confirmed directly on Wiktionary's own Hán Nôm list. Final set: `[điệt, điết]`.

**Real cross-sense bug found and fixed**: `japanese_native` was stored as `おい` ("nephew" — labeled by ja.Wiktionary itself as "rare, classical-Chinese-reading only") while the character's own operative sense throughout the page (`english: niece`, `stand_in: 姪女`) is "niece" — the correct matching kun'yomi is `めい`; corrected. **`japanese` expanded**: ja.Wiktionary lists two 呉音 (ジチ, デチ) and two 漢音 (チツ, テツ); only the 漢音 pair (`CHITSU, TETSU`) was stored — added the missing `JICHI` and `DECHI`.

**Extensive genuine alias research**: four candidates individually verified and all added — 侄 (explicitly "the simplified and variant traditional form of 姪," per Wiktionary; confirmed no separate vault page), 妷, 㜼, and 𡥺 (all unqualified "variant form of 姪" with no ancient/archaic labeling or competing modern meaning).

korean_native (`조카`), `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 578) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[姪女]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[姪女]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 珀 (7057; 1160 characters remaining).

### 2026-08-12, iteration 1345 — [[characters/珀|珀]]

**`mc_id: 8262` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 白` confirmed correct** (形聲, semantic 玉 + phonetic 白, OC \*pʰraːɡ vs. phonetic's own \*braːɡ, an aspirated/voiced phonetic-series pair). **`boundedness: 5` double-checked and confirmed intentional, not a bug**: unusually low for a `cranberry`-tagged character with a compound `stand_in`, but cross-verified against its cranberry partner [[琥]], which shares the identical value — a deliberate convention for this specific bound-morpheme pair, not something to correct.

**Real cross-field bug found and fixed**: `japanese_native` was `ひゃく` — but ja.Wiktionary lists **no kun'yomi at all** for 珀; ひゃく is actually the 呉音 *on'yomi* (already correctly present in `japanese: [HAKU, HYAKU]`), duplicated into the wrong field. Corrected `japanese_native` to `ø` (no kun'yomi exists). `korean_native: 호박` double-checked against a plausible false-positive pattern (cf. [[祉]]'s prior-cycle bug where a copied-over reading was wrong) but confirmed genuinely correct here: the citing word [[琥珀]]'s own Notes explicitly document that both characters share this identical gloss as part of the cranberry relationship, not an error. Vietnamese (`phách`) and `joyo_level: 日本人名用漢字` (Jinmeiyō) both confirmed correct as-is.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[琥珀]] (注音 verified from its own page) to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

**Citing word page [[琥珀]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 卸 (char) (7058; 1159 characters remaining).

### 2026-08-12, iteration 1346 — [[characters/卸 (char)|卸]]

**`mc_id: 6746` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 午` confirmed correct**, per Wiktionary's unusual etymology: 卸 is an omission of 彳 from [[御]] ("to drive, to govern"), with 午 (the residual phonetic already embedded in 御 itself) "still giving the sound" — documented this genealogy explicitly in the Notes bullet rather than presenting it as an ordinary phono-semantic compound.

**Vietnamese narrowed on the strength of the citing word's own deep research**: stored `[dỡ, hằm, tá, xả]` — the citing word [[卸]]'s own Notes explicitly identify `tá` as the sole genuine Hán Việt reading (attested in tá trang 卸妝, tá hóa 卸貨) and call out all three other stored candidates as "unrelated to the reading itself," including `xả` despite it appearing on Wiktionary's own raw list — trusted this more specific citing-word verification over the raw dictionary entry and narrowed to `[tá]` alone.

**Alias research**: 缷 confirmed genuine (unqualified "variant form of 卸," modern/non-archaic usage) and added; 寫 was investigated and correctly excluded — despite Wiktionary confirming it as a historical variant-of-卸 sense, 寫's overwhelmingly dominant modern meaning is "to write" (an extremely common, unrelated character), the same shared-modern-meaning exclusion pattern as [[枝]]'s excluded 支 and [[亨]]'s excluded 享/烹.

korean_native (`풀`, matching the citing word's own documented native gloss 풀다), japanese (`SHA`), japanese_native (`おろ`, stem of おろす/おろし), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 70), and `hanmun_edu_level: 無` (confirmed absent from the Korean 1800-hanja list) all confirmed correct as-is. Filled blank `pos` → `事詞` on the character page, and **also fixed the same bug on the citing word page**: [[卸]]'s own `pos: 動詞` used a category (動詞, "verb") that doesn't exist in this vault's grammar taxonomy at all — corrected to `事詞`, matching the character page.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[卸]]. No Chengyu hits; no derived characters.

**Citing word page [[卸]] had the recurring `../characters/` broken-relative-path bug** — fixed, alongside the `pos` fix above.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 姨 (7059; 1158 characters remaining).

### 2026-08-12, iteration 1347 — [[characters/姨|姨]]

**`mc_id: 5557` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 夷` confirmed correct** (形聲, semantic 女 + phonetic 夷, exact OC and MC match on both sides, `*lil` / `j, iɪ`). **Genuine variant alias added**: 𫰆, independently verified as the "second-round simplified form of 姨" per Wiktionary's own Etymology 2 (a separate, obsolete personal-name-only Etymology 1 sense of the same glyph was not what qualified it — the simplification relationship is what matters here).

**Real cross-reading bug found and fixed**: `japanese_native` was stored as `いもうと` ("younger sister," 妹 — an entirely unrelated word) while the actual attested kun'yomi for 姨 is おば ("aunt"), directly matching `english`/`korean_native`; corrected to `おば`. Vietnamese (`[di, dì]`), korean_native (`이모`, itself the genuine standard Korean word for maternal aunt), and japanese (`I`, the single attested on'yomi) all confirmed correct as-is. Filled blank `joyo_level` → `表外字` (confirmed via ja.Wiktionary) and blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[姨母]]. No Chengyu hits; no derived characters.

**Citing word page [[姨母]] had a blank `pos` field and no `## Notes` section at all** — filled `pos: 名詞` and added the standard compositional gloss bullet, flagging it as the stand-in for [[姨]].

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 淀 (7060; 1157 characters remaining).

### 2026-08-12, iteration 1348 — [[characters/淀|淀]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy (not present in `CC 0000`–`CC 3000`). **`graphemic_classification: 定` confirmed correct** (形聲, semantic 氵 + phonetic 定, OC \*dɯːns vs. phonetic's own \*deːŋs, a plausible codas-matching pair). **`aliases: 澱` confirmed correct** (simplified/traditional pair, same asymmetric-primary-form pattern as [[国]]/國 and [[枢 (char)|枢]]/樞).

**Real wrong-sense bug found and fixed**: `english` was `[swampy]` — neither a real Wiktionary definition (which gives "shallow lake" as a noun, not an adjective) nor the operative Dan'a'yo sense; the character's own `stand_in`, [[沈淀]], and `korean_native` (`앙금`, "sediment/dregs," already correctly matching the operative sense) all point to the "sediment, to settle/precipitate" meaning documented on the alias 澱's own primary definitions — corrected `english` to `[sediment, precipitate, shallow lake]`.

Vietnamese (`điện`), japanese (`[TEN, DEN]`), japanese_native (`よど`, stem of よどむ, "to stagnate/settle" — already correctly matching the sediment sense despite the wrong `english`), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[沈淀]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[沈淀]] had the same stale "swampy" mis-gloss embedded in its own compositional Notes bullet**, plus the recurring `../characters/` broken-relative-path bug — both fixed (the word's own separate prose already correctly described the character's meaning as "sediment, settled matter," making the inline gloss the only stale spot).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 珊 (7061; 1156 characters remaining).

### 2026-08-12, iteration 1349 — [[characters/珊|珊]]

**`mc_id: 5183` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 册` investigated after an apparent conflict and confirmed correct**: the citing word [[珊瑚]]'s own prose claimed 珊's phonetic is "刪," which briefly looked like it might expose a character-page bug (刪's own MC `ʃ/ɣan` is in fact a much closer match to 珊's stored `s/ɑn` than 册's `t͡ʃʰ/ɣɛk`) — but zh.Wiktionary's own explicit glyph-origin breakdown (⿰𤣩册/冊) directly confirms 玉+册/冊 as 珊's actual composition, with a genuinely loose, unmotivated phonetic connection (OC \*slaːn vs. \*sʰreːɡ) rather than a clean match. Concluded the *citing word's* prose contained the error, not the character field — corrected [[珊瑚]]'s prose from "刪" to "册/冊" instead of touching the character page.

Vietnamese (`san`), korean_native (`산호`, the compound coral word doubling as the gloss — same pattern as [[珀]]'s cranberry pair), japanese (`SAN`), japanese_native (`さんち`, confirmed as a genuine kun'yomi despite one source's fetch initially seeming to omit it), and `joyo_level: 日本人名用漢字` (Jinmeiyō) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`. Confirmed the `cranberry` tag's transitivity holds ([[瑚]] shares the identical `stand_in: 珊瑚`).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format, folding in the transliteration-origin nuance from the citing word's own research. **`## Words`**: promoted the stray [[珊瑚]] mention into the properly-tagged reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[珊瑚]] had the factual phonetic-component error described above, plus the recurring `../characters/` broken-relative-path bug** — both fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 殆 (7062; 1155 characters remaining).

### 2026-08-12, iteration 1350 — [[characters/殆|殆]]

**`mc_id: 1154` verified correct as-is** (`CC 1000.md` line 163). **`graphemic_classification: 台` confirmed correct**, despite neither en- nor zh-Wiktionary giving an explicit glyph-origin breakdown for 殆 itself — confirmed via an exact MC match against [[台 (char)|台]]'s own stored reading (`d/ʌi` = `d/ʌi`) and a close OC match (`*l'ɯːʔ` vs. `*lɯ`).

**`japanese` expanded**: ja.Wiktionary lists 呉音 だい(DAI) and 漢音 たい(TAI); only `TAI` was stored — added the missing `DAI`. Vietnamese (`đãi`), korean_native (`거의`, "almost" — matching the "nearly" sense), japanese_native (`あやうい`, matching the "danger" sense, one of six attested kun'yomi), `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 656) all confirmed correct as-is. Filled blank `hsk_level` → `無` (confirmed absent from Wiktionary's HSK data) and blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[危殆]]. No Chengyu hits; no derived characters.

**Citing word page [[危殆]] had a duplicated `## Etymology` section** (the identical heading and bullet appeared twice, once before and once after `## Notes`) — removed the redundant trailing copy; also fixed the recurring `../characters/` broken-relative-path bug (three occurrences across both Etymology instances).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 咳 (7064; 1154 characters remaining).

### 2026-08-12, iteration 1351 — [[characters/咳|咳]]

**Real `mc_id` off-by-one bug found and fixed** (the seventh confirmed instance this session): stored `mc_id: 3370` points to a different character (`CC 3000.md` line 387 = 閹); 咳's true rank is **3371** (line 388), corrected. **`graphemic_classification: 亥` confirmed correct** (形聲, semantic 口 + phonetic 亥, exact MC match `ɣ/ʌi` on both sides, cross-verified against [[亥]]'s own stored MC, same phonetic-series relationship established on [[劾]] earlier this session).

**Real cross-reading bug found and fixed**: 咳 is homographic across (at least) four Mandarin pronunciations — ké/kài "to cough" (matching the stored `cantonese: kat1`, `japanese_native: せ` stem of せき, and `english: cough`), hāi (an interjection of sorrow/surprise), hái (variant of 孩/閡), and a Cantonese-only kak1 — but the stored `mandarin: hāi` named the *wrong* pronunciation, the interjection sense, contradicting every other field on the page; corrected to `ké`, matching the operative cough sense.

**Vietnamese narrowed**: stored `[cay, gay, gây, hãy, hỡi, khái]` included two items (`gay`, `gây`) absent from Wiktionary's own list for this sense — narrowed to `[cay, hãy, hỡi, khái]`, all four independently confirmed. **`japanese` expanded significantly**: ja.Wiktionary lists three 呉音 (ガイ, ケ, ゲ) and one 漢音 (カイ) plus a duplicate 慣用音 ガイ; only `GAI` was stored — added `KE`, `GE`, `KAI`. Filled blank `korean_native` → `기침` (confirmed via ko.Wiktionary's own 훈) and blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: promoted the stray [[咳漱]] mention into the properly-tagged reflexive stand-in. One Chengyu false positive excluded ([[弱不禁風]] merely mentions 咳嗽 in an illustrative example sentence); no derived characters.

**Citing word page [[咳漱]] updated**: fixed the recurring `../characters/` broken-relative-path bug, and filled its own previously-honestly-blank `vietnamese` field (`khái thấu`) now that `khái` is independently confirmed on Wiktionary directly rather than resting on the earlier conflicting search results — updated the word's own explanatory note to reflect this resolution rather than leaving a now-stale "left blank" justification.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 扁 (7065; 1153 characters remaining).

### 2026-08-12, iteration 1352 — [[characters/扁|扁]]

**Real `mc_id` off-by-one bug found and fixed** (the eighth confirmed instance this session): stored `mc_id: 1921` points to a different character (`CC 1000.md` line 962 = 肌); 扁's true rank is **1922** (line 963), corrected. **`graphemic_classification: 會意` confirmed correct** (戶 "door" + 冊 "bamboo tablets," already documented in the pre-existing Notes prose, now folded into the standard bullet format with its OC reconstruction added).

**Vietnamese expanded**: stored `[biển, bên, bẽn, thiên]` was missing `biên`, a genuine third Hán Việt reading confirmed on Wiktionary's own labeled Hán Việt/Nôm split — added, reordered with the three Hán Việt readings first. **Real typo bug found and fixed**: `japanese: [HEN, HAN]` — `HAN` does not correspond to any attested reading (both 呉音 and 漢音 are ヘン/HEN); removed.

korean_native (`납작할`), japanese_native (`ひらたい`), and `joyo_level: 表外字` all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`. **Genuine variant alias added**: 𡈯, independently verified as an unqualified "variant form of 扁" with no ancient/archaic labeling; a second candidate, 𡲜, returned a 404.

Rebuilt `## Notes` (a non-standard "Derived Characters" plain-text label sitting where a proper heading should be, a floating unlinked-CC-name-line pair, and only one derived character listed inline) to the standard 4-bullet format. **`### Derived Characters` substantially expanded**: a systematic check for `graphemic_classification: 扁` turned up five more citing characters beyond the one already inline — [[偏 (char)|偏]], [[篇 (char)|篇]], [[遍 (char)|遍]], [[騙 (char)|騙]], and [[編]] — all confirmed via exact field match and added alongside the pre-existing [[蝙]] (whose ruby tag had no 注音 filled in — corrected). No Chengyu hits.

**Citing word page [[扁平]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 軌 (char) (7066; 1152 characters remaining).

### 2026-08-12, iteration 1353 — [[characters/軌 (char)|軌]]

**Real `mc_id` off-by-one bug found and fixed** (the ninth confirmed instance this session): stored `mc_id: 1608` points to a different character (`CC 1000.md` line 637 = 匪); 軌's true rank is **1609** (line 638), corrected. **`graphemic_classification: 九` confirmed correct**, but the pre-existing Notes bullet prose had the semantic/phonetic roles swapped and corrupted — it claimed 九 was the *semantic* component with an empty gloss and left the phonetic component as a broken empty wikilink `[[]]`. Confirmed via Wiktionary's own compound template that 車 ("vehicle") is semantic and 九 is phonetic (OC \*kuʔ, already correctly present in the corrupted text) — rewrote the bullet with the roles corrected and both links properly filled.

**Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite ja.Wiktionary listing two genuine kun'yomi, わだち ("wheel track") and みち ("road/path") — set to `わだち`, the more precise match for "rut/track." Vietnamese (`[quĩ, quẫy, quỹ]`, matching Wiktionary's set exactly, quĩ/quỹ being orthographic-reform variants of the same reading), korean_native (`바큇자국`, "wheel track"), japanese (`KI`), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 170), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 83) all confirmed correct as-is.

**A dangling factual fragment preserved and properly re-homed**: the pre-existing Notes had a standalone, non-standard line "Added to the Korean HS list in 2000" — verified as factually accurate (軌 is among 44 characters added in the Korean basic-hanja list's December 2000 revision) and folded into the standard levels bullet as a parenthetical, rather than discarding a true fact just because of its non-standard original placement. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[軌]] to a Words section that didn't exist at all. No Chengyu hits; no derived characters.

**Citing word page [[軌]] had the recurring `vietnamese: null` corruption** — fixed to `quỹ`; its empty `## Notes` under a wrong-level heading was also filled with the standard gloss bullet.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 弧 (7067; 1151 characters remaining).

### 2026-08-12, iteration 1354 — [[characters/弧|弧]]

**Real `mc_id` off-by-one bug found and fixed** (the tenth confirmed instance this session): stored `mc_id: 2641` points to a different character (`CC 2000.md` line 670 = 甸); 弧's true rank is **2642** (line 671), corrected. **`graphemic_classification: 瓜` confirmed correct** (形聲, semantic 弓 + phonetic 瓜, OC \*ɡʷlaː vs. phonetic's own \*kʷraː, a voiced/voiceless labiovelar-with-liquid pair).

**`japanese` expanded**: ja.Wiktionary lists 呉音 ゴ(GO) and 漢音 コ(KO); only `KO` was stored — added the missing `GO`. **`japanese_native: ø` double-checked and confirmed correct, not a bug**: ja.Wiktionary explicitly lists no kun'yomi at all for 弧 — an earlier Wiktionary fetch's mention of a "kiyumi" kun reading turned out to be spurious/unconfirmed on direct inspection. `joyo_level: 高等` also double-checked against a source calling 弧 plain "Jōyō" and confirmed consistent, not conflicting — 高等 means "Jōyō but taught in secondary school" (the character was added in the 2010 Jōyō expansion), not "non-Jōyō," the same clarification already established on [[苛]] and [[呪]] earlier this session.

Vietnamese (`hồ`) and korean_native (`활`, "bow," matching the primary sense) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: promoted the stray [[弧線]] mention into the properly-tagged reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[弧線]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 耶 (char) (7068; 1150 characters remaining).

### 2026-08-12, iteration 1355 — [[characters/耶 (char)|耶]]

**Real `mc_id` off-by-one bug found and fixed** (the eleventh confirmed instance this session): stored `mc_id: 1817` points to a different character (`CC 1000.md` line 854 = 騰); 耶's true rank is **1818** (line 855), corrected. **`graphemic_classification: 牙` investigated in depth and confirmed correct, but for an indirect reason**: Wiktionary describes 耶's own glyph origin as "a corruption of 邪," not a fresh phono-semantic compound with 牙 directly (zh-Wiktionary confirms the literal components are 耳+阝-like, not 耳+牙) — but 邪 *itself* is 阝/邑 (semantic) + 牙 (phonetic), and 耶 inherited that same phonetic identity when it graphically replaced 邪's 阝 with 耳. Documented this genealogy honestly in the Notes bullet (the same "inherited phonetic identity via a related character" pattern established on [[呪]] earlier this session) rather than presenting it as a literal 耳+牙 compound.

**Real typo bug found and fixed**: `japanese: [YA, JA]` — `JA` does not correspond to any attested reading (both 呉音 and 漢音 are ヤ/YA per ja.Wiktionary); removed. **Vietnamese expanded**: stored `[gia]` was missing `da`, confirmed on Wiktionary's own reading list — added.

**`english` cleaned up**: stored `["yes?  mm?"]` was a single garbled phrase with a double space, not matching either of Wiktionary's actual senses — corrected to `[questioning particle, "yeah" (interjection)]`, matching Wiktionary's Etymology 1 (particle) and Etymology 3 (interjection) definitions. korean_native (`어조사`, "grammatical particle"), japanese_native (`か`, the sole attested kun'yomi), `joyo_level: 日本人名用漢字` (Jinmeiyō), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 428) all confirmed correct as-is. Filled blank `pos` → `感詞` — the taxonomy's own definition of this category ("can be SFP or stand alone as a complete utterance") matches 耶's documented dual behavior (sentence-final particle + standalone interjection) exactly.

Rebuilt `## Notes` (a non-standard "Derived Characters" plain heading appearing before any proper Notes content, two bare floating unlinked CC-name lines) to the standard 4-bullet format. **`### Derived Characters` expanded**: a systematic check for `graphemic_classification: 耶` turned up a third citing character, [[揶]] ("ridicule"), beyond the two already listed ([[爺]], [[椰]]) — added; also fixed broken `/characters/`-absolute-style links to the vault's standard relative form. **`## Words`**: added the missing reflexive stand-in [[耶]]. Four Chengyu false positives excluded (all apparently Biblical-themed chengyu mentioning 耶穌 "Jesus" in prose, none citing 耶 in their own `characters:` field).

**Citing word page [[耶]] updated to match**: same `english` cleanup, filled a previously-blank `vietnamese` with the character's own confirmed `gia`, and added a missing `## Notes` section.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 柵 (char) (7069; 1149 characters remaining).

### 2026-08-12, iteration 1356 — [[characters/柵 (char)|柵]]

**`mc_id: 6246` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 册` confirmed correct** (形聲, semantic 木 + phonetic 冊/册, exact OC match `*sʰreːɡ` on both sides — the same phonetic component already established this session on [[珊]]). **`mandarin: shān` double-checked against several homographic alternatives** (zhà, shàn, shā, shi are all also attested for this exact "fence" sense) and confirmed as one of the genuinely valid readings, not an error.

**`japanese` significantly expanded**: ja.Wiktionary lists two 呉音 (シャク, セン) and two 漢音 (サク, サン); only the 漢音 pair (`SAKU, SAN`) was stored — added the missing `SHAKU` and `SEN`. `joyo_level: 高等` confirmed correct (added to Jōyō in 2010, already listed on [Jōyō - Kōtō] line 375). Filled blank `hsk_level` → `無` (confirmed absent from Wiktionary's HSK data) and blank `pos` → `名詞`.

**Genuine variant alias added**: 𣑭, independently verified as an unqualified "variant form of 柵" with no ancient/archaic labeling, alongside the already-correct simplified-form alias 栅.

Vietnamese (`sách`), korean_native (`울타리`, "fence"), and japanese_native (`しがら`, stem of しがらみ) all confirmed correct as-is. Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[柵]]. No Chengyu hits; no derived characters.

**Citing word page [[柵]] had three gaps**: a blank `vietnamese` (filled with the character's own confirmed `sách`), no `pos`, and no `## Notes` section — all filled/added.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 峨 (7070; 1148 characters remaining).

### 2026-08-12, iteration 1357 — [[characters/峨|峨]]

**Real `mc_id` off-by-one bug found and fixed** (the twelfth confirmed instance this session): stored `mc_id: 3620` points to a different character (`CC 3000.md` line 649 = 彩); 峨's true rank is **3621** (line 650), corrected. **`graphemic_classification: 我` confirmed correct** (形聲, semantic 山 + phonetic 我, exact MC match and near-exact OC match `*ŋaːl`/`*ŋaːlʔ`). **Genuine variant alias added**: 峩, independently verified as an unqualified "variant form of 峨" with no ancient/archaic labeling.

**Missing reflexive stand-in found and added**: the character's own `stand_in: 峨峨` field pointed to a real, existing word page ([[峨峨]]), but the `## Words` section only listed the unrelated compound [[魏峨]] — added the missing entry. Vietnamese (`nga`), korean_native (`높을`), japanese (`GA`), japanese_native (`けわ`, one of three attested kun stems), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word [[魏峨]]'s own stored `pos`.

Rebuilt `## Notes` (wrong heading level, misplaced after the Words section, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. No Chengyu hits; no derived characters.

**Citing word page [[魏峨]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 弯 (7071; 1147 characters remaining).

### 2026-08-12, iteration 1358 — [[characters/弯|弯]]

**`mc_id: 4748` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range; also confirmed absent from all four lists directly). **`graphemic_classification: 䜌` confirmed correct** (形聲, semantic 弓 + phonetic 䜌 — pageless in this vault — OC \*qroːn vs. the donor's own \*b·roːn, a rime-matching series). **`aliases: 彎` confirmed correct** (simplified/traditional pair, same asymmetric-primary-form pattern as [[国]]/國, [[枢 (char)|枢]]/樞, [[洩]]/泄).

**Real malformed-YAML bug found and fixed**: `japanese_native` was written as a broken mixed scalar-then-list fragment (`ひ` followed by an orphaned `- ひく` list item with no parent key) — cleaned up to the single stem value `ひ` (matching ja.Wiktionary's sole kun'yomi ひく, "to bend"). **`japanese` expanded**: ja.Wiktionary lists 呉音 エン(EN) and 漢音 ワン(WAN); only `WAN` was stored — added the missing `EN`.

Vietnamese (`[loan, thoăn]`), korean_native (`굽을`, "to bend"), and `joyo_level: 表外字` all confirmed correct as-is. Rebuilt `## Notes` (a non-standard "Derived Characters" heading preceding any real Notes content, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`### Derived Characters`**: the existing [[湾]] entry had no ruby/注音/gloss formatting — fixed to match the standard format. **`## Words`**: added the missing reflexive stand-in [[弯曲]] to a Words section that didn't exist at all.

**Citing word page [[弯曲]] had three real bugs**: a leading-space typo in `korean: " 만곡"` (fixed to `만곡`), and a self-referential alias — the word's own `aliases:` list included "弯曲," its own title (removed, keeping the genuine variant `灣曲`).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 拷 (7072; 1146 characters remaining).

### 2026-08-12, iteration 1359 — [[characters/拷|拷]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy (not present in `CC 0000`–`CC 3000`). **`graphemic_classification: 考` confirmed correct with an exact match on every axis**: exact MC (`kʰ/ɑu`) and exact OC (`*kʰluːʔ`) against 考's own stored values — Wiktionary notes 拷 was formed specifically to replace an earlier plain use of 考 itself for "to interrogate," explaining the unusually tight phonetic identity; documented this genealogy in the Notes bullet.

**Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite ja.Wiktionary listing a genuine kun'yomi, うつ ("to hit") — set to `う`, the stem, matching the "beat, flog" sense. Vietnamese (`[khảo, khỉu]`), korean_native (`칠`, "to beat"), japanese (`[GOU, KOU]`), and `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 339) all confirmed correct as-is. **Missing `aliases:` key added** (blank — no genuine variant forms found on Wiktionary, but the key itself was absent from frontmatter entirely rather than present-and-blank as the schema expects). Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[拷問]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[拷問]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 迥 (char) (7074; 1145 characters remaining).

### 2026-08-12, iteration 1360 — [[characters/迥 (char)|迥]]

**`mc_id: 5049` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range, confirmed absent from all four lists directly). **`graphemic_classification: 冋` confirmed correct with an exact OC match** (`*ɡʷeːŋʔ` on both sides, pageless phonetic donor, cross-verified via zh.Wiktionary's component breakdown 辵+冋).

**Extensive alias research across four candidates, two added and two excluded on different grounds**: 㢠 confirmed genuine (unqualified "variant form of 迥," no archaic label) and added; 䢛 confirmed genuine ("non-classical form of 迥," the same non-committal-but-clean wording already accepted for [[炒]]'s 㶤 earlier this session) and added; 逈 excluded as "recorded in historical dictionaries as an unorthodox form" — treated as effectively an archaic/reference-only form rather than a live variant, consistent with this session's ancient-form exclusion discipline; 泂 excluded because it carries its own distinct primary meaning ("deep and vast, of water") under a separate etymology, the same competing-modern-meaning trap as [[亨]]'s excluded 享/烹.

**Vietnamese expanded**: stored `[huếnh, quánh, quýnh]` was missing `huýnh`, confirmed on Wiktionary's own reading list — added. Filled three blank fields: `joyo_level` → `表外字` (confirmed via ja.Wiktionary), `hsk_level` → `無` (confirmed absent from Wiktionary's HSK data), and `pos` → `性詞`. korean_native (`멀`, "far"), japanese (`[KEI, GYOU]`), and japanese_native (`はるか`, one of two attested kun) all confirmed correct as-is.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[迥]]. No Chengyu hits; no derived characters.

**Citing word page [[迥]] had the recurring `vietnamese: null` corruption** — fixed to `huýnh`; its empty `## Notes` under a wrong-level heading was also filled with the standard gloss bullet.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 剌 (7075; 1144 characters remaining).

### 2026-08-12, iteration 1361 — [[characters/剌|剌]]

**Real `mc_id` off-by-one bug found and fixed** (the thirteenth confirmed instance this session): stored `mc_id: 2710` points to a different character (`CC 2000.md` line 743 = 弭); 剌's true rank is **2711** (line 744), corrected. **`graphemic_classification: 柬` investigated and confirmed correct, but for an unusual reason**: Wiktionary's etymology shows 剌's glyph is originally 禾+口+刀 ("to harvest cereal"), only later *stylized* on bronze inscriptions into a shape resembling 柬+刀 — 柬's own MC (`k/ɣɛn`) doesn't match 剌's stored MC (`l/ɑt`) at all, confirming this is a graphic resemblance from stylization rather than a genuine phonetic relationship. Documented this history honestly in the Notes bullet rather than presenting a fabricated phono-semantic 形聲 breakdown.

**`japanese` expanded**: ja.Wiktionary lists 呉音 ラチ(RACHI) and 漢音 ラツ(RATSU); only `RATSU` was stored — added the missing `RACHI`. Filled blank `joyo_level` → `表外字` (confirmed via ja.Wiktionary) and blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Vietnamese (`[lạp, lạt]`), korean_native (`발랄할`, matching the compound-specific "lively" sense already used elsewhere in the vault), and japanese_native (`もと`, stem of もとる, matching the character's own core "to violate" sense — a different sense from the operative "lively" one, but a genuine reading, not a bug) all confirmed correct/reasonable as-is.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **New `### Derived Characters` section added**: a systematic check for `graphemic_classification: 剌` turned up three citing characters — [[辣 (char)|辣]], [[喇]], [[頼]] — all confirmed via exact field match and added. No Chengyu hits.

**Citing word page [[発剌]] had the recurring `../characters/` broken-relative-path bug** — fixed; otherwise an exceptionally well-researched pre-existing page (deep prose on the 溌/撥/潑 alias family and a Mandarin/Cantonese reading divergence specific to this compound) left untouched.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 洒 (char) (7076; 1143 characters remaining).

### 2026-08-12, iteration 1362 — [[characters/洒 (char)|洒]]

**Real `mc_id` off-by-one bug found and fixed** (the fourteenth confirmed instance this session): stored `mc_id: 2914` points to a different character (`CC 2000.md` line 955 = 磨). Unlike the simple off-by-one pattern seen elsewhere, this page's own alias 灑 *also* appears separately in the CC corpus (line 910, rank 2873) — but per the established precedent from [[妬]]/妒 (where both variants are tracked as genuinely distinct corpus entries), the correct value is 洒's *own* entry, not 灑's — confirmed at rank **2915** (line 956) and corrected.

**`graphemic_classification: 麗` investigated in depth and confirmed correct, but for a genealogical reason**: 洒's own direct phonetic (for its *other* senses, cuǐ/xiǎn/sǎ "I") is actually 西, not 麗 — but the vault's operative "sprinkle" sense is specifically 洒 functioning as 灑's simplified form, and 灑 itself is 水+麗 (confirmed via Wiktionary's own compound template for 灑, exact OC match). Documented this sense-specific inherited-identity relationship explicitly in the Notes bullet — the same pattern established on [[呪]] (inheriting from 祝) and [[耶]] (inheriting from 邪) earlier this session.

**Real cross-sense bug found and fixed**: `japanese_native` was `あら` (stem of あらう, "to wash") — but ja.Wiktionary's actual kun'yomi for 灑 is そそぐ ("to pour/sprinkle"), directly matching the operative sense; あらう instead belongs to 洒's separate archaic "wash" sense (a variant of 洗, explicitly documented as a *different* sense with its own distinct Korean reading 세, versus this page's 쇄). Corrected to `そそ`. **`japanese` expanded significantly**: ja.Wiktionary lists two 呉音 (シャ, セ) and two 漢音 (サ, サイ) for 灑; only `SAI` and `SHA` were stored — added `SE` and `SA`.

**Vietnamese reconciled across conflicting Wiktionary data**: the page carries both a sense-specific Nôm sub-list for the "refers to 灑" etymology (`rởi, rưới, sái, tưới`) and a broader character-wide Hán Nôm line covering all senses combined (`sái, tẩy, thối, rải, rảy, rưới, tưới, rẩy, vẩy`) — cross-referenced both, added the missing sense-specific `rởi`, and removed two items only relevant to *other* senses: `tẩy` (belongs to the "wash" sense) and `thối` (unrelated noise, no attested connection to any sense of 洒). Filled blank `korean_native` → `뿌릴` (no dictionary source gave a native gloss for this specific reading, so composed one matching "to sprinkle," documented as such rather than presented as sourced).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[洒]]. **Derived-character false positive investigated and correctly excluded**: [[晒 (char)|晒]] also stores `graphemic_classification: 麗`, but that makes it a *sibling* independently built on 麗 — not a character derived from 洒 itself (whose own field likewise just points to 麗) — so it does not belong in 洒's own Derived Characters section. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 哄 (7077; 1142 characters remaining).

### 2026-08-12, iteration 1363 — [[characters/哄|哄]]

**`mc_id: 9195` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range, confirmed absent from all four lists directly). **`graphemic_classification: 共` confirmed correct** (形聲, semantic 口 + phonetic 共, OC \*ɡloːŋs vs. phonetic's own \*ɡloŋs, a close match).

**Extensive alias research across four Wiktionary-listed variant candidates, one added and three excluded on different grounds**: 鬨 confirmed genuine (traditional/simplified pair, no competing meaning) and added; 嚇 excluded for a hugely dominant, unrelated modern meaning ("to scare/frighten," extremely common independently); 烘 excluded for its own well-documented dominant meaning ("to bake/roast/dry by heat"); 閧 excluded as "an unorthodox character simplified from 鬨" — one derivational step too indirect and explicitly non-standard, the same discipline applied to [[迥]]'s excluded 逈 last cycle.

**`japanese` expanded**: ja.Wiktionary lists two 呉音 (ク, グ) and one 漢音 (コウ); only `KOU` was stored — added `KU` and `GU`. `japanese_native: ø` double-checked and confirmed correct, not a bug — ja.Wiktionary directly confirms no kun'yomi exists (an earlier, less specific fetch's mention of こゑ/たぶらかす turned out to belong to a different sense not carried by this character in Japanese). **Vietnamese narrowed**: removed `hóng` (a common, unrelated modern word — "to follow news/gossip" — absent from Wiktionary's own list for this character). Filled blank `joyo_level` → `表外字` and blank `pos` → `事詞`. korean_native (`떠들썩할`, "boisterous/noisy") confirmed correct.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[哄笑]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[哄笑]] had the same non-taxonomy `pos: 動詞` bug found on [[卸]] a few cycles ago** — corrected to `事詞`; also fixed the recurring `../characters/` broken-relative-path bug.

**Mid-cycle: user requested the cron interval driving this loop be changed from 10 to 15 minutes** — old job (`975099f7`) deleted, new job (`15363c3b`, `7,22,37,52 * * * *`) created with the same standing prompt.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 俄 (7078; 1141 characters remaining).

### 2026-08-12, iteration 1364 — [[characters/俄|俄]]

**`mc_id: 2864` verified correct as-is** (`CC 2000.md` line 901). **`graphemic_classification: 我` confirmed correct** (形聲, semantic 人 + phonetic 我, OC \*ŋaːl vs. phonetic's own \*ŋaːlʔ, an exact match to [[峨]]'s own phonetic relationship, confirmed two cycles ago). No variant forms listed on Wiktionary for this character; `aliases:` correctly left blank.

Vietnamese (`nga`), korean_native (`아까`, "just now/a moment ago" — a plausible temporal match for "suddenly, very soon"), japanese (`GA`), japanese_native (`にわか`, matching both the "sudden" sense and the citing word [[俄雨]]'s own direct Japanese parallel にわか雨), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `副用名詞` (adverbial noun), matching the citing word [[俄然]]'s own stored `pos` — a less common taxonomy category than usual, cross-checked against the vault's grammar reference to confirm it's a genuine class (able to serve as the frame via zero-derivation), not a typo.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[俄然]] and promoted the stray [[俄雨]] mention into a proper ruby entry. No Chengyu hits; no derived characters.

**Both citing word pages ([[俄然]], [[俄雨]]) had the recurring `../characters/` broken-relative-path bug** — fixed on both.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 津 (7079; 1140 characters remaining).

### 2026-08-12, iteration 1365 — [[characters/津|津]]

**`mc_id: 1501` verified correct as-is** (`CC 1000.md` line 526). **`graphemic_classification: 聿` investigated and confirmed correct, but for a subtle reason worth documenting**: Wiktionary's own etymology states 津's phonetic component only *visually resembles* 聿 — it's actually a simplification of 盡 (per Ji Xusheng 2014), a claim corroborated by checking 聿's own attested OC (\*b·lud, from [[筆 (char)|筆]]'s Notes) against 津's own OC (\*ʔslin) — a poor match, consistent with the "resemblance, not identity" finding. Documented this honestly in the Notes bullet rather than presenting a misleadingly clean 形聲 breakdown; 聿 itself is pageless in this vault, so left as bare text rather than a broken wikilink.

**Real wrong-sense bug found and fixed**: `english` included `tsunami`, but no Wiktionary sense of 津 itself means "tsunami" — that gloss belongs entirely to the compound [[津波]] (literally "harbor-wave," a specifically Japanese coinage), not to 津 alone. Corrected to the character's own genuine senses: `[ferry crossing, ford, haven]` (the "haven" sense specifically supporting the 津波 compound's own component gloss).

Vietnamese (`[lọt, lụt, tân]`, an undifferentiated Hán Nôm list with no further split available), korean_native (`나루`, "ferry/ford" — matching the genuine core sense, distinct from the character's own English-field bug), japanese (`SHIN`), japanese_native (`つ`, the kun'yomi meaning "harbor/inlet," directly supporting 津波's own compositional breakdown), and `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 524) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (misplaced after the Words section, wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[津波]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[津波]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 按 (7080; 1139 characters remaining).

### 2026-08-12, iteration 1366 — [[characters/按|按]]

**`mc_id: 1375` verified correct as-is** (`CC 1000.md` line 392). **`graphemic_classification: 安` confirmed correct** (形聲, semantic 手 + phonetic 安, exact OC and MC match on both sides, `*qaːns`/`*qaːn`) — Wiktionary explicitly notes 安 was chosen specifically for its "at ease" sense to motivate the extended meaning "to restrain, to push down," documented in the Notes bullet. **No derived-character false positives added**: [[案]], [[晏]], [[鞍]] all also cite `安` as their own phonetic — they are siblings sharing the same phonetic parent, not characters derived from 按 itself, the same distinction established on [[洒 (char)|洒]]/[[晒 (char)|晒]] last cycle.

**`english` cleaned up**: stored `["put hands on"]` was an awkward single paraphrase — replaced with `[press, push down, restrain]`, matching Wiktionary's actual primary definitions more precisely. Vietnamese (`[án, ướn, ấn]`), korean_native (`누를`, "to press"), japanese (`AN`), japanese_native (`おさ`, stem of おさえる, "to press down"), and `joyo_level: 日本人名用漢字` (Jinmeiyō) all confirmed correct as-is. Filled blank `pos` → `事詞` on both the character page and the citing word page (which had the same blank).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[按摩]]. One Chengyu false positive excluded ([[造人像形]] merely quotes 按著 in prose, not in its `characters:` field); no derived characters.

**Citing word page [[按摩]] had no `## Notes` section at all** — added the standard compositional gloss bullet; its second component, 摩, turned out to be entirely pageless in this vault, so linked as bare text rather than a broken wikilink.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 俐 (7081; 1138 characters remaining).

### 2026-08-12, iteration 1367 — [[characters/俐|俐]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy (not present in `CC 0000`–`CC 3000`). **`graphemic_classification: 利` confirmed correct** (形聲, semantic 人 + phonetic 利, exact MC match `l/iɪ` on both sides, cross-verified via zh.Wiktionary's own component-series listing).

**Alias investigated in unusual depth given ambiguous phrasing**: `aliases: [悧]` looked at first like it might repeat the [[洩]]/渫 and [[呪]]/雎 pattern (a word-level substitution character mistaken for a true character-level variant) — en.Wiktionary describes 悧 only as "used in 怜悧, alternative form of 伶俐," never explicitly "variant form of 俐," and zh.Wiktionary lists it merely as a phonetic-series sibling of 利 (alongside 唎, 猁, 浰, etc.), not an explicit variant of 俐. However, unlike the false-alias cases found earlier, 悧 genuinely has **no other meaning or usage anywhere** — its sole documented role is standing in for 俐 within that one compound, a real (if narrowly-attested) one-to-one graphic substitution. Kept the alias, but noted the reasoning for future reference in case new evidence emerges.

Vietnamese (`[lời, lợi]`), korean_native (`똑똑할`, "clever"), japanese (`RI`), japanese_native (`かしこ`, stem of かしこい), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `性詞` on both the character page and the citing word page (which had the recurring `../characters/` broken-relative-path bug — fixed).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[伶俐]] (confirmed the `cranberry` tag's transitivity holds — [[伶]] shares the identical `stand_in: 伶俐`). No Chengyu hits; no derived characters (checked several 利-phonetic-series siblings, all confirmed to cite 利 directly rather than 俐, so none belong here).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 捌 (char) (7082; 1137 characters remaining).

### 2026-08-12, iteration 1368 — [[characters/捌 (char)|捌]]

**`mc_id: 8402` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 別` confirmed correct** (形聲, semantic 手 + phonetic 別, OC \*preːd/\*praːd vs. phonetic's own \*pred, a close match).

**Significant missing-sense bug found and fixed**: `english` was `[disentangle, sell well]`, entirely omitting 捌's single most well-known real-world use — the formal financial numeral form of 八 ("eight"), used on checks, contracts, and official documents throughout the Sinosphere specifically to prevent fraudulent alteration (alongside 壹貳參肆伍陸柒玖拾). Added `eight (formal financial numeral)` as the first-listed sense and documented the numeral-security convention explicitly in the Notes bullet.

**Real Japanese-reading bug found and fixed**: `japanese: [HATSU, HACHI, BETSU]` included `BETSU`, which does not correspond to any attested on'yomi of 捌 per direct ja.Wiktionary lookup (呉音 ハチ, 漢音 ハツ only) — likely bled over from the unrelated phonetic component 別 itself; removed. **Vietnamese expanded**: stored `[bát, bít, bắt, bịt]` was missing two of Wiktionary's six listed readings (`xốc`, `biết`) — added both.

korean_native (`깨뜨릴`, "to break/smash," matching the "disentangle" sense) and `joyo_level: 表外字` (confirmed via ja.Wiktionary) both confirmed correct as-is. Filled blank `pos` → `事詞` on both the character page and the citing word page (reasoning: the operative Dan'a'yo sense per `stand_in`/`english` is the verb-like "to break apart / to sell well" business sense, not the numeral, so an eventive category fits better than a bare noun).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[捌]]. No Chengyu hits; no derived characters.

**Citing word page [[捌]] updated to match**: same `english` cleanup, filled the previously-missing `pos`, and added a missing `## Notes` section (its own `vietnamese` field was deliberately left blank — no reliable source ties the business "sell well" sense to a specific Vietnamese word, so left unfilled rather than guessed).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 恕 (7083; 1136 characters remaining).

### 2026-08-12, iteration 1369 — [[characters/恕|恕]]

**Real `mc_id` off-by-one bug found and fixed** (the fifteenth confirmed instance this session): stored `mc_id: 2362` points to a different character (`CC 2000.md` line 379 = 誕); 恕's true rank is **2363** (line 380), corrected. **`graphemic_classification: 如` confirmed correct** (形聲, phonetic 如 + semantic 心, exact OC match `*njas` on both sides). **Alias candidate 㣽 investigated and correctly excluded**: explicitly labeled "ancient form of 恕" by Wiktionary, consistent with this session's ancient-form exclusion discipline.

**`english` cleaned up**: stored `[forgive, "show mercy about"]` (the second an awkward phrase) — replaced with `["to forgive, pardon", "to show consideration for others"]`, matching Wiktionary's actual two core senses precisely.

Vietnamese (`thứ`), korean_native (`용서할`, "to forgive"), japanese (`[JO, SHO]`), japanese_native (`ゆる`, stem of ゆるす, "to forgive"), and `joyo_level: 日本人名用漢字` (Jinmeiyō) all confirmed correct as-is. Filled blank `pos` → `事詞` on the character page.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[容恕]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[容恕]] had the same non-taxonomy `pos: 動詞` bug found on [[卸]] and [[哄笑]] earlier this session** (a third instance of this exact pattern) — corrected to `事詞`; also fixed the recurring `../characters/` broken-relative-path bug (two occurrences).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 匿 (7086; 1135 characters remaining).

### 2026-08-12, iteration 1370 — [[characters/匿|匿]]

**`mc_id: 1303` verified correct as-is** (`CC 1000.md` line 320). **`graphemic_classification: 若` confirmed correct** (形聲, semantic 匸 + phonetic 若, OC \*nɯɡ vs. phonetic's own \*njaɡ, a plausible nasal-initial/velar-coda match). No genuine variant forms found; `aliases:` correctly left blank (the only "variant form" mentioned by Wiktionary, 慝, belongs to a wholly separate secondary pronunciation/etymology, not this character's primary sense).

**Vietnamese reordered, all four confirmed genuine**: cross-checked Wiktionary's own labeled Hán Việt/Nôm split — `nặc` is the sole Hán Việt reading (also independently attested as Nôm), with `nắc, nác, nước` as additional Nôm forms; reordered with the Hán Việt reading first rather than removing anything, since all four are directly attested. **`japanese` expanded significantly**: ja.Wiktionary-derived data lists 呉音 にょく(NYOKU), 漢音 じょく(JOKU), and 慣用音 とく(TOKU); only `TOKU` was stored — added the two missing readings.

korean_native (`숨길`, "to hide"), japanese_native (`かくま`, stem of かくまう, "to harbor/hide someone"), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 786), and `hsk_level: 無` all confirmed correct as-is. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[隠匿]] as the reflexive stand-in. Two Chengyu false positives excluded ([[禍延子孫]] and [[塩地光世]] both merely mention 匿 in illustrative prose, not in their `characters:` fields); no derived characters.

**Citing word page [[隠匿]] had the recurring `../characters/` broken-relative-path bug** (three occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 浬 (char) (7087; 1134 characters remaining).

### 2026-08-12, iteration 1371 — [[characters/浬 (char)|浬]]

**`mc_id: 0` confirmed meaningful as-is**, and explicitly noted in the Notes bullet why: 浬 is a modern coinage (water + 里, translating "nautical mile" by pairing the water radical with the traditional land-distance unit), so absence from the Classical Chinese corpus is expected rather than a gap. **`graphemic_classification: 里` confirmed correct** (exact MC match `l/ɨ` on both sides). **No derived-character false positives added**: [[厘 (char)|厘]], [[狸 (char)|狸]], [[理]], [[埋]], [[裏]], [[鯉]] all separately cite 里 as their own phonetic — siblings, not descendants of 浬, the same distinction applied to [[洒 (char)|洒]]/[[晒 (char)|晒]] and [[按]]/[[案]] earlier this session.

**Vietnamese expanded**: stored `[rí]` was missing `lí`, confirmed on Wiktionary's own reading list — added. korean_native (`해리`, "nautical mile"), japanese (`RI`), japanese_native (`かいり`), and `joyo_level: 日本人名用漢字` (Jinmeiyō) all confirmed correct as-is (a katakana loan reading ノット, "knot," was left out of `japanese_native`, consistent with the vault's kun'yomi-in-hiragana-only convention). Filled blank `pos` → `名詞` on the character page.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[浬]]. No Chengyu hits; no derived characters.

**Citing word page [[浬]] had the recurring `vietnamese: null` corruption** (fixed to `rí`), a missing `pos` (filled), and no `## Notes` section (added).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 訊 (7088; 1133 characters remaining).

### 2026-08-12, iteration 1372 — [[characters/訊|訊]]

**Real `mc_id` off-by-one bug found and fixed** (the sixteenth confirmed instance this session): stored `mc_id: 2489` points to a different character (`CC 2000.md` line 510 = 奐); 訊's true rank is **2490** (line 511), corrected. **`graphemic_classification: 卂` confirmed correct** (形聲, semantic 言 + phonetic 卂 — pageless in this vault — exact OC match `*sins` on both sides). **No derived-character false positives added**: [[虱 (char)|虱]] and [[迅]] both separately cite 卂 as their own phonetic — siblings, not descendants of 訊.

**Extensive alias research across nine Wiktionary-listed variant candidates**: only one new genuine addition found — 訙 (unqualified "variant form of 訊," explicitly not labeled ancient, unlike its near-namesake 䛜 which *is* explicitly "ancient form of 訊" and was correctly excluded); 𧪄 excluded as it's actually a variant of an unrelated character, 記 (apparent Wiktionary cross-reference noise); 𧫓 excluded for having no stated variant relationship at all; five others (𧨼, 𠱖, 𠳱, 𡀚) returned 404. The pre-existing `讯` (simplified form) alias was already correct.

**`english` cleaned up**: stored `[hearing, trial]` was a narrower/looser paraphrase — replaced with `["to interrogate, question", "to inquire, ask", "message, news"]`, matching Wiktionary's actual primary senses precisely.

Vietnamese (`tấn`), korean_native (`물을`, "to ask"), japanese (`[JIN, SHIN, SHUN]`), japanese_native (`き`, stem of きく, "to ask"), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[審訊]]. No Chengyu hits; no derived characters.

**Citing word page [[審訊]] had the recurring `../characters/` broken-relative-path bug** — fixed; otherwise an exceptionally well-researched pre-existing page (deep prose on the compound's cross-linguistic legal terminology and Japanese absence) left untouched.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 挽 (7089; 1132 characters remaining).

### 2026-08-12, iteration 1373 — [[characters/挽|挽]]

**Real `mc_id` bug found and fixed, of the asymmetric-primary-form type**: stored `mc_id: 4686` doesn't correspond to any entry in `CC 0000`–`CC 3000` at all, but the page's own alias 輓 (confirmed via Wiktionary as the traditional form, 挽 being its simplifed counterpart) *does* appear at rank 3308 — corrected `mc_id` to 3308 and documented the reasoning ("as its traditional form 輓") in the MC-ordinal bullet, the same pattern as [[国]]/國, [[枢 (char)|枢]]/樞, [[洒 (char)|洒]]/灑, and [[妬]]/妒 earlier this session. **`graphemic_classification: 免` confirmed correct** (形聲, semantic 手 + phonetic 免, OC \*monʔ vs. phonetic's own \*mronʔ, a close match). **No derived-character false positives added**: [[勉 (char)|勉]], [[晩 (char)|晩]], [[冕]], [[娩]] all separately cite 免 as their own phonetic — siblings, not descendants of 挽.

**`english` expanded**: stored `[recover]` alone missed the character's more basic literal sense — replaced with `["to pull, draw back", "to save, recover, reverse"]`, matching Wiktionary's primary Etymology-1 definitions (pull/draw-back listed first, ahead of the extended "recover" sense that the citing word actually uses).

Vietnamese (`vãn`), korean_native (`당길`, "to pull"), japanese (`BAN`), japanese_native (`ひ`, stem of ひく, "to pull"), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[挽回]]. One Chengyu false positive excluded ([[孤軍奮闘]] merely quotes the idiom 力挽狂瀾 in illustrative prose, not in its `characters:` field); no derived characters.

**Citing word page [[挽回]] had no `## Notes` section at all** — added the standard compositional gloss bullet, catching along the way that its second component's filename has a "(char)" suffix (`回 (char).md`, not bare `回.md`).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 栓 (char) (7090; 1131 characters remaining).

### 2026-08-12, iteration 1374 — [[characters/栓 (char)|栓]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy (not present in `CC 0000`–`CC 3000`). **`graphemic_classification: 全` confirmed correct** (形聲, semantic 木 + phonetic 全, OC \*sroːn/\*sron vs. phonetic's own \*zlon, a plausible sibilant/liquid-initial match) — this page already had an unusually complete, correct Notes bullet pre-existing (just needed reformatting: a broken `[木](Radical%20075)` link with no `lookup/` prefix, and a stray Unicode curly-quote-style dash).

**`japanese_native: ø` double-checked and confirmed correct, not a bug**: ja.Wiktionary confirms no kun'yomi exists for 栓 (on'yomi-only character). **Vietnamese expanded**: stored `[thoen, thuyên]` was missing two of Wiktionary's four listed readings (`xuyên`, `thoan`) — added both, all four given as an undifferentiated Hán Nôm list with no further split available. `joyo_level: 高等` confirmed correct (listed on [Jōyō - Kōtō] line 586). Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (fixing the broken radical link and reformatting the existing correct phonetic bullet into the standard style) and added the three missing standard bullets (SKIP, MC-ordinal, levels) that had been omitted entirely. **`## Words`**: added the missing reflexive stand-in [[栓]]. No Chengyu hits; no derived characters.

**Citing word page [[栓]] had the recurring `vietnamese: null` corruption** (fixed to `thoen`), a missing `pos` (filled), and no `## Notes` section (added).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 俳 (7091; 1130 characters remaining).

### 2026-08-12, iteration 1375 — [[characters/俳|俳]]

**`mc_id: 4055` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range, confirmed absent from all four lists directly). **`graphemic_classification: 非` confirmed correct** (形聲, semantic 人 + phonetic 非, OC \*brɯːl vs. phonetic's own \*pɯl, a voiced/voiceless initial pair). **No derived-character false positives added**: nine sibling characters ([[扉 (char)|扉]], [[排 (char)|排]], [[悲 (char)|悲]], [[輩 (char)|輩]], [[啡]], [[斐]], [[徘]], [[緋]], [[菲]]) all separately cite 非 as their own phonetic.

**Vietnamese narrowed**: stored `[bài, bầy, bời]` contained two unrelated/unattested entries (`bầy` "flock/herd," `bời` unclear) alongside the single genuine Hán Việt reading; narrowed to `[bài]` alone, confirmed as the sole reading on Wiktionary's own labeled table. **Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite ja.Wiktionary listing a genuine kun'yomi, わざおぎ ("actor/performer") — filled. **`japanese` expanded**: ja.Wiktionary lists 呉音 べ(BE) and 漢音 ハイ(HAI); only `HAI` was stored — added the missing `BE`.

korean_native (`배우`, "actor"), and `joyo_level: "6"` (confirmed on [Jōyō - Kyōiku] line 857 — a Kyōiku/elementary-taught kanji despite the character page's own `grade_level: 先進` being a wholly separate Dan'a'yo-internal scale, correctly routed independently per the precedent established on [[枝]]) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: promoted the stray [[俳優]] mention into the properly-tagged reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[俳優]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 閃 (7092; 1129 characters remaining).

### 2026-08-12, iteration 1376 — [[characters/閃|閃]]

**`mc_id: 7956` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range, confirmed absent from all four lists directly). **`graphemic_classification: 會意` confirmed correct** (associative compound, 門 "gate" + 人 "person" — originally a person darting through a gate). **`aliases: 闪` confirmed correct** (simplified form).

**Two parallel cross-sense bugs found and fixed in the same cycle**: both `korean_native` (`엿볼`, "to peek/spy") and `japanese_native` (`うかが`, stem of うかがう, "to peep/watch furtively") were documenting an entirely unattested "peeking" sense — no Wiktionary definition of 閃 relates to peeking or spying at all. Corrected both to match the character's actual operative "flash" sense: `korean_native` → `번쩍일` (matching ko.Wiktionary's own 훈 "빛나다"/to shine, refined to the more precise "to flash/glint" verb already used in the stored `english`), `japanese_native` → `ひらめ` (stem of ひらめく, "to flash/sparkle," ja.Wiktionary's actual sole kun'yomi). This is now the fourth-plus instance this session of the "wrong-sense native gloss" pattern, but the first where it struck two independent language fields simultaneously on the same character — possibly indicating both were copied from a shared bad source at once.

Vietnamese (`thiểm`) and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) both confirmed correct as-is. Filled blank `pos` → `名詞`, matching both citing words' own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[閃光]] (the character's actual `stand_in` target, which had been entirely absent) alongside the already-present [[閃電]]. No Chengyu hits; no derived characters.

**Both citing word pages ([[閃光]], [[閃電]]) had the recurring `../characters/` broken-relative-path bug** — fixed on both.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 胴 (7093; 1128 characters remaining).

### 2026-08-12, iteration 1377 — [[characters/胴|胴]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy. **`graphemic_classification: 同` confirmed correct** (形聲, semantic 肉 + phonetic 同, exact OC and MC match on both sides, `*doːŋs`/`*doːŋ` vs. `d/uŋ`). **No derived-character false positives added**: five sibling characters ([[筒 (char)|筒]], [[銅 (char)|銅]], [[桐]], [[洞]], [[用]]) all separately cite 同 as their own phonetic.

**Real Vietnamese wrong-reading bug found and fixed**: stored `động` — but that's actually 動's own reading ("to move"), an easy confusable homophone-adjacent character; the real Hán Việt reading of 胴, confirmed via a Sino-Vietnamese dictionary (Thiều Chửu), is `đỗng`. Corrected. That same dictionary source independently corroborates both of 胴's two Chinese senses ("thân người"/torso and "ruột già"/large intestine), which gave confidence that the stored `korean_native: 큰창자` ("large intestine") — while documenting the character's secondary literary sense rather than the operative "torso" sense used by the citing word — is a genuine, deliberately-chosen field rather than a bug like [[閃]]'s prior "peek" cross-sense error (which had zero textual support anywhere); left as-is rather than force-changed.

**`japanese` expanded**: ja-source lists 呉音 ズウ(ZUU), 漢音 トウ(TOU), and 慣用音 ドウ(DOU, the modern standard reading); only `TOU` and `DOU` were stored — added the missing `ZUU`. `japanese_native: ø` confirmed correct (no kun'yomi exists) and `joyo_level: 高等` confirmed correct (listed on [Jōyō - Kōtō] line 783, added in the 2010 Jōyō expansion). Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[胴体]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[胴体]] had the recurring `../characters/` broken-relative-path bug** (two occurrences) — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 娩 (7094; 1127 characters remaining).

### 2026-08-12, iteration 1378 — [[characters/娩|娩]]

**`mc_id: 7024` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 免` confirmed correct** (形聲, semantic 女 + phonetic 免, exact OC match `*mronʔ` on both sides). **Alias candidate 免 investigated and correctly not added** despite Wiktionary confirming it as an "(obsolete) alternative form of 娩" — 免 carries its own overwhelmingly dominant modern meaning ("to avoid, exempt") and its own vault page, the same shared-ancient-origin-trap exclusion pattern as [[亨]]'s excluded 享/烹.

**Real Japanese-reading bug found and fixed**: `japanese: [BEN, HAN]` — `HAN` does not correspond to any attested reading (real readings are 呉音 マン/メン, 漢音 バン/ベン); corrected to `[MAN, MEN, BAN, BEN]`, adding the two missing 呉音 readings and fixing the apparent typo. **Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite a genuine kun'yomi existing, うむ ("to give birth") — directly matching the operative sense; filled.

**Vietnamese double-checked against a Sino-Vietnamese dictionary** (Thiều Chửu, via hvdic) beyond Wiktionary's single-reading listing — confirmed both stored readings (`miễn`, matching the attested compound 分娩 = phân miễn; `vãn`, the character's other "graceful, gentle" sense) are genuine; a third dictionary-only reading (`phiền`, tied to yet another sense) was not added since it belongs to an unrelated etymology not otherwise represented on this page.

korean_native (`낳을`, "to give birth") and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) both confirmed correct as-is. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[分娩]] as the reflexive stand-in. No Chengyu hits; no derived characters (four sibling characters — [[勉 (char)|勉]], [[晩 (char)|晩]], [[冕]], [[挽]] — all separately cite 免 as their own phonetic, correctly excluded).

**Citing word page [[分娩]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 俵 (7095; 1126 characters remaining).

### 2026-08-12, iteration 1379 — [[characters/俵|俵]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy. **`graphemic_classification: 表` confirmed correct** (形聲, semantic 人 + phonetic 表, OC \*praws vs. phonetic's own \*prawʔ, a very close match). **`stand_in: 名専字` confirmed appropriate** — this character has no standalone Dan'a'yo vocabulary use, restricted to proper names (the Japanese surname Tawara).

**Real cross-field bug found and fixed**: `korean_native` was `뚱뚱할` ("to be fat/plump") — completely unrelated to any sense of this character. Confirmed the real ko.Wiktionary 훈 is "나누어 주다" ("to distribute"), matching the character's actual core Chinese sense; corrected to `나눌`. **`english` corrected/expanded**: stored `[bag]` alone was a decontextualized fragment of the Japanese-specific extension (たわら, "straw bag/sack," from the rice-bale sense 米俵) — replaced with `["to divide, distribute", "straw bag (Japanese)"]`, capturing both the original Chinese sense and the Japanese extension, and documented the surname connection in the Notes bullet.

**Existing alias removed after investigation**: `脿` was pre-existing but, on inspection, Wiktionary explicitly labels it "obsolete form of 俵" (one of three characters it interchangeably substitutes for) — applying this session's established "explicit archaic/obsolete label → exclude" discipline (cf. [[巫]]'s excluded 𢍮, [[迥]]'s excluded 逈, [[乖]]'s excluded 𠁰) retroactively to a pre-existing entry for consistency, since a fresh check today would not have added it.

Vietnamese (`[biếu, biểu]`), japanese (`HYOU`), japanese_native (`たわら`), `joyo_level: "6"` (confirmed on [Jōyō - Kyōiku] line 858), and `hanmun_edu_level: 名` all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format; no `## Words` section applicable given the `名専字` stand-in. No Chengyu hits; no derived characters.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 夷 (7096; 1125 characters remaining).

### 2026-08-12, iteration 1380 — [[characters/夷|夷]]

**`mc_id: 355` verified correct as-is** (`CC 0000.md` line 370). **`graphemic_classification: 象形` confirmed correct** against the vault's own pre-established [List of 象形] membership, despite Wiktionary technically classifying the glyph origin as an associative compound (矢+弓 "to shoot," later reanalyzed as 大+弓) — trusted the vault's own categorization over the more granular external label, the same precedent established on [[乖]] earlier this session.

**Real bad-alias bug found and fixed**: `aliases: [貊]` — checked directly and found 貊 is a wholly distinct, unrelated character (an ancient tribal name, ancestor of the Korean Yemaek people, also meaning "leopard") with **no documented variant relationship to 夷 at all**; the two were evidently conflated purely on thematic grounds (both relate to "non-Han peoples"). Removed.

**Vietnamese cleaned up via an independent Sino-Vietnamese dictionary** (hvdic): confirmed the primary Hán Việt reading is `di` (not previously first-listed) and the Nôm set is `[dai, di, gì, rợ]`; removed `dì` (a likely diacritic typo of `di`, unattested anywhere) and reordered with the Hán Việt reading first.

**Missing reflexive stand-in discovered**: the character's own `stand_in: 東夷` field pointed to a real, existing word page that had never been added to `## Words` at all — the pre-existing entries only covered the unrelated compounds [[蛮夷]] and [[攘夷]]. Added [[東夷]] as the properly-tagged stand-in. **Cascading bug found on [[蛮夷]]**: its own Notes prose falsely claimed "蛮夷 is the stand-in word for 夷," directly contradicting the character's own authoritative `stand_in` field — removed the stale claim.

korean_native (`오랑캐`, "barbarian"), japanese_native (`えびす`, one of four attested kun stems, matching the operative sense), and `joyo_level`/`hanmun_edu_level` (both confirmed, Jinmeiyō and [Korean HS] line 501 respectively) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level entirely absent — no Notes heading existed at all, just a stray Words section followed by floating CC-name lines then a Chengyu section) to the standard 4-bullet format, and converted several `[text](../words/...)`/`[text](../chengyu/...)` bracket-links throughout the character page itself to proper `[[wikilink]]` format with corrected relative paths. **New `### Derived Characters` section added**: [[姨]] and [[胰]], both confirmed via exact `graphemic_classification: 夷` match — notably, [[姨]] was independently perfected earlier this very session and its own OC/MC values were cross-referenced back then, closing the loop.

**Citing word pages [[蛮夷]], [[攘夷]], [[東夷]] all had the recurring `../characters/` broken-relative-path bug** — fixed on all three.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 桁 (char) (7097; 1124 characters remaining).

### 2026-08-12, iteration 1381 — [[characters/桁 (char)|桁]]

**`mc_id: 7135` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 行` confirmed correct** (形聲, semantic 木 + phonetic 行, exact MC match `ɣ/ɑŋ` on both sides). **No derived-character false positives added**: [[荇]] and [[衡]] both separately cite 行 as their own phonetic.

**Vietnamese reconciled across two conflicting sources**: Wiktionary lists only `hành`, but an independent Sino-Vietnamese dictionary (hvdic) additionally confirms `hàng` (plus a third, `hãng`, not added since only one other source mentioned it) — kept `hành` and `hàng` (both cross-source-confirmed) and dropped the pre-existing `hằng` (confirmed by neither source, likely noise). **`japanese` expanded**: ja.Wiktionary lists two 呉音 (ゴウ, ギョウ) and one 漢音 (コウ); only `KOU` was stored — added `GOU` and `GYOU`.

**Filled blank `korean_native`** with a compositional gloss (`들보`, "beam/rafter" — the standard Korean word for the operative sense) after confirming no hanja dictionary gives a direct native-gloss source for this character; documented as compositional rather than presented as sourced. `joyo_level: 高等` confirmed correct (added to Jōyō in 2010, listed on [Jōyō - Kōtō] line 270). Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[桁]]. No Chengyu hits; no derived characters.

**Citing word page [[桁]] had the recurring `vietnamese: null` corruption** (fixed to `hành`), a missing `pos` (filled), and no `## Notes` section (added).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 閻 (char) (7098; 1123 characters remaining).

### 2026-08-12, iteration 1382 — [[characters/閻 (char)|閻]]

**Real `graphemic_classification` bug found and fixed**: stored `陥` (a wholly different character, "to fall into," the Japanese shinjitai of 陷) — checked its own MC (`ɣ/ɣɛm`) against 閻's own MC (`j/iᴇm`) and found a poor match; zh.Wiktionary's own component-series page directly confirms the true phonetic donor is **臽** (pageless in this vault), whose own OC (`*ɡroːms`/`*kʰloːmʔ`) shares the -oːm/-om rime with 閻's own `*lom` — an irregular but genuine historical phonetic-series match, unlike 陥 which has no such connection at all. Corrected the field and documented the irregular-but-attested nature explicitly in the Notes bullet.

**Real `mc_id` off-by-one bug found and fixed** (the seventeenth confirmed instance this session): stored `mc_id: 2250` points to a different character (`CC 2000.md` line 263 = 鱗); 閻's true rank is **2251** (line 264), corrected.

**Extensive genuine alias research**: three new candidates individually verified and all added — 閆 (a modern divergent surname variant from cursive-script simplification, explicitly not archaic), 闫 (the official second-round-simplification form), and 𨳔 (an unqualified "variant form of 閻"); the pre-existing 阎 (simplified form) was already correct.

**Vietnamese narrowed**: stored `[diêm, dàm]` — only `diêm` is attested on Wiktionary's own Hán Nôm table; `dàm` had no support anywhere and was removed. **Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite genuine kun'yomi existing (ちまた, ひらく, すすめる) — filled with `ちまた` ("crossroads/village lane," directly matching the operative sense). Filled blank `joyo_level` → `表外字` and blank `pos` → `名詞`.

korean_native (`마을`, "village") and japanese (`[EN, SEN]`) both confirmed reasonable as-is. Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[閻]] as the reflexive stand-in. No Chengyu hits; no derived characters ([[諂 (char)|諂]] separately cites 臽 as its own phonetic — a sibling, not a descendant of 閻).

**Citing word page [[閻]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 哨 (7099; 1122 characters remaining).

### 2026-08-12, iteration 1383 — [[characters/哨|哨]]

**`mc_id: 5622` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 肖` confirmed correct** (形聲, semantic 口 + phonetic 肖, exact MC match `s/iᴇu` on both sides). **No derived-character false positives added**: nine sibling characters ([[削 (char)|削]], [[消 (char)|消]], [[稍 (char)|稍]], [[宵]], [[梢]], [[硝]], [[趙]], [[逍]], [[鞘]]) all separately cite 肖 as their own phonetic.

**Vietnamese expanded**: stored `[tiêu, toé, téo]` was missing `tiếu`, confirmed on Wiktionary's own Hán Nôm list — added, reordered to match Wiktionary's own listed order. **`japanese` expanded**: ja.Wiktionary lists 呉音 ショウ and 漢音 ショウ/ソウ; only `SHOU` was stored — added the missing `SOU`.

**Real typo bug found and fixed, appearing twice**: `english` contained the misspelling "sentinal" (should be "sentinel") — corrected on both the character page and the citing word page's own compositional gloss, and expanded with the character's other genuine senses (`to patrol`, `whistle`).

korean_native (`망볼`, "to keep watch"), japanese_native (`みはり`, "watchman"), and `joyo_level: 日本人名用漢字` (Jinmeiyō) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, a stray unformatted word-mention sitting where the Words section should be) to the standard 4-bullet format. **`## Words`**: promoted the stray [[哨兵]] mention into the properly-tagged reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[哨兵]] had the same "sentinal" typo plus the recurring `../characters/` broken-relative-path bug** — both fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 浩 (7100; 1121 characters remaining).

### 2026-08-12, iteration 1384 — [[characters/浩|浩]]

**Real `mc_id` off-by-one bug found and fixed** (the eighteenth confirmed instance this session): stored `mc_id: 2561` points to a different character (`CC 2000.md` line 586 = 紅); 浩's true rank is **2562** (line 587), corrected. **`graphemic_classification: 告` confirmed correct** (形聲, semantic 水 + phonetic 告, OC \*ɡuːʔ vs. phonetic's own \*kuːɡs, a close voiced/voiceless match). **No derived-character false positives added**: five sibling characters ([[皓]], [[造]], [[酷]], [[鵠]], [[靠]]) all separately cite 告 as their own phonetic.

**Extensive genuine alias research across five Wiktionary-listed candidates**: three added — 澔 (unqualified "variant form of 浩," no distinct meaning of its own), 㬶 ("same as 浩," no archaic label), and 㵆 ("same as 澔/浩... vast water flow," a minor secondary "radiance of gems" gloss not rising to a competing dominant meaning); one excluded — 灝, which does carry its own distinct primary modern meaning ("soy milk"), the same shared-modern-meaning trap as [[亨]]'s excluded 享/烹; one, 𤅆, returned a 404.

Vietnamese (`hạo`), korean_native (`넓을`, "to be broad/vast"), japanese (`KOU`), japanese_native (`おおき`, stem of おおきい, "big"), `joyo_level: 日本人名用漢字` (Jinmeiyō), and `hanmun_edu_level: 高等` (confirmed on [Korean HS]) all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[浩大]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[浩大]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 捏 (7101; 1120 characters remaining).

### 2026-08-12, iteration 1385 — [[characters/捏|捏]]

**Real `graphemic_classification` bug found and fixed**: stored `日` — but Wiktionary's own compound template explicitly names **涅** as the phonetic component (abbreviated in the modern glyph); confirmed decisively via an **exact OC match** between 捏 and 涅 (`*niːɡ` on both sides, also an exact MC match `n/et`) — 日 has no plausible phonetic connection at all and was likely extracted by mistake from within 涅's own visual structure. Corrected the field. **`mc_id: 0` confirmed meaningful as-is**.

**`japanese` expanded**: ja.Wiktionary lists two 呉音 (ネチ, ネツ) and one 漢音 (デツ); only `NECHI` and `DETSU` were stored, missing `NETSU` — added. **Genuine variant alias added**: 揑, independently verified as an unqualified "variant form of 捏" with no ancient/archaic labeling.

Vietnamese (`[nhét, niết, nát, nạt]`, matching Wiktionary's own undifferentiated Hán Nôm list exactly) and `joyo_level: 表外字` both confirmed correct as-is. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[捏造]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[捏造]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 套 (char) (7102; 1119 characters remaining).

### 2026-08-12, iteration 1386 — [[characters/套 (char)|套]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy. **`graphemic_classification: 會意` confirmed correct** (associative compound, 大 "big" + 镸 "long," per Wiktionary's own compound template). **Genuine variant aliases added**: 㚐 and 𡘷, both independently verified as unqualified "variant form of 套" with no ancient/archaic labeling; two other candidates (𡘂, 𰋛) returned 404.

Vietnamese (`[sáo, thạo]`), japanese (`TOU`, a single reading shared by both 呉音/漢音), japanese_native (`かさ`, stem of かさねる), and `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format, drawing on the citing word [[套]]'s own exceptionally rich pre-existing etymological research (the "long/big" → "covering" semantic shift, cross-linguistic fortunes across Vietnamese/Japanese/Korean) to write a substantive glyph-origin bullet rather than a bare component list. **`## Words`**: added the missing reflexive stand-in [[套]]. No Chengyu hits; no derived characters.

**Citing word page [[套]] had the recurring `../characters/` broken-relative-path bug** — fixed (a single occurrence; the page was otherwise left untouched given its already-excellent research quality).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 挫 (7103; 1118 characters remaining).

### 2026-08-12, iteration 1387 — [[characters/挫|挫]]

**Real `mc_id` off-by-one bug found and fixed** (the nineteenth confirmed instance this session): stored `mc_id: 2541` points to a different character (`CC 2000.md` line 566 = 貉); 挫's true rank is **2542** (line 567), corrected. **`graphemic_classification: 坐` confirmed correct** (形聲, semantic 手 + phonetic 坐, OC \*ʔsoːls vs. phonetic's own MC `d͡z/uɑ`, a close match).

**Vietnamese left deliberately unexpanded**: Wiktionary's own raw list balloons to nine near-duplicate orthographic-variant spellings (dọa/doạ, dóa/doá, tỏa/toả, thọa/thoạ, etc. — many pairs differing only in tone-mark placement convention, several redlinked/nonexistent) with no Hán Việt/Nôm split to filter by; kept the existing conservative three-item set (`doá, doạ, toả`) rather than importing what amounts to spelling-convention noise.

**`english` expanded**: stored `[failure, setback, frustration]` under-represented the character's more basic literal senses — replaced with `["to break, crush", "to frustrate, thwart", "setback, frustration"]`, matching Wiktionary's fuller definition list and the citing word's own etymological prose ("挫 to crush, collapse inward").

korean_native (`꺾을`, "to bend/break"), japanese (`[ZA, SA]`, both attested readings), japanese_native (`くじ`, stem of くじく/くじける), and `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 361) all confirmed correct as-is. Filled blank `pos` → `事詞`, matching the citing word's own stored `pos`.

Rebuilt `## Notes` (misplaced after the Words section, wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[挫折]] as the reflexive stand-in. One Chengyu false positive excluded ([[波乱万丈]] merely mentions 挫折 in an illustrative example sentence); no derived characters.

**Citing word page [[挫折]] had the recurring `../characters/` broken-relative-path bug** — fixed.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 畔 (char) (7104; 1117 characters remaining).

### 2026-08-12, iteration 1388 — [[characters/畔 (char)|畔]]

**`mc_id: 1364` verified correct as-is** (`CC 1000.md` line 381). **`graphemic_classification: 半` confirmed correct** (形聲, semantic 田 + phonetic 半, OC \*baːns vs. phonetic's own \*paːns, a voiced/voiceless match). **No derived-character false positives added**: five sibling characters ([[伴]], [[判]], [[拌]], [[絆]], [[胖]]) all separately cite 半 as their own phonetic.

**Real Vietnamese diacritic-typo bug found and fixed**: stored `bạn` (nặng tone) — but the true Hán Nôm reading, confirmed directly on Wiktionary, is `bản` (hỏi tone), a one-diacritic difference from an unrelated common word ("friend"). Corrected. **`japanese` expanded**: ja.Wiktionary lists 呉音 バン(BAN) and 漢音 ハン(HAN); only `HAN` was stored — added the missing `BAN`.

korean_native (`밭두둑`, "field ridge"), japanese_native (`あぜ`, "paddy ridge"), and `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 848) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[畔]]. No Chengyu hits; no derived characters.

**Citing word page [[畔]] had the recurring `vietnamese: null` corruption** (fixed to `bản`), a missing `pos` (filled), and no `## Notes` section (added).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 俸 (7105; 1116 characters remaining).

### 2026-08-12, iteration 1389 — [[characters/俸|俸]]

**`mc_id: 4287` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 奉` confirmed correct**, with a linguistically interesting genealogy documented in the Notes bullet: Wiktionary identifies 俸 as an "exopassive" morphological derivative of 奉 ("to offer, present"), literally "that which is received" — not just an arbitrary phono-semantic pairing but a direct grammatical derivation, explaining the close OC match (\*poːŋʔ/\*boŋs vs. \*boŋʔ). **No derived-character false positives added**: [[捧 (char)|捧]] and [[棒]] both separately cite 奉 as their own phonetic.

**Vietnamese expanded via a Hán Việt/Nôm cross-check**: stored `[bóng, bống, bổng, bỗng, phỗng, vụng]` was missing two of Wiktionary's eight listed Nôm readings (`bụng`, `vổng`) — added both, and reordered with the single Hán Việt reading (`bổng`) first. **Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite a genuine kun'yomi existing, ふち ("stipend") — filled. **`japanese` expanded**: ja.Wiktionary lists 呉音 ブ(BU) and 漢音 ホウ(HOU); only `HOU` was stored — added the missing `BU`.

korean_native (`녹`, "stipend"), and `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 939) both confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[俸給]] (the character's actual `stand_in` target) as the reflexive stand-in and reordered it ahead of [[俸祿]]. No Chengyu hits; no derived characters.

**Both citing word pages ([[俸給]], [[俸祿]]) had the recurring `../characters/` broken-relative-path bug** — fixed on both; [[俸給]] in particular was otherwise an exceptionally well-researched pre-existing page (deep prose on imperial bureaucratic pay systems and cross-linguistic register distinctions) left untouched.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 朕 (char) (7106; 1115 characters remaining).

### 2026-08-12, iteration 1390 — [[characters/朕 (char)|朕]]

**`mc_id: 815` verified correct as-is** (`CC 0000.md` line 845). **`graphemic_classification: 會意` confirmed correct** (oracle-bone associative compound, 舟 "boat" + two hands holding a rod-like object).

**Significant missing-reading bug found and fixed on both the character page and its citing word**: `vietnamese` on both pages listed only `chũm` (a genuine but secondary Nôm reading) while entirely omitting **`trẫm`** — the famous, overwhelmingly dominant Hán Việt reading for this exact "royal we" sense (a word well-known even outside linguistics circles from Vietnamese historical dramas). Confirmed via an independent Sino-Vietnamese dictionary and added to both pages, first in list order.

**Real cross-field bug found and fixed**: `japanese_native` was wrongly blanked to `ø` despite a genuine kun'yomi existing, われ ("I/me") — filled. **Real bug found and fixed on the Japanese lookup page itself**: [Jōyō - Kōtō]'s own entry for 朕 was a malformed bare `[[朕 (char)]]` wikilink instead of the standard `[label](path)` format used by every surrounding entry — corrected to match the surrounding pattern.

**Two additional bugs found and fixed on the citing word page** ([[朕]]): a `品詞: 副用名詞` field contradicting its own `pos: 代詞` (pronoun) — corrected to match, since 朕 functions as a personal pronoun per the vault's own grammar taxonomy; and a `japanese: ぢむ` value that doesn't correspond to any real Japanese reading of this character (likely a garbled attempt at the Dan'a'yo romanization "jum" rather than genuine Japanese) — corrected to `ちん`, the character's actual on'yomi used as a pronoun. Also added a missing `## Notes` section.

Filled blank `pos` → `代詞` on the character page, matching the citing word.

Rebuilt `## Notes` (a stray non-standard "V pronunciation" fragment, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **New `### Derived Characters` section added**: [[勝]], [[謄]], [[騰]], all confirmed via exact `graphemic_classification: 朕` match. **`## Words`**: added the missing reflexive stand-in [[朕]]. No Chengyu hits.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 倣 (7107; 1114 characters remaining).

### 2026-08-12, iteration 1391 — [[characters/倣|倣]]

**`mc_id: 5147` confirmed as a trusted long-tail value** (beyond this vault's `CC 0000`–`CC 3000` range). **`graphemic_classification: 放` confirmed correct** (形聲, semantic 人 + phonetic 放, exact OC and MC match `*pʰaŋʔ`/`f, ʉɐŋ` on both sides). **`aliases: 仿` confirmed correct and, unusually, the reverse of the vault's usual asymmetric-primary-form pattern**: here 倣 (not 仿) is the vault's chosen primary page despite Wiktionary treating 仿 as the "true" character and 倣 as its variant — 仿 itself is pageless in this vault, documented explicitly in the Notes bullet.

**Significant Vietnamese bug found and fixed**: stored `[phạng, phỏng, phổng, phỗng]` — since 倣 has no independent Vietnamese section of its own (confirmed directly), its readings must come from 仿; cross-checked two sources (Wiktionary + an independent Sino-Vietnamese dictionary) and found only `phỏng` among the stored four was genuinely attested — `phạng`, `phổng`, `phỗng` were unconfirmed noise. Replaced with the confirmed set `[phảng, phỏng, phẳng, phần]`.

korean_native (`본뜰`, "to imitate/model after"), japanese (`HOU`), japanese_native (`なら`, stem of ならう, "to imitate"), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 940), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 267) all confirmed correct as-is. Filled blank `pos` → `事詞` and blank `boundedness` → `90`, matching the citing word's own stored `pos` and the established pattern for two-character `stand_in` compounds respectively.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format, documenting the variant-of-仿 relationship explicitly. **`## Words`**: added the missing reflexive stand-in [[模倣]]. No Chengyu hits; no derived characters.

**Citing word page [[模倣]] had the recurring `../characters/` broken-relative-path bug** — fixed; its own blank `vietnamese` field was left as-is after confirming no source gives a Sino-Vietnamese equivalent for this specific compound.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 窄 (7108; 1113 characters remaining).

### 2026-08-12, iteration 1392 — [[characters/窄|窄]]

**`mc_id: 0` confirmed meaningful as-is** per checklist policy. **`graphemic_classification: 乍` confirmed correct** (形聲, semantic 穴 + phonetic 乍, OC \*ʔsraːɡ vs. phonetic's own \*zraːɡs, a plausible sibilant-initial/-aːɡ-rime match). **No derived-character false positives added**: six sibling characters ([[作 (char)|作]], [[昨 (char)|昨]], [[炸]], [[祚]], [[詐]], [[酢]]) all separately cite 乍 as their own phonetic.

**Real bad-alias bug found and fixed**: `aliases: [齪, 龊]` — checked directly and found 齪 (and its simplified form 龊) is a wholly distinct character with its own Mandarin reading (chuò, not zhǎi) and its own primary compound 齷齪 ("sordid, base") — Wiktionary's own glyph-origin/variant-forms sections for 窄 make zero mention of either character. The two were evidently conflated purely on a loosely overlapping "narrow/petty" gloss. Removed both.

**Vietnamese expanded**: stored `[trách]` was missing `trậc`, confirmed on Wiktionary's own Hán Nôm list — added. **`japanese` expanded**: ja.Wiktionary lists 呉音 しゃく(SHAKU) and 漢音 さく(SAKU); only `SAKU` was stored — added the missing `SHAKU`.

korean_native (`좁을`, "to be narrow"), japanese_native (`すぼ`, stem of すぼめる), `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed), and `pos: 性詞` (already correctly filled) all confirmed correct as-is.

Rebuilt `## Notes` (a non-standard "Components:" bullet, two bare floating unlinked CC-name lines, no other standard bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[狭窄]] as the reflexive stand-in. One Chengyu false positive excluded ([[多召少選]] merely mentions 窄 twice in illustrative Biblical-allusion prose, not in its `characters:` field); no derived characters.

**Citing word page [[狭窄]] had the same non-taxonomy `pos` bug found repeatedly this session**: `形容詞` ("adjective," a real linguistics term but not a category in this vault's own grammar system) — corrected to `性詞`, matching the character page's own already-correct value; also fixed the recurring `../characters/` broken-relative-path bug (three occurrences).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 逝 (7109; 1112 characters remaining).

### 2026-08-12, iteration 1393 — [[characters/逝|逝]]

**`mc_id: 2222` verified correct as-is** (`CC 2000.md` line 235). **`graphemic_classification: 折` confirmed correct despite a modern MC divergence** (逝's MC `ʑ/iᴇi` vs. 折's MC `t͡ɕ/iᴇt` look unrelated at first) — resolved by comparing their OC reconstructions instead: `*ɦljeds` vs. `*ʔljed` share the same core `-ljed` shape, confirming a genuine ancient phonetic relationship that later diverged, the same category of finding as [[俸]]'s exopassive-derivative genealogy last cycle. **No derived-character false positives added**: [[哲]] and [[誓]] both separately cite 折 as their own phonetic.

**Vietnamese expanded**: stored `[thể]` was missing `thệ`, confirmed on Wiktionary's own Hán Nôm list — added. **`japanese` corrected**: stored `[SEI, SETSU]` — cross-checked directly against ja.Wiktionary, which confirms only 呉音 ゼ(ZE) and 漢音 セイ(SEI); `SETSU` could not be independently confirmed on this more authoritative direct lookup and was replaced with the missing `ZE`.

korean_native (`갈`, "to go"), japanese_native (`い`, stem of いく), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 567), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 343) all confirmed correct as-is. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[逝去]]. One Chengyu false positive excluded ([[意気揚揚]] merely quotes 逝 in a poem passage, not in its `characters:` field); no derived characters.

**Citing word page [[逝去]] had the same non-taxonomy `pos` bug found repeatedly this session**: `実詞` (the taxonomy's top-level "Content Words" umbrella category, not a specific leaf category) — corrected to `事詞`; also had no `## Notes` section at all — added.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 鞠 (7110; 1111 characters remaining).

### 2026-08-12, iteration 1394 — [[characters/鞠|鞠]]

**Real `mc_id` off-by-one bug found and fixed** (the twentieth confirmed instance this session): stored `mc_id: 2653` points to a different character (`CC 2000.md` line 682 = 芍); 鞠's true rank is **2654** (line 683), corrected. **`graphemic_classification: 匊` confirmed correct**, but the pre-existing Notes prose had the semantic/phonetic roles reversed (said "phonetic 革 + semantic 匊" when it is actually semantic 革 ("leather") + phonetic 匊, OC \*kluɡ, a close match to 鞠's own \*kuɡ) — corrected in the rebuilt Notes bullet. Also documented that in the narrow "ferment, yeast" sense, 鞠 functions as an earlier written form of the separately-attested, pageless 麴, which has since become the dominant character for that specific sense.

**Malformed and incorrect `aliases` field found and fixed**: stored `aliases: "麴"` was both a plain YAML string rather than a list, and semantically wrong — 麴 has its own distinct dominant modern meaning ("yeast, leaven") rather than being a genuine Wiktionary-attested variant of 鞠, matching this session's established shared-ancient-origin/competing-modern-meaning exclusion pattern (cf. [[挽]]/[[娩]]'s 免, [[浩]]'s 灝, [[卸]]'s 寫). Removed. Investigated two genuine candidates individually: 踘, an unqualified "variant form of 鞠" per Wiktionary — added; 毩, explicitly labeled "ancient form of 鞠" — excluded per this session's ancient-form discipline.

**`japanese` corrected**: stored `[KIKU, KYOU]` — `KYOU` doesn't correspond to any attested reading; cross-checked directly against ja.Wiktionary, which confirms only 呉音 きく(KIKU) and 漢音 ぎく(GIKU) — replaced with the missing `GIKU`.

korean_native (`공`, historical "ball" sense), japanese_native (`まり`, "ball"), `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed), vietnamese (`cúc`, confirmed against an independent Sino-Vietnamese dictionary), and `hanmun_edu_level: 名` all confirmed correct as-is. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[鞠躬]]. No Chengyu hits; no derived characters (菊 (char) separately cites 匊 as its own phonetic — a sibling, not a descendant of 鞠).

**Citing word page [[鞠躬]] had the same non-taxonomy `pos` bug found repeatedly this session**: `動詞`/`品詞: 動詞` (a real linguistics term absent from this vault's own grammar taxonomy) — corrected to `事詞`/`事詞`; also fixed the recurring `../characters/` broken-relative-path bug.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 淑 (7111; 1110 characters remaining).

### 2026-08-12, iteration 1395 — [[characters/淑|淑]]

**`mc_id: 1989` verified correct as-is** (`CC 1000.md` line 1030). **`graphemic_classification: 叔` confirmed correct** (形聲, semantic 水 + phonetic 叔, OC \*ɦljɯwɢ vs. phonetic's own \*hljɯwɢ, a close match). **Alias candidate 俶 investigated and excluded**: Wiktionary labels it "original form of 淑," but 俶 carries its own distinct dominant classical senses ("first; initially," "to arrange," "suddenly") unrelated to 淑's "pure/virtuous" meaning — matching this session's shared-ancient-origin/competing-modern-meaning exclusion pattern (cf. [[鞠]]'s 麴, [[浩]]'s 灝). **Alias candidate 𭂑 investigated and excluded**: an extremely rare CJK Extension glyph with no independently retrievable Wiktionary entry, so its variant status could not be cross-verified.

**`japanese` expanded**: stored `[SHUKU]` was missing the 呉音 `JUKU`(じゅく); ja.Wiktionary confirms both 呉音 じゅく and 漢音 しゅく(Jōyō) — added.

korean_native (`맑을`, "to be clear/pure," matching [Korean MS] line 426), japanese_native (`しと`, stem of しとやか), vietnamese (`thục`, confirmed), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 454), `hsk_level: 無` (confirmed via [HSK No]), and `hanmun_edu_level: 中` (confirmed via [Korean MS]) all confirmed correct as-is. Filled blank `pos` → `性詞`, matching the citing word's own stored value.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[賢淑]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[賢淑]] had two bugs fixed**: the recurring `../characters/` broken-relative-path bug in its opening Notes bullet; and a missing stand-in note per [[AIOS/memory/feedback_standin_note|the standing convention]] — the page's extensive prose already discussed 淑's restriction to compounds but never stated the explicit reciprocal relationship, so appended "— stand-in for [[淑]], which cannot appear independently" to the opening bullet.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 斎 (7112; 1109 characters remaining).

### 2026-08-12, iteration 1396 — [[characters/斎|斎]]

**`mc_id: 2087` confirmed correct, tracked under the traditional alias form**: `CC 2000.md` line 92 records rank 2087 as [[齋]] (斎's own listed alias), the same asymmetric-primary-form pattern established on [[国]]/國, [[枢]]/樞, etc. — no fix needed. **`graphemic_classification: 齊` confirmed correct** (形聲, semantic [[示]] + phonetic 齊, OC \*ʔsriːl vs. phonetic's own \*zliːl/\*zliːls, a close match); 齊 itself is pageless under its own name in this vault, tracked as [[斉]]'s own alias — documented in the rebuilt Notes bullet. **Alias 夈 confirmed genuine**: independently verified as an unqualified "variant form of 齋" with no ancient/archaic labeling.

**Diacritic-typo bug found and fixed**: stored Vietnamese `chái` cross-checked against hvdic.thivien.net, which lists `trai` (Hán Việt) and `chay`/`chây`/`trai`/`trơi` (Nôm) — no `chái` anywhere; corrected to `chây`, the same category of finding as [[畔]]'s bạn→bản.

**`japanese` expanded**: stored `[SAI]` — direct ja.Wiktionary lookup confirms both 呉音 `SE`(セ) and 漢音 `SAI`(サイ, Jōyō); added the missing `SE`.

korean_native (`재계할`, "ritual purification," matching the operative sense), japanese_native (`い`, stem of いむ), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 367), `hsk_level: 無` (confirmed via [HSK No]), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅈ] line 25) all confirmed correct as-is. Filled blank `pos` → `事詞` and blank `boundedness` → `80`, matching the established pattern for bound characters requiring a two-character stand-in.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[斎戒]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[斎戒]] had two bugs fixed**: the same non-taxonomy `pos` bug found repeatedly this session (`動詞` → `事詞`); and the recurring `../characters/` broken-relative-path bug (two occurrences). Its existing stand-in note was already present and left unchanged.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 勒 (7113; 1108 characters remaining).

### 2026-08-12, iteration 1397 — [[characters/勒|勒]]

**`mc_id: 1755` verified correct as-is** (`CC 1000.md` line 788). **`graphemic_classification: 力` confirmed correct** (形聲, semantic 革 + phonetic 力, OC \*rɯːɡ vs. phonetic's own \*rɯɡ, an exact match). No genuine alias candidates: Wiktionary's other "variant" mentions (嘞 modal particle, 捩, a Northern Wu locative-marker sense) are unrelated homographic/dialectal borrowings with their own distinct meanings, not variants of the "bridle/rein in" sense — correctly left blank.

**Vietnamese contamination fixed**: stored `[lấc, lất, lật, lắc, lặc]`; cross-checked against hvdic.thivien.net, which confirms `lặc` (Hán Việt) and `lắc`/`lấc`/`lất` (Nôm) — `lật` is not attested anywhere for this character and was removed.

korean_native (`굴레`, "bridle/halter"), japanese (`ROKU`, both 呉音 and 漢音 per direct ja.Wiktionary lookup), japanese_native (`くつわ`, "bridle"), `hsk_level: 4` (confirmed on [Old HSK 4] line 2060), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㄹ] line 85) all confirmed correct as-is. Filled blank `pos` → `事詞`.

**Shared lookup page bug found and fixed**: [[Hyōgai]] (the lookup page for `joyo_level: 表外字`) was missing an entry for 勒 entirely — added `[[勒]]` to its "Checked" section.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[勒馬]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[勒馬]] had several bugs fixed**: the same non-taxonomy `pos` bug found repeatedly this session (`動詞` → `事詞`); the recurring `../characters/` broken-relative-path bug (three occurrences); and entirely missing `japanese`/`vietnamese` fields — filled compositionally from the constituent characters' own readings (`ろくば` from 勒's ROKU + [[馬 (char)]]'s BA; `lặc mã` from 勒's lặc + 馬's mã). Consolidated the two Notes bullets into one per the standard stand-in-note format.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 焉 (char) (7114; 1107 characters remaining).

### 2026-08-12, iteration 1398 — [[characters/焉 (char)|焉]]

**`mc_id: 109` verified correct as-is** (`CC 0000.md` line 117). **`graphemic_classification: 象形` confirmed correct**: 焉 originally depicted a yellow bird (per Wiktionary's own first definition, now obsolete), later borrowed 假借 for its sound to write a family of unrelated grammatical particles — the "ligature of 於是" theory some sources give describes the etymology of the *grammatical* usage, not the graph's own origin.

**Significant bad-alias bug found and fixed**: stored `aliases: [鄢, 嫣]` — both investigated directly and found to be phono-semantic *derivatives* citing 焉 as their phonetic component (鄢 = 阝 + phonetic 焉, "a place in Henan"; 嫣 = 女 + phonetic 焉, "beautiful"), each with its own wholly distinct meaning and neither ever labeled a variant of 焉 itself. Removed both from `aliases` and documented the true phonetic-derivative relationship in the rebuilt Notes bullet instead (both pageless in this vault, so no `### Derived Characters` section was warranted).

**Vietnamese expanded**: hvdic.thivien.net surfaces a secondary Hán Việt reading `diên` (alongside the primary `yên`) not present in the stored `[vờn, yên]` — added.

korean_native (`어찌`, "how/why"), japanese (`[EN, I]`), japanese_native (`いずく`, stem of いずくんぞ), `hsk_level: 無` (confirmed via [HSK No]), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 443) all confirmed correct as-is. Filled blank `pos` → `連接詞` (conjunction/linker, matching the "therefore" sense and the same leaf category used by [[故而]]/[[而]]/[[或]]).

**Shared lookup page bug found and fixed** (second consecutive cycle): [[Hyōgai]] was missing an entry for 焉 (char) — added.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing self-reference stand-in [[焉]] explicitly. No Chengyu hits (three prose-only false positives excluded: [[喜怒哀楽]], [[断章取義]], [[八紘一宇]], none of which cite 焉 in their `characters:` field); no derived characters.

**Citing word page [[焉]] (the disambiguated self-stand-in stub) had two bugs fixed**: the recurring `vietnamese: null` corruption — replaced with `yên` (confirmed as the primary Hán Việt reading via hvdic); and a missing `pos` field — filled `連接詞` to match. Its bare `# Notes` heading was left empty, matching the established convention for these single-character self-reference stub pages (cf. already-perfected [[岐]]).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 兜 (char) (7115; 1106 characters remaining).

### 2026-08-12, iteration 1399 — [[characters/兜 (char)|兜]]

**`mc_id: 3025` verified correct as-is** (`CC 3000.md` line 30). **Real `graphemic_classification` bug found and fixed**: stored `象形` (pictogram) — both English and Chinese Wiktionary explicitly classify 兜 as **會意** (ideogrammic compound: 𠑹 "cover" + 皃 "head" = "a helmet"), not a single pictographic depiction; corrected. **No genuine alias candidates**: of Wiktionary's four listed variants, 兠 is explicitly "ancient form of 兜" (excluded per this session's discipline), 㿡 is labeled "corrupted form" (訛體, treated the same as an ancient-form exclusion — not a legitimate active variant), and 𦋌/𤾆 are unverifiable rare CJK Extension glyphs with no retrievable Wiktionary entry (same unverifiable-exclusion category as [[淑]]'s 𭂑 last cycle).

**`japanese` expanded**: stored `[TOU]` was missing both 呉音 readings; direct ja.Wiktionary lookup confirms 呉音 `TSU`(ツ) and `TO`(ト) alongside 漢音 `TOU`(トウ) — added both missing readings.

korean_native (`투구`, "helmet"), japanese_native (`かぶと`, "helmet"), vietnamese (`đâu`, confirmed complete via hvdic), `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed on line 420), `hsk_level: 4` (confirmed on [Old HSK 4] line 870), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㄷ] line 43) all confirmed correct as-is. Filled blank `pos` → `名詞`, matching the citing word's own stored value.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format, documenting both pageless components (𠑹, 皃). **`## Words`**: tagged the existing self-reference stand-in [[兜]] explicitly. No Chengyu hits; no derived characters.

**Citing word page [[兜]] had two bugs fixed**: it had been perfected on 2026-07-26, before this cycle's discovery of the `graphemic_classification` error, and its own prose still asserted "兜 is 象形" — corrected to `會意 (𠑹 "cover" + 皃 "head")` to match; also fixed the recurring `../characters/` broken-relative-path bug. Its `date-last-perfect` stamp was left unchanged per the established convention for citing-page fixes made during another character's cycle.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 掠 (7116; 1105 characters remaining).

### 2026-08-12, iteration 1400 — [[characters/掠|掠]]

**`mc_id: 1806` verified correct as-is** (`CC 1000.md` line 843). **`graphemic_classification: 京` confirmed correct** (形聲, semantic 手 + phonetic 京, OC \*ɡraɡ vs. phonetic's own \*kraŋ, a loose but plausible match). **Extensive alias research**: of eight candidates surfaced across Wiktionary, four were genuine unqualified variants and added — 稤, 剠 (also separately a variant of 黥, but with no independent meaning of its own), 䅫, 㨼; four were excluded — 㔀 (only an "unorthodox form of 剠," too indirect a chain to count as a direct variant of 掠), 撂 (its own distinct dominant colloquial meaning "to put down, drop," matching the competing-modern-meaning exclusion pattern), and two unverifiable rare glyphs (𰔡, no retrievable entry).

**`japanese` expanded**: stored `[RYAKU, RYOU]` (both 漢音) was missing both 呉音 readings; direct ja.Wiktionary lookup confirms 呉音 `RAKU`(らく) and `ROU`(ろう) — added both.

korean_native (`노략질할`, "to plunder"), japanese_native (`かす`, stem of かすめる/かする/かすれる), vietnamese (`[lướt, lược, lựng]`, confirmed complete), `joyo_level: 日本人名用漢字` (Jinmeiyō, confirmed on line 118), `hsk_level: 3` (confirmed on [Old HSK 3] line 931), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 165) all confirmed correct as-is. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[掠奪]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[掠奪]] had several bugs fixed**: an entirely missing `vietnamese` field — filled `lược đoạt`, confirmed via hvdic.thivien.net; the recurring `../characters/` broken-relative-path bug; and a missing stand-in note per [[AIOS/memory/feedback_standin_note|the standing convention]] — consolidated the two prose Notes bullets into the standard single-bullet format with the stand-in clause appended.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 毫 (char) (7117; 1104 characters remaining).

### 2026-08-12, iteration 1401 — [[characters/毫 (char)|毫]]

**`mc_id: 2274` verified correct as-is** (`CC 2000.md` line 287). **`graphemic_classification: 高` confirmed correct** (形聲, semantic 毛 + phonetic 高, OC \*ɡaːw vs. phonetic's own \*kaːw, a close match). **Alias candidate 豪 investigated and excluded**: labeled an "alternative form of 毫" by Wiktionary, but 豪 has its own overwhelmingly dominant modern meaning ("heroic, grand, wealthy") and its own independent vault page ([[豪]]) — matching the competing-modern-meaning exclusion pattern, the clearest case yet since the candidate is itself a fully-fledged primary vault entry. **Alias candidate 𡨉 excluded**: unverifiable, no retrievable Wiktionary entry.

**Cross-sense native-gloss bug found and fixed**: stored `japanese_native: ごう` was simply a duplicate of the already-stored on'yomi `GOU`, not a genuine kun'yomi reading at all; direct ja.Wiktionary lookup lists four real kun readings (すこし, ふで, ほそげ, わずか) — corrected to `ほそげ` ("fine hair"), matching the character's own first-listed primary English sense, rather than `すこし`/`わずか` which correspond to the secondary "slightest amount" sense.

korean_native (`터럭`, "hair," confirmed on [Korean HS] line 722), vietnamese (`hào`, confirmed complete), `japanese: [KOU, GOU]` (both confirmed complete via direct ja.Wiktionary lookup — no missing readings this time), `joyo_level: 表外字` (confirmed listed on [Hyōgai] line 128), `hsk_level: 2` (confirmed on [Old HSK 2] line 491), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 722) all confirmed correct as-is. Also confirmed the `諺文: 핫` field is intentionally the Dan'a'yo syllable's own conlang hangul spelling (matching the syllable page [[ㄏㄚㄨ]]), not a copy of the real Sino-Korean reading `호` — a legitimate divergence, not a bug. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, one stray uncontextualized [[毫米]] bullet) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[毫]] alongside the existing [[毫米]]. No Chengyu hits (two prose-only false positives excluded: [[一目瞭然]], [[天衣無縫]]); no derived characters.

**Two citing word pages had bugs fixed**: [[毫]] (the disambiguated self-stand-in stub) had a blank `vietnamese` field (filled `hào`) and a missing `pos` field (filled `名詞`); [[毫米]] had a non-standard `## Etymology` heading (renamed to `## Notes`) and the recurring `../characters/` broken-relative-path bug (two occurrences).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 奚 (char) (7118; 1103 characters remaining).

### 2026-08-12, iteration 1402 — [[characters/奚 (char)|奚]]

**`mc_id: 954` verified correct as-is** (`CC 0000.md` line 987). **Real `graphemic_classification` bug found and fixed** (second consecutive cycle): stored `象形` — English Wiktionary explicitly classifies 奚 as **會意** (a hand grabbing a person by their braids, "servant, slave"), with the interrogative "how/why" sense arising via 假借 phonetic loan; corrected. **Alias candidate 㜎 investigated and excluded**: a phono-semantic derivative (女 + phonetic 奚, "female slave"/"timid"), not a variant of 奚 itself. **Two genuine derived characters found and added**: [[鶏 (char)|鶏]] and [[渓]] both separately cite `graphemic_classification: 奚` — a new `### Derived Characters` section was added (this character previously had none).

**`japanese` expanded**: stored `[KEI]` was missing the 呉音 reading; direct ja.Wiktionary lookup confirms 呉音 `GE`(ゲ) alongside 漢音 `KEI`(ケイ) — added. **Blank `joyo_level` filled** → `表外字`, confirmed via the same ja.Wiktionary lookup (explicitly labeled 表外漢字).

korean_native (`어찌`, "how/why"), japanese_native (`なんぞ`, "why/what," per direct ja.Wiktionary — trusted over en.Wiktionary's broader but less precise three-reading list), vietnamese (`hề`, confirmed complete via hvdic), `hsk_level: 無` (confirmed via [HSK No] line 286), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 702) all confirmed correct as-is. Filled blank `pos` → `代詞`, matching the citing word's own stored value.

**Shared lookup page bug found and fixed** (third consecutive cycle): [[Hyōgai]] was missing an entry for 奚 (char) — added.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing self-reference stand-in [[奚]] explicitly. No Chengyu hits.

**Citing word page [[奚]] (already perfected 2026-08-02) had two bugs fixed**: its rich prose still asserted "奚 is a 象形 character" — despite the same paragraph's own description ("a hand grabbing a person by a rope") actually matching 會意, not a true single pictogram; corrected the label to `會意` to match both the character page and the word's own prose content. Also fixed the recurring `../characters/` broken-relative-path bug. Its `date-last-perfect` stamp was left unchanged per the established convention for citing-page fixes made during another character's cycle.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 措 (7119; 1102 characters remaining).

### 2026-08-12, iteration 1403 — [[characters/措|措]]

**Real `mc_id` off-by-one bug found and fixed** (the twenty-first confirmed instance this session): stored `mc_id: 2309` points to a different character (`CC 2000.md` line 326 = 詹); 措's true rank is **2310** (line 327), corrected. **`graphemic_classification: 昔` confirmed correct** (形聲, semantic 手 + phonetic 昔, cognate with [[作 (char)|作]] in Old Chinese per Wiktionary). **Two alias candidates investigated and excluded**: 錯 (its own overwhelmingly dominant modern meaning "wrong, mistake," plus its own independent vault page [[錯]]) and 厝 (its own dominant living meaning "house" in Min dialects) — both matching the competing-modern-meaning exclusion pattern; the pre-existing `𢵄` alias was left as-is (already vetted, pageless, unverifiable independently but directly sourced from 措's own Wiktionary page).

**Vietnamese reading discrepancy found and fixed**: hvdic.thivien.net separates 措's readings into Hán Việt (`thố`, primary; `trách`, alternate) and Nôm (`láp, số, thá, thò, thố`) — the stored `thó` appears in neither list and could not be independently confirmed, while the genuine Hán Việt alternate `trách` was missing; swapped `thó` out for `trách`.

**`japanese` expanded**: stored `[SO]` was missing the 呉音 reading; direct ja.Wiktionary lookup confirms 呉音 `SU`(ス) alongside 漢音 `SO`(ソ, 表内/jōyō) — added.

korean_native (`둘`, "to place"), japanese_native (`お`, stem of おく), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 606), and `hsk_level: 2` (confirmed via [Old HSK 2] line 1290) all confirmed correct as-is; `pos: 事詞` was already correctly filled.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets; `## Words` was oddly placed above `## Notes`) to the standard 4-bullet format and section order. **`## Words`**: tagged the existing [[措置]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[措置]] had several bugs fixed**: blank `cantonese` (filled `cou3 zi3`, composed from 措's own `cou3` + [[置 (char)]]'s own `zi3`); blank `vietnamese` (filled `thố trí`, composed the same way — the exact compound is unattested in hvdic, so this is a compositional reading rather than a directly-sourced one); and an entirely missing `## Notes` section — added with the standard stand-in-note format.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 舷 (7120; 1101 characters remaining).

### 2026-08-12, iteration 1404 — [[characters/舷|舷]]

**`mc_id: 0` confirmed meaningful as-is** (independently re-confirmed absent from all four `CC 0000`–`CC 3000` lookup lists). **`graphemic_classification: 玄` confirmed correct** (形聲, semantic 舟 + phonetic 玄, OC \*ɡeːn on both sides, an exact match). **Alias candidate 墘 investigated and excluded**: Wiktionary's relationship is actually the reverse of what a naive reading suggests — 墘 is the broader, independently-etymologized character (土 + phonetic 乾, "-side, hem, edge" across many Min-dialect compounds like 路墘/田墘), of which 舷 is treated as a nautical-specific alternative form, not the other way around; too distinct in origin and meaning to count as 舷's own variant.

korean_native (`뱃전`, "ship's side"), japanese (`[KEN, GEN]`, both confirmed complete), japanese_native (`ふなばた`, one of two attested kun readings alongside ふなべり), vietnamese (`huyền`, confirmed complete via hvdic), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 292), `hsk_level: 無` (confirmed via [HSK No]), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅎ] line 57) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[舷辺]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[舷辺]] had several bugs fixed**: a genuine `cantonese` contamination — stored `jin4 dou6` had a nonsensical second syllable; corrected to `jin4 bin1` (舷's own `jin4` + [[辺]]'s own `bin1`); a romanization typo in the prose ("funanabata" → `funabata`, matching ふなばた); the recurring `../characters/` broken-relative-path bug; and consolidated two separate Notes bullets (etymology + stand-in note) into the standard single-bullet format.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 孩 (7121; 1100 characters remaining).

### 2026-08-12, iteration 1405 — [[characters/孩|孩]]

**Real `mc_id` off-by-one bug found and fixed** (the twenty-second confirmed instance this session): stored `mc_id: 3546` points to a different character (`CC 3000.md` line 571 = 旻); 孩's true rank is **3547** (line 572), corrected. **`graphemic_classification: 亥` confirmed correct** (形聲, semantic 子 + phonetic 亥, OC \*ɡɯː vs. phonetic's own \*ɡɯːʔ, a close match). **Genuine variant alias added**: 㜾, independently verified as an unqualified "variant form of 孩" with no ancient/archaic labeling.

**Blank `joyo_level` filled** → `表外字`, confirmed via direct ja.Wiktionary lookup (explicitly labeled 表外漢字). **Shared lookup page bug found and fixed** (fourth consecutive cycle): [[Hyōgai]] was missing an entry for 孩 — added.

korean_native (`어린아이`, "young child"), japanese (`[KAI, GAI]`, both confirmed complete), japanese_native (`ちのみご`, confirmed), vietnamese (`[hài, hời]`, confirmed complete), `hsk_level: 1` (confirmed on [Old HSK 1] line 156), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅎ] line 31) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[孩子]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[孩子]] (already richly perfected 2026-07-23) had one bug fixed**: the recurring `../characters/` broken-relative-path bug in its opening Notes bullet.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 婢 (7122; 1099 characters remaining).

### 2026-08-12, iteration 1406 — [[characters/婢|婢]]

**`mc_id: 1644` verified correct as-is** (`CC 1000.md` line 673). **`graphemic_classification: 卑` confirmed correct** (形聲, semantic 女 + phonetic 卑, OC \*beʔ vs. phonetic's own \*pe, a close match). No variant forms listed anywhere — `aliases` correctly left blank.

**`japanese` expanded**: stored `[HI]` was missing the 呉音 reading; direct ja.Wiktionary lookup confirms 呉音 `BI`(ビ) alongside 漢音 `HI`(ヒ) — added. **Blank `joyo_level` filled** → `表外字`, confirmed via the same lookup. **Vietnamese expanded**: hvdic.thivien.net lists two Hán Việt readings (`tì`, `tỳ`) plus Nôm `ti`; the stored `[ti, tì]` was missing `tỳ` — added.

**Shared lookup page bug found and fixed** (fifth consecutive cycle): [[Hyōgai]] was missing an entry for 婢 — added.

korean_native (`계집종`, "female servant"), japanese_native (`はしため`, confirmed), `hsk_level: 無` (confirmed via [HSK No] line 260), and `hanmun_edu_level: 高等` (confirmed on [Korean HS] line 315) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[婢女]] (initially mis-typed its ruby syllable as ㄅㄧㄋㄩ before cross-checking the word's own stored `注音: ㄅㄧㄋㄜ` and correcting it). No Chengyu hits; no derived characters.

**Citing word page [[婢女]] (already perfected 2026-08-04) had two bugs fixed**: the recurring `../characters/` broken-relative-path bug, and a missing stand-in note per [[AIOS/memory/feedback_standin_note|the standing convention]] — appended to its existing rich prose bullet.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 侠 (7123; 1098 characters remaining).

### 2026-08-12, iteration 1407 — [[characters/侠|侠]]

**`mc_id: 1846` confirmed correct, tracked under the traditional alias form** (`CC 1000.md` line 883 = [[俠]], 侠's own listed alias — the same asymmetric-primary-form pattern as [[斎]]/齋). **`graphemic_classification: 夹` confirmed correct** (形聲, semantic 人 + phonetic 夹/夾). **Alias candidate 挾/挟 investigated and excluded**: a sibling character independently sharing the same phonetic 夾/夹 (扌 + phonetic 夾, "to clasp under the arm"), not a variant of 俠/侠 itself — correctly not added.

**Significant malformed-YAML bug found and fixed**: the frontmatter had `japanese_native: おとこだて` immediately followed by two orphaned list items (`- きゃん`, `- おとこだて`) — invalid YAML mixing a scalar assignment with trailing list syntax, with おとこだて duplicated across both. Cross-checked directly against ja.Wiktionary, which lists both きゃん and おとこだて as genuine kun'yomi readings (contradicting English Wiktionary's claim that きゃん was a 唐音 on'yomi) — restructured as a proper two-item `japanese_native` list, matching the established list-format precedent seen on other characters (e.g. [[了 (char)|了]], [[倒 (char)|倒]]). Also added the missing 呉音 `GYOU` to `japanese` (was `[KYOU]` only), and normalized the malformed scalar `aliases: 俠` to proper list syntax.

korean_native (`의기로울`, "chivalrous"), vietnamese (`hiệp`, confirmed complete), `joyo_level: 日本人名用漢字` (confirmed on [Jinmeiyō] line 508 — consistent with 侠 having genuine 名乗り/nanori readings per Wiktionary despite ja.Wiktionary separately calling it 表外漢字, since jinmeiyō and jōyō are distinct lists), `hsk_level: 6` (confirmed on [Old HSK 6] line 414), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅎ] line 63) all confirmed correct as-is; `pos: 名詞` was already correctly filled.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing [[侠客]] as the reflexive stand-in. No Chengyu hits (one prose-only false positive excluded: [[臥虎蔵龍]]); no derived characters.

**Citing word page [[侠客]] had a genuine `pos` inconsistency found and fixed**: stored `事詞`/`品詞: 事詞` didn't fit either the character's own meaning or the word's own English gloss ("knight-errant, swordsman, hero" — all nominal person-labels, not an eventive/action sense) and mismatched the character page's own `名詞` — corrected both fields to `名詞`. Also fixed the recurring `../characters/` broken-relative-path bug and consolidated the stand-in note into the standard single-bullet format.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 萎 (7124; 1097 characters remaining).

### 2026-08-12, iteration 1408 — [[characters/萎|萎]]

**Real `mc_id` off-by-one bug found and fixed** (the twenty-third confirmed instance this session): stored `mc_id: 3695` points to a different character (`CC 3000.md` line 724 = 榛); 萎's true rank is **3696** (line 725), corrected. **`graphemic_classification: 委` confirmed correct** (形聲, semantic 艸 + phonetic 委, OC \*qrol vs. phonetic's own \*qrolʔ, a close match). **Three alias candidates investigated and all excluded as non-genuine**: an initial fetch had surfaced 虧/亏, 唩, and 踒 as "variant forms," but direct verification of each showed none actually carries any such label — 虧 has its own overwhelmingly dominant independent meaning ("loss, deficit") with no documented relationship to 萎 at all, 唩 has no derivative relationship to any character, and 踒 is merely a phonetic-series sibling (independently citing 委, like 萎 itself) with its own distinct meaning ("to sprain a limb"); the earlier "variant" claims for these three appear to have been fetch errors.

**Vietnamese expanded**: hvdic.thivien.net gives Hán Việt `{nuy, uy, uỷ}` and Nôm `{nuy, uỳ}`; the stored `[nuy, uỳ]` was missing `uy` and `uỷ` — added both.

**Blank `hsk_level` filled** → `無`, confirmed absent from all four HSK lookup lists; also found genuinely missing from the [HSK No] page itself — added.

korean_native (`시들`, "to wither"), japanese (`[I]`, both 呉音/漢音 identical, confirmed), japanese_native (`しお`, stem of しおれる), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 19), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅇ] line 152) all confirmed correct as-is. Filled blank `pos` → `事詞` (matching the intransitive change-of-state pattern established on [[逝]]).

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, one stray uncontextualized [[萎縮]] bullet) to the standard 4-bullet format. **`## Words`**: added the missing reflexive stand-in [[萎縮]] alongside the existing [[萎蕤]] (confirmed [[萎蕤]] is actually the stand-in for its OTHER constituent, [[蕤]], not for 萎 itself — correctly left untagged as 萎's own stand-in). No Chengyu hits; no derived characters.

**Two citing word pages had bugs fixed**: [[萎縮]] had a non-standard `## Etymology` heading (renamed to `## Notes`), blank `pos` (filled `事詞`) and blank `vietnamese` (filled `nuy súc`, compositional — the exact compound is unattested in hvdic), plus the recurring `../characters/` broken-relative-path bug; [[萎蕤]] had the same relative-path bug, fixed, and its two Notes bullets consolidated into the standard single-bullet stand-in format.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 頁 (char) (7125; 1096 characters remaining).

### 2026-08-12, iteration 1409 — [[characters/頁 (char)|頁]]

**Real `mc_id` off-by-one bug found and fixed** (the twenty-fourth confirmed instance this session): stored `mc_id: 2684` points to a different character (`CC 2000.md` line 713 = 阯); 頁's true rank is **2685** (line 714), corrected. **`graphemic_classification: 象形` confirmed correct** (a pictogram of a kneeling person's head, 首+卩). **Two alias candidates resolved**: 葉/叶 excluded (its own overwhelmingly dominant meaning "leaf," plus its own independent vault page [[葉 (char)|葉]]); 𩑋 added as a genuine unqualified "variant form of 頁."

**Significant cross-sense Korean reading bug found and fixed, spanning two pages**: stored `korean: 혈`/`korean_native: 머리` documented the character's *original* "head" sense — but 頁 carries two genuinely distinct Korean hanja readings split by sense (혈 for "head," 엽 for "page"), confirmed via Wiktionary's own sense-labeled Korean section. Since this character's documented operative sense is "page, sheet" (not "head"), corrected to `korean: 엽`/`korean_native: 책면`. Moved the character's entry on the shared [[Korean Name ㅎ]] lookup page (### 혈 section) to [[Korean Name ㅇ]] (### 엽 section) to match. **Romanization bug fixed**: `japanese` list had `KECHI` for 呉音 げち — corrected to `GECHI`.

joyo_level `日本人名用漢字` (confirmed on [Jinmeiyō] line 179), `hsk_level: 1` (confirmed on [Old HSK 1] line 179), vietnamese (`[hiệt, hệt]`, confirmed both genuine per hvdic — sense-undifferentiated, unlike Korean), and japanese_native (`おおがい`, the radical-name kun'yomi) all confirmed correct/left as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format, documenting the head/page sense split and why the vault's own MC-derived Dan'a'yo syllable still follows 頁's native "head"-lineage reading regardless. **`## Words`**: tagged the existing self-reference stand-in [[頁]] explicitly. No Chengyu hits; no derived characters.

**Citing word page [[頁]] (already perfected 2026-08-03, with unusually rich analytical prose) had a genuine correction applied**: its own prose had already flagged the head/page semantic tension but concluded it was simply "an older sense preserved in the native gloss" under a single shared reading — missed that Korean actually splits this into two genuinely distinct hanja readings. Corrected `korean: 혈` → `엽` to match, rewrote the affected prose paragraphs accordingly (including the `kwin` divergence explanation), fixed the stray `KECHI`→`GECHI` reference, and fixed the recurring `../characters/` broken-relative-path bug. `date-last-perfect` left unchanged per the established convention for citing-page fixes made during another character's cycle.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 掻 (char) (7126; 1095 characters remaining).

### 2026-08-12, iteration 1410 — [[characters/掻 (char)|掻]]

**Real `mc_id` off-by-one bug found and fixed** (the twenty-fifth confirmed instance this session): stored `mc_id: 3325` points to a different character (`CC 3000.md` line 342 = 捍); the traditional alias form [[搔]]'s true rank is **3326** (line 343), corrected. **`graphemic_classification: 蚤` confirmed correct** (形聲, semantic 手 + phonetic 蚤, OC \*suː vs. phonetic's own \*ʔsuːʔ, a close match). **Five genuine variant aliases added**: 𢸪, 𲢴, 𢫼, 𤔢, 㮻, each individually verified as an unqualified "variant form of 搔" with no ancient/archaic labeling — the sixth candidate from the initial sweep, 𭫂, was already flagged "erroneous" and correctly excluded.

**Malformed Vietnamese field found and fixed, in two places**: both the character page and its citing word stub had a comma-dump list item `"lau, lao, lạo, trau"` mixed in among proper list items — cross-checked against hvdic.thivien.net (Hán Việt `tao, trảo`; Nôm `tao, trao, trau`), which confirms none of `lau/lao/lạo` are attested at all; decomposed into proper list items and added the missing `trảo` (a sense-specific reading tied to 搔's separate "ancient form of 爪" etymology, included per the established practice of keeping all confirmed readings of the same character regardless of sub-sense).

**Korean-reading form mismatch fixed**: `korean_native: 긁다` (modern dictionary citation form) — Wiktionary's own 훈음 gives `긁을` (the traditional adnominal 훈 form used consistently elsewhere in this vault); corrected.

japanese (`[SOU]`, both 呉音/漢音 identical, confirmed), japanese_native (`かく`, one of four attested kun readings), `joyo_level: 表外字` (confirmed via the redirect note on [[Hyōgai]] line 429), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅅ] line 64) all confirmed correct as-is. **Blank `hsk_level` filled** → `無`, and found genuinely missing from the [HSK No] page itself — added. Filled blank `pos` → `事詞` and blank `boundedness` → `90`, matching the established pattern for self-referential stand-in characters.

Rebuilt `## Notes` (wrong heading level; had substantive but non-standard content — a component-breakdown bullet referencing a rare glyph form 𧈡 of 蚤, a bare lookup-links bullet, and two dangling CC-name wikilinks with no rank info) to the standard 4-bullet format. **`## Words`**: tagged the existing self-reference stand-in [[掻]] explicitly. No Chengyu hits; no derived characters (騒 (char) separately cites 蚤 as its own phonetic — a sibling, not a descendant, of 掻).

**Citing word page [[掻]] (the disambiguated self-stand-in stub) had the same malformed Vietnamese bug fixed**, trimmed to a single canonical reading (`tao`) per the established convention for these stubs, and a missing `pos` field filled (`事詞`).

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 勅 (7127; 1094 characters remaining).

### 2026-08-12, iteration 1411 — [[characters/勅|勅]]

**Significant `mc_id` bug found and fixed**: stored `mc_id: 0` was wrong — the traditional alias form [[敕]] is genuinely tracked in the Classical Chinese frequency corpus at rank **1557** (`CC 1000.md` line 582), not absent as the `0` value implied; corrected, the same asymmetric-primary-form pattern seen on [[斎]]/齋 and [[侠]]/俠. **`graphemic_classification: 會意` confirmed correct** (柬/束 "bundle" + 攴 "a stick in hand, denoting authority"). **Genuine variant alias added**: 勑, verified as an unqualified "variant form of 敕." **Alias candidate 飭 investigated and excluded**: its own distinct dominant meaning ("to put in order, rectify, prudent"), matching the competing-modern-meaning exclusion pattern; several other listed forms (𠡠, 敇, 𢽟, 𠡁, 𠡅) were already explicitly flagged "erroneous/nonstandard" in the source and excluded on sight.

**Real Korean-gloss bug found and fixed**: stored `korean_native: 칙서` doesn't match any attested 훈 for this character; direct ko.Wiktionary lookup gives the actual 훈음 as `조서` ("edict") — corrected. **`japanese` expanded**: stored `[CHOKU]` was missing the 呉音 reading; Wiktionary confirms 呉音 `CHIKI`(ちき) alongside 漢音 `CHOKU`(ちょく) — added.

japanese_native (`いまし`, stem of いましめる), vietnamese (`sắc`, confirmed complete via hvdic), `joyo_level: 高等` (confirmed on [Jōyō - Kōtō] line 712), `hsk_level: 無` (confirmed via [HSK No] line 46), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㅊ] line 100) all confirmed correct as-is. Filled blank `pos` → `名詞` and blank `boundedness` → `80`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets; `## Words` was oddly placed above `## Notes`) to the standard 4-bullet format and section order. **`## Words`**: tagged the existing [[勅令]] as the reflexive stand-in. No Chengyu hits; no derived characters.

**Citing word page [[勅令]] (already richly perfected 2026-06-07) had one bug fixed**: the recurring `../characters/` broken-relative-path bug.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 唵 (char) (7129; 1093 characters remaining).

### 2026-08-12, iteration 1412 — [[characters/唵 (char)|唵]]

**`mc_id: 0` confirmed meaningful as-is** (independently reconfirmed absent from all four CC lookup lists — expected for a Buddhist loan character). **`graphemic_classification: 奄` confirmed correct** (形聲, semantic 口 + phonetic 奄). **Alias candidate 嗡 investigated and excluded**: an independent character (its own dominant "buzzing, humming" onomatopoeia) that happens to separately carry the same Sanskrit "Om" borrowed sense via its own distinct etymology — a synonym, not a labeled variant of 唵.

**Homophone-confusion bug found and fixed in `english`**: stored `Ohm` (the SI electrical-resistance unit) — corrected to `Om`, the Sanskrit sacred syllable this character actually transliterates, matching the pre-existing Notes bullet's own etymology.

**Significant cross-sense reading bugs found and fixed, spanning both the character page and its citing word**: stored `korean: 암`/`korean_native: 머금을` and `japanese_native: ふく` all documented the character's *unrelated native Chinese* "hold in mouth" sense (口+奄's literal construction) rather than the Sanskrit "Om" borrowing actually used here. Direct ko.Wiktionary confirms 唵 carries two distinct hanja readings split by sense — 암 (native) vs **옴** (the Sanskrit-borrowing-specific reading, also independently matching this vault's own Dan'a'yo-derived `諺文: 옴`) — corrected `korean` to `옴` and blanked `korean_native`/`japanese_native` to `ø` (no genuine native gloss exists for this borrowed sense in either language). Moved the character's entry on [[Korean Name ㅇ]] from its `### 암` section to a newly-created `### 옴` section. **Vietnamese trimmed**: hvdic.thivien.net explicitly confirms `úm` (not the stored `ướm`) as the reading proper to this Sanskrit sense — `ướm` is an unrelated native Vietnamese word ("to try on") coincidentally sharing 唵's phonetic value; removed.

**Shared lookup page bug found and fixed** (sixth consecutive cycle): [[Hyōgai]] was missing an entry for 唵 (char) — added.

`joyo_level: 表外字`, `hsk_level: 無` (confirmed on [HSK No] line 345), `hanmun_edu_level: 名` (confirmed on [Korean Name ㅇ], now correctly relocated), `pos: 名詞`, and `japanese: [AN, ON]` (both confirmed complete) all confirmed correct/already filled.

Rebuilt `## Notes` (a "Components:" bullet plus a bare etymology sentence, two dangling CC-name wikilinks with no rank info) to the standard 4-bullet format. **`## Words`**: tagged the existing self-reference stand-in [[唵]] explicitly. No Chengyu hits; no derived characters.

**Citing word page [[唵]] (already perfected 2026-07-27) had already independently caught the Ohm→Om bug in a prior pass, but missed the same Korean cross-sense split found this cycle** — its own prose still asserted "Korean 암 (am) parallels the Sino-xenic reading"; corrected `korean: 암` → `옴` and rewrote the affected prose (Korean reading split, and the Japanese kun'yomi ふく explanation, which likewise belonged to the wrong sense) to match. Also fixed the recurring `../characters/` broken-relative-path bug and added the missing stand-in note. `date-last-perfect` left unchanged per the established convention.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 淋 (char) (7130; 1092 characters remaining).

### 2026-08-12, iteration 1413 — [[characters/淋 (char)|淋]]

**`mc_id: 4258` confirmed as legitimate long-tail data** (淋 not found anywhere in the verifiable `CC 0000`–`CC 3000` range) — left as-is. **`graphemic_classification: 林` confirmed correct** (形聲, semantic 水 + phonetic 林). **Alias candidate 瀶 investigated and excluded**: explicitly labeled "ancient form of 淋" by Wiktionary.

**Vietnamese contamination fixed**: stored `[lem, luôm, lâm, lấm, lầm, rướm, rấm]`; cross-checked against both English Wiktionary and hvdic.thivien.net, neither of which attests `luôm` anywhere — removed; the remaining six all confirmed genuine. **Blank `korean_native` filled**: direct ko.Wiktionary lookup gives the 훈 as "젖다" ("to get wet/soaked"), matching the documented "drain, drip" sense — converted to the standard adnominal `젖을` form used elsewhere in this vault. `korean: 림` confirmed correct as the North Korean/문화어 form (Wiktionary notes the South Korean form has shifted to 임 via 두음법칙, correctly not used here per this vault's standing rule).

japanese (`[RIN]`, both 呉音/漢音 identical, confirmed), japanese_native (`さび`, confirmed as the correct okurigana-split stem of さびしい, not さびし), `joyo_level: 日本人名用漢字` (confirmed on [Jinmeiyō] line 355), `hsk_level: 3` (confirmed on [Old HSK 3] line 1536), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㄹ] line 100) all confirmed correct as-is. Filled blank `pos` → `事詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing self-reference stand-in [[淋]] explicitly. No Chengyu hits; no derived characters.

**Citing word page [[淋]] had two bugs fixed**: the recurring `vietnamese: null` corruption — replaced with `lâm`, the primary Hán Việt reading; and a missing `pos` field — filled `事詞`.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 鱗 (char) (7131; 1091 characters remaining).

### 2026-08-12, iteration 1414 — [[characters/鱗 (char)|鱗]]

**`mc_id: 2250` verified correct as-is** (`CC 2000.md` line 263). **`graphemic_classification: 粦` confirmed correct** (形聲, semantic 魚 + phonetic 粦, pageless in this vault). **Two alias candidates investigated and excluded**: 魿 (not labeled a variant of 鱗 despite sharing the same Japanese kun'yomi うろこ — an independent character in its own right) and 䰼 (a wholly unrelated character meaning "condiment/salted fish," no documented relationship at all).

korean_native (`비늘`, "scale," matching the eumhun exactly), japanese_native (`うろこ`, primary kun), `korean: 린` (confirmed correct North Korean/문화어 form, avoiding the South-Korean-shifted 인), vietnamese (`lân`, confirmed complete via hvdic), `joyo_level: 日本人名用漢字` (confirmed on [Jinmeiyō] line 221), `hsk_level: 無` (confirmed via [HSK No] line 380), and `hanmun_edu_level: 名` (confirmed on [Korean Name ㄹ] line 97) all confirmed correct as-is. Filled blank `pos` → `名詞`.

Rebuilt `## Notes` (wrong heading level, two bare floating unlinked CC-name lines, no other bullets) to the standard 4-bullet format. **`## Words`**: tagged the existing self-reference stand-in [[鱗]] explicitly. No Chengyu hits; no derived characters.

**Citing word page [[鱗]] (already richly perfected 2026-03-25) had no bugs found** — all fields (including japanese/vietnamese as lists, an unusual but valid style for these self-stand stubs) were already correct.

Stamped `date-last-perfect: 2026-08-12`.

Next never-perfected character by `danayo_id`: 聊 (char) (7132; 1090 characters remaining).
