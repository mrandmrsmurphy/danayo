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

### Remaining (34 words)
- 5 more 位-compounds: 水位, 単位, 地位, 部位, 方位 (all already listed with English glosses in 位.md's Words section, same pattern as batch 1)
- 29 others: 掌管, 仙人掌, 分掌, 提供, 提出, 提督, 提琴, 提携, 改革, 処女(alias 处女/處女), 嬴洲, 事宜, 徳沢(alias 德澤/徳澤), 充足, 充電, 充当, 別字, 個別, 勉励, 勉強, 受賞, 受難, 受理, 受胎, 受託, 要塞, 妓女, 舞妓
