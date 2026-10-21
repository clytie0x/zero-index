"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/09-expand

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(609)

MAX_FULL = 100000
MAX_CODE = 10000


def encode(groups):
    return "".join(f"{letter}{count}" for letter, count in groups)


def random_groups(max_count, full_limit, code_limit):
    groups, full, code = [], 0, 0
    while True:
        letter = random.choice(string.ascii_lowercase)
        count = random.randint(1, max_count)
        size = 1 + len(str(count))
        if full + count > full_limit or code + size > code_limit:
            return groups
        groups.append((letter, count))
        full += count
        code += size


def cases():
    yield "sample1", "a3b1c2"
    yield "sample2", "x12y5"
    yield "min", "z1"
    yield "max-one-group", "q100000"
    # ตัวเลขที่มี 0 อยู่ข้างใน ถ้าอ่านแค่หลักเดียวจะได้ 1
    yield "inner-zero", "a10b100c1000"
    yield "same-letter", "m2m3m1"
    yield "max-code-ones", encode((random.choice(string.ascii_lowercase), 1) for _ in range(MAX_CODE // 2))
    yield "max-rand", encode(random_groups(60, MAX_FULL, MAX_CODE))
    yield "max-big-counts", encode(random_groups(20000, MAX_FULL, MAX_CODE))
    yield "rand1", encode(random_groups(15, 500, 200))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_bytes((text + "\n").encode())


if __name__ == "__main__":
    main()
