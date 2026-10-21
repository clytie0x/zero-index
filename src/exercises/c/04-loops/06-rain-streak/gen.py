"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/06-rain-streak
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(406)


def lines(values, per_line=10):
    rows = [values[i:i + per_line] for i in range(0, len(values), per_line)]
    return "\n".join(" ".join(map(str, r)) for r in rows)


def weather(days, chance):
    """แต่ละวันมีโอกาสฝนตก chance ถ้าตกได้ปริมาณ 1 ถึง 120 มิลลิเมตร"""
    return [random.randint(1, 120) if random.random() < chance else 0 for _ in range(days)]


def cases():
    yield "sample1", "0 5 12 0 3 8 20 1 0 0 4"
    yield "all-dry", "0 0 0 0 0"
    yield "all-rain", lines([random.randint(1, 500) for _ in range(30)])
    yield "one-dry", "0"
    yield "one-rain", "7"
    yield "end-streak", "3 0 0 4 0 9 9 9 9 9 9"
    yield "start-streak", "15 22 1 500 0 6 0 6 6 0 0"
    yield "many-lines", "\n".join(map(str, [0, 2, 2, 0, 2, 2, 2, 0, 0, 2]))
    yield "max", lines(weather(100000, 0.6), 20)
    yield "rand1", lines(weather(200, 0.4), 7)
    yield "rand2", lines(weather(5000, 0.85), 50)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
