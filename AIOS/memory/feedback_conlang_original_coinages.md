---
name: feedback-conlang-original-coinages
description: "Unattested in real-world CJKV" is not automatically grounds to skip a candidate word — it may be an intentional Dan'a'yo-original coinage; flag and ask rather than silently unlinking
metadata:
  type: feedback
---

When a candidate term fails every real-world CJKV attestation check, don't assume it's an error or filler and unlink it without comment. The vault has a real, established category of intentionally Dan'a'yo-original vocabulary — proper-noun transliterations for places with no existing Sino-Xenic name (using Dan'a'yo's own phonology rather than borrowing a real CJKV transliteration), and metalinguistic/grammatical coinages like [[文言継承]] or [[四字成語]]. These are marked with `origin: 単亜語` in frontmatter and are completely legitimate vault content — they just don't pass a real-world-attestation test, because they aren't supposed to.

**Why:** [[欽婁]] was skipped during the [[project_geography_history_words_2026-06]] sweep as unattested (the real Sino name for Wales is 威爾士, transliterating English "Wales," and 欽婁 matches neither that nor any other real CJKV form). The user corrected this: 欽婁 was deliberately coined to transliterate the Welsh endonym "Cymru" using Dan'a'yo's own romanization (欽 = *kum* ≈ "Cym-", 婁 = *lu* ≈ "-ru"), precisely because Dan'a'yo's phonology doesn't map cleanly onto any existing CJKV transliteration of that name. This is a different failure mode from [[feedback_idiom_component_attestation]] (under-researching real attestation) — here the term was correctly identified as unattested, but "unattested → skip" was the wrong inference.

**How to apply:** When a candidate fails attestation, especially a proper noun (place/person name) or a metalinguistic term with no obvious real-world equivalent, surface this explicitly to the user as a flagged judgment call ("this doesn't appear in Mandarin/Cantonese/Japanese/Korean/Vietnamese — is this meant to be a Dan'a'yo-original coinage, or should I unlink it?") rather than silently converting it to plain text. If the user confirms it's an intentional coinage, build the cross-linguistic reading fields (mandarin/cantonese/japanese/korean/vietnamese) as the *mechanical* reading of the chosen characters in each system — not as a claim that the term is used in those languages — and say so explicitly in the Notes, plus set `origin: 単亜語`.
