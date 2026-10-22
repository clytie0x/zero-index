"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/04-coldest-station   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนสถานีและสองแสนเหตุการณ์ คำถามครอบเกือบทั้งแนว
ตั้งใจให้วิธีไล่หาค่าต่ำสุดทุกคำถามใน naive.cpp ไม่ทัน
extreme ใช้ค่า -10^9 และ 10^9 จับคนที่ตั้งค่าเริ่มต้นของค่าต่ำสุดเป็น 0 หรือ 1000000
tie กับ rand3 มีค่าซ้ำมาก จับคนที่รวมสองลูกแล้วเลือกฝั่งขวาเมื่ออุณหภูมิเท่ากัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3004)

TOP = 10**9


def build(temps, events):
    rows = [f"{len(temps)} {len(events)}", " ".join(map(str, temps))]
    rows += [" ".join(map(str, e)) for e in events]
    return "\n".join(rows) + "\n"


def random_events(n, q, low, high, wide):
    events = []
    for _ in range(q):
        if random.random() < 0.5:
            events.append((1, random.randint(1, n), random.randint(low, high)))
        elif wide:
            events.append((2, random.randint(1, 50), random.randint(n - 50, n)))
        else:
            l, r = sorted((random.randint(1, n), random.randint(1, n)))
            events.append((2, l, r))
    return events


def cases():
    yield "sample1", build([12, 5, 9, -3, 7, 4], [(2, 1, 3), (2, 2, 6), (1, 4, 10), (2, 2, 6), (1, 2, 8), (2, 1, 2)])
    yield "single", build([-5], [(2, 1, 1), (1, 1, 30), (2, 1, 1)])
    yield "all-positive", build([30, 25, 40, 35], [(2, 1, 4), (2, 3, 4), (1, 2, 50), (2, 1, 2)])
    yield "extreme", build([TOP, TOP, TOP], [(2, 1, 3), (1, 2, -TOP), (2, 1, 3), (2, 3, 3), (1, 2, TOP), (2, 1, 2)])
    # ขอบของช่วงที่ไม่ลงตัวกับต้นไม้ และสถานีสุดท้ายของแนว
    yield "edges", build([9, 8, 7, 6, 5, 4, 3], [(2, 7, 7), (2, 1, 1), (2, 2, 6), (2, 3, 5), (1, 7, 100), (2, 5, 7), (2, 1, 7)])
    # หลายสถานีหนาวเท่ากัน ต้องตอบหมายเลขน้อยสุด ทั้งในต้นไม้ย่อยเดียวกันและคนละฝั่ง
    yield "tie", build([4, 1, 7, 1, 1, 9, 1, 3], [(2, 1, 8), (2, 3, 8), (2, 5, 8), (1, 2, 5), (2, 1, 8), (1, 4, 1), (2, 3, 4), (2, 6, 7)])
    yield "rand1", build([random.randint(-20, 20) for _ in range(15)], random_events(15, 40, -20, 20, False))
    yield "rand2", build([random.randint(-TOP, TOP) for _ in range(3000)], random_events(3000, 3000, -TOP, TOP, False))
    yield "rand3", build([random.randint(0, 5) for _ in range(1000)], random_events(1000, 2000, 0, 5, False))
    n = 200000
    yield "big1", build([random.randint(-TOP, TOP) for _ in range(n)], random_events(n, n, -TOP, TOP, True))
    yield "big2", build([random.randint(0, TOP) for _ in range(n)], [(2, 1, n)] * (n // 2) + random_events(n, n // 2, 0, TOP, True))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
