"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/10-fallen-trees   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big เป็นแผนที่ราว 1000 × 1000 big1 เป็นทางงูเลื้อยยาวเกือบห้าแสนช่องที่มีต้นไม้ล้มทุกช่อง
big2 เป็นทางงูเลื้อยแบบเดียวกันที่มีต้นไม้ล้มทุกสองช่อง สองชุดนี้ตั้งใจให้วิธีไล่ทีละจำนวนต้นที่ตัด
แล้วสแกนทั้งแผนที่ใน naive.cpp ไม่ทัน big3 สุ่มต้นไม้ หิน และทางโล่ง ใช้ตรวจความถูกต้องกับแผนที่ใหญ่
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2710)


def text(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join("".join(r) for r in rows)


def fill(r, c, ch):
    return [[ch] * c for _ in range(r)]


def put(rows, marks):
    for ch, (r, c) in marks.items():
        rows[r][c] = ch
    return rows


def snake(r, c, every=2):
    """ทางงูเลื้อยกว้างหนึ่งช่อง กั้นด้วยหิน บนทางมีต้นไม้ล้มทุก every ช่อง"""
    rows = []
    for i in range(r):
        if i % 2 == 0:
            rows.append(["T" if j % every == every - 1 else "." for j in range(c)])
        elif i % 4 == 1:
            rows.append(["#"] * (c - 1) + ["."])
        else:
            rows.append(["."] + ["#"] * (c - 1))
    return rows


def rand(r, c, trees, rocks):
    rows = []
    for _ in range(r):
        row = []
        for _ in range(c):
            x = random.random()
            row.append("T" if x < trees else "#" if x < trees + rocks else ".")
        rows.append(row)
    a, b = random.sample([(i, j) for i in range(r) for j in range(c)], 2)
    return put(rows, {"S": a, "E": b})


def cases():
    yield "sample1", "5 7\nS.T....\n##T.##.\n..T.#T.\n.##.#TT\n...T#.E"
    yield "sample2", "3 4\nS.#.\nTT#E\n..#."
    yield "no-trees", text(put(fill(20, 30, "."), {"S": (0, 0), "E": (19, 29)}))
    yield "next-door", "1 2\nSE"
    yield "all-trees", text(put(fill(30, 30, "T"), {"S": (0, 0), "E": (29, 29)}))
    yield "tree-line", text(put(fill(1, 50, "T"), {"S": (0, 0), "E": (0, 49)}))
    yield "detour", "5 9\nS...T...E\n.#######.\n.........\nTTTTTTTTT\n........."
    yield "snake", text(put(snake(41, 41), {"S": (0, 0), "E": (40, 40)}))
    yield "rand1", text(rand(8, 10, 0.35, 0.2))
    yield "rand2", text(rand(100, 100, 0.4, 0.25))
    yield "big1", text(put(snake(999, 1000, 1), {"S": (0, 0), "E": (998, 999)}))
    yield "big2", text(put(snake(999, 1000), {"S": (0, 0), "E": (998, 999)}))
    yield "big3", text(rand(1000, 1000, 0.45, 0.2))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
