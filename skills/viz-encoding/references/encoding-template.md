# Visual encoding: <project name>

Terms are defined in the `viz-encoding` skill's marks-channels.md. Tasks come from `docs/task-abstraction.md`, attribute types from `docs/data-abstraction.md`. Sketches: [encoding-sketches.html](encoding-sketches.html) (next to this doc).

| | |
|---|---|
| **Date** | <YYYY-MM-DD> |
| **Status** | <draft / choice confirmed by user> |
| **Scope** | Static: one still image per task, no tooltips, filtering, zooming, animation or linked views |

## T1: <action + target + data, copied from the task abstraction>

### Attributes and channels

| Rank | Attribute | Type | Levels / range | Channel | Reason |
|---|---|---|---|---|---|
| 1 | `<attribute>` | <categorical / ordinal / quantitative> | <n levels / min–max unit> | <position on common scale / …> | <expressiveness and effectiveness, tied to the task> |
| – | `<attribute>` | <…> | <…> | left out | <why it doesn't fit> |

**Mark(s):** one mark = <one item / one aggregate (which) / one link>; type <point / line / area>. <Further mark types, if the design combines them.>

**Reference marks and layout:** <mean tick, threshold rule, offset to separate ties, …: purpose of each / none>

**Effectiveness checklist:** <result of each check in viz-effectiveness.md §4, one line each>

### Alternatives

| # | Design | Mark | Channel of the top attribute | Other channels | Shows well | Shows badly |
|---|---|---|---|---|---|---|
| A | <name> | <…> | <…> | <…> | <…> | <…> |
| B | <name> | <…> | <…> | <…> | <…> | <…> |
| C | <name> | <…> | <…> | <…> | <…> | <…> |

**Real-value sample** (<n> values, how selected):

| <key attribute> | <attribute> | … |
|---|---|---|
| <value> | <value> | … |

### Decision

**Chosen:** <A / B / C>. <2–3 sentences referring to the task.>

**Weakness:** <one thing the design shows badly, and what could cover it>

## Decisions

| # | About | Question | Answer | Consequence |
|---|---|---|---|---|
| D1 | <T1 / attribute> | <question> | <answer> | <consequence> |

## Open questions

| # | About | Question | Best guess used |
|---|---|---|---|
| O1 | <…> | <…> | <…> |

**Deferred:** interaction (tooltips, filtering, linked views), <other later topics, or none>

## Changes

| Date | What changed | Why (evidence) |
|---|---|---|
| <YYYY-MM-DD> | <first version> | <—> |
