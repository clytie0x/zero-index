"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/10-watering-plan   (รันที่รากของโปรเจกต์)

ความต้องการน้ำของแต่ละต้นตั้งจากน้ำที่ได้จริงเมื่อรดครบ k0 ครั้งแรก แล้วลดลงเล็กน้อย คำตอบจึงอยู่ไม่เกิน k0
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนต้นและสองแสนครั้ง แต่ละครั้งรดเกือบทั้งแถว
ตั้งใจให้วิธีรดทีละต้นใน naive.cpp ไม่ทัน big2 รดครบแล้วยังไม่พอ ต้องตอบ -1
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1910)


def build(need, rounds):
    rows = [f"{len(need)} {len(rounds)}", " ".join(map(str, need))] + [f"{l} {r} {w}" for l, r, w in rounds]
    return "\n".join(rows)


def final_water(n, rounds):
    diff = [0] * (n + 2)
    for l, r, w in rounds:
        diff[l] += w
        diff[r + 1] -= w
    got, current = [], 0
    for tree in range(1, n + 1):
        current += diff[tree]
        got.append(current)
    return got


def planned(n, rounds, k0, low, high):
    """ความต้องการของแต่ละต้นอยู่ระหว่าง low ถึง high ส่วนของน้ำที่ได้เมื่อรดครบ k0 ครั้งแรก"""
    return [int(g * random.uniform(low, high)) for g in final_water(n, rounds[:k0])]


def random_round(n, top):
    l, r = sorted((random.randint(1, n), random.randint(1, n)))
    return l, r, random.randint(1, top)


def cases():
    yield "sample1", "5 5\n3 5 2 0 4\n1 3 2\n2 5 3\n4 5 1\n1 1 1\n2 4 7"
    yield "zero-need", build([0, 0, 0], [(1, 3, 5), (2, 2, 1)])
    yield "never", build([1, 1, 1, 1], [(1, 2, 9), (3, 3, 9), (1, 3, 9)])
    yield "single", build([10], [(1, 1, 3), (1, 1, 3), (1, 1, 3), (1, 1, 3), (1, 1, 3)])
    # ต้นสุดท้ายได้น้ำพอในการรดครั้งสุดท้ายพอดี
    yield "last-round", build([4, 4, 4, 4], [(1, 4, 2), (1, 3, 2), (4, 4, 1), (2, 4, 1)])
    # ความต้องการและน้ำรวมเกิน int
    yield "over-int", build([6 * 10**10, 3 * 10**9, 9 * 10**10], [(1, 3, 10**9)] * 50 + [(1, 1, 10**9)] * 50 + [(3, 3, 10**9)] * 60)
    rounds = [random_round(20, 5) for _ in range(30)]
    yield "rand1", build(planned(20, rounds, 18, 0.5, 1.0), rounds)
    rounds = [random_round(2000, 10**9) for _ in range(2000)]
    yield "rand2", build(planned(2000, rounds, 1300, 0.8, 1.0), rounds)
    n = 200000
    rounds = [(random.randint(1, 100), random.randint(n - 100, n), random.randint(1, 10**9)) for _ in range(n)]
    yield "big1", build(planned(n, rounds, 150000, 0.95, 1.0), rounds)
    need = [g + 1 if i == n // 2 else g for i, g in enumerate(final_water(n, rounds))]
    yield "big2", build(need, rounds)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
