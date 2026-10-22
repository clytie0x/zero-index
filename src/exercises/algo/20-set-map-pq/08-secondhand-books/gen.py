"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/08-secondhand-books   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีหนังสือและลูกค้าอย่างละสองแสน ตั้งใจให้การไล่ดูทุกเล่มใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2008)

TOP = 10**9


def case(prices, budgets):
    return f"{len(prices)} {len(budgets)}\n" + " ".join(map(str, prices)) + "\n" + " ".join(map(str, budgets))


def cases():
    yield "sample1", case([120, 80, 250, 80, 40], [100, 100, 100, 30, 300, 260])
    yield "sample2", case([50], [49, 50, 50])
    # ราคาซ้ำหลายเล่ม ขายทีละเล่ม erase ด้วยราคาจะลบหายหมด
    yield "same-price", case([60] * 5, [60] * 7)
    # งบเท่ากับราคาพอดีต้องซื้อได้
    yield "exact-budget", case([10, 20, 30], [30, 20, 10, 30])
    yield "extremes", case([1, TOP, TOP, 1], [TOP - 1, TOP, 1, 1, TOP, TOP])
    yield "all-too-poor", case([500, 600, 700], [499, 1, 100, 499])
    yield "rand1", case([random.randint(1, 100) for _ in range(500)], [random.randint(1, 100) for _ in range(700)])
    yield "rand2", case([random.randint(1, TOP) for _ in range(6000)], [random.randint(1, TOP) for _ in range(6000)])
    yield "big1", case([random.randint(1, TOP) for _ in range(200000)], [random.randint(1, TOP) for _ in range(200000)])
    yield "big2", case([random.randint(1, 1000) for _ in range(200000)], [random.randint(500, 1000) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
