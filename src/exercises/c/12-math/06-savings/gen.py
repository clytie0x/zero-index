"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/06-savings   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีแสนคำถามที่ N ใหญ่ถึง 10^8 วิธีวนทีละวันใน naive.c ไม่ทัน
ชุดอื่นมีงานรวมไม่เกินราว 3 × 10^8 วัน ให้ naive.c ผ่านได้ ชุด max ทำให้ D × N × (N - 1) เกิน long long
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1206)

MAX_A, MAX_D, MAX_N = 10**9, 1000, 10**8


def build(plans):
    return f"{len(plans)}\n" + "\n".join(f"{a} {d} {n}" for a, d, n in plans)


def random_plans(q, max_n):
    return [(random.randint(1, MAX_A), random.randint(0, MAX_D), random.randint(1, max_n)) for _ in range(q)]


def cases():
    yield "sample1", build([(10, 5, 30), (1, 1, 100), (500, 0, 7)])
    yield "one-day", build([(1, 0, 1), (MAX_A, MAX_D, 1)])
    yield "no-step", build([(MAX_A, 0, MAX_N)])
    yield "two-days", build([(3, 1000, 2)])
    yield "max", build([(MAX_A, MAX_D, MAX_N), (1, MAX_D, MAX_N)])
    yield "near-max", build([(MAX_A, MAX_D, MAX_N - 1)])
    yield "rand1", build(random_plans(1000, 10000))
    yield "rand2", build(random_plans(20, 5000000))
    yield "big1", build(random_plans(100000, MAX_N))
    yield "big2", build([(MAX_A, MAX_D, MAX_N)] * 100000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
