"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/09-train-shunting   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big เริ่มด้วยขบวนแสนตู้และมีคำสั่งสองแสนคำสั่ง ตั้งใจให้ naive.c ที่หาตู้แล้วเลื่อนอาเรย์ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1409)
MAX_CAR = 300000


class Pool:
    """เซตของหมายเลขที่สุ่มหยิบและลบได้เร็ว ใช้จำว่าตู้ไหนอยู่ในขบวน ตู้ไหนว่าง"""

    def __init__(self, items):
        self.items = list(items)
        self.where = {v: i for i, v in enumerate(self.items)}

    def add(self, v):
        self.where[v] = len(self.items)
        self.items.append(v)

    def remove(self, v):
        i = self.where.pop(v)
        last = self.items.pop()
        if i < len(self.items):
            self.items[i] = last
            self.where[last] = i

    def pick(self):
        return random.choice(self.items)


def build(n, commands):
    return "\n".join([f"{n} {len(commands)}"] + commands)


def random_case(n, q, insert_rate, front_rate):
    present = Pool(range(1, n + 1))
    absent = Pool(range(n + 1, MAX_CAR + 1))
    commands = []
    for _ in range(q):
        if not present.items or random.random() < insert_rate:
            x = 0 if not present.items or random.random() < front_rate else present.pick()
            y = absent.pick()
            absent.remove(y)
            present.add(y)
            commands.append(f"I {x} {y}")
        else:
            x = present.pick()
            present.remove(x)
            absent.add(x)
            commands.append(f"D {x}")
    return build(n, commands)


def cases():
    yield "sample1", build(5, ["I 2 9", "D 1", "I 0 7", "D 5", "I 4 1"])
    yield "sample2", build(1, ["D 1", "I 0 300000"])
    yield "all-gone", build(3, ["D 2", "D 1", "D 3"])
    # ปลดหัวและท้ายสลับกัน แล้วต่อท้ายตู้สุดท้าย
    yield "ends", build(6, ["D 1", "D 6", "D 2", "D 5", "I 4 10", "I 10 11", "I 0 12"])
    # ปลดแล้วนำหมายเลขเดิมกลับมาต่อที่อื่น
    yield "reuse", build(4, ["D 3", "I 0 3", "D 1", "I 4 1", "D 3", "I 2 3"])
    yield "rand1", random_case(8, 15, 0.5, 0.2)
    yield "rand2", random_case(2000, 4000, 0.5, 0.1)
    yield "rand3", random_case(8000, 8000, 0.55, 0.05)
    yield "big1", random_case(100000, 200000, 0.5, 0.0)
    # พ่วงต่อท้ายตู้สุดท้ายทุกครั้ง ขบวนยาวขึ้นถึงสามแสนตู้ ถ้าเก็บในอาเรย์ต้องไล่หาตู้ x จนสุดขบวนทุกครั้ง
    n = 100000
    yield "big2", build(n, [f"I {n if i == 0 else n + i} {n + i + 1}" for i in range(200000)])
    # สลับกัน พ่วงตู้ใหม่หน้าสุด แล้วปลดตู้ท้ายสุด ถ้าเก็บในอาเรย์ต้องเลื่อนทั้งขบวนและไล่หาจนสุดขบวน
    commands = []
    for i in range(n):
        commands.append(f"I 0 {n + i + 1}")
        commands.append(f"D {n - i}")
    yield "big3", build(n, commands)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
