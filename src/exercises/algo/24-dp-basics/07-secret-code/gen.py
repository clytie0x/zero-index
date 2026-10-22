"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/07-secret-code   (รันที่รากของโปรเจกต์)

naive.cpp ลองตัดหนึ่งหรือสองหลักไปเรื่อยๆ โดยไม่จด ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงยาวไม่เกิน 30 ตัว
ชุดที่ชื่อขึ้นต้นด้วย big ยาวเกือบล้านตัว
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2407)


def digits(length, pool):
    return "".join(random.choice(pool) for _ in range(length))


def encoded(limit):
    """ต่อรหัสของตัวอักษรสุ่มจนยาวเกือบ limit ตัว จึงถอดได้อย่างน้อยหนึ่งแบบเสมอ แม้จะมีเลข 0"""
    parts, length = [], 0
    while True:
        code = str(random.choice([10, 20, 1, 2, 11, 12, 21, 26, 3, 5, 9, 17, 25]))
        if length + len(code) > limit:
            return "".join(parts)
        parts.append(code)
        length += len(code)


def cases():
    yield "sample1", "226"
    yield "sample2", "1020"
    yield "zero", "0"
    yield "leading-zero", "06"
    yield "thirty", "1301"
    yield "one", "7"
    yield "twenty-seven", "2727272727"
    yield "all-ones", "1" * 30
    yield "tens", "10" * 15
    yield "rand1", digits(30, "12")
    yield "rand2", encoded(30)
    # ไม่มี 0 จึงไม่ค่อยเป็นศูนย์ และมีเลข 1 2 มากพอให้คำตอบเกิน 1000000007
    yield "big1", digits(1000000, "1122233456789")
    yield "big2", "1" * 1000000
    yield "big3", encoded(1000000)
    # ไฟล์เล็ก แต่ recursion ตรงๆ กับเลข 1 ยาว 70 ตัวต้องเรียกราว 6 × 10^14 ครั้ง
    yield "big4", "1" * 70


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
