"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/03-name-tag

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(203)


def word(length):
    return random.choice(string.ascii_uppercase) + "".join(
        random.choice(string.ascii_lowercase) for _ in range(length - 1))


def cases():
    yield "sample1", "Somchai Jaidee"
    yield "one-letter", "A B"
    yield "max-both", "Phraphutthayotfachul Wongsakulsirichaiyut"
    yield "long-first", "Kittiphatwongsakorn Ong"
    yield "long-last", "Ploy Sirisombatwattanakul"
    yield "lowercase", "mali saetang"
    for i in range(1, 3):
        yield f"rand{i}", f"{word(random.randint(1, 20))} {word(random.randint(1, 20))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        first, last = text.split()
        assert 1 <= len(first) <= 20 and 1 <= len(last) <= 20 and (first + last).isalpha(), name
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
