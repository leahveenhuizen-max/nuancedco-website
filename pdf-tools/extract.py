#!/usr/bin/env python3
"""Extract The Unmasked Life manuscript from the week-N.html course pages
into print-ready HTML (cover + body) for PDF rendering. Content ships as-is;
only UI chrome is stripped and whitespace normalised."""
import os, re, html
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build")
os.makedirs(BUILD, exist_ok=True)

WEEKS = [
    ("week-1", 1), ("week-2", 2), ("week-3", 3), ("week-4", 4),
]

def clean_text(s):
    s = re.sub(r"\s+", " ", s).strip()
    return s

def strip_icons(el):
    for i in el.find_all("i"):
        i.decompose()
    for b in el.find_all(["button", "audio", "video", "select", "input", "svg"]):
        b.decompose()

def render_inline(el):
    """Inline content of a tag -> safe HTML keeping em/strong/a(text)."""
    out = []
    for node in el.children:
        if isinstance(node, NavigableString):
            out.append(html.escape(str(node)))
        elif isinstance(node, Tag):
            if node.name in ("em", "i") and not (node.get("class") and any("fa-" in c for c in node.get("class"))):
                out.append("<em>" + render_inline(node) + "</em>")
            elif node.name in ("strong", "b"):
                out.append("<strong>" + render_inline(node) + "</strong>")
            elif node.name == "a":
                out.append(render_inline(node))  # plain text; PDFs ship without nav links
            elif node.name == "br":
                out.append("<br>")
            elif node.name in ("span",):
                out.append(render_inline(node))
            # icons and other tags dropped
    return re.sub(r"\s+", " ", "".join(out)).strip()

def render_wp(wp):
    lbl = wp.find(class_="wp-label")
    q = wp.find(class_="wp-question")
    h = '<div class="wp">'
    if lbl: h += f'<p class="wp-label">{html.escape(clean_text(lbl.get_text()))}</p>'
    if q: h += f'<p class="wp-q">{render_inline(q)}</p>'
    # any extra paragraphs inside the prompt
    for p in wp.find_all("p"):
        if p is lbl or p is q or (p.get("class") and ("wp-label" in p["class"] or "wp-question" in p["class"])):
            continue
        h += f"<p>{render_inline(p)}</p>"
    return h + "</div>"

def render_block_children(el, skip_classes=()):
    """Walk a container, rendering p/h/ul/ol/workbook-prompt blocks in order."""
    out = []
    for node in el.descendants:
        if not isinstance(node, Tag):
            continue
        cls = node.get("class") or []
        if any(c in skip_classes for c in cls):
            continue
        if any(c in ("dopamine-note", "milestone-week-tag", "milestone-text", "progress-track") for c in cls):
            continue
        if node.find_parent(class_="milestone-item"):
            continue
        # only handle blocks whose nearest handled ancestor is el (avoid dupes)
        if node.name == "p" and "wp-label" not in cls and "wp-question" not in cls \
           and not node.find_parent(class_="workbook-prompt") \
           and not node.find_parent(class_="qr-card"):
            if "card-label" in cls or "acc-title" in cls:
                continue
            t = render_inline(node)
            if t:
                out.append((node, f"<p>{t}</p>"))
        elif node.name in ("h2", "h3", "h4") and "acc-title" not in cls:
            t = render_inline(node)
            if t:
                out.append((node, f"<h3>{t}</h3>"))
        elif node.name in ("ul", "ol") and "qr-list" not in cls and not node.find_parent(class_="qr-card"):
            items = "".join(f"<li>{render_inline(li)}</li>" for li in node.find_all("li", recursive=False))
            if items:
                out.append((node, f"<{node.name}>{items}</{node.name}>"))
        elif node.name == "div" and "workbook-prompt" in cls:
            out.append((node, render_wp(node)))
    # drop blocks nested inside an already-rendered workbook prompt
    final = []
    for node, htm in out:
        if node.name != "div" and node.find_parent(class_="workbook-prompt"):
            continue
        final.append(htm)
    return "".join(final)

def render_accordion(container, heading=None):
    out = []
    if heading:
        out.append(f'<p class="eyebrow">{html.escape(heading)}</p>')
    for item in container.find_all(class_="acc-item"):
        num = item.find(class_="acc-number")
        title = item.find(class_="acc-title")
        body = item.find(class_="acc-body")
        if not title or not body:
            continue
        strip_icons(body)
        n = clean_text(num.get_text()) if num else ""
        out.append('<section class="lesson-sec">')
        out.append(f'<h2>{("<span class=num>"+html.escape(n)+"</span> ") if n else ""}{render_inline(title)}</h2>')
        out.append(render_block_children(body))
        out.append("</section>")
    return "".join(out)

def render_card(card):
    strip_icons(card)
    lbl = card.find(class_="card-label")
    label = clean_text(lbl.get_text()) if lbl else ""
    if re.search(r"resources|focus timer|display|all milestones", label, re.I):
        return ""
    if re.search(r"milestone", label, re.I):
        mt = card.find(class_="milestone-text")
        if not mt:
            return ""
        return ('<section class="card-sec"><p class="eyebrow">' + html.escape(label)
                + '</p><div class="wp"><p class="wp-label">This week\'s task</p><p class="wp-q">'
                + render_inline(mt) + "</p></div></section>")
    h = '<section class="card-sec">'
    if label:
        h += f'<p class="eyebrow">{html.escape(label)}</p>'
    h += render_block_children(card, skip_classes=("card-label",))
    return h + "</section>"

def render_qr(qr):
    strip_icons(qr)
    lbl = qr.find(class_="qr-card-label")
    h = '<section class="qr">'
    if lbl:
        h += f'<p class="qr-label">{html.escape(clean_text(lbl.get_text()))}</p>'
    for el in qr.find_all(["p", "ul"]):
        cls = el.get("class") or []
        if "qr-card-label" in cls or "wp-label" in cls or "wp-question" in cls:
            continue
        if el.find_parent(class_="workbook-prompt"):
            continue
        if el.name == "ul":
            h += "<ul>" + "".join(f"<li>{render_inline(li)}</li>" for li in el.find_all("li")) + "</ul>"
        else:
            t = render_inline(el)
            if t:
                h += f"<p>{t}</p>"
    for wp in qr.find_all(class_="workbook-prompt"):
        h += render_wp(wp)
    return h + "</section>"

def extract_week(slug, num):
    soup = BeautifulSoup(open(os.path.join(ROOT, f"{slug}.html")).read(), "html.parser")
    main = soup.find(class_="lesson-main")
    header = main.find(class_="lesson-header")
    title_el = header.find("h1") if header else None
    title = render_inline(title_el) if title_el else f"Week {num}"
    intro = ""
    if header:
        strip_icons(header)
        intro = render_block_children(header)
    body = [f'<h1 class="doc-title">{title}</h1>', intro]
    for ch in main.find_all(recursive=False):
        cls = " ".join(ch.get("class") or [])
        if ch.name == "header" or "video-wrap" in cls or "mode-strip" in cls or ch.name == "nav":
            continue
        if "speedread-panel" in cls:
            strip_icons(ch)
            for tp in ch.find_all(class_="transcript-panel"):
                tp.decompose()
            inner = render_block_children(ch, skip_classes=("card-label",))
            if inner:
                body.append('<section class="note"><p class="eyebrow" style="margin-top:0">Week ' + str(num) + ' at a glance</p>' + inner + "</section>")
            continue
        if "card" in cls.split() and "qr-card" not in cls:
            body.append(render_card(ch))
        elif ch.find(class_="acc-item"):
            body.append(render_accordion(ch))
        elif "qr-card" in cls:
            body.append(render_qr(ch))
        elif "scope-block" in cls:
            strip_icons(ch)
            body.append('<section class="note">' + render_block_children(ch) + "</section>")
        else:
            strip_icons(ch)
            inner = render_block_children(ch)
            if inner:
                body.append('<section class="note">' + inner + "</section>")
    return title, "".join(b for b in body if b)

def extract_welcome():
    soup = BeautifulSoup(open(os.path.join(ROOT, "course-dashboard.html")).read(), "html.parser")
    cards = soup.find_all(class_="card")
    intro_html = ""
    for c in cards:
        txt = c.get_text(" ", strip=True)
        if "four-week educational course" in txt or "This is a four-week" in txt:
            strip_icons(c)
            intro_html = render_block_children(c, skip_classes=("card-label",))
            break
    weeks = []
    for sc in soup.find_all(class_="sprint-card"):
        wn = sc.find(class_="sprint-week")
        wt = sc.find(class_="sprint-title")
        if wt:
            weeks.append((clean_text(wn.get_text()) if wn else "", render_inline(wt)))
    if not weeks:
        for slug, num in WEEKS:
            s2 = BeautifulSoup(open(os.path.join(ROOT, f"{slug}.html")).read(), "html.parser")
            h1 = s2.find(class_="lesson-main").find("h1")
            weeks.append((f"Week {num}", render_inline(h1)))
    # scope note from week-1
    s1 = BeautifulSoup(open(os.path.join(ROOT, "week-1.html")).read(), "html.parser")
    scope = s1.find(class_="scope-block")
    strip_icons(scope)
    scope_html = render_block_children(scope)
    start = s1.find(class_="lesson-main").find(class_="card")  # Start here card
    strip_icons(start)
    start_html = render_block_children(start, skip_classes=("card-label",))
    body = ['<h1 class="doc-title">Welcome to The Unmasked Life</h1>']
    if intro_html:
        body.append('<section class="card-sec"><p class="eyebrow">About this course</p>' + intro_html + "</section>")
    body.append('<section class="card-sec"><p class="eyebrow">The four weeks</p><ul class="week-list">' +
                "".join(f"<li><span class=num>{html.escape(w or ('Week '+str(i+1)))}</span>{t}</li>" for i, (w, t) in enumerate(weeks)) + "</ul></section>")
    body.append('<section class="card-sec"><p class="eyebrow">Before you begin</p>' + start_html + "</section>")
    body.append('<section class="note">' + scope_html + "</section>")
    return "Welcome &amp; Start Here", "".join(body)

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "print.css")).read()

def page(title_html, body_html, cover=False, week_label=""):
    kind = "cover" if cover else "body"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<style>{CSS}</style></head><body class="{kind}">{body_html}</body></html>"""

def cover_html(week_label, title):
    return f"""
<div class="cover-page">
  <div class="cover-top">
    <p class="wordmark">Nuanced Co.</p>
    <p class="wordmark-sub">Neurodivergent Consultancy</p>
  </div>
  <div class="cover-mid">
    <p class="cover-eyebrow">{html.escape(week_label)}</p>
    <h1 class="cover-title">{title}</h1>
    <div class="cover-rule"></div>
    <p class="cover-course">The Unmasked Life&trade;</p>
    <p class="cover-tag">A four-week course for late-diagnosed ADHD and AuDHD adults</p>
  </div>
  <div class="cover-foot">
    <p>nuancedco.com.au</p>
  </div>
</div>"""

docs = []
for slug, num in WEEKS:
    title, body = extract_week(slug, num)
    docs.append((slug, f"Week {num}", title, body))
w_title, w_body = extract_welcome()
docs.insert(0, ("welcome", "Start Here", w_title, w_body))

for slug, label, title, body in docs:
    open(os.path.join(BUILD, f"{slug}-cover.html"), "w").write(page(title, cover_html(label, title), cover=True))
    open(os.path.join(BUILD, f"{slug}-body.html"), "w").write(page(title, body))
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    print(f"{slug}: '{re.sub('<[^>]+>','',title)}' — {words} words")
