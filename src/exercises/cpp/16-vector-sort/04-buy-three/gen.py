"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/04-buy-three   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้ selection sort ใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1604)


def line(values):
    return " ".join(map(str, values))


def case(prices):
    return f"{len(prices)}\n{line(prices)}"


def cases():
    yield "sample1", case([120, 35, 80, 50, 15, 60])
    yield "sample2", case([100, 100, 100, 100])
    yield "single", case([999])
    yield "two", case([10, 20])
    # ราคาเรียงจากน้อยไปมากอยู่แล้ว ถ้าไม่เรียงใหม่จะได้คำตอบผิด
    yield "ascending", case(list(range(1, 10)))
    # ราคารวมเกิน int ต้องใช้ long long
    yield "over-int", case([10**6] * 4500)
    yield "rand1", case([random.randint(1, 500) for _ in range(100)])
    yield "rand2", case([random.randint(1, 10**6) for _ in range(5000)])
    yield "big1", case([random.randint(1, 10**6) for _ in range(200000)])
    yield "big2", case([random.choice([10, 20, 50, 100, 10**6]) for _ in range(199999)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
