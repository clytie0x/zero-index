"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/02-song-request   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N สองแสนและรหัสต่างกันเป็นแสน ตั้งใจให้การไล่หาใน vector ของ naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2002)

TOP = 10**9


def case(songs):
    return f"{len(songs)}\n" + " ".join(map(str, songs))


def cases():
    yield "sample1", case([5021, 77, 5021, 900000001, 77, 5021, 3])
    yield "sample2", case([40, 12, 40, 12, 999])
    yield "single", case([TOP])
    # เสมอกันสามเพลง ต้องตอบรหัสน้อยสุดแม้จะมาทีหลัง
    yield "tie", case([TOP, 8, TOP, 500, 8, 500, 1000, 7])
    yield "all-same", case([123456789] * 1000)
    yield "extremes", case([1, TOP, TOP, 1, TOP])
    yield "all-distinct", case(random.sample(range(1, TOP + 1), 3000))
    pool = random.sample(range(1, TOP + 1), 40)
    yield "rand1", case([random.choice(pool) for _ in range(5000)])
    pool = random.sample(range(1, TOP + 1), 2000)
    yield "rand2", case([random.choice(pool) for _ in range(10000)])
    songs = random.sample(range(1, TOP + 1), 199990)
    songs += songs[-10:]
    random.shuffle(songs)
    yield "big1", case(songs)
    pool = random.sample(range(1, TOP + 1), 100000)
    yield "big2", case([random.choice(pool) for _ in range(200000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
