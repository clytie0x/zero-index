"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/07-three-gifts   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N = 5000 ตั้งใจให้ลูปสามชั้นใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1807)


def case(k, prices):
    return f"{len(prices)} {k}\n" + " ".join(map(str, prices))


def cases():
    yield "sample1", case(100, [20, 50, 30, 10, 40, 60])
    # ราคาซ้ำกัน ของคนละชิ้นนับแยก
    yield "sample2", case(9, [3, 3, 3, 3])
    yield "minimum", case(3, [1, 1, 1])
    yield "none", case(10, [random.randint(4, 1000000) for _ in range(300)])
    # ราคาที่ต้องการเกิน 1000000 หรือน้อยกว่า 1 ต้องไม่ออกนอกอาเรย์
    yield "out-of-range", case(3000000, [1000000, 1000000, 1000000, 1, 2, 999999])
    yield "all-same", case(3000, [1000] * 300)
    yield "rand1", case(150, [random.randint(1, 100) for _ in range(200)])
    yield "rand2", case(1500, [random.randint(1, 1000) for _ in range(1000)])
    prices = [random.randint(1, 1000000) for _ in range(800)]
    yield "rand3", case(sum(random.sample(prices, 3)), prices)
    # คำตอบ 5000 × 4999 × 4998 / 6 เกิน int
    yield "big1", case(3000, [1000] * 5000)
    yield "big2", case(1500, [random.randint(1, 1000) for _ in range(5000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
