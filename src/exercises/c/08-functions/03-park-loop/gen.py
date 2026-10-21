"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/03-park-loop

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(803)


def answers(points):
    """คำนวณแบบเดียวกับเฉลย บวกตามลำดับเดียวกัน"""
    n = len(points)
    total = 0.0
    longest = 0.0
    for i in range(n):
        (x1, y1), (x2, y2) = points[i], points[(i + 1) % n]
        leg = math.sqrt(float(x2 - x1) ** 2 + float(y2 - y1) ** 2)
        total += leg
        longest = max(longest, leg)
    return total, longest


def safe(points):
    """Windows กับ Linux ปัดเลขที่ตกตรงครึ่งต่างกัน ตัดชุดที่ใกล้ .xx5 ทิ้ง"""
    for value in answers(points):
        scaled = value * 100
        if abs(scaled - math.floor(scaled) - 0.5) < 1e-6:
            return False
    return True


def make(points):
    assert safe(points), points
    return f"{len(points)}\n" + "\n".join(f"{x} {y}" for x, y in points)


def rand_points(n, low, high):
    while True:
        points = [(random.randint(low, high), random.randint(low, high)) for _ in range(n)]
        if safe(points):
            return points


def cases():
    # ช่วงขากลับยาว 4 จับคนที่ลืมวิ่งกลับจุดแรก
    yield "sample1", make([(0, 0), (3, 0), (3, 4), (0, 4)])
    yield "sample2", make([(0, 0), (5, 2), (1, 6)])
    yield "single", make([(7, -3)])
    # สองจุด วิ่งไปแล้ววิ่งกลับ ระยะรวมเป็นสองเท่าของช่วงเดียว
    yield "two-points", make([(-2, 1), (4, 9)])
    yield "same-place", make([(5, 5), (5, 5), (5, 5)])
    # ช่วงยาวที่สุดคือช่วงขากลับ
    yield "longest-return", make([(0, 0), (1, 1), (2, 2), (3, 3), (100, 100)])
    yield "corners", make([(-10000, -10000), (10000, -10000), (10000, 10000), (-10000, 10000)])
    yield "diagonal-max", make([(-10000, -10000), (10000, 10000)])
    yield "rand1", make(rand_points(10, -50, 50))
    yield "rand2", make(rand_points(200, -10000, 10000))
    yield "max-n", make(rand_points(1000, -10000, 10000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
