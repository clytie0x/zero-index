"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/07-lucky-number
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(407)


def cases():
    yield "sample1", "9875"
    yield "sample2", "7"
    yield "zero", "0"
    yield "ten", "10"
    yield "two-steps", "19"
    yield "over-int", "9999999999"
    yield "max", str(10**18)
    yield "nines", "9" * 18
    for i in range(1, 4):
        yield f"rand{i}", str(random.randint(10**15, 10**18 - 1))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
