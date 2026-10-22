"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/06-row-swap   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีแถวยาวและสลับหลายครั้ง ตั้งใจให้ naive.c ที่คัดลอกทีละช่องไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1006)


def make(table, swaps):
    lines = [f"{len(table)} {len(table[0])} {len(swaps)}"]
    lines += [" ".join(map(str, row)) for row in table]
    lines += [f"{a} {b}" for a, b in swaps]
    return "\n".join(lines)


def rand_table(r, c):
    return [[random.randint(0, 100) for _ in range(c)] for _ in range(r)]


def rand_swaps(r, q):
    return [(random.randint(1, r), random.randint(1, r)) for _ in range(q)]


def cases():
    yield "sample1", make([[8, 9, 10], [5, 7, 6], [10, 10, 9], [3, 4, 8]], [(1, 3), (2, 4), (3, 4)])
    yield "sample2", make([[100, 0, 50, 75, 25]], [(1, 1)])
    # ตารางคอลัมน์เดียว สลับแถวเหมือนสลับในอาเรย์ธรรมดา
    yield "one-column", make([[x] for x in range(10, 0, -1)], [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)])
    # สลับแถวกับตัวเองและสลับไปกลับ ตารางต้องเหมือนเดิม
    yield "same-row", make(rand_table(5, 4), [(2, 2), (5, 5), (1, 4), (4, 1)])
    # R ไม่เท่ากับ C จับโปรแกรมที่สลับขนาดตอนอ่านหรือพิมพ์
    yield "wide", make(rand_table(3, 40), rand_swaps(3, 25))
    yield "tall", make(rand_table(60, 2), rand_swaps(60, 200))
    yield "rand1", make(rand_table(20, 20), rand_swaps(20, 500))
    # แถวยาว 50000 ช่อง สลับ 100000 ครั้ง ถ้าคัดลอกทีละช่องต้องย้ายค่าราว 5 x 10^9 ครั้ง
    yield "big1", make(rand_table(2, 50000), [(1, 2)] * 99999 + [(2, 2)])
    yield "big2", make(rand_table(2, 50000), [random.choice([(1, 2), (2, 1), (1, 2), (2, 1), (1, 1)]) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
