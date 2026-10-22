"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/04-paper-fold   (รันที่รากของโปรเจกต์)

naive.cpp สร้างลายทั้งเส้นจริงๆ ยาว 2^k - 1 ตัว ใช้ได้ถึงราว k = 25
ชุดที่ชื่อขึ้นต้นด้วย big ใช้ k = 60 ลายยาวราว 10^18 ตัว สร้างทั้งเส้นไม่ได้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2204)


def build(k, positions):
    return f"{k} {len(positions)}\n" + "\n".join(map(str, positions))


def edges(k):
    last = 2**k - 1
    near = [1, 2, 3, last - 2, last - 1, last, 2 ** (k - 1) - 1, 2 ** (k - 1), 2 ** (k - 1) + 1]
    for b in range(1, k):
        near += [2**b - 1, 2**b, 2**b + 1]
    return sorted(set(p for p in near if 1 <= p <= last))


def cases():
    yield "sample1", build(3, list(range(1, 8)))
    yield "sample2", "2 4\n3\n1\n2\n3"
    yield "k-one", build(1, [1])
    yield "all-k10", build(10, list(range(1, 2**10)))
    yield "edges-k20", build(20, edges(20))
    yield "rand1", build(20, [random.randint(1, 2**20 - 1) for _ in range(1000)])
    yield "rand2", build(23, [random.randint(1, 2**23 - 1) for _ in range(1000)])
    yield "big1", build(60, [random.randint(1, 2**60 - 1) for _ in range(100000)])
    yield "big2", build(60, edges(60))
    yield "big3", build(45, [random.randint(1, 2**45 - 1) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
