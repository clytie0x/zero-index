"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/04-nearest-shelter   (รันที่รากของโปรเจกต์)

naive.cpp รัน Dijkstra จากศูนย์ทีละแห่ง ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีศูนย์หลักพันถึงหลักหมื่นแห่ง ตั้งใจให้รันทีละแห่งไม่ทัน
over-int และ big2 มีเวลาอพยพเกิน int ส่วน stranded rand2 และ big1 มีหมู่บ้านที่ไปไม่ถึงศูนย์
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2804)


def build(n, edges, shelters):
    rows = [f"{n} {len(edges)} {len(shelters)}"] + [f"{u} {v} {w}" for u, v, w in edges]
    rows.append(" ".join(map(str, shelters)))
    return "\n".join(rows)


def forest(n, m, top, parts):
    """หมู่บ้าน n แห่งแบ่งเป็น parts ก้อนที่ไม่เชื่อมกัน ในแต่ละก้อนไปถึงกันได้หมด"""
    label = list(range(1, n + 1))
    random.shuffle(label)
    groups = [label[i::parts] for i in range(parts)]
    edges = []
    for g in groups:
        for i in range(1, len(g)):
            edges.append((g[random.randrange(i)], g[i], random.randint(1, top)))
    while len(edges) < m:
        g = random.choice(groups)
        if len(g) < 2:
            continue
        u, v = random.sample(g, 2)
        edges.append((u, v, random.randint(1, top)))
    random.shuffle(edges)
    return edges, groups


def cases():
    yield "sample1", "8 9 2\n1 2 7\n2 3 4\n3 4 6\n4 5 3\n5 6 5\n6 7 2\n7 8 9\n2 7 15\n3 6 8\n2 6"
    yield "sample2", "6 3 2\n1 2 5\n2 3 5\n4 5 1\n1 1"
    yield "alone", build(1, [], [1])
    yield "all-shelters", build(4, [(1, 2, 9), (2, 3, 9), (3, 4, 9)], [4, 3, 2, 1])
    # ศูนย์อยู่ปลายเส้นสองข้าง หมู่บ้านตรงกลางห่างทั้งสองข้างเกิน int
    yield "over-int", build(7, [(i, i + 1, 10**9) for i in range(1, 7)], [1, 7, 7])
    edges, groups = forest(10, 14, 20, 3)
    yield "stranded", build(10, edges, [groups[0][0], groups[1][0]])
    edges, groups = forest(40, 80, 100, 1)
    yield "rand1", build(40, edges, random.sample(range(1, 41), 3))
    edges, groups = forest(3000, 6000, 10**9, 4)
    yield "rand2", build(3000, edges, random.sample(groups[0], 20) + random.sample(groups[1], 10) + random.sample(groups[2], 5))
    edges, groups = forest(100000, 200000, 10**9, 2)
    yield "big1", build(100000, edges, random.sample(groups[0], 20000))
    # ถนนเป็นเส้นยาวเส้นเดียว มีถนนซ้ำคู่ที่แพงกว่า ศูนย์ 2000 แห่งกระจายห่างกันมาก
    n = 100000
    chain = [(i, i + 1, random.randint(5 * 10**8, 10**9)) for i in range(1, n)]
    extra = []
    for _ in range(100000):
        i = random.randint(1, n - 1)
        extra.append((i + 1, i, 10**9))
    edges = chain + extra
    random.shuffle(edges)
    yield "big2", build(n, edges, sorted(random.sample(range(1, n + 1), 2000)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
