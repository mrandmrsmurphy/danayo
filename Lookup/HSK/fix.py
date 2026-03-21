import re
from pathlib import Path

filename = input("File name: ").strip()
path = Path(filename)

text = path.read_text(encoding="utf-8")

new_text = re.sub(
    r"^([^:\n]+):\s*(\d+)$",
    r"[[\1]]: \2",
    text,
    flags=re.MULTILINE
)

path.write_text(new_text, encoding="utf-8")
print("Done.")

