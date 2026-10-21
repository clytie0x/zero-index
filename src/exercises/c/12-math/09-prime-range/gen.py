"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/09-prime-range   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีแสนคำถามที่ช่วงยาวหลายล้าน วิธีตรวจทีละเลขใน naive.c ไม่ทัน
ชุดอื่นมีงานรวมไม่เกินราวสองล้านเลข ให้ naive.c ผ่านได้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1209)

TOP = 10**7


def build(queries):
    return f"{len(queries)}\n" + "\n".join(f"{a} {b}" for a, b in queries)


def random_range(low, high, max_length):
    a = random.randint(low, high)
    return a, min(high, a + random.randint(0, max_length))


def cases():
    yield "sample1", build([(1, 10), (10, 20), (1, 1)])
    yield "sample2", build([(1, 100)])
    yield "one-two", build([(1, 1), (1, 2), (2, 2), (2, 3), (4, 4)])
    yield "top", build([(TOP, TOP), (TOP - 100, TOP), (9999991, 9999991), (9999990, 9999990)])
    yield "no-prime", build([(24, 28), (114, 126), (9999972, 9999990)])
    yield "small-many", build([random_range(1, 1000, 100) for _ in range(5000)])
    yield "rand1", build([random_range(1, TOP, 2000) for _ in range(500)])
    yield "rand2", build([random_range(TOP - 1000000, TOP, 200000) for _ in range(5)])
    yield "big1", build([random_range(1, TOP, TOP) for _ in range(100000)])
    yield "big2", build([(1, TOP)] * 100000)
    yield "big3", build([random_range(1, 1000, 1000) for _ in range(50000)] + [(1, TOP)] * 50000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
