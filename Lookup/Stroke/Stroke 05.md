> [[Stroke]]

See also 
- SKIP 1: 
	- [[SKIP-1-1-4]]: [[必 (char)]], [[旧 (char)]]
	- [[SKIP-1-2-3]]: [[加]], [[氷]], [[代]], [[以 (char)|以]], [[仙]], [[仗]], [[付]], [[他 (char)]]
	- [[SKIP-1-3-2]]: [[弘]], [[幼]], [[夗]], [[刊 (char)|刊]], [[功]], [[北]], [[卯]], [[叩]], [[叫 (char)|叫]], [[叭]], [[叱]], [[外]], [[奴]], [[巧]], [[打]], [[氾]], [[汀 (char)|汀]], [[汁 (char)|汁]], [[犯]]
	- [[SKIP-1-4-1]]: [[札 (char)]], [[礼 (char)]]
- SKIP 2: 
	- [[SKIP-2-1-4]]: [[主]], [[永]], [[示]]
	- [[SKIP-2-2-3]]
	- [[SKIP-2-3-2]]
	- [[SKIP-2-4-1]]: [[丕]], [[氐]], [[旦]]
- SKIP 3: 
	- [[SKIP-3-1-4]]: [[司]]
	- [[SKIP-3-2-3]]: [[右]], [[用]], 
	- [[SKIP-3-3-2]]: [[四 (char)|四]]
- SKIP 4
	- [[SKIP-4-5-1]]: [[母]], [[且 (char)|且]]
	- [[SKIP-4-5-2]]: [[由 (char)|由]], 
	- [[SKIP-4-5-3]]
	- [[SKIP-4-5-4]]

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "5" OR stroke_count = 5
SORT skip_number ASC