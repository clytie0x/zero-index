"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/09-no-repeat-jumps   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกระยะที่ไม่ซ้ำก้าวล่าสุดโดยไม่จด ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมี N ไม่เกิน 40
ชุดที่ชื่อขึ้นต้นด้วย big มี N เกือบล้าน คำตอบเกิน 1000000007
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2409)


def cases():
    yield "sample1", "4"
    yield "sample2", "7"
    yield "one", "1"
    yield "two", "2"
    yield "three", "3"
    yield "forty", "40"
    yield "rand1", str(random.randint(10, 20))
    yield "rand2", str(random.randint(25, 35))
    yield "big1", "1000000"
    yield "big2", str(random.randint(500000, 999999))
    # ไฟล์เล็ก แต่ recursion ตรงๆ ที่ 90 ขั้นต้องเรียกราว 2 × 10^14 ครั้ง
    yield "big3", "90"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
