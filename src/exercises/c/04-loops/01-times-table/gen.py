"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/01-times-table
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(401)


def cases():
    yield "sample1", "7 5"
    yield "min", "1 1"
    yield "one-row", "9 1"
    yield "n-one", "1 1000"
    yield "max", "1000 1000"
    yield "wide-n", "1000 12"
    for i in range(1, 4):
        yield f"rand{i}", f"{random.randint(2, 1000)} {random.randint(2, 1000)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
