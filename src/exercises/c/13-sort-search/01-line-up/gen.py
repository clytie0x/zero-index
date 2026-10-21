"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/01-line-up   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1301)


def line(values):
    return " ".join(map(str, values))


def cases():
    yield "sample1", "6\n152 148 160 155 149 171"
    yield "sample2", "5\n160 155 160 148 155"
    yield "single", "1\n137"
    yield "all-same", f"8\n{line([150] * 8)}"
    yield "sorted", f"10\n{line(range(150, 160))}"
    # เรียงกลับด้าน และมีค่าขอบ 100 กับ 200
    descending = [200] + list(range(190, 180, -1)) + [100]
    yield "reversed", f"{len(descending)}\n{line(descending)}"
    yield "rand1", f"50\n{line(random.randint(140, 180) for _ in range(50))}"
    yield "rand2", f"300\n{line(random.randint(100, 200) for _ in range(300))}"
    yield "max", f"1000\n{line(random.randint(100, 200) for _ in range(1000))}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
