"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/06-pass-the-ball   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี K ใหญ่ ตั้งใจให้ naive.c ที่ส่งลูกบอลครบ K - 1 ครั้งจริงไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1406)


def cases():
    yield "sample1", "5 2"
    yield "sample2", "7 3"
    yield "k-one", "6 1"
    yield "one-child", "1 7"
    yield "k-equals-n", "8 8"
    yield "k-more-than-n", "4 10"
    yield "two-children", "2 5"
    yield "rand1", f"{random.randint(10, 30)} {random.randint(2, 40)}"
    yield "rand2", f"{random.randint(500, 1000)} {random.randint(100, 1000)}"
    yield "max-n", f"5000 {random.randint(2, 50)}"
    yield "big1", "5000 1000000000"
    yield "big2", f"4999 {random.randint(900000000, 1000000000)}"
    yield "big-one-child", "1 1000000000"
    yield "big3", f"{random.randint(3000, 5000)} {random.randint(10**7, 10**8)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
