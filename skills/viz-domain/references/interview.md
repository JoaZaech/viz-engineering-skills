# Interviewing the user

How `viz-domain`, `viz-data-abstract`, `viz-task-abstract` and `viz-encoding` ask their questions. The goal is a shared understanding with nothing silently assumed, at the lowest cost to the user.

**Work the design tree in rounds.** Each decision unblocks the ones that hang off it. The *frontier* is every question whose prerequisites are already settled. Ask the whole frontier in one round, then wait for the answers. A question that depends on an answer still open this round belongs to a later round. Recompute the frontier after every round.

**Number each question and recommend an answer**, worded so that "yes" accepts it. The user then only corrects what is wrong instead of composing every answer from scratch:

```
❓ **Q1** - **<title>**: <question, with choices if there are any>

➡️ <your recommended answer>

---

❓ **Q2** - ...
```

**Facts are yours to find, decisions are the user's.** Look up whatever the environment can answer (files, README, codebook, a profile script) before asking; ask only about meaning, intent and priorities. The calling skill may narrow this (in `viz-domain`, facts about the data's meaning come from the user, not from reading the files).

**If the user can't answer now** (they asked you to go ahead, or you run unattended): write the round to `docs/questions-for-user.md`, continue with your recommended answers, and mark every decision that rests on one as **open** (O1, O2, …) in the doc you write, so nothing assumed passes as confirmed.

**Done when the frontier is empty**: every branch visited, each item clear, confirmed by the user, or recorded as open with a best guess. Don't act on the result until the user confirms the summary.
