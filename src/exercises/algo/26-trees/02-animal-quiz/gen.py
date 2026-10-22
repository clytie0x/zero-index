"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/02-animal-quiz   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขโหนดแบบสุ่ม รากจึงไม่ใช่โหนด 1
มีชุดที่เอียงซ้ายล้วนและขวาล้วน ซึ่งทำให้ลำดับทั้งสามแบบต่างกันชัด
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2602)


def build(left, right):
    """left right เป็นลิสต์ที่ index 1 ถึง n สร้างกับรากที่ 1 แล้วสลับหมายเลข"""
    n = len(left) - 1
    label = [0] + random.sample(range(1, n + 1), n)
    new_left = [0] * (n + 1)
    new_right = [0] * (n + 1)
    for v in range(1, n + 1):
        new_left[label[v]] = label[left[v]]
        new_right[label[v]] = label[right[v]]
    return f"{n}\n" + "\n".join(f"{new_left[v]} {new_right[v]}" for v in range(1, n + 1))


def random_binary(n, lean):
    """แขวนโหนดใหม่ไว้ใต้โหนดที่ยังมีที่ว่าง lean ใกล้ 1 ทำให้เลือกโหนดล่าสุดบ่อย ต้นไม้จะลึก"""
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    free = [1]
    for v in range(2, n + 1):
        i = len(free) - 1 if random.random() < lean else random.randrange(len(free))
        p = free[i]
        sides = [s for s, arr in (("L", left), ("R", right)) if arr[p] == 0]
        side = random.choice(sides)
        if side == "L":
            left[p] = v
        else:
            right[p] = v
        if left[p] and right[p]:
            free.pop(i)
        free.append(v)
    return left, right


def chain(n, side):
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for v in range(1, n):
        (left if side == "L" else right)[v] = v + 1
    return left, right


def complete(n):
    left = [0] + [2 * v if 2 * v <= n else 0 for v in range(1, n + 1)]
    right = [0] + [2 * v + 1 if 2 * v + 1 <= n else 0 for v in range(1, n + 1)]
    return left, right


def cases():
    yield "sample1", "6\n0 4\n0 0\n1 6\n0 0\n0 0\n2 5"
    yield "single", "1\n0 0"
    yield "left-chain", build(*chain(1000, "L"))
    yield "right-chain", build(*chain(1000, "R"))
    yield "complete", build(*complete(1000))
    yield "rand1", build(*random_binary(12, 0.3))
    yield "rand2", build(*random_binary(1000, 0.3))
    yield "deep", build(*random_binary(1000, 0.95))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
