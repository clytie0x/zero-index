"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/09-best-stretch   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน และ K ครึ่งหนึ่งของ N ตั้งใจให้วิธีบวกใหม่ทุกช่วงใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(509)


def line(values):
    return " ".join(map(str, values))


def profits(n, low, high):
    return [random.randint(low, high) for _ in range(n)]


def cases():
    yield "sample1", "7 3\n500 -200 800 300 -100 900 -400"
    yield "single", "1 1\n-5"
    yield "k-one", "6 1\n3 9 -2 9 4 1"
    yield "k-all", f"5 5\n{line([-100000, 100000, -1, 0, 7])}"
    # ขาดทุนทุกช่วง จับคนที่เริ่มค่ามากสุดที่ 0
    yield "all-loss", "6 2\n-500 -300 -900 -100 -200 -800"
    # ทุกช่วงเท่ากัน ต้องตอบวันที่ 1
    yield "all-equal", "8 3\n250 250 250 250 250 250 250 250"
    # ผลรวม 30000 × 100000 = 3 × 10^9 เกิน int
    yield "over-int", f"30000 30000\n{line([100000] * 30000)}"
    yield "rand1", f"30 7\n{line(profits(30, -1000, 1000))}"
    yield "rand2", f"2000 300\n{line(profits(2000, -100000, 100000))}"
    yield "big1", f"200000 100000\n{line(profits(200000, -100000, 100000))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
