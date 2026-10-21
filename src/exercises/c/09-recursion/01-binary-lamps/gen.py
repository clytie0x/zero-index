"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/01-binary-lamps   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(901)


def cases():
    yield "sample1", "13"
    yield "sample2", "6"
    yield "zero", "0"
    yield "one", "1"
    yield "two", "2"
    # 2 ยกกำลัง 59 มีเลข 0 ต่อท้าย 59 ตัว จับคนที่พิมพ์หลักกลับด้าน
    yield "power-of-two", str(2**59)
    yield "all-ones", str(2**59 - 1)
    # เกิน int จับคนที่ลืมใช้ long long
    yield "over-int", "3000000000"
    yield "max", str(10**18)
    yield "rand1", str(random.randint(100, 100000))
    yield "rand2", str(random.randint(10**17, 10**18))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
