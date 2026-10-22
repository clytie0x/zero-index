"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/06-sudoku-six   (รันที่รากของโปรเจกต์)

ตาราง 6 × 6 เล็กพอให้ backtracking ทันทุกชุด ข้อนี้ไม่มีชุด big
ปริศนาสุ่มสร้างจากตารางเต็มที่สุ่มขึ้นมา แล้วลบเลขออกบางช่อง
ชุด bad-row และ bad-box มีเลขที่ให้มาขัดกฎกันเอง จับคนที่ไม่ตรวจเลขตั้งต้น
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2106)


def ok(grid, r, c, d):
    for k in range(6):
        if grid[r][k] == d or grid[k][c] == d:
            return False
    top, left = r // 2 * 2, c // 3 * 3
    for i in range(top, top + 2):
        for j in range(left, left + 3):
            if grid[i][j] == d:
                return False
    return True


def random_full():
    grid = [[0] * 6 for _ in range(6)]

    def fill(pos):
        if pos == 36:
            return True
        r, c = divmod(pos, 6)
        digits = list(range(1, 7))
        random.shuffle(digits)
        for d in digits:
            if ok(grid, r, c, d):
                grid[r][c] = d
                if fill(pos + 1):
                    return True
                grid[r][c] = 0
        return False

    fill(0)
    return grid


def remove(grid, keep):
    cells = random.sample(range(36), 36 - keep)
    out = [row[:] for row in grid]
    for cell in cells:
        out[cell // 6][cell % 6] = 0
    return out


def build(grid):
    return "\n".join(" ".join(map(str, row)) for row in grid)


SAMPLE1 = """0 0 3 0 1 0
5 6 0 3 2 0
0 5 4 2 0 3
2 0 6 4 5 0
0 1 2 0 4 5
0 4 0 1 0 0"""

# เลขที่ให้มาไม่ขัดกัน แต่ช่องแถวบนซ้ายใส่อะไรก็ไม่ได้ เพราะแถวมี 2 ถึง 6 ส่วนคอลัมน์มี 1 อยู่แล้ว
SAMPLE2 = """0 2 3 4 5 6
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0"""


def cases():
    yield "sample1", SAMPLE1
    yield "sample2", SAMPLE2
    yield "empty", build([[0] * 6 for _ in range(6)])
    full = random_full()
    yield "already-full", build(full)
    # แถวแรกมีเลข 4 สองตัว
    yield "bad-row", build([[4, 0, 0, 0, 0, 4]] + [[0] * 6 for _ in range(5)])
    # เลข 5 สองตัวอยู่กล่องเดียวกัน แต่คนละแถวคนละคอลัมน์
    yield "bad-box", build([[5, 0, 0, 0, 0, 0], [0, 0, 5, 0, 0, 0]] + [[0] * 6 for _ in range(4)])
    # ตารางเต็มแต่สลับสองช่องให้ผิด
    broken = [row[:] for row in random_full()]
    broken[3][1], broken[3][4] = broken[3][4], broken[3][1]
    yield "full-wrong", build(broken)
    yield "many-answers", build(remove(random_full(), 8))
    yield "rand1", build(remove(random_full(), 14))
    yield "rand2", build(remove(random_full(), 11))
    yield "rand3", build(remove(random_full(), 18))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
