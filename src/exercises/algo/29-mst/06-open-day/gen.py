"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/06-open-day   (รันที่รากของโปรเจกต์)

naive.cpp เปิดถนนทีละวัน แล้ว BFS จากเมือง 1 ทุกวัน O(D(N + M)) เมื่อ D คือจำนวนวันที่ต่างกัน
ชุดที่ชื่อขึ้นต้นด้วย big มีถนนสองแสนเส้นที่เปิดคนละวัน ซึ่ง naive.cpp ไม่ทัน
big2 เป็นสายยาวแสนเมืองที่สลับหมายเลข เมือง 1 อยู่ปลายสาย ถนนเปิดไล่จากเมือง 1 ออกไปวันละเส้น
ถ้าเดินบนต้นไม้ด้วย DFS แบบ recursion จะลึกเกือบแสนชั้น
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


def random_pairs(n, m):
    pairs = []
    while len(pairs) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            pairs.append((a, b))
    return pairs


def long_line(n, extra):
    """สายยาว n เมือง เมือง 1 อยู่ปลาย ถนนเส้นที่ k นับจากเมือง 1 เปิดวันที่ k
    ถนนเพิ่มอีก extra เส้นเปิดหลังสายต่อครบ จึงไม่เปลี่ยนคำตอบ"""
    label = [1] + random.sample(range(2, n + 1), n - 1)
    roads = [(label[k - 1], label[k], k) for k in range(1, n)]
    roads += [(a, b, random.randint(n, TOP)) for a, b in random_pairs(n, extra)]
    random.shuffle(roads)
    return roads


def cases():
    yield "sample1", "5 7\n1 2 4\n2 3 9\n3 4 2\n4 5 9\n1 3 6\n2 5 12\n1 5 9"
    yield "sample2", "4 3\n1 2 1\n2 1 5\n3 4 2"
    yield "two-cities", build(2, [(2, 1, TOP)])
    yield "same-day", build(6, [(a, a % 6 + 1, 77) for a in range(1, 7)] + [(1, 4, 77)])
    # ถนนของเมือง 3 กับ 4 เปิดก่อน แต่ไปถึงเมือง 1 ได้ตอนถนน 1-2 เปิด
    yield "own-road-early", build(4, [(3, 4, 1), (2, 3, 2), (1, 2, 50)])
    # ถนนเปิดไล่จากเมือง 1 ออกไปโดยวันลดลง คำตอบคือวันที่มากที่สุดบนทาง ไม่ใช่วันของถนนเส้นสุดท้าย
    yield "max-on-path", build(6, [(1, 2, 100), (2, 3, 90), (3, 4, 80), (4, 5, 70), (5, 6, 60), (1, 6, 200)])
    yield "never", build(6, [(1, 2, 5), (2, 3, 6), (4, 5, 1), (5, 6, 2), (6, 4, 3), (1, 3, 9)])
    yield "late-bridge", build(8, [(1, 2, 1), (2, 3, 2), (3, 4, 3), (5, 6, 4), (6, 7, 5), (7, 8, 6), (4, 5, TOP), (1, 8, TOP - 1)])
    yield "rand1", build(10, [(a, b, random.randint(1, 15)) for a, b in connected(10, 18)])
    yield "rand2", build(3000, [(a, b, random.randint(1, TOP)) for a, b in connected(3000, 6000)])
    yield "rand-parts", build(500, [(a, b, random.randint(1, 1000)) for a, b in random_pairs(500, 400)])
    yield "big1", build(100000, [(a, b, d) for (a, b), d in zip(connected(100000, 200000), random.sample(range(1, TOP + 1), 200000))])
    yield "big2", build(100000, long_line(100000, 100000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
