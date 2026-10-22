"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/05-broken-board   (รันที่รากของโปรเจกต์)

ชุดเล็กมี N ไม่เกิน 9 ให้ naive.cpp ที่ลองทุกการเรียงสับเปลี่ยนตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มี N = 12 ลองทุกการเรียงสับเปลี่ยน 12! แบบไม่ทัน ต้องตัดกิ่ง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2105)


def build(rows):
    return f"{len(rows)}\n" + "\n".join(rows)


def random_board(n, broken_rate):
    return ["".join("#" if random.random() < broken_rate else "." for _ in range(n)) for _ in range(n)]


def cases():
    yield "sample1", build(["....", "....", "....", "...."])
    yield "sample2", build([".....", ".#...", ".....", "...#.", "....."])
    yield "one-good", build(["."])
    yield "one-broken", build(["#"])
    yield "three", build(["...", "...", "..."])
    # ทั้งแถวแตก วางครบ N ตัวไม่ได้
    yield "dead-row", build(["......", "######", "......", "......", "......", "......"])
    yield "eight", build(random_board(8, 0.1))
    yield "nine", build(random_board(9, 0.2))
    yield "nine-free", build(["." * 9] * 9)
    yield "big1", build(["." * 12] * 12)
    yield "big2", build(random_board(12, 0.1))
    # แนวทแยงหลักแตกทั้งเส้น
    yield "big3", build(["".join("#" if i == j else "." for j in range(12)) for i in range(12)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
