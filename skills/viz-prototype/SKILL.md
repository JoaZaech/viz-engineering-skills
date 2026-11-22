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
| Task abstraction | `viz-task-abstract` | read `docs/task-abstraction.md`; the 5 designs answer its primary task for this question | rewrite the main question as action + target + data, check it against the real need, and pick the one main task the 5 designs answer |
| Encoding | `viz-encoding` | read `docs/encoding.md`; its chosen design and its alternatives become designs 1–3, and the attribute ranking holds | apply [marks-channels.md](../viz-encoding/references/marks-channels.md) and the checklist in [perceptual-principles.md](../viz-encoding/references/perceptual-principles.md) to every design |

Use each skill's references and principles, but don't write the block docs in `docs/`. Record every decision in the prototype's `decisions.md` (step 3) instead, marked with its source, and keep going:
- **doc**: settled by a block doc in `docs/`;
- **data**: read from the data file by your profiling script (a count, a range, which columns are empty);
- **assumed**: your choice where neither the docs nor the data decide (a definition, a threshold, which measure to plot). These are what the user checks first, so mark every judgement call this way, never as doc or data;
- **user**: the user said so.

Layout and build rules that come from this skill are not decisions; leave them out. Build one prototype folder per question. If the user names several questions (or "all"), build one folder for each, in parallel where possible. If they name none, take the one the docs mark as the core. Ask the user only if you don't know which dataset to use.

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
- **Layout:** the active chart fills most of the viewport and resizes with the window. Below it, put a slim caption strip (task | trade-off). At the bottom left, a floating pill nav (`1 Name · 2 Name · … · All`), with keys `1`–`5` and `0`, and `#n` in the URL to open a design directly; the bottom right belongs to the feedback pill, so a centred nav would collide with it. The "All" view is a grid of cards, and clicking a card opens that design. `compare.html` shows each design as a thumbnail via `?thumb#n`; the inlined feedback script then hides `header`, `nav`, `.cap`, `.sub` and the feedback pill. So put the page header in `<header>`, the design nav in `<nav>` and the caption strip in `.cap`, and use the class `.sub` only for things a thumbnail should drop.
- **Titles:** the page header carries the topic (the project or article title) as a small line, then the main question as the title, numbered as in the domain doc (`Q3: …`); no filler words such as "prototypes". Below or beside it, with the fixed context (periods, data source, unit, key definitions) in one compact meta row; nothing is repeated under each design. Each design gets two lines and no label: a headline with the one message the design shows for its task (short, under about 10 words, no list of numbers), and a subtitle that says what is plotted and in which unit. The nav pill already names the chart type. Compute every number and every comparison in a headline, caption or decision with your data script before you write it, and quote what the script printed. Comparative words make claims about all items: "fastest", "most" or "same start" need the comparison across the whole dataset, not just the items you highlighted, and "both rose together" needs a correlation that supports it. Readers trust a finished-looking chart, so a loose headline misleads more than a rough one. Keep headlines neutral if the domain asks for it: state quantities, don't judge claims.
- **Craft:** a quiet neutral background, one readable web font with some character (for example IBM Plex Sans, Source Sans 3, Work Sans or Public Sans; not Inter or Roboto, which make every prototype look alike), light gridlines, no chart borders, and one colour per category kept the same in every design. Labels go on the marks (values, series names, reference lines) instead of in a legend wherever they fit. Add tooltips, and mark key events and periods (a rule or a shaded band). No overlapping or clipped labels at full size or in the grid.
- **Encoding:** pass every design through the `viz-encoding` checklist: magnitudes that must be compared go on aligned position or length, colour stays for categories or a diverging sign, and diverging attributes get a diverging scale centred on their midpoint.
- **Check before you show it:** wait for web fonts before rendering (otherwise the label widths are measured in the wrong font and get clipped). Take a screenshot of every design and of the grid with a headless browser, look at each one, and fix what is broken. `compare.html` loads its thumbnails lazily, so scroll through it before you screenshot it.

Next to it, write `prototypes/<short-name>/decisions.md`: every decision behind the prototype, so the folder can be reused without the conversation. Start it with `# Prototype decisions: Q<n>: <question>`. Number each decision (P1, P2, …) as a table row `| P<n> | decision | source |`, with the source from step 1 (**doc**, **data**, **assumed** or **user**). Sections:
1. Domain situation: stakeholder, the main question chosen and why, tone.
2. Data abstraction: windows or filters, time step, unit, groupings, derived attributes, handling of missing values, plus the key numbers the designs show.
3. Task abstraction: the main {action, target} task, secondary tasks, derived attributes needed.
4. Encoding: one table row per design, with the header `| # | Design | Marks | Strongest channel | Other channels | Best for | Trade-off | Principles |` (marks, what the strongest channel carries, other channels, best for, trade-off, principles), then decisions that hold across designs (colours, scales, labelling). The principles column names the theory each design applies, as `Name: how`, separated by `;`, for example `Effectiveness: share on aligned position; Weber: only the bottom stack layer is aligned; Gestalt enclosure: crisis band`. Use the terms from [marks-channels.md](../viz-encoding/references/marks-channels.md) and [perceptual-principles.md](../viz-encoding/references/perceptual-principles.md): expressiveness, effectiveness, Gestalt (proximity, similarity, enclosure, connection, continuity), Stevens, Weber, pop-out.
5. Build: library and versions, layout, rendering choices.
6. Open: every **assumed** decision the user should confirm, as a checklist.
7. Feedback: a table `| Round | Design | Rating | Tags |`, which you fill from the feedback the user exports, copies or writes in chat (step 4).
8. Outcome: empty until step 5.

**What goes where:** the user's `prototypes/` folder holds only `.html` pages and the `decisions.md` files. Helper scripts you write (data prep, page generator, screenshots) go in a fresh temporary folder of their own; the pages must not depend on them, since the data is inlined. All code lives in this skill's [scripts/](scripts/) folder and is never copied there as a separate file: no `.js`, `.py` or `.css` files in `prototypes/`, and every page is self-contained.

The feedback pill comes from [scripts/feedback.js](scripts/feedback.js); `build.py` inlines it into every `index.html` before `</body>`, so don't add it by hand. It adds a slim feedback pill for the current design: one rating (★ Closest, only one per question; Keep; Drop), fixed issue tags behind an "Issues" button (wrong chart type, hard to read, too busy, headline off, colours, missing context), and no free-text field. There is no server: every click is kept in the browser's `localStorage`, and the pill offers **Export**, which downloads `feedback-<folder>.json`, and **Copy**, which puts the ratings on the clipboard as section-7 table rows to paste into the chat. It relies on the page's globals `D`, `cur` and `show(i)`, so keep those names.

Then run `python <this skill folder>/scripts/build.py prototypes` with a Python 3 that has the `markdown` package (check with `python3 -c 'import markdown'`; try another interpreter on the PATH, such as an Anaconda one, before you `pip install markdown`). It inlines the feedback pill into every `index.html` and turns each `decisions.md` into a plain overview, `decisions.html`: the open items first, then one line per decision grouped by block, with a dot for its source (assumed decisions highlighted), and the five designs with their trade-offs and principles. It also builds `prototypes/compare.html`, a visual comparison structured by Munzner's blocks from top to bottom (domain situation, data abstraction, task abstraction, encoding/idiom, algorithm/build), with the questions side by side in each block. Each block cell shows a bar of doc, assumed and user decisions and lists only the assumed ones. The task block shows the main {action, target} as chips. The encoding block is a grid of live thumbnails (one row per question, five designs each; the page in `?thumb` mode) with the user's rating and principle chips, and clicking one opens that design in the hub. Keep both pages this plain: an overview to check, not a report. It expects the section numbering above, decision rows as `| P<n> | decision | source |`, and the `Principles` column. Rerun it after every change to a `decisions.md`.

Then create or update the hub `prototypes/index.html`: one page that switches between all prototype folders. Its slim top bar holds only a pill nav with one entry per domain question (`Q1` … `Qn`, the full question as a tooltip, greyed out if that question has no folder yet) and an "Open on its own" link; the topic and question already sit in each prototype's header, so don't repeat them; and the selected prototype in a full-size iframe below. A second pill switches the view between **Prototype** (`index.html`) and **Decisions** (`decisions.html`), and a **Compare all** pill opens `compare.html`. `#q2` in the URL opens Q2, `#q2/3` its design 3, `#q2/decisions` its decisions, and `#compare` the comparison. Keep the list of questions in one array at the top of the script. When you add a folder, add or enable its entry and leave the others as they are.

Never start a local server: every page works opened straight from disk. Open the hub as a file (`open prototypes/index.html` on macOS, `xdg-open` on Linux, `start` on Windows), or give the user its absolute path.

## 4. Let the user react

Ask the user to rate the designs with the feedback pill and then click **Export** (or **Copy** and paste the rows into the chat), or just to answer in chat. If they exported, read the newest `~/Downloads/feedback-<folder>*.json` (the browser may add a suffix like ` (1)`); its `designs` object maps each design number to `name`, `rating` and `tags`. Write one row per rated design into section 7 of that `decisions.md`, with the current round number. Treat the ratings and tags as the user's verdict, and ask in chat only when tags conflict or say too little to act on (for example "Colours" without saying which). Mixing is fine ("3's layout with 1's colors"). Each round, revise the same `index.html`, and update `decisions.md` in the same pass: change the affected rows, mark the user's answers as **user**, tick the confirmed items in section 6, raise the round number in the header, and rerun `build.py`. Stop when the user picks a direction.

## 5. Record the outcome

Fill section 8 of `decisions.md`: the chosen design, what was mixed in from others, and why each rejected design lost. If a correction changes an earlier block (wrong task, wrong attribute type), say so and hand off to `viz-iterate`, which can take the decisions straight from this file into the block docs. Keep the folder: `index.html` plus `decisions.md` is the reusable record.
