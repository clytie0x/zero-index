"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/07-days-between

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import datetime
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(807)
FIRST = datetime.date(1900, 1, 1)
LAST = datetime.date(2600, 12, 31)


def line(a, b):
    return f"{a.day} {a.month} {a.year} {b.day} {b.month} {b.year}"


def make(pairs):
    return f"{len(pairs)}\n" + "\n".join(line(a, b) for a, b in pairs)


def d(day, month, year):
    return datetime.date(year, month, day)


def rand_pair(max_gap):
    span = (LAST - FIRST).days
    start = FIRST + datetime.timedelta(days=random.randint(0, span))
    gap = random.randint(0, min(max_gap, (LAST - start).days))
    return start, start + datetime.timedelta(days=gap)


def cases():
    yield "sample1", make([
        (d(28, 2, 2024), d(1, 3, 2024)),
        (d(21, 10, 2026), d(21, 10, 2026)),
        (d(1, 1, 2026), d(1, 1, 2027)),
    ])
    # ปี 1900 หารด้วย 100 ลงตัวแต่ 400 ไม่ลงตัว ไม่ใช่ปีอธิกสุรทิน ส่วน 2000 เป็น
    yield "sample2", make([
        (d(28, 2, 1900), d(1, 3, 1900)),
        (d(28, 2, 2000), d(1, 3, 2000)),
        (d(31, 12, 2025), d(1, 1, 2026)),
    ])
    yield "same-day", make([(d(1, 1, 1900), d(1, 1, 1900))])
    yield "full-range", make([(FIRST, LAST)])
    # ข้ามปลายเดือนทุกเดือนของปีอธิกสุรทิน
    yield "month-ends", make([(d(days, month, 2024), d(1, month % 12 + 1, 2024 + month // 12))
                              for month, days in enumerate([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 1)])
    # กุมภาพันธ์ของปีที่ลงท้ายด้วย 00 มี 29 วันเฉพาะปีที่หารด้วย 400 ลงตัว
    yield "century-years", make([(d(1, 2, year), d(1, 3, year)) for year in range(1900, 2601, 100)])
    yield "rand1", make([rand_pair(60) for _ in range(200)])
    yield "rand2", make([rand_pair(5000) for _ in range(1000)])
    yield "rand3", make([rand_pair(300000) for _ in range(300)])
    # ไล่ทีละวันต้องเดินรวมหลายพันล้านวัน วิธีช้าไม่ทัน
    yield "big1", make([rand_pair(300000) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
