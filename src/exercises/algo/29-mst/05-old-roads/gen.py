"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/05-old-roads   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big ใหญ่เกิน 300 KB จึงไม่เก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2905)

TOP = 10**9


def build(n, old, new):
    rows = [f"{n} {len(old)} {len(new)}"] + [f"{a} {b}" for a, b in old] + [f"{a} {b} {c}" for a, b, c in new]
    return "\n".join(rows)


def random_pairs(n, m):
    pairs = []
    while len(pairs) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            pairs.append((a, b))
    return pairs


def spanning(n):
    label = list(range(1, n + 1))
    random.shuffle(label)
    return [(label[random.randint(0, v - 1)], label[v]) for v in range(1, n)]


def priced(pairs, low, high):
    return [(a, b, random.randint(low, high)) for a, b in pairs]


def cases():
    yield "sample1", "6 3 5\n1 2\n2 3\n4 5\n3 4 8\n1 6 5\n5 6 4\n2 5 9\n4 6 6"
    yield "sample2", "4 4 2\n1 2\n2 3\n3 1\n3 4\n1 4 100\n2 4 50"
    yield "one-city", build(1, [], [])
    yield "impossible", build(5, [(1, 2), (2, 3)], [(3, 1, 4), (4, 5, 2)])
    # ถนนเก่าเป็นวงจร ถ้านับถนนเก่าเป็นเส้นของต้นไม้ จะหยุดเร็วเกินไป
    yield "old-cycle", build(5, [(1, 2), (2, 3), (3, 1)], [(3, 4, 2), (4, 5, 6), (1, 5, 9)])
    yield "no-old", build(5, [], [(1, 2, 3), (2, 3, 3), (3, 4, 3), (4, 5, 3), (5, 1, 3), (1, 3, 1)])
    yield "old-parallel", build(4, [(1, 2), (2, 1), (1, 2)], [(2, 3, 7), (3, 4, 7), (1, 4, 2), (1, 3, 9)])
    yield "max-cost", build(6, [(1, 2)], [(2, 3, TOP), (3, 4, TOP), (4, 5, TOP), (5, 6, TOP), (6, 1, TOP)])
    yield "rand1", build(12, random_pairs(12, 5), priced(random_pairs(12, 20), 1, 30))
    yield "rand2", build(3000, random_pairs(3000, 1500), priced(spanning(3000) + random_pairs(3000, 3000), 1, TOP))
    yield "big1", build(100000, random_pairs(100000, 60000), priced(spanning(100000) + random_pairs(100000, 100000), 1, TOP))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
