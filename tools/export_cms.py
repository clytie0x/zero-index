"""ส่งออกแบบฝึกหัดเป็นโฟลเดอร์ที่ CMS นำเข้าได้ (รูปแบบ italy_yaml)

    python tools/prepare_tests.py               สร้างชุด big ก่อน
    python tools/export_cms.py                  ส่งออกทุกบทไปที่ cms-export/
    python tools/export_cms.py c/05-arrays      ส่งออกเฉพาะบท

ได้โฟลเดอร์ละหนึ่งข้อ ชื่อ zi_<บท>_<ข้อ> ข้างในมี
    task.yaml
    statement/statement.pdf   สร้างจาก statement.html ด้วย Chrome แบบ headless
    input/input0.txt ...      ชุด sample อยู่หน้าสุดและเปิดให้เห็นผล (public_testcases)
    output/output0.txt ...

นำเข้าบนเซิร์ฟเวอร์ด้วย cmsImportTask -L italy_yaml <โฟลเดอร์>
สคริปต์นี้ไม่ติดต่อเซิร์ฟเวอร์ใดๆ
"""

from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXERCISES = ROOT / "src" / "exercises"
OUT = ROOT / "cms-export"

CHROME_CANDIDATES = [
    os.environ.get("ZI_CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "google-chrome", "chromium", "chromium-browser",
]

PDF_PAGE = """<!doctype html>
<html lang="th"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&amp;family=Noto+Sans+Thai:wght@400;700&amp;display=swap">
<style>
body {{ font-family: "Noto Sans Thai", Tahoma, sans-serif; font-size: 14px; line-height: 1.7; margin: 24px 32px; color: #111; }}
h1 {{ font-size: 22px; margin: 0 0 4px; }}
.meta {{ color: #555; font-size: 12px; margin-bottom: 16px; }}
h3 {{ font-size: 15px; margin: 18px 0 4px; }}
code, pre {{ font-family: "JetBrains Mono", Consolas, monospace; font-size: 12.5px; }}
pre {{ background: #f4f5f8; border: 1px solid #dde; border-radius: 6px; padding: 8px 12px; white-space: pre-wrap; }}
table {{ border-collapse: collapse; }} th, td {{ border: 1px solid #ccd; padding: 4px 10px; }}
.io {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
.io b {{ font-size: 12px; color: #555; }}
</style></head><body>
<h1>{title}</h1>
<div class="meta">{meta}</div>
{statement}
{samples}
</body></html>
"""


def find_chrome() -> str | None:
    for c in CHROME_CANDIDATES:
        if c and (Path(c).exists() or shutil.which(c)):
            return c
    return None


def strip_code_blocks(statement: str) -> str:
    """แปลงบล็อกโค้ดของเว็บเป็น <pre> ธรรมดาสำหรับ PDF"""
    return re.sub(r'<div class="code"[^>]*><pre><code>(.*?)</code></pre></div>', r"<pre>\1</pre>", statement, flags=re.S)


def export_task(d: Path, chapter: str, chrome: str, work: Path) -> str:
    task = tomllib.loads((d / "task.toml").read_text(encoding="utf-8"))
    tests = sorted((d / "tests").glob("*.in"))
    samples = [t for t in tests if t.stem.startswith("sample")]
    others = [t for t in tests if not t.stem.startswith("sample")]
    ordered = samples + others
    short = re.sub(r"\W", "_", f"zi_{chapter.split('/')[-1][:2]}_{re.sub(r'^\d+-', '', d.name)}")
    target = OUT / short
    if target.exists():
        shutil.rmtree(target)
    (target / "input").mkdir(parents=True)
    (target / "output").mkdir()
    (target / "statement").mkdir()
    for i, t in enumerate(ordered):
        shutil.copyfile(t, target / "input" / f"input{i}.txt")
        shutil.copyfile(t.with_suffix(".out"), target / "output" / f"output{i}.txt")

    time_limit = task.get("time_limit", 1)
    lines = [
        f"name: {short}",
        f'title: "{task["title"]}"',
        f"time_limit: {time_limit}",
        "memory_limit: 256",
        f"n_input: {len(ordered)}",
        "infile: ''",
        "outfile: ''",
        "token_mode: disabled",
        f"public_testcases: {','.join(str(i) for i in range(len(samples)))}",
    ]
    (target / "task.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    sample_html = []
    for j, s in enumerate(samples, 1):
        inp = html.escape(s.read_text(encoding="utf-8").rstrip("\n"))
        out = html.escape(s.with_suffix(".out").read_text(encoding="utf-8").rstrip("\n"))
        sample_html.append(f'<h3>ตัวอย่างที่ {j}</h3><div class="io"><div><b>ข้อมูลเข้า</b><pre>{inp}</pre></div>'
                           f'<div><b>ข้อมูลออก</b><pre>{out}</pre></div></div>')
    page = PDF_PAGE.format(title=html.escape(task["title"]),
                           meta=f"เวลาไม่เกิน {time_limit} วินาที  หน่วยความจำไม่เกิน 256 MB  ({short})",
                           statement=strip_code_blocks((d / "statement.html").read_text(encoding="utf-8")),
                           samples="".join(sample_html))
    src = work / f"{short}.html"
    src.write_text(page, encoding="utf-8")
    pdf = target / "statement" / "statement.pdf"
    subprocess.run([chrome, "--headless=new", "--disable-gpu", f"--user-data-dir={work / 'profile'}",
                    "--no-pdf-header-footer", "--virtual-time-budget=5000", f"--print-to-pdf={pdf}", src.as_uri()],
                   capture_output=True, timeout=120)
    if not pdf.exists():
        raise RuntimeError(f"{short}: สร้าง PDF ไม่สำเร็จ")
    return short


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    chrome = find_chrome()
    if chrome is None:
        print("ไม่พบ Chrome หรือ Edge ตั้ง ZI_CHROME ให้ชี้ไปที่ตัวโปรแกรม", file=sys.stderr)
        return 1
    OUT.mkdir(exist_ok=True)
    names, missing = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for toml in sorted(EXERCISES.rglob("task.toml")):
            d = toml.parent
            chapter = d.parent.relative_to(EXERCISES).as_posix()
            if not chapter.startswith(only):
                continue
            if any(not t.with_suffix(".out").exists() for t in (d / "tests").glob("*.in")) or \
                    (d / "gen.py").exists() and "big" in (d / "gen.py").read_text(encoding="utf-8") and \
                    not list((d / "tests").glob("big*.in")):
                missing.append(d.relative_to(EXERCISES).as_posix())
                continue
            names.append(export_task(d, chapter, chrome, Path(tmp)))
    for m in missing:
        print(f"ข้าม {m} ชุดทดสอบไม่ครบ ให้รัน tools/prepare_tests.py ก่อน", file=sys.stderr)
    print(f"ส่งออก {len(names)} ข้อที่ {OUT}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
