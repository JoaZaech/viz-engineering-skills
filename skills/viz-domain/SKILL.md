---
name: viz-domain
description: Domain situation (Munzner's first block): interview the user about stakeholders, tasks, questions and data before any visualization is designed. Use at the start of a visualization project, or when asked who a visualization is for or what it should answer.
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

Call the `grilling` skill on the gaps. Three rules from this block override or sharpen it:

- **Facts about the data are the user's to give**, not yours to look up. Everything else in `grilling` applies, including looking up facts in README and docs.
- **Recommended answers are claims about the user's domain** that they can confirm or correct. Never recommend a visualization.
- **Pin vague answers to a concrete case**: "the last time this happened", "what do you do today". Pin vague or overloaded terms too ("renewable" meaning two things): settle one meaning and record it under Domain definitions.

The design tree, root first. Each node unblocks the next:

1. **Problem**: what goes wrong today, why now, what changes if solved.
2. **Stakeholders**: users, audience, decision makers, data owners. For each: role, what they already know (terms, charts they read), when and where they face the problem. Who is missing?
3. **Tasks**: what each stakeholder wants to accomplish, and which decision or action follows.
4. **Questions**: what each stakeholder wants to answer, in domain terms ("which region lost customers last quarter?"). Ask for the last real question they tried to answer.
5. **Data**: what each file, table and field means to the users; their units, codes and names; where it comes from; known gaps and errors; what must be transformed before use; who can explain it. For each question: is the data available, partial or missing? Also existing resources: people, systems, documentation.

Done when every node is covered for every stakeholder, and every question is marked data available, partial or missing.

## 3. Confirm

Summarize the understanding in a few lines (who, tasks, questions, data) and ask the user to confirm it.

Done when the user confirms. Wait for that before writing.

## 4. Write

Fill the template into `docs/domain-situation.md`:

- One S row per stakeholder, one T row per task (linked to its S), one Q row per question (linked to its S and the data needed, or marked missing).
- Every decision from the grill is a D row (D1, D2, ...: about, question, answer, consequence).
- Every defined term goes under Domain definitions; every deferred item under Deferred.

Done when every stakeholder has a task, every task and question has a stakeholder, and every grill answer is a D row.

Finish with the counts of stakeholders, tasks and questions, and list questions with missing data. Next: `viz-data-abstract`.
