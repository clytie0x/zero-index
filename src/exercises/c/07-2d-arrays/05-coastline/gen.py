"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/05-coastline

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(705)


def make(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(rows)


def rand_map(r, c, land):
    return make(["".join("#" if random.random() < land else "." for _ in range(c)) for _ in range(r)])


def cases():
    yield "sample1", make(["......", ".##...", ".###..", "...#..", "......"])
    yield "sample2", make(["#####", "#...#", "#####"])
    yield "one-land", make(["#"])
    yield "one-water", make(["."])
    yield "all-land", make(["#######" for _ in range(4)])
    yield "checker", make(["".join("#" if (r + c) % 2 == 0 else "." for c in range(9)) for r in range(6)])
    yield "max-land", make(["#" * 100 for _ in range(100)])
    yield "max", rand_map(100, 100, 0.55)
    for i in range(1, 3):
        yield f"rand{i}", rand_map(random.randint(10, 60), random.randint(10, 60), 0.5)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
