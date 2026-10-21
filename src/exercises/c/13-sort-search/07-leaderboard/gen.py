"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/07-leaderboard   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นห้าหมื่น ตั้งใจให้ bubble sort ใน naive.c ไม่ทัน 1 วินาที
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1307)


def unique_names(count, max_length=10):
    names = set()
    while len(names) < count:
        length = random.randint(1, max_length)
        names.add("".join(random.choice(string.ascii_lowercase) for _ in range(length)))
    # เรียงก่อนสุ่มลำดับ ลำดับของ set ที่เป็นสตริงเปลี่ยนตาม PYTHONHASHSEED
    names = sorted(names)
    random.shuffle(names)
    return names


def case(rows):
    return f"{len(rows)}\n" + "\n".join(f"{name} {solved} {penalty}" for name, solved, penalty in rows)


def random_rows(count, max_solved, max_penalty):
    return [(name, random.randint(0, max_solved), random.randint(0, max_penalty))
            for name in unique_names(count)]


def cases():
    yield "sample1", case([("somchai", 3, 120), ("malee", 4, 300), ("anan", 3, 95),
                           ("kanya", 3, 120), ("preeda", 1, 10), ("boonmee", 3, 120)])
    yield "sample2", case([("zed", 0, 0), ("amy", 0, 0)])
    yield "single", case([("solo", 10, 100000)])
    yield "all-tied", case([(name, 5, 500) for name in ["dan", "ann", "cat", "bob", "eve"]])
    # ชื่อที่เป็นส่วนต้นของกันและกัน ชื่อสั้นต้องมาก่อน
    yield "prefix-names", case([("abc", 2, 7), ("ab", 2, 7), ("a", 2, 7), ("abcd", 2, 6), ("b", 2, 100000)])
    # ทำผ่านมากแต่เวลาปรับมาก ต้องยังอยู่ก่อนคนที่ทำผ่านน้อยแต่เวลาปรับน้อย
    yield "solved-first", case([("slow", 2, 100000), ("fast", 1, 0), ("mid", 2, 0), ("none", 0, 0)])
    yield "rand1", case(random_rows(100, 3, 20))
    yield "rand2", case(random_rows(2000, 10, 100000))
    yield "big1", case(random_rows(50000, 10, 100000))
    yield "big2", case(random_rows(50000, 3, 30))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
