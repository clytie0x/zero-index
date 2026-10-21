"""สร้างชุดทดสอบ big ที่ไม่ได้เก็บไว้ใน git

    python tools/prepare_tests.py

ชุดที่ชื่อขึ้นต้นด้วย big มีขนาดใหญ่ จึงไม่เก็บใน git (ดู .gitignore)
สคริปต์นี้รัน gen.py ของแต่ละข้อในโฟลเดอร์ชั่วคราว คัดลอกกลับมาเฉพาะ big*.in
แล้วสร้าง big*.out จากเฉลย ชุดอื่นที่เก็บใน git ไม่ถูกแตะ
gen.py ใช้ seed ตายตัว จึงได้ไฟล์เหมือนเดิมทุกครั้ง
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_code import EXERCISES, compile_source, run  # noqa: E402


def prepare(d: Path, work: Path) -> int:
    tmp = work / d.name
    shutil.copytree(d, tmp)
    r = subprocess.run([sys.executable, str(tmp / "gen.py")], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(f"{d}: gen.py ล้มเหลว\n{r.stderr}", file=sys.stderr)
        return -1
    bigs = sorted((tmp / "tests").glob("big*.in"))
    if not bigs:
        return 0
    sol = next((p for p in sorted(d.iterdir()) if p.stem == "solution" and p.suffix in (".c", ".cpp")), None)
    exe, err = compile_source(sol.read_text(encoding="utf-8"), "cpp" if sol.suffix == ".cpp" else "c",
                              work, f"sol_{d.name}", False)
    if exe is None:
        print(f"{d}: คอมไพล์เฉลยไม่ผ่าน\n{err}", file=sys.stderr)
        return -1
    for big in bigs:
        target = d / "tests" / big.name
        shutil.copyfile(big, target)
        code, out = run(exe, target.read_text(encoding="utf-8"))
        if code is None:
            print(f"{target}: เฉลยรันเกินเวลา", file=sys.stderr)
            return -1
        target.with_suffix(".out").write_text(out, encoding="utf-8", newline="\n")
    return len(bigs)


def main() -> int:
    total, failed = 0, 0
    with tempfile.TemporaryDirectory() as tmp:
        for gen in sorted(EXERCISES.rglob("gen.py")):
            n = prepare(gen.parent, Path(tmp))
            if n < 0:
                failed += 1
            else:
                total += n
    print(f"สร้างชุด big {total} ชุด ล้มเหลว {failed} ข้อ")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
