"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/01-about-face   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(501)


def line(values):
    return " ".join(map(str, values))


def cases():
    yield "sample1", "5\n10432 10518 10377 10291 10605"
    yield "min", "1\n42"
    yield "two", "2\n1 99999"
    yield "same", "6\n7 7 7 7 7 7"
    yield "palindrome", "7\n1 2 3 4 3 2 1"
    yield "max", f"1000\n{line(random.randint(1, 99999) for _ in range(1000))}"
    for i, n in enumerate((37, 500), 1):
        yield f"rand{i}", f"{n}\n{line(random.randint(1, 99999) for _ in range(n))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
