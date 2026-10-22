"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/01-study-groups   (รันที่รากของโปรเจกต์)

naive.cpp คือ union-find แบบตรงไปตรงมาในหน้า 29.1 ไม่มี path compression และ union by size
ชุดที่ชื่อขึ้นต้นด้วย big มีนักเรียนสองแสนคน big1 จับคู่ต่อกันเป็นสายยาว ทำให้ต้นไม้ของ naive.cpp เป็นเส้นตรง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2901)


def build(n, pairs):
    return "\n".join([f"{n} {len(pairs)}"] + [f"{a} {b}" for a, b in pairs])


def random_pairs(n, m):
    pairs = []
    while len(pairs) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            pairs.append((a, b))
    return pairs


def cases():
    yield "sample1", "7 5\n1 2\n2 5\n3 4\n5 1\n6 7"
    yield "sample2", "4 0"
    yield "one-student", build(1, [])
    yield "all-together", build(6, [(1, 2), (3, 4), (5, 6), (2, 3), (4, 5)])
    yield "repeat-pair", build(5, [(2, 4), (4, 2), (2, 4), (4, 2)])
    # สายยาวทั้งห้อง ทำให้ union-find แบบตรงไปตรงมาได้ต้นไม้เส้นตรง
    yield "chain", build(300, [(i, i + 1) for i in range(1, 300)])
    yield "two-halves", build(10, [(1, 3), (3, 5), (5, 7), (7, 9), (2, 4), (4, 6), (6, 8), (8, 10)])
    yield "rand1", build(50, random_pairs(50, 30))
    yield "rand2", build(2000, random_pairs(2000, 1500))
    yield "big1", build(200000, [(i, i + 1) for i in range(1, 200000)])
    yield "big2", build(200000, random_pairs(200000, 200000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
