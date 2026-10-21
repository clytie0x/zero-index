"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/03-nearest-shop/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/03-nearest-shop
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1103)
LIMIT = 10**9


def shop_name():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 12)))


def town(home, shops):
    lines = [f"{home[0]} {home[1]}", str(len(shops))]
    lines += [f"{name} {x} {y}" for name, x, y in shops]
    return "\n".join(lines)


def near(home, spread, n):
    return [(shop_name(),
             max(-LIMIT, min(LIMIT, home[0] + random.randint(-spread, spread))),
             max(-LIMIT, min(LIMIT, home[1] + random.randint(-spread, spread)))) for _ in range(n)]


def cases():
    yield "sample1", town((2, 3), [("SevenA", 7, 3), ("Lotus", -1, 6), ("Mart24", 4, -2)])
    yield "sample2", town((0, 0), [("North", 0, 5), ("East", 5, 0), ("Corner", 3, 4)])
    yield "single", town((5, 5), [("Only", -5, 5)])
    yield "at-home", town((100, -100), [("Far", 0, 0), ("Here", 100, -100), ("Also", 100, -100)])
    # สองร้านไกลเท่ากันแต่ทิศต่างกัน ต้องตอบร้านแรก
    yield "tie", town((10, 10), [("Zeta", 13, 14), ("Alpha", 7, 6), ("Beta", 14, 13)])
    # ไกลสุดขอบ กำลังสองของระยะ 8 x 10^18
    yield "far-corners", town((-LIMIT, -LIMIT), [("Edge", LIMIT, LIMIT)])
    yield "far-many", town((LIMIT, -LIMIT), [("A1", -LIMIT, LIMIT), ("B2", -LIMIT, -LIMIT), ("C3", LIMIT, LIMIT)])
    # ผลต่างแค่หลักหมื่น แต่กำลังสองเกิน int แล้ว
    yield "over-int", town((0, 0), [("Big", 50000, 50000), ("Bigger", 60000, 0), ("Small", 46341, 0)])
    yield "rand1", town((123456789, -987654321), near((123456789, -987654321), 10**6, 1000))
    home = (random.randint(-LIMIT, LIMIT), random.randint(-LIMIT, LIMIT))
    yield "rand2", town(home, [(shop_name(), random.randint(-LIMIT, LIMIT), random.randint(-LIMIT, LIMIT)) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
