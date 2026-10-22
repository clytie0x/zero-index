"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/06-price-drop   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนวัน ตั้งใจให้วิธีลองทุกคู่ใน naive.cpp ไม่ทัน
big2 ราคาลดลงทุกวันและ D = 0 คำตอบ 19999900000 เกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2206)

TOP = 10**9


def build(drop, prices):
    return f"{len(prices)} {drop}\n" + " ".join(map(str, prices))


def cases():
    yield "sample1", "6 10\n100 85 120 95 70 110"
    yield "single", build(0, [500])
    yield "rising", build(0, list(range(1, 1001)))
    # ลดลงพอดี D ไม่นับ ต้องลดมากกว่า D
    yield "exact-drop", build(5, [20, 15, 10, 15, 20, 9, 14])
    yield "zero-drop", build(0, [3, 3, 2, 3, 1, 1, 2])
    yield "huge-drop", build(TOP, [TOP, 1, TOP, 1, TOP])
    yield "near-top", build(TOP - 2, [TOP, 1, TOP, 2, TOP - 1, 1])
    yield "rand1", build(random.randint(0, 10**8), [random.randint(1, TOP) for _ in range(2000)])
    yield "rand2", build(3, [random.randint(1, 20) for _ in range(3000)])
    n = 200000
    yield "big1", build(random.randint(0, TOP // 2), [random.randint(1, TOP) for _ in range(n)])
    yield "big2", build(0, list(range(TOP, TOP - n, -1)))
    yield "big3", build(10, [random.randint(1, 100) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
