"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/09-summer-jobs   (รันที่รากของโปรเจกต์)

first-free ทำให้วิธีลงวันว่างวันแรกผิด no-return ทำให้วิธีเรียงตามวันกำหนดแล้วรับโดยไม่คืนงานผิด
far-deadline มีวันกำหนดถึง 10^9 วิธีที่สร้างอาเรย์ตามวันกำหนดจะใช้หน่วยความจำเกิน
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนงานที่แย่งวันท้ายๆ กัน วิธีหาวันว่างวันสุดท้ายใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2309)


def build(jobs):
    return f"{len(jobs)}\n" + "\n".join(f"{d} {p}" for d, p in jobs)


def cases():
    yield "sample1", build([(2, 500), (1, 300), (2, 400), (3, 200), (1, 600)])
    yield "sample2", build([(4, 100), (4, 100), (4, 100)])
    yield "single", build([(1000000000, 1000000000)])
    yield "first-free", build([(3, 5), (2, 1), (3, 4)])
    yield "no-return", build([(1, 1), (1, 100), (2, 2), (2, 50)])
    yield "same-day", build([(2, p) for p in [7, 3, 9, 1, 8, 2]])
    yield "far-deadline", build([(10**9, 10**9), (999999999, 10**9), (1, 5), (10**9, 1), (500000000, 10**9)])
    yield "rand1", build([(random.randint(1, 6), random.randint(1, 20)) for _ in range(10)])
    yield "rand2", build([(random.randint(1, 500), random.randint(1, 10**9)) for _ in range(2000)])
    n = 200000
    yield "big1", build([(random.randint(n // 2, n), random.randint(1, 10**9)) for _ in range(n)])
    yield "big2", build([(random.randint(n, 10**9), random.randint(1, 10**9)) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
