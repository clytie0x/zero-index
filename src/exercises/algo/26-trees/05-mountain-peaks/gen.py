"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/05-mountain-peaks   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขจุดแบบสุ่ม
naive.cpp เดินย้อนขึ้นไปจนเจอจุดที่สูงกว่าหรือเท่ากัน จะช้าเมื่อทางยาวและความสูงเพิ่มขึ้นเรื่อยๆ ตามทาง
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนจุด big1 เป็นเส้นตรงที่สูงขึ้นทุกจุด big2 เป็นด้ามยาวแสนห้าหมื่นจุดที่สูงขึ้นเรื่อยๆ
แล้วปลายด้ามแตกเป็นจุดที่สูงกว่าทุกจุดบนด้าม big3 เป็นเส้นตรงที่สูงขึ้นแต่มีจุดต่ำแทรก
ตั้งใจให้ naive.cpp ไม่ทัน และ recursion ที่ลึกเท่าทางเดินพัง big4 เป็นต้นไม้สุ่มที่ไม่ลึก มีไว้เพราะไฟล์ใหญ่
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2605)


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


def text(parent, heights):
    n = len(parent) - 1
    return f"{n}\n" + " ".join(map(str, parent[1:])) + "\n" + " ".join(map(str, heights[1:]))


def depth_of(parent):
    """ต้นไม้ที่รากคือ 1 และพ่อมีหมายเลขน้อยกว่าลูก"""
    depth = [0] * len(parent)
    for v in range(2, len(parent)):
        depth[v] = depth[parent[v]] + 1
    return depth


def park(parent, heights):
    return text(*relabel(parent, heights))


def rising(parent, noise):
    """ความสูงเพิ่มตามความลึก บวกเลขสุ่มไม่เกิน noise ทำให้บางจุดไม่สูงกว่าจุดก่อนหน้า"""
    depth = depth_of(parent)
    return [0] + [1000 * depth[v] + random.randint(1, noise) for v in range(1, len(parent))]


def cases():
    yield "sample1", "7\n0 1 1 2 2 3 6\n50 70 40 60 90 45 80"
    yield "single", "1\n0\n7"
    yield "same-height", park(random_tree(300, 300), [0] + [500] * 300)
    yield "falling", park(chain(2000), [0] + [10**9 - v for v in range(1, 2001)])
    yield "rising", park(chain(2000), [0] + [v for v in range(1, 2001)])
    yield "star", park(star(1000), [0, 500] + [random.randint(1, 1000) for _ in range(999)])
    yield "rand1", park(random_tree(15, 15), [0] + [random.randint(1, 20) for _ in range(15)])
    tree = random_tree(2000, 5)
    yield "rand2", park(tree, rising(tree, 3000))
    n = 200000
    yield "big1", park(chain(n), [0] + [v * 5000 for v in range(1, n + 1)])
    handle = 150000
    yield "big2", park(broom(n, handle), [0] + [v if v <= handle else 10**9 - v for v in range(1, n + 1)])
    yield "big3", park(chain(n), rising(chain(n), 1500))
    yield "big4", park(random_tree(n, n), [0] + [random.randint(1, 10**9) for _ in range(n)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
