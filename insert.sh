#!/bin/bash
# Insert meta-bind-embed block into all Markdown files under 'characters/'
# Inserts after YAML front matter if it exists, otherwise at the very top.

cd "/Users/robertmarshallmurphy/Documents/danayo" || exit


set -euo pipefail
VAULT="/Users/robertmarshallmurphy/Documents/danayo"
PATTERN='words/*.md'   # change to 'words/**/*.md' if you have subfolders
BACKUP=1               # set to 0 to disable .bak backups

cd "$VAULT" || { echo "Vault not found: $VAULT"; exit 1; }

for f in $PATTERN; do
  [ -f "$f" ] || continue

  # Skip files that already contain the snippet
  if grep -q 'meta-bind-embed' "$f" && grep -q '\[\[nav/word_info\]\]' "$f"; then
    continue
  fi

  echo "Inserting into: $f"
  [ "$BACKUP" -eq 1 ] && cp -p "$f" "$f.bak"

  # Insert after YAML (--- ... ---) if present, else at top
  awk '
    BEGIN {in_yaml=0; inserted=0}
    # Start of YAML (allow spaces after ---)
    NR==1 && $0 ~ /^---[[:space:]]*$/ {in_yaml=1; print; next}

    # End of YAML
    in_yaml && $0 ~ /^---[[:space:]]*$/ && NR>1 {
      in_yaml=0
      print
      if(!inserted){
        print "```meta-bind-embed\n[[nav/word_info]]\n```"
        inserted=1
      }
      next
    }

    # No YAML case — top of file (first non-YAML line)
    NR==1 && !in_yaml && !inserted {
      print "```meta-bind-embed\n[[nav/word_info]]\n```"
      inserted=1
    }

    {print}
  ' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done

echo "Done."
