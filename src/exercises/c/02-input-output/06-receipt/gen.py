"""สร้างไฟล์ข้อมูลเข้าของข้อนี้ แล้วสร้างคำตอบจากเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/02-input-output/06-receipt

คำสั่งแรกรันในโฟลเดอร์ข้อ คำสั่งที่สองรันที่รากของโปรเจกต์
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(206)

ITEMS = ["Pencil", "Eraser", "Notebook", "Ruler", "Glue", "Stapler", "Marker", "Scissors",
         "Highlighter", "Calculator", "Folder", "Tape", "Crayon", "Compass", "Envelope"]


def line(name, qty, satang):
    return f"{name} {qty} {satang // 100}.{satang % 100:02d}"


def rand_line():
    name = random.choice([n for n in ITEMS if len(n) <= 10])
    return line(name, random.randint(1, 999), random.randint(1, 100000))


def cases():
    yield "sample1", "\n".join([line("Pencil", 3, 650), line("Notebook", 12, 2500), line("Glue", 1, 4575)])
    yield "min", "\n".join([line("A", 1, 1), line("B", 1, 1), line("C", 1, 1)])
    yield "max", "\n".join([line("Calculator", 999, 100000)] * 3)
    yield "long-names", "\n".join([line("Calculator", 5, 89900), line("Highlight", 40, 1525), line("X", 999, 1)])
    yield "cents", "\n".join([line("Eraser", 7, 99), line("Tape", 33, 333), line("Marker", 101, 1001)])
    # เลขนัยสำคัญเกิน 7 หลัก ถ้าเก็บด้วย float แทน double จะคลาดในหลักสตางค์
    yield "precision", "\n".join([line("Notebook", 999, 99999), line("Marker", 987, 87654), line("Folder", 913, 12345)])
    for i in range(1, 4):
        yield f"rand{i}", "\n".join(rand_line() for _ in range(3))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        for row in text.split("\n"):
            item, qty, price = row.split()
            assert item.isalpha() and 1 <= len(item) <= 10 and 1 <= int(qty) <= 999, name
            assert 0.01 <= float(price) <= 1000.00 and len(price.split(".")[1]) == 2, name
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
