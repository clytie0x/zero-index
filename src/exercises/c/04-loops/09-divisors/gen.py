"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/09-divisors

ชุดที่ชื่อขึ้นต้นด้วย big มี N ใกล้ 10^12 วิธีลองหาร 1 ถึง N (naive.c) ไม่ทัน
ชุดอื่นมี N ไม่เกิน 10^7 ให้ naive.c ผ่านได้ เพื่อตรวจว่าเฉลยกับวิธีช้าตอบตรงกัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(409)


def cases():
    yield "sample1", "12"
    yield "sample2", "36"
    yield "one", "1"
    yield "prime", "999983"
    yield "square", "1000000"
    yield "many", "720720"
    yield "small-max", "10000000"
    for i in range(1, 3):
        yield f"rand{i}", str(random.randint(2, 10**7))
    yield "big1", "999999999989"
    yield "big2", str(10**12)
    yield "big3", "963761198400"
    yield "big4", str(999999 * 999999)
    yield "big5", str(random.randint(9 * 10**11, 10**12))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
