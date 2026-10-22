"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/08-homework-plan   (รันที่รากของโปรเจกต์)

ชุดที่ไม่ได้ขึ้นต้นด้วย big มีไม่เกิน 8 ชิ้น ให้วิธีลองทุกลำดับใน naive.cpp ตรวจได้
short-trap ทำให้วิธีทำชิ้นสั้นก่อนผิด slack-trap ทำให้วิธีเรียงตาม d - t ผิด
exam-unsorted ให้วันสอบไม่เรียง วิธีที่ไม่เรียงวันสอบก่อนจะนับวันสอบขาด
exam-chain มีวันสอบติดกันหลายวันตรงวันที่ชิ้นงานจะเสร็จพอดี วิธีที่เลื่อนแค่ครั้งเดียวจะผิด
no-exam-effect มีวันสอบหลังงานเสร็จหมด ต้องไม่กระทบคำตอบ
over-int มีวันที่เสร็จเกิน int ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนชิ้น
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2308)


def build(tasks, exams=()):
    rows = [f"{len(tasks)} {len(exams)}"] + [f"{t} {d}" for t, d in tasks]
    if exams:
        rows.append(" ".join(map(str, exams)))
    return "\n".join(rows)


def random_exams(k, top):
    exams = random.sample(range(1, top + 1), k)
    random.shuffle(exams)
    return exams


def random_tasks(n, top_t, slack):
    tasks = []
    total = 0
    for _ in range(n):
        t = random.randint(1, top_t)
        total += t
        tasks.append(t)
    return [(t, max(1, random.randint(1, int(total * slack)))) for t in tasks]


def cases():
    yield "sample1", build([(3, 4), (2, 2), (1, 7), (4, 9), (2, 5)], [6, 3])
    yield "sample2", build([(2, 10), (3, 5), (1, 1)])
    yield "single", build([(10, 3)])
    yield "single-exam", build([(1, 1)], [1])
    yield "short-trap", build([(1, 100), (5, 5)], [2])
    yield "slack-trap", build([(1, 2), (10, 10)], [20])
    yield "same-due", build([(3, 6), (1, 6), (2, 6), (4, 6)], [5, 1])
    yield "exam-unsorted", build([(2, 3), (2, 6), (3, 9)], [8, 2, 5, 4])
    yield "exam-chain", build([(3, 3), (2, 5)], [3, 4, 5, 6])
    yield "no-exam-effect", build([(2, 2), (3, 4)], [99, 100])
    yield "over-int", build([(10**9, 3 * 10**9), (10**9, 10**9), (999999999, 10**14), (10**9, 4500000000), (10**9, 2 * 10**9), (10**9, 4 * 10**9)], [10**9, 3 * 10**9 + 1, 10**14, 5])
    tasks = random_tasks(8, 10, 0.7)
    yield "rand1", build(tasks, random_exams(6, sum(t for t, _ in tasks)))
    tasks = random_tasks(8, 1000, 1.0)
    yield "rand2", build(tasks, random_exams(3000, 2 * sum(t for t, _ in tasks)))
    yield "rand3", build(random_tasks(7, 5, 0.9))
    tasks = random_tasks(200000, 10**9, 0.8)
    yield "big1", build(tasks, random_exams(200000, sum(t for t, _ in tasks)))
    tasks = random_tasks(200000, 10, 1.2)
    yield "big2", build(tasks, random_exams(200000, 2 * sum(t for t, _ in tasks)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
