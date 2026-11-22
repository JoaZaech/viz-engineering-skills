"""Build the prototype pages in the user's prototypes/ folder (default: ./prototypes).

    python <this skill folder>/scripts/build.py [prototypes-dir]

- inlines feedback.js (next to this script) into every <folder>/index.html, so the pages stay self-contained;
- writes <folder>/decisions.html (one prototype) and compare.html (all side by side) from each decisions.md.
The .md files stay the source of truth; rerun after any decisions.md or index.html change.
Only .html and .md files are written into the prototypes folder.
"""
import re, sys
from pathlib import Path

import markdown

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else "prototypes").resolve()
FEEDBACK = Path(__file__).resolve().parent / "feedback.js"
MARK = re.compile(r"<script>/\* vi[sz]-feedback \*/.*?</script>|<script src=\"\.\./feedback\.js\"></script>", re.S)
BLOCKS = [("1.", "Domain"), ("2.", "Data"), ("3.", "Task"), ("4.", "Encoding"), ("5.", "Build")]
CSS = """
:root{--ink:#1c1c1a;--muted:#6b6b66;--line:#e6e5e1;--doc:#c9c7c0;--data:#7a9cc6;--assumed:#e0a526;--user:#3f9a5b}
*{box-sizing:border-box}body{margin:0;background:#fafaf9;color:var(--ink);font:14px/1.5 'IBM Plex Sans',system-ui,sans-serif}
main{padding:20px 24px 48px}.cols{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(340px,1fr);gap:24px;overflow-x:auto}
.one{max-width:760px;margin:0 auto}
h1{font-size:22px;font-weight:600;margin:0 0 16px;line-height:1.3}h2{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:18px 0 4px}
ul{list-style:none;margin:0;padding:0}li{padding:3px 0 3px 14px;position:relative}
li:before{content:"";position:absolute;left:0;top:10px;width:7px;height:7px;border-radius:50%;background:var(--doc)}
li.data:before{background:var(--data)}li.assumed:before{background:var(--assumed)}li.user:before{background:var(--user)}li.assumed{background:#fdf6e6}
.n{color:var(--muted);font-size:11px;margin-right:4px}.p{display:block;color:var(--muted);font-size:12px}
.check li:before{background:var(--assumed)}.key{color:var(--muted);font-size:12px;margin:0 0 12px}
.key i{display:inline-block;width:7px;height:7px;border-radius:50%;margin:0 4px 0 10px}
code{font-size:11px;background:#f1f0ed;padding:0 3px;border-radius:3px}a{color:inherit}
"""
KEY = ('<p class="key">Source:<i style="background:var(--assumed)"></i>assumed by Claude, check these'
       '<i style="background:var(--doc)"></i>from your docs<i style="background:var(--data)"></i>read from the data<i style="background:var(--user)"></i>confirmed by you</p>')
PAGE = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>{title}</title><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">'
        '<style>{css}</style></head><body><main>{body}</main></body></html>')


def sections(md):
    parts = re.split(r"^## ", md, flags=re.M)
    return {p.split("\n", 1)[0]: p.split("\n", 1)[-1] for p in parts[1:]}


def block(secs, prefix):
    return next((v for k, v in secs.items() if k.startswith(prefix)), "")


def rows(text):
    return [[c.strip() for c in l.strip().strip("|").split("|")] for l in text.splitlines()
            if l.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", l)]


def inline(s):
    return markdown.markdown(s).removeprefix("<p>").removesuffix("</p>")


def source(cell):
    m = re.match(r"^\**(doc|data|assumed|user)\b", cell, re.I)
    return m.group(1).lower() if m else "assumed"  # an unknown label is a claim nobody checked


def decisions(text):
    """Rows like | P5 | decision | source | -> (id, text, source)."""
    return [(r[0], r[1], source(r[-1])) for r in rows(text) if re.fullmatch(r"P\d+", r[0]) and len(r) >= 3]


def designs(text):
    t = rows(text)
    head = next((r for r in t if len(r) > 1 and r[1] == "Design"), None)
    return [dict(zip(head, r)) for r in t if head and re.fullmatch(r"[1-9]", r[0]) and len(r) == len(head)]


def overview(folder, link=False):
    md = (folder / "decisions.md").read_text()
    secs = sections(md)
    title = re.search(r"^# (.+)", md, re.M).group(1).replace("Prototype decisions: ", "")
    h = f'<a href="{folder.name}/decisions.html">{title}</a>' if link else title
    out = [f"<section><h1>{h}</h1>"]
    todo = [l[6:] for l in block(secs, "6.").splitlines() if l.startswith("- [ ]")]
    if todo:
        out.append('<h2>Check first</h2><ul class="check">' + "".join(f"<li>{inline(t)}</li>" for t in todo) + "</ul>")
    for pre, name in BLOCKS:
        text = block(secs, pre)
        items = []
        if pre == "4.":
            for d in designs(text):
                pr = d.get("Principles", "")
                items.append(f'<li><span class="n">{d["#"]}</span><b>{inline(d.get("Design", ""))}</b>: {inline(d.get("Trade-off", ""))}'
                             + (f'<span class="p">{inline(pr)}</span>' if pr else "") + "</li>")
        items += [f'<li class="{s}"><span class="n">{i}</span>{inline(t)}</li>' for i, t, s in decisions(text)]
        if items:
            out.append(f"<h2>{name}</h2><ul>{''.join(items)}</ul>")
    fb = [r for r in rows(block(secs, "7.")) if r and r[0].isdigit()]
    if fb:
        out.append("<h2>Your feedback</h2><ul>" + "".join(
            f'<li class="user"><span class="n">round {r[0]}</span><b>{r[1]}</b>: {" · ".join(x for x in r[2:] if x)}</li>' for r in fb) + "</ul>")
    return "".join(out) + "</section>"


def inline_feedback(page):
    """Replace the old <script src> or a previous inline copy with the current feedback.js, before </body>."""
    s = page.read_text()
    tag = "<script>/* viz-feedback */\n" + FEEDBACK.read_text() + "</script>"
    s = MARK.sub("", s)
    i = s.rindex("</body>")
    page.write_text(s[:i] + tag + s[i:])


CMP_CSS = """
.blk{margin:0 0 28px}.blk>h2{font-size:16px;letter-spacing:0;text-transform:none;color:var(--ink);margin:0 0 2px}
.blk>.sub{color:var(--muted);font-size:12px;margin:0 0 10px}
.grid{display:grid;grid-template-columns:repeat(var(--n),minmax(220px,1fr));gap:12px}
.cell{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.cell h3{font-size:12px;margin:0 0 6px}.cell ul{font-size:12px}.cell li{padding:2px 0 2px 14px}
.bar{display:flex;height:8px;border-radius:4px;overflow:hidden;background:#eee;margin:2px 0 4px}
.bar span{display:block}.cnt{font-size:11px;color:var(--muted);margin-bottom:6px}
.chip{display:inline-block;font-size:11px;padding:1px 8px;border-radius:999px;background:#f1f0ed;margin:2px 4px 0 0}
.task{font-weight:600;background:#e8eef7}
.row{display:grid;grid-template-columns:150px repeat(5,minmax(0,1fr));gap:10px;align-items:start;margin-bottom:14px}
.row>b{font-size:12px;padding-top:4px}
.th{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.th:hover{border-color:#1c1c1a}.fr{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;background:#fafaf9}
.fr iframe{position:absolute;top:0;left:0;width:1440px;height:810px;border:0;transform-origin:0 0;pointer-events:none}
.th .meta{padding:6px 8px;font-size:12px}.th .meta b{display:block}
.r{font-size:11px;font-weight:600;padding:1px 7px;border-radius:999px;margin-left:4px}
.r.closest{background:#1c1c1a;color:#fff}.r.keep{background:#cfe8d6}.r.drop{background:#f3c9d0}
"""


def plain(s, n=110):
    s = re.sub(r"[*`]", "", s)
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"


def counts_bar(text):
    c = {"assumed": 0, "doc": 0, "data": 0, "user": 0}
    for _, _, src in decisions(text):
        c[src] += 1
    tot = sum(c.values()) or 1
    bar = "".join(f'<span style="width:{100 * v / tot:.0f}%;background:var(--{k})"></span>' for k, v in c.items() if v)
    return f'<div class="bar">{bar}</div><div class="cnt">' + " · ".join(f"{v} {k}" for k, v in c.items() if v) + "</div>"


def assumed_list(text):
    a = [(i, t) for i, t, src in decisions(text) if src == "assumed"]
    return "<ul>" + "".join(f'<li class="assumed" title="{html_attr(t)}"><span class="n">{i}</span>{plain(t)}</li>' for i, t in a) + "</ul>" if a else ""


def html_attr(s):
    return re.sub(r"[*`]", "", s).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def feedback_of(secs):
    out = {}
    for r in rows(block(secs, "7.")):
        if r and r[0].isdigit() and r[1][:1].isdigit():
            out[r[1].split()[0]] = r[2]  # later rounds overwrite earlier ones
    return out


def compare(folders):
    data = []
    for f in folders:
        md = (f / "decisions.md").read_text()
        secs = sections(md)
        q = re.search(r"^# (.+)", md, re.M).group(1).replace("Prototype decisions: ", "")
        qid = re.search(r"Q\d", q)
        data.append((f, secs, q, qid.group(0).lower() if qid else f.name))
    n = len(data)

    def cells(fn):
        return f'<div class="grid" style="--n:{n}">' + "".join(f'<div class="cell"><h3>{q}</h3>{fn(secs)}</div>' for f, secs, q, _ in data) + "</div>"

    def task(secs):
        t = block(secs, "3.")
        main_rows = [d for d in decisions(t) if "main task" in d[1].lower()] or decisions(t)[:1]
        chips = re.findall(r"\{([^}]+)\}", main_rows[0][1]) if main_rows else []
        return "".join(f'<span class="chip task">{{{c}}}</span>' for c in chips) + counts_bar(t) + assumed_list(t)

    out = [KEY,
           '<section class="blk"><h2>1 · Domain situation</h2><p class="sub">Who it is for and which question each prototype answers.</p>',
           cells(lambda s: counts_bar(block(s, "1.")) + assumed_list(block(s, "1."))), "</section>",
           '<section class="blk"><h2>2 · Data abstraction</h2><p class="sub">Windows, groupings, derived attributes. Orange lines are Claude\'s assumptions.</p>',
           cells(lambda s: counts_bar(block(s, "2.")) + assumed_list(block(s, "2."))), "</section>",
           '<section class="blk"><h2>2 · Task abstraction</h2><p class="sub">The main task as {action, target}.</p>', cells(task), "</section>",
           '<section class="blk"><h2>3 · Encoding / interaction idiom</h2><p class="sub">The five designs per question. Chips name the principles applied; click a design to open it.</p>']
    for f, secs, q, qid in data:
        fb = feedback_of(secs)
        cards = []
        for d in designs(block(secs, "4.")):
            k = d["#"]
            chips = sorted({p.split(":")[0].strip().split(" ")[0] for p in d.get("Principles", "").split(";") if p.strip()})
            r = fb.get(k, "")
            cards.append(f'<a class="th" target="_top" href="index.html#{qid}/{k}" title="{html_attr(d.get("Trade-off", ""))}">'
                         f'<div class="fr"><iframe loading="lazy" tabindex="-1" src="{f.name}/index.html?thumb#{k}"></iframe></div>'
                         f'<div class="meta"><b>{k} · {plain(d.get("Design", ""), 40)}{f" <span class=r {r}>{r}</span>" if r else ""}</b>'
                         + "".join(f'<span class="chip">{c}</span>' for c in chips) + "</div></a>")
        out.append(f'<div class="row"><b><a href="{f.name}/decisions.html">{q}</a>{counts_bar(block(secs, "4."))}</b>{"".join(cards)}</div>')
    out += ["</section>",
            '<section class="blk"><h2>4 · Algorithm / build</h2><p class="sub">Library, layout and rendering choices.</p>',
            cells(lambda s: counts_bar(block(s, "5.")) + assumed_list(block(s, "5."))), "</section>",
            # scale each thumbnail iframe to its card width
            '<script>function fit(){document.querySelectorAll(".fr").forEach(d=>d.firstChild.style.transform=`scale(${d.clientWidth/1440})`)}'
            'addEventListener("resize",fit);fit();</script>']
    return "".join(out)


def main(root=None):
    global ROOT
    ROOT = Path(root).resolve() if root else ROOT
    for page in sorted(ROOT.glob("*/index.html")):
        inline_feedback(page)
    folders = sorted(p.parent for p in ROOT.glob("*/decisions.md"))
    for f in folders:
        (f / "decisions.html").write_text(PAGE.format(title=f.name, css=CSS, body=f'<div class="one">{KEY}{overview(f)}</div>'))
    (ROOT / "compare.html").write_text(PAGE.format(title="Compare prototypes", css=CSS + CMP_CSS, body=compare(folders)))
    for f in folders:
        assert len(designs(block(sections((f / "decisions.md").read_text()), "4."))) == 5, f"{f.name}: expected 5 designs"
    print("built", ", ".join(f.name for f in folders), "+ compare.html")


if __name__ == "__main__":
    main()
