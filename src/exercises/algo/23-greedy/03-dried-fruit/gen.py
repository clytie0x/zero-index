"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/03-dried-fruit   (รันที่รากของโปรเจกต์)

gen.py คำนวณคำตอบจริงเป็นเศษส่วนด้วยจำนวนเต็ม แล้วสุ่มใหม่ถ้าคำตอบอยู่ใกล้กึ่งกลางของการปัดทศนิยม 2 ตำแหน่ง
value-trap ทำให้วิธีเรียงตามราคารวมผิด light-trap ทำให้วิธีเรียงตามน้ำหนักผิด
int-ratio ทำให้วิธีหารจำนวนเต็มในฟังก์ชันเปรียบเทียบผิด whole-only ทำให้วิธีที่ไม่ตักบางส่วนผิด
big1 ใหญ่เกิน 300 KB จึงตั้งชื่อขึ้นต้นด้วย big ข้อนี้ไม่มี naive
"""

import random
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2303)


def exact(capacity, fruit):
    order = sorted(fruit, key=lambda f: Fraction(f[1], f[0]), reverse=True)
    room, total = capacity, Fraction(0)
    for grams, price in order:
        take = min(grams, room)
        total += Fraction(price * take, grams)
        room -= take
    return total


def safe(capacity, fruit):
    total = exact(capacity, fruit) * 100
    remainder = total.numerator % total.denominator
    return abs(2 * remainder - total.denominator) > total.denominator // 50


def build(capacity, fruit):
    assert safe(capacity, fruit), "คำตอบใกล้กึ่งกลางของการปัดเกินไป"
    return f"{len(fruit)} {capacity}\n" + "\n".join(f"{w} {v}" for w, v in fruit)


def random_case(n, top_w, top_v, fill):
    while True:
        fruit = [(random.randint(1, top_w), random.randint(1, top_v)) for _ in range(n)]
        capacity = max(1, int(sum(w for w, _ in fruit) * fill))
        if safe(capacity, fruit):
            return build(capacity, fruit)


def cases():
    yield "sample1", build(50, [(20, 300), (30, 360), (25, 400), (10, 100)])
    yield "sample2", build(7, [(3, 10), (5, 12)])
    yield "one-kind", build(400, [(900, 1000)])
    yield "all-fit", build(10**11, [(10**6, 1), (1, 10**6), (500000, 777777)])
    # ชนิดราคารวมสูงสุดหนักมาก ราคาต่อกรัมต่ำ
    yield "value-trap", build(100, [(1000, 5000), (60, 600), (50, 450)])
    # ชนิดที่เบาที่สุดราคาต่อกรัมต่ำสุด
    yield "light-trap", build(30, [(5, 5), (8, 9), (20, 200), (25, 240)])
    # ราคาต่อกรัม 7.9 กับ 7.1 ตัดเศษแล้วเหลือ 7 เท่ากัน
    yield "int-ratio", build(10, [(10, 71), (10, 79), (20, 142), (20, 157)])
    # ใส่ทั้งชนิดได้แค่ชนิดแรก ที่เหลือต้องตัก
    yield "whole-only", build(100, [(60, 600), (50, 450), (45, 400)])
    yield "rand1", random_case(10, 50, 100, 0.4)
    yield "rand2", random_case(1000, 10**6, 10**6, 0.3)
    yield "big1", random_case(100000, 10**6, 10**6, 0.5)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
