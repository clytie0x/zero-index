"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/10-smallest-number   (รันที่รากของโปรเจกต์)

sample1 ทำให้วิธีลบหลักที่มากที่สุด K หลักผิด rising ทำให้วิธีที่ลืมลบจากท้ายผิด
zeros ทำให้วิธีที่ลืมตัดเลข 0 นำหน้าผิด chain ทำให้วิธีที่ลบได้แค่หลักเดียวก่อนใส่หลักใหม่ผิด
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนหลัก ส่วนที่เรียงจากน้อยไปมากยาว วิธีลบทีละหลักใน naive.cpp
ต้องไล่ข้ามส่วนนั้นทุกรอบจึงไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2310)


def build(k, digits):
    assert digits[0] != "0" and 0 <= k < len(digits)
    return f"{len(digits)} {k}\n{digits}"


def random_digits(n, alphabet="0123456789"):
    return random.choice("123456789") + "".join(random.choice(alphabet) for _ in range(n - 1))


def cases():
    yield "sample1", build(3, "1432219")
    yield "sample2", build(1, "10200")
    yield "keep-all", build(0, "907")
    yield "one-left", build(5, "975318")
    yield "rising", build(3, "1234567")
    yield "zeros", build(1, "100000")
    yield "chain", build(4, "56781")
    yield "same", build(2, "55555")
    yield "rand1", build(4, random_digits(12, "0123"))
    yield "rand2", build(900, random_digits(2000))
    rising = "1" + "".join(sorted(random.choice("123456789") for _ in range(149999)))
    yield "big1", build(100000, rising + "".join(random.choice("0123456789") for _ in range(50000)))
    # ไม่มีหลักไหนมากกว่าหลักถัดไปเลย naive ต้องไล่จนสุดทางทุกรอบก่อนลบหลักท้าย
    yield "big2", build(150000, "".join(sorted(random.choice("123456789") for _ in range(200000))))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
