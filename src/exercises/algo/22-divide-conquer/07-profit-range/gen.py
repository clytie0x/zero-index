"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/07-profit-range   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนวัน ตั้งใจให้วิธีลองทุกช่วงใน naive.cpp ไม่ทัน
big3 กำไรเป็นศูนย์ทุกวันและ L = R = 0 คำตอบ 20000100000 เกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2207)

TOP = 10**9


def build(low, high, profits):
    return f"{len(profits)} {low} {high}\n" + " ".join(map(str, profits))


def cases():
    yield "sample1", "8 3 6\n3 2 -1 1 5 -5 5 0"
    yield "single-in", build(-5, 5, [5])
    yield "single-out", build(1, 10, [-1])
    yield "exact", build(5, 5, [3, 2, -1, 1, 5, -5, 5, 0])
    yield "all-zero", build(0, 0, [0] * 2000)
    yield "negative-range", build(-12, -4, [-3, 4, -6, -2, 1, -5, -1, 2, -7])
    yield "wide", build(-TOP, 2 * TOP, [random.choice([TOP, -TOP, random.randint(-TOP, TOP)]) for _ in range(1500)])
    yield "rand1", build(-4, 7, [random.randint(-10, 10) for _ in range(2000)])
    profits = [random.randint(-TOP, TOP) for _ in range(2000)]
    yield "rand2", build(-3 * TOP, 2 * TOP, profits)
    n = 200000
    yield "big1", build(-20, 35, [random.randint(-10, 10) for _ in range(n)])
    yield "big2", build(-5 * TOP, 10 * TOP, [random.randint(-TOP, TOP) for _ in range(n)])
    yield "big3", build(0, 0, [0] * n)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
