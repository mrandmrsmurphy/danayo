> [[Stroke]]

### 1-1-2
[[小 (char)|小]], [[川 (char)|川]]
### 2-1-2
[[三 (char)|三]]
### 2-2-1
[[乞]]
### 3-1-2
[[刃]]
### 3-2-1
[[万]], [[凡]], [[勺]], [[寸]], [[山]]
### 4-3-1
[[下]], [[久]], [[于 (char)]], [[兀]], [[叉]], [[及]], [[口]], [[夕]], [[子]], [[工]], [[己]], [[已]], [[巳]], [[干]], [[弓]]
### 4-3-2
[[上 (char)]], [[也]], [[亡]], [[土]], [[士]], 
### 4-3-3
[[千]], [[屮]], [[巾]], [[才]]
### 4-3-4
[[丈]], [[与]], [[丸]], [[之 (char)]], [[大 (char)|大]], [[女]]

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "3" OR stroke_count = 3
SORT skip_number ASC