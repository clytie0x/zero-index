"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/07-library-codes   (รันที่รากของโปรเจกต์)

สุ่มคำสั่งโดยจำว่ามีรหัสไหนอยู่ในต้นไม้ ใส่เฉพาะรหัสที่ยังไม่มี และลบเฉพาะรหัสที่มีอยู่
มีชุดที่ลบรากซ้ำๆ ชุดที่ใส่รหัสเรียงกันจนต้นไม้เอียง และชุดที่ลบจนว่าง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2607)


def text(ops):
    return f"{len(ops)}\n" + "\n".join(ops)


def random_ops(q, top, erase_rate, ask_rate):
    present, ops = [], []
    for _ in range(q):
        r = random.random()
        if present and r < erase_rate:
            x = present.pop(random.randrange(len(present)))
            ops.append(f"- {x}")
        elif r < erase_rate + ask_rate:
            if present and random.random() < 0.7:
                x = random.choice(present)
            else:
                x = random.randint(1, top)
            ops.append(f"? {x}")
        else:
            x = random.randint(1, top)
            while x in present:
                x = random.randint(1, top)
            present.append(x)
            ops.append(f"+ {x}")
    return ops


class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


def insert(node, x):
    if node is None:
        return Node(x)
    if x < node.key:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node


def erase(node, x):
    """ลบตามกติกาในโจทย์ ใช้หาว่ารากตอนนี้คืออะไร"""
    if x < node.key:
        node.left = erase(node.left, x)
        return node
    if x > node.key:
        node.right = erase(node.right, x)
        return node
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left
    nxt = node.right
    while nxt.left is not None:
        nxt = nxt.left
    node.key = nxt.key
    node.right = erase(node.right, nxt.key)
    return node


def remove_roots(keys, times):
    """ใส่ keys ตามลำดับ แล้วลบรากซ้ำ times ครั้ง ปิดท้ายด้วยถามความลึกของทุกคีย์"""
    root = None
    ops = []
    for x in keys:
        root = insert(root, x)
        ops.append(f"+ {x}")
    for _ in range(times):
        ops.append(f"- {root.key}")
        root = erase(root, root.key)
    ops += [f"? {x}" for x in keys]
    return ops


def cases():
    yield "sample1", text(["+ 165", "+ 152", "+ 176", "+ 149", "+ 158", "+ 171", "+ 180",
                           "? 171", "? 160", "- 149", "- 152", "- 165", "? 171", "? 180"])
    yield "single", text(["+ 1000000000", "? 1000000000", "? 1"])
    yield "to-empty", text(["+ 5", "+ 3", "+ 8", "- 5", "- 3", "? 8", "- 8", "? 8"])
    yield "sorted", text([f"+ {x}" for x in range(1, 2501)] + [f"? {x}" for x in range(2500, 0, -100)])
    yield "remove-roots", text(remove_roots(random.sample(range(1, 1000), 40), 25))
    yield "one-child", text(["+ 50", "+ 30", "+ 20", "+ 25", "+ 70", "+ 80", "+ 90",
                             "- 30", "? 25", "- 70", "? 90", "- 50", "? 80"])
    yield "rand1", text(random_ops(20, 30, 0.25, 0.25))
    yield "rand2", text(random_ops(5000, 10**9, 0.2, 0.3))
    yield "rand3", text(random_ops(5000, 6000, 0.35, 0.2))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
