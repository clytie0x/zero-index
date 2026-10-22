"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/02-island-count   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big เป็นแผนที่ 1000 × 1000 big1 เป็นเกาะเดียวรูปงูเลื้อยที่มีน้ำล้อมรอบขอบ
big2 เป็นแผ่นดินทั้งแผ่นที่มีน้ำล้อมรอบขอบ big3 สุ่มแผ่นดินราว 58%
big1 กับ big3 ทำให้วิธีกระจายเลขกลุ่มซ้ำจนนิ่งใน naive.cpp ไม่ทัน
big1 กับ big2 ทำให้ recursion ที่ลึกเท่าจำนวนช่องของเกาะพังเพราะ stack เต็ม
sample1 edge-bottom edge-right edge-left มีเกาะที่ช่องแรกที่เจอไม่อยู่บนขอบ แต่มีช่องอื่นแตะแถวล่าง
คอลัมน์ขวา หรือคอลัมน์ซ้าย ดักวิธีที่ดูแค่ช่องแรกของเกาะ และวิธีที่ดูแค่แถวแรกกับคอลัมน์แรก
all-land line thin frame snake ดักวิธีที่นับทุกเกาะโดยไม่สนขอบ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2702)


def text(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(rows)


def full(r, c, ch="#"):
    return [ch * c for _ in range(r)]


def snake(r, c):
    rows = []
    for i in range(r):
        if i % 2 == 0:
            rows.append("#" * c)
        elif i % 4 == 1:
            rows.append("." * (c - 1) + "#")
        else:
            rows.append("#" + "." * (c - 1))
    return rows


def checker(r, c):
    return ["".join("#" if (i + j) % 2 == 0 else "." for j in range(c)) for i in range(r)]


def ring(n):
    rows = []
    for i in range(n):
        rows.append("".join("#" if i in (1, n - 2) or j in (1, n - 2) else "." for j in range(n)))
    rows[n // 2] = rows[n // 2][: n // 2] + "#" + rows[n // 2][n // 2 + 1:]
    return rows


def rand(r, c, p):
    return ["".join("#" if random.random() < p else "." for _ in range(c)) for _ in range(r)]


def framed(rows):
    """ล้อมแผนที่ด้วยน้ำหนึ่งช่องทุกด้าน"""
    c = len(rows[0]) + 2
    return ["." * c] + ["." + row + "." for row in rows] + ["." * c]


def frame(r, c, p):
    """ขอบนอกเป็นแผ่นดินทั้งหมด ถัดเข้าไปหนึ่งช่องเป็นน้ำ ข้างในสุ่ม"""
    inner = framed(rand(r - 4, c - 4, p))
    return ["#" * c] + ["#" + row + "#" for row in inner] + ["#" * c]


def cases():
    yield "sample1", "\n".join(["6 10", "..........", ".##...#...", ".#..####..", "....#...##", ".##.....##", ".##..#.###"])
    yield "sample2", "\n".join(["5 5", ".....", ".###.", ".#.#.", ".###.", "....."])
    yield "one-land", "1 1\n#"
    yield "one-water", "1 1\n."
    yield "all-water", "3 4\n....\n....\n...."
    yield "edge-bottom", "\n".join(["5 7", ".......", ".#...#.", "..#..#.", ".###.#.", "..#..##"])
    yield "edge-right", "\n".join(["5 7", ".......", ".#..##.", ".#...##", ".#...#.", "......."])
    yield "edge-left", "\n".join(["6 6", "......", "..##..", ".##...", "##..#.", "....#.", "......"])
    yield "all-land", text(full(30, 40))
    yield "checker", text(checker(40, 40))
    yield "snake", text(snake(51, 51))
    yield "snake-inside", text(framed(snake(49, 49)))
    yield "ring", text(ring(25))
    yield "line", text(["#" * 1000])
    yield "thin", text(rand(2, 300, 0.5))
    yield "frame", text(frame(42, 60, 0.45))
    yield "rand1", text(rand(10, 15, 0.5))
    yield "rand2", text(rand(200, 200, 0.55))
    yield "big1", text(framed(snake(998, 998)))
    yield "big2", text(framed(full(998, 998)))
    yield "big3", text(rand(1000, 1000, 0.58))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
