// Feedback pill for viz-prototype pages; build.py inlines this file into every prototype index.html. Needs the page globals D, cur and show(i).
// Feedback lives in localStorage; "Export" downloads feedback-<folder>.json for Claude to record in decisions.md.
(() => {
  // ?thumb = thumbnail mode for compare.html: chart only, no header, captions, nav or feedback
  if (new URLSearchParams(location.search).has("thumb")) {
    const st = document.createElement("style");
    st.textContent = "header,nav,.cap,.sub,#fb{display:none!important}main{padding:12px 20px!important}";
    document.head.append(st);
    return;
  }
  const dir = decodeURIComponent(location.pathname.split("/").slice(-2, -1)[0] || "prototype");
  const KEY = "viz-feedback:" + dir;
  const RATINGS = [["closest", "★ Closest"], ["keep", "Keep"], ["drop", "Drop"]];
  const TAGS = ["Wrong chart type", "Hard to read", "Too busy", "Headline off", "Colours", "Missing context"];
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; } };
  const live = location.protocol.startsWith("http"); // served by serve.py: every click is written to decisions.md
  let status = live ? "Saved to decisions.md" : "";
  const save = s => {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch {}
    if (live) fetch("/feedback", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ folder: dir, designs: s }) })
      .then(r => { status = r.ok ? "Saved to decisions.md" : "Not saved"; render(); }, () => { status = "Not saved: is serve.py running?"; render(); });
  };
  let st = load(), tagsOpen = false;

  const css = document.createElement("style");
  css.textContent = `
  #fb{position:fixed;right:24px;bottom:24px;z-index:10;display:flex;flex-direction:column;align-items:flex-end;gap:6px;font:500 12px Inter,system-ui,sans-serif}
  #fb .row{display:flex;gap:4px;padding:5px;background:#fff;border:1px solid #e6e5e1;border-radius:999px;box-shadow:0 6px 24px rgba(0,0,0,.08)}
  #fb .tags{flex-wrap:wrap;justify-content:flex-end;max-width:360px;border-radius:14px}
  #fb button{font:inherit;border:0;background:transparent;color:#6b6b66;padding:6px 11px;border-radius:999px;cursor:pointer;white-space:nowrap}
  #fb button:hover{background:#f1f0ed;color:#1c1c1a}
  #fb button[aria-pressed=true]{background:#1c1c1a;color:#fff}
  #fb button.drop[aria-pressed=true]{background:#c4314b}
  #fb .lbl{align-self:center;color:#6b6b66;padding:0 6px}
  @media (max-width:1100px){#fb{bottom:84px}}`;
  document.head.append(css);
  const box = document.createElement("div"); box.id = "fb"; box.setAttribute("aria-label", "Feedback");
  document.body.append(box);

  function btn(label, pressed, onclick, cls) {
    const b = document.createElement("button"); b.textContent = label; b.className = cls || "";
    b.setAttribute("aria-pressed", pressed); b.onclick = e => { e.stopPropagation(); onclick(); }; return b;
  }
  function set(i, f) { const k = String(i + 1); st[k] = { name: D[i].short, ...st[k] }; f(st[k]); st[k].t = new Date().toISOString(); save(st); render(); }
  function render() {
    box.innerHTML = "";
    const i = cur;
    if (i >= 0) {
      const d = st[String(i + 1)] || {}, tags = new Set(d.tags || []);
      const r = document.createElement("div"); r.className = "row";
      r.append(Object.assign(document.createElement("span"), { className: "lbl", textContent: `Design ${i + 1}` }));
      RATINGS.forEach(([v, l]) => r.append(btn(l, d.rating === v, () => {
        const next = d.rating === v ? undefined : v;
        if (next === "closest") for (const k in st) if (st[k].rating === "closest") st[k].rating = undefined; // only one closest
        set(i, x => x.rating = next);
      }, v)));
      const t = document.createElement("div"); t.className = "row tags";
      TAGS.forEach(tag => t.append(btn(tag, tags.has(tag), () => set(i, x => {
        const s = new Set(x.tags || []); s.has(tag) ? s.delete(tag) : s.add(tag); x.tags = [...s];
      }))));
      r.append(btn(`Issues${tags.size ? " (" + tags.size + ")" : ""} ${tagsOpen ? "▾" : "▴"}`, tagsOpen, () => { tagsOpen = !tagsOpen; render(); }));
      if (tagsOpen) box.append(t);
      box.append(r);
    }
    const n = Object.values(st).filter(x => x.rating || (x.tags || []).length).length;
    const e = document.createElement("div"); e.className = "row";
    if (live) e.append(Object.assign(document.createElement("span"), { className: "lbl", textContent: `${status} (${n})` }));
    else e.append(btn(`Export feedback (${n})`, false, exportJson));
    if (i < 0) box.append(e); else box.lastChild.append(...e.childNodes);
  }
  function exportJson() {
    const out = { folder: dir, question: document.querySelector("h1")?.textContent || "", exported: new Date().toISOString(), designs: st };
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([JSON.stringify(out, null, 2)], { type: "application/json" }));
    a.download = `feedback-${dir}.json`; a.click(); URL.revokeObjectURL(a.href);
  }
  const orig = window.show;
  window.show = function (i) { orig(i); render(); };
  render();
})();
