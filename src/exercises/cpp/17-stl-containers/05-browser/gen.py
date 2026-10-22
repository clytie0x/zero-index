"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/05-browser   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี Q เป็นสองแสน ใหญ่เกินกว่าจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1705)

SITES = ["news", "sport", "weather", "mail", "video", "shop", "map", "school", "game", "music"]


def page():
    return f"{random.choice(SITES)}.{random.randint(1, 99)}"


def case(commands):
    return f"{len(commands)}\n" + "\n".join(commands)


def random_commands(q, weights):
    commands = []
    kinds = ["VISIT", "BACK", "FORWARD"]
    for _ in range(q):
        kind = random.choices(kinds, weights)[0]
        commands.append(f"VISIT {page()}" if kind == "VISIT" else kind)
    return commands


def cases():
    yield "sample1", case(["VISIT news", "VISIT sport", "VISIT football", "BACK", "BACK", "FORWARD", "VISIT tennis",
                           "FORWARD", "BACK", "BACK", "BACK", "BACK"])
    # กดปุ่มตอนยังไม่มีประวัติ
    yield "nothing-yet", case(["BACK", "FORWARD", "BACK", "VISIT a", "FORWARD", "BACK", "BACK", "FORWARD",
                               "FORWARD"])
    # VISIT หลัง BACK ต้องล้าง forward ทั้งหมด
    yield "forward-cleared", case(["VISIT a", "VISIT b", "VISIT c", "VISIT d", "BACK", "BACK", "BACK", "VISIT x",
                                   "FORWARD", "FORWARD", "BACK", "FORWARD", "BACK", "BACK", "BACK"])
    # เปิดหน้าเดิมซ้ำนับเป็นหน้าใหม่
    yield "same-page", case(["VISIT home", "VISIT home", "VISIT mail", "BACK", "BACK", "BACK", "BACK",
                             "FORWARD", "FORWARD", "FORWARD", "FORWARD"])
    yield "single", case(["FORWARD"])
    yield "rand1", case(random_commands(300, [3, 3, 2]))
    yield "rand2", case(random_commands(5000, [2, 3, 3]))
    yield "rand3", case(random_commands(5000, [5, 2, 1]))
    yield "big1", case(random_commands(200000, [3, 3, 2]))
    # สร้างประวัติยาวแสนหน้า ถอยกลับจนสุด แล้วเปิดหน้าใหม่ซึ่งต้องล้าง forward แสนหน้าทีเดียว
    yield "big2", case([f"VISIT {page()}" for _ in range(100000)] + ["BACK"] * 99990 + ["VISIT end", "FORWARD"]
                       + ["BACK"] * 8)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
