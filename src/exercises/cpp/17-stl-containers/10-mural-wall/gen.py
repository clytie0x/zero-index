"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/10-mural-wall   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นล้าน big1 กับ big2 ตั้งใจให้การขยายทีละแผ่นใน naive.cpp ไม่ทัน 1 วินาที
ส่วน big3 เป็นค่าสุ่มขนาดเต็ม วิธีขยายทีละแผ่นผ่านได้ แต่ใหญ่เกินกว่าจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1710)

LIMIT = 10**9


def case(values):
    return f"{len(values)}\n" + " ".join(map(str, values))


def cases():
    yield "sample1", case([3, 1, 4, 4, 6, 2, 5])
    yield "sample2", case([LIMIT])
    # สูงเท่ากันทุกแผ่น พื้นที่ 5 × 10^11 เกิน int
    yield "all-equal", case([LIMIT] * 500)
    yield "rising", case(list(range(1, 801)))
    yield "falling", case(list(range(800, 0, -1)))
    # รูปตัว V แผ่นกลางเตี้ยสุด
    yield "valley", case(list(range(400, 0, -1)) + list(range(1, 401)))
    # แผ่นสูงมากแผ่นเดียว ชนะภาพกว้างที่เตี้ย
    yield "one-tower", case([1] * 300 + [LIMIT] + [1] * 300)
    yield "rand1", case([random.randint(1, 10) for _ in range(1000)])
    yield "rand2", case([random.randint(1, LIMIT) for _ in range(5000)])
    yield "big1", case([LIMIT] * 1000000)
    yield "big2", case(list(range(1, 1000001)))
    yield "big3", case([random.randint(1, LIMIT) for _ in range(1000000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
