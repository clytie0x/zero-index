"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/05-arrays/02-star-students   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(502)


def line(values):
    return " ".join(map(str, values))


def cases():
    yield "sample1", "6\n70 85 90 65 80 58"
    yield "sample2", "3\n50 50 50"
    yield "single", "1\n0"
    yield "zeros", "5\n0 0 0 0 0"
    # ค่าเฉลี่ย 1.5 ถ้าหารแบบตัดเศษจะได้ 1 แล้วนับเกินมาหนึ่งคน
    yield "half", "2\n1 2"
    # ค่าเฉลี่ย 60.001 มีแค่คนได้ 61 คนเดียว ถ้าตัดเศษเหลือ 60 จะนับได้ทั้ง 1000 คน
    yield "just-above", f"1000\n{line([60] * 999 + [61])}"
    yield "full", "4\n100 100 100 99"
    for i, n in enumerate((40, 1000), 1):
        yield f"rand{i}", f"{n}\n{line(random.randint(0, 100) for _ in range(n))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
