"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/24-dp-basics/03-fewest-weights   (รันที่รากของโปรเจกต์)

naive.cpp ลองตุ้มทุกแบบเป็นลูกสุดท้ายโดยไม่จด ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมี X ไม่เกิน 30 และตุ้มไม่เกิน 4 แบบ
ชุดที่ชื่อขึ้นต้นด้วย big มี X ถึงแสนและตุ้มร้อยแบบ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2403)


def build(target, weights):
    return f"{len(weights)} {target}\n" + " ".join(map(str, weights))


def cases():
    yield "sample1", build(6, [1, 3, 4])
    yield "sample2", build(23, [5, 7])
    # greedy หยิบ 9 ก่อนได้ 9 + 1 + 1 สามลูก คำตอบคือ 5 + 6 สองลูก
    yield "sample3", build(11, [9, 6, 5, 1])
    yield "one-weight", build(30, [5])
    yield "one-weight-no", build(29, [5])
    yield "exact", build(17, [17, 2, 3])
    yield "too-heavy", build(4, [5, 6, 7])
    yield "rand1", build(30, [1, 3, 4])
    yield "rand2", build(28, random.sample(range(2, 10), 4))
    yield "big1", build(100000, random.sample(range(1, 100001), 100))
    yield "big2", build(100000, random.sample(range(2, 1000), 100))
    # ตุ้มเป็นเลขคู่ทั้งหมด น้ำหนักคี่จึงทำไม่ได้ ต้องเติมตารางจนครบถึงจะรู้
    yield "big3", build(99999, random.sample(range(2, 100001, 2), 100))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
