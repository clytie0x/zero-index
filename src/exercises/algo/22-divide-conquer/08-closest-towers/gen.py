"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/08-closest-towers   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนจุด ตั้งใจให้วิธีลองทุกคู่ใน naive.cpp ไม่ทัน
far-corners มีระยะกำลังสองถึง 8 × 10^18 ต้องใช้ long long ตั้งแต่ตอนลบพิกัด
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2208)

TOP = 10**9


def build(points):
    return f"{len(points)}\n" + "\n".join(f"{x} {y}" for x, y in points)


def scatter(count, top):
    return [(random.randint(-top, top), random.randint(-top, top)) for _ in range(count)]


def cases():
    yield "sample1", "6\n0 0\n10 3\n4 8\n12 0\n6 6\n-3 5"
    yield "two", build([(-TOP, 0), (TOP, 0)])
    yield "far-corners", build([(-TOP, -TOP), (TOP, TOP)])
    yield "same-place", build([(5, 5), (-2, 9), (5, 5), (100, -100)])
    yield "same-x", build([(7, y) for y in random.sample(range(-TOP, TOP), 1500)])
    yield "same-y", build([(x, -3) for x in random.sample(range(-TOP, TOP), 1500)])
    # จุดแบ่งตรงกลางผ่าคู่ที่ใกล้ที่สุดพอดี
    yield "across-middle", build([(x * 100, (x % 7) * 1000) for x in range(-499, 501) if x != 0] + [(-1, 3000), (1, 3001)])
    yield "grid", build([(x * 7, y * 9) for x in range(40) for y in range(40)])
    yield "rand1", build(scatter(2000, TOP))
    yield "rand2", build(scatter(2000, 30))
    n = 200000
    yield "big1", build(scatter(n, TOP))
    yield "big2", build([(i * 3, (i * 7919) % 1000) for i in range(n)])
    yield "big3", build(scatter(n, 20000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
