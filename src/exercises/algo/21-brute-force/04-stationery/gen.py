"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/04-stationery   (รันที่รากของโปรเจกต์)

ชุดเล็กมี M ไม่เกิน 300 ให้ลูปสามชั้นใน naive.cpp ตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มีราคาถูกและ M ถึง 10000 ลูปสามชั้นต้องลองเกิน 10^10 แบบ ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2104)


def cases():
    yield "sample1", "2 3 5 10"
    yield "sample2", "4 6 10 7"
    yield "min", "1 1 1 1"
    yield "too-expensive", "100 100 100 99"
    yield "one-way", "100 99 98 100"
    yield "same-price", "7 7 7 210"
    yield "rand1", f"{random.randint(1, 10)} {random.randint(1, 10)} {random.randint(1, 10)} {random.randint(100, 300)}"
    yield "rand2", f"{random.randint(1, 100)} {random.randint(1, 100)} {random.randint(1, 100)} {random.randint(200, 300)}"
    # ราคา 1 บาททุกอย่าง คำตอบเกือบ 5 × 10^7
    yield "big1", "1 1 1 10000"
    yield "big2", "1 2 3 10000"
    yield "big3", "3 1 2 9999"
    yield "big4", "2 4 6 9999"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
