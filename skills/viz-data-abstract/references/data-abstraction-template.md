# Data abstraction: <dataset name>

Terms are defined in [data-types.md](data-types.md). Use only those values. **Source** is always `D` (inferred from the data by the profiling script) or `M` (stated in the metadata/documentation); `D+M` when both agree.

| | |
|---|---|
| **File(s)** | `<path>` (one line per file) |
| **Metadata** | <README, codebook, schema, URL; or none> |
| **Date** | <YYYY-MM-DD> |

## 1. Dataset

| | |
|---|---|
| **[Dataset type(s)](data-types.md#5-dataset-types)** | Possible: <every type the data can be read as, each one of table / multidimensional table / network / tree / field / geometry / cluster / set / list; e.g. table (trips); network (stations)>. **Visualized: <type>**: <why, tied to the stakeholders' questions> |
| **[Transformation](data-types.md#8-from-raw-to-visualized-data)** | <how the raw data becomes the visualized type, e.g. aggregate trips into station-to-station edges weighted by trip count; or none> |
| **[Availability](data-types.md#6-dataset-availability)** | <static / dynamic (streaming, regularly updated: cadence)>: <why> |
| **Size** | <n> items × <n> attributes raw; <n> items × <n> attributes kept; <file size on disk> → <size as loaded in the browser, after filtering/aggregation and in the format shipped (CSV / JSON / Parquet, gzipped?)> |

## 2. Items and structure

One row per file (or per item type after transformation).

| File | [Item](data-types.md#1-core-terms): one row/record is | Count | [Key](data-types.md#7-attribute-descriptors) | Uniqueness checked? | Links to |
|---|---|---|---|---|---|
| `<file>` | <item, e.g. one trip (row) / station (node) / grid cell / region (geometry)> | <n> | `<attribute>` (<simple / compound / implicit>) | <yes: 0 duplicates / yes: n duplicates (see I1) / no: reason> | `<file>.<attr>` → `<file>.<attr>` (<1:1 / 1:n / n:m>; <n> unmatched) |

| | |
|---|---|
| **Unambiguous key?** | <yes / no>: <unique by meaning (an ID), or only in this snapshot> |
| **Not a key** | `<attribute>`: <reason, e.g. 3 duplicates> |
| **[Links](data-types.md#4-data-types)** | <source → target, directed / undirected, or none> |
| **[Positions](data-types.md#4-data-types)** | <coordinate attributes, CRS, or none> |
| **[Grid](data-types.md#4-data-types)** | <grid type, dimensions, spacing, or none> |
| **[Clusters / sets / lists](data-types.md#5-dataset-types)** | <grouping, membership, or none> |
| **Hierarchy ([tree](data-types.md#5-dataset-types))** | <levels, or none> |

## 3. Attributes (kept)

One row per attribute you keep, raw and derived. Attribute type is exactly one value; put nuance in Meaning. Ordering direction is `—` for categorical.

| [Attribute](data-types.md#1-core-terms) | [Attribute type](data-types.md#2-attribute-types) | [Ordering direction](data-types.md#3-ordering-direction) | [Unit / range](data-types.md#7-attribute-descriptors) | Meaning | [Source](data-types.md#7-attribute-descriptors) | [Data type](data-types.md#4-data-types) | [Data model](data-types.md#7-attribute-descriptors) | Confidence |
|---|---|---|---|---|---|---|---|---|
| `<attribute>` | <categorical / ordinal / quantitative> | <— / sequential / diverging / cyclic> | <unit; min–max (quantitative) / ordered levels (ordinal) / n levels (categorical)> | <meaning, nuance, why this type> | <D / M / D+M> | <attribute / attribute (key) / link / position / grid> | <int / float / string / bool / date string> | <clear / confirmed (D1) / open (O1)> |

## 4. [Derived attributes](data-types.md#8-from-raw-to-visualized-data)

| Attribute | Formula / procedure | Uses (raw) | Why (question it serves) |
|---|---|---|---|
| `<duration>` | <`end_time - start_time`, in minutes; then aggregated per hour of day (mean)> | `<end_time>`, `<start_time>` | <question> |

## 5. [Dropped attributes](data-types.md#8-from-raw-to-visualized-data)

| Attribute | Reason (one) |
|---|---|
| `<attribute>` | <constant / redundant with `<x>` (1:1 code/label) / not needed for any question / >95 % missing / personal data> |

## 6. [Data issues](data-types.md#8-from-raw-to-visualized-data)

Findings from the profiling checklist. Every check gets a row, even if nothing was found. Handling is one of **filter**, **impute**, **flag**, **keep and show**.

| # | Check | Finding (counts) | Handling | Why |
|---|---|---|---|---|
| I1 | Duplicates in the key | <n duplicate keys / none> | <filter / flag / …> | <reason> |
| I2 | Implausible or impossible values | <e.g. 41 trips with duration < 0; 12 lat outside range> | <…> | <reason> |
| I3 | Missing values: encoding and count | <encoded as empty / NA / -99 / 0; n per attribute> | <…> | <reason> |
| I4 | Inconsistent units or number formats | <e.g. decimal comma vs point; m and km mixed; mixed date formats / none> | <…> | <reason> |
| I5 | Orphan links / unmatched joins | <n ids without match / none / n.a.> | <…> | <reason> |

## 7. Decisions

| # | About | Question | Answer | Consequence |
|---|---|---|---|---|
| D1 | `<attribute>` | <question> | <answer> | <consequence> |

## 8. Open questions

What the documentation does not answer. Each has a best guess, which this abstraction currently uses.

| # | About | Question | Best guess used | Who could answer |
|---|---|---|---|---|
| O1 | `<attribute>` | <question> | <guess> | <data owner / docs URL> |

## 9. Summary

| Group | Count | Attributes |
|---|---|---|
| [Categorical](data-types.md#2-attribute-types) | <n> | `<attribute>` |
| [Ordinal](data-types.md#2-attribute-types) | <n> | `<attribute>` |
| [Quantitative](data-types.md#2-attribute-types) | <n> | `<attribute>` |
| Ordered: [sequential](data-types.md#3-ordering-direction) | <n> | `<attribute>` |
| Ordered: [diverging](data-types.md#3-ordering-direction) | <n> | `<attribute>` |
| Ordered: [cyclic](data-types.md#3-ordering-direction) | <n> | `<attribute>` |
| Derived | <n> | `<attribute>` |
| Dropped | <n> | `<attribute>` |
| Links | <n> | `<source>` → `<target>` |
| Positions | <n> | (`<lon>`, `<lat>`) <CRS> |
| Grids | <n> | <grid> |
| Hierarchies | <n> | `<a>` → `<b>` → `<c>` |
