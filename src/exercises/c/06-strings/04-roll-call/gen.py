"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/04-roll-call

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(604)


def name(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def roll(names):
    return f"{len(names)}\n" + "\n".join(names)


def cases():
    yield "sample1", roll(["somchai", "malee", "anan", "wichai", "kanokwan"])
    yield "one", roll(["pim"])
    yield "all-same", roll(["nok"] * 6)
    # คำที่สั้นกว่ามาก่อน และตัวแรกที่ต่างเป็นตัวตัดสิน ไม่ใช่ความยาว
    yield "prefix", roll(["anna", "an", "ann", "annabelle", "b", "az"])
    base = name(19)
    yield "last-letter", roll([base + c for c in random.sample(string.ascii_lowercase, 10)])
    yield "max", roll([name(random.randint(1, 20)) for _ in range(1000)])
    yield "max-long", roll([name(20) for _ in range(1000)])
    yield "rand1", roll([name(random.randint(1, 8)) for _ in range(30)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for test, text in cases():
        (tests / f"{test}.in").write_bytes((text + "\n").encode())


if __name__ == "__main__":
    main()
