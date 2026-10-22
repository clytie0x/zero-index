"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/08-metro-route   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขสถานีแบบสุ่ม
ชุดที่ชื่อขึ้นต้นด้วย big big1 เป็นเส้นตรงสองแสนสถานี เส้นทางยาวเกือบสองแสนช่วง
big2 เป็นตาราง 400 × 500 ที่มีเส้นทางสั้นสุดเป็นจำนวนมหาศาล big3 เป็นสองเส้นทางยาวที่วิ่งขนานกันและมีทางเชื่อมสุ่ม
ตั้งใจให้วิธีลองสถานีถัดไปแล้ว BFS ใหม่ทุกครั้งใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2708)


def relabel(n, edges, s, t):
    label = [0] + random.sample(range(1, n + 1), n)
    edges = [(label[a], label[b]) if random.random() < 0.5 else (label[b], label[a]) for a, b in edges]
    random.shuffle(edges)
    return n, edges, label[s], label[t]


def chain(n):
    return [(v, v + 1) for v in range(1, n)]


def grid(rows, cols):
    edges = []
    for r in range(rows):
        for c in range(cols):
            v = r * cols + c + 1
            if c + 1 < cols:
                edges.append((v, v + 1))
            if r + 1 < rows:
                edges.append((v, v + cols))
    return edges


def ladder(length, rungs):
    """สองเส้นยาว length สถานี 1..length กับ length+1..2*length มีทางเชื่อมข้ามเส้นตามจุดสุ่ม"""
    edges = chain(length) + [(length + v, length + v + 1) for v in range(1, length)]
    for v in random.sample(range(1, length + 1), rungs):
        edges.append((v, length + v))
    return edges


def random_edges(n, m):
    seen = set()
    while len(seen) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            seen.add((min(a, b), max(a, b)))
    return sorted(seen)


def text(n, edges, s, t):
    return "\n".join([f"{n} {len(edges)} {s} {t}"] + [f"{a} {b}" for a, b in edges])


def cases():
    yield "sample1", "9 9 4 3\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "sample2", "9 9 1 9\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "same", "3 2 2 2\n1 2\n2 3"
    yield "neighbor", "2 1 2 1\n1 2"
    yield "grid", text(*relabel(400, grid(20, 20), 1, 400))
    yield "chain", text(*relabel(3000, chain(3000), 1, 3000))
    yield "ladder", text(*relabel(2000, ladder(1000, 30), 1, 2000))
    yield "rand1", text(*relabel(12, random_edges(12, 16), 1, 12))
    yield "rand2", text(*relabel(3000, random_edges(3000, 4000), 1, 2))
    n, edges, s, t = relabel(225, grid(15, 15), 1, 225)
    edges.sort(key=lambda e: (-min(e), -max(e)))
    yield "grid-desc", text(n, edges, s, t)
    yield "big1", text(*relabel(200000, chain(200000), 1, 200000))
    yield "big2", text(*relabel(200000, grid(400, 500), 1, 200000))
    yield "big3", text(*relabel(200000, ladder(100000, 3000), 1, 200000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
