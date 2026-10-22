"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/01-recipe-steps   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนขั้น ตั้งใจให้วิธีไล่หาขั้นที่ทำได้ทีละรอบใน naive.cpp ไม่ทัน
big1 เป็นสายตรงที่ขั้นเลขมากต้องทำก่อน ทุกรอบต้องไล่เกือบถึงท้าย
big2 สุ่มเงื่อนไขจากเลขมากไปเลขน้อย big3 มีวงยาวแอบอยู่ท้ายสาย ต้องตอบ -1
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3001)


def build(n, rules):
    return f"{n} {len(rules)}\n" + "".join(f"{a} {b}\n" for a, b in rules)


def random_dag(n, m):
    """เงื่อนไขชี้จากขั้นที่อยู่ก่อนในลำดับลับไปขั้นที่อยู่หลัง จึงไม่มีวงแน่นอน"""
    secret = list(range(1, n + 1))
    random.shuffle(secret)
    rules = []
    for _ in range(m):
        i, j = sorted(random.sample(range(n), 2))
        rules.append((secret[i], secret[j]))
    return rules


def cases():
    yield "sample1", "5 4\n3 1\n3 2\n1 4\n5 4\n"
    yield "sample2", "3 3\n1 2\n2 3\n3 1\n"
    yield "single", build(1, [])
    yield "no-rules", build(6, [])
    # ขั้นเลขน้อยว่างทีหลัง ต้องเลือกใหม่ทุกครั้ง ไม่ใช่เรียงตามที่เข้าคิว
    yield "pick-smallest", build(6, [(6, 1), (5, 2), (4, 3), (6, 5)])
    yield "repeat-rule", build(4, [(2, 1), (2, 1), (2, 1), (3, 4)])
    yield "small-cycle", build(7, [(1, 2), (2, 3), (4, 5), (5, 6), (6, 4), (3, 7)])
    yield "rand1", build(30, random_dag(30, 40))
    yield "rand2", build(2000, random_dag(2000, 3000))
    rules = random_dag(1000, 1500)
    rules.append((rules[0][1], rules[0][0]))
    yield "rand-cycle", build(1000, rules)
    n = 200000
    yield "big1", build(n, [(v, v - 1) for v in range(n, 1, -1)])
    rules = []
    for _ in range(n):
        a, b = sorted(random.sample(range(1, n + 1), 2))
        rules.append((b, a))
    yield "big2", build(n, rules)
    rules = [(v, v - 1) for v in range(n, 1, -1)] + [(1, 50)]
    yield "big3", build(n, rules)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
