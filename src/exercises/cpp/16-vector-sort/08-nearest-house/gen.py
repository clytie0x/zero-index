"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/08-nearest-house   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N และ Q สองแสน ตั้งใจให้การไล่ดูทุกบ้านใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1608)

LIMIT = 10**9


def line(values):
    return " ".join(map(str, values))


def case(houses, spots):
    return f"{len(houses)} {len(spots)}\n{line(houses)}\n{line(spots)}"


def cases():
    yield "sample1", case([120, -40, 300, 120, 75, 500], [100, 0, 400, -500, 900, 120])
    yield "sample2", case([10, 30, 30], [20, 25, 35, 10])
    yield "single", case([0], [0, -LIMIT, LIMIT])
    # จุดอยู่ก่อนบ้านหลังแรกและหลังบ้านหลังสุดท้าย จับคนที่ไม่เช็ก k == 0 หรือ k == N
    yield "outside", case([50, -20, 10, 30], [-LIMIT, -21, -20, 51, LIMIT, 50])
    # ห่างเท่ากันทั้งสองข้าง ต้องเลือกตำแหน่งที่น้อยกว่า
    yield "ties", case([-LIMIT, LIMIT, 0, 6, 6, 10], [3, 8, -500000000, 500000000, 7, 9])
    # บ้านซ้ำตำแหน่งเดียวกันหลายหลัง และจุดตรงกับบ้านพอดี
    yield "duplicates", case([7] * 50 + [3] * 50 + [11] * 20, [7, 3, 11, 5, 9, 4, 10, 0, 20])
    yield "rand1", case([random.randint(-1000, 1000) for _ in range(300)],
                        [random.randint(-1100, 1100) for _ in range(300)])
    yield "rand2", case([random.randint(-LIMIT, LIMIT) for _ in range(5000)],
                        [random.randint(-LIMIT, LIMIT) for _ in range(3000)])
    # ค่าแคบ บ้านซ้ำกันมาก และเสมอกันบ่อย
    yield "rand3", case([random.randrange(-40, 41, 4) for _ in range(4000)],
                        [random.randint(-50, 50) for _ in range(4000)])
    yield "big1", case([random.randint(-LIMIT, LIMIT) for _ in range(200000)],
                       [random.randint(-LIMIT, LIMIT) for _ in range(200000)])
    yield "big2", case([random.randrange(-100000, 100001, 2) for _ in range(200000)],
                       [random.randint(-110000, 110000) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
