"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/10-skip-one-day   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกคู่วันเริ่มวันจบ แล้วตัดวันที่คะแนนน้อยที่สุดในช่วง O(N^2)
ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 3000 วัน ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนวัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2410)

TOP = 10**9


def build(scores):
    return f"{len(scores)}\n" + " ".join(map(str, scores))


def cases():
    yield "sample1", build([6, -9, 5, -1, 4])
    yield "sample2", build([-4, -2, -7])
    yield "one", build([-5])
    yield "two-negative", build([-3, -8])
    # ตัดวันเดียวทิ้งไม่ได้ ต้องเหลืออย่างน้อยหนึ่งวัน
    yield "one-positive-rest", build([-1, -1, 5, -1, -1])
    # ไม่ตัดเลยดีที่สุด
    yield "all-positive", build([TOP] * 40)
    yield "all-min", build([-TOP] * 40)
    # ตัดได้แค่วันเดียว วันลบวันที่สองต้องเลี่ยงด้วยการเลือกช่วงให้สั้นลง
    yield "two-dips", build([10, -20, 10, -20, 10])
    yield "rand1", build([random.randint(-10, 10) for _ in range(60)])
    yield "rand2", build([random.randint(-TOP, TOP) for _ in range(3000)])
    yield "rand3", build([random.randint(-30, 10) for _ in range(3000)])
    yield "big1", build([random.randint(-TOP, TOP) for _ in range(200000)])
    yield "big2", build([random.choice([TOP, TOP, -TOP]) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
