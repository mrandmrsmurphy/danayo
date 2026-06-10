---
name: skill-word-creation
description: Step-by-step process for creating Dan'a'yo word files in /words/, including field sources, linter expectations, and known gotchas
type: skill
---

# Skill: Word Creation

See [[AIOS/skills/Word Creation.md|Word Creation.md]] for the full guide. This memory captures the operational details learned by doing it.

## Pre-flight checklist (run before marking done)

- [ ] `english` is a **YAML list** (`- item` form), never a bare string
- [ ] Check each constituent character's `aliases:` field — if any character has a traditional/alternate form alias, the compound likely has one too; add it to `aliases:` on the word
- [ ] If any constituent character lacks `vietnamese:`, check Wiktionary on the **traditional-form compound** (e.g. 骨髓 not 骨髄) for the Vietnamese reading before omitting it
- [ ] `kwin` is set: compare `諺文` and `korean` values exactly — `false` if they differ, `true` if identical
- [ ] If this word is the `stand_in` for any constituent character, the Notes section says so explicitly (link to character + explain it's too bounded to stand alone)
- [ ] Notes section uses `../characters/` relative paths with `%20` for spaces before `(char)`
- [ ] No blank optional fields (`vietnamese:`, `hsk_level:`, `aliases:`) — omit key entirely when empty

---

## Process overview

1. **Check character files** — for each constituent character, determine the filename form (`X.md` vs `X (char).md`) and read `羅馬字`, `諺文`, `注音`, and `english`. Also run `ls words/ | grep -i <chars>` to rule out an existing/duplicate file (including alternate character-form names).
2. **Fetch Wiktionary** — use the traditional form URL if a simplified/traditional split exists (e.g. 三位一體 not 三位一体). Extract: Mandarin Pinyin, Cantonese Jyutping, Japanese hiragana, Korean Hangul, Vietnamese (if present), HSK level (if mentioned).
3. **Assemble frontmatter** — concatenate Dan'a'yo fields from character files; use CJKV readings from Wiktionary. WebSearch to verify/derive missing readings (especially Korean/Japanese/Vietnamese when Wiktionary lacks them) — derive compositionally from constituent character readings, then verify attestation.
4. **Write the file** to `/words/WORD.md`, with a multi-paragraph encyclopedic Notes section (see [[feedback_notes_style]]).
5. **Back-link each character** — for every constituent character file, add a ruby-annotated entry to its `## Words` section (create the section if absent):
   ```markdown
   ## Words
   - <ruby>[[WORD]]<rt>注音</rt></ruby> "english gloss"
   ```
   The `<rt>` content is the full Dan'a'yo Bopomofo (注音) of the new word.
6. **Update the syllable page(s)** — add ruby annotation to the relevant entries; if the word is a stand-in that unblocks the page (all entries now resolve), set `date-last-perfect` to today (see [[feedback_syllable_completion]]).

---

## Frontmatter field sources

| Field | Source |
|---|---|
| `characters` | Manual: list each character using `X (char)` when file is `X (char).md`, plain `X` when `X.md` |
| `羅馬字` | Concatenation of each character's `羅馬字` value — quote with apostrophe when the result starts with one, e.g. `"'yogcong"`, `"cen'yei"` |
| `諺文` | Concatenation of each character's `諺文` value |
| `注音` | Concatenation of each character's `注音` value — **use `·` separator at syllable junctions that would otherwise be ambiguous** (see gotchas) |
| `mandarin` | Wiktionary Pinyin — unquoted |
| `cantonese` | Wiktionary Jyutping — unquoted |
| `japanese` | Wiktionary hiragana — note special readings where they differ from concatenation |
| `korean` | Wiktionary Hangul — unquoted |
| `vietnamese` | Wiktionary — include when present; omit key entirely when absent |
| `pos` / `品詞` | Infer from meaning: 名詞, 動詞, 性詞, 数詞, 副詞, 擬詞, etc. |
| `english` | Brief gloss(es) — **YAML list** — from Wiktionary or from character glosses |
| `hsk_level` | Wiktionary if mentioned; omit key entirely when absent |
| `aliases` | Include traditional/simplified variants (e.g. 三位一體 → 三位一体) |
| `date-last-perfect` | Today's date if all fields are complete |
| `kwin` | Simple string comparison: if `諺文 == korean` exactly, set `true`; otherwise `false`. E.g. 原罪: 諺文=원죄, korean=원죄 → true. 枢机: 諺文=추긔, korean=추기 → false. No phonological analysis — just compare the two field values. |
| `tags` | Always `- word` |

---

## Linter behaviour (observed)

- **`mandarin`, `cantonese`, `korean`**: linter removes surrounding quotes — write unquoted
- **`kwin`**: set to `false`; linter updates to `true` when applicable
- **`date-last-perfect`**: linter accepts today's date when file is complete
- **`注音` separator**: linter inserts `·` at ambiguous syllable boundaries (observed: `⼔ㄧ·ㄧㄊ` in 三位一体)

---

## Body structure

```markdown
---
[frontmatter]
---
​```meta-bind-embed
[[nav/word_info]]
​```

## Notes
- [X (char)](../characters/X%20(char).md) "gloss" + [Y](../characters/Y.md) "gloss" + ...
- [multi-paragraph encyclopedic prose — see feedback_notes_style]
```

- Always use `../characters/` relative paths in Notes links
- URL-encode spaces as `%20` before `(char)`
- Use `+` to separate components
- For words with special Japanese readings, add a plain-text note in the Notes section explaining the reading

---

## Aliases

- Use when the word has a traditional/simplified variant that differs from the filename
- The **filename** uses the Dan'a'yo form (typically the simplified/Japanese shinjitai form)
- The **alias** is the traditional or alternate form
- Wiktionary's traditional-form URL often has fuller CJKV data — prefer it when looking up

---

## Stand-in (legitimizer) words

Some words exist specifically to give a bounded character a usable word form. When a character's `stand_in` field points to the word you are creating, the word is functioning as a **legitimizer** — it carries the same meaning as the bare character, but makes it viable in Dan'a'yo discourse.

**How to detect this:** Before writing, check whether the word matches the `stand_in` value on any of its constituent character files.

**What to add in Notes:** After the character-breakdown line, add a clause making the relationship explicit: `— stand-in for [[X]], which cannot appear independently` (or "for both [[X]] and [[Y]], neither of which..." when both characters are bound). See [[feedback_standin_note]].

---

## Gotchas

### 羅馬字 apostrophes
Characters whose 羅馬字 begins with `'` (glottal/null initial, e.g. 五 = `'o`, 位 = `'wei`, 一 = `'id`) must be handled in YAML. Quote the combined value if the leading apostrophe would be misread: `羅馬字: "'osib"`.

### 注音 ambiguous junctions
When concatenating 注音 values, a `·` separator may be needed where two syllables would otherwise merge unreadably (e.g. `⼔ㄧ` + `ㄧㄊ` → `⼔ㄧ·ㄧㄊ`). The linter inserts this automatically; check the result after creation.

### Japanese special readings
Many date/number/calendar words have fused Japanese readings that are NOT the concatenation of component 注音 (e.g. 八日 → ようか not はちにち, 十日 → とおか). Always fetch Wiktionary and use the actual reading; note it explicitly in ## Notes.

### Wiktionary URL for traditional-form words
Use the traditional character URL for lookup even when the Dan'a'yo filename uses the simplified form. E.g. for 三位一体, fetch `三位一體` on Wiktionary for complete CJKV data.

### Vietnamese
Include `vietnamese:` only when Wiktionary provides it, or when WebSearch can confirm an attested Sino-Vietnamese reading (e.g. searching `<compound> Hán Việt "<candidate reading>" nghĩa`). Omit the key entirely (not blank) when absent, per BP Words common mistakes.

### Filename/duplicate-checking discipline
ALWAYS run `ls words/ | grep -i <chars>` AND `ls characters/ | grep -i <chars>` before creating — check for existing word files (including alternate character forms / traditional-simplified variants) and confirm the constituent characters' filenames. A "broken link" can be caused either by a missing file OR by a mismatched/duplicated stub pointing at the wrong character form (see [[project_broken_links_batch]] for a worked example: 六腑 vs 六府).
