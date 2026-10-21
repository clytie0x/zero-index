"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/02-ribbon-cut   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีริบบิ้นแสนม้วนที่สั้นที่สุดยาวเกือบพันล้าน
ตั้งใจให้วิธีไล่ลองทุกความยาวจากม้วนที่สั้นที่สุดลงมาใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(902)


def build(lengths):
    return f"{len(lengths)}\n" + " ".join(map(str, lengths))


def cases():
    yield "sample1", build([84, 60, 36])
    yield "sample2", build([7, 5])
    yield "single", build([1000000000])
    yield "all-same", build([999999937] * 5)
    yield "has-one", build([1, 1000000000, 999999999])
    # ห.ร.ม. เป็น 1 จำนวนชิ้นรวมเกิน int จับคนที่ลืมใช้ long long
    yield "over-int", build([1000000000, 1000000000, 1000000000, 999999999, 1000000000])
    yield "rand1", build([6 * random.randint(1, 50) for _ in range(10)])
    yield "rand2", build([37 * random.randint(1, 1000) for _ in range(1000)])
    yield "rand3", build([random.randint(1, 1000000) for _ in range(5000)])
    yield "big1", build([random.randint(990000000, 1000000000) for _ in range(100000)])
    yield "big2", build([7 * random.randint(141000000, 142857142) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
