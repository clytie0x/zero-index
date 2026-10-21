"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/06-matrix-multiply

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(706)
LIMIT = 10000


def table(rows):
    return "\n".join(" ".join(str(x) for x in row) for row in rows)


def make(a, b):
    n, m, p = len(a), len(b), len(b[0])
    assert len(a[0]) == m
    return f"{n} {m} {p}\n" + table(a) + "\n" + table(b)


def rand_matrix(r, c, low, high):
    return [[random.randint(low, high) for _ in range(c)] for _ in range(r)]


def cases():
    yield "sample1", make([[1, 2, 0], [-1, 3, 4]], [[2, 1], [0, -2], [5, 3]])
    yield "one", make([[-7]], [[6]])
    yield "dot", make([[1, 2, 3, 4]], [[5], [6], [7], [8]])
    yield "outer", make([[1], [-2], [3]], [[4, 5, -6, 7]])
    identity = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
    yield "identity", make(rand_matrix(3, 5, -50, 50), identity)
    yield "max-positive", make([[LIMIT] * 100 for _ in range(100)], [[LIMIT] * 100 for _ in range(100)])
    yield "max-negative", make([[-LIMIT] * 100 for _ in range(100)], [[LIMIT] * 100 for _ in range(100)])
    yield "max-mixed", make(rand_matrix(100, 100, -LIMIT, LIMIT), rand_matrix(100, 100, -LIMIT, LIMIT))
    for i in range(1, 3):
        n, m, p = random.randint(5, 30), random.randint(5, 30), random.randint(5, 30)
        yield f"rand{i}", make(rand_matrix(n, m, -100, 100), rand_matrix(m, p, -100, 100))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
