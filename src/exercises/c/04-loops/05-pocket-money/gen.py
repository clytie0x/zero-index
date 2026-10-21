"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/05-pocket-money
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(405)


def amount(low=-1000, high=1000):
    while True:
        x = random.randint(low, high)
        if x != 0:
            return x


def lines(values, per_line=10):
    """จัดตัวเลขเป็นหลายบรรทัด บรรทัดละ per_line ตัว แล้วปิดท้ายด้วย 0"""
    values = values + [0]
    rows = [values[i:i + per_line] for i in range(0, len(values), per_line)]
    return "\n".join(" ".join(map(str, r)) for r in rows)


def cases():
    yield "sample1", "50 -20 -15 100 -40 0"
    yield "only-zero", "0"
    yield "one-income", "35 0"
    yield "one-expense", "-35 0"
    yield "only-income", lines([amount(1, 1000) for _ in range(20)], 7)
    yield "only-expense", lines([amount(-1000, -1) for _ in range(20)], 7)
    yield "break-even", "100 -30 -70 20 -20 0"
    yield "max", lines([1000] * 1000, 25)
    yield "min", lines([-1000] * 1000, 25)
    for i in range(1, 3):
        yield f"rand{i}", lines([amount() for _ in range(random.randint(5, 1000))], random.randint(1, 15))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
