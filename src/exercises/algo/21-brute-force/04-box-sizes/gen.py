"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/04-box-sizes   (รันที่รากของโปรเจกต์)

ชุดเล็กมี V ไม่เกิน 10^6 ให้ naive.cpp ที่วน a ถึง V และวน b จน a × b เกิน V ตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มี V ระดับ 10^9 ถึง 10^10 naive ต้องวนราว 10^10 รอบขึ้นไป ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2104)


def cases():
    yield "sample1", "12"
    yield "sample2", "7"
    yield "min", "1"
    # ลูกบาศก์พอดี ลูปที่ใช้ a * a * a < V จะหลุดขนาด 100 × 100 × 100
    yield "cube", "1000000"
    # ตัวหารเยอะ จับคนที่ลืม a ≤ b ≤ c แล้วนับขนาดเดียวกันซ้ำหลายลำดับ
    yield "many-divisors", "720720"
    # จำนวนเฉพาะกำลังสอง มีแค่ 1 × 1 × p² กับ 1 × p × p
    yield "prime-square", "994009"
    yield "rand1", str(random.randint(1000, 100000))
    yield "rand2", str(random.randint(100000, 1000000))
    # ใหญ่ที่สุด และเป็นลูกบาศก์พอดีใกล้ 10^10
    yield "big1", "10000000000"
    yield "big2", str(2154 ** 3)
    # จำนวนเฉพาะ มีขนาดเดียวคือ 1 × 1 × V พื้นที่ผิวราว 4 × 10^10
    yield "big3", "9999999967"
    # V ยังอยู่ใน int แต่พื้นที่ผิว 4V + 2 เกิน int จับคนที่เก็บพื้นที่ผิวเป็น int
    yield "big-prime-int", "1999999973"
    # ตัวหารเยอะที่สุดช่วงนี้
    yield "big4", "6983776800"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
