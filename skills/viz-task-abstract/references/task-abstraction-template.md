# Task abstraction: <project name>

Terms are defined in the `viz-task-abstract` skill's task-types.md. Questions and real needs come from `docs/domain-situation.md`; attributes from `docs/data-abstraction.md`.

| | |
|---|---|
| **Date** | <YYYY-MM-DD> |
| **Status** | <draft / primaries confirmed by user> |

## 1. Tasks per question

One block per domain question.

### Q1: <domain question, verbatim>

**Real need:** <what the user will do with the answer>

**Marked:** <question and real need with task verbs in **bold** and nouns in _italics_>

**Sorted:** task verbs: <…> · delivery verbs (dropped): <… / none> · data: `<attribute>`, … · targets: <…>

**Abstract task(s):**
- T1: <action> + <target> + <data, with card attribute names>. Analyze: <discover (generate / verify) / present / enjoy / annotate / record / derive>. Search: <lookup / locate / browse / explore>. Query: <identify / compare / summarize>.
- T2 (chained, if the goal needs several steps): <then …>

**Testable as:** <what a viewer reads off a chart to complete the task, e.g. "the three stations with the largest negative net flow at 8 am">

**Real-need check:** <unchanged / changed: ~~first version~~ → revised version, and why>

**Missing data:** <`<attribute>`: derive as <formula from raw attributes> / cannot be answered: <which part, why> / none>

## 2. Summary

| Domain question | Real need | Abstract task (action + target + data) | Attributes used | Derived or missing |
|---|---|---|---|---|
| Q1 | <…> | T1: <…> | `<attribute>`, … | <derived `<x>` / missing: … / none> |

## 3. Ranking

| Rank | Task | Primary? | Why |
|---|---|---|---|
| 1 | T1 | <yes / no> | <how it differs in action or target from the other primaries; or why not primary> |

## 4. Consistency check

- [ ] Every attribute in a primary task appears on the data card, as raw or derived attribute.
- [ ] Every derived attribute is needed by at least one task.
- [ ] Every attribute kept on the card is used by at least one task, or the card says why it is kept.
- [ ] Every data issue that affects a primary task has a stated handling.
- [ ] No task contains an output verb or a chart type.
- [ ] Each primary task can be answered with the data. Partly answerable: <which part cannot / none>
- [ ] The visualized dataset type fits the primary tasks.

<one line per exception: which item, why it is accepted>

## 5. Decisions

| # | About | Question | Answer | Consequence |
|---|---|---|---|---|
| D1 | <Q1 / T1 / attribute> | <question asked> | <answer> | <consequence for the tasks or the card> |

## 6. Open questions

| # | About | Question | Best guess used | Who could answer |
|---|---|---|---|---|
| O1 | <T1> | <question> | <guess> | <stakeholder / data owner> |

## 7. Changes

The abstraction is a working document: when encoding or a prototype shows a task was wrong, keep the first version above (struck through) and log the change here.

| Date | What changed | Why (evidence) |
|---|---|---|
| <YYYY-MM-DD> | <first version> | <—> |
