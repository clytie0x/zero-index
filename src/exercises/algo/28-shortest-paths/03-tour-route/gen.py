"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/03-tour-route   (รันที่รากของโปรเจกต์)

โจทย์รับประกันว่าทางที่สั้นที่สุดมีเส้นเดียว gen.py จึงนับจำนวนทางที่สั้นที่สุดด้วย Dijkstra ของตัวเอง
ถ้าเกินหนึ่งทางจะสุ่มน้ำหนักใหม่จนกว่าจะเหลือทางเดียว
naive.cpp คือ Dijkstra แบบอาเรย์ ชุด big มีแสนจุดซึ่งแบบอาเรย์ไม่ทัน
"""

import heapq
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2803)


def build(n, edges):
    return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def count_shortest(n, edges):
    """จำนวนทางที่สั้นที่สุดจาก 1 ไป n นับถึงแค่ 2 ถ้าไปไม่ถึงได้ 0"""
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    inf = float("inf")
    dist = [inf] * (n + 1)
    ways = [0] * (n + 1)
    dist[1], ways[1] = 0, 1
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v], ways[v] = d + w, ways[u]
                heapq.heappush(heap, (dist[v], v))
            elif d + w == dist[v]:
                ways[v] = min(2, ways[v] + ways[u])
    return ways[n]


def random_graph(n, m, top):
    order = list(range(1, n + 1))
    random.shuffle(order)
    pairs = [(order[random.randrange(i)], order[i]) for i in range(1, n)]
    while len(pairs) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            pairs.append((u, v))
    while True:
        edges = [(u, v, random.randint(1, top)) for u, v in pairs]
        if count_shortest(n, edges) == 1:
            random.shuffle(edges)
            return edges


def cases():
    yield "sample1", "6 9\n1 2 4\n1 3 1\n3 2 2\n2 4 5\n3 4 8\n3 5 10\n4 5 2\n4 6 6\n5 6 3"
    yield "sample2", "4 2\n1 2 5\n3 4 5"
    yield "min", "2 1\n1 2 7"
    # ถนนตรงกับทางอ้อม ทางอ้อมถูกกว่าหนึ่งวินาที
    yield "detour", build(5, [(1, 5, 31), (1, 2, 10), (2, 3, 10), (3, 4, 5), (4, 5, 5), (2, 5, 21)])
    # ทางเดียวที่ไปถึงผ่านถนนสามเส้นที่ยาวเกือบ 10^9 รวมเกิน int
    yield "over-int", build(5, [(1, 3, 999999999), (3, 2, 999999998), (2, 5, 999999997), (1, 4, 10**9), (4, 2, 10**9)])
    edges = random_graph(40, 80, 100)
    yield "rand1", build(40, edges)
    edges = random_graph(3000, 8000, 10**9)
    yield "rand2", build(3000, edges)
    yield "big1", build(100000, random_graph(100000, 200000, 10**9))
    # ไปไม่ถึง สองก้อนใหญ่ไม่เชื่อมกัน
    left = random_graph(50000, 100000, 10**9)
    right = [(u + 50000, v + 50000, w) for u, v, w in random_graph(50000, 100000, 10**9)]
    edges = left + right
    random.shuffle(edges)
    yield "big2", build(100000, edges)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
