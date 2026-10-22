"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/07-mango-route   (รันที่รากของโปรเจกต์)

naive.cpp เดินทุกเส้นทางตามลำดับพจนานุกรม (D ก่อน R) แล้วเก็บเส้นแรกที่ได้คะแนนมากสุด
ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีตารางไม่เกิน 10 × 10
ชุดที่ชื่อขึ้นต้นด้วย big มีตาราง 1000 × 1000 ซึ่งเดินทุกเส้นทางไม่ทัน
หลายชุดใช้คะแนนแค่ 0 กับ 1 ให้มีเส้นทางที่ได้เท่ากันเยอะ เพื่อตรวจการเลือกตอนเสมอ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2507)

TOP = 10**9


def build(grid):
    return f"{len(grid)} {len(grid[0])}\n" + "\n".join(" ".join(map(str, row)) for row in grid)


def random_grid(rows, cols, low, high):
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def cases():
    yield "sample1", build([[3, 1, 0, 7], [4, 8, 2, 1], [0, 6, 9, 3]])
    # ทั้งสามเส้นได้ 3 เท่ากัน ต้องตอบ DRR
    yield "sample2", build([[1, 2, 0], [2, 0, 0]])
    yield "one-row", build([[5, -3, 8, 0, 2]])
    yield "one-column", build([[-1], [-2], [-3]])
    yield "all-zero", build([[0] * 6 for _ in range(4)])
    yield "all-negative", build(random_grid(5, 6, -TOP, -1))
    # ย้อนจากท้ายแล้วเลือกขึ้นบนตอนเสมอ จะได้เส้นทางที่ไม่ใช่ตัวแรกตามพจนานุกรม
    yield "tie-trap", build([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    yield "binary1", build(random_grid(8, 9, 0, 1))
    yield "binary2", build(random_grid(10, 10, 0, 1))
    yield "rand1", build(random_grid(10, 10, -TOP, TOP))
    yield "big1", build(random_grid(1000, 1000, 0, 1))
    yield "big2", build(random_grid(1000, 1000, -TOP, TOP))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
