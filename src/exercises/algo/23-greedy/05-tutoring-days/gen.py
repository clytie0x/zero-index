"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/05-tutoring-days   (รันที่รากของโปรเจกต์)

nested ทำให้วิธีเรียงตามวันแรกแล้วนัดที่วันแรกผิด และวิธีเรียงตามวันแรกแล้วนัดที่วันสุดท้ายผิด
touch ทำให้วิธีที่นัดเพิ่มเมื่อวันแรกเท่ากับวันนัดล่าสุดผิด
big1 ใหญ่เกิน 300 KB จึงตั้งชื่อขึ้นต้นด้วย big ข้อนี้ไม่มี naive
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2305)


def build(spans):
    return f"{len(spans)}\n" + "\n".join(f"{a} {b}" for a, b in spans)


def random_spans(n, top, longest):
    spans = []
    for _ in range(n):
        a = random.randint(1, top)
        spans.append((a, min(top, a + random.randint(0, longest))))
    return spans


def cases():
    yield "sample1", build([(1, 4), (2, 6), (5, 8), (7, 10), (9, 9)])
    yield "sample2", build([(3, 3), (3, 3), (3, 3)])
    yield "single", build([(1000000000, 1000000000)])
    yield "nested", build([(1, 100), (10, 20), (30, 40), (15, 35)])
    yield "touch", build([(1, 5), (5, 9), (9, 12), (12, 20)])
    yield "apart", build([(1, 1), (3, 3), (5, 5), (7, 7), (1000000000, 1000000000)])
    yield "rand1", build(random_spans(15, 40, 6))
    yield "rand2", build(random_spans(2000, 100000, 300))
    yield "big1", build(random_spans(200000, 10**9, 50000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
