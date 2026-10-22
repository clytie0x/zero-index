"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/03-water-pipes   (รันที่รากของโปรเจกต์)

naive.cpp ทำ Kruskal แต่ตรวจว่าสองหมู่บ้านถึงกันแล้วหรือยังด้วย BFS บนท่อที่เลือกไว้ทุกแนว O(NM)
ชุดที่ชื่อขึ้นต้นด้วย big มีหมู่บ้านแสนแห่ง ซึ่ง naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2903)

TOP = 10**9


def build(n, pipes):
    return "\n".join([f"{n} {len(pipes)}"] + [f"{a} {b} {c}" for a, b, c in pipes])


def connected(n, m, low, high):
    """ต้นไม้สุ่มให้ต่อถึงกันแน่ แล้วเติมแนวสุ่มจนครบ m แนว สลับหมายเลขและลำดับ"""
    label = list(range(1, n + 1))
    random.shuffle(label)
    pairs = [(label[random.randint(0, v - 1)], label[v]) for v in range(1, n)]
    while len(pairs) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            pairs.append((a, b))
    random.shuffle(pairs)
    return [(a, b, random.randint(low, high)) for a, b in pairs]


def cases():
    yield "sample1", "5 7\n1 2 40\n1 3 25\n2 3 10\n2 4 30\n3 4 45\n4 5 20\n3 5 60"
    yield "sample2", "4 3\n1 2 5\n2 1 3\n3 4 7"
    yield "one-village", build(1, [])
    yield "no-pipe", build(3, [])
    yield "parallel", build(3, [(1, 2, 9), (2, 1, 4), (1, 2, 6), (2, 3, 8), (3, 2, 8)])
    yield "same-cost", build(6, [(a, b, 7) for a in range(1, 7) for b in range(a + 1, 7)])
    # ราคารวม 3 × 10^9 เกิน int
    yield "over-int", build(4, [(1, 2, TOP), (2, 3, TOP), (3, 4, TOP), (1, 4, TOP)])
    # หมู่บ้านสุดท้ายไม่มีท่อไปถึง
    yield "one-left", build(8, connected(7, 15, 1, 100))
    yield "rand1", build(8, connected(8, 14, 1, 20))
    yield "rand2", build(2000, connected(2000, 6000, 1, TOP))
    yield "big1", build(100000, connected(100000, 200000, 1, TOP))
    yield "big2", build(100000, connected(100000, 100000, TOP - 1000, TOP))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
