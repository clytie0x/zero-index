"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/02-race/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/02-race
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(302)


def cases():
    yield "sample1", "1253 1187"
    yield "sample2", "1000 1000"
    yield "first-by-one", "999 1000"
    yield "second-by-one", "1000 999"
    yield "min-tie", "1 1"
    yield "max-tie", "100000 100000"
    yield "first-far", "1 100000"
    yield "second-far", "100000 1"
    for i in range(1, 3):
        yield f"rand{i}", f"{random.randint(900, 1500)} {random.randint(900, 1500)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
