"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/08-houses-in-range   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N และ Q สองแสน ตั้งใจให้การไล่นับใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1608)

LIMIT = 10**9


def line(values):
    return " ".join(map(str, values))


def case(houses, queries):
    return (f"{len(houses)} {len(queries)}\n{line(houses)}\n"
            + "\n".join(f"{left} {right}" for left, right in queries))


def random_query(low, high):
    a = random.randint(low, high)
    b = random.randint(low, high)
    return (min(a, b), max(a, b))


def cases():
    yield "sample1", case([120, -40, 300, 120, 75, 500], [(0, 200), (120, 120), (301, 499), (-100, 1000)])
    yield "sample2", case([5, 5, 5], [(5, 5), (4, 4), (6, 10)])
    yield "single", case([0], [(0, 0), (-LIMIT, -1), (1, LIMIT)])
    # บ้านอยู่ที่ขอบทั้งสองข้าง และช่วงที่ครอบทั้งถนน
    yield "edges", case([-LIMIT, LIMIT, -LIMIT, LIMIT], [(-LIMIT, LIMIT), (-LIMIT, -LIMIT), (LIMIT, LIMIT), (-LIMIT + 1, LIMIT - 1)])
    # ปลายช่วงตรงกับตำแหน่งบ้านที่ซ้ำกันพอดี
    yield "ends-on-house", case([10, 20, 20, 20, 30, 40, 40], [(20, 40), (21, 39), (10, 20), (20, 20), (41, 50), (0, 9)])
    yield "rand1", case([random.randint(-1000, 1000) for _ in range(300)],
                        [random_query(-1100, 1100) for _ in range(300)])
    yield "rand2", case([random.randint(-LIMIT, LIMIT) for _ in range(5000)],
                        [random_query(-LIMIT, LIMIT) for _ in range(3000)])
    yield "rand3", case([random.randint(-20, 20) for _ in range(4000)],
                        [random_query(-25, 25) for _ in range(4000)])
    yield "big1", case([random.randint(-LIMIT, LIMIT) for _ in range(200000)],
                       [random_query(-LIMIT, LIMIT) for _ in range(200000)])
    yield "big2", case([random.randint(-1000, 1000) for _ in range(200000)],
                       [random_query(-1000, 1000) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
