"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/05-doubling-count   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N ตั้งแต่ 10^9 ขึ้นไป ตั้งใจให้การรันลูปตรงๆ ใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1805)


def cases():
    yield "sample1", "5"
    yield "sample2", "16"
    yield "min", "1"
    yield "two", "2"
    yield "power-minus", "1023"
    yield "power", "1024"
    yield "million", "1000000"
    yield "rand1", str(random.randint(10**6, 10**7))
    yield "big1", "1000000000"
    yield "big2", str(2**49)
    yield "big3", str(random.randint(10**12, 10**15))
    yield "big4", "1000000000000000"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
