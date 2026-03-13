import re
from pathlib import Path

WORD_DIR = Path("words")

pattern = re.compile(r"^(.*)\.md$")

for file in WORD_DIR.iterdir():
    if not file.is_file():
        continue

    m = pattern.match(file.name)
    if not m:
        continue

    word = m.group(1)

    # Skip files like "X (char).md" just in case they exist here
    if word.endswith(" (char)"):
        continue

    text = file.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find second ---
    dash_count = 0
    yaml_end = None

    for i, line in enumerate(lines):
        if line.strip() == "---":
            dash_count += 1
            if dash_count == 2:
                yaml_end = i
                break

    if yaml_end is None:
        continue

    # Find first nonblank line after YAML
    j = yaml_end + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1

    # If first content line already starts with >, leave it alone
    if j < len(lines) and lines[j].startswith(">"):
        continue

    insert_block = [
        f">[!tip] This is a page about the word {word}.",
        f"> For the character, see [{word}](/characters/{word} (char).md).",
        ""
    ]

    lines = lines[:yaml_end + 1] + insert_block + lines[yaml_end + 1:]

    file.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("Done.")

