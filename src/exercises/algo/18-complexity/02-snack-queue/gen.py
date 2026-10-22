"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/02-snack-queue   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big ทำให้คิวยาวหลายแสนคนก่อนเริ่มขาย ตั้งใจให้ erase หัว vector ใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1802)


def case(events):
    return f"{len(events)}\n" + "\n".join(events)


def join():
    return f"1 {random.randint(1, 10**9)}"


def mixed(n, join_rate):
    events = [join() if random.random() < join_rate else "2" for _ in range(n - 1)]
    return events + ["2"]


def cases():
    yield "sample1", case(["1 6701", "1 6702", "2", "1 6815", "2", "2", "2"])
    yield "sample2", case(["2", "1 1000000000", "2"])
    yield "only-sell", case(["2"])
    yield "one-each", case(["1 1", "2"])
    # ขายสลับกับมาต่อคิว คิวไม่เคยยาวเกินหนึ่ง
    events = []
    for _ in range(500):
        events += [join(), "2", "2"]
    yield "alternate", case(events)
    yield "join-then-sell", case([join() for _ in range(3000)] + ["2"] * 3001)
    yield "rand1", case(mixed(5000, 0.5))
    yield "rand2", case(mixed(8000, 0.7))
    yield "big1", case([join() for _ in range(500000)] + ["2"] * 500000)
    yield "big2", case([join() for _ in range(400000)] + mixed(600000, 0.5))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
