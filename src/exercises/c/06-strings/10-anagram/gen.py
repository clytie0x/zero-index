"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/10-anagram

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big ตั้งใจให้ naive.c ที่ค้นซ้อนสองชั้นไม่ทันเวลา
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(610)

MAX = 100000


def word(length, letters=string.ascii_lowercase):
    return "".join(random.choice(letters) for _ in range(length))


def shuffle(text):
    chars = list(text)
    random.shuffle(chars)
    return "".join(chars)


def change_one(text):
    chars = list(text)
    i = random.randrange(len(chars))
    chars[i] = random.choice([c for c in string.ascii_lowercase if c != chars[i]])
    return "".join(chars)


def pair(a, b):
    return f"{a}\n{b}"


def cases():
    yield "sample1", pair("listen", "silent")
    yield "sample2", pair("cat", "cut")
    yield "single-same", pair("a", "a")
    yield "single-diff", pair("a", "b")
    # ตัวอักษรชุดเดียวกันแต่จำนวนต่างกัน
    yield "count-differs", pair("aab", "abb")
    yield "length-differs", pair("abc", "abcc")
    yield "same-word", pair("banana", "banana")
    small = word(2000, "abc")
    yield "small-yes", pair(small, shuffle(small))
    yield "small-no", pair(small, shuffle(change_one(small)))
    big = word(MAX)
    yield "big1", pair(big, shuffle(big))
    yield "big2", pair(big, shuffle(change_one(big)))
    yield "big3", pair("a" * MAX, "a" * (MAX - 1) + "b")
    yield "big4", pair("z" * MAX, "z" * MAX)
    # ค้นไม่เจอทุกตัว วิธีค้นซ้อนต้องเดินครบทั้งคำทุกครั้ง
    yield "big5", pair("a" * MAX, "b" * MAX)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_bytes((text + "\n").encode())


if __name__ == "__main__":
    main()
