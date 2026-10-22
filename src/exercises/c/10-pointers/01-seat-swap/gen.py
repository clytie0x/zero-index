"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/01-seat-swap   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1001)


def line(values):
    return " ".join(map(str, values))


def make(ids, swaps):
    lines = [f"{len(ids)} {len(swaps)}", line(ids)]
    lines += [f"{a} {b}" for a, b in swaps]
    return "\n".join(lines)


def ids(n):
    return random.sample(range(1, 1000000001), n)


def rand_swaps(n, q):
    return [(random.randint(1, n), random.randint(1, n)) for _ in range(q)]


def cases():
    yield "sample1", make([6701, 6702, 6703, 6704, 6705], [(1, 4), (2, 5), (4, 5)])
    yield "sample2", make([31, 27, 45], [(2, 2), (3, 1)])
    yield "single", make([1000000000], [(1, 1), (1, 1)])
    # สลับกับตัวเองทุกครั้ง ผลต้องเหมือนเดิม จับวิธีสลับที่พังเมื่อ a เท่ากับ b
    yield "same-seat", make([5, 9, 2, 7], [(1, 1), (2, 2), (3, 3), (4, 4), (2, 2)])
    # สลับคู่เดิมสองรอบ ต้องกลับที่เดิม
    yield "swap-back", make([11, 22, 33, 44, 55, 66], [(2, 6), (6, 2), (1, 3), (3, 1)])
    # ที่นั่งแรกกับที่นั่งสุดท้าย จับการนับ index ผิดไปหนึ่ง
    yield "ends", make([8, 6, 4, 2, 1, 3, 5, 7], [(1, 8), (8, 1), (1, 8)])
    n = 30
    yield "rand1", make(ids(n), rand_swaps(n, 50))
    n = 1000
    yield "rand2", make(ids(n), rand_swaps(n, 2000))
    n = 100000
    yield "big-large", make(random.sample(range(1, 200001), n), rand_swaps(n, 30000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
