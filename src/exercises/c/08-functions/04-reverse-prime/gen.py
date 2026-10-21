"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/04-reverse-prime

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(804)


def cases():
    yield "sample1", "1 20"
    yield "sample2", "90 200"
    # 1 กลับหลังได้ 1 จับ is_prime ที่ลืมเช็ก n < 2
    yield "one", "1 1"
    yield "two", "2 2"
    # 19 เป็นจำนวนเฉพาะแต่ 91 ไม่ใช่ และ 91 ไม่ใช่จำนวนเฉพาะแต่ 19 ใช่ ต้องได้ 0 ทั้งคู่
    yield "half-prime", "19 19"
    yield "reverse-only", "91 91"
    yield "palindrome", "101 101"
    yield "full", "1 100000"
    yield "top", "90000 100000"
    for i in range(1, 3):
        a = random.randint(1, 100000)
        yield f"rand{i}", f"{a} {random.randint(a, 100000)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
