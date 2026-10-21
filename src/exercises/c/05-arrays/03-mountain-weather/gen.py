"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/03-mountain-weather   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(503)


def line(values):
    return " ".join(map(str, values))


def cases():
    yield "sample1", "7\n3 -1 5 5 -2 0 -2"
    yield "single", "1\n-7"
    # ทุกค่าติดลบ จับคนที่เริ่มค่ามากสุดที่ 0
    yield "all-negative", "5\n-18 -20 -16 -19 -16"
    # ทุกค่าเป็นบวก จับคนที่เริ่มค่าน้อยสุดที่ 0
    yield "all-positive", "6\n12 9 15 9 11 15"
    # เท่ากันหมด สูงสุดต้องตอบวันที่ 1 ต่ำสุดต้องตอบวันที่ N
    yield "all-equal", "5\n4 4 4 4 4"
    yield "extremes", "4\n50 -50 50 -50"
    yield "ends", "6\n-30 1 2 3 4 30"
    yield "rand1", f"1000\n{line(random.randint(-50, 50) for _ in range(1000))}"
    yield "rand2", f"60\n{line(random.randint(-10, 5) for _ in range(60))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
