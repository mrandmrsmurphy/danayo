---
name: in-words-batch
description: In progress (started 2026-06-12) — creating words from 'broken links output.md's "In Words" section
type: project
---

# Batch word creation from broken links output.md "## In Words" section

**Why:** The "## In Words" section of `broken links output.md` lists words referenced from existing `words/` files' Notes sections that don't yet have their own file. Goal (set via `/goal`): create each word that does NOT require creating a new character first. See [[skill_word_creation]].

**How to apply:** Resume at the next pending word. Verify against `words/` directory before assuming a word is done.

## Blocked (require new character — excluded from this batch per the goal)
- 驟雨 (in words/俄雨) — needs character 驟
- 葭月 (in words/冬月) — needs character 葭
- 混淪 (in words/混沌) — needs character 淪

## Quick fixes (no new word file needed)
- 平穩 (in words/不穏) — DONE: 平穏.md already has alias 平穩; fixed dangling link in 不穏.md Notes to point to [[平穏]] instead.

## Words to create (38 total, 1 done via quick fix above = 37 remaining)

### Done
- [x] 指事 (六書 set)
- [x] 形声 (六書 set)
- [x] 会意 (六書 set)
- [x] 転注 (六書 set)
- [x] 漢方, 医学 (from words/七情)
- [x] 参拾 (from words/三十)
- [x] 十干 (from words/乙)
- [x] 中秋節 (from words/仲秋)
- [x] 宗徒, 行傳→行伝 (alias 行傳/行传) (from words/使徒)
- [x] 小雨 (from words/俄雨)
- [x] 加多 (from words/加多金)
- [x] 百年, 万年 (from words/千年)
- [x] 印尼 (from words/印度尼西亜)
- [x] 肆拾 (from words/四十)
- [x] 大略 (from words/大概)
- [x] 天地之別 (from words/天地)

### Pending
- [ ] 秋田 (from words/山本)
- [ ] 芻狗 (from words/干芻)
- [ ] 剣道 (from words/弓道)
- [ ] 春秋時代, 麟経, 麟史 (from words/春秋)
- [ ] 折線 (from words/曲線)
- [ ] 尚書 (from words/書経)
- [ ] 茶道 (from words/書道)
- [ ] 開天闢地→開天辟地 (alias 開天闢地) (from words/混沌)
- [ ] 無色 (from words/無形)
- [ ] 牛郎, 織女 (from words/牛郎星)
- [ ] 天神地祇 (from words/神霊)
- [ ] 冰月→氷月 (alias 冰月) (from words/臘月)
- [ ] 露月 (from words/良月)
- [ ] 甘蕉 (from words/芭蕉)
- [ ] 英格蘭 (from words/英国)

## Notes
- Character existence pre-checked for all 38; only 驟, 葭, 淪 are genuinely missing (no alias either). 穩→穏, 傳→伝, 闢→辟, 冰→氷 all resolve via existing aliases.
- 平穏.md already existed and already lists 平穩 as alias — was a false-positive broken link from a Chinese-language paragraph in 不穏.md using traditional 穩.
