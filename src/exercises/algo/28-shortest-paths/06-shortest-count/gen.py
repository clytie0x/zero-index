"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/06-shortest-count   (รันที่รากของโปรเจกต์)

naive.cpp คือ Dijkstra แบบอาเรย์พร้อมนับทาง O(N^2) ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนจุด ตั้งใจให้แบบอาเรย์ไม่ทัน
stale ดักโปรแกรมที่ไม่ข้ามคู่เก่า (จุดที่ถูกใส่ลงคิวสองครั้งจะบวกจำนวนทางซ้ำ)
layers และ big2 มีจำนวนทางเกิน 10^9 + 7 และเวลาเกิน int ส่วน sample2 และ big3 ไปไม่ถึง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2806)


def build(n, edges):
    return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def random_graph(n, m, low, high, offset=0):
    order = list(range(1, n + 1))
    random.shuffle(order)
    edges = [(order[random.randrange(i)], order[i], random.randint(low, high)) for i in range(1, n)]
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            edges.append((u, v, random.randint(low, high)))
    edges = [(u + offset, v + offset, w) for u, v, w in edges]
    random.shuffle(edges)
    return edges


def layered(layers, width, weight):
    """จุด 1 ต่อกับชั้นแรก ทุกจุดในชั้นหนึ่งต่อกับทุกจุดในชั้นถัดไป ชั้นสุดท้ายต่อกับจุด n
    ถนนยาวเท่ากันหมด จำนวนทางที่สั้นที่สุดคือ width ยกกำลัง layers"""
    n = layers * width + 2
    node = lambda layer, i: 2 + layer * width + i
    edges = [(1, node(0, i), weight) for i in range(width)]
    for layer in range(layers - 1):
        for i in range(width):
            for j in range(width):
                edges.append((node(layer, i), node(layer + 1, j), weight))
    edges += [(node(layers - 1, i), n, weight) for i in range(width)]
    random.shuffle(edges)
    return n, edges


def grid_graph(r, c, weights):
    """ตาราง r x c ช่องติดกันมีถนน มุมซ้ายบนคือจุด 1 มุมขวาล่างคือจุด n จุดอื่นสลับหมายเลข
    น้ำหนักสุ่มจาก weights ซึ่งมีค่าซ้ำเยอะ ทางที่สั้นที่สุดจึงมีหลายทาง"""
    n = r * c
    middle = list(range(2, n))
    random.shuffle(middle)
    label = [1] + middle + [n]
    edges = []
    for i in range(r):
        for j in range(c):
            here = label[i * c + j]
            if j + 1 < c:
                edges.append((here, label[i * c + j + 1], random.choice(weights)))
            if i + 1 < r:
                edges.append((here, label[(i + 1) * c + j], random.choice(weights)))
    random.shuffle(edges)
    return n, edges


def cases():
    yield "sample1", "6 9\n1 2 2\n1 3 2\n2 3 1\n2 4 3\n3 4 3\n1 4 7\n4 5 1\n4 6 4\n5 6 3"
    yield "sample2", "5 4\n1 2 3\n2 3 3\n3 1 3\n4 5 1"
    yield "min", "2 3\n1 2 5\n2 1 5\n1 2 6"
    # ทางอ้อมสั้นกว่าทางตรง จุดกลางทางถูกใส่ลงคิวสองครั้ง
    yield "stale", build(7, [(1, 4, 50), (1, 2, 10), (2, 3, 10), (3, 4, 10), (1, 3, 20), (4, 5, 7), (4, 6, 7), (5, 7, 3), (6, 7, 3), (4, 7, 10)])
    n, edges = layered(20, 4, 10**9)
    yield "layers", build(n, edges)
    yield "rand1", build(30, random_graph(30, 70, 1, 3))
    n, edges = grid_graph(50, 60, [1, 1, 1, 2])
    yield "rand2", build(n, edges)
    n, edges = grid_graph(316, 316, [1, 1, 1, 1, 2])
    yield "big1", build(n, edges)
    n, edges = layered(49999, 2, 10**9)
    yield "big2", build(n, edges)
    left = random_graph(50000, 100000, 1, 2)
    right = random_graph(50000, 100000, 1, 2, 50000)
    edges = left + right
    random.shuffle(edges)
    yield "big3", build(100000, edges)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
