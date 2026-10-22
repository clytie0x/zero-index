"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/29-mst/01-study-groups   (รันที่รากของโปรเจกต์)

naive.cpp เก็บหมายเลขกลุ่มของทุกคน รวมกลุ่มโดยไล่เปลี่ยนหมายเลขทั้งห้อง O(N) ต่อการรวม
ชุดที่ชื่อขึ้นต้นด้วย big มีนักเรียนสองแสนคน big1 จับคู่ต่อกันเป็นสายยาวจนทุกคนอยู่กลุ่มเดียว
จำนวนคู่ราว 2 × 10^10 เกิน int และ naive.cpp ต้องไล่ทั้งห้องเกือบสองแสนครั้ง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2901)


def build(n, pairs):
    return "\n".join([f"{n} {len(pairs)}"] + [f"{a} {b}" for a, b in pairs])


def random_pairs(n, m):
    pairs = []
    while len(pairs) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            pairs.append((a, b))
    return pairs


def cases():
    yield "sample1", "6 5\n1 2\n3 4\n2 3\n1 4\n5 6"
    yield "sample2", "4 3\n1 2\n2 1\n3 4"
    yield "two-students", build(2, [(1, 2), (2, 1)])
    yield "repeat-pair", build(5, [(2, 4), (4, 2), (2, 4), (1, 5), (5, 1)])
    # สองกลุ่มสามคนรวมกัน ต้องอ่านขนาดก่อนรวม ถ้าอ่านหลังรวมจะได้ 6 × 3 แทน 3 × 3
    yield "read-before", build(6, [(1, 2), (2, 3), (4, 5), (5, 6), (3, 4), (6, 1)])
    yield "chain", build(300, [(i, i + 1) for i in range(1, 300)])
    yield "star", build(300, [(1, i) for i in range(2, 301)])
    # สองกลุ่มกลุ่มละร้อยคนรวมกันตอนท้าย
    odd = [(i, i + 2) for i in range(1, 198, 2)]
    even = [(i, i + 2) for i in range(2, 199, 2)]
    yield "two-halves", build(200, odd + even + [(199, 200)])
    yield "rand1", build(12, random_pairs(12, 15))
    yield "rand2", build(2000, random_pairs(2000, 1500))
    yield "big1", build(200000, [(i, i + 1) for i in range(1, 200000)])
    yield "big2", build(200000, random_pairs(200000, 200000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
