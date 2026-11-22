---
name: viz-data-abstract
description: >-
  Data abstraction (Munzner's "What?"): identify and describe a dataset's type(s), items, keys, attributes and their types, derived and dropped attributes, data-quality issues and open questions. Use after the domain situation is clarified, before choosing a visualization, or when the user asks what kind of data they have.
---

Describe the dataset in abstract terms: its **dataset type(s)**, its **items**, and each **attribute**'s type. Types follow **semantics**, never storage: `"5k"` is a string but ordinal; a ZIP code is an integer but categorical.

You are in **block 2, Data/task abstraction** (the data part, "What?") of [visualization-blocks.md](../viz-domain/references/visualization-blocks.md). It needs block 1 (`viz-domain`) done; topics from later blocks (charts, marks, colors) are deferred to `viz-encoding`.

Vocabulary and allowed values: [data-types.md](references/data-types.md), with visual summaries [summary_data_types.png](assets/summary_data_types.png) and [summary_dataset_types.png](assets/summary_dataset_types.png). Use its terms only (attribute, not column; data model, not storage type; dataset type, data type and attribute type are three different things). Output format: [data-abstraction-template.md](references/data-abstraction-template.md). Every template section must be filled; write "none" rather than leaving one out.

## 1. Ground

Read the domain situation (stakeholders, questions, data) from the conversation; if absent, run `viz-domain` first. Identify the dataset it concerns, which may be several files, searching the working directory if the user didn't name it.

Done when the file(s) are named and the stakeholders' questions are known.

## 2. Profile

Never read the dataset into context. Write a small Python script (pandas or the standard library) that answers the template's fields for this dataset, run it, and read its output. It prints counts, ranges and at most a few example rows:

- per file: the item, item count, attribute count, file size on disk, and which data types it has (attributes, links, positions, grids)
- per attribute: data model, nulls, distinct count, range or top values
- key candidates: simple and compound attributes, tested for uniqueness on **all** rows; print the duplicate count
- links between files: join attributes, match rate, unmatched ids
- missing values: every encoding (empty, `NA`, `null`, `-99`, `0`, `"unknown"`) and its count per attribute
- implausible or impossible values: negatives where impossible, end before start, coordinates out of range, outliers
- inconsistent units or number formats: decimal comma vs point, mixed date formats, mixed units in one attribute
- hierarchies, 1:1 code/label pairs, constant attributes
- links, positions, grids, when the dataset type has them

Read every metadata file (README, codebook, schema) in full. Tag each fact you record with its source: `D` if the script showed it, `M` if the metadata states it.

Fill what the output and metadata settle. Done when each template field is answered or listed as a doubt.

## 3. Grill

Interview the user on the doubts as described in [interview.md](../viz-domain/references/interview.md): rounds, numbered questions, a recommended answer for each. Look up facts yourself; ask only about meaning and intent. The stakeholders' questions decide which readings matter (temperature can be quantitative, ordinal or categorical, depending on the task). Cover:

- **Dataset type**: every dataset type the data can be read as (a table of trips is also a network of stations), which one to visualize, and the transformation to get there.
- **Item and key**: what one item (row, node, cell) is in each file, how files link, whether the key is unambiguous (unique by meaning).
- **Attributes**: meaning, unit or order the script and metadata could not settle.
- **Keep, derive, drop**: which attributes the questions need, which derived attributes they need (formula and raw inputs), and one reason for each dropped attribute.
- **Data issues**: for each finding, the handling: filter, impute, flag, or keep and show.

Done when every attribute and issue is **clear**, **confirmed** by the user, or recorded **open** with a best guess. No doubts: skip this step.

## 4. Write

Fill [data-abstraction-template.md](references/data-abstraction-template.md) into `docs/data-abstraction.md`:

- **Size** covers raw and kept items × attributes and the size as loaded in the browser, after the transformation and in the shipped format. If it is above ~10 MB, say what aggregation or format change brings it down.
- The **Attributes** table lists kept attributes only, raw and derived. Attribute type is exactly one of categorical, ordinal or quantitative; nuance goes in Meaning. Ordering direction is `—` for categorical.
- Every dropped attribute appears in **Dropped attributes** with one reason. Kept plus dropped equals all raw attributes.
- **Data issues** has a row for each check, even when nothing was found.
- Write every grill decision into **Decisions** (D1, D2, …) and every unanswered question into **Open questions** (O1, O2, …, with the best guess used). Cite them in the attribute's confidence (`confirmed (D1)`, `open (O1)`).

Finish with the visualized dataset type, the attribute count per type, the issues and their handling, and the open questions. Next: `viz-task-abstract`, the other half of this block.
