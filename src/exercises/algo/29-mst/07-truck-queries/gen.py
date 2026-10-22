"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/07-truck-queries   (รันที่รากของโปรเจกต์)

naive.cpp BFS ใหม่ทุกคำถามบนถนนที่รับน้ำหนักได้ O(Q(N + M))
ชุดที่ชื่อขึ้นต้นด้วย big มีเมืองแสนเมืองและคำถามแสนข้อ ซึ่ง naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2907)

TOP = 10**9


def build(n, roads, asks):
    rows = [f"{n} {len(roads)} {len(asks)}"] + [f"{a} {b} {w}" for a, b, w in roads] + [f"{x} {y} {t}" for x, y, t in asks]
    return "\n".join(rows)


def connected(n, m):
    label = list(range(1, n + 1))
    random.shuffle(label)
    pairs = [(label[random.randint(0, v - 1)], label[v]) for v in range(1, n)]
    while len(pairs) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            pairs.append((a, b))
    random.shuffle(pairs)
    return pairs


def random_asks(n, q, low, high):
    return [(random.randint(1, n), random.randint(1, n), random.randint(low, high)) for _ in range(q)]


def cases():
    roads = [(1, 2, 12), (1, 3, 30), (2, 4, 25), (3, 4, 8), (3, 5, 15), (4, 6, 20), (5, 6, 18), (2, 3, 9)]
    yield "sample1", build(6, roads, [(1, 6, 15), (1, 6, 16), (2, 4, 25), (6, 6, 99), (4, 1, 12), (5, 2, 13)])
    # รับได้เท่ากับน้ำหนักรถพอดีต้องผ่าน
    yield "exact-limit", build(3, [(1, 2, 7), (2, 3, 5)], [(1, 3, 5), (1, 3, 6), (1, 2, 7), (1, 2, 8), (3, 2, 5)])
    yield "two-parts", build(6, [(1, 2, 100), (2, 3, 100), (4, 5, 100), (5, 6, 100)], [(1, 3, 1), (1, 4, 1), (6, 4, 100), (3, 6, 50)])
    yield "same-city", build(2, [(1, 2, 1)], [(1, 1, TOP), (2, 2, 1), (1, 2, 2)])
    yield "parallel", build(3, [(1, 2, 3), (2, 1, 9), (1, 2, 5), (2, 3, 4), (3, 2, 6)], [(1, 3, 6), (1, 3, 7), (3, 1, 5), (1, 2, 9), (1, 2, 10)])
    yield "same-weight", build(5, [(1, 2, 50), (2, 3, 50), (3, 4, 49), (4, 5, 50)], [(1, 5, 50), (1, 3, 50), (4, 5, 50), (5, 1, 49), (1, 5, 51)])
    yield "rand1", build(10, [(a, b, random.randint(1, 20)) for a, b in connected(10, 16)], random_asks(10, 30, 1, 22))
    yield "rand2", build(2000, [(a, b, random.randint(1, TOP)) for a, b in connected(2000, 4000)], random_asks(2000, 3000, 1, TOP))
    yield "big1", build(100000, [(a, b, random.randint(1, TOP)) for a, b in connected(100000, 200000)], random_asks(100000, 100000, 1, TOP))
    # รถเบาเกือบทุกคัน ถนนเกือบทุกเส้นใช้ได้ BFS ต้องเดินทั้งกราฟทุกคำถาม
    yield "big2", build(100000, [(a, b, random.randint(1, TOP)) for a, b in connected(100000, 150000)], random_asks(100000, 100000, 1, 1000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
