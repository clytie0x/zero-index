"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/03-heaviest-parcel   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีพัสดุค้างในโกดังเป็นแสนชิ้น ตั้งใจให้การไล่หาค่ามากสุดใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2003)

TOP = 10**9


def case(events):
    return f"{len(events)}\n" + "\n".join(events)


def add(w):
    return f"+ {w}"


def random_events(count, add_chance, low=1, high=TOP):
    return [add(random.randint(low, high)) if random.random() < add_chance else "-" for _ in range(count)]


def cases():
    yield "sample1", case([add(1200), add(450), "-", add(3000), add(450), "-", "-", "-", "-"])
    yield "sample2", case(["-", add(7), "-"])
    yield "only-empty", case(["-"] * 5)
    yield "same-weight", case([add(500)] * 4 + ["-"] * 5)
    yield "extremes", case([add(1), add(TOP), add(TOP), "-", add(1), "-", "-", "-", "-"])
    yield "increasing", case([add(w) for w in range(1, 2001)] + ["-"] * 2001)
    yield "rand1", case(random_events(3000, 0.55, 1, 50))
    yield "rand2", case(random_events(12000, 0.6))
    events = [add(random.randint(1, TOP)) for _ in range(100000)]
    for _ in range(100000):
        events += ["-", add(random.randint(1, TOP))]
    yield "big1", case(events)
    events = [add(random.randint(1, TOP)) for _ in range(150000)] + ["-"] * 150000
    yield "big2", case(events)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
