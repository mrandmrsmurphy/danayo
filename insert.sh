#!/bin/bash
# Insert meta-bind-embed block into all Markdown files under 'characters/'
# Inserts after YAML front matter if it exists, otherwise at the very top.

cd "/Users/robertmarshallmurphy/Documents/danayo" || exit


for f in characters/*.md; do
  # Skip if file already contains the snippet
  if grep -q 'meta-bind-embed' "$f"; then
    continue
  fi

  echo "Inserting into: $f"

  awk '
    BEGIN {in_yaml=0; inserted=0}
    # Detect start of YAML front matter
    NR==1 && $0 ~ /^---[[:space:]]*$/ {in_yaml=1; print; next}

    # Detect end of YAML front matter
    in_yaml && $0 ~ /^---[[:space:]]*$/ && NR>1 {
      in_yaml=0
      print
      if(!inserted){
        print "```meta-bind-embed\n[[nav/char_info]]\n```"
        inserted=1
      }
      next
    }

    # No YAML case — top of file
    NR==1 && !in_yaml && !inserted {
      print "```meta-bind-embed\n[[nav/char_info]]\n```"
      inserted=1
    }

    {print}
  ' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done

