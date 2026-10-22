"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/04-maze-checkpoint   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big เป็นแผนที่ 1000 × 1000 big1 เป็นทางงูเลื้อยยาวราวห้าแสนก้าวต่อขา
big2 โล่งทั้งแผ่น big3 สุ่มกำแพงราว 30% ตั้งใจให้วิธีจำลองทีละนาทีใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2704)


def text(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join("".join(r) for r in rows)


def blank(r, c, ch="."):
    return [[ch] * c for _ in range(r)]


def snake(r, c):
    rows = []
    for i in range(r):
        if i % 2 == 0:
            rows.append(["."] * c)
        elif i % 4 == 1:
            rows.append(["#"] * (c - 1) + ["."])
        else:
            rows.append(["."] + ["#"] * (c - 1))
    return rows


def put(rows, marks):
    for ch, (r, c) in marks.items():
        rows[r][c] = ch
    return rows


def random_maze(r, c, wall):
    rows = [["#" if random.random() < wall else "." for _ in range(c)] for _ in range(r)]
    cells = random.sample([(i, j) for i in range(r) for j in range(c)], 3)
    return put(rows, dict(zip("SPE", cells)))


def cases():
    yield "sample1", "6 8\nS..#....\n.#.#.##.\n.#...#..\n.####.#.\n...E#.#P\n.#......"
    yield "sample2", "3 5\nS.#P#\n..###\n...E."
    yield "tiny", "1 3\nSPE"
    yield "pass-e", "1 5\nS.E.P"
    yield "same-way", "3 3\nE.S\n.#.\n..P"
    yield "p-closed", "4 6\nS....#\n.###.#\n.#P#.#\n.#.#.E"
    yield "e-closed", "2 5\nS.P#E\n...#."
    yield "open", text(put(blank(50, 50), {"S": (0, 0), "P": (49, 49), "E": (0, 49)}))
    yield "snake", text(put(snake(51, 51), {"S": (0, 0), "P": (50, 50), "E": (0, 50)}))
    yield "rand1", text(random_maze(10, 12, 0.25))
    yield "rand2", text(random_maze(100, 100, 0.3))
    yield "big1", text(put(snake(1000, 1000), {"S": (0, 0), "P": (998, 0), "E": (0, 999)}))
    yield "big2", text(put(blank(1000, 1000), {"S": (0, 0), "P": (999, 999), "E": (999, 0)}))
    yield "big3", text(random_maze(1000, 1000, 0.3))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
