"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/02-thai-date

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import datetime
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(202)


def cases():
    yield "sample1", "2010-03-05"
    yield "sample2", "2026-10-21"
    yield "min", "1957-01-01"
    yield "max", "2100-12-31"
    yield "leap-day", "2024-02-29"
    yield "two-digit-day", "2008-11-30"
    first = datetime.date(1957, 1, 1).toordinal()
    last = datetime.date(2100, 12, 31).toordinal()
    for i in range(1, 4):
        yield f"rand{i}", datetime.date.fromordinal(random.randint(first, last)).isoformat()


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
