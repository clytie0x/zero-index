"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/04-race-time/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/04-race-time
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1104)
DAY = 86400


def hms(seconds):
    return f"{seconds // 3600} {seconds % 3600 // 60} {seconds % 60}"


def runner_name():
    return random.choice(string.ascii_uppercase) + "".join(
        random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 9)))


def race(rows):
    # rows คือ (ชื่อ, วินาทีที่ออกตัว, วินาทีที่เข้าเส้น)
    return "\n".join([str(len(rows))] + [f"{n} {hms(s)} {hms(f)}" for n, s, f in rows])


def random_runner(min_used=1, max_used=DAY - 1):
    length = random.randint(min_used, max_used)
    start = random.randint(0, DAY - 1 - length)
    return runner_name(), start, start + length


def cases():
    # คนที่เข้าเส้นก่อนไม่ใช่ผู้ชนะ เพราะออกตัวเร็วกว่ามาก
    yield "sample1", race([("Mali", 6 * 3600, 6 * 3600 + 3000), ("Krit", 6 * 3600 + 1800, 6 * 3600 + 4500),
                           ("Ploy", 6 * 3600 + 900, 6 * 3600 + 3800)])
    # ใช้เวลาเท่ากัน คนที่เข้าเส้นก่อนชนะ ถึงจะอยู่หลังในข้อมูลเข้า
    yield "sample2", race([("Nat", 7 * 3600 + 600, 9 * 3600 + 20), ("Beam", 7 * 3600, 8 * 3600 + 50 * 60 + 20)])
    yield "single", race([("Solo", 0, 1)])
    # เท่ากันทุกอย่าง ต้องได้คนแรก
    yield "full-tie", race([("First", 3600, 7200), ("Second", 3600, 7200), ("Third", 3600, 7200)])
    # ต้องยืมวินาทีและนาที 9 59 50 ถึง 10 0 10
    yield "borrow", race([("Borrow", 9 * 3600 + 59 * 60 + 50, 10 * 3600 + 10), ("Slow", 0, 100)])
    yield "whole-day", race([("Long", 0, DAY - 1), ("Longer", 0, DAY - 1)])
    yield "one-second", race([random_runner(2, 5000) for _ in range(30)] + [("Quick", DAY - 2, DAY - 1)])
    # เวลาที่ใช้มาจากชุดเล็กๆ จึงเท่ากันบ่อย ต้องตัดสินด้วยเวลาเข้าเส้น
    rows = []
    for _ in range(1000):
        length = random.choice([3000, 3001, 3005])
        start = random.randint(0, 20000)
        rows.append((runner_name(), start, start + length))
    yield "many-ties", race(rows)
    yield "rand1", race([random_runner() for _ in range(1000)])
    yield "rand2", race([random_runner(1800, 7200) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
