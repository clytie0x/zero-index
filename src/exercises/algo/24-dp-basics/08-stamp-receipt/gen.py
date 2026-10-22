"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/08-stamp-receipt   (รันที่รากของโปรเจกต์)

naive.cpp ลองจำนวนดวงทีละค่า แล้วค้นทุกชุดที่เรียงจากมากไปน้อยโดยไม่จด
ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมี X ไม่เกิน 40 และแสตมป์ไม่เกิน 5 แบบ
ชุดที่ชื่อขึ้นต้นด้วย big มี X ถึงแสน ใบเสร็จยาวได้ถึงหลายหมื่นดวง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2408)


def build(target, prices):
    return f"{len(prices)} {target}\n" + " ".join(map(str, prices))


def cases():
    yield "sample1", build(13, [3, 1, 4])
    # 3 1 กับ 2 2 ใช้ 2 ดวงเท่ากัน ต้องตอบ 3 1
    yield "sample2", build(4, [2, 1, 3])
    yield "sample3", build(23, [7, 5])
    yield "one-price", build(40, [8])
    yield "exact", build(9, [2, 9, 4])
    # หยิบดวงแพงสุดก่อนได้ 9 1 1 1 สี่ดวง คำตอบคือ 6 6
    yield "not-greedy", build(12, [9, 6, 1])
    # 11 1, 10 2, ..., 6 6 ใช้ 2 ดวงเท่ากันหมด ต้องตอบ 11 1
    yield "many-ties", build(12, [7, 2, 10, 5, 1, 8, 11, 4, 3, 9, 6])
    yield "rand1", build(37, random.sample(range(1, 12), 4))
    yield "rand2", build(40, random.sample(range(2, 20), 5))
    yield "big1", build(100000, random.sample(range(1, 1001), 100))
    yield "big2", build(99999, [1, 3, 4])
    # แสตมป์ราคาคู่ทั้งหมด ราคาคี่จึงทำไม่ได้ ต้องเติมตารางจนครบถึงจะรู้
    yield "big3", build(99999, random.sample(range(2, 100001, 2), 100))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
