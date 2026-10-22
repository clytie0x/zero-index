"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/02-fabric-cut   (รันที่รากของโปรเจกต์)

naive.cpp ลองทุกจำนวนชิ้นของแต่ละแบบ ชุดที่ไม่ได้ขึ้นต้นด้วย big จึงมีผ้ายาวไม่เกิน 2000 เซนติเมตร
ชุดที่ชื่อขึ้นต้นด้วย big มีผ้ายาว 100000 เซนติเมตรและมีแบบที่สั้นมาก ซึ่งวิธีนั้นไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2502)


def build(length, pieces):
    return f"{len(pieces)} {length}\n" + "\n".join(f"{l} {p}" for l, p in pieces)


def cases():
    yield "sample1", build(12, [(2, 30), (5, 80), (7, 120)])
    # ตัดแบบเดียวกันซ้ำ 3 ชิ้นแล้วเหลือเศษ 1 เซนติเมตร ดีกว่าใช้ผ้าจนหมด
    yield "sample2", build(10, [(3, 40), (10, 100), (7, 75)])
    yield "none-fit", build(5, [(6, 100), (100000, 1000000)])
    yield "one-type", build(99, [(10, 7)])
    # แบบสั้นถูก กับแบบยาวที่คุ้มกว่าแค่นิดเดียว
    yield "tiny-piece", build(1000, [(1, 3), (7, 22), (333, 1000)])
    yield "max-price", build(2000, [(1, 1000000), (2, 1999999), (1999, 10**6)])
    yield "rand1", build(random.randint(50, 200), [(random.randint(1, 60), random.randint(1, 1000)) for _ in range(8)])
    yield "rand2", build(2000, [(random.randint(1, 2000), random.randint(1, 10**6)) for _ in range(100)])
    yield "big1", build(100000, [(random.randint(1, 1000), random.randint(1, 10**6)) for _ in range(100)])
    yield "big2", build(100000, [(random.randint(1, 100), random.randint(1, 10**6)) for _ in range(100)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
