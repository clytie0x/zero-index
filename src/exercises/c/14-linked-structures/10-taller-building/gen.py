"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/10-taller-building   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีตึกห้าแสนหลังที่วิธีไล่หาไปทางขวาต้องเดินไกล ตั้งใจให้ naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1410)


def build(heights):
    return f"{len(heights)}\n{' '.join(map(str, heights))}"


def cases():
    yield "sample1", build([3, 7, 4, 4, 9, 2, 8])
    yield "sample2", build([5, 5, 5])
    yield "single", build([1000000000])
    yield "increasing", build(list(range(1, 11)))
    yield "decreasing", build(list(range(10, 0, -1)))
    # สูงเท่ากันไม่นับ ต้องสูงกว่าจริงๆ
    yield "ties", build([2, 2, 3, 3, 1, 3, 4, 4])
    yield "valley", build([9, 1, 2, 3, 4, 5, 6, 7, 8, 10])
    yield "rand1", build([random.randint(1, 10) for _ in range(15)])
    yield "rand2", build([random.randint(1, 10**9) for _ in range(5000)])
    yield "rand3", build([random.randint(1, 100) for _ in range(20000)])
    n = 300000
    # สูงไปเตี้ย ไม่มีใครมีคำตอบ วิธีไล่หาต้องเดินจนสุดถนนทุกหลัง
    yield "big1", build(list(range(10**9, 10**9 - n, -1)))
    # สูงเท่ากันทั้งถนน ห้าแสนหลังเท่าขอบเขต
    yield "big2", build([777] * 500000)
    # สูงไปเตี้ยแล้วมีตึกสูงที่สุดอยู่ท้ายถนน ทุกหลังมีคำตอบเป็นหลังสุดท้าย
    yield "big3", build(list(range(n - 1 + 5, 5, -1)) + [10**9])
    yield "big4", build([random.randint(1, 10**9) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
