"""สร้างเว็บจาก src/ ไปไว้ที่ dist/

ใช้ Python 3.11 ขึ้นไป ไม่ต้องลงไลบรารีเพิ่ม

    python tools/build.py          สร้างเว็บแล้วตรวจลิงก์
    python tools/build.py --serve  สร้างแล้วเปิดดูที่ http://127.0.0.1:8000

ลำดับหน้าทั้งหมดอยู่ใน src/site.toml ไฟล์ใน src/pages เก็บเฉพาะ <article> ของแต่ละหน้า
"""

from __future__ import annotations

import hashlib
import html
import posixpath
import re
import shutil
import sys
import tomllib
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PAGES = SRC / "pages"
DIST = ROOT / "dist"

ICON_PREV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
ICON_NEXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TOC_INLINE = '<ul class="toc-inline" aria-label="ในหน้านี้"></ul>'


@dataclass
class Page:
    path: str            # ที่อยู่ใน dist เช่น c/00-start/why.html
    kind: str            # home, chapter หรือ page
    title: str           # ชื่อที่ใช้ในเมนู
    num: str = ""
    chapter: "Page | None" = None

    @property
    def label(self) -> str:
        """ชื่อเต็มที่ใช้ในแท็บและปุ่มก่อนหน้าถัดไป"""
        return f"{self.num} {self.title}" if self.kind == "page" else self.title


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def load_site() -> tuple[dict, list[Page], list[tuple[Page, list[Page]]]]:
    site = tomllib.loads((SRC / "site.toml").read_text(encoding="utf-8"))
    home = Page(site["home"]["path"], "home", site["home"]["title"])
    order = [home]
    tree = []
    for ch in site.get("chapters", []):
        if "path" not in ch:
            continue  # บทที่วางแผนไว้ ยังไม่มีหน้า
        chapter = Page(ch["path"], "chapter", ch["title"], ch["num"])
        children = [Page(p["path"], "page", p["title"], p["num"], chapter) for p in ch.get("pages", [])]
        order += [chapter, *children]
        tree.append((chapter, children))
    return site, order, tree


def rel(target: str, current: Page) -> str:
    return posixpath.relpath(target, posixpath.dirname(current.path) or ".")


def render_nav(current: Page, home: Page, tree) -> str:
    def cur(p: Page) -> str:
        return ' aria-current="page"' if p is current else ""

    lines = ['    <ul class="nav">']
    toc = TOC_INLINE if home is current else ""
    lines.append(f'      <li><a href="{rel(home.path, current)}"{cur(home)}>{esc(home.title)}</a>{toc}</li>')
    for chapter, children in tree:
        lines.append('      <li class="nav-section">')
        lines.append(f'        <a class="nav-section-title" href="{rel(chapter.path, current)}"{cur(chapter)}>'
                     f'<span class="num-chip">{esc(chapter.num)}</span>{esc(chapter.title)}</a>')
        if chapter is current:
            lines.append(f"        {TOC_INLINE}")
        lines.append("        <ul>")
        for p in children:
            toc = TOC_INLINE if p is current else ""
            lines.append(f'          <li><a href="{rel(p.path, current)}"{cur(p)}><span class="num">{esc(p.num)}</span>'
                         f"<span>{esc(p.title)}</span></a>{toc}</li>")
        lines.append("        </ul>")
        lines.append("      </li>")
    lines.append("    </ul>")
    return "\n".join(lines)


def render_pager(current: Page, prev: Page | None, nxt: Page | None) -> str:
    lines = ['    <nav class="pager" aria-label="หน้าก่อนหน้าและถัดไป">']
    if prev:
        lines += [f'      <a class="prev" href="{rel(prev.path, current)}">',
                  f"        {ICON_PREV}",
                  f'        <span class="pg-text"><span class="pg-label">ก่อนหน้า</span><span class="pg-title">{esc(prev.label)}</span></span>',
                  "      </a>"]
    if nxt:
        lines += [f'      <a class="next" href="{rel(nxt.path, current)}">',
                  f'        <span class="pg-text"><span class="pg-label">ถัดไป</span><span class="pg-title">{esc(nxt.label)}</span></span>',
                  f"        {ICON_NEXT}",
                  "      </a>"]
    lines.append("    </nav>")
    return "\n".join(lines)


def asset_version(name: str) -> str:
    return hashlib.sha256((SRC / "assets" / name).read_bytes()).hexdigest()[:10]


def render_course_map(site: dict, current: Page) -> str:
    """แผนที่คอร์สในหน้าแรก แต่ละบทเป็นช่องหนึ่งช่องเหมือนช่องในอาเรย์"""
    tracks: dict[str, list[dict]] = {}
    for ch in site.get("chapters", []):
        tracks.setdefault(ch["track"], []).append(ch)

    lines = ['<div class="course-map">']
    for track, chapters in tracks.items():
        lines.append(f'        <p class="track-title">{esc(track)}</p>')
        lines.append('        <ol class="cells">')
        for ch in chapters:
            short = re.sub(r"^บทที่\s*\S+\s*", "", ch["title"])
            body = (f'<span class="cell-index">[{esc(ch["num"])}]</span>'
                    f'<span class="cell-title">{esc(short)}</span>'
                    f'<span class="cell-sum">{esc(ch.get("summary", ""))}</span>')
            if "path" in ch:
                meta = f'{len(ch.get("pages", []))} หน้า'
                lines.append(f'          <li class="cell is-ready"><a href="{rel(ch["path"], current)}">{body}'
                             f'<span class="cell-meta">{meta}</span></a></li>')
            else:
                lines.append(f'          <li class="cell is-planned"><div>{body}'
                             f'<span class="cell-meta">กำลังเขียน</span></div></li>')
        lines.append("        </ol>")
    lines.append("      </div>")
    return "\n".join(lines)


def render(site: dict, layout: str, page: Page, home: Page, tree, prev, nxt, article: str) -> str:
    if "<!-- course-map -->" in article:
        article = article.replace("<!-- course-map -->", render_course_map(site, page))
    crumbs = ""
    if page.kind == "page":
        crumbs = (f'    <nav class="crumbs" aria-label="ตำแหน่ง"><a href="{rel(page.chapter.path, page)}">'
                  f"{esc(page.chapter.title)}</a></nav>\n")
    values = {
        "title": site["name"] if page.kind == "home" else f"{page.label} - {site['name']}",
        "description": site["description"],
        "root": rel("assets", page)[: -len("assets")],
        "body_attr": ' class="page-home"' if page.kind == "home" else "",
        "home": rel(home.path, page),
        "name": esc(site["name"]),
        "repo": site["repo"],
        "author": esc(site["author"]),
        "nav": render_nav(page, home, tree),
        "crumbs": crumbs,
        "article": article.rstrip("\n"),
        "pager": render_pager(page, prev, nxt),
        # เปลี่ยนตามเนื้อไฟล์ เบราว์เซอร์จะได้ไม่ใช้ CSS JS ตัวเก่าที่เก็บไว้
        "v_css": asset_version("site.css"),
        "v_js": asset_version("site.js"),
    }
    return re.sub(r"\{\{(\w+)\}\}", lambda m: values[m.group(1)], layout)


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.h1: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])
        if tag == "h1":
            self._in_h1 = True
            self.h1.append("")

    def handle_endtag(self, tag):
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data):
        if self._in_h1:
            self.h1[-1] += data


def check(order: list[Page]) -> list[str]:
    errors = []
    parsed = {}
    for f in DIST.rglob("*.html"):
        p = LinkCollector()
        p.feed(f.read_text(encoding="utf-8"))
        parsed[f.relative_to(DIST).as_posix()] = p

    for page in order:
        p = parsed[page.path]
        dupes = sorted({i for i in p.ids if p.ids.count(i) > 1})
        if dupes:
            errors.append(f"{page.path}: id ซ้ำ {dupes}")
        if page.kind != "home" and [h.strip() for h in p.h1] != [page.label]:
            errors.append(f"{page.path}: h1 {p.h1} ไม่ตรงกับชื่อใน site.toml '{page.label}'")
        for link in p.links:
            if re.match(r"^[a-z]+:", link) or link.startswith("//"):
                continue
            target, _, frag = link.partition("#")
            target = target.partition("?")[0]
            target_path = posixpath.normpath(posixpath.join(posixpath.dirname(page.path), target)) if target else page.path
            if not (DIST / target_path).is_file():
                errors.append(f"{page.path}: ลิงก์ {link} ชี้ไปไฟล์ที่ไม่มี")
            elif frag and target_path.endswith(".html") and frag not in parsed[target_path].ids:
                errors.append(f"{page.path}: ลิงก์ {link} ไม่มี id #{frag} ในหน้านั้น")
    return errors


def build() -> int:
    site, order, tree = load_site()
    home = order[0]

    listed = {p.path for p in order}
    on_disk = {f.relative_to(PAGES).as_posix() for f in PAGES.rglob("*.html")}
    errors = [f"site.toml มี {p} แต่ไม่มีไฟล์ src/pages/{p}" for p in sorted(listed - on_disk)]
    errors += [f"src/pages/{p} ไม่ได้อยู่ใน site.toml" for p in sorted(on_disk - listed)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC / "assets", DIST / "assets")

    layout = (SRC / "layout.html").read_text(encoding="utf-8")
    for i, page in enumerate(order):
        article = (PAGES / page.path).read_text(encoding="utf-8")
        prev = order[i - 1] if i > 0 else None
        nxt = order[i + 1] if i + 1 < len(order) else None
        out = DIST / page.path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(site, layout, page, home, tree, prev, nxt, article), encoding="utf-8", newline="\n")

    errors = check(order)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"สร้าง {len(order)} หน้าที่ dist/ ตรวจลิงก์ผ่าน")
    return 0


def serve() -> None:
    import functools
    import http.server

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler) as httpd:
        print("เปิดดูที่ http://127.0.0.1:8000  กด Ctrl+C เพื่อหยุด")
        httpd.serve_forever()


if __name__ == "__main__":
    code = build()
    if code == 0 and "--serve" in sys.argv:
        serve()
    sys.exit(code)
