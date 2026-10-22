"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/01-club-leaves   (รันที่รากของโปรเจกต์)

ต้นไม้ทุกชุดสลับหมายเลขสมาชิกแบบสุ่ม ประธานจึงไม่ใช่คนหมายเลข 1 ยกเว้นชุดตัวอย่าง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2601)


def relabel(parent):
    """parent[i] คือพ่อของโหนด i (เริ่มที่ 1) ในต้นไม้ที่รากคือ 1 สลับหมายเลขแล้วคืนเป็นข้อความข้อมูลเข้า"""
    n = len(parent) - 1
    label = list(range(1, n + 1))
    random.shuffle(label)
    out = [0] * (n + 1)
    for v in range(1, n + 1):
        out[label[v - 1]] = 0 if parent[v] == 0 else label[parent[v] - 1]
    return f"{n}\n" + " ".join(map(str, out[1:]))


def chain(n):
    return [0, 0] + [v - 1 for v in range(2, n + 1)]


def star(n):
    return [0, 0] + [1] * (n - 1)


def random_tree(n, spread):
    """พ่อของโหนด v สุ่มจาก spread โหนดก่อนหน้า spread น้อยทำให้ต้นไม้ลึก"""
    return [0, 0] + [random.randint(max(1, v - spread), v - 1) for v in range(2, n + 1)]


def cases():
    yield "sample1", "9\n0 1 1 2 2 3 1 5 7"
    yield "sample2", "5\n2 0 2 3 3"
    yield "alone", "1\n0"
    yield "pair", "2\n2 0"
    yield "chain", relabel(chain(1000))
    yield "star", relabel(star(1000))
    yield "rand1", relabel(random_tree(30, 30))
    yield "rand2", relabel(random_tree(1000, 1000))
    yield "deep", relabel(random_tree(1000, 3))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
