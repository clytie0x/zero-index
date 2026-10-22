"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/06-rival-teams   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขนักเรียนแบบสุ่ม
ชุดที่ชื่อขึ้นต้นด้วย big มีราวสองแสนคน big1 เป็นเส้นตรงเส้นเดียว big2 เป็นวงจำนวนคี่วงเดียว
big3 เป็นกราฟสองฝั่งสุ่มหลายกลุ่ม big1 กับ big2 ทำให้ DFS แบบ recursion ลึกเกือบสองแสนชั้นและพัง
ข้อนี้ไม่มี naive.cpp เพราะการลองแบ่งทุกแบบใช้ได้แค่ N ไม่เกินราว 20
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2706)


def relabel(n, edges):
    label = [0] + random.sample(range(1, n + 1), n)
    edges = [(label[a], label[b]) if random.random() < 0.5 else (label[b], label[a]) for a, b in edges]
    random.shuffle(edges)
    return n, edges


def chain(n, first=1):
    return [(v, v + 1) for v in range(first, first + n - 1)]


def ring(n, first=1):
    return chain(n, first) + [(first, first + n - 1)]


def bipartite_part(first, left, right, m):
    """กลุ่มหนึ่งที่มีฝั่งซ้าย left คนและฝั่งขวา right คน เชื่อมเป็นต้นไม้ก่อนให้ถึงกันหมด แล้วเติมเส้นสุ่มให้ครบ m"""
    a = list(range(first, first + left))
    b = list(range(first + left, first + left + right))
    order = [a[0], b[0]] + random.sample(a[1:] + b[1:], left + right - 2)
    placed = ([], [])
    edges = {(a[0], b[0])}
    for v in order:
        side = 0 if v < first + left else 1
        if placed[1 - side] and v not in (a[0], b[0]):
            u = random.choice(placed[1 - side])
            edges.add((min(u, v), max(u, v)))
        placed[side].append(v)
    while len(edges) < m:
        u, v = random.choice(a), random.choice(b)
        edges.add((min(u, v), max(u, v)))
    return sorted(edges)


def groups(sizes, extra):
    edges, first = [], 1
    for left, right in sizes:
        edges += bipartite_part(first, left, right, min(left * right, left + right - 1 + extra))
        first += left + right
    return first - 1, edges


def text(n, edges):
    return "\n".join([f"{n} {len(edges)}"] + [f"{a} {b}" for a, b in edges])


def cases():
    yield "sample1", "9 9\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "sample2", "4 3\n1 2\n2 3\n3 1"
    yield "single", "1 0"
    yield "no-rivals", "6 0"
    yield "even-ring", text(*relabel(1000, ring(1000)))
    yield "odd-ring", text(*relabel(999, ring(999)))
    yield "star", text(*relabel(300, [(1, v) for v in range(2, 301)]))
    yield "groups", text(*relabel(*groups([(random.randint(1, 8), random.randint(1, 8)) for _ in range(40)], 3)))
    n, edges = groups([(random.randint(5, 30), random.randint(5, 30)) for _ in range(50)], 20)
    yield "rand", text(*relabel(n, edges))
    sizes = [(random.randint(5, 30), random.randint(5, 30)) for _ in range(50)]
    n, edges = groups(sizes, 20)
    last_left = n - sum(sizes[-1]) + 1
    edges.append((last_left, last_left + 1))
    yield "late-conflict", text(n, edges)
    yield "big1", text(*relabel(200000, chain(200000)))
    yield "big2", text(*relabel(199999, ring(199999)))
    sizes = []
    while sum(map(sum, sizes)) < 190000:
        sizes.append((random.randint(10, 1500), random.randint(10, 1500)))
    n, edges = groups(sizes[:-1], 50)
    yield "big3", text(*relabel(n, edges))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
