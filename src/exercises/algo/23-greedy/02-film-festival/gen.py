"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/02-film-festival   (รันที่รากของโปรเจกต์)

long-first ทำให้กฎเริ่มเร็วสุดก่อนผิด short-middle ทำให้กฎสั้นสุดก่อนผิด
touch-gap ทำให้วิธีที่ลืมบวก G ผิด touch-zero ทำให้วิธีที่ใช้ > แทน >= ผิด
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนเรื่องและดูได้เป็นหมื่นเรื่องขึ้นไป วิธี O(N^2) ใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2302)


def build(gap, films):
    return f"{len(films)} {gap}\n" + "\n".join(f"{s} {e}" for s, e in films)


def random_films(n, top, longest):
    films = []
    for _ in range(n):
        s = random.randint(0, top - 1)
        films.append((s, min(top, s + random.randint(1, longest))))
    return films


def cases():
    yield "sample1", build(10, [(0, 100), (90, 200), (110, 180), (190, 300), (200, 260), (270, 400)])
    yield "sample2", build(0, [(60, 120), (0, 60), (30, 90), (120, 180)])
    yield "single", build(1000000000, [(0, 1000000000)])
    yield "long-first", build(5, [(0, 1000), (10, 100), (105, 200), (205, 300), (305, 400), (405, 500)])
    yield "short-middle", build(0, [(0, 50), (50, 100), (45, 55), (100, 150), (150, 200), (145, 155)])
    yield "touch-gap", build(3, [(0, 10), (10, 20), (20, 30), (30, 40), (13, 18)])
    yield "touch-zero", build(0, [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)])
    yield "same-films", build(2, [(5, 9)] * 4 + [(11, 15)] * 3 + [(16, 17)])
    yield "rand1", build(random.randint(0, 5), random_films(20, 100, 20))
    yield "rand2", build(random.randint(0, 50), random_films(2000, 100000, 500))
    yield "big1", build(random.randint(0, 100), random_films(200000, 10**9, 100000))
    films = [(i * 5000, i * 5000 + 4000) for i in range(200000)]
    random.shuffle(films)
    yield "big2", build(1000, films)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
