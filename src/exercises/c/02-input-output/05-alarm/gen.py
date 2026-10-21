"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/05-alarm

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(205)


def case(hour, minute, wait):
    return f"{hour:02d}:{minute:02d}\n{wait}"


def cases():
    yield "sample1", case(7, 45, 30)
    yield "sample2", case(23, 30, 45)
    yield "zero", case(0, 0, 0)
    yield "to-midnight", case(23, 59, 1)
    yield "one-day", case(12, 34, 1440)
    yield "same-hour", case(9, 5, 3)
    yield "max", case(23, 59, 1000000)
    for i in range(1, 4):
        yield f"rand{i}", case(random.randint(0, 23), random.randint(0, 59), random.randint(0, 1000000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
