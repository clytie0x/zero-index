"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/06-exam-rank   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นแสน ตั้งใจให้ bubble sort ใน naive.c ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1306)


def line(values):
    return " ".join(map(str, values))


def case(scores, queries):
    return f"{len(scores)} {len(queries)}\n{line(scores)}\n" + "\n".join(map(str, queries))


def exam_scores(n):
    """คะแนนกระจุกตรงกลางแบบข้อสอบจริง และตัดให้อยู่ใน 0 ถึง 100"""
    return [max(0, min(100, round(random.gauss(55, 18)))) for _ in range(n)]


def cases():
    yield "sample1", case([72, 85, 64, 85, 90, 58], [1, 2, 3, 6])
    yield "sample2", case([50, 50, 50, 40, 40], [3, 4, 5, 1])
    yield "single", case([0], [1])
    yield "all-same", case([77] * 10, [1, 5, 10])
    yield "extremes", case([0, 100, 0, 100, 0], [1, 2, 3, 4, 5])
    # คะแนนว่างช่วงกลาง ไล่ข้ามคะแนนที่ไม่มีใครได้
    yield "gaps", case([100, 3, 99, 2, 1, 98], [3, 4, 6])
    scores = exam_scores(1000)
    yield "rand1", case(scores, [random.randint(1, 1000) for _ in range(50)])
    scores = [random.randint(0, 100) for _ in range(5000)]
    yield "rand2", case(scores, [1, 5000] + [random.randint(1, 5000) for _ in range(198)])
    scores = exam_scores(200000)
    yield "big1", case(scores, [1, 200000] + [random.randint(1, 200000) for _ in range(998)])
    scores = [random.choice([0, 25, 50, 75, 100]) for _ in range(150000)]
    yield "big2", case(scores, [random.randint(1, 150000) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
