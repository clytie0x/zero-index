"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/02-digit-sum

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(602)


def number(digits):
    first = str(random.randint(1, 9))
    return first + "".join(str(random.randint(0, 9)) for _ in range(digits - 1))


def cases():
    yield "sample1", "2569"
    yield "min", "1"
    yield "single", "7"
    yield "ten", "10"
    yield "fits-long-long", "9223372036854775807"
    yield "over-long-long", "12345678901234567890"
    yield "max-nines", "9" * 1000
    yield "max-power", "1" + "0" * 999
    yield "max-rand", number(1000)
    yield "rand1", number(random.randint(20, 999))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_bytes((text + "\n").encode())


if __name__ == "__main__":
    main()
