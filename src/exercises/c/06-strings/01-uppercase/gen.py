"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/01-uppercase

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(601)


def word(length, letters=string.ascii_letters):
    return "".join(random.choice(letters) for _ in range(length))


def cases():
    yield "sample1", "Sports"
    yield "min-lower", "a"
    yield "min-upper", "Z"
    yield "edges", "azAZ"
    yield "all-upper", "OPENHOUSE"
    yield "max-lower", word(100, string.ascii_lowercase)
    yield "max-mixed", word(100)
    for i in range(1, 3):
        yield f"rand{i}", word(random.randint(2, 99))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_bytes((text + "\n").encode())


if __name__ == "__main__":
    main()
