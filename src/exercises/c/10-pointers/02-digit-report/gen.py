"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/02-digit-report   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1002)


def make(numbers):
    return "\n".join([str(len(numbers))] + [str(x) for x in numbers])


def cases():
    yield "sample1", make([2569, 7, 1000])
    yield "sample2", make([0, 98089])
    # 0 มีหนึ่งหลัก ลูปแบบ while (x > 0) จะได้ 0 หลัก
    yield "zero", make([0, 0, 0])
    # 10^18 มี 19 หลัก เกิน int และเลขโดดน้อยสุดคือ 0
    yield "max", make([10**18, 999999999999999999, 2147483648])
    yield "one-digit", make(list(range(10)))
    # ทุกหลักเท่ากัน เลขโดดน้อยสุดกับมากสุดต้องเท่ากัน
    yield "same-digits", make([5555, 111111111111111111, 88, 9])
    # มี 0 อยู่ตรงกลางและท้าย จับการตั้งค่าเริ่มต้นของเลขโดดน้อยสุดผิด
    yield "inner-zeros", make([102030405, 900000000000000009, 70])
    yield "rand1", make([random.randint(0, 10**18) for _ in range(50)])
    yield "rand2", make([random.randint(0, 10 ** random.randint(1, 18)) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
