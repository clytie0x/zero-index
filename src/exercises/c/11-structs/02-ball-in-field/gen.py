"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/02-ball-in-field/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/02-ball-in-field
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1102)
LIMIT = 10000


def field(x1, y1, x2, y2, balls):
    lines = [f"{x1} {y1} {x2} {y2}", str(len(balls))]
    lines += [f"{x} {y}" for x, y in balls]
    return "\n".join(lines)


def scatter(x1, y1, x2, y2, n, margin):
    # สุ่มรอบสนาม ให้มีทั้งข้างใน บนเส้น และข้างนอก
    balls = []
    for _ in range(n):
        x = random.randint(max(-LIMIT, x1 - margin), min(LIMIT, x2 + margin))
        y = random.randint(max(-LIMIT, y1 - margin), min(LIMIT, y2 + margin))
        if random.random() < 0.2:
            x = random.choice([x1, x2])
        elif random.random() < 0.2:
            y = random.choice([y1, y2])
        balls.append((x, y))
    return balls


def cases():
    yield "sample1", field(0, 0, 10, 6, [(3, 2), (10, 4), (12, 3), (0, 0), (5, 6), (7, 7)])
    yield "sample2", field(-5, -3, 5, 3, [(0, 0), (-5, 3), (6, 0)])
    yield "single-inside", field(0, 0, 2, 2, [(1, 1)])
    yield "corners", field(-2, -1, 4, 3, [(-2, -1), (-2, 3), (4, -1), (4, 3)])
    # อยู่บนเส้นตรงที่ต่อจากขอบ แต่เลยสนามไปแล้ว ต้องนับเป็นข้างนอก
    yield "extended-lines", field(0, 0, 10, 10, [(0, 11), (0, -1), (10, 20), (-3, 0), (15, 10), (10, -1), (0, 5), (5, 10)])
    # สนามบางที่สุด ไม่มีจุดจำนวนเต็มอยู่ข้างในเลย
    yield "thin", field(3, 3, 4, 4, [(3, 3), (4, 4), (3, 4), (4, 3), (5, 5), (2, 3)])
    yield "all-outside", field(0, 0, 1, 1, [(random.randint(2, LIMIT), random.randint(-LIMIT, LIMIT)) for _ in range(50)])
    yield "full-field", field(-LIMIT, -LIMIT, LIMIT, LIMIT, [(-LIMIT, LIMIT), (LIMIT, 0), (0, 0), (9999, -9999), (-10000, -10000)])
    yield "rand1", field(-200, -100, 300, 400, scatter(-200, -100, 300, 400, 1000, 200))
    yield "rand2", field(-9000, 100, 9000, 200, scatter(-9000, 100, 9000, 200, 1000, 1000))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
