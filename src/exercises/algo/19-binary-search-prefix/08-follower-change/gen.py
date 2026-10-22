"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/08-follower-change   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนวัน ตั้งใจให้วิธีลองทุกคู่ใน naive.cpp ไม่ทัน
big2 เป็นศูนย์ทั้งหมด คำตอบ 20000100000 เกิน int
big3 ค่ากว้างถึงพันล้าน ใช้อาเรย์นับแบบหน้า 19.5 ไม่ได้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1908)

TOP = 10**9


def build(k, changes):
    return f"{len(changes)} {k}\n" + " ".join(map(str, changes))


def cases():
    yield "sample1", "7 4\n2 2 -3 5 0 -1 4"
    yield "single", build(-7, [-7])
    yield "none", build(100, [1, -1, 2, -2, 3, -3])
    # ช่วงที่เริ่มวันแรกต้องนับด้วย
    yield "from-first", build(10, [10, 0, 0, -5, 5, 10])
    yield "zero-k", build(0, [3, -3, 3, -3, 0, 0, 3])
    yield "all-zero", build(0, [0] * 2000)
    # ผลรวมเกิน int และ K ติดลบ
    yield "wide", build(-2 * TOP, [TOP, -TOP, -TOP, -TOP, TOP, -TOP, 0, -TOP, TOP])
    changes = [random.randint(-3, 3) for _ in range(60)]
    yield "rand1", build(random.randint(-4, 4), changes)
    changes = [random.randint(-TOP, TOP) for _ in range(2000)]
    l, r = sorted(random.sample(range(2000), 2))
    yield "rand2", build(sum(changes[l:r + 1]), changes)
    n = 200000
    yield "big1", build(2, [random.randint(-3, 3) for _ in range(n)])
    yield "big2", build(0, [0] * n)
    changes = [random.choice([TOP, -TOP, random.randint(-TOP, TOP)]) for _ in range(n)]
    l, r = sorted(random.sample(range(n), 2))
    yield "big3", build(sum(changes[l:r + 1]), changes)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
