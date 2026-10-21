"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/08-hanoi-kth-move   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี n ถึง 45 หรือ 60 จำนวนครั้งที่ย้ายถึงราว 10^18
ตั้งใจให้วิธีไล่ย้ายจริงจนถึงครั้งที่ K ใน naive.c ไม่ทัน ชุดเล็กมี n ไม่เกิน 20
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(908)


def build(n, queries):
    return "\n".join([f"{n} {len(queries)}"] + [str(k) for k in queries])


def random_queries(n, count):
    return [random.randint(1, 2**n - 1) for _ in range(count)]


def cases():
    yield "sample1", build(3, list(range(1, 8)))
    yield "one-disk", build(1, [1])
    yield "two-disks", build(2, [3, 1, 2])
    # n คู่ ครั้งแรกย้ายไป B ไม่ใช่ C จับคนที่เดาจากรูปแบบ n = 3
    yield "four-disks", build(4, list(range(1, 16)))
    yield "rand1", build(10, random_queries(10, 200))
    yield "rand2", build(16, random_queries(16, 100))
    # ครั้งกลางพอดีและรอบๆ ครั้งแรกและครั้งสุดท้าย
    yield "edges-small", build(20, [2**19, 1, 2**20 - 1, 2**19 - 1, 2**19 + 1])
    yield "big1", build(60, random_queries(60, 1000))
    edges = [1, 2, 3, 2**59 - 1, 2**59, 2**59 + 1, 2**60 - 2, 2**60 - 1, 2**58, 3 * 2**58]
    yield "big2", build(60, edges)
    yield "big3", build(45, random_queries(45, 1000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
