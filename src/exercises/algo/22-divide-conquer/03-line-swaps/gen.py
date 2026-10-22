"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/03-line-swaps   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีนักเรียนสองแสนคน ตั้งใจให้วิธีลองทุกคู่ใน naive.cpp ไม่ทัน
big1 เรียงจากสูงไปเตี้ย คำตอบ 19999900000 เกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2203)

TOP = 10**9


def build(heights):
    return f"{len(heights)}\n" + " ".join(map(str, heights))


def cases():
    yield "sample1", "5\n150 160 155 145 158"
    yield "sample2", "4\n140 140 135 140"
    yield "single", build([170])
    yield "sorted", build(list(range(100, 1100)))
    yield "all-equal", build([150] * 500)
    yield "reversed", build(list(range(2000, 0, -1)))
    # ส่วนสูงซ้ำเยอะ คนที่สูงเท่ากันไม่ต้องสลับกัน
    yield "many-ties", build([random.randint(1, 5) for _ in range(3000)])
    yield "rand1", build([random.randint(1, TOP) for _ in range(3000)])
    n = 200000
    yield "big1", build(list(range(n, 0, -1)))
    yield "big2", build([random.randint(1, TOP) for _ in range(n)])
    yield "big3", build([random.randint(1, 100) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
