"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/02-first-loop   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2902)


def build(n, roads):
    return "\n".join([f"{n} {len(roads)}"] + [f"{a} {b}" for a, b in roads])


def random_tree(n):
    """ถนน n - 1 เส้นที่ไม่ทำให้วนเลย สลับลำดับและหมายเลขอำเภอ"""
    label = list(range(1, n + 1))
    random.shuffle(label)
    roads = [(label[random.randint(0, v - 1)], label[v]) for v in range(1, n)]
    random.shuffle(roads)
    return [(a, b) if random.random() < 0.5 else (b, a) for a, b in roads]


def random_roads(n, m):
    roads = []
    while len(roads) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            roads.append((a, b))
    return roads


def cases():
    yield "sample1", "5 6\n1 2\n3 4\n2 3\n5 4\n1 3\n2 5"
    yield "sample2", "4 3\n1 2\n2 3\n4 1"
    yield "two-towns", build(2, [(1, 2)])
    yield "duplicate", build(2, [(1, 2), (2, 1), (1, 2)])
    # วงที่ปิดตอนเส้นสุดท้ายพอดี
    yield "last-closes", build(6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])
    # ถนนต่อกันเป็นวงย่อยตั้งแต่เส้นที่ 3 แต่อำเภอทั้งหมดยังไม่ถึงกัน
    yield "early-loop", build(7, [(1, 2), (2, 3), (3, 1), (4, 5), (6, 7), (5, 6), (7, 4), (1, 4)])
    yield "tree", build(1000, random_tree(1000))
    yield "rand1", build(30, random_roads(30, 25))
    yield "rand2", build(3000, random_tree(3000)[:2000] + random_roads(3000, 2000))
    yield "big1", build(100000, random_tree(100000) + random_roads(100000, 5))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
