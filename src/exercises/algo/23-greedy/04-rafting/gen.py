"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/04-rafting   (รันที่รากของโปรเจกต์)

neighbor-trap ทำให้วิธีจับคู่คนที่น้ำหนักติดกันหลังเรียงผิด
heavy-pair ทำให้วิธีจับคนหนักสุดกับคนหนักรองลงมาผิด
big1 ใหญ่เกิน 300 KB จึงตั้งชื่อขึ้นต้นด้วย big ข้อนี้ไม่มี naive
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2304)


def build(limit, weights):
    return f"{len(weights)} {limit}\n" + " ".join(map(str, weights))


def cases():
    yield "sample1", build(100, [70, 50, 30, 80, 20])
    yield "sample2", build(10, [5, 5, 5, 5, 5])
    yield "single", build(1, [1])
    yield "all-alone", build(100, [51, 99, 60, 100, 75])
    yield "exact-limit", build(1000000000, [500000000, 400000000, 600000000, 500000000])
    yield "neighbor-trap", build(10, [1, 2, 8, 9, 3, 7])
    yield "heavy-pair", build(10, [6, 5, 4, 4])
    weights = [random.randint(1, 30) for _ in range(15)]
    yield "rand1", build(30, weights)
    yield "rand2", build(10**6, [random.randint(1, 10**6) for _ in range(2000)])
    yield "big1", build(10**9, [random.randint(1, 10**9) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
