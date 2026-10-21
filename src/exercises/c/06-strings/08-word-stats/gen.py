"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/08-word-stats

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(608)

MAX = 100000


def word(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def paragraph(total, max_word, max_gap):
    parts = [" " * random.randint(0, max_gap)]
    while sum(map(len, parts)) < total:
        parts.append(word(random.randint(1, max_word)))
        parts.append(" " * random.randint(1, max_gap))
    return "".join(parts)[:total]


def cases():
    yield "sample1", "my school  has a big   library"
    yield "sample2", "   hello   "
    yield "single", "a"
    yield "only-spaces", " " * 1000
    yield "max-spaces", " " * MAX
    yield "max-one-word", word(MAX)
    yield "max-tiny-words", " ".join("x" * MAX)[:MAX]
    yield "max-rand", paragraph(MAX, 15, 4)
    yield "long-last", "a bb ccc " + word(5000)
    yield "rand1", paragraph(random.randint(50, 3000), 12, 3)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, line in cases():
        (tests / f"{name}.in").write_bytes((line + "\n").encode())


if __name__ == "__main__":
    main()
