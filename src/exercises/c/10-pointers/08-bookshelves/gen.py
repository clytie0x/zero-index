"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/08-bookshelves   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big ถามช่วงยาวบนชั้นยาว ตั้งใจให้ naive.c ที่บวกทีละเล่มไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1008)
MAX_WORDS = 100000


def make(shelves, queries):
    assert sum(len(books) for books in shelves) <= 100000 and len(queries) <= 100000
    lines = [str(len(shelves))]
    lines += [" ".join(map(str, [len(books)] + books)) for books in shelves]
    lines.append(str(len(queries)))
    lines += [f"{s} {a} {b}" for s, a, b in queries]
    return "\n".join(lines)


def books(n, high=MAX_WORDS):
    return [random.randint(1, high) for _ in range(n)]


def rand_query(shelves):
    s = random.randint(1, len(shelves))
    n = len(shelves[s - 1])
    a = random.randint(1, n)
    return (s, a, random.randint(a, n))


def long_query(shelves, s):
    n = len(shelves[s - 1])
    return (s, random.randint(1, n // 10), random.randint(n - n // 10, n))


def cases():
    yield "sample1", make([[120, 85, 300, 64], [250], [40, 410, 99]], [(1, 2, 3), (3, 1, 3), (2, 1, 1), (1, 1, 4)])
    yield "sample2", make([[7, 8], [9, 10, 11]], [(2, 2, 3), (1, 2, 2)])
    yield "one-book", make([[MAX_WORDS]], [(1, 1, 1)] * 3)
    # ชั้นละเล่ม 30000 ชั้น ชั้นสั้นที่สุดติดกันหลายชั้น
    many = [books(1) for _ in range(30000)]
    yield "big-many-shelves", make(many, [rand_query(many) for _ in range(1000)])
    # ชั้นเดียวยาว 30000 เล่ม เล่มละ 100000 คำ รวม 3 x 10^9 เกิน int
    full = [[MAX_WORDS] * 30000]
    yield "over-int", make(full, [(1, 1, 30000), (1, 2, 29999), (1, 15000, 15000)])
    # ถามตั้งแต่เล่มแรก จับการใช้ prefix[a - 1] ผิด
    shelves = [books(random.randint(1, 30)) for _ in range(20)]
    yield "from-first", make(shelves, [(s, 1, random.randint(1, len(shelves[s - 1]))) for s in range(1, 21)] * 5)
    shelves = [books(random.randint(1, 50)) for _ in range(30)]
    yield "rand1", make(shelves, [rand_query(shelves) for _ in range(200)])
    shelves = [books(random.randint(1, 2000)) for _ in range(50)]
    yield "big-rand2", make(shelves, [rand_query(shelves) for _ in range(2000)])
    shelves = [books(50000), books(40000)] + [books(random.randint(1, 100)) for _ in range(100)]
    yield "big1", make(shelves, [long_query(shelves, random.randint(1, 2)) for _ in range(20000)])
    shelves = [books(99000)] + [books(10) for _ in range(100)]
    yield "big2", make(shelves, [(1, 1, 99000)] + [long_query(shelves, 1) for _ in range(99999)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
