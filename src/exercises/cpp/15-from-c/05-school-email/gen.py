"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/05-school-email   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1505)

USER_CHARS = string.ascii_lowercase + string.digits + "._-"


def case(domain, items):
    return f"{domain}\n{len(items)}\n" + "\n".join(items)


def user(low=1, high=15):
    return "".join(random.choice(USER_CHARS) for _ in range(random.randint(low, high)))


def tricky(domain):
    """ข้อความที่หน้าตาคล้ายอีเมลโรงเรียนแต่ผิดกฎ หรืออีเมลที่ถูกต้อง"""
    kind = random.randint(0, 9)
    if kind <= 3:
        return user() + "@" + domain
    if kind == 4:
        return user() + "@my" + domain
    if kind == 5:
        return user() + "@" + domain + ".com"
    if kind == 6:
        return user() + "@" + domain.upper()
    if kind == 7:
        return user() + "@" + user() + "@" + domain
    if kind == 8:
        return "@" + domain
    return user() + "@gmail.com"


def cases():
    yield "sample1", case("school.ac.th", ["malee@school.ac.th", "somchai@gmail.com", "ploy.w@school.ac.th",
                                           "nok@myschool.ac.th", "anan"])
    yield "sample2", case("school.ac.th", ["boy@School.ac.th", "kitti@school.ac.th.com"])
    yield "single", case("x.y", ["a@x.y"])
    # D อยู่ในข้อความแต่ไม่ได้อยู่หลัง @ พอดี จับคนที่ใช้ find(D) อย่างเดียว
    yield "contains-domain", case("kku.ac.th", ["a@akku.ac.th", "kku.ac.th@kku.ac.th", "kku.ac.th", "b@kku.ac.th.th",
                                               "c@kku.ac.t", "d@kku.ac.th"])
    # @ สองตัว และชื่อผู้ใช้ว่าง จับคนที่เช็กแค่ส่วนท้าย
    yield "at-count", case("psu.ac.th", ["x@y@psu.ac.th", "@psu.ac.th", "@@psu.ac.th", "ok@psu.ac.th", "psu.ac.th@"])
    # D สั้นมาก และชื่อผู้ใช้มีจุด ขีด ขีดล่าง
    yield "short-domain", case("a", ["first.last@a", "x_y-z@a", "a@aa", "a@a@a", "q@a"])
    yield "none-valid", case("school.ac.th", ["a@gmail.com", "b@SCHOOL.AC.TH", "school.ac.th", "c@school-ac-th"])
    yield "rand1", case("satit.ac.th", [tricky("satit.ac.th") for _ in range(60)])
    yield "max", case("camp.posn.or.th", [tricky("camp.posn.or.th") for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
