"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/10-biggest-number   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นแสน ตั้งใจให้ bubble sort ใน naive.c ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1310)


def line(values):
    return " ".join(map(str, values))


def case(values):
    return f"{len(values)}\n{line(values)}"


def cases():
    yield "sample1", case([30, 5, 34, 3, 9])
    yield "sample2", case([10, 2])
    yield "single-zero", case([0])
    yield "all-zeros", case([0, 0, 0, 0])
    # ศูนย์ปนกับเลขอื่น ศูนย์ต้องไปอยู่ท้าย
    yield "zeros-mixed", case([0, 100, 0, 1])
    # 3 กับ 30 จับวิธีที่เทียบแค่ strcmp ส่วน 12 กับ 121 จับวิธีที่ถือว่าเลขสั้นมาก่อนเสมอ
    yield "prefix-trap", case([3, 30, 12, 121, 34, 343])
    yield "same-digit", case([9, 99, 999, 9999, 98, 989])
    yield "max-values", case([1000000000, 999999999, 1000000000, 99999999])
    yield "rand1", case([random.randint(0, 1000) for _ in range(100)])
    yield "rand2", case([random.randint(0, 10**9) for _ in range(2000)])
    yield "big1", case([random.randint(0, 10**9) for _ in range(100000)])
    yield "big2", case([random.randint(0, 99) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
