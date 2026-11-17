---
name: viz-prototype
description: Go through Munzner's design blocks autonomously (domain situation, data abstraction, task abstraction, encoding) and build a visualization prototype with 5 different, near-finished D3.js designs per question, plus a decisions.md that records every choice, so the user can react to real pictures instead of abstract choices. Use when the user wants to see options, try a quick prototype, or is unsure which chart or encoding fits, even if the domain, data or task docs are still incomplete or missing.
---

You go through Munzner's nested blocks in [visualization-blocks.md](../viz-domain/references/visualization-blocks.md) on your own, from the domain situation through the data and task abstraction down to **block 3, Visual encoding/interaction idiom**, settling every open question yourself instead of stopping to ask. The goal is to make design choices visible, not to ship. The code is disposable, but the pictures must look finished: a rough chart gets rejected for its rough look, not for its design.

## 1. Run every block yourself

Walk through the viz-skills in block order and settle each block on your own, without interviewing the user. Each block builds on the one before: the domain gives the questions, the data abstraction gives the attribute types, the task abstraction turns each question into {action, target}, and the encoding picks marks and channels for those types and that task.

| Block | Skill | If its doc exists | If it is missing |
|---|---|---|---|
| Domain situation | `viz-domain` | read `docs/domain-situation.md` | infer the stakeholder, the tasks and the questions from the data and the request |
| Data abstraction | `viz-data-abstract` | read `docs/data-abstraction.md` | type the attributes you will use, and name the derived ones |
| Task abstraction | `viz-task-abstract` | read it | rewrite the main question as {action, target}, and pick the one main task the 5 designs answer |
| Encoding | `viz-encoding` | read the encoding notes | apply [marks-channels.md](../viz-encoding/references/marks-channels.md) and the checklist in [perceptual-principles.md](../viz-encoding/references/perceptual-principles.md) to every design |

Use each skill's references and principles, but don't write the block docs in `docs/`. Record every decision in the prototype's `decisions.md` (step 3) instead, marked **doc**, **assumed** or **user**, and keep going. Build one prototype folder per question. If the user names several questions (or "all"), build one folder for each, in parallel where possible. If they name none, take the one the docs mark as the core. Ask the user only if you don't know which dataset to use.

## 2. Pick 5 genuinely different designs

Each design is a different answer to the main task, not a restyle of the same chart. Vary at least one of:
- **mark and chart type**: bars, dots, lines, area, heatmap cells
- **the attribute on the strongest channel**: whatever sits on the shared position axis is what readers compare best ([marks-channels.md](../viz-encoding/references/marks-channels.md))
- **arrangement**: one view, small multiples, sorted or grouped
- **what is derived**: raw values, differences, ranks, shares

Write down the task each design serves best and the trade-off it makes. If two designs answer the same task the same way, replace one of them.

## 3. Build one file

Write `prototypes/<short-name>/index.html`: a single self-contained page.
- Use the real data (inlined, or a sample if it's large), never fake numbers.
- Put all 5 designs on the page, with tabs or keys `1`–`5` to switch between them, and a "show all" grid.
- Under each design, add one caption: its name, the task it serves, and its trade-off.
- Build every design with **D3.js v7**, loaded from a CDN with a pinned version (`https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js`). Draw SVG yourself with D3 scales, axes, shapes and joins: one `draw(el, small)` function per design that fills `el` and redraws on resize, so the same code renders the full view, the "All" grid card and the thumbnail. No other charting library, no build step, no framework.

Work each design out almost fully:
- **Layout:** the active chart fills most of the viewport and resizes with the window. Below it, put a slim caption strip (task | trade-off). At the bottom, a floating pill nav (`1 Name · 2 Name · … · All`), with keys `1`–`5` and `0`, and `#n` in the URL to open a design directly. The "All" view is a grid of cards, and clicking a card opens that design.
- **Titles:** the page header carries the topic (the project or article title) as a small line, then the main question as the title, numbered as in the domain doc (`Q3: …`); no filler words such as "prototypes". Below or beside it, with the fixed context (periods, data source, unit, key definitions) in one compact meta row; nothing is repeated under each design. Each design gets two lines and no label: a headline with the one message the design shows for its task (short, under about 10 words, no list of numbers), and a subtitle that says what is plotted and in which unit. The nav pill already names the chart type. Check the message against the data before you write it. Keep headlines neutral if the domain asks for it: state quantities, don't judge claims.
- **Craft:** a quiet neutral background, one web font, light gridlines, no chart borders, and one colour per category kept the same in every design. Labels go on the marks (values, series names, reference lines) instead of in a legend wherever they fit. Add tooltips, and mark key events and periods (a rule or a shaded band). No overlapping or clipped labels at full size or in the grid.
- **Encoding:** pass every design through the `viz-encoding` checklist: magnitudes that must be compared go on aligned position or length, colour stays for categories or a diverging sign, and diverging attributes get a diverging scale centred on their midpoint.
- **Check before you show it:** wait for web fonts before rendering (otherwise the label widths are measured in the wrong font and get clipped). Take a screenshot of every design and of the grid with a headless browser, look at each one, and fix what is broken.

Next to it, write `prototypes/<short-name>/decisions.md`: every decision behind the prototype, so the folder can be reused without the conversation. Number each decision (P1, P2, …) and give its source (**doc**, **assumed** or **user**). Sections:
1. Domain situation: stakeholder, the main question chosen and why, tone.
2. Data abstraction: windows or filters, time step, unit, groupings, derived attributes, handling of missing values, plus the key numbers the designs show.
3. Task abstraction: the main {action, target} task, secondary tasks, derived attributes needed.
4. Encoding: one table row per design (marks, what the strongest channel carries, other channels, best for, trade-off, principles), then decisions that hold across designs (colours, scales, labelling). The principles column names the theory each design applies, as `Name: how`, separated by `;`, for example `Effectiveness: share on aligned position; Weber: only the bottom stack layer is aligned; Gestalt enclosure: crisis band`. Use the terms from [marks-channels.md](../viz-encoding/references/marks-channels.md) and [perceptual-principles.md](../viz-encoding/references/perceptual-principles.md): expressiveness, effectiveness, Gestalt (proximity, similarity, enclosure, connection, continuity), Stevens, Weber, pop-out.
5. Build: library and versions, layout, rendering choices.
6. Open: every **assumed** decision the user should confirm, as a checklist.
7. Feedback: a table `| Round | Design | Rating | Tags |`, written by `serve.py` on every click of the page's feedback buttons.
8. Outcome: empty until step 5.

**What goes where:** the user's `prototypes/` folder holds only `.html` pages and the `decisions.md` files. All code lives in this skill's [scripts/](scripts/) folder and is never copied there as a separate file: no `.js`, `.py` or `.css` files in `prototypes/`, and every page is self-contained.

The feedback pill comes from [scripts/feedback.js](scripts/feedback.js); `build.py` inlines it into every `index.html` before `</body>`, so don't add it by hand. It adds a slim feedback pill for the current design: one rating (★ Closest, only one per question; Keep; Drop), fixed issue tags behind an "Issues" button (wrong chart type, hard to read, too busy, headline off, colours, missing context), and no free-text field. When the page is served by [scripts/serve.py](scripts/serve.py) (http://127.0.0.1:8765/, HTML pages only), every click is posted to the server, which rewrites the current round's rows in section 7 of that `decisions.md` and reruns `build.py`; the pill shows "Saved to decisions.md". Opened as a plain file, the pill falls back to "Export feedback", which downloads `feedback-<folder>.json`. It relies on the page's globals `D`, `cur` and `show(i)`, so keep those names.

Then run `python <this skill folder>/scripts/build.py prototypes` (Python 3 with the `markdown` package; if it is missing, `pip install markdown`). It inlines the feedback pill into every `index.html` and turns each `decisions.md` into a plain overview, `decisions.html`: the open items first, then one line per decision grouped by block, with a dot for its source (assumed decisions highlighted), and the five designs with their trade-offs and principles. It also builds `prototypes/compare.html`, a visual comparison structured by Munzner's blocks from top to bottom (domain situation, data abstraction, task abstraction, encoding/idiom, algorithm/build), with the questions side by side in each block. Each block cell shows a bar of doc, assumed and user decisions and lists only the assumed ones. The task block shows the main {action, target} as chips. The encoding block is a grid of live thumbnails (one row per question, five designs each; the page in `?thumb` mode) with the user's rating and principle chips, and clicking one opens that design in the hub. Keep both pages this plain: an overview to check, not a report. It expects the section numbering above, decision rows as `| P<n> | decision | source |`, and the `Principles` column. Rerun it after every change to a `decisions.md`.

Then create or update the hub `prototypes/index.html`: one page that switches between all prototype folders. Its slim top bar holds only a pill nav with one entry per domain question (`Q1` … `Qn`, the full question as a tooltip, greyed out if that question has no folder yet) and an "Open on its own" link; the topic and question already sit in each prototype's header, so don't repeat them; and the selected prototype in a full-size iframe below. A second pill switches the view between **Prototype** (`index.html`) and **Decisions** (`decisions.html`), and a **Compare all** pill opens `compare.html`. `#q2` in the URL opens Q2, `#q2/3` its design 3, `#q2/decisions` its decisions, and `#compare` the comparison. Keep the list of questions in one array at the top of the script. When you add a folder, add or enable its entry and leave the others as they are.

Open the hub through `serve.py` (or the file directly if the server can't run), or tell the user the address.

## 4. Let the user react

Start `python <this skill folder>/scripts/serve.py prototypes` in the background and point the user to http://127.0.0.1:8765/. Ask them to rate the designs with the feedback pill (the clicks land in section 7 of `decisions.md` by themselves) or to answer in chat. Then read section 7. If they used a plain file and exported instead, read the newest `~/Downloads/feedback-<folder>*.json` (the browser may add a suffix like ` (1)`) and add the rows yourself. Treat the ratings and tags as the user's verdict, and ask in chat only when tags conflict or say too little to act on (for example "Colours" without saying which). Mixing is fine ("3's layout with 1's colors"). Each round, revise the same `index.html`, and update `decisions.md` in the same pass: change the affected rows, mark the user's answers as **user**, tick the confirmed items in section 6, raise the round number in the header, and rerun `build.py`. Stop when the user picks a direction.

## 5. Record the outcome

Fill section 8 of `decisions.md`: the chosen design, what was mixed in from others, and why each rejected design lost. If a correction changes an earlier block (wrong task, wrong attribute type), say so and hand off to `viz-iterate`, which can take the decisions straight from this file into the block docs. Keep the folder: `index.html` plus `decisions.md` is the reusable record.
