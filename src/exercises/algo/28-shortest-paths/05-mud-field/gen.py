"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/05-mud-field   (รันที่รากของโปรเจกต์)

naive.cpp คือ Dijkstra แบบอาเรย์บนทุกช่อง O((RC)^2) ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีราว 500 x 500 ช่อง ตั้งใจให้แบบอาเรย์ไม่ทัน
detour ต้องก้าวขึ้นด้วย snake กับ big2 เป็นทางคดเคี้ยวที่ต้องเดินไปทางซ้ายด้วย คำตอบเกิน int
walled-in กับ big3 ไปไม่ถึงช่องขวาล่าง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2805)


def build(grid):
    rows = [f"{len(grid)} {len(grid[0])}"] + [" ".join(map(str, row)) for row in grid]
    return "\n".join(rows)


def random_grid(r, c, low, high, wall_rate):
    grid = [[random.randint(low, high) for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if random.random() < wall_rate:
                grid[i][j] = -1
    grid[0][0] = random.randint(low, high)
    grid[r - 1][c - 1] = random.randint(low, high)
    return grid


def snake(r, c, low, high):
    """แถวคู่เปิดโล่ง แถวคี่เป็นบ่อน้ำเกือบทั้งแถว เว้นช่องเดียวสลับซ้ายขวา ทางจึงคดไปมา"""
    grid = [[random.randint(low, high) for _ in range(c)] for _ in range(r)]
    for i in range(1, r, 2):
        gap = c - 1 if (i // 2) % 2 == 0 else 0
        for j in range(c):
            if j != gap:
                grid[i][j] = -1
    return grid


def cases():
    yield "sample1", "4 6\n1 3 9 1 1 2\n1 -1 9 -1 9 1\n1 1 2 1 1 -1\n9 -1 1 1 1 1"
    yield "sample2", "3 3\n1 1 -1\n1 -1 1\n-1 1 1"
    yield "single", "1 1\n7"
    yield "start-pond", "2 2\n-1 1\n1 1"
    # ทางที่ก้าวน้อยที่สุดผ่านโคลนลึก ทางอ้อมรอบใหญ่ถูกกว่า
    yield "detour", build([[1, 1000000000, 1, 1, 1], [1, 1000000000, 1, -1, 1], [1, 1, 1, -1, 1], [-1, -1, -1, -1, 1]])
    # ไปได้ทางเดียวผ่านโคลนลึกทุกช่อง รวมเกิน int
    yield "over-int", build([[10**9, 10**9, 10**9], [-1, -1, 10**9]])
    grid = random_grid(6, 7, 1, 9, 0.2)
    for j in range(7):
        grid[3][j] = -1
    yield "walled-in", build(grid)
    yield "snake", build(snake(9, 8, 10**8, 10**9))
    yield "rand1", build(random_grid(10, 12, 1, 20, 0.25))
    yield "rand2", build(random_grid(40, 50, 1, 10**9, 0.15))
    yield "big1", build(random_grid(500, 500, 1, 10**9, 0.2))
    yield "big2", build(snake(499, 500, 10**6, 10**9))
    grid = random_grid(500, 500, 1, 10**9, 0.1)
    for i in range(495, 500):
        for j in range(495, 500):
            if i == 495 or j == 495:
                grid[i][j] = -1
    yield "big3", build(grid)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
