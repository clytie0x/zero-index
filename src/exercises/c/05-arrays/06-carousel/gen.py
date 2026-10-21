"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/06-carousel   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี K ใหญ่ ตั้งใจให้วิธีหมุนทีละครั้งใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(506)


def line(values):
    return " ".join(map(str, values))


def horses(n):
    return random.sample(range(1, 1000001), n)


def cases():
    yield "sample1", "5 2\n1 2 3 4 5"
    yield "sample2", "4 8\n7 3 9 1"
    yield "single", "1 7\n42"
    yield "no-turn", "6 0\n6 5 4 3 2 1"
    yield "one-less", "6 5\n10 20 30 40 50 60"
    yield "rand1", f"20 37\n{line(horses(20))}"
    yield "rand2", f"500 999\n{line(horses(500))}"
    yield "big1", f"1000 999999999\n{line(horses(1000))}"
    yield "big2", f"100000 123456789\n{line(horses(100000))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
