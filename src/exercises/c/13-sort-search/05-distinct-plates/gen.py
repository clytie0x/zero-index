"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/05-distinct-plates   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นแสน ตั้งใจให้ bubble sort ใน naive.c ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1305)

MAX_CODE = 10**9


def line(values):
    return " ".join(map(str, values))


def case(values):
    return f"{len(values)}\n{line(values)}"


def cases():
    yield "sample1", case([5521, 120, 5521, 98000, 120, 5521, 7])
    yield "sample2", case([1000000000, 1, 999999999])
    yield "single", case([42])
    yield "all-same", case([31337] * 12)
    yield "all-distinct", case(random.sample(range(1, MAX_CODE + 1), 15))
    # กลุ่มที่ยาวที่สุดอยู่ท้ายสุดหลังเรียง จับวิธีที่ลืมปิดกลุ่มสุดท้าย
    yield "last-group", case([3, 1, MAX_CODE, 2, MAX_CODE, MAX_CODE, 1])
    yield "rand1", case([random.randint(1, 50) for _ in range(1000)])
    rand2 = [random.randint(1, MAX_CODE) for _ in range(3000)]
    for _ in range(500):
        rand2[random.randrange(3000)] = random.choice(rand2)
    yield "rand2", case(rand2)
    yield "big1", case([random.randint(1, MAX_CODE) for _ in range(100000)])
    yield "big2", case([random.randint(1, 30000) * 33331 for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
