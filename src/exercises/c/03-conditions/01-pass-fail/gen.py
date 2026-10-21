"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/01-pass-fail/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/01-pass-fail
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(301)


def cases():
    yield "sample1", "32 25"
    yield "sample2", "20 29"
    yield "exact", "20 30"
    yield "zero", "0 0"
    yield "full", "40 60"
    yield "exam-only", "0 50"
    yield "just-fail", "40 9"
    yield "just-pass", "40 10"
    for i in range(1, 3):
        yield f"rand{i}", f"{random.randint(0, 40)} {random.randint(0, 60)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
