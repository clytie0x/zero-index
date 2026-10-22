"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/07-rice-piles   (รันที่รากของโปรเจกต์)

equal-four กับ in-line ทำให้วิธีเรียงครั้งเดียวแล้วรวมเรียงแถวผิด over-int ทำให้วิธีที่ใช้ int ผิด
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนกอง วิธีไล่หาสองกองที่เบาที่สุดทุกรอบใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2307)


def build(weights):
    return f"{len(weights)}\n" + " ".join(map(str, weights))


def cases():
    yield "sample1", build([40, 10, 30, 20])
    yield "sample2", build([500])
    yield "two", build([1000000000, 1000000000])
    yield "equal-four", build([5, 5, 5, 5])
    yield "in-line", build([30, 20, 50, 40, 60, 10, 10])
    yield "one-heavy", build([1, 1, 1, 1, 1000])
    yield "over-int", build([10**9 - random.randint(0, 1000) for _ in range(50)])
    yield "rand1", build([random.randint(1, 100) for _ in range(15)])
    yield "rand2", build([random.randint(1, 10**9) for _ in range(3000)])
    yield "big1", build([random.randint(1, 10**9) for _ in range(200000)])
    yield "big2", build([random.randint(1, 1000) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
