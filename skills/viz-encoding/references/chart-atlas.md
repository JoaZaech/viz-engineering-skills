# Chart Atlas

A plain listing of chart and diagram types, grouped into families, with the data each one takes and how it relates to other types. It contains **no recommendations**: it is a catalogue of candidates to look through. Whether a candidate fits a task is decided by describing it in marks and channels ([marks-channels.md](marks-channels.md)) and checking it against expressiveness and effectiveness ([viz-effectiveness.md](viz-effectiveness.md)).

Data is named with the terms of [data-types.md](../../viz-data-abstract/references/data-types.md): categorical (cat), ordinal (ord), quantitative (quant), time, positions, links. Families are grouped by what a chart is commonly used to show; a chart can appear in several families.

Adapted from *The Data Visualization Atlas* (generated with Claude).

## Contents

1. [Master list](#1-master-list)
2. [Comparison](#2-comparison)
3. [Distribution](#3-distribution)
4. [Composition (part-to-whole)](#4-composition-part-to-whole)
5. [Relationship and correlation](#5-relationship-and-correlation)
6. [Change over time](#6-change-over-time)
7. [Ranking](#7-ranking)
8. [Deviation](#8-deviation)
9. [Flow and process](#9-flow-and-process)
10. [Hierarchy](#10-hierarchy)
11. [Networks](#11-networks)
12. [Spatial and geographic](#12-spatial-and-geographic)
13. [Multivariate and high-dimensional](#13-multivariate-and-high-dimensional)
14. [Uncertainty](#14-uncertainty)
15. [Text](#15-text)
16. [Sets and overlaps](#16-sets-and-overlaps)
17. [Tables and single values](#17-tables-and-single-values)
18. [Conceptual and structural diagrams](#18-conceptual-and-structural-diagrams)
19. [Domain-specific charts](#19-domain-specific-charts)
20. [Transformations between charts](#20-transformations-between-charts)

---

## 1. Master list

```
Comparison ........ bar, column, grouped bar, back-to-back bar, bullet, radial bar, Marimekko,
                    dot plot (Cleveland), lollipop, dumbbell, pictogram, proportional symbol,
                    radar, small multiples
Distribution ...... histogram, density (KDE), ECDF, rug, Wilkinson dot plot, stem-and-leaf,
                    frequency polygon, box, violin, strip/jitter, beeswarm, ridgeline, raincloud,
                    letter-value (boxen), population pyramid, 2D histogram, hexbin, 2D density/contour,
                    joint/marginal plot
Composition ....... pie, donut, waffle, stacked bar, 100% stacked bar, treemap, mosaic/Marimekko,
                    waterfall, funnel, parliament; stacked area, 100% stacked area, streamgraph,
                    stacked column over time
Relationship ...... scatter, scatter with trend line, connected scatter, bubble, 3D scatter,
                    scatter plot matrix (SPLOM), ternary, correlation matrix, correlogram
Change over time .. line, step, area, smoothed line, sparkline, horizon; column over time, slope, bump;
                    calendar heatmap, radial line, seasonal subseries, cycle plot;
                    timeline, Gantt, swimlane timeline, event/spike plot; candlestick, OHLC
Ranking ........... ordered bar, ordered dot/lollipop, bump, slope, Pareto
Deviation ......... diverging bar, diverging stacked bar (Likert), surplus/deficit line, spine chart, waterfall
Flow and process .. Sankey, alluvial, chord, flow map, parallel sets; flowchart, swimlane, BPMN,
                    value stream map, state machine, PERT
Hierarchy ......... tree, dendrogram, radial tree, org chart, mind map; treemap, circle packing,
                    sunburst, icicle, Voronoi treemap
Networks .......... force-directed, arc, hive plot, radial network, edge bundling, adjacency matrix,
                    chord, NodeTrix
Spatial ........... choropleth, cartogram, tile grid map, bivariate choropleth; dot density,
                    proportional symbol map, pin map, density heat map; flow map, route map,
                    isoline/contour map; relief, raster, extruded (prism) map
Multivariate ...... parallel coordinates, radar, clustered heatmap, SPLOM, Andrews curves,
                    Chernoff faces, star/glyph plots, projections (PCA, t-SNE, UMAP, MDS), biplot
Uncertainty ....... error bars, confidence band, fan chart, gradient/density interval,
                    hypothetical outcome plots, quantile dot plot, forest plot, spaghetti plot
Text .............. word cloud, word tree, phrase net, theme river, annotated text, sentiment timeline
Sets .............. Venn, Euler, UpSet, radial sets / set matrix
Tables, values .... table, heat table, KPI card, gauge, progress bar/ring, bullet
Conceptual ........ UML, ER, C4/architecture, data flow; SWOT, 2×2 quadrant, fishbone, canvas, RACI,
                    journey map; concept map, mind map, affinity, cycle; floor plan, wireframe,
                    schematic, exploded view, cross-section
Domain-specific ... finance, statistics/ML, quality control, science, biology/medicine, project management
```

## 2. Comparison

| Chart | Data | Related |
|---|---|---|
| Bar / column | 1 cat + 1 quant | Base of comparison, composition, ranking and deviation charts; horizontal or vertical |
| Grouped (clustered) bar | 2 cat + 1 quant | Sibling of stacked bar: subgroups side by side instead of on top |
| Paired / back-to-back bar | 1 cat + 2 quant, mirrored | Generalizes to the population pyramid |
| Bullet chart | value, target, qualitative ranges | A bar plus reference markers; alternative form of a gauge |
| Radial bar | 1 cat + 1 quant | Polar transform of the bar chart |
| Marimekko (variable-width bar) | 2 cat + 1 quant | 100% stacked bar with variable widths |
| Dot plot (Cleveland) | 1 cat + 1 or more quant | Bar reduced to a point; parent of lollipop and dumbbell |
| Lollipop | 1 cat + 1 quant | Hybrid of bar and dot plot |
| Dumbbell (connected dot) | 1 cat + 2 quant (two states) | Slope chart shows the same data with time on the x-axis |
| Pictogram / isotype | counts | Unit chart; cousin of the waffle |
| Proportional symbol (bubble) | 1 cat + 1 quant | Bubble chart adds x/y position; proportional symbol map adds geography |
| Radar / spider | several quant attributes for few items | Polar version of parallel coordinates |
| Small multiples (trellis, facets) | any, split by a cat attribute | A technique, not a chart: the same chart repeated per subgroup with shared axes |

## 3. Distribution

| Chart | Data | Related |
|---|---|---|
| Histogram | 1 quant, binned | Bars over a binned quant axis; smoothed into a density plot |
| Density plot (KDE) | 1 quant | Smoothed histogram; mirrored becomes a violin, stacked becomes a ridgeline |
| Cumulative distribution (ECDF) | 1 quant | Integral of the density |
| Rug plot | 1 quant | 1D strip plot, often on a chart's margin |
| Stem-and-leaf / Wilkinson dot plot | 1 quant, small n | Text- or dot-based histogram |
| Frequency polygon | 1 quant, binned | Histogram drawn as a line |
| Box plot | 1 quant across 1 cat | Summary of the violin; extended into the letter-value (boxen) plot |
| Violin | 1 quant across 1 cat | Mirrored density, often with a box inside |
| Strip / jitter, beeswarm | 1 quant across 1 cat | Raw-point base of box and violin; beeswarm places points without overlap |
| Ridgeline (joy) | 1 quant across many groups or periods | Stacked density plots |
| Raincloud | 1 quant across groups | Half-violin + box + strip plot |
| Letter-value (boxen) | 1 quant across 1 cat | Box plot with more quantile levels |
| Population pyramid | ord bins × 2 groups | Back-to-back histogram |
| 2D histogram, hexbin, 2D density / contour | 2 quant, many points | Binned or smoothed scatter plot; contour links to isoline maps |
| Joint / marginal plot | 2 quant | Scatter in the centre, univariate distributions on the margins |

## 4. Composition (part-to-whole)

| Chart | Data | Related |
|---|---|---|
| Pie | 1 cat + 1 quant summing to a whole | Polar transform of a single 100% stacked bar |
| Donut | as pie | Pie with a hole; nested donuts become a sunburst |
| Waffle | proportions | Grid of units; cousin of pie and pictogram |
| Stacked bar (absolute) / 100% stacked bar | 2 cat + 1 quant | Grouped bar is its side-by-side sibling; 100% stacked bar is an unrolled pie |
| Mosaic / Marimekko | 2 cat + 1 quant | 100% stacked bar with variable widths; a two-level treemap |
| Waterfall | sequential additive contributions | Floating bars; also a deviation chart |
| Funnel | ordered stages + values | Centred bar chart; Sankey shows where the drop-off goes |
| Parliament (semicircle) | counts of discrete units by cat | Waffle arranged on a half-donut |
| Stacked area / 100% stacked area / streamgraph | time + 1 cat + 1 quant | Line chart with stacked, filled layers; streamgraph centres the baseline |
| Stacked column over time | time + 1 cat + 1 quant | Stacked bar on a time axis |

## 5. Relationship and correlation

| Chart | Data | Related |
|---|---|---|
| Scatter | 2 quant | Base of the family; binned into hexbin/2D histogram; size added → bubble; time order added → connected scatter |
| Scatter with trend / regression line | 2 quant | Often with a confidence band and a residual plot |
| Connected scatter | 2 quant + time order | Hybrid of scatter and line chart |
| Bubble | 3 quant (x, y, size) + optional cat | Scatter + proportional symbol |
| 3D scatter | 3 quant | Alternatives in 2D: SPLOM, bubble |
| Scatter plot matrix (SPLOM) | n quant | Small multiples of scatter plots |
| Ternary | 3 proportions summing to 1 | Both a composition and a relationship chart |
| Correlation matrix / correlogram | pairwise coefficients of n quant | Heatmap of a correlation matrix; condensed SPLOM |

## 6. Change over time

| Chart | Data | Related |
|---|---|---|
| Line | time + 1 quant (+ cat for several lines) | Filled → area; stepped → step chart; tiny → sparkline |
| Step | time + values changing at discrete moments | Line with horizontal holds |
| Area | time + 1 quant | Line filled to the baseline; stacked → stacked area |
| Spline / smoothed line | time + 1 quant | Smoothed line |
| Sparkline | time series, minimal | Stripped-down line chart |
| Horizon | many time series | Area chart sliced into bands and folded, with colour |
| Column over time | time + 1 quant | Bar chart on a time axis |
| Slope | 2 time points × cat | Line with only two points; horizontal cousin of the dumbbell |
| Bump | rank over time | Line chart of ranks |
| Calendar heatmap | daily values | Heatmap on a calendar grid |
| Radial / polar line, seasonal subseries, cycle plot | cyclic time series | Line wrapped onto a circle or split by season |
| Timeline | events with dates | One-dimensional event plot |
| Gantt / swimlane timeline | tasks with start, end (+ dependencies) | Floating bars on a time axis; PERT shows the dependencies as a network |
| Event / spike plot | event times | Marks on a time axis |
| Candlestick / OHLC | open, high, low, close per period | Box-like glyph on a time axis |

## 7. Ranking

| Chart | Data | Related |
|---|---|---|
| Ordered bar / dot / lollipop | 1 cat + 1 quant, sorted | Sorted versions of the comparison charts |
| Bump | rank over time | Line chart of ranks |
| Slope | two rankings or two time points | See change over time |
| Pareto | cat sorted by frequency + cumulative % | Ordered bar + cumulative line |

## 8. Deviation

| Chart | Data | Related |
|---|---|---|
| Diverging bar | 1 cat + 1 signed quant | Bar chart centred on a reference |
| Diverging stacked bar (Likert) | ordinal survey scales | 100% stacked bar centred on neutral |
| Surplus / deficit filled line | time series vs baseline | Area chart coloured by sign |
| Spine chart | indicators vs a reference distribution | Diverging bar with range bands |
| Waterfall | sequential contributions | See composition |

## 9. Flow and process

| Chart | Data | Related |
|---|---|---|
| Sankey | source, target, magnitude (multi-stage) | Width-encoded flow; generalizes the funnel |
| Alluvial / parallel sets | cat attributes across stages or dimensions | Sankey with fixed columns; parallel coordinates for categorical data |
| Chord | matrix of flows between entities | Circular adjacency matrix; circular Sankey |
| Flow map | origin, destination, magnitude, positions | Sankey on a map |
| Flowchart, swimlane, BPMN, value stream map | steps, decisions, actors | Directed graphs with semantic shapes; swimlanes add actor lanes |
| State machine | states and transitions | Directed graph; a UML diagram |
| PERT / network schedule | tasks with dependencies | Gantt drawn as a directed acyclic graph |

## 10. Hierarchy

Two branches: **node-link** (structure drawn as links) and **space-filling** (enclosure or adjacency).

| Chart | Data | Related |
|---|---|---|
| Tree diagram (tidy tree) | tree | Base of the family |
| Dendrogram | tree with leaves aligned; branch height = distance | Output of hierarchical clustering; often attached to heatmaps |
| Radial tree | tree | Polar transform of the tree |
| Org chart | tree of people and reporting lines | Domain-specific tree |
| Mind map | free tree around a central idea | Informal radial tree |
| Treemap | tree + quant size | Nested rectangles; recursive Marimekko |
| Circle packing | tree + quant size | Treemap with nested circles |
| Sunburst | tree + quant size | Polar icicle; nested donut |
| Icicle / partition | tree + quant size | Cartesian sunburst; nested stacked bars |
| Voronoi treemap | tree + quant size | Treemap with Voronoi cells |

## 11. Networks

| Chart | Data | Related |
|---|---|---|
| Force-directed graph | nodes + links | Node-link layout from simulated forces |
| Arc diagram | nodes on a line + links as arcs | 1D layout of a network; unwrapped chord |
| Hive plot | nodes assigned to axes by attribute | Axis-based node-link layout |
| Radial network | nodes on a circle + links | Wrapped arc diagram |
| Hierarchical edge bundling | network + a hierarchy over nodes | Radial tree + network links |
| Adjacency matrix | nodes + (weighted) links | Heatmap of connections; chord is its circular form |
| Chord | weighted links between few entities | Between flow and network families |
| NodeTrix | network with dense clusters | Node-link + matrix hybrid |

Node-link and matrix are two views of the same graph.

## 12. Spatial and geographic

| Chart | Data | Related |
|---|---|---|
| Choropleth | regions (geometry) + 1 quant or cat | Heatmap on a map |
| Cartogram (contiguous, Dorling, Demers) | regions + 1 quant (as size) | Region size distorted by value |
| Hexbin / tile grid map | regions as equal tiles + 1 quant | Cartogram with equal sizes |
| Bivariate choropleth | regions + 2 quant | 2D colour scheme on a map |
| Dot density map | positions, one dot = N units | Strip plot or waffle on a map |
| Proportional symbol map | positions + 1 quant | Bubble chart on a map |
| Pin / marker map | positions of discrete items | Points on a map |
| Density heat map | positions, smoothed | 2D density on a map |
| Flow map | origin–destination + magnitude | Sankey on a map |
| Route / connection map | paths between positions | Lines on a map |
| Isoline / contour map | field (grid) of quant values | Contour plot on a map |
| Topographic / relief, raster, extruded (prism) map | field or regions + quant | Surface or 3D representations |

## 13. Multivariate and high-dimensional

| Chart | Data | Related |
|---|---|---|
| Parallel coordinates | n quant for many items | Unrolled radar; categorical version is parallel sets |
| Heatmap (clustered) | matrix: 2 cat or binned axes + 1 quant | Becomes correlation matrix, calendar heatmap, adjacency matrix, confusion matrix, heat table; clustered heatmap adds dendrograms |
| Scatter plot matrix | n quant | See relationship |
| Star / glyph plots, Chernoff faces | n attributes per item in one small shape | Small multiples of radar charts (star plot) |
| Andrews curves | n quant mapped to Fourier series | Smooth relative of parallel coordinates |
| Projections (PCA, t-SNE, UMAP, MDS) | high-dimensional data reduced to 2D | Output is a scatter plot |
| Biplot | projection + variable loadings | Scatter with loading arrows |

## 14. Uncertainty

| Chart | Data | Related |
|---|---|---|
| Error bars | estimate + interval | Added to bar, dot or scatter |
| Confidence band / ribbon | interval over x | Area around a line |
| Fan chart | forecast with nested intervals | Several stacked ribbons |
| Gradient / density interval | full distribution per estimate | Violin squashed into a bar |
| Quantile dot plot | discrete outcomes from a distribution | Wilkinson dot plot of quantiles |
| Hypothetical outcome plots (HOPs) | sampled outcomes, animated | Animated small multiples |
| Forest plot | effect sizes + intervals across studies | Dot plot with error bars |
| Spaghetti plot | ensemble of simulations | Many-line chart |

## 15. Text

| Chart | Data | Related |
|---|---|---|
| Word cloud | term frequencies | Proportional symbols for words |
| Word tree | phrases following a word | Tree diagram of text |
| Phrase net | word pairs | Network of words |
| Theme river | topics over time | Streamgraph of topics |
| Sentiment timeline | tone over time | Line or diverging area |
| Annotated text | text + highlighted passages | Colour encoding on text |

## 16. Sets and overlaps

| Chart | Data | Related |
|---|---|---|
| Venn diagram | set membership, all intersections drawn | Conceptual diagram |
| Euler diagram | set membership, only existing intersections, optionally area-proportional | Generalized Venn |
| UpSet plot | membership in many sets, intersection sizes | Bar chart + membership matrix |
| Radial sets / set matrix | many overlapping sets | Matrix or chord-like layout |

## 17. Tables and single values

| Chart | Data | Related |
|---|---|---|
| Table / data grid | any | No graphic encoding |
| Heat table | table + colour by value | Table × heatmap |
| KPI card / big number | one value, often + sparkline and delta | Text + sparkline |
| Gauge / speedometer | one value vs a range | Pie segment; bullet chart is a linear form |
| Progress bar / ring | completion share | Single 100% stacked bar or donut |

## 18. Conceptual and structural diagrams

These show ideas, structures or systems rather than measured data, mostly built from node-link and hierarchy layouts plus semantic shapes.

```
Software and data ... UML (class, sequence, activity, use case, component, state), ER diagram,
                      C4 / architecture, data flow diagram, network topology
Business ............ SWOT matrix, 2×2 quadrant, fishbone (Ishikawa), business model canvas,
                      RACI matrix, customer journey map, pyramid / layered diagram
Thinking ............ concept map, mind map, affinity diagram, cycle diagram, Venn
Physical, layout .... floor plan, wireframe / mockup, circuit schematic, exploded view, cross-section
```

## 19. Domain-specific charts

| Domain | Charts | Related |
|---|---|---|
| Finance | candlestick, OHLC, Kagi, Renko, point-and-figure, waterfall, Marimekko | Candlestick: box-like glyph on time; Kagi/Renko/point-and-figure ignore time |
| Statistics, ML | Q-Q, P-P, residual plot, ROC, precision-recall, lift/gain, confusion matrix, Bland-Altman, funnel plot (meta-analysis) | Mostly scatter or line plots in metric space; confusion matrix is a heatmap |
| Quality control | control chart (Shewhart), run chart, Pareto | Control chart: line + limit bands |
| Science, engineering | spectrogram, polar plot / wind rose, phase diagram, ternary, Smith chart, nomogram, Hertzsprung-Russell | Spectrogram: heatmap of frequency × time; wind rose: radial bar |
| Biology, medicine | Kaplan-Meier, Manhattan plot, volcano plot, phylogenetic tree, genome browser | Kaplan-Meier: step chart; Manhattan and volcano: scatter; phylogenetic tree: dendrogram |
| Project management | Gantt, PERT, burndown / burnup, cumulative flow, Kanban board | Burndown: line; cumulative flow: stacked area |

## 20. Transformations between charts

Many charts are the same data in a different coordinate system, layout or level of aggregation. Each row is one transformation.

### Cartesian ⟷ polar

| Cartesian | Polar |
|---|---|
| Bar | Radial bar, Nightingale (coxcomb) rose |
| 100% stacked bar | Pie, donut |
| Icicle | Sunburst |
| Tree | Radial tree |
| Line | Radial line |
| Parallel coordinates | Radar |
| Arc diagram | Chord, radial network |
| Histogram of directions | Wind rose |

### Node-link ⟷ matrix

| Node-link | Matrix |
|---|---|
| Network | Adjacency matrix |
| Chord | Flow matrix |
| Venn | UpSet membership matrix |
| Sankey | Origin–destination table |

### Raw ⟷ binned ⟷ summarized ⟷ smoothed

| Raw | Binned | Summarized | Smoothed |
|---|---|---|---|
| Strip plot | Histogram | Box plot | Density, violin |
| Scatter | Hexbin | Regression line | 2D density, contour |
| Dot map | Choropleth | Value per region | Density heat map |

### Static ⟷ over time

| Snapshot | Over time |
|---|---|
| Bar | Line, bump |
| Pie, 100% stacked bar | 100% stacked area |
| Stacked bar | Stacked area, streamgraph |
| Scatter | Connected scatter, animated bubble |
| Histogram | Ridgeline |
| Sankey (one period) | Alluvial (several periods) |
| Choropleth | Small-multiple maps, animated map |

### Abstract ⟷ geographic

| Abstract | On a map |
|---|---|
| Heatmap | Choropleth |
| Bubble | Proportional symbol map |
| Strip / dot plot | Dot density map |
| 2D density | Density heat map |
| Sankey | Flow map |
| Contour plot | Isoline map |
| Equal-tile grid | Hexbin / tile map |

### Derivations from the bar chart

```
Bar ── sort ─────────────── ordered bar ── + cumulative line ── Pareto
    ── split, side by side ─ grouped bar
    ── split, on top ─────── stacked bar ── normalize ── 100% stacked bar ── polar ── pie ── donut ── sunburst
                                                                         ── variable width ── Marimekko ── recurse ── treemap
                                                                         ── centre on neutral ── diverging stacked (Likert)
                                                                         ── as units ── waffle
                                         ── over time ── stacked column ── stacked area ── streamgraph
    ── float ────────────── waterfall · Gantt (on time) · range bar ── candlestick
    ── centre on zero ───── diverging bar
    ── mirror two groups ── back-to-back bar ── population pyramid
    ── reduce to a point ── dot plot ── lollipop · dumbbell
    ── bin a quant axis ─── histogram ── density ── violin · ridgeline
    ── add target marks ─── bullet
    ── polar ────────────── radial bar ── wind rose
    ── centre and shrink ── funnel
    ── icons ────────────── pictogram
```

### Derivations from the scatter plot

```
Scatter ── add size ────────── bubble ── on a map ── proportional symbol map
        ── connect in time ─── connected scatter
        ── add model line ──── regression plot ── residual plot
        ── bin ─────────────── 2D histogram · hexbin ── heatmap
        ── smooth ──────────── 2D density ── contour ── isoline map
        ── all pairs ───────── SPLOM ── correlation matrix
        ── project ─────────── PCA / t-SNE / UMAP ── biplot
        ── one axis cat ────── strip/jitter ── beeswarm ── box ── boxen
                                                      ── violin ── raincloud
        ── one axis only ───── rug · Wilkinson dot plot ── quantile dot plot
```

### Derivations from the line chart

```
Line ── fill ──────────── area ── stacked area ── streamgraph · theme river
                               ── band and fold ── horizon
     ── hold values ───── step ── Kaplan-Meier
     ── shrink ────────── sparkline ── KPI card
     ── two points ────── slope
     ── plot ranks ────── bump
     ── add interval ──── confidence band ── fan chart
     ── many runs ─────── spaghetti plot
     ── wrap on circle ── radial line · seasonal plot
     ── one axis per attribute ── parallel coordinates ── radar (polar) · parallel sets (cat)
     ── control limits ── control chart
```

### Derivations from the heatmap (grid)

```
Heatmap ── correlations ──── correlation matrix
        ── connections ───── adjacency matrix ── chord (circular)
        ── days as cells ─── calendar heatmap
        ── predicted × actual ── confusion matrix
        ── numbers inside ── heat table
        ── reorder + cluster ── clustered heatmap (+ dendrograms)
        ── frequency × time ── spectrogram
        ── geographic cells ── choropleth · tile grid map ── cartogram
```

### Derivations from the node-link diagram

```
Node-link ── no cycles, one root ── tree ── dendrogram ── phylogenetic tree
                                         ── radial tree ── mind map
                                         ── org chart · word tree
                                         ── space-filling: icicle ── sunburst · treemap · circle packing · Voronoi treemap
          ── general graph ──────── force-directed ── arc diagram ── radial network
                                                    ── hive plot · edge bundling
          ── weighted, directed, staged ── Sankey ── alluvial ── flow map
          ── with semantics ─────── flowchart ── swimlane · BPMN · UML · ER · state machine
                                    ── with time ── PERT ── Gantt
```
