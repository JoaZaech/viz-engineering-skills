---
name: viz-encoding
description: >-
  Visual encoding (Munzner's "How?"): for each primary task, rank its attributes, choose the mark, assign channels by expressiveness and effectiveness, compare three static alternatives drawn from 10-20 real values, and pick one with its reason and its weakness. Use after the data and task abstraction, or when asked which chart, mark, colour or channel fits an attribute or a task, or why one encoding beats another.
---

Design a **static** visual encoding for each primary task: one still image that answers the task without tooltips, filtering, zooming, animation or linked views. Interaction is a separate decision, deferred to after this block; a static image forces the encoding itself to carry the answer.

You are in **block 3, Visual encoding/interaction idiom** of [visualization-blocks.md](../viz-domain/references/visualization-blocks.md). It needs block 1 (`docs/domain-situation.md`, from `viz-domain`) and block 2 (`docs/data-abstraction.md` from `viz-data-abstract`, `docs/task-abstraction.md` from `viz-task-abstract`); if one is missing, run that skill first.

References:
- [marks-channels.md](references/marks-channels.md): marks, channels, the channel ranking, expressiveness and effectiveness ([marks.png](assets/marks.png), [channels.png](assets/channels.png), [channel-effectiveness.png](assets/channel-effectiveness.png)).
- [perceptual-principles.md](references/perceptual-principles.md): why the ranking holds (Gestalt, Stevens, Weber) and a design checklist.
- [viz-effectiveness.md](references/viz-effectiveness.md): accuracy, discriminability, separability, popout, grouping, and the effectiveness checklist ([example_seperability.png](assets/example_seperability.png)).

Output format: [encoding-template.md](references/encoding-template.md). Work through the steps below for each primary task, or for the ones the user names; start with the top-ranked one. Each task gets its own view; combining views is a later decision. If the primaries are not yet confirmed, go ahead, but list the encoding's dependence on them under Open questions.

## 1. Task and attributes

Copy the task from `docs/task-abstraction.md` (action + target + data). List the attributes it uses with their type from the data card and their number of levels (categorical, ordinal) or range (quantitative), and rank them by importance **for this task**: the attribute the target is about comes first.

## 2. Mark

State what one mark represents (one item, one aggregate, or one link) and its type (point, line, area). If the task's data is an aggregate (a mean per month), the mark is the aggregate, not the raw item.

## 3. Channels

Assign one channel per attribute, in priority order:
- **Expressiveness**: ordered attributes (ordinal, quantitative) get magnitude channels; categorical attributes get identity channels. A magnitude channel on a categorical attribute invents an order that isn't there.
- **Effectiveness**: the most important attribute gets the most effective channel still free, usually position on a common scale.
- Keep to about 8 hues and 5 shapes; beyond that, viewers can no longer tell the categories apart.
- An attribute that doesn't fit is left out, and you say so. A cluttered encoding answers no task well.
- A cyclic attribute (month, hour, weekday) keeps its order on the axis; say how the wrap is handled (Dec next to Jan: repeat a month, or a radial layout if the wrap matters for the task).
- Reference marks (a mean tick, a threshold rule) and layout devices (a small offset to separate ties) are not data attributes; list them separately with their purpose.

Run the effectiveness checklist in [viz-effectiveness.md](references/viz-effectiveness.md#4-effectiveness-checklist) on the result.

## 4. Three alternatives

Sketch three designs that differ in the **mark** or in the **channel of a top-priority attribute**, not only in colour. Three restyles of one chart give the user no real choice. Each alternative should be one you could defend for the task; don't add a deliberately weak design as filler, and if two candidates turn out nearly equal in effectiveness, say so: that's a finding too. Good sources of candidates: From Data to Viz (by data type), the FT Visual Vocabulary (by what the chart should show), the D3 gallery. Describe each candidate in marks and channels and check it against step 3 before keeping it.

Draw them from **10 to 20 real values** taken from the data with a short script; never invent values. If the mark is an aggregate and the task compares a small complete set (12 months × 4 years), use the whole set rather than cutting the comparison, and say so. A small real sample shows the actual problems (a skewed value, a long label, a tie) that fake data hides. List the sample in the doc.

Render the three sketches side by side in `docs/encoding-sketches.html`: one self-contained page, D3.js v7 from a pinned CDN URL (`https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js`), the sample inlined, no tooltips or other interaction. Under each, one line: mark, the channel of the top attribute, and what it shows well. Take a screenshot with a headless browser if one is available, look at it, and fix overlapping or clipped labels.

## 5. Decide

Recommend one design, with the reason in 2 to 3 sentences that refer to the task (not to taste), and name one thing it shows badly. Every encoding has a weakness, and naming it shows what a second view or the interaction milestone must cover. Ask the user to confirm the choice, as in [interview.md](../viz-domain/references/interview.md).

## 6. Write

Fill [encoding-template.md](references/encoding-template.md) into `docs/encoding.md`: one section per primary task with the task sentence, the attribute table (attribute, type, levels or range, rank, channel, reason), the mark, the three alternatives, the real-value sample, the chosen design and its weakness. Record decisions (D1, …) and open questions (O1, …).

Finish with each primary task, its chosen design in one line and its weakness. If a step showed that a task or an attribute is wrong, hand off to `viz-iterate` instead of patching it here. Next: `viz-prototype` to build the chosen designs out, or the interaction design.
