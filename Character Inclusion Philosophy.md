# Character Inclusion Philosophy

This document records the observed rubric for character inclusion in Dan'a'yo, synthesised from the existing character database (~3,314 characters as of May 2026).

---

## Scale and Architecture

| Grade | Count | % |
|---|---|---|
| Grades 1–6 (core) | ~2,000 | 60% |
| 先進 (advanced) | 532 | 16% |
| 名 (naming) | 794 | 24% |

**The central fact:** ~2,820 characters (~85%) are bound to a specific compound via `stand_in`. Standalone characters (`stand_in` = the character itself) are vanishingly rare. This is the architecture: **Dan'a'yo vocabulary is built from compounds, not from standalone morphemes.** The character inventory exists to make compounds possible, not to be words in itself.

---

## Grade-level Rubric

### Grades 1–6
- Contributes to core vocabulary across at least 3–4 of the 5 CJKV languages
- Appears in HSK and/or Jōyō and/or Hanmun education lists
- Its compound(s) cover a concept Dan'a'yo needs at that register

### 先進
- The concept is real and cross-culturally significant, but not everyday
- Recognised in at least Jōyō 高 or HSK 5–6 or Korean HS — known to educated readers in at least one language
- Its compound would not be replaced by a simpler paraphrase

### 名
- Appears in important proper names (countries, classical deities, famous people, major place names) across the CJKV sphere
- Has no productive standalone use in Dan'a'yo vocabulary
- Omitting it would make those names unwritable in Dan'a'yo script

### 名専字
- Functions exclusively in proper nouns, with no semantic load of its own
- Even educated native readers only recognise it in one specific name

---

## 借代字 — What They Are

A **借代字** is a character included in Dan'a'yo not as an independent word but as a bound member of a specific compound. Its `stand_in` field names that compound. Neither constituent character is productive outside it.

Examples from the database: 鳳凰, 麒麟, 鸚鵡, 鴛鴦, 黼黻, 飢餓, 錯誤, 跳躍, 鵖鴔, 雴霫.

The count of 2 on both members of a pair (e.g. both 鳳 and 凰 point to 鳳凰) is the signature: *both characters are mutually bound to the same word.*

---

## 借代字 Inclusion Rubric

### Include a character as a 借代字 if ALL of the following hold:

1. **The compound it anchors is a needed Dan'a'yo word** — the concept has a clear place in the language at the appropriate register
2. **The compound uses the same characters across at least 3 of the 5 CJKV languages** — it is a genuinely pan-East-Asian form, not a local coinage
3. **No already-included character(s) can substitute for it** — there is no simpler existing compound that covers the concept
4. **The concept cannot be expressed productively from existing characters** — a paraphrase with included characters is not available or would be unnatural

### Reject if:

- The compound is specific to only one CJKV tradition (Japanese-only coinage, etc.)
- The concept is already expressible in Dan'a'yo by other means
- The character's only occurrence is in a personal name → use 名専字 instead

---

## The Long Tail

Statistical pressure on the long tail comes from three distinct sources, which may warrant different inclusion thresholds:

| Source | Example | Suggested threshold |
|---|---|---|
| **Cultural necessity** | 鳳凰, 麒麟 | Include if pan-CJKV and culturally central |
| **Scientific/technical** | Chemical elements, anatomical terms | Include if standard across ≥3 CJKV educational systems |
| **Proper name anchoring** | Place names, deity names, surnames | Prefer 名専字; only elevate to 名 if the name is of major cross-cultural importance |

---

## Proposed Future Field

Consider adding a `borrowing_reason` field (or a tag) to distinguish *why* a 借代字 was included:

- `cultural` — mythological, literary, or ceremonial significance
- `scientific` — technical terminology stable across CJKV
- `toponym` — major place name
- `zoonym` / `phytonym` — fauna/flora whose name requires these specific characters

This would make future inclusion decisions auditable and allow tightening or loosening thresholds by category.
