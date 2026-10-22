"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/07-three-bottles   (รันที่รากของโปรเจกต์)

สถานะมีไม่เกิน 101 × 101 แบบ DFS ทันทุกชุด ข้อนี้ไม่มีชุด big
ชุด many-states ไปถึงได้ 258 สถานะ มากที่สุดที่เจอจากการสุ่มลอง 20000 แบบ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2107)


def build(caps, water):
    return " ".join(map(str, caps)) + "\n" + " ".join(map(str, water))


def random_case(low, high):
    caps = [random.randint(low, high) for _ in range(3)]
    water = [random.randint(0, cap) for cap in caps]
    return build(caps, water)


def cases():
    yield "sample1", build([3, 5, 8], [0, 0, 8])
    yield "sample2", build([2, 4, 6], [0, 1, 4])
    yield "no-water", build([10, 20, 30], [0, 0, 0])
    yield "all-full", build([7, 11, 13], [7, 11, 13])
    yield "tiny", build([1, 1, 1], [1, 0, 0])
    yield "same-size", build([6, 6, 6], [6, 0, 3])
    yield "many-states", build([63, 94, 100], [60, 56, 11])
    yield "max-full", build([100, 100, 100], [100, 0, 100])
    yield "rand1", random_case(1, 20)
    yield "rand2", random_case(50, 100)
    yield "rand3", random_case(1, 100)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
