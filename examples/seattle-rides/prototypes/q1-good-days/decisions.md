# Prototype decisions: Q1 good riding days

| | |
|---|---|
| **Prototype** | [index.html](index.html): 5 designs, keys `1`–`5`, `0` = all, `#n` in the URL opens design n |
| **Date** | 2026-11-17 |
| **Status** | round 1. Rated by the user, waiting for the pick. |
| **Inputs read** | [domain-situation.md](../../docs/domain-situation.md), [data-abstraction.md](../../docs/data-abstraction.md). No task abstraction and no encoding notes exist, so both blocks are assumed below. |

Source: **doc** = taken from an existing block doc; **assumed** = Claude decided in place of the user; **user** = the user said so. Open items are listed in section 6.

## 1. Domain situation (`viz-domain`)

| # | Decision | Source |
|---|---|---|
| P1 | Stakeholder: the club's ride organizer (S1), planning the 2027 calendar and sharing one chart in the newsletter. | doc (S1) |
| P2 | Question: **Q1**, which months give the most good riding days. | doc (Q1) |
| P3 | Tone: practical and plain; headlines say what a rider can expect. | doc (D1) |

## 2. Data abstraction (`viz-data-abstract`)

| # | Decision | Source |
|---|---|---|
| P4 | Good riding day = 0 mm rain and a high of 15–30 °C. | doc (definitions) |
| P5 | Derived `outcome` per day: Good, Wet (any rain), Too cold (dry, high < 15 °C), Too hot (dry, high > 30 °C). Wet wins over temperature. | assumed |
| P6 | Months are compared on the average of 2012–2015 (good days ÷ 4); single years only in design 4. | doc (D2) |
| P7 | Key numbers: May 20.8, Jun 19.0, Jul 22.1, Aug 21.1, Sep 20.5 good days per month; Dec 0, Jan 0.5, Nov 0.5. In July 23 of 124 days are too hot and 11 wet. | assumed |

## 3. Task abstraction (`viz-task-abstract`)

| # | Decision | Source |
|---|---|---|
| P8 | Main task: {compare, distribution} of good days across months, to pick the core season. | assumed |
| P9 | Secondary tasks: {identify, features} why a month fails (rain, cold or heat); {compare, trends} between years for reliability. | assumed |

## 4. Encoding (`viz-encoding`), per design

| # | Design | Marks | Strongest channel carries | Other channels | Best for | Trade-off | Principles |
|---|---|---|---|---|---|---|---|
| 1 | Months | bars | good days per month (length from 0) | value labels; dashed rule at 20 days | ranking the months | hides why months fail and how years differ | Effectiveness: count on aligned length; Expressiveness: ordered months on a common axis |
| 2 | Why not | normalized stacked bars | share of good days (bottom layer, aligned) | hue = outcome; % labels in segments | the reason each month fails | only the bottom layer is aligned; months of different length look equal | Effectiveness: good share on aligned position; Weber: upper layers float; Gestalt similarity: one hue per outcome |
| 3 | Calendar | one rect per day | day of year (horizontal position) | hue = outcome; one row per year | runs of good days and year-to-year consistency | counting by eye is hard | Gestalt proximity: runs form blocks; Pop-out: green season against grey and blue |
| 4 | Years | lines with points | good days per month and year | lightness = year; shaded band on Sep–Oct | reliability of each month | crossing lines; no single average | Gestalt connection: one line per year; Enclosure: shaded swing months |
| 5 | Temperature | jittered dots | daily high (vertical position) | hue = outcome; green band = riding range | the margin to the temperature rule | 1,461 dots overlap; counts unreadable | Gestalt enclosure: the riding band; Stevens: position for temperature; Pop-out: green dots inside the band |

| # | Cross-design decision | Source |
|---|---|---|
| P10 | One colour per outcome in every design: Good green, Wet blue, Too cold grey-blue, Too hot orange. | assumed |
| P11 | Labels on the marks wherever they fit; a legend only where four outcomes share a mark. | assumed |

## 5. Build

| # | Decision | Source |
|---|---|---|
| P12 | D3.js 7.9.0 from jsDelivr, SVG, Inter font, one hand-written draw function per design; real data inlined (1,461 rows). | user (skill) |
| P13 | Layout and titles from the viz-prototype skill; jitter uses a fixed seed so dots stay put between redraws; charts redraw on resize. | user (skill) |

## 6. Open: to confirm

- [ ] P5: should a day with a trace of rain (< 1 mm) still count as rideable?
- [ ] P8: is ranking months the main task, or is the reason (design 2) what the newsletter needs?
- [ ] P10: is orange for "too hot" fine next to the green, or should heat be a second blue?

## 7. Feedback

One row per rated design and round, recorded by the agent from the feedback you export, copy or write in chat.

| Round | Design | Rating | Tags |
|---|---|---|---|
| 1 | 1 Months | keep |  |
| 1 | 2 Why not | closest | Missing context |
| 1 | 3 Calendar | keep |  |
| 1 | 4 Years | drop | Hard to read |
| 1 | 5 Temperature | drop | Too busy |

## 8. Outcome

_Not chosen yet._ Record here which design was chosen, what was mixed in from other designs, and why each rejected design lost. If a correction changes P1–P9, hand off to `viz-iterate`.
