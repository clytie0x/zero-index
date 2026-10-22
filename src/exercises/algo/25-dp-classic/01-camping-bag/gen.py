"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/01-camping-bag   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกชุดด้วย backtracking ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีอุปกรณ์ไม่เกิน 20 ชิ้น
ชุดที่ชื่อขึ้นต้นด้วย big มี 100 ชิ้นและเป้จุ 100000 กรัม ซึ่งวิธีลองทุกชุดไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2501)


def build(capacity, items):
    return f"{len(items)} {capacity}\n" + "\n".join(f"{w} {v}" for w, v in items)


def cases():
    yield "sample1", build(10, [(5, 60), (4, 40), (6, 70), (3, 30), (2, 15)])
    # ชิ้นที่คะแนนต่อน้ำหนักดีที่สุดกินที่จนใส่คู่ที่ดีกว่าไม่ลง greedy จะได้ 30
    yield "sample2", build(10, [(6, 30), (5, 20), (5, 20)])
    yield "none-fit", build(50, [(51, 7), (100, 9), (99999, 5)])
    yield "single-exact", build(100000, [(100000, 10**9)])
    # ใส่ได้ทุกชิ้น คะแนนรวม 2 × 10^10 เกิน int
    yield "all-fit", build(100000, [(random.randint(1, 5000), 10**9) for _ in range(20)])
    yield "same-weight", build(35, [(7, random.randint(1, 100)) for _ in range(12)])
    yield "rand1", build(random.randint(10, 60), [(random.randint(1, 20), random.randint(1, 100)) for _ in range(15)])
    items = [(random.randint(1, 100000), random.randint(1, 10**9)) for _ in range(20)]
    yield "rand2", build(sum(w for w, _ in items) // 2, items)
    yield "big1", build(100000, [(random.randint(1, 2000), random.randint(1, 10**9)) for _ in range(100)])
    yield "big2", build(100000, [(random.randint(900, 1100), random.randint(10**8, 10**9)) for _ in range(100)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
