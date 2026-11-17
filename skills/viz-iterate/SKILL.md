---
name: viz-iterate
description: Rework an existing visualization. Use when the user has a finished or draft chart or a viz-prototype round and says it isn't working, wants to change or improve it, or got feedback on it. Reads the block docs, the prototypes, their decisions.md and the user's ratings, infers what to optimize, finds which design block each problem belongs to and re-runs that block's skill and every block after it.
---

1. Gather everything that already exists:
   - the current viz, and the block docs (docs/domain-situation.md, docs/data-abstraction.md, the task abstraction, the encoding);
   - every `prototypes/<name>/` folder for the question: look at `index.html` (take screenshots of each design with a headless browser if you can't tell from the code) and read `decisions.md`, especially the decisions P1, P2, … and their source, section 6 (open items), section 7 (feedback: rating and issue tags per design and round) and section 8 (outcome). If the user exported feedback instead, read the newest `~/Downloads/feedback-<folder>*.json`.
2. Infer what to optimize before asking. Read the prototypes as evidence:
   - **Ratings:** what the ★ Closest and Keep designs share (mark, what sits on the strongest channel, arrangement, derived attribute) is what works; what the Drop designs share is what to avoid. Name the pattern, not just the winner.
   - **Issue tags**, mapped to a block: wrong chart type → `viz-encoding`, or `viz-task-abstract` if every design got it (the task is wrong, not the chart); hard to read / too busy → `viz-encoding` (channel, density, labelling); colours → `viz-encoding`; headline off → check the message against the data, or `viz-domain` if the question itself is off; missing context → `viz-domain` or `viz-data-abstract` (missing attribute, period, unit).
   - **Assumed decisions:** every **assumed** row that a Drop or an issue tag points at is a likely root cause; confirmed **user** rows are fixed constraints, don't change them.
   - **Rounds:** compare rounds; a tag that persists after a revision means the fix was in the wrong block, so move one block up.
   - **Outcome:** keep the chosen design and what was mixed in, and don't reintroduce what section 8 says lost and why.
   Write the inferred optimizations as a short list (each: evidence → block → change) and show it to the user. Ask only what the evidence leaves open, or the user's own complaint if there is no prototype or feedback.
3. Place each problem in the earliest block it touches, using [visualization-blocks.md](../viz-domain/references/visualization-blocks.md):
   - wrong audience or wrong question → `viz-domain`
   - attribute typed wrong, missing or needs deriving → `viz-data-abstract`
   - the viz doesn't support what users need to do → `viz-task-abstract`
   - wrong chart, channel or color → `viz-encoding`
   - unsure which design is better → `viz-prototype` (5 alternatives to compare), seeded with what step 2 found: keep the patterns that worked, drop the ones that didn't
   - only rendering bugs → fix the code directly, no skill needed
4. Run that skill, updating its doc rather than starting over. Carry the prototype decisions into the block docs: **user** decisions go in as confirmed, **assumed** ones only if the feedback supports them, otherwise flag them as open.
5. Re-run each later block in order. Keep what still holds and change only what the upstream change breaks.
6. If a prototype folder exists, update its `decisions.md` in the same pass (change the affected rows, mark the user's answers as **user**, tick confirmed items in section 6, note the round in section 8) and rerun the `viz-prototype` skill's `scripts/build.py prototypes`.
7. Show what changed in each doc, which feedback or decision drove each change, and the new viz.
