"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/02-tired-climb   (รันที่รากของโปรเจกต์)

naive.cpp เป็น recursion ตรงๆ ที่แตกสองกิ่ง ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 30 ขั้น
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนขั้น ผลรวมเกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2402)

TOP = 10**9


def build(costs):
    return f"{len(costs)}\n" + " ".join(map(str, costs))


def cases():
    yield "sample1", build([3, 8, 2, 7, 1, 9])
    # greedy ที่ก้าวไปขั้นที่เหนื่อยน้อยกว่าทีละก้าวได้ 1 + 5 + 5 + 1 = 12 แต่คำตอบคือ 5 + 5 + 1 = 11
    yield "sample2", build([1, 5, 100, 5, 1])
    yield "one", build([42])
    yield "two", build([7, 3])
    yield "all-zero", build([0] * 20)
    yield "all-max", build([TOP] * 30)
    yield "rand1", build([random.randint(0, 20) for _ in range(25)])
    yield "rand2", build([random.randint(0, TOP) for _ in range(30)])
    yield "big1", build([random.randint(0, TOP) for _ in range(200000)])
    yield "big2", build([TOP - random.randint(0, 5) for _ in range(200000)])
    # ไฟล์เล็ก แต่ recursion ตรงๆ ที่ 70 ขั้นต้องเรียกราว 6 × 10^14 ครั้ง
    yield "big3", build([random.randint(0, 100) for _ in range(70)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
