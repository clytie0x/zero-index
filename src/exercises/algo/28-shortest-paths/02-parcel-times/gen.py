"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/02-parcel-times   (รันที่รากของโปรเจกต์)

naive.cpp คือ Dijkstra แบบอาเรย์ O(N^2) ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนจุด ตั้งใจให้แบบอาเรย์ไม่ทัน
one-way มีจุดที่ไปถึงได้แต่กลับไม่ได้ ซึ่งดักคนที่ใส่ถนนสองทาง
ทุกชุดตั้งแต่ rand2 มีระยะเกิน int และมีจุดที่ไปไม่ถึง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2802)


def build(n, start, edges):
    return f"{n} {len(edges)} {start}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def random_directed(n, m, top, reach):
    """จุด 1 ถึง reach ไปถึงกันจากจุด 1 ด้วยต้นไม้ทิศออก จุดที่เหลือมีถนนเข้าหากลุ่มแรกได้ แต่ไม่มีถนนออกจากกลุ่มแรกไปหา"""
    edges = []
    for v in range(2, reach + 1):
        edges.append((random.randint(1, v - 1), v, random.randint(1, top)))
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u == v or (u <= reach < v):
            continue
        edges.append((u, v, random.randint(1, top)))
    random.shuffle(edges)
    return edges


def relabel(n, start, edges):
    """สลับหมายเลขจุด ให้จุดเริ่มไม่ใช่ 1 และจุดที่ไปไม่ถึงกระจายไปทั่ว"""
    perm = list(range(1, n + 1))
    random.shuffle(perm)
    new = {old: perm[old - 1] for old in range(1, n + 1)}
    return new[start], [(new[u], new[v], w) for u, v, w in edges]


def cases():
    yield "sample1", "5 6 2\n2 1 4\n2 3 1\n3 1 2\n1 4 7\n4 2 3\n5 4 1"
    yield "min", "2 1 2\n1 2 9"
    # จุดเริ่มไม่มีถนนออกเลย
    yield "stuck", build(3, 3, [(1, 2, 5), (2, 3, 5)])
    yield "one-way", build(4, 1, [(1, 2, 3), (2, 3, 3), (4, 1, 1), (3, 1, 100)])
    yield "over-int", build(5, 5, [(5, 4, 10**9), (4, 3, 10**9), (3, 2, 10**9), (2, 1, 10**9), (5, 1, 10**9 - 1)])
    s, e = relabel(30, 1, random_directed(30, 70, 100, 25))
    yield "rand1", build(30, s, e)
    s, e = relabel(3000, 1, random_directed(3000, 6000, 10**9, 2700))
    yield "rand2", build(3000, s, e)
    s, e = relabel(100000, 1, random_directed(100000, 200000, 10**9, 90000))
    yield "big1", build(100000, s, e)
    # เส้นยาวทางเดียว ระยะของจุดท้ายราว 5 x 10^13
    n = 100000
    chain = [(i, i + 1, random.randint(10**8, 10**9)) for i in range(1, n)]
    back = [(random.randint(2, n), 1, random.randint(1, 10**9)) for _ in range(100000)]
    s, e = relabel(n, 1, chain + back)
    random.shuffle(e)
    yield "big2", build(n, s, e)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
