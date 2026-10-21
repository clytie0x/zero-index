"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/04-password   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1504)

UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
DIGIT = string.digits
SYMBOL = "!@#$%_-."


def case(passwords):
    return f"{len(passwords)}\n" + "\n".join(passwords)


def make(length, pools):
    """สุ่มรหัสยาว length จากกลุ่มตัวอักษรที่ให้ และมีทุกกลุ่มอย่างน้อยหนึ่งตัวถ้ายาวพอ"""
    chars = [random.choice(pool) for pool in pools][:length]
    every = "".join(pools)
    chars += [random.choice(every) for _ in range(length - len(chars))]
    random.shuffle(chars)
    return "".join(chars)


def random_password():
    pools = [p for p in (UPPER, LOWER, DIGIT, SYMBOL) if random.random() < 0.8] or [SYMBOL]
    return make(random.randint(1, 50), pools)


def cases():
    yield "sample1", case(["abc", "school2026", "School2026", "SCHOOL2026", "SchoolDays"])
    yield "single", case(["Ab3!Ab3!"])
    # ยาว 7 กับ 8 พอดี จับคนที่ใช้ <= 8 หรือ > 8
    yield "length-edge", case(["Abc1234", "Abc12345", "A1b2C3d", "A1b2C3d4"])
    # รหัสสั้นที่ผิดกฎข้ออื่นด้วย ต้องตอบ TOO SHORT เท่านั้น
    yield "short-first", case(["a", "1", "!", "ABCDEFG", "abcdefg", "1234567"])
    # ผิดหลายข้อพร้อมกัน ต้องตอบข้อที่มาก่อน
    yield "order", case(["12345678", "abcdefgh", "ABCDEFGH", "!@#$%_-.", "abcd1234", "ABCD1234", "ABCDabcd"])
    # เครื่องหมายที่อยู่ติดขอบช่วงในตาราง ASCII คือ / : ติดกับ 0 9 @ [ ติดกับ A Z และ ` { ติดกับ a z
    yield "ascii-edge", case(["@@@@@@@@Zz9", "Aa0" + "." * 5, "zZ" + "9" * 6, "AZaz09!!",
                              "@[`{AAAA", "@[`{aaaa1", "/:/:/:Aa", "Zz/:/:/:"])
    yield "max-length", case([make(50, [UPPER, LOWER, DIGIT]), "a" * 50, "Z" * 49 + "z", make(50, [UPPER, LOWER, SYMBOL])])
    yield "rand1", case([random_password() for _ in range(40)])
    yield "max", case([random_password() for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
