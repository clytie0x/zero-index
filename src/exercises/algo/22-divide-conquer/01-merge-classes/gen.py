"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/22-divide-conquer/01-merge-classes   (รันที่รากของโปรเจกต์)

ข้อนี้ไม่มี naive เพราะต่อสองห้องแล้ว sort ก็ทันเวลา ชุด big1 ใหญ่เกิน 300 KB จึงตั้งชื่อขึ้นต้นด้วย big
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2201)

TOP = 10**9


def build(room_a, room_b):
    return f"{len(room_a)} {len(room_b)}\n" + " ".join(map(str, room_a)) + "\n" + " ".join(map(str, room_b))


def sorted_scores(count, top):
    return sorted(random.randint(0, top) for _ in range(count))


def cases():
    yield "sample1", "4 5\n35 52 70 88\n40 41 66 90 95"
    yield "sample2", "3 2\n10 20 30\n40 50"
    yield "single", build([7], [7])
    # ห้อง A มากกว่าทุกคนในห้อง B ต้องหยิบจากห้อง B จนหมดก่อน แล้วค่อยเทห้อง A ที่เหลือ
    yield "a-after-b", build([60, 70, 80, 90], [5, 15, 25])
    yield "all-equal", build([50] * 5, [50] * 6)
    yield "edge-values", build([0, 0, TOP], [0, TOP, TOP, TOP])
    yield "many-ties", build(sorted_scores(300, 5), sorted_scores(200, 5))
    yield "rand1", build(sorted_scores(1000, TOP), sorted_scores(1500, TOP))
    yield "rand2", build(sorted_scores(1, TOP), sorted_scores(2000, TOP))
    yield "big1", build(sorted_scores(200000, TOP), sorted_scores(200000, TOP))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
