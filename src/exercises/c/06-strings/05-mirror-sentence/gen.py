"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/05-mirror-sentence

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(605)

NOISE = " " * 6 + string.digits + ".,!?'-"
MAX = 100000


def decorate(letters, total):
    """สุ่มตัวพิมพ์ใหญ่เล็ก แล้วแทรกตัวที่ไม่ใช่ตัวอักษรจนยาว total ตัว"""
    out = [c.upper() if random.random() < 0.5 else c for c in letters]
    while len(out) < total:
        out.insert(random.randint(0, len(out)), random.choice(NOISE))
    return "".join(out)


def mirror(half, odd):
    middle = random.choice(string.ascii_lowercase) if odd else ""
    return half + middle + half[::-1]


def letters(n):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def cases():
    yield "sample1", "Was it a car or a cat I saw?"
    yield "sample2", "Hello, World"
    yield "single", "Q"
    yield "two-diff", "Ab"
    yield "case-only", "aBbA"
    # ตัวเลขต้องถูกข้าม ถ้านับตัวเลขด้วยจะได้ NO
    yield "digits-skip", "1a2b3b4a5"
    yield "ends-differ", "x" + "abcba" * 3 + "y"
    yield "max-yes", decorate(mirror(letters(35000), True), MAX)
    near = list(mirror(letters(40000), False))
    near[40000] = "a" if near[40000] != "a" else "b"
    yield "max-no-middle", decorate("".join(near), MAX)
    yield "max-same", "Z" * MAX
    yield "rand1", decorate(mirror(letters(200), False), 600)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, line in cases():
        (tests / f"{name}.in").write_bytes((line + "\n").encode())


if __name__ == "__main__":
    main()
