"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/07-nearest-branch   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขหมู่บ้านแบบสุ่ม และให้รายชื่อสาขาไม่เรียง
ชุดที่ชื่อขึ้นต้นด้วย big big1 เป็นเส้นตรงสองแสนหมู่บ้านมีสองหมื่นสาขา big2 สุ่มสองแสนหมู่บ้านมีหนึ่งหมื่นสาขา
big3 เป็นตาราง 250 × 500 ที่ระยะเสมอกันบ่อยมาก มีห้าพันสาขา ตั้งใจให้วิธี BFS จากทุกสาขาใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2707)


def relabel(n, edges, branches):
    label = [0] + random.sample(range(1, n + 1), n)
    edges = [(label[a], label[b]) if random.random() < 0.5 else (label[b], label[a]) for a, b in edges]
    random.shuffle(edges)
    branches = [label[b] for b in branches]
    random.shuffle(branches)
    return n, edges, branches


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


def random_edges(n, m):
    seen = set()
    while len(seen) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            seen.add((min(a, b), max(a, b)))
    return sorted(seen)


def pick(n, k):
    return random.sample(range(1, n + 1), k)


def text(n, edges, branches):
    return "\n".join([f"{n} {len(edges)} {len(branches)}", " ".join(map(str, branches))] + [f"{a} {b}" for a, b in edges])


def cases():
    yield "sample1", "5 4 2\n5 1\n1 2\n2 3\n3 4\n4 5"
    yield "sample2", "9 9 2\n9 4\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "single", "1 0 1\n1"
    yield "all-branches", text(*relabel(50, random_edges(50, 80), list(range(1, 51))))
    yield "no-roads", text(*relabel(20, [], [3, 7, 11]))
    yield "grid", text(*relabel(900, grid(30, 30), [1, 30, 871, 900, 436]))
    yield "chain", text(*relabel(3000, chain(3000), pick(3000, 40)))
    yield "star", text(*relabel(400, [(1, v) for v in range(2, 401)], [5, 9, 300]))
    yield "rand1", text(*relabel(15, random_edges(15, 14), pick(15, 3)))
    yield "rand2", text(*relabel(5000, random_edges(5000, 5000), pick(5000, 60)))
    n = 200000
    yield "big1", text(*relabel(n, chain(n), pick(n, 20000)))
    yield "big2", text(*relabel(n, random_edges(n, 200000), pick(n, 10000)))
    yield "big3", text(*relabel(125000, grid(250, 500), pick(125000, 5000)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
