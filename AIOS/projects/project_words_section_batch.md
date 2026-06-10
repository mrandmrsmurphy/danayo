# Project: "## Words"-section batch word creation

## Source
`broken links output.md`'s `## Words` section: 44 words referenced inside character files' own `## Words` sections that don't yet exist as files in `/words/`. User instruction: do not create any new character files — only words whose constituent characters already exist (verified for all 44 via alias resolution).

## Alias-parent resolutions needed (per established alias-parent rule)
- 处女 → build as **処女** (処 canonical; aliases [处, 處]), word-level aliases: [处女, 處女]
- 德澤 → build as **徳沢** (徳 canonical w/ alias 德; 沢 canonical w/ aliases [澤, 泽]), word-level aliases: [德澤, 徳澤]
- 座位 → build as **坐位** (坐 canonical, alias 座), word-level alias: [座位] — DONE

## Progress

### Batch 1 — 位-compounds, first 10 (complete 2026-06-09)
即位, 帝位, 王位, 下位, 学位, 穴位, 坐位 (alias 座位), 在位, 爵位, 上位
- All 10 word files created with full frontmatter + encyclopedic Notes
- Back-links added to constituent character pages (即/帝/王/下/学/穴/坐/在/爵/上 — several of these gained their first `## Words` section)
- 位.md's `## Words` section: converted these 10 entries from plain `[[XX位]]` links to ruby-annotated `<ruby>[[XX位]]<rt>...</rt></ruby>` format
- Syllable page `⼔ㄧ.md` perfected: converted 4 long-pending "but requires X" entries (位→定位, 危→危険, 倭→倭人, 萎→萎縮) to "-->" format since all target words already existed; date-last-perfect updated to 2026-06-09

### Batch 2 — remaining 位-compounds + 掌/提 group (complete 2026-06-10)
水位, 単位, 地位, 部位, 方位, 掌管, 仙人掌, 分掌, 提供, 提出
- All 10 word files created with full frontmatter + encyclopedic Notes
- Back-links added to constituent character pages (水/単/地/部/方/掌/管/仙/人/分/提/供/出 — 単, 管, 仙, 出 gained their first `## Words` section)
- 位.md's `## Words` section: converted the remaining 5 位-entries to ruby format (now all 15 done)
- 仙人掌's Japanese reading is the native loanword さぼてん (saboten), not on'yomi-compositional — noted in its Notes as a rare exception
- No syllable pages required updates for this batch (checked all constituent syllables for "but requires" entries pointing at these 10 words — none found)

### Batch 3 — final 23 words (complete 2026-06-10)
提督, 提琴, 提携, 改革, 処女 (alias 处女/處女), 嬴洲, 事宜, 徳沢 (alias 德澤/徳澤), 充足, 充電, 充当, 別字, 個別, 勉励, 勉強, 受賞, 受難, 受理, 受胎, 受託, 要塞, 妓女, 舞妓
- All 23 word files created with full frontmatter + encyclopedic Notes
- Back-links added/converted to ruby format across 提/督/琴/携/改/革/処/女/洲/事/宜/徳/沢/充/足/電/当/別/字/個/勉/励/強/受/賞/難/理/胎/託/要/塞/妓/舞 — 琴, 個, 励, 強, 賞, 胎, 要, 舞 gained their first `## Words` section; 革, 電, 足 also gained one
- 嬴.md already had its 嬴洲 back-link pre-existing in ruby format; only 洲 (char).md needed the new link
- 徳 (char).md's pre-existing `[[德澤]]` link retargeted to `[[徳沢]]` (alias-parent rule)
- 娘 (char).md's plain `[[处女]]` reference converted to ruby `[[処女]]`
- 勉強's Notes documents the Mandarin/Cantonese/Vietnamese "reluctant, forced" sense vs. the Japanese "to study" sense — a notable cross-language semantic divergence
- 舞妓's Notes documents まいこ (maiko) as a non-compositional Japanese reading, following the 仙人掌/さぼてん precedent
- `broken links output.md`'s entire "## Words" section is now empty — this project is complete
