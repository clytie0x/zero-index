"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/07-calculator/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/07-calculator
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(307)


def cases():
    yield "sample1", "7 / 2"
    yield "sample2", "15 % 0"
    yield "add-max", "1000000000 + 1000000000"
    yield "sub-negative", "3 - 1000000000"
    yield "mul-max", "1000000000 * 1000000000"
    yield "mul-zero", "0 * 999"
    yield "div-zero", "0 / 0"
    yield "div-exact", "1000000000 / 1"
    yield "mod", "17 % 5"
    yield "mod-zero-left", "0 % 7"
    yield "mod-bigger", "5 % 1000000000"
    # B เป็น 0 กับเครื่องหมายอื่น ต้องไม่ตอบ error
    yield "add-zero", "5 + 0"
    yield "sub-zero", "5 - 0"
    yield "mul-zero-right", "5 * 0"
    for i, op in enumerate("+-*/%", 1):
        yield f"rand{i}", f"{random.randint(0, 10**9)} {op} {random.randint(1, 10**9)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
