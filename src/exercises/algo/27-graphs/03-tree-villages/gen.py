"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/03-tree-villages   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขหมู่บ้านแบบสุ่ม
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนหมู่บ้าน big1 เป็นเส้นตรงเส้นเดียว big2 เป็นวงแหวนวงเดียว
big3 เป็นวงแหวน เขตที่มีวงจรแบบอื่น และต้นไม้ปนกัน
big1 กับ big2 ทำให้ DFS แบบ recursion ลึกสองแสนชั้นและพังเพราะ stack เต็ม ข้อนี้ไม่มี naive.cpp
lollipop mixed shapes big3 มีเขตที่ถนนเท่ากับจำนวนหมู่บ้านแต่ไม่ใช่วงแหวน (วงจรมีหาง)
ดักวิธีที่ตัดสินวงแหวนจากจำนวนถนนอย่างเดียว และวิธีที่นับทุกเขตที่มีถนนวนเป็นวงแหวน
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


def lollipop(cycle, tail, first=1):
    """วงจรยาว cycle มีหางเป็นเส้นตรงยาว tail ต่อออกจากจุดแรกของวง ถนนเท่ากับจำนวนหมู่บ้านพอดี"""
    edges = ring(cycle, first)
    prev = first
    for v in range(first + cycle, first + cycle + tail):
        edges.append((prev, v))
        prev = v
    return edges


def figure_eight(a, b, first=1):
    """วงจรสองวงยาว a กับ b ใช้หมู่บ้านแรกร่วมกัน"""
    edges = ring(a, first)
    loop = [first] + list(range(first + a, first + a + b - 1))
    edges += [(loop[i], loop[i + 1]) for i in range(len(loop) - 1)] + [(loop[-1], first)]
    return edges


def shapes(kinds):
    """ต่อเขตหลายแบบเข้าด้วยกัน kinds เป็นรายการของ (ชนิด, ขนาด)"""
    edges, first = [], 1
    for kind, size in kinds:
        if kind == "tree":
            part = random_tree(size, first)
        elif kind == "ring":
            part = ring(size, first)
        elif kind == "lollipop":
            tail = random.randint(1, size - 3)
            part = lollipop(size - tail, tail, first)
        elif kind == "eight":
            a = random.randint(3, size - 2)
            part = figure_eight(a, size - a + 1, first)
        else:
            part = random_tree(size, first)
            have = {(min(a, b), max(a, b)) for a, b in part}
            while len(part) < size + 1:
                a, b = random.randint(first, first + size - 1), random.randint(first, first + size - 1)
                if a != b and (min(a, b), max(a, b)) not in have:
                    have.add((min(a, b), max(a, b)))
                    part.append((a, b))
        edges += part
        first += size
    return first - 1, edges


def random_kinds(count, low, high):
    kinds = []
    for _ in range(count):
        kind = random.choice(["tree", "ring", "lollipop", "eight", "extra"])
        kinds.append((kind, random.randint(max(low, 5), high)))
    return kinds


def cases():
    yield "sample1", "9 9\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "sample2", "7 6\n1 2\n2 3\n3 4\n4 1\n5 6\n6 7"
    yield "single", "1 0"
    yield "triangle", text(*relabel(3, ring(3)))
    yield "lollipop", text(*relabel(6, lollipop(3, 3)))
    yield "chain", text(*relabel(2000, chain(2000)))
    yield "ring", text(*relabel(2000, ring(2000)))
    yield "star", text(*relabel(300, [(1, v) for v in range(2, 301)]))
    yield "forest", text(*relabel(*shapes([("tree", random.randint(1, 40)) for _ in range(60)])))
    yield "mixed", text(*relabel(*shapes([("tree" if i % 3 else "extra", random.randint(3, 40)) for i in range(80)])))
    yield "shapes", text(*relabel(*shapes(random_kinds(150, 5, 30))))
    yield "rand", text(*relabel(3000, random_edges(3000, 2500)))
    n = 200000
    yield "big1", text(*relabel(n, chain(n)))
    yield "big2", text(*relabel(n, ring(n)))
    kinds = []
    while sum(size for _, size in kinds) < 190000:
        kinds += random_kinds(1, 5, 3000)
    yield "big3", text(*relabel(*shapes(kinds)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
