"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/04-team-sales   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขพนักงานแบบสุ่ม หัวหน้าจึงไม่ได้มีหมายเลขน้อยกว่าลูกทีมเสมอ
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนคน big1 เป็นสายตรงทั้งต้นที่ทุกคนขายได้ 10^9 ยอดของผู้จัดการใหญ่จึงเป็น 2 × 10^14
big2 เป็นด้ามยาวแสนห้าหมื่นคน ตั้งใจให้วิธีบวกขึ้นไปทุกชั้นใน naive.cpp ไม่ทัน และ recursion ที่ลึกเท่าสายบังคับบัญชาพัง
big3 เป็นต้นไม้สุ่มที่ไม่ลึก มีไว้เพราะไฟล์ใหญ่เกินจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2604)


def relabel(parent, extra=None):
    """parent[v] คือพ่อของโหนด v (index 1 ถึง n) ในต้นไม้ที่รากคือ 1
    สลับหมายเลขโหนดแบบสุ่ม คืนลิสต์พ่อใหม่ และลิสต์ extra ที่ย้ายตามหมายเลขใหม่"""
    n = len(parent) - 1
    label = [0] + random.sample(range(1, n + 1), n)
    new_parent = [0] * (n + 1)
    new_extra = [0] * (n + 1)
    for v in range(1, n + 1):
        new_parent[label[v]] = label[parent[v]] if parent[v] else 0
        if extra is not None:
            new_extra[label[v]] = extra[v]
    return new_parent, new_extra


def chain(n):
    return [0, 0] + [v - 1 for v in range(2, n + 1)]


def star(n):
    return [0, 0] + [1] * (n - 1)


def broom(n, handle):
    """ด้ามยาว handle โหนดเป็นเส้นตรง ที่เหลือเป็นใบที่ปลายด้าม"""
    return [0, 0] + [v - 1 if v <= handle else handle for v in range(2, n + 1)]


def random_tree(n, spread):
    """พ่อของโหนด v สุ่มจาก spread โหนดก่อนหน้า spread น้อยทำให้ต้นไม้ลึก"""
    return [0, 0] + [random.randint(max(1, v - spread), v - 1) for v in range(2, n + 1)]


def text(parent, sales):
    n = len(parent) - 1
    return f"{n}\n" + " ".join(map(str, parent[1:])) + "\n" + " ".join(map(str, sales[1:]))


def company(parent, low, high):
    sales = [0] + [random.randint(low, high) for _ in range(len(parent) - 1)]
    return text(*relabel(parent, sales))


def cases():
    yield "sample1", "6\n0 1 1 2 2 3\n50 20 30 10 5 7"
    yield "single", "1\n0\n1000000000"
    yield "zero-sales", company(random_tree(50, 50), 0, 0)
    yield "star", company(star(1000), 0, 10**9)
    yield "chain-max", company(chain(2000), 10**9, 10**9)
    yield "broom", company(broom(2000, 1000), 1, 100)
    yield "rand1", company(random_tree(15, 15), 0, 50)
    yield "rand2", company(random_tree(2000, 2000), 0, 10**9)
    n = 200000
    yield "big1", company(chain(n), 10**9, 10**9)
    yield "big2", company(broom(n, 150000), 0, 10**9)
    yield "big3", company(random_tree(n, n), 0, 10**9)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
