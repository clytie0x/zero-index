"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/06-beaker-pairs   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน ตั้งใจให้วิธีลองทุกคู่ใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1806)
MAX_V = 10**6


def case(volumes):
    return f"{len(volumes)}\n" + " ".join(map(str, volumes))


def cases():
    yield "sample1", case([50, 100, 250, 30, 500])
    # สองใบจุเท่ากัน นับสองทิศ
    yield "sample2", case([200, 200, 600])
    yield "two-same", case([1, 1])
    yield "no-ways", case([7, 11, 13, 17, 19, 23])
    # ใบที่จุ 1 มิลลิลิตรตักใส่ได้ทุกใบ
    yield "has-one", case([1] + [random.randint(2, MAX_V) for _ in range(999)])
    yield "max-volume", case([MAX_V, MAX_V, 500000, 1, 2, 999999])
    yield "all-same", case([360] * 2000)
    yield "rand1", case([random.randint(1, 100) for _ in range(3000)])
    yield "rand2", case([random.randint(1, MAX_V) for _ in range(10000)])
    # ค่าเล็กซ้ำกันมาก คำตอบเกิน int
    yield "big1", case([random.randint(1, 20) for _ in range(200000)])
    yield "big2", case([random.randint(1, MAX_V) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
