"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/04-minesweeper

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(704)


def make(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(rows)


def rand_board(r, c, density):
    return make(["".join("*" if random.random() < density else "." for _ in range(c)) for _ in range(r)])


def cases():
    yield "sample1", make(["*...", "..*.", ".*..", "...*"])
    yield "one-safe", make(["."])
    yield "one-mine", make(["*"])
    yield "no-mines", make(["....." for _ in range(4)])
    yield "all-mines", make(["***", "***"])
    yield "surrounded", make(["***", "*.*", "***"])
    # ทุ่นระเบิดอยู่ที่มุมและขอบ จับโปรแกรมที่ไม่เช็กขอบ
    yield "corners", make(["*....*", "......", "*....*"])
    yield "one-row", make([".*..**.*."])
    yield "max", rand_board(100, 100, 0.3)
    for i in range(1, 3):
        yield f"rand{i}", rand_board(random.randint(10, 50), random.randint(10, 50), 0.2)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
