"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/05-savings-jar   (รันที่รากของโปรเจกต์)

naive.cpp วนทีละวัน ชุดที่ไม่ใช่ big จึงให้ n ไม่เกิน 10^5
ชุดที่ชื่อขึ้นต้นด้วย big มี n ถึง 10^18 วนทีละวันไม่มีทางทัน
no-inverse ใช้ m ที่ a - 1 กับ m มีตัวประกอบร่วม สูตรอนุกรมเรขาคณิตที่หารด้วย a - 1 ใช้ไม่ได้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2205)

TOP = 10**9


def build(rows):
    return f"{len(rows)}\n" + "\n".join(f"{a} {n} {m}" for a, n, m in rows)


def cases():
    yield "sample1", "3\n2 4 1000\n3 5 7\n5 1 100"
    yield "m-one", build([(7, 10, 1), (TOP, 99999, 1), (1, 1, 1)])
    yield "a-one", build([(1, n, m) for n, m in [(5, 3), (100000, 7), (99999, TOP), (1, 2)]])
    yield "a-multiple", build([(12, 1000, 6), (TOP, 100000, TOP), (20, 7, 4)])
    yield "no-inverse", build([(500000001, 100000, TOP), (7, 99998, 12), (13, 77777, 36), (TOP, 100000, 999999999)])
    yield "rand1", build([(random.randint(1, TOP), random.randint(1, 100000), random.randint(1, TOP)) for _ in range(40)])
    yield "rand2", build([(random.randint(1, 20), random.randint(1, 1000), random.randint(1, 50)) for _ in range(100)])
    yield "big1", build([(random.randint(1, TOP), random.randint(1, 10**18), random.randint(1, TOP)) for _ in range(100)])
    rows = [(random.randint(2, TOP), 10**18, random.choice([TOP, 999999999, 2**29, 1000000007])) for _ in range(50)]
    rows += [(500000001, 10**18 - k, TOP) for k in range(25)]
    rows += [(3, 2**59 - 1, 1000), (1, 10**18, TOP), (TOP, 10**18, TOP)]
    yield "big2", build(rows)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
