"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/01-above-average   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีนักเรียนแสนคนตามขอบเขตโจทย์ ไม่เก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1601)


def line(values):
    return " ".join(map(str, values))


def case(scores, per_line=20):
    rows = [line(scores[i:i + per_line]) for i in range(0, len(scores), per_line)]
    return "\n".join(rows) + "\n-1"


def cases():
    yield "sample1", "72 85 64 90 58 -1"
    yield "sample2", "80 80 80\n80 -1"
    yield "single", case([55])
    yield "all-zero", case([0] * 12)
    # ค่าเฉลี่ย 50.5 คนที่ได้ 50 ไม่สูงกว่า คนที่ได้ 51 สูงกว่า
    yield "half", case([50, 51, 50, 51, 0, 100, 50, 51])
    # มีคนเดียวที่ต่างจากคนอื่น ค่าเฉลี่ยจึงไม่ใช่จำนวนเต็ม
    yield "one-high", case([0] * 9 + [100])
    yield "one-low", case([100] * 9 + [0])
    yield "rand1", case([random.randint(40, 100) for _ in range(500)])
    yield "rand2", case([random.randint(0, 100) for _ in range(20000)])
    yield "big1", case([random.randint(0, 100) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
