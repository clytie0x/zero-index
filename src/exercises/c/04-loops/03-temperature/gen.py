"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/03-temperature
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(403)


def text(temps):
    return f"{len(temps)}\n{' '.join(map(str, temps))}"


def cases():
    yield "sample1", text([12, 8, -2, 15, 15, 3, -2])
    yield "single", text([-7])
    yield "all-negative", text([-12, -3, -25, -3, -40, -8])
    yield "all-positive", text([18, 25, 31, 22, 31, 19])
    yield "all-equal", text([0] * 6)
    yield "ends", text([50, -50, 10, 20, -50, 50])
    yield "late", text([-1, 0, 1, 2, -2, 3, -3])
    yield "max", text([random.randint(-50, 50) for _ in range(100000)])
    for i in range(1, 3):
        yield f"rand{i}", text([random.randint(-50, 0) for _ in range(random.randint(2, 30))])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
