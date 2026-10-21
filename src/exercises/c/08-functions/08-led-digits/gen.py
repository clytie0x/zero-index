"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/08-led-digits

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(808)


def digits(length):
    return "".join(random.choice("0123456789") for _ in range(length))


def cases():
    yield "sample1", "1 0123456789"
    yield "sample2", "2 2026"
    yield "min", "1 1"
    yield "one-eight", "1 8"
    # ขึ้นต้นด้วย 0 จับคนที่รับเป็นตัวเลขแล้ว 0 หาย
    yield "leading-zero", "3 007"
    yield "max-size", "10 9"
    # ยาวสุดและใหญ่สุด กว้าง 20 × 12 + 19 คอลัมน์
    yield "max", f"10 {'8' * 20}"
    yield "ones", "4 1111"
    yield "rand1", f"{random.randint(1, 5)} {digits(random.randint(1, 8))}"
    yield "rand2", f"{random.randint(1, 10)} {digits(20)}"
    yield "rand3", f"{random.randint(5, 10)} {digits(random.randint(10, 20))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
