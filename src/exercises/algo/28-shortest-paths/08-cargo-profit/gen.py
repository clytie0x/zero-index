"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/08-cargo-profit   (รันที่รากของโปรเจกต์)

กราฟที่ไม่มีวงติดลบสร้างด้วยความสูง h ค่าใช้จ่ายของ u ไป v คือ สุ่มไม่ติดลบ + h[u] - h[v]
ผลรวมรอบวงใดๆ ของ h หักล้างกันหมด วงจึงไม่ติดลบ แต่ถนนแต่ละเส้นติดลบได้
cycle-off-route กับ cycle-unreached มีวงติดลบที่ไม่มีผลกับคำตอบ
over-int และ under-int มีคำตอบเกิน int ทั้งทางบวกและทางลบ
long-chain ทางที่ดีที่สุดผ่านทุกโกดังเรียงกัน และเส้นทางอยู่ในรายการกลับด้าน ต้องผ่อนครบเกือบ N - 1 รอบ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2808)


def build(n, edges):
    return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def potential_graph(n, m, base, height):
    """กราฟสุ่มไม่มีวงติดลบ ไปถึงทุกโกดังได้จากโกดัง 1 ค่าใช้จ่ายอยู่ในช่วง -height ถึง base + height"""
    h = [0] + [random.randint(0, height) for _ in range(n)]
    order = list(range(2, n + 1))
    random.shuffle(order)
    order = [1] + order
    edges = []
    for i in range(1, n):
        u, v = order[random.randrange(i)], order[i]
        edges.append((u, v, random.randint(0, base) + h[u] - h[v]))
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            edges.append((u, v, random.randint(0, base) + h[u] - h[v]))
    return edges


def cases():
    yield "sample1", "4 4\n2 4 3\n3 2 -4\n1 3 5\n1 2 2"
    yield "sample2", "5 5\n1 2 4\n2 3 -2\n3 4 3\n4 2 -2\n4 5 1"
    yield "unreachable", build(4, [(1, 2, -5), (2, 1, 6), (4, 3, -1), (3, 4, -1)])
    # วงติดลบที่ไปจากโกดัง 1 ได้ แต่เดินต่อไปโกดัง N ไม่ได้
    yield "cycle-off-route", build(5, [(1, 2, 2), (2, 5, 2), (1, 3, 1), (3, 4, -3), (4, 3, 1)])
    # วงติดลบที่ไปถึงโกดัง N ได้ แต่ไปจากโกดัง 1 ไม่ถึง
    yield "cycle-unreached", build(5, [(1, 5, 9), (2, 3, -3), (3, 2, 1), (3, 5, 1), (4, 2, 1)])
    # วงที่ผลรวมเป็น 0 ไม่ใช่วงติดลบ
    yield "zero-cycle", build(4, [(1, 2, 5), (2, 3, -7), (3, 2, 7), (3, 4, 1)])
    yield "over-int", build(4, [(1, 2, 10**9), (2, 3, 10**9), (3, 4, 10**9), (2, 1, 10**9)])
    yield "under-int", build(5, [(1, 2, -10**9), (2, 3, -10**9), (3, 4, -10**9), (4, 5, -10**9), (1, 5, 10**9)])
    yield "rand1", build(30, potential_graph(30, 80, 100, 60))
    yield "rand2", build(2000, potential_graph(2000, 5000, 5 * 10**8, 2 * 10**8))
    # กราฟสุ่มแบบไม่มีวงติดลบ แล้วเติมวงติดลบหนึ่งวงที่อยู่บนทางจาก 1 ไป N
    edges = potential_graph(2000, 4993, 5 * 10**8, 2 * 10**8)
    ring = random.sample(range(2, 2000), 5)
    for i in range(5):
        edges.append((ring[i], ring[(i + 1) % 5], -10**9 if i == 0 else 10**8))
    edges += [(1, ring[2], 7), (ring[3], 2000, 7)]
    random.shuffle(edges)
    yield "rand3", build(2000, edges)
    n = 2000
    chain = [(i, i + 1, random.randint(-10**6, 10**6)) for i in range(n - 1, 0, -1)]
    extra = [(i, i + 2, 10**9) for i in range(1, n - 1)][:5000 - len(chain)]
    yield "long-chain", build(n, chain + extra)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
