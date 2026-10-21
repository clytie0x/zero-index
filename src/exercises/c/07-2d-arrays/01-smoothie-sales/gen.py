"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/01-smoothie-sales

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(701)


def table(rows):
    return "\n".join(" ".join(str(x) for x in row) for row in rows)


def make(n, m, rows):
    return f"{n} {m}\n" + table(rows)


def rand_table(n, m, low, high):
    return make(n, m, [[random.randint(low, high) for _ in range(m)] for _ in range(n)])


def cases():
    yield "sample1", make(3, 4, [[12, 5, 8, 3], [7, 15, 10, 9], [9, 11, 6, 14]])
    yield "min", make(1, 1, [[0]])
    yield "all-zero", make(3, 5, [[0] * 5 for _ in range(3)])
    # วันที่ 2 กับ 4 ยอดรวม 10 เท่ากัน เมนูที่ 1 กับ 3 ยอดรวม 12 เท่ากัน ต้องตอบหมายเลขน้อย
    yield "ties", make(4, 3, [[1, 2, 2], [5, 0, 5], [2, 2, 2], [4, 3, 3]])
    yield "one-row", rand_table(1, 100, 0, 1000)
    yield "one-column", rand_table(100, 1, 0, 1000)
    yield "last-wins", make(3, 3, [[1, 1, 1], [2, 2, 2], [3, 3, 9]])
    yield "max", make(100, 100, [[1000] * 100 for _ in range(100)])
    for i in range(1, 3):
        n, m = random.randint(20, 100), random.randint(20, 100)
        yield f"rand{i}", rand_table(n, m, 0, 1000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
