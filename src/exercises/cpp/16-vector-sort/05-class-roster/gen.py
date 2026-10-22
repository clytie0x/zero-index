"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/16-vector-sort/05-class-roster   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่มีคนห้องเดียวกันคะแนนเท่ากันเกิน 16 คน ทำให้ sort ที่ไม่ใช่ stable_sort สลับลำดับผิด
ชุดที่ชื่อขึ้นต้นด้วย big มีนักเรียนแสนคน ไม่เก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1605)

NAMES = ["ploy", "mint", "beam", "film", "earth", "fah", "nam", "palm", "boss", "fern",
         "ice", "bank", "pim", "tonkla", "kaew", "first", "june", "nut", "oil", "toey"]


def case(people):
    return f"{len(people)}\n" + "\n".join(f"{name} {room} {score}" for name, room, score in people)


def random_name():
    if random.random() < 0.7:
        return random.choice(NAMES)
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(1, 10)))


def random_people(n, rooms, scores):
    return [(random_name(), random.randint(1, rooms), random.choice(scores)) for _ in range(n)]


def cases():
    yield "sample1", case([("ploy", 3, 85), ("beam", 1, 70), ("mint", 3, 92), ("film", 1, 70),
                           ("earth", 2, 60), ("fah", 3, 85)])
    yield "sample2", case([("nam", 5, 40), ("nam", 5, 40), ("palm", 2, 100), ("nam", 2, 100)])
    yield "single", case([("a", 20, 0)])
    # ทุกคนห้องเดียวกันคะแนนเท่ากัน ต้องออกตามลำดับที่ส่งทุกคน
    yield "all-tie", case([("s" + chr(97 + i % 26) + chr(97 + i // 26), 7, 50) for i in range(40)])
    # ห้องกลับลำดับ คะแนนจากน้อยไปมาก
    yield "reversed", case([(NAMES[i % 20], 20 - i // 5, i % 5 * 25) for i in range(100)])
    yield "extremes", case([("x", 1, 0), ("y", 20, 100), ("z", 1, 100), ("x", 20, 0), ("y", 1, 0)])
    yield "rand1", case(random_people(200, 4, [60, 70, 80]))
    yield "rand2", case(random_people(3000, 20, list(range(0, 101))))
    yield "rand3", case(random_people(3000, 2, [50, 51]))
    yield "big1", case(random_people(100000, 20, list(range(0, 101))))
    yield "big2", case(random_people(100000, 3, [0, 100]))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
