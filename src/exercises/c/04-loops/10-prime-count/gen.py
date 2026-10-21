"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/10-prime-count

ชุดที่ชื่อขึ้นต้นด้วย big มีจำนวนเฉพาะขนาดใหญ่หลายหมื่นตัวในช่วง
วิธีลองหารถึง x - 1 (naive.c) ไม่ทัน ชุดอื่นมีขนาดที่ naive.c ผ่านได้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(410)


def cases():
    yield "sample1", "1 10"
    yield "sample2", "10 20"
    yield "one", "1 1"
    yield "two", "2 2"
    yield "no-prime", "24 28"
    yield "hundred", "1 100"
    yield "top", "999000 1000000"
    yield "mid", "1 100000"
    for i in range(1, 3):
        a = random.randint(1, 50000)
        yield f"rand{i}", f"{a} {random.randint(a, a + 20000)}"
    yield "big1", "1 1000000"
    yield "big2", "500000 1000000"
    yield "big3", "2 999999"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
