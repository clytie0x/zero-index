"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/08-chicken-rice-shop   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1408)


def build(k, customers):
    rows = [f"{len(customers)} {k}"] + [f"{t} {s}" for t, s in customers]
    return "\n".join(rows)


def random_day(n, k, max_gap, max_cook):
    t = random.randint(0, 100)
    customers = []
    for _ in range(n):
        t += random.randint(0, max_gap)
        customers.append((t, random.randint(1, max_cook)))
    return build(k, customers)


def cases():
    yield "sample1", build(1, [(0, 5), (1, 3), (2, 4), (5, 2), (6, 1), (8, 2)])
    yield "sample2", build(2, [(10, 3), (13, 2), (13, 4), (14, 1)])
    yield "one", build(1, [(1000000000, 100000)])
    # มาห่างกันจนไม่มีใครต้องรอ
    yield "no-wait", build(1, [(i * 10, 10) for i in range(8)])
    # มาพร้อมกันหมด เก้าอี้ตัวเดียว
    yield "same-time", build(1, [(0, 3)] * 5)
    # ทำเสร็จตรงเวลาที่คนใหม่มาถึงพอดีทุกครั้ง ต้องทำเสร็จก่อนแล้วค่อยดูคนใหม่
    yield "exact-finish", build(1, [(0, 4), (1, 4), (4, 4), (8, 4), (9, 1), (12, 1), (12, 1), (13, 1)])
    # แสนคนมาพร้อมกันที่เวลา 10^9 จานละแสนนาที เวลาเกิน int
    n = 100000
    yield "big-long-day", build(n, [(1000000000, 100000)] * n)
    yield "rand1", random_day(12, 2, 4, 6)
    yield "rand2", random_day(2000, random.randint(1, 20), 10, 15)
    yield "big-rand3", random_day(100000, random.randint(5, 50), 3, 8)
    yield "big-rand4", random_day(100000, 1, 50, 100)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
