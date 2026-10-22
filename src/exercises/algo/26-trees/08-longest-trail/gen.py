"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/08-longest-trail   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขจุดแบบสุ่ม naive.cpp หาระยะจากทุกจุด จึงมีไม่เกินสองพันจุดในชุดที่ไม่ใช่ big
ชุด fork และ big2 มีทางที่ยาวที่สุดไม่ผ่านศูนย์บริการ
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนจุด big1 เป็นเส้นตรงที่ทุกช่วงยาว 10^9 คำตอบจึงเกิน int มาก
big2 ศูนย์บริการต่อกับจุดเดียวแล้วแตกเป็นสองสายยาวสายละเกือบแสน big3 เป็นต้นไม้สุ่ม
ตั้งใจให้ naive.cpp ไม่ทัน และ recursion ที่ลึกเท่าทางเดินพัง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2608)


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


def fork(n):
    """ราก 1 มีลูกตัวเดียวคือ 2 แล้ว 2 แตกเป็นสองสายยาวเท่าๆ กัน"""
    parent = [0, 0, 1]
    half = (n - 2) // 2
    for v in range(3, n + 1):
        if v == 3 or v == 3 + half:
            parent.append(2)
        else:
            parent.append(v - 1)
    return parent


def trail(parent, low, high):
    lengths = [0, 0] + [random.randint(low, high) for _ in range(len(parent) - 2)]
    parent, lengths = relabel(parent, lengths)
    n = len(parent) - 1
    return f"{n}\n" + " ".join(map(str, parent[1:])) + "\n" + " ".join(map(str, lengths[1:]))


def cases():
    yield "sample1", "7\n0 1 1 2 2 3 6\n0 4 2 7 3 5 6"
    yield "single", "1\n0\n0"
    yield "two", trail(chain(2), 10**9, 10**9)
    yield "star", trail(star(2000), 1, 10**9)
    yield "fork", trail(fork(2000), 1, 1000)
    yield "chain", trail(chain(2000), 10**9, 10**9)
    yield "rand1", trail(random_tree(12, 12), 1, 9)
    yield "rand2", trail(random_tree(2000, 2000), 1, 10**9)
    yield "deep", trail(random_tree(2000, 3), 1, 10**6)
    n = 200000
    yield "big1", trail(chain(n), 10**9, 10**9)
    yield "big2", trail(fork(n), 1, 10**9)
    yield "big3", trail(random_tree(n, n), 1, 10**9)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
