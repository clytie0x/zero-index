"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/02-reading-goal   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนวันและสองแสนคำถาม คำถามส่วนใหญ่เริ่มต้นๆ และเป้าสูง
ตั้งใจให้วิธีบวกทีละวันใน naive.cpp ต้องไล่เกือบทุกวันทุกคำถามจนไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1902)

TOP = 10**9


def build(pages, questions):
    rows = [f"{len(pages)} {len(questions)}", " ".join(map(str, pages))] + [f"{s} {t}" for s, t in questions]
    return "\n".join(rows)


def cases():
    yield "sample1", "7 5\n30 45 0 0 60 25 40\n1 75\n3 1\n3 60\n6 66\n2 200"
    yield "single", build([5], [(1, 1), (1, 5), (1, 6)])
    yield "all-zero", build([0] * 6, [(1, 1), (3, 1), (6, TOP)])
    # วันที่ไม่ได้อ่านอยู่ตรงที่คำตอบพอดี ต้องได้วันแรกที่ถึง ไม่ใช่วันท้ายของค่าที่ซ้ำ
    yield "zero-days", build([0, 0, 10, 0, 0, 0, 10, 0, 0], [(1, 10), (1, 11), (1, 20), (2, 20), (4, 10), (8, 1), (3, 10), (3, 21)])
    # เป้าเท่ากับผลรวมพอดี และเกินไปหนึ่งหน้า
    pages = [random.randint(0, 10000) for _ in range(50)]
    total = sum(pages)
    yield "exact", build(pages, [(1, total), (1, total + 1), (50, pages[49] if pages[49] > 0 else 1), (25, sum(pages[24:]))])
    yield "max-target", build([10000] * 30, [(1, TOP), (1, 300000), (30, 10000), (30, 10001), (16, 150000)])
    pages = [random.choice([0, 0, random.randint(1, 20)]) for _ in range(60)]
    yield "rand1", build(pages, [(random.randint(1, 60), random.randint(1, 120)) for _ in range(60)])
    pages = [random.randint(0, 10000) for _ in range(2000)]
    yield "rand2", build(pages, [(random.randint(1, 2000), random.randint(1, 5000000)) for _ in range(2000)])
    n = 200000
    pages = [random.randint(0, 10000) for _ in range(n)]
    total = sum(pages)
    yield "big1", build(pages, [(random.randint(1, 1000), random.randint(total // 2, total)) for _ in range(n)])
    pages = [random.choice([0] * 9 + [1]) for _ in range(n)]
    yield "big2", build(pages, [(random.randint(1, 100), random.randint(1, TOP)) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
