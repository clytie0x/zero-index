"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/01-rumor-days   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขนักเรียนแบบสุ่ม
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนคน big1 เป็นเส้นตรงทั้งเส้นโดย S อยู่ปลาย big2 มีด้ามเส้นตรงยาวแสนห้าหมื่นคน
big3 เป็นเส้นตรงสองเส้นที่มาบรรจบกันที่ S ทั้งสามชุดทำให้ข่าวเดินทางนานเป็นแสนวัน
ตั้งใจให้วิธีจำลองทีละวันใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2701)


def relabel(n, edges, s):
    label = [0] + random.sample(range(1, n + 1), n)
    edges = [(label[a], label[b]) if random.random() < 0.5 else (label[b], label[a]) for a, b in edges]
    random.shuffle(edges)
    return n, edges, label[s]


def chain(n):
    return [(v, v + 1) for v in range(1, n)]


def random_edges(n, m, start=1):
    seen = set()
    while len(seen) < m:
        a, b = random.randint(start, n), random.randint(start, n)
        if a != b:
            seen.add((min(a, b), max(a, b)))
    return sorted(seen)


def text(n, edges, s):
    return "\n".join([f"{n} {len(edges)} {s}"] + [f"{a} {b}" for a, b in edges])


def cases():
    yield "sample1", "9 9 1\n1 2\n1 4\n2 3\n2 5\n4 5\n5 6\n3 6\n7 8\n8 9"
    yield "sample2", "5 2 5\n1 2\n3 4"
    yield "single", "1 0 1"
    yield "chain-end", text(*relabel(2000, chain(2000), 1))
    yield "chain-middle", text(*relabel(2001, chain(2001), 1001))
    yield "star", text(*relabel(500, [(1, v) for v in range(2, 501)], 7))
    yield "complete", text(*relabel(50, [(a, b) for a in range(1, 51) for b in range(a + 1, 51)], 1))
    yield "rand1", text(*relabel(30, random_edges(30, 25), 1))
    yield "rand2", text(*relabel(5000, random_edges(5000, 4000), 1))
    n = 200000
    yield "big1", text(*relabel(n, chain(n), 1))
    yield "big2", text(*relabel(n, chain(150000) + random_edges(n, 50000, 150000), 1))
    yield "big3", text(*relabel(n, chain(n), n // 2))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
