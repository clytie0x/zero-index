"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/02-name-tag   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1502)


def case(people):
    return f"{len(people)}\n" + "\n".join(f"{a} {b}" for a, b in people)


def mixed(word):
    return "".join(random.choice([c.lower(), c.upper()]) for c in word)


def random_word(low, high):
    return "".join(random.choice(string.ascii_letters) for _ in range(random.randint(low, high)))


def cases():
    yield "sample1", case([("sOMCHAI", "jaidee"), ("MALEE", "Srisuk"), ("ploy", "WONG")])
    yield "single", case([("anan", "boonma")])
    # ชื่อตัวเดียวและนามสกุลตัวเดียว
    yield "one-letter", case([("a", "b"), ("Z", "Y"), ("q", "Q")])
    # เขียนถูกรูปแบบอยู่แล้ว ต้องได้เหมือนเดิม
    yield "already-good", case([("Somchai", "Jaidee"), ("Nok", "Kaewkla")])
    # ตัวพิมพ์ใหญ่ล้วน จับคนที่แก้แค่ตัวแรกแต่ลืมเปลี่ยนที่เหลือเป็นตัวเล็ก
    yield "all-upper", case([("PRAPAI", "THONGDEE"), ("KITTI", "SUKSAN"), ("WANCHAI", "MEESUK")])
    yield "max-length", case([("A" * 20, "b" * 20), (mixed("abcdefghijklmnopqrst"), "x" * 20)])
    yield "rand1", case([(mixed(random_word(2, 10)), mixed(random_word(2, 12))) for _ in range(30)])
    yield "max", case([(random_word(1, 20), random_word(1, 20)) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
