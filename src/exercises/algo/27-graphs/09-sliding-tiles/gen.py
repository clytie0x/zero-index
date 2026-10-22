"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/09-sliding-tiles   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big big1 มีหนึ่งแสนกระดานสุ่ม ราวครึ่งหนึ่งไปถึงเป้าหมายไม่ได้
big2 มีสองพันกระดานที่ต้องใช้ 28 ถึง 31 ครั้ง ตั้งใจให้วิธี BFS ใหม่ทุกกระดานใน naive.cpp ไม่ทัน
ข้อนี้เป็นกราฟของสถานะที่มีขนาดตายตัว จึงไม่มีชุดเส้นตรงยาวแบบข้ออื่น
"""

import random
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2709)
GOAL = "123456780"


def all_moves():
    """BFS จากเป้าหมาย ใช้เลือกกระดานตามจำนวนครั้ง"""
    dist = {GOAL: 0}
    queue = deque([GOAL])
    while queue:
        board = queue.popleft()
        b = board.index("0")
        r, c = divmod(b, 3)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                cells = list(board)
                cells[b], cells[nr * 3 + nc] = cells[nr * 3 + nc], cells[b]
                nxt = "".join(cells)
                if nxt not in dist:
                    dist[nxt] = dist[board] + 1
                    queue.append(nxt)
    return dist


DIST = all_moves()
BY_MOVES = {}
for board in sorted(DIST):
    BY_MOVES.setdefault(DIST[board], []).append(board)


def shuffled():
    cells = list(GOAL)
    random.shuffle(cells)
    return "".join(cells)


def text(boards):
    return f"{len(boards)}\n" + "\n".join(boards)


def cases():
    yield "sample1", text(["123456780", "123450786", "120453786", "213456780"])
    yield "sample2", text(["123406758", "012453786"])
    yield "solved", text([GOAL])
    yield "one-move", text(BY_MOVES[1])
    yield "parity", text(["213456780", "123456870", "876543210"])
    yield "hardest", text(BY_MOVES[31])
    yield "few-moves", text([random.choice(BY_MOVES[k]) for k in range(2, 12)])
    yield "mixed", text([random.choice(BY_MOVES[random.randint(12, 26)]) for _ in range(6)] + ["123456708", "203156478"])
    yield "big1", text([shuffled() for _ in range(100000)])
    far = BY_MOVES[28] + BY_MOVES[29] + BY_MOVES[30] + BY_MOVES[31]
    yield "big2", text([random.choice(far) for _ in range(2000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
