"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/01-clinic-route   (รันที่รากของโปรเจกต์)

naive.cpp คือ Dijkstra แบบอาเรย์ O(N^2) ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนจุด ตั้งใจให้แบบอาเรย์ไม่ทัน
over-int และ big2 มีคำตอบเกิน int ส่วน unreachable และ big3 ไปไม่ถึงคลินิก
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2801)


def build(n, edges):
    return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def random_graph(n, m, top, connected=True):
    """กราฟสุ่ม n จุด m เส้น น้ำหนัก 1 ถึง top ถ้า connected ทุกจุดต่อกันเป็นก้อนเดียว"""
    edges = []
    if connected:
        order = list(range(1, n + 1))
        random.shuffle(order)
        for i in range(1, n):
            edges.append((order[random.randrange(i)], order[i], random.randint(1, top)))
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            edges.append((u, v, random.randint(1, top)))
    random.shuffle(edges)
    return edges


def two_parts(n, m, top):
    """จุด 1 กับจุด n อยู่คนละก้อน"""
    half = n // 2
    left = [(u, v, w) for u, v, w in random_graph(half, m // 2, top)]
    right = [(u + half, v + half, w) for u, v, w in random_graph(n - half, m - m // 2, top)]
    edges = left + right
    random.shuffle(edges)
    return edges


def cases():
    yield "sample1", "6 9\n1 2 4\n1 3 1\n3 2 2\n2 4 5\n3 4 8\n3 5 10\n4 5 2\n4 6 6\n5 6 3"
    yield "sample2", "5 3\n1 2 7\n2 3 4\n4 5 1"
    yield "min", "2 1\n2 1 1000000000"
    # ถนนตรงแพงกว่าทางอ้อม และมีถนนซ้ำคู่ที่ถูกกว่าเส้นแรก
    yield "parallel", build(4, [(1, 4, 100), (1, 2, 30), (2, 4, 50), (2, 4, 20), (1, 4, 60), (3, 4, 1)])
    # ทางเดียวที่ไปถึงยาวสี่เส้น เส้นละ 10^9 รวมเกิน int
    yield "over-int", build(6, [(1, 2, 10**9), (2, 3, 10**9), (3, 4, 10**9), (4, 6, 10**9), (5, 6, 1), (5, 4, 10**9)])
    yield "unreachable", build(8, two_parts(8, 12, 50))
    yield "rand1", build(30, random_graph(30, 60, 100))
    yield "rand2", build(2000, random_graph(2000, 5000, 10**9))
    yield "big1", build(100000, random_graph(100000, 200000, 10**9))
    # เส้นยาวผ่านทุกจุดเรียงกัน กับถนนซ้ำคู่ที่แพงกว่า คำตอบราว 5 x 10^13
    n = 100000
    chain = [(i, i + 1, random.randint(10**8, 10**9 - 1)) for i in range(1, n)]
    extra = []
    for _ in range(100000):
        u, v, w = random.choice(chain)
        extra.append((v, u, random.randint(w + 1, 10**9)))
    edges = chain + extra
    random.shuffle(edges)
    yield "big2", build(n, edges)
    yield "big3", build(100000, two_parts(100000, 200000, 10**9))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
