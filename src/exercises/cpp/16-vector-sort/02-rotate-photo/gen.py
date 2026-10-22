"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/02-rotate-photo   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี R × C เต็มขอบเขต 200000 ไม่เก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1602)


def line(values):
    return " ".join(map(str, values))


def case(photo):
    rows = len(photo)
    cols = len(photo[0])
    return f"{rows} {cols}\n" + "\n".join(line(row) for row in photo)


def random_photo(rows, cols):
    return [[random.randint(0, 255) for _ in range(cols)] for _ in range(rows)]


def cases():
    yield "sample1", case([[1, 2, 3], [4, 5, 6]])
    yield "sample2", case([[0, 255], [128, 64], [10, 20]])
    yield "single", case([[7]])
    yield "one-row", case([list(range(1, 11))])
    yield "one-column", case([[v] for v in range(1, 11)])
    yield "square", case([[r * 4 + c for c in range(4)] for r in range(4)])
    yield "rand1", case(random_photo(7, 13))
    yield "rand2", case(random_photo(150, 80))
    yield "big1", case(random_photo(1, 200000))
    yield "big2", case(random_photo(200000, 1))
    yield "big3", case(random_photo(400, 500))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
