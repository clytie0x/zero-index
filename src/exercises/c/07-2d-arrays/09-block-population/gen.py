"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/09-block-population

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
ชุดที่ชื่อขึ้นต้นด้วย big ตั้งใจให้ naive.c ที่บวกทีละช่องไม่ทันเวลา
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(709)
MAX_VALUE = 10000


def make(grid, queries):
    lines = [f"{len(grid)} {len(grid[0])}"]
    lines += [" ".join(str(x) for x in row) for row in grid]
    lines.append(str(len(queries)))
    lines += [f"{a} {b} {c} {d}" for a, b, c, d in queries]
    return "\n".join(lines)


def rand_grid(r, c, high=MAX_VALUE):
    return [[random.randint(0, high) for _ in range(c)] for _ in range(r)]


def rand_query(r, c):
    r1, r2 = sorted((random.randint(1, r), random.randint(1, r)))
    c1, c2 = sorted((random.randint(1, c), random.randint(1, c)))
    return (r1, c1, r2, c2)


def large_query(r, c):
    """สี่เหลี่ยมใหญ่ มุมบนซ้ายอยู่ในสิบส่วนแรก มุมล่างขวาอยู่ในสิบส่วนสุดท้าย"""
    return (random.randint(1, r // 10), random.randint(1, c // 10),
            random.randint(r - r // 10 + 1, r), random.randint(c - c // 10 + 1, c))


def cases():
    yield "sample1", make([[4, 0, 6, 2, 5], [1, 8, 3, 7, 0], [9, 2, 5, 1, 3], [0, 4, 7, 6, 2]],
                          [(2, 2, 3, 4), (1, 1, 4, 5), (4, 1, 4, 5)])
    yield "sample2", make([[3, 1], [4, 1], [5, 9]], [(3, 2, 3, 2), (1, 1, 1, 1), (2, 1, 3, 2)])
    yield "one-block", make([[MAX_VALUE]], [(1, 1, 1, 1)] * 3)
    g = rand_grid(1, 300)
    yield "one-row", make(g, [rand_query(1, 300) for _ in range(200)])
    g = rand_grid(300, 1)
    yield "one-column", make(g, [rand_query(300, 1) for _ in range(200)])
    # สี่เหลี่ยมไม่แตะขอบบนหรือขอบซ้ายเลย จับโปรแกรมที่ลืมบวกมุมคืน
    g = rand_grid(40, 40)
    yield "middle", make(g, [(random.randint(2, 20), random.randint(2, 20), random.randint(21, 40), random.randint(21, 40))
                             for _ in range(300)])
    for i in range(1, 3):
        r, c = random.randint(20, 80), random.randint(20, 80)
        yield f"rand{i}", make(rand_grid(r, c), [rand_query(r, c) for _ in range(500)])
    yield "big1", make(rand_grid(500, 500), [large_query(500, 500) for _ in range(50000)])
    # ทุกบล็อกมี 10000 คน ผลรวมทั้งเมือง 2.5 x 10^9 เกิน int
    yield "big2", make([[MAX_VALUE] * 500 for _ in range(500)],
                       [(1, 1, 500, 500)] + [large_query(500, 500) for _ in range(49999)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
