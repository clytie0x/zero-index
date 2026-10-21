"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/07-trip-speed

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(207)


def is_tie(start, end, tenths):
    # ความเร็วคูณ 100 คือ (tenths / 10) * 60 * 100 / minutes = 600 * tenths / minutes
    minutes = end - start
    return (1200 * tenths) % (2 * minutes) == minutes


def case(start, end, tenths):
    return f"{start // 60:02d}:{start % 60:02d}\n{end // 60:02d}:{end % 60:02d}\n{tenths // 10}.{tenths % 10}"


def cases():
    yield "sample1", case(8 * 60 + 15, 10 * 60 + 5, 455)
    yield "sample2", case(13 * 60 + 40, 14 * 60 + 25, 120)
    yield "one-minute", case(6 * 60, 6 * 60 + 1, 1)
    yield "whole-day", case(0, 23 * 60 + 59, 10000)
    yield "exact-hours", case(7 * 60 + 30, 9 * 60 + 30, 333)
    yield "under-hour", case(9 * 60 + 50, 10 * 60 + 17, 87)
    count = 0
    while count < 3:
        start = random.randint(0, 1438)
        end = random.randint(start + 1, 1439)
        tenths = random.randint(1, 10000)
        if is_tie(start, end, tenths):
            continue
        count += 1
        yield f"rand{count}", case(start, end, tenths)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        first, second, dist = text.split("\n")
        start = int(first[:2]) * 60 + int(first[3:])
        end = int(second[:2]) * 60 + int(second[3:])
        tenths = round(float(dist) * 10)
        assert start < end and 1 <= tenths <= 10000 and not is_tie(start, end, tenths), name
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
