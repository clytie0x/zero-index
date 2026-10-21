"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/05-ticket-line   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(505)


def line(values):
    return " ".join(map(str, values))


def tickets(n):
    return random.sample(range(1, 1000001), n)


def cases():
    yield "sample1", "6\n11 12 13 14 15 16\n3 2 99"
    yield "single", "1\n5\n1 1 7"
    yield "leave-first", "5\n21 22 23 24 25\n1 3 50"
    yield "leave-last", "5\n21 22 23 24 25\n5 2 50"
    yield "join-first", "5\n21 22 23 24 25\n3 1 50"
    yield "join-last", "5\n21 22 23 24 25\n2 5 50"
    yield "same-place", "5\n21 22 23 24 25\n4 4 50"
    n = 1000
    yield "max", f"{n}\n{line(tickets(n))}\n{random.randint(1, n)} {random.randint(1, n)} {random.randint(1, 1000000)}"
    n = 30
    yield "rand1", f"{n}\n{line(tickets(n))}\n{random.randint(1, n)} {random.randint(1, n)} {random.randint(1, 1000000)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
