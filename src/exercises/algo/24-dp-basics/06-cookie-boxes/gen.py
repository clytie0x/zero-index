"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/06-cookie-boxes   (รันที่รากของโปรเจกต์)

naive.cpp ลองจำนวนกล่องของทุกขนาดทีละขนาดโดยไม่จด ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมี X ไม่เกิน 60
ชุดที่ชื่อขึ้นต้นด้วย big มี X ถึงแสนและกล่องร้อยขนาด คำตอบเกิน 1000000007
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2406)


def build(target, sizes):
    return f"{len(sizes)} {target}\n" + " ".join(map(str, sizes))


def cases():
    # ถ้านับแบบลำดับสำคัญจะได้ 9
    yield "sample1", build(5, [1, 2, 5])
    yield "sample2", build(10, [3, 4])
    yield "none", build(7, [2, 4, 6])
    yield "one-size", build(60, [1])
    yield "exact", build(8, [8])
    yield "too-big", build(3, [5, 9])
    yield "small-many", build(40, [1, 2, 3, 4, 5, 6])
    yield "rand1", build(50, random.sample(range(2, 15), 5))
    yield "rand2", build(60, random.sample(range(1, 30), 7))
    yield "big1", build(100000, random.sample(range(1, 101), 100))
    yield "big2", build(99991, random.sample(range(1, 100001), 100))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
