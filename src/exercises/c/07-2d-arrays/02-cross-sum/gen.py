"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/02-cross-sum

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(702)
LIMIT = 10**9


def make(rows):
    return f"{len(rows)}\n" + "\n".join(" ".join(str(x) for x in row) for row in rows)


def rand_square(n, low, high):
    return make([[random.randint(low, high) for _ in range(n)] for _ in range(n)])


def cases():
    yield "sample1", make([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
    yield "sample2", make([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    yield "one", make([[-7]])
    yield "two", make([[1, -2], [-3, 4]])
    yield "max-even", make([[LIMIT] * 100 for _ in range(100)])
    yield "min-odd", make([[-LIMIT] * 99 for _ in range(99)])
    yield "odd-random", rand_square(99, -LIMIT, LIMIT)
    for i in range(1, 3):
        yield f"rand{i}", rand_square(random.randint(5, 30), -1000, 1000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
