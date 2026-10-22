"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/08-solar-or-cable   (รันที่รากของโปรเจกต์)

naive.cpp สร้างเส้นทุกคู่บ้านรวมกับเส้นจากโหนดสมมติ แล้วทำ Kruskal
ชุดที่ชื่อขึ้นต้นด้วย big มีบ้าน 7000 หลัง เส้นราว 24.5 ล้านเส้น ซึ่ง naive.cpp ใช้ราว 2 วินาทีและหน่วยความจำราว 500 MB
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2908)

TOP = 10**6


def build(per_meter, houses):
    return "\n".join([f"{len(houses)} {per_meter}"] + [f"{x} {y} {s}" for x, y, s in houses])


def scattered(n, size, low, high):
    return [(random.randint(0, size), random.randint(0, size), random.randint(low, high)) for _ in range(n)]


def clustered(n, centers, spread, low, high):
    middle = [(random.randint(spread, TOP - spread), random.randint(spread, TOP - spread)) for _ in range(centers)]
    houses = []
    for _ in range(n):
        cx, cy = random.choice(middle)
        houses.append((cx + random.randint(-spread, spread), cy + random.randint(-spread, spread), random.randint(low, high)))
    return houses


def cases():
    yield "sample1", "5 10\n0 0 500\n3 4 900\n4 4 300\n50 50 400\n52 49 1000"
    yield "one-house", build(1000, [(TOP, TOP, 10**9)])
    # สายแพงมาก ทุกบ้านติดแผงเอง
    yield "all-solar", build(1000, [(0, 0, 5), (TOP, 0, 7), (0, TOP, 3), (TOP, TOP, 9)])
    # สายถูกมาก ติดแผงหลังเดียวแล้วเดินสายที่เหลือ
    yield "one-solar", build(1, [(i, 0, 10**9 - i) for i in range(8)])
    yield "same-spot", build(1000, [(500, 500, 40), (500, 500, 30), (500, 500, 20), (501, 500, 10**9)])
    # สายเส้นเดียวราคา 2 × 10^9 เกิน int
    yield "over-int", build(1000, [(0, 0, 10**9), (TOP, TOP, 10**9), (0, TOP, 10**9)])
    yield "rand1", build(7, scattered(9, 100, 1, 1000))
    yield "rand2", build(50, clustered(500, 12, 2000, 10**5, 10**7))
    yield "big1", build(1000, scattered(7000, TOP, 1, 10**9))
    yield "big2", build(997, scattered(7000, TOP, 10**8, 10**9))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
