"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/08-triangle/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/08-triangle
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(308)


def cases():
    yield "sample1", "3 4 5"
    yield "sample2", "2 2 3"
    yield "equilateral", "7 7 7"
    # ผลบวกเท่ากับด้านที่เหลือพอดี ให้ด้านยาวอยู่ทุกตำแหน่ง จับคนที่เช็กไม่ครบสามคู่หรือใช้ <
    yield "flat-last", "1 2 3"
    yield "flat-first", "3 1 2"
    yield "flat-middle", "2 3 1"
    # ด้านเท่ากันสองด้านแต่ไม่ใช่สามเหลี่ยม จับคนที่ดูด้านเท่ากันก่อน
    yield "equal-but-flat", "1 1 3"
    yield "equal-but-long", "5 10 5"
    # ด้านเท่ากันสองด้านในทุกตำแหน่ง
    yield "iso-ab", "3 3 2"
    yield "iso-bc", "2 3 3"
    yield "iso-ac", "3 2 3"
    yield "min", "1 1 1"
    yield "max-equal", "1000000000 1000000000 1000000000"
    yield "max-thin", "1000000000 1000000000 1"
    yield "max-flat", "1000000000 1 999999999"
    yield "max-scalene", "999999998 999999999 1000000000"
    for i in range(1, 3):
        yield f"rand{i}", " ".join(str(random.randint(1, 100)) for _ in range(3))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
