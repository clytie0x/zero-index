"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/04-chat-rooms   (รันที่รากของโปรเจกต์)

naive.cpp คือ union-find แบบตรงไปตรงมาที่จำขนาดไว้ที่หัวหน้า แต่ไม่มี path compression และ union by size
ชุดที่ชื่อขึ้นต้นด้วย big มีผู้ใช้สองแสนคน big1 รวมห้องต่อกันเป็นทอดๆ ให้ต้นไม้ของ naive.cpp เป็นเส้นตรง แล้วถามซ้ำสองแสนครั้ง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2904)


def build(n, ops):
    return "\n".join([f"{n} {len(ops)}"] + [" ".join(map(str, op)) for op in ops])


def random_ops(n, q, merge_share):
    ops = []
    for _ in range(q):
        r = random.random()
        a, b = random.randint(1, n), random.randint(1, n)
        if r < merge_share:
            ops.append((1, a, b))
        elif r < merge_share + (1 - merge_share) / 2:
            ops.append((2, a, b))
        else:
            ops.append((3, a))
    return ops


def chain_then_ask(n, asks):
    ops = [(1, i, i + 1) for i in range(1, n)]
    for k in range(asks):
        x = random.randint(1, n)
        ops.append((2, 1, x) if k % 2 == 0 else (3, x))
    return ops


def cases():
    yield "sample1", "6 9\n1 1 2\n2 1 2\n2 1 3\n1 3 4\n1 4 2\n3 1\n1 1 3\n3 4\n2 5 6"
    yield "single", build(1, [(3, 1), (2, 1, 1), (1, 1, 1), (3, 1)])
    yield "same-room", build(4, [(1, 1, 2), (1, 2, 1), (1, 1, 2), (3, 1), (3, 2), (3, 3)])
    # ห้องเล็กรวมเข้าห้องใหญ่ แล้วถามขนาดจากคนที่ไม่ใช่หัวหน้า
    yield "not-leader", build(8, [(1, 1, 2), (1, 3, 4), (1, 1, 3), (1, 5, 6), (1, 7, 5), (3, 4), (3, 6), (3, 7), (1, 8, 2), (3, 3), (2, 6, 8)])
    yield "chain", build(500, chain_then_ask(500, 500))
    yield "rand1", build(10, random_ops(10, 40, 0.3))
    yield "rand2", build(3000, random_ops(3000, 6000, 0.5))
    yield "few-merges", build(2000, random_ops(2000, 4000, 0.05))
    yield "big1", build(200000, chain_then_ask(200000, 200001))
    yield "big2", build(200000, random_ops(200000, 400000, 0.5))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
