"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/03-char-kinds

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(603)

PUNCT = ".,!?:;'-()"


def text(length, pool):
    return "".join(random.choice(pool) for _ in range(length))


def cases():
    yield "sample1", "Bus 8 leaves at 7:45 AM."
    yield "single", "x"
    yield "only-spaces", "     "
    yield "edge-spaces", "   Hi there 42   "
    yield "punct-only", "!?.,;:"
    yield "digits", "0123456789"
    yield "max-no-space", text(1000, string.ascii_letters + string.digits + PUNCT)
    pool = string.ascii_letters + string.digits + PUNCT + " " * 12
    yield "max-mixed", text(1000, pool)
    yield "rand1", text(random.randint(50, 900), pool)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, line in cases():
        (tests / f"{name}.in").write_bytes((line + "\n").encode())


if __name__ == "__main__":
    main()
