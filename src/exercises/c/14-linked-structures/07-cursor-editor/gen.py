"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/07-cursor-editor   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big ยาวราวสองล้านตัวและพิมพ์หรือลบใกล้หน้าข้อความ ตั้งใจให้ naive.c ที่เลื่อนอาเรย์ทุกครั้งไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1407)
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def random_keys(length, weights):
    """weights คือโอกาสของ ตัวอักษร < > # ตามลำดับ"""
    kinds = random.choices(["letter", "<", ">", "#"], weights=weights, k=length)
    return "".join(random.choice(LETTERS) if k == "letter" else k for k in kinds)


def cases():
    yield "sample1", "abc<<x>y#z"
    yield "sample2", "hi#<#>##"
    yield "letters-only", "competitiveprogramming"
    # เลื่อนและลบตอนข้อความว่าง ต้องไม่เกิดอะไร
    yield "keys-on-empty", "<<>>##<a"
    yield "delete-at-start", "abc<<<###>>>"
    yield "right-past-end", "ab>>>>c<<<<<<d"
    yield "rand1", random_keys(40, [5, 2, 2, 1])
    yield "rand2", random_keys(3000, [5, 3, 2, 1])
    yield "rand3", random_keys(20000, [6, 3, 2, 2])
    # พิมพ์หน้าสุดทุกครั้ง ข้อความยาวล้านตัว
    yield "big1", "".join(random.choice(LETTERS) + "<" for _ in range(1000000))
    # พิมพ์ยาวหกแสนตัว ถอยไปหน้าสุด แล้วพิมพ์อีกแปดแสนตัวที่หน้าข้อความ
    yield "big2", random_keys(600000, [1, 0, 0, 0]) + "<" * 600000 + random_keys(800000, [1, 0, 0, 0])
    # พิมพ์ยาวเจ็ดแสนตัว แล้วกลับไปลบตัวแรกของข้อความซ้ำๆ รวมยาว 1999999 ตัว
    yield "big3", random_keys(700000, [1, 0, 0, 0]) + "<" * 699999 + "#>" * 300000
    # สุ่มยาวสองล้านตัว เท่าขอบเขต
    yield "big4", random_keys(2000000, [6, 4, 1, 1])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
