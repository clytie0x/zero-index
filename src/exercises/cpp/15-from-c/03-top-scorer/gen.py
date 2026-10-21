"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/03-top-scorer   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ค่าเฉลี่ยที่ตกตรงครึ่งของทศนิยมตำแหน่งที่สองพอดี ปัดต่างกันในแต่ละระบบ gen.py จึงสุ่มใหม่จนไม่ตกตรงนั้น
"""

import random
import string
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1503)


def is_half(scores):
    """ค่าเฉลี่ยคูณ 100 แล้วเหลือเศษครึ่งพอดีหรือไม่"""
    return Fraction(100 * sum(scores), len(scores)).denominator == 2


def case(people):
    assert not is_half([s for _, s in people]), people
    return f"{len(people)}\n" + "\n".join(f"{name} {score}" for name, score in people)


def random_name():
    first = random.choice(string.ascii_uppercase)
    return first + "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 9)))


def random_class(n, low, high):
    while True:
        people = [(random_name(), random.randint(low, high)) for _ in range(n)]
        if not is_half([s for _, s in people]):
            return people


def cases():
    yield "sample1", case([("Malee", 72), ("Somchai", 85), ("Ploy", 64)])
    yield "sample2", case([("Anan", 90), ("Nok", 95), ("Kitti", 95), ("Wan", 88), ("Pim", 70), ("Ton", 81)])
    yield "single", case([("Oak", 100)])
    # ทุกคนได้ 0 คนแรกต้องเป็นคำตอบ จับคนที่เริ่มค่ามากสุดที่ 0 แล้วเทียบด้วย >
    yield "all-zero", case([("Fah", 0), ("Mint", 0), ("Bank", 0)])
    # คะแนนสูงสุดซ้ำกันหลายคน และคนแรกไม่ได้อยู่หัวรายชื่อ จับคนที่ใช้ >=
    yield "tie-middle", case([("Jom", 40), ("Bee", 98), ("Pond", 98), ("Earth", 12), ("Tan", 98), ("Gift", 7)])
    # ค่าเฉลี่ยลงตัวเป็นจำนวนเต็ม ต้องพิมพ์ .00
    yield "whole-average", case([("Max", 60), ("Min", 80)])
    # คนสุดท้ายได้มากสุด และค่าเฉลี่ยมีทศนิยมไม่รู้จบ
    yield "best-last", case([("Aom", 10), ("Boy", 20), ("Nat", 100)])
    yield "rand1", case(random_class(40, 30, 100))
    yield "max", case(random_class(1000, 0, 100))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
