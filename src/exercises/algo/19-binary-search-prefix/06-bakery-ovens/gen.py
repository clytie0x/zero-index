"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/06-bakery-ovens   (รันที่รากของโปรเจกต์)

ชุดที่ไม่ได้ขึ้นต้นด้วย big มีคำตอบไม่เกินหลักแสน ให้วิธีลองทีละนาทีใน naive.cpp ตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มีคำตอบถึงหลักพันล้านขึ้นไป ซึ่งวิธีลองทีละนาทีไม่ทัน
all-fast ทำให้ตัวนับถาดล้นถ้าตั้ง hi ไว้ที่ 10^18 แล้วนับครบทุกเตาโดยไม่หยุด
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1906)


def build(trays, minutes):
    return f"{len(minutes)} {trays}\n" + " ".join(map(str, minutes))


def cases():
    yield "sample1", "3 10\n4 6 10"
    yield "one-oven", build(9, [7])
    yield "one-tray", build(1, [50, 13, 20, 13])
    yield "same-speed", build(100, [3] * 8)
    yield "all-fast", build(1000, [1] * 50)
    # เตาช้ามากเตาเดียวไม่ช่วยอะไร
    yield "one-slow", build(500, [2, 3, 1000000000])
    minutes = [random.randint(1, 20) for _ in range(10)]
    yield "rand1", build(random.randint(1, 300), minutes)
    minutes = [random.randint(1, 1000) for _ in range(50)]
    yield "rand2", build(random.randint(1000, 5000), minutes)
    minutes = [random.randint(1, 10**9) for _ in range(100000)]
    yield "big1", build(10**9, minutes)
    yield "big2", build(10**9, [10**9])
    minutes = [random.randint(10**6, 10**7) for _ in range(100000)]
    yield "big3", build(random.randint(10**8, 10**9), minutes)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
