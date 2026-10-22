"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/04-mango-hives   (รันที่รากของโปรเจกต์)

naive.cpp ลองทั้งเขย่าและไม่เขย่าทุกต้นโดยไม่จด ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 30 ต้น
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนต้น ผลรวมเกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2404)

TOP = 10**9


def build(fruits):
    return f"{len(fruits)}\n" + " ".join(map(str, fruits))


def cases():
    yield "sample1", build([20, 50, 30, 10, 60, 40, 30])
    # greedy เขย่าต้นที่ผลมากที่สุดก่อนได้ 60 คำตอบคือ 50 + 50
    yield "sample2", build([50, 60, 50])
    yield "one", build([7])
    yield "two", build([3, 9])
    yield "all-zero", build([0] * 15)
    yield "all-max", build([TOP] * 29)
    # ต้องข้ามสองต้นติดกันบ้าง ไม่ใช่สลับเว้นต้นเสมอ
    yield "skip-two", build([10, 1, 1, 10, 1, 1, 10, 1, 1, 10])
    yield "rand1", build([random.randint(0, 50) for _ in range(25)])
    yield "rand2", build([random.randint(0, TOP) for _ in range(30)])
    yield "big1", build([random.randint(0, TOP) for _ in range(200000)])
    yield "big2", build([TOP - random.randint(0, 3) for _ in range(200000)])
    # ไฟล์เล็ก แต่ recursion ตรงๆ ที่ 70 ต้นต้องเรียกราว 6 × 10^14 ครั้ง
    yield "big3", build([random.randint(0, 100) for _ in range(70)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
