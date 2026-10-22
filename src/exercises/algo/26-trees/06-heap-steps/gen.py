"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/06-heap-steps   (รันที่รากของโปรเจกต์)

มีชุดที่ค่าซ้ำกันเยอะ เพื่อจับโปรแกรมที่เลือกลูกหรือสลับตอนค่าเท่ากันผิดกติกา
ชุดที่ชื่อขึ้นต้นด้วย big มีค่าเริ่มต้นแสนค่าและคำสั่งแสนคำสั่ง ไฟล์ใหญ่เกินจะเก็บใน git ข้อนี้ไม่มี naive
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2606)


def build(values, ops):
    lines = [str(len(values)), " ".join(map(str, values)), str(len(ops))]
    lines += ["-" if x is None else f"+ {x}" for x in ops]
    return "\n".join(lines)


def random_ops(q, size, low, high, pop_rate):
    """สุ่มคำสั่ง ไม่หยิบออกตอนฮีปว่าง"""
    ops = []
    for _ in range(q):
        if size > 0 and random.random() < pop_rate:
            ops.append(None)
            size -= 1
        else:
            ops.append(random.randint(low, high))
            size += 1
    return ops


def cases():
    yield "sample1", build([30, 50, 10, 80, 20, 70, 60, 40], [None, 90, None, None, 55])
    yield "single", build([7], [None, 3, 9, None, None])
    yield "all-equal", build([5] * 20, [5, None, 5, None, None, 5])
    values = [random.randint(1, 3) for _ in range(40)]
    yield "few-values", build(values, random_ops(60, 40, 1, 3, 0.5))
    yield "ascending", build(list(range(1, 501)), [None] * 100 + list(range(1000, 1100)))
    yield "descending", build(list(range(500, 0, -1)), list(range(1, 101)) + [None] * 300)
    yield "drain", build([random.randint(1, 100) for _ in range(30)], [None] * 30)
    yield "rand1", build([random.randint(1, 50) for _ in range(10)], random_ops(12, 10, 1, 50, 0.5))
    values = [random.randint(1, 10**9) for _ in range(3000)]
    yield "rand2", build(values, random_ops(3000, 3000, 1, 10**9, 0.6))
    values = [random.randint(1, 10**9) for _ in range(100000)]
    yield "big1", build(values, random_ops(100000, 100000, 1, 10**9, 0.5))
    values = [random.randint(1, 5) for _ in range(100000)]
    yield "big2", build(values, random_ops(100000, 100000, 1, 5, 0.7))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
