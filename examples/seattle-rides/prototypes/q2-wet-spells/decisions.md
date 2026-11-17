# Prototype decisions: Q2 wet spells

| | |
|---|---|
| **Prototype** | [index.html](index.html): 5 designs, keys `1`–`5`, `0` = all, `#n` in the URL opens design n |
| **Date** | 2026-11-17 |
| **Status** | round 1. Waiting for the user's ratings. |
| **Inputs read** | [domain-situation.md](../../docs/domain-situation.md), [data-abstraction.md](../../docs/data-abstraction.md). No task abstraction and no encoding notes exist, so both blocks are assumed below. |

Source: **doc** = taken from an existing block doc; **assumed** = Claude decided in place of the user; **user** = the user said so. Open items are listed in section 6.

## 1. Domain situation (`viz-domain`)

| # | Decision | Source |
|---|---|---|
| P1 | Stakeholder: the club's ride organizer (S1), deciding between postponing and cancelling rained-off rides. | doc (S1) |
| P2 | Question: **Q2**, how long a wet spell lasts once a ride is rained off. | doc (Q2) |
| P3 | Tone: practical and plain. | doc (D1) |

## 2. Data abstraction (`viz-data-abstract`)

| # | Decision | Source |
|---|---|---|
| P4 | Wet day = any precipitation above 0 mm; a wet spell is a run of wet days ending on the first dry day. | doc (definitions) |
| P5 | Derived spell attributes: start, end, length in days, total mm, mm per day; 204 spells in 2012–2015. | doc (derived attributes) |
| P6 | Length groups for colour: 1 day, 2–3, 4–6, 7+ days. | assumed |
| P7 | A spell crossing 31 Dec is drawn up to 31 Dec in the timeline and counted once, in the year it starts. | assumed |
| P8 | Key numbers: 149 of 204 spells last 1–3 days; the longest is 19 days from 9 Dec 2012; 16 of 17 spells of 7+ days start between October and March; 43 % of all days are wet. | assumed |

## 3. Task abstraction (`viz-task-abstract`)

| # | Decision | Source |
|---|---|---|
| P9 | Main task: {summarize, distribution} of spell lengths, to judge whether postponing by a few days is enough. | assumed |
| P10 | Secondary tasks: {locate, outliers} long spells in the year; {compare, trends} wet days by month; {correlate, features} length vs intensity. | assumed |

## 4. Encoding (`viz-encoding`), per design

| # | Design | Marks | Strongest channel carries | Other channels | Best for | Trade-off | Principles |
|---|---|---|---|---|---|---|---|
| 1 | Lengths | bars | number of spells per length (length from 0) | dark = 1–3 days; value labels | the share of short spells | hides timing in the year | Effectiveness: count on aligned length; Pop-out: dark short spells |
| 2 | Timeline | one rect per spell | start day in the year (horizontal position) | width = length; lightness = length group; shaded Apr–Aug | when long spells happen | short spells are slivers; year-end cut | Gestalt proximity: winter clusters; Enclosure: the dry season band; Weber: width differences only clear for long spells |
| 3 | Wet days | heatmap cells | — (month × year as two position axes) | sequential blue = wet days; number in each cell; average row outlined | wet days by month and year | colour is less precise; days, not spells | Expressiveness: sequential scale for a count; Gestalt enclosure: the average row |
| 4 | Tomorrow | line with points | chance the next day is wet (vertical position) | % labels; spell counts; dashed baseline | the postpone decision | a derived rate; small samples after 5 days | Effectiveness: rate on aligned position; Gestalt connection: one line |
| 5 | Intensity | jittered dots + mean bars | mm per day (vertical position) | lightness = length group; mean labels | heavier rain in long spells | groups hide the exact relation | Stevens: position for intensity; Gestalt similarity: one shade per group |

| # | Cross-design decision | Source |
|---|---|---|
| P11 | One blue ramp for spell length in every design, darker = longer. | assumed |
| P12 | Labels on the marks; legends only for the length groups. | assumed |

## 5. Build

| # | Decision | Source |
|---|---|---|
| P13 | D3.js 7.9.0 from jsDelivr, SVG, Inter font, one hand-written draw function per design; real data inlined (1,461 rows), spells derived in the page. | user (skill) |
| P14 | Layout and titles from the viz-prototype skill; charts redraw on resize. | user (skill) |

## 6. Open: to confirm

- [ ] P4: does a drizzle day (< 1 mm) end a spell for riding purposes?
- [ ] P6: are 1 / 2–3 / 4–6 / 7+ days the groups members think in?
- [ ] P9: is the length distribution the main task, or the "tomorrow" chance (design 4)?

## 7. Feedback

One row per rated design and round, written automatically by `serve.py` when you click the feedback buttons in `index.html`.

| Round | Design | Rating | Tags |
|---|---|---|---|

## 8. Outcome

_Not chosen yet._ Record here which design was chosen, what was mixed in from other designs, and why each rejected design lost. If a correction changes P1–P10, hand off to `viz-iterate`.
