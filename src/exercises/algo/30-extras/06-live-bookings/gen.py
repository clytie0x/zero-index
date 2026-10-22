"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/06-live-bookings   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนคืนและสองแสนเหตุการณ์ การจองแต่ละครั้งยาวเกือบทั้งช่วง
ตั้งใจให้วิธีบวกทีละคืนใน naive.cpp ไม่ทัน
last-night จองถึงคืนสุดท้าย ถ้าลบที่ r + 1 โดยไม่ระวังจะเขียนเลยขอบ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3006)

TOP = 10**9


def build(n, events):
    rows = [f"{n} {len(events)}"] + [" ".join(map(str, e)) for e in events]
    return "\n".join(rows) + "\n"


def random_events(n, q, top, wide):
    events = []
    for _ in range(q):
        if random.random() < 0.5:
            if wide:
                l, r = random.randint(1, 50), random.randint(n - 50, n)
            else:
                l, r = sorted((random.randint(1, n), random.randint(1, n)))
            events.append((1, l, r, random.randint(1, top)))
        else:
            events.append((2, random.randint(1, n)))
    return events


def cases():
    yield "sample1", build(7, [(1, 2, 4, 3), (2, 3), (1, 1, 2, 5), (2, 2), (2, 5), (1, 3, 3, 4), (2, 3), (2, 4)])
    yield "single", build(1, [(2, 1), (1, 1, 1, 9), (2, 1), (1, 1, 1, 1), (2, 1)])
    yield "ask-first", build(5, [(2, 1), (2, 5), (1, 1, 5, 2), (2, 3)])
    yield "last-night", build(6, [(1, 4, 6, 7), (1, 6, 6, 1), (2, 6), (2, 5), (2, 3), (1, 1, 6, 2), (2, 6)])
    yield "one-night", build(5, [(1, 3, 3, 8), (2, 2), (2, 3), (2, 4), (1, 1, 1, 5), (2, 1), (2, 2)])
    yield "over-int", build(4, [(1, 1, 4, TOP)] * 5 + [(2, 1), (2, 4), (1, 2, 3, TOP), (2, 2)])
    yield "rand1", build(15, random_events(15, 40, 9, False))
    yield "rand2", build(3000, random_events(3000, 3000, TOP, False))
    n = 200000
    yield "big1", build(n, random_events(n, n, TOP, True))
    yield "big2", build(n, [(1, 1, n, random.randint(1, 1000)) for _ in range(n // 2)] + [(2, random.randint(1, n)) for _ in range(n // 2)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
