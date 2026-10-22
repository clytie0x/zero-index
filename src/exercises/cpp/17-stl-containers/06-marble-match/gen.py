"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/06-marble-match   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big ยาวล้านตัว ตั้งใจให้วิธีวนหาคู่ใหม่ตั้งแต่ซ้ายสุดใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1706)


def no_adjacent_pair(length, letters):
    """สตริงที่ไม่มีตัวติดกันซ้ำเลย"""
    out = [random.choice(letters)]
    while len(out) < length:
        c = random.choice(letters)
        if c != out[-1]:
            out.append(c)
    return "".join(out)


def mirror(half):
    """ครึ่งหน้ากับครึ่งหลังกลับด้าน แตกจากตรงกลางออกไปจนหมด"""
    return half + half[::-1]


def cases():
    yield "sample1", "abccbd"
    yield "sample2", "xyyxzz"
    yield "single", "q"
    # สามลูกติดกัน แตกได้คู่เดียว เหลือหนึ่งลูก
    yield "triple", "abbbc"
    yield "no-pairs", no_adjacent_pair(3000, string.ascii_lowercase)
    yield "all-same-even", "a" * 1000
    yield "all-same-odd", "z" * 999
    yield "nested-small", mirror(no_adjacent_pair(1500, "abc"))
    yield "rand1", "".join(random.choice("ab") for _ in range(2000))
    yield "rand2", "".join(random.choice("abc") for _ in range(5000))
    yield "big1", mirror(no_adjacent_pair(500000, string.ascii_lowercase))
    yield "big2", "".join(random.choice("ab") for _ in range(1000000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
