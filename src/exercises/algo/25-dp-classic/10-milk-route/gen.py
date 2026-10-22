"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/10-milk-route   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกลำดับร้านด้วย next_permutation ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 9 จุด
ชุดที่ชื่อขึ้นต้นด้วย big มี 15 ถึง 16 จุด ซึ่งลองทุกลำดับไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2510)

TOP = 10**6


def build(dist):
    return f"{len(dist)}\n" + "\n".join(" ".join(map(str, row)) for row in dist)


def random_dist(n, low, high, symmetric=False):
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = random.randint(low, high)
    if symmetric:
        for i in range(n):
            for j in range(i):
                dist[i][j] = dist[j][i]
    return dist


def one_way_trap(n):
    """ไปตามเลขจุดเรียงกันสั้นมาก ย้อนกลับยาวมาก ร้านที่ใกล้โรงนมที่สุดคือร้านสุดท้าย"""
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = 1 if j == i + 1 else TOP
    for j in range(1, n):
        dist[0][j] = 2
    dist[0][n - 1] = 1
    return dist


def cases():
    yield "sample1", build([[0, 4, 8, 5], [4, 0, 3, 7], [8, 3, 0, 2], [5, 7, 2, 0]])
    yield "sample2", build([[0, 10, 1], [1, 0, 1], [10, 1, 0]])
    yield "only-plant", build([[0]])
    yield "two", build([[0, TOP], [1, 0]])
    yield "symmetric", build(random_dist(7, 1, 100, symmetric=True))
    yield "one-way", build(one_way_trap(8))
    yield "rand1", build(random_dist(8, 1, 1000))
    yield "rand2", build(random_dist(9, 1, TOP))
    yield "big1", build(random_dist(16, 1, TOP))
    yield "big2", build(random_dist(15, 1, 10))
    yield "big3", build(one_way_trap(16))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
