# Data abstraction: Seattle daily weather 2012–2015

| | |
|---|---|
| **File(s)** | `data.csv` |
| **Date** | 2026-11-17 |
| **Dataset type** | **table**: one item per day, a time series |
| **Size** | 1,461 items × 6 attributes; derived: 204 wet spells |

## Items and keys

| File | Item | Count | Key | Uniqueness checked? |
|---|---|---|---|---|
| `data.csv` | one calendar day in Seattle | 1,461 | `date` (simple) | yes: 0 duplicates, 0 missing days |
| *derived* spells | one run of consecutive wet days | 204 | `start` (simple) | yes, by construction |

## Attributes

| Attribute | Type | Ordering direction | Unit / range | Notes |
|---|---|---|---|---|
| `date` | ordinal (temporal) | sequential | 2012-01-01 … 2015-12-31 | key; cyclic by month and day of year |
| `precipitation` | quantitative | sequential | 0 … 55.9 mm | 0 on 838 days |
| `temp_max` | quantitative | diverging around the 15–30 °C riding range | −1.6 … 35.6 °C | |
| `temp_min` | quantitative | sequential | −7.1 … 18.3 °C | not used |
| `wind` | quantitative | sequential | 0.4 … 9.5 m/s | not used |
| `weather` | categorical | — | sun, rain, fog, drizzle, snow | not used: `precipitation` is more exact |

## Derived attributes

| Attribute | Type | Derived from |
|---|---|---|
| `outcome` | categorical: Good, Wet, Too cold, Too hot | `precipitation`, `temp_max` and the riding range |
| `good_days` per month | quantitative | count of `outcome = Good` |
| spell `length` | quantitative (days) | runs of `precipitation > 0` |
| spell `rain_per_day` | quantitative (mm) | spell total ÷ length |
