"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/05-best-streak   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกคู่วันเริ่มวันจบ O(N^2) ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 3000 วัน
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนวัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2405)

TOP = 10**9


def build(profits):
    return f"{len(profits)}\n" + " ".join(map(str, profits))


def cases():
    yield "sample1", build([-3, 5, -2, 4, -6, 3, 2, -1])
    yield "sample2", build([-5, -2, -8, -3])
    yield "one", build([-7])
    # ทุกช่วงที่มีแต่ 0 ได้เท่ากัน ต้องตอบ 1 1
    yield "all-zero", build([0] * 10)
    # สองช่วงได้ 6 เท่ากัน ช่วงแรกเริ่มเร็วกว่า
    yield "tie-later", build([1, 5, -10, 6, -20, 2, 4])
    # ต่อด้วยช่วงผลรวม 0 ได้เท่ากัน ต้องตอบช่วงที่จบเร็วกว่า
    yield "tie-zero-tail", build([4, -4, 0, 3, -3])
    # ช่วงก่อนหน้าผลรวม 0 ต้องต่อ เพื่อให้เริ่มเร็วที่สุด
    yield "tie-zero-head", build([2, -2, 5, -1])
    yield "all-positive", build([TOP] * 50)
    yield "all-min", build([-TOP] * 50)
    yield "rand1", build([random.randint(-20, 20) for _ in range(60)])
    yield "rand2", build([random.randint(-3, 3) for _ in range(3000)])
    yield "rand3", build([random.randint(-TOP, TOP) for _ in range(3000)])
    yield "big1", build([random.randint(-TOP, TOP) for _ in range(200000)])
    yield "big2", build([random.randint(-2, 2) for _ in range(200000)])
    yield "big3", build([TOP - random.randint(0, 2 * TOP) // 50 for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
