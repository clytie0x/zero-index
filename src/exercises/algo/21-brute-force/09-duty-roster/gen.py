"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/09-duty-roster   (รันที่รากของโปรเจกต์)

ชุดเล็กมี N ไม่เกิน 9 ให้ naive.cpp ที่ลองทุกการจับคู่ตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มี N = 13 ลองครบ 13! แบบไม่ทัน ต้องตัดกิ่ง
ชุด greedy ถ้าให้ครูแต่ละคนเลือกเวรที่ถูกที่สุดที่ยังว่างตามลำดับ จะได้คำตอบไม่ดีที่สุด
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2109)


def build(cost):
    return f"{len(cost)}\n" + "\n".join(" ".join(map(str, row)) for row in cost)


def random_cost(n, low, high):
    return [[random.randint(low, high) for _ in range(n)] for _ in range(n)]


def cases():
    yield "sample1", build([[4, 2, 8], [4, 3, 7], [3, 1, 6]])
    yield "sample2", build([[9, 1], [1, 9]])
    yield "one", build([[42]])
    # ครูคนแรกเลือกเวรถูกสุด (1) แล้วครูคนที่สองต้องรับเวรที่เหนื่อย 100 รวม 101 แต่สลับกันได้ 5
    yield "greedy", build([[1, 2], [3, 100]])
    yield "all-same", build([[5] * 9 for _ in range(9)])
    yield "max-cost", build(random_cost(8, 999000, 1000000))
    yield "rand1", build(random_cost(9, 1, 1000))
    yield "rand2", build(random_cost(9, 1, 3))
    yield "big1", build(random_cost(13, 1, 1000))
    yield "big2", build(random_cost(13, 90, 110))
    yield "big3", build(random_cost(13, 1, 1000000))
    yield "big4", build(random_cost(13, 1, 10))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
