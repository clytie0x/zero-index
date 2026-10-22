"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/06-open-day   (รันที่รากของโปรเจกต์)

naive.cpp เปิดถนนทีละวัน แล้ว BFS ตรวจว่าทุกเมืองถึงกันหรือยัง O(D(N + M)) เมื่อ D คือจำนวนวันที่ต่างกัน
ชุดที่ชื่อขึ้นต้นด้วย big มีถนนสองแสนเส้นที่เปิดคนละวัน ซึ่ง naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2906)

TOP = 10**9


def build(n, roads):
    return "\n".join([f"{n} {len(roads)}"] + [f"{a} {b} {d}" for a, b, d in roads])


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


def cases():
    yield "sample1", "5 7\n1 2 4\n2 3 9\n3 4 2\n4 5 9\n1 3 6\n2 5 12\n1 5 9"
    yield "sample2", "4 3\n1 2 1\n2 1 5\n3 4 2"
    yield "two-cities", build(2, [(2, 1, TOP)])
    yield "same-day", build(6, [(a, a % 6 + 1, 77) for a in range(1, 7)] + [(1, 4, 77)])
    # วันคำตอบมีถนนหลายเส้น บางเส้นอยู่หลังเส้นที่ทำให้ครบในลำดับที่เรียง
    yield "tie-after", build(5, [(1, 2, 3), (3, 4, 3), (2, 3, 8), (4, 5, 8), (5, 1, 8), (2, 4, 8), (1, 3, 10)])
    yield "never", build(6, [(1, 2, 5), (2, 3, 6), (4, 5, 1), (5, 6, 2), (6, 4, 3), (1, 3, 9)])
    yield "late-bridge", build(8, [(1, 2, 1), (2, 3, 2), (3, 4, 3), (5, 6, 4), (6, 7, 5), (7, 8, 6), (4, 5, TOP), (1, 8, TOP - 1)])
    yield "rand1", build(10, [(a, b, random.randint(1, 15)) for a, b in connected(10, 18)])
    yield "rand2", build(3000, [(a, b, random.randint(1, TOP)) for a, b in connected(3000, 6000)])
    yield "big1", build(100000, [(a, b, d) for (a, b), d in zip(connected(100000, 200000), random.sample(range(1, TOP + 1), 200000))])
    yield "big2", build(100000, [(a, b, random.randint(1, 300000)) for a, b in connected(100000, 200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
