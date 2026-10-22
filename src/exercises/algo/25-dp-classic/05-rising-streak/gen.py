"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/05-rising-streak   (รันที่รากของโปรเจกต์)

naive.cpp เป็น DP แบบ O(N^2) ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 3000 ค่า
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนค่า ซึ่ง O(N^2) ไม่ทัน
big3 เพิ่มขึ้นแบบมีค่าซ้ำติดกันเป็นคู่ ใช้ upper_bound จะได้คำตอบเป็นสองเท่าของที่ถูก
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2505)

TOP = 10**9


def build(values):
    return f"{len(values)}\n" + " ".join(map(str, values))


def cases():
    yield "sample1", build([3, 1, 4, 1, 5, 9, 2, 6])
    yield "sample2", build([7, 7, 8, 8, 8, 9, 3])
    yield "one", build([-TOP])
    yield "all-equal", build([42] * 50)
    yield "decreasing", build(list(range(TOP, TOP - 300, -1)))
    yield "increasing", build(list(range(-TOP, -TOP + 3000)))
    yield "negative", build([random.randint(-TOP, -TOP + 40) for _ in range(30)])
    yield "rand1", build([random.randint(1, 20) for _ in range(25)])
    yield "rand2", build([random.randint(-TOP, TOP) for _ in range(3000)])
    yield "big1", build([random.randint(-TOP, TOP) for _ in range(200000)])
    yield "big2", build([random.randint(-50, 50) for _ in range(200000)])
    yield "big3", build([i // 2 for i in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
