"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/02-ticket-digits

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(802)


def make(tickets):
    return f"{len(tickets)}\n" + " ".join(map(str, tickets))


def cases():
    yield "sample1", make([4096, 512, 77, 1999, 30])
    # 1999 กับ 2899 ได้ 28 เท่ากัน ใบที่เลขมากกว่ามาก่อน จับคนที่เอาใบแรกที่เจอ
    yield "sample2", make([2899, 45, 1999, 600])
    yield "single-zero", make([0])
    yield "all-zero", make([0, 0, 0])
    # 10^9 ผลบวกแค่ 1 แต่ 999999999 ได้ 81
    yield "max-values", make([1000000000, 999999999, 1000000000])
    # ผลบวกเท่ากันทุกใบ ต้องได้เลขน้อยสุดซึ่งอยู่ท้ายสุด
    yield "tie-last", make([900, 810, 702, 630, 540, 450, 360, 270, 180, 9])
    yield "same-ticket", make([123, 321, 123, 213])
    yield "rand1", make([random.randint(0, 10**6) for _ in range(50)])
    yield "rand2", make([random.randint(0, 10**9) for _ in range(1000)])
    yield "many", make([random.randint(0, 10**9) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
