"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/08-shelf-space   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนชั้นและสองแสนกล่อง
big1 ชั้นหน้าโกดังเกือบเต็มหมด มีที่ว่างเยอะแค่ชั้นท้ายๆ ทุกกล่องต้องเดินเกือบสุดโกดัง
ตั้งใจให้วิธีเดินหาทีละชั้นใน naive.cpp ไม่ทัน
big2 กล่องใหญ่เกินทุกชั้นปนอยู่ครึ่งหนึ่ง ต้องตอบ 0 โดยไม่ไล่ทั้งโกดัง
big3 สุ่มทั้งหมด
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3008)

TOP = 10**9


def build(space, boxes):
    return f"{len(space)} {len(boxes)}\n" + " ".join(map(str, space)) + "\n" + " ".join(map(str, boxes)) + "\n"


def cases():
    yield "sample1", build([5, 12, 3, 8], [4, 6, 7, 2, 9, 3, 1])
    yield "single", build([10], [3, 3, 3, 3, 1, 1])
    yield "zero-space", build([0, 0, 5, 0], [1, 5, 1])
    yield "too-big", build([7, 7, 7], [8, 7, 8, 1, 7, 6])
    # ชั้นแรกพอดีเป๊ะ และชั้นที่ที่ว่างลดลงจนกล่องถัดไปต้องข้ามไป
    yield "exact-fit", build([4, 9, 4], [4, 4, 4, 5, 4, 1])
    yield "last-shelf", build([1, 1, 1, 1, 1, 100], [2, 50, 50, 1, 1])
    yield "max-values", build([TOP, TOP, 1], [TOP, TOP, 1, TOP, 1])
    yield "rand1", build([random.randint(0, 20) for _ in range(10)], [random.randint(1, 10) for _ in range(30)])
    yield "rand2", build([random.randint(0, TOP) for _ in range(3000)], [random.randint(1, TOP // 3) for _ in range(3000)])
    n = 200000
    space = [random.randint(0, 50) for _ in range(n - 100)] + [TOP] * 100
    yield "big1", build(space, [random.randint(51, 100) for _ in range(n)])
    space = [random.randint(0, 50) for _ in range(n - 100)] + [TOP - 1] * 100
    boxes = [random.choice([random.randint(51, 100), TOP]) for _ in range(n)]
    yield "big2", build(space, boxes)
    yield "big3", build([random.randint(0, TOP) for _ in range(n)], [random.randint(1, TOP) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
