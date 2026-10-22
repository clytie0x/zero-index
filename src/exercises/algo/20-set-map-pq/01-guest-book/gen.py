"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/01-guest-book   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2001)


def random_name(low, high):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(low, high)))


def case(names):
    return f"{len(names)}\n" + "\n".join(names)


def cases():
    yield "sample1", case(["nok", "beam", "arm", "nok", "ploy", "beam", "nok"])
    yield "sample2", case(["somchai"])
    yield "all-same", case(["mint"] * 50)
    # ชื่อที่เป็นส่วนต้นของอีกชื่อ ต้องมาก่อน
    yield "prefix", case(["anna", "ann", "an", "a", "annabelle", "ann", "b", "anna"])
    yield "all-distinct", case(sorted({random_name(1, 20) for _ in range(300)}, reverse=True))
    yield "max-length", case(["z" * 20, "a" * 20, "z" * 19, "a" * 20, "z" * 20])
    pool = sorted({random_name(1, 6) for _ in range(500)})
    yield "rand1", case([random.choice(pool) for _ in range(2000)])
    pool = sorted({random_name(3, 8) for _ in range(5000)})
    yield "rand2", case([random.choice(pool) for _ in range(20000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
