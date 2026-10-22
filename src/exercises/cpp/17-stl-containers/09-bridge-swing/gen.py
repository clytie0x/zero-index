"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/09-bridge-swing   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นล้านและ K เป็นแสน ตั้งใจให้การไล่ทุกช่วงใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1709)

LIMIT = 2 * 10**9


def case(k, values):
    return f"{len(values)} {k}\n" + " ".join(map(str, values))


def cases():
    yield "sample1", case(3, [5, -2, 7, 7, 1, -6, 3, 2])
    yield "single", case(1, [-LIMIT])
    # K = 1 ทุกช่วงแกว่ง 0
    yield "k-one", case(1, [random.randint(-50, 50) for _ in range(300)])
    # K = N มีช่วงเดียว
    yield "k-full", case(500, [random.randint(-LIMIT, LIMIT) for _ in range(500)])
    # ค่าสุดขั้วสลับกัน คำตอบ 4 × 10^9 เกิน int
    yield "extremes", case(2, [LIMIT, -LIMIT, LIMIT, -LIMIT, 0, LIMIT, LIMIT])
    yield "all-equal", case(7, [-42] * 300)
    yield "falling", case(25, list(range(1000, 0, -1)))
    yield "rising", case(40, [i * 3 - 1500 for i in range(1000)])
    yield "rand1", case(5, [random.randint(-9, 9) for _ in range(2000)])
    yield "rand2", case(300, [random.randint(-LIMIT, LIMIT) for _ in range(4000)])
    yield "big1", case(500000, [random.randint(-LIMIT, LIMIT) for _ in range(1000000)])
    yield "big2", case(300000, list(range(LIMIT, LIMIT - 1000000, -1)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
