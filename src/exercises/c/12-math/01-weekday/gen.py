"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/01-weekday   (รันที่รากของโปรเจกต์)

ชุดที่ K ติดลบจับโปรแกรมที่ใช้ % ตรงๆ ชุด max และ min จับโปรแกรมที่เก็บ K ใน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1201)

LIMIT = 10**18


def cases():
    yield "sample1", "3 -12"
    yield "sample2", "0 10"
    yield "no-shift", "5 0"
    yield "back-one", "0 -1"
    yield "forward-one", "6 1"
    yield "back-week", "2 -7"
    yield "over-int", "1 3000000001"
    yield "max", f"6 {LIMIT}"
    yield "min", f"0 {-LIMIT}"
    yield "min-saturday", f"6 {-LIMIT}"
    for i in range(1, 3):
        yield f"rand-back{i}", f"{random.randint(0, 6)} {random.randint(-LIMIT, -1)}"
    yield "rand-forward", f"{random.randint(0, 6)} {random.randint(1, LIMIT)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
