"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/06-recipe-fraction

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(806)


def make(fractions):
    return f"{len(fractions)}\n" + "\n".join(f"{a}/{b}" for a, b in fractions)


def rand_fractions(n):
    return [(random.randint(1, 1000), random.randint(1, 20)) for _ in range(n)]


def cases():
    yield "sample1", make([(3, 4), (1, 3), (5, 6)])
    # รวมได้จำนวนเต็มพอดี ต้องพิมพ์ 2 ไม่ใช่ 2/1
    yield "sample2", make([(1, 2), (3, 4), (3, 4)])
    yield "single", make([(1, 1)])
    # ตัวเดียวแต่ยังไม่เป็นอย่างต่ำ
    yield "reduce-one", make([(6, 4)])
    yield "max-one", make([(1000, 1)])
    # ตัวส่วน 1 ถึง 20 ครบ ส่วนของคำตอบคือ ค.ร.น. ของ 1 ถึง 20
    yield "all-denominators", make([(1, b) for b in range(1, 21)])
    # ตัวส่วนเป็นจำนวนเฉพาะ ถ้าไม่ทำอย่างต่ำระหว่างทาง ตัวเศษจะเกิน long long และ p × b เกิน int ตั้งแต่กลางทาง
    yield "primes-max", make([(1000, b) for b in [19, 17, 13, 11, 7, 5, 3, 2, 19, 17, 13, 11, 7, 5, 3, 2, 19, 17, 13, 11]])
    # ตัวส่วนใหญ่ทุกตัว ผลคูณของตัวส่วนทั้ง 20 ตัวเกิน long long
    yield "large-denominators", make([(997, 19), (999, 20), (991, 17), (983, 18)] * 5)
    # ทุกตัวหน้าเท่ากับตัวส่วน รวมได้ 20 ถ้วยพอดี
    yield "all-whole", make([(b, b) for b in range(1, 21)])
    yield "rand1", make(rand_fractions(5))
    yield "rand2", make(rand_fractions(20))
    yield "rand3", make(rand_fractions(20))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
