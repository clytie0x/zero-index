"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/01-frog-hops   (รันที่รากของโปรเจกต์)

naive.cpp เป็น recursion ตรงๆ ที่แตกสามกิ่ง ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมี N ไม่เกิน 30
ชุดที่ชื่อขึ้นต้นด้วย big มี N เกือบล้าน ซึ่ง recursion ตรงๆ ไม่ทัน และคำตอบจริงเกิน 1000000007 มาก
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2401)


def cases():
    yield "sample1", "4"
    yield "sample2", "6"
    yield "one", "1"
    yield "two", "2"
    yield "three", "3"
    yield "thirty", "30"
    yield "rand1", str(random.randint(10, 20))
    yield "rand2", str(random.randint(21, 29))
    yield "big1", "1000000"
    yield "big2", str(random.randint(900000, 999999))
    # ไฟล์เล็ก แต่ recursion ตรงๆ ต้องเรียกราว 10^16 ครั้ง ไม่ทันโดยไม่ต้องพังเพราะ stack
    yield "big3", "60"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
