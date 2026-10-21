"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/01-percent

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(201)


def is_tie(score, total):
    # เปอร์เซ็นต์คูณ 100 คือ 10000 * score / total ถ้าเศษเป็นครึ่งพอดี การปัดจะต่างกันตามระบบ
    return (20000 * score) % (2 * total) == total


def cases():
    yield "sample1", "45 60"
    yield "sample2", "7 9"
    yield "zero", "0 1"
    yield "full", "1000 1000"
    yield "one-third", "1 3"
    yield "two-thirds", "2 3"
    yield "tiny", "1 1000"
    yield "almost-full", "999 1000"
    count = 0
    while count < 3:
        total = random.randint(1, 1000)
        score = random.randint(0, total)
        if is_tie(score, total):
            continue
        count += 1
        yield f"rand{count}", f"{score} {total}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        score, total = map(int, text.split())
        assert not is_tie(score, total), name
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
