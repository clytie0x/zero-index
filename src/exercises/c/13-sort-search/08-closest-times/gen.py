"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/08-closest-times   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นแสน ตั้งใจให้การเทียบทุกคู่ใน naive.c ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1308)

LIMIT = 2 * 10**9


def line(values):
    return " ".join(map(str, values))


def case(values):
    return f"{len(values)}\n{line(values)}"


def cases():
    yield "sample1", case([350, -120, 900, 410, 15, 470])
    yield "sample2", case([8, 3, 8, 3, 8])
    # ผลต่าง 4 × 10^9 เกิน int
    yield "two-extremes", case([LIMIT, -LIMIT])
    # ค่าใหญ่ทั้งบวกและลบ ฟังก์ชันเปรียบเทียบแบบลบกันจะเรียงผิด
    yield "overflow-compare", case([LIMIT, -LIMIT, 1500000000, -1500000000, 7, -7, 1999999000, -1999999000])
    yield "all-same-small", case([-5] * 7)
    yield "equal-gaps", case(list(range(-1000, 1001, 250)))
    yield "rand1", case([random.randint(-10**6, 10**6) for _ in range(1000)])
    yield "rand2", case([random.randint(-LIMIT, LIMIT) for _ in range(5000)])
    yield "big1", case([random.randint(-LIMIT, LIMIT) for _ in range(100000)])
    # ทุกค่าเท่ากัน จำนวนคู่ 4999950000 เกิน int
    yield "big2", case([123456789] * 100000)
    spread = random.sample(range(-LIMIT, LIMIT, 40000), 100000)
    yield "big3", case(spread)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
