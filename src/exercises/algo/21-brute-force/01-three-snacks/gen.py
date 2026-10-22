"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/01-three-snacks   (รันที่รากของโปรเจกต์)

N ไม่เกิน 100 ลูปสามชั้นทันทุกชุด ข้อนี้ไม่มีชุด big
ชุด repeat จับคนที่หยิบชิ้นเดิมซ้ำเพราะเริ่มลูปที่ 0
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2101)


def build(budget, prices):
    return f"{len(prices)} {budget}\n" + " ".join(map(str, prices))


def cases():
    yield "sample1", build(100, [35, 20, 48, 27, 60])
    yield "sample2", build(10, [5, 4, 6, 8])
    yield "min-exact", build(6, [1, 2, 3])
    yield "min-over", build(5, [1, 2, 3])
    # หยิบชิ้นราคา 1 สามครั้งได้ 3 พอดี แต่มีชิ้นราคา 1 อยู่ชิ้นเดียว คำตอบจริงคือ -1
    yield "repeat", build(3, [1, 100, 100, 100])
    # สามชิ้นที่ต่างกันถูกสุดคือ 60 เกินงบ คำตอบจริงคือ -1 แต่ถ้าหยิบชิ้นซ้ำจะได้ราว 50 ถึง 59
    yield "repeat2", build(59, [10, 20, 30, 1000])
    yield "all-same", build(21, [7] * 50)
    yield "max", build(3000000, [random.randint(1, 10**6) for _ in range(100)])
    prices = [random.randint(1, 10**6) for _ in range(100)]
    yield "rand1", build(random.randint(500000, 1500000), prices)
    prices = [random.randint(1, 1000) for _ in range(100)]
    yield "rand2", build(random.randint(3, 3000), prices)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
