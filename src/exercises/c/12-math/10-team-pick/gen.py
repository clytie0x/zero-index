"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/10-team-pick   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีคนรวมถึงสองพันคน recursion ที่ไม่จำคำตอบใน naive.c ไม่ทัน
ชุดอื่นมีคนรวมไม่เกิน 22 คน ให้ naive.c ผ่านได้
ชุด big-negative เลือกเฉพาะคำถามที่ C(N + M, K) หลัง mod น้อยกว่า C(N, K) หลัง mod
จับโปรแกรมที่ลืมบวก MOD หลังลบ
"""

import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1210)

MOD = 1000000007


def build(queries):
    assert all(0 <= n <= 1000 and 1 <= m <= 1000 and 1 <= k <= n + m for n, m, k in queries)
    return f"{len(queries)}\n" + "\n".join(f"{n} {m} {k}" for n, m, k in queries)


def random_query(max_boys, max_girls):
    n = random.randint(0, max_boys)
    m = random.randint(1, max_girls)
    return n, m, random.randint(1, n + m)


def negative_query():
    # สุ่มจนได้คำถามที่ผลลบหลัง mod ติดลบ
    while True:
        n, m, k = random_query(1000, 1000)
        if k <= n and math.comb(n + m, k) % MOD < math.comb(n, k) % MOD:
            return n, m, k


def cases():
    yield "sample1", build([(2, 1, 2), (3, 2, 2), (0, 3, 3)])
    yield "sample2", build([(10, 10, 5)])
    yield "girls-only", build([(0, 1, 1), (0, 20, 10), (0, 22, 22)])
    yield "more-than-boys", build([(3, 4, 5), (5, 1, 6), (10, 12, 11)])
    yield "one-girl", build([(21, 1, k) for k in range(1, 23)])
    yield "small-all", build([(n, m, k) for n in range(0, 6) for m in range(1, 6) for k in range(1, n + m + 1)])
    yield "rand1", build([random_query(11, 11) for _ in range(30)])
    yield "big-max", build([(1000, 1000, 1000), (1000, 1000, 2000), (1000, 1000, 1), (1000, 1, 500)])
    yield "big-negative", build([negative_query() for _ in range(1000)])
    yield "big-rand", build([random_query(1000, 1000) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
