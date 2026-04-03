---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. No
2. [[SKIP-3-8-2]]: 勉, 閃
3. [[SKIP-3-8-3]]: 問, 彪, 閉
4. [[SKIP-3-8-4]]: 悶, 開, 閏, 閑, 間, 閔, 閙
5. No
6. [[SKIP-3-8-6]]: 聞, 関, 閣, 閥, 閨
7. [[SKIP-3-8-7]]: 閲, 魅
8. [[SKIP-3-8-8]]: 䦧 (char), 䦨
9. [[SKIP-3-8-9]]: 闊
10. [[SKIP-3-8-10]]: 闕, 闖, 闘


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-8")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```