"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/07-fabric-pattern   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big ยาวล้านตัวอักษร
big1 เป็น a เกือบล้านตัวแล้วจบด้วย b ทุกความยาวที่ลองต้องเทียบเกือบถึงท้ายก่อนจะพบว่าไม่ได้
ตั้งใจให้วิธีลองทีละความยาวใน naive.cpp ไม่ทัน
big2 แม่แบบยาวเจ็ดแสนกว่าตัวที่ส่วนต้นแทบจะซ้ำตัวเอง big3 แม่แบบสั้นซ้ำทั้งผืน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3007)


def random_text(n, letters):
    return "".join(random.choice(letters) for _ in range(n))


def woven(block, n):
    return (block * (n // len(block) + 1))[:n]


def cases():
    yield "sample1", "abcabcab"
    yield "sample2", "abcd"
    yield "one", "z"
    yield "same-letter", "kkkkkkk"
    # จบกลางแม่แบบ และแม่แบบที่มีส่วนต้นซ้ำกับส่วนท้ายของตัวเอง
    yield "half-block", "abaababaab"
    yield "not-divisor", woven("aabaa", 13)
    yield "almost", "a" * 30 + "b"
    yield "ends-like-start", "abcxyzab"
    yield "rand1", woven(random_text(7, "ab"), 50)
    yield "rand2", random_text(3000, "ab")
    yield "rand3", woven(random_text(400, "abc"), 5000)
    n = 1000000
    yield "big1", "a" * (n - 1) + "b"
    block = "a" * 350000 + "b" + "a" * 400000
    yield "big2", woven(block, n)
    yield "big3", woven(random_text(37, "xy"), n)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
