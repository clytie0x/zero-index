"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/05-project-plan   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนงาน
big1 เป็นสายตรงยาวทั้งโครงการ เงื่อนไขเขียนจากท้ายสายย้อนมาต้นสาย
วิธีวนปรับค่าจนนิ่งใน naive.cpp ส่งค่าได้แค่หนึ่งงานต่อรอบ จึงต้องวนสองแสนรอบ
big2 สุ่มเงื่อนไขหนาแน่นสองแสนข้อ ค่าวันใหญ่จนคำตอบเกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3005)

TOP = 10**9


def build(days, rules):
    rows = [f"{len(days)} {len(rules)}", " ".join(map(str, days))]
    rows += [f"{a} {b}" for a, b in rules]
    return "\n".join(rows) + "\n"


def random_dag(n, m):
    secret = list(range(1, n + 1))
    random.shuffle(secret)
    rules = []
    for _ in range(m):
        i, j = sorted(random.sample(range(n), 2))
        rules.append((secret[i], secret[j]))
    return rules


def cases():
    yield "sample1", build([3, 2, 4, 1, 5, 2], [(1, 2), (1, 3), (2, 4), (3, 4), (5, 6)])
    yield "single", build([7], [])
    yield "no-rules", build([4, 9, 2, 9, 1], [])
    # เส้นทางที่มีงานมากกว่าไม่ได้ยาวกว่าเสมอ
    yield "few-long", build([1, 1, 1, 1, 10, 1], [(1, 2), (2, 3), (3, 4), (5, 6)])
    yield "diamond", build([2, 5, 1, 3], [(1, 2), (1, 3), (2, 4), (3, 4), (1, 4)])
    yield "repeat-rule", build([1, 2, 3], [(1, 2), (1, 2), (2, 3), (2, 3)])
    yield "over-int", build([TOP] * 5, [(1, 2), (2, 3), (3, 4), (4, 5)])
    yield "rand1", build([random.randint(1, 9) for _ in range(12)], random_dag(12, 15))
    n = 2000
    yield "rand2", build([random.randint(1, TOP) for _ in range(n)], random_dag(n, 4000))
    chain = [(v, v + 1) for v in range(1, 300)]
    yield "rand-chain", build([random.randint(1, 100) for _ in range(300)], chain[::-1])
    n = 200000
    yield "big1", build([random.randint(1, TOP) for _ in range(n)], [(v, v + 1) for v in range(n - 1, 0, -1)])
    yield "big2", build([random.randint(1, TOP) for _ in range(n)], random_dag(n, n))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
