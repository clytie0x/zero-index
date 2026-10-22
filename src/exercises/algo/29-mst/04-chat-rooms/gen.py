"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/04-chat-rooms   (รันที่รากของโปรเจกต์)

naive.cpp เก็บหมายเลขห้องของทุกคน รวมห้องโดยไล่เปลี่ยนหมายเลขของผู้ใช้ทุกคน O(N) ต่อการรวม
ชุดที่ชื่อขึ้นต้นด้วย big มีผู้ใช้สองแสนคน big1 รวมห้องต่อกันเป็นทอดๆ เกือบสองแสนครั้ง แล้วถามอีกสองแสนครั้ง
ห้องใหญ่ถูกย้ายเข้าห้องคนเดียวทุกครั้ง ถ้าใช้หัวหน้าของ union by size เป็นหมายเลขห้องจะตอบผิด
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
        a, b = random.randint(1, n), random.randint(1, n)
        if random.random() < merge_share:
            ops.append((1, a, b))
        else:
            ops.append((2, a))
    return ops


def chain_then_ask(n, asks):
    """ห้องของ i ย้ายเข้าห้องของ i + 1 ทุก i หมายเลขห้องสุดท้ายคือ n
    ถามผู้ใช้ 1 ก่อน ซึ่งอยู่ลึกที่สุดถ้าต่อหัวหน้าของ b ใต้ a เสมอโดยไม่มี union by size"""
    ops = [(1, i + 1, i) for i in range(1, n)] + [(2, 1)]
    for _ in range(asks - 1):
        ops.append((2, random.randint(1, n)))
    return ops


def cases():
    yield "sample1", "6 10\n1 2 3\n2 3\n1 4 2\n2 3\n1 5 6\n1 4 6\n2 6\n2 1\n1 3 2\n2 2"
    yield "single", build(1, [(2, 1), (1, 1, 1), (2, 1)])
    yield "same-room", build(4, [(1, 1, 2), (1, 2, 1), (1, 1, 2), (1, 3, 3), (2, 1), (2, 2), (2, 3)])
    # ห้องห้าคนย้ายเข้าห้องคนเดียว หมายเลขห้องต้องเป็นของห้องคนเดียว
    yield "small-takes-big", build(8, [(1, 1, 2), (1, 1, 3), (1, 4, 5), (1, 1, 4), (2, 5), (1, 6, 3), (2, 1), (2, 6),
                                       (1, 7, 6), (2, 2), (1, 8, 7), (2, 8), (2, 4)])
    # สลับกันว่าห้องไหนย้ายเข้าห้องไหน และถามจากคนที่ไม่ใช่หัวหน้า
    yield "back-and-forth", build(6, [(1, 2, 1), (2, 1), (1, 3, 4), (1, 1, 3), (2, 4), (1, 5, 2), (2, 3), (1, 6, 6), (2, 6)])
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
