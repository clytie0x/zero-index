"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/07-rotate-group   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีกลุ่มยาวและ k % ความยาวกลุ่มใหญ่ ตั้งใจให้ naive.c ที่หมุนทีละคนไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1007)


def make(people, moves):
    lines = [f"{len(people)} {len(moves)}", " ".join(map(str, people))]
    lines += [f"{l} {r} {k}" for l, r, k in moves]
    return "\n".join(lines)


def people(n):
    return random.sample(range(1, 1000001), n)


def rand_moves(n, q, max_k):
    out = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        out.append((l, r, random.randint(0, max_k)))
    return out


def long_moves(n, q):
    """กลุ่มยาวอย่างน้อยครึ่งแถว และ k % ความยาวอยู่แถวกลางกลุ่ม"""
    out = []
    for _ in range(q):
        l = random.randint(1, n // 4)
        r = random.randint(n - n // 4, n)
        length = r - l + 1
        k = length * random.randint(0, 9000) + random.randint(length // 3, 2 * length // 3)
        out.append((l, r, k))
    return out


def cases():
    yield "sample1", make([11, 12, 13, 14, 15, 16, 17], [(2, 6, 2), (1, 7, 10)])
    yield "sample2", make([5, 4, 3], [(1, 3, 0), (2, 2, 7)])
    yield "single", make([42], [(1, 1, 1000000000)])
    # k เป็นพหุคูณของความยาวกลุ่ม ต้องได้แถวเดิม
    yield "full-turn", make(list(range(1, 11)), [(1, 10, 10), (3, 7, 1000000000 // 5 * 5), (4, 5, 2)])
    # k ใหญ่ถึง 10^9 จับโปรแกรมที่ลืมลดด้วย % ก่อนหมุน
    yield "huge-k", make(people(30), [(1, 30, 999999999), (5, 25, 1000000000), (2, 29, 123456789)])
    # กลุ่มชิดหัวแถวและท้ายแถว จับการนับตำแหน่งผิดไปหนึ่ง
    yield "edges", make(list(range(1, 13)), [(1, 4, 1), (9, 12, 3), (1, 12, 5), (12, 12, 4), (1, 1, 2)])
    yield "rand1", make(people(50), rand_moves(50, 40, 100))
    yield "rand2", make(people(2000), rand_moves(2000, 300, 10**9))
    yield "big1", make(random.sample(range(1, 100001), 50000), long_moves(50000, 500))
    yield "big2", make(random.sample(range(1, 100001), 50000), [(1, 50000, 25000 + i) for i in range(499)] + [(1, 50000, 10**9)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
