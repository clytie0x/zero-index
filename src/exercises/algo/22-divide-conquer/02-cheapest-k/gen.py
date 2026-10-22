"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/02-cheapest-k   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสินค้าห้าแสนชิ้น ตั้งใจให้วิธีหาค่าน้อยสุดทีละรอบใน naive.cpp ซึ่งเป็น O(NK) ไม่ทัน
big2 ซื้อครบทุกชิ้น ยอดรวมถึง 5 × 10^14 เกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2202)

TOP = 10**9


def build(k, prices):
    return f"{len(prices)} {k}\n" + " ".join(map(str, prices))


def cases():
    yield "sample1", "6 3\n120 45 300 45 80 999"
    yield "k-one", build(1, [500, 20, 999, 21, 300])
    yield "k-all", build(7, [9, 3, 7, 3, 1, 8, 2])
    yield "single", build(1, [TOP])
    yield "all-same", build(4, [250] * 9)
    # ราคาที่ตรงกับชิ้นที่ K พอดีมีหลายชิ้น ต้องซื้อแค่บางชิ้นในกลุ่มนั้น
    yield "ties-at-k", build(5, [10, 40, 40, 40, 40, 40, 90, 5, 40])
    yield "over-int", build(3000, [TOP - random.randint(0, 9) for _ in range(3000)])
    prices = [random.randint(1, TOP) for _ in range(2000)]
    yield "rand1", build(random.randint(1, 2000), prices)
    prices = [random.randint(1, 50) for _ in range(5000)]
    yield "rand2", build(2500, prices)
    n = 500000
    yield "big1", build(n // 2, [random.randint(1, TOP) for _ in range(n)])
    yield "big2", build(n, [random.randint(TOP // 2, TOP) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
