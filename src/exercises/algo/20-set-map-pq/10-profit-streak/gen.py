"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/10-profit-streak   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้การลองทุกช่วงใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2010)

TOP = 10**9


def case(profits, target):
    return f"{len(profits)} {target}\n" + " ".join(map(str, profits))


def cases():
    # rand2 กับ big3 ใช้ค่าสุ่มกว้าง เลือก K เป็นผลรวมของช่วงหนึ่งที่มีอยู่จริง จะได้มีคำตอบอย่างน้อย 1
    yield "sample1", case([300, -100, 200, -200, 300, 100], 400)
    yield "sample2", case([5, -5, 5, -5], 0)
    yield "single-hit", case([-7], -7)
    yield "single-miss", case([7], -7)
    yield "all-zero", case([0] * 1000, 0)
    # ผลรวมสะสมถึง 10^12 ต้องเป็น long long
    yield "huge-sum", case([TOP] * 1000, 500 * TOP)
    yield "all-negative", case([-TOP] * 600, -3 * TOP)
    yield "no-answer", case([2, 4, 6, 8, 10], 7)
    yield "rand1", case([random.randint(-5, 5) for _ in range(3000)], 3)
    profits = [random.randint(-TOP, TOP) for _ in range(5000)]
    yield "rand2", case(profits, sum(profits[1200:3400]))
    yield "rand3", case([random.randint(-100, 100) for _ in range(5000)], -42)
    yield "big1", case([random.randint(-3, 3) for _ in range(200000)], 2)
    # ทุกช่วงมีกำไรรวมเป็นศูนย์ คำตอบ 20000100000 เกิน int
    yield "big2", case([0] * 200000, 0)
    profits = [random.randint(-TOP, TOP) for _ in range(200000)]
    yield "big3", case(profits, sum(profits[50000:150000]))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
