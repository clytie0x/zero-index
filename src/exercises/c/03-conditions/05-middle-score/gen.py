"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/05-middle-score/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/05-middle-score
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(305)


def cases():
    yield "sample1", "72 95 88"
    yield "sample2", "70 70 50"
    # คะแนนไม่ซ้ำ ครบทั้ง 6 แบบของการเรียง ให้คะแนนกลางอยู่ได้ทุกตำแหน่ง
    for i, order in enumerate(("30 60 90", "30 90 60", "60 30 90", "60 90 30", "90 30 60", "90 60 30"), 1):
        yield f"order{i}", order
    # มีคะแนนซ้ำสองค่า ทั้งซ้ำฝั่งมากและฝั่งน้อย ในทุกตำแหน่ง
    for i, order in enumerate(("80 80 40", "80 40 80", "40 80 80", "40 40 80", "40 80 40", "80 40 40"), 1):
        yield f"pair{i}", order
    yield "same", "65 65 65"
    yield "zeros", "0 0 0"
    yield "full", "100 100 100"
    yield "extremes", "100 0 50"
    for i in range(1, 3):
        yield f"rand{i}", " ".join(str(random.randint(0, 100)) for _ in range(3))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
