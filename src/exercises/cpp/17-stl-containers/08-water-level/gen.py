"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/08-water-level   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นล้าน big1 กับ big2 ตั้งใจให้การเดินย้อนใน naive.cpp ไม่ทัน 1 วินาที
ส่วน big3 เป็นค่าสุ่มขนาดเต็ม วิธีเดินย้อนผ่านได้ แต่ใหญ่เกินกว่าจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1708)

LIMIT = 10**9


def case(values):
    return f"{len(values)}\n" + " ".join(map(str, values))


def cases():
    yield "sample1", case([120, 110, 115, 130, 125, 125, 140, 100])
    yield "single", case([LIMIT])
    yield "rising", case(list(range(1, 501)))
    yield "falling", case(list(range(500, 0, -1)))
    # ระดับเท่ากันทุกวัน ต้องนับรวมทั้งหมด วิธีที่ใช้ < แทน <= จะได้ 1 ทุกวัน
    yield "all-equal", case([777] * 400)
    # ขึ้นแล้วลง แล้วขึ้นเกินยอดเดิม
    yield "mountain", case(list(range(1, 201)) + list(range(200, 0, -1)) + list(range(1, 260)))
    # ค่าซ้ำเยอะจากช่วงค่าที่แคบ
    yield "rand1", case([random.randint(1, 5) for _ in range(1000)])
    yield "rand2", case([random.randint(1, LIMIT) for _ in range(5000)])
    # ขึ้นช้าๆ แต่มีวันตกสลับ เดินย้อนไกลแต่ไม่ถึงต้น
    yield "sawtooth", case([i // 3 + (5 if i % 3 == 0 else 0) for i in range(3000)])
    yield "big1", case(list(range(1, 1000001)))
    yield "big2", case([123456789] * 1000000)
    yield "big3", case([random.randint(1, LIMIT) for _ in range(1000000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
