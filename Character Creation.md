# Skill: Character Creation

Character files are rare additions to the database. Each one requires data from multiple external sources, cross-referenced against the vault's phonological system. The filename is probably `X.md`, stored in `/characters/`.

---

## External sources

| Source | What to get |
|---|---|
| **Wiktionary** (`en.wiktionary.org/wiki/X`) | Mandarin Pinyin, Cantonese Jyutping, Japanese on/kun-yomi, Korean Hangul, Vietnamese (if present), Middle Chinese initial + final + tone, Old Chinese reconstruction, stroke count, radical, composition type, phonetic component, compounds |
| **Naver Hanja** (`hanja.dict.naver.com/#/search?query=X`) | `korean_native` — native Korean descriptive gloss |
| **EDRDG WWWJDIC** (`edrdg.org/cgi-bin/wwwjdic/wwwjdic?1MMJ[UTF-8 char]`) | SKIP number (authoritative) |
| **Vault phonology** | Dan'a'yo 注音, 羅馬字, 諺文 — derived from MC initial + final (see below) |

---

## Frontmatter fields

### Always required

```yaml
mandarin: yì                    # Pinyin with tone marks — unquoted
cantonese: jeoi6                # Jyutping with tone number — unquoted
korean: 예                      # Sino-Korean Hangul — unquoted
korean_native: 후손             # Native Korean gloss from Naver
japanese:                       # On-yomi in rōmaji, as a list
  - EI
japanese_native:                # Kun-yomi in hiragana, as a list
  - すそ
  - すえ
middle_chinese_initial: j       # IPA symbol from Wiktionary
middle_chinese_final: iᴇi       # IPA symbol from Wiktionary — always use the listed form
stroke_count: 13
radical: 衣                     # Kangxi radical character only
skip_number: 2-2-11             # From EDRDG — do not calculate manually
grade_level: 先進               # See grade decision below
pos: 名詞                       # Part of speech
english:                        # Gloss(es) as a list
  - descendant
羅馬字: "'ye"                   # Dan'a'yo romanisation — from vault phonology
諺文: 여                        # Hangul of Dan'a'yo pronunciation — from vault phonology
joyo_level: 表外字              # See level values below
hsk_level: "5"                  # Quoted string
hanmun_edu_level: 名            # See level values below
danayo_id: 7542                 # See ID allocation below
mc_id: 2350                     # Classical Chinese frequency rank (from Wiktionary)
graphemic_classification: 㕯    # Phonetic component name (形声), or 象形/指事/会意
stand_in: 後裔                  # See stand_in decision below
注音: ⼶                        # Dan'a'yo Bopomofo — from vault phonology
date-last-perfect:              # Leave blank until all criteria met
kwin: false                     # Linter will set to true if applicable
tags:
  - character
```

### Include only when non-empty

```yaml
vietnamese:
  - duệ
aliases:
  - 裸            # simplified, traditional, or regional variants
```

**Vietnamese**: include when Wiktionary lists it. For obscure characters it may be absent; a phonologically-derived guess is acceptable. Omit the key entirely when absent.

---

## Dan'a'yo phonology (注音 / 羅馬字 / 諺文)

The Dan'a'yo reading is derived from the Middle Chinese initial + final combination. **Do not guess — look it up in the vault.**

1. Find the MC initial and final from Wiktionary.
2. Search `characters/` for another character with the **same MC initial + final**:
   ```
   grep -rl 'middle_chinese_initial:.*X' characters/ | while read f; do
     fin=$(grep '^middle_chinese_final:' "$f" | ...); ...
   done
   ```
3. Read its `注音`, `羅馬字`, and `諺文` — these apply to the new character too.
4. Always use the exact MC final as listed on Wiktionary (e.g. `iᴇi`, not a sub-variant). The CC final lookup file to use in the Notes bullet is determined by matching against the files in `lookup/CC/finals/`.

**諺文 construction**: the Hangul is built from the Dan'a'yo romanisation syllable-by-syllable. A null initial `'` gives the vowel alone (e.g. `'ye` → 여). A final consonant adds the appropriate 받침 (e.g. `'yeg` → 역).

---

## Grade level decision

| Situation | grade_level |
|---|---|
| In HSK 1–4 and/or Jōyō kyōiku | `"1"`–`"4"` |
| In HSK 5–6 and/or Jōyō and/or Korean MS/HS | `"5"` or `"6"` or `先進` |
| HSK 5–6 + Jōyō 高等 or better educational recognition | `先進` |
| Hyōgai + Korean name list + HSK 5 | `先進` |
| No HSK, Hyōgai or worse, Korean name only | `名` |
| Restricted to proper names only | `名` + `stand_in: 名専字` |

Note: 先進 is listed under `lookup/Grade Advanced.md`.

---

## `stand_in` decision

| Situation | stand_in value |
|---|---|
| Character is independently meaningful, appears in multiple compounds | Character itself (e.g. `stand_in: 裔`) |
| Character only makes sense in one specific compound | That compound (e.g. `stand_in: 後裔`) |
| Character appears only in proper names | `名専字` |
| Character is being created specifically as a name character | `名専字` |

It is fine for `stand_in` to reference a word file that does not yet exist. The word will be created eventually.

---

## `danayo_id` allocation

The `danayo_id` is **not** the same as `mc_id`. It is a Dan'a'yo-internal ID, assigned by incrementing from the highest current ID within the character's grade level.

To find the next available ID: ask the user, or check the current highest value for that grade across all character files.

---

## `joyo_level` values

| Value | Meaning |
|---|---|
| `"1"`–`"6"` | Jōyō kyōiku grade |
| `高等` | Jōyō kōtō (secondary school) |
| `表外字` | Hyōgai (outside Jōyō) |
| `日本人名用漢字` | Jinmeiyō (name use) |

---

## `hanmun_edu_level` values

| Value | Meaning |
|---|---|
| `中` | Korean middle school list |
| `高等` | Korean high school list |
| `名` | Korean name character list |
| `無` | Not in any Korean list |

---

## Body structure

```markdown
​```meta-bind-embed
[[nav/char_info]]
​```

## Notes
- [graphemic bullet]
- [SKIP / Stroke bullet]
- [Middle Chinese rank bullet]
- [Levels bullet]

## Words
- <ruby>[[WordFile]]<rt>注音</rt></ruby> "gloss"
```

### Bullet 1 — Graphemic

**形声:**
```markdown
- 形声 (OC \*lats): semantic [衣](Radical%20145) ("clothing") + phonetic [[㕯]] – brief semantic note.
```
- OC reconstruction from Wiktionary (Baxter–Sagart preferred), escaped with `\*`
- Semantic radical linked as `[CHAR](Radical%20NNN)` — number from Kangxi radical number
- Phonetic component linked as `[[CHAR]]` — if no character page exists yet, the link will be unresolved until created

**会意:**
```markdown
- 会意 of [[亻]] ("person upright") + [[𠤎]] ("person inverted") – semantic note.
```

**象形 / 指事:**
```markdown
- [List of 象形](lookup/List%20of%20象形.md): describes what is depicted.
- [List of 指事](lookup/List%20of%20指事.md): describes what the indicator marks.
```

### Bullet 2 — SKIP / Stroke 

```markdown
- [SKIP-2-2-11](../lookup/SKIP/SKIP-2/SKIP-2-2-11.md) ([Stroke 13](../lookup/Stroke/Stroke%2013.md)) 
```

### Bullet 3 — Middle Chinese rank

```markdown
- 2350th most used character in Classical Chinese. Ancient [[Lookup/CC/initials/聲 以|j]] + [[Lookup/CC/finals/韻 祭A三開|iᴇi]] → [⼶](../syllables/⼶.md)
```
- CC initial file: `lookup/CC/initials/聲 INITIAL_NAME.md` — display text is the IPA symbol
- CC final file: `lookup/CC/finals/韻 FINAL_NAME.md` — display text is the IPA symbol
- Always use the MC final exactly as listed on Wiktionary to select the correct final file

### Bullet 4 — Levels

```markdown
- [Hyōgai](../lookup/Japanese/Hyōgai.md), [Old HSK 5](../lookup/HSK/Old%20HSK%205.md), [Korean Name ㅇ](../lookup/Korean/Korean%20Name%20ㅇ.md)
```
- **Korean Name** is indexed by initial consonant of the Korean reading (e.g. 예 → ㅇ → `Korean Name ㅇ`)
- **Grade link** included for grades 1–6 and 名; Advanced for 先進.
- Order: Jōyō, HSK, Korean, Grade

### Words section

List every Dan'a'yo word using this character with its full 注音 in the `<rt>` tag:
```markdown
- <ruby>[[後裔]]<rt>ㄏㄨㄛ⼶</rt></ruby> "descendant"
```
It is fine to list a word whose file does not yet exist.

---

## `date-last-perfect` criteria

Leave blank if **any** of the following are incomplete:
- Any required frontmatter field is missing or unverified
- Graphemic bullet is missing or links unresolved components
- Levels bullet is missing any link (except the 先進 grade link, which has no target file)
- Words section is missing a word that uses this character

Set to today's date when all verifiable criteria are met.
