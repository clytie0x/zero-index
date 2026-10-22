"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/04-sorted-pairs   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้วิธีไล่ทุกคู่ใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1804)
MAX_P = 10**9


def case(k, prices):
    prices = sorted(prices)
    return f"{len(prices)} {k}\n" + " ".join(map(str, prices))


def distinct(n, low, high):
    return random.sample(range(low, high + 1), n)


def cases():
    yield "sample1", case(1000, [150, 300, 450, 550, 700, 850, 990])
    yield "sample2", case(20, [1, 5, 10, 15, 19])
    yield "single", case(2, [1])
    # ชิ้นเดียวที่ราคาครึ่งหนึ่งของ K ห้ามจับคู่กับตัวเอง
    yield "half-k", case(100, [10, 50, 70, 95])
    # ราคารวมเกิน int
    yield "over-int", case(2 * MAX_P - 1, [1, 2, MAX_P - 1, MAX_P])
    yield "none", case(3, distinct(2000, 2, MAX_P))
    # ทุกชิ้นจับคู่ได้ คำตอบคือ N / 2
    yield "all-match", case(3001, list(range(1, 3001)))
    prices = distinct(10000, 1, 30000)
    yield "rand1", case(30001, prices)
    prices = distinct(8000, 1, MAX_P)
    yield "rand2", case(sum(random.sample(prices, 2)), prices)
    # ทุกชิ้นจับคู่ได้ คำตอบ 100000
    yield "big1", case(200001, list(range(1, 200001)))
    prices = distinct(200000, 1, 1000000)
    yield "big2", case(1000001, prices)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
