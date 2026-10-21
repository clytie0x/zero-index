"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/08-functions/05-two-rooms

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(805)


def make(room_a, room_b):
    return (f"{len(room_a)}\n" + " ".join(map(str, room_a)) + "\n"
            + f"{len(room_b)}\n" + " ".join(map(str, room_b)))


def scores(n, low=0, high=100):
    return [random.randint(low, high) for _ in range(n)]


def cases():
    yield "sample1", make([62, 88, 75, 91, 70], [80, 95, 95, 60])
    # ค่าเฉลี่ย 1.5 กับ 1 หาร int แล้วได้ 1 เท่ากัน จับคนที่หารแบบตัดเศษ
    yield "sample2", make([1, 2], [1])
    # ค่าเฉลี่ยเท่ากันพอดีทั้งที่จำนวนคนต่างกัน
    yield "same-average", make([70, 80], [60, 90, 75, 75])
    yield "one-each", make([50], [50])
    yield "zero-and-full", make([0, 0, 0], [100])
    # ห้อง B มีคนเดียว ค่ามากสุดกับน้อยสุดเป็นค่าเดียวกัน
    yield "single-b", make([10, 100, 55, 0, 99], [77])
    # ค่าเฉลี่ยต่างกันน้อยมาก 999 คนได้ 100 กับอีกคนได้ 99 เทียบกับทุกคนได้ 100 อีกห้อง
    yield "tiny-gap", make([100] * 999 + [99], [100] * 1000)
    yield "rand1", make(scores(20, 40, 100), scores(25, 40, 100))
    yield "rand2", make(scores(1000), scores(1000))
    # สองห้องเหมือนกันแต่สลับลำดับ ต้องได้ SAME
    room = scores(1000)
    shuffled = room[:]
    random.shuffle(shuffled)
    yield "same-scores", make(room, shuffled)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
