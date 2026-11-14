# Log

Changes to the vault, newest first. History lives here and nowhere else — pages hold only the working content. Older entries are in the archive files beside this one (`Log/log YYYY-MM-DD to YYYY-MM-DD.md`); the log rolls over to a new file at about 300 KB.

## 2026-11-13

### History sentences removed from content pages

- **History sentences deleted from content pages (user: "Delete all such sentences like 'an earlier version…'. That is expressly what the log is for."):** about 110 `chengyu/` pages, 50 `words/` pages, 6 `characters/` and `lookup/CC/` pages (`韻 豪`, `聲 知`, `聲 群`, `聲 從`, `聲 澄`, `夹`, `稷`, `醴`). Removed: "an earlier version of this page said…", "previously read…", "**Corrected.**" paragraphs, "has been removed" and "now reads" narration, "rebuilt from" narration. Where such a paragraph also held a present-state fact (the true source, what was verified, what is unverified, why a look-alike word is not an alias), the fact stays as a plain statement. A few paragraphs were dropped whole because they only repeated a claim the old page had made: `chengyu/重文軽武` (the 《新唐書·兵志》 sentence), `chengyu/風声鶴唳` (the 《晉書》 paragraph), `chengyu/論功行賞`, `chengyu/海闊天空`, `chengyu/殺姦窃偽`, `words/老鼠人`, `words/臘八粥`, `words/臘八節`. Checked: `lint_chengyu.py` 0 of 247 defects, grouping pages OK. Not done: the six `characters/` hub-alias sentences and the other regex hits were false positives ("is kept here as this page's alias" is a present-state statement) and were left.

### Log rollover

- **Log rolled over (user: standing rule, about 300 KB per file):** `Log/log.md` had reached 463 KB; the dates 2026-11-05 to 2026-11-09 moved unchanged into `Log/log 2026-11-05 to 2026-11-09.md` (276 KB), leaving 2026-11-10 to 2026-11-13 in `Log/log.md` (187 KB). The rule and the archive naming are written in `AIOS/log-convention.md`.

### 文法 - 99韻図 re-derived from the corpus

- `grammar/文法 - 99韻図.md`: the Dan'a'yo (D) column of the Vowels table was rewritten from the corpus (the author wrote the page from memory). For each of the 160 finals, D is now the largest group on the final's CC page, written in the vault's romanization, plus the second and third groups where each holds at least 35% of attested characters. 55 rows changed (e.g. 鍾 `ong/yong`, 夬開 `ai`, 廢合 `e`, 廢開 `yi`, 刪合 `wam/wan`, 陽合 `ang`, 尤 `yu`, 登開 `ung/ǝng`); the four finals with no attested characters (臻, 質合, 陌三合, 錫合) keep their old values; the MC Sound of 乏 was corrected to the corpus value `iɐp`. In the Consonants table, 莊 changed `s`→`j`, 端 `d/t`→`d`, 徹 `t/c`→`c/t`, 精 `j `→`j`; the M/C/J/K/V columns were not touched. Authority: the character corpus as summarised on the CC pages.
- The CC finals pages that quote a documented value were updated to the new D values (about 45 pages, mostly the backticked value in the CJKV Evolution paragraph); the table-discrepancy notes on 韻 刪合, 夬開, 夬合, 廢合, 廢開 and 聲 莊 were rewritten as agreement notes, and 韻 佳開, 庚三合, 鹽A三 were reworded by hand.

### CC initials and finals pass

- **諸 moved from 戈三開 to 麻三開 (user: chose 麻三開):** `characters/諸 (char).md` `middle_chinese_final` ɨɑ → ia, and its etymology link now points to `lookup/CC/finals/韻 麻三開`; its spelling ㄐㄚ is unchanged (ㄐ cannot carry the y-glide, like 姉, 遮, 借, 者). `lookup/CC/finals/韻 戈三開.md` now holds 伽 only (size 2 → 1), the 諸 data-quality flag removed; `lookup/CC/finals/韻 麻三開.md` size 26 → 27, ㄚ group 4 → 5, cites en.Wiktionary 諸 (魚 and 麻 readings, read 2026-11-13); the AIOS skill link on that page was replaced with plain wording. 韻 戈三開 stamped 2026-11-13; 韻 麻三開 keeps its 2026-10-06 stamp until its own re-check.
- `lookup/CC/finals/韻 戈三開.md`: size 2 = ruby 2 = corpus 2 after pipe-aliasing 諸's ruby link; row 096 of 文法 - 99韻図 (`ya/a`) checked; the 諸 data-quality flag now cites en.Wiktionary 諸 (魚 /t͡ɕɨʌ/ and 麻 /t͡ɕia/ readings, neither 戈三開), read 2026-11-13; added that 伽 has `mc_id: 0`; 諸's final left as the corpus has it (character page unedited, still flagged for re-check); stamped 2026-11-13.
- `lookup/CC/finals/韻 戈三合.md`: size 1 = ruby 1 = corpus 1 (靴 on ⺢), row 097 of 文法 - 99韻図 (`wa`) checked; added 靴's daughter readings; stamped 2026-11-13.
- `lookup/CC/finals/韻 戈一合.md`: size 36 = ruby 36 = corpus 36, groups 21 ⺢ / 13 ㄚ / 1 ㄜ / 1 ⺢ㄇ re-counted, row 095 of 文法 - 99韻図 (`wa/a`) checked; fixed 破's crowd claim (ㄆㄚ holds 玻 and 叵 only, 頗 is on ㄈㄚ), added the tone-only near-homophone evidence for 破/叵 and 課/顆, removed a link to the AIOS skill page and "cleanest confirmation yet"; stamped 2026-11-13.
- `lookup/CC/finals/韻 德開.md`: size 14 = ruby 14 = corpus 14, groups 10 ㄨㄎ / 4 ㄜㄎ, row 131 of 文法 - 99韻図 (`uk`) checked; 徳/得 divergence now shows Vietnamese differs too, 勒/肋 noted as true homophones, "documented repeatedly in this sweep" dropped; stamped 2026-11-13.
- `lookup/CC/finals/韻 德合.md`: size 3 = ruby 3 = corpus 3, all on ㄛㄎ, row 132 of 文法 - 99韻図 (`ok`) checked; added the daughter readings (或/惑 exact homophones, 国 differs in initial only); stamped 2026-11-13.
- `lookup/CC/finals/韻 微開.md`: size 15 = ruby 15 = corpus 15, all on ㄧㄜ, row 020 of 文法 - 99韻図 (`iǝ`) checked; dropped the "in this stretch of the sweep" wording and added the daughter readings and the ㄎ/ㄍ aspiration split; stamped 2026-11-13.
- `lookup/CC/finals/韻 微合.md`: size 36 = ruby 36 = corpus 36, groups 26 ㄨㄧ / 4 ㄧ / 3 ㄛㄧ / 1 ㄝㄧ / 1 ㄚㄧ / 1 ㄨ re-counted (nine f/fʰ characters checked), row 021 of 文法 - 99韻図 (`ui`) checked; the ㄛㄧ group (威, 慰, 畏) was undiagnosed and is now explained as a near-homophone escape from the seven-member null-initial ㄨㄧ slot; the 彙 cross-reference sentence rewritten without page history; stamped 2026-11-13.
- `lookup/CC/finals/韻 廢開.md`: size 2 = ruby 2 = corpus 2, both on ⼘ㄧ; replaced "near-identical" with the actual daughter readings (identical in Mandarin, Cantonese, Korean; Vietnamese differs); row 027 of 文法 - 99韻図 gives `yai` against the corpus's `yi`, now stated on the page, table unedited and flagged for the user; stamped 2026-11-13.
- `lookup/CC/finals/韻 廢合.md`: size 3 = ruby 3 = corpus 3, all on ㄝ; completed the daughter readings (Cantonese, Vietnamese added); row 028 of 文法 - 99韻図 gives `ye` against the corpus's bare `e`, now stated on the page, table unedited and flagged for the user; stamped 2026-11-13.
- `lookup/CC/finals/韻 庚二開.md`: size 25 = ruby 25 = corpus 25 (22 ㄚㄫ / 1 ⼶ㄫ / 1 ⺢ㄫ / 1 excluded 檸), three-member ㄏㄚㄫ crowd re-verified, row 109 of 文法 - 99韻図 (`ang`) checked; summary line corrected (two glide-adding exceptions plus the overridden 檸, not three glide-adders); 荇 re-diagnosed as a true homophone of 杏 rather than an unconditioned singleton; stamped 2026-11-13.
- `lookup/CC/finals/韻 庚二合.md`: size 2 = ruby 2 = corpus 2, both on ⺢ㄫ, row 110 of 文法 - 99韻図 (`wang`) checked; added the daughter readings of 横 and 鉱; stamped 2026-11-13.
- `lookup/CC/finals/韻 庚三開.md`: size 34 = ruby 34 = corpus 34, groups 29 ⼶ㄫ / 3 ㄝㄫ / 2 ㄧㄫ, crowd counts (7 labial, 11 k/g, 影/映 pair) re-verified from the corpus, row 111 of 文法 - 99韻図 (`ing/eng/yeng`) checked; added the daughter readings that show 瑛/英 vs 影/映 and 苹 vs 平 are near-homophone splits; stamped 2026-11-13.
- `lookup/CC/finals/韻 庚三合.md`: size 7 = ruby 7 = corpus 7, groups 4 ㄨㄧㄫ / 3 ⼄ㄫ, every daughter reading in the prose re-checked against the character files (all correct), row 112 of 文法 - 99韻図 (`wing`) checked; added the Vietnamese split (v- vs h-/qu-/c-); stamped 2026-11-13.
- `lookup/CC/finals/韻 幽.md`: size 6 = ruby 6 = corpus 6 after pipe-aliasing 幽's ruby link; groups 4 ⼜ㄛ / 2 ⼜, row 138 of 文法 - 99韻図 (`yu/yuu`) checked; 赳/糾 homophony confirmed in all four daughters (added Vietnamese *củ*), 謬's Korean 류 noted as unexplained; stamped 2026-11-13.
- `lookup/CC/finals/韻 帖.md`: size 18 = ruby 18 = corpus 18, groups 15 ㄝㄆ / 2 ㄧㄆ / 1 ㄛㄆ, the six-member d/tʰ cluster re-counted, row 158 of 文法 - 99韻図 (`ep`) checked; 帖 and 怗 now diagnosed as true homophones of 貼 from the daughter readings (tip3, 첩, thiếp); stamped 2026-11-13.
- `lookup/CC/finals/韻 山開.md`: size 16 = ruby 16 = corpus 16, groups 13 ㄚㄋ / 3 ⼘ㄋ, row 073 of 文法 - 99韻図 (`an`) checked; rewrote the exceptions paragraph: 柬/揀 are true homophones of 簡 (crowding escape), 弁 has no collision (ㄅㄚㄋ holds only 辦) and follows its front-vowel Cantonese *bin6*/Korean 변; dropped the 魂 cross-reference; stamped 2026-11-13.
- `lookup/CC/finals/韻 山合.md`: size 1 = ruby 1 = corpus 1 (幻 on ⺢ㄋ), row 074 of 文法 - 99韻図 (`wan`) checked; added the daughter readings of 幻; stamped 2026-11-13.
- `lookup/CC/finals/韻 屑開.md`: size 22 = ruby 22 = corpus 22, groups 20 ㄝㄊ / 1 ㄛㄊ / 1 ㄚㄊ, ㄉㄝㄊ crowd of three and 截's unique d͡ʒ initial re-verified, row 087 of 文法 - 99韻図 (`et`) checked; fixed a typo (迭itself), added the daughter readings that make 迭 a true homophone and show nothing explains 截; stamped 2026-11-13.
- `lookup/CC/finals/韻 屑合.md`: size 4 = ruby 4 = corpus 4, all on ⼔ㄊ, row 088 of 文法 - 99韻図 (`wet`) checked; added the daughter readings and a note that 決/訣 (same k initial, identical readings) are spelled ㄎ vs ㄍ on their character pages (left unedited); stamped 2026-11-13.
- `lookup/CC/finals/韻 屋三.md`: size 45 = ruby 45 = corpus 45, 育/郁 correctly folded into ㄨㄎ (initial-driven glide), row 004 of 文法 - 99韻図 (`uk`) checked; 尗/叔 now shown as a true-homophone divergence across all four daughters (suk1, 숙, thúc), 偪's daughter codas added; stamped 2026-11-13.
- `lookup/CC/finals/韻 屋一.md`: size 21 = ruby 21 = corpus 21, groups 20 ㄛㄎ / 1 ㄨㄎ, row 003 of 文法 - 99韻図 (`ok`) checked; 攴/撲 corrected from "true homophone" to near-homophone (Korean 복 vs 박, Vietnamese *phộc* vs *buộc*); history-style wording trimmed; stamped 2026-11-13.
- `lookup/CC/finals/韻 尤.md`: corpus had 115, page 114 — 畴 (ɖ, ㄐㄨㄛ) added to the ㄨㄛ group (29→30), size 114→115, prose totals updated (109 in the four main groups + 6 outliers); dropped the unverified "biggest final page" claim; added 肘's Vietnamese *khuỷu* (no coda); Cantonese readings of 否/愁/驟 re-checked; row 136 of 文法 - 99韻図 (`~`) noted; stamped 2026-11-13.
- `lookup/CC/finals/韻 寒.md`: size 50 = ruby 50 = corpus 50 after pipe-aliasing eight un-aliased ruby links (壇, 岸, 残, 汗, 灘, 炭, 看, 餐); corrected the ㄏㄚㄋ crowd size (six, not ten), noted 䦨's empty Vietnamese field, dropped the "in this sweep" wording; row 061 of 文法 - 99韻図 (`an`) checked; stamped 2026-11-13.
- `lookup/CC/finals/韻 宵B.md`: size 20 = ruby 20 = corpus 20, groups 14 ⼘ㄨ / 6 ㄚㄨ re-counted, retroflex rule re-verified from the corpus initials (ɖ/ʈʰ for exactly the six, none in the main group), row 092 of 文法 - 99韻図 (`yau`) checked; added the daughter readings; stamped 2026-11-13.
- `lookup/CC/finals/韻 宵A.md`: size 45 = ruby 45 = corpus 45, groups 27 ⼄ㄨ / 12 ㄛㄨ / 3 ⼄ / 2 ㄛ / 1 ㄚㄨ re-counted, the 9-of-12 affricate count checked from the initials, row 091 of 文法 - 99韻図 (`ou`) checked; fixed 礁's crowd size (ㄐㄛㄨ has 7 members, not 3) and added the daughter readings that make 擾/繞 a true-homophone split; stamped 2026-11-13.
- `lookup/CC/finals/韻 夬開.md`: size 5 = ruby 5 = corpus 5, all on ㄚㄧ; row 029 of 文法 - 99韻図 still carries `wai` (flagged on the page, table unedited, user decision pending); dropped the "checked so far"/"earlier in this sweep" wording and added the daughter readings; stamped 2026-11-13.
- `lookup/CC/finals/韻 夬合.md`: size 2 = ruby 2 = corpus 2, both on ⺢ㄧ, row 030 of 文法 - 99韻図 (`wai`) checked; dropped the "in this sweep" wording and added the daughter readings of 快 and 話; row 029 (夬開) still carries `wai` and is flagged on 韻 夬開; stamped 2026-11-13.
- `lookup/CC/finals/韻 嚴.md`: size 2 = ruby 2 = corpus 2, one character per group (⼘ㄇ, ⼶ㄇ), row 145 of 文法 - 99韻図 (`yam/yem`) checked; added the daughter readings of 欠 and 杴 from the character files; stamped 2026-11-13.
- `lookup/CC/finals/韻 唐開.md`: size 50 = ruby 50 = corpus 50, groups 44 ㄚㄫ / 5 ⺢ㄫ / 1 ⼘ㄫ re-counted, row 101 of 文法 - 99韻図 (`ang`) checked; the aspiration remark narrowed to the aspirated affricate t͡sʰ (the stops pʰ, kʰ, tʰ stay in the main group), and 芒's homophone claim corrected (茫/忙 exact, 莽 differs in tone); stamped 2026-11-13.
- `lookup/CC/finals/韻 唐合.md`: size 15 = ruby 15 = corpus 15, all on ⺢ㄫ, row 102 of 文法 - 99韻図 (`wang`) checked; added the daughter-coda summary (all four keep -ng) from the character files; stamped 2026-11-13.
- `lookup/CC/finals/韻 咸.md`: size 6 = ruby 6 = corpus 6, all on ㄚㄇ, row 151 of 文法 - 99韻図 (`am`) checked; added the daughter-coda summary (Cantonese -aam, Korean -m, Mandarin -n, Vietnamese mixed) from the character files; stamped 2026-11-13.
- `lookup/CC/finals/韻 咍.md`: size 62 = ruby 62 = corpus 62, groups 57 ㄚㄧ / 4 ㄛㄧ / 1 ㄧ re-counted, finals-only labels, row 041 of 文法 - 99韻図 checked; the Cantonese remark now carries counts from the corpus (43 of 57 regular characters are `-oi` like the three attested ㄛㄧ ones; eight are `-aai`) and 啡's diagnosis adds its Cantonese *fe1*; stamped 2026-11-13.
- `lookup/CC/finals/韻 合.md`: size 16 = ruby 16 = corpus 16, groups 9 ㄚㄆ / 7 ㄛㄆ re-counted, finals-only labels, row 160 (`ap/op`) of 文法 - 99韻図 checked; 䏜 note now cites its Vietnamese *mạp*; new data-quality flag for 显, whose readings are those of 顕 (-n coda) against its ʌp tag (character page left unedited); stamped 2026-11-13.
- `lookup/CC/finals/韻 刪開.md`: size 19 = ruby 19 = corpus 19; fixed two un-aliased ruby links (贋, 雁 filenames carry " (char)"); data-quality note updated, since 諌's Mandarin is now *jiàn* and only its Cantonese field (*dung2*) still mismatches (character page left unedited); stamped 2026-11-13.
- `lookup/CC/finals/韻 刪合.md`: size 9 = ruby 9 = corpus 9, groups 5 ⺢ㄇ / 4 ⺢ㄋ re-counted, finals-only labels; 関/慣 added as a near-homophone split and the daughter codas checked (all -n, none predicts the m-group); the reference-table discrepancy (`wam` in row 070 of 文法 - 99韻図 against the 山攝 -n history and an n-coda in half the corpus) left unedited and flagged for the user; stamped 2026-11-13.
- `lookup/CC/finals/韻 凡.md`: fixed two un-aliased ruby links (剣, 厳 filenames carry " (char)"), so size 12 = ruby 12 = corpus 12 with all matched; prose: the three main groups shown to equal the Vowels table's documented triple `am/om/im` (row 146 of 文法 - 99韻図), Vietnamese múp (-p) and phàn (-n) noted as support for the two coda shifts, 帆 fān added to the Mandarin readings; stamped 2026-11-13.
- `lookup/CC/finals/韻 冬.md`: size 8 = ruby 8 = corpus 8, finals-only labels; the thirteen-member ㄉㄛㄫ crowd counted from the corpus (13 ✓), 彤 added as a true homophone of 同 (tóng, tung4, 동), Vowels-table row 005 cited; stamped 2026-11-13.
- `lookup/CC/finals/韻 先開.md`: size 47 = ruby 47 = corpus 47, finals-only labels, every spelling matches its group; crowding counts re-checked (ㄉㄝㄋ 9 ✓; the ㄏㄝㄋ crowd is five, with 蜆 added to 顕/弦/賢/舷); 殿/電 added as a true-homophone split; `en` cited as row 085 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 先合.md`: size 6 = ruby 6 = corpus 6, all six spelled ⼔ㄋ; Vowels-table winner `wen` confirmed in row 086 of 文法 - 99韻図 and now cited, with the six characters' Middle Chinese initials noted; no other change; stamped 2026-11-13.
- `lookup/CC/finals/韻 元開.md`: size 8 = ruby 8 = corpus 8, all eight spelled ㄝㄋ; Vowels-table winner `en` confirmed in row 065 of 文法 - 99韻図 and now cited, with the initial classes of the eight noted; no other change; stamped 2026-11-13.
- `lookup/CC/finals/韻 元合.md`: size 37 = ruby 37 = corpus 37, finals-only labels, every spelling matches its group; the prose corrected from the character files (the v-initial cohort is five, not three: 飯 and 藩 stay on ㄅㄛㄋ/ㄆㄛㄋ; ㄅㄛㄋ holds 飯 and 坂, not one member; the null-initial crowd on ㄛㄋ is ten, five ʔ and five ø, not five); `on` cited as row 066 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 非.md`: size 43 = ruby 43 = corpus 43, counts 42 ㄈ / 1 ㄅ; the claim that Korean 부 agrees with a light-labial f- for 傅 corrected (ㅂ; the ㄈ characters 付/府/夫 are also 부) and 傅/付 added as a true-homophone split; Consonants-table winner `f` confirmed in row 010 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 邪.md`: size 49 = ruby 49 = corpus 49; counts 46 ㄙ / 1 ㄏ / 1 ㄐ / 1 ㄑ re-counted; the three singletons re-read in the character files (辞: Mandarin and Cantonese aspirated, Korean and Vietnamese not; 鱏: only Mandarin xún supports ㄏ; 俟: no support, poll-only); the muddled "sole 俟-initial character" count explanation replaced (俟 is tagged z and counted in the 49); Consonants-table winner `s` confirmed in row 023 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 透.md`: size 67 = ruby 67 = corpus 67; counts 63 ㄊ / 4 ㄑ re-counted; the four ㄑ characters now tied to their Korean ㅊ readings (추, 청, 청, 체) against 정 for 汀/訂/町 on the same final; Consonants-table winner `t` confirmed in row 016 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 見.md`: size 303 = ruby 303 = corpus 303; the prose's "284 of 301" corrected to 285 of 303 and the unexplained "one ㄈ fiat (see below)" in the summary tied to 攫 (already annotated in the group); 軌 (guǐ) and the Vietnamese readings of the 九 family noted; Consonants-table winner `g` confirmed in row 041 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 莊.md`: size 27 = ruby 27 = corpus 27, counts 26 ㄐ / 1 ㄑ; 鄒's Korean-explains claim corrected (皺 has the same Cantonese and Korean readings and stays on ㄐ, so the split is unconditioned); the discrepancy that row 027 of 文法 - 99韻図 gives `s` as the 莊 value while the corpus is 26 of 27 on ㄐ recorded on the page and left unedited in the table (decision for the user); stamped 2026-11-13.
- `lookup/CC/initials/聲 船.md`: size 50 = ruby 50 = corpus 50, all spellings begin with ㄙ; the page-level history sentence about 船's former mistag removed (history belongs in the log; the earlier correction is recorded there); Consonants-table winner `s` confirmed in row 038 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 群.md`: the corpus has 91 characters carrying g but the page listed 90 — 耆 (ㄍㄧㄜ) was missing; added to the ㄍ group, `size` 90 → 91, counts 87 ㄍ / 4 ㄎ; the "clean, fully-explained exception" claim for 期/旗/埼/禽 corrected (35 ㄍ characters also have aspirated Mandarin q-, so the split is unconditioned), 禽/琴 cross-referenced to 韻 侵B; Consonants-table winner `g` confirmed in row 043 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 精.md`: size 99 = ruby 99 = corpus 99 (97 ㄐ + 走, 奏 on ㄙ); the prose's claim that the ㄐ majority "follows Mandarin palatalization exactly" corrected from the corpus (only 40 of 97 have a palatal Mandarin reading; 57 are z-/c-), 走/奏 re-diagnosed as the only 精-initial characters with final əu (shared with 韻 侯) instead of a back-vowel rule; Consonants-table winner `j` confirmed in row 019 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 端.md`: size 79 = ruby 79 = corpus 79; the prose's "56 of 80" corrected to 79 and the summary line's nonexistent ㄙ minority removed (groups: ㄉ 56, ㄊ 16, ㄑ 5, ㄐ 2); the ㄑ/ㄐ palatalization tied to the seven characters' Korean affricate readings (조, 초, 정); the table's dual `d/t` cited from row 015 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 章.md`: size 100 = ruby 100 = corpus 100; the prose's "93 of 99" corrected to 94 of 100 (ㄐ) with 5 ㄑ and 之 on ㄊ; 之/芝 added as a true-homophone split, Cantonese readings of 彰/招/燭 noted; Consonants-table winner `j` confirmed in row 034 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 禪.md`: size 35 = ruby 35 = corpus 35; counts 33 ㄙ / 2 ㄐ re-counted; 盾 and 垂 re-checked (Korean and Vietnamese readings are sibilants, pointing to ㄙ, so poll-only stands); Consonants-table winner `s` confirmed in row 036 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 知.md`: size 48 = ruby 48 = corpus 48; counts 26 ㄐ / 8 ㄑ / 7 ㄉ / 7 ㄊ re-counted; the poll-only list corrected ("three" naming four characters → five: 珍, 鎮, 張, 貞, 壴; 脹 supported by Korean 창); the "none of the ㄉ seven" claim corrected (嫡 has dental-stop Mandarin dí and Cantonese dik1); Consonants-table winner `j` confirmed in row 030 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 疑.md`: size 115 = ruby 115 = corpus 115 (114 ø + 牛 on ㄋ); the prose's "113 of the 114" corrected to 114 of 115 and the stale "明 pending" removed; 牛's Vietnamese ngưu added; Consonants-table winner `ø` confirmed in row 044 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 生.md`: size 44 = ruby 44 = corpus 44, all spellings begin with ㄙ; Consonants-table winner `s` confirmed in row 026 of 文法 - 99韻図 and now cited; no other change needed; stamped 2026-11-13.
- `lookup/CC/initials/聲 澄.md`: the corpus has 72 characters carrying ɖ but the page listed 71 — 畴 (alias 疇, ㄐㄨㄛ) was missing; added to the ㄐ group, `size` 71 → 72, counts updated to 34 ㄐ / 19 ㄉ / 17 ㄑ / 2 ㄊ and 53 against 19 for the unaspirated and aspirated pairs; Consonants-table winner `j` confirmed in row 032 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 滂.md`: size 52 = ruby 52 = corpus 52; counts 50 ㄆ / 1 ㄈ / 1 ㄅ re-counted; 頗/叵 added as a true-homophone divergence on the same final, 魄's Mandarin and Cantonese aspiration noted (only Korean 백 supports ㄅ), 咅's pʰ tag cross-referenced to 韻 侯; Consonants-table winner `p` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 溪.md`: size 121 = ruby 121 = corpus 121, all spellings begin with ㄎ; the prose's "largest fully clean page in this project" corrected (聲 來 has 216 with a single outcome); Consonants-table winner `k` confirmed in row 042 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 清.md`: size 71 = ruby 71 = corpus 71, all spellings begin with ㄑ; the prose's "all 69 characters" corrected to 71 and the stale "聲 昌 pending" replaced with 昌's actual state (one exception, 串); Consonants-table winner `c` confirmed in row 020 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 泥.md`: size 44 = ruby 44 = corpus 44, all spellings begin with ㄋ; Consonants-table winner `n` (and the Cantonese `n~l` note) taken from row 018 of 文法 - 99韻図; no other change needed; stamped 2026-11-13.
- `lookup/CC/initials/聲 書.md`: size 71 = ruby 71 = corpus 71; counts 69 ㄙ / 1 ㄊ / 1 ㄑ re-counted; 弒 re-diagnosed as a true homophone of 試 (and its Vietnamese thí th- is the regular 書 reflex, not support), 沈's Vietnamese chìm added; Consonants-table winner `s` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 曉.md`: size 108 = ruby 108 = corpus 108; counts 103 ㄏ / 3 ㄍ / 1 ㄑ / 1 ⼔ re-counted; the claim that Cantonese shows a stop g- for all three ㄍ characters corrected (霍 is fok3, an f-; only Korean 곽 supports its ㄍ, 軣's Mandarin is hōng) and 矣's Vietnamese hĩ noted; Consonants-table winner `h` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 明.md`: size 142 = ruby 142 = corpus 142, all spellings begin with ㄇ; the overstatements corrected ("/m/ survives everywhere" → the 明 row shows v, w and kan-on b in some daughters; "largest fully clean page" → equal to 心, with 來 and 見 larger); 冘's m tag cross-referenced to 韻 侵A; Consonants-table winner `m` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 昌.md`: size 34 = ruby 34 = corpus 34; the prose's "32 of 33" corrected to 33 of 34 (ㄑ) + 串 on ㄐ; 串's "unexplained poll-only" label revised (Korean 곶 and Vietnamese quán are not aspirated, cross-referenced to 韻 仙A三合); Consonants-table winner `c` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 日.md`: size 53 = ruby 53 = corpus 53, all spellings begin with ㄋ; the prose's "all 52 characters" corrected to 53; the daughter-language split (Vietnamese nh, Japanese go-on n against Korean ø, kan-on/tō-on z, Mandarin ɻ/ʔ, Cantonese y) and `n` taken from the 日 row of 文法 - 99韻図; the "first character of Japan" design account marked as unrecorded on the character page; stamped 2026-11-13.
- `lookup/CC/initials/聲 敷.md`: size 36 = ruby 36 = corpus 36, all spellings begin with ㄈ; the comparison with 非 made exact (42 of 43 there, 傅 the one exception); Consonants-table winner `f` confirmed in row 011 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 心.md`: size 142 = ruby 142 = corpus 142, all spellings begin with ㄙ; the prose's "all 139 characters — the largest fully clean page yet" corrected to 142 and "one of the larger" (聲 來 has 216 with a single outcome); Consonants-table winner `s` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 徹.md`: size 25 = ruby 25 = corpus 25; counts 14 ㄑ / 11 ㄊ re-counted; "the one initial" with a dual table value corrected (端's `d/t` is the other); added the final-type tendency found in the corpus (ɣ-initial finals: 7 of 9 on ㄊ; others: 12 of 16 on ㄑ), noting the daughter readings do not separate the groups; `t/c` confirmed in row 031 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 微.md`: size 36 = ruby 36 = corpus 36, all 36 spellings begin with ㄇ (checked); Consonants-table winner `m` confirmed in row 014 of 文法 - 99韻図 and now cited; no other change needed; stamped 2026-11-13.
- `lookup/CC/initials/聲 從.md`: size 66 = ruby 66 = corpus 66; counts 51 ㄐ / 15 ㄑ re-counted; the poll-only list corrected from three (匠, 蔵, 造) to two (匠, 造): 蔵 (cáng, cong4) and 瓷 (cí, ci4) are aspirated in Mandarin and Cantonese and 瓷 had been left out of the prose altogether; 匠's shared final with 牆/薔 noted; Consonants-table winner `j` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 影.md`: size 145 = ruby 145 = corpus 145, and no spelling begins with a consonant letter (checked); the prose's "all 144 characters" corrected to 145; Consonants-table winner `ø` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 幫.md`: fixed the un-aliased ruby link for 氷 (filename carries " (char)"), so size 109 = ruby 109 = corpus 109 with all matched; counts 87 ㄅ / 19 ㄆ / 3 ㄈ re-counted; the ㄆ minority diagnosed against the Korean readings (11 of 19 aspirated; 8 poll-only), the ㄈ three noted as unsupported by their own readings and 輩 tied to the 佩/培/徘 final; Consonants-table winner `b` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 崇.md`: size 19 = ruby 19 = corpus 19; counts 14 ㄐ / 4 ㄙ / 1 ㄑ re-counted; the claim that the four ㄙ characters show no daughter-language support corrected (士 sh-/s-/사/sãi, 床 상, 愁 sau4/수, 驟 sậu), 士/事 added as true homophones in Mandarin, Cantonese and Korean landing on ㄙ and ㄐ; Consonants-table winner `j` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 定.md`: fixed the un-aliased ruby link for 鈍 (filename carries " (char)"), so size 140 = ruby 140 = corpus 140 with all matched; counts 128 ㄉ / 9 ㄊ / 3 ㄐ re-counted; 条's ㄐ now tied to its Korean 조, the nine ㄊ characters checked against their Mandarin readings (締, 逓 unaspirated in Mandarin, aspirated in Korean 체); Consonants-table winner `d` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 娘.md`: size 13 = ruby 13 = corpus 13 (12 on ㄋ + 檸 in the overridden-reading line); the "`mc_id: 0`" claim for 檸 corrected to an empty `mc_id` field, its n- readings (níng, ning4, 녕) and the 레몬-based override stated, from the character file; Consonants-table winner `n` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 奉.md`: size 50 = ruby 50 = corpus 50; counts 34 ㄅ / 9 ㄈ / 6 ㄆ / 1 ㄇ re-counted; the claim that no daughter language hints at 柉's nasal initial corrected (Vietnamese múp begins with m-); 煩/繁 added as true homophones in all four daughters landing on ㄈ and ㄆ; Consonants-table winner `b` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 匣.md`: size 177 = ruby 177 = corpus 177; counts 170 ㄏ / 3 ㄎ / 4 null re-counted; the three ㄎ and four null characters re-read in the character files; 侑 added as a true-homophone divergence from 佑 (same y- readings, spelled ㄏ⼜); Consonants-table winner `h` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 初.md`: size 24 = ruby 24 = corpus 24, every spelling begins with ㄑ, value t͡ʃʰ (with tie bar U+0361) matches the corpus; the daughter-language summary re-read against the Consonants rows of 文法 - 99韻図 (D `c` for 初, 清 and 昌 confirmed); the Vietnamese `ʂ > s` shift narrowed from "the whole 生/莊/初/崇 block" to 生, 初 and 崇 (莊 has `ʈ > tr`); stamped 2026-11-13.
- `lookup/CC/initials/聲 俟.md`: empty page confirmed (0 characters carry ʒ; size 0 = ruby 0 = corpus 0; Datacheck base filters on ʒ); the quoted claim "俟 is the sole character in the corpus with 邪母 initial /z/" qualified (49 characters carry z; 俟 is one of 邪's 49) and the Consonants-table value `j` for the 俟 column (文法 - 99韻図) added; 俟's character page prose left as is; stamped 2026-11-13.
- `lookup/CC/initials/聲 來.md`: size 216 = ruby 216 = corpus 216, every spelling begins with ㄌ; the prose's "all 214 characters, the largest page in the set" corrected to 216 and second-largest (聲 見 has 303); Consonants-table winner `l` confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/initials/聲 以.md`: size 121 = ruby 121 = corpus 121, every character once in its own 注音's group; the prose's "all 120 characters confirm a y- glide in Mandarin" corrected from the character files (121 characters; Mandarin y- 112, w- 2, r- 5, q- 1, x- 1, with Cantonese j- for the r/q cases) and 羨 flagged (sibilant readings in Cantonese, Korean and Vietnamese); character file untouched; stamped 2026-11-13.
- `lookup/CC/initials/聲 云.md`: size 50 = ruby 50 = corpus 50, 49 ø + 彙 ㄏ re-counted, every character once in its own 注音's group; the Zhengzhang `/ɦʉiH/`, Baxter `hjw+jH` and Zhengzhang OC `*ɢruds` for 彙 read at en.wiktionary (彙) and now linked; stamped 2026-11-13.
- `lookup/CC/initials/聲 並.md`: size 99 = ruby 99 = corpus 99, every character once in its own 注音's initial group, counts 84/12/3 recomputed; the tone-conditioned aspiration claim now cites Wikipedia (Historical Chinese phonology, read; stops only, tone 1) with its limits stated; 佩/培/徘 shared final uʌi and their phonetic components taken from the character files; 皮/疲 noted as true homophones landing on ㄅ and ㄆ; stamped 2026-11-13.
- `lookup/CC/finals/韻 侵B.md`: fixed three un-aliased ruby links (金, 陰, 飲 carry " (char)" in their filenames), so size 21 = ruby 21 = corpus 21 with every character matched; prose: row 140 cited for `im/um/om`, velar scatter now includes 欽, 琴/禽 added as true homophones in different groups, 錦 diagnosed as a crowding escape (initial and vowel both change), from the character files; stamped 2026-11-13.
- `lookup/CC/finals/韻 侵A.md`: fixed two un-aliased ruby links (淫 and 針 filenames carry " (char)"), so size 25 = ruby 25 = corpus 25 with every character matched; prose: the table's winner is the dual `im/um` (row 139 of 文法 - 99韻図) and the ㄨㄇ group is its `um` half; 凜/懍 corrected from near- to true homophones (identical Mandarin, Cantonese, Korean readings); 稟/冘 labial note; 冘's mistag flag kept, character file untouched; stamped 2026-11-13.
- `lookup/CC/finals/韻 侯.md`: size 52 = ruby 52 = corpus 52, value əu (U+0259) matches, every character once in its own 注音's group, finals-only labels; prose corrected from the character files (後 is a true homophone of 候 and 后; the ㄏㄛㄨ slot has six members; 兜's crowded slot is the 5-member ㄉㄛㄨ, not 6 incl. 頭); the 咅 data-quality flag revised using en.wiktionary (咅: Cantonese tau3, MC initial 透 tʰ, final 侯), which supports tau3 and puts the oddity in the corpus's pʰ; character file left as is; Vowels-table `ou` confirmed in row 137 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 佳開.md`: size 22 = ruby 22 = corpus 22, every character once in its own 注音's group, finals-only labels; removed the link to the AIOS skill page and the unrechecked "9/9 zero exceptions" count from the prose; added the 崖/涯/厓 true-homophone three-way split, the 娃/矮 note and 擺 as a crowding escape (ㄅㄚㄧ and ㄆㄚㄧ both full), from the character files; Vowels-table `ai/yai` confirmed in row 031 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 佳合.md`: size 3 = ruby 3 = corpus 3, every character once in its own 注音's group, finals-only labels; the prose's "tracks the aspiration difference" corrected (that explains 咼's initial ㄎ, not its y-glide; its Mandarin, Cantonese, Korean and Vietnamese readings give no y-glide support, so the glide is unconditioned); Vowels-table `wai` confirmed in row 032 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 仙B三開.md`: size 11 = ruby 11 = corpus 11, every character once in its own 注音's group, finals-only labels; 展/纏 re-diagnosed as the phonotactic constraint (ㄐ cannot take a y-glide) instead of "no explanation"; 諺 left as an unconditioned glide-drop, paralleled by 彦 on 仙A三開, from the character files; Vowels-table `yen/en` confirmed in row 079 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 仙B三合.md`: size 12 = ruby 12 = corpus 12, every character once in its own 注音's group, finals-only labels; the prose's "y-glide-bearing half" corrected to the w-glide `wen` half of the Vowels table's `wen/on` (row 080 of 文法 - 99韻図); 媛 diagnosed as a true homophone of 院 and 援 as close but not identical, from the character files; stamped 2026-11-13.
- `lookup/CC/finals/韻 仙A三開.md`: size 42 = ruby 42 = corpus 42, every character once in its own 注音's group, finals-only labels; group count corrected from 25-15 to 25-16 (+鮮 alone); 然/肰 diagnosed as true homophones (same readings, split anyway) and 這 flagged for its unusual readings vs 彦, from the character files; Vowels-table `yen` confirmed in row 077 of 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 仙A三合.md`: size 24 = ruby 24 = corpus 24, every character once in its own 注音's group, finals-only labels; group counts (9 ㄝㄋ, 8 ⼔ㄋ, the j-initial 鳶縁鉛 vs 沿) and the Vowels-table dual winner `yen/wen` (row 078 of 文法 - 99韻図) re-checked against the character files; the 串/川 passage corrected (they differ in the initial ㄐ/ㄑ as well as the coda, and 串's Vietnamese quán is also an outlier); stamped 2026-11-13.
- `lookup/CC/finals/韻 乏.md`: size 9 = ruby 9 = corpus 9, every character once in the group matching its own 注音; the readings behind the prose (姂/乏 true homophones fá, fat6, 핍; 灋 = 法's fǎ, faat3, 법; 猲 kʰ with 怯; 脅 alone) re-read from the character files; 灋's MC initial p (not f) added to the prose; Vowels table row 148 (iap, D `ap`) confirmed in 文法 - 99韻図; stamped 2026-11-13.
- `lookup/CC/finals/韻 之.md`: loop switched from characters/words/chengyu to the CC pages (oldest date-last-perfect first). Checked: size 91 = ruby entries 91 = characters carrying final ɨ in the corpus; every character exactly once, each in the group matching its own 注音; final-only labels; the prose counts (67 ㄧ; the ㄙ-initial split 9 ㄧ / 8 ㄚ / 4 ㄜ; 俟 and 士 singletons; 士's initial shared only by 事 in this final) recomputed from the corpus; the Vowels-table winner `i` confirmed in row 019 of 文法 - 99韻図; stamped 2026-11-13.

### Oldest-page pass (characters, words, chengyu)

- `chengyu/風声鶴唳.md`: 晉書 卷114 (苻堅下) read at Wikisource and linked; the page's long quotation (餘眾棄甲宵遁…死者十七八), wrongly placed in that chapter, replaced by the text's real sentence 聞風聲鶴唳，皆謂晉師之至 with its context; examples labelled constructed; stamped 2026-11-13.

- `chengyu/電光石火.md`: 景德傳燈錄 卷24 (石火電光已經塵劫, entry 保壽匡祐) and 五燈會元 卷7 (保福從展, X1565) lines read at the deerpark.app CBETA reader and linked; the reader's punctuation noted; examples labelled constructed; stamped 2026-11-13.

- `chengyu/雲昼火夜.md`: Exodus 13:21 和合本 read at Wikisource and linked (quotation and example 2 corrected: no comma after 日間, 、/． punctuation); KJV and parallel passages flagged unrechecked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/除我莫神.md`: Isaiah 45:5 and Exodus 20:3 和合本 read at Wikisource and linked; Source quotation corrected and example 2's non-text wording (我是耶和華，再沒有別神；…) replaced by the real verse; KJV not re-checked; examples marked; stamped 2026-11-13.

- `chengyu/阿鼻叫喚.md`: the eight hot hells' order (叫喚 fourth, 阿鼻 eighth) confirmed at zh.wikipedia and linked; the 往生要集 / 俱舍論 statements and the compound's origin left marked unverified as already recorded; examples labelled constructed; stamped 2026-11-13.

- `chengyu/鏡花水月.md`: 滄浪詩話 (卷1 §五) and 品花寶鑒 序 read at Wikisource and linked (the latter's punctuation noted; 鑑→鑒 in the title); the 楞嚴經 non-find left as recorded; examples labelled constructed (example 1 had been presented like a quotation); stamped 2026-11-13.

- `chengyu/銀盤呈首.md`: Mark 6:28 和合本 read at Wikisource and linked (quotation/example 2 corrected: 盤子裏, 他母親, 、 punctuation); the KJV/Greek statements and Matthew 14 not re-checked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/金科玉律.md`: 劇秦美新 sentence confirmed verbatim at Wikisource and linked; Matthew 7:12 和合本 read at Wikisource, linked and its punctuation corrected; example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/金城湯池.md`: 漢書 卷45 蒯通 sentence confirmed verbatim at Wikisource and linked; Japanese field and Pronunciations historical kana きんじやうたうち corrected to modern きんじょうとうち; examples labelled constructed; stamped 2026-11-13.

- `chengyu/重文軽武.md`: 儒林外史 第46回 line confirmed at Wikisource and linked; 二刻拍案驚奇 卷17 line confirmed only on a secondary reading site (5000yan, simplified; Wikisource 404, ctext blocked) and linked with that said in-page; the 新唐書 removal note kept; examples marked; stamped 2026-11-13.

- `chengyu/邪心常悪.md`: Genesis 6:5 and 8:21 和合本 read at Wikisource and linked (quotations and example 2 corrected: 、/． punctuation, 心裏, 懷着, 纔); cnbible.com/新譯本/KJV claims flagged unrechecked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/選士唯賢.md`: Dan'a'yo-coined; 墨子·尚賢上 sentence confirmed at Wikisource (爲 form) and linked; 科挙 history claims marked unchecked; examples marked (1 real, 2–4 constructed); stamped 2026-11-13.

- `chengyu/遠交近攻.md`: 史記·范雎蔡澤列傳 (卷079) sentence confirmed verbatim at Wikisource and linked; example 1 corrected (得寸則王之寸也, with 也); biographical/background statements and 三十六計 numbering marked unrechecked; examples marked; stamped 2026-11-13.

- `chengyu/道活墨殺.md`: 2 Corinthians 3:6 和合本 read at Wikisource and linked (quotation/example 2 corrected: 憑着, 因爲, ．/、 and the 精意或作聖靈 note); cnbible.com/新譯本/標準譯本/KJV/Greek claims flagged unrechecked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/造人像形.md`: Genesis 1:26 和合本 read at Wikisource and linked (quotation and example 2 corrected: 照着, 按着, 、 punctuation); cnbible.com/現代標點和合本/新譯本/KJV claims flagged unrechecked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/轄魚鳥牲.md`: Genesis 1:26 和合本 read at Wikisource and linked (quotation and example 2 corrected: 海裏, 照着, 按着, 、 punctuation); removed a duplicated sentence about 轄; cnbible.com/新譯本/KJV claims flagged unrechecked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/起死回生.md`: 史記·扁鵲倉公列傳 (卷105) sentence re-read at Wikisource and linked (the earlier check had no link); the quoted wording matches; the surrounding diagnosis/treatment account is the usual telling and not re-read; examples labelled constructed; stamped 2026-11-13.

- `chengyu/貪官汚吏.md`: 鴛鴦被 line read in the 元曲選 text (ccddb.net) and linked, replacing the "search summary" check: the text is 敕賜勢劍金牌。一應貪官污吏。准許先斬後聞。, spoken by 李府尹; same in example 2; 論語 2:1 confirmed at Wikisource and linked; examples marked; stamped 2026-11-13.

- `chengyu/諸行無常.md`: 大般涅槃經 T374 卷14 (聖行品) verse read at the deerpark.app CBETA reader and linked; the Heike Monogatari opening, 雪山童子 and iroha statements flagged unchecked; examples labelled constructed; stamped 2026-11-13.

- `chengyu/諸法無我.md`: 大智度論 卷22 三法印 sentence linked (Wikisource, simplified page) and 卷15's 一切法無我印 passage read at the deerpark.app CBETA reader and linked (its third seal reads 涅槃實法印); examples labelled constructed; stamped 2026-11-13.

- `chengyu/論功行賞.md`: 隋書·蘇威傳 sentence now read in the text at Wikisource (隋書/卷41) and linked, replacing "checked against the Ministry's entry"; examples marked (1 real, 2–4 constructed); stamped 2026-11-13.

- `chengyu/誠心誠意.md`: 禮記·大學 passage read at Wikisource and linked; quotation corrected to the text's 脩 and full stops; examples labelled constructed; stamped 2026-11-13.

- `chengyu/詞彙兼容.md`: Dan'a'yo-coined, no external source to check; readings agree with the four character pages, back-links present, 語用 link and all nine linked sister mottos confirmed to exist; the historical remarks on Confucian/Buddhist term borrowing are background, unsourced on the page; examples labelled constructed; stamped 2026-11-13.

- `chengyu/詛地哀食.md`: Genesis 3:17 和合本 read at Wikisource and linked (quotation and example 2 corrected: 爲, 纔, 地裏, 喫, ．/、); cnbible.com/新譯本/KJV claims flagged unrechecked; sister-chengyu links confirmed; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/言行一致.md`: 邵氏聞見後錄 卷二十 read at Wikisource and linked; quotation replaced with the text's wording (自茲…遇事坦然有余地矣) and the speaker corrected (Sima Guang's own seven-year practice, recounted by Liu Anshi, not Liu Anshi's); the 元城語録/仕學規範 claim marked unchecked; 論語 4.24 confirmed and linked; examples labelled constructed; stamped 2026-11-13.

- `chengyu/覧昭和決.md`: Dan'a'yo-coined; the 1946/1949 reform dates confirmed at en.wikipedia (Tōyō kanji) and linked (the table's name not seen there); readings agree with the four character pages, back-links and 文字法 link confirmed; examples labelled constructed; stamped 2026-11-13.

- `chengyu/蒼海桑田.md`: 神仙傳 麻姑 passage found at Wikisource 卷三 (not 卷七) and read; quotation corrected (麻姑自說：, 水又淺於往昔，會時略半也, 豈將復還為陵陸乎, 海中行復揚塵也) and linked, replacing the secondary-page wording; example 1 aligned (no final full stop), marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/荊棘荻蓬.md`: Genesis 3:18 和合本 read at Wikisource and linked (quotation/example 1 corrected: 喫, 、 punctuation); cnbible.com/新譯本/ESV claims flagged unrechecked; Japanese field and Pronunciations katakana → hiragana (けいきょくてきほう); example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/茫然自失.md`: 列子·仲尼 sentence confirmed verbatim at Wikisource (仲尼篇) and linked; surrounding-context account and the 孟子·滕文公上 claim for 茫然若失 marked unrechecked; examples labelled constructed; stamped 2026-11-13.

- `chengyu/色即是空.md`: 心經 (T251, Xuanzang) passage read at the CBETA-based deerpark.app reader and linked (original punctuation recorded); film 色即ぜねれいしょん corrected from 2019 to 2009 (ja.wikipedia, linked); Kumārajīva/649 CE claims marked unchecked; example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/自由自在.md`: 景德傳燈錄 卷23 read at the CBETA-based deerpark.app reader and linked (entry 衡州華光範禪師); the quotation corrected: the first answer is 自由。自在。 (two words), only the second is 自由自在, not both; 西遊記 ch. 5 sentence confirmed at Wikisource and linked; examples labelled constructed; stamped 2026-11-13.

- `chengyu/自業自得.md`: 正法念處經 卷7 verse (非異人作惡…眾生皆如是) re-read at the CBETA-based deerpark.app reader and linked (地獄品之三, spoken by Yama's attendants); the earlier LaṅkĀvatāra non-find and the 佛學大辭典 remark left as recorded, unrechecked; example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/自暴自棄.md`: 孟子·離婁上 section 10 re-read at Wikisource and the link added (the earlier check had no link); the quotation matched (page has 有為, text 有爲, as already noted); examples labelled constructed; stamped 2026-11-13.

- `chengyu/臥薪嘗胆.md`: 史記 卷41 (越王句踐世家) and 擬孫權答曹操書 (attributed to Su Shi) read at Wikisource and linked, variant forms (呉 旣 句踐 卽) noted; the 伍子胥 claim marked unchecked; example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/義重於音.md`: Dan'a'yo-coined, no external source to check; readings agree with the four character pages, back-links present, 語用 link and linked sister mottos (義以立名, 信達雅化 etc.) exist; the Yan Fu 信達雅 remark is background, unsourced on the page; examples labelled constructed; stamped 2026-11-13.

- `chengyu/義以立名.md`: Dan'a'yo-coined, no external source to check; readings agree with the four character pages, back-links present, 語用 link and all ten linked sister mottos confirmed to exist; examples labelled constructed; stamped 2026-11-13.

- `chengyu/羊衣餓狼.md`: Matthew 7:15 和合本 read at Wikisource and linked; quotation and example 2 corrected to that text (這裏, 披着, 裏面, ． and 、); cnbible.com/新譯本/KJV/Greek claims flagged unrechecked; example 2 marked real, others constructed; stamped 2026-11-13.

- `chengyu/結髪夫妻.md`: 留別妻 (opening line, listed under Su Wu) and 古詩為焦仲卿妻作 (結髮同枕席，黃泉共為友) read at Wikisource and linked; the line's context corrected (the husband speaks to his mother, not pleads against sending his wife away) and the poem's ending marked unrechecked; examples 1–2 marked real, 3–4 constructed; stamped 2026-11-13.

- `chengyu/糟糠之妻.md`: 後漢書 卷26 宋弘 passage read at Wikisource and linked; quotation marks around 貴易交，富易妻 added to match the text; the text's 其竭 (vs the page's 其意) noted, not changed; examples labelled constructed; stamped 2026-11-13.

- `chengyu/粉骨砕身.md`: 石灰吟 read at Wikisource and linked (that text has 千錘萬击 and 全不顧/一作怕; the page's 全不怕 form noted as the variant); example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/空前絶後.md`: 登幽州臺歌 confirmed at Wikisource and linked; zh.wiktionary page read (no origin given, noted); example 1 marked as the real poem, not containing the idiom; examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/禍延子孫.md`: 朱子家訓 sentence (禍延子孫) read at Wikisource and linked (semicolon, not full stop, between clauses); 周易·坤·文言 line linked; Exodus 20:5 和合本 read at Wikisource and linked, quotation/example 2 given in that text's punctuation, cnbible.com/新譯本/KJV claims flagged unrechecked; examples labelled; stamped 2026-11-13.

- `chengyu/磨穿鉄硯.md`: 新五代史 卷29 桑維翰 sentence confirmed verbatim at Wikisource and linked; example 1 (an unconfirmed 舊五代史 wording) replaced by that real line; the 舊五代史/春渚記聞/923–926 statements marked unrechecked; examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/破頭傷足.md`: Genesis 3:15 和合本 read at Wikisource and linked (quotation corrected to 脚跟, 、 punctuation, also in example 1); Vulgate wording confirmed at la.wikisource and linked; Hebrew/LXX/Irenaeus statements flagged unrechecked; examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/盛衰栄辱.md`: 周易 雜卦 and 繫辭上 ch. 8 lines re-confirmed verbatim at Wikisource and linked; Zdic/MOE-entry claims still unopened and marked so; example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/百聞不如一見.md`: 漢書·趙充國辛慶忌傳 (Wikisource 卷069) opened and linked; quotation corrected (上遣問焉，曰 / 充國曰 / comma after 一見, not 上曰 / 充國對曰 / full stop) and example 3's invented 老將軍對曰 replaced by the real wording; examples 1, 2, 4 labelled constructed; stamped 2026-11-13.

- `chengyu/百家共承.md`: Dan'a'yo-coined, no external source to check; readings agree with the four character pages, back-links present, 語用 link and the eight linked sister mottos confirmed to exist; examples labelled constructed; stamped 2026-11-13.

- `chengyu/白頭偕老.md`: 詩經·擊鼓 couplet re-confirmed at Wikisource and linked; the 教育部《成語典》 citations (白頭吟, 女曰雞鳴, 婁堅, 懷香記, 浮生六記) now read via the school-hosted copy and listed with their quoted sentences (flagged as not checked against the texts); example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/異体不容.md`: Dan'a'yo-coined; 書同文 line confirmed (史記·秦始皇本紀, Wikisource) and linked, with the 小篆 detail flagged as beyond that line; 康熙字典 date/entry count confirmed at Wikipedia and linked, "majority are variants" flagged unchecked; examples labelled constructed; stamped 2026-11-13.

- `chengyu/画龍点睛.md`: 歴代名畫記 卷七 (四庫全書本 on Wikisource) opened and linked, replacing "secondary pages, Wikisource would not load"; passage confirmed (variant 㸃/湏 forms noted; the page's leading 又 not seen in the excerpt); examples labelled constructed; stamped 2026-11-13.

- `chengyu/画蛇添足.md`: 戰國策·齊策二 (Wikisource 卷09, 昭陽為楚伐魏) opened and linked, replacing "checked against a search summary"; quotation orthography corrected to the text's 巵 and 飲; unread middle sentences flagged in-page; examples labelled constructed; stamped 2026-11-13.

- `chengyu/生机勃勃.md`: 《創業》 citation was credited to the 教育部《成語典》 via a search summary; opened both pages: the 成語典 entry has no 創業/張天民 citation (only a definition and a garden example), the 成語字典 (chinesewords.org) page does; Source now says so, with both links; examples labelled; stamped 2026-11-13.

- `chengyu/瑠璃清天.md`: Exodus 24:10 和合本 read at Wikisource and linked; quotation corrected to that text (脚, 、 punctuation) in Source and example 1; earlier cnbible.com / 新譯本 claims flagged unrechecked; Japanese field and Pronunciations katakana → hiragana (るりせいてん); example 1 marked real, 2–4 constructed; stamped 2026-11-13.

- `chengyu/珠投猪前.md`: Matthew 7:6 和合本 read at Wikisource and linked; quotation corrected to that text (他 not 牠, 、 punctuation) in Source and example 2; earlier cnbible.com / 新譯本 / 標準譯本 claims flagged unrechecked; example 2 marked as the real verse, others constructed; stamped 2026-11-13.

- `chengyu/玩世不恭.md`: 漢書·東方朔傳贊 line confirmed at Wikisource and linked (context corrected: it is Dongfang Shuo's advice to his son, quoted by Ban Gu); 《雪蓑道人傳》 quotation confirmed as cited on chinesewords.org and linked, still not in a primary text; 教育百科 entry noted; examples labelled constructed; stamped 2026-11-13.

- `chengyu/焚琴煮鶴.md`: 義山雜纂 殺風景 list opened at Wikisource and linked; example 1 (a six-item list that is not in the text) replaced by the real consecutive items; removed the claim that the list carries a 《西清詩話》 note (it sits under 七不稱意); examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/焚書坑儒.md`: 史記·秦始皇本紀 (Wikisource 卷006) opened and linked; the "verbatim" claim fixed: the text has 制曰：「可。」 (not 始皇可其議), 皆阬之咸陽 (阬, not 坑), and 悉詣守、尉; same corrections in example 1; Heine's "1820" date marked unchecked; examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/混然一体.md`: 識仁篇 passage located in 二程遺書 卷二上 at Wikisource and linked; quotation corrected (the page had called 仁者，渾然與物同體 the opening line and joined it with the next clause using 智; the text opens 學者須先識仁。仁者，渾然與物同體。義、禮、知、信，皆仁也。); origin of the title 識仁篇 not checked; examples labelled constructed; stamped 2026-11-13.

- `chengyu/涅盤寂静.md`: 大智度論 卷22 三法印 sentence confirmed at Wikisource (simplified-character page; CBETA reader showed no text) and linked, replacing the unlinked "checked against the CBETA text"; the 根本說一切有部毘奈耶 claim stays flagged unverified; examples labelled constructed; stamped 2026-11-13.

- `chengyu/海闊天空.md`: opened the 教育部《成語典》 entry directly (was "as reported by a search summary"), confirmed the 庾信〈道士步虛詞〉 line and the 成語典's own reserve (「也許就從這裡演變而出」), linked it; later 書證 listed as read only on that page; examples labelled constructed; stamped 2026-11-13.

- `chengyu/流言飛語.md`: 尚書·金縢 and 史記·魏其武安侯列傳 (卷107) quotations confirmed verbatim at Wikisource and linked; Korean field and Pronunciations changed from South Korean 유언비어 to North Korean 류언비어 (standing rule), the 두음법칙 note rewritten to say so; examples labelled constructed; stamped 2026-11-13.

- `chengyu/波乱万丈.md`: 太平廣記 卷346 (story 《李湘》) opened at Wikisource and linked; example 1 still carried the old wrong wording (其心波瀾萬丈，嫉妒相仇，猛於禽獸) that contradicted the page's own Source section, now replaced with the verified line; examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/沈魚落雁.md`: 莊子·齊物論 quotation confirmed verbatim at Wikisource and linked; the Four Beauties assignments (西施 沉魚, 王昭君 落雁, 貂蟬 閉月, 楊玉環 羞花) confirmed at Wikipedia and linked; example 2 no longer labelled "Classical" (no source traced for the 沈魚落雁之容，閉月羞花之貌 pairing); examples 3–4 labelled constructed; stamped 2026-11-13.

- `chengyu/汗食帰泥.md`: Genesis 3:19 和合本 read at Wikisource and linked; quotation corrected to the text's forms (纔得餬口, 因爲, 、/． punctuation) in Source and example 2; the earlier cnbible.com claim and 新譯本 wording flagged unrechecked; examples 1, 3, 4 labelled constructed; stamped 2026-11-13.

- `chengyu/毎字明意.md`: Dan'a'yo-coined, no external source to check; readings agree with the four character pages, back-links present, 文字法 link confirmed; examples labelled constructed; stamped 2026-11-13.

- `chengyu/殺姦窃偽.md`: Exodus 20:13–16 (和合本) read in full at Wikisource and linked (replaces the partial cnbible.com check); Japanese field and Pronunciations switched from katakana to hiragana (さつかんせつぎ); examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/欲求不満.md`: 道德經 ch. 37 checked at Wikisource and linked (quotation extended to 無名之樸，夫亦將無欲…); the Lin Zexu couplet's "1839" now confirmed and linked at Wikipedia (越華書院 visit, 10 March 1839); examples labelled constructed; stamped 2026-11-13.

- `chengyu/欲夫治汝.md`: Genesis 3:16 和合本 checked at Wikisource and linked (cnbible.com unreachable this pass, so the earlier "checked on cnbible.com" claim and the 新譯本 wording are flagged unrechecked; KJV clause not re-read); example 2 marked as the real verse, others constructed; stamped 2026-11-13.

- `chengyu/欣喜雀躍.md`: 水滸傳 (120回本) 第108回 and 莊子·在宥 opened at Wikisource and linked; 九分九釐 corrected to the text's 九分九厘; 拊髀/脾 variant noted; examples labelled constructed; stamped 2026-11-13.

- `chengyu/森羅万象.md`: example 1 (森羅万象，無非真如, an invented Buddhist-sounding line) replaced by the 陶弘景 line actually quoted in the 佛學大辭典 entry; that entry read on Wikisource and linked (法句經 line still unconfirmed in a primary text; searches suggest 一法之所印 may belong to 華嚴/禪 commentary, not noted in-page); examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/東奔西走.md`: Source rewritten from the 教育部《成語典》 entry (linked): the Wei Chu line is verified, but the 成語典 titles the poem 〈自揣平生〉 whereas the page's origin says 〈留別次張周卿韻〉 (left as is, discrepancy noted in-page); removed the unverified later lines and the unsupported "checked against 青崖集"; 西遊記 ch. 35 quotation corrected to the 成語典's wording and marked as read on a secondary page; examples labelled constructed; stamped 2026-11-13.

- `chengyu/東亜自通.md`: Dan'a'yo-coined, no external source to check; readings agree with the four character pages, back-links present, 序文 link confirmed; examples labelled constructed; stamped 2026-11-13.

- `chengyu/朽木糞牆.md`: 論語·公冶長 5.10 checked at Wikisource and linked; second quotation's punctuation fixed (；於予與改是); examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/未雨紬謬.md`: 詩經·豳風·鴟鴞 quotation checked at Wikisource and linked (page punctuation 桑土。綢繆 matched); examples labelled constructed; noted the 紬/綢 and 謬/繆 variant claims were not re-checked; stamped 2026-11-13.

- `chengyu/朝鮮正音.md`: the "not re-checked" 1446 date for 訓民正音 now checked at Wikipedia (Hunminjeongeum) and linked, with the 1443 first presentation noted; examples labelled constructed; stamped 2026-11-13.

- `chengyu/朝三暮四.md`: opened Wikisource 莊子/齊物論 and linked it; quotation punctuation fixed (comma after 名實未虧), noted the text's bracketed 而 and 衆/爲 forms; examples labelled constructed; stamped 2026-11-13.

- `chengyu/暴飲暴食.md`: confirmed 飲食自倍，腸胃乃傷 is in 素問·痺論篇第四十三 (Wikisource 四部叢刊本 卷第十二) and replaced the "chapter unidentified" caveat with the link; confirmed 食不厭精，膾不厭細 in 論語·鄉黨 and linked it; examples 2–4 labelled constructed; stamped 2026-11-13.

- `chengyu/暗送秋波.md`: opened Wikisource 三國演義 第八回, 菩薩蠻 (李煜) and 挂枝兒 (私窺 line) and linked all three beside their quotations; the 三國演義 quotation's punctuation now matches the text (。 between the two clauses); examples 1–3 labelled as constructed; stamped 2026-11-13.
- 春夏秋冬: opened 管子/第40篇四時 and 史記/卷130 on wikisource, confirmed both quotations and linked them in Source and Origin; labelled example sentences 2–4 as constructed; the 詩經 line and the claims about other season orders stay flagged as unchecked; back-links re-checked; lint clean; stamped.
- 日月星辰: opened 尚書/堯典 on wikisource, confirmed the quoted sentence and linked it in Source and Origin; back-links re-checked; the cosmology interpretation stays flagged as unchecked; lint clean; stamped.
- 旗幟鮮明: opened 列子/黃帝篇 and 漢書/卷072 on wikisource, confirmed both quotations word for word and linked them in Source and Origin; back-links re-checked; lint clean; stamped.
- 文音共決: 単亜語 orthographic maxim with no external source (nothing to link); linked chengyu and back-links re-checked; no change needed; lint clean; stamped. Open question for the user: this page says Literary Dan'a'yo allows no exception to the ruby rule, while 声形和決 lets the phonetic layer be omitted under space constraints.
- 文質彬彬: opened 論語/雍也第六 on wikisource, confirmed the quotation and linked it (verse numbering differs by edition, now noted); removed the Usage Note, which was prose about the 諺文/Korean difference (kwin commentary the vault does not keep); linked words and back-links re-checked; lint clean; stamped.
- 文言現代: 単亜語 syntax principle with no external source (nothing to link); checked it against 文言継承, 現代適応 and 文法 - 04句法, which agree with it (including SVO語順 as part of 現代適応); back-links re-checked; no change needed; lint clean; stamped. Open question for the user: 先題後述 and 形助顕理 describe SVO as incidental while 現代適応 names SVO語順 as a principle.
- 文体並存: 単亜語 register principle with no external source (nothing to link); the many linked chengyu and the grammar page and back-links re-checked; no change needed; lint clean; stamped.
- 招災引禍: opened 聖經 (和合本)/加拉太書 on wikisource, confirmed Galatians 6:7 and linked it; labelled example sentences 1 and 4 as constructed; the 招災惹禍 and 《巧團圓》 remark stays flagged as unchecked; linked words and back-links re-checked; lint clean; stamped.
- 成家立業: opened 孟子/滕文公上 on wikisource, confirmed 「民之為道也…」 and linked it; labelled Example Sentence 1 as a real quotation that does not contain the phrase and examples 2–4 as constructed; the Zdic 《夢粱錄》 passage still could not be reached, so it stays as reported (no link); back-links re-checked; lint clean; stamped.
- 愛隣如自: opened 聖經 (和合本) 利未記 and 馬太福音 on wikisource, confirmed Leviticus 19:18 and Matthew 22:39 (愛人如己) and linked both in Source and Origin; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; back-links re-checked; lint clean; stamped.
- 愛主耳錐: opened 聖經 (和合本)/出埃及記 on wikisource, confirmed Exodus 21:5–6 and linked it in Source and Origin (noting its orthographic variants); Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; back-links re-checked; lint clean; stamped.
- 意味深長: opened 晦菴集卷四十七 on wikisource, confirmed the 答呂子約 sentence and linked it in Source and Origin; Example Sentence 1 still gave the removed 《朱子語類》 quotation (dated 1270), replaced with the verified letter sentence; the 答張敬夫 quotation has no link yet; back-links re-checked; lint clean; stamped.
- 形助顕理: 単亜語 morphology maxim with no external source (nothing to link); replaced two mentions of an "SVO framework" with the language's own topic-comment, modifier-first structure so the page agrees with 先題後述 and 修飾先行; linked chengyu and back-links re-checked; lint clean; stamped.
- 弱肉強食: opened 送浮屠文暢師序 on wikisource, confirmed the quoted passage word for word and added the link to Source and Origin; back-links re-checked; the Meiji/Social Darwinism remark stays flagged as unchecked; lint clean; stamped.
- 弱不禁風: Example Sentence 1 gave an invented couplet dated "1196" as Lu You; replaced it with the real line from 《劍南詩稿》卷三十四 already quoted in Source and Origin; relabelled the Daiyu example as constructed (the phrase is not in 《紅樓夢》) and hedged the Cultural Notes' Daiyu remark; back-links checked; lint clean; stamped.
- 引出奴家: Exodus 20:2 citation (KJV and 和合本, already checked on cnbible.com), linked words and back-links re-checked; no change needed; lint clean; stamped.
- 左由右至: 単亜語 stroke-order term with no external citation; flagged the three regional phrasings of the rule as unchecked; linked pages and back-links re-checked; lint clean; stamped.
- 少即是多: 《道德經》 chapter 48 quotation (already checked on wikisource) and back-links re-checked; Browning and Mies attributions already flagged on the page as not read at source; no change needed; lint clean; stamped.
- 尊王攘夷: Example Sentence 1 still quoted the Gongyang line 「葵丘之盟，尊周室，攘夷狄…」 that the Source section had removed as not found in the text; replaced it with the checked 僖公四年 sentence; removed the alias that duplicated the page's own name; 《論語·憲問》 remark left flagged as not re-checked; back-links checked; lint clean; stamped.
- 尊敬父母: Exodus 20:12 citation (KJV and 和合本, already checked on cnbible.com), linked words and chengyu and back-links re-checked; no change needed; lint clean; stamped.
- 対牛弾琴: 《牟子理惑論》 passage (already checked on wikisource) and back-links re-checked; replaced the Korean example sentence, which used the vernacular phrase the page had removed as unattested, with one using 대우탄금; lint clean; stamped.
- 安心立命: corrected the 《孟子·盡心上》 quotation to the wikisource wording 存其心，養其性 (the page had the contracted 存心養性) and made Example Sentence 2 match the 《景德傳燈錄》 wording already quoted in Source and Origin; back-links re-checked; lint clean; stamped.
- 孤立無援: 《後漢書·班梁列傳》 passage (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 孝親天賜: Exodus 20:12 and Ephesians 6:2–3 citations (KJV and 和合本, already checked on cnbible.com) and back-links re-checked; no change needed; lint clean; stamped.
- 天衣無縫: replaced Example Sentence 1, which gave an invented dialogue under the old title 《靈怪録·郭翰》, with the verified 《太平廣記》卷六十八 wording already quoted in Source and Origin (source named 《靈怪集》); back-links re-checked; lint clean; stamped.
- 天真乱漫: Gong Kai citation (Ministry of Education entry, as the page states) and 《莊子·漁父》 passage (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 天圓地方: 《淮南子·天文訓》 and 《大戴禮記·曾子天圓》 passages (already checked on wikisource; the 晉書 attribution stays flagged as unverified) and back-links re-checked; no change needed; lint clean; stamped.
- 大器晩成: 《道德經·第四十一章》 passage (already checked against the text) and back-links re-checked; flagged the account of how the idiom's sense shifted across dynasties as an unchecked interpretation; lint clean; stamped.
- 大同小異: 《莊子·天下》 passage (already checked against the text, idiom noted as not in it) and back-links re-checked; flagged the Cultural Notes' frequency and register comparisons as unchecked; lint clean; stamped.
- 多召少選: Matthew 22:14 citation (ESV and Chinese versions, already checked on cnbible.com) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 声形和決: 単亜語 orthographic principle with no external citation; linked grammar page and back-links re-checked; the remarks on furigana, Taiwanese Bopomofo pedagogy and historical Korean systems were not looked up; lint clean; stamped.
- 塩地光世: Matthew 5:13–14 citation (KJV and the Chinese versions, already checked on cnbible.com) and back-links re-checked; no change needed; lint clean; stamped.
- 因果報応: 《大唐大慈恩寺三藏法師傳》卷七 quotation (already checked in the CBETA text), linked words and back-links re-checked; no change needed; lint clean; stamped.
- 因小失大: 《劉子·貪愛》 passage (already checked on wikisource, with later fiction uses noted) and back-links re-checked; no change needed; lint clean; stamped.
- 四面楚歌: 《史記·項羽本紀》 passage (already checked on wikisource, with the 皆 compression noted) and back-links re-checked; no change needed; lint clean; stamped.
- 呵呵大笑: 《景德傳燈錄》 occurrences (already checked in the CBETA text) and linked word and back-links re-checked; no change needed; lint clean; stamped.
- 呉越同舟: could not load the 孫子 text itself on wikisource; added two secondary quotations found there (《長短經》 under 孫子曰, and the parallel 《孔叢子》 passage via 《太平御覽》) to the caveat, which stays; back-links re-checked; lint clean; stamped.
- 呉牛喘月: 《世說新語·言語》 passage (already checked against the text) and back-links re-checked; no change needed; lint clean; stamped.
- 合漢再決: 単亜語 founding motto with no external citation; linked grammar page and back-links re-checked; no change needed; lint clean; stamped.
- 古今東西: no classical citation to check (origin "not established", as the page says); the Nakamura Masanao 1889 example and the interpretive remarks stay flagged as unchecked; back-links re-checked; no change needed; lint clean; stamped.
- 厚顔無恥: 《詩經·巧言》 and 《北山移文》 quotations (already checked against the texts) and back-links re-checked; no change needed; lint clean; stamped.
- 単刀直入: re-confirmed the 《景德傳燈錄》卷十二 quotation on wikisource (also in 《五燈會元》 and 《指月錄》); other citations were already checked on the page; back-links re-checked; no change needed; lint clean; stamped.
- 千差万別: confirmed the 《朱子語類》卷六十 sentence on wikisource and noted a 《指月錄》 use (undated) in Source and Origin; back-links re-checked; lint clean; stamped.
- 千山萬水: confirmed the 宋之問 poem title and line on wikisource and noted its variant reading 千里萬里; back-links re-checked; lint clean; stamped.
- 十人不滅: Genesis 18:32 citation (KJV and 和合本, already checked) and back-links re-checked; the minyan remark in Cultural Notes read as a stated later development and was not re-checked; no change needed; lint clean; stamped.
- 勿貪隣物: Exodus 20:17 citation (KJV, 和合本 and 新譯本, already checked) and back-links re-checked; no change needed; lint clean; stamped.
- 勿妄称名: Exodus 20:7 citation (KJV and 和合本, already checked) and back-links re-checked; no change needed; lint clean; stamped.
- 加哀痛産: Genesis 3:16 citation (KJV and 和合本, already checked) and back-links re-checked; the Hebrew-doubling remark stays flagged as unchecked; no change needed; lint clean; stamped.
- 刻舟求剣: confirmed the 《呂氏春秋·察今》 passage on wikisource (呂氏春秋/卷十五) and noted that later quotations (太平御覽, 事類賦) read 刻 for 契, which is closer to the idiom; back-links re-checked; lint clean; stamped.
- 内柔外剛: corrected a real error: the page listed 外柔內剛 as an interchangeable variant and alias, but it is the opposite idiom (soft outside, firm inside); replaced the alias with 外剛內柔 (a reordering with the same meaning) and rewrote Extended Meaning, Cultural Notes and Sentiment to follow Wiktionary ("tough outside, weak-willed or gentle within", neither praise nor blame); the 易經 passage and back-links re-checked; stamped.
- 六作一止: Exodus 20:9–10 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 公明正大: confirmed the 朱熹 sentence (公明正大之人用於世…) in 《晦菴集》卷七十六 and its attribution to 〈金華潘公文集序〉 (via 《易附錄纂註》) on wikisource; linked words and pages and back-links re-checked; no change needed; lint clean; stamped.
- 八紘一宇: tried to find the 日本書紀 line on Chinese wikisource and found it only quoted in a secondary document, so the page keeps its note that the quotation rests on Japanese Wikipedia; the disputed-date caveat for Tanaka Chigaku stays; linked word and back-links re-checked; no change needed; lint clean; stamped.
- 光明正大: confirmed the 《朱子語類》卷十五 quotation (洞然光明正大…) on wikisource; removed the alias 公明正大, which is the name of its own chengyu page (and which the Cultural Notes already treat as a separate close synonym); linked pages and back-links re-checked; stamped.
- 先題後述: 単亜語 grammar term with no external citation; linked grammar and chengyu pages and back-links re-checked; the Li and Thompson topic-prominence remark left as written (not re-read); no change needed; lint clean; stamped.
- 先画後点: 単亜語 stroke-order term with no external citation; flagged the Chinese and Japanese phrasings of the rule as unchecked; linked word and back-links re-checked; lint clean; stamped.
- 先横後豎: 単亜語 stroke-order term with no external citation; flagged the three regional phrasings and the 勒/努 stroke names as unchecked; linked pages and back-links re-checked; lint clean; stamped.
- 先撇後捺: 単亜語 stroke-order term with no external citation; flagged the three regional phrasings of the rule as unchecked; linked page and back-links re-checked; lint clean; stamped.
- 先外後内: 単亜語 stroke-order term with no external citation; flagged the three regional phrasings of the rule as unchecked; linked page and back-links re-checked; lint clean; stamped.
- 先填後閉: 単亜語 stroke-order term with no external citation; flagged the Chinese and Japanese phrasings of the rule as unchecked; linked page and back-links re-checked; lint clean; stamped.
- 先中後両: 単亜語 stroke-order term with no external citation; flagged the three regional phrasings of the rule as unchecked; linked pages and back-links re-checked; lint clean; stamped.
- 傍若無人: 《史記·刺客列傳》 quotation (already checked against the text, with the original spelling 旁 noted) and back-links re-checked; no change needed; lint clean; stamped.
- 修飾先行: 単亜語 grammar term with no external citation; replaced "the Altaic members of the Sinosphere" (a contested grouping) with "Japanese and Korean"; linked grammar page and back-links re-checked; lint clean; stamped.
- 信達雅化: 単亜語 coinage built on 嚴復's 信達雅 (《天演論》譯例言 quotation already checked on wikisource); linked page and back-links re-checked; no change needed; lint clean; stamped.
- 佳人薄命: 蘇軾《薄命佳人》 citation (already checked on wikisource) and back-links re-checked; unverified remarks about the Edo period and Truyện Kiều remain flagged on the page; no change needed; lint clean; stamped.
- 頑固: all five readings and the stubborn/obstinate senses (including the medical "hard to treat" sense) confirmed on Wiktionary; stand-in note (頑 points to 頑固), kwin, lexipedia placement and back-links checked; no change needed; stamped.
- 面疱: Mandarin, Cantonese and Japanese readings (めんぽう, with にきび as the common word) and the acne sense confirmed on Wiktionary under 面皰 (no Korean or Vietnamese there); stand-in note (疱 points to 面疱), kwin, lexipedia placement and back-links checked; no change needed; stamped.
- 銀色: Mandarin, Cantonese and Japanese readings and the silver-colour sense confirmed on Wiktionary (no Korean or Vietnamese there); reworded the unclear claim that Sino-Korean 은 is also the native word for silver; blank line before ## Notes; kwin, linked word, lexipedia placement and back-links checked; stamped.
- 金色: Mandarin, Cantonese and Japanese readings (きんいろ; こんじき as a poetic usage; rare こんしょく) confirmed on Wiktionary (no Korean or Vietnamese there); reworded the Notes' "Buddhist-flavored" claim for こんじき to what Wiktionary says; blank line before ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 酩丁: Mandarin, Cantonese and Japanese readings and the "dead drunk" sense confirmed on Wiktionary (via 酩酊; no Korean or Vietnamese there); corrected "neither character appears outside this compound" (酊 also means tincture, as in 酊劑) and added the variant reading míngdǐng; stand-in note (酩 points to 酩丁), kwin, linked word, lexipedia placement and back-links checked; stamped.
- 道成肉身: confirmed the 和合本 John 1:14 wording on Wikisource (no Wiktionary entry for the word, so its five readings are compositional); the Notes' remarks on 肉身, 受肉, nhập thể and 降生成人 were not looked up; blank line before ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 賢淑: Mandarin and Cantonese readings and the "morally excellent woman" sense confirmed on Wiktionary, which also gives the Taiwan reading xiánshú (added); removed the unverified claim that 현숙 was among the most popular Korean women's names of the mid-century; no Japanese, Korean or Vietnamese entry there; stand-in note (淑 points to 賢淑), kwin, linked word, lexipedia placement and back-links checked; stamped.
- 螟蛉: Mandarin, Cantonese, Japanese and Korean readings and the caterpillar and adopted-son senses confirmed on Wiktionary (no Vietnamese there); confirmed the 詩經·小宛 lines and the 類我 tradition on Wikisource and added both, plus Wiktionary's identification of the larva (green rice caterpillar); stand-in note (螟 and 蛉 point to 螟蛉), kwin, linked word, lexipedia placement and back-links checked; stamped.
- 虹霓: Wiktionary gives Mandarin hóngní (the page said hóngnì), Cantonese hung4 ngai4 and Japanese こうげい (the page said こうげ); corrected both in the frontmatter and Notes and added the Chinese neon word 霓虹 (níhóng, 虹霓 reversed); no Korean or Vietnamese entry there; stand-in note (霓 points to 虹霓), kwin, linked words, lexipedia placement and back-links checked; stamped.
- 臘八粥: Mandarin and Cantonese readings and the "Laba porridge" sense confirmed on Wiktionary (no Japanese, Korean or Vietnamese there); rewrote the Notes against English Wikipedia (Laba congee): kept eight-plus ingredients, the Beijing recipe and the Han/Northern-Southern/Song/Qing outline, and removed the unverified Tang, Song-court, Qing-banner, Sichuan, Shanxi, temple, neighbour-gift and Zhou-sacrifice claims, flagging the Korean and Japanese comparisons as unchecked; blank line before ## Notes; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 臘八節: Mandarin and Cantonese readings and the festival sense confirmed on Wiktionary (no Japanese, Korean or Vietnamese there); checked the Notes' history against English Wikipedia (Laba Festival): kept the eight-gods sacrifice origin, the Buddha-enlightenment layer and the Rōhatsu parallel; removed the unverified 臘月 naming by Qin/Han, the OC etymology of 臘, the Tang monastery and Song court porridge claims and the "Chan Buddhism" dating, and flagged the proverb as unfound; blank line before ## Notes; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 聖餐: Mandarin, Cantonese, Japanese and Korean readings and the Eucharist sense confirmed on Wiktionary (no Vietnamese there), which also gives the Japanese second reading せいざん (noted); blank line before ## Notes; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 老鼠人: checked the Notes' account of the slang against 2025 Chinese media pieces (via Digitaling): kept the 2023 鼠鼠文学 background and the 2025 spread, added the ~2 billion view figure and the UK-students origin and the performative-vlog criticism; removed the unverified 叔叔我呀 pun and the Russian крысиные люди stream and the Weibo claim; blank line before ## Notes; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 石灰: Mandarin, Cantonese, Japanese (せっかい, also いしばい) and Korean readings and the lime sense confirmed on Wiktionary (no Vietnamese there); checked 于謙's 石灰吟 on Wikisource (粉骨碎身 is the main reading, 粉身碎骨 a variant, now noted); flagged the unverified Erlitou and Great Wall claims; kwin, linked word, lexipedia placement and back-links checked; stamped.
- 石油: Mandarin and Cantonese readings and the crude-oil sense confirmed on Wiktionary (its Japanese and Korean sections were cut off in the fetch); confirmed the 夢溪筆談 卷二十四 line on Wikisource, noted the 事實類苑 variant of the closing line and that it was not re-read in the original, and fixed the Korean romanisation (seogyu); kwin, linked words, lexipedia placement and back-links checked; stamped.
- 無限: all five readings and the infinity/unlimited senses confirmed on Wiktionary; blank line before ## Notes; kwin, linked words, lexipedia placement and back-links checked; no other change needed; stamped.
- 無明: all five readings and the Buddhist avidyā sense confirmed on Wiktionary; the 無名 homophone remark checked (different Dan'a'yo sound, so no callout is needed); kwin, lexipedia placement and back-links checked; no change needed; stamped.
- 淡紫: no Wiktionary entry found; added a plain note that its readings are compositional; blank line before ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 海湾: Mandarin and Cantonese readings and the bay/gulf sense confirmed on Wiktionary (no Japanese, Korean or Vietnamese there), which also lists the Chinese proper-noun senses (added to the Notes); stand-in note (湾 points to 海湾), kwin, lexipedia placement and back-links checked; stamped.
- 泡沫: Mandarin, Cantonese, Japanese and Korean readings and senses confirmed on Wiktionary (no Vietnamese there); replaced the unattested Japanese 泡沫経済 with what Wiktionary shows (バブル経済, 泡沫景気, うたかた) and added the Mandarin 互联网泡沫 example; stand-in note (泡 points to 泡沫), kwin, lexipedia placement and back-links checked; stamped.
- 水色: Japanese reading and "light blue" sense confirmed on Wiktionary (no usable Mandarin, Cantonese, Korean or Vietnamese data there); the Mandarin usage remark is now flagged as unchecked; blank line before ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 横数: Dan'a'yo coinage for "imaginary number" (no dictionary entry to check); the Notes' mathematics (Argand diagram, √−1) and the standard terms 虚數 etc. read correctly; blank line before ## Notes; kwin, linked word, lexipedia placement and back-links checked; stamped.
- 桃色: Mandarin, Cantonese and Japanese readings and senses checked on Wiktionary (no Korean or Vietnamese there); rewrote the Notes: Chinese has a figurative erotic/scandal sense (confirmed), the unsupported Japanese and Korean erotic claims and the pink-film remark were removed or flagged; blank line before ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 栗色: Mandarin, Cantonese and Japanese readings and the chestnut/maroon sense confirmed on Wiktionary (no Korean or Vietnamese entry there; the Korean field keeps the North Korean 률색); blank line before ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 朱色: Japanese and Korean readings and the vermilion sense confirmed on Wiktionary (no Mandarin, Cantonese or Vietnamese entry there); the claim that 朱 pictures red heartwood is now stated as a common guess, since Wiktionary only says the tree's core is marked; blank line before ## Notes; homophone callout (主食, reciprocal), stand-in note (朱 points to 朱沙), kwin, lexipedia placement and back-links checked; stamped.
- 曲線: Mandarin, Cantonese, Japanese and Korean readings and the "curve" sense confirmed on Wiktionary (no Vietnamese there), which also gives the alternative Mandarin reading qǔxiàn (added to the Notes); kwin, linked words, lexipedia placement and back-links checked; stamped.
- 救贖: Mandarin and Cantonese readings and the redemption/atonement sense confirmed on Wiktionary (no Japanese, Korean or Vietnamese there); blank line before ## Notes; stand-in note (贖 points to 贖罪), kwin, linked words, lexipedia placement and back-links checked; stamped.
- 放腐: checked the Notes' claims about 摆烂: kept the NBA-tanking origin with the Language Log caveat and the 21.3% June 2023 figure (now stated with its method), replaced the unverified "hundreds of millions of reads" and March 2022 date with what sources support, and replaced the unsupported censorship sentence with the 2025 Wikipedia report; blank line before ## Notes; kwin, linked word, lexipedia placement and back-links checked; stamped.
- 抽出: Mandarin, Cantonese, Japanese and Korean readings and the extract/sample senses confirmed on Wiktionary (no Vietnamese there); stand-in note (抽 points to 抽出), kwin, linked words, lexipedia placement and back-links checked; no change needed; stamped.
- 恩寵: Mandarin, Cantonese, Japanese and Korean readings and the Christian "grace of God" sense confirmed on Wiktionary (no Vietnamese there); blank line before ## Notes; stand-in note (恩 points to 恩寵), kwin, linked words, lexipedia placement and back-links checked; stamped.
- 思慕: Mandarin, Cantonese and Japanese readings and the senses confirmed on Wiktionary (no Korean or Vietnamese there); corrected the graphic etymology of 慕 (莫 is only the phonetic, 心 the semantic element); stand-in note (慕 points to 思慕), kwin, lexipedia placement and back-links checked; stamped.
- 弓道: all five readings confirmed on Wiktionary; checked the history paragraph against English Wikipedia (Kyūdō): kept the 1919 change of name from 弓術 and the 1953 Kyudo Manual, and removed the unconfirmed Uno Yōzaburō, Dai Nippon Butoku Kai, federation-dates, 221 cm and Awa Kenzō claims (Herrigel 1948 and Yamada Shōji's 2001 essay kept, attributed to the article); kwin, linked words, lexipedia placement and back-links checked; stamped.
- 小行星帯: Mandarin and Cantonese readings and the "asteroid belt" sense confirmed on Wiktionary (via 小行星帶; no Japanese, Korean or Vietnamese there); blank line before ## Notes; kwin, linked words, lexipedia placement and back-links checked; stamped.

## 2026-11-12

### Oldest-page pass (characters, words, chengyu)
- 射出: Mandarin, Cantonese, Japanese and Korean readings and senses (emit, eject, inject) confirmed on Wiktionary; stand-in note (射 points to 射出), kwin, linked word, lexipedia placement and back-links checked; no change needed; stamped.
- 宇宙人: Mandarin, Japanese and Korean readings and senses confirmed on Wiktionary (no Cantonese or Vietnamese there); the Notes now say Wiktionary also lists "astronaut" as a secondary Japanese sense; blank line before ## Notes; kwin, linked word, lexipedia placement and back-links checked; stamped.
- 大韓民国: all five readings and the definition confirmed on Wiktionary (via 大韓民國); the gloss of 民国 now reads "republic" like its own word page (it said "people's republic; republic"); kwin, linked words, both lexipedia placements and back-links checked; stamped.
- 墓穴: Mandarin and Cantonese readings and the grave sense confirmed on Wiktionary, which also gives the Taiwan variant mùxuè (added to the Notes); stand-in note (墓 points to 墓穴), kwin, linked words, lexipedia placement and back-links checked; stamped.
- 圓錐: Mandarin, Cantonese and Korean readings and the "cone" sense confirmed on Wiktionary; the mathematical and cross-language notes read correctly and were left as written; kwin, linked word, lexipedia placement and back-links checked; no change needed; stamped.
- 国務領: checked the 1925–1927 dates and holders against Korean Wikipedia (국무령) and English Wikipedia; added the nominated-but-declined names, the 1927 chairman system and the 1932–1933 revival for Kim Gu; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 史学者: no entry found for the word itself on Wiktionary or kotobank; added a plain note that its readings are compositional and its "standard academic title" claim is unconfirmed; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 双子: Mandarin, Cantonese and Japanese data checked on Wiktionary; corrected the Mandarin usage note (雙子 is chiefly dialectal for "twins", 雙胞胎 is standard) and added the Cantonese 孖仔/孖女; blank line before ## Notes; kwin, lexipedia placement (Numbers, Kinship) and back-links checked; stamped.
- 単独: all five readings confirmed on Wiktionary (via 單獨); added the blank line between the embed and ## Notes; kwin, lexipedia placement and back-links checked; stamped.
- 南美洲: Mandarin and Cantonese readings and the definition confirmed on Wiktionary; kwin, linked words, lexipedia placement and back-links checked; no change needed; stamped.
- 千年: Mandarin, Cantonese, Japanese and Korean readings and senses confirmed on Wiktionary; removed the unsourced stock phrase 千年不朽 from the Notes; kwin, linked words, lexipedia placement and back-links checked; stamped.
- 北美洲: Mandarin and Cantonese readings and the definition confirmed on Wiktionary (no Japanese, Korean or Vietnamese there; 北 has bắc among its Vietnamese readings); kwin, linked words, lexipedia placement and back-links checked; no change needed; stamped.
- 募集: Mandarin, Cantonese and Japanese readings confirmed on Wiktionary; added its note that Mandarin "to recruit" is chiefly Hong Kong usage; stand-in note (募 → 募集), kwin, lexipedia placement and back-links checked; stamped.
- 刺客: readings in all five languages confirmed on Wiktionary; kwin, linked word, lexipedia placement and back-links checked; no change needed; stamped.
- 初代: Japanese reading and senses confirmed on Wiktionary; replaced the unsourced Mandarin usage claim with a plain statement that it was not checked; kwin, linked word, lexipedia placement and back-links checked; stamped.
- 共産党: frontmatter, kwin, linked words, lexipedia placement and character back-links checked; no change needed; stamped.

### Coinage: 果位
- 果位: replaced the "attestation not confirmed" note with the user-supplied sources for the readings (かい on kotobank, 과위 on the Dongguk Buddhist dictionary, quả vị on WisdomLib); kotobank and WisdomLib were opened and agree, the Dongguk page would not load (certificate error).
- New word `words/果位.md` ("stage of attainment", Buddhism), made at the user's request as the borrowed Buddhist term (checked against Chinese Wikipedia and 佛光大辭典 entries for 證果, 因位 and 佛果). Added to the 果 and 位 Words sections and to the Religion lexipedia page (Buddhist & Cosmological Concepts). Japanese, Korean and Vietnamese fields are the compositional Sino readings; the page says their attestation was not confirmed.

### Chengyu pass
- 令行禁止: checked the 管子 (立政, 七法, 明法解) and 荀子 lines on wikisource; the 立政 line was misquoted (「…此所謂政令」), now 「令則行，禁則止，憲之所及，俗之所被，如百體之從心，政之所期也」; added 天下願 to the 荀子·王制 line and described 七法 correctly; removed the unverified Cultural Notes claims (pandemic, PLA, Huawei, legal codes); back-links checked; lint clean; stamped.
- 人山人海: found 人山人海 in the 《西湖老人繁勝錄》 text and the 《水滸傳》 chapter 51 clause on wikisource and added both to Source and Origin (the book's list carries 南瓦/中瓦/上瓦/下瓦 annotations, noted without a firm reading); back-links checked; lint clean; stamped.
- 事事皆旧: Ecclesiastes 1:9 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 乾坤一擲: 韓愈《過鴻溝》 quotation (already checked on wikisource), linked word and back-links re-checked; no change needed; lint clean; stamped.
- 乳蜜流地: Exodus 3:8 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; the 魚米之鄉 history flag stays (its Wikipedia page could not be opened); lint clean; stamped.
- 主宰万物: Psalm 24 citation (和合本, already checked), linked words and back-links re-checked; no change needed; lint clean; stamped.
- 不言不語: 《佛說阿遫達經》 citation (already checked on wikisource, translator and date flagged as not identified) and back-links re-checked; no change needed; lint clean; stamped.
- 上由下至: 単亜語 coinage with no external citation; frontmatter, sections, linked pages and back-links checked; no change needed; lint clean; stamped.
- 不打不成器: 《禮記·學記》 and Proverbs citations (already checked) and back-links re-checked; confirmed the 《三字經》 line on wikisource and replaced the unchecked flag; lint clean; stamped.
- 骨肉相連: 《北齊書》 and Genesis 2:23 citations (already checked) and back-links re-checked; confirmed the 《管子·輕重丁》 line with 骨肉相親 on wikisource and replaced the unchecked flag with the quotation; lint clean; stamped.
- 金銀銅鉄: Daniel 2:31–33 citation (ESV and 和合本, already checked) and back-links re-checked; replaced the unchecked flag on the four-kingdoms identification with what the Wikipedia article on the Book of Daniel says (traditional and modern readings); Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 財愛悪根: 1 Timothy 6:10 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 豹斑改乎: Jeremiah 13:23 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 血誓盟約: Exodus 24:8 citation (ESV and 和合本, already checked) and back-links re-checked; replaced the "not checked" flag on 歃血為盟 with what wikisource shows (a Tang memorial and later novels, earliest use not established); Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 種瓜得瓜: tried to find the 《喻世明言》 passage on wikisource and could not; the page keeps its note that the citation rests on the Ministry of Education entry and that the 《涅槃經》 attribution is unverified; back-links checked; no change; lint clean; stamped.
- 石山盈界: Daniel 2:34–35 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 無為而治: 《論語·衛靈公》 and 《老子》 chapter 57 quotations (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 数数衡分: Daniel 5:25–28 citation (ESV and 和合本, already checked) and back-links re-checked; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; lint clean; stamped.
- 指記二碑: confirmed Exodus 31:18 (和合本, 西乃山) on wikisource and noted it in Source and Origin; example 1 now reads 西乃山 like the 和合本 and the quoted verse; Japanese reading changed from katakana to hiragana in frontmatter and Pronunciations; back-links checked; lint clean; stamped.
- 意気揚揚: 《史記·管晏列傳》 charioteer passage (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 帰塵帰土: Genesis 3:19 and Ecclesiastes 3:20 citations (ESV and 和合本, already checked) and back-links re-checked; no change needed; lint clean; stamped.
- 家分不立: Matthew 12:25 citation (ESV and 和合本, already checked) and back-links re-checked; the Japanese reading (frontmatter and Pronunciations) changed from katakana to hiragana, as the checklist asks; lint clean; stamped.
- 孤軍奮闘: checked the 《魏書·趙遐傳》 quotation against 《魏書》卷五十二 on wikisource; restored the subject 遐 and the spelling 直閤 in the quoted line and named Zhao Xia in the translation; back-links checked; lint clean; stamped.
- 剣生剣死: Matthew 26:52 citation (ESV, Greek and RCUV, already checked) and back-links re-checked; the Pronunciations Japanese line now uses hiragana, matching the frontmatter and checklist; lint clean; stamped.
- 世間罪盛: Bible citations (和合本 Genesis 6:5 and Romans 5:20, already checked on cnbible.com), linked word and back-links re-checked; no change needed; lint clean; stamped.
- 世仇宿敵: Genesis 3:15 (KJV and 和合本, already checked) , linked words and back-links re-checked; no change needed; lint clean; stamped.
- 不遠千里: 《孟子·梁惠王上》 quotation (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 不可思議: 《維摩詰所說經·不思議品》 quotation (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 不共戴天: 《禮記·曲禮上》 quotation (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 三綱五常: confirmed Ma Rong's gloss 「所因，謂三綱五常」 in 《論語集解》為政 on wikisource and rewrote the caveat and that bullet to say so (the 白虎通義 and 春秋繁露 quotations are still unchecked and stay flagged); back-links checked; lint clean; stamped.
- 万物生長: 《周易·繫辭下》 and 《中庸》 quotations (already checked on wikisource) and back-links re-checked; origin stays "not established", as the page says; no change needed; lint clean; stamped.
- 一触即発: moved Pronunciations ahead of Cultural Notes (checklist order); the 李開先《原性堂記》 text is not on wikisource, so the page keeps its note that the quotation was checked against the Ministry of Education entry only; back-links checked; lint clean; stamped.
- 一網打尽: 《東軒筆錄》 and 《宋史》 citations (already checked on wikisource) and back-links re-checked; no change needed; lint clean; stamped.
- 一石二鳥: no named primary citation (modern calque; the page already states what is unverified); frontmatter, sections and back-links checked; no change needed; lint clean; stamped.
- 一目瞭然: confirmed the 《朱子語類》 卷一三七 line 「見得道理透後，從高視下，一目瞭然」 on wikisource and said so in Source and Origin; back-links checked; lint clean; stamped.
- 一期一会: back-links checked; the 《山上宗二記》 and 《茶湯一会集》 quotations could not be found in a primary text on ja.wikisource, so the page keeps its existing note that they were verified through secondary pages only; lint clean; stamped.
- 一朝一夕: 《周易·坤·文言》 quotation and back-links re-checked; no change needed; lint clean; stamped.
- 一日三秋: 《詩經·王風·采葛》 quotation (三秋 in the second stanza) and back-links re-checked; no change needed; lint clean; stamped.
- 一攫千金: 《列子·說符》 quotation checked word for word against wikisource (列子/說符篇); no change needed; lint clean; stamped.
- 一帆風順: read Yang Wanli 〈曉出洪澤霜晴風順〉 on wikisource (《誠齋集》卷二十九) and quoted it in Source and Origin; its last line has 順風…一帆 but not the four-character form, now stated; rest of page checked; lint clean; stamped.
- 鶏鳴狗盗: citations (《史記·孟嘗君列傳》, 王安石《讀孟嘗君傳》) and back-links re-checked, no change; added the alias 鷄鳴狗盜 (the variant the Standard Form section names); lint clean; stamped.
- 魑魅罔両: re-checked against checklist_chengyu.md (frontmatter, sections, Zuo Zhuan citation already verified 2026-10-04 and left as is); lint clean; stamped.

### SKIP stem pass
- SKIP-3-5: fixed the breadcrumb, added the stroke description (surrounding part 5 strokes), gaps 1 and 11 as `SKIP-3-5-N: none`; leaves, previews and size verified; stamped.
- SKIP-3-6: positions 1, 2 and 10 have no leaf file, so the bare `ø` is now `SKIP-3-6-N: none`; leaves, previews, description and size verified; stamped.
- SKIP-3-7: positions 1 and 6 had a bare `ø` but no leaf file, and 10–12 a bare `none`; all now `SKIP-3-7-N: none`; leaves, previews, description and size verified; stamped.
- SKIP-3-8: position 1 had a bare `ø` but no leaf file, now `SKIP-3-8-1: none`; leaves, previews, description and size verified; stamped.
- SKIP-3-9: positions 1, 3, 4 and 6–8 had a bare `ø` but no leaf file, now `SKIP-3-9-N: none`; leaves, previews, description and size verified; stamped.
- SKIP-4-1: verified leaf list, previews, description and size; no change needed; stamped.
- SKIP-4-10: inline tags, breadcrumb spacing, added the one-line description, `No` → `SKIP-4-10-1: none`, `_only redirect_` → ø; leaves, previews and size verified; stamped.
- SKIP-4-11: Stroke link made standard, added the one-line description, `No` → `SKIP-4-11-N: none`; leaves, previews and size 3 verified; stamped.
- SKIP-4-12: inline tags, added the one-line description, `No` → `SKIP-4-12-N: none`; leaves, previews and size 1 verified; stamped.
- SKIP-4-13: empty leaf 3 previewed as ø, "does not exist" gaps written as `SKIP-4-13-N: none`; leaves, previews, description and size 1 verified; stamped.
- SKIP-4-14: wikilink breadcrumb, Stroke link and leaf link made standard, added the one-line description, gaps 2–4 as `SKIP-4-14-N: none`; leaves, previews and size 1 verified; stamped.
- SKIP-4-15: breadcrumb link made standard, added the one-line description, gaps 1–3 as `SKIP-4-15-N: none`; leaves, previews and size 1 verified; stamped.
- SKIP-4-2: fixed the breadcrumb, added the Stroke link and the one-line description, converted wikilink leaf entries to standard links; leaves, previews and size 11 verified; stamped.
- SKIP-4-3: fixed the breadcrumb, Stroke link and leaf links (wikilinks with `=` → standard links with `:`); leaves, previews, description and size 30 verified; stamped.
- SKIP-4-4: verified leaf list, previews, description and size 33; no change needed; stamped.
- SKIP-4-5: added the one-line description and `stroke_count`; leaves, previews and size 35 verified; stamped.
- SKIP-4-6: breadcrumb, Stroke link and leaf links made standard, added the one-line description; leaves, previews and size 22 verified; stamped.
- SKIP-4-7: added the one-line description and `stroke_count`; leaves, previews and size 18 verified; stamped.
- SKIP-4-8: breadcrumb and Stroke link made standard, added the one-line description; leaves, previews and size 8 verified; stamped.
- SKIP-4-9: added the one-line description and `stroke_count`; leaves, previews and size 9 verified; stamped.
- SKIP-2-19: verified leaf list, ø/none markers, description and size 0; no change needed; stamped.
- SKIP-1-16: verified leaf list, ø/none markers, description and size 0; no change needed; stamped.
- SKIP-1-18: verified leaf list, ø/none markers, description and size 0; no change needed; stamped.
- SKIP-2-20: verified leaf list, ø/none markers, description and size 0; no change needed; stamped.

## 2026-11-11

### SKIP stem pass
- SKIP-1-1: verified leaf list, previews and size against the characters; wrote the empty positions as `SKIP-1-1-N: none`; stamped.
- SKIP-1-10: verified leaf list (1–19), previews, ø/none markers and size 34 against the characters; no change needed; stamped.
- SKIP-1-11: verified leaves, previews and size 35; empty leaf previews written as ø (2 places) per the checklist; stamped.
- SKIP-1-12: fixed the breadcrumb, added the stroke description (left half 12 strokes), wrote the gap as `SKIP-1-12-8: none`; leaves, previews and size 12 verified; stamped.
- SKIP-1-13: fixed the breadcrumb, added the stroke description (left half 13 strokes), wrote the gaps as `SKIP-1-13-N: none`; leaves, previews and size 3 verified; stamped.
- SKIP-1-14: verified leaf list (1–9), previews, ø/none markers, description and size 2; no change needed; stamped.
- SKIP-1-15: replaced the wikilink breadcrumb with the standard link, added the stroke description (left half 15 strokes), wrote gaps as `SKIP-1-15-N: none`, inline tags; leaves, previews and size 1 verified; stamped.
- SKIP-1-17: verified leaves 1–11 (including the new 1-17-8 and 1-17-9 ø leaves), previews and size 1; no further change; stamped.
- SKIP-1-2: replaced the wikilink breadcrumb with the standard link, added the stroke description (left half 2 strokes), wrote gaps as `SKIP-1-2-N: none`; leaves, previews and size 159 verified; stamped.
- SKIP-1-3: added the stroke description (left half 3 strokes), wrote gaps 23 and 24 as `none`; leaves, previews and size 636 verified; stamped.
- SKIP-1-4: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-1-5: added the stroke description (left half 5 strokes); leaves, previews, markers and size verified; stamped.
- SKIP-1-6: empty leaf previews 16 and 17 written as ø per the checklist; leaves, previews and size verified; stamped.
- SKIP-1-7: empty leaf previews 17–19 written as ø per the checklist; leaves, previews and size verified; stamped.
- SKIP-1-8: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-1-9: tags put inline like the other stems; leaves, previews, markers, description and size verified; stamped.
- SKIP-2-1: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-2-10: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-2-11: gap markers 1 and 12 written as `SKIP-2-11-N: none`; leaves, previews, description and size verified; stamped.
- SKIP-2-12: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-2-13: replaced the wikilink breadcrumb, added the stroke description (top component 13 strokes), wrote gaps 1, 2, 8 and 10 as `SKIP-2-13-N: none`; leaves, previews and size verified; stamped.
- SKIP-2-14: fixed the breadcrumb, added the stroke description (top component 14 strokes), wrote the gap markers as `SKIP-2-14-N: none`; leaves, previews and size verified; stamped.
- SKIP-2-15: gap markers written as `SKIP-2-15-N: none`, tags inline; leaves, previews, description and size verified; stamped.
- SKIP-2-16: verified leaf list (including the new 2-16-5 ø leaf), previews, description and size; no further change; stamped.
- SKIP-2-2: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-2-3: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-2-4: gap markers 14–16 written as `SKIP-2-4-N: none`, empty leaf 17 previewed as ø; leaves, previews and size verified; stamped.
- SKIP-2-5: empty leaf previews 16, 17 and 19 written as ø, gap 18 as `SKIP-2-5-18: none`; leaves, previews and size verified; stamped.
- SKIP-2-6: empty leaves 17 and 19 previewed as ø, gaps 18 and 20–25 written as `SKIP-2-6-N: none` (26 is the new 籲 ø leaf); leaves, previews and size verified; stamped.
- SKIP-2-7: verified leaf list, previews, markers, description and size; no change needed; stamped.
- SKIP-2-8: gap markers 14 and 15 written as `SKIP-2-8-N: none`; leaves (including the new 靇 leaf 16), previews, description and size verified; stamped.
- SKIP-2-9: gap markers (8, 10, 11, 13–17) written as `SKIP-2-9-N: none`; leaves, previews, description and size verified; stamped.
- SKIP-3-1: fixed the breadcrumb, added the stroke description (surrounding part 1 stroke), made the leaf links full paths, wrote gaps as `SKIP-3-1-N: none`; leaves, previews and size 7 verified; stamped.
- SKIP-3-10: breadcrumb spacing fixed, gap markers (1–3, 9, 12, 13, 15) written as `SKIP-3-10-N: none`; leaves, previews, description and size 3 verified; stamped.
- SKIP-3-2: added the stroke description (surrounding part 2 strokes), wrote gaps (16, 18, 19, 21, 23–27) as `SKIP-3-2-N: none`; leaves, previews and size verified; stamped.
- SKIP-3-3: fixed the breadcrumb, added the stroke description (surrounding part 3 strokes), gaps 19–20 as `none`, empty leaf 22 as ø; leaves, previews and size verified; stamped.
- SKIP-3-4: breadcrumb link made standard, added the stroke description (surrounding part 4 strokes), gaps (1, 16–18) as `SKIP-3-4-N: none`; leaves, previews and size verified; stamped.

### New SKIP leaf pages for the alias and forbidden glyphs
- Created SKIP-2-17-4, 2-17-8, 1-17-8, 2-16-5, 1-17-9, 2-17-16 and 2-6-26 as empty leaves holding the redirects (䶳, 龡, 䶴 → 吹; 龣 → 角; 龒 → 龍) and forbidden lines (龤, 龥, 龗, 籲); created the stem SKIP-2-17 and listed it on SKIP.md; filled the empty slots on SKIP-2-16, SKIP-1-17 and SKIP-2-6 (extended to 26).

### Cleanup after the alias pass
- Deleted the `制 --> 製` line on Radical 145 (制 has its own page) and the 䶵/篪 note on Radical 214 (no page for 篪).
- 夘 is now an alias of 卯 only: removed from 夗's frontmatter and `## Aliases`, its redirects removed on Stroke 05, SKIP-1-3-2 and Radical 036; 夗 has a Notes line pointing to 卯.
- Created Stroke 32 (籲) and Stroke 33 (龗) with their forbidden lines, and listed both on Stroke.md. SKIP guesses for the nine new forbidden entries added to the guesses file.

### Forbidden list, radical headings and extra aliases
- `文法 - 98違法字.md`: added 龑, 龓, 龖, 龘, 龗, 靇, 龤, 龥, 籲 (Chinese, 幽霊文字; Chinese 136 → 145, total 442 → 451). Lines written on the Stroke, Radical 212/173/214/118 and (where the page exists) SKIP pages; the prose notes on Radical 212 and 214 were replaced by those lines.
- Radical pages: negative stroke groups are written in the plus style, `### +-1 Stroke` (user ruling), on the 30 pages that had `### -N`; `radical_fmt.py` and `checklist_radicals.md` updated to match.
- Aliases added (frontmatter, `## Aliases`, Stroke, SKIP and Radical redirects): 叐, 𡗜, 𤝜 → 犮; 雎 → 狙; 狢, 貉 → 狸; 䶳, 龡, 䶴 → 吹; 龢 → 和; 龣 → 角; 龏 → 恭; 龒 → 龍. Annotated `variant of` lines on Radical 094, 145 and 212 became plain redirects, and 叐, 雎, 貉 moved to the radical Unihan gives them (029, 172, 153). SKIP numbers are computed guesses, listed in the skip-guesses project file.

- **Radicals.md**: `lint_radicals.py` passes on all 214 radical pages and the index; stamped (the radical loop's full re-stamp pass is complete).
- **Radical 214 (龠)**: converted the `## Characters` / `### Note` / `### Aliases` / `### Forbidden` layout to `## Strokes` (no characters are filed here); the six "ancient variant" redirects (䶳, 龡, 䶴 → 吹; 龢 → 和; 龣 → 角; 䶵 → 篪) are not aliases on their targets' pages and carry no stroke data, so they and the forbidden 龤 and 龥/籲 (not on the master 違法字 list) are kept as prose under `### Other`; stamped.
- **Radical 213 (龜)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (亀, 11 strokes, in a `### -5 Strokes` group, counted from the radical's Kangxi 16 strokes; redirects and ¡𪚲! filed by stroke count); turned the annotated `龝 --> 秋 (ancient variant)` into a plain alias-backed `龝 --> 秋` and dropped the duplicate annotated `龞 --> 鼈 (ancient variant; also of 鱉)`, stamped.
- **Radical 212 (龍)**: converted the old `[[wikilink]]` ruby entries and the `## Characters` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (龍 +0, 龐 +3, 龔 and 龕 +6, counted from the radical's Kangxi 16 strokes; 龛, 龎, 龚, 龙 redirects filed by stroke count, the duplicate annotated `龎 --> variant of 龐` dropped); the two unbacked annotated variants (龏, 龒) and the four forbidden coinages (龑, 龓, 龖/龘, 龗/靇, none of which is on the master 違法字 list) are kept as prose under `### Other`; stamped.
- **Radical 211 (齒)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (齢 +2, 齦 +6, counted from the radical's Kangxi 15 strokes; eight redirects filed by stroke count); removed `齖 --> 牙`, `齟 --> 𪗱` and `龄 --> 齢`, because 牙 and 齢 do not list them as aliases and 𪗱 has no page (rare forms, not added as aliases); stamped.
- **Radical 210 (齊)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups, counted from the radical's Kangxi 14 strokes (斉, 8 strokes, in a `### -6 Strokes` group as 才 is under 手; 齊 and 齐 → 斉 and 齋 → 斎 filed by stroke count), stamped.
- **Radical 209 (鼻)**: converted the `## Characters` / `### Used` layout to the standard +N Strokes groups (鼻 +0, 鼾 +3, counted from the radical's Kangxi 14 strokes), stamped.
- **Radical 208 (鼠)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard `## Strokes` layout (鼠 under +0; 鼡 → 鼠 filed by stroke count); removed the redirects `鼯 --> 吾`, `鼴 --> 晏`, `鼹 --> 晏`, `鼷 --> 小鼡` and `鼺 --> 鼯鼠 --> 吾鼠`, because 吾 and 晏 do not list them as aliases and 小鼡 has no page (rare forms, not added as aliases); stamped.
- **Radical 207 (鼓)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard `## Strokes` layout (鼓 under +0; 鼕 → 冬 and 鼗 → 鞀 filed by stroke count), stamped.
- **Radical 206 (鼎)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard `## Strokes` layout (鼎 under +0; 䵺 → 町 filed by stroke count), stamped.
- **Radical 205 (黽)**: converted the `## Characters` / `### Used` layout to `## Strokes` (鼈 +12, counted from the radical's Kangxi 13 strokes); removed the redirects `鼄 --> 蛛`, `鼅 --> 蜘`, `䵹 --> 蜘` and `鼇 --> 鰲`, because 蛛 and 蜘 list no aliases and 鰲 has no page (rare Unicode-only forms, not added as aliases); kept the `### Other` notes; stamped.
- **Radical 204 (黹)**: converted the `## Characters` / `### Used` layout to the standard +N Strokes groups (黻 +5, 黼 +7, counted from the radical's Kangxi 12 strokes), stamped.
- **Radical 203 (黑)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups, counted from the radical's Kangxi 12 strokes (黒, 11 strokes, in a `### -1 Stroke` group; 黙 +3, 黛 +4, 黜 +5; four redirects and ¡𪐷! filed by stroke count), stamped.
- **Radical 202 (黍)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (黍 +0, 黎 +3, counted from the radical's Kangxi 12 strokes; 䵘 → 晒 and 黏 → 粘 filed by stroke count), stamped.
- **Radical 201 (黃)**: converted the `## Characters` / `### Used` / `### Aliases` layout to `## Strokes`, counted from the radical's Kangxi 12 strokes (黄, 11 strokes, in a `### -1 Stroke` group as 才 is under 手; 黃 → 黄 filed under +0), stamped.
- **Radical 200 (麻)**: converted the `## Characters` / `### Used` / `### Forbidden` layout to the standard +N Strokes groups (麻 +0; ¡麼! +3 and ¡麿! +7 as 違法字 lines; the annotated `麽 --> variant of 麼, forbidden with it` kept beside 麼 in +3, since 麽 is only listed as a variant on the forbidden list), stamped.
- **Radical 199 (麦)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups, counted from the radical's Kangxi 11 strokes (麦, 7 strokes, in a `### -4 Strokes` group as 才 is under 手; 麺 +5; five redirects filed by stroke count), stamped.
- **Radical 198 (鹿)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (鹿 +0, 麒 麓 麗 +8, 麟 +12, counted from the radical's Kangxi 11 strokes; 麝 → 射 and 麐 → 麟 filed by stroke count), stamped.
- **Radical 197 (鹵)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (鹵 +3 from its `stroke_count` of 14, 鹸 +8, counted from the radical's Kangxi 11 strokes; 鹹 → 咸, 鹽 → 塩, 鹼 → 鹸 filed by stroke count), stamped.
- **Radical 196 (鳥)**: merged the redirect lines under seven malformed `### +-N Strokes` headings into negative groups ahead of +0; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (19 lines, six forbidden glyphs as 違法字 lines), stamped.
- **Radical 195 (魚)**: fixed the malformed heading `### +-3 Strokes` to `### -3 Strokes`; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (30 lines: four redirects and 26 forbidden glyphs as 違法字 lines); the redirects `鯛 --> 周`, `鱶 --> 養` and `鯰 --> 鮎` became `¡X! - 違法字` lines because those glyphs are on the forbidden list; stamped.
- **Radical 194 (鬼)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (鬼 +0, 魁 and 魂 +4, 魄 and 魅 +5, 魏 +8, 魑 and 魔 +11, counted from the radical's Kangxi 10 strokes; five redirects filed by stroke count), stamped.
- **Radical 193 (鬲)**: converted the `## Characters` / `### Note` / `### Aliases` layout to `## Strokes` (no characters are filed here; 𩱦 → 炒 and 鬻 → 粥 filed by stroke count); removed `鬲 --> 隔` and the note's claim that 鬲 is an alias of 隔, because 隔's page lists no aliases; stamped.
- **Radical 192 (鬯)**: converted the `## Characters` / `### Note` / `### Aliases` layout to `## Strokes` (no characters are filed here; the note is kept above the groups; 鬱 and 鬰 → 欝 filed by stroke count), stamped.
- **Radical 191 (鬥)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (䦧 +6, counted from the radical's Kangxi 10 strokes; eight redirects filed by stroke count), stamped.
- **Radical 190 (髟)**: converted the `## Characters` / `### Used` / `### Forbidden` / `### Aliases` layout to the standard +N Strokes groups (髪 +4, 髯 +5, 鬚 +12, 鬣 +15, counted from the radical's Kangxi 10 strokes; eight redirects and ¡髭! filed by stroke count), stamped.
- **Radical 189 (高)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard `## Strokes` layout (高 under +0; 䯨 → 敲 filed by stroke count), stamped.
- **Radical 188 (骨)**: moved the bottom Aliases block into the +N Strokes groups (髓 → 髄, 體 → 体), stamped.
- **Radical 187 (馬)**: merged the redirect lines under eleven malformed `### +-N Strokes` headings into negative groups (`-5` to `-1`, ahead of +0); moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (駛, 驶 → 使, 駿, 骏 → 俊, 马 → 馬 and ¡駲! as a 違法字 line), stamped.
- **Radical 186 (香)**: moved the bottom Aliases block into the +N Strokes groups (馫 → 馨), stamped.
- **Radical 185 (首)**: switched the `## Characters` / `### Used` layout to the standard `## Strokes` / `### +0 Strokes` layout (the single entry 首 was already present), stamped.
- **Radical 184 (食)**: merged the redirect lines under five malformed `### +-N Strokes` headings into negative groups (`-4`, `-2`, `-1`, ahead of +0); moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (饭 → 飯, 饱 → 飽 and ¡䭏!, ¡饂!, ¡𩛰! as 違法字 lines), stamped.
- **Radical 183 (飛)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (飛 +0; 飞 → 飛 and 飜 → 翻 filed by stroke count); removed `䬡 --> 翻`, which is not in 翻's aliases (rare Unicode-only form, not added as an alias); stamped.
- **Radical 182 (風)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (風 +0, 颯 +5; 颱, 风, 颳, 飒 → redirects and ¡颪! filed by stroke count), stamped.
- **Radical 181 (頁)**: merged the redirect lines under three malformed `### +-N Strokes` headings into `### -3 Strokes` and `### -1 Stroke` (ordered ahead of +0); moved the bottom Aliases block into the +N Strokes groups (頽 → 退, 颇 → 頗), stamped.
- **Radical 180 (音)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (音 +0, 韻 +10, 響 +11; 韵 → 韻 filed by stroke count), stamped.
- **Radical 179 (韭)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (韮 +3, stroke_count 12 less the radical's Kangxi 9; 韭 → 韮 filed under +0), stamped.
- **Radical 178 (韋)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (韋 +1, 韓 +9, counted from the radical's Kangxi 9 strokes; 韩 → 韓 and 韦 → 韋 filed by stroke count), stamped.
- **Radical 177 (革)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (革 +0, 靴 +4, 鞀 and 鞄 +5, 鞋 and 鞍 +6, 鞘 +7, 鞠 +8, 鞭 +9; nine redirects and ¡靹! filed by stroke count), stamped.
- **Radical 176 (面)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard `## Strokes` layout (面 under +0; 䩊 → 婉 filed by stroke count), stamped.
- **Radical 175 (非)**: converted the `## Characters` / `### Used` layout to the standard +N Strokes groups (非 +0, 靠 +7, 靡 +11), stamped.
- **Radical 174 (青)**: moved the bottom Aliases block into the +N Strokes groups (靑 → 青), stamped.
- **Radical 173 (雨)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (霄, 䨭 → 宵, 霦 → 彬, 霹 → 辟, 霤 → 留, 霰 → 散 and ¡雫! as a 違法字 line), stamped.
- **Radical 172 (隹)**: moved the bottom Aliases block into the +N Strokes groups (雞 → 鶏, 雏 → 雛, 隻 → 只), stamped.
- **Radical 171 (隶)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (隷 under +8; 隶 → 隷 under +0, 隸 → 隷 filed by stroke count), stamped.
- **Radical 170 (阜)**: merged the redirect lines under three malformed `### +-N Strokes` headings (plus one proper `-1 Stroke`) into negative groups ahead of +0; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (4 lines, three forbidden glyphs as 違法字 lines), stamped.
- **Radical 169 (門)**: merged the nine redirect lines under nine malformed `### +-N Strokes` headings into `### -3 Strokes`, `### -2 Strokes` and `### -1 Stroke`; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (12 lines, three forbidden glyphs as 違法字 lines), stamped.
- **Radical 168 (長)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard `## Strokes` layout (長 under +0; 长 → 長 and 镸 → 長 filed by stroke count), stamped.
- **Radical 167 (金)**: merged the redirect lines under the malformed `### +-1 Strokes` (twice) and `### +-2 Strokes` headings into `### -2 Strokes` and `### -1 Stroke`; moved the bottom Forbidden/Aliases blocks into the +N Strokes groups (14 lines, ten forbidden glyphs as 違法字 lines), stamped.
- **Radical 166 (里)**: verified (4 characters, groups and the 釐 → 厘 redirect correct), stamped; no content change.
- **Radical 165 (釆)**: verified (3 characters, groups and the 釋 → 釈 redirect correct), stamped; no content change.
- **Radical 164 (酉)**: moved the bottom Aliases block into the +N Strokes groups (醗, 醱 → 発, 醫 → 医), stamped.
- **Radical 163 (邑)**: fixed the malformed heading `### +-2 Strokes` to `### -2 Strokes`; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (邨 → 村, 鄱 → 番 and ¡𨛗! as a 違法字 line), stamped.
- **Radical 162 (辵)**: fixed the malformed headings `### +-1 Strokes` and `### +-2 Strokes` to `### -1 Stroke` and `### -2 Strokes` (ordered -3, -2, -1, +0; the -3 group was created by the migration); moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (seven redirects and eleven forbidden glyphs as 違法字 lines), stamped.
- **Radical 161 (辰)**: verified (3 characters, groups and 2 alias-backed redirects correct), stamped; no content change.
- **Radical 160 (辛)**: verified (5 characters, groups and 5 alias-backed redirects correct), stamped; no content change.
- **AIOS/scripts/radical_fmt.py**: `heading()` now writes negative groups as `### -1 Stroke` / `### -3 Strokes` instead of the malformed `### +-1 Strokes`, which `radical_migrate.py` and the alias/forbidden tools produced for characters with fewer strokes than the radical.
- **Radical 159 (車)**: fixed the malformed headings `### +-2 Strokes`, `### +-1 Strokes` and a `### +-3 Strokes` that the migration tool created, to `### -2 Strokes`, `### -1 Stroke` and `### -3 Strokes`; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (nine redirects and ¡𨋳!, ¡𨏍! as 違法字 lines), stamped.
- **Radical 158 (身)**: converted the `## Characters` / `### Used` / `### Forbidden` / `### Aliases` layout to the standard +N Strokes groups (身 +0, 躬 +3; 躭 → 耽, 躳 → 躬 and eight forbidden glyphs as 違法字 lines filed by stroke count), stamped.
- **Radical 157 (足)**: moved the bottom Forbidden/Aliases blocks into the +N Strokes groups (蹶 → 決, 躇 → 着 and six forbidden glyphs as 違法字 lines), stamped.
- **Radical 156 (走)**: moved the bottom Forbidden block into the +N Strokes groups (¡趁!, ¡趟!, ¡趕! as 違法字 lines), stamped.
- **Radical 155 (赤)**: verified (3 characters, groups correct, no aliases or redirects needed), stamped; no content change.
- **Radical 154 (貝)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (贊, 赞 → 賛, 賣 → 売 and ¡贏! as a 違法字 line); removed `贠 --> 員`, which is not in 員's aliases (rare Unicode-only form, not added as an alias); stamped.
- **Radical 153 (豸)**: verified (3 characters, groups and 5 alias-backed redirects correct), stamped; no content change.
- **Radical 094 (犬)**: removed `兽 --> 獣`, `貍 --> 狸`, `貓 --> 猫`, `豬 --> 猪`, which I had filed there by mistake: each belongs to another radical's page and is already on it (Radical 012, 153, 153 and 152).
- **Radical 152 (豕)**: moved the bottom Aliases block into the +N Strokes groups (豬 → 猪), stamped.
- **Radical 151 (豆)**: verified (4 characters, groups and 2 alias-backed redirects correct), stamped; no content change.
- **Radical 150 (谷)**: switched the `## Characters` / `### Used` layout to the standard `## Strokes` / `### +0 Strokes` layout (the single entry 谷 was already present), stamped.
- **Radical 149 (言)**: merged 19 redirect lines scattered under 19 malformed `### +-N Strokes` headings into three proper groups (`### -3 Strokes`, `### -2 Strokes`, `### -1 Stroke`, ahead of +0); moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (24 lines, four forbidden glyphs as 違法字 lines), stamped.
- **Radical 148 (角)**: moved the bottom Forbidden block into the +N Strokes groups (¡鵤! as a 違法字 line), stamped.
- **Radical 147 (見)**: fixed the malformed headings `### +-1 Strokes` and `### +-3 Strokes` to `### -1 Stroke` and `### -3 Strokes` (ordered before +0); moved the bottom Aliases block into the +N Strokes groups (视 → 視), stamped.
- **Radical 146 (襾)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (西 +0, 要 +3, 覆 +12, 覇 +13; 覃 → 湛 filed by stroke count), stamped.
- **Radical 145 (衣)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (襠, 裆, 衹 redirects and ¡裹!, ¡裃!, ¡褝!, ¡襅! as 違法字 lines); dropped the annotated duplicate `裡 --> variant of 裏`; turned the alias-backed `錶 --> variant of 表` into a plain `錶 --> 表` under +10 (Stroke 16); moved the unbacked `制 --> variant of 製` to +2 (8 strokes); stamped.
- **Radical 144 (行)**: moved the bottom Aliases block into the +N Strokes groups (衕 → 同), stamped.
- **Radical 143 (血)**: verified (3 characters, groups and 4 alias-backed redirects correct), stamped; no content change.
- **Radical 142 (虫)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (蚯, 蚬, 蛔, 蜚, 蠱, 蛊 redirects and ¡﨡!, ¡蟎! as 違法字 lines), stamped.
- **Radical 141 (虍)**: moved the bottom Aliases block into the +N Strokes groups (號 → 号, 處 → 処), stamped.
- **Radical 140 (艸)**: fixed the malformed headings `### +-1 Strokes` and `### +-2 Strokes` (the latter created by the migration tool) to `### -1 Stroke` and `### -2 Strokes`; refiled 菲 (+5 → +8), 莽 (+6 → +7) and 茜 (+7 → +6) by their `stroke_count` (baseline 3, as the page intro states) and renumbered the entries; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (23 lines, nine forbidden glyphs as 違法字 lines), stamped.
- **Radical 139 (色)**: converted the `## Characters` / `### Used` layout to the standard +N Strokes groups (色 +0, 艶 +13), stamped.
- **Radical 138 (艮)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (艮 +0, 良 +1, 艱 +11; 艰 → 艱 filed by stroke count); dropped the annotated duplicate `艰 --> simplified form of 艱`, stamped.
- **Radical 137 (舟)**: converted the `## Characters` / `### Used` / `### Forbidden` / `### Aliases` layout to the standard +N Strokes groups (舟 +0, 航 and 般 +4, 舵 舶 舷 船 +5, 艇 +7, 艙 +10, 艦 +15; 𦩻, 舱, 舰 redirects and ¡艘!, ¡艠! filed by stroke count), stamped.
- **Radical 136 (舛)**: verified (3 characters, groups correct, no aliases or redirects needed), stamped; no content change.
- **Radical 135 (舌)**: verified (3 characters, groups and 3 alias-backed redirects correct), stamped; no content change.
- **Radical 134 (臼)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (臼 +0, 舅 +7, 興 +10; entries renumbered in stroke order; six redirects filed by stroke count), stamped.
- **Radical 133 (至)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (至 +0, 致 +4, 臺 → 台 filed by stroke count), stamped.
- **Radical 132 (自)**: converted the `## Characters` / `### Used` layout to the standard +N Strokes groups (自 +0, 臭 +3), stamped.
- **Radical 131 (臣)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (臣 +1, 臥 +3, 臨 +12, counted from the radical's Kangxi 6 strokes; 臧 → 臓 and 臦 → 囧 filed by stroke count), kept the 頤 note under `### Other`, stamped.
- **Radical 130 (肉)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (胶 → 交, 膽 → 胆, 胜 → 勝, 腱 → 建 and ¡臉!, ¡脖!, ¡肚!, ¡膵! as 違法字 lines), stamped.
- **Radical 129 (聿)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (肆 +7, 肇 +8; 肅, 肃 → 粛 and 肈 → 肇 filed by stroke count), stamped.
- **Radical 128 (耳)**: moved the bottom Aliases block into the +N Strokes groups (聲 → 声, 聯 → 連, 联 → 連), stamped.
- **Radical 127 (耒)**: switched the `## Characters` / `### Used` layout to the standard `## Strokes` layout (耕 and 耗 both under +4, stroke_count 10), stamped.
- **Radical 126 (而)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (而 +0, 耐 +3, 耑 → 専 filed by stroke count), stamped.
- **Radical 125 (老)**: verified (4 characters, groups correct, no aliases or redirects needed), stamped; no content change.
- **Radical 124 (羽)**: moved the bottom Aliases block into the +N Strokes groups (翳 → 影), stamped.
- **Radical 123 (羊)**: moved the bottom Aliases block into the +N Strokes groups (羔 → 皐), stamped.
- **Radical 122 (网)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (9 characters filed by stroke count, 罒 under a `-1 Stroke` group and 罓 under +0 with their component-only notes kept); dropped the annotated `simplified form of` duplicates of 罗 → 羅 and 罢 → 罷; filed 罚 → 罰, 罗 → 羅, 罢 → 罷, 网 → 網, ¡罖!, ¡罩! by stroke count, stamped.
- **Radical 121 (缶)**: verified (4 characters, groups and 5 alias-backed redirects correct), stamped; no content change.
- **Radical 120 (糸)**: fixed the malformed heading `### +-1 Strokes` to `### -1 Stroke`; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (絕, 绝, 练, 綾, 纸, 缚, 繆, 缪 redirects, ¡繳!, ¡綁!, ¡纃! as 違法字 lines), stamped.
- **Radical 119 (米)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (粮 → 糧, 粃 → 比 and ten forbidden glyphs as 違法字 lines), stamped.
- **Radical 118 (竹)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (箇 → 個, 筑 → 築 and 11 forbidden glyphs as 違法字 lines); 筺 is on the forbidden list, so its `筺 --> 筐` redirect became a `¡筺! - 違法字` line; stamped.
- **Radical 117 (立)**: moved the bottom Forbidden block into the +N Strokes groups (¡竍!, ¡竡!, ¡竏! as 違法字 lines), stamped.
- **Radical 116 (穴)**: verified (21 characters, groups and 13 alias-backed redirects correct), stamped; no content change.
- **Radical 115 (禾)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (穐, 秌, 秕, 稀, 稔 redirects and ¡䆆! as a 違法字 line), stamped.
- **Radical 114 (禸)**: moved the bottom Aliases block into the +N Strokes groups (𥝅 → 万), stamped.
- **Radical 113 (示)**: moved the bottom Aliases block into the +N Strokes groups (禦 → 御, 祂 → 他, 禄 → 祿), stamped.
- **Radical 112 (石)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (矽 → 硅, 硏 → 研 and ¡碰!, ¡砸!, ¡砍!, ¡硴!, ¡硲!, ¡碓! as 違法字 lines), stamped.
- **Radical 111 (矢)**: moved the bottom Aliases block into the +N Strokes groups (𥎵 and 𥏼 → 知), stamped.
- **Radical 110 (矛)**: switched the `## Characters` / `### Used` layout to the standard `## Strokes` / `### +0 Strokes` layout (the single entry 矛 was already present), stamped.
- **Radical 109 (目)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (眀, 眞, 矍 redirects and ¡睜!, ¡盯!, ¡瞇!, ¡瞧!, ¡瞪! as 違法字 lines), stamped.
- **Radical 066 (攴)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (收 → 収, 攵 → 攴, 敎 → 教 and ¡敾! as a 違法字 line), kept the `## Other` notes, stamped.
- **Radical 108 (皿)**: verified (13 characters, groups and 11 alias-backed redirects correct), stamped; no content change.
- **Radical 107 (皮)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (皮 +0, 皺 +10; 皰 → 疱 and 皱 → 皺 filed by stroke count), stamped.
- **Radical 106 (白)**: moved the bottom Aliases block into the +N Strokes groups (皋 → 皐, 皃 → 貌, 畠 → 田), stamped.
- **Radical 105 (癶)**: moved the bottom Aliases block into the +N Strokes groups (發 → 発), removed a stray double blank line, stamped.
- **Radical 104 (疒)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (𤻮 → 応 and ¡疼!, ¡疤!, ¡癪! as 違法字 lines), stamped.
- **Radical 103 (疋)**: moved the bottom Aliases block into the +N Strokes groups (疋 → 匹 under +0), stamped.
- **Radical 102 (田)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (six redirects and ¡畓!, ¡畑!, ¡畩! as 違法字 lines), stamped.
- **Radical 101 (用)**: converted the `## Characters` / `### Used` / `### Forbidden` / `### Aliases` layout to the standard +N Strokes groups (用 +0, 甫 and 甬 +2; 甯 → 寧 and ¡甭! filed by stroke count), stamped.
- **Radical 100 (生)**: moved the bottom Aliases block into the +N Strokes groups (𤯞 → 青), stamped.
- **Radical 099 (甘)**: verified (3 characters, groups correct, no aliases or redirects needed), stamped; no content change.
- **Radical 098 (瓦)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (瓯 → 甌 and five forbidden glyphs as `¡X! - 違法字` lines), stamped.
- **Radical 097 (瓜)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (瓜 +0, 瓢 +12, 瓣 → 弁 filed by stroke count), stamped.
- **Radical 096 (玉)**: refiled 王 (stroke_count 4, one fewer than the radical) under a new `### -1 Stroke` group, as 才 is under 手; moved the bottom Aliases block into the +N Strokes groups, stamped.
- **Radical 095 (玄)**: removed the duplicate annotated redirect `玅 --> variant of 妙` (the plain alias-backed `玅 --> 妙` stays); 3 characters and groups verified, stamped.
- **Radical 094 (犬)**: removed legacy annotated redirect lines ("traditional form of…", "simplified of…", "variant of…") that duplicated alias-backed redirects and sat in wrong stroke groups; converted 貍 → 狸, 貓 → 猫, 豬 → 猪, 兽 → 獣 to plain redirects filed by the Stroke pages' counts; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups; kept the six annotated redirects with no alias backing (叐, 𡗜, 𤝜 → 犮; 雎 → 狙; 狢, 貉 → 狸) and re-filed 雎/狢/貉 by their stroke counts; stamped.
- **Radical 093 (牛)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (牠 → 他, ¡㸴! as a 違法字 line), stamped.
- **Radical 092 (牙)**: switched the `## Characters` / `### Used` layout to the standard `## Strokes` / `### +0 Strokes` layout (the single entry 牙 was already present), stamped.
- **Radical 091 (片)**: verified (3 characters, groups and 3 alias-backed redirects correct), stamped; no content change.
- **Radical 090 (爿)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (牒 +9, 牆 +13, listed in stroke order, so 牒 is now no. 1 and 牆 no. 2); dropped the empty Aliases heading, stamped.
- **Radical 089 (爻)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (爼 → 俎 +5, 爽 +7), stamped.
- **Radical 088 (父)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (父 +0, 爹 +6, 爺 +9; 㸘 and 爷 redirects and ¡爸! filed by stroke count), stamped.
- **Radical 087 (爪)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (爪 +0, 爬 +4, 爰 +5, 爵 +13; redirects 爭, 爯, 爱, 爲, 𤔢 filed by stroke count), kept the 舜 note under `### Other`, stamped.
- **Radical 086 (火)**: refiled 熊 from +20 to +10 (stroke_count 14) and renumbered the entries; moved the bottom Aliases/Forbidden blocks into the +N Strokes groups, stamped.
- **Radical 085 (水)**: verified (175 characters, groups and 123 alias-backed redirect lines correct); removed 2 stray blank lines in the numbered list, stamped.
- **Radical 084 (气)**: converted the `## Characters` / `### Used` / `### Aliases` / `### Forbidden` layout to the standard +N Strokes groups (气 → 気 +0, 気 +2, ¡𬇐! +5, 氣 → 気 +6, 㲵 → 宵 +7, ¡氮! +8), stamped.
- **Radical 083 (氏)**: converted the `## Characters` / `### Used` layout to the standard +N Strokes groups (氏 +0; 氐 and 民 +1), stamped.
- **Radical 082 (毛)**: converted the `## Characters` / `### Used` / `### Forbidden` / `### Aliases` layout to the standard +N Strokes groups (毛 +0; 毫, ¡毟!, 毬 → 球 under +7), stamped.
- **Radical 081 (比)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (比 +0, 毕 → 畢 +2, 毘 and 毗 → 毘 +5), stamped.
- **Radical 080 (毋)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (毋 → 母 under +0, 母 +1, 毎 +2, 每 → 毎 +3, 毒 +4), stamped.
- **Radical 079 (殳)**: verified (8 characters, groups and 5 alias-backed redirects correct), stamped; no content change.
- **Radical 078 (歹)**: verified (8 characters, groups and 4 alias-backed redirects correct), stamped; no content change.
- **Radical 077 (止)**: moved the bottom Aliases block into the +N Strokes groups (歸 → 帰), stamped.
- **Radical 076 (欠)**: verified (12 characters, groups and 8 alias-backed redirects correct), stamped; no content change.
- **Radical 075 (木)**: verified (162 characters, groups and 116 redirect lines correct and alias-backed); removed one stray blank line in the numbered list, stamped.
- **Radical 074 (月)**: moved the bottom Forbidden/Aliases blocks into the +N Strokes groups (朞 → 期, ¡膤! as a 違法字 line), stamped.
- **Radical 073 (曰)**: verified (11 characters, groups and the 曾 → 曽 redirect correct); removed stray double blank lines, stamped.
- **Radical 072 (日)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups, stamped.
- **Radical 071 (无)**: converted the `## Characters` / `### Used` / `### Aliases` layout to the standard +N Strokes groups (无 → 無 under +0, 既 under +6, 旣 → 既 under +7), stamped.
- **Radical 070 (方)**: moved the bottom Forbidden block into the +N Strokes groups (¡旀!, ¡㫇!, ¡㫈!, ¡旕! as 違法字 lines), stamped.
- **Radical 069 (斤)**: verified (7 characters, groups and the three redirects all correct), stamped; no content change.
- **Radical 068 (斗)**: moved the bottom Forbidden block into the +N Strokes groups (¡㪲! and ¡㪳! as 違法字 lines), stamped.
- **Radical 067 (文)**: verified (4 characters, groups and aliases all correct; no redirects needed), stamped; no content change.
- **Radical 065 (支)**: switched the `## Characters` / `### Used` layout to the standard `## Strokes` / `### +0 Strokes` layout (the single entry 支 was already present), stamped.
- **Radical 064 (手)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups, removed a stray blank line in the numbered list, stamped.
- **Radical 063 (戶)**: moved the bottom Aliases block into the +N Strokes groups (戼 → 卯, 戶/户 → 戸), stamped.
- **Radical 062 (戈)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups (redirects re-filed by stroke count), stamped.
- **Radical 061 (心)**: moved the bottom Aliases/Forbidden blocks into the +N Strokes groups, refiled 懺 from +17 to +16 (stroke_count 20), removed a stray blank line in the list, stamped.
- **Radical loop, firing 59 (Radical 060):** grouped page (size 25); verified the 25 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (徵 → 徴) and Forbidden (`¡㣴!`, `¡很!`, `¡𭛝!`, `- 違法字`) sections into the +N groups. Stamped Radical 060.

- **Radical loop, firing 58 (Radical 059):** grouped page (size 10) already in the in-group standard; verified the ten entries, their groups and the redirect 彥 → 彦 against the characters' own radical and alias data (backed); no changes needed. Stamped Radical 059.

- **Radical loop, firing 57 (Radical 058):** prosaic-style page (size 3); verified the three entries and three aliases (彚, 归, 录) against the characters' own radical and alias data (all backed) and shortened the forbidden line for 彔 to `¡彔! - 違法字`. Stamped Radical 058.

- **Radical loop, firing 56 (Radical 057):** grouped page (size 16); verified the sixteen entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (彆, 彊, 强) and Forbidden (`¡㢱!`, `¡彁!`, `¡弖!`, `- 違法字`) sections into the +N groups. Stamped Radical 057.

- **Radical loop, firing 55 (Radical 056):** prosaic-style page (size 2) already in order; verified the two entries (式, 弒) and five aliases against the characters' own radical and alias data (all backed); no changes needed. Stamped Radical 056.

- **Radical loop, firing 54 (Radical 055):** grouped page (size 4); verified the four entries and their groups against the characters' own radical and stroke data, and all four redirects against their main characters' alias lists (backed). Migrated the bottom Aliases (弃, 开) into the +N groups. Stamped Radical 055.

- **Radical loop, firing 53 (Radical 054):** prosaic-style page (size 3) already in order; verified the three entries (延, 廷, 建) and the one alias against the characters' own radical and alias data (backed); no changes needed. Stamped Radical 054.

- **Radical loop, firing 52 (Radical 053):** grouped page (size 24); verified the 24 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (廁, 廚, 𢊍, 座, 应) and Forbidden (`¡廤! - 違法字`) sections into the +N groups. Stamped Radical 053.

- **Radical loop, firing 51 (Radical 052):** grouped page (size 4) already in the in-group standard; verified the four entries, their groups and the one redirect against the characters' own radical and alias data (backed); no changes needed. Stamped Radical 052.

- **Radical loop, firing 50 (Radical 051):** grouped page (size 5) already in the in-group standard; verified the five entries, their groups and both redirects against the characters' own radical and alias data (backed); no changes needed. Stamped Radical 051.

- **Radical loop, firing 49 (Radical 050):** grouped page (size 24); verified the 24 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases block (幂, 帋, 幗, 帼, 师) into the +N groups. Stamped Radical 050.

- **Radical loop, firing 48 (Radical 049):** prosaic-style page (size 7); verified the seven entries and two aliases (㠯, 巺) against the characters' own radical and alias data (backed) and shortened the forbidden line for 巼 to `¡巼! - 違法字`. Stamped Radical 049.

- **Radical loop, firing 47 (Radical 048):** grouped page (size 6); verified the six entries and their groups against the characters' own radical and stroke data, and the redirect 㠮 → 肛 against its main character's alias list (backed). Migrated the bottom Forbidden section (巪, 巬, 巭, 𪩣, 𪩩; now `¡X! - 違法字`) into new +3, +6 and +14 groups. Stamped Radical 048.

- **Radical loop, firing 46 (Radical 047):** grouped page (size 6); verified the six entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases block (𢀎 → 河) into its +N group. Stamped Radical 047.

- **Radical loop, firing 45 (Radical 046):** grouped page (size 23); verified the entries against the characters' own radical and stroke data and found 屿 (stroke_count 6) filed under +14; moved it to +3 and renumbered the entries. Checked every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (嶂, 岛, 巖, 巌) and Forbidden (岾, 屶, 峠, 峅, `- 違法字`) sections into the +N groups; `屶 → 会` became the forbidden line, as the tool files a forbidden glyph. Stamped Radical 046.

- **Radical loop, firing 44 (Radical 045):** prosaic-style page (size 2) already in order; verified the two entries (屮, 屯) and the one alias against the characters' own radical and alias data (all backed); no changes needed. Stamped Radical 045.

- **Radical loop, firing 43 (Radical 044):** grouped page (size 21); verified the 21 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Forbidden section (`¡𡱖! - 違法字`) into its +N group. Stamped Radical 044.

- **Radical loop, firing 42 (Radical 043):** prosaic-style page (size 3) already in order; verified the three entries (尤, 尭, 就) against the characters' own radical data; the page has no aliases or forbidden entries and the characters' alias data adds none; no changes needed. Stamped Radical 043.

- **Radical loop, firing 41 (Radical 042):** grouped page (size 8); verified the eight entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (尝, 尙, 尓, 尔) and Forbidden (`¡龸! - 違法字`) sections into the +N groups. Stamped Radical 042.

- **Radical loop, firing 40 (Radical 041):** grouped page (size 13); verified the thirteen entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (导, 將) and Forbidden (`¡寽! - 違法字`) sections into the +N groups. Stamped Radical 041.

- **Radical loop, firing 39 (Radical 040):** grouped page (size 46); verified the 46 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the Aliases block (宔, 宥, 㝎) that sat under `## Other` into the +N groups. Stamped Radical 040.

- **Radical loop, firing 38 (Radical 039):** grouped page (size 13); verified the thirteen entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases block (學 → 学) into its +N group. Stamped Radical 039.

- **Radical loop, firing 37 (Radical 038):** grouped page (size 62); verified the 62 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (娚, 娼) and Forbidden (奶, 媤, 妛, 媸, 嬶, 𪥽 and 她, now `¡X! - 違法字`) sections into the +N groups; the old `她 → 他` redirect became the forbidden line, as the migration tool files a forbidden glyph. Stamped Radical 038.

- **Radical loop, firing 36 (Radical 037):** grouped page (size 23); verified the 23 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (奛, 奌, 㚔, 夬, 头) and Forbidden (`¡夻!`, `¡𡗗!`, `- 違法字`) sections into the +N groups; no redirect lost or added. Stamped Radical 037.

- **Radical loop, firing 35 (Radical 036):** grouped page (size 6); verified the six entries and their groups against the characters' own radical and stroke data. Migrated the bottom Aliases (夘 → 卯) and Forbidden (`¡夞!`, `¡夠!`, `- 違法字`) sections into the +N groups (new +7 and +8 groups). Open question: 夘 is listed as an alias of both 卯 and 夗, so the page carries both redirects until the user picks one parent. Stamped Radical 036.

- **Radical loop, firing 34 (Radical 035):** prosaic-style page (size 1) already in order; verified the entry 夏 and the two aliases against the characters' own radical and alias data (all backed); no changes needed. Stamped Radical 035.

- **Radical loop, firing 33 (Radical 034):** prosaic-style page (size 2); verified the two entries and three aliases (处, 备, 夆) against the characters' own radical and alias data (all backed) and shortened the forbidden line for 复 to `¡复! - 違法字`. Stamped Radical 034.

- **Radical loop, firing 32 (Radical 033):** grouped page (size 8); verified the eight entries, their groups and every redirect against the characters' own radical and alias data (all backed). Migrated the bottom Forbidden section (`¡壭! - 違法字`) into a new +2 group. Stamped Radical 033.

- **Radical loop, firing 31 (Radical 032):** grouped page (size 67); verified the 67 entries and their groups against the characters' own radical and stroke data, and every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (圣, 坮, 场, 塲) and Forbidden (13 lines, now `¡X! - 違法字`) sections into the +N groups; no redirect was lost or added. Stamped Radical 032.

- **Radical loop, firing 30 (Radical 031):** grouped page (size 16); verified the sixteen entries, their groups and every redirect against the characters' own radical and alias data (all backed). Migrated the bottom Aliases (圍, 围, 國, 图; 圖 was already in its group) and Forbidden (`¡圕! - 違法字`) sections into the +N groups. Stamped Radical 031.

- **Radical loop, firing 29 (Radical 030):** grouped page (size 123); verified the 123 entries and their groups against the characters' own radical and stroke data, and checked every redirect against its main character's alias list (all backed). Migrated the bottom Aliases (15 lines) and Forbidden (33 lines) sections into the +N groups with radical_migrate.py, the forbidden lines now `¡X! - 違法字`. Stamped Radical 030.

- **Radical loop, firing 28 (Radical 029):** grouped page (size 14); verified the fourteen entries, their groups and all aliases (叛, 发, 㕛, 变, 叏, 叠) against the characters' own radical and alias data (all backed). Migrated the bottom Aliases and Forbidden (`¡叟! - 違法字`) sections into the +N groups (new +3 and +8 groups) and removed a stray blank line that split the numbered list in +2. Stamped Radical 029.

- **Radical loop, firing 27 (Radical 028):** prosaic-style page (size 2); verified the two entries and the six aliases (厷, 县, 參, 叁, 厶, 㕗) against the characters' own radical and alias data (all backed) and shortened the forbidden line for 厼 to `¡厼! - 違法字`. Stamped Radical 028.

- **Radical loop, firing 26 (Radical 027):** grouped page (size 11); verified the eleven entries, their groups and all aliases (厕, 㕑, 厲, 厅, 厈, 压, 厦, 厭) against the characters' own radical and alias data (all backed). Migrated the bottom Aliases (厕, 㕑, 厰, 厂) and Forbidden (`¡历! - 違法字`) sections into the +N groups (new +0 group for the radical handle 厂 → 廠). Stamped Radical 027.

- **Radical loop, firing 25 (Radical 026):** grouped page (size 8); verified the eight entries, their groups and all aliases (卬, 卻, 卽, 卷, 卫) against the characters' own radical and alias data (all backed). Migrated the bottom Aliases (卬, 卽, 卷) and Forbidden (`¡卪!`, `¡𰆊!`, `¡厁!`, `- 違法字`) sections into the +N groups (new +0, +2, +6 and +11 groups). Stamped Radical 026.

## 2026-11-10

- **Radical loop, firing 24 (Radical 025):** prosaic-style page (size 4); verified the four entries and three aliases (𠀝, 卢, 卤) against the characters' own radical and alias data (all backed) and shortened the forbidden line for 卡 to `¡卡! - 違法字`. Stamped Radical 025.

- **Radical loop, firing 23 (Radical 024):** grouped page (size 14); verified the fourteen entries, their groups and all six aliases (卆, 协, 卐, 单, 华, 卖) against the characters' own radical and alias data. Migrated the bottom Aliases (单, 卖) and Forbidden (`¡卂!`, `¡卅!`, `- 違法字`) sections into the +N groups. Stamped Radical 024.

- **Radical loop, firing 22 (Radical 023):** grouped page (size 5) already in order; verified the five entries, their groups and the redirect 區 → 区 against the characters' own radical and alias data; no changes needed. Stamped Radical 023.

- **Radical loop, firing 21 (Radical 022):** prosaic-style page (size 1) already in order; verified the entry 匡 and the alias 匯 → 彙 against the characters' own radical and alias data; no changes needed. Stamped Radical 022.

- **Radical loop, firing 20 (Radical 021):** prosaic-style page (size 4) already in order; verified the four entries and two aliases (匘, 㔬) against the characters' own radical and alias data; no changes needed. Stamped Radical 021.

- **Radical loop, firing 19 (Radical 020):** grouped page (size 6); verified the six entries, their groups and the redirects (匀, 匊, 匋, 匐) against the characters' own radical and alias data (all backed). Migrated the bottom Forbidden section (`¡匁!`, `¡匂!`, `- 違法字`) into the +2 group. Stamped Radical 020.

- **Radical loop, firing 18 (Radical 019):** grouped page (size 28); verified the 28 entries and their groups against the characters' own radical and stroke data. Migrated the bottom Forbidden (`¡㔖!`, `¡㔔!`, `¡𪟧!`) and Aliases (勞, 劳) sections into the +N groups, removed ten plain redirects already covered by an annotated line (动, 务, 劲, 势, 劳, 勋, 勛, 勞, 勳, 勸) and the stale `𠠲 → variant of 力` (力 no longer lists 𠠲 as an alias). Stamped Radical 019.

- **Radical loop, firing 17 (Radical 018):** grouped page (size 39); verified the 39 entries and their groups against the characters' own radical and stroke data, and every redirect (划, 刘, 则, 刚, 创, 删, 别, 剎, 剏, 剑, 剔, 剥, 剧, 剩, 劍, 劑, 劒, 劔) against its main character's alias list. Migrated the bottom Aliases (劍, 剑, 别, 删, 划, 剧) and Forbidden (`¡刖! - 違法字`) sections into the +N groups. Stamped Radical 018.

- **Radical loop, firing 16 (Radical 017):** prosaic-style page (size 5) already in order; verified the five entries and two aliases (击, 凾) against the characters' own radical and alias data; no changes needed. Stamped Radical 017.

- **Radical loop, firing 15 (Radical 016):** prosaic-style page (size 4); verified the four entries and four aliases against the characters' own radical and alias data (all backed) and shortened the three forbidden lines (凧, 凪, 凩) to `¡X! - 違法字`. Stamped Radical 016.

- **Radical loop, firing 14 (Radical 015):** grouped page (size 10); verified the ten entries, their groups and all aliases against the characters' own radical and alias data (all backed). Migrated the bottom Aliases block (净, 决, 冽) into the +N groups and removed a stray blank line that split the numbered list in +5. Stamped Radical 015.

- **Radical loop, firing 13 (Radical 014):** grouped page (size 8) already in the in-group standard; verified the eight entries, their groups and the five aliases against the characters' own radical and alias data; no changes needed. Stamped Radical 014.

- **Radical loop, firing 12 (Radical 013):** prosaic-style page (size 6); verified the six entries and the seven aliases against the characters' own radical and alias data (all backed) and shortened the forbidden line for 冋 to `¡冋! - 違法字`. Stamped Radical 013.

- **Radical loop, firing 11 (Radical 012):** grouped page (size 10); verified the ten entries, their groups and the seven aliases against the characters' own radical and alias data. Migrated the Forbidden (`¡兯!`) and Aliases (兴, 关, 冀) blocks that sat under `## Other` into the +N groups (new +14 group for 冀) and removed stray blank lines that split the numbered lists in +2 and +6. Stamped Radical 012.

- **Radical loop, firing 10 (Radical 011):** grouped page (size 3); verified the three entries and their groups against the characters' own radical and stroke data. Migrated the bottom Aliases and Forbidden sections into the +N groups (`¡㒱! - 違法字`), dropped the placeholder `forbidden 㒱` and the plain redirects already covered by an annotated line (`𠓛 → 集`, `㒰 → 全`, `內 → 内`, `兩 → 両`, `㒳 → 両`). Stamped Radical 011.

- **Radical loop, firing 9 (Radical 010):** grouped page (size 16); verified the sixteen entries and their groups against the characters' own radical and stroke data, and all aliases (儿, 兑, 兒, 兔, 兖) against the characters' alias lists. Migrated the bottom Aliases (兖, 兔, 兇) and Forbidden (`¡𪞄!`, `- 違法字`) sections into the +N groups (new +13 group for 𪞄). Stamped Radical 010.

- **Radical loop, firing 8 (Radical 008):** grouped page (size 11); verified the eleven entries, their groups and the aliases against the characters' own radical and alias data (all backed), and migrated the bottom Forbidden section into the groups (`¡亪! - 違法字`). Stamped Radical 008.

- **Radical loop, firing 7 (Radical 007):** grouped page (size 9); verified the nine entries and groups against the characters' own radical and stroke data. Migrated the bottom Forbidden section into the groups (`¡亍!` and `¡亟!`, `- 違法字`), dropped the placeholder lines `forbidden 亍` and `forbidden 亟`, the plain redirects already covered by an annotated line (亖, 云, 亚, 亞) and `亏 → variant of 虧` (虧 has no page). Stamped Radical 007.

- **Radical loop, firing 6 (Radical 006):** prosaic-style page (size 4); verified the four entries and three aliases against the characters' own radical and alias data (亊 is backed by 事's alias section), and shortened the forbidden line for 亇 to `¡亇! - 違法字`. Stamped Radical 006.

- **Radical loop, firing 5 (Radical 005):** prosaic-style page (size 7); verified the seven entries and seven aliases against the characters' own radical and alias data (all backed), and shortened all 27 forbidden lines (every one is on 文法 - 98違法字) to `¡X! - 違法字`. Stamped Radical 005.

- **Radical loop, firing 4 (Radical 004):** prosaic-style page (size 10); verified the ten entries and the thirteen aliases against the characters' own radical and alias data (all backed), and shortened the six forbidden lines (乊, 乒, 乓, 𠂇, 乄, 〆) to `¡X! - 違法字`. Stamped Radical 004.

- **Radical loop, firing 3 (Radical 003):** prosaic-style page (size 3); verified the three entries (丸, 丹, 主) and the four aliases (丼, 举, 为, 义) against the characters' own radical and alias data, and shortened the forbidden line for 丷 to `¡丷! - 違法字`. Stamped Radical 003.

- **Radical loop, firing 2 (Radical 002):** verified the 2 entries (中, 串) and groups against the characters' radical data. Migrated the bottom Aliases and Forbidden sections into the +N groups (forbidden 㐃 and 丵 now `¡X! - 違法字`), dropped the duplicate `个 → 個` and the placeholder lines `forbidden 丩`, `forbidden 㐃` and `forbidden 丵` (丩 is an alias of 糾, not on the forbidden list). Stamped Radical 002.

- **Radical loop, firing 1 (Radical 001):** character list, +N groups and size (20) verified against the characters' own `radical` and stroke data. Migrated the bottom Aliases and Forbidden sections into the +N Strokes groups with radical_migrate.py (new groups +4 to +11 entries for 业, 㐀, 𠀃, 𠀇, 两, 严, 丆, 丟, 𠁈), standardised the forbidden lines to `¡X! - 違法字`, and removed 17 plain redirects already covered by an annotated line (e.g. `丂 → 考` under `丂 → ancient variant of 于 and of 考`) plus the legacy `丟/丢` bullet. Also corrected the 心 count on Radicals.md from 106 to 107. Stamped Radical 001.

- **SKIP leaf loop, firing 58 (SKIP-2-12-9, 2-13-6, 2-15-7, 2-19-3, 2-20-5, 2-4-18, SKIP-3-2-28, 3-5-15, 3-5-17, SKIP-1-1-1) — sweep complete:** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Replaced a stray non-breaking space in the 八 entry of SKIP-1-1-1. The stroke-count flags on SKIP-2-15-7 and 2-20-5 are alias-only leaves whose stroke_count matches the alias's real total. Every SKIP leaf now carries today's stamp.

- **SKIP leaf loop, firing 57 (SKIP-1-13-4, 1-14-4, 1-16-4, 1-17-4, 1-17-5, 1-18-10, 1-4-19, 1-9-12, SKIP-2-12-10, 2-12-12):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. The stroke-count heuristic flagged SKIP-1-17-4 and 1-9-12, but 22 is the true total of 歡, and SKIP-1-9-12 collects aliases of different stroke counts (饒, 鞾, 饑) under one code, so its single stroke_count cannot match them all; nothing changed. Stamped the ten leaves.

- **SKIP leaf loop, firing 56 (SKIP-2-13-11, 2-13-7, 2-16-2, 2-19-4, 2-8-12, SKIP-3-2-14, 3-5-14, 3-8-11, SKIP-1-10-16, 1-12-11):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 55 (SKIP-3-9-5, SKIP-1-17-2, 1-17-7, 1-2-1, 1-2-3, 1-5-15, SKIP-2-1-12, 2-1-8, 2-12-11, 2-12-6):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. The stroke-count heuristic flagged SKIP-1-17-2, 1-17-7 and 1-5-15, but their stroke_count values (20, 25, 19) are the real totals of 勸, 觀, 襤 and 礦, so nothing changed. Stamped the ten leaves.

- **SKIP leaf loop, firing 54 (SKIP-2-7-1, 2-7-14, 2-8-1, 2-9-1, 2-9-9, SKIP-3-10-6, 3-5-16, 3-5-2, 3-5-3, 3-8-13):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 53 (SKIP-1-2-17, 1-2-20, 1-3-25, 1-4-20, 1-4-24, 1-5-16, 1-8-13, 1-9-15, SKIP-2-10-1, 2-6-1):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. My stroke-count heuristic (left + right strokes) flagged SKIP-1-2-20 as 21 vs 22, but 21 is the correct Unihan total for 儼 (亻 counts as one stroke there), so the leaf, Stroke 21 and Radical 009 stay as they are. Stamped the ten leaves.

- **SKIP leaf loop, firing 52 (SKIP-4-9-2 to 4-9-4, SKIP-1-3-20, 1-12-1, 1-13-3, SKIP-2-12-15, 2-14-15, 2-9-18, SKIP-1-1-5):** the last three leaves from the original 2026-10-31 batch plus the oldest of the leaves stamped on 2026-11-05 to 2026-11-09; checked each against the characters' own `skip_number` and `## Aliases` data, no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 51 (SKIP-4-6-4, 4-7-1 to 4-7-4, 4-8-1 to 4-8-4, 4-9-1):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 50 (SKIP-4-4-2 to 4-4-4, 4-5-1 to 4-5-4, 4-6-1 to 4-6-3):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 49 (SKIP-4-15-4, 4-2-1 to 4-2-4, 4-3-1 to 4-3-4, 4-4-1):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 48 (SKIP-4-1-4, 4-10-2 to 4-10-4, 4-11-3, 4-11-4, 4-12-4, 4-13-1, 4-13-3, 4-14-1):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 47 (SKIP-3-8-10, 3-8-2, 3-8-4, 3-8-6 to 3-8-9, SKIP-3-9-2, 3-9-9, SKIP-4-1-1):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. SKIP-3 is now fully stamped; only the SKIP-4 leaves remain. Stamped the ten leaves.

- **SKIP leaf loop, firing 46 (SKIP-3-6-8, 3-6-9, SKIP-3-7-13, SKIP-3-7-2 to 3-7-5, 3-7-7 to 3-7-9):** checked each leaf against the characters' own `skip_number` and `## Aliases` data, including SKIP-3-7-13, the redirect-only leaf built during the alias loop; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 45 (SKIP-3-5-6 to 3-5-9, SKIP-3-6-11, SKIP-3-6-3 to 3-6-7):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 44 (SKIP-3-4-6 to 3-4-9, SKIP-3-5-10, 3-5-12, 3-5-13, 3-5-18, 3-5-4, 3-5-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data, including SKIP-3-5-18, the redirect-only leaf built during the alias loop; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 43 (SKIP-3-4-11 to 3-4-15, 3-4-19, SKIP-3-4-2 to 3-4-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 42 (SKIP-3-3-21, 3-3-22, SKIP-3-3-3 to 3-3-9, SKIP-3-4-10):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 41 (SKIP-3-3-10 to 3-3-18, SKIP-3-3-2):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. In SKIP-3-3-2 removed the annotated duplicate `弍 → [[二 (char)]]` (the plain `弍 → 二` stays). Stamped the ten leaves.

- **SKIP leaf loop, firing 40 (SKIP-3-2-20, 3-2-22, SKIP-3-2-3 to 3-2-9, SKIP-3-3-1):** checked each leaf against the characters' own `skip_number` and `## Aliases` data, including SKIP-3-2-20, the redirect-only leaf built during the alias loop; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 39 (SKIP-3-10-7, 3-10-8, SKIP-3-2-1, 3-2-10 to 3-2-13, 3-2-15, 3-2-17, 3-2-2):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. In SKIP-3-10-8 merged the separate Redirect block into the Aliases block, dropped the duplicate `鬩 → [[䦧 (char)]]` and removed `魍 → 罔` (罔 only notes 魍 as a 代用字 relationship, not an alias). Removed `厮 → 廝` from SKIP-3-2-12 (廝 has no page and no alias entry). Stamped the ten leaves.

- **SKIP leaf loop, firing 38 (SKIP-3-1-1, 3-1-2, 3-1-4, 3-1-7, SKIP-3-10-10, 3-10-11, 3-10-14, 3-10-16, 3-10-4, 3-10-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the duplicated `鬧 → 閙` redirect in SKIP-3-10-5. Stamped the ten leaves (SKIP-1 and SKIP-2 are now fully stamped; SKIP-3 and SKIP-4 remain).

- **SKIP leaf loop, firing 37 (SKIP-2-8-6 to 2-8-9, SKIP-2-9-12, SKIP-2-9-2, 2-9-4 to 2-9-7):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 36 (SKIP-2-7-7, 2-7-9, SKIP-2-8-10, 2-8-11, 2-8-13, 2-8-16, SKIP-2-8-2 to 2-8-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the orphaned redirect `鬯 → 暢` from SKIP-2-8-2: the 暢 page records that 鬯 was deliberately removed as an alias. Stamped the ten leaves.

- **SKIP leaf loop, firing 35 (SKIP-2-6-5 to 2-6-9, SKIP-2-7-11, SKIP-2-7-3 to 2-7-6):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. SKIP-2-6-6 had its redirects split over two alias blocks (a `## Aliases` and a `### Aliases`) with `筑 → 築` and `單 → 単` each listed twice; merged them into one deduplicated `### Aliases` block (no redirect added or lost). Stamped the ten leaves.

- **SKIP leaf loop, firing 34 (SKIP-2-6-12 to 2-6-17, 2-6-19, SKIP-2-6-2 to 2-6-4):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 33 (SKIP-2-5-2 to 2-5-9, SKIP-2-6-10, 2-6-11):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 32 (SKIP-2-5-1, 2-5-10 to 2-5-17, 2-5-19):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 31 (SKIP-2-4-12, 2-4-13, 2-4-17, SKIP-2-4-2 to 2-4-4, 2-4-6 to 2-4-9):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the orphaned redirect `曩 → 嚢` from SKIP-2-4-17 (嚢 does not list 曩 as an alias and no other lookup page carries it); the leaf is now an empty ø leaf. Stamped the ten leaves.

- **SKIP leaf loop, firing 30 (SKIP-2-3-3 to 2-3-9, SKIP-2-4-1, 2-4-10, 2-4-11):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 29 (SKIP-2-3-12 to 2-3-20, SKIP-2-3-2):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the orphaned redirects `騫 → 鍵` (SKIP-2-3-17) and `巍 → 魏` (SKIP-2-3-18): neither 鍵 nor 魏 lists them as an alias and no other lookup page carries them. Stamped the ten leaves.

- **SKIP leaf loop, firing 28 (SKIP-2-2-3 to 2-2-9, SKIP-2-3-1, 2-3-10, 2-3-11):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **囑 added as an alias of 嘱 (user decision):** `aliases:` now lists 囑 (traditional form, EDRDG SKIP 1-3-21, 24 strokes); new `## Aliases` section; redirects on Stroke 24, Radical 030 and the existing SKIP-1-3-21 entry. 嘱 has no Classical Chinese rank (nor does 囑), so `mc_id` stays blank.

- **SKIP leaf loop, firing 27 (SKIP-2-2-12 to 2-2-20):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the duplicate `襃 → 褒` from SKIP-2-2-15 (it belongs to SKIP-2-2-14, where it already is) and the wrong `齎 → 斉` from SKIP-2-2-19 and Radical 210: the 斉 page states that 齎 is a separate character, not a variant, so it is no alias (SKIP-2-2-19 is now an empty ø leaf). Stamped the ten leaves.

- **SKIP leaf loop, firing 26 (SKIP-2-15-2, 2-15-8, SKIP-2-16-3, 2-16-4, 2-16-6, 2-16-7, SKIP-2-19-11, SKIP-2-2-1, 2-2-10, 2-2-11):** checked each leaf against the characters' own `skip_number` and `## Aliases` data, including the redirect-only leaves built during the alias loop (2-15-8, 2-16-3, 2-19-11); no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 25 (SKIP-2-12-7, 2-12-8, SKIP-2-13-3 to 2-13-5, 2-13-9, SKIP-2-14-2 to 2-14-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 24 (SKIP-2-11-6 to 2-11-9, SKIP-2-12-13, 2-12-14, 2-12-16, SKIP-2-12-3 to 2-12-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 23 (SKIP-2-10-7 to 2-10-9, SKIP-2-11-10, 2-11-11, 2-11-13, SKIP-2-11-2 to 2-11-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the orphaned `瞿 → 衢` from SKIP-2-10-8 (衢 lists 矍, not 瞿, as its alias, and `矍 → 衢` is already in SKIP-2-10-10) and the self-redirect `熈 → 熈` from SKIP-2-11-4 (the real `熈 → 熙` stays). Stamped the ten leaves.

- **SKIP leaf loop, firing 22 (SKIP-2-10-10 to 2-10-13, 2-10-15, 2-10-16, 2-10-2, 2-10-3, 2-10-5, 2-10-6):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the misplaced `蠶 → 蚕` redirect from SKIP-2-10-16 (蚕's alias section puts 蠶 at SKIP 2-12-12, where its redirect already is); the leaf is now an empty ø leaf. Stamped the ten leaves.

- **SKIP leaf loop, firing 21 (SKIP-1-9-9, SKIP-2-1-1, 2-1-11, SKIP-2-1-2 to 2-1-7, 2-1-9):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 20 (SKIP-1-8-9, SKIP-1-9-10, 1-9-11, SKIP-1-9-2 to 1-9-8):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 19 (SKIP-1-8-15, 1-8-16, 1-8-19, SKIP-1-8-2 to 1-8-8):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 18 (SKIP-1-7-5 to 1-7-9, SKIP-1-8-1, 1-8-10 to 1-8-12, 1-8-14):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no mismatches. Replaced the non-breaking spaces in a Forbidden note in SKIP-1-7-6 with ordinary spaces. Stamped the ten leaves.

- **SKIP leaf loop, firing 17 (SKIP-1-7-13 to 1-7-19, SKIP-1-7-2 to 1-7-4):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 16 (SKIP-1-6-4 to 1-6-9, SKIP-1-7-1, SKIP-1-7-10 to 1-7-12):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 15 (SKIP-1-6-11 to 1-6-17, SKIP-1-6-2, SKIP-1-6-22, SKIP-1-6-3):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 14 (SKIP-1-5-2 to 1-5-9, SKIP-1-6-1, SKIP-1-6-10):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 13 (SKIP-1-4-7 to 1-4-9, SKIP-1-5-1, SKIP-1-5-10 to 1-5-14, SKIP-1-5-17):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 12 (SKIP-1-4-15 to 1-4-18, 1-4-2, 1-4-21, 1-4-3 to 1-4-6):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. Removed the duplicated `爛 → 乱` redirect in SKIP-1-4-17. Stamped the ten leaves.

- **SKIP leaf loop, firing 11 (SKIP-1-3-6 to 1-3-9, SKIP-1-4-1, SKIP-1-4-10 to 1-4-14):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 10 (SKIP-1-3-16 to 1-3-19, 1-3-2, 1-3-21, 1-3-22, 1-3-3, 1-3-4, 1-3-5):** checked each leaf against the characters' own `skip_number` and `## Aliases` data. In SKIP-1-3-16 removed three orphaned redirects, 瀘 → 盧, 瀚 → 翰 and 瀟 → 䔥 (no character page lists them as aliases; 翰 has no page at all). SKIP-1-3-21 keeps `囑 → 嘱`, which no alias section backs yet (嘱 names 囑 as its traditional form in prose only). Stamped the ten leaves.

- **SKIP leaf loop, firing 9 (SKIP-1-2-7 to 1-2-9, SKIP-1-3-1, SKIP-1-3-10 to 1-3-15):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 8 (SKIP-1-2-11 to 1-2-15, 1-2-19, 1-2-2, 1-2-4, 1-2-5, 1-2-6):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 7 (SKIP-1-14-3, 1-14-9, 1-15-10, 1-15-4, 1-15-5, 1-15-6, 1-15-9, 1-16-11, 1-17-11, 1-2-10):** checked each leaf against the characters' own `skip_number` and `## Aliases` data, including the redirect-only leaves built during the alias loop (1-14-9, 1-15-4, 1-15-9, 1-16-11); no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 6 (SKIP-1-12-2 to 1-12-7, 1-12-9, 1-13-2, 1-13-6, 1-14-2):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 5 (SKIP-1-11-18, SKIP-1-11-2 to 1-11-9, SKIP-1-12-10):** checked each leaf against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 4 (SKIP-1-11-11 to 1-11-16, SKIP-2-10-4, SKIP-2-4-5, SKIP-2-9-3, SKIP-3-8-3):** checked each leaf against the characters' own data. Removed the duplicated `鱆 → 章` redirect in SKIP-1-11-11 and the stray `糶 → 翟` redirect in SKIP-1-11-14 (翟 does not list 糶 as an alias, and 糶 has no page), with its now-empty Aliases heading. Stamped the ten leaves.

- **SKIP leaf loop, firing 3 (SKIP-1-10-19, 1-10-2 to 1-10-9, 1-11-10):** checked each leaf's characters, redirects and frontmatter against the characters' own `skip_number` and `## Aliases` data; no differences found. Stamped the ten leaves.

- **SKIP leaf loop, firing 2 (SKIP-1-1-4, 1-1-7, 1-1-8, 1-10-10 to 1-10-14, 1-10-17, 1-10-18):** checked each leaf's characters, redirects and frontmatter. In SKIP-1-10-11 removed the stray redirects 髏 → 婁, 鶲 → 翁, 鶻 → 紇, 鷂 → 紙鳶 and 鷆/鷏 → 真 (no character page lists them as aliases), 鶺 → 脊 (it belongs to SKIP-2-10-11, where it already is), and the duplicated 鷄 → 鶏. Stamped the ten leaves.

- **SKIP leaf loop, firing 1 (SKIP-4-0-1…4, SKIP-3-8-5, SKIP-3-8-12, SKIP-1-1-1, SKIP-1-1-11, SKIP-1-1-2, SKIP-1-1-3):** checked against the characters' own `skip_number` values and their `## Aliases` sections (no missing or stray redirects); removed the duplicated `儿 --> 児` redirect in SKIP-1-1-1 (one copy used a non-breaking space) and normalised the non-breaking space in `刂 --> Radical 018`; stamped the ten pages.

- **湧 (last alias page):** `aliases:` rewritten as a list (it was a bare scalar the tool could not read), `## Aliases` section and redirects built for 涌 (EDRDG 1-3-7); `mc_id` 2620 from its rank. The alias backlog is now zero.

- **Alias loop, batch 150 (遡, 麻, 懺, 芹) — backlog complete:** `## Aliases` sections and redirects for 泝, 溯, 痲, 忏, 懴 and 斳 (all but 忏 from EDRDG; its computed SKIP code is logged in project_alias_skip_guesses). `mc_id` of 遡 set to 3917 (泝). Removed the rare 菦 and 䓅 (no usable definitions). Every character with an `aliases:` list now has its `## Aliases` section.

- **Alias loop, batch 149 (獺, 蟻, 鰥, 愕, 京, 懐, 攘, 暴, 沢, 耗):** `## Aliases` sections and redirects for 獭, 蚁, 螘, 鳏, 咢, 亰, 懷, 襄, 曝, 澤, 泽 and 秏 (most from EDRDG; computed SKIP codes for 獭, 蚁, 鳏 and 泽 logged in project_alias_skip_guesses). Corrected 獺's `mc_id` from 0 to 3831: it does appear in `CC 3000` at rank 3831, and its rank bullet now says so. Removed the rare 㺚, 㐮 and 㘪 (no usable definitions).

- **Alias loop, batch 148 (用, 約, 耀, 赤, 鉄, 閏, 験, 鳩, 儺, 兌):** `## Aliases` sections and redirects for 癰, 痈, 癕, 佣, 傭, 约, 燿, 瑶, 鐵, 铁, 鐡, 銕, 鋨, 闰, 閠, 驗, 验, 騐, 鸠, 傩 and 兑 (most from EDRDG; computed SKIP codes for the simplified forms logged in project_alias_skip_guesses). New redirect-only leaf SKIP-3-5-18 (for 癰) with its index entry. Removed the rare 砽, 㿈, 灻, 𤆍, 烾, 𨬿, 𨮯, 𨫓, 䥫, 䦞, 𥹿, 𩥾 and 䲥 (no usable definitions), so 赤 now has no aliases.

- **Alias loop, batch 147 (冉, 力, 厉, 姉, 姪, 婦, 尺, 弟, 彩, 従):** `## Aliases` sections and redirects for 冄, 厲, 蛎, 蠣, 蠇, 癩, 癘, 疠, 姐, 姊, 侄, 妷, 妇, 睪, 悌, 棣, 鵜, 綵, 從, 从, 慫 and 怂 (most from EDRDG; computed SKIP codes for 蠇, 疠, 妇 and 怂 logged in project_alias_skip_guesses). `mc_id` of 彩 set to 3188 (綵). Removed the rare 𠠲, 㜼 and 𡥺 (no definitions), so 力 now has no aliases.

- **Alias loop, batch 146 (龍, 巷, 張, 攅, 濁, 燐, 猿, 臘, 詩, 霓):** `## Aliases` sections and redirects for 竜, 龙, 隴, 陇, 瓏, 壟, 衖, 张, 漲, 涨, 攢, 攒, 浊, 磷, 鏻, 粦, 璘, 猴, 腊, 臈, 诗, 蜺 and 蛪 (most from EDRDG; computed SKIP codes for the simplified forms logged in project_alias_skip_guesses). New redirect-only leaf SKIP-2-16-3 (for 壟) with its index entry. `mc_id` of 猿 set to 3334 (猴) and of 霓 to 2997 (蜺). Removed the rare 龎 (it belongs to 龐), 𨻫, 㡣, 䮾, 𢅛, 𨞠, 𨜕, 䢽, 𧃮, 㷠, 𤝌, 𫞇, 𦡳 and 𦠼 (no usable definitions).

- **Alias loop, batch 145 (晩, 杯, 架, 棕, 蝎, 誹, 跳, 還, 顔, 餓):** `## Aliases` sections and redirects for 晚, 盃, 桮, 椶, 蠍, 诽, 还, 顏, 颜 and 饿 (盃, 桮, 椶, 蠍 and 顏 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). Removed the rare 榢, 𨁓, 𨃜, 䟭 and 𨁔 (no usable definitions), so 架 and 跳 now have no aliases.

- **Alias loop, batch 144 (十, 叉, 及, 向, 岸, 已, 慙, 才, 把, 択):** `## Aliases` sections and redirects for 什, 扠, 笈, 曏, 嚮, 屽, 厈, 慚, 惭, 纔, 杷, 擇 and 择 (all but 惭 and 择 from EDRDG; the two computed SKIP codes are logged in project_alias_skip_guesses). `mc_id` of 慙 set to 1726 (慚). Removed the rare 㣾, 紁, 﨤, 㟁, 垾, 㠯 and 𰑧 (no usable definitions), so 已 now has no aliases.

- **Alias loop, batch 143 (七, 上, 中, 之, 乙, 井, 公, 刀, 分, 剝):** `## Aliases` sections and redirects for 柒, 桼, 丄, 釔, 钇, 丼, 蚣, 蜙, 份 and 剥 (all but 钇 from EDRDG; its computed SKIP code is logged in project_alias_skip_guesses). New redirect-only leaves SKIP-1-8-1 (for 釔) and SKIP-1-5-1 (for 钇) with their index entries. Removed the rare 𠀁, 𠁩, 㞢, 𠔇, 𡳿, 𧌻, 𠚣, 𠚩, 𠚬 and 𠧓 (no definitions), so 中, 之 and 刀 now have no aliases.

- **Alias loop, batch 142 (膚, 花, 虫, 謝, 貝, 転, 辛, 野, 鋭, 闘):** `## Aliases` sections and redirects for 肤, 蟲, 谢, 藉, 贝, 轉, 转, 亲, 墅, 埜, 壄, 銳, 锐, 鬪, 鬥 and 鬭 (蟲, 藉, 轉, 墅, 埜, 壄, 鬪, 鬥 and 鬭 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). New redirect-only leaf SKIP-3-10-14 (for 鬭) with its index entry. Removed the rare 𩸽, 䇂, 㙒, 𡐨 and 𡑀 (no usable definitions), so 花 now has no aliases.

- **Alias loop, batch 141 (煙, 父, 狭, 獣, 監, 種, 純, 絞, 繋, 胡):** `## Aliases` sections and redirects for 烟, 狹, 獸, 兽, 监, 种, 纯, 諄, 绞, 繫 and 鬍 (烟, 狹, 獸, 諄, 繫 and 鬍 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). New redirect-only leaves SKIP-1-15-4 (for 獸) and SKIP-2-10-9 (for 鬍) with their index entries. Removed the rare 𠇑 (a Zhuang character, no Chinese definition), so 父 now has no aliases.

- **Alias loop, batch 140 (敗, 显, 東, 楽, 歌, 死, 母, 氷, 沌, 焼):** `## Aliases` sections and redirects for 败, 顯, 东, 樂, 乐, 欨, 謌, 屍, 姆, 毋, 拇, 冰, 坉, 飩, 烧 and 燒 (顯, 樂, 欨, 謌, 屍, 姆, 毋, 拇, 冰, 飩 and 燒 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). `mc_id` of 显 lowered to 639 (顯). Removed the rare 㬎 and 仌 (no usable definitions), so 氷 keeps only 冰.

- **Alias loop, batch 139 (喿, 塵, 増, 婁, 子, 孚, 彗, 思, 恵, 戯):** `## Aliases` sections and redirects for 噪, 尘, 增, 娄, 褸, 縷, 蔞, 褛, 缕, 仔, 崽, 孵, 篲, 恖, 惠, 戲, 戱 and 戏 (噪, 娄, 褸, 縷, 蔞, 仔, 崽, 孵, 篲, 恖, 惠 and 戲 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). Removed the rare 㜽, 𡿹, 𡐫 and 𣕓 (no definitions) from 子.

- **Alias loop, batch 138 (𡿺, 𢭏, 𢭐, 𥈞, 𦚖, 𦜝, 𧦅, 側, 利, 務):** `## Aliases` sections and redirects for 㐫, 瑙, 碯, 擣, 捣, 撈, 捞, 瞞, 瞒, 眨, 臍, 脐, 謳, 赞, 讴, 侧, 鯏 and 务 (瑙, 碯, 擣, 撈, 瞞, 眨, 臍, 謳 and 鯏 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). Removed the description sequence ⿱𭕄凶 from 𡿺 (not a character).

- **Alias loop, batch 137 (麟, 麺, 黎, 黒, 鼈, 鼠, 齦, 龐, 龔, 𡈼):** `## Aliases` sections and redirects for 麐, 麵, 麪, 黑, 龞, 鱉, 鳖, 鼡, 龈, 庞, 龎, 龚, 莛 and 葶 (麵, 麪, 龞, 鱉, 鼡, 莛 and 葶 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). New redirect-only leaf SKIP-2-12-16 (for 龞) with its index entry. `mc_id` of 鼈 set to 2039 (鱉). Removed the rare 㴝, 𥣥, 𱌇, 䑕 and 厐 (no definitions), so 黎 now has no aliases.

- **Alias loop, batch 136 (鵖, 鵝, 鵠, 鵡, 鵰, 鶴, 鸚, 鹵, 鹸, 麗):** `## Aliases` sections and redirects for 鹅, 鵞, 鹄, 鹉, 雕, 鹤, 隺, 鸖, 鹦, 卤, 鹼, 碱 and 丽 (鵞, 雕, 隺, 鸖, 鹼 and 碱 from EDRDG; computed SKIP codes for the rest logged in project_alias_skip_guesses). New redirect-only leaf SKIP-1-16-11 (for 鸖) with its index entries. Removed the rare 𱉝, 𫛲 and 𫠗 (no definitions), so 鵖 now has no aliases.

