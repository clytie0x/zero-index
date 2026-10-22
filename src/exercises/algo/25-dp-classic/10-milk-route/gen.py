"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/10-milk-route   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกลำดับร้านด้วย next_permutation ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 9 จุด
ชุดที่ชื่อขึ้นต้นด้วย big มี 15 ถึง 16 จุด ซึ่งลองทุกลำดับไม่ทัน
open-trap ดักวิธีที่ลืมกลับโรงนม urgent-trap ดักวิธีที่ลืมเงื่อนไขร้านด่วน
no-detour ดักวิธีที่หาทางสั้นสุดทุกคู่ก่อน (ระยะสุ่มไม่ตามอสมการสามเหลี่ยม ทางอ้อมจึงสั้นกว่าได้)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2510)

TOP = 10**6


def build(dist, urgent=()):
    rows = [f"{len(dist)} {len(urgent)}"] + [" ".join(map(str, row)) for row in dist]
    if urgent:
        rows.append(" ".join(map(str, urgent)))
    return "\n".join(rows)


def random_urgent(n, k):
    return random.sample(range(1, n), k)


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
    yield "sample2", build([[0, 4, 8, 5], [4, 0, 3, 7], [8, 3, 0, 2], [5, 7, 2, 0]], [2])
    yield "only-plant", build([[0]])
    yield "two", build([[0, TOP], [1, 0]], [1])
    # ไปร้าน 1 แล้วร้าน 2 แบบไม่กลับสั้นที่สุด แต่ร้าน 2 กลับโรงนมไกลมาก
    yield "open-trap", build([[0, 1, 50], [50, 0, 1], [1000, 50, 0]])
    # ถ้าไม่สนร้านด่วน ไป 1 2 3 วนกลับได้ 4 แต่ร้าน 3 เป็นร้านด่วน
    yield "urgent-trap", build([[0, 1, 9, 9], [9, 0, 1, 9], [9, 9, 0, 1], [1, 9, 9, 0]], [3])
    # ถนนตรงระหว่างคู่ยาวมาก แต่อ้อมผ่านจุดอื่นสั้นกว่า
    yield "no-detour", build([[0, 1, 100, 1], [1, 0, 1, 100], [100, 1, 0, 1], [1, 100, 1, 0]], [2])
    yield "all-urgent", build(random_dist(8, 1, 1000), list(range(1, 8)))
    yield "symmetric", build(random_dist(7, 1, 100, symmetric=True), random_urgent(7, 3))
    yield "one-way", build(one_way_trap(8), [5])
    yield "rand1", build(random_dist(8, 1, 1000), random_urgent(8, 2))
    yield "rand2", build(random_dist(9, 1, TOP), random_urgent(9, 4))
    yield "rand3", build(random_dist(9, 1, 20))
    yield "big1", build(random_dist(16, 1, TOP), random_urgent(16, 5))
    yield "big2", build(random_dist(15, 1, 10))
    yield "big3", build(one_way_trap(16), random_urgent(16, 3))
    yield "big4", build(random_dist(16, 1, TOP), random_urgent(16, 15))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
