"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/03-project-pairs   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้วิธีไล่ทุกคู่ใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1803)


def case(k, values):
    return f"{len(values)} {k}\n" + " ".join(map(str, values))


def cases():
    yield "sample1", case(100, [30, 70, 55, 45, 70, 20])
    # K เป็นเลขคู่ คนที่ได้ครึ่งหนึ่งของ K จับคู่กันเอง
    yield "sample2", case(10, [5, 5, 5, 3, 7])
    yield "single", case(2, [1])
    yield "none", case(1000, [random.randint(501, 1000000) for _ in range(500)])
    # K − x เกิน 1000000 หรือน้อยกว่า 1 ต้องไม่ออกนอกอาเรย์
    yield "out-of-range", case(2000000, [1, 999999, 1000000, 1000000, 2, 1000000])
    yield "smallest-k", case(2, [1, 1, 2, 1, 3])
    # ทุกคนได้ครึ่งหนึ่งของ K คำตอบคือ 2000 × 1999 / 2
    yield "all-half", case(1000000, [500000] * 2000)
    yield "rand1", case(1000, [random.randint(1, 999) for _ in range(3000)])
    yield "rand2", case(150000, [random.randint(1, 149999) for _ in range(10000)])
    # คำตอบ 200000 × 199999 / 2 เกิน int
    yield "big1", case(1000000, [500000] * 200000)
    yield "big2", case(1000000, [random.randint(1, 999999) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
