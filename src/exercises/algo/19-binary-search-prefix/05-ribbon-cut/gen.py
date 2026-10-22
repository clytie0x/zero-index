"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/05-ribbon-cut   (รันที่รากของโปรเจกต์)

ชุดที่ไม่ได้ขึ้นต้นด้วย big ใช้ริบบิ้นสั้น ให้วิธีลองทุกความยาวใน naive.cpp ตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big ใช้ริบบิ้นยาวถึงพันล้าน ซึ่งวิธีลองทุกความยาวไม่ทัน
big3 ทำให้จำนวนเส้นรวมเกิน int ถ้าไม่ใช้ long long
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1905)


def build(k, lengths):
    return f"{len(lengths)} {k}\n" + " ".join(map(str, lengths))


def cases():
    yield "sample1", "5 13\n730 410 980 260 555"
    yield "sample2", "3 20\n5 9 4"
    yield "k-one", build(1, [17, 3, 99, 42])
    yield "one-ribbon", build(7, [100])
    yield "all-equal", build(12, [60] * 4)
    # ต้องได้ทุกเส้นพอดี ทั้งที่ตัดแล้วไม่มีเศษเลย
    yield "exact", build(30, [30, 60, 90, 120])
    yield "just-enough", build(sum([1000, 999, 1, 2]), [1000, 999, 1, 2])
    lengths = [random.randint(1, 100) for _ in range(20)]
    yield "rand1", build(random.randint(1, sum(lengths)), lengths)
    lengths = [random.randint(1, 100000) for _ in range(100)]
    yield "rand2", build(random.randint(1, 5000), lengths)
    lengths = [random.randint(1, 10**9) for _ in range(100000)]
    yield "big1", build(random.randint(10**8, 10**9), lengths)
    lengths = [random.randint(9 * 10**8, 10**9) for _ in range(1000)]
    yield "big2", build(10**9, lengths)
    # ลูปจะตรวจความยาว 1 ซม. ซึ่งได้เส้นรวมเกิน int ถ้านับด้วย int จะได้ 0 แทน 2
    yield "big3", build(10**9, [943464097, 920246633, 952992312])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
