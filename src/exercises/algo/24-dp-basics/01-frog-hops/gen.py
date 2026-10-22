"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/01-frog-hops   (รันที่รากของโปรเจกต์)

naive.cpp เติมตารางใหม่ทุกคำถาม ถูกแต่ใช้เวลา Q × N
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนคำถาม N ถึงล้าน ซึ่ง naive.cpp ไม่ทัน และคำตอบจริงเกิน 1000000007 มาก
far-last มีคำถามที่ไกลที่สุดอยู่ท้ายสุด วิธีที่สร้างตารางตามขนาดของคำถามแรกจะอ่านเกินตาราง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2401)


def build(queries):
    return f"{len(queries)}\n" + " ".join(map(str, queries))


def cases():
    yield "sample1", build([4, 6, 1])
    yield "sample2", build([3, 3])
    yield "one", build([1])
    yield "small-all", build(list(range(1, 31)))
    yield "far-last", build([5, 2, 40, 7, 1000])
    yield "rand1", build([random.randint(1, 30) for _ in range(20)])
    yield "rand2", build([random.randint(1, 1000000) for _ in range(50)])
    yield "max-once", build([1000000])
    yield "big1", build([random.randint(900000, 1000000) for _ in range(100000)])
    yield "big2", build([1000000] * 100000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
