"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/05-one-way-streets   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขเมืองแบบสุ่ม โดยเมือง 1 ยังเป็นเมือง 1
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนเมือง big1 เป็นถนนทางเดียวต่อกันเป็นเส้นตรงออกจากเมือง 1
big2 เป็นเส้นตรงที่วิ่งเข้าหาเมือง 1 big3 เป็นวงใหญ่วงเดียวกับถนนสุ่มอีกแสนเส้น
ตั้งใจให้วิธี BFS จากทุกเมืองใน naive.cpp ไม่ทัน และ DFS แบบ recursion ที่ลึกสองแสนชั้นพัง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2705)


def relabel(n, roads):
    label = [0, 1] + random.sample(range(2, n + 1), n - 1)
    roads = [(label[a], label[b]) for a, b in roads]
    random.shuffle(roads)
    return n, roads


def forward(n):
    return [(v, v + 1) for v in range(1, n)]


def backward(n):
    return [(v + 1, v) for v in range(1, n)]


def random_roads(n, m, taken=()):
    taken = set(taken)
    seen = set()
    while len(seen) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b and (a, b) not in taken:
            seen.add((a, b))
    return sorted(seen)


def text(n, roads):
    return "\n".join([f"{n} {len(roads)}"] + [f"{a} {b}" for a, b in roads])


def cases():
    yield "sample1", "6 7\n1 2\n2 3\n3 1\n3 4\n4 5\n6 1\n5 4"
    yield "sample2", "3 0"
    yield "single", "1 0"
    yield "cycle", text(*relabel(1000, forward(1000) + [(1000, 1)]))
    yield "forward", text(*relabel(1000, forward(1000)))
    yield "backward", text(*relabel(1000, backward(1000)))
    yield "two-way", text(*relabel(1000, forward(1000) + backward(1000)))
    yield "star", text(*relabel(500, [(1, v) for v in range(2, 300)] + [(v, 1) for v in range(250, 501)]))
    yield "rand1", text(*relabel(12, random_roads(12, 18)))
    yield "rand2", text(*relabel(3000, random_roads(3000, 4500)))
    n = 200000
    yield "big1", text(*relabel(n, forward(n)))
    yield "big2", text(*relabel(n, backward(n)))
    ring = forward(n) + [(n, 1)]
    yield "big3", text(*relabel(n, ring + random_roads(n, 100000, ring)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
