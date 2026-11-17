"""Serve the user's prototypes/ folder and write feedback clicks straight into each decisions.md.

    python <this skill folder>/scripts/serve.py [prototypes-dir] [--no-open]   # http://127.0.0.1:8765/

feedback.js POSTs {folder, designs} to /feedback on every click; this rewrites the current round's rows in
section "7. Feedback" of <folder>/decisions.md and reruns build.py. Local only (bound to 127.0.0.1).
"""
import functools, http.server, json, re, sys, webbrowser
from pathlib import Path

import build

ROOT = Path(next((a for a in sys.argv[1:] if not a.startswith("-")), "prototypes")).resolve()
PORT = 8765
RATINGS = {"closest", "keep", "drop"}
TAGS = {"Wrong chart type", "Hard to read", "Too busy", "Headline off", "Colours", "Missing context"}


def clean(payload):
    """Validate the browser's payload; raise ValueError on anything unexpected."""
    folder = payload.get("folder")
    if not (isinstance(folder, str) and re.fullmatch(r"[A-Za-z0-9_-]+", folder) and (ROOT / folder / "decisions.md").is_file()):
        raise ValueError("unknown folder")
    out = []
    for k, d in sorted((payload.get("designs") or {}).items(), key=lambda kv: int(kv[0]) if str(kv[0]).isdigit() else 99):
        if not (str(k).isdigit() and 1 <= int(k) <= 9 and isinstance(d, dict)):
            raise ValueError("bad design")
        rating = d.get("rating")
        tags = [t for t in d.get("tags") or [] if t in TAGS]
        if rating not in RATINGS:
            rating = None
        if rating or tags:
            name = re.sub(r"[|\n]", " ", str(d.get("name", "")))[:40]
            out.append((int(k), name, rating, tags))
    return folder, out


def record(folder, rows):
    p = ROOT / folder / "decisions.md"
    md = p.read_text()
    m = re.search(r"round (\d+)", md)
    rnd = m.group(1) if m else "1"
    sec = re.search(r"^## 7\. Feedback\n(.*?)(?=^## )", md, re.M | re.S)
    if not sec:
        raise ValueError("decisions.md has no '## 7. Feedback' section")
    body = sec.group(1)
    sep = re.search(r"^\|[-| ]+\|\n", body, re.M)
    if not sep:
        raise ValueError("feedback table header missing")
    table_end = sep.end()
    while table_end < len(body) and body[table_end] == "|":
        table_end = body.index("\n", table_end) + 1
    kept = [l for l in body[sep.end():table_end].splitlines() if not l.startswith(f"| {rnd} |")]  # replace this round's rows
    new = [f"| {rnd} | {k} {name} | {rating or ''} | {', '.join(tags)} |" for k, name, rating, tags in rows]
    table = "".join(l + "\n" for l in kept + new)
    body = body[:sep.end()] + table + body[table_end:]
    p.write_text(md[:sec.start(1)] + body + md[sec.end(1):])


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]
        if not (path.endswith("/") or path.endswith(".html")):
            return self.send_error(404)  # the user's folder is served as HTML pages only
        super().do_GET()

    def do_POST(self):
        if self.path != "/feedback":
            return self.send_error(404)
        try:
            n = int(self.headers.get("Content-Length", 0))
            if n > 20000:
                raise ValueError("payload too large")
            folder, rows = clean(json.loads(self.rfile.read(n)))
            record(folder, rows)
            build.main(ROOT)
        except (ValueError, json.JSONDecodeError) as e:
            return self.send_error(400, str(e))
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    # self-check of the table rewrite on a throwaway copy
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "x"; d.mkdir()
        (d / "decisions.md").write_text("Status | round 2.\n## 7. Feedback\n\n| Round | Design | Rating | Tags |\n|---|---|---|---|\n| 1 | 1 A | drop |  |\n\n## 8. Outcome\n")
        old, ROOT = ROOT, Path(t)
        record("x", [(2, "B", "closest", ["Too busy"])]); record("x", [(2, "B", "keep", [])])
        txt = (d / "decisions.md").read_text(); ROOT = old
        assert "| 1 | 1 A | drop |  |" in txt and "| 2 | 2 B | keep |  |" in txt and "closest" not in txt, txt
    build.main(ROOT)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Handler, directory=str(ROOT)))
    print(f"Prototype hub: http://127.0.0.1:{PORT}/  (Ctrl+C to stop)")
    if "--no-open" not in sys.argv:
        webbrowser.open(f"http://127.0.0.1:{PORT}/")
    srv.serve_forever()
