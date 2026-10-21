"""สร้างไฟล์ .in ของข้อนี้ จากนั้นสร้าง .out ด้วยเฉลย

    python gen.py
    python tools/make_outputs.py src/exercises/c/04-loops/02-class-average
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(402)


def is_tie(scores):
    """ค่าเฉลี่ยตกตรงกึ่งกลางของทศนิยมตำแหน่งที่ 2 พอดี เช่น 62.125 ปัดได้สองทาง ไม่ใช้ชุดแบบนี้"""
    total, n = sum(scores), len(scores)
    return (total * 200) % n == 0 and (total * 200 // n) % 2 == 1


def text(scores):
    assert not is_tie(scores)
    return f"{len(scores)}\n{' '.join(map(str, scores))}"


def random_scores(n, low=0, high=100):
    while True:
        scores = [random.randint(low, high) for _ in range(n)]
        if not is_tie(scores):
            return scores


def cases():
    yield "sample1", text([55, 70, 49, 81])
    yield "sample2", text([70, 85, 90])
    yield "one-pass", text([50])
    yield "one-fail", text([49])
    yield "all-zero", text([0] * 5)
    yield "all-full", text([100] * 1000)
    yield "edge", text([49, 50, 49, 50, 51, 48, 50])
    yield "max", text(random_scores(1000))
    for i in range(1, 3):
        yield f"rand{i}", text(random_scores(random.randint(2, 50), 30, 70))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
