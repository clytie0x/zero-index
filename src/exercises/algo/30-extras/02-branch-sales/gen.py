"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/02-branch-sales   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนสาขาและสองแสนเหตุการณ์ คำถามเกือบทุกข้อครอบเกือบทั้งถนน
ตั้งใจให้วิธีบวกทีละสาขาใน naive.cpp ไม่ทัน
set-twice ตั้งยอดสาขาเดิมซ้ำหลายครั้ง จับคนที่บวก v เพิ่มแทนการแทนที่
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3002)

TOP = 10**9


def build(sales, events):
    rows = [f"{len(sales)} {len(events)}", " ".join(map(str, sales))]
    rows += [" ".join(map(str, e)) for e in events]
    return "\n".join(rows) + "\n"


def random_events(n, q, top, wide):
    events = []
    for _ in range(q):
        if random.random() < 0.5:
            events.append((1, random.randint(1, n), random.randint(0, top)))
        elif wide:
            events.append((2, random.randint(1, 50), random.randint(n - 50, n)))
        else:
            l, r = sorted((random.randint(1, n), random.randint(1, n)))
            events.append((2, l, r))
    return events


def cases():
    yield "sample1", build([120, 80, 0, 45, 300], [(2, 1, 5), (1, 3, 60), (2, 2, 4), (1, 1, 100), (1, 3, 10), (2, 1, 3)])
    yield "single", build([7], [(2, 1, 1), (1, 1, 0), (2, 1, 1), (1, 1, 5), (2, 1, 1)])
    yield "set-twice", build([10, 20, 30], [(1, 2, 50), (1, 2, 50), (1, 2, 5), (2, 1, 3), (1, 1, 0), (2, 1, 2)])
    yield "one-branch", build([1, 2, 3, 4, 5, 6], [(2, 3, 3), (2, 6, 6), (2, 1, 1), (1, 6, 0), (2, 6, 6), (2, 5, 6)])
    yield "over-int", build([TOP] * 10, [(2, 1, 10), (1, 5, 0), (2, 1, 10), (2, 4, 6), (1, 5, TOP), (2, 3, 7)])
    yield "only-ask", build([random.randint(0, 100) for _ in range(50)], [(2, 1, 50), (2, 10, 20), (2, 50, 50)])
    sales = [random.randint(0, 50) for _ in range(20)]
    yield "rand1", build(sales, random_events(20, 40, 50, False))
    sales = [random.randint(0, TOP) for _ in range(3000)]
    yield "rand2", build(sales, random_events(3000, 3000, TOP, False))
    n = 200000
    sales = [random.randint(0, TOP) for _ in range(n)]
    yield "big1", build(sales, random_events(n, n, TOP, True))
    sales = [random.randint(0, TOP) for _ in range(n)]
    yield "big2", build(sales, [(2, 1, n)] * (n // 2) + random_events(n, n // 2, TOP, True))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
