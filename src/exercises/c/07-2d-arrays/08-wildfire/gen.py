"""สร้างไฟล์ .in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/07-2d-arrays/08-wildfire

ขั้นแรกเขียนเฉพาะ tests/*.in ขั้นที่สองรันเฉลยเพื่อเขียน .out
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(708)


def make(rows, minutes):
    return f"{len(rows)} {len(rows[0])} {minutes}\n" + "\n".join(rows)


def rand_forest(r, c, tree, fires):
    g = [["#" if random.random() < tree else "." for _ in range(c)] for _ in range(r)]
    for _ in range(fires):
        g[random.randrange(r)][random.randrange(c)] = "*"
    return ["".join(row) for row in g]


def cases():
    yield "sample1", make(["#####", "##*##", "#.###", "#.#.#"], 2)
    yield "no-fire", make(["#.#", "###"], 5)
    yield "one-burning", make(["*"], 1)
    yield "one-tree", make(["#"], 3)
    # ไฟอยู่ซ้ายสุดของแถวต้นไม้ ถ้าเขียนทับตารางเดิม ไฟจะลามทั้งแถวในนาทีเดียว
    yield "one-row", make(["*##########"], 3)
    yield "firebreak", make(["##.##", "#*.##", "##.##"], 10)
    yield "corner-fire", make(["*" + "#" * 99] + ["#" * 100 for _ in range(99)], 100)
    yield "burn-out", make(["#" * 20] * 4 + ["#########*##########"] + ["#" * 20] * 5, 100)
    yield "max", make(rand_forest(100, 100, 0.7, 5), 37)
    for i in range(1, 3):
        r, c = random.randint(10, 50), random.randint(10, 50)
        yield f"rand{i}", make(rand_forest(r, c, 0.6, 3), random.randint(1, 30))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
