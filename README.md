# viz-engineering-skills

Agent skills that design data visualizations the way a visualization researcher would, following Tamara Munzner's nested model (*Visualization Analysis and Design*): first who the chart is for and what they ask, then what the data is, then what the reader must do with it, and only then which marks, channels and colours to use. The skills are plain `SKILL.md` folders, so they work with Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode and any other agent that reads Agent Skills.

## Skills

| Skill | Block | What it does |
|---|---|---|
| [`viz-domain`](skills/viz-domain) | 1. Domain situation | Interviews you about stakeholders, their questions and the data; writes `docs/domain-situation.md`. |
| [`viz-data-abstract`](skills/viz-data-abstract) | 2. Data abstraction ("What?") | Types every attribute (categorical, ordinal, quantitative), dataset type, keys, derived attributes; writes `docs/data-abstraction.md`. |
| [`viz-task-abstract`](skills/viz-task-abstract) | 2. Task abstraction ("Why?") | Rewrites each domain question as an abstract `{action, target}` task. |
| [`viz-encoding`](skills/viz-encoding) | 3. Visual encoding ("How?") | Picks marks and channels with the expressiveness and effectiveness principles, Gestalt, Stevens and Weber. |
| [`viz-prototype`](skills/viz-prototype) | All blocks, autonomously | Builds 5 genuinely different, near-finished designs per question in one HTML page, a `decisions.md` recording every choice, and a local feedback loop where your ratings land in that file. |
| [`viz-iterate`](skills/viz-iterate) | Any block | Reworks an existing chart: reads the prototypes, their decisions and your ratings, infers what to change, and re-runs the earliest block the problem touches and every block after it. |

Typical flow: `viz-domain` → `viz-data-abstract` → `viz-task-abstract` → `viz-encoding`, or jump straight to `viz-prototype` to see options first, then `viz-iterate` until it works.

## Install

### Any agent (npx)

With the open [skills](https://github.com/vercel-labs/skills) CLI, which installs into Claude Code, Codex, Cursor, Gemini CLI, Copilot, OpenCode and others:

```bash
npx skills add JoaZaech/viz-engineering-skills
```

It asks which agents and skills to install, and whether to install for the project or globally. Add `--skill viz-prototype` to pick a single skill.

### Claude Code plugin

```
/plugin marketplace add JoaZaech/viz-engineering-skills
/plugin install viz-engineering-skills@viz-engineering-skills
```

### Manually

Copy the folders in [`skills/`](skills) into your agent's skills folder, for example:

```bash
git clone https://github.com/JoaZaech/viz-engineering-skills
cp -r viz-engineering-skills/skills/* ~/.claude/skills/      # Claude Code (or .claude/skills/ in a project)
cp -r viz-engineering-skills/skills/* .agents/skills/        # Codex and other agents that read .agents/skills
```

For claude.ai or the Claude desktop app, zip a skill folder (for example `viz-prototype/`) and upload it under Settings → Capabilities → Skills.

## Use

Ask in plain language; the agent picks the skill from its description:

- "Who is this chart for and what should it answer?" → `viz-domain`
- "What kind of data is `data.csv`?" → `viz-data-abstract`
- "Show me some options for visualizing Q2" → `viz-prototype`
- "Design 3 is close but too busy, improve it" → `viz-iterate`

Or call one by name, for example `/viz-prototype` in Claude Code.

## Requirements

`viz-prototype` builds its overview pages and runs a local feedback server with Python 3 and the [`markdown`](https://pypi.org/project/Markdown/) package (`pip install markdown`). The server binds to `127.0.0.1:8765` only. Prototype pages load one charting library from a CDN, so viewing them needs an internet connection. The other skills need nothing beyond the agent.

## Credits

The method and vocabulary follow Tamara Munzner, *Visualization Analysis and Design*, A K Peters/CRC Press, 2014. The figures in `skills/*/assets/` are taken or adapted from that book, its lecture material and other visualization literature (Roth's visual variables, Stevens' and Weber's laws) and remain the property of their authors; they are included for reference and attribution, not under this repository's MIT license. See the [book's page](https://www.cs.ubc.ca/~tmm/vadbook/) for terms of use.

## License

MIT for the skill text and code, see [LICENSE](LICENSE). Figures: see Credits.
