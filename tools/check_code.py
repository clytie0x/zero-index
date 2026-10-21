"""คอมไพล์และรันโค้ดในเอกสาร เพื่อยืนยันว่าทุกตัวอย่างใช้ได้จริง

    python tools/check_code.py

ตรวจสองส่วน
1. ตัวอย่างในหน้าเนื้อหา บล็อกโค้ดที่มี data-test="ชื่อ" จะถูกคอมไพล์
   ถ้ามีบล็อก data-lang="input" data-for="ชื่อ" จะใช้เป็น input
   ถ้ามีบล็อก data-lang="output" data-for="ชื่อ" ผลที่รันได้ต้องตรงกัน
   ใส่ data-allow-warnings ถ้าตั้งใจให้ตัวอย่างนั้นมีคำเตือน
2. แบบฝึกหัดใน src/exercises เฉลยทุกไฟล์ (solution*) ต้องผ่านชุดทดสอบทุกชุด
   วิธีช้า (naive*) ต้องผ่านทุกชุดที่ชื่อไม่มีคำว่า big

คอมไพล์ด้วย -Wall -Wextra และถือว่าคำเตือนคือข้อผิดพลาด เพราะเอกสารสอนให้น้องเปิด -Wall
เลือก compiler ได้ด้วยตัวแปร ZI_GCC และ ZI_GXX (ค่าเริ่มต้น gcc และ g++)
"""

from __future__ import annotations

import html
import os
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "src" / "pages"
EXERCISES = ROOT / "src" / "exercises"

GCC = os.environ.get("ZI_GCC", "gcc")
GXX = os.environ.get("ZI_GXX", "g++")
C_FLAGS = ["-std=c17", "-O2", "-Wall", "-Wextra"]
CPP_FLAGS = ["-std=gnu++17", "-O2", "-Wall", "-Wextra"]
RUN_TIMEOUT = 10

BLOCK = re.compile(r'<div class="code"([^>]*)><pre><code>(.*?)</code></pre></div>', re.S)
ATTR = re.compile(r'([\w-]+)(?:="([^"]*)")?')
ANNO = re.compile(r"\s*//\s*\(\d+\)!\s*$", re.M)
# Code::Blocks เติมสองบรรทัดนี้ท้ายหน้าต่างผลลัพธ์ โปรแกรมไม่ได้พิมพ์เอง
CB_FOOTER = re.compile(r"\n*Process returned -?\d+ \(0x[0-9A-Fa-f]+\)\s+execution time : [\d.]+ s\nPress any key to continue\.\s*$")


def normalize(text: str) -> str:
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    return "\n".join(lines).strip("\n")


def compile_source(src: str, lang: str, workdir: Path, name: str, allow_warnings: bool) -> tuple[Path | None, str]:
    ext = ".cpp" if lang == "cpp" else ".c"
    source = workdir / f"{name}{ext}"
    source.write_text(src, encoding="utf-8")
    exe = workdir / f"{name}.exe"
    flags = CPP_FLAGS if lang == "cpp" else C_FLAGS
    if not allow_warnings:
        flags = flags + ["-Werror"]
    cmd = [GXX if lang == "cpp" else GCC, *flags, str(source), "-o", str(exe), "-lm"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return None, r.stderr.strip()
    return exe, ""


def run(exe: Path, stdin: str) -> tuple[int | None, str]:
    try:
        r = subprocess.run([str(exe)], input=stdin, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=RUN_TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, ""
    return r.returncode, r.stdout


def blocks_in(path: Path) -> list[tuple[dict, str]]:
    out = []
    for m in BLOCK.finditer(path.read_text(encoding="utf-8")):
        attrs = {k: (v if v is not None else "") for k, v in ATTR.findall(m.group(1))}
        out.append((attrs, html.unescape(m.group(2))))
    return out


def check_pages(workdir: Path) -> tuple[int, list[str]]:
    count, errors = 0, []
    for page in sorted(PAGES.rglob("*.html")):
        rel = page.relative_to(PAGES).as_posix()
        blocks = blocks_in(page)
        inputs = {a["data-for"]: t for a, t in blocks if a.get("data-lang") == "input" and "data-for" in a}
        outputs = {a["data-for"]: t for a, t in blocks if a.get("data-lang") == "output" and "data-for" in a}
        for attrs, text in blocks:
            name = attrs.get("data-test")
            if not name:
                continue
            count += 1
            lang = attrs.get("data-lang", "c")
            src = ANNO.sub("", text)
            exe, err = compile_source(src, lang, workdir, re.sub(r"\W", "_", f"{rel}_{name}"), "data-allow-warnings" in attrs)
            if exe is None:
                errors.append(f"{rel} [{name}] คอมไพล์ไม่ผ่าน\n{err}")
                continue
            code, got = run(exe, inputs.get(name, ""))
            if code is None:
                errors.append(f"{rel} [{name}] รันเกิน {RUN_TIMEOUT} วินาที")
                continue
            if name in outputs:
                want = normalize(CB_FOOTER.sub("", outputs[name]))
                if normalize(got) != want:
                    errors.append(f"{rel} [{name}] ผลลัพธ์ไม่ตรงกับในหน้า\n--- ในหน้า\n{want}\n--- รันได้\n{normalize(got)}")
    return count, errors


def check_exercises(workdir: Path) -> tuple[int, list[str]]:
    count, errors = 0, []
    if not EXERCISES.exists():
        return 0, []
    for task in sorted(EXERCISES.rglob("task.toml")):
        d = task.parent
        rel = d.relative_to(EXERCISES).as_posix()
        tomllib.loads(task.read_text(encoding="utf-8"))  # ให้ไฟล์ toml ที่พังโผล่ตรงนี้
        tests = sorted((d / "tests").glob("*.in"))
        if not tests:
            errors.append(f"แบบฝึกหัด {rel} ไม่มีชุดทดสอบ")
            continue
        solutions = sorted(p for p in d.iterdir()
                           if p.stem.startswith(("solution", "naive")) and p.suffix in (".c", ".cpp"))
        if not solutions:
            errors.append(f"แบบฝึกหัด {rel} ไม่มีเฉลย")
            continue
        for sol in solutions:
            count += 1
            lang = "cpp" if sol.suffix == ".cpp" else "c"
            exe, err = compile_source(sol.read_text(encoding="utf-8"), lang, workdir,
                                      re.sub(r"\W", "_", f"ex_{rel}_{sol.stem}"), False)
            if exe is None:
                errors.append(f"แบบฝึกหัด {rel}/{sol.name} คอมไพล์ไม่ผ่าน\n{err}")
                continue
            for t in tests:
                # วิธีช้าตรวจเฉพาะชุดเล็ก ชุดที่ชื่อมีคำว่า big ตั้งใจให้วิธีช้าไม่ทัน
                if sol.stem.startswith("naive") and "big" in t.stem:
                    continue
                ans = t.with_suffix(".out")
                if not ans.exists():
                    errors.append(f"แบบฝึกหัด {rel} ไม่มี {ans.name}")
                    continue
                code, got = run(exe, t.read_text(encoding="utf-8"))
                if code is None:
                    errors.append(f"แบบฝึกหัด {rel}/{sol.name} ชุด {t.stem} รันเกิน {RUN_TIMEOUT} วินาที")
                elif normalize(got) != normalize(ans.read_text(encoding="utf-8")):
                    errors.append(f"แบบฝึกหัด {rel}/{sol.name} ชุด {t.stem} ได้คำตอบไม่ตรง")
    return count, errors


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        n_pages, e_pages = check_pages(work)
        n_ex, e_ex = check_exercises(work)
    errors = e_pages + e_ex
    for e in errors:
        print(e, end="\n\n", file=sys.stderr)
    print(f"ตัวอย่างในหน้า {n_pages} ชิ้น เฉลยแบบฝึกหัด {n_ex} ไฟล์ พบปัญหา {len(errors)} จุด")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
