"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/07-signal-towers   (รันที่รากของโปรเจกต์)

naive.cpp ลองระยะห่างของทุกคู่จุดเป็นคำตอบ ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีไม่เกิน 200 จุด
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนจุด ซึ่งวิธีลองทุกคู่ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1907)

TOP = 10**9


def build(towers, spots):
    return f"{len(spots)} {towers}\n" + " ".join(map(str, spots))


def distinct(count, low, high):
    return random.sample(range(low, high + 1), count)


def cases():
    yield "sample1", "6 3\n12 3 30 1 20 8"
    yield "two-spots", build(2, [TOP, 0])
    yield "c-two", build(2, [500, 77, 913, 300, 12])
    yield "c-all", build(7, [40, 10, 31, 1, 22, 52, 46])
    yield "even", build(4, [i * 25 for i in range(13)])
    # จุดกระจุกกันเป็นสองกลุ่ม ห่างกันมาก
    yield "clusters", build(5, [1, 2, 3, 4, 5, 999999995, 999999996, 999999997, 999999998, 999999999])
    yield "rand1", build(4, distinct(15, 0, 100))
    yield "rand2", build(37, distinct(200, 0, TOP))
    yield "big1", build(random.randint(2, 100000), distinct(100000, 0, TOP))
    yield "big2", build(30000, distinct(100000, 0, 10**6))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
