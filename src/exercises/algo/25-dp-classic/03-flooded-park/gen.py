"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/03-flooded-park   (รันที่รากของโปรเจกต์)

naive.cpp เดินทุกเส้นทางด้วย recursion ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีตารางไม่เกิน 13 × 13
ชุดที่ชื่อขึ้นต้นด้วย big มีตาราง 1000 × 1000 ซึ่งมีเส้นทางมากเกินกว่าจะเดินทีละเส้น
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2503)


def build(lines):
    return f"{len(lines)} {len(lines[0])}\n" + "\n".join(lines)


def random_grid(rows, cols, flood_percent):
    lines = []
    for _ in range(rows):
        lines.append("".join("#" if random.randint(1, 100) <= flood_percent else "." for _ in range(cols)))
    return lines


def cases():
    yield "sample1", build(["....", ".#..", "...."])
    yield "sample2", build(["..#", "##.", "..."])
    yield "start-flooded", build(["#..", "...", "..."])
    yield "end-flooded", build(["...", "...", "..#"])
    yield "one-cell", build(["."])
    yield "one-row", build(["." * 13])
    # ท่วมในแถวแรกกับคอลัมน์แรก ช่องที่อยู่หลังจุดท่วมบนขอบไปไม่ถึง
    yield "edge-flood", build(["..#......", ".........", "#........", ".........", "........."])
    yield "full-wall", build(["...#...", "...#...", "...#...", "...#..."])
    yield "rand1", build(random_grid(8, 9, 20))
    yield "rand2", build(random_grid(13, 13, 8))
    yield "big1", build(["." * 1000 for _ in range(1000)])
    big = random_grid(1000, 1000, 4)
    big[0] = "." + big[0][1:]
    big[-1] = big[-1][:-1] + "."
    yield "big2", build(big)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
