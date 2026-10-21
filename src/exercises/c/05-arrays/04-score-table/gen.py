"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/04-score-table   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(504)


def line(values):
    return " ".join(map(str, values))


def cases():
    yield "sample1", "8\n70 85 70 100 64 85 70 0"
    yield "single", "1\n100"
    yield "all-zero", "5\n0 0 0 0 0"
    # คะแนนเต็มทุกคน จับอาเรย์นับที่มีแค่ 100 ช่อง
    yield "all-full", "3\n100 100 100"
    yield "ends", "4\n0 100 0 100"
    every = list(range(101)) + [random.randint(0, 100) for _ in range(99)]
    random.shuffle(every)
    yield "every-score", f"{len(every)}\n{line(every)}"
    yield "rand1", f"50\n{line(random.randint(40, 80) for _ in range(50))}"
    yield "many", f"100000\n{line(random.randint(0, 100) for _ in range(100000))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
