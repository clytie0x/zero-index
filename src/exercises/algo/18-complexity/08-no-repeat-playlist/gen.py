"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/18-complexity/08-no-repeat-playlist   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสน และช่วงที่ไม่ซ้ำยาวเป็นแสน
ตั้งใจให้ naive.cpp ที่เริ่มนับใหม่ทุกจุดเริ่มต้องเดินช่วงยาวซ้ำๆ จนไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1808)


def case(songs):
    return f"{len(songs)}\n" + " ".join(map(str, songs))


def cases():
    yield "sample1", case([4, 7, 4, 9, 2, 7, 5, 9])
    # ช่วงยาว 3 มีสองช่วง ต้องตอบช่วงที่เริ่มก่อน
    yield "sample2", case([1, 2, 3, 1, 2, 3])
    yield "single", case([1000000])
    yield "all-same", case([42] * 2000)
    yield "all-distinct", case(random.sample(range(1, 1000001), 3000))
    # สองช่วงยาว 5 เท่ากัน ช่วงหลังจบที่เพลงสุดท้าย ต้องตอบช่วงแรก
    yield "best-at-end", case([5, 5, 5, 1, 2, 3, 4, 5])
    yield "rand1", case([random.randint(1, 50) for _ in range(2000)])
    yield "rand2", case([random.randint(1, 1000000) for _ in range(20000)])
    perm = random.sample(range(1, 3001), 3000)
    yield "repeat-block", case(perm + perm[:1500])
    yield "big1", case(random.sample(range(1, 1000001), 200000))
    perm = random.sample(range(1, 1000001), 100000)
    yield "big2", case(perm + perm)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
