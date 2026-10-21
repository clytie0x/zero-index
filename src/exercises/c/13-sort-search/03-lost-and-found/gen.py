"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/03-lost-and-found   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1303)


def line(values):
    return " ".join(map(str, values))


def case(target, codes):
    return f"{len(codes)} {target}\n{line(codes)}"


def cases():
    yield "sample1", case(870, [1024, 5531, 870, 4410, 870, 9902])
    yield "sample2", case(77, [12, 34, 56, 78])
    yield "single-found", case(5, [5])
    yield "single-miss", case(5, [6])
    yield "first-only", case(31, [31, 32, 33, 34, 35])
    yield "last-only", case(1000000000, [999999999, 1, 2, 1000000000])
    yield "all-same", case(8, [8] * 20)
    # ค่าที่ใกล้เคียงกันแต่ไม่เท่า จับการเทียบผิดเครื่องหมาย
    yield "near-miss", case(500, [499, 501, 5000, 50, 1500, 500000])
    small = [random.randint(1, 20) for _ in range(1000)]
    yield "rand1", case(7, small)
    big = [random.randint(1, 10**9) for _ in range(1000)]
    big[random.randrange(1000)] = big[0]
    yield "rand2", case(big[0], big)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
