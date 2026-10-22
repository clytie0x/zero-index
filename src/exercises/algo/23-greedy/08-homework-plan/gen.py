"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/08-homework-plan   (รันที่รากของโปรเจกต์)

ชุดที่ไม่ได้ขึ้นต้นด้วย big มีไม่เกิน 8 ชิ้น ให้วิธีลองทุกลำดับใน naive.cpp ตรวจได้
short-trap ทำให้วิธีทำชิ้นสั้นก่อนผิด slack-trap ทำให้วิธีเรียงตาม d - t ผิด
over-int มีวันที่เสร็จเกิน int ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนชิ้น
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2308)


def build(tasks):
    return f"{len(tasks)}\n" + "\n".join(f"{t} {d}" for t, d in tasks)


def random_tasks(n, top_t, slack):
    tasks = []
    total = 0
    for _ in range(n):
        t = random.randint(1, top_t)
        total += t
        tasks.append(t)
    return [(t, max(1, random.randint(1, int(total * slack)))) for t in tasks]


def cases():
    yield "sample1", build([(3, 4), (2, 2), (1, 7), (4, 9), (2, 5)])
    yield "sample2", build([(2, 10), (3, 5), (1, 1)])
    yield "single", build([(10, 3)])
    yield "short-trap", build([(1, 100), (5, 5)])
    yield "slack-trap", build([(1, 2), (10, 10)])
    yield "same-due", build([(3, 6), (1, 6), (2, 6), (4, 6)])
    yield "over-int", build([(10**9, 3 * 10**9), (10**9, 10**9), (999999999, 10**14), (10**9, 4500000000), (10**9, 2 * 10**9), (10**9, 4 * 10**9)])
    yield "rand1", build(random_tasks(8, 10, 0.7))
    yield "rand2", build(random_tasks(8, 1000, 1.0))
    yield "big1", build(random_tasks(200000, 10**9, 0.8))
    yield "big2", build(random_tasks(200000, 10, 1.2))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
