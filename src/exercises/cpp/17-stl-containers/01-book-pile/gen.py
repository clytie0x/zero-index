"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/01-book-pile   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี Q เป็นแสน ใหญ่เกินกว่าจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1701)

WORDS = ["math", "thai", "physics", "atlas", "comic", "novel", "chem", "bio", "history", "poem",
         "english", "art", "music", "code", "map", "cook", "sport", "game", "space", "sea"]


def title():
    if random.random() < 0.5:
        return random.choice(WORDS)
    return f"{random.choice(WORDS)}-{random.randint(1, 999)}"


def case(commands):
    return f"{len(commands)}\n" + "\n".join(commands)


def random_commands(q, shelve_max):
    commands = []
    for _ in range(q):
        r = random.random()
        if r < 0.6:
            commands.append(f"RETURN {title()}")
        elif r < 0.8:
            commands.append(f"SHELVE {random.randint(1, shelve_max)}")
        else:
            commands.append("TOP")
    return commands


def cases():
    yield "sample1", case(["RETURN math-1", "RETURN thai-novel", "TOP", "RETURN physics", "SHELVE 2",
                           "RETURN atlas", "SHELVE 5", "TOP", "SHELVE 1", "RETURN comic"])
    # คำสั่งแรกๆ เจอตะกร้าว่าง
    yield "empty-start", case(["TOP", "SHELVE 3", "RETURN poem", "SHELVE 1", "SHELVE 1", "TOP"])
    # หยิบพอดีกับที่มี แล้วหยิบเกิน
    yield "exact-k", case(["RETURN a", "RETURN b", "RETURN c", "SHELVE 3", "RETURN d", "RETURN e",
                           "SHELVE 100000", "TOP"])
    # ชื่อซ้ำกันได้
    yield "duplicates", case(["RETURN map", "RETURN map", "RETURN map-2", "RETURN map", "TOP", "SHELVE 2",
                              "TOP", "SHELVE 1", "TOP"])
    yield "single", case(["RETURN zz-999-abcdefghijklm"])
    yield "rand1", case(random_commands(200, 4))
    yield "rand2", case(random_commands(2000, 10))
    # บรรทัดยาวสองพันชื่อ จับช่องว่างเกินท้ายบรรทัด
    yield "shelve-long", case([f"RETURN {title()}" for _ in range(2000)] + ["SHELVE 5000", "TOP"])
    yield "big1", case(random_commands(100000, 30))
    yield "big2", case([f"RETURN {title()}" for _ in range(99997)] + ["SHELVE 100000", "SHELVE 1", "TOP"])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
