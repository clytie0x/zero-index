"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/03-generations   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขคนแบบสุ่ม พ่อจึงไม่ได้มีหมายเลขน้อยกว่าลูกเสมอ
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนคน big1 เป็นสายตรงทั้งต้น big2 เป็นด้ามยาวแสนห้าหมื่นรุ่น
ตั้งใจให้วิธีเดินขึ้นจากทุกคนใน naive.cpp ไม่ทัน และ recursion ที่ลึกเท่าจำนวนรุ่นพัง
big3 เป็นต้นไม้สุ่มที่ไม่ลึก มีไว้เพราะไฟล์ใหญ่เกินจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2603)


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


def text(parent):
    return f"{len(parent) - 1}\n" + " ".join(map(str, parent[1:]))


def cases():
    yield "sample1", "9\n0 1 1 2 2 3 1 5 7"
    yield "single", "1\n0"
    yield "star", text(relabel(star(500))[0])
    yield "chain", text(relabel(chain(2000))[0])
    yield "broom", text(relabel(broom(2000, 1500))[0])
    yield "rand1", text(relabel(random_tree(20, 20))[0])
    yield "rand2", text(relabel(random_tree(2000, 2000))[0])
    yield "deep", text(relabel(random_tree(2000, 2))[0])
    n = 200000
    yield "big1", text(relabel(chain(n))[0])
    yield "big2", text(relabel(broom(n, 150000))[0])
    yield "big3", text(relabel(random_tree(n, n))[0])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
