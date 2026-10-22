"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/03-nearest-shops   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีร้านแสนร้านตามขอบเขตโจทย์ ไม่เก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1603)


def line(values):
    return " ".join(map(str, values))


def case(distances, k):
    return f"{len(distances)} {k}\n{line(distances)}"


def cases():
    yield "sample1", case([450, 120, 800, 120, 300], 3)
    yield "sample2", case([700, 700, 700, 50], 4)
    yield "single", case([0], 1)
    # ทุกร้านห่างเท่ากัน ต้องเรียงตามหมายเลขล้วนๆ
    yield "all-same", case([500] * 15, 15)
    yield "extremes", case([10**9, 0, 10**9, 0, 1], 5)
    # เรียงจากไกลไปใกล้มาก่อน
    yield "reversed", case(list(range(1000, 0, -10)), 7)
    yield "rand1", case([random.randint(0, 2000) for _ in range(300)], 50)
    # ระยะซ้ำกันเยอะ ทดสอบการเทียบหมายเลข
    yield "rand2", case([random.randint(0, 30) for _ in range(5000)], 5000)
    yield "big1", case([random.randint(0, 10**9) for _ in range(100000)], 100000)
    yield "big2", case([random.randint(0, 1000) for _ in range(100000)], 1)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
