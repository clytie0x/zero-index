"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/01-bird-days   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N และ Q สองแสน และถาม k ใหญ่ๆ
ตั้งใจให้ naive.cpp ที่ไล่ k วันแรกใหม่ทุกคำถามไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1801)


def case(birds, ks):
    return f"{len(birds)} {len(ks)}\n" + " ".join(map(str, birds)) + "\n" + "\n".join(map(str, ks))


def cases():
    yield "sample1", case([7, 3, 7, 12, 3, 5], [1, 3, 4, 6, 2])
    yield "sample2", case([1000000, 1000000, 1], [2, 3, 1])
    yield "single", case([1], [1])
    yield "all-same", case([424242] * 2000, [1, 2000, 1000])
    # ทุกวันเจอชนิดใหม่ คำตอบเท่ากับ k
    yield "all-new", case(random.sample(range(1, 1000001), 3000), [random.randint(1, 3000) for _ in range(3000)])
    birds = [random.randint(1, 30) for _ in range(5000)]
    yield "few-kinds", case(birds, [random.randint(1, 5000) for _ in range(3000)])
    birds = [random.randint(1, 1000000) for _ in range(5000)]
    yield "rand1", case(birds, [random.randint(1, 5000) for _ in range(3000)])
    birds = [random.randint(1, 2000) for _ in range(8000)]
    yield "rand2", case(birds, list(range(8000, 0, -1)))
    birds = [random.randint(1, 1000000) for _ in range(200000)]
    yield "big1", case(birds, [random.randint(150000, 200000) for _ in range(200000)])
    birds = [random.randint(1, 100000) for _ in range(200000)]
    yield "big2", case(birds, [200000] * 200000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
