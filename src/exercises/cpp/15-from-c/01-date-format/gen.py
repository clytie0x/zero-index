"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/01-date-format   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import datetime
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1501)


def fmt(d):
    return f"{d.day:02d}/{d.month:02d}/{d.year:04d}"


def case(dates):
    return f"{len(dates)}\n" + "\n".join(dates)


def random_date(first_year, last_year):
    start = datetime.date(first_year, 1, 1).toordinal()
    end = datetime.date(last_year, 12, 31).toordinal()
    return datetime.date.fromordinal(random.randint(start, end))


def cases():
    yield "sample1", case(["05/03/2010", "28/11/2009", "14/02/2011"])
    yield "single", case(["01/01/2000"])
    # ทุกส่วนมีเลข 0 นำหน้า จับคนที่อ่านเป็นตัวเลขแล้วพิมพ์ออกไปไม่ครบ
    yield "leading-zeros", case(["01/02/2003", "09/09/2009", "02/01/1999", "07/06/0999"])
    yield "no-zeros", case(["31/12/2099", "25/10/2026", "11/11/2011"])
    yield "leap-day", case(["29/02/2012", "29/02/2000", "28/02/1900"])
    # วันมากกว่า 12 ทุกตัว ถ้าสลับวันกับเดือนจะเห็นทันทีว่าเดือนเกิน 12
    yield "day-over-12", case(["13/01/2001", "20/05/1995", "31/07/2024"])
    yield "rand1", case([fmt(random_date(1990, 2015)) for _ in range(50)])
    yield "max", case([fmt(random_date(1000, 2999)) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
