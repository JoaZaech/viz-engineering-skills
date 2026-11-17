# Domain situation: planning the 2027 ride calendar for Seattle Weekend Riders

| | |
|---|---|
| **Date** | 2026-11-17 |
| **Status** | confirmed by user |
| **Note** | Example scenario for the viz-engineering-skills README. The club and its organizer are made up; the data is real. |

## 1. Overview

| | |
|---|---|
| **Problem** | A volunteer plans the weekend group rides of a small Seattle cycling club. Every year rides are cancelled for rain at short notice, and members ask whether the calendar could avoid that. Before fixing the 2027 dates, the organizer wants to know which months are reliably rideable and what to expect when it does rain. |
| **Data** | `data.csv`: daily weather for Seattle, 2012-01-01 to 2015-12-31 (1,461 days), from NOAA as shipped in [vega-datasets](https://github.com/vega/vega-datasets): precipitation (mm), daily high and low (°C), wind (m/s) and a weather label. No hourly detail, so a day with any rain counts as wet even if the morning was dry. |
| **Resources** | The club's past ride log (not used here); members' preferences collected at the annual meeting. |

**Domain definitions**
- **Good riding day:** no rain at all (0 mm) and a daily high between 15 °C and 30 °C, the range the club's members said they ride in.
- **Wet day:** any precipitation above 0 mm.
- **Wet spell:** a run of consecutive wet days; it ends on the first dry day.

## 2. Stakeholders

| # | Who | Role | Knowledge | Context of use |
|---|---|---|---|---|
| S1 | Ride organizer of Seattle Weekend Riders | user, decides the calendar | Rides weekly, knows the local weather, no statistics background. | Plans once a year at a laptop; shares one chart with ~40 members in the club newsletter. |

## 3. Questions

| # | Question | Why |
|---|---|---|
| Q1 | Which months give the most good riding days? | Put the long rides into the reliable months. |
| Q2 | When rain cancels a ride, how long does the wet spell last? | Decide whether to postpone by a few days or cancel, and when to plan indoor alternatives. |

## 4. Decisions

| # | Decision |
|---|---|
| D1 | Tone: practical and plain; members read the chart in a newsletter. |
| D2 | Months are compared on the average over 2012–2015; single years are shown only to judge reliability. |
