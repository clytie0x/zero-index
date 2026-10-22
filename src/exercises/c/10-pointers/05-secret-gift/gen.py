"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/05-secret-gift   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1005)


def make(rooms):
    lines = [str(len(rooms))]
    for drawn in rooms:
        lines += [str(len(drawn)), " ".join(map(str, drawn))]
    return "\n".join(lines)


def shuffled(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    return a


def cycle(n):
    """คนที่ i จับได้ i + 1 คนสุดท้ายจับได้คนแรก คำตอบต่างจากข้อมูลเข้าทุกตำแหน่ง"""
    return [i % n + 1 for i in range(1, n + 1)]


def cases():
    yield "sample1", make([[3, 1, 4, 2], [1]])
    yield "sample2", make([[2, 3, 1], [2, 1]])
    # ทุกคนจับได้ชื่อตัวเอง
    yield "self", make([list(range(1, 8)), [1]])
    # จับเป็นวง คนที่พิมพ์รายการจับฉลากเดิมออกไปจะผิดทุกตำแหน่ง
    yield "cycle", make([cycle(10), cycle(2), cycle(5)])
    # ห้องละคน 20000 ห้อง ห้องเล็กที่สุดติดกันหลายห้อง
    yield "many-rooms", make([[1]] * 20000)
    yield "rand1", make([shuffled(random.randint(1, 12)) for _ in range(10)])
    yield "rand2", make([shuffled(random.randint(1, 1000)) for _ in range(30)])
    # ห้องเดียวขนาดเต็ม ต้องจองตามขนาดจริง
    yield "big-one-room", make([shuffled(100000)])
    sizes = [40000, 25000, 10000, 4990] + [1] * 10
    yield "big-mixed", make([shuffled(n) for n in sizes])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
