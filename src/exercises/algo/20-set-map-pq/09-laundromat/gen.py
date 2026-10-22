"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/09-laundromat   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีเครื่องและลูกค้าเป็นแสน ตั้งใจให้การไล่ดูทุกเครื่องใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2009)

TOP = 10**9


def case(k, customers):
    return f"{len(customers)} {k}\n" + "\n".join(f"{t} {d}" for t, d in customers)


def random_customers(n, max_gap, low_d, high_d, start=0):
    customers = []
    t = start
    for _ in range(n):
        t = min(TOP, t + random.randint(0, max_gap))
        customers.append((t, random.randint(low_d, high_d)))
    return customers


def cases():
    yield "sample1", case(2, [(0, 30), (5, 10), (10, 20), (15, 5), (40, 5), (40, 5)])
    yield "sample2", case(3, [(100, 7), (200, 7), (300, 7)])
    yield "one-machine", case(1, [(0, 5), (1, 5), (2, 5), (20, 1)])
    # เครื่องว่างหลายเครื่องแต่ว่างคนละเวลา ต้องเลือกตามหมายเลข ไม่ใช่ตามเวลาที่ว่าง
    yield "pick-by-number", case(3, [(0, 50), (0, 10), (0, 20), (60, 1), (60, 1), (60, 1)])
    # คนแรกต้องรอ คนถัดไปมาเวลาเดียวกันก็ต้องรอด้วย และเสร็จพร้อมกันสองเครื่อง
    yield "wait-together", case(2, [(0, 10), (0, 10), (3, 4), (3, 4), (3, 4)])
    yield "huge-time", case(2, [(TOP, TOP)] * 5)
    yield "more-machines", case(10, random_customers(6, 3, 1, 5))
    yield "rand1", case(4, random_customers(2000, 5, 1, 30))
    yield "rand2", case(50, random_customers(5000, 100, 1, 10000))
    yield "big1", case(200000, random_customers(200000, 5000, 1, TOP))
    yield "big2", case(100000, random_customers(200000, 1, 1, 200000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
