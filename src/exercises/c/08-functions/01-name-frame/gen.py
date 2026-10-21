"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/01-name-frame

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(801)
LETTERS = string.ascii_letters + string.digits


def word(length):
    return "".join(random.choice(LETTERS) for _ in range(length))


def cases():
    yield "sample1", "POSN 1"
    yield "sample2", "Ann 0"
    yield "min", "A 0"
    # ชื่อสั้นแต่เว้นมาก ช่องว่างข้างในกว้างกว่าชื่อหลายเท่า
    yield "wide-pad", "X 5"
    yield "max", f"{word(50)} 5"
    yield "digits", "2569 2"
    yield "long-no-pad", f"{word(50)} 0"
    for i in range(1, 4):
        yield f"rand{i}", f"{word(random.randint(1, 50))} {random.randint(0, 5)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
