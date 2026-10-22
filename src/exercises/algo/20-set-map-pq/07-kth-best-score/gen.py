"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/07-kth-best-score   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สามแสน ตั้งใจให้การแทรกลงอาเรย์ที่เรียงไว้ใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2007)

TOP = 10**9


def case(scores, k):
    return f"{len(scores)} {k}\n" + " ".join(map(str, scores))


def cases():
    yield "sample1", case([70, 90, 85, 60, 85, 95, 40], 3)
    yield "sample2", case([500, 200], 1)
    yield "k-equals-n", case([5, 3, 9, 1, 7], 5)
    yield "single", case([TOP], 1)
    yield "all-same", case([42] * 30, 7)
    yield "extremes", case([0, TOP, 0, TOP, 0, TOP, 0], 2)
    yield "increasing", case(list(range(1, 2001)), 50)
    yield "decreasing", case(list(range(2000, 0, -1)), 50)
    yield "rand1", case([random.randint(0, 100) for _ in range(3000)], 10)
    yield "rand2", case([random.randint(0, TOP) for _ in range(8000)], 1000)
    yield "big1", case([random.randint(0, TOP) for _ in range(300000)], 150000)
    # คะแนนเพิ่มขึ้นเรื่อยๆ คะแนนใหม่ดีที่สุดเสมอ การแทรกลงอาเรย์ที่เรียงจากมากไปน้อยต้องเลื่อนทั้งแถวทุกครั้ง
    yield "big2", case([3000 * i + random.randint(0, 2999) for i in range(300000)], 1)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
