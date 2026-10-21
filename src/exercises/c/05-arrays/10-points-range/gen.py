"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/10-points-range   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีผู้เล่นแสนคนและคำถามแสนข้อ ตั้งใจให้วิธีไล่นับทุกคนทุกคำถามใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(510)

TOP = 1000000


def line(values):
    return " ".join(map(str, values))


def build(points, queries):
    rows = [f"{len(points)} {len(queries)}", line(points)] + [f"{a} {b}" for a, b in queries]
    return "\n".join(rows)


def random_query(low, high):
    a, b = random.randint(low, high), random.randint(low, high)
    return (a, b) if a <= b else (b, a)


def cases():
    yield "sample1", "6 4\n120 50 999 50 0 1000000\n0 1000000\n50 50\n51 998\n0 49"
    yield "single", "1 3\n0\n0 0\n1 1000000\n0 1000000"
    yield "same-points", build([777] * 8, [(777, 777), (0, 776), (778, TOP), (700, 800)])
    # แต้มที่ขอบ 0 กับ 1000000 และคำถามที่ A เป็น 0
    yield "edges", build([0, 0, TOP, TOP, 500000], [(0, 0), (TOP, TOP), (0, TOP), (1, TOP - 1), (0, 499999)])
    yield "empty-range", build([10, 20, 30, 40], [(11, 19), (41, TOP), (0, 9), (21, 29)])
    points = [random.randint(0, 100) for _ in range(50)]
    yield "rand1", build(points, [random_query(0, 100) for _ in range(50)])
    points = [random.randint(0, TOP) for _ in range(2000)]
    yield "rand2", build(points, [random_query(0, TOP) for _ in range(2000)])
    points = [random.randint(0, TOP) for _ in range(100000)]
    yield "big1", build(points, [random_query(0, TOP) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
