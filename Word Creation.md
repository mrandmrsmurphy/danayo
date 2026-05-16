# Skill: Word Creation

## Process overview

1. **Check character files** — for each constituent character, determine the filename form (`X.md` vs `X (char).md`) and read `羅馬字`, `諺文`, `注音`, and `english`.
2. **Fetch Wiktionary** — use the traditional form URL if a simplified/traditional split exists (e.g. 三位一體 not 三位一体). Extract: Mandarin Pinyin, Cantonese Jyutping, Japanese hiragana, Korean Hangul, Vietnamese (if present), HSK level (if mentioned).
3. **Assemble frontmatter** — concatenate Dan'a'yo fields from character files; use CJKV readings from Wiktionary.
4. **Write the file** to `/words/WORD.md`.
5. **Back-link each character** — for every constituent character file, add a ruby-annotated entry to its `## Words` section (create the section if absent):
   ```markdown
   ## Words
   - <ruby>[[WORD]]<rt>注音</rt></ruby> "english gloss"
   ```
   The `<rt>` content is the full Dan'a'yo Bopomofo (注音) of the new word.

---

## Frontmatter field sources

| Field | Source |
|---|---|
| `characters` | Manual: list each character using `X (char)` when file is `X (char).md`, plain `X` when `X.md` |
| `羅馬字` | Concatenation of each character's `羅馬字` value |
| `諺文` | Concatenation of each character's `諺文` value |
| `注音` | Concatenation of each character's `注音` value — **use `·` separator at syllable junctions that would otherwise be ambiguous** (see gotchas) |
| `mandarin` | Wiktionary Pinyin — unquoted |
| `cantonese` | Wiktionary Jyutping — unquoted |
| `japanese` | Wiktionary hiragana — note special readings where they differ from concatenation |
| `korean` | Wiktionary Hangul — unquoted |
| `vietnamese` | Wiktionary — include when present; omit key entirely when absent |
| `pos` | Infer from meaning: 名詞, 動詞, 性詞, 数詞, 副詞, etc. |
| `english` | Brief gloss — from Wiktionary or from character glosses |
| `hsk_level` | Wiktionary if mentioned; omit key entirely when absent |
| `aliases` | Include traditional/simplified variants (e.g. 三位一體 → 三位一体) |
| `date-last-perfect` | Today's date if all fields are complete |
| `kwin` | Include as `false` — linter will correct to `true` if applicable |
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
Include `vietnamese:` only when Wiktionary provides it. Omit the key entirely (not blank) when absent, per BP Words common mistakes.
