"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/08-diamond
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(408)


def cases():
    yield "sample1", "4"
    yield "min", "1"
    yield "two", "2"
    yield "three", "3"
    yield "five", "5"
    yield "ten", "10"
    yield "max", "50"
    for i in range(1, 3):
        yield f"rand{i}", str(random.randint(6, 49))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
