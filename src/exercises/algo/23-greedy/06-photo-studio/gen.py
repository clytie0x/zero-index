"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/06-photo-studio   (รันที่รากของโปรเจกต์)

ทุกชุดให้เวลาถ่ายมาไม่เรียง วิธีที่ไม่สนจำนวนช่าง หรือแจกคิววนตามลำดับที่มาจะผิด
over-int มีผลรวมเกิน int ซึ่ง naive ยังรันทัน
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนคน วิธีไล่หาคนที่ใช้เวลาน้อยสุดทีละคนใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2306)


def build(k, minutes):
    return f"{len(minutes)} {k}\n" + " ".join(map(str, minutes))


def cases():
    yield "sample1", build(2, [5, 2, 8, 3, 4])
    yield "sample2", build(1, [7, 3, 1, 5])
    yield "one-person", build(1, [1000000])
    yield "k-equals-n", build(4, [9, 1, 7, 3])
    yield "same-time", build(3, [10] * 10)
    yield "uneven", build(2, [1, 1, 1, 1, 100, 100])
    yield "rand1", build(3, [random.randint(1, 20) for _ in range(12)])
    yield "rand2", build(37, [random.randint(1, 10**6) for _ in range(2000)])
    yield "over-int", build(1, [random.randint(900000, 10**6) for _ in range(2000)])
    yield "big1", build(1000, [random.randint(1, 10**6) for _ in range(200000)])
    yield "big2", build(1, [random.randint(1, 10**6) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
