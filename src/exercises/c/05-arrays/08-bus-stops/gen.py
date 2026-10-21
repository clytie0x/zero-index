"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/08-bus-stops   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีคำถามแสนข้อที่เกือบทุกข้อถามช่วงยาว ตั้งใจให้วิธีบวกใหม่ทุกคำถามใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(508)


def line(values):
    return " ".join(map(str, values))


def build(n, gaps, queries):
    rows = [f"{n} {len(queries)}", line(gaps)] + [f"{a} {b}" for a, b in queries]
    return "\n".join(rows)


def random_case(n, q, max_gap):
    gaps = [random.randint(1, max_gap) for _ in range(n - 1)]
    queries = [(random.randint(1, n), random.randint(1, n)) for _ in range(q)]
    return build(n, gaps, queries)


def cases():
    yield "sample1", "5 3\n120 300 80 500\n1 5\n4 2\n3 3"
    yield "two-stops", "2 3\n100000\n1 2\n2 1\n2 2"
    yield "same-stop", build(6, [5, 4, 3, 2, 1], [(1, 1), (3, 3), (6, 6)])
    yield "backward", build(6, [5, 4, 3, 2, 1], [(6, 1), (5, 2), (4, 3), (2, 1)])
    # ระยะรวมถึง 99999 × 100000 เกิน int
    n = 100000
    yield "long-road", build(n, [100000] * (n - 1), [(1, n), (n, 1), (1, 2), (50000, 50001), (2, n)])
    yield "rand1", random_case(10, 10, 1000)
    yield "rand2", random_case(1000, 1000, 100000)
    n = q = 100000
    gaps = [random.randint(1, 100000) for _ in range(n - 1)]
    queries = []
    for _ in range(q):
        a, b = random.randint(1, n // 10), random.randint(n - n // 10, n)
        queries.append((a, b) if random.random() < 0.5 else (b, a))
    yield "big1", build(n, gaps, queries)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
