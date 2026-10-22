"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/01-delivery-range   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีบ้านสองแสนหลังและสองแสนวัน ตั้งใจให้วิธีไล่ทุกบ้านทุกวันใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1901)

LIMIT = 10**9


def build(houses, days):
    rows = [f"{len(houses)} {len(days)}", " ".join(map(str, houses))] + [f"{p} {d}" for p, d in days]
    return "\n".join(rows)


def random_day(low, high, reach):
    return random.randint(low, high), random.randint(0, reach)


def cases():
    yield "sample1", "6 4\n3 -2 10 3 7 15\n5 2\n0 3\n12 1\n3 0"
    yield "single", build([0], [(0, 0), (1, 0), (-1, 1), (LIMIT, LIMIT)])
    yield "same-place", build([42] * 7, [(42, 0), (41, 0), (40, 1), (40, 2), (-LIMIT, LIMIT)])
    # p + d และ p - d ไปถึง 2 × 10^9 และ -2 × 10^9 ไกลเกินบ้านทุกหลัง
    yield "far-reach", build([LIMIT, -LIMIT, 0, LIMIT - 1, -LIMIT + 1],
                            [(LIMIT, LIMIT), (-LIMIT, LIMIT), (0, LIMIT), (LIMIT, 0), (-LIMIT, 0), (1, LIMIT - 1)])
    # บ้านอยู่ตรงขอบช่วงพอดี และช่วงที่ไม่มีบ้านเลย
    yield "edges", build([1, 5, 5, 9, 20], [(5, 4), (5, 3), (14, 6), (14, 5), (12, 2), (100, 79), (100, 80)])
    houses = [random.randint(-50, 50) for _ in range(40)]
    yield "rand1", build(houses, [random_day(-60, 60, 20) for _ in range(40)])
    houses = [random.randint(-LIMIT, LIMIT) for _ in range(2000)]
    yield "rand2", build(houses, [random_day(-LIMIT, LIMIT, LIMIT // 3) for _ in range(2000)])
    houses = [random.randint(-LIMIT, LIMIT) for _ in range(200000)]
    yield "big1", build(houses, [random_day(-LIMIT, LIMIT, LIMIT) for _ in range(200000)])
    houses = [random.randint(-1000, 1000) for _ in range(200000)]
    yield "big2", build(houses, [random_day(-LIMIT, LIMIT, LIMIT) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
