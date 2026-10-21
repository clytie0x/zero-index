"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/04-seat-code

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(204)


def case(room, row, seat):
    return f"{room}\n{row}\n{seat}"


def cases():
    yield "sample1", case(402, "B", 7)
    yield "min", case(100, "A", 1)
    yield "max", case(999, "Z", 99)
    yield "two-digit-seat", case(315, "K", 10)
    yield "seat-nine", case(220, "C", 9)
    for i in range(1, 4):
        yield f"rand{i}", case(random.randint(100, 999), random.choice(string.ascii_uppercase), random.randint(1, 99))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
