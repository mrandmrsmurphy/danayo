# Vault Memory

Running log of architectural decisions, corrections, and gotchas for future sessions. Read this at the start of every session.

---

## Character Creation

**2026-05-14** — Syllable link belongs only on the MC rank bullet (bullet 3), not on the SKIP/Stroke bullet (bullet 2). Bullet 2 ends after the Stroke link. The `→ [syllable](...)` arrow lives exclusively in bullet 3.

**2026-05-14** — `X (char).md` filename is only used when a `words/X.md` file also exists for the same character, requiring disambiguation. Characters with `stand_in: 名専字` (no word file) use plain `X.md`.

**2026-05-14** — Characters absent from the CC corpus (all four CC files, covering ranks 1–4000) put `mc_id: 0` and `date-last-perfect:` blank. Do not guess or approximate a rank.

## Character Inclusion Philosophy — Alias as Stand-In

**2026-05-14** — When a character is too narrow to justify full inclusion but still needs "no recourse" coverage for names, add it as an **alias on its phonetic parent** rather than creating a new character entry. The alias is valid when the two characters are phonetically identical across all CJKV languages. Examples: 蒔 (Jinmeiyō only) → alias on 時 (char).md (蒔 = 艹+時); 佈 (traditional form of 布, names only outside China) → alias on 布.md (佈 = 亻+布). The stronger the phonetic and semantic overlap, the cleaner the alias — 佈→布 is cleaner than 蒔→時 because 布 is both phonetic and semantic parent of 佈.

## Character Inclusion Philosophy

**2026-05-14** — The "no recourse" argument: if a character appears in personal names across the CJKV sphere and has no substitutable form in Dan'a'yo, it qualifies for 名 grade with `stand_in: 名専字`, even if it fails the vocabulary-grade criteria. Korean Name lookup presence is a direct signal.

**2026-05-14** — Semantic divergence across CJKV (e.g. 舅 = maternal uncle in Chinese/Vietnamese but father-in-law in Japanese) disqualifies a character from productive vocabulary grades but does not prevent 名 inclusion.

**2026-05-14** — Strong Chinese/Vietnamese presence with absent Japanese/Korean vocabulary (e.g. 址) is grounds for 名 rather than 先進, even if HSK level is low.
