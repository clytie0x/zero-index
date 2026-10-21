"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/07-vegetable-plots

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(707)


def make(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(rows)


def rand_garden(r, c, tries, max_side):
    """วางแปลงสี่เหลี่ยมแบบสุ่ม แปลงใหม่ต้องไม่ทับและไม่มีด้านติดกับแปลงเดิม แตะกันที่มุมได้"""
    g = [["."] * c for _ in range(r)]
    for _ in range(tries):
        h, w = random.randint(1, max_side), random.randint(1, max_side)
        top, left = random.randint(0, r - h), random.randint(0, c - w)
        ok = True
        for i in range(top, top + h):
            for j in range(left, left + w):
                for di, dj in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and g[ni][nj] == "#":
                        ok = False
        if ok:
            for i in range(top, top + h):
                for j in range(left, left + w):
                    g[i][j] = "#"
    return make(["".join(row) for row in g])


def cases():
    yield "sample1", make(["##..#.", "##..#.", "......", ".###.#", ".###.."])
    # แปลงแตะกันที่มุม นับแยกกัน
    yield "sample2", make(["##...", "##...", "..###", "#.###"])
    yield "empty", make(["....", "...."])
    yield "one-plot", make(["#"])
    yield "full", make(["#" * 8 for _ in range(5)])
    yield "diagonal", make(["".join("#" if (i + j) % 2 == 0 else "." for j in range(7)) for i in range(5)])
    yield "one-row", make(["##.#.###.#"])
    # แปลงใหญ่สุดอยู่มุมล่างขวา จับโปรแกรมที่เดินไม่ถึงขอบ
    yield "corner", make(["#.....", "......", "...###", "...###"])
    yield "max", rand_garden(100, 100, 3000, 12)
    for i in range(1, 3):
        yield f"rand{i}", rand_garden(random.randint(20, 60), random.randint(20, 60), 400, 8)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
