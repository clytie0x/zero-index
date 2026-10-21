"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/03-base-convert   (รันที่รากของโปรเจกต์)

มีชุดที่ค่าเป็นศูนย์ ชุดที่มีเลข 0 นำหน้า และชุดที่ค่าเท่ากับ 10^18 ซึ่งเกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1203)

SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LIMIT = 10**18


def to_base(value, base):
    digits = ""
    while True:
        digits = SYMBOLS[value % base] + digits
        value //= base
        if value == 0:
            return digits


def case(value, from_base, to, zeros=0):
    digits = to_base(value, from_base)
    zeros = min(zeros, 60 - len(digits))  # โจทย์บอกว่า N ยาวไม่เกิน 60 ตัว
    return f"{'0' * zeros}{digits} {from_base} {to}"


def cases():
    yield "sample1", "11111101010 2 10"
    yield "sample2", "2026 10 16"
    yield "zero", "0 7 2"
    yield "zeros-only", "0000 5 36"
    yield "leading-zeros", "000101 2 10"
    yield "same-base", "ZZZ 36 36"
    yield "one-digit", "Z 36 2"
    yield "max-to-binary", case(LIMIT, 10, 2)
    yield "max-from-36", case(LIMIT, 36, 10)
    yield "max-binary-in", case(LIMIT, 2, 36)
    yield "long-input", case(12345, 3, 7, zeros=60 - len(to_base(12345, 3)))
    for i in range(1, 4):
        value = random.randint(1, LIMIT)
        yield f"rand{i}", case(value, random.randint(2, 36), random.randint(2, 36), zeros=random.randint(0, 2))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
