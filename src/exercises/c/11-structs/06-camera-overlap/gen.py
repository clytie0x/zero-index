"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/06-camera-overlap/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/06-camera-overlap

ชุด big ไม่เก็บใน git สร้างใหม่ได้ด้วยสคริปต์นี้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1106)
LIMIT = 10**9


def cameras(rects):
    return "\n".join([str(len(rects))] + [f"{a} {b} {c} {d}" for a, b, c, d in rects])


def shuffle_corners(low_x, low_y, high_x, high_y):
    # เขียนมุมตรงข้ามคู่ใดคู่หนึ่ง ในลำดับใดก็ได้
    if random.random() < 0.5:
        corners = [(low_x, low_y), (high_x, high_y)]
    else:
        corners = [(low_x, high_y), (high_x, low_y)]
    random.shuffle(corners)
    (a, b), (c, d) = corners
    return a, b, c, d


def around(core, n):
    # สี่เหลี่ยมทุกรูปครอบ core ไว้ ส่วนที่ทุกรูปเห็นจึงไม่ว่าง
    x1, y1, x2, y2 = core
    return [shuffle_corners(random.randint(-LIMIT, x1), random.randint(-LIMIT, y1),
                            random.randint(x2, LIMIT), random.randint(y2, LIMIT)) for _ in range(n)]


def cases():
    yield "sample1", cameras([(0, 0, 6, 4), (3, 1, 8, 5)])
    yield "sample2", cameras([(10, 10, 2, 3), (0, 8, 7, 0), (5, 12, 1, 4)])
    yield "single-reversed", cameras([(5, -2, -3, 7)])
    # ห่างกันแนวทแยง ถ้าไม่ตรวจความกว้างกับความสูงจะได้ค่าบวก
    yield "diagonal", cameras([(0, 0, 2, 2), (8, 8, 5, 5)])
    yield "apart-x", cameras([(0, 0, 2, 10), (5, 3, 9, 4)])
    yield "touch-edge", cameras([(0, 0, 2, 2), (4, 2, 2, 0)])
    yield "touch-corner", cameras([(0, 0, 2, 2), (2, 2, 4, 4)])
    yield "nested", cameras([(-100, -100, 100, 100), (-10, 20, 30, -5), (0, 0, 1, 1)])
    yield "max-area", cameras([(LIMIT, -LIMIT, -LIMIT, LIMIT), (-LIMIT, -LIMIT, LIMIT, LIMIT)])
    yield "over-int", cameras([(0, 0, 100000, 100000), (100001, 100001, -1, -1)])
    yield "rand1", cameras(around((-50, 10, 70, 20), 200))
    yield "big1", cameras(around((-1000, -3000, 2000, 1000), 100000))
    # ทุกรูปครอบจุดกลาง ยกเว้นสองรูปที่อยู่คนละมุม ส่วนที่ทุกรูปเห็นจึงว่าง
    rects = around((-100, -100, 100, 100), 99998)
    rects.insert(random.randint(0, len(rects)), (-LIMIT, -LIMIT, -500, -500))
    rects.insert(random.randint(0, len(rects)), (500, 500, LIMIT, LIMIT))
    yield "big2", cameras(rects)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
