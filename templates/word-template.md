---
characters: <%* tR = await tp.system.prompt("Constituent characters (comma-separated, e.g. 羅, 馬)") %><%= tR %>
mandarin: <%* tR = await tp.system.prompt("Mandarin pronunciation (pinyin)") %><%= tR %>
cantonese: <%* tR = await tp.system.prompt("Cantonese pronunciation (jyutping)") %><%= tR %>
korean: <%* tR = await tp.system.prompt("Korean reading (Hangul)") %><%= tR %>
japanese: <%* tR = await tp.system.prompt("Japanese reading(s)") %><%= tR %>
vietnamese: <%* tR = await tp.system.prompt("Vietnamese reading(s)") %><%= tR %>
pos: <%* tR = await tp.system.prompt("Part of speech") %><%= tR %>
meanings: <%* tR = await tp.system.prompt("English meanings (comma-separated)") %><%= tR %>
grade_level: <%* tR = await tp.system.prompt("Dan'ayo grade level (1–6, 先進字, 名字)") %><%= tR %>
danayo_id: <%* tR = await tp.system.prompt("Dan'ayo ID number") %><%= tR %>
usage_notes: <%* tR = await tp.system.prompt("Usage notes / register (optional)") %><%= tR %>
---
