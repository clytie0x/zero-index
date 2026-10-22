"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/09-pipe-welding   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกลำดับการเชื่อม ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีท่อไม่เกิน 9 ท่อน
ชุดที่ชื่อขึ้นต้นด้วย big มี 500 ท่อน ซึ่งลองทุกลำดับไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2509)

TOP = 10**6


def build(pipes):
    return f"{len(pipes)}\n" + " ".join(map(str, pipes))


def cases():
    yield "sample1", build([40, 10, 30, 20])
    yield "sample2", build([7])
    yield "two", build([TOP, TOP])
    yield "all-equal", build([5] * 8)
    # greedy ที่เชื่อมคู่ที่รวมกันสั้นที่สุดก่อนได้ 187 แต่ค่าน้อยสุดจริงคือ 169
    yield "greedy-trap", build([17, 2, 19, 18, 19])
    yield "increasing", build([1, 2, 4, 8, 16, 32, 64, 128, 256])
    yield "rand1", build([random.randint(1, 100) for _ in range(8)])
    yield "rand2", build([random.randint(1, TOP) for _ in range(9)])
    yield "big1", build([random.randint(1, TOP) for _ in range(500)])
    yield "big2", build([TOP] * 500)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
