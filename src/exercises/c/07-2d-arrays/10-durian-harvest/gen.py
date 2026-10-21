"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/10-durian-harvest

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
ชุดที่ชื่อขึ้นต้นด้วย big ตั้งใจให้ naive.c ที่บวกทีละช่องไม่ทันเวลา
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(710)


def make(rows, k):
    return f"{len(rows)} {len(rows[0])} {k}\n" + "\n".join(rows)


def rand_orchard(n, m, low=0, high=9):
    return ["".join(str(random.randint(low, high)) for _ in range(m)) for _ in range(n)]


def cases():
    yield "sample1", make(["31415", "92653", "58979", "32384"], 2)
    # สองพื้นที่ได้เท่ากัน ต้องเลือกพื้นที่ที่อยู่แถวบนกว่า
    yield "sample2", make(["1001", "0000", "0110", "0000"], 2)
    yield "one", make(["7"], 1)
    yield "k-one", make(rand_orchard(6, 9), 1)
    yield "k-full", make(rand_orchard(5, 5), 5)
    yield "all-zero", make(["0" * 8 for _ in range(6)], 3)
    yield "all-nine", make(["9" * 30 for _ in range(20)], 7)
    # พื้นที่ที่ดีที่สุดอยู่ชิดมุมล่างขวาพอดี จับลูปที่หยุดก่อนตำแหน่งสุดท้าย
    rows = ["1" * 12 for _ in range(10)]
    rows[8] = "1" * 9 + "999"
    rows[9] = "1" * 9 + "999"
    yield "bottom-right", make(rows, 3)
    yield "thin", make(rand_orchard(1, 1000), 1)
    for i in range(1, 3):
        n, m = random.randint(20, 80), random.randint(20, 80)
        yield f"rand{i}", make(rand_orchard(n, m), random.randint(1, min(n, m)))
    yield "big1", make(rand_orchard(1000, 1000), 500)
    yield "big2", make(rand_orchard(1000, 1000, 3, 9), 300)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
