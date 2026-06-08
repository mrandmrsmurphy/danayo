---
name: broken-links-batch
description: Active project — working through ~70 missing words listed in 'broken links output.md', currently at #51/69
type: project
---

# Batch word creation from broken links output.md

**Why:** The vault-root file `broken links output.md` lists words referenced by syllable pages but missing from `/words/`. Goal: create each word, back-link its constituent characters, add ruby annotations to syllable pages, then set `date-last-perfect` once a syllable's entries all resolve. See [[skill_word_creation]] and [[skill_character_creation]].

**How to apply:** Resume at the next pending word. Don't trust a prior "complete" claim without spot-checking — verify by checking whether the word file actually exists in `words/` (a 2026-06-07 correction found a prior "complete" claim was false: only ~10 of ~94 lines had actually been done).

## Current status (as of 2026-06-08)

**Done: words #1-50** of the original 69-word list (詔書 through 殉難), each with full frontmatter + encyclopedic Notes, character back-links, and syllable ruby annotations.

**Also resolved out of order: #28 潮汐** (was skipped initially — required creating a new character, 汐, first; see "Characters created mid-batch" below).

**STOPPING POINT:** paused after word #50 (殉難) at the user's request ("stop when you reach the end of a set" / "stop after 31-40") — a clean break since #48-50 (巡回, 迅速, 殉難) all share the ㄙ⼜ㄋ syllable and were perfected together.

**Remaining: #51-69** (19 words) — 新鮮, 寺刹, 刪除, 梗塞, 懐愁, 吉祥, 鳳笙, 追溯, 蘇生, 刀鞘, 蕃藷, 損失, 蜀国, 宋朝, 漏洩, 楔子, 解釈, 潟湖, 碩大. All confirmed createable (constituent characters already exist) — spot-checked.

## Characters created mid-batch

- **汐** (2026-06-08): the one word in the batch (#28, 潮汐) that was genuinely blocked on a missing character. Created `characters/汐.md` (形声, 水 + phonetic 夕; 注音 ㄙㄝㄎ derived by exact match to 夕's MC z+iᴇk reading; grade 名, stand_in 潮汐, danayo_id 8807), then `words/潮汐.md` (羅馬字 causeg, 諺文 찻석, korean 조석, japanese ちょうせき, vietnamese triều tịch). Fully perfected both ㄑㄚㄨ and ㄙㄝㄎ syllables.

## Notable judgment calls and gotchas hit during this batch

- **#13 in the list was written 乾淨, but the canonical vault file is 乾浄** (shinjitai 浄, with 淨/净 as aliases) — edited the existing stub in place rather than duplicating. Always grep `words/` for alternate character forms before writing a new word file.
- **六腑 vs 六府** (found and fixed 2026-06-08, outside this batch but same failure class): a duplicate stub `words/六腑.md` existed alongside the canonical `words/六府.md` (which already lists 六腑 as a word-level alias, since 腑 is correctly aliased to 府 — same MC reading). The stub was malformed and pointed at a nonexistent `腑 (char).md`, generating a phantom broken link. **Lesson: a "broken link" can be caused by a missing file OR by a duplicate/mismatched stub — always check both** before assuming a character needs creating.
- **淘汰 vs 陶汰** (found and fixed 2026-06-08, outside this batch but same failure class): a malformed duplicate `words/淘汰.md` existed, built on the *aliased* character form 淘 — pointing at a nonexistent `characters/淘.md` (淘 is correctly aliased onto 陶, same MC reading, in `characters/陶.md`'s `aliases:` list). The canonical word file `words/陶汰.md` already existed (with `aliases: [洮汰, 淘汰]`). Deleted the stub and repointed every reference that had drifted onto the alias name — `characters/汰.md`'s `stand_in` field and `## Words` ruby link, plus `syllables/ㄊㄚㄧ.md` entry 7 — to the canonical `[[陶汰]]`. **Lesson: when a word's first character is an alias, the canonical word file (and every `stand_in`/ruby reference to it) must use the alias's *parent* character form, not the alias form** — building on the alias form produces the same "missing character file" symptom as a genuinely missing character.
- **禿鷲 → 禿就** (found and fixed 2026-06-08, outside this batch but same failure class — this time the *second* character was the alias, and no canonical file existed yet): `words/禿鷲.md` was built on 鷲, which is aliased onto [[就]] (`characters/就 (char).md` lists 鷲/鹫 as aliases, same MC reading). Unlike the 陶汰 case, there was no pre-existing canonical file — but [[就鳥]] (built on 就, with 鷲鳥/鹫鸟 as word-level aliases) established the precedent: **Dan'a'yo word construction always uses the alias's parent character; the real-world spelling becomes a word-level `aliases:` entry, not the filename.** Renamed `words/禿鷲.md` → `words/禿就.md` (frontmatter unchanged — its 注音/羅馬字/諺文 were already correctly derived from 就's reading ㄐㄨㄛ, only the `characters:`/Etymology link was wrong), added `aliases: [禿鷲, 秃鹫]`, and updated back-links in `characters/禿 (char).md` and `characters/就 (char).md`'s 借代字 note.
- **顕著** (ㄏㄝㄋ): confirmed 著 is correctly an alias of 着 (one glyph, one Dan'a'yo sound — Mandarin's zhe/zhuó/zhù split doesn't carry over to Dan'a'yo).
- **恍惚** (ㄏㄛㄊ): required creating 恍 first. Wiktionary lists both 怳 and 芒 as "alternative forms," but only 怳 was aliased — 芒 is a thriving independent modern character already discussed on its own terms elsewhere in the vault, and aliasing it would have repeated the 歇/欠 mistake (below).
- **穹窿** (ㄎㄨㄫ): a *good* aliasing case, contrasted with 歇/欠. 窿 was aliased to 隆 — same MC initial+final, same readings, AND a transparently-extended meaning (隆 "arch/bulge" → 窿 "an arched cavity" — narrowing, not branching). **Test for legitimate aliasing: same derivable Dan'a'yo sound AND a transparent/metaphorical meaning link — both must hold, not just one.**
- **間歇** (ㄏㄝㄊ): a deeper fix. A prior session had wrongly aliased 歇 → 欠 (rationalized via Japanese 同音の漢字による書きかえ substitution), but the two characters have **distinct Dan'a'yo sounds AND meanings** — aliasing them violated 一字一音/毎字明意. Reverted: removed the alias, restored 歇's stand_in, deleted the wrongly-built word file, and built 間歇 directly on 歇.
- **General lesson for alias judgment calls**: before treating two characters as aliases (one-glyph-one-sound), check whether they already have SEPARATE full character files with DIFFERENT 注音 values — if so, they are not graphic variants and must not be aliased, regardless of what other languages' substitution conventions (e.g. Japanese 代用字) suggest.
- **百越/粤**: found and corrected a false legitimizer claim — 百越 doesn't actually contain 粤; changed 粤's `stand_in` to 名専字 and updated the ⼔ㄊ syllable entry accordingly.

## Genuinely blocked entries elsewhere in the vault (require new character files first — separate from this batch's word list, but same failure class)

- [[嬌媚]] in ㄍ⼘ㄨ — needs 媚
- [[僵屍]] in ㄍ⼘ㄫ — needs 屍
- [[緣故]] in ㄍㄛ — needs 緣
- [[污垢]] in ㄍㄛㄨ — needs 污
- [[伎倆]] in ㄍㄝ — needs 倆
- [[貝殼]] in ㄎㄚㄎ — needs 殼
- [[粃糠]] in ㄎㄚㄫ — needs 粃
- [[欺瞞]] in ㄎㄧ — needs 瞞
- [[廞]] in ㄏㄜㄇ — needs 廞 character file itself
- [[裝飾]] in ㄙㄧㄎ — needs 裝
- [[倦厭]] in ㄍ⼔ㄋ — needs 厭

## Syllables perfected this batch (date-last-perfect → 2026-06-07/08)

ㄐㄝㄆ, ㄐㄝㄫ, ㄐㄧㄎ, ㄐㄨㄎ, ㄐㄨㄧ, ㄑㄚㄋ, ㄑㄚㄎ, ㄌㄚㄆ, ㄑㄛㄨ, ㄑㄛㄫ, ⼶ㄧ, ㄑㄝㄋ, ㄑㄝㄫ, ㄑㄧㄇ, ㄑㄧㄎ, ㄑㄨㄋ, ㄑㄨㄛ, ㄑㄨㄫ, ㄙ⺢, ㄙ⺢ㄫ, ㄙ⼔, ㄙ⼜ㄋ, ㄑㄚㄨ, ㄙㄝㄎ — plus ㄏㄝㄋ, ㄏㄛㄊ, ㄎㄨㄫ, ㄏㄝㄊ from the alias-correction side-quests above.

(For the larger ~115-syllable backlog perfected across earlier sessions before this batch began, see git history on the `syllables/` directory — that level of detail isn't worth duplicating here.)
