---
name: viz-domain
description: >-
  Domain situation (Munzner's first block): interview the user about the target users, their goal, at least 5 domain questions with the real need behind each, and the data, before any visualization is designed. Use at the start of a visualization project, or when asked who a visualization is for or what it should answer.
---

Establish the **domain situation**: who the visualization is for, what they need to do, which questions it must answer, and what data exists, in the users' own terms. Abstract types and tasks belong to `viz-data-abstract`.

Output: [domain-situation-template.md](references/domain-situation-template.md). You are in **block 1, Domain situation** of [visualization-blocks.md](references/visualization-blocks.md) ([diagram](assets/levels-of-viz-design.png)); check it when unsure whether a topic belongs to this block or a later one.

## The domain test

Ask only what passes: _could the user answer this without knowing anything about visualization?_ What fails is **deferred** to a later block: attribute and dataset types, abstract tasks, chart types, marks, colors, layout, interaction, format, framework, hosting, performance, deadline.

When the user drifts, return to the domain and record the drift under Deferred in one line. A chart request ("a bar chart of sales by region") gets the question behind it ("what do you want to find out?").

## The data stays closed

The user is the only source of facts about the data. List data file paths and nothing more: contents, samples and profiles come later, in `viz-data-abstract`, and a fact you read yourself replaces the meaning only the user can give. No sub-agents for data.

## 1. Ground

Read what the user already said, plus README and docs if present. List data file paths (names only). Fill the template with what is settled; list the rest as gaps.

Done when every template field is filled or listed as a gap.

## 2. Grill

Interview the user on the gaps as described in [interview.md](references/interview.md): rounds, numbered questions, a recommended answer for each. Three rules from this block override or sharpen it:

- **Facts about the data are the user's to give**, not yours to look up. Everything else in [interview.md](references/interview.md) applies, including looking up facts in README and docs.
- **Recommended answers are claims about the user's domain** that they can confirm or correct. Never recommend a visualization.
- **Pin vague answers to a concrete case**: "the last time this happened", "what do you do today". Pin vague or overloaded terms too ("renewable" meaning two things): settle one meaning and record it under Domain definitions.

The design tree, root first. Each node unblocks the next:

1. **Problem**: what goes wrong today, why now, what changes if solved.
2. **Target users**: one concrete role ("a transit planner at the city of Heilbronn"), not "everyone interested in X". Settle one primary user group: a different stakeholder per question splits the design into unrelated charts later. Audience, decision makers and data owners can be added as supporting rows. For each: role, what they already know (terms, charts they read), when and where they face the problem.
3. **Tasks**: what each stakeholder wants to accomplish, and which decision or action follows.
4. **Questions**: at least 5 that the target users would ask, in their words ("which region lost customers last quarter?"), before anyone thinks about charts. Ask for the last real question they tried to answer. For each question:
   - **Real need**: one sentence on what the user will do with the answer. A stated request ("show me a map of stations") often hides a different task ("find out when stations run empty"), and the real need is what the task abstraction checks against.
   - **Source**: dataset documentation, a real stakeholder, published use of the data, or **assumed**. Assumed questions are allowed when labelled.
   - Order the questions so they tell one story: the same users pursue one goal, and the answer to one question leads to the next (first find the stations that run empty, then when, then compare them with nearby stations).
5. **Data**: what each file, table and field means to the users; their units, codes and names; where it comes from; known gaps and errors; what must be transformed before use; who can explain it. For each question: is the data available, partial or missing? Also existing resources: people, systems, documentation.

Done when every node is covered, there are at least 5 questions with a real need and a source each, and every question is marked data available, partial or missing.

## 3. Confirm

Summarize the understanding in a few lines (who, tasks, questions, data) and ask the user to confirm it.

Done when the user confirms. Wait for that before writing.

## 4. Write

Fill the template into `docs/domain-situation.md`:

- One S row for the primary target users (plus supporting rows if any), one T row per task, one Q row per question with its real need, source and the data needed (or marked missing), in story order.
- Every decision from the grill is a D row (D1, D2, ...: about, question, answer, consequence).
- Every defined term goes under Domain definitions; every deferred item under Deferred.

Done when the target users are one concrete role, every question has a real need and a source, and every grill answer is a D row.

Finish with the target users in one sentence, the questions as the story they tell, and the questions with missing data. Next: `viz-data-abstract`.
