"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/09-reading-room   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้การนับทุกคู่ใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1609)

LIMIT = 10**9


def case(visits):
    return f"{len(visits)}\n" + "\n".join(f"{s} {e}" for s, e in visits)


def random_visit(start_max, length_max):
    s = random.randint(0, start_max)
    return (s, min(LIMIT, s + random.randint(1, length_max)))


def cases():
    yield "sample1", case([(10, 50), (20, 30), (40, 70), (25, 45), (60, 80)])
    # ออกกับเข้าที่เวลาเดียวกัน ไม่นับว่าอยู่พร้อมกัน
    yield "sample2", case([(0, 10), (10, 20), (20, 30)])
    yield "single", case([(0, LIMIT)])
    yield "same-time", case([(5, 9)] * 6)
    # เข้าออกต่อกันเป็นทอดๆ ถ้าให้คนเข้าก่อนคนออกจะได้ 2 แทน 1
    yield "relay", case([(i * 10, i * 10 + 10) for i in range(30)])
    # ค่ามากสุดเกิดสองครั้ง ต้องตอบครั้งแรก
    yield "twice", case([(100, 200), (150, 250), (500, 600), (550, 650), (0, 1)])
    yield "nested", case([(i, 2 * 50 - i) for i in range(50)])
    yield "rand1", case([random_visit(1000, 100) for _ in range(200)])
    yield "rand2", case([random_visit(LIMIT - 1, 10**7) for _ in range(4000)])
    yield "rand3", case([random_visit(50, 5) for _ in range(4000)])
    yield "big1", case([random_visit(LIMIT - 1, 10**6) for _ in range(200000)])
    yield "big2", case([random_visit(100, 3) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
