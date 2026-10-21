"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/07-duplicate-ticket   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน และบัตรใบแรกที่ซ้ำคือใบสุดท้าย ตั้งใจให้วิธีเทียบทุกคู่ใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(507)


def line(values):
    return " ".join(map(str, values))


def cases():
    yield "sample1", "7\n5 3 8 3 5 9 8"
    yield "sample2", "4\n10 20 30 40"
    yield "single", "1\n1000000"
    yield "adjacent", "3\n7 7 7"
    # เลขที่ขอบ 1 กับ 1000000 จับอาเรย์ seen ที่ขาดไปหนึ่งช่อง
    yield "extremes", "4\n1 1000000 1000000 1"
    yield "last", "6\n2 4 6 8 10 4"
    yield "rand1", f"1000\n{line(random.randint(1, 1000000) for _ in range(1000))}"
    yield "rand2", f"2000\n{line(random.randint(1, 3000) for _ in range(2000))}"
    tickets = random.sample(range(1, 1000001), 199999)
    yield "big1", f"200000\n{line(tickets + [tickets[0]])}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
