"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/08-student-election   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีบัตรล้านใบ ไฟล์ละ 9 ถึง 16 MB จึงไม่เก็บใน git
ข้อนี้ไม่มี naive.cpp เพราะวัดแล้ว cin แบบปกติที่ -O2 ใช้ 0.65 วินาทีกับ big1 และ 1.06 วินาทีกับ big2
ซึ่งเฉียดขอบ 1 วินาทีเกินไปที่จะใช้เป็นตัวอย่างของวิธีที่ไม่ทัน
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1508)


def case(names, ballots):
    return f"{len(names)}\n{' '.join(names)}\n{len(ballots)}\n" + "\n".join(ballots)


def mixed(word):
    return "".join(random.choice([c.lower(), c.upper()]) for c in word)


def typo(word):
    """เปลี่ยนตัวอักษรหนึ่งตัว หรือเติมหนึ่งตัว หรือลบหนึ่งตัว ให้กลายเป็นบัตรเสีย"""
    i = random.randrange(len(word))
    kind = random.randint(0, 2)
    if kind == 0:
        other = random.choice([c for c in string.ascii_lowercase if c != word[i]])
        return word[:i] + other + word[i + 1:]
    if kind == 1 and len(word) < 15:
        return word[:i] + random.choice(string.ascii_lowercase) + word[i:]
    if len(word) > 1:
        return word[:i] + word[i + 1:]
    return word + "x"


def ballots(names, weights, n, invalid_rate):
    out = []
    for _ in range(n):
        vote = random.choices(names, weights)[0]
        if random.random() < invalid_rate:
            vote = typo(vote)
        out.append(mixed(vote))
    return out


def unique_names(k, low, high):
    names = []
    while len(names) < k:
        w = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(low, high)))
        if w not in names:
            names.append(w)
    return names


def cases():
    yield "sample1", case(["malee", "somchai", "ploy"],
                          ["Malee", "SOMCHAI", "malee", "plooy", "Ploy", "mALEE", "somchai"])
    yield "sample2", case(["anan", "nok"], ["Anan", "NOK", "anann", "nok", "ANAN"])
    yield "single", case(["x"], ["X"])
    # ผู้สมัครคนเดียวและบัตรเสียทุกใบ ผู้ชนะยังเป็นคนนั้น เพราะไม่มีใครเสมอ
    yield "one-candidate", case(["solo"], ["sol", "soloo", "olos", "SOLOX"])
    # ไม่มีใครได้คะแนนเลย ทุกคนเสมอที่ 0
    yield "all-zero", case(["aa", "bb", "cc"], ["ab", "ba", "c", "aaa"])
    # ชื่อหนึ่งเป็นส่วนต้นของอีกชื่อ จับคนที่เทียบแค่บางส่วน
    yield "prefix-names", case(["tan", "tanya", "ta"], ["TAN", "Tanya", "ta", "TANY", "t", "tanyaa", "TA", "tanya"])
    # คนที่ชนะอยู่ท้ายรายชื่อ และคนหัวรายชื่อได้ 0
    yield "last-wins", case(["pim", "pond", "earth"], ["EARTH", "pond", "earth", "Earth", "pimm", "eartH"])
    names = unique_names(10, 3, 15)
    yield "rand1", case(names, ballots(names, [random.randint(1, 10) for _ in names], 300, 0.1))
    names = unique_names(10, 1, 15)
    # ให้สองคนแรกคะแนนเท่ากันพอดี
    votes = [mixed(names[0]) for _ in range(2000)] + [mixed(names[1]) for _ in range(2000)]
    votes += ballots(names[2:], [1] * 8, 1000, 0.3)
    random.shuffle(votes)
    yield "rand-tie", case(names, votes)
    names = unique_names(10, 5, 12)
    yield "big1", case(names, ballots(names, [random.randint(1, 100) for _ in names], 10**6, 0.05))
    # ชื่อยาว 15 ตัวทุกชื่อ บัตรยาวสุด
    names = unique_names(10, 15, 15)
    yield "big2", case(names, ballots(names, [1] * 10, 10**6, 0.2))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
