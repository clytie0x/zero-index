"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/06-top-letter

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(606)

MAX = 100000


def shuffled(parts):
    chars = list("".join(parts))
    random.shuffle(chars)
    return "".join(chars)


def cases():
    yield "sample1", "Banana Bread"
    yield "sample2", "abc, cba!"
    yield "single", "Z"
    yield "one-among-noise", "!!! 42 x ???"
    yield "all-tie", string.ascii_uppercase
    yield "late-tie", "zzyy"
    # ถ้าไม่ tolower จะนับ M กับ m แยก แล้วตอบ a ผิด
    yield "max-case-mix", shuffled(["M" * 30000, "m" * 30000, "a" * 39000, " " * 1000])
    yield "max-same", "Q" * MAX
    pool = string.ascii_letters + string.digits + " .,!?"
    yield "max-rand", "".join(random.choice(pool) for _ in range(MAX))
    yield "rand1", "".join(random.choice(pool) for _ in range(random.randint(100, 5000)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, line in cases():
        (tests / f"{name}.in").write_bytes((line + "\n").encode())


if __name__ == "__main__":
    main()
