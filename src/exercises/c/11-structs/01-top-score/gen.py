"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/01-top-score/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/01-top-score
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1101)


def name(length=None):
    if length is None:
        length = random.randint(3, 10)
    return random.choice(string.ascii_uppercase) + "".join(
        random.choice(string.ascii_lowercase) for _ in range(length - 1))


def students(rows):
    return "\n".join([str(len(rows))] + [f"{n} {s}" for n, s in rows])


def cases():
    yield "sample1", students([("Mali", 87), ("Krit", 92), ("Ploy", 78), ("Nat", 92), ("Beam", 65)])
    yield "sample2", students([("Somchai", 45), ("Kanya", 60), ("Somsak", 59)])
    yield "single", students([("Pim", 0)])
    # คนแรกได้สูงสุด และมีคนเท่ากันอยู่ท้ายสุด
    yield "first-and-last", students([("Ann", 99)] + [(name(), random.randint(0, 98)) for _ in range(20)] + [("Zed", 99)])
    # คนสุดท้ายได้สูงสุดคนเดียว
    yield "last-best", students([(name(), random.randint(0, 99)) for _ in range(30)] + [("Last", 100)])
    yield "all-zero", students([(name(), 0) for _ in range(50)])
    # ทุกคนได้เต็มเท่ากัน คำตอบต้องเป็นคนแรก
    yield "all-full", students([(name(), 100) for _ in range(1000)])
    # ชื่อยาวสุด 20 ตัว
    yield "long-names", students([(name(20), random.randint(0, 100)) for _ in range(10)])
    # ชื่อซ้ำกันแต่คะแนนต่างกัน
    yield "same-names", students([("Nok", 70), ("Nok", 85), ("Nok", 85), ("Nok", 10)])
    for i in range(1, 3):
        yield f"rand{i}", students([(name(), random.randint(0, 100)) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
