"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/10-free-ticket   (รันที่รากของโปรเจกต์)

naive.cpp ลองใช้ตั๋วกับถนนทีละเส้นแล้วรัน Dijkstra ใหม่ทุกครั้ง ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนถนน ตั้งใจให้วิธีนั้นไม่ทัน
one-ticket ดักโปรแกรมที่ใช้ตั๋วได้มากกว่าหนึ่งครั้ง
detour ทางที่ดีที่สุดเมื่อมีตั๋วไม่ใช่ทางที่สั้นที่สุดเมื่อไม่มีตั๋ว
over-int และ big2 มีคำตอบเกิน int ส่วน sample2 และ big3 ไปไม่ถึง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2810)


def build(n, edges):
    return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def random_graph(n, m, top, offset=0):
    order = list(range(1, n + 1))
    random.shuffle(order)
    edges = [(order[random.randrange(i)], order[i], random.randint(1, top)) for i in range(1, n)]
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            edges.append((u, v, random.randint(1, top)))
    edges = [(u + offset, v + offset, w) for u, v, w in edges]
    random.shuffle(edges)
    return edges


def cases():
    yield "sample1", "6 9\n1 2 4\n1 3 1\n3 2 2\n2 4 5\n3 4 8\n3 5 10\n4 5 2\n4 6 6\n5 6 3"
    yield "sample2", "4 2\n1 2 5\n3 4 5"
    yield "min", "2 1\n1 2 1000000000"
    yield "one-ticket", build(4, [(1, 2, 10**9), (2, 3, 10**9), (3, 4, 1)])
    # ไม่มีตั๋ว ทางบนถูกกว่า มีตั๋ว ทางล่างที่มีถนนแพงเส้นเดียวถูกกว่า
    yield "detour", build(5, [(1, 2, 10), (2, 3, 10), (3, 5, 10), (1, 4, 1), (4, 5, 100)])
    yield "over-int", build(6, [(1, 2, 10**9), (2, 3, 10**9), (3, 4, 10**9), (4, 5, 10**9), (5, 6, 10**9)])
    yield "rand1", build(30, random_graph(30, 60, 100))
    yield "rand2", build(800, random_graph(800, 2000, 10**9))
    yield "big1", build(100000, random_graph(100000, 200000, 10**9))
    n = 100000
    chain = [(i, i + 1, random.randint(10**8, 10**9)) for i in range(1, n)]
    extra = []
    for _ in range(100001):
        i = random.randint(1, n - 1)
        extra.append((i + 1, i, 10**9))
    edges = chain + extra
    random.shuffle(edges)
    yield "big2", build(n, edges)
    edges = random_graph(50000, 100000, 10**9) + random_graph(50000, 100000, 10**9, 50000)
    random.shuffle(edges)
    yield "big3", build(100000, edges)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
