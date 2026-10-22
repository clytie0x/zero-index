"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/04-top-words   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2004)


def random_word(low, high):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(low, high)))


def case(words, m, per_line=12):
    rows = [" ".join(words[i:i + per_line]) for i in range(0, len(words), per_line)]
    return f"{len(words)} {m}\n" + "\n".join(rows)


def cases():
    text = "the exam is on monday the room is near the library is the exam hard"
    yield "sample1", case(text.split(), 3)
    yield "sample2", case("ok ok fine".split(), 5)
    yield "single", case(["hello"], 1)
    # ทุกคำปรากฏเท่ากัน อันดับขึ้นกับตัวอักษรอย่างเดียว
    yield "all-tie", case("pear apple fig banana apple pear fig banana".split(), 3)
    # คำที่เป็นส่วนต้นของอีกคำ และจำนวนเท่ากัน
    yield "prefix-tie", case("an ann anna ann an anna a".split(), 4)
    yield "fewer-than-m", case("x y z y".split(), 100)
    pool = sorted({random_word(1, 4) for _ in range(30)})
    yield "rand1", case([random.choice(pool) for _ in range(500)], 10)
    pool = sorted({random_word(2, 15) for _ in range(3000)})
    weights = [random.randint(1, 50) for _ in pool]
    yield "rand2", case(random.choices(pool, weights=weights, k=20000), 100)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
