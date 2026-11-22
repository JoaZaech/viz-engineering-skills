# Data Types and Semantics

The vocabulary for answering **"What?"** (data abstraction): what the items and attributes are, and what kind of dataset they form.

## Contents

1. [Core terms](#1-core-terms): item, attribute
2. [Attribute types](#2-attribute-types): categorical, ordinal, quantitative
3. [Ordering direction](#3-ordering-direction): sequential, diverging, cyclic
4. [Data types](#4-data-types): items, attributes, links, positions, grids
5. [Dataset types](#5-dataset-types): tables, networks, fields, geometry, and the data types that make up each
6. [Dataset availability](#6-dataset-availability): static, dynamic
7. [Attribute descriptors](#7-attribute-descriptors): key, data model, unit / range, source
8. [From raw to visualized data](#8-from-raw-to-visualized-data): transformation, derived, dropped, data issues and their handling
9. [Temporal and hierarchical semantics](#9-temporal-and-hierarchical-semantics): time as value or key, attribute hierarchies

Visual summaries (the tables below transcribe their content):
- [summary_data_types.png](../assets/summary_data_types.png): data types, dataset types, attribute types, ordering direction, dataset availability
- [summary_dataset_types.png](../assets/summary_dataset_types.png): dataset types and the data types each one is built from

---

## 1. Core terms

The same numbers mean different things depending on **semantics** (real-world meaning: grouping, unit, order) and **data type** (structural or mathematical interpretation). `22, 7, 0, 19.3, 14.19, 7` can be one point in 6-D space, two points in 3-D space, or the weight of the heaviest fish caught on each of the last 6 days, and each reading needs a different chart. Semantics can sometimes be inferred from the raw data (a `Date` column); otherwise it comes from **metadata** (a dataset description). The line between data and metadata is often blurry.


- **Item**: an individual entity; a discrete unit. Examples: a row in a table, a node in a network, a city or country in geometry.
- **Attribute**: a property of an item that can be measured, observed or logged. Example: a column in a table.

## 2. Attribute types

| Type | Ordered? | Meaning | Example |
|---|---|---|---|
| **Categorical** | No | Can only be compared for equality. May have a hierarchy or grouping (apple Gala vs. apple Pink Lady vs. orange) | Run clubs; shapes + ● ■ ▲ |
| **Ordinal** | Yes | Can be compared and ordered, but arithmetic is often not sensible | Race distance 5k < 10k < half < marathon (a race classified by length); shirt sizes S, M, L |
| **Quantitative** | Yes | Arithmetic is meaningful | Height of a person; time to finish a race |

Ordinal and quantitative attributes together are **ordered** data. Ordered data also has an [ordering direction](#3-ordering-direction).

![Attribute types: categorical (shapes), ordered: ordinal (shirt sizes), quantitative (lengths)](../assets/summary_data_types.png)

## 3. Ordering direction

Applies only to ordered attributes ([ordinal or quantitative](#2-attribute-types)).

- **Sequential**: a homogeneous range from a minimum to a maximum. Example: race time; mountain height above sea level.
- **Diverging**: two sequences that meet at a common zero point. Example: temperature around 0 °C; elevation relative to sea level.
- **Cyclic**: values wrap around back to the start point. Example: an annual race date; time of day.

## 4. Data types

The five building blocks of any dataset:

- **Items**: see [Core terms](#1-core-terms).
- **Attributes**: see [Core terms](#1-core-terms).
- **Links**: relationships between items, as in a graph.
- **Positions**: points in 2D or 3D space, usually latitude/longitude or x/y/z.
- **Grids**: a strategy for sampling continuous data. A grid defines its *geometry* (where the cells are) and its *topology* (how neighboring cells are connected).

## 5. Dataset types

Dataset types arise from combinations of the [data types](#4-data-types).

| Dataset type | Built from | Notes |
|---|---|---|
| **Tables** | Items, Attributes | **Flat table**: each row is an item, each column an attribute, each cell a value; usually one key. **Multidimensional table**: several keys index a cell (runner × year × race length → time). It can be **sparse** (some key combinations are empty) and **sliced** (fix one key to get a lower-dimensional table, e.g. all 10k times), which is especially useful with aggregation. |
| **Networks & Trees** | Items (nodes), Links, Attributes | Nodes connected by links; both nodes and links can have attributes. The layout of a network is a design choice, independent of the abstract dataset. A **tree** has no cycles and usually expresses a hierarchy. |
| **Fields** (continuous) | Grids, Positions, Attributes | The key is a continuous spatial position; each cell holds values from a continuous domain, so sampling and interpolation matter. Tasks concern spatial structure or shape. Grid types: **uniform** (geometry and topology implicit: origin, spacing, dimensions), **rectilinear** (non-uniform axis coordinates, topology implicit), **structured/curvilinear** (geometry explicit per point, topology implicit), **unstructured** (geometry and topology explicit: points and a cell list). |
| **Geometry** (spatial) | Items, Positions | Items with an intrinsic spatial location and shape, e.g. countries on a map. Can carry an intrinsic hierarchy (country → state → town); shapes are of interest. |
| **Clusters, Sets, Lists** | Items | Groupings of items. **Set**: unordered collection, membership given (can overlap). **List**: ordered collection, the position is part of the data (a leaderboard). **Cluster**: grouping computed from attribute similarity, typically not in the raw data. |

![Dataset types: tables, networks, fields, geometry, and the data types each is built from](../assets/summary_dataset_types.png)

## 6. Dataset availability

- **Static**: the whole dataset is available at once (e.g. a table of race results from one date).
- **Dynamic**: aspects of the dataset change: data arrives as a stream or is updated (a live ranking during a race; corrected end results).

## 7. Attribute descriptors

Recorded per attribute in the data abstraction, alongside its [attribute type](#2-attribute-types).

- **Key vs. value**: keys are **independent** attributes that identify an item; values are **dependent** attributes, always looked up by the keys. A name can be a key only if it is unique; a runner ID is better (flat tables often use an implicit row index). In a multidimensional table, each key becomes one axis.
- **Key**: an attribute (or combination) that uniquely identifies an item. Unambiguous when uniqueness follows from its meaning (e.g. an ID), not just from this snapshot. Simple (one attribute), compound (several attributes together), or implicit (row index). Always check uniqueness on the full data and record the duplicate count.
- **Data model**: how values are stored (int, float, string, bool, date string). Not the same as attribute type: a ZIP code stored as int is categorical.
- **Unit / range**: physical unit (km, kW), format (dd.mm.yyyy), or reference system (WGS84); none if unitless. Plus the range, which replaces cardinality: min–max for quantitative attributes, the ordered levels for ordinal ones, the number of levels for categorical ones.
- **Source**: where a fact about an attribute comes from: D (inferred from the data) or M (stated in the metadata/documentation).

## 8. From raw to visualized data

- **Transformation**: changing the dataset type, e.g. aggregating a table of trips into a network of station-to-station links.
- **Derived attribute**: an attribute computed from raw ones, recorded with its formula or procedure and the raw attributes it uses (e.g. `duration = end_time - start_time`, aggregated per hour of day).
- **Dropped attribute**: a raw attribute that is not used, recorded with one reason (constant, redundant, not needed for any question, mostly missing).
- **Data issue**: a key duplicate, implausible or impossible value, missing value (with its encoding: empty, `NA`, `-99` …), or inconsistent unit or number format. Each issue is handled in one of four ways:
  - **Filter**: remove the affected items.
  - **Impute**: replace the value with an estimate, and record the method.
  - **Flag**: keep the item and mark it with an attribute such as `is_suspect`.
  - **Keep and show**: keep the item as is and make it visible in the visualization (e.g. a "missing" category).
- **Open question**: something the documentation does not answer, recorded with the best guess currently in use.

## 9. Temporal and hierarchical semantics

- **Time as a value** (temporal data): time is an attribute of an item, e.g. the date a race took place. Patterns to look for are **recurring** (does a runner run faster in the morning?) and **change over time** (does a runner get faster over the season?).
- **Time as a key** (time-varying data): the dataset is indexed by time, e.g. animal-tracking sensors that give one interaction network per time step.
- **Time series**: one value per regular time step, e.g. a stock price.
- **Attribute hierarchy**: an attribute can be aggregated at several levels (GDP of continents → countries → states; a stock price within a week vs. a multi-year trend; super nodes that aggregate items in a network). Record the levels, and which one each question needs.
