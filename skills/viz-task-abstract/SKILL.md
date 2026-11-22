---
name: viz-task-abstract
description: >-
  Task abstraction (Munzner's "Why?"), the task half of the data/task abstraction block, paired with viz-data-abstract: rewrite each stakeholder's domain question as an abstract task (action + target + data, with analyze, search and query level), check it against the real need behind the question, list missing or derived data, rank the tasks and pick 2-3 primary ones, then run the data/task consistency check. Use after the data abstraction, before choosing a visualization, or when the user asks what users need to do with the data, why they need a visualization, or which tasks a chart must support.
---

Translate each domain question into one or more **abstract tasks**: an *action* on a *target* in named *data*. Abstract tasks are domain-independent, so the encoding can be chosen and judged against them; a question still in domain words ("which stations run empty?") can't be checked against a chart, an abstract task ("locate + extremes + bike count per station and hour") can.

You are in **block 2, Data/task abstraction** (the task part, "Why?") of [visualization-blocks.md](../viz-domain/references/visualization-blocks.md). It needs block 1 (`docs/domain-situation.md`, from `viz-domain`) and the data part (`docs/data-abstraction.md`, from `viz-data-abstract`); if either is missing, run that skill first. Charts, marks and colours are deferred to `viz-encoding`.

Vocabulary (actions at three levels, targets, chained tasks), worked examples and what makes an abstraction good: [task-types.md](references/task-types.md). The vocabulary is a starting point, not a form to fill in: a good abstraction is **precise**, **shared with the domain expert** and **testable**, whichever words it uses. If Munzner's terms are too coarse for the data (graph or spatio-temporal tasks), borrow from the taxonomies listed there and say so; if nothing fits, describe the task in plain words rather than forcing a label. Output format: [task-abstraction-template.md](references/task-abstraction-template.md).

## 1. Ground

Read the domain questions, each with its **real need** (what the user will do with the answer) and source, from `docs/domain-situation.md`, and the attribute card from `docs/data-abstraction.md`.

Done when every domain question and every kept, derived and dropped attribute is known.

## 2. Abstract, one question at a time

Keep one block per question. For each:

1. **Mark** the verbs and nouns in the question and in its real need: verbs in **bold**, nouns in _italics_.
2. **Sort.** A verb either names a task (find, compare, see whether) or only says how the result is delivered ("show", "plot", "make a map"); drop the delivery verbs, because they name a solution, not a task. A question that arrives as a chart request ("show me a map of the stations") is the *solution-first trap*: its real need, not its chart, decides the task (see the bike-sharing example in [task-types.md](references/task-types.md#6-worked-examples)). A noun either names data on the card (an item, an attribute) or names what the user looks for in that data (a trend, an outlier, a neighbour); the second kind are the **targets**.
3. **Write** the abstraction as one or more sentences of the form *action + target + data*, with an action at all three levels: **analyze** (why at all: discover, either generating or verifying a hypothesis; present; enjoy; or produce: annotate, record, derive), **search** (what the user already knows: lookup, locate, browse, explore) and **query** (how much: identify, compare, summarize). Name the data with the card's attribute names. A complex goal is a **chain** ("derive net flow, then discover its daily pattern"): write each link as its own task, in order.
   Then test it: could you say what a viewer has to read off a chart to complete this task? If not, it is too vague to judge a design against; sharpen the target or the data.
4. **Check against the real need.** Read the real-need sentence again. If it changes the action, the target or the data, the stated question hid a different task: revise. Keep the first version (struck through) and note what changed and why; the change is often the most useful finding of this block.
5. **List missing data.** For every attribute the task needs that is not on the card: say how to derive it (formula and raw attributes), or say that this part of the question cannot be answered with this data.

Fill what the docs settle. Ambiguous words in a question ("good", "busy", "unusual") are doubts, not choices to make silently. Abstract the task of the target users from the domain doc; if the same view is also used to present the answer to someone else, that is a separate task (analyze: present), not a second reading of this one.

Done when every question has at least one abstract task, a real-need check and a missing-data line.

## 3. Rank and confirm

Rank all tasks by how much the target users' decision depends on them (the real need), then by how often they come up, and propose 2 or 3 as **primary**. The encoding will be judged against the primary tasks, so choose tasks that differ in action or target, not several variants of the same lookup.

Interview the user as described in [interview.md](../viz-domain/references/interview.md) on: the primary tasks, each real-need revision, the meaning of ambiguous words, and any task the data can only partly answer. Recommend an answer for each. Read each primary task back in the user's domain words ("so you want to find the stations that run empty most often, then see at what hour"): an abstraction the domain expert doesn't recognise is not shared yet.

Done when the primaries are confirmed and every doubt is confirmed or recorded open with a best guess.

## 4. Consistency check

Data and task abstraction must fit each other. Go through this list and fix the tasks, or `docs/data-abstraction.md`, until every item holds:

- Every attribute in a primary task appears on the data card, as raw or derived attribute.
- Every derived attribute is needed by at least one task.
- Every attribute kept on the card is used by at least one task, or the card says why it is kept.
- Every data issue that affects a primary task has a stated handling (e.g. missing values in an attribute you compare).
- No task contains an output verb ("show", "display", "visualize") or a chart type.
- Each primary task can be answered with the data; if only partly, say which part cannot.
- The visualized dataset type fits the primary tasks (a task about paths or neighbours needs a network, even if the file is a table).

When a fix touches the data card, edit `docs/data-abstraction.md` in place and add a row to its Changes section (add the section if an older doc lacks it), so both docs stay true.

Done when every item is ticked or carries a stated exception.

## 5. Write

Fill [task-abstraction-template.md](references/task-abstraction-template.md) into `docs/task-abstraction.md`: one block per question, the summary table, the ranking with primaries, the consistency checklist, decisions (D1, D2, …) and open questions (O1, O2, …).

Finish with the primary tasks as one line each, what changed after the real-need checks, and any question the data cannot answer. Next: `viz-encoding`, for each primary task.
