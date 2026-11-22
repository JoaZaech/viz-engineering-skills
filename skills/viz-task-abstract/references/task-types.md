# Task Types

The vocabulary for answering **"Why?"** (task abstraction), from Munzner, *Visualization Analysis and Design*, ch. 3, and Brehmer & Munzner (2013).

## Contents

1. [Why abstract tasks](#1-why-abstract-tasks): what an abstraction is for, and what makes one good
2. [Actions](#2-actions): analyze, search, query, with examples
3. [Targets](#3-targets): what the user looks for in the data
4. [Verbs and nouns](#4-verbs-and-nouns): from a domain sentence to action and target
5. [Chained tasks](#5-chained-tasks): complex goals as a sequence
6. [Worked examples](#6-worked-examples): the solution-first trap, used cars, same task in two domains
7. [Other vocabularies](#7-other-vocabularies): when Munzner's terms are too coarse

The bike-sharing examples come from one scenario: stations in Heilbronn (Hbf, Markt, Campus, Sontheim, …) gain or lose bikes over the day, and staff rebalance them by truck.

---

## 1. Why abstract tasks

A domain question uses domain words, so every project looks different. An abstract task (verbs become **actions**, nouns become **targets**, and the sentence describes the user's goal) makes questions comparable: two questions from different domains with the same abstract task can be served by the same idiom, and two questions from the same domain with different tasks need different idioms.

The vocabulary is a **starting point, not a checklist**. Its purpose is to make questions comparable and to structure design thinking, not to fill in every field. A good abstraction is:
- **precise**: one reading only; the data it needs is named with attribute names;
- **shared with the domain expert**: they recognise their question in it (read it back to them in plain words);
- **testable**: you can say what a viewer would have to read off a chart to complete it, so a design can be judged against it.

Which vocabulary it uses is secondary.

## 2. Actions

A task contains an action at **all three levels**: why the user looks at all (analyze), what they already know (search), and how much of the data the answer concerns (query).

### Analyze (high level): why use the visualization?

| Action | Meaning | Example |
|---|---|---|
| **Consume: discover** | Find something new. *Generate* a new hypothesis, or *verify* (confirm or disconfirm) an existing one. Message unknown beforehand: often many views, no annotation | "Is there a correlation between heat and bike rentals?" |
| **Consume: present** | Communicate something the presenter already understands, typically after the analysis. Message known: one view, a headline, a callout | "Rentals drop when there is a heatwave" |
| **Consume: enjoy** | Casual, curiosity-driven use, often not aligned with the designer's goals | A research tool on name popularity, used by parents-to-be to pick a baby name |
| **Produce: annotate** | Add text or graphics to the view. Associated with items, an annotation becomes a new attribute; it is not persistent by itself | Labels for clusters in a network |
| **Produce: record** | Store a persistent artefact: a screenshot, view parameters, a list of items. Can make annotations persistent | Saving the filter settings that reproduce a view |
| **Produce: derive** | Produce new data from existing data: a new attribute (statistics, rounding, coordinates from a town name) or a transformed dataset (a table of genes into an interaction network). Can be the designer's choice and greatly expands the design space | `net flow = returns − rentals` per station and hour |

### Search (mid level): what does the user already know?

|  | **Target known** | **Target unknown** |
|---|---|---|
| **Location known** | **Lookup**: "How many bikes are at Hbf right now?" | **Browse**: "Which stations close to Hbf are nearly empty?" (the region is an attribute specification; which stations is unknown) |
| **Location unknown** | **Locate**: "Where is Campus in today's capacity list?" | **Explore**: "Is there anything unusual in the data this week?" |

"Location" means where in the visualization the target sits: which item, or which range of an attribute.

### Query (low level): how much of the data?

| Action | Scope | Example |
|---|---|---|
| **Identify** | One target: inspect its characteristics | "How many bikes does Sontheim lose at 8 am?" |
| **Compare** | Some targets | "Do Hbf and Sontheim mirror each other?" |
| **Summarize** | All targets: an overview | "When is the network most imbalanced?" |

## 3. Targets

The aspect of the data the user is interested in, typically a noun in the task sentence.

| Scope | Target | Meaning | Example |
|---|---|---|---|
| All data | **Trends** | High-level pattern: increase, decrease, peak | Rentals rise in summer, fall in autumn |
| | **Outliers** | Items that don't fit | A week with a power outage of the rental system |
| | **Features** | Task- and domain-dependent structures of interest | The wine festival week that lifted rentals |
| One attribute | **Distribution** | How values spread | Trip duration is right-skewed |
| | **Extremes** | Minimum and maximum | Shortest and longest trips |
| Many attributes | **Dependency** | One attribute determines another | Price as a function of duration |
| | **Correlation** | Attributes vary together | Rentals vs. temperature |
| | **Similarity** | Items or attributes behave alike | Net flow by hour at Hbf and Markt |
| Network data | **Topology** | Structure, e.g. motifs: clique, star, cycle | Hbf links most stations (a star) |
| | **Paths** | Connections between two nodes | Truck route Sontheim → Hbf → Böckingen |
| Spatial data | **Shape** | Understanding or comparing shapes | Morning demand stretches along the river, evening demand is compact |

## 4. Verbs and nouns

- **Task verbs** describe what the user does: find, compare, check, see whether, rank, spot, track, prioritise. They map to actions.
- **Delivery verbs** only describe the output: show, display, plot, visualize, make a map or chart. Drop them: they name a solution, not a task.
- **Data nouns** name items or attributes on the data card: stations, trips, price, year.
- **Target nouns** name what the user looks for in that data: a trend, an outlier, the busiest, a pattern, neighbours. They map to targets.

## 5. Chained tasks

A complex goal is a **sequence of tasks**, where the output of one is the input of the next. Write it as a chain: "derive, then identify", "locate, then compare". Typical: derive an attribute first (change, net flow, rank), then search and query on it. Each link in the chain is a task with its own action and target; the chain as a whole is what the design must support.

## 6. Worked examples

### The solution-first trap (bike sharing)

The CTO says: "I want to optimize where and when we send out employees to balance stations. We have the current status of stations, and I want you to show me a map."

Taking the request literally gives a map of stations coloured by binned status, with zoom, pan and a filter. The CTO is happy, but the design answers the stated request, not the work. Looking at the data (a **dynamic** table with positions, current status and a predicted risk of running empty or full) and interviewing the staff who rebalance stations gives the real tasks:
- Find stations likely to be empty or full in the next 2 hours → **discover + outliers + predicted risk per station**, search *browse*, query *identify*.
- Rank and compare them by severity to prioritise visits → **present/discover + extremes + risk across stations**, query *compare*.
- Filter by area and inspect recent history → **browse + trends + bike count per station over time**, query *identify*.
- Underneath: **derive** `net flow = returns − rentals` per station and hour, **then discover** the recurring pattern that sets truck times.

These tasks lead to a station × hour heatmap of net flow (rows ordered to reveal spatial and temporal patterns) with a simplified map used only to filter by area: simpler than the map and more useful. "Show me a map" contained a delivery verb and a chart type; neither survived the abstraction.

### Used-car listings

Question: "Which cars are a **good deal** for their age?" Real need: the buyer wants a shortlist to call.
- Marked: **are** a good deal (task: judge) · _cars_ (data: listings) · _good deal_ (target) · _age_ (data: `year`).
- Abstract task: **discover + outliers + `price` relative to `year` within each `model`**, search *locate*, query *compare*.
- Missing data: needs the derived attribute *expected price per model and year*. The listings contain no condition data, so "good deal" can only mean "cheap for model and age"; record that limit.

### Same task, two domains

- A running coach asks "Which runner improved most this season?"; a biologist asks "Which gene changed most after treatment?". Both are **derive change, then identify + extremes**, and one idiom serves both: a sorted bar chart of the change.
- The biologist also asks "Which genes interact with gene X?": **locate X, then identify + network neighbours**. Same domain, different task, different idiom: a node-link diagram.

## 7. Other vocabularies

Munzner's terms are general. Where they are too coarse for the data, borrow from a specific taxonomy and say so:
- **Graph tasks** (Lee et al. 2006): adjacency, accessibility, common connection, …
- **Spatio-temporal tasks** (Andrienko & Andrienko 2006)
- **Multi-dimensional design space of tasks** (Schulz et al. 2013)
- Domain-specific taxonomies extend these where general terms are too coarse.
