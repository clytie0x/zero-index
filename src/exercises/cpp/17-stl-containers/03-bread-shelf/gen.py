"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/03-bread-shelf   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี Q เป็นสองแสน ใหญ่เกินกว่าจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1703)


def case(commands):
    return f"{len(commands)}\n" + "\n".join(commands)


def random_commands(q, check_max):
    commands = []
    size = 0
    for _ in range(q):
        r = random.random()
        if r < 0.35:
            commands.append(f"BAKE {random.randint(1, 10**9)}")
            size += 1
        elif r < 0.5:
            commands.append(f"FOUND {random.randint(1, 10**9)}")
            size += 1
        elif r < 0.62:
            commands.append("FRESH")
            size = max(size - 1, 0)
        elif r < 0.74:
            commands.append("SALE")
            size = max(size - 1, 0)
        else:
            # ส่วนใหญ่ถามชิ้นที่มีอยู่จริง บางครั้งถามเกิน
            if size > 0 and random.random() < 0.85:
                commands.append(f"CHECK {random.randint(1, size)}")
            else:
                commands.append(f"CHECK {random.randint(1, check_max)}")
    return commands


def cases():
    yield "sample1", case(["BAKE 101", "BAKE 102", "FOUND 95", "CHECK 1", "CHECK 3", "CHECK 4", "FRESH", "SALE",
                           "BAKE 103", "CHECK 2", "SALE"])
    yield "empty-ops", case(["FRESH", "SALE", "CHECK 1", "BAKE 7", "SALE", "FRESH", "CHECK 1"])
    # i ใหญ่ถึงพันล้าน และถามชิ้นสุดท้ายพอดี
    yield "check-limits", case(["BAKE 1000000000", "BAKE 2", "BAKE 3", "CHECK 1000000000", "CHECK 3", "CHECK 4",
                                "CHECK 1"])
    # FOUND อย่างเดียว ชิ้นขวาสุดคือชิ้นที่เจอเป็นชิ้นแรก
    yield "found-only", case(["FOUND 5", "FOUND 4", "FOUND 3", "FOUND 2", "CHECK 1", "FRESH", "SALE", "CHECK 2"])
    yield "single", case(["CHECK 1"])
    yield "rand1", case(random_commands(200, 50))
    yield "rand2", case(random_commands(4000, 10**9))
    yield "big1", case(random_commands(200000, 10**9))
    bakes = [f"BAKE {random.randint(1, 10**9)}" for _ in range(100000)]
    tail = []
    size = 100000
    for _ in range(100000):
        if random.random() < 0.5:
            tail.append("SALE")
            size -= 1
        else:
            tail.append(f"CHECK {random.randint(1, max(size, 1))}")
    yield "big2", case(bakes + tail)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
