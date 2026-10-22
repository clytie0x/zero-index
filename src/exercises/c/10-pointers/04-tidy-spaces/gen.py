"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/04-tidy-spaces   (รันที่รากของโปรเจกต์)
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1004)
WORD_CHARS = string.ascii_letters + string.digits + ".,!?'-()"


def messy(length):
    """สุ่มคำคั่นด้วยช่องว่าง 1 ถึง 4 ช่อง มีช่องว่างหัวและท้ายด้วย"""
    out = " " * random.randint(0, 5)
    while True:
        w = "".join(random.choice(WORD_CHARS) for _ in range(random.randint(1, 9)))
        gap = " " * random.randint(1, 4)
        if len(out) + len(w) + len(gap) > length:
            break
        out += w + gap
    return out[:length]


def cases():
    yield "sample1", "   Hello,   my  name is    Somchai.  "
    yield "sample2", "Grade:A    Score:  95"
    # มีแต่ช่องว่าง ต้องได้บรรทัดว่าง
    yield "all-spaces", " " * 37
    yield "one-char", "x"
    # จัดเรียบร้อยอยู่แล้ว ต้องได้เหมือนเดิมทุกตัว
    yield "already-tidy", "The quick brown fox jumps over the lazy dog."
    yield "one-word", "          lonely          "
    # ช่องว่างสองช่องสลับกับตัวอักษรตัวเดียว
    yield "single-letters", "  a  b  c  d  e  f  g  " * 10
    yield "rand1", messy(80)
    yield "rand2", messy(1000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        assert 1 <= len(text) <= 1000
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
