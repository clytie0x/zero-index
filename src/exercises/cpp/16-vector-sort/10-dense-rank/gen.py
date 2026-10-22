"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/10-dense-rank   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้การไล่นับใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1610)

LIMIT = 10**9


def line(values):
    return " ".join(map(str, values))


def case(points):
    return f"{len(points)}\n{line(points)}"


def cases():
    yield "sample1", case([85, 90, 70, 85])
    yield "sample2", case([300, 1200, 300, 950, 1200, 0, 950])
    yield "single", case([0])
    yield "all-same", case([LIMIT] * 10)
    yield "all-different", case(list(range(20, 0, -1)))
    yield "extremes", case([0, LIMIT, 0, LIMIT, 1, LIMIT - 1])
    yield "rand1", case([random.randint(0, 50) for _ in range(300)])
    yield "rand2", case([random.randint(0, LIMIT) for _ in range(5000)])
    yield "rand3", case([random.choice([10, 20, 30]) * random.randint(1, 3) for _ in range(5000)])
    yield "big1", case([random.randint(0, LIMIT) for _ in range(200000)])
    yield "big2", case(random.sample(range(0, LIMIT), 200000))
    yield "big3", case([random.randint(0, 1000) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
