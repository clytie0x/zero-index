"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/04-dna-match   (รันที่รากของโปรเจกต์)

naive.cpp เป็น recursion ที่ไม่จดคำตอบ ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีสายยาวไม่เกิน 12 ตัว
ชุดที่ชื่อขึ้นต้นด้วย big มีสายยาว 5000 ตัว ซึ่ง recursion ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2504)


def dna(length, letters="ACGT"):
    return "".join(random.choice(letters) for _ in range(length))


def cases():
    yield "sample1", "GATTACA\nTACGTA"
    yield "sample2", "AAAA\nCCC"
    yield "one-letter", "G\nG"
    yield "same", "ACGTTGCA\nACGTTGCA"
    # ตัวแรกของทั้งสองสายเท่านั้นที่ตรงกัน
    yield "first-only", "ACCCCC\nAGGGGGGG"
    yield "inside", "CGT\nAACAAGAATAA"
    yield "rand1", dna(10) + "\n" + dna(12)
    yield "rand2", dna(12, "AC") + "\n" + dna(11, "AC")
    yield "big1", dna(5000) + "\n" + dna(5000)
    yield "big2", dna(5000, "AC") + "\n" + dna(4999, "CG")


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
