"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/08-nesting-boxes   (รันที่รากของโปรเจกต์)

naive.cpp เรียงตามความกว้างแล้วทำ DP แบบ O(N^2) ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 3000 ใบ
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนใบ ซึ่ง O(N^2) ไม่ทัน
หลายชุดมีกล่องกว้างเท่ากันแต่ยาวต่างกัน ถ้าเรียงความยาวจากน้อยไปมากเมื่อกว้างเท่ากัน จะนับกล่องพวกนี้ซ้อนกันผิดๆ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2508)

TOP = 10**9


def build(boxes):
    return f"{len(boxes)}\n" + "\n".join(f"{w} {h}" for w, h in boxes)


def cases():
    yield "sample1", build([(50, 40), (60, 70), (30, 50), (60, 45), (20, 20)])
    # กว้างเท่ากันทั้งหมด ซ้อนกันไม่ได้เลย
    yield "sample2", build([(10, 1), (10, 2), (10, 3), (10, 4)])
    yield "one", build([(TOP, TOP)])
    yield "all-same", build([(7, 7)] * 20)
    yield "chain", build([(i, 2 * i) for i in range(500, 0, -1)])
    yield "same-height", build([(i, 99) for i in range(1, 40)])
    # ความกว้างซ้ำเป็นกลุ่ม แต่ละกลุ่มมีความยาวเพิ่มขึ้นตามความกว้าง
    yield "width-groups", build([(w, w * 10 + k) for w in range(1, 30) for k in range(5)])
    yield "rand1", build([(random.randint(1, 10), random.randint(1, 10)) for _ in range(12)])
    yield "rand2", build([(random.randint(1, 200), random.randint(1, 200)) for _ in range(3000)])
    yield "big1", build([(random.randint(1, TOP), random.randint(1, TOP)) for _ in range(100000)])
    yield "big2", build([(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(100000)])
    boxes = [(w, w + k) for w in range(1, 20001) for k in range(5)]
    random.shuffle(boxes)
    yield "big3", build(boxes)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
