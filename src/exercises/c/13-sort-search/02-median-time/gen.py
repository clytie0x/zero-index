"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/02-median-time   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดตัวอย่าง extremes rand และ many-ties จัดให้ช่องกลางของข้อมูลที่ยังไม่เรียงไม่ใช่ค่ากลาง เพื่อจับวิธีที่ลืมเรียง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1302)


def line(values):
    return " ".join(map(str, values))


def unsorted_middle(values):
    """สลับจนช่องกลางของข้อมูลที่ยังไม่เรียงไม่ใช่ค่ากลาง ถ้าทำได้"""
    values = values[:]
    median = sorted(values)[len(values) // 2]
    if all(v == median for v in values):
        return values
    while values[len(values) // 2] == median:
        random.shuffle(values)
    return values


def case(values):
    return f"{len(values)}\n{line(values)}"


def cases():
    yield "sample1", case([1820, 1795, 2410, 1650, 3600])
    yield "sample2", case([2100, 1980, 2100, 2650, 1700, 2100, 1990])
    yield "single", case([42])
    yield "all-same", case([2500] * 9)
    yield "sorted", case(list(range(1000, 1015)))
    yield "reversed", case(list(range(100000, 99000, -10))[:99])
    yield "extremes", case(unsorted_middle([1, 100000, 1, 100000, 50000, 1, 100000]))
    yield "rand1", case(unsorted_middle([random.randint(1500, 4000) for _ in range(51)]))
    yield "rand2", case(unsorted_middle([random.randint(1, 100000) for _ in range(999)]))
    yield "many-ties", case(unsorted_middle([random.choice([1800, 1900, 2000]) for _ in range(301)]))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
