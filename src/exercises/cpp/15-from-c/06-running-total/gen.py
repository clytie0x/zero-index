"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/06-running-total   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N = 10^6 ตั้งใจให้ naive.cpp ที่ใช้ cin cout แบบปกติกับ endl ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1506)

LIMIT = 10**9


def case(amounts):
    return f"{len(amounts)}\n" + " ".join(map(str, amounts))


def cases():
    yield "sample1", case([500, -200, 1000, -1300, 50])
    yield "single", case([-7])
    # ยอดสะสมเกิน int ตั้งแต่รายการที่สาม จับคนที่ใช้ int เก็บยอด
    yield "over-int", case([LIMIT, LIMIT, LIMIT, -LIMIT, -LIMIT, -LIMIT, -LIMIT])
    yield "zeros", case([0] * 10)
    # ติดลบจนต่ำกว่าขอบล่างของ int
    yield "deep-negative", case([-LIMIT] * 5 + [LIMIT] * 5)
    yield "rand1", case([random.randint(-1000, 1000) for _ in range(1000)])
    yield "rand2", case([random.randint(-LIMIT, LIMIT) for _ in range(5000)])
    yield "big1", case([random.randint(-LIMIT, LIMIT) for _ in range(10**6)])
    # ทุกรายการเป็นค่ามากสุด ยอดสุดท้ายคือ 10^15 และทุกบรรทัดยาวที่สุดเท่าที่เป็นไปได้
    yield "big2", case([LIMIT] * 10**6)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
