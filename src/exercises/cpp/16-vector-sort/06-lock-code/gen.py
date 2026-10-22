"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/06-lock-code   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1606)


def cases():
    yield "sample1", "1203 3"
    yield "sample2", "112 7"
    yield "zero-alone", "0 7"
    # ทุกลำดับขึ้นต้นด้วย 0 จึงไม่มีรหัสที่ใช้ได้
    yield "all-zero", "000 1"
    yield "one-digit", "9 3"
    yield "same-digits", "55555555 5"
    # ตัวเลขต่างกันครบ 8 ตัว ลำดับเริ่มต้นไม่ได้เรียงไว้ ต้อง sort ก่อน
    yield "all-distinct", "86427531 1"
    yield "huge-k", "98765432 999983"
    yield "none", "2468 5"
    yield "zeros-inside", "10020030 7"
    for i in range(1, 4):
        digits = "".join(random.choice("0123456789") for _ in range(random.randint(5, 8)))
        yield f"rand{i}", f"{digits} {random.randint(2, 500)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
