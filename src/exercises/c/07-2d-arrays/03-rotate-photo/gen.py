"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/03-rotate-photo

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(703)


def make(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(rows)


def rand_photo(r, c, dark):
    return make(["".join("#" if random.random() < dark else "." for _ in range(c)) for _ in range(r)])


def cases():
    yield "sample1", make(["#....", "#....", "#####"])
    yield "one", make(["#"])
    yield "one-row", make(["##.#.."])
    yield "one-column", make(["#", ".", ".", "#", "#"])
    # รูปตัว L หมุนผิดทิศจะได้รูปที่ต่างกันชัดเจน
    yield "letter-l", make(["#...", "#...", "#...", "####"])
    yield "square", rand_photo(7, 7, 0.4)
    yield "max", rand_photo(100, 100, 0.5)
    yield "wide", rand_photo(3, 100, 0.3)
    for i in range(1, 3):
        yield f"rand{i}", rand_photo(random.randint(10, 60), random.randint(10, 60), 0.35)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
