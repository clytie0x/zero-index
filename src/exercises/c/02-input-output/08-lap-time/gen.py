"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/08-lap-time

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(208)


def lap(millis):
    return f"{millis // 60000}:{millis // 1000 % 60:02d}.{millis % 1000:03d}"


def case(*laps):
    return "\n".join(lap(m) for m in laps)


def cases():
    yield "sample1", case(65070, 62930, 70500)
    yield "sample2", case(59999, 1, 0)
    yield "zero", case(0, 0, 0)
    yield "small-millis", case(1, 2, 3)
    yield "max", case(3599999, 3599999, 3599999)
    yield "carry-seconds", case(45600, 30500, 44000)
    yield "leading-zero-millis", case(5007, 10010, 20040)
    for i in range(1, 3):
        yield f"rand{i}", case(*(random.randint(0, 3599999) for _ in range(3)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
