"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/09-water-bill/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/09-water-bill
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(309)


def cases():
    yield "sample1", "25"
    yield "sample2", "4"
    # ค่าขั้นต่ำ 6 หน่วยได้ 48 บาท 7 หน่วยได้ 56 บาท
    yield "zero", "0"
    yield "one", "1"
    yield "below-minimum", "6"
    yield "above-minimum", "7"
    # สองฝั่งของทุกขอบขั้นบันได
    yield "tier1-end", "10"
    yield "tier2-start", "11"
    yield "tier2-end", "30"
    yield "tier3-start", "31"
    yield "max", "1000000"
    for i in range(1, 3):
        yield f"rand{i}", str(random.randint(31, 1000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
