"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/07-broken-stairs   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี n ถึง 70 ตั้งใจให้ recursion ที่ไม่จดคำตอบใน naive.c ไม่ทัน
ชุดเล็กมี n ไม่เกิน 28 ให้ naive.c ตรวจได้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(907)


def build(n, broken):
    text = f"{n} {len(broken)}"
    if broken:
        text += "\n" + " ".join(map(str, broken))
    return text


def random_broken(n, count):
    return sorted(random.sample(range(1, n), count))


def cases():
    yield "sample1", build(4, [])
    yield "sample2", build(6, [3])
    yield "one-step", build(1, [])
    yield "first-broken", build(5, [1])
    # สามขั้นติดกันชำรุด ข้ามไม่ได้ คำตอบเป็น 0
    yield "blocked", build(12, [5, 6, 7])
    # ชำรุดสองขั้นติดกัน ยังก้าวสามขั้นข้ามได้
    yield "two-in-row", build(15, [4, 5, 9, 10])
    yield "rand1", build(20, random_broken(20, 4))
    yield "rand2", build(28, random_broken(28, 3))
    yield "big1", build(70, [])
    # คำตอบราว 3.8 × 10^9 เกิน int ไม่มาก จับคนที่ลืมใช้ long long
    yield "big-over-int", build(37, [])
    yield "big2", build(70, random_broken(70, 12))
    # คำตอบเป็น 0 ทุกขั้น จับคนที่ใช้ 0 แทนคำว่ายังไม่ได้คำนวณ
    yield "big-zero", build(70, [1, 2, 3])
    # ชำรุดเฉพาะขั้นคี่ในครึ่งบน ไม่มีสามขั้นติดกัน คำตอบจึงไม่เป็น 0 และครึ่งล่างยังต้องคำนวณเยอะ
    yield "big3", build(69, sorted(random.sample(range(35, 69, 2), 10)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
