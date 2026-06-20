---
name: feedback-idiom-component-attestation
description: Before declaring a 2-character candidate "unattested," check whether it's the head/component of a longer attested 4-character idiom — standalone-word dictionaries (plain Wiktionary lookup) will miss this
metadata:
  type: feedback
---

A 2-character term with no standalone Wiktionary entry can still be a real, creatable word if it's a component of a longer attested classical idiom (chengyu). Don't conclude "unattested" from a standalone-word lookup alone — also check whether the candidate's literal characters form the head of any 4-character idiom (search `"XY" 成語` / `"XY眾民"`-style queries, or check Wiktionary's idiom entries directly), and check Japanese dictionaries (e.g. Kotobank) independently, since Japanese sometimes attests a term that Chinese standalone dictionaries don't surface.

**Why:** [[広土]] was skipped during the [[project_geography_history_words_2026-06]] sweep as "unattested" based on a standalone-word check alone. The user corrected this: 廣土 is the first half of 廣土眾民, a real Mencius-derived idiom, *and* 広土 (こうど) turned out to be independently attested in Japanese (Kotobank) too — a fact a standalone Mandarin/Cantonese-only check missed. The same pattern was already correctly applied earlier in that same sweep for [[諸子百家]] (split into 諸子 + 百家, both real even though the 4-character compound is itself also attested) — so the precedent existed, but wasn't generalized into a standing check.

**How to apply:** When a 2-character (or short) candidate word fails a standalone dictionary check, before skipping it: (1) search for it as the head of a longer idiom, (2) check Japanese dictionaries (Kotobank, Weblio) independently rather than assuming Japanese pedigree from a Chinese-language source alone, (3) if the user pushes back with idiom evidence, treat that as authoritative and re-verify rather than re-asserting the original "unattested" call.
