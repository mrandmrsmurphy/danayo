---
characters: <% tR = await tp.system.prompt("Constituent characters comma-sep") %>
mandarin: <% tR = await tp.system.prompt("Mandarin pronunciation (pinyin)") %>
cantonese: <% tR = await tp.system.prompt("Cantonese pronunciation (jyutping)") %>
korean: <% tR = await tp.system.prompt("Korean reading (Hangul)") %>
japanese: <% tR = await tp.system.prompt("Japanese reading(s)") %>
vietnamese: <% tR = await tp.system.prompt("Vietnamese reading(s)") %>
pos: <% tR = await tp.system.prompt("Part of speech") %><%= tR %>
meanings: <% tR = await tp.system.prompt("English meanings (comma-separated)") %>
grade_level: <% tR = await tp.system.prompt("Dan'ayo grade level (1–6, 先進字, 名字)") %>
danayo_id: <% tR = await tp.system.prompt("Dan'ayo ID number") %>
usage_notes: <% tR = await tp.system.prompt("Usage notes / register (optional)") %>
---
