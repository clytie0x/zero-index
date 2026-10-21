"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/04-odd-sock   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีถุงเท้าเกือบล้านข้าง วิธีนับทีละสีด้วยลูปซ้อนใน naive.c ไม่ทัน
ชุดอื่นมีไม่เกินสามพันข้าง ให้ naive.c ผ่านได้ เพื่อตรวจว่าเฉลยกับวิธีช้าตอบตรงกัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1204)

TOP = 10**9


def build(odd_color, odd_times, pair_colors):
    # pair_colors คือรายการสีที่จะใส่สีละสองข้าง สีซ้ำในรายการได้ จำนวนรวมยังเป็นเลขคู่
    socks = [odd_color] * odd_times
    for color in pair_colors:
        socks += [color, color]
    random.shuffle(socks)
    return f"{len(socks)}\n" + " ".join(map(str, socks))


def random_case(n, low, high):
    odd_color = random.randint(low, high)
    pairs = [random.randint(low, high) for _ in range((n - 1) // 2)]
    pairs = [c for c in pairs if c != odd_color]
    return build(odd_color, n - 2 * len(pairs), pairs)


def cases():
    yield "sample1", "5\n41 7 93 7 41"
    yield "sample2", "7\n2 5 2 5 5 9 9"
    yield "single", "1\n0"
    yield "zero-color", "3\n4 0 4"
    yield "max-color", "3\n1000000000 1000000000 1000000000"
    yield "all-same", build(123456789, 2999, [])
    yield "few-colors", random_case(2999, 1, 5)
    yield "rand1", random_case(2999, 0, TOP)
    yield "rand2", random_case(1001, 999999000, TOP)
    yield "big1", random_case(999999, 0, TOP)
    yield "big2", build(0, 1, [random.randint(1, 1000) for _ in range(499999)])
    yield "big3", build(TOP, 1, [random.randint(0, TOP - 1) for _ in range(499999)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
