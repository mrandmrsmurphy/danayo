---
name: feedback-standin-note
description: Word pages must note when the word is the stand-in legitimizer for a character that cannot appear alone
type: feedback
---

When a word is the `stand_in` for one of its constituent characters (i.e., the character file's `stand_in:` field equals this word), add a note on the word page flagging this.

Place it in the opening Notes bullet, after the character glosses.

**Why:** Characters with high boundedness cannot stand alone as vault entries; their stand-in word is what legitimises them in the syllable page and the database. Making this explicit on the word page helps readers understand why the word exists and what role it plays structurally.

**How to apply:** In the first Notes bullet (the etymology line), append a clause like:
> `— stand-in for [[粛]], which cannot appear independently`

Or, when **both** constituent characters are bound by this same word:
> `— stand-in for both [[X]] and [[Y]], neither of which can appear independently`

Example:
```
- [厳 (char)](../characters/厳%20(char).md) "strict" + [粛](../characters/粛.md) "solemn" — synonym compound for grave solemnity; stand-in for [[粛]], which cannot appear independently
```

Check each constituent character's `stand_in:` field when creating a word. If any character's `stand_in` equals the word being created, add the note.
