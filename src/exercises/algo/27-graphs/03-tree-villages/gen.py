"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/03-tree-villages   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขหมู่บ้านแบบสุ่ม
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนหมู่บ้าน big1 เป็นเส้นตรงเส้นเดียว big2 เป็นวงเดียว big3 สุ่ม
big1 กับ big2 ทำให้ DFS แบบ recursion ลึกสองแสนชั้นและพังเพราะ stack เต็ม ข้อนี้ไม่มี naive.cpp
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2703)


def relabel(n, edges):
    label = [0] + random.sample(range(1, n + 1), n)
    edges = [(label[a], label[b]) if random.random() < 0.5 else (label[b], label[a]) for a, b in edges]
    random.shuffle(edges)
    return n, edges


def chain(n, first=1):
    return [(v, v + 1) for v in range(first, first + n - 1)]


def ring(n, first=1):
    return chain(n, first) + [(first, first + n - 1)]


def random_tree(n, first=1):
    return [(first + v, first + random.randint(0, v - 1)) for v in range(1, n)]


def random_edges(n, m):
    seen = set()
    while len(seen) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            seen.add((min(a, b), max(a, b)))
    return sorted(seen)


def text(n, edges):
    return "\n".join([f"{n} {len(edges)}"] + [f"{a} {b}" for a, b in edges])


def forest(sizes, loops):
    """ต้นไม้สุ่มขนาดตาม sizes ต้นที่ index อยู่ใน loops เติมถนนอีกหนึ่งเส้นให้เกิดวง"""
    edges, first = [], 1
    for i, size in enumerate(sizes):
        part = random_tree(size, first)
        if i in loops and size >= 3:
            have = {(min(a, b), max(a, b)) for a, b in part}
            while True:
                a, b = random.randint(first, first + size - 1), random.randint(first, first + size - 1)
                if a != b and (min(a, b), max(a, b)) not in have:
                    part.append((a, b))
                    break
        edges += part
        first += size
    return first - 1, edges


def cases():
    yield "sample1", "9 9\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "sample2", "4 0"
    yield "single", "1 0"
    yield "triangle", text(*relabel(3, ring(3)))
    yield "chain", text(*relabel(2000, chain(2000)))
    yield "ring", text(*relabel(2000, ring(2000)))
    yield "star", text(*relabel(300, [(1, v) for v in range(2, 301)]))
    yield "forest", text(*relabel(*forest([random.randint(1, 40) for _ in range(60)], set())))
    yield "mixed", text(*relabel(*forest([random.randint(1, 40) for _ in range(80)], set(range(0, 80, 3)))))
    yield "rand", text(*relabel(3000, random_edges(3000, 2500)))
    n = 200000
    yield "big1", text(*relabel(n, chain(n)))
    yield "big2", text(*relabel(n, ring(n)))
    yield "big3", text(*relabel(n, random_edges(n, 150000)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
