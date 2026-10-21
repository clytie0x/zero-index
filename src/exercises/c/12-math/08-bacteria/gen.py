"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/08-bacteria   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีเลขชี้กำลังใหญ่ถึง 10^18 วิธีคูณทีละชั่วโมงใน naive.c ไม่ทัน
ชุดอื่นมีงานรวมไม่เกินราว 10^7 รอบ ให้ naive.c ผ่านได้
ชุด big-base มี A ใหญ่กว่า MOD จับโปรแกรมที่ลืม mod ฐานก่อนคูณ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1208)

MOD = 1000000007
TOP = 10**18


def build(queries):
    return f"{len(queries)}\n" + "\n".join(f"{a} {n}" for a, n in queries)


def cases():
    yield "sample1", build([(2, 10), (3, 0), (5, 3)])
    yield "sample2", build([(2, 100)])
    yield "zero-hours", build([(1, 0), (TOP, 0), (MOD, 0)])
    yield "one", build([(1, 1000000), (1, 1), (7, 1)])
    yield "multiple-of-mod", build([(MOD, 5), (2 * MOD, 1), (MOD * 999999993, 3)])
    yield "base-trap", build([(TOP, 2), (TOP - 1, 3), (MOD + 2, 10), (MOD - 1, 2)])
    yield "rand1", build([(random.randint(1, 10**9), random.randint(0, 1000)) for _ in range(1000)])
    yield "rand2", build([(random.randint(1, TOP), random.randint(0, 100000)) for _ in range(100)])
    yield "big1", build([(2, TOP), (3, TOP - 1), (TOP, TOP)])
    yield "big2", build([(random.randint(1, TOP), random.randint(0, TOP)) for _ in range(100000)])
    yield "big3", build([(random.randint(1, 10**9), random.randint(10**17, TOP)) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
