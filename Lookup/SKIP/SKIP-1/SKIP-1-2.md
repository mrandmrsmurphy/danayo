---
date-last-perfect: 2026-03-06
---

> [[SKIP]] : 1

1. no
2. [SKIP-1-2-2](lookup/SKIP/SKIP-1/SKIP-1-2-2.md): 什, 仁, 仇, 仍, 切, 刈, 化, 双, 収, 比
3. [SKIP-1-2-3](lookup/SKIP/SKIP-1/SKIP-1-2-3.md): 他, 仗, 付, 仙, 代, 以, 加, 氷
4. [SKIP-1-2-4](lookup/SKIP/SKIP-1/SKIP-1-2-4.md): 仮, 仰, 仲, 件, 任, 伊, 伍, 伎, 伏, 伐, 休, 伝, 佤, 州, 次
5. [SKIP-1-2-5](lookup/SKIP/SKIP-1/SKIP-1-2-5.md): 伯, 伴, 伶, 伸, 伺, 伽, 似, 佃, 但, 佇, 位, 低, 住, 佐, 佑, 体, 何, 作, 佛, 佞, 冴, 冶, 冷
6. [SKIP-1-2-6](lookup/SKIP/SKIP-1/SKIP-1-2-6.md): 佳, 使, 侃, 例, 侍, 侏, 侑, 侘, 供, 依, 価, 侮, 協
7. [SKIP-1-2-7](lookup/SKIP/SKIP-1/SKIP-1-2-7.md): 侠, 侯, 侵, 侶, 便, 俁, 係, 促, 俄, 俊, 俐, 俗, 俘, 保, 信
8. [SKIP-1-2-8](lookup/SKIP/SKIP-1/SKIP-1-2-8.md): 修, 俯, 俳, 俵, 俸, 俺, 個, 倍, 倒, 候, 倚, 借, 倣, 値, 倫, 倭, 倶, 倹, 凄, 准, 凍, 唳, 帰
9. [SKIP-1-2-9](lookup/SKIP/SKIP-1/SKIP-1-2-9.md): 倦, 偈, 偏, 偕, 停, 健, 偪, 偰, 偲, 側, 偵, 偶, 偷, 偽, 頂, 頃
10. [SKIP-1-2-10](lookup/SKIP/SKIP-1/SKIP-1-2-10.md): 偉, 傀, 傅, 傍, 備, 僅, 博, 馮
11. [SKIP-1-2-11](lookup/SKIP/SKIP-1/SKIP-1-2-11.md): 傑, 催, 傭, 傲, 債, 傷, 傾, 僧, 損, 鳩
12. [SKIP-1-2-12](lookup/SKIP/SKIP-1/SKIP-1-2-12.md): 僑, 僕, 僚, 像
13. [SKIP-1-2-13](lookup/SKIP/SKIP-1/SKIP-1-2-13.md): 僵, 僻, 儀, 億, 凜
14. [SKIP-1-2-14](lookup/SKIP/SKIP-1/SKIP-1-2-14.md): 儒, 凝
15. [SKIP-1-2-15](lookup/SKIP/SKIP-1/SKIP-1-2-15.md): 償, 儡, 儧, 優, 儲

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-2")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```