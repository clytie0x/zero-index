"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/10-shopping-subsets   (รันที่รากของโปรเจกต์)

ชุดเล็กมี N ไม่เกิน 22 ให้ naive.cpp ที่ลองครบ 2^N แบบตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มี N ถึง 40 ลองครบไม่ทัน และคำตอบใหญ่จนนับทีละแบบไม่ไหว
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2110)


def build(budget, prices):
    return f"{len(prices)} {budget}\n" + " ".join(map(str, prices))


def cases():
    yield "sample1", build(10, [3, 5, 7, 2])
    yield "sample2", build(0, [4, 1, 6])
    yield "one-fits", build(5, [5])
    yield "one-too-big", build(4, [5])
    yield "all-fit", build(10**10, [random.randint(1, 10**9) for _ in range(10)])
    yield "same-price", build(30, [10] * 12)
    prices = [random.randint(1, 1000) for _ in range(21)]
    yield "rand-odd", build(sum(prices) // 3, prices)
    prices = [random.randint(1, 10**9) for _ in range(22)]
    yield "rand-even", build(sum(prices) // 2, prices)
    # ทุกตะกร้าไม่เกินงบ คำตอบคือ 2^40 เกิน int มาก
    yield "big-all", build(4 * 10**10, [10**9] * 40)
    prices = [random.randint(1, 10**9) for _ in range(40)]
    yield "big-half", build(sum(prices) // 2, prices)
    prices = [random.randint(1, 10**9) for _ in range(39)]
    yield "big-odd", build(sum(prices) // 4, prices)
    prices = [random.randint(10**8, 10**9) for _ in range(40)]
    yield "big-small-budget", build(2 * 10**9, prices)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
