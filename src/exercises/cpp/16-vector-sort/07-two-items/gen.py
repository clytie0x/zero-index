"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/07-two-items   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้การเทียบทุกคู่ใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1607)

MAX_SIZE = 2 * 10**9


def line(values):
    return " ".join(map(str, values))


def case(sizes, space):
    return f"{len(sizes)} {space}\n{line(sizes)}"


def cases():
    yield "sample1", case([700, 300, 1200, 500, 900], 1500)
    yield "sample2", case([4, 4, 4, 4], 8)
    yield "two-fit", case([1, 1], 2)
    yield "two-no-fit", case([1, 2], 2)
    # ขนาดรวมของสองไฟล์ใหญ่สุดเกิน int
    yield "huge-files", case([MAX_SIZE, MAX_SIZE, MAX_SIZE - 1, 1], 4 * 10**9)
    yield "none", case([MAX_SIZE] * 6, 3 * 10**9)
    yield "rand1", case([random.randint(1, 1000) for _ in range(300)], random.randint(200, 1800))
    yield "rand2", case([random.randint(1, MAX_SIZE) for _ in range(5000)], random.randint(10**9, 4 * 10**9))
    yield "rand3", case([random.randint(1, 50) for _ in range(5000)], 50)
    yield "big1", case([random.randint(1, MAX_SIZE) for _ in range(200000)], 2 * 10**9)
    # ทุกคู่ใส่ได้ จำนวนคู่ 4999950000 เกิน int
    yield "big2", case([1] * 100000, 4 * 10**9)
    yield "big3", case([random.randint(1, 10**6) for _ in range(200000)], 10**6)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
